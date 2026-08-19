"""
Video 3: "Before You Quit Your Job, Check These 3 Things"  Thirteen slides.

Built in the approved Capability Formation system, using Video 1 v2.4 and
Video 2 v1.1 as visual, reveal and production precedent. Cream ground, deep
navy type, the lighter blue for one contrast moment, muted gold accent, rust
only as a small mark. One idea per slide, an upper-left presenter safe area on
every slide, progressive reveals only where they teach.

The three checks are three standalone section breaks at three separate
moments. They appear together once, on the recap, after all three are taught.

The safety boundary is stated on slide 2 and again in the speaker notes. It is
not softened anywhere.
"""
import os
from deck import *

# slide number -> number of progressive reveal steps.
# Section breaks (3, 5, 7) and the recap (9) never build.
STEPS = {1: 1, 2: 1, 3: 1, 4: 4, 5: 1, 6: 5, 7: 1, 8: 4, 9: 1, 10: 3, 11: 3,
         12: 1, 13: 1}

TITLES = {
    1: "Title",
    2: "Recognition, once you leave access changes",
    3: "Section break 01, preserve the evidence",
    4: "Check one, what to keep and what not to take",
    5: "Section break 02, name what the work built",
    6: "Check two, problem constraint judgment outcome",
    7: "Section break 03, test the next move",
    8: "Check three, uses something proven and builds something new",
    9: "Recap, all three checks together",
    10: "Decision reading, three directions",
    11: "Before you resign, three questions",
    12: "Career Decision Evidence Check",
    13: "Next-video bridge",
}

SLUGS = {
    1: "title", 2: "recognition-access-changes", 3: "section-01-preserve-evidence",
    4: "check-1-keep-and-not-take", 5: "section-02-name-what-built",
    6: "check-2-problem-constraint-judgment-outcome", 7: "section-03-test-next-move",
    8: "check-3-proven-and-new", 9: "recap-three-checks",
    10: "decision-reading", 11: "before-you-resign", 12: "career-decision-evidence-check",
    13: "next-video-bridge",
}


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def kicker_head(sl, kick, head, head_size=66, color=NAVY, sub=None,
                sub_color=None, kick_color=GOLD, sub_size=32):
    eyebrow(sl, TOP_X, TOP_Y, kick, color=kick_color, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W,
          [(head, dict(size=head_size, bold=True, color=color, spacing=1.1))])
    if sub:
        nlines = head.count("\n") + 1
        y = TOP_Y + 52 + nlines * head_size * 1.1 + 26
        block(sl, TOP_X, y, TOP_W,
              [(sub, dict(size=sub_size, font=BODY, color=sub_color or NAVY_DIM,
                          spacing=1.32))])


def numbered_rows(sl, items, step, y0, size=38, color=NAVY, rule=RULE_CREAM,
                  gap=52, x_num=120, x_text=240, w_text=1560, first=1):
    y = y0
    for i, text in enumerate(items):
        lines = text.count("\n") + 1
        h = lines * size * 1.2
        if i + first <= step:
            block(sl, x_num, y + 6, 90, [
                ("0%d" % (i + 1), dict(size=30, bold=True, color=GOLD, spacing=1.0)),
            ])
            block(sl, x_text, y, w_text, [
                (text, dict(size=size, bold=True, color=color, spacing=1.2)),
            ])
            if i < len(items) - 1:
                hairline(sl, x_num, y + h + gap / 2 - 6, x_text + w_text - x_num,
                         color=rule, h=2)
        y += h + gap


