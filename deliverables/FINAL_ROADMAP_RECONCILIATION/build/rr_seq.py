# -*- coding: utf-8 -*-
"""Sequence, Watch Next, artifacts, evidence, CTA, packaging, decisions."""

SEQ = [
 dict(n="V15", src="old V17", title="How to Prove Your Value When AI Does More of the Task",
      thumb="SO WHAT DID YOU DO?", block="Promised block",
      note="Named by title in locked V4's recorded Watch Next."),
 dict(n="V16", src="old V16", title="What to Do When Your Work Is Valued but You Are Overlooked",
      thumb="RELIED ON. STILL SKIPPED.", block="Promised block",
      note="Named by title in locked V7's recorded Watch Next."),
 dict(n="V17", src="old V35 plus the V8 boundary", title="Before a Layoff, Know What You Can Still Prove",
      thumb="KEEP THE EVIDENCE", block="Promised block",
      note="Named by title in locked V8's recorded Watch Next."),
 dict(n="V18", src="old V21", title="What You Must Relearn When You Change Industries",
      thumb="EXPERIENCED AND NEW", block="Bridge",
      note="Publishes before the series so it owns experienced and new before MR8 borrows the idea."),
 dict(n="V19", src="old V15", title="The Career Gaps You Don't See Until the Work Gets Harder",
      thumb="WHAT DO YOU RECOMMEND?", block="Bridge",
      note="Owns readiness at the individual level before V22 reads it at the structural level. "
           "Deliberately two slots from V22, not adjacent."),
 dict(n="V20", src="MR1", title="What Happens When the Next Step in Your Career Disappears?",
      thumb="THERE'S NO NEXT ROLE", block="Missing Rung test block",
      note="Opens the playlist. Gives up its twelve-month question to V21 and its org-chart "
           "paragraph to V22."),
 dict(n="V21", src="MR3, absorbing old roadmap V29", title="How Do You Grow When There Are Fewer Roles Above You?",
      thumb="WHAT DOES “UP” MEAN NOW?", block="Missing Rung test block",
      note="Keeps the twelve-month question. Two people, same level is the best teaching device "
           "in the series."),
 dict(n="V22", src="MR4", title="The Career Ladder Doesn't Work the Same Way Anymore",
      thumb="THE NEXT RUNG IS GONE", block="Missing Rung test block",
      note="The diagnosis, and the org-chart artifact. Closes the test block, which is the right "
           "place to measure whether the territory works."),
 dict(n="REVIEW", src="n/a", title="REVIEW POINT BEFORE THE REMAINING FOUR",
      thumb="n/a", block="Decision",
      note="Three episodes is enough to read retention, comments and search behaviour in a "
           "territory the research itself calls a content-market test."),
 dict(n="V23", src="MR5 absorbing V20's source", title="Your Company Gave You More People, Not a Promotion. Is That Growth?",
      thumb="MORE PEOPLE. SAME LEVEL.", block="Missing Rung, remainder",
      note="The practical consequence of V22's structure. Also the natural destination for the "
           "dangling Watch Next promise in locked V5."),
 dict(n="V24", src="MR6 absorbing V21's source", title="Should You Still Want to Be a Manager?",
      thumb="IS MANAGEMENT STILL THE GOAL?", block="Missing Rung, remainder",
      note="The management-work decision, for the person being offered it and the person already "
           "in it. Packaging decision open: V21's search title is stronger."),
 dict(n="V25", src="MR7", title="You Lost the Manager Title. What Did You Actually Lose?",
      thumb="TITLE GONE. VALUE GONE?", block="Missing Rung, remainder",
      note="Seven uploads from V17 so the two loss episodes do not sit together."),
 dict(n="V26", src="MR2 merged with MR8", title="If You Go Back to an Individual Contributor Role, Did You Move Backward?",
      thumb="IS THIS A DEMOTION?", block="Missing Rung, remainder",
      note="Closes the playlist by running from MR2's recognition to MR8's decision."),
]

PLAYLIST = [
 ("1", "V20", "MR1", "Recognition. There is no next role."),
 ("2", "V21", "MR3", "Redefine growth without dismissing promotion."),
 ("3", "V22", "MR4", "Read the real structure."),
 ("4", "V23", "MR5 + V20", "Wider span against real development."),
 ("5", "V24", "MR6 + V21", "The management-work decision."),
 ("6", "V25", "MR7", "Title loss and portable value."),
 ("7", "V26", "MR2 + MR8", "The deliberate IC move."),
]

