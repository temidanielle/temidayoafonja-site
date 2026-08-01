#!/usr/bin/env python3
"""
Build the Session Workbook ("Should I Stay or Should I Move?") in the
Capability Formation Field Kit's visual system.

Content is frozen and taken verbatim from the v5.3 fillable workbook PDF.
Presentation is rebuilt from scratch to match the Field Kit
(The_Capability_Formation_FieldKit.pdf), which is the canonical house style.
None of the v5.3 PDF's visual decisions are carried over: no navy emphasis
bands, no borderless invisible fields, section openers added.

Pipeline:
  1. ReportLab draws every page (static graphics + all 104 AcroForm fields,
     styled: pale-blue fill, tan border, correct flags, multiline where the
     source field is multiline, read-only on the ten computed totals).
  2. A pymupdf post-pass attaches the tolerant calculation JavaScript to the
     ten computed fields (which also builds the /CO calculation-order array)
     and sets NeedAppearances so the totals fire in Acrobat and most desktop
     readers.

Usage:
    python3 build_workbook.py [output.pdf]
        default output: Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf
"""
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
import fitz  # pymupdf, used only for the calculation post-pass

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    HERE, "Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf")

# ----------------------------------------------------------------- palette
# Exact tokens from the handoff spec. No colour outside this set is used for
# the design. (The pale-blue field fill + tan field border below are the one
# functional exception the spec itself mandates for form widgets, so that a
# participant can see what is typeable.)
def rgb(h):
    h = h.lstrip("#")
    return Color(int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255)

NAVY = rgb("0F2347")   # section pages, header bars, body text/headings, state cards
RUST = rgb("C1440E")   # numerals, emphasis italics, Compounding card, brand-mark square
GOLD = rgb("C9A84C")   # rules, small-caps labels, borders, brand mark — on dark grounds
GOLD_DEEP = rgb("B89532")  # gold text on light grounds, for contrast
SAND = rgb("F5F0E8")   # page field and callout fill (cream)
WHITE = rgb("FFFFFF")  # content-page ground

# Functional form-widget affordance (mandated by the spec for fields only):
FIELD_FILL = rgb("E9F0F8")   # pale blue
FIELD_BORDER = rgb("CDAE70")  # tan
FIELD_BW = 0.75

# ----------------------------------------------------------------- fonts
FONTS = {
    "CG": ("CG-Regular.ttf", "CormGaramond"),
    "CGSb": ("CG-SemiBold.ttf", "CormGaramond-SemiBold"),
    "CGB": ("CG-Bold.ttf", "CormGaramond-Bold"),
    "CGI": ("CG-MediumItalic.ttf", "CormGaramond-MediumItalic"),
    "CGSbI": ("CG-SemiBoldItalic.ttf", "CormGaramond-SemiBoldItalic"),
    "DM": ("DM-Regular.ttf", "DMSans"),
    "DMMed": ("DM-Medium.ttf", "DMSans-Medium"),
    "DMSb": ("DM-SemiBold.ttf", "DMSans-SemiBold"),
    "DMB": ("DM-Bold.ttf", "DMSans-Bold"),
    "DMI": ("DM-Italic.ttf", "DMSans-Italic"),
}
FN = {}  # short key -> registered reportlab font name
for key, (fname, psname) in FONTS.items():
    pdfmetrics.registerFont(TTFont(psname, os.path.join(FONT_DIR, fname)))
    FN[key] = psname

# ----------------------------------------------------------------- geometry
PW, PH = 612.0, 792.0
ML, MR = 54.0, 558.0
CW = MR - ML                       # 504 content width
HEADER_H = 96.0                    # navy header bar height (matches Field Kit)
HEADER_TOP = PH                    # bar spans PH-HEADER_H .. PH
CONTENT_TOP = PH - HEADER_H - 24   # first content baseline region
FOOTER_RULE_Y = 44.0
FOOTER_TEXT_Y = 31.0

IDENTITY = "SESSION WORKBOOK   ·   TEMIDAYO AFONJA   ·   TEMIDAYOAFONJA.COM"

# =================================================================== helpers
def set_fill(c, col):
    c.setFillColor(col)

def tracked(c, x, y, text, font, size, color, tracking=0.0, align="left"):
    """Draw text with letter tracking (used for small-caps labels).

    Wrapped in save/restore so the Tc (character-spacing) operator does not
    leak into subsequent plain drawString calls.
    """
    if align != "left":
        w = stringWidth(text, font, size) + tracking * max(len(text) - 1, 0)
        if align == "center":
            x -= w / 2.0
        elif align == "right":
            x -= w
    c.saveState()
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(tracking)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()

def label(c, x, y, text, size=8.0, color=GOLD_DEEP, tracking=1.3, align="left"):
    """Gold small-caps field label."""
    tracked(c, x, y, text.upper(), FN["DMSb"], size, color, tracking, align)

def simple(c, x, y, text, font, size, color, align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)

