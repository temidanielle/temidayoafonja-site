# -*- coding: utf-8 -*-
# ============================================================================
# EDITABLE SOURCE — Capability Position Read, Free Flagship Worksheet v1.1
#
# This document family is script-built, so this file is the source of record
# for the worksheet. Editing it and re-running it regenerates the PDF whole:
# every page, field, constraint and calculation.
#
#   python3 Capability_Position_Read_FREE_FLAGSHIP_Worksheet_v1.1_SOURCE.py
#
# Requires: reportlab, pypdf, and the three brand typefaces as .ttf files in
# work/gf/ — Cormorant Garamond (Regular/Bold/Italic), DM Sans
# (Regular/Bold/Italic) and Montserrat (Regular/Bold). All three are Open Font
# License faces and are the same families the deck embeds.
#
# The build refuses to produce a page whose content crosses the footer rule;
# guard() raises rather than letting an overrun ship.
#
# v1.1: a bare "?" is rejected on corrected-score fields, and the four axis
# totals are no longer read-only, so they can be typed in a reader that does
# not run form JavaScript.
# ============================================================================
"""Capability Position Read — FREE FLAGSHIP Worksheet v1.0 CANDIDATE.

Eight pages, US Letter, fillable AcroForm + usable by hand in print.
The instrument is carried verbatim from the flagship deck, which carries it
verbatim from v5.3.1 FINAL. Nothing here is generated prose where the method
has governing words.

Score fields are validated by keystroke JavaScript attached after layout:
 - initial read  : 1-5 only
 - corrected read: 1-5, optionally followed by ONE question mark (the frozen
                   uncertainty convention, e.g. 3?)
Totals auto-calculate where a viewer runs JS, and every total is also a plain
visible box that can be filled in by hand.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = "out/Capability_Position_Read_FREE_FLAGSHIP_Worksheet_v1.1_CANDIDATE.pdf"
os.makedirs("out", exist_ok=True)

# ── brand system ────────────────────────────────────────────────────────────
NAVY  = HexColor("#0F2347"); CREAM = HexColor("#F5F0E8"); GOLD = HexColor("#C9A84C")
RUST  = HexColor("#C1440E"); PALE  = HexColor("#E9EDF3"); MUTED= HexColor("#5A6B84")
LIGHT = HexColor("#B8C5D9"); WHITE = HexColor("#FFFFFF"); HAIR = HexColor("#D6DEE9")

G = "work/gf/"
for nm, fn in [("Cormorant","CormorantGaramond-Regular"), ("Cormorant-B","CormorantGaramond-Bold"),
               ("Cormorant-I","CormorantGaramond-Italic"), ("DMSans","DMSans-Regular"),
               ("DMSans-B","DMSans-Bold"), ("DMSans-I","DMSans-Italic"),
               ("Mont","Montserrat-Regular"), ("Mont-B","Montserrat-Bold")]:
    pdfmetrics.registerFont(TTFont(nm, G + fn + ".ttf"))

PW, PH = letter                       # 612 x 792
ML = 46; MR = 46; CW = PW - ML - MR    # content width 520

# ── frozen instrument ───────────────────────────────────────────────────────
DENSITY = [
 "In the last ninety days I have been handed a problem I did not already know how to solve.",
 "I work close enough to people who are better than me that I can watch how they think.",
 "My work is reviewed by someone who can tell the difference between good and adequate, and who says so directly.",
 "The feedback I receive changes what I do next, not just how I feel.",
 "I regularly operate at the edge of my competence rather than the comfortable center of it.",
 "Looking back six months, the work I do now would have been genuinely hard for me then."]
OPTIONALITY = [
 "The capability I am building would be valued by an employer in a different industry.",
 "I can describe what I do in terms of outcomes, not just my company’s internal language.",
 "If my role disappeared tomorrow, the capability I built would still be mine to carry.",
 "People with the power to hire or advance me, inside or outside my company, can already see what I am good at.",
 "What I am learning is a transferable capability rather than a company-specific procedure.",
 "I could rebuild a strong position somewhere else within a year."]
BOUNDARY = "19 to 30 high   ·   6 to 18 low   ·   17 to 21 is a boundary on either axis"
MOVES = [
 ("Remain and deepen", "The formation conditions are real and worth protecting."),
 ("Translate what is built", "The capability exists. The language for it does not."),
 ("Widen exposure", "The work is good and the wrong people have seen it."),
 ("Test portability", "Find out what travels before you need it to."),
 ("Repair formation conditions", "Change the work, not the employer, first."),
 ("Prepare for exit", "Your evidence gives you reason to prepare in case the conditions do not repair."),
 ("Seek an external perspective", "High stakes, incomplete evidence, or a boundary position.")]

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Capability Position Read — Free Flagship Worksheet")
c.setAuthor("Temidayo Afonja")
c.setSubject("Participant worksheet. Private to the participant; nothing is collected.")
form = c.acroForm
FIELDS = []                            # (name, kind) recorded for the JS pass

# ── primitives ──────────────────────────────────────────────────────────────
def wrap(txt, font, size, width):
    words, line, out = txt.split(), "", []
    for w in words:
        t = (line + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width or not line:
            line = t
        else:
            out.append(line); line = w
    if line: out.append(line)
    return out

def para(txt, x, y, w, font="DMSans", size=9.5, color=NAVY, lead=None, align="l"):
    lead = lead or size * 1.34
    c.setFont(font, size); c.setFillColor(color)
    for ln in wrap(txt, font, size, w):
        if align == "c":
            c.drawCentredString(x + w / 2.0, y, ln)
        else:
            c.drawString(x, y, ln)
        y -= lead
    return y + lead

def para_h(txt, font, size, w, lead=None):
    return len(wrap(txt, font, size, w)) * (lead or size * 1.34)

def rect(x, y, w, h, fill=None, stroke=None, lw=0.6):
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.rect(x, y, w, h, fill=1 if fill else 0, stroke=1 if stroke else 0)

def label(txt, x, y, size=7.4, color=MUTED, font="Mont-B", track=1.1):
    c.setFont(font, size); c.setFillColor(color)
    c.drawString(x, y, txt) if not track else c.drawString(x, y, txt)

def tracked(txt, x, y, size=7.4, color=MUTED, font="Mont-B", track=1.0, w=None, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    tw = pdfmetrics.stringWidth(txt, font, size) + track * (len(txt) - 1)
    sx = x if align == "l" else x + (w - tw) / 2.0
    t = c.beginText(sx, y); t.setCharSpace(track); t.textOut(txt)
    t.setCharSpace(0); c.drawText(t)      # Tc persists in the text state — always reset it
    return tw

FLOOR = 58          # nothing may be drawn below this; the footer rule sits at 42

def guard(y, page_no):
    assert y >= FLOOR, f"PAGE {page_no} OVERFLOWS: content ends at y={y:.1f}, floor {FLOOR}"

def notes_block(y, page_no, lines=4, title="NOTES"):
    tracked(title, ML, y, 7.2, MUTED, "Mont-B", 1.3)
    y -= 20
    c.setStrokeColor(HAIR); c.setLineWidth(0.5)
    for i in range(lines):
        c.line(ML, y - i * 22, PW - MR, y - i * 22)
    return y - (lines - 1) * 22 - 6

def page_frame(n, eyebrow_txt):
    """running header + footer, identical on all eight pages"""
    tracked("CAPABILITY POSITION READ", ML, PH - 34, 6.8, LIGHT, "Mont-B", 1.3)
    c.setFont("Mont-B", 6.8); c.setFillColor(LIGHT)
    c.drawRightString(PW - MR, PH - 34, "FREE FLAGSHIP WORKSHEET")
    c.setStrokeColor(HAIR); c.setLineWidth(0.5); c.line(ML, PH - 44, PW - MR, PH - 44)
    c.setStrokeColor(HAIR); c.line(ML, 42, PW - MR, 42)
    tracked("TEMIDAYO AFONJA   |   THE DENSITY GROUP", ML, 31, 6.4, MUTED, "Mont-B", 0.8)
    c.setFont("Mont-B", 6.8); c.setFillColor(MUTED)
    c.drawRightString(PW - MR, 31, str(n))
    if eyebrow_txt:
        tracked(eyebrow_txt, ML, PH - 68, 8.2, GOLD, "Mont-B", 1.4)

def head(title_txt, kicker_txt, y=PH - 96, size=25):
    c.setFont("Cormorant-B", size); c.setFillColor(NAVY)
    c.drawString(ML, y, title_txt)
    y -= 16
    if kicker_txt:
        y = para(kicker_txt, ML, y, CW, "DMSans-I", 9.4, MUTED) - 4
    return y

def txtfield(name, x, y, w, h, size=10, maxlen=200, align="l", kind="score"):
    """align is applied as /Q in the post-layout pass — reportlab has no alignment arg."""
    FIELDS.append((name, kind, align))
    form.textfield(name=name, x=x, y=y, width=w, height=h, borderWidth=0.7,
                   fillColor=WHITE, borderColor=LIGHT, textColor=NAVY,
                   fontName="Helvetica", fontSize=size, maxlen=maxlen,
                   fieldFlags="", forceBorder=True, annotationFlags="print")

def checkbox(name, x, y, size=11):
    FIELDS.append((name, "check", "l"))
    form.checkbox(name=name, x=x, y=y, size=size, borderWidth=0.8,
                  borderColor=MUTED, fillColor=WHITE, textColor=NAVY, fieldFlags="",
                  buttonStyle="check", annotationFlags="print", forceBorder=True)

# ════════════════════════════ PAGE 1 — START HERE ═══════════════════════════
page_frame(1, None)
HB = 214
rect(ML, PH - 56 - HB, CW, HB, fill=NAVY)
tracked("A CAPABILITY FORMATION EXPERIENCE", ML + 24, PH - 92, 7.6, GOLD, "Mont-B", 1.6)
c.setFont("Cormorant-B", 33); c.setFillColor(CREAM)
c.drawString(ML + 24, PH - 128, "Capability Position Read")
c.setFont("DMSans", 13); c.setFillColor(GOLD)
c.drawString(ML + 24, PH - 149, "Free Flagship Worksheet")
rect(ML + 24, PH - 168, 92, 1.6, fill=GOLD)
c.setFont("Cormorant-I", 15.5); c.setFillColor(CREAM)
for i, ln in enumerate(wrap("This worksheet helps you read your current position. "
                            "It does not tell you whether to stay or leave.",
                            "Cormorant-I", 15.5, CW - 48)):
    c.drawString(ML + 24, PH - 192 - i * 19, ln)
tracked("PRIVATE TO YOU  ·  NOTHING IS SUBMITTED  ·  KEEP BOTH READINGS",
        ML + 24, PH - 250, 6.9, LIGHT, "Mont-B", 1.2)

y = PH - 296
BLOCKS = [
 ("THE EVIDENCE WINDOW",
  "Score everything against the last ninety days only — work that actually happened, not work "
  "that was approved, promised or planned."),
 ("THE RESPONSE SCALE",
  "1 is strongly disagree. 5 is strongly agree. Whole numbers. On the second read you may mark a "
  "score with one question mark when the evidence cannot support it either way."),
 ("PRIVACY",
  "Nothing on this worksheet is submitted, collected or shared. No score, state, employer or "
  "identifying information is requested at any point. This worksheet is yours."),
 ("KEEP BOTH READINGS",
  "You will score the twelve statements twice. Do not erase or overwrite the first set. The "
  "distance between the two readings is the finding."),
]
for k, v in BLOCKS:
    h = 20 + para_h(v, "DMSans", 9.4, CW - 34)
    rect(ML, y - h, CW, h, fill=PALE)
    rect(ML, y - h, 2.4, h, fill=GOLD)
    tracked(k, ML + 17, y - 15, 7.2, NAVY, "Mont-B", 1.2)
    para(v, ML + 17, y - 30, CW - 34, "DMSans", 9.4, NAVY)
    y -= h + 9

y -= 6
tracked("THE EIGHT PAGES", ML, y, 7.2, MUTED, "Mont-B", 1.3); y -= 15
CONTENTS = [("2", "Initial Density read"), ("3", "Initial Optionality read, initial position"),
            ("4", "The evidence protocol"), ("5", "Evidence-backed Density read"),
            ("6", "Evidence-backed Optionality read"), ("7", "Corrected position and sensitivity"),
            ("8", "The Next-Move Note")]
col = CW / 2.0 - 8
for i, (n, t) in enumerate(CONTENTS):
    cx = ML + (i % 2) * (col + 16); cy = y - (i // 2) * 15
    rect(cx, cy - 3, 12, 12, fill=NAVY)
    c.setFont("Mont-B", 7); c.setFillColor(CREAM); c.drawCentredString(cx + 6, cy + 0.6, n)
    c.setFont("DMSans", 9.2); c.setFillColor(NAVY); c.drawString(cx + 19, cy, t)
y -= 4 * 15 + 6
y = para("Everything in this worksheet is available from the start. Nothing is released in stages. "
         "If you are watching a recording, work at your own pace — every step is here.",
         ML, y, CW, "DMSans-I", 9, MUTED)
guard(y, 1)
c.showPage()

# ═══════════ shared: a six-statement scoring block ══════════════════════════
def statement_block(items, first_n, prefix, y, evidence=False):
    """Returns the y below the block. evidence=True adds a corrected-score + phrase row."""
    c.setStrokeColor(HAIR); c.setLineWidth(0.5); c.line(ML, y + 2, PW - MR, y + 2)
    tracked("1  STRONGLY DISAGREE      ·      3  MIXED      ·      5  STRONGLY AGREE",
            ML, y - 11, 6.6, MUTED, "Mont-B", 1.0)
    y -= 22
    for i, t in enumerate(items):
        n = first_n + i
        FS, LEAD = 10.8, 14.4
        lines = wrap(t, "DMSans", FS, CW - 136)
        body_h = len(lines) * LEAD
        h = max(48, body_h + 24) + (24 if evidence else 0)
        rect(ML, y - h, CW, h, fill=PALE if i % 2 == 0 else WHITE)
        rect(ML + 12, y - 27, 18, 18, fill=NAVY)
        c.setFont("Mont-B", 8.6); c.setFillColor(CREAM)
        c.drawCentredString(ML + 21, y - 21.8, str(n))
        c.setFont("DMSans", FS); c.setFillColor(NAVY)
        for j, ln in enumerate(lines):
            c.drawString(ML + 40, y - 21 - j * LEAD, ln)
        # score field, right-hand column
        fx = PW - MR - 88
        tracked("SCORE", fx, y - 16, 6.2, MUTED, "Mont-B", 0.9)
        txtfield(f"{prefix}{n}", fx, y - 40, 34, 19, size=12, maxlen=2 if evidence else 1,
                 align="c", kind="score2" if evidence else "score1")
        c.setFont("DMSans", 8.4); c.setFillColor(MUTED)
        c.drawString(fx + 40, y - 34, "1–5")
        if evidence:
            c.setFont("DMSans", 7.6)
            c.drawString(fx + 40, y - 44, "or 3?")
            ey = y - body_h - 30
            tracked("EVIDENCE FROM THE LAST NINETY DAYS", ML + 40, ey + 8, 6.2, MUTED, "Mont-B", 0.9)
            txtfield(f"{prefix}e{n}", ML + 40, ey - 12, CW - 50 - 98, 17, size=9.5,
                     maxlen=160, kind="text")
        y -= h + 5
    return y

def total_block(y, title_txt, fieldname, note_txt=None):
    h = 68
    rect(ML, y - h, CW, h, fill=NAVY)
    tracked(title_txt, ML + 20, y - 20, 7.6, GOLD, "Mont-B", 1.3)
    txtfield(fieldname, ML + 20, y - 52, 80, 22, size=14, maxlen=3, align="c", kind="total")
    c.setFont("Cormorant-B", 19); c.setFillColor(CREAM)
    c.drawString(ML + 110, y - 46, "/  30")
    c.setFont("DMSans", 8.6); c.setFillColor(LIGHT)
    c.drawRightString(PW - MR - 20, y - 30, BOUNDARY.split("·")[0].strip() + "   ·   "
                      + BOUNDARY.split("·")[1].strip())
    c.drawRightString(PW - MR - 20, y - 44, BOUNDARY.split("·")[2].strip())
    c.setFont("DMSans-I", 7.4); c.setFillColor(LIGHT)
    c.drawString(ML + 20, y - 60, "Adds up automatically in most readers — you can also type it in.")
    y -= h + 8
    if note_txt:
        y = para(note_txt, ML, y - 2, CW, "DMSans-I", 9, MUTED) - 6
    return y

# ════════════════════════════ PAGE 2 — INITIAL DENSITY ══════════════════════
page_frame(2, "INITIAL READ  ·  DENSITY")
y = head("Initial Density read",
         "Statements 1 to 6. Score each one against the last ninety days. "
         "Write the number that is true, not the number you would prefer.", size=24) - 8
y = statement_block(DENSITY, 1, "d", y)
y = total_block(y - 4, "INITIAL DENSITY TOTAL", "dtotal",
                "No evidence line yet — that is deliberate. You will come back to these "
                "twelve statements with evidence on pages 5 and 6.")
guard(y, 2)
c.showPage()

# ════════════════════ PAGE 3 — INITIAL OPTIONALITY + POSITION ═══════════════
page_frame(3, "INITIAL READ  ·  OPTIONALITY")
y = head("Initial Optionality read",
         "Statements 7 to 12. Same scale, same ninety-day window.", size=24) - 6
y = statement_block(OPTIONALITY, 7, "d", y)
y = total_block(y - 2, "INITIAL OPTIONALITY TOTAL", "ototal")

STATES = ["Compounding", "Depth Trap", "Stagnant", "Fragile", "Boundary"]
h = 74
rect(ML, y - h, CW, h, fill=PALE)
tracked("INITIAL POSITION", ML + 16, y - 17, 7.4, NAVY, "Mont-B", 1.3)
c.setFont("DMSans-I", 8.6); c.setFillColor(MUTED)
c.drawString(ML + 112, y - 17, "Cross your two totals. Tick one. Hold it lightly.")
for i, s in enumerate(STATES):
    sx = ML + 16 + i * ((CW - 32) / 5.0)
    checkbox(f"pos_{s.lower().replace(' ', '_')}", sx, y - 42, 11)
    c.setFont("DMSans", 9); c.setFillColor(NAVY); c.drawString(sx + 16, y - 39, s)
c.setStrokeColor(LIGHT); c.setLineWidth(0.5); c.line(ML + 16, y - 50, PW - MR - 16, y - 50)
c.setFont("DMSans-B", 9.4); c.setFillColor(NAVY)
c.drawString(ML + 16, y - 65, "Rate your confidence in this placement from 1 to 5.")
txtfield("conf_initial", ML + 268, y - 69, 28, 16, size=11, maxlen=1, align="c", kind="score1")
c.setFont("DMSans-I", 8.6); c.setFillColor(MUTED)
c.drawString(ML + 302, y - 65, "Private. You will rate it again on page 7 and compare.")
y -= h + 8
y = para("Boundary is a legitimate reading. So is deciding, later, that an axis is incomplete.",
         ML, y, CW, "DMSans-I", 9, MUTED)
guard(y, 3)
c.showPage()

# ════════════════════════════ PAGE 4 — EVIDENCE PROTOCOL ════════════════════
page_frame(4, "THE STANDARD")
y = head("The evidence protocol",
         "This is what your second reading has to survive.", size=25) - 4
h = 56
rect(ML, y - h, CW, h, fill=NAVY)
c.setFont("Cormorant-B", 16); c.setFillColor(CREAM)
c.drawString(ML + 20, y - 26,
             "Every corrected score requires an evidence line from the last ninety days.")
c.setFont("DMSans", 9.4); c.setFillColor(GOLD)
c.drawString(ML + 20, y - 43, "Every score, in both directions.")
y -= h + 14

TIERS = [("A 4 OR 5", "At least one clear positive instance from within the window.", GOLD),
         ("A 3", "The mixed or inconsistent pattern. A 3 is a reading, not an absence of one.", GOLD),
         ("A 1 OR 2", "What repeatedly happened instead, a counterexample, or no qualifying "
                      "instance in the window.", GOLD),
         ("A  ?", "Cannot support it either way? Write your most defensible number and add one "
                  "question mark: 3?, 4?, 2?", RUST)]
for k, v, accent in TIERS:
    th = 12 + max(16, para_h(v, "DMSans", 10, CW - 154))
    rect(ML, y - th, CW, th, fill=PALE)
    rect(ML, y - th, 3, th, fill=accent)
    c.setFont("Mont-B", 9.6); c.setFillColor(NAVY)
    c.drawString(ML + 18, y - 20, k)
    para(v, ML + 128, y - 19, CW - 148, "DMSans", 10, NAVY)
    y -= th + 8

y -= 4
rect(ML, y - 34, CW, 34, fill=NAVY)
c.setFont("Cormorant-B", 16); c.setFillColor(CREAM)
c.drawCentredString(PW / 2.0, y - 22, "A 3 means mixed.   A question mark means unsupported.")
y -= 34 + 18

tracked("WHAT THE QUESTION MARKS DO TO YOUR AXIS", ML, y, 7.6, MUTED, "Mont-B", 1.3); y -= 14
RULES = [("NONE", "No unsupported-item sensitivity range is required. Use the corrected total "
                  "normally, subject to the standard boundary rule.", PALE, NAVY),
         ("1 OR 2", "That axis is PROVISIONAL. Run the neighbouring-score sensitivity check on "
                    "page 7: total it as written, then again with every marked item one point "
                    "lower, then one point higher.", NAVY, GOLD),
         ("3+", "That axis is INCOMPLETE. Do not place yourself on it today. Incomplete is a "
                "legitimate reading, not a failure.", RUST, CREAM)]
for k, v, chipfill, chiptext in RULES:
    rh = 12 + para_h(v, "DMSans", 9.5, CW - 92)
    rect(ML, y - rh, 68, rh, fill=chipfill)
    c.setFont("Mont-B", 8.4); c.setFillColor(chiptext)
    c.drawCentredString(ML + 34, y - rh / 2.0 - 3, k)
    rect(ML + 76, y - rh, CW - 76, rh, fill=PALE)
    para(v, ML + 90, y - 18, CW - 106, "DMSans", 9.5, NAVY)
    y -= rh + 7

y -= 6
y = para("Every neighbouring score stays inside the 1 to 5 scale — a 1? is never tested at 0, "
         "a 5? is never tested at 6. 17 to 21 remains the boundary band on either axis. This is "
         "an operational convention, not a statistical confidence interval, and it carries no "
         "margin of error.", ML, y, CW, "DMSans-I", 9, MUTED) - 26

tracked("A WORKED EXAMPLE", ML, y, 7.2, MUTED, "Mont-B", 1.3); y -= 18
eh = 14 + para_h("The rotation starts in March. In the last ninety days I solved problems I "
                 "already knew. Statement 1 scores a 2: no qualifying instance in the window.",
                 "Cormorant-I", 13, CW - 36)
rect(ML, y - eh, CW, eh, fill=PALE)
para("The rotation starts in March. In the last ninety days I solved problems I already knew. "
     "Statement 1 scores a 2: no qualifying instance in the window.",
     ML + 18, y - 17, CW - 36, "Cormorant-I", 13, NAVY)
y -= eh + 8
y = para("An evidence line is a phrase, not an essay. One instance, one counterexample, or one "
         "honest \u201cno qualifying instance in the window\u201d is enough.",
         ML, y, CW, "DMSans-I", 9, MUTED) - 24
guard(y, 4)
c.showPage()

# ══════════════════ PAGES 5 & 6 — EVIDENCE-BACKED READS ═════════════════════
page_frame(5, "EVIDENCE-BACKED READ  ·  DENSITY")
y = head("Evidence-backed Density read",
         "Statements 1 to 6 again. New numbers with evidence behind them — not a review of your "
         "first set. Short phrases, not essays.", size=23) - 4
y = statement_block(DENSITY, 1, "c", y, evidence=True)
y = total_block(y - 2, "CORRECTED DENSITY TOTAL", "ctotal")
guard(y, 5)
c.showPage()

page_frame(6, "EVIDENCE-BACKED READ  ·  OPTIONALITY")
y = head("Evidence-backed Optionality read",
         "Statements 7 to 12 again. Evidence in both directions — a low score needs a "
         "counterexample as much as a high score needs an instance.", size=23) - 4
y = statement_block(OPTIONALITY, 7, "c", y, evidence=True)
y = total_block(y - 2, "CORRECTED OPTIONALITY TOTAL", "cototal")
guard(y, 6)
c.showPage()

# ════════════════════════ PAGE 7 — CORRECTED POSITION ═══════════════════════
page_frame(7, "SECOND PLACEMENT")
y = head("Your corrected position",
         "Cross your two corrected totals. Then test whether the placement survives your "
         "question marks.", size=25) - 6

GUT, CELLH = 58, 92
cw2 = (CW - GUT) / 2.0
QUAD = [("DEPTH TRAP", "Deep expertise fused to one context.", 0, 0),
        ("COMPOUNDING", "Deep capability that travels.", 1, 0),
        ("STAGNANT", "The work stopped asking more of you.", 0, 1),
        ("FRAGILE", "Options on paper, not enough depth beneath.", 1, 1)]
mtop = y
for k, v, col_i, row_i in QUAD:
    cx = ML + GUT + col_i * cw2
    cy = mtop - (row_i + 1) * CELLH
    rect(cx, cy, cw2, CELLH, fill=PALE if (col_i + row_i) % 2 == 0 else WHITE,
         stroke=LIGHT, lw=0.7)
    checkbox(f"state_{k.lower().replace(' ', '_')}", cx + 14, cy + CELLH - 30, 13)
    c.setFont("Mont-B", 9); c.setFillColor(NAVY)
    c.drawString(cx + 34, cy + CELLH - 27, k)
    para(v, cx + 34, cy + CELLH - 47, cw2 - 48, "DMSans", 9, MUTED)
# axis labels
for txt, row_i in (("DENSITY / HIGH", 0), ("DENSITY / LOW", 1)):
    cy = mtop - (row_i + 1) * CELLH
    c.saveState(); c.translate(ML + 20, cy + CELLH / 2.0); c.rotate(90)
    c.setFont("Mont-B", 6.9); c.setFillColor(MUTED)
    c.drawCentredString(0, 0, txt); c.restoreState()
y = mtop - 2 * CELLH - 14
tracked("OPTIONALITY:   LOW AT LEFT   →   HIGH AT RIGHT", ML + GUT, y, 6.9, MUTED,
        "Mont-B", 1.2, w=CW - GUT, align="c")
y -= 20

# question-mark status
rect(ML, y - 46, CW, 46, fill=PALE)
tracked("QUESTION-MARK STATUS", ML + 16, y - 16, 7.2, NAVY, "Mont-B", 1.3)
QM = [("qm_none", "No marked items"), ("qm_provisional", "1–2 marked items  →  provisional"),
      ("qm_incomplete", "3+ marked items on an axis  →  incomplete")]
qx = ML + 16
for nm, t in QM:
    checkbox(nm, qx, y - 38, 11)
    c.setFont("DMSans", 8.8); c.setFillColor(NAVY); c.drawString(qx + 15, y - 35, t)
    qx += pdfmetrics.stringWidth(t, "DMSans", 8.8) + 42
y -= 46 + 10

# sensitivity, per axis
SH = 104
rect(ML, y - SH, CW, SH, fill=WHITE, stroke=LIGHT, lw=0.7)
tracked("SENSITIVITY  —  RUN THIS ON ANY AXIS CARRYING ONE OR TWO MARKED ITEMS",
        ML + 14, y - 18, 7.2, NAVY, "Mont-B", 1.2)
colx = [ML + 132, ML + 132 + 126, ML + 132 + 252]
for cx_, t in zip(colx, ["CORRECTED TOTAL", "MARKED ITEMS ONE|POINT LOWER",
                         "MARKED ITEMS ONE|POINT HIGHER"]):
    for j, ln in enumerate(t.split("|")):
        c.setFont("Mont-B", 6.4); c.setFillColor(MUTED); c.drawString(cx_, y - 36 - j * 9, ln)
for i, axis in enumerate(("DENSITY", "OPTIONALITY")):
    ry = y - 74 - i * 24
    c.setFont("Mont-B", 7.4); c.setFillColor(NAVY); c.drawString(ML + 14, ry + 5, axis)
    for j, cx_ in enumerate(colx):
        txtfield(f"sens_{axis[:3].lower()}_{j}", cx_, ry, 54, 17, size=10, maxlen=3,
                 align="c", kind="text")
y -= SH + 12

# final reading + corrected confidence
FH = 106
rect(ML, y - FH, CW, FH, fill=NAVY)
tracked("FINAL READING", ML + 16, y - 20, 7.2, GOLD, "Mont-B", 1.3)
fx = ML + 16
for nm, t in (("final_state", "State"), ("final_boundary", "Boundary"),
              ("final_incomplete", "Incomplete")):
    checkbox(nm, fx, y - 46, 12)
    c.setFont("DMSans", 9.4); c.setFillColor(CREAM); c.drawString(fx + 17, y - 43, t)
    fx += pdfmetrics.stringWidth(t, "DMSans", 9.4) + 46
c.setFont("DMSans", 9); c.setFillColor(LIGHT)
c.drawString(fx + 6, y - 43, "If a state, write it:")
txtfield("final_state_name", fx + 92, y - 48, PW - MR - 16 - (fx + 92), 17, size=9.5, kind="text")
c.setFont("DMSans-B", 9.4); c.setFillColor(CREAM)
c.drawString(ML + 16, y - 74, "Rate your confidence in this placement from 1 to 5.")
txtfield("conf_corrected", ML + 274, y - 79, 30, 17, size=11, maxlen=1, align="c", kind="score1")
c.setFont("DMSans-I", 8.8); c.setFillColor(LIGHT)
c.drawString(ML + 16, y - 93,
             "Compare it with the number you wrote on page 3. The comparison is private.")
y -= FH + 16
c.setFont("Cormorant-B", 18); c.setFillColor(NAVY)
c.drawString(ML, y, "State is not identity.")
c.setFont("DMSans-I", 9.2); c.setFillColor(MUTED)
c.drawString(ML + 168, y, "It reads conditions in a ninety-day window, and it moves.")
y = notes_block(y - 26, 7, lines=3)
guard(y, 7)
c.showPage()

# ═════════════════════════ PAGE 8 — THE NEXT-MOVE NOTE ══════════════════════
page_frame(8, "THE ARTIFACT")
y = head("The Next-Move Note",
         "Three lines. Yours, private, and enough to act on.", size=26) - 8

PROMPTS = [("MY CURRENT READ", "My position appears to be:", "nmn_read",
            "State  /  boundary  /  incomplete"),
           ("WHAT I NEED TO TEST", "The category of move my evidence supports testing is:",
            "nmn_move", "One of the seven categories below."),
           ("WHAT HAPPENS NEXT",
            "One action, conversation, or piece of evidence I will pursue next is:",
            "nmn_next", "One thing. Something you could begin this month.")]
for k, q, nm, hint in PROMPTS:
    ph = 64
    rect(ML, y - ph, CW, ph, fill=PALE)
    rect(ML, y - ph, 2.4, ph, fill=GOLD)
    tracked(k, ML + 17, y - 16, 7.2, NAVY, "Mont-B", 1.3)
    c.setFont("DMSans", 9.4); c.setFillColor(NAVY); c.drawString(ML + 17, y - 31, q)
    txtfield(nm, ML + 17, y - 54, CW - 34, 18, size=10, kind="text")
    c.setFont("DMSans-I", 7.8); c.setFillColor(MUTED); c.drawString(ML + 17, y - 62, hint)
    y -= ph + 11

y -= 12
tw = tracked("THE SEVEN CATEGORIES OF MOVE", ML, y, 7.2, MUTED, "Mont-B", 1.3)
c.setFont("DMSans-I", 8.4); c.setFillColor(MUTED)
c.drawString(ML + tw + 16, y, "Direction, not a plan.")
y -= 17
for i, (k, v) in enumerate(MOVES):
    ry = y - i * 19
    rect(ML, ry - 4, 14, 14, fill=NAVY)
    c.setFont("Mont-B", 7); c.setFillColor(CREAM); c.drawCentredString(ML + 7, ry, str(i + 1))
    c.setFont("DMSans-B", 9); c.setFillColor(NAVY); c.drawString(ML + 22, ry, k)
    c.setFont("DMSans", 8.8); c.setFillColor(MUTED); c.drawString(ML + 182, ry, v)
y -= 7 * 19 + 6
c.setFont("DMSans-I", 8.8); c.setFillColor(RUST)
c.drawString(ML, y, "No square prescribes a category. Your evidence and constraints still apply.")
y -= 22

rect(ML, y - 40, CW, 40, fill=NAVY)
c.setFont("Cormorant-B", 15.5); c.setFillColor(CREAM)
c.drawCentredString(PW / 2.0, y - 18,
                    "This is a note, not a decision.")
c.setFont("DMSans", 9); c.setFillColor(GOLD)
c.drawCentredString(PW / 2.0, y - 32,
                    "It records what your evidence supports testing next.")
y -= 40 + 14
c.setFont("DMSans-B", 10); c.setFillColor(NAVY)
c.drawString(ML, y, "My rescore date:")
txtfield("rescore_date", ML + 100, y - 5, 140, 18, size=10, kind="text")
c.setFont("DMSans-I", 8.6); c.setFillColor(MUTED)
c.drawString(ML + 252, y, "Ninety days out. Notice what changed.")
y = notes_block(y - 30, 8, lines=3)
guard(y, 8)
c.showPage()
c.save()
print("layout written:", OUT, "fields:", len(FIELDS))


# ═══════════════════════ FIELD BEHAVIOUR (second pass) ══════════════════════
"""Attach field behaviour reportlab cannot express.

 - /Q alignment on centred score boxes
 - keystroke validation:
     initial read  (d1..d12, conf_*)  -> a single character, 1-5 only
     corrected read (c1..c12)         -> 1-5, optionally followed by ONE '?'
 - calculate actions on the four axis totals (sum, '?' ignored for the sum,
   exactly as the method says: total the axis using the numbers as written)
 - no submit action, no JS that transmits anything, no hidden fields

