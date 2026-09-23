# -*- coding: utf-8 -*-
"""Dispositions, deep comparisons and the duplication map."""

V = [
 ("V15  AI and proof", "KEEP DISTINCT", "MODERATE",
  "No Missing Rung episode touches AI or the record that survives an "
  "AI-assisted deliverable. Promised by name in locked V4's spoken Watch "
  "Next, so the slot is not movable."),
 ("V16  Valued but overlooked", "KEEP DISTINCT", "MODERATE",
  "MR7 is title loss after holding the title. V16 is never being given it. "
  "Adjacent reads, different viewer. Boundary: V16 must not drift into there "
  "is no role above me, which is MR1's job. Promised by name in locked V7."),
 ("V17  Before a layoff", "KEEP DISTINCT", "SUBSTANTIAL",
  "Nothing in the series does evidence preservation. Promised by name in "
  "locked V8. Its scope problem against V8 is unchanged and still blocking."),
 ("V18  Relearn changing industries", "KEEP DISTINCT", "MODERATE",
  "A context change between industries, not a structure change inside one "
  "organization. But MR8 closes on V18's locked thumbnail phrase, which is a "
  "packaging conflict rather than a duplication. V18 should publish first so "
  "it owns the phrase."),
 ("V19  Career gaps", "KEEP DISTINCT, with the tightest boundary in the slate",
  "MODERATE",
  "MR4's readiness problem against structure problem is V19's practice and "
  "authority gap seen from the other side. V19 owns is this a learning, "
  "practice or evidence problem in me. MR4 owns is the ladder itself gone. "
  "Neither may cross, and they must not publish adjacent."),
 ("V20  Role expands but authority does not", "MERGE INTO MR5", "n/a",
  "Same editorial job. MR5 is the stronger spine. See the deep comparison."),
 ("V21  IC or manager", "MERGE INTO MR6", "n/a",
  "Same question from two viewer states, and most of V21 is already inside "
  "MR6. See the deep comparison."),
]

MR = [
 ("MR1  No next step", "KEEP DISTINCT", "SUBSTANTIAL", 407,
  "Nothing else does broad missing-rung recognition, and separate the title "
  "from what it was supposed to give you is the series' entry idea. Two fixes: "
  "its THE READ paragraph describing the flattened org chart is MR4's job and "
  "should move there, and its twelve-month question is word for word MR3's "
  "and should live in one episode only."),
 ("MR2  Did you move backward?", "MERGE WITH MR8", "SUBSTANTIAL", 379,
  "Both put a manager role beside an IC role and read authority, complexity, "
  "return and reversibility. Both close on the same thought. One episode with "
  "two halves: MR2's recognition, then MR8's decision."),
 ("MR3  Growth with fewer roles above", "KEEP DISTINCT", "SUBSTANTIAL", 290,
  "Redefining growth is its own job and no locked video does it. Two people "
  "same level is the best teaching device in the series. Keeps the "
  "twelve-month question; MR1 gives it up. Absorbs retired old roadmap V29."),
 ("MR4  The ladder does not work the same way", "KEEP DISTINCT",
  "SUBSTANTIAL", 331,
  "The structural diagnosis and the strongest dignity line in the series: you "
  "are allowed to stop blaming yourself for a bottleneck that may not be "
  "about your capability. Best org-chart artifact candidate in the roadmap. "
  "Inherits MR1's flattening paragraph."),
 ("MR5  More people, not a promotion", "ABSORB V20", "SUBSTANTIAL", 262,
  "Survives as the spine of the merged episode. Shortest master in the series "
  "and the one that gains most from V20's material."),
 ("MR6  Should you still want to be a manager?", "ABSORB V21",
  "SUBSTANTIAL", 315,
  "Survives as the management-work decision for both viewer states. Gains "
  "V21's reversibility question and its sample-the-work material."),
 ("MR7  You lost the manager title", "KEEP DISTINCT", "SUBSTANTIAL", 295,
  "Genuinely new. No locked video covers title loss while still employed, and "
  "the two-column read plus the third question, what can I still prove "
  "outside this company, is the cleanest evidence beat in the series. "
  "Boundary: that third column must point at locked V8, not rebuild it."),
 ("MR8  When an IC role is not a step back", "MERGE WITH MR2",
  "SUBSTANTIAL", 389,
  "Its reversibility material and its when-it-is-not section are the sharper "
  "half of the merged episode and it should close the series, which is where "
  "it already sits."),
]

