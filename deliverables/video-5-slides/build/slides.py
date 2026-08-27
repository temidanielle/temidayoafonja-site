"""Video 5: "Should I Make an Internal Move? 3 Questions to Decide"  Twelve slides.

Built in the approved Capability Formation system, using the Video 4 deck as the
visual master: deep navy ground, warm cream typography, muted gold accents, thin
gold rules, generous negative space, restrained editorial treatment.

Every word on every slide is copied verbatim from Section 5 of the Video 5
production package. Nothing is rewritten, expanded or summarised, and no Video 4
wording or subject matter is carried over.

No opening title card. The video begins full screen on Temidayo; slide 1 is the
first teaching visual and lands only after the opening promise.
"""
import os
from deck import *

# Slide number -> number of progressive reveal states.
# The package specifies reveals for 1, 2, 4, 6, 8, 9 and 10 only. Total 25.
STEPS = {1: 2, 2: 3, 3: 1, 4: 4, 5: 1, 6: 2, 7: 1, 8: 3, 9: 3, 10: 3,
         11: 1, 12: 1}

TITLES = {
    1:  "Core distinction",
    2:  "The three questions",
    3:  "Question 1, will the work change",
    4:  "Access test",
    5:  "Question 2, will your judgment expand",
    6:  "Critical distinction, tasks and judgment",
    7:  "Question 3, will the evidence travel",
    8:  "Portable evidence",
    9:  "Decision read",
    10: "Conversation prompts",
    11: "Primary CTA, Career Decision Evidence Check",
    12: "Watch next",
}

SLUGS = {
    1: "core-distinction", 2: "the-three-questions", 3: "q1-will-the-work-change",
    4: "access-test", 5: "q2-will-your-judgment-expand",
    6: "more-tasks-more-judgment", 7: "q3-will-the-evidence-travel",
    8: "portable-evidence", 9: "decision-read", 10: "conversation-prompts",
    11: "career-decision-evidence-check", 12: "watch-next",
}

DIM_ON_NAVY = RGBColor(0x63, 0x74, 0x8C)
PLAYLIST = RGBColor(0x3E, 0x50, 0x6B)


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def not_equal(sl, x, y, size=34, color=GOLD, bar=6):
    """The not-equal sign, drawn.

    No font in the repository contains U+2260, so the glyph in the approved
    copy cannot be typeset in the brand faces. It is drawn instead, which keeps
    the mark editable and on-palette rather than substituting another character
    or a non-brand font.
    """
    gap = size * 0.30
    rect(sl, x, y, size, bar, fill=color)
    rect(sl, x, y + gap, size, bar, fill=color)
    rect(sl, x + size / 2 - bar / 2, y - size * 0.34, bar, size * 1.05,
         fill=color, rot=22)


def question_header(sl, num, head, sub=None, on_navy=True):
    """The numbered question marker, identical across slides 3, 5 and 7."""
    c_head = CREAM if on_navy else NAVY
    block(sl, 136, 168, 200, [(num, dict(size=88, bold=True, color=GOLD,
                                         spacing=1.0))])
    hairline(sl, 136, 290, 92, color=GOLD, h=4)
    block(sl, 136, 342, 1600, [(head, dict(size=62, bold=True, color=c_head,
                                           spacing=1.12))])
    if sub:
        block(sl, 136, 560, 1620, [(sub, dict(size=44, font=BODY,
                                              color=CREAM if on_navy else NAVY_DIM,
                                              spacing=1.3))])