PLAYLIST_NOTE = (
 "Seven episodes, and every retained one keeps its position relative to the "
 "others. The merges land at the later of the two original slots, which is "
 "why MR2 moves from second to last: it merges with MR8, which already "
 "closed the series. Playlist order is independent of upload order, so the "
 "journey stays coherent whether or not the remaining four publish "
 "consecutively.")

CONSECUTIVE = [
 ("Recommendation", "Three consecutive, then a review point, then the "
  "remaining four. Not seven straight."),
 ("Why not seven straight",
  "The research does not establish search demand and calls the playlist a "
  "content-market test. Seven consecutive uploads is roughly two months of "
  "the schedule spent on an untested territory, with the channel's front "
  "door, career portability, off the air for that whole time. That is the "
  "wrong risk posture for a test."),
 ("Why three and not two or four",
  "Three is the smallest block that still delivers a real journey: "
  "recognition, reframe, diagnosis. A viewer who watches all three has been "
  "given something usable even if the series stops there."),
 ("Why not interleave from the start",
  "The first three route to each other by name and build one argument. "
  "Breaking them up costs the binge and costs the playlist its opening. "
  "Interleaving is the right answer for the remaining four if the test is "
  "mixed."),
 ("What the review should look at",
  "Retention across the three, whether comments show the situation being "
  "recognized rather than debated, and whether the playlist retains viewers "
  "past episode one. Not view count alone."),
 ("If the test is strong", "Run the remaining four consecutively."),
 ("If the test is mixed", "Interleave the remaining four with broader "
  "Capability Formation episodes. The playlist still reads as one journey."),
 ("If the test is weak", "The three still stand on their own and nothing is "
  "wasted. V23's teaching would then need a home, because V20's material "
  "lives inside it."),
]

WATCH_NEXT = [
 ("locked V4", "V15", "Recorded. Names the title."),
 ("locked V7", "V16", "Recorded. Names the title."),
 ("locked V8", "V17", "Recorded. Names the title."),
 ("V15", "locked V12", "The exercise that fixes the problem V15 exposes."),
 ("V16", "V17", "Before any of this gets decided for you, know what you can "
  "still prove."),
 ("V17", "locked V13", "After a loss, where the experience carries."),
 ("V18", "V19", "You relearned the context; now the work gets harder."),
 ("V19", "V20", "And if the reason you never got to carry the call is that "
  "the role above you is gone. The bridge into the series, and it has to be "
  "written deliberately."),
 ("V20", "V21", "CHANGED. MR1 currently routes to MR2, which now closes the "
  "series. Re-point to the growth episode."),
 ("V21", "V22", "Unchanged from MR3's master."),
 ("V22", "V23", "Unchanged from MR4's master."),
 ("V23", "V24", "Unchanged from MR5's master."),
 ("V24", "V25", "Unchanged from MR6's master."),
 ("V25", "V26", "CHANGED. MR7 currently routes to MR8 by its old title. "
  "Re-point to the merged episode's title."),
 ("V26", "V18", "CHANGED. MR8 currently routes back to the playlist start. "
  "Routing to the relearning episode is stronger: you took the IC role and "
  "you are experienced and new at the same time."),
]

ARTIFACTS = [
 ("V15", "ESSENTIAL", "Before and after of one AI-assisted deliverable."),
 ("V16", "OPTIONAL, leaning decorative", "Camera-led is stronger."),
 ("V17", "WOULD DECORATE", "Carried by restraint."),
 ("V18", "OPTIONAL", "One full-screen line about licensing at most."),
 ("V19", "WOULD DECORATE", "The three readings already do the work."),
 ("V20", "OPTIONAL", "MR1's expectation list could go full screen. Its "
  "org-chart paragraph moves to V22, and the artifact should move with it."),
 ("V21", "RECOMMENDED", "Two people, same level. A genuine side-by-side that "
  "the master already writes and that needs no real document."),
 ("V22", "ESSENTIAL", "The old structure against the structure that exists "
  "today. The strongest org-chart read in the roadmap. Needs either a real "
  "anonymized chart with private provenance, or a clearly labelled "
  "constructed one. MR4's master does not say which."),
 ("V23", "RECOMMENDED", "Before and after scope: people, responsibility, "
  "authority, decision rights, compensation, future options. Buildable from "
  "the two masters without a real document."),
 ("V24", "OPTIONAL, upgradeable", "A management job description against what "
  "the person is currently rewarded for. No lawful document in the workspace."),
 ("V25", "RECOMMENDED", "MR7's own two columns plus the third question. The "
  "master already writes the artifact."),
 ("V26", "ESSENTIAL", "MR2's Role A and Role B side by side. Already written "
  "in the master, and already constructed rather than real, which has to be "
  "labelled on screen."),
]

