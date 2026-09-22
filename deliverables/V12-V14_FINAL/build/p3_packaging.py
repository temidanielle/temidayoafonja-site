# -*- coding: utf-8 -*-
"""V14 final packaging assessment, run against the reconciled script.

Three candidates, as instructed. Not a new brainstorm: A is the editorial review's
recommendation, B is the strongest survivor from the Phase 2 packaging document, and C
exists only because the reconciled script earns it. One recommendation. Nothing locked.
"""

RETIRED = ("PROVES / SUGGESTS was retired as packaging language. “Proves” is too absolute "
           "for career evidence: a checkable line supports a claim, it does not establish "
           "causation, readiness, or how any reader will take it. The reconciled script no "
           "longer builds that binary, and no V14 file carries the phrase.")

EXCLUDED = "The Experience Gap Hiring Managers Care About"

OPTIONS = [
dict(k="A",
 title="I Read Two Similar Jobs. They Wanted Different Proof",
 thumb="SAME WORK. DIFFERENT REQUIREMENTS.",
 source="Recommended by the in-depth editorial review.",
 gap="Two jobs that read almost the same on paper, and the thing one of them calls optional "
     "is the thing the other one will not move on.",
 fit=("It puts the behavior that makes this channel different right in the title. Temidayo reads, "
      "and the reading produces the finding. It is conversational, it is first person without "
      "being about her, and “they wanted different proof” is employer-side and factually "
      "precise: both postings did ask to be shown different things, and the script shows exactly "
      "where. It claims nothing about intent, so it survives the no-mind-reading rule in the "
      "title itself."),
 cost=("The thumbnail sits very close to V13's SAME WORDS. DIFFERENT WORK. At sidebar size the "
       "two could read as the same video. If that is a concern, C's thumbnail drops straight in "
       "without touching the title.")),
dict(k="B",
 title="I Read Two Real Job Postings Line by Line",
 thumb="REQUIRED OR PREFERRED?",
 source="Strongest survivor from the Phase 2 packaging document (its runner-up), with the "
        "retired thumbnail replaced.",
 gap="Halfway down the second posting it becomes obvious that these two employers are not "
     "asking for the same thing at all.",
 fit=("Truth in packaging. The episode is a read-along and the viewer can verify that promise in "
      "ten seconds. The thumbnail carries the single most usable mechanic in the video, which is "
      "the difference between what a posting requires and what it merely prefers."),
 cost=("It describes the format rather than the viewer's problem, so it is the weakest of the "
       "three on evergreen search. It also gives away no finding, which costs curiosity.")),
dict(k="C",
 title="Two Similar Jobs. Different Hard Requirements.",
 thumb="REQUIRED, NOT PREFERRED",
 source="New. Written against the reconciled script, which now says “hard requirement” "
        "in ordinary speech where it used to say gate.",
 gap="One of these two employers will not move on the years. The other one says in writing that "
     "you do not need to know the subject matter yet.",
 fit=("It is the plainest of the three and it uses the exact words the reconciled script now "
      "uses on camera. The thumbnail is fully distinct from V13's, and REQUIRED, NOT PREFERRED "
      "is the one phrase a viewer can act on immediately."),
 cost=("It leads with the finding rather than the reading, so it does less to establish the "
       "watch-me-read behavior the channel is building. Least distinctive voice of the three.")),
]

RECOMMENDED = "A"
LABEL = "RECOMMENDED FOR TEMIDAYO APPROVAL"

WHY = ("A is recommended. It is the only one of the three that carries the behavior and the "
       "finding at the same time, it reads like something Temidayo would say out loud, and it is "
       "factually precise on the employer side without claiming to know what anybody thinks. B is "
       "honest but gives away no finding. C is the most immediately usable but trades away the "
       "reading. The one real cost of A is thumbnail proximity to V13, and that is fixable "
       "without changing the title: swap in REQUIRED, NOT PREFERRED from C.")

CRITERIA = [
 ("Fast comprehension", "A reads in one pass. B reads in one pass. C is the fastest of the three."),
 ("Curiosity", "A holds the finding back just enough to earn the click. C states the finding, so "
                "it trades curiosity for clarity. B carries the least."),
 ("Conversational language", "A is the closest to spoken English. C is plain but clipped. B is "
                             "plain and slightly flat."),
 ("Distinction from V13", "A's title is fully distinct; its thumbnail is not. B and C are "
                          "distinct on both."),
 ("Watch-me-read behavior", "A and B both put the reading in the title. C does not."),
 ("Employer-side differentiation", "A and C both say the employers asked for different things. "
                                   "B leaves it implied."),
 ("Factual precision", "All three are accurate to the two postings. A's “different proof” "
                       "is supported: one posting requires five years of project management, the "
                       "other seven years in financial services."),
 ("No mind-reading", "None of the three claims to know what a reader thinks."),
 ("No overclaim", "None promises an outcome, an interview, or a hire."),
]

SWAP_POINTS = [
 "V14 recording master, HOOK and CLOSE: no spoken line names the title, so the script survives "
 "any of the three unchanged.",
 "V14 metadata sheet: title and thumbnail fields.",
 "V14 description, opening line.",
 "V14 full-screen title card and the thumbnail text itself.",
 "V13 description, Watch next line, which carries the V14 working title with a bracketed confirm "
 "note. V13's spoken Watch Next describes V14 instead of naming it, so no re-record is needed.",
]
