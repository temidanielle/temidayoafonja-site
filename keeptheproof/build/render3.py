#!/usr/bin/env python3
"""Render pages of a PDF through PyMuPDF, Poppler (pdftoppm), and Ghostscript.
Usage: python3 render3.py <pdf> <outdir> <page[,page...]|all>
Produces <outdir>/<engine>_p<NN>.png. Also renders Poppler whole-doc vs isolated.
Reports per-page rendered pixel stats so blank/near-blank pages are flagged."""
import sys, os, subprocess, fitz

PDF, OUTD, pagespec = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUTD, exist_ok=True)
d = fitz.open(PDF); N = d.page_count
pages = list(range(1, N+1)) if pagespec == "all" else [int(x) for x in pagespec.split(",")]
DPI = 120

def stats(png):
    p = fitz.open(png)[0] if png.endswith(".pdf") else None
    pix = fitz.Pixmap(png)
    # fraction of non-background pixels (background ~ cream/navy solid); use stdev proxy
    import statistics
    n = pix.width*pix.height
    # sample: count distinct-ish by summing; cheap ink proxy = pixels far from the modal corner color
    data = pix.samples
    # modal bg = top-left pixel
    bg = data[0:pix.n]
    step = max(1, (len(data)//pix.n)//4000)
    diff = 0; tot = 0
    for i in range(0, len(data)-pix.n, pix.n*step):
        tot += 1
        px = data[i:i+pix.n]
        if sum(abs(px[j]-bg[j]) for j in range(pix.n)) > 40:
            diff += 1
    return round(100*diff/max(tot,1), 2)

# PyMuPDF
for pg in pages:
    out = f"{OUTD}/pymupdf_p{pg:02d}.png"
    fitz.open(PDF)[pg-1].get_pixmap(dpi=DPI).save(out)

# Poppler whole-doc (single command over all pages, then pick cited ones)
subprocess.run(["pdftoppm","-r",str(DPI),"-png",PDF,f"{OUTD}/popplerall"],
               check=True, capture_output=True)
# rename cited pages
for pg in pages:
    src = f"{OUTD}/popplerall-{pg:02d}.png"
    if not os.path.exists(src): src = f"{OUTD}/popplerall-{pg}.png"
    if os.path.exists(src):
        os.replace(src, f"{OUTD}/poppler_whole_p{pg:02d}.png")

# Poppler isolated (one page at a time)
for pg in pages:
    subprocess.run(["pdftoppm","-r",str(DPI),"-png","-f",str(pg),"-l",str(pg),
                    "-singlefile",PDF,f"{OUTD}/poppler_iso_p{pg:02d}"],
                   check=True, capture_output=True)

# Ghostscript whole-doc
subprocess.run(["gs","-q","-dNOPAUSE","-dBATCH","-sDEVICE=png16m",f"-r{DPI}",
                f"-sOutputFile={OUTD}/gs_p%02d.png", PDF], check=True, capture_output=True)

# report ink coverage per engine per page
print(f"page | pymupdf | poppler_whole | poppler_iso | ghostscript")
for pg in pages:
    row = [f"{pg:4d}"]
    for tag in ["pymupdf", "poppler_whole", "poppler_iso", "gs"]:
        f = f"{OUTD}/{tag}_p{pg:02d}.png"
        row.append(f"{stats(f):>7}" if os.path.exists(f) else "   n/a ")
    print(" | ".join(row))
# clean stray poppler pages
for f in os.listdir(OUTD):
    if f.startswith("popplerall-"): os.remove(os.path.join(OUTD, f))
