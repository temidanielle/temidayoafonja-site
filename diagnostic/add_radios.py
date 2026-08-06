#!/usr/bin/env python3
"""Add clickable 1-5 rating radio-button groups over the drawn circles in the
Capability Formation Diagnostic PDF. One radio group per statement (12 groups,
5 options each = 60 widgets). Selecting a circle draws a navy ring around it
(the printed number stays visible). Native AcroForm radio buttons -> single
selection per row, works in any PDF viewer, no JavaScript.
"""
import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DictionaryObject, ArrayObject, NameObject, NumberObject,
    TextStringObject, FloatObject, DecodedStreamObject, BooleanObject,
)

SRC = "diag_edited.pdf"
OUT = "The_Capability_Formation_Diagnostic.pdf"

NAVY = "0.058824 0.137255 0.278431"
R = 8.0          # widget half-size (circle radius ~7.5)
RING_R = 7.2     # ring radius
LW = 1.6         # ring stroke width

# rows: (page_index, center_y_topOrigin, group_name)
ROWS = [
    (0, 275.3, "rate_s1"), (0, 326.6, "rate_s2"), (0, 377.8, "rate_s3"),
    (0, 424.0, "rate_s4"), (0, 470.2, "rate_s5"), (0, 521.4, "rate_s6"),
    (1, 165.8, "rate_s7"), (1, 205.9, "rate_s8"), (1, 245.9, "rate_s9"),
    (1, 286.0, "rate_s10"), (1, 326.0, "rate_s11"), (1, 361.0, "rate_s12"),
]
XCENTERS = [466.5, 484.5, 502.5, 520.5, 538.5]
PAGE_H = 792.0

reader = PdfReader(SRC)
writer = PdfWriter()
writer.append(reader)

root = writer._root_object
acro = root["/AcroForm"]
acro = acro.get_object()
fields = acro["/Fields"]
# use our explicit ring appearance streams (not viewer-regenerated ones)
acro[NameObject("/NeedAppearances")] = BooleanObject(False)

def circle_path(cx, cy, r):
    k = 0.5523 * r
    return (f"{cx+r:.2f} {cy:.2f} m "
            f"{cx+r:.2f} {cy+k:.2f} {cx+k:.2f} {cy+r:.2f} {cx:.2f} {cy+r:.2f} c "
            f"{cx-k:.2f} {cy+r:.2f} {cx-r:.2f} {cy+k:.2f} {cx-r:.2f} {cy:.2f} c "
            f"{cx-r:.2f} {cy-k:.2f} {cx-k:.2f} {cy-r:.2f} {cx:.2f} {cy-r:.2f} c "
            f"{cx+k:.2f} {cy-r:.2f} {cx+r:.2f} {cy-k:.2f} {cx+r:.2f} {cy:.2f} c ")

def make_ap(on):
    """Appearance XObject: navy ring if on, empty if off. BBox 2R x 2R."""
    side = 2 * R
    if on:
        content = f"{NAVY} RG {LW} w {circle_path(R, R, RING_R)}S\n".encode("latin-1")
    else:
        content = b" "
    s = DecodedStreamObject()
    s.set_data(content)
    s[NameObject("/Type")] = NameObject("/XObject")
    s[NameObject("/Subtype")] = NameObject("/Form")
    s[NameObject("/FormType")] = NumberObject(1)
    s[NameObject("/BBox")] = ArrayObject(
        [FloatObject(0), FloatObject(0), FloatObject(side), FloatObject(side)])
    s[NameObject("/Resources")] = DictionaryObject()
    return writer._add_object(s)

for page_i, cy, gname in ROWS:
    page = writer.pages[page_i]
    parent = DictionaryObject()
    parent[NameObject("/FT")] = NameObject("/Btn")
    parent[NameObject("/Ff")] = NumberObject(1 << 15)          # Radio
    parent[NameObject("/T")] = TextStringObject(gname)
    parent[NameObject("/V")] = NameObject("/Off")
    kids = ArrayObject()
    parent[NameObject("/Kids")] = kids
    parent_ref = writer._add_object(parent)

    for val, cx in enumerate(XCENTERS, 1):
        on_name = f"/{val}"
        rect_y0 = PAGE_H - (cy + R)   # convert top-origin -> PDF bottom-origin
        rect_y1 = PAGE_H - (cy - R)
        kid = DictionaryObject()
        kid[NameObject("/Type")] = NameObject("/Annot")
        kid[NameObject("/Subtype")] = NameObject("/Widget")
        kid[NameObject("/FT")] = NameObject("/Btn")
        kid[NameObject("/Ff")] = NumberObject(1 << 15)
        kid[NameObject("/Parent")] = parent_ref
        kid[NameObject("/Rect")] = ArrayObject(
            [FloatObject(cx - R), FloatObject(rect_y0),
             FloatObject(cx + R), FloatObject(rect_y1)])
        kid[NameObject("/F")] = NumberObject(4)                # Print
        kid[NameObject("/AS")] = NameObject("/Off")
        ap_n = DictionaryObject()
        ap_n[NameObject(on_name)] = make_ap(True)
        ap_n[NameObject("/Off")] = make_ap(False)
        ap = DictionaryObject()
        ap[NameObject("/N")] = ap_n
        kid[NameObject("/AP")] = ap
        mk = DictionaryObject()
        kid[NameObject("/MK")] = mk
        kid_ref = writer._add_object(kid)
        kids.append(kid_ref)
        # register on the page
        if "/Annots" not in page:
            page[NameObject("/Annots")] = ArrayObject()
        page["/Annots"].append(kid_ref)
    fields.append(parent_ref)

with open(OUT, "wb") as f:
    writer.write(f)
print("wrote", OUT, "with 12 radio groups (60 buttons)")
