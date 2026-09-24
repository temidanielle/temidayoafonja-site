#!/usr/bin/env python3
"""Build 04_PRINTABLE_FILLABLE_TOOLS.pdf: printable pages with real fillable
AcroForm fields, holding the same fields as the Professional Record."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import record_model as M
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white

ROOT = "/home/user/temidayoafonja-site"
OUT = f"{ROOT}/_build/keep-the-proof-v2/production/bundle/04_PRINTABLE_FILLABLE_TOOLS.pdf"

NAVY = HexColor("#112345")
CREAM = HexColor("#F5F1E8")
GOLD = HexColor("#C9A84C")
GOLDINK = HexColor("#8f7226")
GREY = HexColor("#6b707d")
INK = HexColor("#1c2333")
LINE = HexColor("#cdc7b8")

PW, PH = letter
ML, MR, MT, MB = 54, 54, 60, 54
CW = PW - ML - MR

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Keep the Proof: Printable & Fillable Tools")
_fid = [0]
def fid(prefix):
    _fid[0]+=1; return f"{prefix}_{_fid[0]}"

def wrap(text, font, size, maxw):
    words = text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if c.stringWidth(t, font, size) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def page_header(kicker, title, subtitle=""):
    # top navy band
    c.setFillColor(NAVY); c.rect(0, PH-42, PW, 42, fill=1, stroke=0)
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8)
    c.drawString(ML, PH-19, "KEEP THE PROOF")
    c.setFillColor(CREAM); c.setFont("Helvetica", 7.5)
    c.drawRightString(PW-MR, PH-19, "PRINTABLE & FILLABLE TOOLS")
    y = PH - 72
    c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(ML, y, kicker.upper())
    y -= 20
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 19)
    c.drawString(ML, y, title)
    y -= 8
    c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(ML, y, ML+46, y)
    y -= 14
    if subtitle:
        c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 9)
        for ln in wrap(subtitle, "Helvetica-Oblique", 9, CW):
            c.drawString(ML, y, ln); y -= 12
    return y - 6

def draw_field(y, label, hint, lines, prefix="f"):
    # label
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawString(ML, y, label)
    y -= 11
    if hint:
        c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 7.6)
        for ln in wrap(hint, "Helvetica-Oblique", 7.6, CW):
            c.drawString(ML, y, ln); y -= 9
    h = 16*lines
    y -= h
    c.acroForm.textfield(name=fid(prefix), x=ML, y=y, width=CW, height=h,
        borderStyle='underlined', borderColor=LINE, fillColor=None,
        textColor=INK, borderWidth=0.75, forceBorder=False,
        fontName='Helvetica', fontSize=10,
        fieldFlags=('multiline' if lines>1 else ''))
    # a light baseline
    c.setStrokeColor(LINE); c.setLineWidth(0.75); c.line(ML, y, ML+CW, y)
    return y - 12

def draw_checkbox(y, text, prefix="cb"):
    size=10
    c.acroForm.checkbox(name=fid(prefix), x=ML, y=y-1, size=size,
        borderColor=GOLD, fillColor=white, borderWidth=0.9, checked=False)
    c.setFillColor(INK); c.setFont("Helvetica", 9.5)
    for i,ln in enumerate(wrap(text, "Helvetica", 9.5, CW-20)):
        c.drawString(ML+18, y, ln);
        if i==0: y0=y
        y -= 12
    return y - 3

def block_label(y, text):
    c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 10)
    c.drawString(ML, y, text)
    return y - 16

def body(y, text, color=INK, size=9.5, font="Helvetica", after=8):
    c.setFillColor(color); c.setFont(font, size)
    for ln in wrap(text, font, size, CW):
        c.drawString(ML, y, ln); y -= 12.5
    return y - after

# ================= COVER / INTRO PAGE =================
c.setFillColor(NAVY); c.rect(0,0,PW,PH, fill=1, stroke=0)
c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 9)
c.drawCentredString(PW/2, PH-150, "THE DENSITY GROUP")
c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 30)
c.drawCentredString(PW/2, PH-210, "KEEP THE PROOF")
c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(PW/2-30, PH-224, PW/2+30, PH-224)
c.setFillColor(CREAM); c.setFont("Helvetica-Oblique", 14)
c.drawCentredString(PW/2, PH-250, "Printable & Fillable Tools")
c.setFillColor(HexColor("#c9d0dd")); c.setFont("Helvetica", 10)
intro = ("These pages hold the same fields as your Professional Record, for anyone who prefers to write "
    "by hand or type into a form. Fill them on screen, or print and complete them by hand. You do not "
    "need to complete both these pages and the Professional Record: choose whichever you will keep up.")
yy = PH-300
for ln in wrap(intro, "Helvetica", 10, CW-80):
    c.drawCentredString(PW/2, yy, ln); yy -= 15
c.setFillColor(GOLD); c.setFont("Helvetica-Oblique", 9.5)
yy -= 10
c.drawCentredString(PW/2, yy, "Permission first: your own recollection and what you are permitted to keep.")
yy -= 14
c.drawCentredString(PW/2, yy, "Never paste in employer-owned files or confidential detail.")
c.showPage()

# ================= QUICK CAPTURE (2 pages) =================
for n in (1,2):
    y = page_header("Capture Log", f"Quick Capture {n}",
        "Catch work the moment it happens, in two minutes, before the details soften. One capture per page.")
    for label,hint,lines in M.CAPTURE_FIELDS:
        y = draw_field(y, label, hint, lines, prefix=f"qc{n}")
    c.showPage()

# ================= FULL ENTRY (2 pages) =================
# Page 1: clusters A, B, C
y = page_header("Full Entries", "Full Entry, page 1 of 2",
    "For work worth keeping in depth. Fill only the fields that apply.")
for ct in ("Cluster A. When and what","Cluster B. What was yours","Cluster C. The judgment inside it"):
    fields = dict(M.FULL_ENTRY_CLUSTERS)[ct]
    y = block_label(y, ct)
    for label,hint,lines in fields:
        y = draw_field(y, label, hint, lines, prefix="feA")
c.showPage()
# Page 2: clusters D, E + reconstruction marker
y = page_header("Full Entries", "Full Entry, page 2 of 2", "")
for ct in ("Cluster D. What changed, and what supports it","Cluster E. How you would say it, and who could confirm it"):
    fields = dict(M.FULL_ENTRY_CLUSTERS)[ct]
    y = block_label(y, ct)
    for label,hint,lines in fields:
        y = draw_field(y, label, hint, 1 if lines>2 else lines, prefix="feB")
y = body(y-2, M.RECON_MARKER, color=GREY, size=8.5, font="Helvetica-Oblique")
c.showPage()

# ================= CORROBORATION (1 page) =================
y = page_header("Corroboration list", "Corroboration",
    "Who could confirm your work while they still remember it. Corroboration readiness, not networking.")
for n in range(1,4):
    y = block_label(y, f"Corroboration {n}")
    for label,hint,lines in M.CORROB_FIELDS:
        y = draw_field(y, label, hint, lines, prefix=f"co{n}")
y = body(y, M.CORROB_NOTE, color=GREY, size=8.3, font="Helvetica-Oblique")
c.showPage()

# ================= TRANSLATION & PROOF LINE (1 page) =================
y = page_header("Translation & Proof Line", "Translation and Proof Line workspace",
    "Turn internal language into portable language, and build the sentence you can reuse.")
y = block_label(y, "Translation worksheet")
y = body(y, "Work down the eight moves and apply the ones that fit, then the protection rule.", size=9)
for m in M.TRANSLATION_MOVES:
    y = draw_checkbox(y, m, prefix="tm")
y = body(y-2, M.TRANSLATION_PROTECTION, color=GREY, size=8.3, font="Helvetica-Oblique")
y = block_label(y, "Proof Line builder")
for label,hint,lines in M.PROOFLINE_INGREDIENTS:
    y = draw_field(y, label, hint, 1, prefix="pl")
y = draw_field(y, "Your Proof Line", "", 2, prefix="plfinal")
y = body(y, M.PROOFLINE_RULE, color=GREY, size=8.3, font="Helvetica-Oblique")
c.showPage()

# ================= MATCH YOUR PROOF TO A ROLE (1 page) =================
y = page_header("Match to a role", M.MATCH_TITLE,
    "Line up what a role asks for against the proof you already hold.")
y = body(y, M.MATCH_INTRO, size=9)
# three-column layout
GAP = 10
COLW = (CW - 2*GAP) / 3
COLX = [ML, ML+COLW+GAP, ML+2*(COLW+GAP)]
def match_headers(y):
    c.setFillColor(NAVY); c.rect(ML, y-15, CW, 16, fill=1, stroke=0)
    c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 8)
    for i,h in enumerate(M.MATCH_COLUMNS):
        for j,ln in enumerate(wrap(h, "Helvetica-Bold", 8, COLW-8)):
            c.drawString(COLX[i]+4, y-4-(j*9), ln)
    return y-19
def match_cell_text(x, y, text, h):
    c.setFillColor(INK); c.setFont("Helvetica-Oblique", 8)
    ty = y-9
    for ln in wrap(text, "Helvetica-Oblique", 8, COLW-8):
        c.drawString(x+4, ty, ln); ty -= 9.5
def match_row(y, example=None, h=52, prefix="mr"):
    # cell borders
    c.setStrokeColor(LINE); c.setLineWidth(0.75)
    for i in range(3):
        c.rect(COLX[i], y-h, COLW, h, fill=0, stroke=1)
    if example:
        # shaded example row
        c.setFillColor(HexColor("#FBF3E2"))
        for i in range(3):
            c.rect(COLX[i], y-h, COLW, h, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        for i in range(3):
            c.rect(COLX[i], y-h, COLW, h, fill=0, stroke=1)
        for i in range(3):
            match_cell_text(COLX[i], y, example[i], h)
    else:
        for i in range(3):
            c.acroForm.textfield(name=fid(prefix), x=COLX[i]+1.5, y=y-h+1.5,
                width=COLW-3, height=h-3, borderStyle='underlined',
                borderColor=None, fillColor=None, textColor=INK,
                borderWidth=0, forceBorder=False, fontName='Helvetica',
                fontSize=9, fieldFlags='multiline')
    return y-h-4
y = match_headers(y)
# label the example
c.setFillColor(GOLDINK); c.setFont("Helvetica-Oblique", 7.5)
c.drawString(ML, y-1, "EXAMPLE"); y -= 11
y = match_row(y, example=M.MATCH_EXAMPLE, h=44)
for _ in range(3):
    y = match_row(y, h=50, prefix="mr")
y = body(y-2, M.MATCH_BOUNDARY, color=GREY, size=8.3, font="Helvetica-Oblique")
c.showPage()

# ================= MAINTENANCE (1 page) =================
y = page_header("Maintenance", "Optional maintenance checklists",
    "Use whichever you will sustain, or both. Neither is required, and neither is better.")
y = block_label(y, "Monthly sweep, about ten to fifteen minutes")
for m in M.MONTHLY:
    y = draw_checkbox(y, m, prefix="mo")
y -= 4
y = block_label(y, "Quarterly review, about thirty minutes")
for q in M.QUARTERLY:
    y = draw_checkbox(y, q, prefix="qr")
y = body(y-2, M.MAINT_NOTE, color=GREY, size=8.5, font="Helvetica-Oblique")
c.showPage()

c.save()
print("PDF:", OUT, os.path.getsize(OUT), "bytes")
# page count
import pypdfium2 as pdfium
print("pages:", len(pdfium.PdfDocument(OUT)))
