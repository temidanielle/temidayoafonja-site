"""Video 4: "How to Explain Your Career Change"  Eleven slides.

Built in the approved Capability Formation system, using Video 1 v2.4 as the
master visual reference: deep navy ground, warm cream typography, muted gold
accents, thin gold rules, generous negative space, restrained editorial
treatment.

Every word on every slide is copied verbatim from Section 5 of the Video 4
production package. Nothing is rewritten, expanded or summarised.

No opening title card. The video begins full screen on Temidayo and the first
teaching visual is slide 1, the career path.
"""
import os
from deck import *

# Slide number -> number of progressive reveal states.
# The package specifies reveals for 1, 2, 4, 5, 6, 7 and 9 only.
STEPS = {1: 4, 2: 2, 3: 1, 4: 5, 5: 2, 6: 3, 7: 3, 8: 1, 9: 3, 10: 1, 11: 1}

TITLES = {
    1:  "Career path",
    2:  "Core distinction, chronology and portability",
    3:  "Part 1, name the chapters briefly",
    4:  "Part 2, find the repeated work",
    5:  "Look beneath the nouns",
    6:  "Part 3, explain the direction",
    7:  "Three-sentence structure",
    8:  "Honesty boundary",
    9:  "Explanation test",
    10: "Primary CTA, Keep the Proof",
    11: "Watch next",
}

SLUGS = {
    1: "career-path", 2: "chronology-and-portability",
    3: "part-1-name-the-chapters", 4: "part-2-find-the-repeated-work",
    5: "look-beneath-the-nouns", 6: "part-3-explain-the-direction",
    7: "three-sentence-structure", 8: "honesty-boundary",
    9: "explanation-test", 10: "keep-the-proof", 11: "watch-next",
}

def arrow_down(sl, x, y, length=58, color=GOLD, stem=3, head_w=20, head_h=15):
    """A drawn directional arrow. The brand fonts contain no U+2192 glyph, and
    the brief calls for simple directional lines and arrows, so the path marker
    is a vector shape rather than a substituted character or a foreign font."""
    rect(sl, x, y, stem, length - head_h, fill=color)
    rect(sl, x - head_w / 2 + stem / 2, y + length - head_h, head_w, head_h,
         fill=color, shape="tri_down")
DIM_ON_NAVY = RGBColor(0x63, 0x74, 0x8C)
DIM_ON_CREAM = RGBColor(0xA8, 0xAF, 0xBC)


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl, color=GOLD):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=color, lw=2)


def part_header(sl, num, head, on_navy=True):
    """The numbered part marker, identical across slides 3, 4 and 6."""
    c_head = CREAM if on_navy else NAVY
    block(sl, 136, 150, 200, [(num, dict(size=88, bold=True, color=GOLD,
                                         spacing=1.0))])
    hairline(sl, 136, 272, 92, color=GOLD, h=4)
    block(sl, 136, 320, 1560, [(head, dict(size=64, bold=True, color=c_head,
                                           spacing=1.12))])


# ------------------------------------------------------------------ slide 1
CHAPTERS = ["ACCOUNTING & AUDIT", "CYBERSECURITY", "PEOPLE STRATEGY",
            "ENTERPRISE TRANSFORMATION"]