# V20 x MR5
V20_MR5 = [
 ("The trigger", "More projects, teams and problems nobody owns.",
  "More people specifically.",
  "MR5's is narrower and far more recognizable. More people is a scene; more "
  "scope is a category."),
 ("The hook", "Your title did not change. Your pay may not have changed "
  "either. But your role keeps expanding.",
  "Your boss calls you in with good news. The team is getting bigger. There "
  "is one detail. Same level.",
  "MR5 wins clearly. It is a moment rather than a description."),
 ("The central question",
  "What can you decide now that you could not decide before?",
  "What can you decide now that you could not decide before?",
  "Identical sentence in both masters. This is the clearest evidence that "
  "these are one episode."),
 ("The read", "Three named kinds of authority: decision, design, escalation.",
  "Three unnamed sections: complexity, authority, return.",
  "MR5's is cleaner and avoids a named triple. V20's design and escalation "
  "dimensions are genuinely useful and are not in MR5, so they travel as "
  "questions rather than as a named set."),
 ("Negotiation", "If I am going to own the outcome, I would like clarity on "
  "which decisions I can make without additional approval.",
  "What decisions come with the larger span? What changes in compensation or "
  "level? When will we review the scope?",
  "V20's wording is more usable out loud. MR5's four questions are the better "
  "structure. Take both."),
 ("The pattern over time", "If responsibility keeps rising while authority, "
  "recognition and return stay flat, you may be the shock absorber for the "
  "system.", "Not present.",
  "V20 only. This is the most important thing that has to travel, because it "
  "is what turns one assignment into a career read."),
 ("Constraint honesty", "Legal approvals, regulated decisions, budget "
  "controls and governance rules that cannot simply move to you.",
  "Sometimes accepting more without an immediate return is still rational.",
  "Both are real and both should survive. V20's is the more specific."),
 ("Address", "Contains a seven-paragraph manager-side section.",
  "One experienced professional throughout.",
  "MR5 is correct. V20's manager-side section breaks the single-viewer rule "
  "and should not travel."),
 ("The close", "Count what became yours to decide.",
  "Do not confuse being able to carry more with being developed for what "
  "comes next.", "MR5 wins."),
]

V20_MR5_VERDICT = (
 "One episode, built on MR5. I recommended the opposite before the masters "
 "were available, on the reasoning that V20's title covered both the "
 "more-people and the more-projects viewer. Having read MR5, that was the "
 "wrong call: its hook, its read and its close are all stronger, and the "
 "coverage problem is solved inside the script rather than by a vaguer title. "
 "The opening should widen once, early, so the viewer who got three more "
 "projects and no new reports knows the episode is for them.")

# V21 x MR2 x MR6 x MR8
IC_JOBS = [
 ("V21", "Should You Stay an Individual Contributor or Become a Manager?",
  "Management is being offered and nobody has described the job.",
  "What does the job consume. Does the other path exist here. What authority "
  "comes with it. Can you come back. Five variables that do not move "
  "together. Sample the work before committing.",
  "Reversibility with real examples, and the sampling material. Neither is in "
  "MR6."),
 ("MR6", "Should You Still Want to Be a Manager?",
  "You already manage and you are not sure you want to.",
  "Separate wanting seniority from wanting the work. Read an ordinary week. "
  "Inspect whether a real senior IC path exists here. Which hard parts would "
  "you rather own.",
  "The structural premise and the craft-loss hook. Read your week is V21's "
  "what does the job consume, asked better."),
 ("MR2", "If You Go Back to an Individual Contributor Role, Did You Move "
  "Backward?",
  "An IC role is being offered to you in a restructuring and it feels like a "
  "demotion.",
  "Put two roles on the table. Authority, complexity, return, reversibility. "
  "No direct reports does not automatically mean less senior.",
  "The identity hook and the demotion word. The strongest emotional entry in "
  "the series."),
 ("MR8", "When Taking an Individual Contributor Role Is Not a Step Back",
  "You are considering an IC role deliberately.",
  "When it can be forward. When it is not. Put the current manager role "
  "beside the proposed IC role and read decisions, problems, evidence, "
  "compensation, access, next options. Reversibility.",
  "The when-it-is-not section and the question about whether you are choosing "
  "the work or accepting what is left."),
]

