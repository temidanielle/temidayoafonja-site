# -*- coding: utf-8 -*-
"""The reconciliation determinations."""

# (video, verdict, confidence, why)
V15_21 = [
 ("V15  AI and proof", "KEEP DISTINCT", "FIRM",
  "Nothing in the Missing Rung touches AI or the record that survives an AI-assisted deliverable. "
  "Also promised by name in locked V4's spoken Watch Next, so it is not movable."),
 ("V16  Valued but overlooked", "KEEP DISTINCT", "FIRM",
  "MR7 is title loss after having the title. V16 is never being given it. Different situation, "
  "different viewer. Boundary to hold: V16 must not drift into there is no role above me, which "
  "is MR1's job. Promised by name in locked V7."),
 ("V17  Before a layoff", "KEEP DISTINCT", "FIRM",
  "Evidence preservation has its own job and no Missing Rung episode does it. Promised by name in "
  "locked V8. Its own scope problem against locked V8 is unchanged from yesterday's audit and is "
  "still the blocking decision for that episode."),
 ("V18  What you must relearn changing industries", "KEEP DISTINCT", "FIRM",
  "Experienced and new is shared emotional territory, not shared teaching. V18 is a context "
  "change between industries. The Missing Rung is a structure change inside one organization. "
  "Boundary to hold: the merged manager-to-IC episode will also feel experienced and new, so it "
  "must not re-teach V18's relearning layers."),
 ("V19  Career gaps you do not see until the work gets harder", "KEEP DISTINCT, with a stated boundary", "FIRM",
  "The real adjacency is with MR4, not with the series generally. V19's practice-and-authority "
  "gap already says the structure of the role kept you close to the decision but never gave you "
  "ownership, and MR4's diagnosis is readiness problem against structure problem. Same mechanism, "
  "different question. V19 owns is this a learning, practice or evidence problem in me. MR4 owns "
  "is the ladder itself gone. Neither may cross into the other."),
 ("V20  Role expands but authority does not", "MERGE with MR5", "FIRM",
  "Same editorial job, different trigger. V20's trigger is more scope; MR5's is more people, "
  "which is a special case of more scope. Both teach count what became yours to decide. Their "
  "thumbnails, MORE SCOPE. SAME POWER. and MORE PEOPLE. SAME LEVEL., would read as the same video "
  "in a sidebar. Build one episode on V20's source, which is a complete 775-word master with "
  "three kinds of authority, usable negotiation language and real constraint honesty, and open it "
  "with MR5's more-people situation."),
 ("V21  IC or manager", "KEEP as the forward decision, ABSORB MR6", "FIRM on the merge, PROVISIONAL on which wording survives",
  "V21's source is the strongest in the whole V15 to V21 slate and yesterday's audit rated it "
  "LIGHT. It already contains MR6's argument: management is often offered as a reward, but it is "
  "not a reward, it is a different job. What MR6 adds is the structural version of the question, "
  "should you still want it now that fewer of these roles exist. That is a beat, not an episode. "
  "Fold it in and retire MR6 as a separate build."),
]

MR = [
 ("MR1  No next step", "KEEP DISTINCT", "FIRM",
  "Nothing in V15 to V21 or V4 to V14 does broad missing-rung recognition. It is the entry point "
  "of the series and the bridge from V19."),
 ("MR2  Did you move backward?", "MERGE with MR8", "FIRM",
  "Both are manager to IC. MR2 is the identity question after or during the move; MR8 is the "
  "deliberate decision. That is one episode with two halves, recognition then decision, and "
  "running them separately would ask the viewer to sit through the same premise twice."),
 ("MR3  How do you grow with fewer roles above you?", "KEEP DISTINCT", "FIRM",
  "Redefining growth is its own job and no locked video does it. Absorbs old roadmap V29's four "
  "ways a move creates value: scope, judgment, evidence, portability. Boundary: this is where the "
  "series must not dismiss promotion or tell anyone compensation does not matter."),
 ("MR4  The ladder does not work the same way", "KEEP DISTINCT", "FIRM",
  "Reading the real structure is the diagnostic spine of the series and the strongest org-chart "
  "artifact candidate. Shares almost the exact title of old roadmap V29, which is now absorbed, "
  "so only one of the two can ever be built."),
 ("MR5  More people, not a promotion", "MERGE into the V20 slot", "FIRM",
  "See V20. The span-specific trigger survives as the opening situation; the episode is built on "
  "the stronger source."),
 ("MR6  Should you still want to be a manager?", "ABSORB into V21", "FIRM",
  "Its unique asset, wanting the work rather than only the level, is one beat and V21's source "
  "already carries most of the argument. Two episodes on the management decision is one too many."),
 ("MR7  You lost the manager title", "KEEP DISTINCT", "FIRM",
  "Genuinely new. No locked video covers title loss while still employed. Boundary: its evidence "
  "beat must reference locked V8 rather than re-teach it, and it must keep the real "
  "market-legibility consequence of a lost title rather than reassuring it away."),
 ("MR8  When an IC role is not a step back", "MERGE with MR2", "FIRM",
  "See MR2. Its reversibility and constraints material becomes the second half and it should "
  "close the series, which is where MR8 already sits."),
]

