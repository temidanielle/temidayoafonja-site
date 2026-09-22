# -*- coding: utf-8 -*-
"""Sequencing, Watch Next, artifacts, evidence, CTA, revision levels, decisions."""

CONSECUTIVE = [
 ("Recommendation", "Publish V15, V16 and V17 first, then run V20 to V26 as an unbroken block."),
 ("Why those three go first",
  "Locked V4, V7 and V8 each name one of them by title in spoken audio that is already recorded. "
  "Three promises already made outrank any sequencing preference."),
 ("Why V18 and V19 stay where they are",
  "V18 establishes experienced and new before the block borrows that territory, and V19 is the "
  "natural bridge: it ends on why the bigger call never became yours, which is exactly where V20 "
  "starts. Neither needed moving, so neither was moved."),
 ("Why the block runs consecutively",
  "It is a decision journey and the playlist is the product. Broken up, episodes four through "
  "seven stop making sense as answers to episode one."),
 ("The cost, stated plainly",
  "Seven consecutive episodes on one structural situation is the longest single-topic run the "
  "channel will have done, and it takes career portability off the upload schedule for roughly "
  "two months. The alternative is a four and three split with one general episode between. "
  "Recommendation is to run it consecutively and review after the first three."),
 ("Interleaving", "Not recommended. The series survives as a named playlist either way, but the "
                  "Watch Next chain below only works unbroken."),
]

WATCH_NEXT = [
 ("locked V4", "V15", "Already recorded. Names the title."),
 ("locked V7", "V16", "Already recorded. Names the title."),
 ("locked V8", "V17", "Already recorded. Names the title."),
 ("V15", "locked V12", "The exercise that fixes the problem V15 exposes. Routes into an existing "
                       "episode rather than forward, which is fine and keeps V12 alive."),
 ("V16", "V17", "Before any of this gets decided for you, know what you can still prove."),
 ("V17", "locked V13", "After a loss, the next question is where the experience carries."),
 ("V18", "V19", "You have relearned the context; now the work gets harder."),
 ("V19", "V20", "And if the reason you never got to carry the call is that the role above you is "
                "gone. This is the bridge into the block and it has to be written deliberately."),
 ("V20", "V21", "Recognition to the first constructive move."),
 ("V21", "V22", "Redefining growth to reading the actual structure."),
 ("V22", "V23", "Structure to its practical consequence."),
 ("V23", "V24", "Authority to the management question."),
 ("V24", "V25", "The decision to the loss."),
 ("V25", "V26", "Loss to the deliberate move."),
 ("V26", "V18", "You took the IC role and you are experienced and new at the same time. Closes "
                "the loop into an existing episode."),
]

ARTIFACTS = [
 ("V15", "ESSENTIAL", "Before and after of one AI-assisted deliverable."),
 ("V16", "OPTIONAL, leaning decorative", "No real document exists; camera-led is stronger."),
 ("V17", "WOULD DECORATE", "No document to read and manufacturing one would be tasteless."),
 ("V18", "OPTIONAL", "One full-screen line about licensing at most. A layer ladder is a framework "
                     "card."),
 ("V19", "WOULD DECORATE", "The three readings of one moment already do the work."),
 ("V20", "RECOMMENDED", "Old structure against new structure, simply drawn."),
 ("V21", "OPTIONAL", "A side-by-side scope comparison if one can be sourced."),
 ("V22", "ESSENTIAL", "The org-chart read. Strongest Watch-Me-Read candidate in the roadmap."),
 ("V23", "ESSENTIAL if sourceable", "Role as written against decisions actually owned."),
 ("V24", "OPTIONAL, upgradeable", "A management posting against current reward criteria."),
 ("V25", "OPTIONAL", "Title, scope and access compared, only if it teaches."),
 ("V26", "ESSENTIAL if sourceable", "Manager role against proposed senior IC role."),
]

ARTIFACT_NOTE = ("Four of the twelve need a real document that does not exist in the workspace: "
                 "V23, V24, V26 and, to a lesser degree, V21. None may be invented. This is one "
                 "sourcing question, not four, and answering it unblocks the strongest artifacts "
                 "in the roadmap.")

