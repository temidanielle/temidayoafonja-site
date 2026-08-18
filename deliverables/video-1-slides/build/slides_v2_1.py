"""
Video 1 deck, version 2.1. Ten slides.

A controlled narrative and copy revision of slides.py, not a redesign. The
grid, palette, typography, presenter safe area and end-screen reserve are
carried over unchanged. What changed: the two Field Kit quotation slides are
gone, the Field Kit invitation now follows the whole teaching sequence and the
viewer exercise, and the visible copy and speaker notes follow the natural
voice standard.

Version 2.1 makes two corrections only: the slide 2 capability bridge now
reads "into cybersecurity and later into people strategy", and the slide 6
notes credit the work as "the onboarding redesign I led with my team".
"""
import os
from deck import *

A = lambda n: os.path.join(ASSETS, n)

PHOTO_WINE = A("photo-portrait-wine.png")
FK_COVER   = A("fieldkit-cover.png")
FK_PAGE06  = A("fieldkit-page-06.png")

# slide number -> number of progressive reveal steps
STEPS = {1: 1, 2: 1, 3: 3, 4: 3, 5: 2, 6: 2, 7: 4, 8: 3, 9: 1, 10: 1}

TITLES = {
    1: "Title",
    2: "Career path and capability bridge",
    3: "Three things that helped",
    4: "Move one - look underneath the title",
    5: "Move two - explain what the work changed",
    6: "Move two evidence - 47 to 75",
    7: "Move three - keep evidence",
    8: "Three-question exercise",
    9: "Field Kit invitation",
    10: "Next-video bridge",
}

SLUGS = {
    1: "title", 2: "career-path", 3: "three-things", 4: "move-1-look-underneath",
    5: "move-2-translation", 6: "move-2-evidence-47-to-75", 7: "move-3-keep-evidence",
    8: "three-question-exercise", 9: "fieldkit-invitation", 10: "next-video-bridge",
}


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def kicker_head(sl, kick, head, head_size=66, color=NAVY, sub=None,
                sub_color=None, kick_color=GOLD, sub_size=32):
    """Standard header: kicker and headline to the right of the safe area."""
    eyebrow(sl, TOP_X, TOP_Y, kick, color=kick_color, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W,
          [(head, dict(size=head_size, bold=True, color=color, spacing=1.1))])
    if sub:
        nlines = head.count("\n") + 1
        y = TOP_Y + 52 + nlines * head_size * 1.1 + 26
        block(sl, TOP_X, y, TOP_W,
              [(sub, dict(size=sub_size, font=BODY, color=sub_color or NAVY_DIM,
                          spacing=1.32))])