The '?' allowance on the corrected read is required by the frozen uncertainty
convention. Restricting those boxes to bare 1-5 would make the instrument
impossible to complete correctly, so the brief's "1-5 only" rule is applied to
the initial read and to both confidence ratings, where no '?' is ever valid.
"""
def attach_field_behaviour():
    import re
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import (DictionaryObject, NameObject, NumberObject,
                               DecodedStreamObject, ArrayObject, BooleanObject)
    SRC = "out/Capability_Position_Read_FREE_FLAGSHIP_Worksheet_v1.1_CANDIDATE.pdf"

    KS_15  = ('if(event.change && !/^[1-5]$/.test(event.change)) event.rc = false;')
    # A corrected score is blank, 1-5, or 1-5 followed by ONE question mark.
    # A bare "?" is rejected: the convention is "your most defensible number,
    # marked once" -- never a mark with no number under it.
    CORR_RE = '/^([1-5]\\??)?$/'
    KS_15Q = ('if(event.change){\n'
              '  var v = event.value.substring(0,event.selStart) + event.change +'
              ' event.value.substring(event.selEnd);\n'
              '  if(!' + CORR_RE + '.test(v)) event.rc = false;\n'
              '}')
    VAL_15Q = ('if(event.value != "" && !' + CORR_RE + '.test(event.value)) {\n'
               '  app.alert("Enter a score from 1 to 5. You may mark it once, as 3?, when '
               'the evidence cannot support it either way. A question mark on its own is '
               'not a score.");\n'
               '  event.rc = false;\n}')

    def calc_js(prefix, lo, hi):
        return (f'var t=0, any=false;\n'
                f'for (var i={lo}; i<={hi}; i++) {{\n'
                f'  var f = this.getField("{prefix}"+i);\n'
                f'  if (f) {{ var s = String(f.value).replace("?","");\n'
                f'    if (s !== "") {{ t += Number(s); any = true; }} }}\n'
                f'}}\n'
                f'event.value = any ? t : "";')

    CENTRED = re.compile(r"^(d|c)(\d+)$|^conf_|^sens_")
    INIT15  = re.compile(r"^d([1-9]|1[0-2])$|^conf_initial$|^conf_corrected$")
    CORR    = re.compile(r"^c([1-9]|1[0-2])$")
    TOTALS  = {"dtotal": ("d", 1, 6), "ototal": ("d", 7, 12),
               "ctotal": ("c", 1, 6), "cototal": ("c", 7, 12)}

    r = PdfReader(SRC)
    w = PdfWriter()
    w.append(r)

    def js_action(src, key):
        st = DecodedStreamObject()
        st.set_data(src.encode("utf-8"))
        ref = w._add_object(st)
        return DictionaryObject({NameObject("/S"): NameObject("/JavaScript"),
                                 NameObject("/JS"): ref})

    touched = {"align": 0, "ks15": 0, "ks15q": 0, "calc": 0}
    calc_order = []
    for page in w.pages:
        for a in page.get("/Annots", []):
            o = a.get_object()
            nm = o.get("/T")
            if not nm:
                continue
            nm = str(nm)
            if CENTRED.match(nm):
                o[NameObject("/Q")] = NumberObject(1)
                touched["align"] += 1
            aa = DictionaryObject()
            if INIT15.match(nm):
                aa[NameObject("/K")] = js_action(KS_15, nm); touched["ks15"] += 1
            elif CORR.match(nm):
                aa[NameObject("/K")] = js_action(KS_15Q, nm)
                aa[NameObject("/V")] = js_action(VAL_15Q, nm)
                touched["ks15q"] += 1
            elif nm in TOTALS:
                p, lo, hi = TOTALS[nm]
                # Auto-calculate where the reader runs form JavaScript, but never
                # read-only: in a reader without JS the participant must still be
                # able to type the total in, without printing the worksheet.
                aa[NameObject("/C")] = js_action(calc_js(p, lo, hi), nm)
                o[NameObject("/Ff")] = NumberObject(0)
                calc_order.append(a)
                touched["calc"] += 1
            if aa:
                o[NameObject("/AA")] = aa

    # calculation order, and force appearances to regenerate so totals show up
    acro = w._root_object["/AcroForm"]
    acro[NameObject("/CO")] = ArrayObject(calc_order)
    acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    with open(SRC, "wb") as fh:
        w.write(fh)
    print("field behaviour attached:", touched)
    print("pages:", len(r.pages))

attach_field_behaviour()