def wrap_lines(text, font, size, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if stringWidth(trial, font, size) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def para(c, x, y, text, font, size, color, leading, max_w, align="left"):
    """Draw a wrapped paragraph from baseline y downward. Returns y after."""
    for ln in wrap_lines(text, font, size, max_w):
        if align == "center":
            simple(c, x, y, ln, font, size, color, "center")
        else:
            simple(c, x, y, ln, font, size, color, "left")
        y -= leading
    return y

def hairline(c, x0, y, x1, color=GOLD, w=0.6):
    c.setStrokeColor(color)
    c.setLineWidth(w)
    c.line(x0, y, x1, y)

# ----------------------------------------------------------------- brand mark
def brand_mark(c, cx, top_y, sq, gap, filled="tr", outline=GOLD, fill=RUST, ow=1.0):
    """2x2 brand mark. cx = left x of left column, top_y = top of top row.
    filled in {'tr','tl','br','bl'} names which square is rust-filled."""
    cols = [cx, cx + sq + gap]
    rows = [top_y - sq, top_y - sq - (sq + gap)]  # y of bottom-left of each row
    cells = {"tl": (cols[0], rows[0]), "tr": (cols[1], rows[0]),
             "bl": (cols[0], rows[1]), "br": (cols[1], rows[1])}
    for key, (x, y) in cells.items():
        if key == filled:
            c.setFillColor(fill)
            c.rect(x, y, sq, sq, stroke=0, fill=1)
        else:
            c.setStrokeColor(outline)
            c.setLineWidth(ow)
            c.rect(x, y, sq, sq, stroke=1, fill=0)

def mini_brand(c):
    """Small brand mark in the top-right of a content header bar."""
    sq, gap = 9.0, 3.0
    right = MR
    left_col = right - sq - gap - sq   # left column x
    top = PH - 43.0
    brand_mark(c, left_col, top, sq, gap, filled="tr", ow=0.9)

# ----------------------------------------------------------------- icons
def icon_square(c, x, y, s):
    c.setFillColor(RUST)
    c.rect(x, y, s, s, stroke=0, fill=1)

def _wm(c, x, y, s, col, w):
    c.setStrokeColor(col)
    c.setLineWidth(w)

def draw_icon(c, kind, x, y, s):
    """White vector glyph inside the rust icon square (x,y = square origin)."""
    icon_square(c, x, y, s)
    c.saveState()
    c.setStrokeColor(WHITE)
    c.setFillColor(WHITE)
    cx, cy = x + s / 2, y + s / 2
    lw = 1.3
    c.setLineWidth(lw)
    if kind == "bars":  # bar chart
        for i, h in enumerate((6, 10, 8, 12)):
            bx = x + 5 + i * 3.6
            c.rect(bx, y + 5, 2.2, h, stroke=0, fill=1)
    elif kind == "grid":  # 2x2 window
        gs = 4.5
        for gx in (cx - gs - 1, cx + 1):
            for gy in (cy - gs - 1, cy + 1):
                c.rect(gx, gy, gs, gs, stroke=1, fill=0)
    elif kind == "swap":  # portability: two horizontal arrows drawn as vectors
        c.line(x + 5, cy + 2.5, x + s - 5, cy + 2.5)
        c.line(x + s - 5, cy + 2.5, x + s - 8, cy + 5)
        c.line(x + s - 5, cy + 2.5, x + s - 8, cy)
        c.line(x + 5, cy - 2.5, x + s - 5, cy - 2.5)
        c.line(x + 5, cy - 2.5, x + 8, cy)
        c.line(x + 5, cy - 2.5, x + 8, cy - 5)
    elif kind == "check":  # checklist
        for i in range(3):
            yy = y + s - 6 - i * 4.5
            c.setLineWidth(1.4)
            c.line(x + 5, yy, x + 7, yy - 2)
            c.line(x + 7, yy - 2, x + 10, yy + 2)
            c.setLineWidth(1.0)
            c.line(x + 12, yy, x + s - 5, yy)
    elif kind == "scale":  # balance / weigh
        c.line(cx, y + 5, cx, y + s - 5)
        c.line(x + 5, y + s - 6, x + s - 5, y + s - 6)
        c.circle(x + 6, y + s - 9, 2.4, stroke=1, fill=0)
        c.circle(x + s - 6, y + s - 9, 2.4, stroke=1, fill=0)
    elif kind == "compass":  # direction / decide
        c.circle(cx, cy, s / 2 - 4.5, stroke=1, fill=0)
        c.setFillColor(WHITE)
        p = c.beginPath()
        p.moveTo(cx, cy + 5)
        p.lineTo(cx + 2.5, cy)
        p.lineTo(cx, cy - 5)
        p.lineTo(cx - 2.5, cy)
        p.close()
        c.drawPath(p, stroke=0, fill=1)
    elif kind == "calendar":  # log / thirty days
        c.rect(x + 5, y + 5, s - 10, s - 11, stroke=1, fill=0)
        c.line(x + 5, y + s - 9, x + s - 5, y + s - 9)
        c.line(x + 8, y + s - 4, x + 8, y + s - 8)
        c.line(x + s - 8, y + s - 4, x + s - 8, y + s - 8)
    elif kind == "card":  # position card / self
        c.rect(x + 4.5, y + 6, s - 9, s - 12, stroke=1, fill=0)
        c.setLineWidth(1.0)
        c.line(x + 8, cy + 1, x + s - 8, cy + 1)
        c.line(x + 8, cy - 3, x + s - 12, cy - 3)
    elif kind == "compare":  # what moved: two arrows up/down
        c.line(cx - 4, y + 5, cx - 4, y + s - 5)
        c.line(cx - 4, y + s - 5, cx - 6.5, y + s - 8)
        c.line(cx - 4, y + s - 5, cx - 1.5, y + s - 8)
        c.line(cx + 4, y + s - 5, cx + 4, y + 5)
        c.line(cx + 4, y + 5, cx + 6.5, y + 8)
        c.line(cx + 4, y + 5, cx + 1.5, y + 8)
    elif kind == "signpost":  # where you go from here
        c.line(cx, y + 5, cx, y + s - 5)
        c.rect(cx, y + s - 12, s / 2 - 6, 5, stroke=1, fill=0)
        c.rect(x + 6, y + s - 19, s / 2 - 6, 5, stroke=1, fill=0)
    elif kind == "book":  # read this / distinctions
        c.line(cx, y + 6, cx, y + s - 6)
        c.rect(x + 5, y + 6, s / 2 - 5, s - 12, stroke=1, fill=0)
        c.rect(cx, y + 6, s / 2 - 5, s - 12, stroke=1, fill=0)
    c.restoreState()

# ----------------------------------------------------------------- chrome
def footer(c, page_no, on_navy=False):
    if on_navy:
        simple(c, MR, FOOTER_TEXT_Y, "%02d" % page_no, FN["DM"], 8.5, GOLD, "right")
        return
    hairline(c, ML, FOOTER_RULE_Y, MR, GOLD, 0.6)
    tracked(c, ML, FOOTER_TEXT_Y, IDENTITY, FN["DM"], 7.2, NAVY, 0.6)
    simple(c, MR, FOOTER_TEXT_Y, "%02d" % page_no, FN["DMSb"], 8.5, NAVY, "right")

def header_bar(c, title, subtitle, icon):
    """Navy full-bleed header bar with rust icon square, white Cormorant title,
    gold subtitle, and the mini brand mark top-right."""
    c.setFillColor(NAVY)
    c.rect(0, PH - HEADER_H, PW, HEADER_H, stroke=0, fill=1)
    isz = 26.0
    iy = PH - 40.0 - isz
    draw_icon(c, icon, ML, iy, isz)
    tx = ML + isz + 14
    simple(c, tx, PH - 54, title, FN["CGSb"], 22, WHITE)
    tracked(c, tx + 1, PH - 71, subtitle, FN["DM"], 9.5, GOLD, 0.2)
    mini_brand(c)

def emphasis(c, y, text, size=13.5, align="left", x=None, max_w=CW):
    """Rust italic Cormorant emphasis line, set on the page, no container."""
    if x is None:
        x = ML if align == "left" else PW / 2
    return para(c, x, y, text, FN["CGSbI"], size, RUST, size + 3.5, max_w, align)

def note(c, y, text, size=9.0, color=NAVY, x=ML, max_w=CW, font=None, leading=None):
    return para(c, x, y, text, font or FN["DM"], size, color,
                leading or (size + 3.5), max_w)

# ----------------------------------------------------------------- boxes
def callout(c, x, y_top, w, h, fill=SAND, border=GOLD, bw=1.0):
    c.setFillColor(fill)
    c.setStrokeColor(border)
    c.setLineWidth(bw)
    c.rect(x, y_top - h, w, h, stroke=1, fill=1)

def total_box(c, y_top, label_text, field_name, h=34.0):
    """Cream box, gold 1.5pt border, navy bold text, field at right."""
    callout(c, ML, y_top, CW, h, fill=SAND, border=GOLD, bw=1.5)
    cy = y_top - h / 2
    simple(c, ML + 16, cy - 4, label_text, FN["DMSb"], 11, NAVY)
    fw, fh = 62, 22
    fx, fy = MR - 16 - fw, cy - fh / 2
    field(c, field_name, fx, fy, fw, fh, computed=True, readonly=True,
          align="center", size=12)
    return y_top - h

# ----------------------------------------------------------------- fields
COMPUTED = {}   # field name -> calculation JS (filled by field(computed=True))

def _sum_js(fields):
    arr = ",".join("'%s'" % f for f in fields)
    return ("var s=0;var F=[%s];for(var i=0;i<F.length;i++){"
            "var v=this.getField(F[i]);if(v){"
            "var t=(v.value+'').replace(/[^0-9.\\-]/g,'');"
            "var x=parseFloat(t);if(!isNaN(x))s+=x;}}event.value=s;") % arr

# source-field lists for the computed totals
SUM_SRC = {
    "dens_initial": ["d1_1", "d1_2", "d1_3", "d1_4", "d1_5", "d1_6"],
    "opt_initial": ["d1_7", "d1_8", "d1_9", "d1_10", "d1_11", "d1_12"],
    "dens_corr": ["d2_1", "d2_2", "d2_3", "d2_4", "d2_5", "d2_6"],
    "opt_corr": ["d2_7", "d2_8", "d2_9", "d2_10", "d2_11", "d2_12"],
    "dens_initial_copy": ["d1_1", "d1_2", "d1_3", "d1_4", "d1_5", "d1_6"],
    "opt_initial_copy": ["d1_7", "d1_8", "d1_9", "d1_10", "d1_11", "d1_12"],
    "dens_initial_r": ["d1_1", "d1_2", "d1_3", "d1_4", "d1_5", "d1_6"],
    "opt_initial_r": ["d1_7", "d1_8", "d1_9", "d1_10", "d1_11", "d1_12"],
    "dens_corr_r": ["d2_1", "d2_2", "d2_3", "d2_4", "d2_5", "d2_6"],
    "opt_corr_r": ["d2_7", "d2_8", "d2_9", "d2_10", "d2_11", "d2_12"],
}

FIELD_COUNT = {"text": 0, "check": 0}

def field(c, name, x, y, w, h, multiline=False, computed=False, readonly=False,
          align="left", size=10.0):
    flags = []
    if multiline:
        flags.append("multiline")
    if readonly:
        flags.append("readOnly")
    tcol = NAVY
    c.acroForm.textfield(
        name=name, x=x, y=y, width=w, height=h,
        borderStyle="solid", borderWidth=FIELD_BW, borderColor=FIELD_BORDER,
        fillColor=FIELD_FILL, textColor=tcol, forceBorder=True,
        fontName="Helvetica", fontSize=size,
        fieldFlags=" ".join(flags) if flags else 0,
        annotationFlags="print",
    )
    FIELD_COUNT["text"] += 1
    if computed:
        COMPUTED[name] = _sum_js(SUM_SRC[name])

def checkbox(c, name, x, y, s=12.0):
    c.acroForm.checkbox(
        name=name, x=x, y=y, size=s, checked=False, buttonStyle="check",
        borderStyle="solid", borderWidth=FIELD_BW, borderColor=FIELD_BORDER,
        fillColor=FIELD_FILL, textColor=NAVY, forceBorder=True,
        annotationFlags="print",
    )
    FIELD_COUNT["check"] += 1

def score_field(c, name, x, y, w=40, h=20):
    field(c, name, x, y, w, h, align="center", size=11)

# ----------------------------------------------------------------- matrix
STATES = [
    ("DEPTH TRAP", "Deep expertise fused to one context.", "tl"),
    ("COMPOUNDING", "Deep capability that travels.", "tr"),
    ("STAGNANT", "The work stopped asking more of you.", "bl"),
    ("FRAGILE", "Options on paper, not enough depth beneath.", "br"),
]

def matrix(c, y_top, cbnames, cell_w=234, cell_h=104):
    """2x2 placement grid with a checkbox in each cell.
    cbnames = dict pos->field name, pos in {'tl','tr','bl','br'}."""
    gx = ML
    gy_top = y_top
    positions = {
        "tl": (gx, gy_top - cell_h),
        "tr": (gx + cell_w, gy_top - cell_h),
        "bl": (gx, gy_top - 2 * cell_h),
        "br": (gx + cell_w, gy_top - 2 * cell_h),
    }
    for state, desc, pos in STATES:
        x, y = positions[pos]
        is_comp = (pos == "tr")
        c.setFillColor(RUST if is_comp else SAND)
        c.rect(x, y, cell_w, cell_h, stroke=0, fill=1)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.0)
        c.rect(x, y, cell_w, cell_h, stroke=1, fill=0)
        txt_col = WHITE if is_comp else NAVY
        simple(c, x + cell_w / 2, y + cell_h - 40, state, FN["DMB"], 12.5, txt_col, "center")
        para(c, x + 24, y + cell_h - 58, desc, FN["DM"], 8.8,
             txt_col, 11, cell_w - 48, "center") if False else \
            _center_desc(c, x, y, cell_w, cell_h, desc, txt_col)
        # checkbox top-left of cell
        checkbox(c, cbnames[pos], x + 12, y + cell_h - 26, 13)
    # axis labels
    label(c, gx, gy_top + 8, "DENSITY:  HIGH AT TOP,  LOW AT BOTTOM", 7.5, GOLD_DEEP, 1.0)
    label(c, gx, gy_top - 2 * cell_h - 15,
          "OPTIONALITY:  LOW AT LEFT   to   HIGH AT RIGHT", 7.5, GOLD_DEEP, 1.0)
    return gy_top - 2 * cell_h - 15

