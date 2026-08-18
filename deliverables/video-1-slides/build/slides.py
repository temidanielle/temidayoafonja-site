"""The twelve slides. Every slide function takes a reveal step (1-based)."""
import os
from deck import *

A = lambda n: os.path.join(ASSETS, n)

PHOTO_GREEN = A("photo-headshot-green.png")
PHOTO_CREAM = A("photo-headshot-cream.png")
PHOTO_WINE  = A("photo-portrait-wine.png")
FK_COVER    = A("fieldkit-cover.png")
FK_PAGE06   = A("fieldkit-page-06.png")

# slide number -> number of progressive reveal steps
STEPS = {1: 1, 2: 1, 3: 3, 4: 4, 5: 1, 6: 2, 7: 2, 8: 1, 9: 1, 10: 4, 11: 3, 12: 1}

TITLES = {
    1: "Title", 2: "Career path", 3: "The three moves", 4: "Move 1 - title vs capability",
    5: "Field Kit p6 statement 9", 6: "Move 2 - work vs outcomes",
    7: "Evidence - integrating score 47 to 75", 8: "Field Kit p6 statement 8",
    9: "Field Kit invitation", 10: "Move 3 - 90-day evidence card",
    11: "Three questions", 12: "End screen - next video",
}


SLUGS = {1: 'title', 2: 'career-path', 3: 'three-moves', 4: 'move-1-title-vs-capability', 5: 'fieldkit-statement-9', 6: 'move-2-work-vs-outcomes', 7: 'evidence-47-to-75', 8: 'fieldkit-statement-8', 9: 'fieldkit-invitation', 10: 'move-3-evidence-card', 11: 'three-questions', 12: 'end-screen'}


def notes(sl, text):
    sl.notes = text.strip()


def gold_frame(sl):
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)


