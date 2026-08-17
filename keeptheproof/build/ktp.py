#!/usr/bin/env python3
"""Keep the Proof — production engine.

A ReportLab/Platypus build system for the Keep the Proof handbook and the
standalone Career Evidence Ledger. Provides the brand system (Capability
Formation / Temidayo Afonja tokens), page templates (cover, section divider,
content, ledger), and custom flowables (callouts, before/after tables, example
cards, fillable form rows). US Letter portrait. Brand fonts embedded.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, Flowable, NextPageTemplate, PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")

# ---- palette -------------------------------------------------------------
NAVY   = HexColor("#0F2347")
CREAM  = HexColor("#F5F0E8")
PAPER  = HexColor("#FBF8F2")   # slightly lighter cream for page ground
GOLD   = HexColor("#C9A84C")
RUST   = HexColor("#C1440E")
BLUE   = HexColor("#2C5282")   # mid-blue accent (evidence motif)
INK    = HexColor("#26313F")   # near-navy body ink on light
MUTE   = HexColor("#5A6B82")   # secondary text
HAIR   = HexColor("#D9CBB2")   # hairline on cream
FIELDBG= HexColor("#FFFFFF")
CREAMSOFT = HexColor("#C9C7C0")

PAGE_W, PAGE_H = letter    # 612 x 792
MARGIN = 66
CONTENT_W = PAGE_W - 2*MARGIN

# ---- fonts ---------------------------------------------------------------
def register_fonts():
    reg = [("CG",       "CormorantGaramond-Medium.ttf"),
           ("CG-Semi",  "CormorantGaramond-SemiBold.ttf"),
           ("CG-Bold",  "CormorantGaramond-Bold.ttf"),
           ("DM",       "DMSans-Regular.ttf"),
           ("DM-Med",   "DMSans-Medium.ttf"),
           ("DM-Bold",  "DMSans-Bold.ttf")]
    for name, fn in reg:
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, fn)))

# ---- paragraph styles ----------------------------------------------------
def styles():
    S = {}
    S["eyebrow"] = ParagraphStyle("eyebrow", fontName="DM-Bold", fontSize=10.5,
        textColor=GOLD, leading=14, spaceAfter=8, tracking=2, keepWithNext=1)
    S["h1"] = ParagraphStyle("h1", fontName="CG-Semi", fontSize=30, textColor=NAVY,
        leading=33, spaceAfter=10)
    S["h2"] = ParagraphStyle("h2", fontName="CG-Semi", fontSize=20, textColor=NAVY,
        leading=24, spaceBefore=16, spaceAfter=7, keepWithNext=1)
    S["h3"] = ParagraphStyle("h3", fontName="DM-Bold", fontSize=11.5, textColor=NAVY,
        leading=15, spaceBefore=12, spaceAfter=4, keepWithNext=1)
    S["body"] = ParagraphStyle("body", fontName="DM", fontSize=10.3, textColor=INK,
        leading=15.6, spaceAfter=8, alignment=TA_LEFT)
    S["body_j"] = ParagraphStyle("body_j", parent=S["body"], alignment=TA_JUSTIFY)
    S["lead"] = ParagraphStyle("lead", fontName="CG", fontSize=14.5, textColor=NAVY,
        leading=20, spaceAfter=10)
    S["bullet"] = ParagraphStyle("bullet", fontName="DM", fontSize=10.3, textColor=INK,
        leading=15.2, spaceAfter=3, leftIndent=16, bulletIndent=2, firstLineIndent=0)
    S["note"] = ParagraphStyle("note", fontName="DM", fontSize=9.4, textColor=MUTE,
        leading=13.4, spaceAfter=5)
    S["callout_t"] = ParagraphStyle("callout_t", fontName="DM-Bold", fontSize=9.5,
        textColor=GOLD, leading=13, spaceAfter=4, tracking=1.5)
    S["callout_b"] = ParagraphStyle("callout_b", fontName="DM", fontSize=10.2,
        textColor=CREAM, leading=15, spaceAfter=6)
    S["callout_b_ink"] = ParagraphStyle("callout_b_ink", fontName="DM", fontSize=10.2,
        textColor=INK, leading=15, spaceAfter=6)
    S["quote"] = ParagraphStyle("quote", fontName="CG", fontSize=16, textColor=NAVY,
        leading=22, spaceAfter=8, alignment=TA_LEFT)
    S["fieldlabel"] = ParagraphStyle("fieldlabel", fontName="DM-Bold", fontSize=8.6,
        textColor=NAVY, leading=11, spaceAfter=2, tracking=0.5)
    S["fieldhint"] = ParagraphStyle("fieldhint", fontName="DM", fontSize=8.0,
        textColor=MUTE, leading=10.5)
    S["tbl_h"] = ParagraphStyle("tbl_h", fontName="DM-Bold", fontSize=8.8,
        textColor=CREAM, leading=12, tracking=0.6)
    S["tbl"] = ParagraphStyle("tbl", fontName="DM", fontSize=9.2, textColor=INK, leading=12.8)
    S["tbl_em"] = ParagraphStyle("tbl_em", fontName="DM-Med", fontSize=9.2, textColor=NAVY, leading=12.8)
    S["kicker"] = ParagraphStyle("kicker", fontName="DM-Bold", fontSize=8.6, textColor=RUST,
        leading=12, tracking=1.4, spaceAfter=3, keepWithNext=1)
    S["footer"] = ParagraphStyle("footer", fontName="DM", fontSize=8, textColor=MUTE, leading=10)
    return S

# apply letter-spacing (ReportLab has no native tracking on ParagraphStyle;
# emulate by setting charSpace via canvas is complex, so we bake spaces into
# all-caps labels manually where needed). Keep tracking attr for reference.

# ---- custom flowables ----------------------------------------------------
class HRule(Flowable):
    def __init__(self, width, color=GOLD, thick=1.2, space=6):
        super().__init__(); self.width=width; self.color=color; self.thick=thick; self.space=space
    def wrap(self, aw, ah): return (self.width, self.thick+self.space)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thick)
        self.canv.line(0, self.space/2, self.width, self.space/2)

class RustTab(Flowable):
    """Short rust rule used as a section accent."""
    def __init__(self, w=54, color=RUST, thick=3):
        super().__init__(); self.w=w; self.color=color; self.thick=thick
    def wrap(self, aw, ah): return (self.w, self.thick+10)
    def draw(self):
        self.canv.setFillColor(self.color); self.canv.rect(0, 6, self.w, self.thick, fill=1, stroke=0)

class Callout(Flowable):
    """Colored box with a left accent bar, a small caps title and body paras.
    bg: 'navy'|'sand'|'blue'. Rendered as a single-cell table for flow safety."""
    pass  # implemented via helper build_callout below (Table-based, splittable-safe)

def _para(text, style):
    return Paragraph(text, style)

def build_callout(title, body_html, S, bg="navy", bar=RUST, width=CONTENT_W):
    if bg == "navy":
        fill = NAVY; tstyle = S["callout_t"]; bstyle = S["callout_b"]
    elif bg == "blue":
        fill = BLUE; tstyle = ParagraphStyle("ct2", parent=S["callout_t"], textColor=CREAM); bstyle = S["callout_b"]
    else:
        fill = CREAM; tstyle = ParagraphStyle("ct3", parent=S["callout_t"], textColor=RUST); bstyle = S["callout_b_ink"]
    inner = []
    if title: inner.append(_para(title, tstyle))
    if isinstance(body_html, str): body_html = [body_html]
    for b in body_html: inner.append(_para(b, bstyle))
    cell = Table([[inner]], colWidths=[width-24])
    cell.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),22),("RIGHTPADDING",(0,0),(-1,-1),16),
        ("TOPPADDING",(0,0),(-1,-1),13),("BOTTOMPADDING",(0,0),(-1,-1),11),
        ("BACKGROUND",(0,0),(-1,-1),fill),("LINEBEFORE",(0,0),(0,-1),5,bar),
    ]))
    outer = Table([[cell]], colWidths=[width])
    outer.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return outer

def build_table(rows, S, col_w, header=True, zebra=True, head_fill=NAVY, align=None, pad=6, cell_style=None):
    """rows: list of lists of strings (HTML). First row = header if header."""
    body_style = cell_style or S["tbl"]
    data = []
    for r_i, row in enumerate(rows):
        cells = []
        for c_i, txt in enumerate(row):
            if header and r_i == 0:
                cells.append(_para(txt, S["tbl_h"]))
            else:
                cells.append(_para(txt, body_style))
        data.append(cells)
    t = Table(data, colWidths=col_w, repeatRows=1 if header else 0)
    cmds = [("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
            ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
            ("LINEBELOW",(0,0),(-1,-1),0.6,HAIR)]
    if header:
        cmds += [("BACKGROUND",(0,0),(-1,0),head_fill),("LINEBELOW",(0,0),(-1,0),0,head_fill),
                 ("TOPPADDING",(0,0),(-1,0),7),("BOTTOMPADDING",(0,0),(-1,0),7)]
    if zebra:
        for i in range(1, len(rows)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND",(0,i),(-1,i),HexColor("#FBF6EC")))
    if align:
        for (c, a) in align: cmds.append(("ALIGN",(c,0),(c,-1),a))
    t.setStyle(TableStyle(cmds))
    return t

# ---- fillable field flowable --------------------------------------------
class Field(Flowable):
    """A single fillable AcroForm text field drawn at flow position.
    height sets the box; multiline wraps. Registers via canvas.acroForm."""
    _seen = set()
    def __init__(self, name, width, height=20, fontsize=9.5, multiline=False,
                 border=GOLD, tab=None):
        super().__init__(); self.name=name; self.width=width; self.height=height
        self.fontsize=fontsize; self.multiline=multiline; self.border=border; self.tab=tab
    def wrap(self, aw, ah): return (self.width, self.height+4)
    def drawOn(self, canvas, x, y, _sW=0):
        # acroForm fields ignore the canvas CTM and place at absolute page
        # coords. When this flowable is nested in a Table, x,y arrive relative
        # to the table's translated canvas, so map (x,y) through the current
        # matrix to recover the true absolute lower-left before placing.
        try:
            a, b, c, d, e, f = canvas._currentMatrix
            ax = a * x + c * y + e
            ay = b * x + d * y + f
        except Exception:
            ax, ay = x, y
        nm = self.name
        if nm in Field._seen:
            k = 2
            while f"{nm}_{k}" in Field._seen: k += 1
            nm = f"{nm}_{k}"
        Field._seen.add(nm)
        canvas.acroForm.textfield(
            name=nm, x=ax, y=ay+2, width=self.width, height=self.height,
            borderStyle="solid", borderWidth=1.0, borderColor=self.border,
            fillColor=FIELDBG, textColor=INK, forceBorder=True,
            fontName="Helvetica", fontSize=self.fontsize,
            fieldFlags=("multiline" if self.multiline else 0),
            annotationFlags="print")
    def draw(self):  # not used (drawOn overridden) but kept for safety
        pass

def field_row(label, name, S, width=CONTENT_W, height=20, hint=None, multiline=False, keep=True):
    flow = [_para(label, S["fieldlabel"])]
    if hint: flow.append(_para(hint, S["fieldhint"]))
    flow.append(Spacer(1, 2))
    flow.append(Field(name, width, height=height, multiline=multiline))
    return KeepTogether(flow) if keep else flow

# ---- document template ---------------------------------------------------
class KTPDoc(BaseDocTemplate):
    def __init__(self, filename, footer_title="Keep the Proof", url="temidayoafonja.com", **kw):
        super().__init__(filename, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=MARGIN, bottomMargin=MARGIN, **kw)
        self.footer_title = footer_title; self.url = url
        self._page_from = 2  # first page (cover) shows no footer
        content_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H-2*MARGIN, id="content",
                              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        full_frame = Frame(0, 0, PAGE_W, PAGE_H, id="full", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[full_frame], onPage=self._cover_bg),
            PageTemplate(id="divider", frames=[Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H-2*MARGIN, id="div")],
                         onPage=self._divider_bg),
            PageTemplate(id="content", frames=[content_frame], onPage=self._content_bg),
        ])
    def _cover_bg(self, canv, doc):
        canv.setFillColor(NAVY); canv.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    def _divider_bg(self, canv, doc):
        canv.setFillColor(NAVY); canv.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        self._footer(canv, doc, light=True)
    def _content_bg(self, canv, doc):
        canv.setFillColor(PAPER); canv.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        self._footer(canv, doc, light=False)
    def _footer(self, canv, doc, light=False):
        pg = canv.getPageNumber()
        if pg < self._page_from: return
        col = CREAMSOFT if light else MUTE
        rulecol = HexColor("#33425A") if light else HAIR
        canv.setStrokeColor(rulecol); canv.setLineWidth(0.6)
        canv.line(MARGIN, 52, PAGE_W-MARGIN, 52)
        canv.setFont("DM", 8); canv.setFillColor(col)
        canv.drawString(MARGIN, 40, f"{self.footer_title}")
        canv.drawCentredString(PAGE_W/2, 40, self.url)
        canv.drawRightString(PAGE_W-MARGIN, 40, str(pg))
        # make the centred URL a working link
        uw = canv.stringWidth(self.url, "DM", 8)
        canv.linkURL(f"https://{self.url}", (PAGE_W/2-uw/2, 38, PAGE_W/2+uw/2, 50), relative=0, thickness=0)

# device: quiet "evidence record" motif — three stacked ledger lines with a
# gold tick. Not the quadrant, not circles.
def record_motif(canv, x, y, w=46, color=GOLD, accent=RUST):
    canv.saveState()
    canv.setLineWidth(2.2); canv.setStrokeColor(color)
    for i in range(3):
        yy = y - i*7
        canv.line(x, yy, x+w*(0.62 if i==1 else 1.0), yy)
    canv.setFillColor(accent); canv.rect(x+w+6, y-14, 7, 20, fill=1, stroke=0)
    canv.restoreState()
