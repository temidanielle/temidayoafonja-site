# -*- coding: utf-8 -*-
"""Videos 4 and 5, mapped by hand.

These two were rewritten hardest, so none of their old trigger sentences
survives and no automatic match is trustworthy. Their frameworks did survive
intact, so the cards are kept and re-anchored by reading the new scripts.

Two cards are removed rather than re-anchored. Both sat on the opening
moment, and both openings are now Temidayo telling her own experience. The
standing rule for this pass is that a recognition moment stays camera-led, so
a graphic there works against the thing the pass exists to create.
"""

# Removed, with the reason recorded for the change log.
DROP = {
 "v4_01_title_new_work_not_new":
   "The story-led V4 opens on Temidayo's own experience of stepping into "
   "three roles nobody had held. That is a recognition moment and it should "
   "stay on camera. A full-screen card over the first two sentences would "
   "cover exactly the moment the pass was written to create.",
 "v5_01_changed_tracks_not_zero":
   "The story-led V5 opens on Temidayo's own track changes and then moves "
   "into the car analogy, which is a spoken image rather than a diagram. "
   "Both are camera-led. The two-mistakes point this card carried is still "
   "made in the speech, immediately, so nothing is lost by staying on her.",
}

# Explicit mode overrides. Everything else keeps the mode it already had.
MODES = {}


def _h(trigger, why, status="COPY UPDATE"):
    return dict(trigger=trigger, status=status, why=why)


CARD_KEPT = ("The card is unchanged and still teaches what this part of the "
             "story-led script teaches. Only the sentence it lands on "
             "changed, so the cue is re-anchored.")

HAND = {
 # ---------------------------------------------------------------- V4
 "v4_02_three_stops": _h(
   "I stopped doing three things.",
   CARD_KEPT + " It now lands after the opening scene rather than inside "
   "it, so the three stops arrive once the viewer has recognized the "
   "situation."),
 "v4_04_remove_the_title": _h(
   "Take the title away for a minute.", CARD_KEPT),
 "v4_05_task_list_vs_judgment": _h(
   "A task list can help when the new job looks almost exactly like your "
   "old job.", CARD_KEPT),
 "v4_06_gap_is_not_a_verdict": _h(
   "A real career move should probably include things you do not know yet.",
   CARD_KEPT),
 "v4_07_three_line_readiness_case": _h(
   "Here is the test I want you to use.", CARD_KEPT),

 # ---------------------------------------------------------------- V5
 "v5_02_four_things": _h(
   "I use four questions:",
   CARD_KEPT + " The four questions now arrive out of the car analogy "
   "rather than as the opening claim."),
 "v5_03_carry_test": _h(
   "Start with the parts of your experience that still matter in the new "
   "setting.", CARD_KEPT),
 "v5_04_translate": _h(
   "The next step is translation.", CARD_KEPT),
 "v5_05_relearn_without_beginner": _h(
   "Then comes the part people sometimes want to skip.", CARD_KEPT),
 "v5_06_confidence_both_directions": _h(
   "You do not have to erase your past.", CARD_KEPT),
 "v5_07_prove_the_level": _h(
   "If the new role asks for a higher level of work, your proof also needs "
   "to show that level.", CARD_KEPT),
 "v5_09_cta": _h(
   "If you are thinking about changing tracks, write four lines.",
   CARD_KEPT),
 "v5_10_watch_next": _h(
   "But it does require you to know what is actually coming with you.",
   "The card is unchanged. The story-led V5 speaks no Watch Next line, so "
   "the card is cued off the final spoken sentence and remains the last "
   "full-screen visual."),
}

CAMERA_LED = ("Re-anchored one beat later. The story-led script opens this "
              "video on a recognition moment, and the old cue sat on the "
              "scene prose itself, where a full-screen card would cover the "
              "very thing the pass was written to create. The card is "
              "unchanged and now lands on the line the scene builds to.")

HAND.update({
 "v6_01_movement_is_not_growth": _h(
   "A role can come with more money, more visibility, a more senior title, "
   "and a different company name, and still leave you solving almost the "
   "same class of problem.", CAMERA_LED),
 "v8_01_success_hides_the_work": _h(
   "The process exists. People use it. The decisions have become routine.",
   CAMERA_LED),
 "v16_01_called_then_skipped": _h(
   "And you are not in the conversation.",
   CAMERA_LED + " It now punctuates the end of the scene rather than "
   "opening over it."),
 "v17_01_two_days_forty_minutes": _h(
   "Now a tool produces most of it in forty minutes.",
   CAMERA_LED + " The card shows the two-days-to-forty-minutes contrast, so "
   "it lands where the contrast completes."),
 "v18_01_congratulated": _h(
   "Management is often offered as a reward. But it is not a reward. It is "
   "a different job.", CAMERA_LED),
})
