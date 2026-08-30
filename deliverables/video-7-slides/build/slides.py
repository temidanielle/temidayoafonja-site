"""Video 7: "How to Show Your Impact at Work When You Built It From Scratch".

Twelve slides in the approved Capability Formation system, using the Video 6
deck as the visual master: deep navy ground, warm cream typography, muted gold
accents, thin gold rules, generous negative space, restrained editorial
treatment. Palette, geometry and type come from deck.py unchanged.

Every word on every slide is copied verbatim from Section 5 of the Video 7
production package. Layout devices deliberately differ from Video 6 so the two
decks are not clones; Video 6's wording and subject matter are not carried over.

No opening title card. The video begins full screen on Temidayo; slide 1 is the
first teaching visual and lands only after the hook and viewer promise.
"""
import os
from deck import *

# Slide number -> reveal states. Package reveal map, total 24.
STEPS = {1: 2, 2: 2, 3: 3, 4: 2, 5: 2, 6: 2, 7: 1, 8: 3, 9: 2, 10: 3,
         11: 1, 12: 1}

TITLES = {
    1:  "No blueprint",
    2:  "Why it goes quiet",
    3:  "The three moves",
    4:  "Reconstruct the before",
    5:  "What did not exist",
    6:  "Name what you built",
    7:  "The judgment involved",
    8:  "What the work returned",
    9:  "Evidence without invented numbers",
    10: "Before, build, return",
    11: "Primary CTA, Keep the Proof",
    12: "Watch next",
}

SLUGS = {
    1: "no-blueprint", 2: "why-it-goes-quiet", 3: "the-three-moves",
    4: "reconstruct-the-before", 5: "what-did-not-exist",
    6: "name-what-you-built", 7: "the-judgment-involved",
    8: "what-the-work-returned", 9: "evidence-without-invented-numbers",
    10: "before-build-return", 11: "keep-the-proof", 12: "watch-next",
}

DIM_ON_NAVY = RGBColor(0x63, 0x74, 0x8C)
DIM_ON_CREAM = RGBColor(0x8E, 0x98, 0xA8)
PLAYLIST = RGBColor(0x3E, 0x50, 0x6B)


def notes(sl, text):
    sl.notes = text.strip()


def step_mark(sl, x, y, size=30, color=GOLD):
    """The sequence mark between rows on slide 10, drawn.

    No font in the repository contains U+2192, so the arrow in the approved
    copy cannot be typeset in the brand faces. It is drawn as an editable
    triangle instead, which keeps it on-palette and editable rather than
    substituting another character or a non-brand font. Same method approved
    for Video 4.
    """
    rect(sl, x, y, size, size * 0.62, fill=color, shape="tri_down")


# ------------------------------------------------------------------ slide 1
def slide_01(sl, step=1):
    """Navy, gold frame. The single hardest idea in the video, stated once."""
    bg(sl, NAVY)
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)
    logomark(sl, 1668, 104)
    block(sl, 160, 300, 1420, [
        ("YOU WERE NOT\nIMPROVING SOMETHING.",
         dict(size=70, bold=True, color=CREAM, spacing=1.14)),
    ])
    if step >= 2:
        hairline(sl, 160, 592, 300, color=GOLD, h=4)
        block(sl, 160, 660, 1420, [
            ("YOU WERE THE BEFORE.",
             dict(size=70, bold=True, color=GOLD, spacing=1.14)),
        ])
    notes(sl, """Timing: approximately 0:35.

First visual after the hook. Begin full screen on Temidayo; this lands only
after the opening distinction and the viewer promise.

Reveal the first statement, hold it, then bring in the payoff line. Do not rush
the gap — the second line is the thesis of the whole video.""")


# ------------------------------------------------------------------ slide 2
def slide_02(sl, step=1):
    """Cream above, navy band below. The mechanism, not the complaint."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Why the work goes quiet", color=NAVY_DIM, size=24)
    block(sl, 160, 232, 1600, [
        ("MOST WORKPLACE EVIDENCE\nIS COMPARATIVE.",
         dict(size=62, bold=True, color=NAVY, spacing=1.08)),
    ])
    hairline(sl, 160, 404, 200, color=RULE_CREAM, h=4)
    block(sl, 160, 450, 1600, [
        ("A baseline moved. A number improved. A cycle time dropped.",
         dict(size=40, font=BODY, color=NAVY_DIM, spacing=1.3)),
    ])
    if step >= 2:
        rect(sl, 0, 576, W, 504, fill=NAVY)
        block(sl, 160, 646, 1600, [
            ("FOUNDATIONAL WORK HAS NO PRIOR STATE.",
             dict(size=54, bold=True, color=CREAM, spacing=1.08)),
        ])
        hairline(sl, 160, 792, 200, color=GOLD, h=4)
        block(sl, 160, 838, 1600, [
            ("The instrument that would have recorded it\ndid not exist yet.",
             dict(size=40, font=BODY, color=CREAM_DIM, spacing=1.32)),
        ])
    notes(sl, """Timing: approximately 1:25.

