# -*- coding: utf-8 -*-
"""Hero visual specifications for Videos 4 to 21, corrected-runtime batch.

Support and reference cards for the Riverside editor. Not a deck that covers
the script paragraph by paragraph.

Fields per asset: key, draw, trigger (verified to sit inside ONE thought block
of the corrected master), purpose, mode, reveal, emphasis, hold, captions,
sound (an OPTIONAL candidate, never cumulative), after, status, why.

`status` is the audit against the prior production package supplied as a
secondary reference. REUSE means a rendered asset exists there whose concept
still matches the corrected script exactly. Nothing is called REUSE because a
visual topic merely sounds similar.
"""
import lay421 as X

SETS = {}


def F(**kw):
    kw.setdefault("mode", "FULL SCREEN")
    kw.setdefault("captions", "No burned-in captions. Suppress any designed "
                              "caption for the whole hold.")
    kw.setdefault("after", "Return to camera on the next spoken line.")
    kw.setdefault("sound", None)
    return kw


# ------------------------------------------------------------------- V4
# 5-MINUTE RETENTION TEST. Entirely new script: new title, new framework.
# The September 9 V4 assets were built around Chapters/Spine and the
# twenty-second answer, none of which survives.
SETS[4] = [
 F(key="v4_01_title_new_work_not_new",
   draw=lambda c: X.statement(
     c, "Three times in five years",
     "The title was new. The work underneath it was not completely new.",
     None, dark=True, size=76),
   trigger="Three times in five years, I stepped into a role that did not "
           "have a predecessor. Each time, the title was new to me. But the "
           "work underneath it was not completely new.",
   purpose="The hook, stated as the distinction the whole video rests on.",
   reveal="Single state. Let the sentence land.",
   emphasis="The second half of the sentence.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REMOVE, replaced by NEW",
   why="The September 9 V4 opened on the interview question and the "
       "twenty-second answer. That script is superseded entirely. "
       "V4_MG01_Introduction_Or_Defense.png has no place in the corrected "
       "script."),

 F(key="v4_02_three_stops",
   draw=lambda c: X.ladder(
     c, "What I stopped doing", None,
     [("Waiting for an exact title match", None),
      ("Proving readiness with a task list", None),
      ("Treating every learning gap as a verdict", None)],
     size=58),
   trigger="What changed was how I judged whether I was ready. I stopped "
           "waiting for an exact title match. I stopped proving myself with a "
           "task list. And I stopped treating every learning gap like "
           "evidence that I was not ready.",
   purpose="The spine of the video, given in the first minute.",
   reveal="One line at a time in the spoken order.",
   emphasis="Equal weight.",
   hold="About 2 seconds each, 3 on the complete set.",
   sound="Candidate: one tick as the third line lands.",
   status="NEW",
   why="The three-stop structure does not exist in any prior V4 asset."),

 F(key="v4_03_three_questions",
   draw=lambda c: X.three_lines(
     c, "Use three questions instead", None,
     ["What problem will I be trusted to solve?",
      "What can I already prove?",
      "What do I genuinely need to learn?"],
     dark=True, size=60),
   trigger="If you are looking at a role you have never held before, use "
           "three questions instead: What problem will I be trusted to "
           "solve? What can I already prove? What do I genuinely need to "
           "learn?",
   purpose="The early payoff. The viewer can act on this alone.",
   reveal="One question at a time.",
   emphasis="All three equal.",
   hold="2 seconds each, 4 on the complete frame. Viewers will pause here.",
   sound="Candidate: one tick on the third question.",
   status="NEW",
   why="New framing introduced by the corrected master."),

 F(key="v4_04_remove_the_title",
   draw=lambda c: X.duo(
     c, "Compare the roles without their titles", None,
     ("The title says", "A role you have never held."),
     ("The work asks",
      "Diagnose ambiguity. Align people who do not report to you. Build a "
      "structure that did not exist. Recommend under uncertainty."),
     foot="'I have never held this title' is not the same as 'I have never "
          "done the underlying work.'"),
   trigger="A useful way to test this is to compare the old and new role "
           "without their titles.",
   purpose="Make stop one usable rather than reassuring.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds on the right side, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="REBUILD",
   why="V4_MG03_Order_Depends_On_The_Question.png tested a different idea. "
       "The comparison shape is reusable; the content is entirely new."),

 F(key="v4_05_task_list_vs_judgment",
   draw=lambda c: X.duo(
     c, "Evidence of judgment", None,
     ("A task list", "Works when the new job is almost identical to the old "
                     "one."),
     ("Evidence of judgment",
      "What did people trust you to notice? What tradeoff did you weigh? "
      "What did you recommend when there was more than one reasonable "
      "answer?"),
     foot="A real example has a decision, a constraint, what you did, and "
          "what happened.",
     dark=True),
   trigger="For unfamiliar work, look for evidence of judgment.",
   purpose="The most useful correction in the video.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line, which is the standard.",
   hold="2 seconds left, 4 right, 3 foot.",
   sound="Candidate: one soft tick as the foot line lands.",
   status="NEW",
   why="Judgment-over-activity is new to the corrected V4."),

 F(key="v4_06_gap_is_not_a_verdict",
   draw=lambda c: X.struck(
     c, "Stop treating the learning gap as a verdict", None,
     "I can already do every part of this.",
     "Here is what I can carry, here is the proof, and here is what I still "
     "need to learn."),
   trigger="A credible readiness case is not, 'I can already do every part "
           "of this.' It is, 'Here is what I can carry, here is the proof, "
           "and here is what I still need to learn.'",
   purpose="Protect the channel's standing position that not everything "
           "transfers, inside a five-minute cut.",
   reveal="The weak claim. Hold. Struck. Then the credible version.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="NEW",
   why="No prior V4 asset carried this."),

 F(key="v4_07_three_line_readiness_case",
   draw=lambda c: X.labeled_rows(
     c, "The 3-line readiness case", None,
     [("Problem", "What does this role actually need someone to solve?"),
      ("Proof", "What have I already done that shows I can handle the "
                "underlying judgment?"),
      ("Gap", "What do I genuinely need to learn, earn, or experience in "
              "this context?")]),
   trigger="Take one role you have never held and write three lines.",
   purpose="The artifact. The frame viewers photograph.",
   reveal="One row at a time.",
   emphasis="All three equal. The Gap row is not styled as a weakness.",
   hold="3 seconds per row, 4 on the complete frame.",
   sound="Candidate: one tick as the third row lands.",
   status="NEW",
   why="The readiness case replaces the prior twenty-second and "
       "ninety-second answer assets entirely."),

 F(key="v4_08_what_it_does_not_guarantee",
   draw=lambda c: X.statement(
     c, "What a readiness case does not do",
     "It does not guarantee that an employer will choose you.",
     "Credentials, markets, relationships, compensation, employer "
     "preferences, and bias still matter.", dark=True, size=68,
     support_size=42),
   trigger="A strong readiness case does not guarantee that an employer will "
           "choose you.",
   purpose="The honesty beat. Required by the standing editorial rule and "
           "spoken in the master.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds. Do not rush it because the video is short.",
   sound="Not a candidate. Let this land in silence.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 33% of the "
       "text is shared with the closest prior card, which read: A "
       "STORY EXPLAINS. PROOF SUPPORTS. The story gets the question. "
       "Evidence answers it.. The editorial note written when this "
       "card was built, kept as written: V4_MG08 carried a limits "
       "concept and the corrected master keeps a limits beat, but the "
       "wording is new, so the render is rebuilt while the editorial "
       "slot is preserved."),

 F(key="v4_09_cta",
   draw=lambda c: X.cta_action(
     c, "One role", "Write the three lines.",
     "Problem. Proof. Gap.",
     "Being new to the title is not being new to the work."),
   trigger="Being new to the title does not automatically mean being new to "
           "the work.",
   purpose="The single action. This master names no resource route, so none "
           "is shown.",
   reveal="Headline, support, then the closing line.",
   emphasis="The closing line in gold.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="V4_CTA_Career_Evidence_Starter.png routed to a resource. The "
       "corrected master names no resource, so no route is shown and none "
       "is added."),

 F(key="v4_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "I Changed Career Tracks Without Starting Over. Here's What I "
     "Carried With Me.", "Video 5"),
   trigger="Being new to the title does not automatically mean being new to "
           "the work.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="V4_WatchNext_Why_Nobody_Can_Tell.png pointed at the old V5 title. "
       "The destination is still V5; its title changed, so the card is "
       "rebuilt with the corrected title."),
]

# ------------------------------------------------------------------- V5
# 5-MINUTE RETENTION TEST. New title, new framework. The September 9 V5
# assets were built on Claim / Spine / Receipts, which is superseded.
SETS[5] = [
 F(key="v5_01_changed_tracks_not_zero",
   draw=lambda c: X.statement(
     c, "Changing tracks", "Other people can start reading you like a "
     "beginner.",
     "The more expensive mistake is when you start doing it to yourself.",
     dark=True, size=72, support_size=44),
   trigger="When you change career tracks, other people can start reading "
           "you like a beginner. The more expensive mistake is when you "
           "start doing it to yourself.",
   purpose="The hook. The risk is self-erasure, not other people's opinion.",
   reveal="Headline. Hold. Then the support line.",
   emphasis="The support line.",
   hold="2 seconds, then 3 with the support.",
   sound="Candidate: one soft tick as the support line lands.",
   status="REMOVE, replaced by NEW",
   why="V5_MG01_Two_Versions_Of_The_Same_Career.png belonged to the "
       "superseded legibility script."),

 F(key="v5_02_four_things",
   draw=lambda c: X.four_bucket(
     c, "Separate four things", None,
     [("CARRY", "The judgment that still helps at the destination."),
      ("TRANSLATE", "How that capability shows up in the new context."),
      ("RELEARN", "What genuinely has to be learned from inside."),
      ("PROVE", "One example that supports the level you are claiming.")]),
   trigger="What helped was separating four things: what I could Carry, what "
           "I had to Translate, what I genuinely needed to Relearn, and what "
           "I could Prove.",
   purpose="The framework, delivered in the first minute.",
   reveal="One bucket at a time in spoken order.",
   emphasis="Equal. None is the good outcome.",
   hold="2 seconds each, 4 on the complete grid.",
   sound="Candidate: one tick on the fourth bucket.",
   status="NEW",
   why="Carry / Translate / Relearn / Prove does not exist in the prior "
       "package."),

 F(key="v5_03_carry_test",
   draw=lambda c: X.statement(
     c, "Carry", "Remove the employer name, the old title, and the "
     "industry language.",
     "Which parts of your experience would still help you solve the "
     "destination problem? That is what you carry.", size=62,
     support_size=44),
   trigger="Ask: if the employer name, old title, and industry language "
           "disappeared, which parts of my experience would still help me "
           "solve the destination problem?",
   purpose="Make Carry a test rather than a claim.",
   reveal="Question, then the one-line answer.",
   emphasis="The question.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="New test introduced by the corrected master."),

 F(key="v5_04_translate",
   draw=lambda c: X.duo(
     c, "Translate", None,
     ("Not this", "Repeat the old label and hope they understand it."),
     ("This", "What did you have to notice? What decision did you support? "
              "What tradeoff did you manage? What changed because of your "
              "contribution?"),
     foot="Translation is not changing the story. It is removing the "
          "context-specific language."),
   trigger="Do not repeat the old label and hope they understand it. "
           "Translate the underlying work.",
   purpose="The most practical section of the video.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line, which prevents the obvious misreading.",
   hold="2 seconds left, 4 right, 3 foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="REBUILD",
   why="V5_MG05_Remove_The_Nouns.png tested an adjacent idea. The shape is "
       "reusable; the corrected content replaces it."),

 F(key="v5_05_relearn_without_beginner",
   draw=lambda c: X.statement(
     c, "Relearn", "Needing to learn them does not erase everything you "
     "already know how to do.",
     "Systems. Regulation. Domain language. Relationships. Sometimes "
     "credentials or practice under a different consequence.",
     dark=True, size=66, support_size=42),
   trigger="Those gaps matter. Your experience does not make them optional. "
           "But needing to learn them does not erase everything you already "
           "know how to do.",
   purpose="Hold both halves of the channel's position in one frame.",
   reveal="Headline, then the list of what is genuinely new.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v5_06_confidence_both_directions",
   draw=lambda c: X.duo(
     c, "Confidence can mislead in both directions", None,
     ("Do not", "Apologize for every gap."),
     ("Also do not",
      "Rename a real domain or credential requirement as a transferable "
      "skill because that makes the move easier to explain."),
     foot="Name the gap accurately, then decide whether it is a reasonable "
          "learning curve or a reason not to move yet."),
   trigger="You do not need to apologize for every gap. But you also do not "
           "get to rename a real domain or credential requirement as a "
           "transferable skill because that makes the move easier to "
           "explain.",
   purpose="The line that protects the whole body of work from sounding "
           "like everything transfers.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="At least 4 seconds on the right side.",
   sound="Not a candidate. Let this land in silence.",
   status="NEW",
   why="New to the corrected master and editorially load-bearing."),

 F(key="v5_07_prove_the_level",
   draw=lambda c: X.struck(
     c, "Prove the level", None,
     ["I have fifteen years of experience.", "I was a director."],
     "What difficult problem did you own? What did you decide when the "
     "answer was not obvious? What scope or consequence did you carry?"),
   trigger="Do not rely on 'I have fifteen years of experience' or 'I was a "
           "director.' Those statements tell me duration and title, not what "
           "level of judgment you can carry into a new context.",
   purpose="Replace duration and title with evidence.",
   reveal="Both weak claims. Hold. Struck. Then the questions.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="REBUILD",
   why="V5_MG07_Test_The_Claim.png tested a different claim. Rebuilt to the "
       "corrected content."),

 F(key="v5_08_four_line_move_case",
   draw=lambda c: X.labeled_rows(
     c, "The 4-line move case", None,
     [("Carry", "The capability that still helps."),
      ("Translate", "How that capability shows up in the new context."),
      ("Relearn", "The genuine gap."),
      ("Prove", "One example that supports the level you are claiming.")]),
   trigger="For one move you are considering, write four lines:",
   purpose="The artifact. The frame viewers photograph.",
   reveal="One row at a time.",
   emphasis="Equal weight.",
   hold="2 seconds per row, 4 on the complete frame.",
   sound="Candidate: one tick as the fourth row lands.",
   status="NEW",
   why="Replaces the prior Claim and Receipts artifact entirely."),

 F(key="v5_09_cta",
   draw=lambda c: X.cta_action(
     c, "One move", "Write the four lines.",
     "Carry. Translate. Relearn. Prove.",
     "More honest than 'I am starting over' or 'everything transfers.'"),
   trigger="That gives you a more honest position than either 'I am starting "
           "over' or 'everything I have done transfers.'",
   purpose="The single action. This master names no resource route.",
   reveal="Headline, support, then the closing line.",
   emphasis="The closing line in gold.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="V5_CTA_Career_Evidence_Starter.png routed to a resource. The "
       "corrected master names none, so none is shown."),

 F(key="v5_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "I've Worked Across 8 Industries and Sectors. Here's How I Know If a "
     "New Role Is Actually Growth.", "Video 6"),
   trigger="The job is to know what travels, translate it clearly, relearn "
           "what does not, and prove the level you are asking someone else "
           "to trust.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="V5_WatchNext_Change_Jobs.png pointed at V1. The corrected sequence "
       "runs V5 into V6, so the destination and the copy both change."),
]