def _center_desc(c, x, y, cw, ch, desc, col):
    lines = wrap_lines(desc, FN["DM"], 8.8, cw - 44)
    yy = y + ch - 56
    for ln in lines:
        simple(c, x + cw / 2, yy, ln, FN["DM"], 8.8, col, "center")
        yy -= 11

# =================================================================== PAGES
def page_cover(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)
    # inset gold hairline frame
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.0)
    c.rect(30, 30, PW - 60, PH - 60, stroke=1, fill=0)
    # brand mark (large), top-left
    brand_mark(c, 72, PH - 150, 30, 6, filled="tr", ow=1.4)
    # category small caps
    label(c, 72, PH - 330, "A LIVE CAPABILITY POSITION READ", 10.5, GOLD, 3.2)
    # title, big white Cormorant, two lines
    simple(c, 70, PH - 386, "Should I Stay", FN["CGB"], 46, WHITE)
    simple(c, 70, PH - 444, "or Should I Move?", FN["CGB"], 46, WHITE)
    # rust short rule
    c.setStrokeColor(RUST)
    c.setLineWidth(2.4)
    c.line(72, PH - 466, 72 + 150, PH - 466)
    # gold italic standfirst
    simple(c, 72, PH - 492, "Read what your current work is building before you decide.",
           FN["CGI"], 16, GOLD)
    # body window line
    para(c, 72, PH - 520,
         "Bring the last ninety days of your actual working life. Every score in this "
         "workbook is made against that window and nothing else.",
         FN["DM"], 10, SAND, 15, 456)
    # name / date fields
    fy = PH - 600
    label(c, 72, fy + 26, "YOUR NAME", 8.5, GOLD, 1.6)
    field(c, "name", 72, fy, 232, 24, size=11)
    label(c, 334, fy + 26, "DATE", 8.5, GOLD, 1.6)
    field(c, "date", 334, fy, 206, 24, size=11)
    # author block
    simple(c, 72, PH - 664, "Temidayo Afonja", FN["CGSb"], 15, WHITE)
    simple(c, 72, PH - 680, "Founder, The Density Group.  Author, The Capability Audit.",
           FN["DM"], 9.5, GOLD)
    # version line
    tracked(c, 72, PH - 712,
            "CAPABILITY FORMATION INSTRUMENT VERSION 1.1   ·   WORKBOOK V5.0   ·   FILLABLE",
            FN["DM"], 8, GOLD_DEEP, 1.0)
    # fillable notice
    label(c, 72, PH - 736, "THIS IS A FILLABLE DOCUMENT", 8.5, GOLD, 1.6)
    para(c, 72, PH - 750,
         "Type directly into every field. Your two axis totals calculate themselves as "
         "you score. Save a copy when you are done.",
         FN["DM"], 9, SAND, 13, 456)
    footer(c, 1, on_navy=True)

