"""
Video 2: "Is Your Job Making You Less Marketable?"  Thirteen slides. v1.1.

Content and timing come from the Video 2 un-script working sheet v1.0.
The visual system is the approved Video 1 v2.4 system, unchanged: cream ground,
deep navy type, lighter blue for the one contrast moment, muted gold accent,
rust only as a small mark, one idea per slide, an upper-left presenter safe
area on every slide, and progressive reveals only where they teach.

The three tests are three standalone section breaks at three separate moments.
They appear together once, on the recap, after all three have been taught.

Version 1.1 changes two lines of copy on slide 2 and nothing else. The
headline and the supporting line now name the second question directly
instead of describing the pair in the abstract.
"""
import os
from deck import *

A = lambda n: os.path.join(ASSETS, n)
FK_COVER = A("fieldkit-cover.png")
FK_PAGE06 = A("fieldkit-page-06.png")

# slide number -> number of progressive reveal steps.
# Section breaks (3, 5, 7) and the recap (9) never build.
STEPS = {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 4, 7: 1, 8: 4, 9: 1, 10: 1, 11: 4,
         12: 1, 13: 1}

TITLES = {
    1: "Title",
    2: "Recognition, valuable here and legible elsewhere",
    3: "Section break 01, remove the company nouns",
    4: "Test one, before and after language",
    5: "Section break 02, find outside-context evidence",
    6: "Test two, four sources of evidence",
    7: "Section break 03, read the last 90 days",
    8: "Test three, new judgment or the same work faster",
    9: "Recap, all three tests together",
    10: "Interpretation, two questions",
    11: "What to change before you leave",
    12: "Field Kit invitation",
    13: "Next-video bridge",
}

