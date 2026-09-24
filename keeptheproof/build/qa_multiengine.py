#!/usr/bin/env python3
"""Multi-engine page QA (RC4).

Renders every page through several independent engines and, for each page,
compares not only the whole-page average difference but the TOP EDGE and the
CONTENT BOUNDING BOX across engines. A top-of-page clip or vertical shift moves
the content bounding box while barely moving the whole-page average, so the
RC3 harness (whole-page mean diff with a coarse threshold, plus pdftoppm
-singlefile "isolation" that still parses the whole document) could not catch
it. This harness adds:

  * TRUE single-page isolation via `pdfseparate` (a genuinely separated
    one-page PDF is rendered on its own, not a -f/-l window into the full doc);
  * explicit top-edge and content-bbox checks per page across engines;
  * Ghostscript with annotation printing forced on (`-dPrinted`), so the
    AcroForm widget appearance layer is actually rasterised;
  * PDFium (pypdfium2, the Chromium engine) when available;
  * a record of every engine version used.

Usage: qa_multiengine.py <pdf> <outdir>
Exit status is nonzero if any page is blank or any engine diverges in
whole-page mean, top edge, or content bounding box.
"""
import sys, os, subprocess, shutil
import fitz
from PIL import Image
import numpy as np

PDF, OUTD = sys.argv[1], sys.argv[2]
os.makedirs(OUTD, exist_ok=True)
DPI = 150
INK_THRESH = 220          # grayscale < this counts as ink
TOP_TOL = 3               # px; allowed top-edge spread across engines (AA floor)
BBOX_TOL = 3              # px; allowed bbox-edge spread across engines
MEAN_TOL = 8.0            # whole-page mean abs diff engine divergence
BLANK_INK = 0.4           # %; below this a page is blank-suspect

try:
    import pypdfium2 as pdfium
    HAVE_PDFIUM = True
except Exception:
    HAVE_PDFIUM = False

def engine_versions():
    v = {}
    v["PyMuPDF"] = fitz.VersionBind
    try:
        out = subprocess.run(["pdftoppm", "-v"], capture_output=True, text=True)
        v["Poppler(pdftoppm)"] = (out.stderr or out.stdout).strip().splitlines()[0]
    except Exception as e:
        v["Poppler(pdftoppm)"] = f"n/a ({e})"
    try:
        out = subprocess.run(["pdfseparate", "-v"], capture_output=True, text=True)
        v["Poppler(pdfseparate)"] = (out.stderr or out.stdout).strip().splitlines()[0]
    except Exception as e:
        v["Poppler(pdfseparate)"] = f"n/a ({e})"
    try:
        out = subprocess.run(["gs", "--version"], capture_output=True, text=True)
        v["Ghostscript"] = out.stdout.strip()
    except Exception as e:
        v["Ghostscript"] = f"n/a ({e})"
    v["PDFium"] = (str(getattr(pdfium, "PDFIUM_INFO", getattr(pdfium, "V_LIBPDFIUM", "?")))
                   if HAVE_PDFIUM else "not installed")
    return v

def render_all():
    """Produce, for every page, a dict engine->png path."""
    d = fitz.open(PDF); N = d.page_count
    # PyMuPDF
    for i in range(N):
        fitz.open(PDF)[i].get_pixmap(dpi=DPI).save(f"{OUTD}/pymupdf-{i+1:03d}.png")
    # Poppler whole-document
    subprocess.run(["pdftoppm", "-r", str(DPI), "-png", PDF, f"{OUTD}/popwhole"],
                   check=True, capture_output=True)
    # Poppler TRUE isolation: pdfseparate each page to its own PDF, render that
    sepdir = f"{OUTD}/sep"; os.makedirs(sepdir, exist_ok=True)
    subprocess.run(["pdfseparate", PDF, f"{sepdir}/pg-%d.pdf"], check=True, capture_output=True)
    for i in range(N):
        subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-singlefile",
                        f"{sepdir}/pg-{i+1}.pdf", f"{OUTD}/popiso-{i+1:03d}"],
                       check=True, capture_output=True)
    # Ghostscript whole-document, annotations/printing forced on
    subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=png16m", f"-r{DPI}",
                    "-dPrinted", f"-sOutputFile={OUTD}/gs-%03d.png", PDF],
                   check=True, capture_output=True)
    # PDFium whole-document (with forms initialised)
    if HAVE_PDFIUM:
        pdf = pdfium.PdfDocument(PDF)
        try: pdf.init_forms()
        except Exception: pass
        scale = DPI / 72.0
        for i in range(N):
            pdf[i].render(scale=scale).to_pil().convert("RGB").save(f"{OUTD}/pdfium-{i+1:03d}.png")
    return N