def slide_01(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    y = 232
    for i, chapter in enumerate(CHAPTERS):
        if i + 1 <= step:
            block(sl, 208, y, 1500, [(chapter, dict(size=58, bold=True,
                                                    color=CREAM, spacing=1.0))])
        y += 76
        if i < len(CHAPTERS) - 1:
            if i + 1 < step:
                arrow_down(sl, 216, y + 10, length=56)
            y += 80
    if step >= len(CHAPTERS):
        hairline(sl, 200, 862, 300, color=GOLD, h=3)
        block(sl, 200, 900, 1520, [
            ("THE TITLES CHANGED. THE CAPABILITY KEPT ACCUMULATING.",
             dict(size=26, bold=True, color=CREAM_DIM, tracking=3.4)),
        ])
    notes(sl, """Timing: approximately 0:35 to 2:35.

Begin full screen on Temidayo. This is the first teaching visual and it
appears only after the viewer payoff and the early proof beat.

Reveal one chapter at a time as the path is narrated, then hold the full path
while the recurring work underneath is described.

The footer lands last, on the complete path.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    bg(sl, CREAM)
    x1, x2, col_w = 190, 1075, 660
    block(sl, x1, 430, col_w, [("CHRONOLOGY", dict(size=56, bold=True,
                                                   color=NAVY, spacing=1.05))])
    hairline(sl, x1, 522, 170, color=RULE_CREAM, h=4)
    block(sl, x1, 574, col_w, [("Where you have been",
                                dict(size=36, font=BODY, color=NAVY_DIM,
                                     spacing=1.3))])
    if step >= 2:
        rect(sl, 985, 340, 800, 380, fill=NAVY)
        block(sl, x2, 430, col_w, [("PORTABILITY", dict(size=56, bold=True,
                                                        color=CREAM,
                                                        spacing=1.05))])
        hairline(sl, x2, 522, 170, color=GOLD, h=4)
        block(sl, x2, 574, col_w, [("What traveled with you",
                                    dict(size=36, font=BODY, color=CREAM_DIM,
                                         spacing=1.3))])
    notes(sl, """Timing: approximately 1:05.

Two-column comparison. Chronology first, on its own, while the point about
giving someone the chronology is made.

Bring PORTABILITY in second and let it carry the weight. It is the half the
listener is not being given.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    part_header(sl, "1", "NAME THE CHAPTERS — BRIEFLY")
    block(sl, 136, 470, 1560, [("Roles • Functions • Industries",
                                dict(size=40, font=BODY, color=CREAM_DIM,
                                     spacing=1.3))])
    hairline(sl, 136, 566, 1200, color=DIM_ON_NAVY, h=2)
    block(sl, 136, 614, 1560, [("One sentence, not a defense.",
                                dict(size=38, font=BODY, color=GOLD,
                                     spacing=1.3))])
    notes(sl, """Timing: approximately 2:35 to 3:35.

Section break. Hold briefly, then return to presenter.

The point being carried: orient the listener, do not defend every decision or
recite every position. Enough chronology to establish the shape of the path,
short enough that there is room left to explain what the chapters built.""")


# ------------------------------------------------------------------ slide 4
VERBS = ["NOTICE", "TRANSLATE", "BUILD", "DECIDE"]

def slide_04(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    part_header(sl, "2", "FIND THE REPEATED WORK")
    shown = min(step, len(VERBS))
    if shown:
        block(sl, 136, 492, 1660, [
            (" • ".join(VERBS[:shown]),
             dict(size=50, bold=True, color=CREAM, spacing=1.0)),
        ])
    if step >= 5:
        hairline(sl, 136, 660, 1200, color=DIM_ON_NAVY, h=2)
        block(sl, 136, 712, 1600, [
            ("What did people repeatedly trust you to carry?",
             dict(size=46, bold=True, color=GOLD, spacing=1.22)),
        ])
    notes(sl, """Timing: approximately 3:35 to 5:10.

Reveal the verbs one at a time as they are named. Verbs reveal portability
where titles, industries and internal terminology create separation.

The question lands last, after all four verbs are on screen.

Each verb needs evidence. A portable capability is not a word you like; it is
something your work repeatedly required you to demonstrate.""")


# ------------------------------------------------------------------ slide 5
NOUNS = ["JOB TITLES", "COMPANY LANGUAGE", "INDUSTRY VOCABULARY"]

def slide_05(sl, step=1):
    bg(sl, CREAM)
    muted = step >= 2
    y = 250
    for noun in NOUNS:
        block(sl, 160, y, 1200, [
            (noun, dict(size=48, bold=True,
                        color=DIM_ON_CREAM if muted else NAVY, spacing=1.05)),
        ])
        y += 104
    if muted:
        hairline(sl, 160, 600, 1400, color=GOLD, h=4)
        block(sl, 160, 660, 1620, [
            ("What did you notice, decide, solve,\ninfluence or change?",
             dict(size=58, bold=True, color=NAVY, spacing=1.18)),
        ])
    notes(sl, """Timing: approximately 4:00.

State one: the three nouns as they normally arrive, at full weight.

State two: mute the noun list and bring the question forward. The nouns stay
on screen, dimmed, so the viewer sees what is being set aside rather than
watching it disappear.""")


# ------------------------------------------------------------------ slide 6
STAGES = ["PAST CHAPTERS", "REPEATED CAPABILITY", "NEXT VALUE"]

def slide_06(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    part_header(sl, "3", "EXPLAIN THE DIRECTION")
    y = 512
    for i, stage in enumerate(STAGES):
        if i + 1 <= step:
            block(sl, 208, y, 1400, [(stage, dict(size=54, bold=True,
                                                  color=CREAM, spacing=1.0))])
        y += 72
        if i < len(STAGES) - 1:
            if i + 1 < step:
                arrow_down(sl, 216, y + 8, length=52)
            y += 74
    notes(sl, """Timing: approximately 5:10 to 6:45.

Simple directional build, one stage at a time.

The third part is to explain why the work you want next follows from what you
have already built. This is the shape of that argument, nothing more.""")


# ------------------------------------------------------------------ slide 7
STEMS = ["My career has moved across…",
         "Across those chapters, I kept being asked to…",
         "That is why I am now focused on…"]

def slide_07(sl, step=1):
    bg(sl, CREAM)
    y = 300
    for i, stem in enumerate(STEMS):
        if i + 1 <= step:
            hairline(sl, 160, y + 4, 60, color=GOLD, h=4)
            block(sl, 260, y - 18, 1520, [
                (stem, dict(size=48, bold=True, color=NAVY, spacing=1.2)),
            ])
        y += 172
    notes(sl, """Timing: approximately 5:30.

Reveal one sentence stem at a time.

This is an editing frame, not a script to memorise. It keeps the speaker from
spending three minutes on chronology and ten seconds on meaning.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    block(sl, 160, 320, 1600, [
        ("DO NOT INVENT\nA PERFECT PLAN.",
         dict(size=86, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 160, 606, 300, color=GOLD, h=4)
    block(sl, 160, 660, 1600, [
        ("Name the constraint, experiment or redirection.",
         dict(size=40, font=BODY, color=CREAM_DIM, spacing=1.32)),
        ("Explain what became clearer.",
         dict(size=40, font=BODY, color=CREAM_DIM, spacing=1.32,
              space_before=18)),
    ])
    notes(sl, """Timing: approximately 6:45 to 7:35.

Use this slide full screen briefly, then return to Temidayo.

Coherence is not the same as claiming every move was strategic. A truthful
explanation can include interruption and redirection. The goal is not to make
the career look linear. The goal is to make the formation legible.""")


# ------------------------------------------------------------------ slide 9
TESTS = ["Can a stranger hear why the next move follows?",
         "Does it show ability — not only interest?",
         "Is there evidence behind each verb?"]

def slide_09(sl, step=1):
    bg(sl, CREAM)
    y = 292
    for i, q in enumerate(TESTS):
        if i + 1 <= step:
            block(sl, 160, y, 100, [("0%d" % (i + 1),
                                     dict(size=30, bold=True, color=GOLD,
                                          spacing=1.0))])
            block(sl, 280, y - 12, 1500, [
                (q, dict(size=50, bold=True, color=NAVY, spacing=1.2)),
            ])
            if i < len(TESTS) - 1:
                hairline(sl, 160, y + 118, 1600, color=RULE_CREAM, h=2)
        y += 178
    notes(sl, """Timing: approximately 8:05.

Progressive reveal with a brief pause between questions so each one can be
answered before the next arrives.

If the answer to any of them is no, the career may not be the problem. The
explanation may still be carrying too much chronology and not enough
portability.""")


# ----------------------------------------------------------------- slide 10
def slide_10(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    block(sl, 160, 372, 1500, [
        ("KEEP THE PROOF", dict(size=92, bold=True, color=CREAM, spacing=1.05)),
    ])
    hairline(sl, 160, 500, 300, color=GOLD, h=5)
    block(sl, 160, 556, 1500, [
        ("A 60-Minute Career Evidence System",
         dict(size=44, font=BODY, color=CREAM_DIM, spacing=1.3)),
    ])
    block(sl, 160, 660, 1500, [
        ("temidayoafonja.com/keep-the-proof",
         dict(size=38, bold=True, color=GOLD, spacing=1.2)),
    ])
    notes(sl, """Timing: approximately 8:38.

Simple CTA card. No competing offer on screen.

Keep the Proof does not decide the next move. It preserves what will be needed
to explain the value once the context changes.

ROUTE CHECK: temidayoafonja.com/keep-the-proof must resolve before publication.""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=1):
    bg(sl, CREAM)
    eyebrow(sl, 160, 250, "Watch next", color=GOLD, w=900)
    block(sl, 160, 316, 900, [
        ("HOW TO KNOW IF\nAN INTERNAL MOVE IS\nTHE RIGHT NEXT STEP",
         dict(size=62, bold=True, color=NAVY, spacing=1.16)),
    ])
    hairline(sl, 160, 634, 240, color=GOLD, h=4)
    block(sl, 160, 686, 900, [
        ("Playlist: Career Portability: Career Pivots,\nInternal Moves & Growth",
         dict(size=33, font=BODY, color=NAVY_DIM, spacing=1.34)),
    ])
    notes(sl, """Timing: final 15 to 20 seconds.

All content is held left of x=1130 so the right side stays clear for YouTube
end-screen elements.

Closing line: your career does not need to look linear to be coherent, but you
do have to make the continuity visible.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11}