# ------------------------------------------------------------------ slide 1
def slide_01(sl, step=1):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    eyebrow(sl, 136, 462, "Video three  ·  Capability Formation", w=1400)
    block(sl, 136, 520, 1560, [
        ("3 Things to Do\nBefore Quitting\nYour Job",
         dict(size=96, bold=True, color=CREAM, spacing=1.08)),
    ])
    hairline(sl, 136, 890, 220, color=RUST, h=6)
    block(sl, 136, 930, 1200, [
        ("Temidayo Afonja  ·  temidayoafonja.com",
         dict(size=24, color=CREAM_DIM, bold=True, tracking=4)),
    ])
    notes(sl, """Timing: 0:00-0:50

Begin full-screen on Temidayo, not on this slide.

Open on the decision the viewer is already carrying: growth has stopped, the
conditions changed, another opportunity appeared, or the role no longer looks
like the right place to stay.

Give the payoff before the title appears. By the end they will know what
evidence to preserve before access changes, how to name what the work built,
and how to test whether the next move uses something proven while requiring
something genuinely new.

Then the brief channel line, then the title slide.

Do not make the opening alarmist and do not talk anyone out of leaving.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    bg(sl, CREAM)
    kicker_head(sl, "Before you resign", "Once you leave,\naccess changes.",
                head_size=60)
    block(sl, 120, 512, 1560, [
        ("Evidence, systems and people can become harder to reach.",
         dict(size=34, font=BODY, color=NAVY_DIM, spacing=1.35)),
    ])
    hairline(sl, 120, 660, 180, color=RUST, h=4)
    block(sl, 120, 706, 1560, [
        ("If your health or safety is at risk, or you are facing harassment or\n"
         "discrimination, this is not a reason to wait.",
         dict(size=30, bold=True, color=NAVY, spacing=1.38)),
    ])
    notes(sl, """Timing: 0:50-1:35

Speak from ideas, calmly. The point is timing, not fear. Most of what makes a
career decision legible is easiest to gather while you still have access.

State the safety boundary out loud, clearly, and do not soften it:

"If your health or safety is at risk, or you are facing harassment,
discrimination or another urgent threat, nothing in this video is a reason to
delay leaving. Please act on that first."

Then return to the viewer who has time to think, and say that the rest of the
video is for them.""")


# ------------------------------------------ slides 3, 5, 7: section breaks
def _section_intro(sl, number, statement, support, notes_text):
    bg(sl, CREAM)
    eyebrow(sl, 120, 452, "Three checks before you resign", w=1400)
    block(sl, 120, 500, 400, [
        ("0%d" % number, dict(size=160, bold=True, color=GOLD, spacing=1.0)),
    ])
    block(sl, 120, 690, 1500, [
        (statement, dict(size=76, bold=True, color=NAVY, spacing=1.14)),
    ])
    block(sl, 120, 900, 1500, [
        (support, dict(size=30, font=BODY, color=NAVY_DIM, spacing=1.3)),
    ])
    notes(sl, notes_text)


def section_01(sl, step=1):
    _section_intro(sl, 1, "Preserve the\nevidence", "Keep what is yours to keep.",
                   """Timing: 1:35-1:43

A section break, four to seven seconds. Say: "The first check is to preserve
the evidence."

Do not teach it here. The next slide carries it.

Only this check is on screen. The second and third come later, each in its own
moment.""")


def section_02(sl, step=1):
    _section_intro(sl, 2, "Name what\nthe work built",
                   "An achievement is useful when you understand what it proves.",
                   """Timing: 3:15-3:23

A section break, four to seven seconds. Say: "The second check is to name what
the work built."

Do not restate the first check.""")


def section_03(sl, step=1):
    _section_intro(sl, 3, "Test the\nnext move",
                   "Look for overlap between what is proven and what must still grow.",
                   """Timing: 4:55-5:03

A section break, four to seven seconds. Say: "The third check is to test the
next move."

Do not restate the first two.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Check one", "Preserve the evidence.", head_size=60,
                sub="Keep only what you are entitled to keep.")
    rect(sl, 120, 496, 820, 490, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 496, 820, color=GOLD, h=8)
    block(sl, 164, 540, 740, [
        ("Yours to keep", dict(size=24, bold=True, color=GOLD, tracking=4)),
    ])
    keep = [
        "Your own performance reviews",
        "Recognition you received",
        "Nonconfidential metrics already\nshared with you",
        "Project dates",
        "Scope of responsibility",
        "Permitted notes on decisions or\nproblems you helped resolve",
    ]
    y = 596
    for i, item in enumerate(keep):
        lines = item.count("\n") + 1
        if i // 2 + 1 <= step:
            block(sl, 164, y, 740, [
                (item, dict(size=27, bold=True, color=NAVY, spacing=1.24)),
            ])
        y += lines * 27 * 1.24 + 14

    if step >= 4:
        rect(sl, 980, 496, 820, 490, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, 980, 496, 820, color=RUST, h=8)
        block(sl, 1024, 540, 740, [
            ("Not yours to take", dict(size=24, bold=True, color=RUST, tracking=4)),
        ])
        y = 596
        for item in ["Confidential information", "Customer data", "Employee data",
                     "Proprietary documents",
                     "Anything employer-owned you have\nno right to keep"]:
            lines = item.count("\n") + 1
            block(sl, 1024, y, 740, [
                (item, dict(size=27, bold=True, color=NAVY_DIM, spacing=1.24)),
            ])
            y += lines * 27 * 1.24 + 14
    notes(sl, """Timing: 1:43-3:15

Speak from ideas. Reveal the left column two items at a time, then bring up
the boundary column.

Say the boundary plainly. Do not take confidential information, customer data,
employee data, proprietary documents, or anything the employer owns that you
have no right to keep. Preserving your record does not mean taking their
material.

The test to say out loud: if you are not entitled to keep it, do not take it.

Then give the shape of the record itself, spoken, not on the slide:

What changed? What was the starting condition? What did I decide or influence?
Who was affected? What permitted evidence supports the result?

Nothing here needs a screenshot of an employer system.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=5):
    bg(sl, CREAM)
    kicker_head(sl, "Check two", "Name what the work built.", head_size=60,
                sub="A resume bullet does not automatically show what you can do.")
    rect(sl, 120, 486, 1680, 396, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 486, 1680, color=GOLD, h=8)
    rows = [
        ("Problem", "What problem was being solved?"),
        ("Constraint", "What made the situation difficult?"),
        ("Judgment", "What did I notice, decide, interpret or influence?"),
        ("Outcome", "What changed or was prevented?"),
    ]
    y = 522
    for i, (label, value) in enumerate(rows):
        if i + 1 <= step:
            block(sl, 164, y + 6, 320, [
                (label, dict(size=26, bold=True, color=GOLD, tracking=4)),
            ])
            block(sl, 500, y, 1260, [
                (value, dict(size=36, bold=True, color=NAVY, spacing=1.26)),
            ])
            if i < len(rows) - 1:
                hairline(sl, 164, y + 68, 1476, color=RULE_CREAM, h=2)
        y += 90
    if step >= 5:
        block(sl, 120, 926, 1680, [
            ("Then ask: where else could that combination matter?",
             dict(size=32, bold=True, color=BLUE, spacing=1.3)),
        ])
    notes(sl, """Timing: 3:23-4:55

Speak from ideas. Reveal one row at a time, then the closing question.

Use the generic example. Someone may have reduced the time an internal process
took. The portable value is usually not the number. It is the ability to
identify where work was getting stuck, align people who owned different parts
of the system, redesign the handoff, and do it without creating a new control
failure.

That combination is what another organization can use. Do not invent
statistics; the shape of the judgment is the evidence.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=4):
    bg(sl, BLUE)
    eyebrow(sl, TOP_X, TOP_Y, "Check three", color=GOLD, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Test the next move.", dict(size=60, bold=True, color=CREAM, spacing=1.1)),
    ])
    block(sl, TOP_X, TOP_Y + 148, TOP_W, [
        ("A strong move does two things at once.",
         dict(size=30, font=BODY, color=CREAM_DIM, spacing=1.32)),
    ])
    block(sl, 120, 500, 780, [
        ("Uses something\nproven", dict(size=58, bold=True, color=GOLD, spacing=1.14)),
    ])
    rect(sl, 958, 496, 3, 150, fill=CREAM_DIM)
    block(sl, 1020, 500, 780, [
        ("Builds something\nnew", dict(size=58, bold=True, color=CREAM, spacing=1.14)),
    ])
    prompts = [
        "What will this next role allow me to carry?",
        "What new judgment, exposure or responsibility will it force me to develop?",
        "What will I be able to do after a year that I cannot do now?",
    ]
    for i, q in enumerate(prompts):
        if i + 2 > step:
            continue
        y = 730 + i * 78
        block(sl, 120, y + 2, 90, [
            ("0%d" % (i + 1), dict(size=26, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, 240, y, 1580, [
            (q, dict(size=34, bold=True, color=CREAM, spacing=1.2)),
        ])
    notes(sl, """Timing: 5:03-6:30

Speak from ideas. Hold the contrast, then reveal the questions one at a time.

Two cautions, spoken rather than on the slide.

A move that uses nothing you have already developed may impose an unnecessary
reset.

And a move that simply repeats the same work at another employer may change
the scenery without changing your position.

The move worth making usually does both things at once.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    bg(sl, CREAM)
    kicker_head(sl, "The three checks",
                "Take them in order,\nbefore you resign.", head_size=54)
    cards = [
        ("01", "Preserve the\nevidence"),
        ("02", "Name what\nthe work built"),
        ("03", "Test the\nnext move"),
    ]
    for i, (num, title) in enumerate(cards):
        x = 120 + i * 575
        rect(sl, x, 520, 550, 420, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, x, 520, 550, color=GOLD, h=8)
        block(sl, x + 44, 566, 460, [
            (num, dict(size=76, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, x + 44, 700, 470, [
            (title, dict(size=36, bold=True, color=NAVY, spacing=1.24)),
        ])
    notes(sl, """Timing: 6:30-6:45

The first and only moment all three checks appear together.

Name them once, in order: preserve the evidence, name what the work built,
test the next move. Do not teach them again.""")


# ----------------------------------------------------------------- slide 10
def slide_10(sl, step=3):
    bg(sl, CREAM)
    kicker_head(sl, "Reading the evidence",
                "Three directions the\nevidence can point.", head_size=54,
                sub="The point is not to make the decision slow.\n"
                    "The point is to make it legible.")
    rows = [
        ("Leave", "The evidence says leaving is right, and you are ready."),
        ("Reposition inside", "Another role, project or scope change could restore\n"
                              "growth without an immediate exit."),
        ("Build a bridge", "You need something first: a credential, outside-context\n"
                           "evidence, financial runway, or a clearer translation of\n"
                           "what your experience can do elsewhere."),
    ]
    y = 540
    for i, (label, value) in enumerate(rows):
        lines = value.count("\n") + 1
        h = lines * 32 * 1.3
        if i + 1 <= step:
            block(sl, 120, y + 4, 400, [
                (label, dict(size=26, bold=True, color=GOLD, tracking=4)),
            ])
            block(sl, 560, y, 1240, [
                (value, dict(size=32, bold=True, color=NAVY, spacing=1.3)),
            ])
            if i < len(rows) - 1:
                hairline(sl, 120, y + h + 22, 1680, color=RULE_CREAM, h=2)
        y += h + 64
    notes(sl, """Timing: 6:45-7:45

Reveal one direction at a time. Keep this provisional. You are not diagnosing
the viewer and you are not telling them which one is correct.

Say the line as written: the point is not to make the decision slow, the point
is to make it legible.

If the earlier safety boundary applies to someone watching, repeat it briefly
here. A harmful situation does not need a bridge plan.""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=3):
    bg(sl, NAVY)
    eyebrow(sl, TOP_X, TOP_Y, "Before you resign", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Answer these three\nfirst.", dict(size=60, bold=True, color=CREAM,
                                            spacing=1.1)),
    ])
    numbered_rows(sl, [
        "What evidence do I need to preserve now?",
        "What does my strongest evidence show I can do?",
        "What must the next move use and build?",
    ], step, y0=536, size=44, color=CREAM, rule=BLUE, gap=76)
    notes(sl, """Timing: 7:45-8:35

Ask one question at a time and pause after each one. Leave five to seven
seconds of quiet after the third.

Tell the viewer they can pause the video here and write the answers down.""")