# ------------------------------------------------------------------- V6
# Regular long-form. Work / Judgment / Evidence is preserved from the
# September 9 package; the personal-authority framing and the broader
# role-growth argument are new.
SETS[6] = [
 F(key="v6_01_movement_is_not_growth",
   draw=lambda c: X.statement(
     c, "Eight industries and sectors",
     "Movement can look like career growth long before the work actually "
     "changes.", None, dark=True, size=76),
   trigger="I have worked across eight industries and sectors, and one thing "
           "that taught me is that movement can look like career growth long "
           "before the work actually changes.",
   purpose="The hook, carrying the personal warrant without becoming "
           "autobiography.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="NEW",
   why="The eight-industries warrant is new to the corrected master. "
       "V6_MG01_New_Title_Same_Work.png opened differently."),

 F(key="v6_02_work_judgment_evidence",
   draw=lambda c: X.trio(
     c, "Three things I want answered", None,
     [("WORK", "Will the problem actually change?"),
      ("JUDGMENT", "Will my decision rights expand?"),
      ("EVIDENCE", "Will the growth travel somewhere else?")],
     foot="A role does not have to maximize growth to be a good decision."),
   trigger="So when I judge a new role now, I want three things answered: "
           "will the Work change, will my Judgment expand, and will the "
           "Evidence travel?",
   purpose="The framework, delivered early.",
   reveal="One column at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 4 on the complete set.",
   sound="Candidate: one tick as the third column lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 22% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: V6_MG02_Three_Questions.png carries "
       "the same Work / Judgment / Evidence framework and the "
       "corrected master preserves it. The copy is updated to the "
       "corrected question wording, so the render is regenerated "
       "rather than carried across as a file."),

 F(key="v6_03_harder_later",
   draw=lambda c: X.duo(
     c, "Why this gets harder later in a career", None,
     ("Earlier", "Almost any new responsibility can teach you something."),
     ("Later", "Is this role expanding what you can carry, or simply using "
               "more of what you already know?"),
     foot="The problem is calling every move development when the work "
          "underneath it has barely changed."),
   trigger="Earlier in a career, almost any new responsibility can teach you "
           "something.",
   purpose="Establish why the framework is needed at this career stage.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds left, 3 right, 3 foot.",
   sound="Not a candidate.",
   status="NEW",
   why="The broader role-growth argument is new to the corrected master."),

 F(key="v6_04_ordinary_monday",
   draw=lambda c: X.statement(
     c, "Work", "Start with an ordinary Monday.",
     "What problems will you own? Which customers, systems, regulations, "
     "operating models, or stakeholders will you have to understand that you "
     "do not understand today?", dark=True, size=92, support_size=42),
   trigger="Start with an ordinary Monday.",
   purpose="The single most practical instruction in the video.",
   reveal="The instruction alone. Hold. Then the questions.",
   emphasis="The instruction, at maximum size.",
   hold="2 seconds alone, 4 with the questions.",
   sound="Strong candidate: one soft tick as the instruction lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 44% of the "
       "text is shared with the closest prior card, which read: "
       "QUESTION ONE WHAT WILL BE DIFFERENT ON AN ORDINARY MONDAY? "
       "Problems · Systems · Stakeholders · Context. The editorial "
       "note written when this card was built, kept as written: "
       "V6_MG03_Ordinary_Monday.png carries the same instruction and "
       "the corrected master keeps it verbatim. Regenerated because "
       "the supporting questions changed."),

 F(key="v6_05_responsibility_is_not_judgment",
   draw=lambda c: X.duo(
     c, "Judgment", None,
     ("Responsibility", "You own the deadline."),
     ("Judgment", "Somebody else still controls scope, resources, sequence, "
                  "and the decision that determines whether the deadline is "
                  "possible."),
     foot="If accountability is growing and your judgment has nowhere to go, "
          "keep investigating."),
   trigger="Responsibility is not the same as judgment.",
   purpose="The distinction the framework turns on.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="V6_MG04_Tasks_Vs_Judgment.png held the adjacent tasks-versus-"
       "judgment idea. The corrected master sharpens it into "
       "responsibility-versus-judgment, so the copy is replaced."),

 F(key="v6_06_three_kinds_of_return",
   draw=lambda c: X.trio(
     c, "Evidence", None,
     [("A RESULT", "I can support."),
      ("JUDGMENT", "I can explain."),
      ("RANGE", "I did not have before.")],
     foot="If the role produces none of those, I want to know what I am "
          "getting instead."),
   trigger="I look for three kinds of return: a result I can support, "
           "judgment I can explain, and range I did not have before.",
   purpose="Make Evidence checkable rather than abstract.",
   reveal="One column at a time.",
   emphasis="The foot line.",
   hold="2 seconds each, 3 on the foot.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="V6_MG05_Portable_Evidence.png covered portable evidence. The "
       "corrected master names three specific returns, so the copy is "
       "replaced."),

 F(key="v6_07_read_the_three_answers",
   draw=lambda c: X.trio(
     c, "Read the three answers", None,
     [("ALL THREE YES", "You can see what the work is likely to build."),
      ("TWO YES", "Negotiate the missing one, do not reject the role."),
      ("ZERO OR ONE", "Movement. Be accurate about what it gives you.")],
     foot="A new employer can give you a new logo and the same work."),
   trigger="If two are yes, identify the missing dimension.",
   purpose="The read, which is where the framework becomes a decision.",
   mode="FULL SCREEN",
   reveal="One column per answer as each is named, then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per column, 5 on the complete frame.",
   captions="Suppressed.",
   sound="Candidate: one tick as the foot line lands.",
   after="Return to camera.",
   status="NEW",
   why="The section it serves was cut out of the compressed master and is "
       "restored from the approved September 9 master, so no prior card "
       "exists for it."),
 F(key="v6_07_twelve_month_question",
   draw=lambda c: X.statement(
     c, "The 12-month question",
     "Twelve months from now, what will I be able to do, decide, or prove "
     "that I cannot do today?",
     "If the answer is mostly 'I will be busier, more visible, and managing "
     "more of the same,' you have learned something important.",
     dark=True, size=64, support_size=42),
   trigger="Then ask one question: twelve months from now, what will I be "
           "able to do, decide, or prove that I cannot do today?",
   purpose="The take-away question. The frame viewers photograph.",
   reveal="Question. Hold long. Then the support line.",
   emphasis="The question.",
   hold="At least 5 seconds.",
   sound="Strong candidate: one soft tick as the question lands.",
   status="NEW",
   why="The 12-month question is named in the corrected framework and has "
       "no prior asset."),

 F(key="v6_08_what_this_cannot_solve",
   draw=lambda c: X.labeled_rows(
     c, "What this test cannot solve", None,
     [("THE EMPLOYER",
       "Your company may not contain the work. A manager may control "
       "access. Compensation bands and politics set limits."),
      ("BIAS",
       "Bias and age discrimination shape who gets access to "
       "opportunities."),
      ("YOUR LIFE",
       "Caregiving, benefits, immigration status, health and timing can "
       "outweigh the developmental case.")],
     dark=True),
   trigger="These three questions read the work. They do not replace the "
           "rest of the decision.",
   purpose="The boundary. The channel never implies that reading the work "
           "settles the decision.",
   mode="FULL SCREEN",
   reveal="One row at a time.",
   emphasis="THE EMPLOYER.",
   hold="3 seconds per row, 5 on the complete frame.",
   captions="Suppressed.",
   sound="Not a candidate. Let this one land quietly.",
   after="Return to camera.",
   status="NEW",
   why="The section it serves was cut out of the compressed master and is "
       "restored from the approved September 9 master, so no prior card "
       "exists for it."),
 F(key="v6_08_yes_no_negotiate",
   draw=lambda c: X.three_lines(
     c, "Before your next move", None,
     ["Write one sentence under Work.",
      "One under Judgment.",
      "One under Evidence."],
     foot="If one area is weak, ask whether it can be redesigned before you "
          "accept.", size=56),
   trigger="Before your next move, write one sentence under Work, Judgment, "
           "and Evidence.",
   purpose="The application, and the negotiate option most advice omits.",
   reveal="One line at a time, then the foot.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="V6_MG07_Questions_To_Ask.png covered the asking step. The corrected "
       "master ends on a written yes, no or negotiate decision."),

 F(key="v6_09_cta",
   draw=lambda c: X.cta(
     c, "One sentence each", "Work. Judgment. Evidence.",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="If you are actively deciding whether to stay, move internally, or "
           "leave, the free Career Decision Evidence Check gives you a "
           "structured way to read the evidence behind that choice. It is "
           "linked below.",
   purpose="The single action named by the corrected master. The resource "
           "route lives in the description and the pinned comment, not on "
           "this card.",
   reveal="Label, headline, the three words, then the closing line.",
   emphasis="The three words.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Rebuilt for the restored master. The compressed September 11 "
       "master had no spoken CTA at all, so this card correctly "
       "carried the action alone. The restored master speaks the Career Decision Evidence Check "
       "once after the teaching, exactly as the approved September 9 "
       "master did, so the card carries the route again."),

 F(key="v6_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "It Took Me Years to Stop Mistaking More Work for Career Growth",
     "Video 7"),
   trigger="That is what we are testing next in 'It Took Me Years to Stop "
           "Mistaking More Work for Career Growth.'",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Card unchanged. The trigger moves to the restored "
       "spoken Watch Next line. The compressed master had "
       "no spoken handoff, so the card had been cued off "
       "the final teaching sentence instead."),
]

# ------------------------------------------------------------------- V7
# Regular long-form. CAR is preserved from the September 9 package. The
# opening and the lived-experience framing are revised.
SETS[7] = [
 F(key="v7_01_valuable_to_them_not_to_you",
   draw=lambda c: X.statement(
     c, "The trade nobody names",
     "You can become more valuable to your organization without becoming "
     "more valuable to your own future.",
     "It took me years to learn that being trusted with more is not the same "
     "as being developed for more.", dark=True, size=66, support_size=42),
   trigger="You can become more valuable to your organization without "
           "becoming more valuable to your own future.",
   purpose="The hook, and the sentence the title is built from.",
   reveal="Headline. Hold. Then the personal line.",
   emphasis="The headline.",
   hold="3 seconds, then 3 with the support.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="V7_MG01_Opening_Consequence.png opened on a different consequence. "
       "The corrected master opens on the value trade, so the frame is "
       "rebuilt."),

 F(key="v7_02_car",
   draw=lambda c: X.trio(
     c, "Three tests", None,
     [("COMPLEXITY", "Did the problem get harder, or did the volume get "
                     "bigger?"),
      ("AUTHORITY", "Did your decision rights move with the "
                    "responsibility?"),
      ("RETURN", "What is the extra work giving back?")],
     foot="CAR is not a score. You are looking for a pattern."),
   trigger="I use three tests now: Complexity, Authority, Return. CAR.",
   purpose="The framework, delivered in the first minute.",
   reveal="One column at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 4 on the complete set.",
   sound="Candidate: one tick as the third column lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 10% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: V7_MG02_CAR_Framework.png carries the "
       "same framework and the corrected master preserves CAR "
       "exactly. Regenerated because the question wording under each "
       "letter is updated."),

 F(key="v7_03_dependable_people",
   draw=lambda c: X.duo(
     c, "Why dependable people are vulnerable", None,
     ("Arrives quickly", "Work."),
     ("Arrives later, if at all",
      "Authority, support, recognition, and formal scope."),
     foot="Temporary coverage quietly becomes the permanent design of your "
          "job."),
   trigger="Reliability attracts work quickly. Authority, support, "
           "recognition, and formal scope often arrive later, if they arrive "
           "at all.",
   purpose="Explain the mechanism so the viewer does not read it as a "
           "personal failing.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds per side, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The corrected master adds this mechanism section."),

 F(key="v7_04_complexity",
   draw=lambda c: X.duo(
     c, "Complexity", None,
     ("Capacity use", "Three nearly identical projects last year. Eight "
                      "now."),
     ("Complexity", "A new customer, a new regulation, a different operating "
                    "model, conflicting priorities, incomplete "
                    "instructions."),
     foot="If the only answer is 'more of the same,' call that capacity use. "
          "Do not automatically call it growth.",
     dark=True),
   trigger="Complexity changes when the variables change: a new customer, a "
           "new regulation, a different operating model, conflicting "
           "priorities, incomplete instructions, stakeholders whose "
           "incentives do not line up.",
   purpose="The first test, made checkable.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 6% of its "
       "text. The editorial note written when this card was built, "
       "kept as written: V7_MG03_Complexity.png covers the same test "
       "and the corrected master preserves it. Copy updated to the "
       "corrected variable list."),

 F(key="v7_05_authority",
   draw=lambda c: X.trio(
     c, "Authority", None,
     [("RESPONSIBILITY", "What you are expected to carry."),
      ("ACCOUNTABILITY", "What you will answer for."),
      ("AUTHORITY", "What you can influence or decide.")],
     foot="Those three do not always expand together."),
   trigger="Responsibility is what you are expected to carry. "
           "Accountability is what you will answer for. Authority is what "
           "you can influence or decide. Those three do not always expand "
           "together.",
   purpose="The three-way separation that makes the second test usable.",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 70% of the "
       "text is shared with the prior card, which read: A IS FOR "
       "AUTHORITY Three words people use as one. RESPONSIBILITY What "
       "you carry. ACCOUNTABILITY What you answ…. The editorial note "
       "written when this card was built, kept as written: "
       "V7_MG04_Authority.png carries the same three-way separation, "
       "preserved by the corrected master."),

 F(key="v7_06_return",
   draw=lambda c: X.trio(
     c, "Return", None,
     [("CAPABILITY", "You did not have before."),
      ("EVIDENCE", "You could not previously claim."),
      ("RECOGNITION", "Tied to the contribution.")],
     foot="Praise is welcome. Praise alone is not role design."),
   trigger="I look in three places: capability, evidence, and recognition.",
   purpose="The third test, and the line that lands hardest.",
   reveal="One column at a time, then the foot line, which holds longest.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Strong candidate: one soft tick as the foot line lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 44% of the "
       "text is shared with the closest prior card, which read: R IS "
       "FOR RETURN 01 CAPABILITY 02 EVIDENCE 03 RECOGNITION What did "
       "the work return?. The editorial note written when this card "
       "was built, kept as written: V7_MG05_Return.png carries the "
       "same three returns and the praise line, both preserved by the "
       "corrected master."),

 F(key="v7_07_read_the_car_pattern",
   draw=lambda c: X.trio(
     c, "Read CAR as a pattern", None,
     [("ALL THREE EXPANDING", "Demanding, but you can see what it builds."),
      ("COMPLEXITY ONLY", "A stretch assignment with a design problem."),
      ("VOLUME ONLY", "The role expanded mainly as workload.")],
     foot="Give the season a boundary. Coverage without a review date "
          "becomes the baseline."),
   trigger="If volume increased but Complexity, Authority, and Return did "
           "not, the role has expanded mainly as workload.",
   purpose="The read. CAR is a pattern, not a score.",
   mode="FULL SCREEN",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per column, 5 on the complete frame.",
   captions="Suppressed.",
   sound="Candidate: one tick as the foot line lands.",
   after="Return to camera.",
   status="NEW",
   why="The section it serves was cut out of the compressed master and is "
       "restored from the approved September 9 master, so no prior card "
       "exists for it."),
 F(key="v7_07_review_point",
   draw=lambda c: X.three_lines(
     c, "Before the next 'Can you take this too?'", None,
     ["What becomes more complex?",
      "What authority comes with it?",
      "When will we review what this additional scope returns?"],
     foot="Temporary stretch without a review point becomes permanent "
          "absorption.", dark=True, size=52),
   trigger="Before the next ‘Can you take this too?’, ask: what becomes more "
           "complex? What authority comes with it? When will we review what "
           "this additional scope returns?",
   purpose="The application. The third question is the one people omit.",
   reveal="One question at a time. The third holds longest.",
   emphasis="The third question.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the third question lands.",
   status="COPY UPDATE",
   why="V7_MG06_Pattern_Read.png covered reading the pattern. The corrected "
       "master ends on three questions asked before saying yes."),

 F(key="v7_08_scope_conversation",
   draw=lambda c: X.numbered(
     c, "Take four questions to your manager",
     ["Which of these responsibilities should remain with me?",
      "What should come off my plate as this becomes part of my role?",
      "Which decisions need to belong to me for these outcomes?",
      "How and when will the expanded scope be formally reviewed?"],
     foot="Stronger than 'I have too much work.'", size=46),
   trigger="Then take four questions into the conversation with your "
           "manager: Which of these responsibilities should remain with me?",
   purpose="The viewer tool. This is the conversation the video is for.",
   mode="FULL SCREEN",
   reveal="One question at a time, then the foot line.",
   emphasis="The fourth question.",
   hold="2 seconds per question, 5 on the complete frame.",
   captions="Suppressed.",
   sound="Candidate: one soft tick per question.",
   after="Return to camera.",
   status="NEW",
   why="The section it serves was cut out of the compressed master and is "
       "restored from the approved September 9 master, so no prior card "
       "exists for it."),
 F(key="v7_08_more_work_is_not_proof",
   draw=lambda c: X.statement(
     c, None, "More work can be part of growth. It is not proof of it.",
     None, dark=True, size=88),
   trigger="More work can be part of growth. It is not proof of it.",
   purpose="The final spoken line at full size, and the thumbnail's "
           "argument.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   after="Move to the resource card, then Watch Next.",
   status="NEW",
   why="The corrected master's closing line differs from the September 9 "
       "ending."),

 F(key="v7_09_cta",
   draw=lambda c: X.cta(
     c, "Run CAR", "On one responsibility you added in the last six months.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="If you want a structured way to examine what your current work is "
           "actually building in you, the Capability Formation Field Kit helps "
           "you read the evidence in your role, see where your options may be "
           "expanding or narrowing, and identify where the role may need a "
           "boundary or redesign. It is linked below.",
   purpose="The single action named by the corrected master. The resource "
           "route lives in the description and the pinned comment, not on "
           "this card.",
   reveal="Label, headline, the three words, then the closing line.",
   emphasis="The three words.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Rebuilt for the restored master. The compressed September 11 "
       "master had no spoken CTA at all, so this card correctly "
       "carried the action alone. The restored master speaks the Field Kit "
       "once after the teaching, exactly as the approved September 9 "
       "master did, so the card carries the route again."),

 F(key="v7_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Show Your Impact at Work When You Built It From Scratch",
     "Video 8"),
   trigger="In the next video, I will show you how to make that work visible: "
           "'How to Show Your Impact at Work When You Built It From Scratch.'",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Card unchanged. The trigger moves to the restored "
       "spoken Watch Next line. The compressed master had "
       "no spoken handoff, so the card had been cued off "
       "the final teaching sentence instead."),
]

