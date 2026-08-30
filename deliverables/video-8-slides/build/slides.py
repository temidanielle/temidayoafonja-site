# -*- coding: utf-8 -*-
"""Video 8: "How to Move Into a New Industry Without Starting Over".

Twelve slides in the approved Capability Formation system, inheriting the
Video 7 deck as the visual master: deep navy ground, warm cream typography,
muted gold accents, thin gold rules, generous negative space, restrained
editorial treatment. Palette, geometry and type come from deck.py unchanged.

Every word on every slide is copied verbatim from Section 5 of the Video 8
production package. Layout devices deliberately differ from Video 7 so the two
decks are not clones; Video 7's wording and subject matter are not carried over.

No opening title card. The video begins full screen on Temidayo; slide 1 is the
first teaching visual and lands only after the hook and viewer promise.
"""
import os
from deck import *

# Slide number -> reveal states. Package reveal map, total 24.
STEPS = {1: 2, 2: 2, 3: 3, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 3, 10: 3,
         11: 1, 12: 1}

TITLES = {
    1:  "New to a context",
    2:  "What actually changes",
    3:  "Capability, context, credential",
    4:  "What travels",
    5:  "What must be relearned",
    6:  "What must be earned",
    7:  "Start from the destination",
    8:  "Translate, do not recite",
    9:  "Bridge evidence",
    10: "The three columns",
    11: "Primary CTA, Capability Formation Field Kit",
    12: "Watch next",
}

SLUGS = {
    1: "new-to-a-context", 2: "what-actually-changes",
    3: "capability-context-credential", 4: "what-travels",
    5: "what-must-be-relearned", 6: "what-must-be-earned",
    7: "start-from-the-destination", 8: "translate-do-not-recite",
    9: "bridge-evidence", 10: "the-three-columns", 11: "field-kit",
    12: "watch-next",
}

RULE_NAVY = RGBColor(0x22, 0x3A, 0x60)
PLAYLIST = RGBColor(0x8E, 0x9C, 0xB2)   # 5.59:1 on navy; see Video 7 QA


def notes(sl, text):
    sl.notes = text.strip()


def num(sl, x, y, n, size=54):
    block(sl, x, y, 120, [(n, dict(size=size, bold=True, color=GOLD,
                                   spacing=1.0))])