EVIDENCE = [
 ("The anonymization rule conflicts with the V13 and V14 lock", "BLOCKING CONFLICT",
  "The strategic update says public materials should not name the employers used in job-posting "
  "examples and that this applies to V13 and V14. V13 names Humana, Wells Fargo and Mass General "
  "Brigham on camera. V14 names Humana and J.P. Morgan Wealth Management on camera. Both are "
  "locked and this task's own baseline forbids changing them. The two instructions cannot both be "
  "followed. I have not resolved it. Recommendation: apply the rule prospectively from V15 "
  "onward and let V13 and V14 ship as recorded, because unlocking them would mean a re-record, "
  "not an edit. The alternative is a deliberate unlock, which is Temidayo's call alone."),
 ("The Missing Rung source report is not in the workspace", "BLOCKING FOR MR CONTENT",
  "The Second-Reader Audit and Market Discovery Report, September 22, 2026 is named as the "
  "primary source for the whole series and it is not here. Every structural claim in V20, V21, "
  "V22, V23, V25 and V26 traces to it. It needs to be in the workspace with a checksum before any "
  "of those scripts can be written, exactly as the 28-posting record backs V13 and V14."),
 ("The eight MR masters are not in the workspace", "LIMITS THIS AUDIT",
  "Searched by filename and by content across the filesystem. Not present. The merges recommended "
  "here rest on each episode's stated job and its strongest-and-development row, which is enough "
  "to decide duplication but not enough to decide which sentences survive a merge."),
 ("Anonymization must not blur context", "RULE FOR EVERY FUTURE POSTING READ",
  "A healthcare posting and a financial-services posting are accurate neutral identifiers. "
  "Posting A and Posting B are acceptable where the sector does not matter. What is not "
  "acceptable is letting a neutral label turn one posting into an industry-wide claim, which is "
  "the failure mode V13 was built to avoid."),
 ("Private provenance requirements are unchanged", "STANDING",
  "Employer, exact title, URL, collection date, requisition or window, capture route and the "
  "exact language quoted. Every public claim stays traceable even when the public wording is "
  "neutral."),
 ("Forum language is not prevalence", "STANDING",
  "The series may report that professionals describe the manager role as over or a move back as a "
  "demotion. It may not report how common either is."),
]

CTA = [
 ("V15", "Career Evidence Starter", "One piece of work whose judgment left no record."),
 ("V16", "None", "The hinge version leaves the viewer needing to tell two situations apart, and "
                 "no offer is that."),
 ("V17", "Keep the Proof", "The only episode where the system is exactly the problem."),
 ("V18", "Capability Formation Field Kit", "Testing one destination."),
 ("V19", "None", "Naming which of three gaps you have matches no offer."),
 ("V20", "None", "Recognition episode. The viewer is not ready to buy anything and should not be "
                 "asked."),
 ("V21", "Capability Formation Field Kit", "Growth has to be redefined against a direction, which "
                                           "is the Field Kit's job."),
 ("V22", "None", "Diagnostic episode. Give the read and stop."),
 ("V23", "None", "The viewer finishes with a negotiation to prepare."),
 ("V24", "Career Move Review if live, otherwise none", "Consequential specific decision. Still no "
                                                       "destination in the workspace."),
 ("V25", "Career Evidence Starter", "The portable half of what the title carried has to be written "
                                    "down before it can be used."),
 ("V26", "Career Move Review if live, otherwise Field Kit", "Consequential move. Field Kit is the "
                                                            "honest fallback, not a substitute "
                                                            "chosen for pacing."),
]

CTA_NOTE = ("Five of the twelve carry no commercial ask. Four Field Kit or Career Evidence Starter "
            "placements, one Keep the Proof, and two that depend on whether Career Move Review "
            "exists. Searched again: no page and no URL for Career Move Review anywhere in the "
            "workspace.")