Reveal the cream half first — this is the rule the viewer already lives inside.
Bring the navy band in on "you are the before."

The point is diagnostic, not consoling: the work is not invisible because she
was quiet. Keep the delivery level.""")


# ------------------------------------------------------------------ slide 3
def slide_03(sl, step=1):
    """Navy. Three numbered moves, revealed one at a time."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 150, "The three moves", color=GOLD, size=24)
    rows = [
        ("1", "RECONSTRUCT THE BEFORE"),
        ("2", "NAME WHAT YOU BUILT"),
        ("3", "SHOW WHAT IT RETURNED"),
    ]
    for i, (num, text) in enumerate(rows):
        if step < i + 1:
            continue
        y = 288 + i * 232
        block(sl, 160, y, 120, [(num, dict(size=64, bold=True, color=GOLD,
                                           spacing=1.0))])
        block(sl, 320, y + 4, 1440, [(text, dict(size=54, bold=True,
                                                 color=CREAM, spacing=1.06))])
        hairline(sl, 320, y + 108, 1300, color=RGBColor(0x22, 0x3A, 0x60), h=3)
    notes(sl, """Timing: approximately 2:10.

One move per beat. Say the move, let it land, then advance.

This slide returns as the spine of the video — slides 4, 6 and 8 each open one
of these three. Do not paraphrase the wording here; it is repeated verbatim
later.""")


# ------------------------------------------------------------------ slide 4
def slide_04(sl, step=1):
    """Cream. Move one, stated as an instruction rather than a concept."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Move one", color=GOLD, size=24)
    block(sl, 160, 240, 1600, [
        ("DOCUMENT THE ABSENCE\nYOU WALKED INTO.",
         dict(size=64, bold=True, color=NAVY, spacing=1.08)),
    ])
    if step >= 2:
        hairline(sl, 160, 508, 200, color=GOLD, h=4)
        block(sl, 160, 566, 1500, [
            ("Not the state of the world when you arrived.",
             dict(size=42, font=BODY, color=NAVY_DIM, spacing=1.34)),
            ("What was missing from it.",
             dict(size=42, font=BODY, color=NAVY, spacing=1.34,
                  space_before=14)),
        ])
    notes(sl, """Timing: approximately 2:35.

The distinction in the reveal is the whole move. "What it was like" is a story;
"what was missing" is a baseline.

Hold on the second line. This is the step most viewers skip.""")


# ------------------------------------------------------------------ slide 5
def slide_05(sl, step=1):
    """Navy. The absence checklist, in two columns, four then four."""
    bg(sl, NAVY)
    block(sl, 160, 156, 1600, [
        ("WHAT DID NOT EXIST?", dict(size=58, bold=True, color=CREAM,
                                     spacing=1.06)),
    ])
    hairline(sl, 160, 258, 200, color=GOLD, h=4)
    left = ["No owner", "No system", "No shared language",
            "No baseline anyone trusted"]
    right = ["No decision process", "No relationships across functions",
             "No standard", "No repeatable method"]
    for i, t in enumerate(left):
        block(sl, 160, 348 + i * 128, 760,
              [(t, dict(size=42, font=BODY, color=CREAM, spacing=1.2))])
        hairline(sl, 160, 348 + i * 128 + 78, 700,
                 color=RGBColor(0x22, 0x3A, 0x60), h=2)
    if step >= 2:
        for i, t in enumerate(right):
            block(sl, 1020, 348 + i * 128, 760,
                  [(t, dict(size=42, font=BODY, color=CREAM, spacing=1.2))])
            hairline(sl, 1020, 348 + i * 128 + 78, 700,
                     color=RGBColor(0x22, 0x3A, 0x60), h=2)
    notes(sl, """Timing: approximately 3:05.

Left column first, then the right. Read them as questions she is asking the
viewer, not as a list to get through.

