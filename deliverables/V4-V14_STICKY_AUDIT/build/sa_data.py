# -*- coding: utf-8 -*-
"""V4 to V14 sticky-realization reconciliation. Editorial analysis only.

Every row below was written after reading that video's newest approved spoken
master end to end. The master each row was read from is recorded in SOURCES,
with a checksum where the source is a document.
"""

STAMP = "Tuesday, September 23, 2026"

SOURCES = {
 4: ("NEW_V04_Reconciled_Recording_Master.docx", "61da7b8f57cb89fe", 1036),
 5: ("NEW_V05_Reconciled_Recording_Master.docx", "39ba37458fa76ae3", 966),
 6: ("NEW_V06_Reconciled_Recording_Master.docx", "aae268438ce06da8", 1096),
 7: ("NEW_V07_Reconciled_Recording_Master.docx", "d3cdabdca894ae76", 1170),
 8: ("NEW_V08_Reconciled_Recording_Master.docx", "77ea6cb3057e5a12", 889),
 9: ("NEW_V09_Reconciled_Recording_Master.docx", "a7c077f2c5a1b4af", 1069),
 10: ("NEW_V10_Reconciled_Recording_Master.docx", "b8553ead49f5a328", 1701),
 11: ("NEW_V11_Reconciled_Recording_Master.docx", "325b956a583e9dce", 1289),
 12: ("p4_script12.py, locked V12-V14 pack", "module", 1297),
 13: ("p5_script13.py, V13/V14 anonymization patch", "module", 1462),
 14: ("p5_script14.py, V13/V14 anonymization patch", "module", 1457),
}

SOURCE_NOTE = ("V4 to V11 were read from the reconciled recording masters in "
               "V4-V11_SYNC, which are the newest approved spoken masters for "
               "those videos. V12 was read from the locked V12-V14 pack. V13 "
               "and V14 were read from the anonymization patch, which "
               "supersedes the locked versions of those two. Word counts are "
               "the spoken stream only.")

