# -*- coding: utf-8 -*-
"""Full-screen slides and reveal states for V1, V2 and V3.

V1 reuses the approved flagship sequence rather than inventing a competing
framework, as the refresh brief requires. Its eight teaching slides are the
flagship slides; four card lines were changed, and only where the new spoken
master says something different from the line the flagship card carried. Those
four are listed in V1_CARD_CHANGES so the reconciliation is auditable.

V2 and V3 are built from their own slide intents on the same visual system.

Every video gains three full-screens the flagship package did not have: the
seven-day memory card the sticky-realization pass requires, the full-screen
CTA, and the full-screen Watch Next that is the final frame.
"""
import st_lay as L
import fl_frames as FL

# --------------------------------------------------------------------- V1
# Reconciliation against the new master. Each entry is (card, was, is now, why).
V1_CARD_CHANGES = [
 ("FLAG_02D_WHERE_ADVICE_STOPS",
  "This is where “transferable skills” advice often stops.",
  "This is where transferable-skills advice often stops.",
  "The new master says transferable-skills as a compound. The card quoted it "
  "as two words in quotation marks, which reads as scare quotes the spoken "
  "line does not have."),
 ("FLAG_03_MATCHING_WORDS",
  "Matching words aren't enough. / What decision sits under the word?",
  "Matching words are not enough. / What decision sits underneath the word?",
  "This is V1's seven-day memory line, so the card has to be the sentence the "
  "viewer hears. The master says are not, and underneath."),
 ("FLAG_05C_HIGHER_TITLE",
  "A higher title doesn't just mean more of the same work.",
  "A higher title does not just mean more of the same work.",
  "Contraction the spoken master does not use."),
 ("FLAG_06C_ALL_GAPS",
  "Better resume language doesn't create experience you haven't had.",
  "Better resume language does not create experience you have not had.",
  "Contractions the spoken master does not use."),
]

FL.SETS  # imported for its side-effect-free frame data; states() is rebuilt below

def _v1_s2d(c):
    L.compare_rows(c, "FIRST READ", "A lot of this looks familiar.",
                   FL.S2_LEFT, FL.S2_RIGHT, match=FL.S2_MATCH,
                   banner="This is where transferable-skills advice often stops.",
                   dark=True, divider=None, shown=2, foot=None)

def _v1_s3(c):
    L.beat(c, "THE RE-HOOK", "Matching words are not enough.",
           "What decision sits underneath the word?", dark=True)

def _v1_s5c(c):
    L.compare_rows(c, "THE DIFFERENCE", None, FL.S5_LEFT, FL.S5_RIGHT,
                   banner="A higher title does not just mean more of the same work.",
                   dark=True, divider=None, shown=2, foot=None)

def _v1_s6c(c):
    L.framework(c, "THE REAL GAP", "This is not a wording problem.",
                [(g, None) for g in FL.S6_GAPS], active=None, dark=True,
                foot="Better resume language does not create experience "
                     "you have not had.")

def _v1_memory(c):
    L.beat(c, "SEVEN-DAY MEMORY", "My experience does not\nmove as one block.",
           "Put your current work beside the destination.", dark=True)

def _v1_action(c):
    L.action(c, "THEN DO ONE THING",
             "Separate the move into four columns.",
             ["What travels", "What does not", "What you can prove",
              "What you may need to relearn"],
             resource=None, dark=False)

def _v1_cta(c):
    L.action(c, "ONE THING TO DO", "Start with the evidence side.",
             ["Take one accomplishment.",
              "Turn it into something another person can understand and judge."],
             resource=("Career Evidence Starter",
                       "temidayoafonja.com/career-evidence-starter"), dark=True)

def _v1_watch(c):
    L.watch_next(c, "Is Your Job Making You Harder to Hire?")

# V1 sequence: flagship families 1-8 unchanged except the four reconciled
# states, then the three new full-screens.
V1_SETS = []
for fam, sts in FL.SETS:
    out = []
    for name, draw, note in sts:
        if name == "FLAG_02D_WHERE_ADVICE_STOPS":
            draw = _v1_s2d
        elif name == "FLAG_03_MATCHING_WORDS":
            draw = _v1_s3
        elif name == "FLAG_05C_HIGHER_TITLE":
            draw = _v1_s5c
        elif name == "FLAG_06C_ALL_GAPS":
            draw = _v1_s6c
        out.append((name.replace("FLAG_", "V1_"), draw, note))
    V1_SETS.append((fam.replace("FLAG_", "V1_"), out))
