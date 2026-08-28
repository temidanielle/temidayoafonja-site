"""Video 6: "Are You Growing—or Just Being Given More Work?"  Twelve slides.

Built in the approved Capability Formation system, using the Video 5 deck as the
visual master: deep navy ground, warm cream typography, muted gold accents, thin
gold rules, generous negative space, restrained editorial treatment.

Every word on every slide is copied verbatim from Section 5 of the Video 6
production package. Continuity with Video 5 is kept in palette, type and
restraint; the layout devices deliberately differ so the two decks are not
clones. Video 5's wording and subject matter are not carried over.

No opening title card. The video begins full screen on Temidayo; slide 1 is the
first teaching visual and lands only after the hook and viewer promise.
"""
import os
from deck import *

# Slide number -> reveal states. Package reveal map, total 23.
STEPS = {1: 2, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 3, 9: 2, 10: 3,
         11: 1, 12: 1}

TITLES = {
    1:  "Core distinction",
    2:  "Growth versus load",
    3:  "The three tests",
    4:  "Complexity test",
    5:  "Capability question",
    6:  "Authority distinction",
    7:  "Authority warning",
    8:  "Return test",
    9:  "Pattern read",
    10: "Scope conversation",
    11: "Primary CTA, Capability Formation Field Kit",
    12: "Watch next",
}

SLUGS = {
    1: "core-distinction", 2: "growth-versus-load", 3: "the-three-tests",
    4: "complexity-test", 5: "capability-question", 6: "authority-distinction",
    7: "authority-warning", 8: "return-test", 9: "pattern-read",
    10: "scope-conversation", 11: "field-kit", 12: "watch-next",
}

DIM_ON_NAVY = RGBColor(0x63, 0x74, 0x8C)
DIM_ON_CREAM = RGBColor(0x8E, 0x98, 0xA8)
PLAYLIST = RGBColor(0x3E, 0x50, 0x6B)


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def not_equal(sl, x, y, size=44, color=GOLD, bar=7):
    """The not-equal sign, drawn.

    No font in the repository contains U+2260, so the glyph in the approved
    copy cannot be typeset in the brand faces. It is drawn instead, which keeps
    the mark editable and on-palette rather than substituting another character
    or a non-brand font. Same method approved for Video 5.
    """
    gap = size * 0.30
    rect(sl, x, y, size, bar, fill=color)
    rect(sl, x, y + gap, size, bar, fill=color)
    rect(sl, x + size / 2 - bar / 2, y - size * 0.34, bar, size * 1.05,
         fill=color, rot=22)


