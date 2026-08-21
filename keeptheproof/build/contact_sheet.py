#!/usr/bin/env python3
"""RC3 icon-review contact sheet: renders the covers, the five handbook part
dividers, the selected handbook tool pages, and one example of each ledger form
icon into a labelled grid PNG. Usage: contact_sheet.py <handbook.pdf> <ledger.pdf> <out.png>"""
import sys, fitz
from PIL import Image, ImageDraw, ImageFont

HB, LG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
items = [
    (HB, 1,  "Handbook cover — evidence mark"),
    (LG, 1,  "Ledger cover — evidence mark"),
    (HB, 5,  "Part One — record + magnifier"),
    (HB, 11, "Part Two — shield + check"),
    (HB, 15, "Part Three — form + pencil"),
    (HB, 26, "Part Four — layered cards"),
    (HB, 29, "Part Five — calendar + loop"),
    (HB, 16, "Tool p16 — clock + pencil"),
    (HB, 17, "Tool p17 — form card"),
    (HB, 23, "Tool p23 — translate arrow"),
    (HB, 24, "Tool p24 — proof lines"),
    (HB, 30, "Tool p30 — 60-min clock"),
    (HB, 31, "Tool p31 — calendar loop"),
    (HB, 32, "Tool p32 — record + magnifier"),
    (LG, 3,  "Ledger — Quick Capture band"),
    (LG, 5,  "Ledger — Full Entry band"),
    (LG, 8,  "Ledger — Translation band"),
    (LG, 9,  "Ledger — Proof Line band"),
    (LG, 10, "Ledger — Monthly Sweep band"),
    (LG, 11, "Ledger — Quarterly Review band"),
    (LG, 12, "Ledger — Evidence Index"),
]
TW = 300                     # thumb width
cols = 4
cap_h = 22
docs = {}
def get(p):
    if p not in docs: docs[p] = fitz.open(p)
    return docs[p]
thumbs = []
for path, pg, cap in items:
    d = get(path)
    pix = d[pg-1].get_pixmap(dpi=96)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    th = int(im.height * TW / im.width)
    im = im.resize((TW, th))
    thumbs.append((im, cap))
maxh = max(t[0].height for t in thumbs)
cellw, cellh = TW + 16, maxh + cap_h + 16
rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (cols*cellw, rows*cellh), "#F5F0E8")
dr = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except Exception: font = ImageFont.load_default()
for i, (im, cap) in enumerate(thumbs):
    r, c = divmod(i, cols)
    x, y = c*cellw + 8, r*cellh + 8
    sheet.paste(im, (x, y))
    dr.text((x, y + im.height + 4), cap, fill="#0F2347", font=font)
sheet.save(OUT)
print("wrote", OUT, sheet.size)