# ----------------------------------------------------------------- slide 12
def slide_12(sl, step=1):
    bg(sl, CREAM)
    eyebrow(sl, TOP_X, TOP_Y, "Career Decision Evidence Check", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Before you make the move,\nread what the work has built.",
         dict(size=54, bold=True, color=NAVY, spacing=1.12)),
    ])
    hairline(sl, 120, 600, 200, color=RUST, h=4)
    rect(sl, 120, 700, 900, 96, fill=NAVY)
    block(sl, 120, 700, 900, [
        ("temidayoafonja.com/career-decisions",
         dict(size=40, bold=True, color=CREAM, align="c")),
    ], anchor="m", h=96)
    logomark(sl, 1668, 700, unit=44, gap=12)
    notes(sl, """Timing: 8:35-9:00

Calm and brief. This is the only invitation in the video, and it is the Career
Decision Evidence Check, not the Field Kit.

Say it plainly: if you want a structured read of the evidence behind the
decision you are weighing, that is what this is for, and it is at
temidayoafonja.com/career-decisions.

Before publishing, confirm that route is live and reaches the right place.""")


# ----------------------------------------------------------------- slide 13
def slide_13(sl, step=1):
    bg(sl, NAVY)
    eyebrow(sl, 120, 462, "Watch next", w=900)
    block(sl, 120, 516, 980, [
        ("How to Change Jobs\nWithout Starting\nYour Career Over",
         dict(size=74, bold=True, color=CREAM, spacing=1.12)),
    ])
    hairline(sl, 120, 824, 200, color=RUST, h=6)
    logomark(sl, 1712, 928, unit=32, gap=9, lw=2)
    notes(sl, """Timing: 9:00-9:25

If the move changes function or industry, this is the video that answers what
carries across.

Do not summarize this video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: section_01, 4: slide_04,
            5: section_02, 6: slide_06, 7: section_03, 8: slide_08,
            9: slide_09, 10: slide_10, 11: slide_11, 12: slide_12,
            13: slide_13}
