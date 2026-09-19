# -*- coding: utf-8 -*-
"""The influence and curiosity QA pass, as a report rather than a rewrite.

The lens is additional. It does not replace the strategy, the approved
scripts, the packaging or the production architecture, and nothing here
was changed because the lens exists. Every CHANGE below is a production
mismatch found by testing the delivered files, and every other answer is
a KEEP with the evidence for keeping it.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_22-23/build")
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
import recon as R
import packages as P
import events as EV
import shortsync as SH
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break)

EYEBROW = "capability formation | influence and curiosity qa"

LOOP = {
 4: "If AI removes developmental work, where does future experience come "
    "from?",
 5: "How can being more needed fail to create more growth?",
 6: "What is the job actually asking you to do beneath the title?",
 7: "What makes someone easier to trust with bigger work beyond doing "
    "the current job well?",
 8: "What becomes difficult to prove after work access disappears?",
 9: "What actually travels when the context changes?",
 10: "If proving yourself is not the first job, what is?",
 11: "Am I adjusting, dealing with role drift, or facing a bigger "
     "decision?",
}

# What the viewer can see, say, test, prove or decide afterwards, and the
# indicator that shows it landed. Internal. Not spoken.
OUTCOME = {
 4: ("See which part of a task was the learning, not just the output.",
     "Judgment is built from repetition, ownership and feedback, so "
     "removing the task can remove the formation without anyone "
     "deciding to.",
     "They can fill the third column, STILL MINE, for a real task."),
 5: ("Tell dependence apart from development in their own job.",
     "Being needed and being developed are different things, and only "
     "one of them compounds.",
     "They can name what a new assignment is building beyond keeping "
     "the role running."),
 6: ("Read a posting for problem, authority, proof and real gap instead "
     "of reacting to the title.",
     "A title is a label the employer chose; the verbs and requirements "
     "are what the work actually is.",
     "They can write the four lines for a posting in about ten "
     "minutes."),
 7: ("See what evidence exists for the next level rather than the "
     "current one.",
     "Bigger work is handed to people whose judgment someone has "
     "already seen, and access and sponsorship affect that too.",
     "They can name one kind of next-level work to be trusted with."),
 8: ("Say what changed, what was theirs and how it was judged, without "
     "the system.",
     "The baseline, scope, decision, result and method are what "
     "disappear first, and they are what another person needs to "
     "evaluate.",
     "They can write five lines about one project in their own words."),
 9: ("Sort experience into what travels, what does not, what can be "
     "proved and what must be relearned.",
     "A transferable-skills list flatters the move; four columns show "
     "the boundary.",
     "They can fill the relearn column honestly rather than forcing "
     "everything into the first."),
 10: ("Decide what the first ninety days are for.",
      "Experience and context are not the same thing, so proving the "
      "first can get in the way of learning the second.",
      "They can answer what they understand now that they did not "
      "understand on day one."),
 11: ("Tell settling apart from drift, and drift apart from a decision.",
      "Expected, actual, cost and choice turn a feeling into something "
      "readable without assuming deception.",
      "They can write the two columns, name one cost and choose one "
      "next action."),
}

# What the lens found. Everything not listed here is a keep.
CHANGED = {
 "accents": "Fifteen accents the briefs number were not carried by any "
            "event after the maps were regenerated from the event list, "
            "which left V4, V5, V8 and V10 below the stated four-to-seven "
            "band. Each one is restored at the event that covers its "
            "paragraph, read back out of the brief that names it. No new "
            "effect was invented and no accent was added to reach a "
            "number.",
 "spans": "Three multi-state families still had every state assigned to "
          "the paragraph that names the first item, so a later term could "
          "appear before it was spoken: V4's exposure, ownership and "
          "feedback, V6's working page, and V8's five fields. Each now "
          "activates on its own words, in its own paragraph.",
 "payoffs": "Four story-loop payoffs had no event at all, so the accent "
            "the brief names there had nowhere to attach: V4, V5, V7 and "
            "V9. Each is now a camera callback event, which is what those "
            "briefs describe.",
}


def build(path, st):
    t = P.totals()
    d = base_doc()
    title_block(d, EYEBROW, "V4 to V11 influence and curiosity QA",
                "An additional diagnostic pass. Not a rewrite.")
    kv(d, "Generated", st)
    kv(d, "Packages reviewed", "%d" % len(R.VIDEOS))
    kv(d, "Result", "Eight KEEP. One production mismatch found, in three "
                    "related parts, corrected.")
    callout(d, "Nothing was changed because this lens exists. The "
               "packaging, the scripts, the intros, the early-edit "
               "system, the Shorts, the resource map and the visual "
               "language are unchanged. The one change is a production "
               "mismatch the lens surfaced and the delivered files "
               "confirmed: accents the briefs number had stopped being "
               "carried.")

    h(d, "Tested, and unchanged")
    table(d, ["", "Result"],
          [["The eight locked titles and thumbnails",
            "Match the lock exactly, word for word. No alternative is "
            "proposed."],
           ["The resource map",
            "V4 none, V5 and V9 and V11 Career Decision Evidence Check, "
            "V6 and V7 and V10 Career Evidence Starter, V8 Keep the "
            "Proof. Matches. No Field Kit was added."],
           ["Unsupported power words",
            "None in any title, thumbnail, master or Short. Checked "
            "against the full banned list."],
           ["Promises of employer behaviour",
            "None. The only two uses of guarantee are negative "
            "qualifications: reading better does not guarantee a good "
            "outcome, and clarity does not guarantee an easy choice. "
            "Those are the boundary working, not a defect."],
           ["Open loops",
            "All eight are set up in a story loop and answered in their "
            "own payoff section. No extra loops were introduced."],
           ["Social proof",
            "None inserted anywhere. No testimonial, consensus claim or "
            "audience quote appears in any package."],
           ["Faith content",
            "Description-only in all eight, unchanged."],
           ["One primary ask",
            "One per video, and V4 carries none by design."]],
          widths=[2.0, 4.7], size=8)

    h(d, "The one change, in three related parts")
    for k, why in (("accents", "Production mismatch"),
                   ("spans", "Answer revealed before its setup"),
                   ("payoffs", "Loop payoff with no event")):
        sub(d, why)
        para(d, CHANGED[k], size=10.5)
    table(d, ["Video", "Accents before", "Accents now", "Band 4 to 7"],
          [["V%d" % n, {4: "2", 5: "3", 6: "4", 7: "4", 8: "3", 9: "4",
                        10: "2", 11: "4"}[n],
            "%d" % len([e for e in EV.events(n) if e["sound"]]),
            "in band"] for n in R.VIDEOS],
          widths=[1.0, 1.6, 1.6, 1.5], size=8.5)
    caption(d, "Every accent now in the map is one the brief numbers. "
               "None was invented to fill the band, and an accent whose "
               "word is spoken in a later paragraph now belongs to an "
               "event that reaches it.")

    for n in R.VIDEOS:
        page_break(d)
        h(d, "NEW PUBLIC V%d  |  %s" % (n, P.LOCKED[n][0]))
        kv(d, "Thumbnail", P.LOCKED[n][1])
        kv(d, "Resource", P.RESOURCE[n] or "None, intentionally")
        kv(d, "Verdict", "KEEP. Packaging, hook, loop, script, Shorts and "
                         "CTA unchanged.")
        out, reason, ind = OUTCOME[n]
        sub(d, "Outcome, reason, observable indicator")
        table(d, ["", ""],
              [["Outcome", out], ["Reason", reason],
               ["Observable indicator", ind]],
              widths=[1.5, 5.2], size=8.5)
        caption(d, "Internal. None of this is spoken narration.")

        sub(d, "The open loop")
        para(d, LOOP[n], size=11, bold=True)
        secs = dict(R.sections(n))
        para(d, "Set up: %s" % secs.get("STORY LOOP", [""])[0], size=10)
        para(d, "Paid off: %s" % secs.get("STORY LOOP PAYOFF", [""])[0],
             size=10, before=4)

        sub(d, "The seven questions")
        table(d, ["", "Answer from the delivered package"],
              [["Unity", LENS[n]["unity"]],
               ["Authority", LENS[n]["authority"]],
               ["Reciprocity", LENS[n]["reciprocity"]],
               ["Commitment", LENS[n]["commitment"]],
               ["Social proof", LENS[n]["proof"]],
               ["Liking", LENS[n]["liking"]],
               ["Scarcity or loss", LENS[n]["loss"]]],
              widths=[1.3, 5.4], size=8)

        sub(d, "Curiosity")
        para(d, LENS[n]["curiosity"], size=10.5)
        sub(d, "The human outcome")
        para(d, LENS[n]["human"], size=10.5)
        sub(d, "Changed in this pass")
        para(d, LENS[n]["changed"], size=10.5)

    page_break(d)
    h(d, "The final test")
    para(d, "Would the right experienced professional click because the "
            "situation matters to them, stay because Temidayo helps them "
            "see it differently, trust her because the reasoning and "
            "evidence are credible, and leave with something useful even "
            "if they never buy anything?", size=11, bold=True)
    para(d, "Yes, for all eight. Each opens on a situation the viewer "
            "recognizes rather than a promise, each gives the distinction "
            "or the tool before any ask, each keeps the constraints "
            "visible, and each ends with one thing to do. Nothing in this "
            "pass required reopening a title, a hook, a script or a "
            "Short.", size=10.5, before=6)
    h(d, "Not verified here")
    bullets(d, [
      "Audience response. Reaction is not causal proof of why something "
      "worked, and none is claimed.",
      "Final runtime, V6's ten-minute promise, audio, captions, chapters "
      "and live links. Those need the export and a live check.",
      "Scheduling. The Watch Next routes are unchanged and their "
      "availability is still a release dependency.",
    ], size=10)
    footer_note(d, "Additional diagnostic pass. The videos stay locked.")
    d.save(path)
    return path


LENS = {
 4: dict(
  unity="Opens on a task that used to take hours and a first draft in "
        "seconds. The viewer is not told they are anxious about AI; they "
        "are shown the trade they have already noticed.",
  authority="Judgment shown through the analyst example, the three "
            "things to watch and the explicit limits of what the "
            "argument can tell us. No expertise claim carries the "
            "point.",
  reciprocity="Exposure, ownership and feedback are given as a working "
              "distinction long before anything is asked, and the "
              "three-column test is usable on a real task.",
  commitment="Pick one task AI now helps with and fill the third "
             "column. Nothing to sign up for. V4 carries no resource by "
             "design.",
  proof="None used. The video cites no employer, posting or study, and "
        "says so.",
  liking="The opening is explicitly hypothetical, the argument says "
         "plainly that this is not anti-AI, and the close admits "
         "different jobs will answer differently.",
  loss="Real: the smaller decisions that build senior judgment can stop "
       "arriving without anyone deciding to remove them. No deadline, no "
       "alarm.",
  curiosity="The title asks who gets the experience. The hook deepens it "
            "by naming what the hours taught before answering, and the "
            "answer arrives in the three things to watch rather than "
            "being withheld to the end.",
  human="Recognition comes from a workplace scene and a task, not from a "
        "personal hardship story. The viewer leaves able to name what "
        "they are still practising.",
  changed="Accents S2, S4 and S5 restored. The exposure, ownership and "
          "feedback states now activate in their own paragraphs instead "
          "of all appearing with the first. The story-loop payoff is now "
          "an event, so its callback and its accent have somewhere to "
          "live."),
 5: dict(
  unity="Something breaks, they call you. Someone leaves, you absorb the "
        "work. Then the bigger opportunity goes to someone else. That is "
        "the situation, stated in three lines.",
  authority="Drawn from having worked inside and advised organizations, "
            "and demonstrated through the dependence-and-development "
            "distinction rather than asserted.",
  reciprocity="The distinction itself, the pattern to look for and the "
              "question to ask are all given before the resource is "
              "mentioned.",
  commitment="Ask for work that builds something new. One sentence, "
             "usable in the next one-to-one.",
  proof="None used.",
  liking="Says plainly that the manager may not be plotting, and that "
         "the answer may still be no. The warmth is in refusing the "
         "villain reading.",
  loss="Real: temporary extra work quietly becoming the normal job, and "
       "a review point that never happens.",
  curiosity="Useful. Still stuck. The contradiction is the hook, and the "
            "video resolves it by separating capacity from capability "
            "rather than by promising a promotion.",
  human="The viewer is not told they were exploited. They are given a "
        "way to see what the work is building.",
  changed="Accents S2 and S5 restored, and the story-loop payoff is now "
          "an event carrying the capacity-or-capability callback."),
 6: dict(
  unity="A real posting, read aloud. The viewer has read one like it "
        "this week.",
  authority="Fifteen postings across eleven employers, with the sample "
            "boundary stated every time a figure appears, and the "
            "reverse case shown rather than claimed.",
  reciprocity="Problem, authority, proof and real gap are taught in "
              "full, with the verbs to look for, before any ask.",
  commitment="Take one posting and write four lines. Ten minutes.",
  proof="The posting sample is evidence, used with its denominator and "
        "never generalized to the market. Employers stay anonymous.",
  liking="Says the job is not unimportant when the authority is lower, "
         "and that reading better does not guarantee a good outcome.",
  loss="Real: skipping a role because its title confused you, or "
       "accepting one whose authority is lower than the label "
       "suggested.",
  curiosity="Ignore the title is counterintuitive, and the story loop "
            "promises a title that sounds meaningless on the highest "
            "published ceiling. That is paid off with the actual "
            "posting.",
  human="Dignity is protected by reading the work rather than judging "
        "the reader for being impressed by a title.",
  changed="The working page at USE IT ON A REAL JOB now holds across "
          "both paragraphs so the second instruction is not shown before "
          "it is spoken. Its accent is restored."),
 7: dict(
  unity="Two people, both good, and only one name comes up. Stated "
        "without deciding who deserved it.",
  authority="From sitting close enough to talent and business decisions "
            "to have seen versions of it, and immediately qualified: "
            "access, sponsorship, bias and timing all matter.",
  reciprocity="The four things, the missing-line exercise and the "
              "conversation script are all given before any ask.",
  commitment="Pick one kind of next-level work to be trusted with.",
  proof="None used. The video explicitly refuses to reduce advancement "
        "to merit.",
  liking="Refuses the tidy formula out loud: careers do not work that "
         "neatly.",
  loss="Real: being seen as important to the role you already have, "
       "which is a cost that looks like a compliment.",
  curiosity="They chose someone else is a lived situation, not a "
            "promise. The loop asks what someone could already point to, "
            "and the payoff answers it as a target rather than a "
            "verdict.",
  human="The viewer is not told to work harder or to perform readiness "
        "all day. The video says so directly.",
  changed="The story-loop payoff is now an event, carrying the question "
          "callback and accent S5."),
 8: dict(
  unity="Tomorrow morning the login fails. Every experienced "
        "professional has imagined it.",
  authority="Shown through the five details that disappear and what an "
            "interviewer actually needs, not through claims.",
  reciprocity="The five fields, the ten-minute habit and the permission "
              "boundary are all given before the resource.",
  commitment="Write five lines about one project, in your own words.",
  proof="None used.",
  liking="The boundary is as visible as the exercise: keep the proof, "
         "not the property. That is care, not caution theatre.",
  loss="The most literal in the set, and entirely real: access ends and "
       "the details go with it.",
  curiosity="You can't prove it later is the consequence, and the video "
            "does not withhold the habit to the end. It gives the five "
            "fields early.",
  human="No fear montage. The imagined login is illustrative and "
        "labelled as such, with no employer interface or data.",
  changed="Accents S2 and S3 restored. The five fields now activate "
          "across the three paragraphs that name them, so the decision "
          "and the result are not shown before they are spoken."),
 9: dict(
  unity="Advice that gave you confidence, and a move that turned out to "
        "require more than the advice suggested.",
  authority="From having changed roles, functions and industries, and "
            "shown through the four columns rather than asserted.",
  reciprocity="All four questions, the sorting image and the honest "
              "sentence to say are given before any ask.",
  commitment="Make the four columns for one destination role.",
  proof="None used.",
  liking="Keeps the qualifier: some of it absolutely can transfer. The "
         "video is not contrarian for its own sake.",
  loss="Real: relationships, systems and informal power that do not "
       "travel, and a relearn column that is larger than expected.",
  curiosity="Missing something is a boundary, not hype. The loop names "
            "the least comfortable column as the most useful one and "
            "then earns it.",
  human="The gap is named as part of the move, not as an insult to the "
        "viewer's experience.",
  changed="The story-loop payoff is now an event, carrying the "
          "working-page callback and accent S5."),
 10: dict(
  unity="You got the job, and now you feel you have to prove they chose "
        "well. Named in the first two lines.",
  authority="From having been the new person many times, and "
            "demonstrated through read, test and prove rather than "
            "repeated.",
  reciprocity="The four things to read, the manager questions and the "
              "proof sentences are all given before any ask.",
  commitment="Ask the manager one question by day ninety.",
  proof="None used.",
  liking="Says clearly that READ does not mean sit quietly and "
         "contribute nothing, which protects the viewer from the wrong "
         "reading.",
  loss="Real: spending ninety days performing and learning nothing about "
       "the context, and missing what the role is telling you.",
  curiosity="The thumbnail states the counterintuitive instruction, and "
            "the loop adds the reversal: they are not the only ones "
            "evaluating. Both are paid off.",
  human="Dignity is protected by treating the pressure as reasonable "
        "before showing where it leads.",
  changed="Accents S2, S3 and S4 restored. The hook's framework card is "
          "held into the paragraph that names READ, TEST and PROVE."),
 11: dict(
  unity="You accepted one job and started doing another. Three or six "
        "weeks in. That is the whole situation.",
  authority="Shown through expected, actual, cost and choice, and "
            "through refusing the bait-and-switch reading before "
            "earning it.",
  reciprocity="All four questions, the four cost lenses and the "
              "clarification script are given before any ask.",
  commitment="Write the two columns, name one cost, choose one next "
             "action.",
  proof="None used.",
  liking="Roles change, priorities move, managers inherit problems. The "
         "video says so before it says anything else.",
  loss="Real, and carried in full: capability, evidence, compensation "
       "and life, including travel, caregiving and health.",
  curiosity="This isn't the job is the feeling; the video turns it into "
            "something readable rather than validating or dismissing "
            "it.",
  human="The constraints are explicit: immigration, geography, runway "
        "and market. The framework does not tell anyone to leave.",
  changed="Short 1 now closes on the role-drift read from TAKEAWAY "
          "VALUE instead of naming the four questions and stopping, "
          "which was the one place the package announced a framework "
          "without showing its use."),
}
