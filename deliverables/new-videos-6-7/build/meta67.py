# -*- coding: utf-8 -*-
"""Locked packaging for Videos 6 and 7, taken from the Recording Masters."""

META = {
6: dict(number=6,
  title="Should I Make an Internal Move? 3 Questions to Decide",
  thumbnail="YOU MAY NOT NEED TO LEAVE",
  runtime="Approximately 11:30 to 12:30 finished. Do not pad to force runtime.",
  framework="Three questions: Work, Judgment, Evidence",
  cta_name="Career Decision Evidence Check",
  cta_url="https://temidayoafonja.com/career-decisions",
  watch_next="Are You Growing, or Just Being Given More Work?",
  watch_next_slot="Video 7",
  spoken_words=1511,
  master="Video_6_Revised_Recording_Master_v1.0.docx"),
7: dict(number=7,
  title="Are You Growing, or Just Being Given More Work?",
  thumbnail="MORE WORK is not GROWTH   (artwork uses the approved symbol form)",
  runtime="Approximately 11:30 to 12:30 finished. Do not pad to force runtime.",
  framework="CAR test: Complexity, Authority, Return",
  cta_name="Capability Formation Field Kit",
  cta_url="https://temidayoafonja.com/fieldkit",
  watch_next="How to Show Your Impact at Work When You Built It From Scratch",
  watch_next_slot="Video 8",
  spoken_words=1455,
  master="Video_7_Revised_Recording_Master_v1.0.docx"),
}

FULLSCREEN_RULE = """TRUE FULL SCREEN means all of the following:

  - the visual occupies the ENTIRE 16:9 canvas
  - Temidayo is NOT visible moving behind it
  - Temidayo is NOT visible around the sides or the edges
  - there is NO smaller graphic or video rectangle floating over her camera
    footage
  - the visual is its own scene, not an overlay
  - her spoken audio continues underneath
  - then cut cleanly back to her

The instruction to give Co-Creator is not "make the graphic full screen." It is:

  "HIDE / REMOVE THE CAMERA VISUALLY DURING THIS SCENE. The motion graphic or
   B-roll must be the only visual filling the entire 16:9 canvas."

This applies to substantive B-roll exactly as it applies to graphics."""

GRAMMAR = [
 ("SHORT SINGLE-LINE CALLOUT", "May appear over Temidayo on camera."),
 ("FRAMEWORK, COMPARISON, DECISION PATH, NUMBERED STRUCTURE, SUMMARY",
  "TRUE FULL-SCREEN motion graphic."),
 ("MEANINGFUL B-ROLL", "TRUE FULL-SCREEN visual break."),
 ("CTA", "TRUE FULL SCREEN."),
 ("WATCH NEXT", "TRUE FULL SCREEN, final visual, no return to camera after it."),
]

MOBILE = """MOBILE LEGIBILITY IS A HARD REQUIREMENT

Every substantive full-screen graphic has to be readable on a normal phone held
at arm's length. The reference assets in this package are built to that
constraint, and any motion version must keep it.

Use:
  - large, bold typography
  - high contrast
  - very short support copy
  - one dominant idea per visual state
  - sequential reveals

Avoid:
  - tiny labels
  - dense grids
  - long paragraphs
  - important text in a footer position
  - elegant desktop layouts that stop working at phone size
  - several small boxes each holding a full sentence

Where a framework holds several ideas, reveal them one at a time rather than
showing all of them small at once. Every reveal order in the build map is
written to that rule."""

CAPTIONS = """CAPTIONS

Suppress, simplify, hide or reposition captions during:
  - full-screen motion graphics
  - substantive B-roll
  - the CTA
  - Watch Next

Captions must never compete with designed text. The words on the graphic are
the message; a caption bar over them is a defect, not a preference."""

SUBSCRIBE = """SUBSCRIBE CUE

One cue per video, and only after the viewer has already received something
useful.

  - about one second
  - premium, small, and easy to miss if you are not looking for it
  - subtle fade, slide, or gentle scale
  - paired with a quiet click, a soft pop, or a restrained whoosh

Never in the opening. Never a loud or cartoonish YouTube animation."""

SOUND = """SOUND DESIGN

Four to seven restrained accents across the video. Not one per caption and not
one per cut. Every accent sits clearly under Temidayo's voice.

Reserve them for:
  - the hero framework entering
  - a major comparison
  - a numbered reveal
  - an important distinction
  - the Subscribe cue
  - the CTA entrance
  - the Watch Next handoff

Palette: soft whoosh, subtle click, gentle pop, restrained impact, clean sweep."""
