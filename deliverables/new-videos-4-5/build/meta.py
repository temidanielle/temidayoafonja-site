# -*- coding: utf-8 -*-
"""Packaging metadata for the new Videos 4 and 5, per the September 7 roadmap."""

CLAIM = ("I get brought in when the evidence is incomplete and an important "
         "decision still has to be made.")

META = {
4: dict(
  number=4,
  title="Why Nobody Can Tell What You're Actually Good At",
  thumbnail="THEY CAN'T READ YOU",
  alt_title="Stop Explaining Your Career. Do This Instead.",
  alt_thumbnail="STOP EXPLAINING",
  runtime="17:00 to 18:30",
  role="Outlier / browse-suggested. The outward-facing video: can anyone else "
       "see what I have?",
  cta="Write your one-line Claim in the comments.",
  cta_url=None,
  watch_next="How to Change Jobs Without Starting Your Career Over",
  watch_next_slot="Video 1",
  search_phrase="why nobody can tell what you are good at",
  primary_frame="THE ONE-LINE TEST: Claim, Spine, Receipts"),

5: dict(
  number=5,
  title="How to Explain a Career That Looks All Over the Place",
  thumbnail="YOUR CAREER MAKES SENSE",
  alt_title="Stop Explaining Your Career in Order.",
  alt_thumbnail="STOP EXPLAINING IN ORDER",
  runtime="12:00 to 14:00",
  role="Search-durable sibling. The specific room: what do I actually say?",
  cta="Keep the Proof, a 60-minute career evidence system.",
  cta_url="https://temidayoafonja.com/keep-the-proof",
  watch_next="Why Nobody Can Tell What You're Actually Good At",
  watch_next_slot="Video 4",
  search_phrase="how to explain a career that looks all over the place",
  primary_frame="Chapters, Spine, Next direction"),
}

# September 7, 2026 roadmap renumbering. Recorded once, used everywhere.
RENUMBER = [
 ("Video 4", "Why Nobody Can Tell What You're Actually Good At", "NEW"),
 ("Video 5", "How to Explain a Career That Looks All Over the Place", "NEW"),
 ("retired", "How to Explain Your Career Change", "former Video 4, slot retired"),
 ("Video 6", "Should I Make an Internal Move? 3 Questions to Decide", "was Video 5"),
 ("Video 7", "Are You Growing, or Just Being Given More Work?", "was Video 6"),
 ("Video 8", "How to Show Your Impact at Work When You Built It From Scratch", "was Video 7"),
 ("Video 9", "How to Switch Industries Without Starting Over", "was Video 8"),
]

# The permanent Riverside grammar. One definition, quoted into every artifact
# that an editor or Co-Creator will read.
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

This has been a recurring Riverside failure. State it on every scene."""

GRAMMAR = [
 ("SHORT TEXT CALLOUT", "May appear over Temidayo on camera."),
 ("FRAMEWORK, COMPARISON, MULTI-POINT IDEA", "TRUE FULL-SCREEN motion graphic."),
 ("B-ROLL, VIDEO CUTAWAY", "TRUE FULL-SCREEN visual break."),
 ("CTA", "TRUE FULL SCREEN."),
 ("WATCH NEXT", "TRUE FULL SCREEN, and the final visual of the video."),
]

SOUND_PLAN = """SOUND DESIGN

Four to seven restrained accents across a long-form video. Not one per caption
and not one per cut. Every accent sits clearly under Temidayo's voice.

Use an accent only on:
  - a hero motion graphic entering
  - the framework reveal
  - a numbered section advancing
  - a comparison flipping from one side to the other
  - a major text emphasis
  - a meaningful visual change

Palette: soft whoosh, subtle click, gentle pop, restrained impact, clean sweep.

If Riverside cannot place these automatically, do not treat sound as a blocker.
Place the strongest few by hand and ship. The manual placements are listed per
video in the build map."""