def page_opener(c, n, word, standfirst, page_no):
    c.setFillColor(NAVY)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)
    brand_mark(c, 72, PH - 236, 26, 6, filled="tr", ow=1.4)
    label(c, 74, PH - 330, "SECTION %d" % n, 11, GOLD, 4.0)
    simple(c, 72, PH - 384, word, FN["CGB"], 40, WHITE)
    para(c, 72, PH - 414, standfirst, FN["CGI"], 15.5, GOLD, 20, 470)
    footer(c, page_no, on_navy=True)

def page_before(c, pno):
    header_bar(c, "Before you start", "Read this page while people are arriving.", "book")
    y = CONTENT_TOP
    y = note(c, y,
        "This session will not tell you to stay or leave. It will help you read what your "
        "current environment is building in you, what remains portable, and what category "
        "of move your evidence supports testing.", 10.5, NAVY, ML, CW, leading=15.5)
    y -= 6
    y = note(c, y, "What you score today is a position you occupy, and positions change.",
             10.5, NAVY, ML, CW, font=FN["DMMed"], leading=15.5)
    y -= 20
    label(c, ML, y, "HOW THE NEXT HUNDRED AND FIVE MINUTES WORK", 9, GOLD_DEEP, 1.6)
    y -= 22
    steps = [
        ("Initial read", "You score all twelve statements as you read them today. No evidence "
         "required yet. This is your uncalibrated baseline."),
        ("Calibration", "The evidence protocol, the three ways capable people misread their own "
         "position, and the correction map."),
        ("Evidence-backed read", "You score all twelve again, this time with evidence in both "
         "directions. You keep the first number."),
        ("Decide", "Re-total, place yourself again, and write your Next-Move Decision."),
    ]
    for i, (head, body) in enumerate(steps, 1):
        simple(c, ML, y - 2, str(i), FN["CGB"], 20, RUST)
        simple(c, ML + 30, y, head, FN["DMSb"], 10.5, NAVY)
        yy = note(c, y - 15, body, 10, NAVY, ML + 30, CW - 30, leading=14)
        y = yy - 12
    y -= 4
    callout(c, ML, y, CW, 52)
    para(c, ML + 16, y - 16,
         "Your first score is not a test you can fail. It is the reading you would have carried "
         "into a decision this week if you had never come here. That is exactly why it is worth "
         "capturing before anything corrects it.",
         FN["DMI"], 9.5, NAVY, 13.5, CW - 32)
    y -= 52 + 20
    label(c, ML, y, "A NOTE ON THIS SESSION", 9, GOLD_DEEP, 1.6)
    y -= 16
    y = note(c, y,
        "This is a founding pilot, and you are helping refine the delivery and evidence process. "
        "The instrument itself is frozen at Version 1.1 and is not being changed by this room. "
        "Room-level counts are recorded with no names and no totals. Nothing you write in this "
        "workbook is collected. Thirty days from now you will get one short set of questions about "
        "what actually happened, and answering it is optional.", 9.5, NAVY, ML, CW, leading=14)
    y -= 16
    emphasis(c, y,
        "This read informs a career decision. It does not replace financial, legal, medical, "
        "immigration, contractual, or family judgment.", 13, "left", ML, CW)
    footer(c, pno)

STATEMENTS_D = [
    "In the last ninety days I have been handed a problem I did not already know how to solve.",
    "I work close enough to people who are better than me that I can watch how they think.",
    "My work is reviewed by someone who can tell the difference between good and adequate, and who says so directly.",
    "The feedback I receive changes what I do next, not just how I feel.",
    "I regularly operate at the edge of my competence rather than the comfortable center of it.",
    "Looking back six months, the work I do now would have been genuinely hard for me then.",
]
STATEMENTS_O = [
    "The capability I am building would be valued by an employer in a different industry.",
    "I can describe what I do in terms of outcomes, not just my company's internal language.",
    "If my role disappeared tomorrow, the capability I built would still be mine to carry.",
    "People with the power to hire or advance me, inside or outside my company, can already see what I am good at.",
    "What I am learning is a transferable capability rather than a company-specific procedure.",
    "I could rebuild a strong position somewhere else within a year.",
]

def _pass_one(c, pno, title, sub, axis_word, statements, start_no, fields, total_name, total_label):
    header_bar(c, title, sub, "bars")
    y = CONTENT_TOP + 6
    y = note(c, y,
        "Score 1 strongly disagree to 5 strongly agree, against the last ninety days you "
        "actually lived. Type a number in each box. No evidence line yet, and that is deliberate.",
        9.5, NAVY, ML, CW - 70, font=FN["DMI"], leading=13.5)
    y -= 14
    row_h = 66
    for i, stmt in enumerate(statements):
        num = start_no + i
        simple(c, ML, y - 2, str(num), FN["CGB"], 19, RUST)
        stmt_y = note(c, y, stmt, 10.5, NAVY, ML + 30, CW - 30 - 70, leading=14)
        # score label + field at right
        label(c, MR - 60, y + 12, "1 - 5", 7.5, GOLD_DEEP, 1.2, align="left")
        score_field(c, fields[i], MR - 40, y - 6, 40, 20)
        y = min(stmt_y, y - 30) - row_h + 30
    y -= 6
    total_box(c, y, total_label, total_name)
    y -= 34 + 14
    note(c, y, "19 to 30 is high on this axis. 6 to 18 is low.", 9, NAVY, ML, CW, font=FN["DMMed"])
    note(c, y - 14, "Any score between 17 and 21 is a boundary, even a high one.",
         9, NAVY, ML, CW)
    footer(c, pno)

def page_pass_one_density(c, pno):
    _pass_one(c, pno, "Your initial read",
              "Density. Learning velocity, whether this environment is still forming you.",
              "Density", STATEMENTS_D, 1,
              ["d1_1", "d1_2", "d1_3", "d1_4", "d1_5", "d1_6"],
              "dens_initial", "Add the six answers.  Density, initial (out of 30):")

def page_pass_one_opt(c, pno):
    _pass_one(c, pno, "Your initial read",
              "Optionality. Market portability, whether what you built is yours to carry.",
              "Optionality", STATEMENTS_O, 7,
              ["d1_7", "d1_8", "d1_9", "d1_10", "d1_11", "d1_12"],
              "opt_initial", "Add the six answers.  Optionality, initial (out of 30):")

