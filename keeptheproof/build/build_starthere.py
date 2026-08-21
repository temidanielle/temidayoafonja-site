#!/usr/bin/env python3
"""Build the customer 'Start Here' orientation page as a one-page PDF in the
Keep the Proof visual language (warm ivory ground, navy type, restrained gold
accents, the approved line-icon style). Product content is untouched; this is a
packaging piece. Run: python3 build_starthere.py <out.pdf>
"""
import sys
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, Flowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
import ktp
from ktp import (NAVY, PAPER, GOLD, RUST, INK, MUTE, HAIR, CREAM, PAGE_W, PAGE_H,
                 MARGIN, CONTENT_W, register_fonts, ic_clock60, ic_layered_cards, IconMark)

OUT = sys.argv[1] if len(sys.argv) > 1 else "start_here.pdf"
register_fonts()

# ---- styles (handbook family, tuned for a calm single page) --------------
eyebrow = ParagraphStyle("eyebrow", fontName="DM-Bold", fontSize=10, textColor=GOLD,
    leading=13, spaceAfter=6, tracking=2)
title = ParagraphStyle("title", fontName="CG-Semi", fontSize=30, textColor=NAVY,
    leading=33, spaceAfter=10)
lead = ParagraphStyle("lead", fontName="DM", fontSize=10.6, textColor=INK,
    leading=16.2, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="CG-Semi", fontSize=16, textColor=NAVY,
    leading=19, spaceBefore=13, spaceAfter=6)
toolname = ParagraphStyle("toolname", fontName="DM-Bold", fontSize=10.8, textColor=NAVY,
    leading=14, spaceAfter=2)
tooldesc = ParagraphStyle("tooldesc", fontName="DM", fontSize=9.7, textColor=INK,
    leading=13.8)
body = ParagraphStyle("body", fontName="DM", fontSize=9.9, textColor=INK,
    leading=14.4, spaceAfter=3)
olist = ParagraphStyle("olist", fontName="DM", fontSize=9.9, textColor=INK,
    leading=13.6, leftIndent=17, firstLineIndent=-17, spaceAfter=2.5)
signame = ParagraphStyle("signame", fontName="DM-Bold", fontSize=10, textColor=NAVY,
    leading=14, spaceBefore=2)
sigline = ParagraphStyle("sigline", fontName="DM", fontSize=9.3, textColor=MUTE, leading=13)

def P(t, s): return Paragraph(t, s)

class HRule(Flowable):
    """A thin full-width hairline with a short gold lead segment (house accent)."""
    def __init__(self, gold_w=44, pad=0):
        super().__init__(); self.gold_w=gold_w; self.pad=pad
    def wrap(self, aw, ah): return (CONTENT_W, 8)
    def draw(self):
        c=self.canv
        c.setStrokeColor(HAIR); c.setLineWidth(0.7); c.line(0,4,CONTENT_W,4)
        c.setStrokeColor(GOLD); c.setLineWidth(1.6); c.line(0,4,self.gold_w,4)

def tool_row(icon_fn, name, desc):
    """A numbered tool: small navy line icon at left, name + description at right."""
    class Icon(Flowable):
        def wrap(self, aw, ah): return (26, 26)
        def draw(self): icon_fn(self.canv, 1, 1, 22, NAVY)
    cell = [P(name, toolname), P(desc, tooldesc)]
    t = Table([[Icon(), cell]], colWidths=[34, CONTENT_W-34])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return t

# ---- document with ivory ground and the exact customer footer ------------
class StartHereDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=(PAGE_W, PAGE_H), leftMargin=MARGIN,
            rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
            title="Keep the Proof - Start Here", author="Temidayo Afonja",
            subject="Keep the Proof v1.0.1", keywords="Keep the Proof, v1.0.1")
        frame = Frame(MARGIN, 62, CONTENT_W, PAGE_H-MARGIN-62, id="c",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="content", frames=[frame], onPage=self._bg)])
    def _bg(self, canv, doc):
        canv.setFillColor(PAPER); canv.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        # footer: thin rule + exact customer footer line, centred, quiet
        canv.setStrokeColor(HAIR); canv.setLineWidth(0.6); canv.line(MARGIN,52,PAGE_W-MARGIN,52)
        canv.setFont("DM", 8); canv.setFillColor(MUTE)
        canv.drawCentredString(PAGE_W/2, 40,
            "Keep the Proof v1.0.1  |  For the purchaser’s personal use")

story = [
    P("KEEP THE PROOF", eyebrow),
    P("Start Here", title),
    HRule(),
    Spacer(1, 8),
    P("Welcome to Keep the Proof.", lead),
    P("In the next 60 minutes, you will turn scattered memories of your work into a "
      "private career evidence system you can return to before you need a resume, "
      "interview story, promotion case, or career move.", lead),

    P("Your two tools", h2),
    tool_row(ic_clock60, "1.  The 60-Minute Career Evidence System",
        "Begin with the main handbook. It will guide you through choosing meaningful "
        "work, identifying what changed because of your contribution, separating "
        "evidence from memory, and translating internal work into language that can travel."),
    Spacer(1, 7),
    tool_row(ic_layered_cards, "2.  The Career Evidence Ledger",
        "Use the ledger after completing the handbook. It is your reusable place to "
        "capture new evidence, complete monthly and quarterly reviews, and keep your "
        "proof current over time."),

    P("Recommended order", h2),
    P("1.  Download both PDFs to your computer.", olist),
    P("2.  Open them in Adobe Acrobat Reader for the best fillable experience.", olist),
    P("3.  Save a separate working copy before you begin.", olist),
    P("4.  Complete the 60-Minute Career Evidence System first.", olist),
    P("5.  Continue using the Career Evidence Ledger monthly and quarterly.", olist),

    P("Keep your evidence safe", h2),
    P("Keep this system private. Do not enter confidential employee information, "
      "protected customer information, proprietary company data, passwords, or "
      "sensitive business records.", body),
    P("Describe the work and its outcome without including information you are not "
      "permitted to retain.", body),

    Spacer(1, 9),
    HRule(),
    Spacer(1, 7),
    P("You should leave the first hour with at least one completed Career Evidence "
      "Entry and a repeatable way to keep the proof of what your work has built.", lead),
    Spacer(1, 6),
    P("Temidayo Afonja", signame),
    P("Founder, The Density Group", sigline),
    P("Creator of Capability Formation", sigline),
    P('<a href="https://temidayoafonja.com" color="#5A6B82">temidayoafonja.com</a>', sigline),
]

StartHereDoc(OUT).build(story)
print("wrote", OUT)