# ------------------------------------------------------------------ slide 1
def slide_01(sl, step=1):
    """Navy, gold frame. The locked opening distinction, in two beats."""
    bg(sl, NAVY)
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)
    logomark(sl, 1668, 104)
    block(sl, 160, 292, 1420, [
        ("CHANGING INDUSTRIES\nDOES NOT MAKE YOU\nENTRY-LEVEL AT EVERYTHING.",
         dict(size=62, bold=True, color=CREAM, spacing=1.16)),
    ])
    if step >= 2:
        hairline(sl, 160, 668, 300, color=GOLD, h=4)
        block(sl, 160, 736, 1420, [
            ("IT MAKES YOU NEW\nTO A CONTEXT.",
             dict(size=62, bold=True, color=GOLD, spacing=1.16)),
        ])
    notes(sl, """Timing: approximately 0:30.

First visual after the hook. Begin full screen on Temidayo; this lands only
after the opening distinction and the viewer promise.

Reveal the first statement, hold it, then bring in the second. The gap between
them is the whole video — do not rush it.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    """Cream list, then a navy band. Six things that change, named plainly."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 150, "What actually changes", color=NAVY_DIM, size=24)
    items = ["Language", "Stakeholders", "Incentives",
             "Regulation", "Operating rhythm", "Risks"]
    for i, t in enumerate(items):
        col, row = divmod(i, 3)
        block(sl, 160 + col * 820, 236 + row * 110, 760,
              [(t, dict(size=44, font=BODY, color=NAVY, spacing=1.2))])
        hairline(sl, 160 + col * 820, 236 + row * 110 + 76, 700,
                 color=RULE_CREAM, h=3)
    if step >= 2:
        rect(sl, 0, 640, W, 440, fill=NAVY)
        block(sl, 160, 716, 1600, [
            ("NONE OF THAT IS YOUR COMPETENCE.",
             dict(size=52, bold=True, color=CREAM, spacing=1.1)),
            ("ALL OF IT IS CONTEXT.",
             dict(size=52, bold=True, color=GOLD, spacing=1.1,
                  space_before=20)),
        ])
        hairline(sl, 160, 916, 200, color=GOLD, h=4)
        block(sl, 160, 956, 1600, [
            ("And context is learnable.",
             dict(size=38, font=BODY, color=CREAM_DIM, spacing=1.28)),
        ])
    notes(sl, """Timing: approximately 1:20.

Read the six as a list she is walking through, not as a grid to get past.
Incentives is the one viewers underestimate — give it a beat.

The navy band is the relief line. It reframes the whole problem from
competence to information, so let it land before moving on.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=1):
    """Navy. The three-way separation, one row per reveal."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 140, "Move one", color=GOLD, size=24)
    rows = [
        ("CAPABILITY", "Judgment that stays useful when the setting changes."),
        ("CONTEXT", "What the new field knows and you do not — yet."),
        ("CREDENTIAL", "Formal evidence or permission the destination requires."),
    ]
    for i, (head, body) in enumerate(rows):
        if step < i + 1:
            continue
        y = 250 + i * 240
        num(sl, 160, y, str(i + 1), size=46)
        block(sl, 300, y - 4, 1460,
              [(head, dict(size=50, bold=True, color=CREAM, spacing=1.05,
                           tracking=2.0))])
        block(sl, 300, y + 76, 1460,
              [(body, dict(size=36, font=BODY, color=CREAM_DIM, spacing=1.28))])
        hairline(sl, 300, y + 160, 1440, color=RULE_NAVY, h=2)
    notes(sl, """Timing: approximately 2:15.

One row per beat. This is the spine of the video: slides 4, 5 and 6 open each
of the three in turn.

The reason to separate them is that they have different remedies. Say that
line here rather than saving it — it is what makes the slide useful.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=1):
    """Cream. Capability, made concrete rather than adjectival."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Capability", color=GOLD, size=24)
    block(sl, 160, 236, 1600, [
        ("WHAT TRAVELS", dict(size=62, bold=True, color=NAVY, spacing=1.06)),
    ])
    hairline(sl, 160, 340, 200, color=RULE_CREAM, h=4)
    if step >= 2:
        block(sl, 160, 412, 1600, [
            ("Finding the real decision in a room of stated positions.",
             dict(size=40, font=BODY, color=NAVY, spacing=1.3)),
            ("Structuring a problem nobody has framed yet.",
             dict(size=40, font=BODY, color=NAVY, spacing=1.3,
                  space_before=26)),
            ("Knowing when a number is too clean to be true.",
             dict(size=40, font=BODY, color=NAVY, spacing=1.3,
                  space_before=26)),
            ("Holding a position when the room would rather you did not.",
             dict(size=40, font=BODY, color=NAVY, spacing=1.3,
                  space_before=26)),
        ])
        hairline(sl, 160, 760, 200, color=GOLD, h=4)
        block(sl, 160, 806, 1600, [
            ("None of these belong to an industry.",
             dict(size=40, bold=True, color=NAVY, spacing=1.2)),
        ])
    notes(sl, """Timing: approximately 2:50.

Concrete examples, not adjectives. Adaptable, strategic and fast learner are
explicitly rejected later — do not let them in here.

Invite the viewer to add two of their own before advancing.""")


# ------------------------------------------------------------------ slide 5
def slide_05(sl, step=1):
    """Navy. Context, restated as an information gap."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 168, "Context", color=GOLD, size=24)
    block(sl, 160, 236, 1600, [
        ("WHAT MUST BE RELEARNED",
         dict(size=62, bold=True, color=CREAM, spacing=1.06)),
    ])
    hairline(sl, 160, 344, 200, color=GOLD, h=4)
    if step >= 2:
        block(sl, 160, 424, 1600, [
            ("The names the same idea goes by here.",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28)),
            ("Who must be convinced, and who can quietly stop it.",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=24)),
            ("What the pressure is, and where it comes from.",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=24)),
            ("What everyone here is quietly afraid of.",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=24)),
        ])
        rect(sl, 160, 776, 1600, 3, fill=RULE_NAVY)
        block(sl, 160, 822, 1600, [
            ("It feels like a competence gap. It is an information gap.",
             dict(size=40, bold=True, color=GOLD, spacing=1.2)),
        ])
    notes(sl, """Timing: approximately 3:25.

The last line is the reassurance the viewer came for, so deliver it level
rather than warmly — it is a finding, not comfort.

Do not promise the gap closes quickly. Say it closes faster than expected when
someone is deliberate about it.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=1):
    """Cream, single state. Credential, including the honest third case."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Credential", color=GOLD, size=24)
    block(sl, 160, 236, 1600, [
        ("WHAT MUST BE EARNED",
         dict(size=62, bold=True, color=NAVY, spacing=1.06)),
    ])
    hairline(sl, 160, 344, 200, color=RULE_CREAM, h=4)
    rows = [
        ("Genuinely required", "There is no way around it. Plan for it."),
        ("A signal", "Not required, but it shortens the conversation."),
        ("Neither", "Chased because it feels like progress."),
    ]
    for i, (head, body) in enumerate(rows):
        y = 430 + i * 186
        block(sl, 160, y, 620,
              [(head, dict(size=40, bold=True, color=NAVY, spacing=1.1))])
        block(sl, 820, y + 4, 940,
              [(body, dict(size=36, font=BODY, color=NAVY_DIM, spacing=1.26))])
        hairline(sl, 160, y + 118, 1600, color=RULE_CREAM, h=2)
    notes(sl, """Timing: approximately 4:05.

One state, no build. The three cases are more useful read together than
revealed one at a time.

The third case is the one that saves the viewer money and months. Say it
plainly and without mockery — chasing a credential is a reasonable response to
feeling stuck.""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=1):
    """Navy. Move two: work from the destination backwards."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 150, "Move two", color=GOLD, size=24)
    block(sl, 160, 216, 1620, [
        ("START FROM THE DESTINATION,\nNOT FROM YOUR CV.",
         dict(size=56, bold=True, color=CREAM, spacing=1.14)),
    ])
    hairline(sl, 160, 400, 300, color=GOLD, h=4)
    if step >= 2:
        block(sl, 160, 470, 1620, [
            ("What does that industry keep failing to solve?",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28)),
            ("Which of those decisions have you made before?",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=26)),
            ("Which patterns do you already recognise early?",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=26)),
            ("Which constraints have you worked inside?",
             dict(size=38, font=BODY, color=CREAM, spacing=1.28,
                  space_before=26)),
        ])
    notes(sl, """Timing: approximately 4:45.