IC_VERDICT = [
 ("V21 and MR6 are one episode", "FIRM",
  "Three of V21's four questions are already inside MR6. What does the job "
  "consume is MR6's read your week. Does the other path really exist here is "
  "MR6's inspect the alternative. Neither answer is the brave one is MR6's "
  "which set of hard parts you would rather own. The viewer states differ, "
  "the teaching does not. Build one episode on MR6 and carry V21's "
  "reversibility question and its sampling material across."),
 ("MR2 and MR8 are one episode", "FIRM",
  "Both put a manager role beside an IC role. Both read authority, "
  "complexity, return and reversibility. MR2 closes on read the work; MR8 "
  "closes on it is forward when the actual work, return and future options "
  "fit. That is the same sentence twice. Build one episode that runs from "
  "MR2's demotion question to MR8's deliberate decision."),
 ("The territory goes from four episodes to two", "RECOMMENDATION",
  "One asks whether management work is what you want. One asks whether a move "
  "to IC is backward and when it is not. Those are two genuinely different "
  "questions. Four episodes answering them was three too many."),
 ("What is lost, stated honestly", "COST",
  "V21's title is the stronger evergreen search phrase. Should You Stay an "
  "Individual Contributor or Become a Manager? has clearer search intent than "
  "Should You Still Want to Be a Manager? If Temidayo wants the search title, "
  "the merged episode can take V21's title with MR6's premise and hook. That "
  "is a packaging decision, not an architecture one, and it is listed in the "
  "decisions section."),
]

DUPES = [
 ("MR5 against V20", "MERGE", "Same question, same central sentence."),
 ("MR6 against V21", "MERGE", "Same question, two viewer states."),
 ("MR8 against MR2", "MERGE", "Same read, run twice, closing on the same "
  "thought."),
 ("MR1 against MR4", "DE-DUPLICATE, KEEP BOTH",
  "MR1's THE READ paragraph describes the flattened org chart, which is MR4's "
  "whole job. Move it. The questions the two episodes answer are genuinely "
  "different: MR1 asks what do I do now, MR4 asks is this me or the "
  "structure. If a seven-episode series is ever preferred over eight, this is "
  "the only other defensible merge."),
 ("MR1 against MR3", "DE-DUPLICATE, KEEP BOTH",
  "The twelve-month question appears word for word in both. It belongs in "
  "MR3, where it is a section. MR1's list of what the next title was supposed "
  "to give you is also close to MR3's read-growth list; MR1's should stay "
  "about expectation and MR3's about inspection."),
 ("MR4 against V19", "BOUNDARY, KEEP BOTH",
  "Readiness against structure is the same distinction from opposite sides. "
  "Tightest adjacency across the two slates. They must not publish next to "
  "each other."),
 ("MR7 against locked V8", "BOUNDARY, KEEP BOTH",
  "MR7's third column, what can I still prove outside this company, is V8's "
  "territory. Point at it, do not rebuild it."),
 ("MR7 against V17", "BOUNDARY AND SCHEDULE SEPARATION",
  "Two loss episodes. Different losses. The recommended sequence puts seven "
  "uploads between them."),
 ("MR7 against V16", "NO DUPLICATION", "Never given the role against having "
  "it taken away."),
 ("MR3 against locked V5", "BOUNDARY, KEEP BOTH",
  "MR3's boundary, do not let growth become a nice word a company uses when "
  "it wants senior work at the same pay, sits close to V5's thesis. State the "
  "difference inside MR3: V5 is an employer who will not develop you, MR3 is "
  "an organization with nowhere to promote you into."),
 ("MR2 and MR8 against locked V9 and V13", "BOUNDARY",
  "What still belongs to you is V9 and V13's mechanism. Apply it, do not "
  "re-teach it."),
 ("MR8 against V18", "PACKAGING CONFLICT, NOT DUPLICATION",
  "MR8 closes on you can be experienced and new at the same time, which is "
  "V18's locked thumbnail. V18 owns the phrase. MR8 may use the idea and "
  "should not close on those words."),
 ("Old roadmap V29", "RETIRED AND ABSORBED",
  "Career Ladders Don't Work Like They Used To is within two words of MR4's "
  "title and its four ways a move creates value is MR3's territory. Confirmed "
  "now that both masters have been read."),
 ("MR1 and MR4 against locked V11", "NO DUPLICATION",
  "V11 is role drift inside a job you just accepted."),
 ("MR6 against locked V10", "NO DUPLICATION", "Different situation entirely."),
]