# Cross-checks against the locked catalogue
LOCKED_CHECKS = [
 ("MR3 against locked V5, If Your Company Needs You but Won't Grow You", "NO DUPLICATION",
  "V5 is an employer who will not develop you. MR3 is an organization with nowhere left to "
  "promote you into. Adjacent, and the distinction has to be stated inside MR3."),
 ("MR3 against locked V7, I've Seen Who Gets the Bigger Role and Why", "NO DUPLICATION",
  "V7 is selection among candidates. MR3 is scarcity of roles."),
 ("MR7 against locked V8, What Disappears When Your Work Access Ends", "BOUNDARY REQUIRED",
  "V8 owns the lawful-record habit. MR7 may point at it and must not rebuild it."),
 ("MR7 against V17, Before a Layoff", "BOUNDARY REQUIRED, AND SEPARATION IN THE SCHEDULE",
  "Both are loss episodes. Different losses, but they should not publish next to each other. The "
  "recommended sequence puts six uploads between them."),
 ("MR2 and MR8 against locked V9 and V13", "BOUNDARY REQUIRED",
  "What travels from the manager role is V9 and V13's mechanism. The merged episode applies it to "
  "one decision. It must not re-teach it."),
 ("MR1 and MR4 against locked V11", "NO DUPLICATION",
  "V11 is role drift inside a job you just accepted. MR1 and MR4 are structural change around a "
  "job you already hold."),
 ("Old roadmap V29, Career Ladders Don't Work Like They Used To", "RETIRE AND ABSORB",
  "Its territory is MR3's and its title is within two words of MR4's. Mark it absorbed so it is "
  "not built later. Note that its four ways a move creates value is another counted framework and "
  "must not travel into MR3 as a named set."),
]