V1_SETS += [
 ("V1_09_SEVEN_DAY_MEMORY", [
   ("V1_09A_MEMORY_LINE", _v1_memory,
    "The memory card. Held longer than any other beat in the video, because "
    "this is the sentence that has to come back next week."),
   ("V1_09B_THE_ACTION", _v1_action,
    "The four columns as an instruction, not as the teaching matrix again.")]),
 ("V1_10_CTA", [("V1_10_CTA", _v1_cta, "Full screen. One resource.")]),
 ("V1_11_WATCH_NEXT", [("V1_11_WATCH_NEXT", _v1_watch,
   "Full screen. The final frame of the video.")]),
]

# --------------------------------------------------------------------- V2
V2_ARTIFACT = "I own the QBR process for this business unit."
V2_UNDERNEATH = ("I combine incomplete operating data, surface the decision "
                 "leaders are avoiding, and create a shared view of what "
                 "needs to happen next.")

V2_OUTSIDE = [
 "Has another function used your judgment?",
 "Has a client or customer relied on it?",
 "Has a former colleague come back to you after the context changed?",
 "Have you solved a similar problem with different people or constraints?",
]
V2_90 = [
 "What unfamiliar problem did I have to solve?",
 "What decision can I now make with less help?",
 "What new constraint, audience or context did I learn to work across?",
 "Is the main change new judgment, or familiar work faster?",
]
# Four situations, described and not ranked. The brief for V2 says this is a
# paired read and NOT a score, so no quadrant is tinted as the good one and
# nothing is added up. Labels are kept short enough to sit on one line.
V2_PATTERN = [
 ("Judgment growing, travels",
  ["Your work may be expanding your options."]),
 ("Judgment growing, tied to here",
  ["Real depth that still needs to be tested or made legible elsewhere."]),
 ("Travels, but no longer stretching",
  ["You may be maintaining value without adding much new."]),
 ("Neither one moving",
  ["Worth paying attention to. One quarter is not a pattern."]),
]
V2_TESTS = [
 ("A PROBLEM, NOT MORE VOLUME", "Ask for work that gives you new judgment."),
 ("ANOTHER FUNCTION", "Work across a different part of the business."),
 ("A DIFFERENT CONTEXT", "Take something you know and use it somewhere else."),
 ("PERMITTED EVIDENCE", "Write down what currently lives only in your head."),
]

def _v2_01(c):
    L.beat(c, "THE TENSION", "Valuable here is not\nthe same as legible\nelsewhere.",
           "How much of that value still makes sense when the company name "
           "disappears?", dark=True)

def _v2_02(c):
    L.claim_card(c, "ON A RESUME", "What the sentence says", V2_ARTIFACT,
                 foot="Inside the company this may mean a lot. Outside it, "
                      "this is the name of an internal process.",
                 dark=False, synthetic=True)

def _v2_03(c):
    L.beat(c, "THE MOVE", "Remove the\ncompany nouns.",
           "What is the person actually doing?", dark=True)

def _v2_04(c):
    L.claim_card(c, "UNDERNEATH IT", "What the work actually is",
                 V2_UNDERNEATH,
                 foot="A teaching example written for this video. It is not "
                      "an employer's words and not anyone's real resume.",
                 dark=False, synthetic=True, size=52)

def _v2_05(shown):
    def draw(c):
        L.ask(c, "DOES IT STILL WORK WHEN THE CONTEXT CHANGES?", None,
                    V2_OUTSIDE[:shown] if shown else V2_OUTSIDE,
                    foot="You do not need a public brand or a job offer.",
                    dark=True)
    return draw

def _v2_06(shown):
    def draw(c):
        L.ask(c, "READ THE LAST 90 DAYS", None,
                    V2_90[:shown] if shown else V2_90,
                    foot="Not: was I busy. Not: did I perform well.",
                    dark=True)
    return draw

