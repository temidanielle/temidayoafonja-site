#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/keeptheproof/build")
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Table, TableStyle, Flowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from ktp import (NAVY, PAPER, GOLD, INK, MUTE, HAIR, PAGE_W, PAGE_H, MARGIN,
                 CONTENT_W, register_fonts)

OUT = sys.argv[1]
register_fonts()
GREEN = HexColor("#2F6B3A")

eyebrow = ParagraphStyle("e", fontName="DM-Bold", fontSize=10, textColor=GOLD, leading=13, spaceAfter=5, tracking=2)
title = ParagraphStyle("t", fontName="CG-Semi", fontSize=27, textColor=NAVY, leading=30, spaceAfter=4)
sub = ParagraphStyle("s", fontName="DM", fontSize=9.5, textColor=MUTE, leading=13, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="CG-Semi", fontSize=15, textColor=NAVY, leading=18, spaceBefore=13, spaceAfter=5)
body = ParagraphStyle("b", fontName="DM", fontSize=9.6, textColor=INK, leading=14, spaceAfter=5)
bodys = ParagraphStyle("bs", fontName="DM", fontSize=9.2, textColor=INK, leading=13)
bullet = ParagraphStyle("bu", fontName="DM", fontSize=9.4, textColor=INK, leading=13.4, leftIndent=14, bulletIndent=2, spaceAfter=3)
cellh = ParagraphStyle("ch", fontName="DM-Bold", fontSize=8.8, textColor=HexColor("#FFFFFF"), leading=11)
cell = ParagraphStyle("c", fontName="DM", fontSize=8.8, textColor=INK, leading=11.5)
cellb = ParagraphStyle("cb", fontName="DM-Bold", fontSize=8.8, textColor=GREEN, leading=11.5)
mono = ParagraphStyle("m", fontName="Courier", fontSize=8, textColor=INK, leading=11)

def P(t, s=body): return Paragraph(t, s)
def bl(t): return Paragraph(t, bullet, bulletText="•")

class Rule(Flowable):
    def __init__(self, gold=46): super().__init__(); self.g=gold
    def wrap(self,aw,ah): return (CONTENT_W,8)
    def draw(self):
        c=self.canv; c.setStrokeColor(HAIR); c.setLineWidth(0.7); c.line(0,4,CONTENT_W,4)
        c.setStrokeColor(GOLD); c.setLineWidth(1.6); c.line(0,4,self.g,4)

def tbl(data, widths, aligns=None):
    t=Table(data, colWidths=widths)
    st=[("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),HexColor("#FFFFFF")),
        ("GRID",(0,0),(-1,-1),0.5,HAIR),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[PAPER,HexColor("#EFE8DA")])]
    t.setStyle(TableStyle(st)); return t

class Doc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=(PAGE_W,PAGE_H), leftMargin=MARGIN, rightMargin=MARGIN,
                         topMargin=MARGIN, bottomMargin=MARGIN, title="Keep the Proof v1.0.1 — Release Readiness")
        fr=Frame(MARGIN,60,CONTENT_W,PAGE_H-MARGIN-60,id="c",leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="c",frames=[fr],onPage=self._bg)])
    def _bg(self,c,d):
        c.setFillColor(PAPER); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        c.setStrokeColor(HAIR); c.setLineWidth(0.6); c.line(MARGIN,52,PAGE_W-MARGIN,52)
        c.setFont("DM",8); c.setFillColor(MUTE)
        c.drawString(MARGIN,40,"Keep the Proof v1.0.1  |  Release Readiness & QA Sign-off")
        c.drawRightString(PAGE_W-MARGIN,40,"Prepared 2026-08-21")

def ch(t): return Paragraph(t, cellh)
def cc(t,s=cell): return Paragraph(t, s)

