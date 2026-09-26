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
ICON_DIR = f"{ROOT}/_build/keep-the-proof-v2/production/assets/icons"

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

def newpage():
    # footer page number, centered; skip the cover (page 1)
    if c.getPageNumber() > 1:
        c.setFillColor(GREY); c.setFont("Helvetica", 8)
        c.drawCentredString(PW/2, 30, str(c.getPageNumber()))
    c.showPage()

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

def icon_img(name, x, y, size):
    c.drawImage(f"{ICON_DIR}/{name}.png", x, y, width=size, height=size, mask='auto')

def page_header(kicker, title, subtitle="", icon=None):
    # top navy band
    c.setFillColor(NAVY); c.rect(0, PH-42, PW, 42, fill=1, stroke=0)
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8)
    c.drawString(ML, PH-19, "KEEP THE PROOF")
    c.setFillColor(CREAM); c.setFont("Helvetica", 7.5)
    c.drawRightString(PW-MR, PH-19, "PRINTABLE & FILLABLE TOOLS")
    y = PH - 72
    if kicker:
        c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 8.5)
        c.drawString(ML, y, kicker.upper())
        y -= 20
    tx = ML
    if icon:
        icon_img(icon, ML, y-3, 21); tx = ML + 29
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 19)
    c.drawString(tx, y, title)
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

def block_label(y, text, icon=None):
    tx = ML
    if icon:
        icon_img(icon, ML, y-3, 14); tx = ML + 20
    c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 10)
    c.drawString(tx, y, text)
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
newpage()

# ================= BEFORE YOU REBUILD ANYTHING (1 page) =================
y = page_header("Before you begin", "Before you rebuild anything",
    "Two moves before Part One: name three moments, then read the words that hold.", icon="reconstruct")
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
c.drawString(ML, y, M.THREE_MOMENTS_LABEL); y -= 11
c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 7.6)
for ln in wrap(M.THREE_MOMENTS_HINT, "Helvetica-Oblique", 7.6, CW):
    c.drawString(ML, y, ln); y -= 9
y -= 6
for i in range(3):
    c.acroForm.textfield(name=fid("moment"), x=ML, y=y-16, width=CW, height=16,
        borderStyle='underlined', borderColor=LINE, fillColor=None, textColor=INK,
        borderWidth=0.75, forceBorder=False, fontName='Helvetica', fontSize=10)
    c.setStrokeColor(LINE); c.setLineWidth(0.75); c.line(ML, y-16, ML+CW, y-16)
    y -= 30
y -= 14
# Words That Hold panel
icon_img("words", ML, y-3, 14)
c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 10)
c.drawString(ML+20, y, M.WORDS_TITLE); y -= 13
c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 8)
for ln in wrap(M.WORDS_LEAD, "Helvetica-Oblique", 8, CW):
    c.drawString(ML, y, ln); y -= 10
y -= 6
panel_h = 20*len(M.WORDS_AFFIRMATIONS) + 40
c.setFillColor(HexColor("#FBF3E2"))
c.roundRect(ML, y-panel_h, CW, panel_h, 8, fill=1, stroke=0)
c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(ML, y-panel_h, ML, y)
ty = y - 20
c.setFillColor(NAVY); c.setFont("Helvetica-Oblique", 11)
for w in M.WORDS_AFFIRMATIONS:
    c.drawString(ML+18, ty, w); ty -= 20
ty -= 2
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
c.drawString(ML+18, ty, M.WORDS_FILLIN)
fw = c.stringWidth(M.WORDS_FILLIN, "Helvetica-Bold", 9)
c.acroForm.textfield(name=fid("wfill"), x=ML+18+fw+6, y=ty-3, width=CW-36-fw-6, height=14,
    borderStyle='underlined', borderColor=GOLD, fillColor=None, textColor=INK,
    borderWidth=0.75, forceBorder=False, fontName='Helvetica', fontSize=10)
newpage()

# ================= READ-BACK CARD (1 page) =================
# No kicker: the title and intro stand on their own.
y0 = page_header("", "Read-Back Card",
    "Read this each morning for 30 days. Keep it where you will see it.", icon="words")