def _v2_07(shown):
    def draw(c):
        L.paired(c, "READ THE PATTERN", None, V2_PATTERN, shown=shown,
                 dark=False,
                 foot="A way of looking, not a score. Nothing here is added up."
                      if shown == 4 else None)
    return draw

def _v2_08(c):
    L.lines(c, "ONE THING TO TEST BEFORE YOU LEAVE", None, V2_TESTS,
            foot="Pick one and watch what changes.", dark=True)

def _v2_09(c):
    L.beat(c, "THE PAYOFF",
           "If this context disappeared,\ncould another person see and\nuse what I know how to do?",
           "That is a harder question. It is also a much more useful one.",
           dark=True)

def _v2_memory(c):
    L.beat(c, "SEVEN-DAY MEMORY",
           "What part of this is me,\nand what part is my access\nto this environment?",
           "The next time somebody says we cannot do this without you.",
           dark=True)

def _v2_action(c):
    L.action(c, "TOMORROW", "Take one thing people rely on you for.",
             ["Remove the company language.",
              "Explain the judgment underneath it in plain English.",
              "Then ask where else that judgment has worked."],
             resource=None, dark=False)

def _v2_cta(c):
    L.action(c, "ONE THING TO DO", "Your evidence may still be buried in "
                                   "company language.",
             ["Take one accomplishment.",
              "Make the work underneath it visible."],
             resource=("Career Evidence Starter",
                       "temidayoafonja.com/career-evidence-starter"), dark=True)

def _v2_watch(c):
    L.watch_next(c, "Before You Quit Your Job, Save This First")

V2_SETS = [
 ("V2_01_VALUE_VS_LEGIBLE", [("V2_01_VALUE_VS_LEGIBLE", _v2_01,
   "Cold open beat. On screen before the uncomfortable question is asked.")]),
 ("V2_02_THE_SENTENCE", [("V2_02_THE_SENTENCE", _v2_02,
   "The artifact. Held long enough to be read twice.")]),
 ("V2_03_REMOVE_THE_NOUNS", [("V2_03_REMOVE_THE_NOUNS", _v2_03,
   "One beat. The turn from reading to stripping.")]),
 ("V2_04_UNDERNEATH", [("V2_04_UNDERNEATH", _v2_04,
   "The reveal. Same card shape as slide 2 so the swap is the whole point.")]),
 ("V2_05_ACROSS_CONTEXTS", [
   ("V2_05A_FIRST", _v2_05(1), "One question at a time as each is asked."),
   ("V2_05B_TWO", _v2_05(2), "As above."),
   ("V2_05C_THREE", _v2_05(3), "As above."),
   ("V2_05D_ALL", _v2_05(0), "All four, held.")]),
 ("V2_06_LAST_90_DAYS", [
   ("V2_06A_FIRST", _v2_06(1), "Built one line at a time."),
   ("V2_06B_TWO", _v2_06(2), "As above."),
   ("V2_06C_THREE", _v2_06(3), "As above."),
   ("V2_06D_ALL", _v2_06(0), "The fourth question is the one that separates "
    "new judgment from familiar work done faster.")]),
 ("V2_07_THE_PATTERN", [
   ("V2_07A_ONE", _v2_07(1), "One read at a time. Never scored, never ranked."),
   ("V2_07B_TWO", _v2_07(2), "As above."),
   ("V2_07C_THREE", _v2_07(3), "As above."),
   ("V2_07D_ALL", _v2_07(4), "The paired read complete. The footer says out "
    "loud that this is not a score.")]),
 ("V2_08_ONE_TEST", [("V2_08_ONE_TEST", _v2_08,
   "Four options, one choice. Held while the boundary is spoken.")]),
 ("V2_09_PAYOFF", [("V2_09_PAYOFF", _v2_09, "The payoff question, held.")]),
 ("V2_10_SEVEN_DAY_MEMORY", [
   ("V2_10A_MEMORY_LINE", _v2_memory, "The memory card. The longest hold in "
    "the video."),
   ("V2_10B_THE_ACTION", _v2_action, "The action, as three steps somebody "
    "could do tomorrow.")]),
 ("V2_11_CTA", [("V2_11_CTA", _v2_cta, "Full screen. One resource.")]),
 ("V2_12_WATCH_NEXT", [("V2_12_WATCH_NEXT", _v2_watch,
   "Full screen. The final frame of the video.")]),
]