story=[
    P("KEEP THE PROOF", eyebrow),
    P("Release Readiness &amp; QA Sign-off", title),
    P("Internal build RC5  ·  Public version 1.0.1 (unpublished)", sub),
    Rule(), Spacer(1,7),
    P('<font color="#2F6B3A"><b>Status: RELEASE-READY.</b></font> Both QA release gates are passed. '
      'No open release blocker remains on the QA side. Nothing has been published &#8212; final '
      'publication remains a deliberate owner action.'),

    P("Release gates", h2),
    tbl([[ch("Gate"),ch("Requirement"),ch("Status"),ch("Confirmed")],
         [cc("1  Adobe acceptance"),cc("Interactive field-capacity acceptance in Adobe Acrobat Reader"),cc("PASSED",cellb),cc("2026-08-21")],
         [cc("2  Poppler 26.05+"),cc("Page 37 renders correctly on Poppler 26.05 or later"),cc("PASSED",cellb),cc("2026-08-21")]],
        [92,232,58,66]),

    P("Gate 1 &#8212; Adobe Acrobat Reader field-capacity acceptance", h2),
    P("The product owner ran the manual acceptance test on both RC5 PDFs in Adobe Acrobat Reader and confirmed: "
      "long multiline entries and short fields accept their intended input; saving, closing, and reopening preserve "
      "the values exactly; fields remain editable; and handbook page 37 renders correctly. This closes the "
      "typeability question that earlier programmatic tests could not establish. Underlying correction: every field "
      "previously inherited ReportLab&#8217;s default /MaxLen 100; RC5 assigns a deliberate per-field capacity "
      "(full narrative / evidence &#8805; 300, medium &#8805; 180, verifier / confidentiality / support &#8805; 140, "
      "short metadata sized per field). All 142 fields persist their full intended-length value after save and reopen "
      "with zero truncation."),

    P("Gate 2 &#8212; Poppler 26.05+ page-37 rendering", h2),
    P("The local build environment caps Poppler at 24.02, so the gate was exercised in CI: a GitHub Actions job in an "
      "Arch Linux container running <b>Poppler 26.07.0</b> &#8212; at or beyond the reported failing version &#8212; "
      "rendered the shipped RC5 handbook page 37 in every mode, comparing the content top edge and bounding box "
      "against the approved PyMuPDF reference (top = 156&#8239;px at 150&#8239;dpi)."),
    tbl([[ch("Render mode (Poppler 26.07.0)"),ch("Top edge"),ch("Result")],
         [cc("Blank &#8212; whole document"),cc("155 px"),cc("OK (within 1px)",cellb)],
         [cc("Blank &#8212; pdfseparate true isolation"),cc("155 px"),cc("OK (within 1px)",cellb)],
         [cc("Blank &#8212; annotations hidden (control)"),cc("155 px"),cc("OK (within 1px)",cellb)],
         [cc("Stress-filled &#8212; whole document"),cc("155 px"),cc("OK (within 1px)",cellb)],
         [cc("Stress-filled &#8212; pdfseparate true isolation"),cc("155 px"),cc("OK (within 1px)",cellb)]],
        [250,90,108]),
    Spacer(1,4),
    P('<font color="#2F6B3A"><b>VERDICT: PASS.</b></font> The page-37 heading and top content sit at the reference '
      'position in every mode; bounding box within 1&#8239;px (antialiasing floor). No clipping, no shift &#8212; '
      'whole-document or isolated, blank or filled, annotations on or off. (CI run 32530971761.)', bodys),

    P("Customer deliverables", h2),
    P("<b>Customer bundle</b> (KEEP_THE_PROOF_CUSTOMER_BUNDLE_v1.0.1.zip) contains exactly three purchaser-facing "
      "files and nothing else:"),
    bl("Keep_the_Proof_A_60_Minute_Career_Evidence_System_v1.0.1_FINAL.pdf  (handbook, 41 pages)"),
    bl("Keep_the_Proof_Career_Evidence_Ledger_v1.0.1_FINAL.pdf  (ledger, 12 pages)"),
    bl("KEEP_THE_PROOF_START_HERE_v1.0.1.pdf  (one-page orientation)"),
    P("The plain-text README was replaced by the designed one-page Start Here PDF. No source, QA, or internal "
      "materials are in the bundle."),

    P("SHA-256 &#8212; customer-facing files", h2),
    tbl([[ch("File"),ch("SHA-256")],
         [cc("Handbook PDF"),cc("7ee951ce…bcf78c2a",mono)],
         [cc("Career Evidence Ledger PDF"),cc("259315b0…f8717f81",mono)],
         [cc("Start Here PDF"),cc("5cfc6f0f…c1f9f2fc",mono)],
         [cc("Customer bundle ZIP"),cc("d2e4030d…d98cbc87",mono)]],
        [210,238]),
    Spacer(1,3),
    P("Both product-PDF hashes are unchanged since RC5; the Start Here PDF and bundle are new.", bodys),

    P("Recommendation", h2),
    P("<b>RC5 v1.0.1 is release-ready.</b> Both QA gates are passed and there is no open release blocker. The "
      "recommended next step is the owner&#8217;s deliberate publication action (website download link and Gumroad "
      "delivery). Publication has intentionally not been performed; public version remains 1.0.1, unpublished."),
]
Doc(OUT).build(story)
print("wrote", OUT)