def page_first_placement(c, pno):
    header_bar(c, "First placement",
               "Your initial read, placed. The position you were carrying when you walked in.",
               "grid")
    y = CONTENT_TOP + 4
    # two carried totals
    label(c, ML, y, "DENSITY, INITIAL", 8.5, GOLD_DEEP, 1.4)
    field(c, "dens_initial_copy", ML, y - 30, 62, 22, computed=True, readonly=True,
          align="center", size=12)
    simple(c, ML + 70, y - 24, "/ 30", FN["DMMed"], 11, NAVY)
    label(c, ML + 258, y, "OPTIONALITY, INITIAL", 8.5, GOLD_DEEP, 1.4)
    field(c, "opt_initial_copy", ML + 258, y - 30, 62, 22, computed=True, readonly=True,
          align="center", size=12)
    simple(c, ML + 328, y - 24, "/ 30", FN["DMMed"], 11, NAVY)
    y -= 58
    ybot = matrix(c, y, {"tl": "p1_DepthTrap", "tr": "p1_Compounding",
                         "bl": "p1_Stagnant", "br": "p1_Fragile"}, cell_h=122)
    y = ybot - 34
    label(c, ML, y, "TICK YOUR SQUARE ABOVE, THEN COMPLETE THESE", 8.5, GOLD_DEEP, 1.4)
    y -= 30
    label(c, ML, y, "MY INITIAL STATE", 8, GOLD_DEEP, 1.3)
    field(c, "state1", ML, y - 28, 222, 24, size=11)
    label(c, ML + 262, y, "CONFIDENCE IN THAT PLACEMENT, 1 TO 5", 8, GOLD_DEEP, 1.3)
    field(c, "conf1", ML + 262, y - 28, 44, 24, align="center", size=11)
    y -= 28 + 30
    note(c, y,
         "19 to 30 is high on an axis. 6 to 18 is low. Any score between 17 and 21 is a boundary, "
         "even a high one, and you read both neighbouring states. Hold this placement lightly: you "
         "will do it again, on different numbers, in about forty minutes.",
         9.5, NAVY, ML, CW, leading=14.5)
    footer(c, pno)

def page_distinctions(c, pno):
    header_bar(c, "Read this before you go further",
               "Four distinctions. Each one changes how the square should be read.", "book")
    y = CONTENT_TOP + 4
    items = [
        ("Performance and formation are different readings",
         "Performance measures what you delivered for somebody else. Formation measures what the "
         "work is doing to you. Strong reviews and flat formation are routine companions."),
        ("State is not identity",
         "A current condition rather than a personality type or a permanent address. People move "
         "between squares."),
        ("Exposure is not ability",
         "A low Optionality score measures who has seen the work rather than what the work is worth."),
        ("Your first score is not wrong",
         "It is uncalibrated. Those are different things, and the uncalibrated read is what "
         "everybody carries into a decision until something corrects it."),
    ]
    y = CONTENT_TOP - 4
    for head, body in items:
        simple(c, ML, y, head, FN["CGSb"], 17, NAVY)
        y -= 24
        y = note(c, y, body, 10.5, NAVY, ML, CW, leading=15.5)
        y -= 22
        hairline(c, ML, y, MR, GOLD, 0.5)
        y -= 52
    y -= 8
    emphasis(c, y,
        "This is not a performance rating, a potential rating, or a nine-box grid. It reads your "
        "conditions, not your worth to an employer.", 15.5, "left", ML, CW)
    footer(c, pno)

def page_evidence_protocol(c, pno):
    header_bar(c, "The evidence protocol",
               "Calibration begins here. This is what your second reading has to survive.", "check")
    y = CONTENT_TOP + 4
    y = note(c, y,
        "Every corrected score requires an evidence line from the last ninety days. Every score, "
        "in both directions.", 11.5, NAVY, ML, CW, font=FN["DMSb"], leading=15.5)
    y -= 22
    bands = [
        ("A 4 or 5", "At least one clear positive instance from within the window."),
        ("A 3", "The mixed or inconsistent pattern. A 3 is a reading, not an absence of one."),
        ("A 1 or 2", "What repeatedly happened instead, a relevant counterexample, or a statement "
         "that no qualifying instance occurred across the window."),
    ]
    for head, body in bands:
        simple(c, ML, y, head, FN["DMB"], 11, RUST)
        y = note(c, y - 15, body, 10, NAVY, ML + 14, CW - 14, leading=14) - 20
    y -= 4
    cbh = 74
    callout(c, ML, y, CW, cbh)
    label(c, ML + 16, y - 18, "WHEN YOU CANNOT SUPPORT IT EITHER WAY", 8.5, GOLD_DEEP, 1.4)
    para(c, ML + 16, y - 34,
         "Write your most defensible number and put a question mark after it: 3?, 4?, 2?. Do not "
         "force the number downward and do not default to a 3. A 3 means mixed. A question mark "
         "means unsupported. Those are different findings.",
         FN["DM"], 9.5, NAVY, 13.5, CW - 32)
    y -= cbh + 24
    for head, body in [
        ("One or two marked items on an axis",
         "The axis and your placement are provisional. You will run a quick check on the next "
         "round to see whether the uncertainty changes anything."),
        ("Three or more on one axis",
         "That axis is incomplete and you will not place on it. That is a finding about what the "
         "last ninety days contained, not a low score."),
    ]:
        simple(c, ML, y, head, FN["DMSb"], 10.5, NAVY)
        y = note(c, y - 15, body, 9.5, NAVY, ML + 14, CW - 14, leading=13.5) - 22
    y -= 8
    emphasis(c, y, "A score without an evidence line is a guess with decimal points.", 15.5)
    footer(c, pno)

def page_correction_map(c, pno):
    header_bar(c, "What has to change before you score again",
               "Tick the ones you recognise in your own scoring.", "swap")
    y = CONTENT_TOP + 2
    label(c, ML + 34, y, "ENTERING BELIEF", 8, GOLD_DEEP, 1.3)
    label(c, ML + 34 + 250, y, "EXITING BELIEF", 8, GOLD_DEEP, 1.3)
    y -= 26
    pairs = [
        ('"The work is demanding, so I must be growing."',
         '"A demanding role can stop forming me and still feel full."'),
        ('"I would have options if I decided to look."',
         '"Options depend on whether people outside can already see what I am good at."'),
        ('"This is what my role gives me."', '"I scored the ninety days I actually lived."'),
        ('"They rely on me here."', '"Being needed and being formed are separate conditions."'),
        ('"A low score means I am not good enough."',
         '"A low Optionality score is a fact about exposure."'),
    ]
    cbnames = ["corr0", "corr1", "corr2", "corr3", "corr4"]
    col_w = 232
    for i, (a, b) in enumerate(pairs):
        checkbox(c, cbnames[i], ML, y - 11, 14)
        ya = note(c, y, a, 10.5, NAVY, ML + 34, col_w - 20, font=FN["DMI"], leading=14.5)
        yb = note(c, y, b, 10.5, NAVY, ML + 34 + 250, col_w - 10, font=FN["DMMed"], leading=14.5)
        y = min(ya, yb) - 30
        if i < len(pairs) - 1:
            hairline(c, ML, y + 12, MR, GOLD, 0.4)
            y -= 20
    y -= 16
    callout(c, ML, y, CW, 54)
    para(c, ML + 16, y - 19,
         "Now score all twelve again, on the next four pages. Do not look back at your first "
         "numbers while you do it, and do not change them. The pair is the finding.",
         FN["DMMed"], 10, NAVY, 14.5, CW - 32)
    footer(c, pno)