def kicker_head(sl, kick, head, head_size=66, color=NAVY, sub=None,
                sub_color=None, kick_color=GOLD):
    """Standard instructional-slide header, placed right of the presenter safe area."""
    eyebrow(sl, TOP_X, TOP_Y, kick, color=kick_color, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W,
          [(head, dict(size=head_size, bold=True, color=color, spacing=1.1))])
    if sub:
        nlines = head.count("\n") + 1
        y = TOP_Y + 52 + nlines * head_size * 1.1 + 26
        block(sl, TOP_X, y, TOP_W,
              [(sub, dict(size=32, font=BODY, color=sub_color or NAVY_DIM,
                          spacing=1.3))])


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
    notes(sl, """0:00-0:35 Opening promise - memorize exactly.
Start on your face, not this slide. Move to the title only after
'the three things that helped me do it.'
Camera: full frame for the first sentence, then drop to the small
presenter box in the upper-left safe area.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    bg(sl, CREAM)
    # real photographs, past to present, in the top-right zone
    for path, x in ((PHOTO_GREEN, 700), (PHOTO_CREAM, 1076), (PHOTO_WINE, 1452)):
        img_cover(sl, path, x, 96, 344, 316)
        rect(sl, x, 96, 344, 316, fill=None, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 462, 1680, color=RULE_CREAM, h=2)

    eyebrow(sl, 120, 500, "My path was not straight")
    block(sl, 120, 548, 1560, [
        ("The titles changed.\nThe capability kept accumulating.",
         dict(size=60, bold=True, color=NAVY, spacing=1.12)),
    ])

    # timeline
    spine_y, x0, x1 = 812, 230, 1660
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
        block(sl, cx - 155, spine_y + 42, 310, [
            (label.upper(), dict(size=27, bold=True, tracking=2.5, align="c",
                                 color=NAVY if last else NAVY_DIM, spacing=1.2)),
        ])
    notes(sl, """0:35-1:25 Personal context - speak from ideas.
Landing line: 'The continuity was not always visible in the job titles.
I had to look underneath the titles and ask what the work was teaching me to do.'
Gem: 'The titles changed. The capability kept accumulating.'
Camera: keep the presenter box small or hide it while the timeline is up.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=3):
    bg(sl, CREAM)
    kicker_head(sl, "The three moves", "Three practices that\ncarried the value forward.",
                head_size=56)
    cards = [
        ("01", "Separate the title\nfrom the capability"),
        ("02", "Translate the work\ninto outcomes"),
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
    notes(sl, """1:25 Set up the three moves, then teach them one at a time.
Reveal one card at a time. Camera stays in the upper-left safe area.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Move one", "Separate the title\nfrom the capability.",
                sub="A title tells people where the work sat. It does not tell them\n"
                    "what the work trained you to see, decide or solve.")
    qs = [
        "What problems can I now solve?",
        "What decisions can I make with better judgment?",
        "What can I do today that I could not do two years ago?",
        "What would remain mine if this role disappeared?",
    ]
    for i, q in enumerate(qs):
        if i + 1 > step:
            continue
        y = 520 + i * 118
        block(sl, 120, y + 8, 90, [
            ("0%d" % (i + 1), dict(size=32, bold=True, color=GOLD, spacing=1.0)),
        ])
        block(sl, 240, y, 1560, [
            (q, dict(size=44, bold=True, color=NAVY, spacing=1.2)),
        ])
        if i < len(qs) - 1:
            hairline(sl, 120, y + 96, 1680, color=RULE_CREAM, h=2)
    notes(sl, """1:25-3:10 Move 1 - speak from ideas, reveal one question at a time.
Gem: 'Being new to the setting did not erase what I already knew how to do.'
Viewer action: write your title, then three problems people trust you to solve.""")


# --------------------------------------------------------- slides 5 and 8
def _fieldkit_statement(sl, number, statement, ):
    bg(sl, NAVY)
    gold_frame(sl)
    logomark(sl, 1668, 104)
    eyebrow(sl, 160, 452,
            "The Capability Formation Field Kit  ·  page 06  ·  optionality",
            w=1600, align="c")
    hairline(sl, 910, 512, 100, color=RUST, h=4)
    block(sl, 260, 570, 1400, [
        (statement, dict(size=72, font=SERIF, color=CREAM, align="c", spacing=1.24)),
    ])
    rect(sl, 770, 880, 380, 62, fill=None, line=GOLD, lw=2)
    block(sl, 770, 880, 380, [
        ("Statement %d  ·  score 1-5" % number,
         dict(size=21, bold=True, color=GOLD, tracking=3, align="c")),
    ], anchor="m", h=62)


def slide_05(sl, step=1):
    _fieldkit_statement(sl, 9,
        "“If my role disappeared tomorrow,\nthe capability I built would still\nbe mine to carry.”")
    notes(sl, """Artifact for Move 1. Field Kit page 6, statement 9, rebuilt as
readable slide type - do not put the whole PDF page on screen.
Camera: hide the presenter box briefly here.""")


def slide_08(sl, step=1):
    _fieldkit_statement(sl, 8,
        "“I can describe what I do in terms\nof outcomes, not just my company’s\ninternal language.”")
    notes(sl, """Artifact for Move 2. Field Kit page 6, statement 8, rebuilt as
readable slide type. Move to the 47-to-75 proof slide after this.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=2):
    bg(sl, CREAM)
    kicker_head(sl, "Move two", "Translate the work\ninto outcomes.",
                sub="The translation question: what changed because I was there?")
    # internal description
    rect(sl, 120, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 520, 760, color=NAVY_DIM, h=8)
    block(sl, 164, 566, 680, [
        ("Internal description", dict(size=24, bold=True, color=NAVY_DIM, tracking=4)),
    ])
    block(sl, 164, 630, 680, [
        ("Led an onboarding\nredesign.", dict(size=46, bold=True, color=NAVY, spacing=1.2)),
    ])
    if step >= 2:
        block(sl, 890, 660, 160, [
            ("→", dict(size=90, color=GOLD, align="c", spacing=1.0)),
        ])
        rect(sl, 1040, 520, 760, 380, fill=WHITE, line=RULE_CREAM, lw=2)
        hairline(sl, 1040, 520, 760, color=GOLD, h=8)
        block(sl, 1084, 566, 680, [
            ("Portable outcome", dict(size=24, bold=True, color=GOLD, tracking=4)),
        ])
        block(sl, 1084, 630, 680, [
            ("Helped redesign the new-hire\nintegration experience; the\nintegrating score moved from\n47 to 75.",
             dict(size=36, bold=True, color=NAVY, spacing=1.22)),
        ])
    block(sl, 120, 940, 1680, [
        ("Outcome language: time saved  ·  errors reduced  ·  adoption improved  ·  risk lowered  ·  retention strengthened  ·  capability built",
         dict(size=24, font=BODY, color=NAVY_DIM)),
    ])
    notes(sl, """3:10-5:05 Move 2 - one concrete before-and-after, not a list.
Say clearly that this was done with a team.
Gem: 'The project name tells people what I worked on.
The result tells them what the work changed.'""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=2):
    bg(sl, BLUE)
    eyebrow(sl, TOP_X, TOP_Y, "Move two  ·  the evidence", color=GOLD, w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Onboarding redesign.", dict(size=60, bold=True, color=CREAM, spacing=1.1)),
    ])
    block(sl, TOP_X, TOP_Y + 148, TOP_W, [
        ("New-hire integrating score, led with the team.",
         dict(size=30, font=BODY, color=CREAM_DIM, spacing=1.3)),
    ])
    # before
    block(sl, 380, 500, 440, [
        ("47", dict(size=260, bold=True, color=CREAM, align="c", spacing=1.0)),
    ])
    block(sl, 380, 862, 440, [
        ("Before", dict(size=28, bold=True, color=CREAM_DIM, tracking=5, align="c")),
    ])
    if step >= 2:
        block(sl, 820, 560, 280, [
            ("→", dict(size=120, color=GOLD, align="c", spacing=1.0)),
        ])
        block(sl, 1100, 500, 440, [
            ("75", dict(size=260, bold=True, color=GOLD, align="c", spacing=1.0)),
        ])
        block(sl, 1100, 862, 440, [
            ("After", dict(size=28, bold=True, color=GOLD, tracking=5, align="c")),
        ])
    block(sl, 120, 950, 1680, [
        ("A score without an evidence line is a guess with decimal points.",
         dict(size=30, font=SERIF, italic=True, color=CREAM_DIM, align="c")),
    ])
    notes(sl, """Reveal 47 first, then 75. Return to camera when you explain
why the outcome travels outside the company.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    bg(sl, CREAM)
    # the real Field Kit: actual assessment page behind, actual cover in front
    img_contain(sl, FK_PAGE06, 1010, 190, 430, 556, rotation=-7)
    img_contain(sl, FK_COVER, 1270, 128, 560, 724)

    eyebrow(sl, 120, 486, "The Capability Formation Field Kit")
    block(sl, 120, 534, 880, [
        ("Know what your\nwork is building.", dict(size=64, bold=True, color=NAVY,
                                                   spacing=1.1)),
    ])
    block(sl, 120, 706, 840, [
        ("Complete the full assessment privately, using evidence from the last ninety days.",
         dict(size=30, font=BODY, color=NAVY_DIM, spacing=1.32)),
    ])
    rect(sl, 120, 838, 720, 96, fill=NAVY)
    block(sl, 120, 838, 720, [
        ("temidayoafonja.com/book", dict(size=40, bold=True, color=CREAM, align="c")),
    ], anchor="m", h=96)
    notes(sl, """5:05-5:35 Field Kit invitation - memorize exactly.
The only purchase invitation in the video. Keep it calm, specific, brief.
Camera: visible but smaller than the product. Do not show Maven in this video.""")


# ----------------------------------------------------------------- slide 10
def slide_10(sl, step=4):
    bg(sl, CREAM)
    kicker_head(sl, "Move three", "Keep evidence\nbefore you need it.",
                sub="A 90-day record. No confidential information required.")
    rect(sl, 120, 496, 1680, 500, fill=WHITE, line=RULE_CREAM, lw=2)
    hairline(sl, 120, 496, 1680, color=GOLD, h=8)
    rows = [
        ("Problem", "New hires needed a stronger integration experience."),
        ("Action", "Led the onboarding redesign with the team."),
        ("Outcome", "The integrating score moved from 47 to 75."),
        ("Capability", "Diagnosing an employee-experience problem and leading\na measurable organizational response."),
    ]
    for i, (label, value) in enumerate(rows):
        if i + 1 > step:
            continue
        y = 528 + i * 120
        block(sl, 164, y + 10, 320, [
            (label, dict(size=26, bold=True, color=GOLD, tracking=4)),
        ])
        block(sl, 500, y, 1250, [
            (value, dict(size=36, bold=True, color=NAVY, spacing=1.24)),
        ])
        if i < len(rows) - 1:
            hairline(sl, 164, y + 100, 1476, color=RULE_CREAM, h=2)
    notes(sl, """5:35-7:25 Move 3 - teach the card slowly, one row at a time.
Gem: 'A score without an evidence line is a guess with decimal points.'""")


# ----------------------------------------------------------------- slide 11
def slide_11(sl, step=3):
    bg(sl, NAVY)
    eyebrow(sl, TOP_X, TOP_Y, "Before your next move", w=TOP_W)
    block(sl, TOP_X, TOP_Y + 52, TOP_W, [
        ("Three questions.", dict(size=66, bold=True, color=CREAM, spacing=1.1)),
    ])
    qs = [
        ("What can I solve?",
         "What problem can I solve today\nthat I could not solve two years ago?"),
        ("What changed?",
         "What outcome have I produced\nthat another employer would understand?"),
        ("What can I carry?",
         "If my current role disappeared tomorrow,\nwhat capability would still be mine?"),
    ]
    for i, (label, q) in enumerate(qs):
        if i + 1 > step:
            continue
        y = 476 + i * 176
        block(sl, 120, y, 1680, [
            (label, dict(size=24, bold=True, color=GOLD, tracking=4)),
        ])
        block(sl, 120, y + 46, 1680, [
            (q, dict(size=42, bold=True, color=CREAM, spacing=1.2)),
        ])
        if i < len(qs) - 1:
            hairline(sl, 120, y + 158, 1680, color=BLUE, h=2)
    notes(sl, """7:25-8:25 Viewer exercise - slow down.
Ask one question, pause, then reveal the next.
Leave five to seven seconds of quiet after the last question.""")


# ----------------------------------------------------------------- slide 12
def slide_12(sl, step=1):
    bg(sl, NAVY)
    eyebrow(sl, 120, 462, "Watch next", w=900)
    block(sl, 120, 516, 960, [
        ("Is your job\nmaking you less\nmarketable?",
         dict(size=88, bold=True, color=CREAM, spacing=1.1)),
    ])
    hairline(sl, 120, 852, 200, color=RUST, h=6)
    block(sl, 120, 896, 900, [
        ("temidayoafonja.com/book", dict(size=30, bold=True, color=GOLD)),
    ])
    logomark(sl, 1712, 928, unit=32, gap=9, lw=2)
    notes(sl, """8:25-9:00 Next-video bridge - memorize exactly. Do not summarize.
The right side of this frame is deliberately empty for YouTube's
linked-video end-screen element. Hold for at least 12 seconds.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11, 12: slide_12}