# Recommended public sequence: 10 fields per the brief
SEQ = [
 dict(n="V15", src="old V17, unchanged by this reconciliation",
      title="How to Prove Your Value When AI Does More of the Task", thumb="SO WHAT DID YOU DO?",
      problem="A tool produced most of the visible work and the person cannot show what they "
              "decided.",
      artifact="ESSENTIAL. Before and after of one AI-assisted deliverable, from the constructed "
               "example already in the source.",
      audit="What can you prove?",
      boundary="AI automation is not capability loss. Faster is not worse.",
      adj="Promised by name in locked V4. First upload after V14.",
      offer="Career Evidence Starter"),
 dict(n="V16", src="old V16, unchanged",
      title="What to Do When Your Work Is Valued but You Are Overlooked",
      thumb="RELIED ON. STILL SKIPPED.",
      problem="Trusted for delivery, absent from the conversation about scope.",
      artifact="OPTIONAL, leaning decorative. Camera-led is stronger.",
      audit="What can you prove?",
      boundary="Advancement is not pure merit. A clearer record does not override bias or create "
               "a role that does not exist.",
      adj="Promised by name in locked V7. Must not drift into there is no role above me, which is "
          "V20's job.",
      offer="None, if the hinge version is built"),
 dict(n="V17", src="old V35 plus the boundary set by locked V8",
      title="Before a Layoff, Know What You Can Still Prove", thumb="KEEP THE EVIDENCE",
      problem="A layoff is visible or has happened and the record lives inside systems that are "
              "closing.",
      artifact="WOULD DECORATE. This episode is carried by restraint.",
      audit="What can you prove?",
      boundary="Keep the proof, not the property. Never encourage taking employer files. Good "
               "proof does not guarantee the next job.",
      adj="Promised by name in locked V8. Its scope against V8 is still the blocking decision.",
      offer="Keep the Proof"),
 dict(n="V18", src="old V21, unchanged",
      title="What You Must Relearn When You Change Industries", thumb="EXPERIENCED AND NEW",
      problem="The work is doable and the room is not.",
      artifact="OPTIONAL. At most one full-screen line about licensing.",
      audit="What must you relearn?",
      boundary="Adjacent experience is not automatic qualification. A credential requirement does "
               "not bend to framing. Relearning is not failure.",
      adj="Sits before the Missing Rung block so its emotional territory is established before "
          "the block borrows it.",
      offer="Capability Formation Field Kit"),
 dict(n="V19", src="old V15, unchanged",
      title="The Career Gaps You Don't See Until the Work Gets Harder",
      thumb="WHAT DO YOU RECOMMEND?",
      problem="You know the work and have never had to carry the call.",
      artifact="WOULD DECORATE.",
      audit="What must you relearn?",
      boundary="Exposure is not carrying the decision. Some gaps are not yours to solve alone. No "
               "verdict on the viewer.",
      adj="Last general episode before the block, and the bridge into it. Must stay a diagnosis "
          "of the person, never of the org chart, because V22 owns that.",
      offer="None"),
 dict(n="V20", src="MR1",
      title="What Happens When the Next Step in Your Career Disappears?",
      thumb="THERE'S NO NEXT ROLE",
      problem="The role you were working toward is not there any more.",
      artifact="RECOMMENDED. A simple old structure against new structure.",
      audit="What travels? What does not?",
      boundary="Middle management is not dead. This is one organization changing shape, not a "
               "universal claim.",
      adj="Opens the Missing Rung playlist. Picks up directly from V19's question about why the "
          "bigger call never became yours.",
      offer="None"),
 dict(n="V21", src="MR3, absorbing old roadmap V29",
      title="How Do You Grow When There Are Fewer Roles Above You?",
      thumb="WHAT DOES “UP” MEAN NOW?",
      problem="Growth was defined by the next title and the next title is gone.",
      artifact="OPTIONAL. A side-by-side scope comparison if one can be sourced.",
      audit="What travels?",
      boundary="Do not dismiss promotion. Do not tell anyone compensation does not matter. Do not "
               "romanticize flattening.",
      adj="Follows recognition with the first constructive move. Old V29's four ways a move "
          "creates value may inform it but must not arrive as a named set.",
      offer="Capability Formation Field Kit"),
 dict(n="V22", src="MR4",
      title="The Career Ladder Doesn't Work the Same Way Anymore", thumb="THE NEXT RUNG IS GONE",
      problem="Is this me, or is this the structure?",
      artifact="ESSENTIAL. The strongest org-chart read in the series and the best Watch-Me-Read "
               "candidate anywhere in the roadmap.",
      audit="What does not travel?",
      boundary="Readiness and structure are both real. Naming the structure does not excuse the "
               "readiness question, and it does not make the viewer's frustration irrational.",
      adj="The diagnostic spine. Must not re-run V19's three gaps.",
      offer="None"),
 dict(n="V23", src="V20 source, old V25, merged with MR5",
      title="If Your Role Expands but Your Authority Doesn't", thumb="MORE SCOPE. SAME POWER.",
      problem="More work, more people, more accountability, and the same decisions.",
      artifact="ESSENTIAL if a lawful role description exists. Role as written against decisions "
               "actually owned.",
      audit="What can you prove?",
      boundary="Responsibility is not growth. Exposure is not carrying the decision. Expanded "
               "responsibility may still build real capability.",
      adj="The practical consequence of V22's structure. Opens with MR5's more-people situation.",
      offer="None"),
 dict(n="V24", src="V21 source, old V18, absorbing MR6",
      title="Should You Stay an Individual Contributor or Become a Manager?",
      thumb="TWO JOBS. NOT TWO LEVELS.",
      problem="Management is being offered, or wanted, and nobody has described the job.",
      artifact="OPTIONAL, upgradeable. A management job description against what the person is "
               "currently rewarded for.",
      audit="What travels? What must you relearn?",
      boundary="Neither answer is the brave one. No universal recommendation. Life constraints, "
               "organization and role design all matter.",
      adj="The forward-looking half of the management question. MR6's structural version, should "
          "you still want it now that fewer exist, becomes the opening beat.",
      offer="Career Move Review if it is live, otherwise none"),
 dict(n="V25", src="MR7",
      title="You Lost the Manager Title. What Did You Actually Lose?",
      thumb="TITLE GONE. VALUE GONE?",
      problem="The position is gone and the person cannot tell what left with it.",
      artifact="OPTIONAL. Title, scope and access compared, only if it teaches.",
      audit="What travels? What can you prove?",
      boundary="A lost title has real market-legibility consequences. Do not reassure them away, "
               "and do not dismiss what the title was doing.",
      adj="The loss episode of the series. Deliberately six uploads away from V17 so the two loss "
          "episodes do not sit together.",
      offer="Career Evidence Starter"),
 dict(n="V26", src="MR2 merged with MR8",
      title="If You Go Back to an Individual Contributor Role, Did You Move Backward?",
      thumb="IS THIS A DEMOTION?",
      problem="The move to IC is on the table and it feels like losing.",
      artifact="ESSENTIAL if sourceable. The manager role against the proposed senior IC role.",
      audit="What travels? What must you relearn?",
      boundary="An IC move is not automatically progress and not automatically a demotion. "
               "Preserve pay, authority, market legibility, reversibility and every personal "
               "constraint.",
      adj="Closes the playlist by turning the series' identity question into a decision. Runs "
          "from MR2's recognition to MR8's decision.",
      offer="Career Move Review if it is live, otherwise Field Kit"),
]