Follow the slide with the spoken example about three channels and no one
reconciling them — the specificity is what makes the checklist usable.""")


# ------------------------------------------------------------------ slide 6
def slide_06(sl, step=1):
    """Cream, then a navy band. Move two: under the output."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Move two", color=GOLD, size=24)
    block(sl, 160, 240, 1600, [
        ("THE OUTPUT IS THE\nSMALLEST PART.",
         dict(size=64, bold=True, color=NAVY, spacing=1.08)),
    ])
    if step >= 2:
        rect(sl, 0, 576, W, 504, fill=NAVY)
        block(sl, 160, 656, 1600, [
            ("DEFINITIONS   ·   RELATIONSHIPS   ·   DECISIONS",
             dict(size=46, bold=True, color=CREAM, spacing=1.18)),
            ("ALIGNMENT   ·   REPEATABLE CAPABILITY",
             dict(size=46, bold=True, color=CREAM, spacing=1.18,
                  space_before=22)),
        ])
        hairline(sl, 160, 860, 200, color=GOLD, h=4)
        block(sl, 160, 902, 1600, [
            ("What the organisation can do now that it could not do before.",
             dict(size=38, font=BODY, color=CREAM_DIM, spacing=1.3)),
        ])
    notes(sl, """Timing: approximately 4:30.

The tracker, the programme, the playbook — those are the output. The band is
what sat underneath it.

The last line is the definition of a capability and is repeated in the CTA
block. Keep the wording exact.""")


# ------------------------------------------------------------------ slide 7
def slide_07(sl, step=1):
    """Navy, single state. The judgment slide is deliberately unrevealed."""
    bg(sl, NAVY)
    block(sl, 160, 268, 1620, [
        ("JUDGMENT IS THE PART\nTHAT DOES NOT TRANSFER\nINTO A SLIDE.",
         dict(size=62, bold=True, color=CREAM, spacing=1.16)),
    ])
    hairline(sl, 160, 660, 300, color=GOLD, h=4)
    block(sl, 160, 726, 1620, [
        ("Name the choice. Name the alternative you rejected.\nName the reason.",
         dict(size=44, font=BODY, color=GOLD, spacing=1.32)),
    ])
    notes(sl, """Timing: approximately 5:40.

One state, no build. The idea does not benefit from being taken apart.

This is the slide that separates the video from personal-branding advice: a
record of thinking, not a claim about herself.""")


# ------------------------------------------------------------------ slide 8
def slide_08(sl, step=1):
    """Cream. Move three, three bands of evidence revealed in sequence."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 150, "Move three", color=GOLD, size=24)
    block(sl, 160, 216, 1600, [
        ("WHAT IS DIFFERENT NOW?", dict(size=60, bold=True, color=NAVY,
                                        spacing=1.06)),
    ])
    hairline(sl, 160, 322, 200, color=RULE_CREAM, h=4)
    bands = [
        "ADOPTION   ·   CONTINUED USE   ·   BETTER DECISIONS",
        "REDUCED AMBIGUITY   ·   REPEATABILITY   ·   RECOGNITION",
        "A CLEAN HANDOFF   ·   A CAPABILITY THAT REMAINED",
    ]
    for i, t in enumerate(bands):
        if step < i + 1:
            continue
        y = 404 + i * 190
        rect(sl, 160, y, 1600, 150, fill=None, line=RULE_CREAM, lw=3)
        block(sl, 208, y + 46, 1520,
              [(t, dict(size=40, bold=True, color=NAVY, spacing=1.1))])
    notes(sl, """Timing: approximately 6:30.

One band per beat, in order. Do not reveal all three at once — the point is
that the list is longer than the viewer expects.

None of these is a percentage. That is deliberate and is stated out loud in the
next block.""")


# ------------------------------------------------------------------ slide 9
def slide_09(sl, step=1):
    """Navy. The two boundaries: no invented precision, no taken material."""
    bg(sl, NAVY)
    block(sl, 160, 208, 1620, [
        ("A NUMBER YOU CANNOT DEFEND\nIS WORSE THAN NO NUMBER.",
         dict(size=58, bold=True, color=CREAM, spacing=1.12)),
    ])
    hairline(sl, 160, 424, 300, color=GOLD, h=4)
    block(sl, 160, 480, 1620, [
        ("“Used by every team in the region for two years\nafter I left it.”",
         dict(size=42, font=BODY, color=GOLD, spacing=1.32)),
    ])
    if step >= 2:
        rect(sl, 160, 704, 1600, 4, fill=RGBColor(0x22, 0x3A, 0x60))
        eyebrow(sl, 160, 756, "What you may keep", color=GOLD, size=22)
        block(sl, 160, 818, 1620, [
            ("Outcomes, decisions, what you learned, non-confidential\n"
             "examples in your own words. Not documents, not data,\n"
             "not anything employer-owned.",
             dict(size=36, font=BODY, color=CREAM_DIM, spacing=1.3)),
        ])
    notes(sl, """Timing: approximately 8:35.