def gray(f):
    return np.asarray(Image.open(f).convert("L")).astype(int)

def ink_pct(a):
    return round(100 * float((a < INK_THRESH).mean()), 3)

def geom(a):
    """Return (top, bottom, left, right) of the ink bounding box, or None."""
    ink = a < INK_THRESH
    rows = np.where(ink.any(axis=1))[0]
    cols = np.where(ink.any(axis=0))[0]
    if len(rows) == 0:
        return None
    return int(rows[0]), int(rows[-1]), int(cols[0]), int(cols[-1])

def norm(f, w, h):
    return np.asarray(Image.open(f).convert("L").resize((w, h))).astype(int)

def main():
    versions = engine_versions()
    print(f"== {os.path.basename(PDF)} : multi-engine QA ==")
    for k, v in versions.items():
        print(f"   {k}: {v}")
    N = render_all()
    print(f"   pages: {N}\n")

    engines = ["pymupdf", "popwhole", "popiso", "gs"] + (["pdfium"] if HAVE_PDFIUM else [])
    def path(e, n):
        if e == "popwhole":
            p2 = f"{OUTD}/popwhole-{n:02d}.png"
            return p2 if os.path.exists(p2) else f"{OUTD}/popwhole-{n:03d}.png"
        return f"{OUTD}/{e}-{n:03d}.png"

    print("pg | ink% (pymu/popW/popISO/gs" + ("/pdfium" if HAVE_PDFIUM else "") + ")"
          " | top-edge spread | bbox spread | mean-diff(max) | flags")
    blanks = []; diverge = []; topclip = []; bboxshift = []
    for i in range(N):
        n = i + 1
        arrs = {e: gray(path(e, n)) for e in engines}
        inks = {e: ink_pct(a) for e, a in arrs.items()}
        geos = {e: geom(a) for e, a in arrs.items()}
        # normalise top-edge/bbox to page height/width fractions so differing
        # engine raster sizes are comparable
        tops = []; boxes = []
        for e, a in arrs.items():
            g = geos[e]
            if g is None:
                continue
            h, w = a.shape
            tops.append(g[0] / h)
            boxes.append((g[0] / h, g[1] / h, g[2] / w, g[3] / w))
        flags = []
        if min(inks.values()) < BLANK_INK:
            flags.append("BLANK?"); blanks.append(n)
        # top-edge spread in px at DPI (fraction * nominal 11in*DPI)
        pageH_px = 11.0 * DPI
        pageW_px = 8.5 * DPI
        top_spread = (max(tops) - min(tops)) * pageH_px if tops else 0.0
        if top_spread > TOP_TOL:
            flags.append("TOP-EDGE!"); topclip.append(n)
        # bbox spread: max per-edge spread in px
        if boxes:
            t = [b[0] for b in boxes]; bo = [b[1] for b in boxes]
            l = [b[2] for b in boxes]; r = [b[3] for b in boxes]
            bbox_spread = max((max(t)-min(t))*pageH_px, (max(bo)-min(bo))*pageH_px,
                              (max(l)-min(l))*pageW_px, (max(r)-min(r))*pageW_px)
        else:
            bbox_spread = 0.0
        if bbox_spread > BBOX_TOL:
            flags.append("BBOX-SHIFT!"); bboxshift.append(n)
        # whole-page mean diff vs PyMuPDF reference
        H = min(a.shape[0] for a in arrs.values())
        W = min(a.shape[1] for a in arrs.values())
        ref = norm(path("pymupdf", n), W, H)
        maxmean = 0.0
        for e in engines:
            if e == "pymupdf":
                continue
            m = float(np.abs(ref - norm(path(e, n), W, H)).mean())
            maxmean = max(maxmean, m)
        if maxmean > MEAN_TOL:
            flags.append("ENGINE-DIVERGE"); diverge.append(n)
        inkstr = "/".join(f"{inks[e]:.2f}" for e in engines)
        print(f"{n:3d} | {inkstr} | {top_spread:5.1f}px | {bbox_spread:5.1f}px | "
              f"{maxmean:5.2f} | {' '.join(flags)}")

    print(f"\nblank-suspect pages: {blanks or 'none'}")
    print(f"top-edge divergent pages: {topclip or 'none'}")
    print(f"bbox-shift pages: {bboxshift or 'none'}")
    print(f"engine-divergent pages: {sorted(set(diverge)) or 'none'}")
    bad = bool(blanks or diverge or topclip or bboxshift)
    print("RESULT:", "FAIL" if bad else "PASS")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
