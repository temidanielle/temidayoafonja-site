# -*- coding: utf-8 -*-
"""Editorial development briefs for Videos 14 to 21, plus one reserved brief.

Everything here is a PROPOSAL for editorial review. Nothing in this file is
approved speech, a script, publishing copy, or a production instruction.

Field meanings, used identically in every brief:

  label        the planning working title. For unchanged slots it is the locked
               roadmap title. For V14 it is the descriptive title the roadmap's
               own evidence gate says to retain until research is completed.
  status       where the slot stands, in the roadmap's own status vocabulary.
  problem      the viewer's recognizable moment.
  job          the one job this video does that no other slot does.
  separate     the distinctions the video has to make to be useful.
  opening      proposed opening TERRITORY. Not a hook, not approved speech.
  shape        proposed structure of the teaching.
  research     what has to be gathered, verified or documented before scripting.
  honesty      what must be said out loud so the video does not overpromise.
  nofill       evidence gaps that must stay open rather than be filled by
               invention. These are the lines that must not be crossed.
  outcome      the artifact or sentence the viewer leaves with.
  boundary     separation from the neighboring slots, keyed to slot numbers.
  route        proposed resource route. Existing offers only.
  watchnext    proposed Watch Next. Routing is settled with the real script.
  thumb        thumbnail COPY position. Never artwork.
  donot        the explicit prohibitions carried from the brief instruction.
  open         questions editorial review still has to answer.
"""

# The four resource routes that already exist. No new product is proposed
# anywhere in these briefs, and no existing offer is described as doing
# something it does not do.
OFFERS = [
    ("Career Evidence Starter", "temidayoafonja.com/career-evidence-starter",
     "Free starter for building a first evidence record."),
    ("Field Kit", "temidayoafonja.com/fieldkit",
     "The working kit routed to most direction-and-method videos."),
    ("Career Decision Evidence Check", "temidayoafonja.com/career-decisions",
     "The decision-side route, used where the video ends on a choice."),
    ("Keep the Proof", "temidayoafonja.com/keep-the-proof",
     "The paid career evidence system, routed to proof-of-contribution videos."),
]

