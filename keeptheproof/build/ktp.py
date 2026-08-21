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

# ---- AcroForm appearance hardening (RC4) ---------------------------------
# Every blank text-field appearance ReportLab emits ends with the standard
# variable-text wrapper:  /Tx BMC  q  <x y w h re>  W n  ...  Q  EMC.
# For a *blank* field nothing is painted between the clip and the Q, so that
# interior "<rect> re W n" is a clipping path that clips nothing — a no-op.
# It is the only active graphics-state construct living in the widget
# annotation's appearance layer. Independent field QA reported page 37 of the
# handbook rendering with clipped/shifted top content in whole-document
# Ghostscript and Poppler 26.x while rendering cleanly with annotations
# disabled — i.e. the fault is in the annotation appearance layer, not the page
# content. To remove that entire class of renderer appearance-isolation hazard,
# we strip the no-op interior clip from blank appearance streams. This changes
# no visible pixel (the clip bounds nothing when there is no value to draw) and
# leaves the marked-content and q/Q pairing balanced; every field name, type,
# flag, rectangle, MaxLen, border style and colour is untouched.
from reportlab.pdfbase import acroform as _acroform
import re as _re

_CLIP_RE = _re.compile(r'(/Tx BMC \nq\n)[-\d.]+ [-\d.]+ [-\d.]+ [-\d.]+ re\nW\nn\n')

def _strip_noop_clip(stream_obj):
    old = getattr(stream_obj, "content", None)
    if not isinstance(old, str):
        return stream_obj
    new = _CLIP_RE.sub(r'\1', old)
    if new != old:
        stream_obj.content = new
        ref = getattr(stream_obj, "_af_refstr", None)
        if isinstance(ref, str) and ref.startswith(old):
            stream_obj._af_refstr = new + ref[len(old):]
    return stream_obj

_orig_txAP = _acroform.AcroForm.txAP
def _txAP_hardened(self, *a, **k):
    return _strip_noop_clip(_orig_txAP(self, *a, **k))
if getattr(_acroform.AcroForm.txAP, "__name__", "") != "_txAP_hardened":
    _acroform.AcroForm.txAP = _txAP_hardened

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
        # Save/restore around the widget so no graphics-state change leaks into
        # the surrounding content stream and produces renderer-dependent output.
        canvas.saveState()
        canvas.acroForm.textfield(
            name=nm, x=ax, y=ay+2, width=self.width, height=self.height,
            borderStyle="solid", borderWidth=1.0, borderColor=self.border,
            fillColor=FIELDBG, textColor=INK, forceBorder=True,
            fontName="Helvetica", fontSize=self.fontsize,
            fieldFlags=("multiline" if self.multiline else 0),
            annotationFlags="print")
        canvas.restoreState()
    def draw(self):  # not used (drawOn overridden) but kept for safety
        pass

def field_row(label, name, S, width=CONTENT_W, height=20, hint=None, multiline=False, keep=True):
    flow = []
    if label: flow.append(_para(label, S["fieldlabel"]))
    if hint: flow.append(_para(hint, S["fieldhint"]))
    flow.append(Spacer(1, 2))
    flow.append(Field(name, width, height=height, multiline=multiline))
    return KeepTogether(flow) if keep else flow

