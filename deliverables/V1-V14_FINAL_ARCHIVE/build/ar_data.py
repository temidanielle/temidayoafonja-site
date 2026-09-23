# -*- coding: utf-8 -*-
"""Manifest content. Every editorial field is carried forward from an approved
document; nothing here is a new editorial decision."""

STAMP = "Tuesday, September 23, 2026"

# Memory line and observable action: V1 to V3 from the approved follow-up
# prompt, V4 to V14 from the approved V4-V14 reconciliation. Not re-derived.
MEMORY = {
1: ("My experience does not move as one block.",
    "Put your current work beside the destination and separate what travels, "
    "what does not, what can be proved, and what may need relearning."),
2: ("What part of this is me, and what part is my access to this environment?",
    "Take one thing people rely on you for, remove the company language, "
    "explain the judgment underneath it, then look for evidence it works "
    "elsewhere."),
3: ("Keep the proof, not the property.",
    "Before access ends, capture one permitted example: the problem, what was "
    "yours, what changed, and what permitted evidence supports it."),
4: ("If the tool gets faster, what is the person still getting better at?",
    "Take one task AI now helps with and write three columns: BEFORE AI, WITH "
    "AI, STILL MINE."),
5: ("Are they asking for more of your capacity, or expanding your capability?",
    "Ask for one piece of work that builds a new decision, a new problem or "
    "new proof, and set a date to review what changed."),
6: ("The title can start the search. It cannot finish the read.",
    "Take one posting and write four lines: problem, authority, proof, real "
    "gap. Then circle the strongest verbs."),
7: ("If the bigger role opened tomorrow, what could someone already point to?",
    "Write down the last three times you were trusted with something bigger, "
    "and for each name the problem, the decision, who saw it, what changed."),
8: ("Keep the proof. Not the property.",
    "Pick one project and write five things in your own words: baseline, "
    "scope, the decision that was yours, the result, and how it was judged."),
9: ("The capability may still be there. The shortcuts are not.",
    "Take one destination role and make four columns: travels, does not "
    "travel, proof, relearn."),
10: ("Your first 90 days are not only evidence about you. They are your first "
     "real evidence about the job.",
     "Write four lines at day 90: READ, TEST, PROVE, ROLE CHECK."),
11: ("If those two versions are different, name the difference before you "
     "normalize it.",
     "Write EXPECTED and ACTUAL side by side, name one real cost, then choose "
     "one next action: clarify, negotiate, test, or plan another option."),
12: ("You did the work. I believe you. The sentence does not.",
     "Take one accomplishment and write four lines: what was true before, what "
     "was mine to decide, what was not obvious, what changed and how I know."),
13: ("You can carry the method. You cannot carry the instinct for what counts "
     "as a risk in a room you have never been in.",
     "Take one posting and underline every language match, then ask whether "
     "the decision underneath matches too."),
14: ("Sometimes the employer wrote the important part down. Read it.",
     "Read one posting twice: mark required versus preferred in the posting's "
     "own words, then write what the words support and what you cannot tell."),
}

CTA = {
1: "Career Evidence Starter", 2: "Career Evidence Starter",
3: "Career Decision Evidence Check",
4: "None named in the spoken master",
5: "None named in the spoken master",
6: "None named in the spoken master",
7: "None named in the spoken master",
8: "None named in the spoken master",
9: "None named in the spoken master",
10: "None named in the spoken master",
11: "None named in the spoken master",
12: "Career Evidence Starter",
13: "Capability Formation Field Kit",
14: "Capability Formation Field Kit",
}

WATCH_NEXT = {
1: "Is Your Job Making You Harder to Hire?",
2: "Before You Quit Your Job, Save This First",
3: "How to Change Careers After 10+ Years Without Starting Over",
4: "How to Prove Your Value When AI Does More of the Task",
5: "It Took Me Years to Stop Mistaking More Work for Career Growth",
6: "Turn One Accomplishment Into Proof in 10 Minutes",
7: "What to Do When Your Work Is Valued but You Are Overlooked",
8: "Before a Layoff, Know What You Can Still Prove",
9: "Which Parts of Your Experience Actually Transfer to Another Industry?",
10: "What to Do When Your New Job Isn’t the Job You Accepted",
11: "If Your Company Needs You but Won’t Grow You",
12: "Which Parts of Your Experience Actually Transfer to Another Industry?",
13: "I Read Two Similar Jobs. They Wanted Different Proof",
14: "How to Turn One Accomplishment Into Proof in 10 Minutes",
}