def _pass_two(c, pno, sub, trip, dfields, efields):
    header_bar(c, "Evidence-backed read", sub, "bars")
    y = CONTENT_TOP - 6
    for i in range(3):
        num = trip[i]
        stmt = (STATEMENTS_D + STATEMENTS_O)[num - 1]
        simple(c, ML, y - 2, str(num), FN["CGB"], 20, RUST)
        ystmt = note(c, y, stmt, 10.5, NAVY, ML + 30, CW - 30 - 74, leading=14)
        label(c, MR - 44, y + 14, "CORRECTED", 7.5, GOLD_DEEP, 1.0)
        score_field(c, dfields[i], MR - 44, y - 8, 44, 22)
        y = min(ystmt, y - 22) - 22
        label(c, ML, y, "EVIDENCE FROM THE LAST NINETY DAYS", 8, GOLD_DEEP, 1.3)
        field(c, efields[i], ML, y - 62, CW, 56, multiline=True, size=9.5)
        y -= 62 + 38
    y += 8
    note(c, y,
        "Evidence in both directions. If you cannot support it either way, write the number and "
        "add a question mark.", 9.5, NAVY, ML, CW, font=FN["DMI"], leading=13.5)
    footer(c, pno)

def page_pass_two(c, pno, which):
    cfg = {
        9:  ("Density, statements 1 to 3.", [1, 2, 3], ["d2_1", "d2_2", "d2_3"], ["ev_1", "ev_2", "ev_3"]),
        10: ("Density, statements 4 to 6.", [4, 5, 6], ["d2_4", "d2_5", "d2_6"], ["ev_4", "ev_5", "ev_6"]),
        11: ("Optionality, statements 7 to 9.", [7, 8, 9], ["d2_7", "d2_8", "d2_9"], ["ev_7", "ev_8", "ev_9"]),
        12: ("Optionality, statements 10 to 12.", [10, 11, 12], ["d2_10", "d2_11", "d2_12"], ["ev_10", "ev_11", "ev_12"]),
    }[which]
    _pass_two(c, pno, cfg[0], cfg[1], cfg[2], cfg[3])

def page_retotal(c, pno):
    header_bar(c, "Re-total and place again",
               "New numbers. A fresh placement, not a review of the first one.", "grid")
    y = CONTENT_TOP + 2
    label(c, ML, y, "DENSITY, CORRECTED  ( AUTO )", 8.5, GOLD_DEEP, 1.3)
    field(c, "dens_corr", ML, y - 28, 62, 22, computed=True, readonly=True, align="center", size=12)
    simple(c, ML + 70, y - 22, "/ 30", FN["DMMed"], 11, NAVY)
    label(c, ML + 258, y, "OPTIONALITY, CORRECTED  ( AUTO )", 8.5, GOLD_DEEP, 1.3)
    field(c, "opt_corr", ML + 258, y - 28, 62, 22, computed=True, readonly=True, align="center", size=12)
    simple(c, ML + 328, y - 22, "/ 30", FN["DMMed"], 11, NAVY)
    y -= 46
    # sensitivity check
    callout(c, ML, y, CW, 118, fill=SAND, border=GOLD, bw=1.0)
    yy = y - 15
    label(c, ML + 14, yy, "IF AN AXIS CARRIES ONE OR TWO QUESTION MARKS, RUN THIS CHECK BEFORE YOU PLACE",
          7.6, GOLD_DEEP, 1.0)
    yy -= 16
    checks = [
        "Total the axis using the numbers exactly as you wrote them.",
        "Total it again with every marked item one point lower.",
        "Total it again with every marked item one point higher.",
        "If all three totals stay on the same side of 19, and none lands between 17 and 21, place "
        "yourself and mark the placement provisional.",
        "If they do not, do not pick one square. Read both neighbouring states.",
    ]
    for i, ck in enumerate(checks, 1):
        simple(c, ML + 14, yy - 1, str(i), FN["CGB"], 12, RUST)
        yy = note(c, yy, ck, 9, NAVY, ML + 30, CW - 44, leading=12) - 3
    y -= 118 + 16
    ybot = matrix(c, y, {"tl": "p2_DepthTrap", "tr": "p2_Compounding",
                         "bl": "p2_Stagnant", "br": "p2_Fragile"}, cell_h=92)
    y = ybot - 24
    label(c, ML, y, "MY CORRECTED STATE", 7.5, GOLD_DEEP, 1.2)
    field(c, "state2", ML, y - 24, 154, 20, size=10.5)
    label(c, ML + 174, y, "CORRECTED CONFIDENCE, 1 TO 5", 7.5, GOLD_DEEP, 1.2)
    field(c, "conf2", ML + 174, y - 24, 44, 20, align="center", size=10.5)
    label(c, ML + 336, y, "DATE OF THIS READ", 7.5, GOLD_DEEP, 1.2)
    field(c, "readdate", ML + 336, y - 24, 162, 20, size=10.5)
    y -= 24 + 20
    note(c, y,
         "Three or more marked items on one axis: that axis is incomplete and you do not place on "
         "it today. It means the last ninety days did not contain enough evidence to read that "
         "axis, usually a period of leave, a transition, or a role you had only just started. That "
         "is worth knowing before you make a decision on it.", 8.5, NAVY, ML, CW, leading=12.5)
    footer(c, pno)

def page_what_moved(c, pno):
    header_bar(c, "What moved",
               "Both readings side by side. Fill this in immediately after your second placement.",
               "compare")
    y = CONTENT_TOP + 4
    # comparison table
    col_label_x = ML
    col_i_x = ML + 180
    col_c_x = ML + 348
    col_w = 138
    label(c, col_i_x, y, "INITIAL", 8, GOLD_DEEP, 1.3)
    label(c, col_c_x, y, "CORRECTED", 8, GOLD_DEEP, 1.3)
    y -= 8
    rows = [
        ("Density", "dens_initial_r", "dens_corr_r", True),
        ("Optionality", "opt_initial_r", "opt_corr_r", True),
        ("State", "state1_r", "state2_r", False),
        ("Confidence", "conf1_r", "conf2_r", False),
    ]
    rh = 34
    for name, fi, fc, comp in rows:
        hairline(c, ML, y - 2, MR, GOLD, 0.4)
        simple(c, col_label_x, y - 22, name, FN["DMSb"], 11, NAVY)
        field(c, fi, col_i_x, y - 27, col_w, 22,
              computed=comp, readonly=comp, size=10.5)
        field(c, fc, col_c_x, y - 27, col_w, 22,
              computed=comp, readonly=comp, size=10.5)
        y -= rh
    hairline(c, ML, y - 2, MR, GOLD, 0.4)
    y -= 22
    reflect = [
        ("THE STATEMENT I OVERRATED, AND THE EVIDENCE I COULD NOT NAME", "ov"),
        ("THE STATEMENT I UNDERRATED, AND WHY I SCORED IT LOW", "un"),
        ("THE ITEMS I MARKED WITH A QUESTION MARK, AND WHAT THAT TELLS ME ABOUT THE WINDOW", "qm"),
    ]
    for lab, fn in reflect:
        label(c, ML, y, lab, 8, GOLD_DEEP, 1.2)
        field(c, fn, ML, y - 42, CW, 36, multiline=True, size=9.5)
        y -= 42 + 20
    y -= 4
    y = note(c, y,
         "You are comparing your first and corrected readings and examining what, if anything, "
         "moved. Nothing about your working life changed while you were scoring. Only the reading did.",
         9.5, NAVY, ML, CW, leading=13.5)
    y -= 22
    emphasis(c, y,
        "A self-score cannot tell you whether you scored yourself accurately. That is a property "
        "of self-assessment rather than a flaw in you.", 14, "left", ML, CW)
    footer(c, pno)

