# -*- coding: utf-8 -*-
"""Standing Riverside / Co-Creator rules for Videos 8 to 13.

Every block here goes into every per-video master prompt, so each prompt is
self-contained and usable with a newly recorded video by an editor who has
never seen this conversation.
"""

OPENING = """I am giving you a NEW RECORDING. Create the visual and audio editing layer from this recording and its transcript. Do not look for existing graphics to convert, and do not assume any earlier version of this video exists.

The approved Recording Master controls INTENDED MEANING. The actual recorded performance controls EDIT TIMING.

If the recorded speech materially differs from the approved master, flag the mismatch and tell me which lines differ. Never manufacture missing speech, and never generate or synthesize audio I did not record."""

CAMERA_LED = """CAMERA-LED FORMAT

Horizontal 16:9, exported at least 1920 x 1080.

Clean false starts, unnecessary repetitions, and accidental waiting footage.

Preserve useful pauses, natural rhythm, complete explanations, and the full ending. Do not over-shorten the teaching."""

FULLSCREEN = """TRUE FULL-SCREEN SCENES

Frameworks, comparisons, multi-point teaching, substantive B-roll, the resource card and Watch Next must fill the entire canvas.

Completely hide Temidayo visually during those scenes while her voice continues.

  - no moving Temidayo behind or around the visual
  - no smaller rectangle floating over her camera footage
  - no transparent background revealing her behind a major graphic

Use an opaque full-frame scene where necessary.

Only short single-idea callouts and the restrained Subscribe cue may appear over camera."""

RETURN_TO_CAMERA = """RETURN TO CAMERA

Return only where the individual scene map calls for it.

This instruction NEVER applies to Watch Next.

Watch Next is final, with no camera return."""

MOBILE = """MOBILE LEGIBILITY

Use large bold typography, high contrast, short phrases, and sequential reveals.

Use navy #112345, warm cream, and selective gold or yellow emphasis.

Do not use tiny explanatory labels, dense grids, essential footer text, or long paragraphs inside small boxes.

Keep evidence qualifications and illustration labels readable. Where a frame carries a SYNTHETIC DATA, PREPARED AI-ASSISTED EXAMPLE, ILLUSTRATION or WORK SAMPLE label, that label is part of the teaching and must stay legible at phone size.

The headline should register quickly. Detailed comparisons need enough time to read.

Split the visual instead of shrinking important information."""

ZOOM = """ZOOM-INS AND ZOOM-OUTS

Use approximately 3 to 5 deliberate camera-emphasis beats across the ENTIRE long-form video.

Use gentle push-ins on insight, tension, or a reframe. Use occasional pull-backs, or a return to base framing, to reset the viewer's eye.

This is ONE COMBINED camera-motion budget. It is not punch-ins plus an additional zoom quota.

Keep movement smooth, minimal, and intentional. Preserve headroom and source quality.

No aggressive crops, pulsing, or constant movement."""

BROLL = """B-ROLL

Use approximately 2 to 4 meaningful full-screen moments where useful, not as a quota.

Avoid generic handshakes, fake boardrooms, meaningless typing, AI-looking people, or private-looking documents presented as authentic.

Motion graphics should do the main visual teaching."""

SUBSCRIBE = """ONE VISUAL SUBSCRIBE CUE

Add one brief, readable branded Subscribe cue after the first meaningful payoff, ideally once back on camera.

It is VISUAL ONLY. Do not add spoken dialogue and do not modify the recording script for it.

Allow about 2 to 3 seconds including its entrance and exit. Use a restrained fade, slide, or gentle scale with one quiet accent.

Do not interrupt a useful pause or cover teaching text."""

SOUND = """SOUND BUDGET

Use approximately 4 to 7 restrained sound accents TOTAL per long-form video, INCLUDING the Subscribe cue.

Per-scene sound suggestions in the scene map are OPTIONAL CANDIDATES, not cumulative instructions. Do not add a sound to every question, item, caption, cut, or reveal. Adding up the per-scene suggestions would exceed the budget on its own. The budget wins.

Select the strongest moments. Use soft whooshes, quiet clicks, gentle pops, or restrained sweeps where appropriate.

Keep effects clearly quieter than the voice."""

MUSIC = """MUSIC AND VOICE

Voice remains clear and dominant. Keep music subtle.

Do not over-compress, and do not compensate for quiet speech by making effects louder.

Use real licensed music only where available. NEVER invent a track name, attribution, or license code."""

PICTURE = """PICTURE

Preserve natural skin tone and texture.

Use modest exposure, white-balance, contrast, clarity, sharpness, and noise correction where supported.

No beauty-filter look, no artificial face brightening, no heavy smoothing."""

CAPTIONS = """CAPTIONS

Keep normal on-camera captions clean.

Suppress competing designed or burned-in captions during major graphics, B-roll, the resource card, and Watch Next.

Do not delete the audio or the transcript words in order to hide a visual caption.

A separate SRT must include the COMPLETE speech and must match the actual final edit."""

ENDING = """ENDING

Preserve the complete resource mention, the Watch Next handoff, and the exact final spoken line.

Watch Next is the final full-screen visual. Reserve a clean area for the clickable video element.

No camera return, extra outro, unrelated sting, black tail, music-only tail, or unused footage afterward.

Keep a purposeful final-card hold and a natural final 1 to 2 second music fade where appropriate.

Do not blindly cut at the final word if that destroys the planned ending.

If a required closing line was never recorded, flag a pickup. Do not invent it."""

UNSUPPORTED = """UNSUPPORTED OPERATIONS

If a requested operation cannot be performed automatically, identify the specific manual step or the supplied-asset fallback.

Do not claim the effect was executed merely because this prompt requests it.

Known fallbacks:
  - if a reveal state cannot be animated separately, hold the supplied
    reference PNG full frame for longer rather than shrinking the type
  - if the camera cannot be hidden for a scene, cut to the supplied reference
    PNG full frame for the hold rather than placing the graphic over footage
  - if captions cannot be suppressed per scene, move them clear of the designed
    text rather than letting them overlap it"""

ORDER = [
 ("CAMERA-LED FORMAT", CAMERA_LED),
 ("TRUE FULL-SCREEN SCENES", FULLSCREEN),
 ("RETURN TO CAMERA", RETURN_TO_CAMERA),
 ("MOBILE LEGIBILITY", MOBILE),
 ("ZOOM-INS AND ZOOM-OUTS", ZOOM),
 ("B-ROLL", BROLL),
 ("ONE VISUAL SUBSCRIBE CUE", SUBSCRIBE),
 ("SOUND BUDGET", SOUND),
 ("MUSIC AND VOICE", MUSIC),
 ("PICTURE", PICTURE),
 ("CAPTIONS", CAPTIONS),
 ("ENDING", ENDING),
 ("UNSUPPORTED OPERATIONS", UNSUPPORTED),
]

# Where the one Subscribe cue sits, per video: after the first meaningful
# payoff, taken from each locked script.
SUBSCRIBE_AT = {
 8: "after the output-versus-problem demonstration lands, once back on camera",
 9: "after the two mistakes are named and the framework arrives, once back on "
    "camera",
10: "after the calendar-versus-contribution rewrite lands, once back on camera",
11: "after the case-mix explanation lands, once back on camera",
12: "after the constraint-versus-conclusion reframe lands, once back on camera",
13: "after the vague-versus-testable destination lands, once back on camera",
}