LH = 16  # a handwriting line

def rb_label(x, y, text, w, size=9):
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", size)
    for ln in wrap(text, "Helvetica-Bold", size, w):
        c.drawString(x, y, ln); y -= 11
    return y

def rb_lines(x, y, w, prefix, n=3):
    # a multi-line fillable box with n printed handwriting rules
    h = n * LH
    c.acroForm.textfield(name=fid(prefix), x=x, y=y-h, width=w, height=h,
        borderStyle='underlined', borderColor=LINE, fillColor=None, textColor=INK,
        borderWidth=0, forceBorder=False, fontName='Helvetica', fontSize=10,
        fieldFlags='multiline')
    c.setStrokeColor(LINE); c.setLineWidth(0.6)
    for i in range(n):
        yy = y - (i + 1) * LH
        c.line(x, yy, x + w, yy)
    return y - h - 10

# --- Words That Hold: six lines in a cream panel, handbook serif ---
icon_img("words", ML, y0-3, 13)
c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 10)
c.drawString(ML+18, y0, "Words That Hold")
py = y0 - 17
inner = CW - 36
aff_lines = []
for w in M.WORDS_AFFIRMATIONS:
    aff_lines += wrap(w, "Times-Italic", 13.5, inner)
panel_h = 14 + len(aff_lines) * 19 + 12
c.setFillColor(HexColor("#FBF3E2"))
c.roundRect(ML, py - panel_h, CW, panel_h, 8, fill=1, stroke=0)
c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(ML, py - panel_h, ML, py)
ty = py - 20
c.setFillColor(NAVY); c.setFont("Times-Italic", 13.5)
for ln in aff_lines:
    c.drawString(ML + 18, ty, ln); ty -= 19
y = py - panel_h - 14
# fill-in with a two-line box
y = rb_label(ML, y, M.WORDS_FILLIN, CW)
y = rb_lines(ML, y, CW, "rbfill", n=2)

# --- My evidence: two balanced columns of multi-line boxes ---
y -= 4
c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 10)
c.drawString(ML, y, "My evidence")
y -= 16
GAP2 = 24
COLW2 = (CW - GAP2) / 2
LX = ML
RX = ML + COLW2 + GAP2
# left column: the three record moments (four lines each)
ly = y
for _ in range(3):
    ly = rb_label(LX, ly, "A moment or Proof Line from my record", COLW2)
    ly = rb_lines(LX, ly, COLW2, "rbmoment", n=4)
# right column: the belief pair and the shrink pair (three lines each)
ry = y
ry = rb_label(RX, ry, "The line I am learning to believe", COLW2)
ry = rb_lines(RX, ry, COLW2, "rbline", n=3)
ry = rb_label(RX, ry, "The entry that supports it", COLW2)
ry = rb_lines(RX, ry, COLW2, "rbentry", n=3)
ry = rb_label(RX, ry, "A sentence that shrinks my work", COLW2)
ry = rb_lines(RX, ry, COLW2, "rbshrink", n=3)
ry = rb_label(RX, ry, "What would have been different if I had not been there?", COLW2)
ry = rb_lines(RX, ry, COLW2, "rbdiff", n=3)

# --- bottom: 30 numbered checkboxes, near the footer ---
by = 108
c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 9)
c.drawString(ML, by, "Mornings read")
by -= 18
pitch = CW / 30.0
for i in range(30):
    cx = ML + i * pitch
    c.acroForm.checkbox(name=fid("morning"), x=cx, y=by-9, size=9,
        borderColor=GOLD, fillColor=white, borderWidth=0.8, checked=False)
    c.setFillColor(GREY); c.setFont("Helvetica", 5.5)
    c.drawCentredString(cx+4.5, by-18, str(i+1))
newpage()

# ================= QUICK CAPTURE (2 pages) =================
for n in (1,2):
    y = page_header("Capture Log", f"Quick Capture {n}",
        "Catch work the moment it happens, in two minutes, before the details soften. One capture per page.", icon="capture")
    for label,hint,lines in M.CAPTURE_FIELDS:
        y = draw_field(y, label, hint, lines, prefix=f"qc{n}")
    newpage()