def page_state_costs(c, pno):
    header_bar(c, "What each state costs",
               "A short reference. Read your own square before you write the next page.", "scale")
    y = CONTENT_TOP + 6
    cards = [
        ("DEPTH TRAP", "Value legible inside one building, close to illegible outside it.",
         '"They could never replace me here."', False),
        ("COMPOUNDING", "Results live in internal language, so the organisation decides what they "
         "are worth.", '"I am doing well, so this square has nothing to tell me."', True),
        ("STAGNANT", "The clock is running and nothing is accruing on either axis.",
         '"I am well regarded here."', False),
        ("FRAGILE", "Portable now, on capability that is thinning, and the market has not noticed yet.",
         '"I could leave tomorrow."', False),
    ]
    cw, ch = 246, 176
    vgap = 20
    gap = CW - 2 * cw
    positions = [(ML, y - ch), (ML + cw + gap, y - ch),
                 (ML, y - 2 * ch - vgap), (ML + cw + gap, y - 2 * ch - vgap)]
    for (name, cost, quote, is_comp), (x, yb) in zip(cards, positions):
        c.setFillColor(RUST if is_comp else NAVY)
        c.rect(x, yb, cw, ch, stroke=0, fill=1)
        simple(c, x + 18, yb + ch - 30, name, FN["DMB"], 12.5, WHITE)
        label(c, x + 18, yb + ch - 52, "IMMEDIATE COST", 7.2, GOLD, 1.2)
        yy = para(c, x + 18, yb + ch - 68, cost, FN["DM"], 9.3, WHITE, 13.5, cw - 34)
        label(c, x + 18, yy - 6, "FALSE REASSURANCE", 7.2, GOLD, 1.2)
        para(c, x + 18, yy - 22, quote, FN["CGI"], 11, SAND, 13.5, cw - 34)
    y = y - 2 * ch - vgap - 26
    y = note(c, y,
         "The fuller version is already yours. Section 5 of your Field Kit, the Standing-Still "
         "Worksheet, works this properly: the learning gap, the translation gap, and the exposure, "
         "with rough numbers where they fit and a worked example. Use it in the next thirty days. "
         "This page is the in-session reference, not the whole treatment.",
         9.5, NAVY, ML, CW, leading=14)
    y -= 22
    emphasis(c, y, "No state is a verdict, and no state prescribes a move.", 15.5)
    footer(c, pno)

def page_my_costs(c, pno):
    header_bar(c, "What my state costs me",
               "Your square. Your words. Not what to do about it, what it takes if nothing changes.",
               "scale")
    y = CONTENT_TOP + 6
    items = [
        ("THE IMMEDIATE COST", "c_imm"),
        ("THE HIDDEN COST", "c_hid"),
        ("THE COST OF WAITING", "c_wait"),
        ("THE FALSE REASSURANCE THAT KEEPS ME HERE", "c_fr"),
    ]
    for lab, fn in items:
        label(c, ML, y, lab, 8.5, GOLD_DEEP, 1.3)
        field(c, fn, ML, y - 62, CW, 54, multiline=True, size=9.5)
        y -= 62 + 24
    y -= 2
    label(c, ML, y, "WHAT ONE MORE QUARTER IN THIS STATE TAKES FROM ME, IN ONE LINE", 8.5, GOLD_DEEP, 1.3)
    field(c, "c_oneline", ML, y - 32, CW, 26, multiline=True, size=10)
    y -= 32 + 30
    emphasis(c, y,
        "Once it has words, standing still stops being background anxiety and becomes a choice you "
        "are making.", 15, "left", ML, CW)
    footer(c, pno)

def page_categories(c, pno):
    header_bar(c, "Seven categories of move",
               "Direction, not a plan. Tick the one your evidence supports.", "compass")
    y = CONTENT_TOP + 4
    cats = [
        ("Remain and deepen", "The formation conditions are real and worth protecting."),
        ("Translate what is built", "The capability exists. The language for it does not."),
        ("Widen exposure", "The work is good and the wrong people have seen it."),
        ("Test portability", "Find out what travels before you need it to."),
        ("Repair formation conditions", "Change the work, not the employer, first."),
        ("Prepare for exit", "The conditions will not repair, and the clock is running."),
        ("Seek an external perspective",
         "The stakes are high, the evidence is incomplete, or your position is near a boundary. "
         "Ask someone with sufficient distance and standing to challenge the read."),
    ]
    names = ["cat0", "cat1", "cat2", "cat3", "cat4", "cat5", "cat6"]
    y = CONTENT_TOP - 2
    for i, (head, body) in enumerate(cats):
        checkbox(c, names[i], ML, y - 12, 14)
        simple(c, ML + 32, y, head, FN["DMSb"], 11.5, NAVY)
        yb = note(c, y - 16, body, 9.8, NAVY, ML + 32, CW - 32, leading=13.5)
        y = yb - 24
        if i < len(cats) - 1:
            hairline(c, ML + 32, y + 10, MR, GOLD, 0.35)
            y -= 14
    y -= 12
    callout(c, ML, y, CW, 54)
    para(c, ML + 16, y - 19,
         "No square prescribes a category. Your evidence, your decision horizon, your constraints, "
         "and your risk tolerance all still apply. Almost every category here needs another person, "
         "which is why the next page asks who.", FN["DM"], 9.5, NAVY, 14, CW - 32)
    footer(c, pno)

def page_nmd(c, pno):
    """The hero page: the strongest page in the document."""
    header_bar(c, "The Next-Move Decision", "Ten lines. This is the page you leave with.", "compass")
    # accent band under header: a thin rust rule spanning content width
    c.setStrokeColor(RUST)
    c.setLineWidth(2.2)
    c.line(ML, PH - HEADER_H - 12, MR, PH - HEADER_H - 12)
    lines = [
        "My corrected state is",
        "The evidence supporting this read is",
        "The assumption I corrected today is",
        "The immediate and hidden cost of remaining unchanged is",
        "The risk of doing nothing for the next ninety days is",
        "The category of move my evidence supports testing is",
        "The first action I will take, and by when, is",
        "The person I will say this to, and by when, is",
        "The evidence that would cause me to revise this decision is",
        "The date I will rescore is",
    ]
    names = ["nmd%d" % i for i in range(1, 11)]
    y = PH - HEADER_H - 34
    row_h = 55
    for i, (prompt, fn) in enumerate(zip(lines, names), 1):
        simple(c, ML, y - 4, "%02d" % i, FN["CGB"], 20, RUST)
        simple(c, ML + 34, y - 2, prompt, FN["DMSb"], 10.5, NAVY)
        field(c, fn, ML + 34, y - 26, CW - 34, 22, size=11)
        hairline(c, ML + 34, y - 33, MR, GOLD, 0.35)
        y -= row_h
    footer(c, pno)