# ------------------------------------------------------------------ slide 1
def slide_01(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    block(sl, 160, 286, 1580, [
        ("MORE RESPONSIBILITY\nCAN MEAN GROWTH.",
         dict(size=68, bold=True, color=CREAM, spacing=1.14)),
    ])
    block(sl, 160, 500, 1580, [
        ("IT CAN ALSO MEAN\nYOU ABSORB MORE.",
         dict(size=68, bold=True, color=CREAM, spacing=1.14)),
    ])
    if step >= 2:
        hairline(sl, 160, 726, 300, color=GOLD, h=4)
        block(sl, 160, 788, 620, [("BUSIER",
                                   dict(size=54, bold=True, color=GOLD,
                                        tracking=2.4))])
        not_equal(sl, 452, 800, size=44, bar=7)
        block(sl, 550, 788, 1200, [("MORE CAPABLE.",
                                    dict(size=54, bold=True, color=GOLD,
                                         tracking=2.4))])
    notes(sl, """Timing: approximately 0:30.

First visual after the hook. Begin full screen on Temidayo; this lands only
after the opening distinction and viewer promise.

Reveal the first two statements together, then the final distinction.

The not-equal sign is drawn rather than typeset: no brand font contains that
glyph.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    """Stacked bands, not a side-by-side. Video 5 already owns the column pair."""
    bg(sl, CREAM)
    block(sl, 160, 210, 1600, [("MORE WORK", dict(size=64, bold=True,
                                                  color=NAVY, spacing=1.05))])
    hairline(sl, 160, 308, 200, color=RULE_CREAM, h=4)
    block(sl, 160, 360, 1600, [("Volume • coordination • availability",
                                dict(size=46, font=BODY, color=NAVY_DIM,
                                     spacing=1.3))])
    if step >= 2:
        rect(sl, 0, 500, W, 360, fill=NAVY)
        block(sl, 160, 560, 1600, [("REAL GROWTH", dict(size=64, bold=True,
                                                        color=CREAM,
                                                        spacing=1.05))])
        hairline(sl, 160, 658, 200, color=GOLD, h=4)
        block(sl, 160, 710, 1600, [("Complexity • judgment • portable evidence",
                                    dict(size=46, font=BODY, color=CREAM,
                                         spacing=1.3))])
    notes(sl, """Timing: approximately 1:15.

Reveal MORE WORK first, on its own, while the point about volume is made.

Then the navy band brings REAL GROWTH in underneath and lets it carry the
weight. Stacked rather than side by side, so this reads differently from the
Video 5 comparison slide.""")


# ------------------------------------------------------------------ slide 3
TESTS = ["DID THE PROBLEM BECOME\nMORE COMPLEX?",
         "DID YOUR AUTHORITY EXPAND?",
         "WHAT RETURN DID THE\nWORK CREATE?"]

def slide_03(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    y = 214
    for i, q in enumerate(TESTS):
        if i + 1 <= step:
            block(sl, 150, y + 4, 110, [("%d" % (i + 1),
                                         dict(size=48, bold=True, color=GOLD,
                                              spacing=1.0))])
            block(sl, 300, y, 1470, [(q, dict(size=54, bold=True, color=CREAM,
                                              spacing=1.14))])
            if i < 2:
                hairline(sl, 150, y + 196, 1620, color=DIM_ON_NAVY, h=2)
        y += 244
    notes(sl, """Timing: approximately 2:20.

Reveal one test at a time, then hold the complete list.

Complexity, authority, return. These are the three the rest of the video runs
on, so let each land before the next arrives.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=1):
    """Muted left, full-weight right. The right side carries the stronger weight."""
    bg(sl, CREAM)
    muted = step >= 2
    block(sl, 160, 452, 780, [
        ("MORE UNITS\nOF THE SAME\nPROBLEM",
         dict(size=52, bold=True,
              color=DIM_ON_CREAM if muted else NAVY, spacing=1.16)),
    ])
    if muted:
        block(sl, 962, 522, 180, [("versus", dict(size=38, font=BODY,
                                                  color=GOLD, spacing=1.0))])
        hairline(sl, 1150, 396, 620, color=GOLD, h=5)
        block(sl, 1150, 444, 640, [
            ("NEW VARIABLES •\nAMBIGUITY •\nTRADEOFFS",
             dict(size=56, bold=True, color=NAVY, spacing=1.16)),
        ])
    notes(sl, """Timing: approximately 2:20 to 4:35.

State one holds the left side alone: more units of the same problem.

State two mutes the left, brings "versus" forward and lands the right side at
full weight. The right side carries the stronger visual weight, as specified.

Repetition can build speed and reliability. It does not expand range forever.""")


# ------------------------------------------------------------------ slide 5
def slide_05(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    block(sl, 160, 366, 1600, [
        ("WHAT CAN YOU DO NOW\nTHAT YOU COULD NOT\nCREDIBLY DO BEFORE?",
         dict(size=76, bold=True, color=CREAM, spacing=1.18)),
    ])
    hairline(sl, 160, 754, 300, color=GOLD, h=5)
    notes(sl, """Timing: approximately 4:00.

Brief full-screen question. Hold it, then return to Temidayo.

If the only answer is that you can do more of the same thing, that is capacity
use. Do not automatically call it career growth.""")


# ------------------------------------------------------------------ slide 6
PAIR = [("ACCOUNTABILITY", "What you answer for"),
        ("AUTHORITY", "What you can influence or decide")]

def slide_06(sl, step=1):
    """Stacked definition rows, revealed in two parts."""
    bg(sl, CREAM)
    y = 300
    for i, (head, sub) in enumerate(PAIR):
        if i + 1 <= step:
            block(sl, 160, y, 1600, [(head, dict(size=64, bold=True,
                                                 color=NAVY, spacing=1.05))])
            block(sl, 160, y + 108, 1600, [(sub, dict(size=48, font=BODY,
                                                      color=NAVY_DIM,
                                                      spacing=1.3))])
            if i == 0:
                hairline(sl, 160, y + 216, 1600, color=RULE_CREAM, h=2)
        y += 290
    notes(sl, """Timing: approximately 4:35 to 6:55.

Two-part reveal. Accountability first, then authority.

Definitions are held large enough for phone viewing. These do not always expand
together, and that gap is the whole point of the test.""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    block(sl, 160, 330, 1600, [
        ("ACCOUNTABILITY\nWITHOUT AUTHORITY",
         dict(size=76, bold=True, color=CREAM, spacing=1.14)),
    ])
    hairline(sl, 160, 590, 300, color=GOLD, h=5)
    block(sl, 160, 652, 1600, [
        ("IS A WARNING—NOT A\nDEVELOPMENT PLAN.",
         dict(size=60, bold=True, color=GOLD, spacing=1.16)),
    ])
    notes(sl, """Timing: approximately 6:20.

Restrained navy statement slide. No red treatment, no warning symbol; the
weight comes from the type and the gold, nothing else.

Exposure can be useful. Sustained accountability without growing decision
rights is not a development plan.""")


# ------------------------------------------------------------------ slide 8
RETURNS = ["CAPABILITY", "EVIDENCE", "RECOGNITION"]

def slide_08(sl, step=1):
    bg(sl, CREAM)
    block(sl, 160, 236, 1600, [("WHAT DID THE WORK RETURN?",
                                dict(size=58, bold=True, color=NAVY,
                                     spacing=1.08))])
    hairline(sl, 160, 336, 240, color=GOLD, h=5)
    y = 430
    for i, item in enumerate(RETURNS):
        if i + 1 <= step:
            block(sl, 160, y + 6, 90, [("0%d" % (i + 1),
                                        dict(size=30, bold=True, color=GOLD,
                                             spacing=1.0))])
            block(sl, 300, y, 1470, [(item, dict(size=60, bold=True,
                                                 color=NAVY, spacing=1.05))])
            if i < 2:
                hairline(sl, 160, y + 128, 1610, color=RULE_CREAM, h=2)
        y += 190
    notes(sl, """Timing: approximately 6:55 to 9:10.

Reveal the three returns sequentially as each is defined.

Capability, evidence, recognition. Some worthwhile assignments will be stronger
in one than another; the question is whether the return is real and whether the
time boundary is clear.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    """Two results with clear vertical separation. The lower one is not punitive."""
    bg(sl, NAVY)
    gold_frame(sl)
    block(sl, 160, 250, 1600, [("COMPLEXITY ↑  AUTHORITY ↑  RETURN ↑",
                                dict(size=48, bold=True, color=CREAM,
                                     spacing=1.1))])
    hairline(sl, 160, 340, 200, color=GOLD, h=5)
    block(sl, 160, 392, 1600, [("REAL GROWTH", dict(size=76, bold=True,
                                                    color=GOLD, spacing=1.05))])
    if step >= 2:
        hairline(sl, 160, 578, 1600, color=DIM_ON_NAVY, h=2)
        block(sl, 160, 646, 1600, [("VOLUME ↑ ONLY",
                                    dict(size=48, bold=True, color=CREAM,
                                         spacing=1.1))])
        hairline(sl, 160, 736, 200, color=DIM_ON_NAVY, h=5)
        block(sl, 160, 788, 1600, [("MORE LOAD", dict(size=76, bold=True,
                                                      color=CREAM_DIM,
                                                      spacing=1.05))])
    notes(sl, """Timing: approximately 9:10 to 10:20.

Clear vertical separation between the two readings.

The lower result is deliberately not punitive or alarmist: cream-dim on navy,
a muted rule, no red. More load may be acceptable for a short season. It just
needs a boundary and a review date.""")


# ----------------------------------------------------------------- slide 10
ASKS = ["What should come off my plate?",
        "Which decisions belong to me?",
        "How and when will this scope be reviewed?"]

def slide_10(sl, step=1):
    bg(sl, CREAM)
    block(sl, 160, 226, 1620, [("ASK BEFORE THE SCOPE\nEXPANDS AGAIN",
                                dict(size=56, bold=True, color=NAVY,
                                     spacing=1.12))])
    hairline(sl, 160, 400, 240, color=GOLD, h=5)
    y = 486
    for i, q in enumerate(ASKS):
        if i + 1 <= step:
            hairline(sl, 160, y + 30, 52, color=GOLD, h=4)
            block(sl, 258, y, 1520, [(q, dict(size=48, bold=True, color=NAVY,
                                              spacing=1.2))])
        y += 146
    notes(sl, """Timing: approximately 10:20 to 11:15.

Reveal the three questions one at a time.

This is a stronger conversation than saying only that there is too much work.
It discusses priorities, authority, support and recognition using the actual
design of the role.""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    block(sl, 160, 330, 1600, [
        ("CAPABILITY FORMATION\nFIELD KIT",
         dict(size=84, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 160, 566, 300, color=GOLD, h=5)
    block(sl, 160, 630, 1560, [
        ("What is your work building in you?",
         dict(size=50, font=BODY, color=CREAM, spacing=1.3)),
    ])
    block(sl, 160, 782, 1560, [
        ("temidayoafonja.com/fieldkit",
         dict(size=60, bold=True, color=GOLD, spacing=1.15)),
    ], h=82)
    notes(sl, """Timing: approximately 11:15 to 11:45.

Simple CTA card. No competing offer and no QR code. This is the only CTA in the
video: no Career Decision Evidence Check, no Keep the Proof, no book or
workshop.""")


# ----------------------------------------------------------------- slide 12
def slide_12(sl, step=1):
    bg(sl, CREAM)
    eyebrow(sl, 160, 250, "Watch next", color=GOLD, w=900)
    block(sl, 160, 316, 940, [
        ("HOW TO PROVE THE\nVALUE OF WORK\nTHAT HAD NO BLUEPRINT",
         dict(size=58, bold=True, color=NAVY, spacing=1.16)),
    ])
    hairline(sl, 160, 634, 240, color=GOLD, h=4)
    block(sl, 160, 686, 940, [
        ("Playlist: Career Portability: Career Pivots,\nInternal Moves & Growth",
         dict(size=44, bold=True, color=PLAYLIST, spacing=1.32)),
    ])
    notes(sl, """Timing: final 15 to 20 seconds.

Routes to Video 7, How to Prove the Value of Work That Had No Blueprint.

All content is held left of x=1130 so the right side stays clear for YouTube
end-screen elements.

Closing line: more work can be part of growth, but it is not proof of it.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11, 12: slide_12}
