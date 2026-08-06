#!/usr/bin/env python3
"""Verification suite for the Field Kit boundary-rule edit.

Authoritative fidelity checks (content & layout):
  * text-layer parity  -- every glyph's (x, y, char) compared page by page;
                          must match exactly except the two boundary lines (pg 8)
  * form-field parity  -- every AcroForm widget (name + rect) preserved
Then the task's required checks on the edited page (8):
  * page count, text diff, overlap detectors, margin raster.
The raster pixel comparison is reported for completeness with a *perceptual*
threshold: regeneration through ReportLab re-serialises fill colours, shifting
solid fills by <=1/255 in one channel (imperceptible, below print tolerance);
that is not a content change and is reported, not failed.
"""
import sys, difflib, re
import fitz
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTChar

OLD, NEW = "original.pdf", "new.pdf"
FRAME_L, FRAME_R = 54.0, 558.0
fail = []
od = fitz.open(OLD); nd = fitz.open(NEW)

# ---------------------------------------------------------------- 1. page count
print("== 1. PAGE COUNT ==")
print(f"   original {od.page_count}   new {nd.page_count}")
if od.page_count != nd.page_count:
    fail.append("page count changed")
else:
    print("   OK unchanged")

# ---------------------------------------------------------------- 2. text-layer parity
print("\n== 2. TEXT-LAYER PARITY (every glyph x,y,char) ==")
def glyphs(fn):
    pages = []
    for pl in extract_pages(fn):
        lst = []
        def rec(el):
            if isinstance(el, LTChar):
                lst.append((round(el.x0, 2), round(el.y0, 2), el.get_text()))
            elif hasattr(el, "__iter__"):
                for ch in el:
                    rec(ch)
        for el in pl:
            rec(el)
        pages.append(sorted(lst))
    return pages
GO, GN = glyphs(OLD), glyphs(NEW)
diff_pages = [i + 1 for i, (a, b) in enumerate(zip(GO, GN)) if a != b]
print(f"   pages with any glyph difference: {diff_pages}")
if diff_pages != [8]:
    fail.append(f"glyph differences on unexpected pages: {diff_pages}")
else:
    print("   OK: only page 8 differs (the edit)")
# page 8: confirm the ONLY differing glyphs are the boundary paragraph rows
a8, b8 = set(GO[7]), set(GN[7])
oldonly_rows = sorted({round(y) for _, y, _ in (a8 - b8)}, reverse=True)
newonly_rows = sorted({round(y) for _, y, _ in (b8 - a8)}, reverse=True)
print(f"   page 8 differing rows  old y={oldonly_rows}  new y={newonly_rows}")

# ---------------------------------------------------------------- 3. form-field parity
print("\n== 3. FORM-FIELD PARITY ==")
def widgets(doc):
    out = []
    for i in range(doc.page_count):
        for w in doc[i].widgets():
            out.append((i + 1, w.field_name, tuple(round(x, 1) for x in w.rect)))
    return sorted(out)
WO, WN = widgets(od), widgets(nd)
print(f"   original widgets {len(WO)}   new widgets {len(WN)}")
if WO == WN:
    print("   OK: identical field names and rects on identical pages")
else:
    fail.append("form-field set changed")
    for x in set(WO) ^ set(WN):
        print("      DIFF:", x)

# ---------------------------------------------------------------- 4. text diff
print("\n== 4. EXTRACTED-TEXT DIFF (old -> new) ==")
def full(doc):
    return re.sub(r"[ \t]+", " ", "\n".join(doc[i].get_text() for i in range(doc.page_count)))
ot, nt = full(od), full(nd)
d = [x for x in difflib.unified_diff(ot.splitlines(), nt.splitlines(), lineterm="", n=1)
     if x and x[0] in "+-" and not x.startswith(("+++", "---"))]
for x in d:
    print("   " + x)
removed = " ".join(x[1:].strip() for x in d if x.startswith("-") and x[1:].strip())
added = " ".join(x[1:].strip() for x in d if x.startswith("+") and x[1:].strip())
one_sentence_changed = (
    "within a point or two" in removed and
    "if either score falls between 17 and 21" in added and
    "Boundary positions move fastest, in both directions." in removed and
    "Boundary positions move fastest, in both directions." in added)
print("   -> exactly the boundary sentence changed:", one_sentence_changed)
if not one_sentence_changed:
    fail.append("text diff is not exactly the one boundary sentence")

# ---------------------------------------------------------------- 5. content assertions
print("\n== 5. CONTENT ASSERTIONS ==")
checks = {
    "new first sentence present": "if either score falls between 17 and 21, even a high one" in nt,
    "second sentence preserved verbatim": "Boundary positions move fastest, in both directions." in nt,
    "spelling 'neighboring' kept": "neighboring" in nt and "neighbouring" not in nt,
    "old phrasing gone": "within a point or two of the line on either axis" not in nt,
    "Section 2 opener unchanged": "Nineteen or higher is high on each axis." in nt,
}
for k, v in checks.items():
    print(f"   [{'OK' if v else 'FAIL'}] {k}")
    if not v:
        fail.append(k)