def page_log(c, pno):
    header_bar(c, "Thirty-day evidence log",
               "One line a week. The action, and what actually happened.", "calendar")
    y = CONTENT_TOP + 4
    note(c, y,
         "Line 7 is provisional. Line 9 is what makes it responsible. This page is where you find "
         "out which one was right.", 9.5, NAVY, ML, CW, font=FN["DMI"], leading=13.5)
    y -= 24
    # grid header
    label(c, ML, y, "WEEK", 8, GOLD_DEEP, 1.2)
    label(c, ML + 70, y, "WHAT I DID", 8, GOLD_DEEP, 1.2)
    label(c, ML + 288, y, "WHAT CHANGED, OR WHAT DID NOT", 8, GOLD_DEEP, 1.2)
    y -= 8
    weeks = ["W1", "W2", "W3", "W4"]
    rh = 74
    ca_w, cb_w = 205, 205
    for i, wk in enumerate(weeks):
        hairline(c, ML, y - 2, MR, GOLD, 0.4)
        simple(c, ML, y - 32, wk, FN["CGB"], 17, RUST)
        field(c, "log%da" % i, ML + 70, y - rh + 8, ca_w, rh - 16, multiline=True, size=9.5)
        field(c, "log%db" % i, ML + 288, y - rh + 8, cb_w, rh - 16, multiline=True, size=9.5)
        y -= rh
    hairline(c, ML, y - 2, MR, GOLD, 0.4)
    y -= 26
    label(c, ML, y, "THE DATE I RESCORE", 8, GOLD_DEEP, 1.3)
    field(c, "rescoredate", ML, y - 28, 232, 22, size=10.5)
    label(c, ML + 262, y, "WHERE I RESCORE", 8, GOLD_DEEP, 1.3)
    simple(c, ML + 262, y - 22, "Field Kit, Section 7: the Quarterly Loop", FN["DMSb"], 10, NAVY)
    y -= 28 + 28
    y = note(c, y,
         "Rescore in ninety days using the evidence process in your Field Kit. Section 7, the "
         "Quarterly Loop, is built for exactly this: rescore all twelve, compare statement by "
         "statement rather than totals, re-place, and reset the date.",
         9.5, NAVY, ML, CW, leading=14)
    y -= 22
    emphasis(c, y, "Even in a good quarter. Especially in a good quarter.", 15.5)
    footer(c, pno)

def page_where(c, pno):
    header_bar(c, "Where you go from here",
               "Three things, and they do different jobs. Read the difference before you choose.",
               "signpost")
    y = CONTENT_TOP + 6
    routes = [
        ("Today's live Capability Position Read",
         "What you just did. Twelve statements read twice, corrected against evidence, placed "
         "twice, in a calibrated room.",
         "COMPLETE  ·  THIS WORKBOOK IS THE RECORD"),
        ("The Capability Formation Field Kit",
         "Yours, unlocked today. Section 5 works out what your state costs in your own numbers. "
         "Section 7 is your ninety-day rescore, and it is the tool to use: it runs the same "
         "evidence process you were taught today.",
         "INCLUDED  ·  UNLOCKED TODAY  ·  YOUR RESCORE TOOL"),
        ("The free Diagnostic",
         "The same twelve statements, self-scored and uncalibrated. It is the entry point for "
         "someone who has not been in a room like this one. It is not your rescore tool: you have "
         "been calibrated, and the Field Kit is built to hold that standard.",
         "FREE  ·  FOR SOMEONE YOU WOULD SEND IT TO"),
    ]
    y = CONTENT_TOP + 6
    for i, (head, body, tag) in enumerate(routes, 1):
        simple(c, ML, y - 2, str(i), FN["CGB"], 22, RUST)
        simple(c, ML + 34, y, head, FN["CGSb"], 18, NAVY)
        yb = note(c, y - 21, body, 10.2, NAVY, ML + 34, CW - 34, leading=15.5)
        label(c, ML + 34, yb - 6, tag, 7.8, GOLD_DEEP, 1.2)
        y = yb - 30
        hairline(c, ML, y + 10, MR, GOLD, 0.4)
        y -= 44
    y -= 6
    callout(c, ML, y, CW, 50)
    para(c, ML + 16, y - 18,
         "Next thirty days. One line a week on page 19. You will get one short set of questions on "
         "day thirty, and a rescore reminder on day ninety.",
         FN["DMMed"], 10, NAVY, 14.5, CW - 32)
    y -= 50 + 30
    emphasis(c, y, "You have read your position. The move is the next conversation.", 16)
    footer(c, pno)

# =================================================================== assemble
def build():
    c = canvas.Canvas(OUT, pagesize=(PW, PH))
    c.setTitle("Should I Stay or Should I Move? — Session Workbook")
    c.setAuthor("Temidayo Afonja")
    c.setSubject("A Live Capability Position Read")

    seq = []
    def add(fn):
        seq.append(fn)

    # page number is the position in the final document (openers included)
    pages = [
        page_cover,                                   # 1
        lambda cc, n: page_before(cc, n),             # 2
        ("opener", 1, "Your initial read",
         "Twelve statements, scored against the last ninety days you actually lived. "
         "No evidence yet, and that is deliberate."),
        page_pass_one_density,                        # pass one density
        page_pass_one_opt,
        page_first_placement,
        page_distinctions,
        ("opener", 2, "Calibration",
         "The evidence protocol, the ways capable people misread their own position, and "
         "what has to change before you score again."),
        page_evidence_protocol,
        page_correction_map,
        ("opener", 3, "Evidence-backed read",
         "Score all twelve again, this time with evidence in both directions. "
         "You keep the first number."),
        lambda cc, n: page_pass_two(cc, n, 9),
        lambda cc, n: page_pass_two(cc, n, 10),
        lambda cc, n: page_pass_two(cc, n, 11),
        lambda cc, n: page_pass_two(cc, n, 12),
        page_retotal,
        page_what_moved,
        ("opener", 4, "Decide",
         "Re-total, place yourself again, and write the Next-Move Decision you leave with."),
        page_state_costs,
        page_my_costs,
        page_categories,
        page_nmd,
        page_log,
        page_where,
    ]

    pno = 0
    for item in pages:
        pno += 1
        if isinstance(item, tuple) and item[0] == "opener":
            _, secn, word, standfirst = item
            page_opener(c, secn, word, standfirst, pno)
        elif item is page_cover:
            page_cover(c)
        else:
            item(c, pno)
        c.showPage()
    c.save()
    return pno

def post_pass():
    """Attach calculation JS (builds /CO) and set NeedAppearances."""
    doc = fitz.open(OUT)
    set_calc = 0
    for page in doc:
        for w in page.widgets():
            if w.field_name in COMPUTED:
                w.script_calc = COMPUTED[w.field_name]
                w.update()
                set_calc += 1
    cat = doc.pdf_catalog()
    af = doc.xref_get_key(cat, "AcroForm")
    if af[0] == "xref":
        axref = int(af[1].split()[0])
        doc.xref_set_key(axref, "NeedAppearances", "true")
    doc.saveIncr()
    doc.close()
    return set_calc

if __name__ == "__main__":
    total = build()
    calc = post_pass()
    print("Wrote %s" % OUT)
    print("Pages: %d" % total)
    print("Text fields: %d   Checkboxes: %d   Total: %d"
          % (FIELD_COUNT["text"], FIELD_COUNT["check"],
             FIELD_COUNT["text"] + FIELD_COUNT["check"]))
    print("Computed fields with calc JS attached: %d (expected %d)"
          % (calc, len(COMPUTED)))
    assert calc == len(COMPUTED), "not all computed fields received calc JS"