LEVELS = [
 ("V15", "MODERATE", "Two competing four-line structures to remove, and a CTA pointed at the "
                     "wrong offer."),
 ("V16", "MODERATE", "The hinge is buried while the first half re-teaches locked V5 and V12."),
 ("V17", "SUBSTANTIAL", "Most of the source is locked V8's material. Re-scope, do not revise."),
 ("V18", "MODERATE", "A named five-layer inventory, and an opening that re-teaches locked V13."),
 ("V19", "MODERATE", "Excellent material on a named three-part structure, with one leg that is "
                     "locked V12's whole video."),
 ("V20", "MODERATE, PROVISIONAL", "MR1 is a first master written before the V12 to V14 standard "
                                  "existed. Level is an estimate until the script can be read."),
 ("V21", "MODERATE, PROVISIONAL", "Same, plus it absorbs old V29's four-part structure, which "
                                  "must not arrive as a named set."),
 ("V22", "MODERATE, PROVISIONAL", "Same, plus it gains the roadmap's most demanding artifact."),
 ("V23", "SUBSTANTIAL", "A genuine merge of two sources, plus old V25's manager-side section has "
                        "to come out and its negotiation beat has to shrink against locked V11."),
 ("V24", "MODERATE", "The source is the strongest in the V15 to V21 slate and yesterday's audit "
                     "rated it LIGHT. It rises to MODERATE only because it now absorbs MR6."),
 ("V25", "MODERATE, PROVISIONAL", "Needs an evidence beat that points at locked V8 instead of "
                                  "rebuilding it."),
 ("V26", "SUBSTANTIAL", "A genuine merge of two episodes into one recognition-to-decision arc."),
]

PACKAGING = [
 ("V23", "Two viable packagings", "MORE SCOPE. SAME POWER. against MR5's MORE PEOPLE. SAME LEVEL. "
  "Recommend V20's, because it covers both the more-people and the more-projects viewer and the "
  "merged episode has to serve both. DECISION."),
 ("V24", "Two viable packagings", "V21's title and TWO JOBS. NOT TWO LEVELS. against MR6's Should "
  "You Still Want to Be a Manager? and IS MANAGEMENT STILL THE GOAL? Recommend V21's unchanged: "
  "the title is the more complete question and the thumbnail is the reversal. DECISION."),
 ("V26", "Two viable packagings", "MR2's title with IS THIS A DEMOTION? against MR8's When Taking "
  "an Individual Contributor Role Is Not a Step Back with BACKWARD... OR BETTER? Recommend MR2's: "
  "it names the actual fear, and MR8's title answers its own question before the click. DECISION."),
 ("V22", "Comprehension check, not a change", "The Career Ladder Doesn't Work the Same Way "
  "Anymore sits within two words of retired old V29. Since V29 will not be built there is no "
  "collision, but the retirement has to be recorded so nobody builds both."),
 ("V20 and V21 thumbnails", "No change", "THERE'S NO NEXT ROLE and WHAT DOES “UP” MEAN "
  "NOW? do different jobs from their titles and from each other."),
 ("Everything else", "No change", "V15 to V19 and V25 keep the packaging already approved. Nothing "
  "here is changed for novelty."),
]

DECISIONS = [
 ("The anonymization rule against the V13 and V14 lock", "BLOCKING",
  "Prospective from V15, or unlock V13 and V14 for a re-record. Recommendation: prospective. This "
  "is the only decision in this document that touches locked material."),
 ("Supply the Second-Reader Audit report", "BLOCKING FOR ALL MISSING RUNG SCRIPTS",
  "No Missing Rung structural claim can be written or checked until it is in the workspace."),
 ("Supply the eight MR masters", "BLOCKING FOR FINAL MERGE WORDING",
  "The merges are decided. Which sentences survive them is not, and cannot be until the scripts "
  "can be read."),
 ("Confirm the three merges", "BLOCKING",
  "MR5 into V20's slot, MR6 into V21's, MR2 with MR8. Everything downstream, including the public "
  "numbering, depends on these three."),
 ("Confirm the two-month block", "OPEN",
  "Seven consecutive Missing Rung uploads, or a four and three split with one general episode "
  "between."),
 ("Artifact sourcing", "BLOCKING FOR FOUR EPISODES",
  "Does Temidayo have a lawful role description, a lawful management job description, and a "
  "lawful senior IC role description she is willing to anonymize? If not, V23, V24 and V26 stay "
  "camera-led and nothing is invented."),
 ("Career Move Review", "OPEN",
  "Still no page and no URL in the workspace. It is the natural offer for V24 and V26 and cannot "
  "be used until it exists."),
 ("V17's scope against locked V8", "BLOCKING, CARRIED FORWARD",
  "Unchanged from yesterday's audit and unaffected by the Missing Rung. V17 cannot be written "
  "until it is settled."),
 ("Learn, Practice, Prove in V19", "BLOCKING, CARRIED FORWARD",
  "Also unchanged. Recommendation remains: keep all three distinctions, stop presenting them as a "
  "named trio."),
 ("Three packaging choices", "OPEN",
  "V23, V24 and V26 each have two viable packagings. Recommendations are stated above and none is "
  "locked."),
]