ARTIFACT_NOTE = (
 "Five of the twelve need no external document at all, because the masters "
 "already write the comparison. Only V22 and V24 need something that does not "
 "exist in the workspace. That is a much smaller sourcing problem than the "
 "previous pass estimated, and it is the single clearest gain from having the "
 "masters in hand.")

EVIDENCE = [
 ("The Second-Reader Audit report is still not in the workspace", "BLOCKING",
  "Named as the primary source for the series. Every structural claim in "
  "V20, V21, V22 and V23 traces to it: contraction in management openings, "
  "pressure on layers in the middle, forum language about the role being "
  "over. It needs to be in the workspace with a checksum before those "
  "scripts are written, the way the 28-posting record backs V13 and V14."),
 ("MR2's two roles are constructed and not labelled as such", "REAL, FIXABLE",
  "Role A with eight direct reports and Role B as a principal IC are written "
  "illustrations, not postings. V12 labels its synthetic accomplishment on "
  "camera and on the card. V26 must do the same."),
 ("MR4's org chart has no stated source", "REAL, FIXABLE",
  "The master says imagine the old org chart. If that becomes a full-screen "
  "artifact it needs either a real anonymized chart with private provenance "
  "or an on-screen label saying it is constructed."),
 ("MR8 carries a Watch-Me-Read section label", "REAL, FIXABLE",
  "The master's section label reads WATCH ME READ THE MOVE. Labels are not "
  "spoken, but that is exactly the string that reaches a chapter title or a "
  "card. Rename it."),
 ("Anonymization against the locked V13 and V14", "OPEN, CARRIED FORWARD",
  "The rule is locked prospectively. V13 and V14 name four employers on "
  "camera and cannot be changed. Unresolved from the previous pass."),
 ("No new research was conducted", "NOTE",
  "Nothing here rests on anything outside the workspace and the supplied "
  "masters."),
]

CTA = [
 ("V15", "Career Evidence Starter", "One piece of work whose judgment left no record."),
 ("V16", "None", "The hinge version leaves the viewer needing to tell two situations apart."),
 ("V17", "Keep the Proof", "The system is exactly the problem."),
 ("V18", "Capability Formation Field Kit", "Testing one destination."),
 ("V19", "None", "Naming which of three gaps you have matches no offer."),
 ("V20", "None", "Recognition. Do not sell to someone who has just been told there is no next role."),
 ("V21", "Capability Formation Field Kit", "Growth has to be redefined against a direction."),
 ("V22", "None", "Diagnosis. Give the read and stop."),
 ("V23", "None", "The viewer finishes with a scope conversation to prepare."),
 ("V24", "Career Move Review if live, otherwise none", "Consequential decision, no destination in the workspace."),
 ("V25", "Career Evidence Starter", "MR7's third column, what can I still prove outside this company, is evidence formation."),
 ("V26", "Career Move Review if live, otherwise Field Kit", "Consequential move. Field Kit is the honest fallback."),
]

CTA_NOTE = ("None of the eight masters carries a CTA, which is the correct "
            "default and should be preserved wherever the viewer is not ready "
            "to act. Five of the twelve carry no commercial ask. Career Move "
            "Review still has no page and no URL anywhere in the workspace.")

