# -*- coding: utf-8 -*-
"""The standing Riverside instructions that apply from Video 4 onward.

These are reproduced in every Co-Creator master prompt and, where relevant, in
the run of show and the visual build map.
"""

FULLSCREEN = """TRUE FULL-SCREEN GRAPHICS

Hide the camera visually during every substantive framework, comparison,
multi-point question, CTA and Watch Next scene. That means all of the
following:

  - the visual occupies the ENTIRE 16:9 canvas
  - Temidayo is NOT visible moving behind it
  - Temidayo is NOT visible around the sides or the edges
  - there is NO smaller graphic or video rectangle floating over her footage
  - the visual is its own scene, not an overlay
  - her voice continues underneath
  - then cut cleanly back to her

RETURN-TO-CAMERA EXCEPTION

Return to camera only where the scene map calls for it. This instruction never
applies to Watch Next. Watch Next is the final visual, continues through the
final spoken line and intentional closing hold, and has no camera return.

Substantive B-roll also fills the entire frame, on the same rule.

Short single-line callouts may sit over camera. Nothing else may.

The instruction to give Co-Creator is not "make the graphic full screen." It is:

  "HIDE / REMOVE THE CAMERA VISUALLY DURING THIS SCENE. The motion graphic or
   B-roll must be the only visual filling the entire 16:9 canvas." """

CAMERA_LED = """CAMERA-LED FORMAT

Use 16:9 and export at least 1920 x 1080.

Preserve meaning, thoughtful delivery and natural skin tone. Do not
over-shorten the teaching. Do not apply a beauty-filter look. Restrained
exposure, white balance, contrast, clarity, mild sharpening and mild noise
reduction only."""

MOBILE = """MOBILE CLARITY

Use large, bold typography, short phrases, high contrast, and one dominant idea
per reveal.

The main point should register quickly. But detailed comparisons need adequate
reading time. Do not force all the information into a one- or two-second
display, and do not shrink a comparison so that it fits a shorter hold.

Do not rely on tiny labels or footer text.

Check actual normal-phone-size previews rather than declaring success from font
size alone. The reference assets in this package were checked that way: each
frame was rendered at 1920 x 1080, downscaled to 390 points wide, and read at
that size."""

ZOOM = """ZOOM-INS AND ZOOM-OUTS ON TEMIDAYO

Use gentle push-ins on important insights, tension points and reframes. Use
occasional pull-backs, or a return to the base composition, to reset the
framing.

Plan approximately 3 to 5 deliberate camera-emphasis beats across the ENTIRE
long-form video. That is the whole budget. It is not three to five punch-ins
plus a separate quota of zooms.

Keep the motion smooth, minimal and intentional. Preserve comfortable headroom
and source image quality.

No aggressive zooms. No constant pulsing. No camera movement visible behind
full-screen graphics."""

SOUND = """SOUND AND MUSIC

Plan approximately 4 to 7 restrained sound accents in total across the whole
video, INCLUDING the Subscribe cue. That is the whole budget. Do not allocate
four to seven sounds to every section, and not one per caption or per cut.

Use them on selected entrances, transitions or payoffs. Keep the voice
dominant, sound effects quieter than speech, and music subtle.

SOUND CUES ARE SELECTIVE, NOT CUMULATIVE

Scene notes that suggest an accent per item, per question, per column, per step
or per word are OPTIONAL SOUND CANDIDATES, not instructions to execute. Do not
play every suggested scene-level accent automatically. Choose the few most
meaningful moments across the whole video and leave the others silent.

Adding up the per-scene suggestions would exceed the budget on its own. The
budget wins.

Never invent music-license information. Add a music credit only when the real
track and license from the finished project are known."""

BROLL = """MEANINGFUL B-ROLL

Use approximately 2 to 4 meaningful full-screen moments where they are useful.
This is a guide, not a quota. If a shot does not add meaning, use a motion
graphic or stay on camera.

Avoid generic handshakes, fake boardrooms, meaningless typing, cliche resume
footage, AI-looking people, and invented private documents presented as
authentic.

Where a designed illustration could be mistaken for a real document or event,
label it as an illustration."""

CAPTIONS = """CAPTIONS AND SUBTITLE FILES

Suppress competing designed or burned-in captions during major graphics,
substantive B-roll, the CTA and Watch Next. Captions must never compete with
designed text.

A separately delivered subtitle transcript must still include the COMPLETE
spoken content. Do not delete spoken words from the transcript merely because a
graphic replaces the camera on screen."""

ENDING = """ENDING

Preserve the complete recorded CTA, the Watch Next handoff and the final spoken
line.

Watch Next is the final visual, with a clear area for the clickable video
element. No camera return and no extra outro afterward.

Remove unused waiting footage, but preserve the intentional final-card hold and
a natural one- to two-second music fade where appropriate. Do not blindly cut
at the last word if that destroys the planned ending.

If required closing speech was not recorded, flag a real pickup. Do not invent
or synthesize it."""

TIMING = """TIMING FOLLOWS THE ACTUAL FOOTAGE

Actual footage controls edit timing. The approved script controls intended
meaning.

If recorded speech differs materially from the master, flag the mismatch. Do
not claim that unrecorded words can be restored.

Do not build YouTube chapters from the script. Build them from the finished
export."""

CAPABILITY = """IF A CAPABILITY IS UNAVAILABLE

If any instruction here cannot be executed in Co-Creator as written, say which
one and name the specific fallback or manual step. Do not report an instruction
as applied when it was not.

Known fallbacks:
  - If a reveal state cannot be animated separately, hold the built reference
    frame longer rather than shrinking the type to fit a shorter hold.
  - If the camera cannot be hidden for a scene, cut to the reference PNG full
    frame for the hold rather than placing the graphic over the footage.
  - If captions cannot be suppressed per scene, move them clear of the designed
    text rather than letting them overlap it."""

SUBSCRIBE_AT = {
4: "after the modeled twenty-second answer and its intentional silence",
5: "after the initial Claim and rejected-Claim payoff",
6: "after Question 1",
7: "after Complexity",
}


def subscribe(n):
    return """ONE VISUAL SUBSCRIBE CUE

Add one brief, readable visual Subscribe cue %s, once meaningful value has been
delivered.

This is a visual only. It is NOT new spoken dialogue and the recording script
is not modified for it.

  - about one second
  - premium, small and restrained
  - a subtle fade, slide or gentle scale, with a quiet click or soft pop

Do not interrupt the speech. Do not cover important text. Do not create another
closing CTA sequence. It counts inside the 4 to 7 sound budget.""" % SUBSCRIBE_AT[n]


ORDER = [("CAMERA-LED FORMAT", CAMERA_LED), ("TRUE FULL-SCREEN GRAPHICS", FULLSCREEN),
         ("MOBILE CLARITY", MOBILE), ("ZOOM-INS AND ZOOM-OUTS", ZOOM),
         ("SOUND AND MUSIC", SOUND), ("MEANINGFUL B-ROLL", BROLL),
         ("CAPTIONS AND SUBTITLE FILES", CAPTIONS), ("ENDING", ENDING),
         ("TIMING", TIMING), ("IF A CAPABILITY IS UNAVAILABLE", CAPABILITY)]