# ================= FULL ENTRY (2 pages) =================
# Page 1: clusters A, B, C
y = page_header("Full Entries", "Full Entry, page 1 of 2",
    "For work worth keeping in depth. Fill only the fields that apply.", icon="clarify")
for ct in ("Cluster A. When and what","Cluster B. What was yours","Cluster C. The judgment inside it"):
    fields = dict(M.FULL_ENTRY_CLUSTERS)[ct]
    y = block_label(y, ct)
    for label,hint,lines in fields:
        y = draw_field(y, label, hint, lines, prefix="feA")
newpage()
# Page 2: clusters D, E + reconstruction marker
y = page_header("Full Entries", "Full Entry, page 2 of 2", "")
for ct in ("Cluster D. What changed, and what supports it","Cluster E. How you would say it, and who could confirm it"):
    fields = dict(M.FULL_ENTRY_CLUSTERS)[ct]
    y = block_label(y, ct)
    for label,hint,lines in fields:
        y = draw_field(y, label, hint, 1 if lines>2 else lines, prefix="feB")
y = body(y-2, M.RECON_MARKER, color=GREY, size=8.5, font="Helvetica-Oblique")
newpage()

# ================= CORROBORATION (1 page) =================
y = page_header("Corroboration list", "Corroboration",
    "Who could confirm your work while they still remember it. Corroboration readiness, not networking.")
for n in range(1,4):
    y = block_label(y, f"Corroboration {n}")
    for label,hint,lines in M.CORROB_FIELDS:
        y = draw_field(y, label, hint, lines, prefix=f"co{n}")
y = body(y, M.CORROB_NOTE, color=GREY, size=8.3, font="Helvetica-Oblique")
newpage()

# ================= TRANSLATION & PROOF LINE (1 page) =================
y = page_header("Translation & Proof Line", "Translation and Proof Line workspace", icon="proofline", subtitle=
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
newpage()

# ================= MATCH YOUR PROOF TO A ROLE (1 page) =================
y = page_header("Match to a role", M.MATCH_TITLE,
    "Line up what a role asks for against the proof you already hold.", icon="match")
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
newpage()

# ================= PUT YOUR RECORD TO WORK (1 page) =================
y = page_header("Put your record to work", M.PUT_TO_WORK_TITLE,
    "Carry one Proof Line into the four places people use most. Public-use check first: only what you may share, and Keep, Care, Never.", icon="carry")
_ptw_lines = [1, 2, 3, 3]
_ptw_icons = ["resume", "about", "interview", "promotion"]
for _i,(title,purpose) in enumerate(M.PUT_TO_WORK_USES):
    y = block_label(y, title, icon=_ptw_icons[_i])
    y = body(y, purpose, color=GREY, size=8.6, font="Helvetica-Oblique", after=3)
    y = draw_field(y, "", "", _ptw_lines[_i], prefix="ptw")
newpage()

# ================= MAINTENANCE (1 page) =================
y = page_header("Maintenance", "Optional maintenance checklists",
    "Use whichever you will sustain, or both. Neither is required, and neither is better.")
y = block_label(y, "Monthly sweep, about ten to fifteen minutes", icon="monthly")
for m in M.MONTHLY:
    y = draw_checkbox(y, m, prefix="mo")
y -= 4
y = block_label(y, "Quarterly review, about thirty minutes", icon="quarterly")
for q in M.QUARTERLY:
    y = draw_checkbox(y, q, prefix="qr")
y = body(y-2, M.MAINT_NOTE, color=GREY, size=8.5, font="Helvetica-Oblique")
c.setFillColor(GOLDINK); c.setFont("Helvetica-Bold", 9)
c.drawString(ML, y-4, "Tell me how it went: temidayoafonja.com/review.")
newpage()

c.save()
print("PDF:", OUT, os.path.getsize(OUT), "bytes")
# page count
import pypdfium2 as pdfium
print("pages:", len(pdfium.PdfDocument(OUT)))