The quoted line is an example of defensible evidence, not a claim about
Temidayo. Read it as an example.

The second state is the permitted-evidence boundary and is not optional — it
must appear on screen while she says it.""")


# ------------------------------------------------------------------ slide 10
def slide_10(sl, step=1):
    """Cream. The application, three rows, one per paragraph the viewer writes."""
    bg(sl, CREAM)
    eyebrow(sl, 160, 168, "Three paragraphs", color=NAVY_DIM, size=24)
    rows = [
        ("BEFORE", "What did not exist."),
        ("BUILD", "What you created underneath the output."),
        ("RETURN", "What is different now—and how someone else could tell."),
    ]
    for i, (head, body) in enumerate(rows):
        if step < i + 1:
            continue
        y = 296 + i * 228
        block(sl, 160, y, 520, [(head, dict(size=52, bold=True, color=NAVY,
                                            spacing=1.05, tracking=2.0))])
        block(sl, 700, y + 8, 1060,
              [(body, dict(size=40, font=BODY, color=NAVY_DIM, spacing=1.28))])
        hairline(sl, 160, y + 122, 1600, color=RULE_CREAM, h=3)
        if i < 2:
            step_mark(sl, 160, y + 158, size=30)
    notes(sl, """Timing: approximately 9:20.

One row per paragraph, revealed as she names it.

The sequence marks are drawn shapes, not typed characters: no brand font
contains that glyph. They stay editable in the PPTX.

Say the instruction plainly — three short paragraphs, written this week, while
the detail is still recoverable.""")


# ------------------------------------------------------------------ slide 11
def slide_11(sl, step=1):
    """Navy. Primary CTA. One offer on screen, nothing competing."""
    bg(sl, NAVY)
    rect(sl, 56, 56, W - 112, H - 112, fill=None, line=GOLD, lw=2)
    logomark(sl, 1668, 104)
    eyebrow(sl, 160, 300, "Keep the proof", color=GOLD, size=26)
    block(sl, 160, 370, 1420, [
        ("A 60-MINUTE CAREER\nEVIDENCE SYSTEM",
         dict(size=66, bold=True, color=CREAM, spacing=1.12)),
    ])
    hairline(sl, 160, 620, 300, color=GOLD, h=4)
    block(sl, 160, 682, 1420, [
        ("Reconstruct the before. Name what you built.\nRecord what it returned.",
         dict(size=40, font=BODY, color=CREAM_DIM, spacing=1.3)),
    ])
    block(sl, 160, 856, 1420, [
        ("temidayoafonja.com/keep-the-proof",
         dict(size=44, bold=True, color=GOLD, spacing=1.1)),
    ])
    notes(sl, """Timing: approximately 9:55.

One offer only. No competing route on this slide and none in this block of the
script.

Hold the URL on screen for the full CTA. It also belongs in the first two lines
of the description and in the pinned comment.""")


# ------------------------------------------------------------------ slide 12
def slide_12(sl, step=1):
    """Navy. Watch next. Right side kept clear for the YouTube end-screen card."""
    bg(sl, NAVY)
    eyebrow(sl, 160, 236, "Watch next", color=GOLD, size=24, w=900)
    block(sl, 160, 306, 900, [
        ("HOW TO EXPLAIN A\nNONLINEAR CAREER\nWITHOUT LOOKING\nUNFOCUSED",
         dict(size=52, bold=True, color=CREAM, spacing=1.16)),
    ])
    hairline(sl, 160, 730, 260, color=GOLD, h=4)
    block(sl, 160, 786, 900, [
        ("Career Portability: Career Pivots,\nInternal Moves & Growth",
         dict(size=34, font=BODY, color=PLAYLIST, spacing=1.28)),
    ])
    notes(sl, """Timing: approximately 10:25.

Everything sits left of x=1130. The right third is reserved for the YouTube
end-screen element and must stay empty.

Route to the single video if it has published by the time Video 7 goes live;
otherwise point at the Career Portability playlist. The playlist line is on the
slide either way, so no re-render is needed to switch.""")


BUILDERS = {1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05,
            6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10,
            11: slide_11, 12: slide_12}