def two_up_fields(left, right, S, gap=16):
    """Place two field_row specs side by side as separate AcroForm fields.
    left/right: dict(label, name, height, hint, multiline). Short metadata may
    share a row; this never merges two prompts into one field."""
    w = (CONTENT_W - gap) / 2
    lft = field_row(left["label"], left["name"], S, width=w, height=left.get("height", 22),
                    hint=left.get("hint"), multiline=left.get("multiline", False), keep=False)
    rgt = field_row(right["label"], right["name"], S, width=w, height=right.get("height", 22),
                    hint=right.get("hint"), multiline=right.get("multiline", False), keep=False)
    t = Table([[lft, rgt]], colWidths=[w + gap/2, w + gap/2])
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,0),gap),
        ("RIGHTPADDING",(1,0),(1,0),0),("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),("VALIGN",(0,0),(-1,-1),"TOP")]))
    return t

# ---- canonical reusable forms (identical wording/order/logic in both PDFs) --
# The Quick Capture (five prompts) and the two-page Full Career Evidence Entry
# (twenty taught fields) are defined once so the handbook form and the standalone
# ledger form never drift. The caller supplies its own heading chrome and the
# field-name prefix; suffixes below stay constant so the taught order is fixed.

def quick_capture_fields(S, prefix):
    """The five Quick Capture prompts, one per page. First three hold a full
    200-300 character answer; the verifier and confidential-detail fields hold
    80-140 characters. Every field is true multiline, full page width."""
    P = prefix
    return [
        field_row("What happened?", f"{P}_what", S, height=60, multiline=True,
                  hint="The event or piece of work."),
        Spacer(1, 8),
        field_row("What was my specific contribution or judgment?", f"{P}_contrib", S,
                  height=60, multiline=True, hint="Your part, not the team&#8217;s."),
        Spacer(1, 8),
        field_row("What changed, improved, became possible, or was prevented?", f"{P}_change", S,
                  height=60, multiline=True, hint="The consequence."),
        Spacer(1, 8),
        field_row("Verifier role or permitted public reference", f"{P}_verify", S,
                  height=40, multiline=True,
                  hint="Use a role or public source. Do not store a colleague&#8217;s personal details."),
        Spacer(1, 8),
        field_row("Confidential detail to keep out", f"{P}_out", S, height=40, multiline=True,
                  hint="Name it, so you remember to leave it out."),
    ]

def full_entry_pages(S, prefix):
    """Return three flowable lists for the twenty-field Full Career Evidence
    Entry. Every narrative field is full page width and multiline so a realistic
    120-300 character answer stays visible without scrolling; only genuinely
    short metadata (date/project, retrieval tags) sits on a shared row. None of
    the forbidden combinations are merged into a single field."""
    P = prefix
    def fr(label, suf, height, multiline=False, hint=None):
        return field_row(label, f"{P}_{suf}", S, height=height, multiline=multiline, hint=hint)
    def tu(la, na, ha, ma, lb, nb, hb, mb):
        return two_up_fields({"label":la,"name":f"{P}_{na}","height":ha,"multiline":ma},
                             {"label":lb,"name":f"{P}_{nb}","height":hb,"multiline":mb}, S)
    page_one = [
        tu("Date or period","date",22,False, "Project or work event","proj",22,False),
        Spacer(1,7), fr("Situation or need","sit",52,True),
        Spacer(1,7), fr("Why it mattered","why",52,True),
        Spacer(1,7), fr("Formal responsibility","formal",40,True),
        Spacer(1,7), fr("Actual ownership","actual",40,True),
        Spacer(1,7), fr("Decision or judgment exercised","judge",50,True),
        Spacer(1,7), fr("Actions taken","actions",50,True),
    ]
    page_two = [
        fr("People and functions involved","people",40,True),
        Spacer(1,7), fr("Scope and constraint","scope",40,True),
        Spacer(1,7), fr("Outcome or observable change","outcome",52,True),
        Spacer(1,7), fr("Problem prevented","prevented",52,True),
        Spacer(1,7), fr("Quantitative evidence, accurate and permitted","quant",40,True),
        Spacer(1,7), fr("Qualitative evidence or validation","qual",40,True),
        Spacer(1,7), fr("Team result vs. your honest part","team",50,True),
    ]
    page_three = [
        fr("Internal wording, before translation","internal",46,True),
        Spacer(1,7), fr("Portable-language version","portable",46,True),
        Spacer(1,7), fr("Permitted evidence reference","evref",36,True,
                        hint="Name the permitted source or location. Do not paste the artifact or confidential content here."),
        Spacer(1,7), fr("Confidentiality and permission check","conf",40,True),
        Spacer(1,7), fr("Retrieval tags","tags",26,True,
                        hint="Review, promotion, compensation, resume, interview, biography, transition."),
    ]
    return page_one, page_two, page_three

# ---- PDF outline / bookmarks ---------------------------------------------
class Bookmark(Flowable):
    """Zero-height marker that registers a PDF outline entry at its page.
    Placed in the story just before the section it names."""
    _n = 0
    def __init__(self, title, level=0):
        super().__init__(); self.title=title; self.level=level
        Bookmark._n += 1; self.key = f"bm{Bookmark._n}"
    def wrap(self, aw, ah): return (0, 0)
    def drawOn(self, canvas, x, y, _sW=0):
        canvas.bookmarkPage(self.key)
        canvas.addOutlineEntry(self.title, self.key, self.level, 0)
    def draw(self): pass

# ==========================================================================
# Icon system (RC3). One family of native ReportLab vector marks, shared by the
# handbook and the ledger. No emoji, Unicode, icon font, or raster. Every mark
# saves and restores canvas state, uses palette constants, and draws with round
# caps/joins at a consistent optical weight. Coordinates are the lower-left of an
# s x s box; the caller positions the box.
# ==========================================================================
def _pen(c, col, w):
    c.setStrokeColor(col); c.setFillColor(col)
    c.setLineWidth(w); c.setLineCap(1); c.setLineJoin(1)

def _card(c, x, y, w, h, col, lw, r=None):
    c.setStrokeColor(col); c.setLineWidth(lw); c.setLineCap(1); c.setLineJoin(1)
    c.roundRect(x, y, w, h, r if r is not None else min(w, h)*0.14, stroke=1, fill=0)

def evidence_mark(c, x, y, s=54, card=CREAM, proof=GOLD, accent=RUST):
    """The Keep the Proof product mark: two offset outlined record cards, a short
    gold proof line on the front card, and a small rust tab accent."""
    c.saveState()
    w, h = s*0.74, s*0.60
    off = s*0.17
    _card(c, x+off, y+off, w, h, card, max(1.1, s*0.045))      # back card
    _card(c, x, y, w, h, card, max(1.3, s*0.05))               # front card
    _pen(c, proof, max(1.4, s*0.058))                          # proof line (gold)
    c.line(x+w*0.16, y+h*0.40, x+w*0.70, y+h*0.40)
    _pen(c, card, max(1.0, s*0.038))                           # a shorter line
    c.line(x+w*0.16, y+h*0.63, x+w*0.52, y+h*0.63)
    c.setFillColor(accent); c.setStrokeColor(accent)           # rust tab accent
    tw, th = s*0.075, s*0.20
    c.rect(x-tw*0.5, y+h*0.30, tw, th, fill=1, stroke=0)
    c.restoreState()

def badge(c, x, y, d, icon_fn, fill=RUST, line=CREAM):
    """A rust rounded-square badge with a cream line icon centred inside.
    (x, y) is the lower-left of the d x d badge."""
    c.saveState()
    c.setFillColor(fill); c.setStrokeColor(fill)
    c.roundRect(x, y, d, d, d*0.24, stroke=0, fill=1)
    pad = d*0.22
    icon_fn(c, x+pad, y+pad, d-2*pad, line)
    c.restoreState()

# ---- topical line icons (draw inside an s x s box at (x, y)) --------------
def ic_record_search(c, x, y, s, col):      # card + magnifier (understand / retrieve / index)
    c.saveState(); _pen(c, col, max(1.0, s*0.075))
    cw, ch = s*0.60, s*0.74; cx, cy = x, y+s*0.14
    _card(c, cx, cy, cw, ch, col, max(1.0, s*0.075))
    c.setLineWidth(max(0.8, s*0.055))
    c.line(cx+cw*0.20, cy+ch*0.66, cx+cw*0.80, cy+ch*0.66)
    c.line(cx+cw*0.20, cy+ch*0.45, cx+cw*0.62, cy+ch*0.45)
    r = s*0.17; mx, my = x+s*0.70, y+s*0.28   # magnifier
    c.setLineWidth(max(1.0, s*0.085))
    c.circle(mx, my, r, stroke=1, fill=0)
    c.line(mx+r*0.72, my-r*0.72, x+s*0.98, y+s*0.02)
    c.restoreState()

def ic_shield_check(c, x, y, s, col):        # permission & protection
    c.saveState(); _pen(c, col, max(1.1, s*0.08))
    cx = x+s*0.5; top = y+s*0.94; bot = y+s*0.06
    wsh = s*0.34
    c.bezier(cx-wsh, top, cx-wsh, top, cx-wsh, y+s*0.42, cx, bot)
    c.bezier(cx, bot, cx+wsh, y+s*0.42, cx+wsh, top, cx+wsh, top)
    c.line(cx-wsh, top, cx+wsh, top)
    c.setLineWidth(max(1.2, s*0.10))         # check mark
    c.line(cx-s*0.16, y+s*0.50, cx-s*0.02, y+s*0.36)
    c.line(cx-s*0.02, y+s*0.36, cx+s*0.20, y+s*0.66)
    c.restoreState()

def ic_form_pencil(c, x, y, s, col):         # the tools (form card + pencil)
    c.saveState(); _pen(c, col, max(1.0, s*0.075))
    cw, ch = s*0.62, s*0.82; cx, cy = x, y+s*0.09
    _card(c, cx, cy, cw, ch, col, max(1.0, s*0.075))
    c.setLineWidth(max(0.8, s*0.05))
    for i,fr in enumerate((0.72, 0.54, 0.36)):
        c.line(cx+cw*0.18, cy+ch*fr, cx+cw*(0.82 if i else 0.82), cy+ch*fr)
    c.setLineWidth(max(1.0, s*0.08))         # pencil (diagonal), bottom-right
    px, py = x+s*0.58, y+s*0.06
    c.line(px, py, px+s*0.34, py+s*0.34)
    c.line(px+s*0.30, py+s*0.30, px+s*0.40, py+s*0.40)  # tip
    c.restoreState()

def ic_form_card(c, x, y, s, col):           # structured form card
    c.saveState(); _pen(c, col, max(1.0, s*0.075))
    cw, ch = s*0.74, s*0.88; cx, cy = x+s*0.13, y+s*0.06
    _card(c, cx, cy, cw, ch, col, max(1.0, s*0.075))
    c.setLineWidth(max(0.8, s*0.05))
    for fr in (0.76, 0.58, 0.40, 0.22):
        c.line(cx+cw*0.16, cy+ch*fr, cx+cw*0.84, cy+ch*fr)
    c.restoreState()

def ic_layered_cards(c, x, y, s, col):       # worked examples (layered cards)
    c.saveState(); _pen(c, col, max(1.0, s*0.07))
    w, h = s*0.60, s*0.50
    _card(c, x+s*0.30, y+s*0.34, w, h, col, max(1.0, s*0.06))
    _card(c, x+s*0.14, y+s*0.20, w, h, col, max(1.0, s*0.065))
    _card(c, x, y+s*0.06, w, h, col, max(1.1, s*0.075))
    c.setLineWidth(max(0.8, s*0.05))
    c.line(x+w*0.16, y+s*0.06+h*0.60, x+w*0.72, y+s*0.06+h*0.60)
    c.line(x+w*0.16, y+s*0.06+h*0.36, x+w*0.54, y+s*0.06+h*0.36)
    c.restoreState()

def ic_calendar_arrow(c, x, y, s, col):      # routines / continued use (calendar + loop)
    c.saveState(); _pen(c, col, max(1.0, s*0.075))
    cw, ch = s*0.80, s*0.72; cx, cy = x+s*0.10, y+s*0.10
    _card(c, cx, cy, cw, ch, col, max(1.0, s*0.06))
    c.setLineWidth(max(0.9, s*0.06))
    c.line(cx, cy+ch*0.74, cx+cw, cy+ch*0.74)      # header rule
    c.line(cx+cw*0.28, cy+ch, cx+cw*0.28, cy+ch*0.86)  # hangers
    c.line(cx+cw*0.72, cy+ch, cx+cw*0.72, cy+ch*0.86)
    import math
    r = s*0.17; mx, my = cx+cw*0.5, cy+ch*0.36       # circular arrow
    c.setLineWidth(max(1.0, s*0.07))
    c.arc(mx-r, my-r, mx+r, my+r, 20, 280)
    c.line(mx+r*0.94, my+r*0.34, mx+r*1.28, my+r*0.10)  # arrow head
    c.line(mx+r*0.94, my+r*0.34, mx+r*0.72, my+r*0.60)
    c.restoreState()

def ic_calendar_single(c, x, y, s, col):     # monthly sweep (calendar)
    c.saveState(); _pen(c, col, max(1.0, s*0.075))
    cw, ch = s*0.82, s*0.74; cx, cy = x+s*0.09, y+s*0.10
    _card(c, cx, cy, cw, ch, col, max(1.0, s*0.06))
    c.setLineWidth(max(0.9, s*0.06))
    c.line(cx, cy+ch*0.74, cx+cw, cy+ch*0.74)
    c.line(cx+cw*0.28, cy+ch, cx+cw*0.28, cy+ch*0.86)
    c.line(cx+cw*0.72, cy+ch, cx+cw*0.72, cy+ch*0.86)
    c.setLineWidth(max(0.8, s*0.05))               # a couple of day marks
    for gx in (0.30, 0.52, 0.74):
        c.line(cx+cw*gx, cy+ch*0.44, cx+cw*(gx+0.10), cy+ch*0.44)
    for gx in (0.30, 0.52):
        c.line(cx+cw*gx, cy+ch*0.26, cx+cw*(gx+0.10), cy+ch*0.26)
    c.restoreState()

def ic_clock_pencil(c, x, y, s, col):        # quick capture (clock + pencil)
    c.saveState(); _pen(c, col, max(1.1, s*0.08))
    r = s*0.30; mx, my = x+s*0.36, y+s*0.60
    c.circle(mx, my, r, stroke=1, fill=0)
    c.setLineWidth(max(1.0, s*0.07))
    c.line(mx, my, mx, my+r*0.62); c.line(mx, my, mx+r*0.5, my)
    px, py = x+s*0.52, y+s*0.02                    # pencil
    c.setLineWidth(max(1.0, s*0.08))
    c.line(px, py, px+s*0.40, py+s*0.40)
    c.line(px+s*0.34, py+s*0.28, px+s*0.46, py+s*0.40)
    c.restoreState()

def ic_clock60(c, x, y, s, col):             # 60-minute setup
    c.saveState(); _pen(c, col, max(1.1, s*0.085))
    r = s*0.40; mx, my = x+s*0.5, y+s*0.46
    c.circle(mx, my, r, stroke=1, fill=0)
    c.line(mx, my+r, mx, my+r*0.72)                # 12 tick
    c.setLineWidth(max(1.0, s*0.075))
    c.line(mx, my, mx, my+r*0.60)                  # minute hand (to 12 -> full hour)
    c.line(mx, my, mx+r*0.42, my+r*0.10)           # hour hand
    c.restoreState()

def ic_translate_arrow(c, x, y, s, col):     # translate (two lines + arrow)
    c.saveState(); _pen(c, col, max(1.1, s*0.08))
    c.line(x+s*0.06, y+s*0.72, x+s*0.44, y+s*0.72)   # internal line (short)
    c.line(x+s*0.06, y+s*0.58, x+s*0.34, y+s*0.58)
    c.line(x+s*0.56, y+s*0.30, x+s*0.96, y+s*0.30)   # portable line
    c.line(x+s*0.56, y+s*0.16, x+s*0.86, y+s*0.16)
    ax0, ay0, ax1, ay1 = x+s*0.30, y+s*0.62, x+s*0.66, y+s*0.30   # arrow
    c.setLineWidth(max(1.1, s*0.085))
    c.line(ax0, ay0, ax1, ay1)
    c.line(ax1, ay1, ax1-s*0.16, ay1+s*0.06)
    c.line(ax1, ay1, ax1-s*0.04, ay1+s*0.20)
    c.restoreState()

def ic_prooflines(c, x, y, s, col):          # proof line (many lines resolve into one)
    c.saveState(); _pen(c, col, max(0.9, s*0.06))
    for fr, ln in ((0.86,0.42),(0.70,0.60),(0.54,0.34)):
        c.line(x+s*0.04, y+s*fr, x+s*0.04+s*ln, y+s*fr)
    c.setLineWidth(max(1.4, s*0.11))              # the one clear proof line
    c.line(x+s*0.04, y+s*0.20, x+s*0.92, y+s*0.20)
    c.setLineWidth(max(0.9, s*0.06))              # converging guides
    c.line(x+s*0.46, y+s*0.54, x+s*0.60, y+s*0.24)
    c.restoreState()

class IconMark(Flowable):
    """Zero-height flowable that draws a vector icon at a position derived from
    its flow location. Because it consumes no space it never changes text flow,
    field coordinates, page count, bookmarks, or links. draw_fn receives
    (canvas, x, y) where (x, y) is the flowable's absolute lower-left."""
    def __init__(self, draw_fn):
        super().__init__(); self.draw_fn = draw_fn
    def wrap(self, aw, ah): return (0, 0)
    def drawOn(self, canvas, x, y, _sW=0):
        canvas.saveState()
        self.draw_fn(canvas, x, y)
        canvas.restoreState()
    def draw(self): pass

def divider_badge_mark(part_num, d=31, gap=10):
    """Return a draw_fn that places a Part badge above the PART label at the
    left edge. Insert the IconMark right before the PART paragraph."""
    icon = PART_ICON[part_num]
    def _fn(c, x, y):
        badge(c, x, y + gap, d, icon)
    return _fn

def chip_mark(icon_fn, d=20, dy=-30):
    """Return a draw_fn that places a small badge at the top-right of a tool
    page, vertically near the kicker/title. Insert the IconMark at the very
    start of the section (its y is the content-frame top)."""
    def _fn(c, x, y):
        badge(c, PAGE_W - MARGIN - d, y + dy, d, icon_fn)
    return _fn

class IconCell(Flowable):
    """A fixed-size cell that draws a line icon, for the far-right of a ledger
    form-title band. Sized <= the band's title height so it never increases the
    band height (form-field coordinates below stay identical)."""
    def __init__(self, icon_fn, d=17, col=CREAM):
        super().__init__(); self.icon_fn=icon_fn; self.d=d; self.col=col
    def wrap(self, aw, ah): return (self.d, self.d)
    def draw(self):
        self.icon_fn(self.canv, 0, 0, self.d, self.col)

# ---- named topical icons for placement -----------------------------------
PART_ICON = {
    1: ic_record_search, 2: ic_shield_check, 3: ic_form_pencil,
    4: ic_layered_cards, 5: ic_calendar_arrow,
}

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