The direction of travel is the point. Most viewers start from their own
history and hope it matches; this reverses it.

Name the real sources out loud — trade press, earnings calls, regulator
commentary, and how job descriptions read when a team is frustrated.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=1):
    """Cream. The adjective trap and what replaces it."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Translate, do not recite", color=NAVY_DIM, size=24)
    block(sl, 160, 240, 1600, [
        ("“ADAPTABLE.”   “STRATEGIC.”\n“A FAST LEARNER.”",
         dict(size=54, bold=True, color=NAVY_DIM, spacing=1.16)),
    ])
    hairline(sl, 160, 428, 200, color=RULE_CREAM, h=4)
    block(sl, 160, 476, 1600, [
        ("These describe how you would like to be seen.",
         dict(size=38, font=BODY, color=NAVY_DIM, spacing=1.28)),
    ])
    if step >= 2:
        rect(sl, 0, 596, W, 484, fill=NAVY)
        block(sl, 160, 676, 1600, [
            ("THE UNIT THAT TRANSFERS IS JUDGMENT,\nWITH EVIDENCE ATTACHED.",
             dict(size=50, bold=True, color=CREAM, spacing=1.16)),
        ])
        hairline(sl, 160, 872, 200, color=GOLD, h=4)
        block(sl, 160, 918, 1600, [
            ("Not a job title. Not a task list.",
             dict(size=38, font=BODY, color=CREAM_DIM, spacing=1.28)),
        ])
    notes(sl, """Timing: approximately 5:40.

Read the three adjectives flatly. They are not being mocked; they are being
shown to carry no information.

Follow immediately with the honest limit: managing a regulated programme
transfers, knowing how a specific regulator behaves does not.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    """Navy. Move three, three bands of permitted bridge evidence."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 140, "Move three", color=GOLD, size=24)
    block(sl, 160, 206, 1620, [
        ("BRIDGE EVIDENCE",
         dict(size=58, bold=True, color=CREAM, spacing=1.06)),
    ])
    hairline(sl, 160, 306, 200, color=GOLD, h=4)
    bands = [
        "A RELEVANT PROJECT   ·   CROSS-FUNCTIONAL WORK",
        "RESEARCH TURNED INTO A POINT OF VIEW   ·   A WORK SAMPLE",
        "PRACTITIONER CONVERSATIONS   ·   A FIRST-90-DAYS PLAN",
    ]
    for i, t in enumerate(bands):
        if step < i + 1:
            continue
        y = 382 + i * 176
        rect(sl, 160, y, 1620, 140, fill=None, line=RULE_NAVY, lw=3)
        block(sl, 206, y + 44, 1540,
              [(t, dict(size=36, bold=True, color=CREAM, spacing=1.1))])
    notes(sl, """Timing: approximately 6:20.