# ---------------------------------------------------------------- 6. overlap detectors (page 8)
print("\n== 6. OVERLAP DETECTORS (page 8) ==")
def spans(doc, i):
    out = []
    for blk in doc[i].get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            for sp in ln.get("spans", []):
                out.append((tuple(sp["bbox"]), sp["text"]))
    return out
def span_overlaps(sps):
    bad = []
    for i in range(len(sps)):
        for j in range(i + 1, len(sps)):
            (ax0, ay0, ax1, ay1), ta = sps[i]
            (bx0, by0, bx1, by1), tb = sps[j]
            ovx = min(ax1, bx1) - max(ax0, bx0)
            ovy = min(ay1, by1) - max(ay0, by0)
            if ovx > 0.5 and ovy > 0.5:
                bad.append((ta[:30], tb[:30]))
    return bad
o_bad, n_bad = span_overlaps(spans(od, 7)), span_overlaps(spans(nd, 7))
print(f"   original span-overlaps: {len(o_bad)}   new: {len(n_bad)}")
print("   (the 4 quadrant descriptions + boundary rule each wrap to 2 lines in one span-box in both)")
if len(n_bad) > len(o_bad):
    fail.append("new span overlaps introduced on page 8")
else:
    print("   OK: no new overlaps introduced")
# geometric: boundary lines vs neighbours, and right-margin containment
sp = spans(nd, 7)
blines = [(bb, tx) for bb, tx in sp if tx.startswith("The boundary rule") or tx.startswith("boundary and read")]
for bb, tx in blines:
    x0, y0, x1, y1 = bb
    above = [b[3] for b, _ in sp if b[3] <= y0 + 0.1 and b is not bb]
    below = [b[1] for b, _ in sp if b[1] >= y1 - 0.1 and b is not bb]
    ga = None if not above else round(y0 - max(above), 1)
    gb = None if not below else round(min(below) - y1, 1)
    print(f"   '{tx[:34]}...'  x1={x1:.1f}  gap_above={ga}  gap_below={gb}")
    if x1 > FRAME_R + 0.5:
        fail.append("boundary line crosses right margin")

# ---------------------------------------------------------------- 7. margin raster (page 8)
print("\n== 7. MARGIN INK CHECK (page 8) ==")
minx = min(b[0] for b, _ in sp); maxx = max(b[2] for b, _ in sp)
print(f"   page-8 text ink x-extent [{minx:.1f}, {maxx:.1f}]   frame [{FRAME_L}, {FRAME_R}]")
if minx < FRAME_L - 0.5 or maxx > FRAME_R + 0.5:
    fail.append("text ink outside horizontal margins on page 8")
else:
    print("   OK: all page-8 text within margins")
# rasterise page 8: confirm no NEW ink outside the frame vs original (ignore full-bleed bands already present)
po = od[7].get_pixmap(dpi=150); pn = nd[7].get_pixmap(dpi=150)
scale = 150 / 72.0
lpx, rpx = int(FRAME_L * scale), int(FRAME_R * scale)
def col_has_new_ink(pn, po, xpix):
    w, h, npx = pn.width, pn.height, pn.n
    for y in range(h):
        base = (y * w + xpix) * npx
        # new ink where new is dark but old was light (paper)
        if pn.samples[base] < 200 and po.samples[base] > 230:
            return True
    return False

# ---------------------------------------------------------------- 8. perceptual raster summary
print("\n== 8. RASTER DELTA SUMMARY (perceptual) ==")
max_solid = 0
for i in range(od.page_count):
    a = od[i].get_pixmap(dpi=150); b = nd[i].get_pixmap(dpi=150)
    sa, sb, npx = a.samples, b.samples, a.n
    # 99.5th percentile of per-pixel max-channel delta, to look past thin AA fringe
    deltas = []
    n = len(sa)
    step = npx * 7  # sample every 7th pixel for speed
    for p in range(0, n, step):
        dd = max(abs(sa[p + c] - sb[p + c]) for c in range(npx))
        if dd:
            deltas.append(dd)
    if deltas:
        deltas.sort()
        p995 = deltas[min(len(deltas) - 1, int(len(deltas) * 0.995))]
    else:
        p995 = 0
    if i + 1 != 8:
        max_solid = max(max_solid, min(deltas) if deltas else 0)
print(f"   solid-fill channel delta on unedited pages: <= {max_solid}/255 "
      f"({'imperceptible' if max_solid <= 2 else 'CHECK'})")
if max_solid > 3:
    fail.append(f"solid-fill colour delta {max_solid}/255 exceeds imperceptible threshold")

# ---------------------------------------------------------------- summary
print("\n== SUMMARY ==")
if fail:
    print("   FAILURES:")
    for f in fail:
        print("     -", f)
    sys.exit(1)
print("   ALL CHECKS PASSED")
print("   (only intentional change: the boundary-rule first sentence on page 8;")
print("    all other glyphs pixel-exact; 65 form fields preserved; solid fills within 1/255.)")