# ------------------------------------------------------------------ slide 1
def slide_01(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    block(sl, 160, 300, 1560, [
        ("A DIFFERENT EMPLOYER\nIS NOT THE ONLY WAY TO\nACCESS DIFFERENT WORK.",
         dict(size=72, bold=True, color=CREAM, spacing=1.14)),
    ])
    if step >= 2:
        hairline(sl, 160, 690, 300, color=GOLD, h=4)
        block(sl, 160, 754, 700, [("INTERNAL MOVE",
                                   dict(size=36, bold=True, color=CREAM,
                                        tracking=2.6))])
        not_equal(sl, 640, 768)
        block(sl, 716, 754, 900, [("AUTOMATIC GROWTH.",
                                   dict(size=36, bold=True, color=CREAM,
                                        tracking=2.6))])
    notes(sl, """Timing: approximately 0:25.

Begin full screen on Temidayo. This is the first teaching visual and it lands
only after the opening promise.

State one holds the main statement. Reveal the second line after the first
statement has been made.

The not-equal sign is drawn rather than typeset: no brand font contains that
glyph.""")


# ------------------------------------------------------------------ slide 2
QUESTIONS = ["WILL THE WORK CHANGE?", "WILL YOUR JUDGMENT EXPAND?",
             "WILL THE EVIDENCE TRAVEL?"]

def slide_02(sl, step=1):
    bg(sl, CREAM)
    y = 250
    for i, q in enumerate(QUESTIONS):
        if i + 1 <= step:
            block(sl, 160, y + 6, 100, [("%d" % (i + 1),
                                         dict(size=46, bold=True, color=GOLD,
                                              spacing=1.0))])
            block(sl, 300, y, 1500, [(q, dict(size=58, bold=True, color=NAVY,
                                              spacing=1.1))])
            if i < 2:
                hairline(sl, 160, y + 134, 1600, color=RULE_CREAM, h=2)
        y += 208
    notes(sl, """Timing: approximately 0:38.

Reveal one question at a time as each is named. These are the three tests the
whole video runs on, so let each land before the next arrives.

Do not put the answers here. The questions alone.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    question_header(sl, "1", "WILL THE WORK CHANGE?",
                    "What will be different on an ordinary Monday?")
    notes(sl, """Timing: approximately 2:35 to 4:40.

Section break. Hold briefly, then return to presenter.

The point being carried: do not begin with the title. Ask what will actually be
different on an ordinary Monday.""")


# ------------------------------------------------------------------ slide 4
ACCESS = ["NEW PROBLEMS", "NEW SYSTEMS", "NEW STAKEHOLDERS", "NEW CONTEXT"]

def slide_04(sl, step=1):
    bg(sl, CREAM)
    y = 236
    for i, item in enumerate(ACCESS):
        if i + 1 <= step:
            hairline(sl, 160, y + 34, 56, color=GOLD, h=5)
            block(sl, 262, y, 1500, [(item, dict(size=62, bold=True, color=NAVY,
                                                 spacing=1.05))])
        y += 158
    notes(sl, """Timing: approximately 3:05.

Reveal one line at a time as each is named.

These are the four things to look for before calling a move real access. If
none of them can be named, the first answer may be no.""")


# ------------------------------------------------------------------ slide 5
def slide_05(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    question_header(sl, "2", "WILL YOUR JUDGMENT\nEXPAND?",
                    "What will you notice, weigh, recommend or own?")
    notes(sl, """Timing: approximately 4:40 to 6:45.

Section break.

This is where more responsibility can be misleading. More volume is not more
judgment.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=1):
    bg(sl, CREAM)
    x1, x2, col_w = 190, 1075, 660
    block(sl, x1, 400, col_w, [("MORE TASKS", dict(size=54, bold=True,
                                                   color=NAVY, spacing=1.05))])
    hairline(sl, x1, 490, 170, color=RULE_CREAM, h=4)
    block(sl, x1, 542, col_w, [("Volume • Coordination • Absorption",
                                dict(size=38, font=BODY, color=NAVY_DIM,
                                     spacing=1.34))])
    if step >= 2:
        rect(sl, 985, 316, 800, 404, fill=NAVY)
        block(sl, x2, 400, col_w, [("MORE JUDGMENT",
                                    dict(size=54, bold=True, color=CREAM,
                                         spacing=1.05))])
        hairline(sl, x2, 490, 170, color=GOLD, h=4)
        block(sl, x2, 542, col_w, [("Interpretation • Tradeoffs • Consequence",
                                    dict(size=38, font=BODY, color=CREAM,
                                         spacing=1.34))])
    notes(sl, """Timing: approximately 5:05.

Show MORE TASKS first, on its own, while the point about volume is made.

Then contrast with MORE JUDGMENT and let it carry the weight. Neither example
makes the operational task unimportant. The distinction is what the work is
forming.""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    question_header(sl, "3", "WILL THE EVIDENCE\nTRAVEL?",
                    "Can you explain the work beyond internal language?")
    notes(sl, """Timing: approximately 6:45 to 8:50.

Section break.

Internal credibility can be powerful inside one company and almost invisible
outside it. Portable evidence does not mean taking confidential material.""")


# ------------------------------------------------------------------ slide 8
EVIDENCE = [("RESULT", "What changed?"),
            ("JUDGMENT", "What did you notice or decide?"),
            ("RANGE", "What new context can you now handle?")]

def slide_08(sl, step=1):
    bg(sl, CREAM)
    y = 250
    for i, (head, sub) in enumerate(EVIDENCE):
        if i + 1 <= step:
            block(sl, 160, y, 500, [(head, dict(size=52, bold=True, color=NAVY,
                                                spacing=1.05))])
            block(sl, 680, y + 12, 1080, [(sub, dict(size=42, font=BODY,
                                                     color=NAVY_DIM,
                                                     spacing=1.3))])
            if i < 2:
                hairline(sl, 160, y + 118, 1600, color=RULE_CREAM, h=2)
        y += 190
    notes(sl, """Timing: approximately 7:30.

Reveal Result, Judgment and Range sequentially.

A move becomes more portable when it creates all three.""")


# ------------------------------------------------------------------ slide 9
READS = [("3 YES", "STRONG GROWTH CASE"),
         ("2 YES", "INVESTIGATE OR NEGOTIATE"),
         ("0-1 YES", "MOVEMENT, NOT MUCH FORMATION")]

def slide_09(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    y = 262
    for i, (k, v) in enumerate(READS):
        if i + 1 <= step:
            block(sl, 160, y, 380, [(k, dict(size=56, bold=True, color=GOLD,
                                             spacing=1.05))])
            block(sl, 610, y + 6, 1180, [(v, dict(size=48, bold=True,
                                                  color=CREAM, spacing=1.1))])
            if i < 2:
                hairline(sl, 160, y + 132, 1600, color=DIM_ON_NAVY, h=2)
        y += 206
    notes(sl, """Timing: approximately 8:50.

Reveal rows one at a time.

Two yeses is not a rejection. Identify the missing dimension and investigate
whether it can be designed into the move.

Zero or one yes may still be the right choice for pay, flexibility, stability
or a better manager. Just not a formation case.""")


# ----------------------------------------------------------------- slide 10
PROMPTS = ["What problems will I own in the first six months?",
           "Which decisions belong to this role?",
           "How will success be measured?"]

def slide_10(sl, step=1):
    bg(sl, CREAM)
    y = 268
    for i, q in enumerate(PROMPTS):
        if i + 1 <= step:
            block(sl, 160, y + 4, 100, [("0%d" % (i + 1),
                                         dict(size=30, bold=True, color=GOLD,
                                              spacing=1.0))])
            block(sl, 288, y - 10, 1500, [(q, dict(size=48, bold=True,
                                                   color=NAVY, spacing=1.2))])
            if i < 2:
                hairline(sl, 160, y + 128, 1600, color=RULE_CREAM, h=2)
        y += 190
    notes(sl, """Timing: approximately 9:30.

Progressive reveal, one prompt at a time.

These are for the internal hiring conversation. Listen for concrete work, not
encouraging adjectives.""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    block(sl, 160, 330, 1600, [
        ("CAREER DECISION\nEVIDENCE CHECK",
         dict(size=84, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 160, 566, 300, color=GOLD, h=5)
    block(sl, 160, 622, 1560, [
        ("A free next step for an active stay,\ninternal-move or leave decision",
         dict(size=42, font=BODY, color=CREAM, spacing=1.3)),
    ])
    block(sl, 160, 800, 1560, [
        ("temidayoafonja.com/career-decisions",
         dict(size=56, bold=True, color=GOLD, spacing=1.15)),
    ], h=76)
    notes(sl, """Timing: approximately 11:20.

Simple CTA card. No competing offer on screen. Do not add Keep the Proof or the
Capability Formation Field Kit.

PUBLICATION GATE: temidayoafonja.com/career-decisions is not live yet. The page
must exist before Video 5 is published.""")


# ----------------------------------------------------------------- slide 12
def slide_12(sl, step=1):
    bg(sl, CREAM)
    eyebrow(sl, 160, 250, "Watch next", color=GOLD, w=900)
    block(sl, 160, 316, 940, [
        ("ARE YOU GROWING—\nOR JUST BEING GIVEN\nMORE WORK?",
         dict(size=62, bold=True, color=NAVY, spacing=1.16)),
    ])
    hairline(sl, 160, 634, 240, color=GOLD, h=4)
    block(sl, 160, 686, 940, [
        ("Playlist: Career Portability: Career Pivots,\nInternal Moves & Growth",
         dict(size=38, bold=True, color=PLAYLIST, spacing=1.32)),
    ])
    notes(sl, """Timing: final 15 to 20 seconds.

All content is held left of x=1130 so the right side stays clear for YouTube
end-screen elements.

Closing line: you may not need to leave, but you do need different work.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11, 12: slide_12}
