#!/usr/bin/env python3
"""Rebuild the Diagnostic from the ORIGINAL (fonts keep their cmaps so the score
boxes stay typeable): apply the boundary rewording + the /audit->/diagnostic URL
change in one pass. No PyMuPDF subset_fonts (that strips cmaps). Radio buttons
are added afterwards by add_radios.py.
"""
import fitz

SRC = "original_diag.pdf"
OUT = "diag_edited.pdf"
NAVY = (0x0F/255, 0x23/255, 0x47/255)
GOLD = (0xC9/255, 0xA8/255, 0x4C/255)
RUST = (0xC1/255, 0x44/255, 0x0E/255)

reg = fitz.Font(fontfile="Inter_s.ttf")
itf = fitz.Font(fontfile="Inter-It_s.ttf")
sbf = fitz.Font(fontfile="Inter-SB_s.ttf")

d = fitz.open(SRC)

# ---- boundary paragraph (page index 1) ----
BOUND_REDACT = [fitz.Rect(66.0, 542.3, 308.4, 553.2),
                fitz.Rect(66.0, 555.4, 292.5, 566.3),
                fitz.Rect(66.0, 568.4, 227.0, 579.3)]
BOUND_LINES = [  # (baseline_y, [(text, italic)])
    (551.05, [("Any score between 17 and 21 sits close enough to the line", False)]),
    (564.10, [("to go either way, even a high one. Check here: ", False), ("I am on a", True)]),
    (577.15, [("boundary and will read both neighboring states.", True)]),
]
# ---- URL occurrences (visible text): (page, redact_rect, point, font, size, color) ----
NEW_URL = "temidayoafonja.com/diagnostic"
URL_EDITS = [
    (0, fitz.Rect(135.2, 754.5, 228.1, 764.6), (135.7, 762.29), "reg", 7.5, GOLD),
    (1, fitz.Rect(135.2, 754.5, 228.1, 764.6), (135.7, 762.29), "reg", 7.5, GOLD),
    (2, fitz.Rect(77.1, 545.7, 179.5, 556.4), (77.6, 554.00), "sb", 8.0, RUST),
    (2, fitz.Rect(135.2, 754.5, 228.1, 764.6), (135.7, 762.29), "reg", 7.5, GOLD),
]
OLD_URI, NEW_URI = "https://temidayoafonja.com/audit", "https://temidayoafonja.com/diagnostic"

# capture original /audit link rects before redaction removes them
old_links = {pi: [fitz.Rect(l["from"]) for l in d[pi].get_links() if l.get("uri") == OLD_URI]
             for pi in range(d.page_count)}

# redact per page (text only) then insert
for pi in range(d.page_count):
    pg = d[pi]
    if pi == 1:
        for r in BOUND_REDACT:
            pg.add_redact_annot(r)
    for e in [x for x in URL_EDITS if x[0] == pi]:
        pg.add_redact_annot(e[1])
    if pi == 1 or any(x[0] == pi for x in URL_EDITS):
        pg.apply_redactions(graphics=fitz.PDF_REDACT_LINE_ART_NONE,
                            images=fitz.PDF_REDACT_IMAGE_NONE)
    pg.insert_font(fontname="reg", fontfile="Inter_s.ttf")
    pg.insert_font(fontname="itf", fontfile="Inter-It_s.ttf")
    pg.insert_font(fontname="sb", fontfile="Inter-SB_s.ttf")
    # boundary text
    if pi == 1:
        for baseline, runs in BOUND_LINES:
            x = 66.0
            for text, ital in runs:
                pg.insert_text((x, baseline), text, fontname=("itf" if ital else "reg"),
                               fontsize=9.0, color=NAVY)
                x += (itf if ital else reg).text_length(text, 9.0)
    # URL text
    for _, _, pt, fk, size, color in [x for x in URL_EDITS if x[0] == pi]:
        pg.insert_text(pt, NEW_URL, fontname=fk, fontsize=size, color=color)

# retarget links (recreate; redaction removed the originals)
for pi, rects in old_links.items():
    pg = d[pi]
    for f in rects:
        is_save = abs(f.y0 - 545.3) < 2
        width = (sbf if is_save else reg).text_length(NEW_URL, 8.0 if is_save else 7.5)
        pg.insert_link({"kind": fitz.LINK_URI,
                        "from": fitz.Rect(f.x0, f.y0, f.x0 + width + 1, f.y1),
                        "uri": NEW_URI})

d.save(OUT, garbage=4, deflate=True)   # NO subset_fonts
print("wrote", OUT)