SLUGS = {
    1: "title", 2: "recognition", 3: "section-01-company-nouns",
    4: "test-1-language", 5: "section-02-outside-context",
    6: "test-2-evidence-sources", 7: "section-03-last-90-days",
    8: "test-3-judgment-or-speed", 9: "recap-three-tests",
    10: "interpretation", 11: "what-to-change", 12: "fieldkit-invitation",
    13: "next-video-bridge",
}


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def kicker_head(sl, kick, head, head_size=66, color=NAVY, sub=None,
                sub_color=None, kick_color=GOLD, sub_size=32):
    """Kicker and headline to the right of the presenter safe area."""
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
                  gap=52, x_num=120, x_text=240, w_text=1560, sub_color=None):
    """Numbered rows that space themselves around one and two line entries.
    items = list of (statement, optional supporting line)."""
    y = y0
    for i, item in enumerate(items):
        text, sub = item if isinstance(item, tuple) else (item, None)
        lines = text.count("\n") + 1
        h = lines * size * 1.2
        if sub:
            h += 10 + (sub.count("\n") + 1) * 26 * 1.3
        if i + 1 <= step:
            block(sl, x_num, y + 6, 90, [
                ("0%d" % (i + 1), dict(size=30, bold=True, color=GOLD, spacing=1.0)),
            ])
            block(sl, x_text, y, w_text, [
                (text, dict(size=size, bold=True, color=color, spacing=1.2)),
            ])
            if sub:
                block(sl, x_text, y + lines * size * 1.2 + 10, w_text, [
                    (sub, dict(size=26, font=BODY, spacing=1.3,
                               color=sub_color or NAVY_DIM)),
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
    eyebrow(sl, 136, 462, "Video two  ·  Capability Formation", w=1400)
    block(sl, 136, 520, 1560, [
        ("Is Your Job\nMaking You Less\nMarketable?",
         dict(size=100, bold=True, color=CREAM, spacing=1.08)),
    ])
    hairline(sl, 136, 902, 220, color=RUST, h=6)
    block(sl, 136, 942, 1200, [
        ("Temidayo Afonja  ·  temidayoafonja.com",
         dict(size=24, color=CREAM_DIM, bold=True, tracking=4)),
    ])
    notes(sl, """Timing: 0:00-0:45

Begin full-screen on Temidayo, not on this slide.

Exact opening:

"A job can make you more valuable inside one company while making you harder
to understand everywhere else. That can happen while you are being praised,
well paid, and the person everyone depends on. In this video, I am going to
give you three tests for whether your current success is expanding your
marketability or quietly narrowing it. By the end, you will know what to strip
away from the way you describe your work, what outside-context evidence to
look for, and what the last 90 days have actually added to your judgment. I am
Temidayo Afonja. On this channel, I help experienced professionals make
clearer career decisions by looking at what their work is actually building in
them."

Move to the title only after the three-test promise and the channel line are
clear. Do not make the opening alarmist.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    bg(sl, CREAM)
    eyebrow(sl, TOP_X, TOP_Y, "Two different questions", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Being valuable here\nanswers only one question.",
         dict(size=54, bold=True, color=NAVY, spacing=1.1)),
    ])
    block(sl, 120, 540, 780, [
        ("Valuable here", dict(size=68, bold=True, color=NAVY, spacing=1.1)),
    ])
    rect(sl, 958, 528, 3, 130, fill=GOLD)
    block(sl, 1020, 540, 780, [
        ("Legible elsewhere", dict(size=68, bold=True, color=BLUE, spacing=1.1)),
    ])
    hairline(sl, 120, 760, 1680, color=RULE_CREAM, h=2)
    block(sl, 120, 812, 1560, [
        ("The second question is whether another context\ncan recognize and use what you have built.",
         dict(size=32, font=BODY, color=NAVY_DIM, spacing=1.35)),
    ])
    notes(sl, """Timing: 0:45-1:55

Speak from ideas. Keep this mostly on camera; the slide is visual tension,
not a lecture frame.

Beats: praise can rise while the work becomes more context-bound; pay and
responsibility can rise because you know one environment extremely well;
dependence can come from undocumented knowledge, internal relationships or a
fragile process. None of that is a reason to panic or leave.

Name the second question out loud, since the slide now points at it: whether
another context can recognize and use what you have built.

Exact landing line:

"Praise can tell you that you matter here. It cannot tell you how easily your
value travels."
""")


# ------------------------------------------ slides 3, 5, 7: section breaks
def _section_intro(sl, number, statement, support, notes_text):
    """One number, one statement, air. No cards, no reveal."""
    bg(sl, CREAM)
    eyebrow(sl, 120, 452, "Three marketability tests", w=1400)
    block(sl, 120, 500, 400, [
        ("0%d" % number, dict(size=160, bold=True, color=GOLD, spacing=1.0)),
    ])
    block(sl, 120, 690, 1500, [
        (statement, dict(size=76, bold=True, color=NAVY, spacing=1.14)),
    ])
    block(sl, 120, 900, 1400, [
        (support, dict(size=30, font=BODY, color=NAVY_DIM, spacing=1.3)),
    ])
    notes(sl, notes_text)


def section_01(sl, step=1):
    _section_intro(sl, 1, "Remove the\ncompany nouns",
                   "Can the capability still be described?", """Timing: 1:55-2:03

A section break, four to seven seconds. Say: "The first test is to remove the
company nouns."

Do not teach it here. The example slide follows.

Only this test is on screen. The second and third come later, each in its own
moment.""")


def section_02(sl, step=1):
    _section_intro(sl, 2, "Find outside-context\nevidence",
                   "Has the usefulness survived a change in context?", """Timing: 3:15-3:23

A section break, four to seven seconds. Say: "The second test is to find
evidence that your capability has been useful outside its original context."

Do not restate the first test. The evidence slide follows.""")


def section_03(sl, step=1):
    _section_intro(sl, 3, "Read the\nlast 90 days",
                   "What new judgment did the work build?", """Timing: 4:35-4:43

A section break, four to seven seconds. Say: "The third test is to read the
last 90 days."

Do not restate the first two. The judgment slide follows.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=2):
    bg(sl, CREAM)
    kicker_head(sl, "Test one", "Remove the company nouns.", head_size=60,
                sub="Cross out the employer, the internal programs, the systems,\n"
                    "the product names and the acronyms. Read what is left.")
    rect(sl, 120, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 520, 760, color=NAVY_DIM, h=8)
    block(sl, 164, 566, 680, [
        ("Company-bound description",
         dict(size=24, bold=True, color=NAVY_DIM, tracking=4)),
    ])
    block(sl, 164, 636, 680, [
        ("I own the QBR process\nfor this business unit.",
         dict(size=44, bold=True, color=NAVY, spacing=1.22)),
    ])
    if step >= 2:
        block(sl, 890, 660, 160, [
            ("→", dict(size=90, color=GOLD, align="c", spacing=1.0)),
        ])
        rect(sl, 1040, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, 1040, 520, 760, color=GOLD, h=8)
        block(sl, 1084, 566, 690, [
            ("What another employer\ncan understand",
             dict(size=24, bold=True, color=GOLD, tracking=4, spacing=1.15)),
        ])
        block(sl, 1084, 646, 690, [
            ("I combine incomplete operating\ndata, surface the decision leaders\n"
             "are avoiding, and create a shared\nview of what needs to happen next.",
             dict(size=30, bold=True, color=NAVY, spacing=1.3)),
        ])
    notes(sl, """Timing: 2:03-3:15

Speak from ideas. Show the company-bound sentence first, then the clearer
description.

What remains after the nouns come out should still tell another person what
problem you solve and what judgment the work requires.

Viewer action: take one sentence from your resume, your LinkedIn profile or
the way you introduce your work. Remove the company nouns. If the sentence
collapses, rewrite it around the problem you solve and the judgment you bring.

The example is generic. Keep it that way; no employer-specific or
confidential material.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Test two", "Find outside-context evidence.", head_size=60,
                sub="The evidence can be small. It only has to show the usefulness\n"
                    "survived some distance from where it was formed.")
    numbered_rows(sl, [
        ("Cross-functional project",
         "Another group used or sought your judgment."),
        ("External client or customer",
         "The capability created value beyond your immediate team."),
        ("Former colleague",
         "They sought your judgment after the original context changed."),
        ("Another setting or industry contribution",
         "A similar problem or approach remained useful elsewhere."),
    ], step, y0=500, size=38, gap=38)
    notes(sl, """Timing: 3:23-4:35

Speak from ideas. Reveal one source at a time. Keep it simple; this is not a
list of credentials.

Outside-context evidence does not mean job offers or public visibility. Do not
count visibility by itself as proof. The question is whether the judgment was
actually useful beyond the original context.

Viewer action: write down one example where your judgment was useful beyond
your immediate role, team or employer. If you cannot find one yet, that is
useful information to investigate.

Say why indispensability can mislead: an organization may depend on you
because knowledge, relationships or a fragile process run through you. That
raises internal importance without raising what you can do somewhere else.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=4):
    bg(sl, BLUE)
    eyebrow(sl, TOP_X, TOP_Y, "Test three", color=GOLD, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Read the last 90 days.", dict(size=60, bold=True, color=CREAM,
                                        spacing=1.1)),
    ])
    block(sl, TOP_X, TOP_Y + 148, TOP_W, [
        ("What can you now do, see or decide that you could not\ndo ninety days ago?",
         dict(size=30, font=BODY, color=CREAM_DIM, spacing=1.32)),
    ])
    block(sl, 120, 500, 780, [
        ("New judgment", dict(size=68, bold=True, color=GOLD, spacing=1.1)),
    ])
    rect(sl, 958, 490, 3, 110, fill=CREAM_DIM)
    block(sl, 1020, 500, 780, [
        ("Same work faster", dict(size=68, bold=True, color=CREAM_DIM,
                                  spacing=1.1)),
    ])
    prompts = [
        "What unfamiliar problem did I have to solve?",
        "What decision can I now make with less help?",
        "What constraint, audience or context did I learn to work across?",
    ]
    for i, q in enumerate(prompts):
        if i + 2 > step:
            continue
        y = 690 + i * 86
        block(sl, 120, y + 4, 90, [
            ("0%d" % (i + 1), dict(size=26, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, 240, y, 1580, [
            (q, dict(size=36, bold=True, color=CREAM, spacing=1.2)),
        ])
    notes(sl, """Timing: 4:43-5:55

Speak from ideas. Hold the contrast first, then reveal the prompts one at a
time. Let the contrast breathe.

New judgment might come from a more ambiguous problem, a decision made with
incomplete information, influencing a different group, working across a new
constraint, or building judgment where you previously needed help.

Gem to land: "Speed has value. New judgment tells you something different."

Do not ask only whether you were busy or whether you performed well.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    bg(sl, CREAM)
    kicker_head(sl, "The three tests",
                "Together they separate internal\nvalue from external marketability.",
                head_size=52)
    cards = [
        ("01", "Remove the\ncompany nouns"),
        ("02", "Find outside-context\nevidence"),
        ("03", "Read the\nlast 90 days"),
    ]
    for i, (num, title) in enumerate(cards):
        x = 120 + i * 575
        rect(sl, x, 520, 550, 420, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, x, 520, 550, color=GOLD, h=8)
        block(sl, x + 44, 566, 460, [
            (num, dict(size=76, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, x + 44, 700, 470, [
            (title, dict(size=34, bold=True, color=NAVY, spacing=1.24)),
        ])
    notes(sl, """Timing: 5:55-6:25

The first and only moment all three tests appear together.

Name them once, in order: remove the company nouns, find outside-context
evidence, read the last 90 days. Do not teach them again.

Gem to land: "Internal value and external marketability are two different
questions."
""")


# ----------------------------------------------------------------- slide 10
def slide_10(sl, step=1):
    bg(sl, NAVY)
    eyebrow(sl, TOP_X, TOP_Y, "Reading the pattern", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Read them together.", dict(size=60, bold=True, color=CREAM,
                                     spacing=1.1)),
    ])
    block(sl, 120, 500, 1680, [
        ("Is my judgment growing?", dict(size=66, bold=True, color=CREAM,
                                         spacing=1.15)),
    ])
    hairline(sl, 120, 620, 1680, color=BLUE, h=2)
    block(sl, 120, 672, 1680, [
        ("Can another context use it?", dict(size=66, bold=True, color=GOLD,
                                             spacing=1.15)),
    ])
    block(sl, 120, 850, 1560, [
        ("One familiar sign is not a diagnosis. Read the pattern across growth\n"
         "and portability, and keep the reading provisional.",
         dict(size=30, font=BODY, color=CREAM_DIM, spacing=1.35)),
    ])
    notes(sl, """Timing: 6:25-7:10

Keep this quiet and provisional. Do not turn the four patterns into a dramatic
diagnosis of the viewer.

Spoken, not on the slide: if judgment is deepening and the capability is
useful across contexts, the work is compounding. If expertise is deepening but
its usefulness is trapped inside one environment, that can be a Depth Trap. If
visibility is growing but the work is not building depth, the position may be
fragile. If neither the capability nor the options are growing, the role may
be stagnant even while performance stays strong.

Do not diagnose from one familiar sign.""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Before you leave", "What can I change\nbefore I leave?",
                sub="A concern in one test does not mean the answer is to resign.\n"
                    "Choose one thing to test in the next thirty days.")
    numbered_rows(sl, [
        "Ask for work that creates new judgment, not only more volume.",
        "Make the capability visible outside the immediate team\nor function.",
        "Document knowledge or results that exist mainly in your head.",
        "Take on an adjacent problem that forces the capability\ninto a different context.",
    ], step, y0=520, size=38, gap=50)
    notes(sl, """Timing: 7:10-8:00

Speak from ideas. Reveal one option at a time.

Viewer action: choose one thing you can test during the next thirty days.
Sometimes the first move is to change the work before changing the employer.

Gem to land: "Before you change the employer, test whether you can change what
the work is building."
""")


# ----------------------------------------------------------------- slide 12
def slide_12(sl, step=1):
    bg(sl, CREAM)
    img_contain(sl, FK_PAGE06, 1010, 190, 430, 556, rotation=-7)
    img_contain(sl, FK_COVER, 1270, 128, 560, 724)

    eyebrow(sl, 120, 470, "The Capability Formation Field Kit")
    block(sl, 120, 518, 880, [
        ("Is your job still\nbuilding you?", dict(size=64, bold=True, color=NAVY,
                                                  spacing=1.1)),
    ])
    block(sl, 120, 692, 840, [
        ("Complete a private, evidence-led career position\n"
         "assessment using the last 90 days of your\nactual work.",
         dict(size=30, font=BODY, color=NAVY_DIM, spacing=1.32)),
    ])
    rect(sl, 120, 846, 720, 96, fill=NAVY)
    block(sl, 120, 846, 720, [
        ("temidayoafonja.com/fieldkit",
         dict(size=40, bold=True, color=CREAM, align="c")),
    ], anchor="m", h=96)
    notes(sl, """Timing: 8:00-8:30

Exact invitation:

"If these three tests show that you need a fuller read of what your current
work is building and how portable it is, the Capability Formation Field Kit
gives you a private, evidence-led assessment using the last 90 days of your
actual work. It helps you read the position before you decide what comes next.
You can find it at temidayoafonja.com/fieldkit."

Calm and brief. This is the only purchase invitation in the video. Show the
real Field Kit artwork briefly.

Before publishing, verify the live /fieldkit redirect and the current Gumroad
listing.""")


# ----------------------------------------------------------------- slide 13
def slide_13(sl, step=1):
    bg(sl, NAVY)
    eyebrow(sl, 120, 462, "Watch next", w=900)
    block(sl, 120, 516, 960, [
        ("Before You Quit\nYour Job, Check\nThese 3 Things",
         dict(size=80, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 120, 832, 200, color=RUST, h=6)
    logomark(sl, 1712, 928, unit=32, gap=9, lw=2)
    notes(sl, """Timing: 8:30-9:00

Exact bridge:

"Before you decide that a concern means you should resign, there are three
things I want you to check. That is the next video: Before You Quit Your Job,
Check These 3 Things. Watch that one next."

Do not summarize this video again.

The right side of the frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: section_01, 4: slide_04,
            5: section_02, 6: slide_06, 7: section_03, 8: slide_08,
            9: slide_09, 10: slide_10, 11: slide_11, 12: slide_12,
            13: slide_13}