def rows_list(sl, items, step, y0, x_num=120, x_text=240, w_text=1560,
              size=44, color=NAVY, rule=RULE_CREAM, gap=62, numerals=True):
    """A numbered question list that spaces itself around one and two line rows."""
    y = y0
    for i, text in enumerate(items):
        lines = text.count("\n") + 1
        h = lines * size * 1.2
        if i + 1 <= step:
            if numerals:
                block(sl, x_num, y + 6, 90, [
                    ("0%d" % (i + 1), dict(size=32, bold=True, color=GOLD, spacing=1.0)),
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
    eyebrow(sl, 136, 462, "Video one  ·  Capability Formation", w=1400)
    block(sl, 136, 520, 1560, [
        ("How I Changed Jobs\nWithout Starting\nMy Career Over",
         dict(size=100, bold=True, color=CREAM, spacing=1.08)),
    ])
    hairline(sl, 136, 902, 220, color=RUST, h=6)
    block(sl, 136, 942, 1200, [
        ("Temidayo Afonja  ·  temidayoafonja.com",
         dict(size=24, color=CREAM_DIM, bold=True, tracking=4)),
    ])
    notes(sl, """Timing: 0:00-0:35

Begin full-screen on Temidayo rather than on the slide.

Exact opening:

"If you are considering a different job, function or industry, one of the
hardest questions is whether the experience you already have will still
count. I have changed the kind of work I do several times without treating
each move as a return to zero. In this video, I will show you three
questions I use to identify what my experience has built, explain one
result in language another employer can understand and decide what
evidence to preserve before I move."

Move to the title slide after introducing the three questions.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    bg(sl, CREAM)
    # one authentic present-day portrait; the timeline carries the slide
    img_cover(sl, PHOTO_WINE, 1420, 92, 400, 500)
    rect(sl, 1420, 92, 400, 500, fill=None, line=RULE_CREAM, lw=2)

    eyebrow(sl, 120, 500, "My career path")
    block(sl, 120, 548, 1260, [
        ("What connected those career changes",
         dict(size=54, bold=True, color=NAVY, spacing=1.12)),
    ])
    block(sl, 120, 632, 1240, [
        ("Accounting and audit trained me to look for evidence, controls, risk and\n"
         "what a system was failing to reveal. I carried that way of seeing into\n"
         "cybersecurity and later into people strategy.",
         dict(size=29, font=BODY, color=NAVY_DIM, spacing=1.42)),
    ])

    spine_y, x0, x1 = 862, 230, 1660
    hairline(sl, x0, spine_y, x1 - x0, color=BLUE, h=3)
    stages = ["Accounting", "Consulting", "Life\nsciences", "Technology",
              "People\nstrategy", "Capability\nFormation"]
    gap = (x1 - x0) / (len(stages) - 1)
    for i, label in enumerate(stages):
        cx = x0 + i * gap
        last = (i == len(stages) - 1)
        d = 34 if last else 20
        rect(sl, cx - d / 2, spine_y + 1.5 - d / 2, d, d,
             fill=GOLD if last else BLUE, shape="oval")
        block(sl, cx - 140, spine_y + 42, 280, [
            (label.upper(), dict(size=27, bold=True, tracking=2.5, align="c",
                                 color=NAVY if last else NAVY_DIM, spacing=1.2)),
        ])
    notes(sl, """Timing: 0:35-1:35

Speak naturally from the career sequence. Do not read the slide.

Use this transition:

"The continuity was not always visible in the job titles. I had to look
underneath them and ask what the work had actually trained me to do."

Keep the camera in the upper-left safe area while the timeline is up.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=3):
    bg(sl, CREAM)
    kicker_head(sl, "The three moves",
                "Three things helped me carry\nmy experience forward.", head_size=54)
    cards = [
        ("01", "Look underneath\nthe title"),
        ("02", "Explain what\nthe work changed"),
        ("03", "Keep evidence\nbefore you need it"),
    ]
    for i, (num, title) in enumerate(cards):
        if i + 1 > step:
            continue
        x = 120 + i * 575
        rect(sl, x, 520, 530, 420, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, x, 520, 530, color=GOLD, h=8)
        block(sl, x + 44, 566, 440, [
            (num, dict(size=76, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, x + 44, 700, 450, [
            (title, dict(size=40, bold=True, color=NAVY, spacing=1.2)),
        ])
    notes(sl, """Timing: 1:35-1:50

Introduce the three ideas briefly. Do not explain all three on this slide.

Reveal one card at a time.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=3):
    bg(sl, CREAM)
    kicker_head(sl, "Move one", "Look underneath the title.",
                sub="Name what the work has trained you to notice, decide and solve.")
    rows_list(sl, [
        "What problems do people trust me to solve?",
        "What decisions can I now make with better judgment?",
        "What could I do in another setting\nbecause of what I learned here?",
    ], step, y0=576, size=44)
    notes(sl, """Timing: 1:50-3:10

Explain that the title identifies where the work sat, while the questions
reveal what the experience developed.

Reveal one question at a time.

Viewer action:

Write down your current title. Under it, name three problems people now
trust you to solve.""")


# ------------------------------------------------------------------ slide 5
def slide_05(sl, step=2):
    bg(sl, CREAM)
    kicker_head(sl, "Move two", "Explain what the work changed.", head_size=60,
                sub="Ask: What changed because I was there?")
    rect(sl, 120, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 520, 760, color=NAVY_DIM, h=8)
    block(sl, 164, 566, 680, [
        ("Internal description", dict(size=24, bold=True, color=NAVY_DIM, tracking=4)),
    ])
    block(sl, 164, 636, 680, [
        ("Led an onboarding\nredesign.", dict(size=46, bold=True, color=NAVY,
                                              spacing=1.2)),
    ])
    if step >= 2:
        block(sl, 890, 660, 160, [
            ("→", dict(size=90, color=GOLD, align="c", spacing=1.0)),
        ])
        rect(sl, 1040, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, 1040, 520, 760, color=GOLD, h=8)
        block(sl, 1084, 566, 680, [
            ("Portable description", dict(size=24, bold=True, color=GOLD, tracking=4)),
        ])
        block(sl, 1084, 636, 690, [
            ("I led an onboarding redesign with\nmy team. One measure of how well\n"
             "new hires felt integrated moved\nfrom 47 to 75.",
             dict(size=34, bold=True, color=NAVY, spacing=1.26)),
        ])
    notes(sl, """Timing: 3:10-4:10

Explain that "onboarding redesign" names the project but does not yet tell
an unfamiliar viewer what improved.

State clearly that you led the redesign with your team.

Reveal the portable description only after the internal one has been read
aloud and explained.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=2):
    bg(sl, BLUE)
    eyebrow(sl, TOP_X, TOP_Y, "One result", color=GOLD, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("One measure of\nnew-hire integration",
         dict(size=56, bold=True, color=CREAM, spacing=1.1)),
    ])
    block(sl, TOP_X, TOP_Y + 200, TOP_W, [
        ("A team result from a redesign I led",
         dict(size=30, font=BODY, color=CREAM_DIM, spacing=1.3)),
    ])
    block(sl, 380, 520, 440, [
        ("47", dict(size=260, bold=True, color=CREAM, align="c", spacing=1.0)),
    ])
    block(sl, 380, 882, 440, [
        ("Before the redesign", dict(size=26, bold=True, color=CREAM_DIM,
                                     tracking=3, align="c")),
    ])
    if step >= 2:
        block(sl, 820, 580, 280, [
            ("→", dict(size=120, color=GOLD, align="c", spacing=1.0)),
        ])
        block(sl, 1100, 520, 440, [
            ("75", dict(size=260, bold=True, color=GOLD, align="c", spacing=1.0)),
        ])
        block(sl, 1100, 882, 440, [
            ("After the redesign", dict(size=26, bold=True, color=GOLD,
                                        tracking=3, align="c")),
        ])
    notes(sl, """Timing: 4:10-4:55

Say:

"One measure of how well new hires felt integrated moved from 47 to 75
after the onboarding redesign I led with my team. The number becomes
useful because I can explain what it measured, what changed and what I
was responsible for."

Reveal 47 first, then 75.""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Move three", "Keep evidence\nbefore you need it.",
                sub="Write a permitted, high-level account in your own words.\n"
                    "Leave confidential and employer-owned material out.",
                sub_size=30)
    rect(sl, 120, 486, 1680, 516, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 486, 1680, color=GOLD, h=8)
    rows = [
        ("Situation", "New hires needed a stronger integration experience."),
        ("My role", "I led the onboarding redesign with my team."),
        ("What changed", "One measure of how well new hires felt\n"
                         "integrated moved from 47 to 75."),
        ("What this shows", "I can diagnose a weak point in the employee experience\n"
                            "and lead a redesign that improves it."),
    ]
    y = 522
    for i, (label, value) in enumerate(rows):
        lines = value.count("\n") + 1
        h = lines * 36 * 1.26
        if i + 1 <= step:
            block(sl, 164, y + 6, 320, [
                (label, dict(size=26, bold=True, color=GOLD, tracking=4)),
            ])
            block(sl, 500, y, 1260, [
                (value, dict(size=36, bold=True, color=NAVY, spacing=1.26)),
            ])
            if i < len(rows) - 1:
                hairline(sl, 164, y + h + 22, 1476, color=RULE_CREAM, h=2)
        y += h + 52
    notes(sl, """Timing: 4:55-6:40

Explain that professionals often remember project names while losing the
evidence, context and explanation that make the work useful later.

Teach the card one row at a time.

Keep the account permitted and high level. Nothing confidential and no
employer-owned material.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=3):
    bg(sl, NAVY)
    eyebrow(sl, TOP_X, TOP_Y, "Before your next move", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Write down your answers\nto these three questions.",
         dict(size=56, bold=True, color=CREAM, spacing=1.1)),
    ])
    rows_list(sl, [
        "What can I solve now\nthat I could not solve two years ago?",
        "What result can I describe in language\nanother employer would understand?",
        "What could I still do if the title,\nemployer or industry changed?",
    ], step, y0=496, size=44, color=CREAM, rule=BLUE, gap=62)
    notes(sl, """Timing: 6:40-7:45

Ask one question at a time and pause.

Leave five to seven seconds after the third question before moving to the
Field Kit invitation.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
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
         "assessment using the last 90 days of your\n"
         "actual work.",
         dict(size=30, font=BODY, color=NAVY_DIM, spacing=1.32)),
    ])
    rect(sl, 120, 846, 720, 96, fill=NAVY)
    block(sl, 120, 846, 720, [
        ("temidayoafonja.com/book", dict(size=40, bold=True, color=CREAM, align="c")),
    ], anchor="m", h=96)
    notes(sl, """Timing: 7:45-8:20

Exact invitation:

"If these questions are showing you that you need a fuller reading of what
your current work is building, the Capability Formation Field Kit will help
you complete that assessment privately using evidence from the last 90
days."

Keep the delivery calm and brief. This is the only purchase invitation in
the video.""")


# ----------------------------------------------------------------- slide 10
def slide_10(sl, step=1):
    bg(sl, NAVY)
    eyebrow(sl, 120, 462, "Watch next", w=900)
    block(sl, 120, 516, 960, [
        ("Is Your Job\nMaking You Less\nMarketable?",
         dict(size=88, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 120, 852, 200, color=RUST, h=6)
    logomark(sl, 1712, 928, unit=32, gap=9, lw=2)
    notes(sl, """Timing: 8:20-9:00

Exact bridge:

"In the next video, I will show you how to recognize when you are still
performing well but the work is no longer expanding your skills or future
options."

Do not summarize the current video again.

The right side of this frame is left open for the YouTube linked-video
end-screen element. Hold the final frame for at least 12 seconds.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10}