BRIEFS = [
# ---------------------------------------------------------------- V14
dict(
 num="V14",
 label="Which Parts of Your Experience Will Transfer to Another Industry?",
 status=("Direction approved. CONDITIONAL. The numerical, past-tense title "
         "is gated on research that has not been done."),
 problem=("You are reading a posting in another industry. It asks for direct "
          "industry experience. You cannot tell whether the years you already "
          "have count for something here or count for nothing."),
 job=("Teach a repeatable way to read and compare role documents, so the "
      "viewer stops guessing from a job title and starts comparing the "
      "decisions a role actually owns."),
 separate=[
   "The problem a role exists to solve, from the industry it sits in.",
   "Decisions the role owns, from tasks the role performs.",
   "Domain knowledge that must be learned, from capability already held.",
   "A hard requirement such as a license, from a preference written like one.",
   "What a posting claims about the work, from what the work turns out to be.",
 ],
 opening=("Proposed opening territory, not approved speech: put two postings "
          "from different industries side by side and show how much of the "
          "difference is vocabulary rather than work. The real hook is written "
          "after the research, not before it."),
 shape=[
   "Show the comparison being done once, on screen, at full size.",
   "Name every field being coded in each posting so the method is copyable.",
   "Show one clear overlap and one clear non-transfer from the same pair.",
   "State the limits of the method before the viewer applies it.",
   "Hand the viewer the same comparison to run on two or three postings.",
 ],
 research=[
   "Name the three industries and record why those three were chosen.",
   "Define the role family and the inclusion rule before collecting anything.",
   "Record the intended sample size, then record what was actually collected, "
   "including every posting excluded and the reason for excluding it.",
   "For each posting keep source, URL, collection date, employer type, "
   "seniority and whether it is on site, hybrid or remote.",
   "Code each posting for: the problem the role solves, the decisions it owns, "
   "assumed domain knowledge, named tools, credentials or licensing, stated "
   "years of experience, and stated scope and accountability.",
   "Keep the raw coded record so the number in any eventual title is "
   "reproducible by someone else.",
 ],
 honesty=[
   "Job descriptions are recruiting documents. They are partial, and sometimes "
   "inaccurate, descriptions of the work.",
   "Similar wording does not make two roles interchangeable.",
   "A posting says nothing about whether a particular applicant would be "
   "accepted, interviewed or hired.",
   "A sample of postings is not a sample of hiring decisions.",
   "The sample is dated. Say when it was collected and that it may not hold.",
 ],
 nofill=[
   "No number in the title, thumbnail, description or on camera until the "
   "count exists in the record.",
   "No past-tense claim about research that has not been completed.",
   "No invented employer, posting, quotation or salary figure.",
   "No implied finding that the comparison predicts hiring outcomes.",
 ],
 outcome=("A repeatable role-comparison method, and one comparison the viewer "
          "has actually filled in against postings they care about."),
 boundary=("V9 is the decision to change industries. V14 is the method for "
           "comparing opportunities before that decision. V21 is what has to be "
           "relearned after the change. V28 is the long-horizon question of "
           "building a career that survives industry change. Do not collapse "
           "these into one transfer lesson."),
 route=("Field Kit. This is the route the locked roadmap already carries for "
        "slot 14, and the topic did not change, so the route is unaffected by "
        "this addendum."),
 watchnext=("Proposal only: V14 into V21, because the comparison method leads "
            "naturally into what does not travel. Settle routing with the "
            "finished script."),
 thumb=("WHAT REALLY TRANSFERS? is carried from the locked roadmap and still "
        "fits the descriptive title. The thumbnail line was never the part "
        "under the research gate. No artwork is requested here."),
 donot=[
   "Do not use past tense or a numerical claim as active publishing copy "
   "before that research has been completed and documented.",
   "The actual sample size must determine any eventual numerical title.",
   "Do not present a target dressed as a result.",
 ],
 open=[
   "Which three industries, and is one of them Temidayo's own?",
   "One role family across three industries, or three adjacent families?",
   "Is the comparison filmed as a live worked example or as a prepared record?",
 ],
),
# ---------------------------------------------------------------- V15
dict(
 num="V15",
 label="The Career Gaps You Don’t See Until the Work Gets Harder",
 status=("PROPOSED new placement at slot 15. The topic is an approved "
         "editorial input. The placement, the outline and the title are "
         "proposals for review. No script exists."),
 problem=("You can explain what happened in the report. Then someone asks "
          "which decision you recommend, with incomplete evidence and "
          "consequences attached. Nothing in the work so far required you to "
          "answer that."),
 job=("Separate three things that feel identical from the inside and need "
      "completely different responses."),
 separate=[
   "A skill not yet developed. The response is learning and practice.",
   "A responsibility never held, because the opportunity or the authority was "
   "never available. The response is supervised practice or access to a "
   "different kind of work, and the constraint may be organizational rather "
   "than personal.",
   "Capability that is present but cannot be demonstrated. That is an evidence "
   "problem, not a development problem, and the fix is different again.",
 ],
 opening=("Proposed opening territory, not approved speech: the moment the "
          "question changes from what happened to what you would do about it. "
          "Keep it recognizable and specific rather than a general statement "
          "about experience."),
 shape=[
   "Show the moment, in one labeled illustration, at full size.",
   "Name the three causes and show that the same symptom has three sources.",
   "Give one test per cause that the viewer can apply to their own situation.",
   "Match each cause to its own next step, and say plainly that the steps are "
   "not interchangeable.",
   "Close on the single gap the viewer named, not on a list.",
 ],
 research=[
   "Choose one decision scenario specific enough to be recognized and general "
   "enough to travel. Write it as a labeled illustration.",
   "If a real example is used instead, it must be a documented one, with "
   "consent where another person is involved, and identifying detail removed.",
   "Check the wording against V25 and V30 so the three videos do not deliver "
   "the same diagnosis.",
 ],
 honesty=[
   "This is a practical reflection tool. It is not a validated diagnostic, an "
   "assessment instrument, or a measure of anything.",
   "Not every experienced professional carries this gap, and the ones who do "
   "do not all carry the same one.",
   "Some of these gaps cannot be closed by the person alone. Access and "
   "authority are granted by an organization, not chosen by the viewer.",
   "A course can teach a method. A course alone does not supply decision "
   "experience or the consequences that make it real.",
 ],
 nofill=[
   "Do not invent a failure of Temidayo's to open the video.",
   "Do not invent a colleague, a manager, an employer or a project outcome.",
   "Do not imply that all experienced professionals share the same weakness.",
   "Do not present the reflection exercise as a validated diagnostic.",
   "Do not attach a score, a level, a percentage or a type to the viewer.",
 ],
 outcome=("One specific gap named, with the matching next step: learning, "
          "supervised practice, access to a different kind of work, or stronger "
          "permitted evidence."),
 boundary=("V2 examines marketability. V7 tests whether increased workload is "
           "growth. V21 concerns destination-specific relearning. V25 diagnoses "
           "a stalled career. V26 remains the separate developmental-work and "
           "AI topic. V30 chooses assignments. V15's own job is the particular "
           "judgment the prior work may not have required, and telling apart "
           "three causes that look the same from inside."),
 route=("Proposal, not settled. Career Decision Evidence Check fits a video "
        "that ends on naming one gap and one next step. Field Kit is the route "
        "slot 15 already carries, but it was carried for the after-40 topic. "
        "Decide the route with the finished script."),
 watchnext=("Proposal only: V15 into V16, because an unseen gap and being "
            "overlooked are adjacent problems with different causes. Settle "
            "routing with the finished script."),
 thumb=("No approved thumbnail copy exists for this topic. UPDATE. DON’T "
        "ERASE. belongs to the after-40 topic and travels with it into the "
        "forward queue. Copy proposals for review, not artwork: THE GAP UNDER "
        "THE SKILL / NOT A SKILLS GAP / EXPERIENCE ISN'T THE SAME AS PRACTICE. "
        "Final title and thumbnail pairing is settled with the script."),
 donot=[
   "Do not describe the reflection exercise as a validated diagnostic.",
   "Do not imply that all experienced professionals share the same weakness.",
   "Do not suggest that a course alone supplies decision experience.",
 ],
 open=[
   "Three causes, or a fourth for work whose requirements changed underneath "
   "the person?",
   "Does the illustration come from Temidayo's field or a neutral one?",
   "Does this slot need its own thumbnail copy round before scripting?",
 ],
),
# ---------------------------------------------------------------- V16
dict(
 num="V16",
 label="What to Do When Your Work Is Valued but You Are Overlooked",
 status="Unchanged slot. Direction approved. Brief prepared for scripting.",
 problem=("Your work is relied on. People come to you when something has to be "
          "right. Your name is not in the room where assignments, budgets and "
          "promotions are decided."),
 job=("Separate what the viewer can change from what is being decided without "
      "them, and be honest about which is which."),
 separate=[
   "Visibility of the work, from attribution of the contribution.",
   "Being trusted for delivery, from being considered for scope.",
   "An obstacle the viewer can remove, from a constraint they cannot.",
   "A manager who does not know, from a manager who knows and does not act.",
 ],
 opening=("Proposed opening territory, not approved speech: the gap between "
          "being the person everyone asks and the person nobody names. Do not "
          "open on resentment."),
 shape=[
   "What decision-makers actually see, and when they see it.",
   "How contribution disappears into a team, a system or a process.",
   "One removable obstacle, worked through at full size.",
   "The constraints that remain after the removable ones are gone.",
   "How to judge whether to keep investing here or to test elsewhere.",
 ],
 research=[
   "Use a documented or clearly labeled example of contribution disappearing "
   "into a delivered system.",
   "Check the framing against V27 so the organizational video is not "
   "pre-empted.",
 ],
 honesty=[
   "Being clearer does not guarantee a different outcome.",
   "Bias, an unavailable role, a fixed budget and a manager who controls the "
   "narrative are real constraints, and none of them is fixed by better "
   "wording.",
   "The useful move is to remove the removable obstacle and then judge the "
   "constraint that is left, with better information than before.",
 ],
 nofill=[
   "Do not promise that a clearer explanation overrides bias, unavailable "
   "roles, manager control, or other constraints.",
   "Do not invent an employer, a manager, a promotion decision or an outcome.",
   "Do not imply the viewer's invisibility is entirely their own doing.",
   "Do not give advice that quietly requires authority the viewer may not "
   "have without saying so.",
 ],
 outcome=("A short contribution record a decision-maker can read, and a named "
          "assessment of what is still outside the viewer's control."),
 boundary=("V5 makes a whole career legible. V8 proves foundational work that "
           "now looks easy. V16 is recognition inside one organization. V22 is "
           "the promotion decision itself. V27 is the organization's failure to "
           "see the talent it already has. V16 stays with the individual's "
           "position, not the company's system."),
 route="Keep the Proof. Carried from the locked roadmap for slot 16.",
 watchnext=("Proposal only: V16 into V22, because being overlooked leads "
            "directly into the wait-or-move decision."),
 thumb=("VALUED - BUT OVERLOOKED is carried from the locked roadmap. If the "
        "hyphen is restyled at packaging, that is a copy decision to record, "
        "not a redesign."),
 donot=[
   "Do not promise that a clearer explanation overrides bias, unavailable "
   "roles, manager control, or other constraints.",
 ],
 open=[
   "Does the video address the case where the manager is the obstacle, or "
   "hold that for a separate brief?",
   "Is the contribution record the same artifact as V8's, or a shorter one?",
 ],
),
# ---------------------------------------------------------------- V17
dict(
 num="V17",
 label="How to Prove Your Value When AI Does More of the Task",
 status="Unchanged slot. Direction approved. Brief prepared for scripting.",
 problem=("The output you were valued for now takes less time and less skill "
          "to produce. The work you did around it has not changed, but the "
          "visible part of it has."),
 job=("Move the evidence from the output to the parts of the work that still "
      "need a person, and show what leaves a record."),
 separate=[
   "Producing the output, from framing the problem the output answers.",
   "Generating a draft, from verifying it against something real.",
   "Interpretation, from decision.",
   "Decision, from accountability for the decision.",
   "Speed, from correctness.",
 ],
 opening=("Proposed opening territory, not approved speech: the moment the "
          "artifact you were known for stops being the hard part of the job."),
 shape=[
   "Take one specific, supportable task through the stages above.",
   "Mark which stages leave a record and which leave none.",
   "Build the record for the stages that leave none.",
   "State the limit of the whole exercise before closing.",
 ],
 research=[
   "If a tool is shown at all, use a real, dated, captured example, name the "
   "tool accurately, and state the conditions of the capture.",
   "Verify any capability claim against the actual tool at scripting time, "
   "because tool behavior changes between scripting and publication.",
   "Otherwise use a labeled illustration and say on screen that it is one.",
   "Check the separation against V11 and V26 before writing.",
 ],
 honesty=[
   "Judgment does not guarantee that a job is safe. Roles are eliminated for "
   "reasons that have nothing to do with an individual's contribution.",
   "The question this video answers is what can be evidenced, not what is "
   "protected.",
   "Any tool observation is dated and specific to the version tested.",
 ],
 nofill=[
   "Do not fabricate a tool demonstration, a model response, a speed result, a "
   "screen recording or a product interface.",
   "Do not stage an AI failure to make a point.",
   "Do not claim that human judgment guarantees job security.",
   "Do not imply an endorsement, a benchmark or a comparison that was not run.",
 ],
 outcome=("A contribution record that still holds after the task itself "
          "becomes cheap to perform."),
 boundary=("V11 asks what the person is still paid for. V17 is the evidence of "
           "that contribution. V26 is what the job still teaches. The locked "
           "roadmap's separation rule for these three stands unchanged."),
 route="Keep the Proof. Carried from the locked roadmap for slot 17.",
 watchnext=("Proposal only: V17 into V11, or V17 into V26, depending on which "
            "is published first. Settle with the script."),
 thumb="OUTPUT ISN'T ENOUGH is carried from the locked roadmap.",
 donot=[
   "Do not fabricate a tool demonstration.",
   "Do not claim that human judgment guarantees job security.",
 ],
 open=[
   "Which task, and is it one Temidayo can demonstrate with permitted "
   "material?",
   "Does V17 publish before or after V11, given the shared territory?",
 ],
),
# ---------------------------------------------------------------- V18
dict(
 num="V18",
 label="Should You Stay an Individual Contributor or Become a Manager?",
 status=("Unchanged slot, topic kept. One copy variance between the locked "
         "roadmap and the refinement is recorded in the addendum and is not "
         "silently resolved here."),
 problem=("The next visible step is a manager title, and it is the only step "
          "anyone is offering you."),
 job=("Show that scope, responsibility, compensation, authority and people "
      "management are five different things that do not always move together."),
 separate=[
   "Management as a reward, from management as a different job.",
   "More authority, from more accountability without more authority.",
   "A senior individual path that exists, from one that is described but never "
   "filled.",
   "A decision that can be reversed, from one that cannot.",
 ],
 opening=("Proposed opening territory, not approved speech: the offer that "
          "arrives as a compliment and turns out to be a change of occupation."),
 shape=[
   "What the management job actually consists of, hour by hour.",
   "What a senior individual path requires, and how to check whether it "
   "exists here.",
   "How to test the work before committing, where a test is possible.",
   "What the return path looks like, and where there is not one.",
 ],
 research=[
   "Check whether a senior individual track exists in the viewer's own "
   "organization is framed as a question the viewer investigates, not an "
   "assumption the video makes.",
   "Check the boundary against V22 and V24 before writing.",
 ],
 honesty=[
   "Some organizations genuinely cap individual contributors. Saying otherwise "
   "would be false comfort.",
   "Management is not a demotion of ambition, and refusing it is not a failure "
   "of nerve.",
   "Compensation and authority are set by the organization, not by the "
   "viewer's preference.",
 ],
 nofill=[
   "Do not imply that management is the only form of advancement.",
   "Do not imply that refusing management is always the braver choice.",
   "Do not invent an employer's career framework or a compensation figure.",
 ],
 outcome=("A decision record: what the viewer wants more of, what this "
          "specific offer supplies, and the evidence still missing."),
 boundary=("V22 is the promotion timing decision. V24 is growth once already "
           "senior. V18 is the shape of the next role, not the timing of it."),
 route="Career Decision Evidence Check. Carried for slot 18.",
 watchnext=("Proposal only: V18 into V24. Settle with the script."),
 thumb=("YOU DON'T HAVE TO MANAGE is carried from the locked roadmap. Note "
        "that this line reads as advice in one direction; check it against the "
        "finished script's balance before packaging."),
 donot=[
   "Do not imply that management is the only form of advancement.",
 ],
 open=[
   "Does the video take a position, or stay genuinely two-sided?",
   "Is the thumbnail line still right if the script stays two-sided?",
 ],
),
# ---------------------------------------------------------------- V19
dict(
 num="V19",
 label="Is Consulting a Real Next Step for Your Career?",
 status="Unchanged slot. Direction approved. Brief prepared for scripting.",
 problem=("People keep telling you to consult because you have a lot of "
          "experience. Nobody has told you what would actually be bought."),
 job=("Separate having expertise from having a service someone pays for, and "
      "test that separation before anyone quits anything."),
 separate=[
   "Expertise, from a defined service.",
   "A service, from repeatable delivery.",
   "Delivery, from a business with pipeline, contracts and cash flow.",
   "Interest from a former colleague, from a signed engagement.",
 ],
 opening=("Proposed opening territory, not approved speech: the advice to "
          "consult, and the question it never answers, which is what the buyer "
          "is buying."),
 shape=[
   "Name the buyer and the problem they already pay to solve.",
   "Turn the experience into one defined service with a scope.",
   "Look honestly at where the first engagement realistically comes from.",
   "Name the constraints: contracts, notice periods, conflicts of interest, "
   "and anything the viewer's own agreement restricts.",
   "Give the test that happens before the decision, not after it.",
 ],
 research=[
   "Keep every constraint generic and route the viewer to appropriate "
   "professional advice for their own contract and jurisdiction.",
   "Check the boundary against V12 and V13 before writing.",
 ],
 honesty=[
   "Consulting is a different business, not a continuation of the same job "
   "with more freedom.",
   "Income is variable, and business development takes time that is not paid "
   "for directly.",
   "Some employment agreements restrict what can be done and for whom.",
 ],
 nofill=[
   "Do not promise revenue, clients, a timeline or an easy escape from "
   "employment.",
   "Do not turn this into generic business-setup advice about entity types, "
   "invoicing tools or tax.",
   "Do not give legal or tax advice.",
   "Do not invent Temidayo's consulting income, client list or case study.",
 ],
 outcome=("One defined service written as a short proposal, and the list of "
          "what must be true before it becomes a plan."),
 boundary=("V12 is what to do while quitting is not possible. V13 is a 30-day "
           "test of a possible move. V19 is one specific destination examined "
           "on its own terms, and it may borrow V13's testing discipline "
           "without repeating the plan."),
 route="Career Decision Evidence Check. Carried for slot 19.",
 watchnext="Proposal only: V19 into V13. Settle with the script.",
 thumb="EXPERIENCE ISN'T AN OFFER is carried from the locked roadmap.",
 donot=[
   "Do not turn this into generic business-setup advice.",
   "Do not promise revenue, clients, or an easy escape from employment.",
 ],
 open=[
   "Independent consulting, contracting and fractional work are different "
   "routes. Does one video cover all three?",
   "Is there a real, permitted example available, or is this a labeled "
   "illustration throughout?",
 ],
),
# ---------------------------------------------------------------- V20
dict(
 num="V20",
 label="How to Return After a Career Break Without Starting at Zero",
 status="Unchanged slot. Direction approved. Brief prepared for scripting.",
 problem=("The break is the first thing anyone asks about, and you have to "
          "decide what to say about it and what to rebuild before you say it."),
 job=("Separate what is still current from what has to be rebuilt, so the "
      "return is a plan rather than an apology."),
 separate=[
   "What stayed current, from what decayed.",
   "What changed in the field, from what changed in the person.",
   "An evidence problem, from a capability problem.",
   "A re-entry route's real tradeoff, from a verdict on the person's worth.",
 ],
 opening=("Proposed opening territory, not approved speech: the question about "
          "the gap, and the decision about how much of the answer is "
          "explanation and how much is evidence."),
 shape=[
   "A short, honest account of the break that does not over-explain.",
   "An inventory: current, decayed, changed, and unproven.",
   "Recency evidence that can be built starting now, with a date on it.",
   "Re-entry routes and their real tradeoffs, named without ranking them for "
   "everyone.",
 ],
 research=[
   "If a personal story is used, it must be Temidayo's actual experience. "
   "Otherwise use a labeled illustration and say so.",
   "Keep any description of returnship or re-entry programs generic unless a "
   "specific one has been checked and dated.",
 ],
 honesty=[
   "Employer bias against breaks is real, and how the break is framed does not "
   "remove it.",
   "Some routes back require accepting a different scope, title or "
   "compensation at first. That is a tradeoff to decide, not a verdict.",
   "Some fields change enough that returning genuinely requires retraining.",
 ],
 nofill=[
   "Do not invent Temidayo's personal return story.",
   "Do not imply that framing removes employer bias.",
   "Do not invent an employer, a returnship program or a hiring outcome.",
 ],
 outcome=("A two-part return record: what is current with the evidence for it, "
          "and what is being rebuilt now with a date attached."),
 boundary=("V4 explains a career that looks scattered. V9 is the industry "
           "change decision. V20 is specifically the interruption and the "
           "return, and it should not become a general story-telling video."),
 route="Field Kit. Carried for slot 20.",
 watchnext="Proposal only: V20 into V4. Settle with the script.",
 thumb="THE GAP ISN'T THE WHOLE STORY is carried from the locked roadmap.",
 donot=[
   "Do not invent Temidayo's personal return story.",
   "Do not imply that framing removes employer bias.",
 ],
 open=[
   "Does the video address caregiving, health and redundancy breaks together "
   "or name them separately?",
   "Is there a real consenting example available, or a labeled illustration?",
 ],
),
# ---------------------------------------------------------------- V21
dict(
 num="V21",
 label="What You Must Relearn When You Change Industries",
 status="Unchanged slot. Direction approved. Brief prepared for scripting.",
 problem=("You made the change. The parts you were confident about are "
          "working. Something else keeps catching you out, and it is not the "
          "part you prepared for."),
 job=("Give the arriving professional an ordered relearning inventory for one "
      "specific destination."),
 separate=[
   "Capability that travels, from domain knowledge that does not.",
   "Knowledge that can be read, from knowledge that only comes from doing the "
   "work here.",
   "A regulation or credential, from a habit or a preference.",
   "Systems and tooling, from relationships and internal history.",
   "How decisions are made here, from how they were made where you came from.",
 ],
 opening=("Proposed opening territory, not approved speech: the confident "
          "first weeks, and the specific thing that turns out to be the "
          "blocker."),
 shape=[
   "Build the inventory for one destination, at full size.",
   "Order it by what blocks contribution first, not by what is easiest.",
   "Show how to learn each kind without pretending to already know it.",
   "Set expectations for a first ninety days that are honest about pace.",
 ],
 research=[
   "Any regulatory or licensing example must be real, current and dated, or "
   "kept generic.",
   "Check the boundary against V9, V14 and V28 before writing.",
 ],
 honesty=[
   "Strong underlying capability does not remove the need for domain "
   "knowledge, credentials, regulation, relationships, systems, or the local "
   "way of working.",
   "Some of these are genuine barriers to entry, not attitude problems. A "
   "licensing requirement is not a mindset.",
   "Relearning takes time that has to be planned for, not willed away.",
 ],
 nofill=[
   "Do not imply that strong underlying capability eliminates the need for "
   "domain knowledge, credentials, regulation, relationships, systems, or "
   "local ways of working.",
   "Do not invent a regulation, a licensing requirement or a timeline.",
   "Do not invent an employer, a colleague or an onboarding outcome.",
 ],
 outcome=("A destination-specific relearning inventory, ordered, with the "
          "first item already started."),
 boundary=("V9 is the decision to change. V14 is the comparison method before "
           "the decision. V21 is after arrival. V28 is building a career that "
           "survives industry change over a long horizon. V29 is expertise that "
           "has become too narrow."),
 route="Field Kit. Carried for slot 21.",
 watchnext="Proposal only: V21 into V9. Settle with the script.",
 thumb="NOT EVERYTHING TRAVELS is carried from the locked roadmap.",
 donot=[
   "Do not imply that strong underlying capability eliminates the need for "
   "domain knowledge, credentials, regulation, relationships, systems, or "
   "local ways of working.",
 ],
 open=[
   "One worked destination or two contrasting ones?",
   "Does this video assume the change has happened, or serve someone deciding?",
 ],
),
# ------------------------------------------------------- RESERVED BRIEF
dict(
 num="RESERVED",
 label=("Before You Accept the Job, Find Out How the Company Actually Uses "
        "People Like You"),
 status=("RESERVED. No slot number is assigned, and none is proposed here. "
         "The working title is the agreed development direction."),
 problem=("The offer is in front of you. The role sounds right. You still do "
          "not know whether this company will actually use the experience you "
          "are bringing, or park it."),
 job=("Turn a reputation question into a checkable question about one role and "
      "one team, answered before the offer is accepted."),
 separate=[
   "The company's overall reputation, from this team's actual practice.",
   "The advertised role, from the work described in the interviews.",
   "Decision rights, from accountability. Being answerable for an outcome is "
   "not the same as being allowed to decide it.",
   "A stated commitment to internal mobility, from evidence of internal moves "
   "that actually happened.",
   "An anecdote, from a corroborated, dated pattern.",
 ],
 opening=("Proposed opening territory, not approved speech: the offer that "
          "looks right on paper, and the question the interview process never "
          "asked on the viewer's behalf."),
 shape=[
   "State plainly, on camera, what people like you means here: the experience "
   "and contribution someone brings. It is not an assumption about demographic "
   "identity, and the video should say so rather than leave it implied.",
   "The five things to examine: the advertised role, accounts from current and "
   "former employees, decision rights relative to accountability, evidence of "
   "internal moves, and what happened to comparable experienced hires.",
   "How to ask these questions in an interview without sounding adversarial.",
   "How to weigh what comes back, including how to record uncertainty.",
 ],
 research=[
   "Treat employee reviews and anecdotes as leads to investigate, not proof "
   "about every team.",
   "Date and contextualize every claim, seek corroboration, and label "
   "uncertainty where corroboration is not available.",
   "Keep any employer-specific claim out of the script unless it is "
   "documented, dated and corroborated, and send it for review before "
   "publication.",
 ],
 honesty=[
   "A good reputation does not guarantee that this team will develop this "
   "person.",
   "A single negative review is not evidence about an organization, and a "
   "single positive one is not either.",
   "Some of these questions cannot be answered before accepting. Naming the "
   "unanswered question is part of the outcome, not a failure of the method.",
 ],
 nofill=[
   "Do not fabricate employer records, internal policies or hiring data.",
   "Do not publish unsupported accusations about a named employer.",
   "Do not imply that a good reputation guarantees development.",
   "Do not assume a demographic identity behind people like you.",
   "Do not name a real employer as a negative example without documented, "
   "dated, corroborated support, and consider whether naming is necessary at "
   "all.",
 ],
 outcome=("A short offer-check record in three columns: the promise, the "
          "evidence supporting it, and the question still needing an answer. "
          "Compare the role and the team, not just the employer's overall "
          "reputation."),
 boundary=("V9 is the decision to change industries. V13 tests a possible "
           "destination over thirty days. V22 is the wait-or-move decision "
           "inside the current employer. V27 is why companies miss the talent "
           "they already have, from the organization's side. This brief is the "
           "destination check before accepting an offer."),
 route=("Career Decision Evidence Check is the natural fit. This is a proposal, "
        "and no route is committed while the slot is unassigned."),
 watchnext=("Not proposed. Routing cannot be set for an unassigned slot."),
 thumb=("No thumbnail copy is proposed. The slot is unassigned and the title "
        "is a development direction, not final packaging copy."),
 donot=[
   "Do not assign this brief an existing occupied slot silently.",
   "Do not assign it a number without approval.",
   "Do not fabricate employer records, publish unsupported accusations, or "
   "imply that a good reputation guarantees development.",
 ],
 open=[
   "Where does this sit once approved, given that V22 and V23 keep their "
   "positions?",
   "Does it need a legal review pass before scripting, given the employer "
   "reputation territory?",
 ],
),
]


def by_num(num):
    for b in BRIEFS:
        if b["num"] == num:
            return b
    raise KeyError(num)