One band per beat. None of these is invented experience, and that boundary is
stated out loud rather than implied.

Research only counts once it has become a point of view. Make that distinction
audible — it is the difference between reading about a sector and having
something to say about it.""")


# ------------------------------------------------------------------ slide 10
def slide_10(sl, step=1):
    """Cream. The exercise: three columns, one per reveal."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 150, "One page, three columns", color=NAVY_DIM, size=24)
    cols = [
        ("WHAT\nTRAVELS", "Judgment, decisions,\npatterns, ways of working."),
        ("WHAT\nCHANGES", "Language, stakeholders,\nincentives, rhythm, risk."),
        ("WHAT I\nMUST EARN", "The credential or exposure\nnothing substitutes for."),
    ]
    for i, (head, body) in enumerate(cols):
        if step < i + 1:
            continue
        x = 160 + i * 546
        rect(sl, x, 240, 4, 560, fill=GOLD if i == 0 else RULE_CREAM)
        block(sl, x + 44, 250, 470,
              [(head, dict(size=42, bold=True, color=NAVY, spacing=1.14,
                           tracking=1.6))])
        block(sl, x + 44, 430, 470,
              [(body, dict(size=32, font=BODY, color=NAVY_DIM, spacing=1.3))])
    notes(sl, """Timing: approximately 8:35.

One column per beat, left to right.

Say the finding that makes the exercise worth doing: for most people the first
column is longer than they feared and the third is shorter than they assumed.

The translation sentence follows this slide and stays spoken, not typeset —
the viewer should write it in their own words.""")


# ------------------------------------------------------------------ slide 11
def slide_11(sl, step=1):
    """Navy. Primary CTA. One offer on screen, nothing competing."""
    bg(sl, NAVY)
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)
    logomark(sl, 1668, 104)
    eyebrow(sl, 160, 296, "Capability formation", color=GOLD, size=26)
    block(sl, 160, 366, 1420, [
        ("FIELD KIT", dict(size=78, bold=True, color=CREAM, spacing=1.08)),
    ])
    hairline(sl, 160, 508, 300, color=GOLD, h=4)
    block(sl, 160, 570, 1420, [
        ("What has your work built in you?\nHow portable is it? What is still missing?",
         dict(size=40, font=BODY, color=CREAM_DIM, spacing=1.32)),
    ])
    block(sl, 160, 856, 1420, [
        ("temidayoafonja.com/fieldkit",
         dict(size=44, bold=True, color=GOLD, spacing=1.1)),
    ])
    notes(sl, """Timing: approximately 9:30.

One offer only. No Keep the Proof, no Career Decision Evidence Check, no book,
on this slide or anywhere in this block.

State the limits out loud: the Field Kit does not tell the viewer which
industry is hiring and does not replace researching the destination.""")


# ------------------------------------------------------------------ slide 12
def slide_12(sl, step=1):
    """Navy. Watch next. Right side kept clear for the end-screen card."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 250, "Watch next", color=GOLD, size=24, w=900)
    block(sl, 160, 320, 900, [
        ("WHAT TO DO\nBEFORE A LAYOFF\nHAPPENS",
         dict(size=58, bold=True, color=CREAM, spacing=1.16)),
    ])
    hairline(sl, 160, 686, 260, color=GOLD, h=4)
    block(sl, 160, 742, 900, [
        ("Career Portability: Career Pivots,\nInternal Moves & Growth",
         dict(size=34, font=BODY, color=PLAYLIST, spacing=1.28)),
    ])
    notes(sl, """Timing: approximately 10:05.

Everything sits left of x=1130. The right third is reserved for the YouTube
end-screen element and must stay empty.

Video 9 has not been produced. Point the end-screen card at the Career
Portability playlist until it publishes, then switch the card to the video.
The playlist line is on the slide either way, so no re-render is needed.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11, 12: slide_12}