# n: (title, thumbnail, already thinks, realization, memory line, action,
#     earns it, minimal change)
ROWS = {
4: ("AI Took the Task. Who Gets the Experience?", "WHO LEARNS NOW?",
    "AI is making me faster, and faster is good. The only question worth "
    "asking is which tasks it can do.",
    "The unit of analysis is wrong. The question is not which task AI takes. "
    "It is where the learning that task used to produce now happens. Senior "
    "judgment was built from hundreds of small decisions, and if those "
    "decisions stop arriving, nobody notices until they need somebody who has "
    "practiced.",
    "If the tool gets faster, what is the person still getting better at?",
    "Take one task AI now helps with and write three columns: BEFORE AI, WITH "
    "AI, STILL MINE. If the third column is almost empty, ask where the "
    "learning comes from next.",
    "YES",
    "None. LOCKED AS-IS."),
5: ("If Your Company Needs You but Won't Grow You", "USEFUL. STILL STUCK.",
    "I am the person everyone depends on, so I must be safe here. They passed "
    "me over anyway, so maybe I am not good enough.",
    "Being needed and being developed are two different things, and the first "
    "can quietly prevent the second. The manager keeping you in place may have "
    "a real reason that is not about you.",
    "Are they asking for more of your capacity, or expanding your capability?",
    "Ask for one piece of work that builds a new decision, a new problem or "
    "new proof, and set a date to review what actually changed.",
    "YES",
    "None. LOCKED AS-IS."),
6: ("Decode a Job Description in 10 Minutes", "IGNORE THE TITLE",
    "That title sounds too senior for me. I should apply to titles that look "
    "like mine.",
    "The title is not the job, and it misleads in both directions. An "
    "impressive title sat on a $61,500 floor; the least clear title in the "
    "sample sat on the highest published ceiling.",
    "The title can start the search. It cannot finish the read.",
    "Take one posting you are actually considering and write four lines: "
    "problem, authority, proof, real gap. Then circle the strongest verbs.",
    "YES",
    "None. LOCKED AS-IS."),
7: ("I've Seen Who Gets the Bigger Role and Why", "THEY CHOSE SOMEONE ELSE",
    "I work harder than the person who got it. If I keep being dependable, my "
    "turn will come.",
    "The evidence people can see is evidence for the role you already have. "
    "Rescue and cleanup make you more useful without making you easier to "
    "picture at the next level. And some of it is access and sponsorship, not "
    "capability at all.",
    "If the bigger role opened tomorrow, what could someone already point to?",
    "Write down the last three times you were trusted with something bigger, "
    "and for each one name the problem, the decision that was yours, who saw "
    "it, and what changed.",
    "YES",
    "None. LOCKED AS-IS."),
8: ("What Disappears When Your Work Access Ends", "YOU CAN'T PROVE IT LATER",
    "I will write it all down later, before the next interview. And I would "
    "never take company files anyway.",
    "The worst time to reconstruct your evidence is after you lose access to "
    "it. Five specific details go first, and they are exactly the ones that "
    "turn a memory into something another person can judge.",
    "Keep the proof. Not the property.",
    "Pick one project and write five things in your own words: baseline, "
    "scope, the decision that was yours, the result, and how it was judged.",
    "YES",
    "None. LOCKED AS-IS. See the construction collision noted below."),
9: ("Transferable Skills Advice Is Missing Something", "NOT EVERYTHING TRAVELS",
    "My skills are transferable. That is the reassuring part, so I will lead "
    "with it.",
    "The reassuring question hides the useful one. What am I leaving behind? "
    "Some of what made you excellent belonged to the environment, and the "
    "column that makes you least confident is the one that tells you the size "
    "of the move.",
    "The capability may still be there. The shortcuts are not.",
    "Take one destination role and make four columns: travels, does not "
    "travel, proof, relearn. Do not force everything into the first column.",
    "YES",
    "None required. LOCKED AS-IS. One optional single-sentence change is "
    "specified below, and only if Temidayo wants the V1 collision resolved."),
10: ("Your First 90 Days in a New Job: What Really Matters",
     "DON'T SPEND YOUR FIRST 90 DAYS PROVING YOURSELF",
     "I have to prove they made the right decision, fast.",
     "You are not the only one being evaluated. The first 90 days are also "
     "your first real evidence about the job, and experience and context are "
     "not the same thing.",
     "Your first 90 days are not only evidence about you. They are your first "
     "real evidence about the job.",
     "Write four lines at day 90: READ, what do I understand now that I did "
     "not on day one. TEST, what travelled and what needed translating. "
     "PROVE, what can I now show. ROLE CHECK, what have these 90 days taught "
     "me about the job itself.",
     "YES",
     "None. LOCKED AS-IS. See the construction collision noted below."),
11: ("What to Do When Your New Job Isn't the Job You Accepted",
     "THIS ISN'T THE JOB",
     "This is not what I signed up for. Either I was lied to, or I am being "
     "impatient.",
     "Both readings skip the useful question. Roles legitimately change. What "
     "matters is what the drift is costing you, in capability, evidence, "
     "compensation or life, because a mismatch can be fine in one of those and "
     "unacceptable in another.",
     "If those two versions are different, name the difference before you "
     "normalize it.",
     "Write EXPECTED and ACTUAL side by side, name one real cost, then choose "
     "one next action: clarify, negotiate, test for a defined period, or start "
     "planning another option.",
     "YES",
     "None. LOCKED AS-IS."),
12: ("How to Turn One Accomplishment Into Proof in 10 Minutes",
     "CAN YOU PROVE IT?",
     "My resume line is strong. It has a verb, scope and a number in it.",
     "The line is not weak because you were modest. Twelve words cannot carry "
     "a year of context, and what fell out on the way is precisely what a "
     "stranger needs in order to judge it.",
     "You did the work. I believe you. The sentence does not.",
     "Take one accomplishment and write four lines: what was true before, what "
     "was mine to decide, what was not obvious, what changed and how I know. "
     "Then ask whether a stranger could check any of it.",
     "YES",
     "None. LOCKED AS-IS."),
13: ("Which Parts of Your Experience Actually Transfer to Another Industry?",
     "SAME WORDS. DIFFERENT WORK.",
     "I have managed risk for years, so I can do any job that says manage "
     "risk.",
     "Three postings using the same two words describe three different jobs "
     "with three different consequences. The method travels. The instinct for "
     "what counts as wrong in a room you have never been in does not.",
     "You can carry the method. You cannot carry the instinct for what counts "
     "as a risk in a room you have never been in.",
     "Take one posting and underline every place its language matches your "
     "experience. Then for each match ask whether the decision underneath "
     "matches too, and what happens there when it goes wrong.",
     "YES",
     "None. LOCKED AS-IS."),
14: ("I Read Two Similar Jobs. They Wanted Different Proof",
     "SAME WORK. DIFFERENT REQUIREMENTS.",
     "Employers hiring this kind of role all want roughly the same thing, so "
     "there is one right way to present myself.",
     "Two employers hiring the same family of work inverted each other. One "
     "made the method required and the subject matter optional; the other did "
     "the reverse. The requirement is a fact about that posting, not about the "
     "field.",
     "Sometimes the employer wrote the important part down. Read it.",
     "Take one posting and read it twice. First pass, mark every requirement "
     "as required or preferred in the posting's own words. Second pass, write "
     "what the words actually support and what you still cannot tell.",
     "YES",
     "None. LOCKED AS-IS."),
}