# --------------------------------------------------------------------- V3
V3_DISAPPEARS = [
 ("DATES AND CONTEXT", "When it happened, and what was going on around it."),
 ("EXACT RESPONSIBILITY", "What was yours, and what was somebody else's."),
 ("PERMITTED REVIEW HISTORY", "Your own recognition record, while you can still see it."),
 ("WHO WAS INVOLVED", "The people who were in the decision with you."),
 ("WHY IT MATTERED", "The reason the decision was hard at the time."),
]
V3_FOUR = [
 "What was true before?",
 "What was my role?",
 "What decision, judgment or influence was actually mine?",
 "What changed, and what permitted evidence supports that result?",
]
V3_ARTIFACT = "I reduced the time an internal process took."
V3_DEEPER = ("I found where the process kept getting stuck, brought together "
             "the people who owned different parts of it, redesigned the "
             "handoff, and made the change without creating another control "
             "problem.")
V3_SUPPORTS = [
 ("DIAGNOSE A BROKEN HANDOFF", "You can find where work actually stalls."),
 ("ALIGN PEOPLE ACROSS FUNCTIONS", "You can move a decision between owners."),
 ("CHANGE A PROCESS SAFELY", "You can do it without creating a new risk."),
]
V3_NEXT = [
 "What from this example should the next role use?",
 "What should the next role force you to build?",
]
V3_PAYOFF = [
 ("THIS IS WHAT I HANDLED", "The problem, and what was actually mine."),
 ("THIS IS WHAT I BECAME ABLE TO DO", "The judgment the work built in me."),
 ("THIS IS WHAT I NEED NEXT", "What the next role has to use, and to build."),
]

def _v3_01(c):
    L.beat(c, "THE WINDOW", "Before your access\ndisappears.",
           "Your experience did not disappear. Some of your ability to "
           "reconstruct it did.", dark=True)

def _v3_02(shown):
    def draw(c):
        L.lines(c, "WHAT DISAPPEARS", None,
                V3_DISAPPEARS[:shown] if shown else V3_DISAPPEARS,
                foot="The project name stays. The judgment disappears."
                     if not shown else None,
                dark=True)
    return draw

def _v3_03(c):
    L.beat(c, "THE RULE", "Keep the proof,\nnot the property.",
           "If you do not have the right to keep it, do not take it.",
           dark=True)

def _v3_04(c):
    L.beat(c, "THE BOUNDARY", "What stays with\nthe employer.",
           "Confidential information. Customer or employee data. Proprietary "
           "documents. Employer-owned material.", dark=True)

def _v3_05(shown):
    def draw(c):
        L.ask(c, "ONE EXAMPLE, FOUR LINES", None,
                    V3_FOUR[:shown] if shown else V3_FOUR,
                    foot="You do not need a filing cabinet.", dark=True)
    return draw

def _v3_06(c):
    L.claim_card(c, "WHAT YOU WROTE", "The line as most people write it",
                 V3_ARTIFACT,
                 foot="That gives me an outcome, but not much else.",
                 dark=False, synthetic=True)

def _v3_07(c):
    L.claim_card(c, "WHAT THE WORK WAS", "The same example, reconstructed",
                 V3_DEEPER,
                 foot="A teaching example written for this video. It is not "
                      "anyone's real record.",
                 dark=False, synthetic=True, size=46)

def _v3_08(c):
    L.lines(c, "WHAT DOES THIS ACTUALLY SUPPORT?", None, V3_SUPPORTS,
            foot="Keep the claim narrow. Precision makes evidence more "
                 "credible, not less.", dark=True)

def _v3_09(c):
    L.ask(c, "TEST THE NEXT MOVE", None, V3_NEXT,
                foot="A new logo is not automatically a new direction.",
                dark=True)

def _v3_10(c):
    L.lines(c, "BEFORE YOU RESIGN", None, V3_PAYOFF,
            foot="A stronger place to leave from than, I know I did a lot "
                 "there.", dark=False)