PACKAGING = [
 ("MR8 closes on V18's locked thumbnail phrase", "CONFLICT, DECISION NEEDED",
  "You can be experienced and new at the same time is V18's thumbnail, "
  "EXPERIENCED AND NEW. V18 owns it. Recommendation: V26 keeps the idea and "
  "does not close on those exact words, and V18 publishes first."),
 ("MR1 and MR4 thumbnails say the same thing", "CONFLICT, DECISION NEEDED",
  "THERE'S NO NEXT ROLE and THE NEXT RUNG IS GONE are the same sentence two "
  "slots apart and would read as one video in a sidebar. Recommendation: V22 "
  "keeps THE NEXT RUNG IS GONE because it is the structural episode, and V20 "
  "moves to something about the reframe rather than the absence."),
 ("V23 packaging", "RESOLVED BY THE MERGE",
  "MR5's title and MORE PEOPLE. SAME LEVEL. recommended over V20's. The "
  "script widens to the more-projects viewer in the opening rather than the "
  "title doing it."),
 ("V24 packaging", "DECISION NEEDED",
  "MR6's Should You Still Want to Be a Manager? against V21's Should You Stay "
  "an Individual Contributor or Become a Manager? MR6's fits the series and "
  "has the better hook. V21's is the stronger evergreen search phrase. Either "
  "works with MR6's premise underneath."),
 ("V26 packaging", "RESOLVED BY THE MERGE",
  "MR2's title and IS THIS A DEMOTION? recommended over MR8's, which answers "
  "its own question before the click."),
 ("MR4 against retired old roadmap V29", "NO COLLISION",
  "V29 stays retired, so only one of the two near-identical titles can ever "
  "be built."),
 ("Everything else", "NO CHANGE",
  "V15 to V19, V21 and V25 keep the packaging already approved. Nothing is "
  "changed for novelty."),
]

DEFRAME = [
 ("The recurring unnamed four-part read", "KEEP UNNAMED, VARY IT",
  "Authority, complexity, return and future options appear as the read in "
  "MR2, MR3, MR5 and MR8. It is never named, which is right, but four "
  "episodes running the same four dimensions becomes a framework the viewer "
  "feels without being given. Keep it unnamed and unnumbered, vary the order "
  "and the wording between episodes, and never draw it as a four-box card."),
 ("V20's three kinds of authority", "DE-FRAME ON THE WAY INTO V23",
  "Decision, design and escalation authority is a named triple. The "
  "distinctions are useful. Carry them as three questions asked in sequence, "
  "not as a labelled set."),
 ("V21's four questions and five variables", "DE-FRAME ON THE WAY INTO V24",
  "Two counted structures in one source. The reversibility question and the "
  "sampling material are what should travel; the counting should not."),
 ("MR5's COMPLEXITY / AUTHORITY / RETURN section labels", "WATCH",
  "Section labels are not spoken, but these three are the closest the series "
  "comes to naming its own structure. Keep them out of any on-screen card."),
 ("MR1's write down three things and MR7's two columns then a third",
  "ACCEPTABLE", "These are instructions for an exercise, not names for a "
  "system. They can stay."),
]

DECISIONS = [
 ("Confirm the three merges", "BLOCKING",
  "MR5 absorbs V20, MR6 absorbs V21, MR2 merges with MR8. All public "
  "numbering downstream depends on these."),
 ("Confirm the test block rather than seven consecutive", "BLOCKING",
  "Three episodes, a review point, then the remaining four. This is a change "
  "from the previous pass and it is driven by the masters being short and "
  "homogeneous and by the research calling the playlist a content-market "
  "test."),
 ("Supply the Second-Reader Audit report", "BLOCKING FOR FOUR EPISODES",
  "No Missing Rung structural claim can be written or checked without it."),
 ("V24 packaging", "BLOCKING FOR THAT EPISODE",
  "MR6's title with the series fit, or V21's title with the search intent. "
  "Both work over MR6's premise."),
 ("V20's thumbnail", "OPEN",
  "THERE'S NO NEXT ROLE reads as the same card as V22's THE NEXT RUNG IS "
  "GONE. One of the two needs to change and V22 should keep its."),
 ("Whether MR8 may use V18's phrase", "OPEN",
  "Recommendation is that V18 owns it as packaging and V26 keeps the idea "
  "without the exact words."),
 ("Artifact sourcing for V22 and V24", "BLOCKING FOR THOSE TWO",
  "A real anonymized org chart and a lawful management job description. "
  "Neither is in the workspace and neither may be invented. If they do not "
  "exist, V22's chart is built as a clearly labelled constructed example and "
  "V24 stays camera-led."),
 ("Career Move Review", "OPEN",
  "Still no page and no URL. It is the natural offer for V24 and V26."),
 ("V17's scope against locked V8", "BLOCKING, CARRIED FORWARD",
  "Unchanged and unaffected by the Missing Rung."),
 ("Learn, Practice, Prove in V19", "BLOCKING, CARRIED FORWARD",
  "Keep all three distinctions, stop presenting them as a named trio."),
 ("Anonymization against locked V13 and V14", "OPEN, CARRIED FORWARD",
  "The only decision here that touches locked material."),
]