VERDICT = ("All eleven already deliver the four items. Recognition, the "
           "realization, a natural sentence that can survive a week, and an "
           "observable action are present in every one of the newest approved "
           "masters, and in nine of the eleven the memory line is already "
           "spoken twice: once where it lands and again at the payoff. "
           "Nothing needed the smallest additive change, so nothing was "
           "changed. No revised master was produced in this pass.")

WHY_NO_CHANGE = (
 "This is a result, not a shortcut. The follow-up sets the test explicitly: "
 "read the newest approved master, identify the four items, inspect whether "
 "the script already delivers them, and if it does, preserve it. Each of the "
 "eleven was read end to end against that test and each passed it. Writing a "
 "change into a video that already earns its realization would be rewriting "
 "V4 to V14, which the same instruction forbids twice.")

# The one thing the audit did surface, and it is not a defect in any video.
COLLISIONS = [
 ("Keep the proof, not the property.",
  "V8 (locked) and V3 (new refresh)",
  "V8's close is “Keep the proof. Not the property.” V3's specified "
  "seven-day memory line is “Keep the proof, not the property,” and "
  "V3 says it twice, on two separate cards. Both are correct on their own "
  "terms and the sentence is the right sentence for both.",
  "This is an architecture decision, not an error. V8 is locked and V3's line "
  "is specified by the follow-up prompt itself, so neither can be changed "
  "without a decision from Temidayo. Note that V8's Watch Next already routes "
  "to V17, not to V3, so the two do not sit next to each other in the "
  "sequence. RECOMMENDATION: leave both. A line that repeats across a series "
  "is how a series gets a spine, and this is the strongest sentence either "
  "video has."),
 ("The four columns: travels, does not travel, proof, relearn.",
  "V9 (locked), V13 (locked) and V1 (new refresh)",
  "V9 teaches the four columns as its whole structure. V1's observable action "
  "is to build the same four columns. V13 teaches the same distinction with "
  "different words. Three videos in the same territory run the same "
  "construction.",
  "V9 and V13 are locked and were built as the transfer pair. V1 is a "
  "re-record whose action the follow-up specifies. RECOMMENDATION: leave all "
  "three, but if Temidayo wants separation, the cheapest place to get it is "
  "V9, and the change is one sentence. See below."),
 ("Experienced and new at the same time.",
  "V10 (locked) and V1 (new refresh)",
  "V10 says “You can be experienced and still be new to the context.” "
  "V1 closes on “You can be experienced and new at the same time.” "
  "Near-identical constructions in two videos that are four apart in the "
  "sequence.",
  "V10's own realization is the reversal, that the first 90 days are also "
  "evidence about the job, and that is the line recorded as its memory line "
  "in the table above. The experienced-and-new sentence is supporting "
  "material in V10 and the payoff in V1, so the weight already sits "
  "differently. RECOMMENDATION: leave both, and let V10 lead on the reversal."),
]

OPTIONAL = dict(
 video="V9",
 status="OPTIONAL. Not needed by the four-item test. Only if Temidayo wants "
        "the V1 collision resolved.",
 where="STORY LOOP PAYOFF, the paragraph beginning “The question was "
       "never simply…”",
 add="The capability may still be there. The shortcuts are not.",
 why="That sentence is already in V9, at the paragraph about why a move can "
     "feel humbling late in a career. It is the most natural and most "
     "memorable line in the script and it is currently spoken once, in the "
     "middle, and never returned to. Echoing it at the payoff would give V9 a "
     "memory line of its own that is not the four-column construction V1 now "
     "carries. It adds one sentence, removes nothing, and changes no teaching, "
     "no evidence, no boundary, no CTA and no Watch Next.",
 cost="One sentence, about ten words. V9 would move from 1,069 to roughly "
      "1,079 spoken words. Thought blocks would be regenerated from the "
      "revised master exactly.")

NOT_DONE = [
 ("Revised masters", "None was produced, because none was needed. If Temidayo "
                     "approves the optional V9 change, that master and its "
                     "thought blocks can be regenerated in one pass."),
 ("Production assets", "Not rebuilt, by instruction. The follow-up says not "
                       "to rebuild V4 to V14 production assets until this "
                       "reconciliation is approved."),
 ("V15 and above", "Not opened. The follow-up says not to modify V15+ in this "
                   "task, and nothing in V15 to V22 was touched."),
 ("Renumbering", "Nothing was renumbered and no approved strategy was "
                 "reopened."),
]