PRODUCTION = {
1: ("SYNCHRONIZED", "Built September 23, 2026 against this exact master. "
    "Included in 03_PRODUCTION_ASSETS_REFERENCE."),
2: ("SYNCHRONIZED", "Built September 23, 2026 against this exact master. "
    "Included in 03_PRODUCTION_ASSETS_REFERENCE."),
3: ("SYNCHRONIZED", "Built September 23, 2026 against this exact master. "
    "Included in 03_PRODUCTION_ASSETS_REFERENCE."),
}
for n in range(4, 12):
    PRODUCTION[n] = ("SYNCHRONIZED", "Synchronized production package of "
                     "September 16 to 19, 2026, built against this reconciled "
                     "master. Included by reference as a ZIP.")
PRODUCTION[12] = ("SYNCHRONIZED", "In the locked V12-V14 pack, built against "
                  "this master. Included by reference as a ZIP.")
for n in (13, 14):
    PRODUCTION[n] = ("SYNCHRONIZED", "In the anonymization patch, built "
                     "against this corrected master. Included by reference as "
                     "a ZIP. The pre-anonymization production package in the "
                     "locked pack is SUPERSEDED for this video.")

PROVENANCE_NOTES = {
1: "OPEN. The two role types shown on screen are anonymized. The employer "
   "names and source URLs behind them are not in this workspace, were not "
   "supplied, and were not invented. Both roles still need an employer, the "
   "exact advertised title and a source URL with a collection date before "
   "publication.",
2: "The resume sentence and the version underneath it are constructed teaching "
   "examples, labelled SYNTHETIC EXAMPLE on the card.",
3: "The worked example is a constructed teaching example, labelled SYNTHETIC "
   "EXAMPLE on the card. The safety boundary and the property boundary are "
   "spoken on camera.",
12: "The accomplishment is synthetic and is labelled as such on camera and on "
    "the card.",
13: "Employer names were removed by the approved anonymization patch. The "
    "28-posting research record backs every count.",
14: "Employer names were removed by the approved anonymization patch. Both "
    "postings are described by industry only.",
}

FUSED_NOTE = (
 "RESOLVED SEPTEMBER 23, 2026 \u2014 FORMATTING ONLY. NO SPOKEN WORDING "
 "CHANGED.\n\n"
 "V2 and V3 each carried a section label that sat inside the first spoken "
 "paragraph rather than in a paragraph of its own, separated from the sentence "
 "by a line break: READ THE LAST 90 DAYS in V2 and KEEP THE PROOF, NOT THE "
 "PROPERTY in V3. In Word the label already looked like its own line. It "
 "simply was not its own paragraph, so any paragraph-level reader counted the "
 "label as speech. The same condition was present in the recording master and "
 "the thought-block copy of each video, identically.\n\n"
 "Temidayo authorized the repair on September 23, 2026 as a formatting-only "
 "correction. Each label is now its own paragraph, formatted exactly like the "
 "other section labels in the same file, and marked NOT SPOKEN in the "
 "thought-block copies as the other labels are. No spoken word was changed, "
 "added or removed, and no punctuation inside any spoken sentence was "
 "touched. The change was verified token by token against the pre-repair "
 "files: the only difference in either spoken stream is that the label's own "
 "words stopped being counted.\n\n"
 "V2 now reads 888 spoken words and V3 reads 923, in both the master and the "
 "thought-block copy, which is the count the production build already used. "
 "The two counts no longer differ. A scan of all twenty-eight archived files "
 "found these four paragraphs and no others carrying a line break, so no "
 "other word count in this archive was affected.")

CURRENT = [
 "The fourteen recording masters in 01_RECORDING_MASTERS. V2 and V3 carry the\n  authorized formatting repair of September 23, 2026.",
 "The fourteen thought-block copies in 02_THOUGHT_BLOCKS.",
 "The three documents in 00_SOURCE_OF_TRUTH.",
 "The production packages referenced in 03_PRODUCTION_ASSETS_REFERENCE, each "
 "built against the master it sits beside.",
]