def _v3_memory(c):
    L.beat(c, "SEVEN-DAY MEMORY", "Keep the proof,\nnot the property.",
           "The next time you start thinking seriously about leaving.",
           dark=True)

def _v3_action(c):
    L.action(c, "BEFORE YOU CLOSE YOUR LAPTOP",
             "Take one permitted example and write down four things.",
             ["The problem.", "What was yours.", "What changed.",
              "What you can now support with evidence."],
             resource=None, dark=False)

def _v3_cta(c):
    L.action(c, "ONE THING TO DO",
             "Deciding whether to stay, move internally or leave?",
             ["Separate what you know from what you are assuming."],
             resource=("Career Decision Evidence Check",
                       "temidayoafonja.com/career-decisions"), dark=True)

def _v3_watch(c):
    L.watch_next(c, "How to Change Careers After 10+ Years Without Starting Over")

V3_SETS = [
 ("V3_01_THE_WINDOW", [("V3_01_THE_WINDOW", _v3_01,
   "Cold open beat, after the six-months-later scene is spoken to camera.")]),
 ("V3_02_WHAT_DISAPPEARS", [
   ("V3_02A_TWO", _v3_02(2), "Built as each is named."),
   ("V3_02B_FOUR", _v3_02(4), "As above."),
   ("V3_02C_ALL", _v3_02(0), "All five, with the line the video turns on.")]),
 ("V3_03_THE_RULE", [
   ("V3_03A_THE_RULE", _v3_03,
    "The rule card. This is the seven-day memory line, so it gets the longest "
    "hold of any card in the video."),
   ("V3_03B_STAYS_WITH_EMPLOYER", _v3_04,
    "Second state of the same idea: what the rule means in practice, listed "
    "explicitly. Held, not flashed. It is a reveal on the rule rather than a "
    "slide of its own, because the boundary and the rule are one thought.")]),
 ("V3_05_FOUR_LINES", [
   ("V3_05A_ONE", _v3_05(1), "One line at a time. This is the frame people "
    "pause and photograph."),
   ("V3_05B_TWO", _v3_05(2), "As above."),
   ("V3_05C_THREE", _v3_05(3), "As above."),
   ("V3_05D_ALL", _v3_05(0), "All four, held.")]),
 ("V3_06_THE_LINE", [("V3_06_THE_LINE", _v3_06,
   "The thin version of the example.")]),
 ("V3_07_THE_WORK", [("V3_07_THE_WORK", _v3_07,
   "The same example rebuilt. Same card shape as the one before it.")]),
 ("V3_08_WHAT_IT_SUPPORTS", [("V3_08_WHAT_IT_SUPPORTS", _v3_08,
   "Three narrow claims. Held while the do-not-overclaim line is spoken.")]),
 ("V3_09_TEST_THE_NEXT_MOVE", [("V3_09_TEST_THE_NEXT_MOVE", _v3_09,
   "Two questions and the logo line.")]),
 ("V3_10_BEFORE_YOU_RESIGN", [("V3_10_BEFORE_YOU_RESIGN", _v3_10,
   "The three sentences, built as they are spoken.")]),
 ("V3_11_SEVEN_DAY_MEMORY", [
   ("V3_11A_MEMORY_LINE", _v3_memory, "The memory card. Same words as slide "
    "3 on purpose, because repetition is what makes a line survive a week."),
   ("V3_11B_THE_ACTION", _v3_action, "The action, as four things to write.")]),
 ("V3_12_CTA", [("V3_12_CTA", _v3_cta, "Full screen. One resource.")]),
 ("V3_13_WATCH_NEXT", [("V3_13_WATCH_NEXT", _v3_watch,
   "Full screen. The final frame of the video.")]),
]

SETS = {1: V1_SETS, 2: V2_SETS, 3: V3_SETS}

def states(n):
    for fam, sts in SETS[n]:
        for name, draw, note in sts:
            yield fam, name, draw, note

if __name__ == "__main__":
    for n in (1, 2, 3):
        fams = SETS[n]
        print("V%d  %d families  %d states"
              % (n, len(fams), sum(len(s) for _, s in fams)))