# ------------------------------------------------------------------- V8
# Regular long-form. Same broad topic, materially revised teaching
# structure: Before / My Part / Judgment / Proof, plus the evidence levels
# Existence / Use / Effect.
SETS[8] = [
 F(key="v8_01_success_hides_the_work",
   draw=lambda c: X.statement(
     c, "Built from scratch",
     "If you do it well enough, eventually nobody can see how hard it was.",
     "The uncertainty you had to solve at the beginning has disappeared from "
     "view.", dark=True, size=72, support_size=42),
   trigger="One of the strangest things about building something from "
           "scratch is that if you do it well enough, eventually nobody can "
           "see how hard it was.",
   purpose="The hook.",
   reveal="Headline. Hold. Then the support line.",
   emphasis="The headline.",
   hold="3 seconds, then 3 with the support.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 32% of the "
       "text is shared with the closest prior card, which read: THE "
       "WORKED EXAMPLE “ITS EFFECT HAD NOT YET BEEN ESTABLISHED.” "
       "That last sentence does not weaken the story. I…. The "
       "editorial note written when this card was built, kept as "
       "written: The prior package opened on the same disappearance "
       "idea and the corrected master preserves it. Copy updated to "
       "the corrected wording."),

 F(key="v8_02_four_things",
   draw=lambda c: X.four_bucket(
     c, "Four things", None,
     [("BEFORE", "What was true before your solution existed."),
      ("MY PART", "What you personally owned, recommended, or led."),
      ("JUDGMENT", "What was not obvious at the start."),
      ("PROOF", "The strongest result you can support.")]),
   trigger="So I use four things: the Before, My Part, the Judgment, and the "
           "Proof.",
   purpose="The framework, delivered early.",
   reveal="One bucket at a time in spoken order.",
   emphasis="Equal.",
   hold="2 seconds each, 4 on the complete grid.",
   sound="Candidate: one tick on the fourth bucket.",
   status="REBUILD",
   why="The prior package used reconstruct-the-before, show-the-judgment, "
       "keep-the-proof as three steps. The corrected master uses four named "
       "elements, so the framework asset is rebuilt."),

 F(key="v8_03_finished_hides_conditions",
   draw=lambda c: X.duo(
     c, "Finished work hides unfinished conditions", None,
     ("You say", "'I built the process.'"),
     ("They see", "A process. Not the conflicting expectations, the missing "
                  "rule, the tradeoffs, or the decisions that had no obvious "
                  "owner."),
     foot="The solution is not to make the story more dramatic. It is to put "
          "the missing information back."),
   trigger="The solution is not to make the story more dramatic. It is to "
           "put the missing information back.",
   purpose="Name the mechanism so the fix is obvious.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds left, 4 right, 3 foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="New section in the corrected master."),

 F(key="v8_04_weak_and_strong_before",
   draw=lambda c: X.struck(
     c, "Before", None,
     "It was chaos.",
     "There was no shared way to prioritize requests or decide which issues "
     "needed escalation."),
   trigger="A weak Before is ‘It was chaos.’ A stronger Before is ‘There was "
           "no shared way to prioritize requests or decide which issues "
           "needed escalation.’",
   purpose="Show the standard rather than describing it.",
   reveal="The weak version. Hold. Struck. Then the strong version.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v8_05_accurate_attribution",
   draw=lambda c: X.statement(
     c, "My Part", "You do not need sole credit to make your contribution "
     "legible.",
     "You need accurate attribution.", size=70, support_size=48),
   trigger="You do not need sole credit to make your contribution legible. "
           "You need accurate attribution.",
   purpose="The line that keeps the video honest about team work.",
   reveal="Headline, then the support line.",
   emphasis="The support line.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 38% of the "
       "text is shared with the closest prior card, which read: NOW "
       "IT LOOKS EASY. That is exactly why your contribution can "
       "become harder to see.. The editorial note written when this "
       "card was built, kept as written: The prior package carried a "
       "do-not-imply-sole-authorship boundary and the corrected "
       "master states it as a positive rule."),

 F(key="v8_06_judgment_not_the_artifact",
   draw=lambda c: X.duo(
     c, "Judgment", None,
     ("The artifact", "The intake form may be the least interesting part."),
     ("The judgment",
      "What the team would accept, what required an exception, who could "
      "change priority, how two competing needs would be resolved."),
     foot="What was not obvious at the start?",
     dark=True),
   trigger="If you created an intake form, the form may be the least "
           "interesting part.",
   purpose="The most transferable insight in the video.",
   reveal="Left. Then right. Then the foot question.",
   emphasis="The right side.",
   hold="2 seconds left, 4 right, 3 foot.",
   sound="Candidate: one tick as the right side lands.",
   status="NEW",
   why="New example and new framing in the corrected master."),

 F(key="v8_07_existence_use_effect",
   draw=lambda c: X.trio(
     c, "Proof: three levels of evidence", None,
     [("EXISTENCE", "The thing was created."),
      ("USE", "People actually adopted it."),
      ("EFFECT", "Something important changed because of the work.")],
     foot="Do not jump from existence to effect because effect sounds more "
          "impressive."),
   trigger="For foundational work, I separate three levels of evidence: "
           "Existence, Use, Effect.",
   purpose="The sharpest distinction in the video and the reason it is "
           "credible.",
   reveal="One level at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Strong candidate: one soft tick as the foot line lands.",
   status="NEW",
   why="Existence / Use / Effect is new to the corrected master and is the "
       "most important addition in this video."),

 F(key="v8_08_evidence_boundary",
   draw=lambda c: X.statement(
     c, "The boundary", "Proof does not mean taking your employer's files.",
     "Removing a name does not create permission to keep restricted "
     "material. Your own written account can preserve the structure of the "
     "evidence without preserving confidential material.",
     dark=True, size=72, support_size=40),
   trigger="Proof does not mean taking your employer's files.",
   purpose="The legal and ethical boundary, stated plainly on screen.",
   mode="FULL SCREEN",
   reveal="Headline alone. Hold. Then the support line.",
   emphasis="The headline.",
   hold="3 seconds alone, 4 with the support.",
   captions="Suppressed.",
   sound="Not a candidate.",
   after="Return to camera.",
   status="NEW",
   why="The corrected master carries this boundary and no prior rendered "
       "card presented it full screen."),
 F(key="v8_08_four_sentence_account",
   draw=lambda c: X.labeled_rows(
     c, "The four-sentence impact account", None,
     [("Before", "What was true before this existed?"),
      ("My Part", "What did I own, recommend, or lead?"),
      ("Judgment", "What was not obvious that I had to work out?"),
      ("Proof", "The strongest result I can support without overstating "
                "causation.")]),
   trigger="Put it together in four sentences.",
   purpose="The artifact. The frame viewers photograph.",
   reveal="One row at a time.",
   emphasis="The Proof row, which carries the causation caution.",
   hold="3 seconds per row, 4 on the complete frame.",
   sound="Candidate: one tick as the fourth row lands.",
   status="REBUILD",
   why="The prior package had a before-and-after account. The corrected "
       "master specifies four named sentences, so the artifact is rebuilt."),

 F(key="v8_09_cta",
   draw=lambda c: X.cta(
     c, "One thing people take for granted",
     "Write the four sentences.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="Keep the Proof is linked below if you want the deeper evidence "
           "system and reusable ledger. But the four-sentence account from "
           "this video stands on its own.",
   purpose="The single action named by the corrected master. The resource "
           "route lives in the description and the pinned comment, not on "
           "this card.",
   reveal="Label, headline, the four words, then the closing line.",
   emphasis="The four words.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Rebuilt for the restored master. The compressed September 11 "
       "master had no spoken CTA at all, so this card correctly "
       "carried the action alone. The restored master speaks Keep the Proof "
       "once after the teaching, exactly as the approved September 9 "
       "master did, so the card carries the route again."),

 F(key="v8_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Change Industries Without Starting Over", "Video 9"),
   trigger="Watch 'How to Change Industries Without Starting Over' next.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Card unchanged. The trigger moves to the restored "
       "spoken Watch Next line. The compressed master had "
       "no spoken handoff, so the card had been cued off "
       "the final teaching sentence instead."),
]

# ------------------------------------------------------------------- V9
SETS[9] = [
 F(key="v9_01_direct_industry_experience",
   draw=lambda c: X.statement(
     c, "One sentence in a job description",
     "“Direct industry experience required.”",
     "You know you have done difficult work. You know you are not starting "
     "your career over.", dark=True, size=84, support_size=42),
   trigger="“Direct industry experience required.”",
   purpose="The hook. The exact sentence that triggers the feeling.",
   reveal="The quoted line alone. Hold. Then the support.",
   emphasis="The quoted line.",
   hold="2 seconds alone, 3 with the support.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="V9's prior opening asset addressed the same status tension. The "
       "corrected master sharpens it to the posting sentence itself."),

 F(key="v9_02_neither_mistake",
   draw=lambda c: X.struck(
     c, "Do not make either mistake", None,
     ["I can already do all of this.", "None of my experience counts here."],
     "Which part of this destination can I support with evidence now, and "
     "which part still needs to be learned, earned, or verified?"),
   trigger="Do not say, “I can already do all of this.”",
   purpose="Kill both failure modes before the framework arrives.",
   reveal="Both claims. Hold. Struck. Then the better question.",
   emphasis="The strike, then the question.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="NEW",
   why="The corrected master states both mistakes explicitly in the hook."),

 F(key="v9_03_capability_context_credentials",
   draw=lambda c: X.trio(
     c, "Separate three things", None,
     [("CAPABILITY", "What can you already prove?"),
      ("CONTEXT", "What changes in this setting?"),
      ("CREDENTIALS", "What do you genuinely need before the door is "
                      "open?")]),
   trigger="Capability. Context. Credentials.",
   purpose="The framework, delivered inside the first ninety seconds.",
   reveal="One column at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 4 on the complete set.",
   sound="Candidate: one tick as the third column lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 48% of the "
       "text is shared with the closest prior card, which read: THE "
       "THREE-PART READ 01 CAPABILITY 02 CONTEXT 03 CREDENTIALS What "
       "can you prove? What changes here? What is ac…. The editorial "
       "note written when this card was built, kept as written: The "
       "prior V9 package carries the same three-part framework and "
       "the corrected master preserves it. Copy updated to the "
       "corrected questions."),

 F(key="v9_04_same_verb_different_decision",
   draw=lambda c: X.word_vs_work(
     c, "Do not declare equivalence from a shared verb", "APPROVE",
     "In one role", "Checking a routine item.",
     "In another", "Accepting a consequential risk."),
   trigger="“Approve” can mean checking a routine item in one role and "
           "accepting a consequential risk in another.",
   purpose="The transfer boundary, in one frame.",
   reveal="The verb alone. Hold. Then each reading.",
   emphasis="The verb.",
   hold="2 seconds on the verb, 2 per side.",
   sound="Candidate: one tick as the second reading lands.",
   status="NEW",
   why="The corrected master adds this explicit equivalence warning."),

 F(key="v9_05_capability_sentence",
   draw=lambda c: X.statement(
     c, "Write the capability sentence", "“This role needs someone to handle "
     "this problem. My evidence is this example.”",
     "If you cannot finish both halves, you have a question to investigate, "
     "not yet a transfer claim.", size=60, support_size=42),
   trigger="Write the capability sentence this way:",
   purpose="Turn the first layer into one writable sentence.",
   reveal="The sentence, then the condition.",
   emphasis="The sentence.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v9_06_context_is_not_vocabulary",
   draw=lambda c: X.statement(
     c, "Context", "Context is not just vocabulary you can learn over a "
     "weekend.",
     "It can change which answer is responsible.", dark=True, size=68,
     support_size=48),
   trigger="Context is not just vocabulary you can learn over a weekend.",
   purpose="The line that stops the viewer underestimating the second "
           "layer.",
   reveal="Headline, then the support line.",
   emphasis="The support line.",
   hold="At least 4 seconds.",
   sound="Strong candidate: one soft tick as the support line lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v9_07_better_question_to_ask",
   draw=lambda c: X.struck(
     c, "Ask a better question", None,
     "Do you think I could switch industries?",
     "Where do otherwise experienced people tend to need the most support "
     "when they first enter this role?"),
   trigger="“Do you think I could switch industries?”",
   purpose="The single most practical instruction in the video.",
   reveal="The weak question. Hold. Struck. Then the better one.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Candidate: one tick as the strike lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v9_08_credential_three_labels",
   draw=lambda c: X.three_lines(
     c, "Credentials: write down three labels", None,
     ["Confirmed requirement.", "Preferred qualification.",
      "Still unclear."],
     foot="You do not argue a closed requirement open with better wording.",
     dark=True, size=62),
   trigger="Write down:",
   purpose="Make the third layer checkable, and state the hard boundary.",
   reveal="One label at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Strong candidate: one soft tick as the foot line lands.",
   status="COPY UPDATE",
   why="The prior package addressed credentials. The corrected master "
       "specifies these three labels, so the copy is replaced."),

 F(key="v9_09_cta",
   draw=lambda c: X.cta(
     c, "One destination role", "Capability. Context. Credentials.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="Choose one destination role. Not five industries at once.",
   purpose="The resource route named by the corrected master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 41% of the "
       "text is shared with the closest prior card, which read: THE "
       "THREE-PART READ 01 CAPABILITY 02 CONTEXT 03 CREDENTIALS What "
       "can you prove? What changes here? What is ac…. The editorial "
       "note written when this card was built, kept as written: The "
       "prior package routed V9 to the Field Kit and the corrected "
       "master keeps that route."),

 F(key="v9_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "Before a Layoff, Know What You Can Still Prove", "Video 10"),
   trigger="Watch “Before a Layoff, Know What You Can Still Prove” next.",
   purpose="The final visual, cued by the spoken handoff.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 93% of the "
       "text is shared with the prior card, which read: WATCH NEXT "
       "Before a Layoff, Know What You Can Still Prove. The editorial "
       "note written when this card was built, kept as written: "
       "Destination and title unchanged from the prior package."),
]

# ------------------------------------------------------------------- V10
SETS[10] = [
 F(key="v10_01_access_ends",
   draw=lambda c: X.duo(
     c, "Imagine the job ends tomorrow", None,
     ("Your experience", "Did not disappear."),
     ("Your access to the evidence", "Did."),
     foot="Know what you can still prove before you urgently need to explain "
          "it.",
     dark=True),
   trigger="Your experience did not disappear.",
   purpose="The hook, in one comparison.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="2 seconds per side, 3 on the foot.",
   sound="Candidate: one soft tick as the right side lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 57% of the "
       "text is shared with the closest prior card, which read: YOUR "
       "EXPERIENCE DID NOT DISAPPEAR. YOUR ACCESS TO THE EVIDENCE "
       "DID.. The editorial note written when this card was built, "
       "kept as written: V10_MG01_Access_Not_Experience.png carries "
       "the same distinction and the corrected master preserves it."),

 F(key="v10_02_preparation_not_extraction",
   draw=lambda c: X.statement(
     c, "The boundary", "Preparation is not extraction.",
     "Access to a document does not mean you are entitled to keep it. "
     "Removing a company name does not automatically make restricted "
     "material yours to retain.", dark=True, size=92, support_size=40),
   trigger="Access to a document does not mean you are entitled to keep it. "
           "Removing a company name does not automatically make restricted "
           "material yours to retain.",
   purpose="The compliance boundary, placed immediately after the stakes.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, 4 with the support. Do not rush this.",
   sound="Not a candidate. This frame should land in silence.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 49% of the "
       "text is shared with the closest prior card, which read: THE "
       "BOUNDARY PREPARATION IS NOT EXTRACTION. No forwarding "
       "internal emails, downloading dashboards, copying cu…. The "
       "editorial note written when this card was built, kept as "
       "written: V10_MG02_Preparation_Is_Not_Extraction.png carries "
       "the same boundary, preserved by the corrected master."),

 F(key="v10_03_capture_qualify_retrieve",
   draw=lambda c: X.trio(
     c, "An evidence habit", None,
     [("CAPTURE", "The contribution, not the calendar."),
      ("QUALIFY", "The claim."),
      ("RETRIEVE", "Make it findable when the question changes.")]),
   trigger="Capture the contribution.",
   purpose="The framework.",
   reveal="One column at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 4 on the complete set.",
   sound="Candidate: one tick as the third column lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 68% of the "
       "text is shared with the prior card, which read: THE EVIDENCE "
       "HABIT 01 CAPTURE THE CONTRIBUTION 02 QUALIFY THE CLAIM 03 "
       "MAKE IT RETRIEVABLE. The editorial note written when this "
       "card was built, kept as written: "
       "V10_MG03_Capture_Qualify_Retrieve.png carries the same three "
       "steps, preserved by the corrected master."),

 F(key="v10_04_calendar_vs_contribution",
   draw=lambda c: X.struck(
     c, "Capture the contribution, not the calendar", None,
     "Attended weekly implementation meetings.",
     "I identified conflicting completion criteria and helped the teams "
     "agree what needed to be true before handoff."),
   trigger="“Attended weekly implementation meetings.”",
   purpose="Show the standard rather than describing it.",
   reveal="The calendar entry. Hold. Struck. Then the real record.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 85% of the "
       "text is shared with the prior card, which read: One | Capture "
       "the contribution, not the calendar. THE CALENDAR ENTRY "
       "“Attended weekly implementation meetings…. The editorial note "
       "written when this card was built, kept as written: "
       "V10_MG04_Calendar_Versus_Contribution.png carries the same "
       "comparison. Copy updated to the corrected example."),

 F(key="v10_05_three_labels",
   draw=lambda c: X.trio(
     c, "Qualify the claim", None,
     [("CONFIRMED", "You have a permitted basis for the statement."),
      ("QUALIFIED", "The result needs its scope attached."),
      ("NOT YET VERIFIED", "Do not present it as established.")],
     foot="Their job is to stop uncertainty from disappearing when you "
          "shorten the story later."),
   trigger="Now put one of three labels beside the result:",
   purpose="The discipline that makes the record survive scrutiny.",
   reveal="One label at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 3 on the foot.",
   sound="Candidate: one tick as the third label lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 4% of its "
       "text. The editorial note written when this card was built, "
       "kept as written: "
       "V10_MG05_Confirmed_Qualified_Not_Verified.png carries the "
       "same three labels, preserved by the corrected master."),

 F(key="v10_06_language_that_survives",
   draw=lambda c: X.statement(
     c, "Not timid language",
     "It is language that survives the next question.",
     "What exactly does this example establish? What does it not establish? "
     "What could I say if someone asked, how do you know?", dark=True,
     size=76, support_size=40),
   trigger="This is not timid language.",
   purpose="Pre-empt the reading that qualification is weakness.",
   reveal="Headline, then the three questions.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Candidate: one tick as the headline lands.",
   status="NEW",
   why="New framing in the corrected master."),

 F(key="v10_07_name_it_by_the_problem",
   draw=lambda c: X.struck(
     c, "Make it retrievable", None,
     "Project Alpha",
     "Conflicting handoff criteria"),
   trigger="“Conflicting handoff criteria” is more useful than “Project "
           "Alpha,” especially to somebody outside the company.",
   purpose="One concrete habit the viewer can adopt immediately.",
   reveal="The internal name. Hold. Struck. Then the problem name.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 3 after.",
   sound="Candidate: one tick as the strike lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 39% of the "
       "text is shared with the closest prior card, which read: THREE "
       "| MAKE IT RETRIEVABLE Name the entry by the problem, not the "
       "project. “PROJECT ALPHA” Means nothing out…. The editorial "
       "note written when this card was built, kept as written: "
       "V10_MG06_Name_It_By_The_Problem.png carries the same habit, "
       "preserved by the corrected master."),

 F(key="v10_08_two_reasons_evidence_is_thin",
   draw=lambda c: X.duo(
     c, "Two very different reasons an example is missing", None,
     ("You did the work", "And failed to capture it clearly. That needs "
                          "reconstruction."),
     ("You never had the opportunity",
      "To own the decision, access the result, or build that part of your "
      "range. That needs an honest account."),
     foot="Do not solve both problems by writing a stronger sentence."),
   trigger="Do not solve both problems by writing a stronger sentence.",
   purpose="The honesty beat, and the most useful diagnostic in the video.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 20% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: "
       "V10_MG07_Two_Reasons_Evidence_Is_Thin.png carries the same "
       "distinction, preserved by the corrected master."),

 F(key="v10_09_cta",
   draw=lambda c: X.cta(
     c, "Start with one entry",
     "Capture. Qualify. Make it retrievable.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="Start with one entry.",
   purpose="The resource route named by the corrected master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 44% of the "
       "text is shared with the closest prior card, which read: THE "
       "EVIDENCE HABIT 01 CAPTURE THE CONTRIBUTION 02 QUALIFY THE "
       "CLAIM 03 MAKE IT RETRIEVABLE. The editorial note written when "
       "this card was built, kept as written: "
       "V10_RESOURCE_Keep_The_Proof.png routes to the same resource, "
       "preserved by the corrected master."),

 F(key="v10_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "AI Can Do the Task. What Are You Still Paid For?", "Video 11"),
   trigger="Watch “AI Can Do the Task. What Are You Still Paid For?” next.",
   purpose="The final visual, cued by the spoken handoff.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="V10_WATCH_NEXT_AI_Can_Do_The_Task.png points at the same "
       "destination with the same title."),
]

# ------------------------------------------------------------------- V11
SETS[11] = [
 F(key="v11_01_can_we_reduce_the_team",
   draw=lambda c: X.statement(
     c, "The report is ready", "“Does this mean we can reduce the team?”",
     "That is the moment the job changes.", dark=True, size=80,
     support_size=46),
   trigger="“Does this mean we can reduce the team?”",
   purpose="The hook. A status threat, not an abstract AI question.",
   reveal="The question alone. Hold. Then the line under it.",
   emphasis="The question.",
   hold="2 seconds alone, 3 with the support.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 88% of the "
       "text is shared with the prior card, which read: “DOES THIS "
       "MEAN WE CAN REDUCE THE TEAM?” That is the moment the job "
       "changes.. The editorial note written when this card was "
       "built, kept as written: V11_MG01_Can_We_Reduce_The_Team.png "
       "carries the same opening question, preserved by the corrected "
       "master."),

 F(key="v11_02_task_is_not_the_job",
   draw=lambda c: X.trio(
     c, "The task is not the whole job", None,
     [("PRODUCE", "What can the tool help make?"),
      ("INTERPRET", "What does the output actually establish?"),
      ("DECIDE", "Who owns the consequence?")],
     foot="And verify across all three."),
   trigger="Produce. Interpret. Decide.",
   purpose="The framework, and the thumbnail's argument.",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line, because verification runs through all three.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 50% of the "
       "text is shared with the closest prior card, which read: THE "
       "FRAMEWORK 01 PRODUCE 02 INTERPRET 03 DECIDE And verify across "
       "all three.. The editorial note written when this card was "
       "built, kept as written: V11_MG04_Produce_Interpret_Decide.png "
       "carries the same framework, preserved by the corrected "
       "master."),

 F(key="v11_03_headline_rate",
   draw=lambda c: X.statfacts(
     c, "SYNTHETIC DATA  ·  INVENTED TEACHING NUMBERS, NOT CUSTOMER DATA",
     "60% → 80%", "THE HEADLINE RATE",
     [("First period", "60 of 100"), ("Second period", "80 of 100")],
     "Invented teaching numbers. Not customer data and not a result from my "
     "career.", dark=True),
   trigger="Here is a small synthetic service report. These are invented "
           "teaching numbers, not customer data and not a result from my "
           "career.",
   purpose="Establish the demonstration and its label in the same frame.",
   reveal="The label first and permanently, then the numbers.",
   emphasis="The label is not a footer. It stays for the whole hold.",
   hold="At least 4 seconds.",
   sound="Candidate: one soft tick as the rate appears.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 8% of its "
       "text. The editorial note written when this card was built, "
       "kept as written: V11_MG02_The_Headline_Rate.png carries the "
       "same synthetic figures and label, preserved by the corrected "
       "master."),

 F(key="v11_04_the_mix_changed",
   draw=lambda c: X.duo(
     c, "SYNTHETIC DATA  ·  THE SAME NUMBERS, SPLIT", None,
     ("Routine cases", "Met the target 90% of the time in both periods."),
     ("Complex cases", "Met it 40% of the time in both periods."),
     foot="What changed was the mix. The overall number improved even though "
          "the within-category rates did not."),
   trigger="What changed was the mix. The second period had far more routine "
           "cases and fewer complex ones.",
   purpose="The reveal the whole demonstration exists for.",
   reveal="Left. Then right. Then the foot line, which holds longest.",
   emphasis="The foot line.",
   hold="3 seconds per side, 5 on the foot.",
   sound="Strong candidate: one soft tick as the foot line lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 21% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: V11_MG03_The_Mix_Changed.png carries "
       "the same reveal, preserved by the corrected master."),

 F(key="v11_05_what_it_does_not_establish",
   draw=lambda c: X.duo(
     c, "Interpret", None,
     ("It supports", "The aggregate rate rose while the mix shifted toward "
                     "the category with the higher rate."),
     ("It does not establish",
      "That people became more effective within each category, or that "
      "removing experienced staff would preserve the result."),
     foot="That does not mean reducing staff is always wrong. It means this "
          "evidence does not settle that decision.",
     dark=True),
   trigger="It does not establish that people became more effective within "
           "each category.",
   purpose="The interpretive discipline, stated without overclaiming.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line, which keeps the video fair.",
   hold="3 seconds per side, 4 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 4% of its "
       "text. The editorial note written when this card was built, "
       "kept as written: V11_MG05_What_It_Does_Not_Establish.png "
       "carries the same boundary, preserved by the corrected master."),

 F(key="v11_06_the_boundary_is_not",
   draw=lambda c: X.struck(
     c, "Where the boundary actually is", None,
     "Machines never interpret.",
     "Is this interpretation supported, relevant, and sufficient for this "
     "decision in this organization?"),
   trigger="So the boundary is not:",
   purpose="Refuse the easy anti-AI framing the topic invites.",
   reveal="The weak claim. Hold. Struck. Then the real question.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Candidate: one tick as the strike lands.",
   status="NEW",
   why="The corrected master adds this explicit refusal, which the prior "
       "package did not carry."),

 F(key="v11_07_who_owns_the_consequence",
   draw=lambda c: X.ladder(
     c, "Decide: organizational responsibilities", None,
     [("Who is authorized to make the change?", None),
      ("Which risks must be accepted or reduced?", None),
      ("What alternatives are available?", None),
      ("What would trigger a review or reversal?", None),
      ("Who will monitor what happens after?", None)],
     foot="A tool producing a recommendation does not automatically assign "
          "them to anyone.", size=46),
   trigger="Those are organizational responsibilities.",
   purpose="The third stage, made concrete.",
   reveal="One question at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 74% of the "
       "text is shared with the prior card, which read: THREE | "
       "DECIDE 01 Who is authorized to make the change? 02 Which "
       "risks must be accepted or reduced? 03 What a…. The editorial "
       "note written when this card was built, kept as written: "
       "V11_MG06_Who_Owns_The_Consequence.png carries the same set, "
       "preserved by the corrected master."),

 F(key="v11_08_map_your_role",
   draw=lambda c: X.statement(
     c, "Map your role", "Do not look for an AI-proof job.",
     "None of those findings guarantees that a job will remain. Employers "
     "can reduce roles, change scope, or choose a different operating "
     "model.", dark=True, size=88, support_size=40),
   trigger="Take one recurring output from your job.",
   purpose="The application, with the honesty attached rather than "
           "separated.",
   reveal="Headline, then the limit.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 29% of the "
       "text is shared with the closest prior card, which read: "
       "CAPABILITY FORMATION FIELD KIT A broader read of what your "
       "work is building. Not an AI certification and not …. The "
       "editorial note written when this card was built, kept as "
       "written: V11_MG07_Map_Your_Role.png carries the same "
       "application. Copy updated to attach the corrected master's "
       "limit."),

 F(key="v11_09_cta",
   draw=lambda c: X.cta(
     c, "One recurring output", "Build the three-column map.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="Choose one recurring output before your next role conversation.",
   purpose="The resource route named by the corrected master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="The prior package routed V11 to the Field Kit and the corrected "
       "master keeps that route. The headline changes with the corrected "
       "action."),

 F(key="v11_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "What to Do When You Can’t Quit Your Job Yet", "Video 12"),
   trigger="Watch “What to Do When You Can’t Quit Your Job Yet” next.",
   purpose="The final visual, cued by the spoken handoff.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 92% of the "
       "text is shared with the prior card, which read: WATCH NEXT "
       "What to Do When You Can’t Quit Your Job Yet. The editorial "
       "note written when this card was built, kept as written: "
       "Destination and title unchanged from the prior package."),
]

# ------------------------------------------------------------------- V12
SETS[12] = [
 F(key="v12_01_constraint_not_conclusion",
   draw=lambda c: X.duo(
     c, "Two sentences that are not the same", None,
     ("“I cannot leave yet.”", "That is a constraint."),
     ("“Nothing can change.”", "That is a conclusion."),
     foot="They are not the same thing.",
     dark=True),
   trigger="“I cannot leave yet.”",
   purpose="The hook and the whole argument in one frame.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds per side, 3 on the foot.",
   sound="Strong candidate: one soft tick as the foot line lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 79% of the "
       "text is shared with the prior card, which read: These are not "
       "the same thing. “I CANNOT LEAVE YET.” That is a constraint. "
       "“NOTHING CAN CHANGE.” That is a con…. The editorial note "
       "written when this card was built, kept as written: The prior "
       "V12 package carried the same constraint-versus-conclusion "
       "distinction and the corrected master preserves it."),

 F(key="v12_02_protection_first",
   draw=lambda c: X.statement(
     c, "First", "Protection before career strategy.",
     "If health, safety, harassment, discrimination, or another urgent issue "
     "is involved, appropriate support comes before a career exercise.",
     dark=True, size=86, support_size=40),
   trigger="If health, safety, harassment, discrimination, or another urgent "
           "issue is involved, appropriate support comes before a career "
           "exercise.",
   purpose="The safety boundary, placed before any advice.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline.",
   hold="3 seconds alone, 4 with the support. Do not rush it.",
   sound="Not a candidate. Silence is the correct treatment.",
   status="NEW",
   why="The corrected master places this boundary early and explicitly."),

 F(key="v12_03_three_moves",
   draw=lambda c: X.trio(
     c, "What is feasible from where you actually are", None,
     [("PROTECT", "What must hold for now."),
      ("BOUND", "What you can influence safely."),
      ("PREPARE", "One possible next step.")],
     foot="You do not need a second full-time job called escaping the first "
          "one."),
   trigger="You need to protect what must hold, put boundaries where you "
           "can, and prepare one possible next step.",
   purpose="The framework.",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="The prior package separated protection, boundaries, development and "
       "preparation. The corrected master uses three, so the copy is "
       "replaced."),

 F(key="v12_04_name_the_constraint",
   draw=lambda c: X.statement(
     c, "Protect", "For now, any change needs to protect...",
     "Finish that sentence with the constraint you actually have.",
     size=80, support_size=46),
   trigger="Write one sentence:",
   purpose="Turn a vague constraint into a planning input.",
   reveal="The sentence stem, then the instruction.",
   emphasis="The stem.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v12_05_make_the_tradeoff_visible",
   draw=lambda c: X.struck(
     c, "Bound", None,
     "This job is impossible.",
     "These two commitments require the same time, and I need a priority "
     "decision."),
   trigger="“This job is impossible” may capture the feeling.",
   purpose="Show the difference between a feeling and something actionable.",
   reveal="The feeling. Hold. Struck. Then the specific version.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="COPY UPDATE",
   why="The prior package covered boundary language. The corrected master's "
       "example replaces the copy."),

 F(key="v12_06_question_before_activity",
   draw=lambda c: X.duo(
     c, "Prepare", None,
     ("A question",
      "“What would I need to prove to be considered for that role?”"),
     ("An activity without a test", "“I should be on LinkedIn more.”"),
     foot="Choose a question before you choose an activity."),
   trigger="Choose a question before you choose an activity.",
   purpose="The most useful correction in the video.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v12_07_exchange_not_add",
   draw=lambda c: X.statement(
     c, "If there is room inside the current job",
     "Exchange, not automatically add.",
     "Ask what comes off the plate. And if there is no room, do not "
     "manufacture a stretch assignment on top of an already unsustainable "
     "workload just to feel proactive.", dark=True, size=88,
     support_size=40),
   trigger="Exchange, not automatically add.",
   purpose="The line that respects the viewer's actual capacity.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline.",
   hold="2 seconds alone, 4 with the support.",
   sound="Candidate: one tick as the headline lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v12_08_four_lines",
   draw=lambda c: X.three_lines(
     c, "The plan: four lines", None,
     ["What must hold for now?",
      "What part of the current situation can I influence safely?",
      "What one question would make the next option clearer?",
      "When will I review this again?"],
     foot="If your capacity is extremely limited, choose only the first line "
          "and the review point.", size=48),
   trigger="Put four lines on a page:",
   purpose="The artifact, with the permission to do less attached.",
   reveal="One line at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the fourth line lands.",
   status="COPY UPDATE",
   why="The prior package ended on a next-step plan. The corrected master "
       "specifies these four lines and adds the reduced version."),

 F(key="v12_09_cta",
   draw=lambda c: X.cta(
     c, "Write the four lines privately",
     "Keep the action small enough that it can actually happen.",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="Write the four lines privately.",
   purpose="The resource route named by the corrected master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 41% of the "
       "text is shared with the closest prior card, which read: FREE "
       "CAREER DECISION EVIDENCE CHECK Read the evidence behind "
       "staying, moving, or leaving. It does not replace…. The "
       "editorial note written when this card was built, kept as "
       "written: The prior package routed V12 to the Decision Check "
       "and the corrected master keeps that route."),

 F(key="v12_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "A 30-Day Plan to Test Your Next Career Move", "Video 13"),
   trigger="Watch “A 30-Day Plan to Test Your Next Career Move” next.",
   purpose="The final visual, cued by the spoken handoff.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Destination and title unchanged from the prior package."),
]

# ------------------------------------------------------------------- V13
SETS[13] = [
 F(key="v13_01_career_activity",
   draw=lambda c: X.statement(
     c, "Stop collecting career activity",
     "It can make you feel productive without answering the decision.",
     "You have saved the jobs. Rewritten the headline. Maybe started a "
     "course. And you still do not know whether you want the work.",
     dark=True, size=72, support_size=42),
   trigger="It can make you feel productive without answering the decision.",
   purpose="The hook, aimed at the actual failure mode.",
   reveal="Headline. Hold. Then the support line.",
   emphasis="The headline.",
   hold="3 seconds, then 3 with the support.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="The prior package opened differently. The corrected master leads "
       "with the anti-activity hook."),

 F(key="v13_02_define_investigate_try_decide",
   draw=lambda c: X.four_bucket(
     c, "The plan", None,
     [("DEFINE", "Days 1 to 7. The work behind the title."),
      ("INVESTIGATE", "Days 8 to 14. People who know the work."),
      ("TRY", "Days 15 to 21. One bounded piece."),
      ("DECIDE", "Days 22 to 30. Continue, modify, or stop.")]),
   trigger="Define.",
   purpose="The whole plan in one frame, delivered early.",
   reveal="One bucket at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 5 on the complete grid. Viewers will pause here.",
   sound="Candidate: one tick on the fourth bucket.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 40% of the "
       "text is shared with the closest prior card, which read: THE "
       "PLAN 01 DEFINE 02 INVESTIGATE 03 TRY 04 DECIDE And “not this "
       "option” is allowed to be a good result.. The editorial note "
       "written when this card was built, kept as written: The prior "
       "package carried the same four-phase plan and the corrected "
       "master preserves it. Copy updated with the day ranges."),

 F(key="v13_03_not_this_option_is_allowed",
   draw=lambda c: X.statement(
     c, "The test only works if", "“Not this option” is allowed to be a good "
     "result.",
     "A useful test has permission to produce an inconvenient answer.",
     dark=True, size=78, support_size=44),
   trigger="And the test only works if “not this option” is allowed to be a "
           "good result.",
   purpose="The condition that makes the whole plan honest.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="NEW",
   why="The corrected master states this condition in the hook."),

 F(key="v13_04_destination_specific_enough",
   draw=lambda c: X.struck(
     c, "Choose a destination specific enough to test", None,
     "Something strategic.",
     "An internal operations-improvement role that uses my cross-team "
     "problem solving and keeps predictable hours."),
   trigger="“Something strategic” is too vague.",
   purpose="Show the standard for a testable destination.",
   reveal="The vague version. Hold. Struck. Then the testable one.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 4 after.",
   sound="Candidate: one tick as the strike lands.",
   status="NEW",
   why="New to the corrected master."),

 F(key="v13_05_ask_about_the_work",
   draw=lambda c: X.three_lines(
     c, "Investigate: ask about the work", None,
     ["“What is a difficult ordinary week in this role?”",
      "“Where do people with an adjacent background tend to need support?”",
      "“Which decisions distinguish someone who is ready?”"],
     foot="Do not ask for blanket reassurance about your potential.",
     size=44),
   trigger="Do not ask for blanket reassurance about your potential.",
   purpose="Give the viewer the actual questions.",
   reveal="One question at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 3 on the foot.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="The prior package covered the conversations phase. The corrected "
       "master specifies these three questions."),

 F(key="v13_06_work_sample_boundary",
   draw=lambda c: X.duo(
     c, "Try one bounded piece", None,
     ("Do", "Use public, synthetic, or otherwise permitted material. Set a "
            "time limit before you begin."),
     ("Do not", "Recreate a confidential employer process, or turn the "
                "exercise into unpaid operational work for a prospective "
                "employer."),
     foot="Label it as a work sample, not professional experience.",
     dark=True),
   trigger="Do not recreate a confidential employer process.",
   purpose="The compliance boundary on the sampling week.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="The corrected master states this boundary explicitly."),

 F(key="v13_07_three_decisions",
   draw=lambda c: X.trio(
     c, "Days 22 to 30: decide from the evidence", None,
     [("CONTINUE", "Not resign tomorrow. A targeted next action."),
      ("MODIFY", "An adjacent role, a supervised entry point, a longer "
                 "preparation period."),
      ("STOP", "The investigation gave you a reason not to keep investing "
               "here right now.")],
     foot="If the month ends without enough evidence, call the result "
          "inconclusive."),
   trigger="Then choose one of three decisions:",
   purpose="The decision point, with the inconclusive option preserved.",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 20% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: The prior package ended on continue, "
       "modify or stop and the corrected master preserves it, adding "
       "the inconclusive result."),

 F(key="v13_08_effort_is_not_evidence",
   draw=lambda c: X.statement(
     c, "The evidence standard", "Do not confuse effort with evidence.",
     "Reading descriptions, having conversations, and making a sample are "
     "activities. What those activities teach you is the evidence.",
     dark=True, size=90, support_size=40),
   trigger="Do not confuse effort with evidence.",
   purpose="The sharpest line in the video.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="NEW",
   why="New to the corrected master and editorially load-bearing."),

 F(key="v13_09_cta",
   draw=lambda c: X.cta(
     c, "One destination", "Write the hypothesis before you add another "
     "course.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="Choose one destination and write the hypothesis before you add "
           "another course or application to the list.",
   purpose="The resource route named by the corrected master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="The prior package routed V13 to the Field Kit and the corrected "
       "master keeps that route with a new action line."),

 F(key="v13_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Change Industries Without Starting Over", "Video 9"),
   trigger="For a closer look at separating useful experience from "
           "unfamiliar context and actual requirements, watch “How to Change "
           "Industries Without Starting Over” next.",
   purpose="The final visual, cued by the spoken handoff.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: The "
       "corrected master routes V13 back to V9 rather than forward. "
       "The destination changed, so the card is rebuilt."),
]

# ------------------------------------------------------------------- V14
# The corrected V14 master is BYTE-IDENTICAL to the one the September 10
# package was built against, so that frame set is carried across unchanged
# and every frame renders identically. This is the only genuine
# byte-identical reuse in the batch and it is proved at build time.
import sys as _sys
_sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                    "VIDEOS_14-21_FINAL_PRODUCTION/build")
from frames1421 import SETS as _SEP10

SETS[14] = []
for _f in _SEP10[14]:
    _g = dict(_f)
    _g["status"] = "REUSE"
    _g["why"] = ("The corrected V14 master is byte-identical to the master "
                 "this frame was built against, SHA-256 4a36cc83. The "
                 "specification and the render are carried across unchanged, "
                 "and the build proves the PNG is byte-identical.")
    if _g["key"].endswith("_watch_next"):
        # V14's master writes V15's title with a curly apostrophe. V15's own
        # Title row uses a straight one. The production-facing card carries
        # V15's canonical title exactly; the locked V14 source master is not
        # touched, because a punctuation glyph is not a reason to edit
        # approved copy.
        _g["draw"] = (lambda c: X.watch_next(
            c, "The Career Gaps You Don't See Until the Work Gets Harder",
            "Video 15"))
        _g["status"] = "COPY UPDATE"
        _g["why"] = ("The card now carries V15's canonical approved title "
                     "exactly. The September 10 card took the title from "
                     "V14's Watch Next row, which spells it with a curly "
                     "apostrophe where V15's own Title row uses a straight "
                     "one. Normalizing the production-facing card is the "
                     "whole change. The locked V14 master is unaltered and "
                     "its SHA-256 is unchanged.")
    SETS[14].append(_g)

# ------------------------------------------------------------------- V15
SETS[15] = [
 F(key="v15_01_the_question_changes",
   draw=lambda c: X.struck(
     c, "The question changes", None,
     "What happened here?", "What do you recommend we do?"),
   trigger="Then someone turns to you and asks, \"What do you recommend we "
           "do?\"",
   purpose="The moment the whole video sits on.",
   reveal="First question. Hold. Struck. Second question beneath it.",
   emphasis="The second question.",
   hold="2 seconds on the first, at least 3 on the second.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="REUSE",
   why="The concept and the trigger both survive into the restored master "
       "unchanged."),

 F(key="v15_02_three_gaps",
   draw=lambda c: X.trio(
     c, "Three gaps, three responses", None,
     [("LEARN", "There is something you genuinely do not know yet."),
      ("PRACTICE", "You know how the decision should be made, but you have "
                   "never been allowed to own it."),
      ("PROVE", "You already know how, and nobody can see enough proof.")],
     foot="Different problems. Different next moves."),
   trigger="Learn. Practice. Prove. Those are different problems, and they "
           "need different next moves.",
   purpose="The framework, named as the early payoff.",
   reveal="One column at a time in spoken order.",
   emphasis="Equal weight.",
   hold="2 seconds each, 3 on the complete set.",
   sound="Candidate: one tick as the third column lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 97% of the "
       "text is shared with the prior card, which read: THREE GAPS, "
       "THREE RESPONSES LEARN Something you genuinely do not know "
       "yet. PRACTICE You know how the decision…. The editorial note "
       "written when this card was built, kept as written: Concept "
       "and trigger both survive into the restored master."),

 F(key="v15_03_learn_test",
   draw=lambda c: X.statement(
     c, "Test one", "If someone sat with me and walked me through it once, "
     "could I then do it?",
     "If the honest answer is that you would need to be taught, that is a "
     "learning gap.", size=64, support_size=42),
   trigger="Ask yourself this. If someone sat with me and walked me through "
           "it once, could I then do it?",
   purpose="The first test as a sentence the viewer can apply.",
   reveal="Question, then the reading line.",
   emphasis="The question.",
   hold="At least 3 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="The restored master rewords the test, so the frame copy and the "
       "trigger are both updated to the corrected sentence."),

 F(key="v15_04_course_limit",
   draw=lambda c: X.duo(
     c, "What a course can and cannot do", None,
     ("A course can", "Teach you a method."),
     ("A course cannot",
      "Give you the experience of having made a decision that mattered, with "
      "incomplete information, and then living with what happened next."),
     foot="More training will not supply it, and you will be able to feel "
          "that it did not."),
   trigger="A course can teach you a method. A course cannot give you the "
           "experience of having made a decision that mattered, with "
           "incomplete information, and then living with what happened next.",
   purpose="Stop the viewer buying training for a problem training does not "
           "solve.",
   reveal="Left. Hold. Right. Then the foot line.",
   emphasis="The right side.",
   hold="At least 3 seconds on the right side.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master's wording replaces the copy "
       "and the trigger."),

 F(key="v15_05_practice_question",
   draw=lambda c: X.statement(
     c, "Test two", "Have I ever been the person whose name was on the "
     "decision?",
     "Not in the room. Not consulted. Not the person who prepared the "
     "analysis. The person who had to choose, and then answer for it.",
     dark=True, size=68, support_size=42),
   trigger="Ask a different question. Have I ever been the person whose name "
           "was on the decision?",
   purpose="The distinction between being near a decision and carrying one.",
   reveal="Question, then the qualifying line.",
   emphasis="The question.",
   hold="At least 3 seconds.",
   sound="Candidate: one tick as the question lands.",
   status="COPY UPDATE",
   why="The restored master rewords the question, so the trigger and the "
       "copy are updated."),

 F(key="v15_06_organizational_constraint",
   draw=lambda c: X.statement(
     c, "Be fair to yourself about this one",
     "That is an organizational constraint.",
     "Calling it a personal weakness will send you off to fix the wrong "
     "thing.", size=92, support_size=44),
   trigger="That is an organizational constraint, and calling it a personal "
           "weakness will send you off to fix the wrong thing.",
   purpose="The fairness beat the restored depth brings back.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline.",
   hold="2 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="NEW",
   why="The restored master brings back the organizational-constraint "
       "section, which the shortened version had lost."),

 F(key="v15_07_three_reads",
   draw=lambda c: X.trio(
     c, "ILLUSTRATION  ·  CONSTRUCTED EXAMPLE, NOT A REAL CASE", None,
     [("LEARN", "She has never been taught to structure a decision under "
                "uncertainty."),
      ("PRACTICE", "She knows how to weigh it and has never been allowed to "
                   "make the call."),
      ("PROVE", "She has been making these calls for two years and the room "
                "does not know.")],
     foot="Same moment. Same discomfort. Three completely different next "
          "twelve months."),
   trigger="Same moment. Same discomfort. Three completely different next "
           "twelve months.",
   purpose="Show the three gaps producing three readings of one moment.",
   reveal="One reading at a time. The label never leaves.",
   emphasis="The foot line.",
   hold="2 seconds per reading, 4 on the foot.",
   sound="Not a candidate. The label needs to be read.",
   status="COPY UPDATE",
   why="The restored master lengthens the example and changes the closing "
       "line, so the copy and trigger are updated."),

 F(key="v15_08_not_a_diagnostic",
   draw=lambda c: X.statement(
     c, "Limits, said plainly", "This is not a diagnostic.",
     "There is no score at the end of it, no level, no type. You may not "
     "have any of these gaps.", dark=True, size=96, support_size=42),
   trigger="This is not a diagnostic. There is no score at the end of it, no "
           "level, no type.",
   purpose="The boundary, at full size, in the video rather than the notes.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate. Silence is the correct treatment.",
   status="NEW",
   why="The restored master brings back a full limits section, which the "
       "shortened version compressed into a single clause."),

 F(key="v15_09_cta",
   draw=lambda c: X.cta_action(
     c, "One gap, one step", "Put your one gap in the comments.",
     "In a single sentence, using one of the three words.",
     "Learn. Practice. Prove."),
   trigger="Put your one gap in the comments, in a single sentence, using "
           "one of the three words. Learn. Practice. Prove.",
   purpose="The single spoken action. The restored master names no resource "
           "route in its own metadata, so none is shown.",
   reveal="Headline, support, then the three words.",
   emphasis="The three words in gold.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REBUILD",
   why="The September 10 card carried a resource URL. The restored master's "
       "metadata names no resource, so the card carries the action instead "
       "and no route is added."),

 F(key="v15_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "What to Do When Your Work Is Valued but You Are Overlooked",
     "Video 16"),
   trigger="Writing it down as one of those three is most of the value, "
           "because the moment you have to choose a word, you find out "
           "whether you actually know which problem you have.",
   purpose="The final visual, entering on the last spoken line.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: "
       "Destination unchanged. The trigger moves to the restored "
       "master's actual final line."),
]

# ------------------------------------------------------------------- V16
SETS[16] = [
 F(key="v16_01_called_then_skipped",
   draw=lambda c: X.duo(
     c, "Relied on, then skipped", None,
     ("They call you", "When it is urgent. When it breaks. When someone new "
                       "needs to understand how the work really works."),
     ("They skip you", "When the interesting assignment is handed out. When "
                       "the promotion list comes around. When the bigger "
                       "scope is discussed."),
     foot="That is not the same problem as being invisible.",
     dark=True),
   trigger="When something is urgent, they call you.",
   purpose="Land the specific frustration in the first fifteen seconds.",
   reveal="Left column builds line by line, then the right column, then the "
          "foot line.",
   emphasis="The imbalance between the columns.",
   hold="Build with the speech, then hold 3 seconds.",
   sound="Candidate: one soft tick as the right column appears.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master."),

 F(key="v16_02_four_separations",
   draw=lambda c: X.ladder(
     c, "Before you change how you behave", None,
     [("Is the work seen?", None),
      ("Is it attributed to you?", None),
      ("Trusted for delivery, or considered for larger scope?", None),
      ("Is the obstacle one you can actually remove?", None)],
     size=52),
   trigger="Before you change how you behave, separate four things: is the "
           "work seen, is it attributed to you, are you trusted for delivery "
           "or considered for larger scope, and is the obstacle one you can "
           "actually remove?",
   purpose="The structure of the video at full size.",
   reveal="One question at a time.",
   emphasis="Equal.",
   hold="2 seconds each, 3 on the complete set.",
   sound="Candidate: one tick on the fourth.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 94% of the "
       "text is shared with the prior card, which read: BEFORE YOU "
       "CHANGE HOW YOU BEHAVE 1 Is the work seen? 2 Is it attributed "
       "to you? 3 Trusted to deliver, or cons…. The editorial note "
       "written when this card was built, kept as written: Concept "
       "and trigger both survive into the restored master."),

 F(key="v16_03_where_work_disappears",
   draw=lambda c: X.trio(
     c, "Where good work disappears", None,
     [("INTO A SYSTEM", "That runs well, so nobody thinks about it."),
      ("INTO A TEAM RESULT", "Seven people delivered it. One made the two "
                             "calls that saved it."),
      ("INTO PREVENTION", "Nothing happened, and nothing happening is very "
                          "difficult to point at.")],
     foot="The visible artifact of good work is often the absence of a "
          "problem."),
   trigger="Work disappears in predictable places.",
   purpose="Explain the information problem without blaming anyone.",
   reveal="One column at a time. Prevention last and held longest.",
   emphasis="Prevention.",
   hold="2 seconds per column, 3 on the foot.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master's wording replaces the copy "
       "and the trigger."),

 F(key="v16_04_delivery_vs_scope",
   draw=lambda c: X.duo(
     c, "Two different judgments", None,
     ("Trusted to deliver", "If you are the reason a difficult area runs "
                            "smoothly, moving you is expensive."),
     ("Considered for scope", "A separate judgment. You can be at the top of "
                              "one list and absent from the other."),
     foot="Indispensability sounds like a compliment and functions like a "
          "ceiling."),
   trigger="So delivery and scope are being judged separately.",
   purpose="The most surprising point in the video.",
   reveal="Left, then right, then the foot line.",
   emphasis="The foot line.",
   hold="At least 3 seconds on the foot line.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v16_05_the_hinge",
   draw=lambda c: X.duo(
     c, "The hinge", None,
     ("Does not know", "An information problem. Inconvenient, and fixable."),
     ("Knows and does not act",
      "Not an information problem. More explanation is not the missing "
      "ingredient."),
     foot="You cannot tell which of those two you are in until the "
          "information problem is gone.",
     dark=True),
   trigger="A manager who does not know is a completely different situation "
           "from a manager who knows and does not act.",
   purpose="The pivot of the video and the most quotable frame.",
   reveal="Left. Hold. Right. Hold. Then the foot line.",
   emphasis="Two different problems, not degrees of one.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Strong candidate: one soft tick as the right side lands.",
   status="NEW",
   why="Reclassified from REUSE to NEW. Measured: nothing in the "
       "prior package resembles it; the closest card shares 19% of "
       "its text. The editorial note written when this card was "
       "built, kept as written: The hinge survives into the restored "
       "master and the trigger is the same sentence."),

 F(key="v16_06_what_this_does_not_fix",
   draw=lambda c: X.quad(
     c, "What a clearer record does not fix", None,
     [("BIAS", "It does not override it."),
      ("A ROLE THAT DOES NOT EXIST", "It does not create one."),
      ("A BUDGET SET TWO LEVELS UP", "It does not move it."),
      ("A MANAGER WHO HAS DECIDED", "It does not change them.")],
     foot="It removes the one obstacle that was genuinely yours to remove."),
   trigger="This does not override bias.",
   purpose="Keep the video honest. The record has a limit, said out loud.",
   reveal="All four, then the foot line.",
   emphasis="The foot line.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v16_07_three_pieces_four_lines",
   draw=lambda c: X.labeled_rows(
     c, "Three pieces of work. Four lines each.", None,
     [("Situation", "What was true before you touched it."),
      ("Decision", "What you decided, where someone else might have decided "
                   "differently."),
      ("Change", "What that changed, in terms the business cares about."),
      ("Otherwise", "What would have happened if nobody had done it.")]),
   trigger="Take three pieces of work from the last year.",
   purpose="The artifact. The fourth line is how prevention becomes "
           "visible.",
   reveal="One row at a time.",
   emphasis="The fourth row.",
   hold="2 seconds per row, 4 on the complete frame.",
   sound="Candidate: one tick as the fourth row lands.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master renames the fourth line, so "
       "the copy and trigger are updated."),

 F(key="v16_08_waiting_or_testing",
   draw=lambda c: X.duo(
     c, "Deciding what to do with a real answer", None,
     ("Waiting", "Legitimate when you can name the specific thing you are "
                 "waiting for. A reorganization with a date. A budget "
                 "cycle."),
     ("Testing elsewhere", "Not resigning. Finding out what your record "
                           "reads like to people who have no history with "
                           "you."),
     foot="Waiting stops being a choice at the point where you cannot name "
          "what you are waiting for.",
     dark=True),
   trigger="Waiting is a legitimate choice when you can point at the "
           "specific thing you are waiting for.",
   purpose="The decision the short version skipped. Restored depth.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The restored master brings back the keep-or-test decision section."),

 F(key="v16_09_cta",
   draw=lambda c: X.cta(
     c, "Start smaller", "Write one decision you made and what it changed.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="If you want the longer version of how to build that record "
           "properly, Keep the Proof is where I have put it, and the link is "
           "below.",
   purpose="The single resource route, after the teaching.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: Route "
       "unchanged. The trigger moves to the restored master's own "
       "resource sentence."),

 F(key="v16_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Show Your Impact at Work When You Built It From Scratch",
     "Video 8"),
   trigger="If it is difficult to write, that is worth knowing.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: "
       "Destination unchanged. Trigger moved to the restored final "
       "line."),
]

# ------------------------------------------------------------------- V17
SETS[17] = [
 F(key="v17_01_two_days_forty_minutes",
   draw=lambda c: X.duo(
     c, "The visible part got easier", None,
     ("Before", "The report used to take you two days."),
     ("Now", "A tool produces most of it in forty minutes."),
     foot="That question is getting harder to answer because the visible "
          "part of the work is no longer the scarce part.",
     dark=True),
   trigger="The report used to take you two days.",
   purpose="The hook, without celebration or alarm.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds per side, 3 on the foot.",
   sound="Candidate: one soft tick as the right side lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 61% of the "
       "text is shared with the prior card, which read: THE VISIBLE "
       "PART GOT EASIER Before The report used to take you two days. "
       "Now A tool produces most of it in fo…. The editorial note "
       "written when this card was built, kept as written: Concept "
       "and trigger both survive into the restored master."),

 F(key="v17_02_what_did_you_actually_do",
   draw=lambda c: X.statement(
     c, None, "So what did you actually do?", None, dark=True, size=110),
   trigger="Until someone asks, \"So what did you actually do?\"",
   purpose="The thumbnail line as a one-beat card.",
   reveal="Single state, entering hard.",
   emphasis="The whole frame.",
   hold="About 2 seconds. Short, and it lands.",
   sound="Strong candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master."),

 F(key="v17_03_output_is_not_contribution",
   draw=lambda c: X.duo(
     c, "Where the record lives", None,
     ("It used to be", "Attached to the artifact."),
     ("It now has to be", "Attached to the decisions around the artifact."),
     foot="That proxy has broken. Not permanently, and not everywhere, but "
          "in enough places that you have noticed."),
   trigger="The record used to be attached to the artifact. It now has to be "
           "attached to the decisions around the artifact.",
   purpose="The reframe, in one comparison.",
   reveal="Left, then right, then the foot line.",
   emphasis="The right side.",
   hold="3 seconds on the right side.",
   sound="Candidate: one tick as the right side lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 63% of the "
       "text is shared with the prior card, which read: WHERE THE "
       "RECORD LIVES It used to be Attached to the artifact. It now "
       "has to be Attached to the decisions aro…. The editorial note "
       "written when this card was built, kept as written: Concept "
       "and trigger both survive into the restored master."),

 F(key="v17_04_four_lines",
   draw=lambda c: X.ladder(
     c, "The four lines", None,
     [("What was I asked to get right?", "Not what was I asked to produce."),
      ("What did I check, and why did I check that?", None),
      ("What did I conclude that the output did not say?", None),
      ("What was I accountable for if it was wrong?", None)],
     size=46),
   trigger="So here are the four lines. They are deliberately short, because "
           "a record you will not maintain is not a record.",
   purpose="The framework and the artifact.",
   reveal="One line at a time.",
   emphasis="Line two, which the next frame enlarges.",
   hold="3 seconds per line, 4 on the complete frame.",
   sound="Candidate: one tick on the first line only.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master shortens each line, so the "
       "copy and trigger are updated."),

 F(key="v17_05_line_two",
   draw=lambda c: X.statement(
     c, "Line two", "What did I check, and why did I check that?",
     "That knowledge came from doing the work before it got faster, and it "
     "is not visible anywhere unless you write it down.", dark=True,
     size=76, support_size=40),
   trigger="If you only keep one of those, keep the second.",
   purpose="Enlarge the line that carries the contribution.",
   reveal="Question, then the support line.",
   emphasis="The question.",
   hold="At least 4 seconds.",
   sound="Strong candidate: one soft tick as the question lands.",
   status="COPY UPDATE",
   why="Concept preserved; trigger updated to the restored sentence."),

 F(key="v17_06_which_parts_leave_a_record",
   draw=lambda c: X.duo(
     c, "Which parts leave a record", None,
     ("Leaves something behind",
      "The output leaves a document. The timestamp leaves a record of when."),
     ("Leaves nothing",
      "Deciding what the question actually was. Choosing what to check. "
      "Noticing the thing that looked fine and was not."),
     foot="The parts that needed you are exactly the parts with no evidence "
          "attached."),
   trigger="Now mark the parts that leave nothing.",
   purpose="State the problem as plainly as the master states it.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="3 seconds per side, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The restored master brings back this section, which the shortened "
       "version had lost."),

 F(key="v17_07_speed_is_not_correctness",
   draw=lambda c: X.statement(
     c, "Speed is not the same as correctness",
     "The checking time is the part that quietly gets compressed, because "
     "checking is the part nobody can see.",
     "The visible output is better and faster, and the actual risk of it "
     "being wrong has gone up. The accountability has not moved anywhere.",
     size=62, support_size=40),
   trigger="But the report that used to take two days is now expected on the "
           "same afternoon, and the checking time is the part that quietly "
           "gets compressed, because checking is the part nobody can see.",
   purpose="Name the second-order effect without it becoming a complaint.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="The restored master brings this section back in full."),

 F(key="v17_08_worked_example",
   draw=lambda c: X.labeled_rows(
     c, "ILLUSTRATION  ·  CONSTRUCTED EXAMPLE, NOT A CAPTURED CASE", None,
     [("Get right", "That leadership does not leave with a wrong "
                    "impression."),
      ("Checked, why", "Whether the improvement was only timing. Whether "
                       "one customer distorted it."),
      ("Concluded", "Mostly timing. The position was flat."),
      ("Accountable", "That number going into a planning conversation.")]),
   trigger="Let me make that concrete. I have constructed this example so "
           "the structure is visible. It is an illustration, not a captured "
           "case.",
   purpose="Show the four lines filled in. The label is spoken and on screen "
           "for the whole hold.",
   reveal="One row at a time. The label never leaves.",
   emphasis="The second row.",
   hold="3 seconds per row, 4 on the complete frame.",
   sound="Not a candidate. The label needs to be read.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master's example replaces the copy "
       "and the trigger."),

 F(key="v17_09_cta",
   draw=lambda c: X.cta(
     c, "One piece of work", "Write what you checked and why.",
     "Keep the Proof", "temidayoafonja.com/keep-the-proof"),
   trigger="If you want the longer version of building a contribution record "
           "properly, that is Keep the Proof, linked below.",
   purpose="The single resource route named by the restored master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Route unchanged. Trigger moved to the restored resource sentence."),

 F(key="v17_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "AI Can Do the Task. What Are You Still Paid For?", "Video 11"),
   trigger="I would genuinely like to read those, because that sentence is "
           "the one that is disappearing, and it is the one worth keeping.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: "
       "Destination unchanged. Trigger moved to the restored final "
       "line."),
]

# ------------------------------------------------------------------- V18
SETS[18] = [
 F(key="v18_01_congratulated",
   draw=lambda c: X.statement(
     c, "How the offer arrives",
     "They congratulate you before they describe the job.",
     "Management is often offered as a reward. But it is not a reward. It is "
     "a different job.", dark=True, size=76, support_size=42),
   trigger="And before they explain what the job actually is, they "
           "congratulate you.",
   purpose="The opening observation.",
   reveal="Headline. Hold. Then the support line.",
   emphasis="The headline.",
   hold="3 seconds each.",
   sound="Candidate: one soft tick as the support line lands.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master."),

 F(key="v18_02_two_different_jobs",
   draw=lambda c: X.duo(
     c, "Not a higher and a lower version of one career", None,
     ("Senior individual work", "Different days. Different skills. Different "
                                "hard parts."),
     ("Management", "Different days. Different skills. Different hard "
                    "parts."),
     foot="TWO DIFFERENT JOBS. Side by side, not a ladder."),
   trigger="They are different jobs, with different days, different skills, "
           "and different hard parts.",
   purpose="The reframe. The horizontal arrangement is the argument.",
   reveal="Both columns together, then the foot line.",
   emphasis="Neither column is above the other.",
   hold="At least 4 seconds.",
   sound="Candidate: one tick as the foot line lands.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master."),

 F(key="v18_03_five_variables",
   draw=lambda c: X.ladder(
     c, "Five things that do not move together", None,
     [("Scope", None), ("Responsibility", None), ("Compensation", None),
      ("Authority", None), ("People management", None)],
     foot="They do not reliably move together.", size=58),
   trigger="Five things are bundled together in most people's heads, and "
           "they do not reliably move together.",
   purpose="Break the bundle.",
   reveal="One at a time, then show them shifting independently. Never "
          "animate them as one bar.",
   emphasis="The independence, not the list.",
   hold="2 seconds each, 4 on the complete set.",
   sound="Candidate: one tick as the fifth lands.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master defines each of the five, so "
       "the copy gains the definitions and the trigger is updated."),

 F(key="v18_04_responsibility_without_authority",
   draw=lambda c: X.statement(
     c, "The most common bad version",
     "More responsibility and no more authority.",
     "A genuinely difficult place to spend two years.", dark=True, size=88,
     support_size=46),
   trigger="Often they did not, and the most common bad version of this is "
           "more responsibility and no more authority, which is a genuinely "
           "difficult place to spend two years.",
   purpose="Name the trap early so the four questions have a target.",
   reveal="Headline alone. Hold. Then the support.",
   emphasis="The headline.",
   hold="2 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="NEW",
   why="The restored master states the trap explicitly in the framework "
       "section."),

 F(key="v18_05_what_the_job_consumes",
   draw=lambda c: X.quad(
     c, "What actually fills the day", None,
     [("ONE TO ONES", "And hiring."),
      ("PERFORMANCE CONVERSATIONS", "And planning."),
      ("REPORTING UPWARD", "And absorbing pressure."),
      ("DECIDING", "On things you will not personally do.")],
     foot="Ask two managers at your level what their last week actually "
          "contained, hour by hour."),
   trigger="Not what does it sound like. What fills the day.",
   purpose="Make the job concrete, and give the viewer the way to find out.",
   reveal="All four, then the foot line.",
   emphasis="The foot line, because it is what the viewer does.",
   hold="4 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v18_06_ask_for_names",
   draw=lambda c: X.statement(
     c, "Does the other path exist here?", "Ask for names.",
     "Ask what they are paid relative to managers at the same level, and ask "
     "what they are allowed to decide.", dark=True, size=96,
     support_size=40),
   trigger="Ask for names.",
   purpose="The single most practical instruction in the video.",
   reveal="The instruction alone. Hold. Then the support line.",
   emphasis="Ask for names, at maximum size.",
   hold="2 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the two words land.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 57% of the "
       "text is shared with the closest prior card, which read: DOES "
       "THE OTHER PATH REALLY EXIST HERE? Ask for names. Ask what "
       "those people are trusted to decide. Ask how th…. The "
       "editorial note written when this card was built, kept as "
       "written: Concept and trigger both survive into the restored "
       "master."),

 F(key="v18_07_the_other_job_demands",
   draw=lambda c: X.ladder(
     c, "What the senior individual job actually demands", None,
     [("Influence without authority", None),
      ("Choosing what not to work on, and defending it", None),
      ("Keeping real depth while the field moves", None),
      ("Developing people without a manager's levers", None)],
     foot="The option where you get left alone to do the work exists in very "
          "few organizations.", size=48),
   trigger="In most places it means influence without authority, which is "
           "harder than it sounds.",
   purpose="Keep the video two-sided by being honest about the other path.",
   reveal="One at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The restored master brings back this section, which the shortened "
       "version had lost."),

 F(key="v18_08_four_questions",
   draw=lambda c: X.ladder(
     c, "Four questions before you answer", None,
     [("What does the job consume?", None),
      ("Does the other path exist here?", None),
      ("What authority comes with it?", None),
      ("Can I come back?", None)],
     size=58),
   trigger="Ask the four questions. What does the job consume, does the "
           "other path exist here, what authority comes with it, and can I "
           "come back.",
   purpose="The frame viewers photograph.",
   reveal="All four together, since the master speaks them as one list.",
   emphasis="Equal weight.",
   hold="At least 5 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Concept preserved; trigger updated to the restored close."),

 F(key="v18_09_cta",
   draw=lambda c: X.cta(
     c, "Do not answer the offer yet", "Ask the four questions.",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="If you want a structured version of that decision record, the "
           "Career Decision Evidence Check is linked below.",
   purpose="The single resource route named by the restored master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Route unchanged. Trigger moved to the restored resource sentence."),

 F(key="v18_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "What to Do When Your Work Is Valued but You Are Overlooked",
     "Video 16"),
   trigger="In my experience it is usually the second one, and it is usually "
           "the one that changes the decision.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: "
       "Destination unchanged. Trigger moved to the restored final "
       "line."),
]

# ------------------------------------------------------------------- V19
SETS[19] = [
 F(key="v19_01_you_should_consult",
   draw=lambda c: X.statement(
     c, "The compliment", "“You should consult.”",
     "Twenty years of experience can still leave you with nothing a client "
     "knows how to buy.", dark=True, size=104, support_size=42),
   trigger="But twenty years of experience can still leave you with nothing "
           "a client knows how to buy.",
   purpose="The way in, and the sentence that stops it being flattery.",
   reveal="The quote alone. Hold. Then the support line.",
   emphasis="The quote, then the support.",
   hold="2 seconds alone, 4 with the support.",
   sound="Candidate: one soft tick as the support line lands.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master adds the twenty-years line, "
       "which becomes the trigger and the support copy."),

 F(key="v19_02_experience_is_not_an_offer",
   draw=lambda c: X.duo(
     c, "Two different questions", None,
     ("Your experience tells you", "What you know."),
     ("It does not tell you", "What somebody will buy."),
     foot="Deep expertise, no defined offer, no clear buyer, and no evidence "
          "the problem is purchased externally."),
   trigger="Your experience tells you what you know. It does not "
           "automatically tell you what somebody will buy.",
   purpose="The reversal and the thumbnail's argument.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="2 seconds per side, 4 on the foot.",
   sound="Strong candidate: one soft tick as the right side lands.",
   status="REBUILD",
   why="Reclassified from REUSE to REBUILD. Measured: only 58% of the "
       "text is shared with the closest prior card, which read: TWO "
       "DIFFERENT QUESTIONS Your experience tells you What you know. "
       "It does not tell you What somebody will buy.…. The editorial "
       "note written when this card was built, kept as written: "
       "Concept and trigger both survive into the restored master."),

 F(key="v19_03_four_things",
   draw=lambda c: X.four_bucket(
     c, "Four things bundled under one word", None,
     [("EXPERTISE", "What you know and can do."),
      ("A DEFINED SERVICE", "A specific thing somebody receives, with a "
                            "shape and an end."),
      ("REPEATABLE DELIVERY", "Doing it again without rebuilding it from "
                              "nothing."),
      ("A BUSINESS", "Finding the next one while delivering the current "
                     "one.")]),
   trigger="Start by separating four things that get bundled under the word "
           "consulting.",
   purpose="The framework. Most people have the first only.",
   reveal="One bucket at a time.",
   emphasis="The gap after the first bucket.",
   hold="2 seconds each, 4 on the complete grid.",
   sound="Candidate: one tick on the first bucket only.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master renames two of the four, so "
       "the copy and trigger are updated."),

 F(key="v19_04_who_signs_it",
   draw=lambda c: X.duo(
     c, "The buyer question", None,
     ("Not", "Who has the problem. Almost everybody has problems."),
     ("But", "Who currently pays somebody to deal with this one, and what do "
             "they pay for at the moment."),
     foot="If a budget exists, find out who signs it. That is frequently a "
          "different person.",
     dark=True),
   trigger="Not who has the problem. Almost everybody has problems.",
   purpose="The question that decides whether anything else applies.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="3 seconds per side, 3 on the foot.",
   sound="Candidate: one tick as the right side lands.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v19_05_expertise_vs_deliverable",
   draw=lambda c: X.struck(
     c, "What exactly would they receive", None,
     ["I can help with operational efficiency.", "I advise on risk."],
     "A four week review of the handover process across three sites, ending "
     "in a written set of recommendations and one session with the "
     "leadership team."),
   trigger="Those sentences are true and nobody can buy them.",
   purpose="The strongest single comparison in the video.",
   reveal="Both unbuyable sentences. Hold. Struck. Then the buyable one.",
   emphasis="The strike.",
   hold="2 seconds before the strike, 5 after. The replacement is long and "
        "needs reading time.",
   sound="Strong candidate: one soft tick as the strike lands.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master supplies both the unbuyable "
       "sentences and the specific deliverable, so the copy is replaced."),

 F(key="v19_06_what_is_not_included",
   draw=lambda c: X.statement(
     c, "Then write what is not included",
     "The absence of that line is where a fixed fee turns into five months "
     "of work.", None, size=76),
   trigger="The absence of that line is where a fixed fee turns into five "
           "months of work.",
   purpose="The line that protects a fixed fee.",
   reveal="Single state.",
   emphasis="The whole frame.",
   hold="At least 3 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v19_07_repeatable_delivery",
   draw=lambda c: X.ladder(
     c, "What survives the first engagement", None,
     [("A way of running the review", None),
      ("A set of questions you ask at the start", None),
      ("A shape the written output takes", None),
      ("The thing you now know to check in week two", None)],
     foot="You cannot sensibly price something you have never done. You can "
          "price the second one.", size=48),
   trigger="The first engagement is always partly invention. The question is "
           "what survives it.",
   purpose="Develop the third of the four, which the shortened version "
           "skipped.",
   reveal="One at a time, then the foot line.",
   emphasis="The foot line, which connects repeatability to pricing.",
   hold="2 seconds each, 4 on the foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="NEW",
   why="The restored master brings back the repeatable-delivery section."),

 F(key="v19_08_the_costs",
   draw=lambda c: X.trio(
     c, "The costs the compliment leaves out", None,
     [("UNPAID TIME", "Finding work does not stop once you have a client."),
      ("UNEVEN INCOME", "Difficult to plan around even when the total is "
                        "fine."),
      ("THE ORDINARY WORK", "You sell what people are already convinced they "
                            "need.")],
     foot="None of that is an argument against it. But you should be trading "
          "knowingly.",
     dark=True),
   trigger="The time you spend finding work is not paid.",
   purpose="The honesty beat, restored in full.",
   reveal="One column at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 4 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="The restored master brings back the costs section, which the "
       "shortened version compressed."),

 F(key="v19_09_cta",
   draw=lambda c: X.cta(
     c, "One sentence", "What would somebody receive from you, and by when?",
     "Career Decision Evidence Check",
     "temidayoafonja.com/career-decisions"),
   trigger="If you want a structured way to record that decision and what it "
           "rests on, the Career Decision Evidence Check is linked below.",
   purpose="The single resource route named by the restored master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: Route "
       "unchanged. Trigger moved to the restored resource sentence."),

 F(key="v19_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "A 30-Day Plan to Test Your Next Career Move", "Video 13"),
   trigger="It usually means the offer is still a description of you rather "
           "than a description of something a person can buy.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Reclassified from COPY UPDATE to REUSE. Measured: byte- "
       "identical to the prior rendered file. The editorial note "
       "written when this card was built, kept as written: "
       "Destination unchanged. Trigger moved to the restored final "
       "line."),
]

# ------------------------------------------------------------------- V20
SETS[20] = [
 F(key="v20_01_the_gap_is_not_the_whole_return",
   draw=lambda c: X.statement(
     c, "The return", "The explanation matters. But it is not the whole "
     "return.",
     "What from before is still current, what needs updating, and what do I "
     "genuinely need to rebuild?", dark=True, size=72, support_size=42),
   trigger="The explanation matters. But it is not the whole return.",
   purpose="The reframe, close to the opening.",
   mode="SHORT CALLOUT OVER CAMERA for the headline, then FULL SCREEN for "
        "the question.",
   reveal="Headline as a callout while Temidayo is on camera, then full "
          "screen for the three-part question.",
   emphasis="The three-part question.",
   hold="2 seconds on the callout, 4 on the full-screen question.",
   sound="Candidate: one soft tick as the full-screen question lands.",
   after="Return to camera. The opening is Temidayo's own account and stays "
         "camera-led.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master. The "
       "opening sentence itself is reworded, and it remains a real personal "
       "account that is never labelled an illustration."),

 F(key="v20_02_what_can_you_prove",
   draw=lambda c: X.duo(
     c, "The reframe", None,
     ("You prepared for", "An honest, brief answer about the break."),
     ("The conversation moves to", "What can you do now, and what can you "
                                   "prove?"),
     foot="That is where I would put most of the preparation."),
   trigger="But the conversation eventually moves to a harder question: what "
           "can you do now, and what can you prove?",
   purpose="Move the preparation to where it pays.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The right side.",
   hold="2 seconds left, 3 right, 3 foot.",
   sound="Candidate: one tick as the right side lands.",
   status="NEW",
   why="The restored master separates the reframe into its own section."),

 F(key="v20_03_six_categories",
   draw=lambda c: X.ladder(
     c, "Sort what you have into six categories", None,
     [("What stayed current", None),
      ("What decayed", None),
      ("What changed in the field", None),
      ("What changed in your circumstances", None),
      ("What is unproven rather than absent", None),
      ("What genuinely has to be rebuilt", None)],
     size=46),
   trigger="So before the applications, sort what you have into six "
           "categories.",
   purpose="The structure. The fifth is the one the next frame enlarges.",
   reveal="One at a time in spoken order.",
   emphasis="The fifth.",
   hold="2 seconds each, 5 on the complete set.",
   sound="Not a candidate. The next frame is the stronger moment.",
   status="REBUILD",
   why="The September 10 master used three buckets with six things inside. "
       "The restored master uses six categories directly, so the frame is "
       "rebuilt to the corrected structure."),

 F(key="v20_04_unproven_is_not_absent",
   draw=lambda c: X.statement(
     c, None, "Unproven is not the same as absent.",
     "There is a difference between not being able to do something and not "
     "being able to point at recent evidence that you can.", dark=True,
     size=96, support_size=42),
   trigger="There is a difference between not being able to do something and "
           "not being able to point at recent evidence that you can.",
   purpose="The distinction that saves the most viewers.",
   reveal="Headline alone. Hold. Then the support line.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands.",
   status="COPY UPDATE",
   why="Reclassified from REUSE to COPY UPDATE. Measured: 65% of the "
       "text is shared with the prior card, which read: Unproven is "
       "not the same as absent. You may still know how to do "
       "something and simply have no recent evidence…. The editorial "
       "note written when this card was built, kept as written: The "
       "distinction survives into the restored master. Trigger "
       "updated to the restored sentence."),

 F(key="v20_05_current_instance",
   draw=lambda c: X.duo(
     c, "If it is unproven", None,
     ("You do not need", "To relearn it."),
     ("You need", "A current instance. Volunteer work, a short contract, a "
                  "small project you can talk about in detail, a "
                  "qualification you refreshed."),
     foot="It does not have to be big. It has to be recent and it has to be "
          "yours."),
   trigger="If it is unproven, you do not need to relearn it. You need a "
           "current instance of it.",
   purpose="Turn the distinction into an action.",
   reveal="Left. Then right. Then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds left, 4 right, 3 foot.",
   sound="Candidate: one tick as the foot line lands.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v20_06_the_sort",
   draw=lambda c: X.labeled_rows(
     c, "ILLUSTRATION  ·  CONSTRUCTED EXAMPLE, NOT A REAL PERSON'S CASE",
     None,
     [("Current", "How to structure an analysis and read what a number is "
                  "saying."),
      ("Decayed", "The reporting system, now two versions on."),
      ("Unproven", "Complex reconciliations, nothing from the last four "
                   "years."),
      ("To rebuild", "One regulatory area, substantially rewritten.")]),
   trigger="Let me show you the sort. This is a constructed example, put "
           "together to make the categories visible rather than a real "
           "person's case.",
   purpose="Show the sort done once. The label stays for the whole hold.",
   reveal="One row at a time. The label never leaves.",
   emphasis="The unproven row.",
   hold="3 seconds per row, 4 on the complete frame.",
   sound="Not a candidate. The label needs to be read.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated. This constructed "
       "illustration is labelled; the opening personal account is not, and "
       "the two must never be confused."),

 F(key="v20_07_framing_and_bias",
   draw=lambda c: X.statement(
     c, "Honest about the market",
     "No amount of framing changes what a particular person decides about "
     "your application.",
     "What framing does is stop you arguing for the wrong thing.", size=64,
     support_size=44),
   trigger="Bias against career breaks is real.",
   purpose="Keep the video honest about what framing can and cannot do.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate. Let this land in silence.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v20_08_routes_back",
   draw=lambda c: X.quad(
     c, "Routes back, and what each one costs", None,
     [("FORMER EMPLOYER", "Fastest. You may re-enter at the level they "
                          "remember."),
      ("CONTRACT OR INTERIM", "Builds recent evidence quickly. Insecure "
                              "while you do it."),
      ("RETURN PROGRAM", "Designed for this. Limited in number and often in "
                         "location."),
      ("ADJACENT ROLE", "Sometimes easier to enter. A year learning a "
                        "context as well.")],
     foot="I am not ranking those. Which is right depends on your "
          "circumstances."),
   trigger="On the routes back, there are usually several and each one costs "
           "something different.",
   purpose="Give the viewer the real options with their real prices.",
   reveal="One at a time, then the foot line.",
   emphasis="The foot line, because the frame must not rank them.",
   hold="2 seconds each, 4 on the foot.",
   sound="Not a candidate.",
   status="NEW",
   why="The restored master brings back the routes section, which the "
       "shortened version had lost."),

 F(key="v20_09_cta",
   draw=lambda c: X.cta(
     c, "Today", "One thing you are rebuilding, with a date on it.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="If you want a structured way to build the evidence side of that, "
           "the Field Kit is linked below.",
   purpose="The single resource route named by the restored master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Route unchanged. Trigger moved to the restored resource sentence."),

 F(key="v20_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "I Was First in 3 New Roles in 5 Years. Here's What I Stopped "
        "Doing.", "Video 4"),
   trigger="It turns the part of this you can control into something that "
           "has already started.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REBUILD",
   why="Destination unchanged, card copy rebuilt. The September 10 card "
       "carried Video 4's former descriptive title, 'How to Explain a "
       "Career That Looks All Over the Place', which no longer names any "
       "video. The corrected September 11 V4 master is the authority, so "
       "the card now reads its exact title."),
]

# ------------------------------------------------------------------- V21
SETS[21] = [
 F(key="v21_01_the_room_is_different",
   draw=lambda c: X.statement(
     c, "After the change", "You can still do the work.",
     "What keeps catching you are the things nobody thought to explain.",
     dark=True, size=96, support_size=42),
   trigger="And the surprising part is that you can still do the work.",
   purpose="The hook. The surprise is context, not competence.",
   mode="SHORT CALLOUT OVER CAMERA for the headline, then FULL SCREEN for "
        "the support line.",
   reveal="Headline as a callout over camera, then full screen.",
   emphasis="The support line.",
   hold="2 seconds on the callout, 3 on the support.",
   sound="Candidate: one soft tick as the frame goes full screen.",
   status="REUSE",
   why="Concept and trigger both survive into the restored master."),

 F(key="v21_02_what_does_travel",
   draw=lambda c: X.ladder(
     c, "Name what came with you", None,
     [("How you break a problem into parts", None),
      ("How you tell whether work is any good", None),
      ("How you read what is happening in a room", None),
      ("How you work with somebody difficult", None),
      ("Knowing when something is not right before you can explain why",
       None)],
     foot="That is genuine and it is a lot. It is also not everything.",
     size=46),
   trigger="First, quickly, what does travel, because it is real and it is "
           "easy to lose sight of in the first difficult month.",
   purpose="Say what travels clearly and early.",
   reveal="One at a time, then the foot line.",
   emphasis="The foot line.",
   hold="2 seconds each, 3 on the foot.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v21_03_five_layers",
   draw=lambda c: X.ladder(
     c, "The five layers", None,
     [("What the work is actually about here", None),
      ("Regulation and credentials", None),
      ("Systems and tooling", None),
      ("Relationships and internal history", None),
      ("How decisions actually get made", None)],
     foot="Which layer will block useful contribution first in this specific "
          "role?", size=54),
   trigger="Layer one, and the one that blocks you soonest: what the work is "
           "actually about here.",
   purpose="The framework of the video.",
   reveal="One layer at a time as each is named, then the foot question.",
   emphasis="The foot question.",
   hold="2 seconds per layer, 5 on the complete frame.",
   sound="Candidate: one tick as the foot question lands.",
   status="REBUILD",
   why="The five layers survive into the restored master, but the card copy "
       "did not. The September 10 card labeled layer one 'Domain knowledge' "
       "and layer five 'How decisions get made here'. The corrected master "
       "names them 'what the work is actually about here' and 'how decisions "
       "actually get made', so the card now carries the master's own "
       "headings and the slide agrees with the speech."),

 F(key="v21_04_licensing_is_not_a_mindset",
   draw=lambda c: X.statement(
     c, None, "That is not a confidence issue and it is not a mindset "
     "problem.",
     "If a role requires a license, a registration or a specific "
     "qualification that you do not hold, no amount of adjacent experience "
     "substitutes for it.", dark=True, size=80, support_size=42),
   trigger="That is not a confidence issue and it is not a mindset problem.",
   purpose="The line that protects the whole channel from sounding like it "
           "claims everything transfers.",
   reveal="Headline alone. Hold. Then the support line.",
   emphasis="The headline, at maximum size.",
   hold="3 seconds alone, 4 with the support.",
   sound="Strong candidate: one soft tick as the headline lands. The single "
         "most important beat in the video.",
   status="COPY UPDATE",
   why="Concept preserved; the restored master rewords the line, so the "
       "trigger and the headline are updated to the corrected sentence."),

 F(key="v21_05_easiest_layer_trap",
   draw=lambda c: X.statement(
     c, "Systems and tooling",
     "The layer people worry about most is generally the smallest.",
     "It looks intimidating in week one and it is mostly gone by week six.",
     size=72, support_size=44),
   trigger="Layer three. Systems and tooling. This is usually the layer "
           "people worry about most and it is generally the smallest.",
   purpose="Stop the viewer spending preparation time on the wrong layer.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 3 seconds.",
   sound="Not a candidate.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v21_06_has_anyone_tried_this",
   draw=lambda c: X.statement(
     c, "Relationships and internal history",
     "Has anybody tried this before, and what happened?",
     "You cannot read your way into this. It comes from being present and "
     "asking why rather than proposing what.", dark=True, size=80,
     support_size=42),
   trigger="The single most useful question in a first few months is some "
           "version of has anybody tried this before, and what happened.",
   purpose="One practical instruction the viewer can use in week one.",
   reveal="The question, then the support line.",
   emphasis="The question.",
   hold="At least 3 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v21_07_first_ninety_days",
   draw=lambda c: X.statement(
     c, "A word about pace",
     "You are not going to arrive and contribute at the level you left at.",
     "Not because you got worse, but because two of these five layers only "
     "come from time in the place.", size=66, support_size=42),
   trigger="You are not going to arrive and contribute at the level you left "
           "at.",
   purpose="Set expectations without inventing a timeline.",
   reveal="Headline, then the support line.",
   emphasis="The headline.",
   hold="At least 4 seconds.",
   sound="Not a candidate.",
   status="NEW",
   why="The restored master brings back the pace section. The frame states "
       "no timeline, because the master explicitly refuses to give one."),

 F(key="v21_08_order_by_what_blocks_you",
   draw=lambda c: X.statement(
     c, "Application", "What stops me contributing usefully first?",
     "It quite often puts the regulatory item first, ahead of everything you "
     "would rather be studying.", dark=True, size=84, support_size=42),
   trigger="Then order the whole thing by one question, which is what stops "
           "me contributing usefully first.",
   purpose="The ordering rule, which is the useful part of the inventory.",
   reveal="Question, then the support line.",
   emphasis="The question.",
   hold="At least 4 seconds.",
   sound="Candidate: one tick as the question lands.",
   status="COPY UPDATE",
   why="Concept preserved; trigger and copy updated to the restored "
       "wording."),

 F(key="v21_09_cta",
   draw=lambda c: X.cta(
     c, "One destination", "Name the first item.",
     "Capability Formation Field Kit", "temidayoafonja.com/fieldkit"),
   trigger="If you want a structured version of the inventory, that is what "
           "the Field Kit is for, linked below.",
   purpose="The single resource route named by the restored master.",
   reveal="Label, headline, resource name, URL.",
   emphasis="The URL.",
   hold="At least 4 seconds.",
   sound="Candidate: one clean transition sound on entry.",
   status="COPY UPDATE",
   why="Route unchanged. Trigger moved to the restored resource sentence."),

 F(key="v21_10_watch_next",
   draw=lambda c: X.watch_next(
     c, "How to Change Industries Without Starting Over", "Video 9"),
   trigger="It is the difference between a plan that will work and a reading "
           "list that would have made you feel productive for a month.",
   purpose="The final visual.",
   reveal="Label, rule, title, number.",
   emphasis="The title.",
   hold="Hold to the end.",
   sound="Candidate: one restrained transition sound, then music fade.",
   after="NO RETURN TO CAMERA. Watch Next is final.",
   status="REUSE",
   why="Destination and title both match V9's corrected master. Trigger "
       "moved to the restored final line."),
]