SUPERSEDED = [
 ("V1, V2 and V3 published scripts and packages",
  "deliverables/video-1-slides, video-2-slides, video-3-slides",
  "Superseded as spoken source by the FINAL Sticky Realization masters. The "
  "design work in those folders remains the visual reference and was reused."),
 ("V1, V2 and V3 earlier refreshed masters and their thought blocks",
  "Uploaded before September 23, 2026",
  "Intermediate history. Explicitly superseded by the FINAL Sticky Realization "
  "files. Do not package these as current."),
 ("V1, V2 and V3 earlier H.I.T. spoken copies and stronger-hook drafts",
  "deliverables/video-N-slides/hit-final and script folders",
  "Intermediate history."),
 ("V4 to V9 sprint-era masters and thought blocks",
  "deliverables/SPRINT_V4-V9",
  "Superseded by the reconciled masters in V4-V11_SYNC, which are the approved "
  "spoken source for V4 to V9."),
 ("V10 and V11 pre-sync masters and thought blocks",
  "deliverables/V10-V11",
  "Superseded by the reconciled masters in V4-V11_SYNC."),
 ("V4 to V11 edit-sync recording scripts",
  "deliverables/V4-V11_EDIT_SYNC/_source",
  "Intermediate history."),
 ("V12 to V14 phase-two and pre-lock builds",
  "deliverables/V12-V14_PHASE2, deliverables/V12-V14_FINAL",
  "Superseded by the locked V12-V14 pack."),
 ("V13 and V14 pre-anonymization masters, thought blocks, cards and Shorts",
  "deliverables/V12-V14_LOCKED, inside the locked pack",
  "Superseded for V13 and V14 only by the anonymization patch. V12 in the "
  "locked pack is NOT superseded and is the approved source for V12."),
 ("Everything under SUPERSEDED_DO_NOT_USE",
  "deliverables/SUPERSEDED_DO_NOT_USE",
  "Already marked. Listed again for completeness."),
]

NO_DELETION = ("Nothing was deleted. Every file named above is still in the "
               "workspace exactly where it was. This document identifies what "
               "is superseded; it does not remove anything.")

RECURRING = [
 ("KEEP THE PROOF, NOT THE PROPERTY", "V3 and V8",
  "Intentional. Approved as a recurring Capability Formation idea, not "
  "duplication to be removed."),
 ("The permanent audit: what travels, what does not, what can I prove, what "
  "must I relearn", "V1, V9 and V13, and elsewhere where naturally earned",
  "Intentional and permanent. Approved."),
 ("Experienced and new at the same time", "V1, with supporting use in V10",
  "Intentional where already earned. Approved."),
]
RECURRING_NOTE = ("These are preserved deliberately. No replacement slogan was "
                  "manufactured and nothing was reworded to make videos sound "
                  "different from one another.")

DESCRIPTIONS_NOTE = (
 "V1, V2 and V3 publishing descriptions were constructed from the recording "
 "masters, because no refreshed descriptions were ever supplied. They are NOT "
 "YET APPROVED FOR PUBLICATION and are kept in "
 "04_DRAFT_PUBLISHING_DESCRIPTIONS_REVIEW_REQUIRED, away from the locked "
 "spoken sources.\n\n"
 "V4 to V14 publishing descriptions exist inside their synchronized production "
 "packages. Approval of those descriptions, as distinct from approval of the "
 "spoken masters, could not be established from the workspace in this pass. "
 "Following the instruction for that case, they are left inside their "
 "production packages in 03_PRODUCTION_ASSETS_REFERENCE and are NOT promoted "
 "into this archive as approved publishing copy. Nothing was moved or edited "
 "to make them look approved.")

NOT_DONE = [
 ("Scripts", "Nothing was rewritten. No editorial change was applied. The "
             "optional V9 sentence was NOT applied."),
 ("Production assets", "Nothing was rebuilt. Existing packages are included by "
                       "reference only."),
 ("V1 provenance", "Still incomplete, by instruction. Employer names and "
                   "source URLs remain NOT SUPPLIED and were not inferred."),
 ("V1 to V3 descriptions", "Still unapproved, and separated accordingly."),
 ("V4 to V14 description approval", "Could not be established from the "
                                    "workspace, so those descriptions were not "
                                    "promoted. Flagged, not fixed."),
 ("V15 and above", "Not opened."),
 ("The fused label in V2 and V3", "RESOLVED September 23, 2026 under "
                                  "explicit authorization. Formatting only. No "
                                  "spoken wording changed."),
]
