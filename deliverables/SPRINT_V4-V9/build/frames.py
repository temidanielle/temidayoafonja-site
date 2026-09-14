# -*- coding: utf-8 -*-
"""Full-screen assets for the six sprint videos.

The visual system is the approved one: the same navy, cream and warm gold,
the same layouts, the same rules. Nothing here invents teaching to justify a
card. Every word on every card is the script's own wording, and every cue is
anchored to a whole spoken paragraph of its own script.

These scripts are camera-led and short, so the cue count is deliberately low.
The per-video rules in the brief are honoured in the copy, not in a comment:
V4 never frames AI as threat, V5 never implies being needed is bad, V7 never
reduces advancement to merit, V8 never depicts taking property, and V9 keeps
all four audit questions together.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

import sprint as S
import lay23 as L

REUSE, COPY, NEW = "REUSE", "COPY UPDATE", "NEW"
# A card whose architecture is the former V22's but whose copy carries a
# generic employer label instead of the name. It is no longer byte-
# identical, so it may not claim reuse.
ANON = "ANONYMIZED"


def P(n, i):
    return S.paragraphs(n)[i]


def F(key, n, para, purpose, layout, states, cls=NEW, svg=False, hold=None,
      sound=None, source=None, treatment="STATEMENT", build=None):
    return dict(key=key, video=n, former=S.NUMBERS[n], trigger=P(n, para),
                para=para, mode="FULL SCREEN", purpose=purpose, layout=layout,
                states=states, svg=svg, cls=cls,
                build=build or ("SINGLE" if len(states) == 1 else "BUILD"),
                hold=hold or "Hold until the sentence lands, then cut back.",
                sound=sound or "No accent.", source=source,
                treatment=treatment)


def WN(n):
    """The Watch Next end card. Full screen, final, and silent."""
    return dict(key="NEW_V%d_WATCH_NEXT" % n, video=n, former=S.NUMBERS[n],
                trigger=None, para=None, mode="FULL SCREEN", build="SINGLE",
                cls=NEW, svg=False, treatment="WATCH NEXT",
                purpose="The destination the script speaks. Full screen and "
                        "final: nothing returns to camera after it.",
                layout="Watch Next card, house layout.",
                hold="Cut here on the spoken Watch Next line and end the "
                     "video on it.",
                sound="No accent.",
                source="Intended destination, spoken in the script. Confirm "
                       "it is publicly live before upload.",
                states=[dict(name="NEW_V%d_WATCH_NEXT" % n,
                             reveal="Single state. Final card.",
                             draw=(lambda t: (lambda c: L.watch_next(c, t)))(
                                 S.watch_next(n)))])


# ============================================== NEW V4  (former V26)  AI
V4_THREE = [("Exposure", "Does the person still see enough examples to learn "
                         "the pattern?"),
            ("Ownership", "Do they still have to make a choice?"),
            ("Feedback", "When the output is wrong, do they understand why?")]


def _v4three(a):
    return lambda c: L.sequence(c, "three things to watch",
                                "What to watch when a task is automated.",
                                V4_THREE, active=a)


V4 = [
 F("NEW_V4_FS_01_WHO_GETS_THE_EXPERIENCE", 4, 7,
   "Put the video's question on screen in the words the script uses, before "
   "any framework appears.",
   "Statement. Navy ground.",
   [dict(name="NEW_V4_FS_01_WHO_GETS_THE_EXPERIENCE",
         reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the question",
             "Who gets the experience that used to come from doing the "
             "work?", dark=True, size=72))],
   hold="Cut on the question and hold through it. The three short lines "
        "before it stay on camera.",
   sound="One restrained accent."),

 F("NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL", 4, 11,
   "Separate what a task costs from what it teaches, which is the whole "
   "distinction the video turns on.",
   "Two sides of one idea, joined rather than opposed.",
   [dict(name="NEW_V4_FS_02_INEFFICIENT_AND_DEVELOPMENTAL",
         reveal="Single state.",
         draw=lambda c: L.twopart(
             c, "the tension", "A task can be both.",
             ("inefficient", "Slow, repetitive, sometimes wrong."),
             ("developmental", "It taught you what good looked like."),
             joiner="+"))],
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT", 4, 12,
   "Name what the removed work was teaching, in the script's own three "
   "lines, so the loss is specific rather than atmospheric.",
   "Three short rows, all visible. Spoken as one list.",
   [dict(name="NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what the work taught", "",
             [("Repetition", "Pattern recognition"),
              ("Fixing mistakes", "Judgment"),
              ("Seeing ten bad examples",
               "Why the eleventh one is different")]))],
   svg=True, sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V4_FS_04_THE_REAL_QUESTION", 4, 25,
   "State the question the video is actually asking, immediately after the "
   "script has ruled out the anti-AI reading.",
   "Statement.",
   [dict(name="NEW_V4_FS_04_THE_REAL_QUESTION", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "not an anti-ai argument",
             "If AI does the task, what replaces the learning?",
             support="Not: should AI do the task?", size=68))],
   hold="Cut on the question. The three sentences that protect automation "
        "stay on camera before it.",
   sound="One restrained accent."),

 F("NEW_V4_FS_05_THREE_THINGS", 4, 26,
   "Establish the three things to watch, then take them one at a time so "
   "none is read as the whole test.",
   "Numbered sequence, established whole, then activated one at a time.",
   [dict(name="NEW_V4_FS_05_THREE_THINGS",
         reveal="Establish on 'I would watch three things.'",
         draw=_v4three(None)),
    dict(name="NEW_V4_FS_05A_EXPOSURE", reveal="Activate 1 on 'First: "
         "exposure.'", draw=_v4three(0)),
    dict(name="NEW_V4_FS_05B_OWNERSHIP", reveal="Activate 2 on 'Second: "
         "ownership.'", draw=_v4three(1)),
    dict(name="NEW_V4_FS_05C_FEEDBACK", reveal="Activate 3 on 'Third: "
         "feedback.'", draw=_v4three(2))],
   svg=True, build="ESTABLISH",
   hold="One activation per spoken item. Cut back to camera for the "
        "sentence about judgment being formed.",
   sound="One accent on establish. None on the activations.",
   treatment="SEQUENCE"),

 F("NEW_V4_FS_06_MOVED_OR_REMOVED", 4, 41,
   "Show the two futures for the same automated task without deciding which "
   "one any viewer is in.",
   "Side-by-side contrast.",
   [dict(name="NEW_V4_FS_06_MOVED_OR_REMOVED", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the same task, two outcomes", "",
             ("the work moved", "Test the assumptions. Challenge the output. "
                                "Defend the recommendation.", []),
             ("the work left", "Run the tool. Copy the result. Send it "
                               "upward.", []),
             divider=""))],
   hold="Cut on 'But if their job becomes:' and hold through the three short "
        "lines that follow.",
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V4_FS_07_WHAT_DID_IT_TEACH", 4, 49,
   "Give managers the design question in one line.",
   "Rule card.",
   [dict(name="NEW_V4_FS_07_WHAT_DID_IT_TEACH", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "for managers", "Ask",
             "What did this task used to teach?",
             support="Then decide how that learning happens now."))],
   sound="One restrained accent."),

 F("NEW_V4_FS_08_STILL_PRACTICING", 4, 54,
   "Five questions the viewer can ask themselves, all visible because the "
   "script delivers them as one run.",
   "Questions card, sized so five fit and stay readable on a phone.",
   [dict(name="NEW_V4_FS_08_STILL_PRACTICING", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "for professionals", "",
             ["What am I still practicing?",
              "What am I no longer practicing?",
              "What decisions are still mine?",
              "What mistakes am I still learning from?",
              "Can I explain what I contributed?"], dark=True, size=50))],
   hold="Hold through the five questions and the line about future evidence.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V4_FS_09_NOT_ONE_OUTCOME", 4, 60,
   "Keep the boundary visible: the video claims no single outcome for every "
   "job.",
   "Three short rows, all visible.",
   [dict(name="NEW_V4_FS_09_NOT_ONE_OUTCOME", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "the boundary", "Different jobs will answer differently.",
             [("In some work", "AI may increase learning"),
              ("In regulated or high-risk work",
               "Human review may remain essential"),
              ("In other roles", "The task may truly disappear")],
             foot="not a claim about one outcome", dark=True))],
   hold="Hold through the list and the sentence that refuses a single "
        "outcome.",
   sound="No accent.", treatment="SEQUENCE"),

 F("NEW_V4_FS_10_THREE_COLUMNS", 4, 74,
   "The action, as three columns the viewer can actually draw.",
   "Action card. The three columns are the ask.",
   [dict(name="NEW_V4_FS_10_THREE_COLUMNS", reveal="Single state.",
         draw=lambda c: L.action(
             c, "one thing to do", "Audit one task AI now helps you with.",
             ["Before AI.", "With AI.", "Still mine."],
             resource=("If the third column is almost empty, ask where the "
                       "learning comes from next.", "")))],
   hold="Cut on 'Write three columns:' and hold through the three lines that "
        "define them.",
   sound="One accent.", treatment="CTA"),

 F("NEW_V4_FS_11_TASK_IS_NOT_THE_JOB", 4, 82,
   "The closing distinction, which is also the video's protection against "
   "being read as a job-loss prediction.",
   "Statement.",
   [dict(name="NEW_V4_FS_11_TASK_IS_NOT_THE_JOB", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "close",
             "AI taking the task is not the same as AI taking the job.",
             size=64))],
   sound="One restrained accent."),
 WN(4),
]


# ====================================== NEW V5  (former V33)  dependence
V5 = [
 F("NEW_V5_FS_01_NEEDED_NOT_GROWN", 5, 6,
   "Name the painful position in the script's own two lines, before any "
   "analysis of it.",
   "Two sides of one position.",
   [dict(name="NEW_V5_FS_01_NEEDED_NOT_GROWN", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "a painful place to be", "",
             ("needed by the company", "They call you when something "
                                       "breaks.", []),
             ("but not necessarily grown by it",
              "Then a bigger opportunity opens.", []),
             divider=""))],
   hold="Cut on the two-line paragraph and hold through it.",
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V5_FS_02_NOT_ALIGNED", 5, 12,
   "Protect the manager and the organization while keeping the tension "
   "real.",
   "Statement.",
   [dict(name="NEW_V5_FS_02_NOT_ALIGNED", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the trap",
             "Your value to the current role and your value to your future "
             "are not always aligned.",
             support="That does not mean anyone is plotting against you.",
             dark=True, size=58))],
   hold="Hold through the sentence. The line that protects the manager is "
        "on the card, not only on camera.",
   sound="One restrained accent."),

 F("NEW_V5_FS_03_WATCH_FOR_PATTERNS", 5, 14,
   "The pattern, as the script lists it, with the limit attached.",
   "Short rows, all visible, with the one-moment limit on the card.",
   [dict(name="NEW_V5_FS_03_WATCH_FOR_PATTERNS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what it looks like", "",
             [("More rescue work", ""), ("More knowledge transfer", ""),
              ("More dependence on you", ""),
              ("But no new decision room", ""),
              ("No developmental assignment", ""),
              ("No conversation about what comes next", "")],
             foot="one moment does not prove anything. a pattern does."))],
   svg=True,
   hold="Cut on 'Watch for patterns.' and hold through the list and the two "
        "lines that close it.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V5_FS_04_THE_QUESTION", 5, 25,
   "The question the video wants the viewer to hold, in full.",
   "Statement.",
   [dict(name="NEW_V5_FS_04_THE_QUESTION", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "ask",
             "What is this organization building in me beyond my ability to "
             "keep this role running?", size=58))],
   hold="Hold through the two sentences that follow, which protect the "
        "employer.",
   sound="One restrained accent."),

 F("NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE", 5, 35,
   "The cost of depth in one system, stated without judgment.",
   "Two sides of the same fact.",
   [dict(name="NEW_V5_FS_05_INDISPENSABLE_AND_LESS_PORTABLE",
         reveal="Single state.",
         draw=lambda c: L.twopart(
             c, "story", "At the same time.",
             ("more indispensable", "Fewer people can operate without you."),
             ("less portable", "Your experience becomes tied to the "
                               "internal system."), joiner="+"))],
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V5_FS_06_ASK_FOR_DEVELOPMENT", 5, 37,
   "What to ask for, in the script's own list.",
   "Short rows, all visible.",
   [dict(name="NEW_V5_FS_06_ASK_FOR_DEVELOPMENT", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what to ask for", "Not only a promotion.",
             [("A new decision", ""), ("A new problem", ""),
              ("A project outside your usual lane", ""),
              ("Exposure to a different leader", ""),
              ("Evidence beyond rescue work", "")]))],
   svg=True, sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V5_FS_07_THE_ANSWER_MAY_BE_NO", 5, 46,
   "Keep the boundary visible: the video does not promise the ask works.",
   "Short rows, all visible.",
   [dict(name="NEW_V5_FS_07_THE_ANSWER_MAY_BE_NO", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "boundary", "The answer may still be no.",
             [("There may be no budget", ""), ("No opening", ""),
              ("A manager may need you where you are", ""),
              ("Bias may shape who gets opportunities", ""),
              ("The company may not have the path you need", "")],
             foot="that is information too", dark=True))],
   sound="No accent.", treatment="SEQUENCE"),

 F("NEW_V5_FS_08_DEPENDENCE_VS_DEVELOPMENT", 5, 60,
   "The central distinction of the video, in the two sentences the script "
   "uses to voice it.",
   "Side-by-side contrast, quoting both.",
   [dict(name="NEW_V5_FS_08_DEPENDENCE_VS_DEVELOPMENT",
         reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the difference", "",
             ("dependence sounds like",
              "We cannot do this without you.", []),
             ("development sounds like",
              "Here is something you have not done before. We want you to "
              "learn it.", []),
             foot="sometimes the same assignment contains both"))],
   svg=True,
   hold="Cut on 'Dependence sounds like:' and hold through both quotations "
        "and the line that says an assignment can contain both.",
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V5_FS_09_REVIEW_POINT", 5, 71,
   "The practical instrument: what to ask at a review point.",
   "Questions card.",
   [dict(name="NEW_V5_FS_09_REVIEW_POINT", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "at the review point", "",
             ["What became permanent?", "What did I learn?",
              "What authority changed?",
              "What recognition or role design follows?"], dark=True,
             size=54))],
   hold="Cut on 'At that review, ask:' and hold through the four questions.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V5_FS_10_CTA", 5, 78,
   "The closing question, which is the ask.",
   "Action card.",
   [dict(name="NEW_V5_FS_10_CTA", reveal="Single state.",
         draw=lambda c: L.action(
             c, "one question to ask", "Is it also helping you become:",
             ["More capable.", "More visible.", "More portable."],
             resource=("If not, usefulness may be the reason you are stuck.",
                       "")))],
   hold="Cut on the question and hold to the end of the spoken line.",
   sound="One accent.", treatment="CTA"),
 WN(5),
]


# ============================ NEW V6  (former V22)  decode a job description
# The former V22 package is available and its visual architecture is reused
# where the sprint script still teaches the same thing. Where the sprint
# script differs, the sprint script controls. The 10-minute promise is
# protected: no spoken material is added and no card invites one.
HCSC1 = "Sr Divisional Strategy Consultant, Governance"
XAI = "Member of Technical Staff, Governance Risk Compliance"
CAPTURED = "captured september 12, 2026"
HROWS = [("Role purpose", "Tracking strategic opportunities"),
         ("The verb", "Supporting the development of divisional strategies"),
         ("Qualifications", "Business analytics. Microsoft Access.")]
HPOINTS = [("Problem", "A consistent way to evaluate opportunities, track "
                       "them, and report on them."),
           ("Authority", "Supporting the development of strategies. Not "
                         "setting them."),
           ("Proof", "Access is unusually specific. The role may be far more "
                     "hands-on than the title suggests.")]
POSTURES = [("Leads", "Authorization work"), ("Advises", "Leadership"),
            ("Coordinates", "Across teams"),
            ("Operates as", "A subject-matter expert")]


def _hot(i):
    return lambda c: L.hotspot_artifact(c, "posting one", HCSC1, HROWS,
                                        HPOINTS, active=i, source=CAPTURED)


def _post(a):
    return lambda c: L.sequence(c, "posting five",
                                "What the person was expected to do.",
                                POSTURES, active=a)


V6 = [
 F("NEW_V6_FS_01_TITLE_ONLY", 6, 0,
   "Let the title sit alone long enough for the viewer to form an assumption "
   "before anything contradicts it.",
   "Artifact. Nothing else on screen.",
   [dict(name="NEW_V6_FS_01_TITLE_ONLY", reveal="Single state. No build.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Employer", "Large Health Insurer"),
              ("Location", "Chicago, Illinois. Remote.")],
             source=CAPTURED, head_size=72))],
   cls=ANON,
   hold="Hold four to five seconds on the title alone. Do not reveal the "
        "range yet.",
   sound="One restrained reveal accent, then nothing.",
   source="A1. HCSC, requisition R0055598. Card reused unchanged from the "
          "former V22 package.", treatment="ARTIFACT"),

 F("NEW_V6_FS_02_THE_CONTRADICTION", 6, 3,
   "Break the assumption the title created, in two beats rather than one.",
   "Same artifact, two preserved lines, one active at a time.",
   [dict(name="NEW_V6_FS_02A_FLOOR",
         reveal="State A on the published range clause.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=0, source=CAPTURED)),
    dict(name="NEW_V6_FS_02B_FEEDBACK",
         reveal="State B on the required-qualifications clause of the same "
                "sentence.",
         draw=lambda c: L.artifact(
             c, "posting one", HCSC1,
             [("Published range", "$61,500 to $136,100"),
              ("Required qualifications",
               "The ability to accept direction and feedback")],
             active=1, source=CAPTURED))],
   cls=REUSE,
   hold="Both states sit inside one spoken sentence. Return to camera on "
        "'That is why I do not start with the title anymore.'",
   sound="One accent on A, one quieter on B.",
   source="A1. Preserved text. Cards reused unchanged from the former V22 "
          "package.", treatment="ARTIFACT"),

 F("NEW_V6_FS_03_THE_SAMPLE", 6, 6,
   "Put the denominator on screen the moment it is spoken.",
   "One figure held large with its own limit underneath.",
   [dict(name="NEW_V6_FS_03_THE_SAMPLE", reveal="Single state.",
         draw=lambda c: L.stat(
             c, "the evidence", "15", "POSTINGS. 11 EMPLOYERS.",
             support="Read for this research. A bounded sample, not the "
                     "labor market."))],
   cls=REUSE, sound="One accent.",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_05_PARP", 6, 8,
   "Name the method once, in the four words the script uses.",
   "Framework, established whole and left whole.",
   [dict(name="NEW_V6_FS_05_PARP_FRAMEWORK",
         reveal="Single state. Each of the four is taught by its own "
                "section, so nothing is activated here.",
         draw=lambda c: L.framework(
             c, "the method", "The four things.",
             [("Problem", ""), ("Authority", ""), ("Proof", ""),
              ("Real gap", "")]))],
   cls=REUSE, svg=True, sound="One accent.", treatment="SEQUENCE",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_04_THREE_QUESTIONS", 6, 11,
   "Three questions the viewer carries through the video, arriving one at a "
   "time.",
   "Sequential reveal. Earlier questions stay but quiet.",
   [dict(name="NEW_V6_FS_04A_COULD_I_DO_IT", reveal="On 'Could I do this "
         "work?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=0)),
    dict(name="NEW_V6_FS_04B_CAN_I_PROVE_IT",
         reveal="On 'Can I prove relevant evidence?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=1)),
    dict(name="NEW_V6_FS_04C_DO_I_MEET_THE_GATES",
         reveal="On 'Do I meet the stated gates?'",
         draw=lambda c: L.questions(
             c, "what to look for", "Three different questions.",
             ["Could I do this work?", "Can I prove relevant evidence?",
              "Do I meet the stated gates?"], active=2,
             foot="those are not the same question"))],
   cls=REUSE, build="ARRIVE", sound="One quiet accent per reveal.",
   treatment="SEQUENCE",
   source="Cards reused unchanged from the former V22 package."),

 F("NEW_V6_FS_06_POSTING_WALKTHROUGH", 6, 15,
   "Run the method across one real posting, with the artifact large enough "
   "to read on a phone.",
   "Artifact with numbered teaching points, one active at a time.",
   [dict(name="NEW_V6_FS_06A_PROBLEM", reveal="Point 1 active.",
         draw=_hot(0)),
    dict(name="NEW_V6_FS_06B_AUTHORITY", reveal="Point 2 active.",
         draw=_hot(1)),
    dict(name="NEW_V6_FS_06C_PROOF", reveal="Point 3 active.",
         draw=_hot(2))],
   cls=REUSE, svg=True, build="ARRIVE",
   hold="The three states are spread across the PROBLEM, AUTHORITY and PROOF "
        "sections. Cut away to camera between them.",
   sound="One quiet accent per point.",
   source="A1. Cards reused unchanged from the former V22 package.",
   treatment="ARTIFACT"),

 F("NEW_V6_FS_08_READ_THE_VERBS", 6, 18,
   "Fix the second step in the viewer's memory.",
   "Rule card.",
   [dict(name="NEW_V6_FS_08_READ_THE_VERBS", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule one", "Rule one", "Read the verbs.",
             support="This is where job descriptions become much more "
                     "honest."))],
   cls=REUSE, sound="One restrained accent.",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_09_PREDEFINED_DECISIONS", 6, 25,
   "Show that the same employer writes a senior role in bounded-decision "
   "language, without mocking the role.",
   "Artifact, establish then activate the requirement line.",
   [dict(name="NEW_V6_FS_09A_SAME_COMPANY", reveal="Establish.",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Large Health Insurer"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             source=CAPTURED)),
    dict(name="NEW_V6_FS_09B_PREDEFINED",
         reveal="Activate the requirement line on the sentence that quotes "
                "it.",
         draw=lambda c: L.artifact(
             c, "posting two", "Director of Enterprise Resilience",
             [("Same employer, different department",
               "Large Health Insurer"),
              ("Published range", "$133,400 to $247,700"),
              ("Requirement", "Work with executive leadership to make quick "
                              "decisions based on predefined decisions")],
             active=2, source=CAPTURED))],
   cls=ANON,
   hold="The defense of the role is delivered on camera, not on a card.",
   sound="One accent on A, one on B.",
   source="A2. Claim limit: the posting establishes predefined decisions. It "
          "does not establish who created them. Cards reused unchanged from "
          "the former V22 package.", treatment="ARTIFACT"),

 F("NEW_V6_FS_17_REAL_GAP", 6, 43,
   "Show that a real gap is not always a skill gap, using the one posting "
   "that said so outright.",
   "Two stated constraints, the second added when it is spoken.",
   [dict(name="NEW_V6_FS_17A_GEOGRAPHIC", reveal="The geographic boundary.",
         draw=lambda c: L.lines(
             c, "posting six", "A real gap is not always a skill gap.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=0, foot=CAPTURED)),
    dict(name="NEW_V6_FS_17B_TIME_ZONE",
         reveal="The overlap requirement becomes active.",
         draw=lambda c: L.lines(
             c, "posting six", "A real gap is not always a skill gap.",
             [("Stated in the posting",
               "Recruiting experience exclusively in one geographic context "
               "is unlikely to be a strong fit"),
              ("Stated in the posting",
               "At least three hours of overlap with East Africa Time")],
             active=1, foot="an operating constraint, not a skill gap"))],
   cls=REUSE,
   sound="One accent on each.",
   source="A6. GiveDirectly, named on camera, past tense as spoken. No local "
          "meeting time is stated or implied. Cards reused unchanged from "
          "the former V22 package.", treatment="COMPARISON"),

 F("NEW_V6_FS_10_DIRECTOR_COMPARE", 6, 50,
   "Two roles that share a level word, read side by side.",
   "Side-by-side comparison, scope revealed second.",
   [dict(name="NEW_V6_FS_10A_SAME_WORD", reveal="Establish.",
         draw=lambda c: L.compare(
             c, "two director roles", "Two different industries.",
             ("posting three", "Director, Talent Management",
              [("Employer", "Marketing Technology Company"),
               ("Experience minimum", "5 to 7 years")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Employer", "Insurance Brokerage"),
               ("Experience minimum", "5 or more years")]),
             foot=CAPTURED)),
    dict(name="NEW_V6_FS_10B_SCOPE", reveal="Add scope and reporting.",
         draw=lambda c: L.compare(
             c, "two director roles", "Two different industries.",
             ("posting three", "Director, Talent Management",
              [("Focus", "Operational execution"),
               ("Reports to", "A Senior Director")]),
             ("posting four", "Director of Strategic Initiatives",
              [("Focus", "Runs a transformation office"),
               ("Partners with", "A Chief Transformation Officer")]),
             foot=CAPTURED))],
   cls=ANON, svg=True,
   sound="One accent on establish. Nothing on B.",
   source="A3 and A4. No compensation comparison: the script draws none. "
          "Cards reused unchanged from the former V22 package.",
   treatment="COMPARISON"),

 F("NEW_V6_FS_12_TITLE_TEST", 6, 55,
   "Land the section in the four beats the script speaks.",
   "Four short lines, arriving one at a time.",
   [dict(name="NEW_V6_FS_12A_SAME_WORD", reveal="On 'Same broad level "
         "word.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=0)),
    dict(name="NEW_V6_FS_12B_DIFFERENT_WORK", reveal="On 'Different work.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=1)),
    dict(name="NEW_V6_FS_12C_DIFFERENT_AUTHORITY",
         reveal="On 'Different authority.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=2)),
    dict(name="NEW_V6_FS_12D_DIFFERENT_CONTEXT",
         reveal="On 'Different context.'",
         draw=lambda c: L.questions(
             c, "the title test", "",
             ["Same broad level word.", "Different work.",
              "Different authority.", "Different context."], active=3,
             foot="a title can help you find a posting"))],
   cls=REUSE, build="ARRIVE", sound="One quiet accent per line.",
   treatment="SEQUENCE",
   source="Cards reused unchanged from the former V22 package."),

 F("NEW_V6_FS_13_ACRONYM_WALL", 6, 62,
   "Let the unfamiliar title and the density of the language register.",
   "Artifact, then the captured acronym line at full size.",
   [dict(name="NEW_V6_FS_13A_UNFAMILIAR_TITLE", reveal="Title alone.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI,
             [("Employer", "AI Company"),
              ("Location", "Palo Alto, California and Washington, DC")],
             source=CAPTURED, head_size=66)),
    dict(name="NEW_V6_FS_13B_ACRONYM_WALL",
         reveal="Add the acronym line, as captured and unedited.",
         draw=lambda c: L.artifact(
             c, "posting five", XAI,
             [("Employer", "AI Company"),
              ("In the description", "FedRAMP.  ATO.  POAM.  3PAO.  STIG.")],
             active=1, source=CAPTURED, head_size=66, body_size=52))],
   cls=ANON, sound="One accent on B only.",
   source="A5. Cards reused unchanged from the former V22 package.",
   treatment="ARTIFACT"),

 F("NEW_V6_FS_14_AUTHORITY_POSTURES", 6, 65,
   "Four things the posting says the person does, one at a time.",
   "Numbered sequence, established whole, then activated one at a time.",
   [dict(name="NEW_V6_FS_14_AUTHORITY_POSTURES", reveal="Establish.",
         draw=_post(None)),
    dict(name="NEW_V6_FS_14A_LEADS", reveal="Activate 1.", draw=_post(0)),
    dict(name="NEW_V6_FS_14B_ADVISES", reveal="Activate 2.", draw=_post(1)),
    dict(name="NEW_V6_FS_14C_COORDINATES", reveal="Activate 3.",
         draw=_post(2)),
    dict(name="NEW_V6_FS_14D_SUBJECT_MATTER_EXPERT", reveal="Activate 4.",
         draw=_post(3))],
   cls=REUSE, svg=True, build="ESTABLISH",
   hold="One activation per clause inside the one spoken sentence.",
   sound="No accents on the activations.",
   source="A5. Cards reused unchanged from the former V22 package.",
   treatment="SEQUENCE"),

 F("NEW_V6_FS_15_CEILING", 6, 66,
   "Hold the salary reveal to the end of the beat, with the sample boundary "
   "attached.",
   "One figure, then the claim with its limit on the same card.",
   [dict(name="NEW_V6_FS_15A_RANGE", reveal="The published range, alone.",
         draw=lambda c: L.stat(
             c, "posting five", "$180,000 to $440,000", "THE PUBLISHED RANGE",
             size=124,
             support="The range on this posting, revealed after the four "
                     "postures.")),
    dict(name="NEW_V6_FS_15B_IN_THE_SAMPLE",
         reveal="The claim, with 'in the sample' on screen.",
         draw=lambda c: L.stat(
             c, "posting five", "$440,000",
             "HIGHEST PUBLISHED CEILING IN THE SAMPLE",
             support="Of the 15 postings read for this research. Not a claim "
                     "about the market."))],
   cls=REUSE, sound="One accent on A, one on B.",
   source="A5. Claim bounded to the 15-posting sample. Cards reused "
          "unchanged from the former V22 package."),

 F("NEW_V6_FS_16_READ_THE_WORK", 6, 68,
   "The second rule, paired visually with the first.",
   "Rule card.",
   [dict(name="NEW_V6_FS_16_READ_THE_WORK", reveal="Single state.",
         draw=lambda c: L.rule_card(
             c, "rule two", "Rule two",
             "If a title confuses you, do not automatically skip the job.",
             support="Read the work."))],
   cls=REUSE, sound="One restrained accent.",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_18_WHAT_IT_WILL_NOT_DO", 6, 70,
   "Put the limits of the method on screen in the same weight as the method.",
   "Six short lines, all visible.",
   [dict(name="NEW_V6_FS_18_WHAT_IT_WILL_NOT_DO", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "the boundary", "What this method will not tell you.",
             [("Who will get hired", ""),
              ("Whether the authority on paper exists in practice", ""),
              ("Whether a manager would flex on a requirement", ""),
              ("Whether bias will shape the decision", ""),
              ("Whether the team culture matches the posting", ""),
              ("That reading better guarantees a better outcome", "")],
             dark=True))],
   cls=REUSE, sound="No accent.",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_19_FOUR_THINGS", 6, 76,
   "Close on the recurring audit, in the script's own four phrases.",
   "Framework, established whole and left whole.",
   [dict(name="NEW_V6_FS_19_FOUR_THINGS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what you get", "A cleaner read on four things.",
             [("What may travel", ""), ("What may not", ""),
              ("What you can prove", ""),
              ("What you would still need to learn", "")]))],
   cls=REUSE, svg=True, sound="One accent.", treatment="SEQUENCE",
   source="Card reused unchanged from the former V22 package."),

 F("NEW_V6_FS_20_CTA", 6, 79,
   "One ask. No product, no comment ask, nothing stacked, and no second "
   "spoken CTA.",
   "Action card. The verb instruction is added last.",
   [dict(name="NEW_V6_FS_20A_WRITE_FOUR_LINES", reveal="The four lines.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap."])),
    dict(name="NEW_V6_FS_20B_STRONGEST_VERB",
         reveal="Add the closing instruction.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one job description.",
             ["Problem.", "Authority.", "Proof.", "Real gap."],
             resource=("Then find the strongest verb in the posting.", "")))],
   cls=REUSE, sound="One accent on A, one on B.", treatment="CTA",
   source="Cards reused unchanged from the former V22 package."),
 WN(6),
]


# ================================== NEW V7  (former V24)  the bigger role
V7_FOUR = [("Visible proof", "Has this person already handled something that "
                             "looks like part of the next role?"),
           ("Judgment", "When there was no clear answer, did they make a "
                        "sound call?"),
           ("Trust", "Will they surface a problem early and tell the truth "
                     "when the news is bad?"),
           ("Sponsorship and access", "Is someone in the room able and "
                                      "willing to say, give them the shot?")]


def _v7four(a):
    return lambda c: L.framework(
        c, "four things that tend to matter", "",
        V7_FOUR, active=a,
        foot="not a guaranteed formula. a way to read what may be happening.")


V7 = [
 F("NEW_V7_FS_01_NOT_ALWAYS_WHO_WORKED_HARDER", 7, 4,
   "Name the observation the video is built on, without yet explaining it.",
   "Statement.",
   [dict(name="NEW_V7_FS_01_NOT_ALWAYS_WHO_WORKED_HARDER",
         reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the hook",
             "The difference was not always who worked harder.",
             dark=True, size=72))],
   hold="Cut on the sentence. The scene before it stays on camera.",
   sound="One restrained accent."),

 F("NEW_V7_FS_02_TWO_QUESTIONS", 7, 10,
   "Separate the two questions a room is actually asking, which is the "
   "distinction the whole video rests on.",
   "Side-by-side contrast, quoting both.",
   [dict(name="NEW_V7_FS_02_TWO_QUESTIONS", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "in the room", "Those are different questions.",
             ("they are not only asking", "Who is good?", []),
             ("they are asking", "Who do I trust at this level?", []),
             divider=""))],
   hold="Cut on 'At that point, people are not only asking' and hold through "
        "'Those are different questions.'",
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V7_FS_03_USEFUL_NOT_PICTURED", 7, 17,
   "The trap for dependable people, in the script's own sentence.",
   "Statement.",
   [dict(name="NEW_V7_FS_03_USEFUL_NOT_PICTURED", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "what people usually do",
             "You can become more useful without becoming easier to picture "
             "at the next level.", size=60))],
   sound="One restrained accent."),

 F("NEW_V7_FS_04_FOUR_THINGS", 7, 18,
   "Establish the four, then take them one at a time, with the limit on the "
   "card from the first frame so it never reads as a formula.",
   "Framework established whole, then activated one component at a time.",
   [dict(name="NEW_V7_FS_04_FOUR_THINGS",
         reveal="Establish on 'four things tend to matter.'",
         draw=_v7four(None)),
    dict(name="NEW_V7_FS_04A_VISIBLE_PROOF",
         reveal="Activate 1 on 'First: visible proof.'", draw=_v7four(0)),
    dict(name="NEW_V7_FS_04B_JUDGMENT",
         reveal="Activate 2 on 'Second: judgment.'", draw=_v7four(1)),
    dict(name="NEW_V7_FS_04C_TRUST",
         reveal="Activate 3 on 'Third: trust.'", draw=_v7four(2)),
    dict(name="NEW_V7_FS_04D_SPONSORSHIP",
         reveal="Activate 4 on 'Fourth: sponsorship and access.'",
         draw=_v7four(3))],
   svg=True, build="ESTABLISH",
   hold="One activation per spoken item. Hold the fourth through the lines "
        "about bias, relationships and manager support.",
   sound="One accent on establish. None on the activations.",
   treatment="SEQUENCE"),

 F("NEW_V7_FS_05_NOT_MERIT", 7, 32,
   "Keep the boundary visible: advancement is not reduced to merit, and the "
   "card says so in the script's own list.",
   "Short rows, all visible.",
   [dict(name="NEW_V7_FS_05_NOT_MERIT", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "careers do not happen in a vacuum", "",
             [("Bias matters", ""), ("Relationships matter", ""),
              ("Manager support matters", ""),
              ("Who gets access to developmental work matters", "")],
             foot="so i do not want to reduce this to merit", dark=True))],
   hold="Hold through the list and the sentence that refuses to reduce this "
        "to merit.",
   sound="No accent.", treatment="SEQUENCE"),

 F("NEW_V7_FS_06_EVIDENCE_FOR_WHICH_ROLE", 7, 39,
   "The precise reason dependable work does not read as readiness.",
   "Statement.",
   [dict(name="NEW_V7_FS_06_EVIDENCE_FOR_WHICH_ROLE",
         reveal="Single state.",
         draw=lambda c: L.statement(
             c, "visible proof",
             "The evidence people see may be evidence for the role you "
             "already have.",
             support="The problem is not that you have done nothing.",
             size=58))],
   hold="Cut on the sentence and hold through it. The line protecting the "
        "viewer's work is on the card.",
   sound="One restrained accent."),

 F("NEW_V7_FS_07_ASK_WHAT_KIND", 7, 42,
   "What to ask for instead of more responsibility.",
   "Questions card.",
   [dict(name="NEW_V7_FS_07_ASK_WHAT_KIND", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "ask what kind", "",
             ["What decisions will I get to make?",
              "What level of stakeholder will I work with?",
              "What problem will I own end to end?"], dark=True, size=52))],
   hold="Cut on 'Ask what kind.' and hold through the three questions.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V7_FS_08_CHANGES_THE_CONVERSATION", 7, 43,
   "Show the shift the question produces, in the script's own two lines.",
   "Side-by-side contrast, quoting both.",
   [dict(name="NEW_V7_FS_08_CHANGES_THE_CONVERSATION",
         reveal="Single state.",
         draw=lambda c: L.compare(
             c, "that changes the conversation", "",
             ("from", "Can I help more?", []),
             ("to", "What would let me practice the next level of work?",
              []), divider=""))],
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V7_FS_09_THE_BOUNDARY", 7, 55,
   "Name what the organization may simply not give, so the video cannot be "
   "read as work-harder advice.",
   "Short rows, all visible.",
   [dict(name="NEW_V7_FS_09_THE_BOUNDARY", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "organizations are not clean systems", "",
             [("Politics", ""), ("Bias", ""), ("Favoritism", ""),
              ("Timing", ""), ("Budget and headcount limits", ""),
              ("A manager who does not advocate", "")],
             foot="you need to know that too", dark=True))],
   svg=True, sound="No accent.", treatment="SEQUENCE"),

 F("NEW_V7_FS_10_SEPARATE_THREE_THINGS", 7, 58,
   "The separation the whole boundary section exists to produce.",
   "Three short rows, all visible.",
   [dict(name="NEW_V7_FS_10_SEPARATE_THREE_THINGS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "separate", "",
             [("What you can build", ""), ("What you can ask for", ""),
              ("What the organization may not be willing to give you", "")]))],
   hold="Cut on 'It is to separate:' and hold through the three lines.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V7_FS_11_READ_YOUR_OWN_SITUATION", 7, 62,
   "The instrument: four questions against the last three times the viewer "
   "was trusted with something bigger.",
   "Questions card.",
   [dict(name="NEW_V7_FS_11_READ_YOUR_OWN_SITUATION",
         reveal="Single state.",
         draw=lambda c: L.questions(
             c, "for each one, ask", "",
             ["What problem was I trusted with?",
              "What decision was mine?", "Who saw me handle it?",
              "What changed because of it?"], dark=True, size=54))],
   hold="Cut on 'For each one, ask:' and hold through the four questions.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V7_FS_12_THE_MISSING_LINE", 7, 64,
   "Name the diagnostic the exercise produces.",
   "Statement.",
   [dict(name="NEW_V7_FS_12_THE_MISSING_LINE", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "now look", "Now look for the missing line.",
             support="Strong proof nobody senior has seen. Trusted "
                     "execution but not judgment. Judgment inside one narrow "
                     "context.", size=66))],
   hold="Hold through the four 'maybe' lines that follow.",
   sound="One restrained accent."),

 F("NEW_V7_FS_13_CTA", 7, 77,
   "The closing ask, in the three questions the script speaks.",
   "Action card.",
   [dict(name="NEW_V7_FS_13_CTA", reveal="Single state.",
         draw=lambda c: L.action(
             c, "one thing to ask", "Ask:",
             ["What proof of the next level is visible?",
              "What judgment have I already been allowed to practice?",
              "Who has seen it?"],
             resource=("Sometimes the answer tells you what to build. "
                       "Sometimes what to negotiate.", "")))],
   hold="Cut on 'Ask:' and hold to the end of the spoken line.",
   sound="One accent.", treatment="CTA"),
 WN(7),
]


# ============================== NEW V8  (former V28)  when access ends
V8_FIVE = [("The baseline", "What was true before you started"),
           ("The scope", "How many people, teams, customers, locations or "
                         "systems were involved"),
           ("The decision", "What was actually yours to choose"),
           ("The result", "What changed"),
           ("The mechanism", "How you know the result was real")]


def _v8five(a):
    return lambda c: L.framework(c, "five kinds of evidence", "", V8_FIVE,
                                 active=a)


V8 = [
 F("NEW_V8_FS_01_MEMORY_NOT_PROOF", 8, 8,
   "Name the loss precisely: the memory survives and the proof does not.",
   "Statement.",
   [dict(name="NEW_V8_FS_01_MEMORY_NOT_PROOF", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the hook", "You just cannot prove it cleanly.",
             support="You remember that it mattered.", dark=True, size=76))],
   hold="Cut on the sentence. The list of what is gone stays on camera.",
   sound="One restrained accent."),

 F("NEW_V8_FS_02_FIVE_KINDS", 8, 13,
   "Establish the five kinds of evidence, then take them one at a time so "
   "each is heard as a separate thing to record.",
   "Framework established whole, then activated one at a time.",
   [dict(name="NEW_V8_FS_02_FIVE_KINDS",
         reveal="Establish on 'you can lose five kinds of evidence.'",
         draw=_v8five(None)),
    dict(name="NEW_V8_FS_02A_BASELINE", reveal="Activate 1.",
         draw=_v8five(0)),
    dict(name="NEW_V8_FS_02B_SCOPE", reveal="Activate 2.", draw=_v8five(1)),
    dict(name="NEW_V8_FS_02C_DECISION", reveal="Activate 3.",
         draw=_v8five(2)),
    dict(name="NEW_V8_FS_02D_RESULT", reveal="Activate 4.", draw=_v8five(3)),
    dict(name="NEW_V8_FS_02E_MECHANISM", reveal="Activate 5.",
         draw=_v8five(4))],
   svg=True, build="ESTABLISH",
   hold="One activation per spoken pair. Hold the fifth through 'the details "
        "that turn a memory into proof.'",
   sound="One accent on establish. None on the activations.",
   treatment="SEQUENCE"),

 F("NEW_V8_FS_03_KEEP_THE_PROOF", 8, 26,
   "The ethical rule of the video, given the screen the moment it is spoken.",
   "Statement. The rule stays available to the editor for any later beat.",
   [dict(name="NEW_V8_FS_03_KEEP_THE_PROOF", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the important boundary",
             "Keep the proof. Not the property.",
             support="Keeping proof does not mean taking company property.",
             dark=True, size=82))],
   hold="Cut on the sentence and hold through the list of what not to take. "
        "Nothing on screen depicts taking anything.",
   sound="One restrained accent.",
   source="Ethical boundary. No card in this package depicts a file, a "
          "screenshot, a download or any circumvention of access control."),

 F("NEW_V8_FS_04_NOT_THE_ARTIFACT", 8, 30,
   "State what the habit is for, so the rule is not only a prohibition.",
   "Side-by-side contrast.",
   [dict(name="NEW_V8_FS_04_NOT_THE_ARTIFACT", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "the goal", "",
             ("not", "Keeping the artifact.", []),
             ("but", "Keeping a lawful record of your own work.", []),
             divider=""))],
   sound="One accent.", treatment="COMPARISON",
   source="Lawful-record framing, in the script's own words."),

 F("NEW_V8_FS_05_IN_YOUR_OWN_WORDS", 8, 33,
   "Show what a lawful record looks like, using the script's own examples "
   "and nothing resembling an employer system.",
   "Reconstructed examples as plain lines. No interface, no screenshot.",
   [dict(name="NEW_V8_FS_05_IN_YOUR_OWN_WORDS", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what to capture", "In your own words.",
             [("Reduced onboarding time from X to Y over six months", ""),
              ("Built the first process for X", ""),
              ("Owned the decision on Y, but budget approval remained with "
               "Z", ""),
              ("Presented the recommendation to X level", ""),
              ("Measured the result using Y", "")],
             foot="the shape of the evidence, not the company's files"))],
   svg=True,
   hold="Cut on 'For example:' and hold through the five lines.",
   sound="One accent.", treatment="SEQUENCE",
   source="Reconstructed examples with placeholders, exactly as the script "
          "speaks them. No real or fabricated employer record appears."),

 F("NEW_V8_FS_06_THE_DETAILS_BLUR", 8, 46,
   "Show how fast the detail goes, using the script's own three questions.",
   "Questions card.",
   [dict(name="NEW_V8_FS_06_THE_DETAILS_BLUR", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "three months later", "",
             ["Was the starting number 47 or 52?",
              "Was the result measured at 12 months or 18?",
              "Did you own the design or only the rollout?"], dark=True,
             size=52))],
   hold="Cut on 'Three months later, the details blur.' and hold through the "
        "three questions.",
   sound="One accent.", treatment="SEQUENCE",
   source="The numbers are the script's own illustration of forgetting, not "
          "a claim about a real project."),

 F("NEW_V8_FS_07_TEN_MINUTE_HABIT", 8, 51,
   "The habit, as five questions the viewer can answer in ten minutes.",
   "Questions card.",
   [dict(name="NEW_V8_FS_07_TEN_MINUTE_HABIT", reveal="Single state.",
         draw=lambda c: L.questions(
             c, "once a month, ten minutes", "",
             ["What changed?", "What was mine?", "What was hard?",
              "What evidence do I have?",
              "What would I be allowed to say outside the company?"],
             dark=True, size=48))],
   hold="Cut on 'take ten minutes and write down:' and hold through the "
        "sentence about the last question.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V8_FS_08_CAREER_HYGIENE", 8, 58,
   "Move the habit out of the layoff frame, which is what keeps the video "
   "from reading as a job-loss prediction.",
   "Statement.",
   [dict(name="NEW_V8_FS_08_CAREER_HYGIENE", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "when the exit is sudden",
             "This is not only a layoff task. It is a career hygiene task.",
             support="Keep your evidence while you are still employed.",
             size=62))],
   sound="One restrained accent."),

 F("NEW_V8_FS_09_STILL_NOT_ENOUGH", 8, 61,
   "Keep the boundary visible: good evidence does not remove every hiring "
   "problem.",
   "Statement.",
   [dict(name="NEW_V8_FS_09_STILL_NOT_ENOUGH", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "boundary",
             "Good evidence will not remove every hiring problem.",
             support="A future employer can still discount the experience, "
                     "or require a credential or direct domain experience.",
             dark=True, size=60))],
   sound="No accent."),

 F("NEW_V8_FS_10_NOT_ONLY_A_METRIC", 8, 68,
   "Widen what counts as evidence, so a viewer with no number still has a "
   "record to keep.",
   "Four short rows, all visible.",
   [dict(name="NEW_V8_FS_10_NOT_ONLY_A_METRIC", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "you can still record", "Evidence is not only a metric.",
             [("How the process worked before", ""),
              ("What you changed", ""),
              ("What you were trusted to decide", ""),
              ("What the organization did differently afterward", "")]))],
   svg=True,
   hold="Cut on 'You can still record:' and hold through the four lines.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V8_FS_11_A_FACTUAL_RECORD", 8, 75,
   "Answer the discomfort directly: this is a record, not self-promotion.",
   "Side-by-side contrast.",
   [dict(name="NEW_V8_FS_11_A_FACTUAL_RECORD", reveal="Single state.",
         draw=lambda c: L.compare(
             c, "why people wait", "",
             ("not", "An award nomination every month.", []),
             ("this", "A factual record.", []), divider=""))],
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V8_FS_12_CTA", 8, 85,
   "The closing rule, which is the ask.",
   "Action card.",
   [dict(name="NEW_V8_FS_12_CTA", reveal="Single state.",
         draw=lambda c: L.action(
             c, "one thing to do", "Keep the proof.",
             ["Not the property."],
             resource=("Once a month. Ten minutes. Before the login "
                       "disappears.", "")))],
   hold="Cut on 'Keep the proof.' and hold through 'Not the property.'",
   sound="One accent.", treatment="CTA"),
 WN(8),
]


# ========================= NEW V9  (former V27)  transferable skills audit
V9_AUDIT = [("What travels?", ""), ("What does not?", ""),
            ("What can I prove?", ""), ("What must I relearn?", "")]


def _v9audit(a):
    return lambda c: L.framework(c, "four questions instead", "", V9_AUDIT,
                                 active=a)


V9 = [
 F("NEW_V9_FS_01_INCOMPLETE_QUESTION", 9, 3,
   "State the argument precisely: the question is incomplete, not wrong. "
   "This is what keeps the video from reading as anti-transferability.",
   "Statement.",
   [dict(name="NEW_V9_FS_01_INCOMPLETE_QUESTION", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the hook", "The question is incomplete.",
             support="Not wrong. Incomplete.", dark=True, size=84))],
   hold="Cut on the sentence. The quoted question before it stays on camera.",
   sound="One restrained accent."),

 F("NEW_V9_FS_02_WHY_THE_ADVICE_HELPS", 9, 6,
   "Give transferable-skills advice its due before complicating it.",
   "Statement.",
   [dict(name="NEW_V9_FS_02_WHY_THE_ADVICE_HELPS", reveal="Single state.",
         draw=lambda c: L.statement(
             c, "the default",
             "Transferable skills advice stops experienced people from "
             "erasing themselves.", size=58))],
   hold="Hold through the sentence about talking as if ten years "
        "disappeared.",
   sound="One accent."),

 F("NEW_V9_FS_03_FOUR_QUESTIONS", 9, 11,
   "The audit at the centre of the video, established whole so no single "
   "question can stand for the set, then taken one at a time.",
   "Framework established whole, then activated one at a time.",
   [dict(name="NEW_V9_FS_03_FOUR_QUESTIONS",
         reveal="Establish on 'I use four questions instead.' All four stay "
                "on screen together.",
         draw=_v9audit(None)),
    dict(name="NEW_V9_FS_03A_WHAT_TRAVELS",
         reveal="Activate 1 at the WHAT TRAVELS section.", draw=_v9audit(0)),
    dict(name="NEW_V9_FS_03B_WHAT_DOES_NOT",
         reveal="Activate 2 at the WHAT DOES NOT section.",
         draw=_v9audit(1)),
    dict(name="NEW_V9_FS_03C_WHAT_CAN_I_PROVE",
         reveal="Activate 3 at the WHAT CAN I PROVE section.",
         draw=_v9audit(2)),
    dict(name="NEW_V9_FS_03D_WHAT_MUST_I_RELEARN",
         reveal="Activate 4 at the WHAT MUST I RELEARN section.",
         draw=_v9audit(3))],
   svg=True, build="ESTABLISH",
   hold="Establish on the four-questions paragraph and hold through 'That is "
        "a more honest read.' The four activations are cut at the head of "
        "each matching section, so all four questions are on screen together "
        "before any one of them is emphasized.",
   sound="One accent on establish. None on the activations.",
   treatment="SEQUENCE"),

 F("NEW_V9_FS_04_DEMONSTRATED_NOT_CLAIMED", 9, 22,
   "The test for the first column, in two words.",
   "Side-by-side contrast.",
   [dict(name="NEW_V9_FS_04_DEMONSTRATED_NOT_CLAIMED",
         reveal="Single state.",
         draw=lambda c: L.compare(
             c, "what travels", "The key word.",
             ("demonstrated", "Capability the next context can use.", []),
             ("not claimed", "A generic list of soft skills.", []),
             divider=""))],
   sound="One accent.", treatment="COMPARISON"),

 F("NEW_V9_FS_05_TIED_TO_THE_OLD_CONTEXT", 9, 24,
   "Name what does not travel, in the script's own list, without implying "
   "it was worthless.",
   "Short rows, all visible.",
   [dict(name="NEW_V9_FS_05_TIED_TO_THE_OLD_CONTEXT",
         reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what does not", "Tied to the old context.",
             [("Internal relationships", ""),
              ("Company-specific systems", ""),
              ("The language everyone understood without explanation", ""),
              ("Informal authority", ""),
              ("How that employer really gets things done", "")],
             foot="excellent where you are. less legible somewhere else."))],
   svg=True, sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V9_FS_06_WHAT_CAN_ANOTHER_PERSON_SEE", 9, 33,
   "The proof column, as the four questions the script speaks.",
   "Questions card.",
   [dict(name="NEW_V9_FS_06_WHAT_CAN_ANOTHER_PERSON_SEE",
         reveal="Single state.",
         draw=lambda c: L.questions(
             c, "what can i prove", "",
             ["What was broken?", "What did you decide?", "What changed?",
              "How do you know?"], dark=True, size=54))],
   hold="Hold through 'Experience becomes portable when another person can "
        "evaluate it.'",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V9_FS_07_WHAT_THE_NEW_CONTEXT_REQUIRES", 9, 37,
   "Name the real requirements without treating them as insults to the "
   "viewer's experience.",
   "Short rows, all visible.",
   [dict(name="NEW_V9_FS_07_WHAT_THE_NEW_CONTEXT_REQUIRES",
         reveal="Single state.",
         draw=lambda c: L.framework(
             c, "what must i relearn", "",
             [("Regulation", ""), ("Credentials", ""),
              ("Domain knowledge", ""), ("Customer knowledge", ""),
              ("Technical depth", ""), ("Local relationships", "")],
             foot="not insults to your experience. part of the move.",
             dark=True))],
   svg=True,
   hold="Hold through 'They are part of the move.'",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V9_FS_08_SORTING", 9, 41,
   "The image the script uses instead of a suitcase.",
   "Four short rows, all visible.",
   [dict(name="NEW_V9_FS_08_SORTING", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "i picture sorting", "",
             [("Some things come with you exactly as they are", ""),
              ("Some things need translating", ""),
              ("Some things were useful only because of where you were", ""),
              ("And some things have to be learned again", "")]))],
   hold="Cut on 'I picture sorting.' and hold through the four lines.",
   sound="One accent.", treatment="SEQUENCE"),

 F("NEW_V9_FS_09_FOUR_COLUMNS", 9, 49,
   "The application, as four columns the viewer can actually draw.",
   "Action card.",
   [dict(name="NEW_V9_FS_09_FOUR_COLUMNS", reveal="Single state.",
         draw=lambda c: L.action(
             c, "one thing to do", "Take one target role. Four columns.",
             ["Travels.", "Does not travel.", "Proof.", "Relearn."],
             resource=("Do not try to make every line land in the first "
                       "column. The goal is accuracy.", "")))],
   hold="Cut on 'Make four columns.' and hold through the three lines that "
        "read the result.",
   sound="One accent.", treatment="CTA"),

 F("NEW_V9_FS_10_BOUNDARY", 9, 58,
   "Keep every real gate visible, which is what the thumbnail's tension is "
   "resolved by.",
   "Short rows, all visible.",
   [dict(name="NEW_V9_FS_10_BOUNDARY", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "none of this disappears", "",
             [("An employer may prefer direct experience", ""),
              ("A credential may be non-negotiable", ""),
              ("Bias may affect how adjacent experience is read", ""),
              ("Compensation may reset", ""),
              ("The market may be crowded", "")],
             foot="you make a better decision when you know what you are "
                  "asking an employer to believe", dark=True))],
   sound="No accent.", treatment="SEQUENCE"),

 F("NEW_V9_FS_11_FLUENCY_AND_PORTABILITY", 9, 65,
   "The hardest idea in the video, and the reason it is aimed at "
   "experienced people.",
   "Statement.",
   [dict(name="NEW_V9_FS_11_FLUENCY_AND_PORTABILITY",
         reveal="Single state.",
         draw=lambda c: L.statement(
             c, "why this is harder for experienced people",
             "The longer you stay in one context, the easier it is to "
             "confuse fluency with portability.",
             support="The capability is still there. The shortcuts are not.",
             size=54))],
   hold="Hold through the lines about knowing who to call and which meeting "
        "matters.",
   sound="One restrained accent."),

 F("NEW_V9_FS_12_THE_AUDIT_AGAIN", 9, 85,
   "Close on the full audit, so the video resolves the tension its title "
   "created rather than leaving it.",
   "Framework, established whole and left whole.",
   [dict(name="NEW_V9_FS_12_THE_AUDIT_AGAIN", reveal="Single state.",
         draw=lambda c: L.framework(
             c, "ask", "", V9_AUDIT,
             foot="not starting from zero. not carrying everything "
                  "without checking."))],
   svg=True,
   hold="Cut on 'Ask:' and hold through the four questions and the closing "
        "sentence.",
   sound="One accent.", treatment="SEQUENCE"),
 WN(9),
]

SETS = {4: V4, 5: V5, 6: V6, 7: V7, 8: V8, 9: V9}


def states(n):
    return [(f, s) for f in SETS[n] for s in f["states"]]


if __name__ == "__main__":
    from collections import Counter
    for n in S.VIDEOS:
        fs = SETS[n]
        st = states(n)
        bad = [f["key"] for f in fs
               if f["trigger"] and not S.trigger_ok(n, f["trigger"])]
        lab = [f["key"] for f in fs
               if f["trigger"] and S._is_label(f["trigger"])]
        print("NEW V%d (former V%d)  %2d families  %2d states  %d svg"
              % (n, S.NUMBERS[n], len(fs), len(st),
                 sum(1 for f in fs if f["svg"])))
        print("    classes:  ", dict(Counter(f["cls"] for f in fs)))
        print("    triggers not unique:", bad or "none")
        print("    cues on a section label:", lab or "none")
