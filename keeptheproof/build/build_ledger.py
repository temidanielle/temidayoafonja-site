#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the standalone Career Evidence Ledger (customer PDF). Reusable fillable
forms that accompany the Keep the Proof handbook. Run:
    python3 build_ledger.py <out.pdf> <buildtime>
"""
import sys
from ktp import *
from reportlab.platypus import (Paragraph, Spacer, NextPageTemplate, PageBreak,
    Table, TableStyle, KeepTogether, Flowable)

OUT = sys.argv[1] if len(sys.argv) > 1 else "ledger.pdf"
BUILDTIME = sys.argv[2] if len(sys.argv) > 2 else "Monday, August 17, 2026 at 1:05 PM"
VERSION = "Version 1.0.1"
REVLINE = f"{VERSION}  ·  Revised {BUILDTIME} CT"
URL = "temidayoafonja.com"

register_fonts()
S = styles()
Field._seen = set()

# ---- shortcuts ----
def P(t): return Paragraph(t, S["body"])
def H2(t): return Paragraph(t, S["h2"])
def H3(t): return Paragraph(t, S["h3"])
def EY(t): return Paragraph(t.upper(), S["eyebrow"])
def KI(t): return Paragraph(t.upper(), S["kicker"])
def NOTE(t): return Paragraph(t, S["note"])
def SP(h=6): return Spacer(1, h)
def RULE(w=CONTENT_W, c=HAIR, t=0.8): return HRule(w, color=c, thick=t, space=8)
def CO(title, body, bg="navy", bar=RUST): return KeepTogether([build_callout(title, body, S, bg=bg, bar=bar)])
def FR(label, name, w=CONTENT_W, h=20, hint=None, multiline=False, keep=True):
    return field_row(label, name, S, width=w, height=h, hint=hint, multiline=multiline, keep=keep)

def formhead(title, subtitle):
    """Navy band that heads each reusable form."""
    inner = [[Paragraph(title, ParagraphStyle("fh_t", fontName="CG-Semi", fontSize=17,
                 textColor=CREAM, leading=20)),
              Paragraph(subtitle, ParagraphStyle("fh_s", fontName="DM", fontSize=8.6,
                 textColor=GOLD, leading=11))]]
    t = Table([[inner[0][0], inner[0][1]]], colWidths=[CONTENT_W*0.55-14, CONTENT_W*0.45-14])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
        ("TOPPADDING",(0,0),(-1,-1),11),("BOTTOMPADDING",(0,0),(-1,-1),11),("ALIGN",(1,0),(1,0),"RIGHT")]))
    return t

def two_up(l1,n1,l2,n2,h=20):
    w=(CONTENT_W-16)/2
    left=FR(l1,n1,w=w,h=h,keep=False); right=FR(l2,n2,w=w,h=h,keep=False)
    t=Table([[left,right]],colWidths=[w+8,w+8])
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,0),16),
        ("RIGHTPADDING",(1,0),(1,0),0),("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),("VALIGN",(0,0),(-1,-1),"TOP")]))
    return t

story = []

# =====================================================================
# COVER
# =====================================================================
class Cover(Flowable):
    def __init__(self): super().__init__(); self.width=PAGE_W; self.height=PAGE_H
    def wrap(self,aw,ah): return (0,0)
    def drawOn(self, canvas, x, y, _sW=0):
        # Draw at absolute page coordinates. The base Flowable.drawOn translates
        # the canvas to the frame cursor and would push the cover text off the
        # page (the v1.0.0 blank-navy-cover defect); bypass that here.
        self.canv = canvas
        self.draw()
    def draw(self):
        c=self.canv
        record_motif(c, MARGIN, PAGE_H-120, w=52)
        c.setFont("DM-Bold", 11); c.setFillColor(GOLD)
        c.drawString(MARGIN, PAGE_H-186, "K E E P   T H E   P R O O F")
        c.setFont("CG-Semi", 60); c.setFillColor(CREAM)
        c.drawString(MARGIN-2, PAGE_H-286, "Career Evidence")
        c.drawString(MARGIN-2, PAGE_H-348, "Ledger")
        c.setFillColor(RUST); c.rect(MARGIN, PAGE_H-384, 88, 5, fill=1, stroke=0)
        c.setFont("CG", 21); c.setFillColor(HexColor("#D8D2C4"))
        c.drawString(MARGIN, PAGE_H-430, "Reusable Fillable Companion")
        c.setFont("DM", 11); c.setFillColor(CREAMSOFT)
        c.drawString(MARGIN, PAGE_H-458, "The fillable forms from Keep the Proof, gathered to reuse as often as you need.")
        c.setFont("DM", 11); c.setFillColor(CREAMSOFT)
        c.drawString(MARGIN, 150, "Six forms: Quick Capture, Full Entry, Translation, the")
        c.drawString(MARGIN, 133, "Monthly Sweep, the Quarterly Review, and the Evidence")
        c.drawString(MARGIN, 116, "Index. Fill them on screen, or print and write by hand.")
        c.setFont("DM-Bold", 10.5); c.setFillColor(GOLD)
        c.drawString(MARGIN, 74, "Temidayo Afonja")
        c.setFont("DM", 9.5); c.setFillColor(CREAMSOFT)
        c.drawRightString(PAGE_W-MARGIN, 74, URL)
        uw = c.stringWidth(URL, "DM", 9.5)
        c.linkURL(f"https://{URL}", (PAGE_W-MARGIN-uw, 71, PAGE_W-MARGIN, 85), relative=0, thickness=0)

story += [Cover(), NextPageTemplate("content"), PageBreak()]

# =====================================================================
# HOW TO USE + COPYRIGHT
# =====================================================================
story += [SP(6), EY("How to use this ledger"),
    Paragraph("One record, filled in over years", S["h2"]), RULE(),
    P("This ledger holds the six forms from Keep the Proof with room to fill them in. Nothing here repeats the teaching; keep the handbook beside you for the rules and the worked examples. Use this document for the doing."),
    H3("The habit it supports"),
    P("Capture work in the Quick Capture within a day of it happening. Expand what matters into a Full Entry. Translate it into portable language and build a Proof Line. Once a month, run the Monthly Proof Sweep. Once a quarter, run the Quarterly Proof Review and update your Evidence Index. That is the whole rhythm."),
    H3("Filling it in"),
    P("Every form is fillable on screen in any standard PDF reader. You can also print any page and write by hand. Because a record grows past a single copy, print or duplicate the forms you use often. The Quick Capture and the Full Entry are the two you will reuse most."),
    SP(4),
    CO("The one rule that governs every form",
       "You record your own recollection and the information you are permitted to retain. You never copy, forward, or reconstruct material your employer owns. When permission is unclear, you leave it out. If a form ever tempts you past that line, the line wins.",
       bg="navy"),
    SP(6),
    NOTE("Keep the Proof and this ledger are educational and are not legal advice. Where a question of permission genuinely matters, ask your manager, your human resources team, or an attorney before you keep anything."),
    NOTE(REVLINE + "  ·  © 2026 Temidayo Afonja. Licensed for the personal use of the individual purchaser."),
]
story += [PageBreak()]

# =====================================================================
# FORM 1 — TWO-MINUTE QUICK CAPTURE (two blocks)
# =====================================================================
def quick_capture_page(prefix, first=False):
    pg = [Bookmark("Quick Capture", 0)] if first else []
    pg += [SP(6), EY("Form one"),
        Paragraph("Quick Capture", S["h2"]), RULE(),
        P("For catching work before it fades, in the two minutes after it happens. One capture per page, with room to write a real answer. Print or copy this page whenever you need another."),
        SP(6), formhead("Two-Minute Quick Capture", "one work event"), SP(8)]
    pg += quick_capture_fields(S, prefix)
    return pg
story += quick_capture_page("qc1", first=True)
story += [PageBreak()]
story += quick_capture_page("qc2")
story += [PageBreak()]

# =====================================================================
# FORM 2 — FULL CAREER EVIDENCE ENTRY
# =====================================================================
_fe1, _fe2 = full_entry_pages(S, "le_fe")
story += [Bookmark("Full Career Evidence Entry", 0), SP(6), EY("Form two"),
    Paragraph("Full Career Evidence Entry", S["h2"]), RULE(),
    P("For work worth keeping in full. Expand a Quick Capture into a complete entry across the two pages that follow, and fill only the fields that apply."),
    SP(6), formhead("Full Career Evidence Entry", "page one of two"), SP(8)]
story += _fe1
story += [PageBreak()]
story += [SP(6), EY("Form two, continued"),
    Paragraph("Full Career Evidence Entry", S["h2"]), RULE(),
    SP(6), formhead("Full Career Evidence Entry", "page two of two"), SP(8)]
story += _fe2
story += [PageBreak()]

# =====================================================================
# FORM 3 — TRANSLATION WORKSHEET + PROOF LINE
# =====================================================================
def tr_pair(i):
    return two_up_fields({"label":"Internal wording, before translation","name":f"tr_int{i}","height":40,"multiline":True},
                         {"label":"Portable-language version","name":f"tr_por{i}","height":40,"multiline":True}, S)
story += [Bookmark("Translation Worksheet", 0), SP(6), EY("Form three"),
    Paragraph("Translation worksheet", S["h2"]), RULE(),
    P("Turn internal language into portable language. Keep any team result separate from your own part, and never invent a number."),
    SP(6), formhead("Internal to portable", "five lines"), SP(8),
    tr_pair(1), SP(6), tr_pair(2), SP(6), tr_pair(3), SP(6), tr_pair(4), SP(6), tr_pair(5),
]
story += [PageBreak()]
story += [Bookmark("Proof Line Builder", 0), SP(6), EY("Form three, continued"),
    Paragraph("Proof Line builder", S["h2"]), RULE(),
    P("Build one portable sentence from the parts of an entry. Combine them in whatever order reads well. It must be accurate, and yours to say."),
    SP(6), formhead("Proof Line builder", "one portable sentence"), SP(8),
    two_up_fields({"label":"Condition (the problem or situation)","name":"pl_cond","height":34,"multiline":True},
                  {"label":"Your part (what was yours)","name":"pl_part","height":34,"multiline":True}, S),
    SP(6), two_up_fields({"label":"Scope or constraint","name":"pl_scope","height":34,"multiline":True},
                  {"label":"Outcome (changed or prevented)","name":"pl_out","height":34,"multiline":True}, S),
    SP(6), FR("Support (permitted evidence or validation)", "pl_support", h=30, multiline=True,
              hint="A role or public reference, when you have one. Do not store a colleague&#8217;s personal details."),
    SP(6), FR("Proof Line (the finished portable sentence)", "pl_line", h=46, multiline=True,
              hint="Combine the parts above, in whatever order reads well. Accurate, and yours to say."),
]
story += [PageBreak()]

# =====================================================================
# FORM 4 — MONTHLY PROOF SWEEP
# =====================================================================
story += [Bookmark("Monthly Proof Sweep", 0), SP(6), EY("Form four"),
    Paragraph("Monthly Proof Sweep", S["h2"]), RULE(),
    P("Ten to fifteen minutes, once a month. Look back over the month and add what the day-to-day buried. Short is fine; the point is that nothing worth keeping is lost."),
    SP(6), formhead("Monthly Proof Sweep", "month and year"),
    SP(8),
    two_up("Month", "ms_month", "Date completed", "ms_done"),
    SP(6), FR("Projects, decisions, or problems I helped with this month", "ms_projects", h=46, multiline=True),
    SP(6), FR("Anything I improved, prevented, or made possible", "ms_improved", h=44, multiline=True),
    SP(6), FR("Quick Captures added this month (titles or count)", "ms_captures", h=28, multiline=True),
    SP(6), two_up("Confidentiality check: everything here is permitted?", "ms_conf",
                  "Any entry to expand into a Full Entry?", "ms_expand", h=22),
]
story += [PageBreak()]

# =====================================================================
# FORM 5 — QUARTERLY PROOF REVIEW
# =====================================================================
story += [Bookmark("Quarterly Proof Review", 0), SP(6), EY("Form five"),
    Paragraph("Quarterly Proof Review", S["h2"]), RULE(),
    P("About thirty minutes, once a quarter. This is housekeeping, not a verdict. Read your entries, correct anything time has clarified, and index what you have so it stays findable."),
    SP(6), formhead("Quarterly Proof Review", "quarter and year"),
    SP(8),
    two_up("Quarter", "qr_q", "Date completed", "qr_done"),
    SP(6), FR("Entries read and confirmed still accurate", "qr_read", h=40, multiline=True),
    SP(6), FR("Corrections or missing context added", "qr_fixed", h=44, multiline=True),
    SP(6), FR("Strongest entries this quarter, promoted to Proof Lines", "qr_strong", h=44, multiline=True),
    SP(6), FR("Where evidence is thin, without forcing a conclusion", "qr_thin", h=40, multiline=True),
    SP(6), two_up("Next review date", "qr_next", "Confidentiality re-check passed?", "qr_conf", h=22),
]
story += [PageBreak()]

# =====================================================================
# FORM 6 — QUARTERLY EVIDENCE INDEX
# =====================================================================
def index_row(i):
    w = [CONTENT_W*0.16, CONTENT_W*0.40, CONTENT_W*0.26, CONTENT_W*0.18]
    cells = [
        FR("", f"ix_date_{i}", w=w[0]-8, h=18, keep=False),
        FR("", f"ix_entry_{i}", w=w[1]-8, h=18, keep=False),
        FR("", f"ix_tags_{i}", w=w[2]-8, h=18, keep=False),
        FR("", f"ix_pl_{i}", w=w[3]-8, h=18, keep=False),
    ]
    t = Table([[cells[0], cells[1], cells[2], cells[3]]], colWidths=w)
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),("VALIGN",(0,0),(-1,-1),"TOP")]))
    return t

story += [Bookmark("Quarterly Evidence Index", 0), SP(6), EY("Form six"),
    Paragraph("Quarterly Evidence Index", S["h2"]), RULE(),
    P("A running list of what you have, so any entry is a search away. Update it at each quarterly review. Record only what is yours to keep; the index points to your entries, never to employer material."),
    SP(6)]
# header row
hw = [CONTENT_W*0.16, CONTENT_W*0.40, CONTENT_W*0.26, CONTENT_W*0.18]
hdr = Table([[Paragraph("Date or period", S["tbl_h"]), Paragraph("Entry", S["tbl_h"]),
             Paragraph("Retrieval tags", S["tbl_h"]), Paragraph("Proof Line?", S["tbl_h"])]], colWidths=hw)
hdr.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),("LEFTPADDING",(0,0),(-1,-1),6),
    ("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
story += [hdr, SP(4)]
for i in range(1, 15):
    story += [index_row(i), HRule(CONTENT_W, color=HAIR, thick=0.5, space=3)]
story += [SP(8), NOTE("When the record is the only copy you still have, this index is where you start. Keep it current, and a review, a promotion case, or an unexpected change finds you ready.")]

# =====================================================================
# BUILD
# =====================================================================
doc = KTPDoc(OUT, footer_title="Career Evidence Ledger", url=URL)
doc.title = "Career Evidence Ledger: The reusable companion to Keep the Proof"
doc.author = "Temidayo Afonja"
doc.subject = "Reusable fillable forms for capturing, translating, protecting, and retrieving your career evidence."
doc.keywords = "career evidence, ledger, work accomplishments, fillable forms, Temidayo Afonja, Keep the Proof v1.0.1"
doc.build(story)
print("wrote", OUT)
