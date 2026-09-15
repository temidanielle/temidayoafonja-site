# -*- coding: utf-8 -*-
"""Full-screen assets for NEW PUBLIC V10 and V11.

The visual system is the approved house one: the same navy, cream and warm
gold, the same layouts, the same rules. Nothing here invents teaching to
justify a card. Every word on every card is the script's own wording, and
every cue is anchored to a whole spoken paragraph of its own script.

Both videos are camera-led: the camera keeps recognition, lived
interpretation, nuance, boundaries and consequential statements, and only
substantive frameworks, comparisons and multi-point teaching become true
full screen.

The per-video rules are honoured in the copy, not in a comment. V10 never
requires a theatrical quick win and never universalizes what a manager
evaluates. V11 never frames the employer or the manager as a villain, never
uses bait-and-switch as a blanket label, and keeps legitimate role evolution
and real personal constraints visible.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

import v1011 as S
import lay1011 as L

NEW = "NEW"
CAPTURED = None


def P(n, i):
    return S.paragraphs(n)[i]


def F(key, n, para, purpose, layout, states, svg=False, hold=None,
      sound=None, source=None, treatment="STATEMENT", build=None):
    return dict(key=key, video=n, trigger=P(n, para), para=para,
                mode="FULL SCREEN", purpose=purpose, layout=layout,
                states=states, svg=svg, cls=NEW,
                build=build or ("SINGLE" if len(states) == 1 else "BUILD"),
                hold=hold or "Hold until the sentence lands, then cut back.",
                sound=sound or "No accent.", source=source,
                treatment=treatment)


def WN(n):
    """The Watch Next end card. Full screen, final, and silent."""
    t = S.watch_next(n)
    return dict(key="NEW_V%d_WATCH_NEXT" % n, video=n, trigger=None,
                para=None, mode="FULL SCREEN", build="SINGLE", cls=NEW,
                svg=False, treatment="WATCH NEXT",
                purpose="The destination the script speaks. Full screen and "
                        "final: nothing returns to camera after it.",
                layout="Watch Next card, house layout.",
                hold="Cut here on the spoken Watch Next line and end the "
                     "video on it.",
                sound="No accent.",
                source="Intended destination, named on the script's final "
                       "full-screen card. Confirm it is publicly live "
                       "before upload.",
                states=[dict(name="NEW_V%d_WATCH_NEXT" % n,
                             reveal="Single state. Final card.",
                             draw=(lambda tt: (lambda c: L.watch_next(c, tt)))(
                                 t))])


# ===================================================================== V10
V10 = [
 F("NEW_V10_FS_01_READ_TEST_PROVE", 10, 6,
   "The framework arrives only after the pressure has landed on camera. "
   "Sequential, so the viewer meets one word at a time.",
   "Sequence, established whole then activated one line at a time.",
   [dict(name="NEW_V10_FS_01A_ESTABLISH", reveal="Establish all three.",
         draw=lambda c: L.sequence(
             c, "the first 90 days", "Three things to figure out.",
             [("READ", "What do I need to learn about this context?"),
              ("TEST", "What from my experience actually works here?"),
              ("PROVE", "What can I begin to prove in this environment?")],
             dark=True)),
    dict(name="NEW_V10_FS_01B_READ", reveal="Activate READ.",
         draw=lambda c: L.sequence(
             c, "the first 90 days", "Three things to figure out.",
             [("READ", "What do I need to learn about this context?"),
              ("TEST", "What from my experience actually works here?"),
              ("PROVE", "What can I begin to prove in this environment?")],
             active=0, dark=True)),
    dict(name="NEW_V10_FS_01C_TEST", reveal="Activate TEST.",
         draw=lambda c: L.sequence(
             c, "the first 90 days", "Three things to figure out.",
             [("READ", "What do I need to learn about this context?"),
              ("TEST", "What from my experience actually works here?"),
              ("PROVE", "What can I begin to prove in this environment?")],
             active=1, dark=True)),
    dict(name="NEW_V10_FS_01D_PROVE", reveal="Activate PROVE.",
         draw=lambda c: L.sequence(
             c, "the first 90 days", "Three things to figure out.",
             [("READ", "What do I need to learn about this context?"),
              ("TEST", "What from my experience actually works here?"),
              ("PROVE", "What can I begin to prove in this environment?")],
             active=2, dark=True))],
   svg=True, build="ESTABLISH", treatment="SEQUENCE",
   sound="One quiet accent per reveal. Four in total, not one per word.",
   hold="Hold the complete frame before the first activation.",
   source="Spoken: READ. TEST. PROVE. The three questions are the "
          "script's own, in the script's order."),

 F("NEW_V10_FS_02_EXPERIENCED_BUT_NEW", 10, 9,
   "The distinction the whole video rests on. It is a consequential "
   "statement, so it is stated plainly and alone.",
   "Statement. Nothing else on screen.",
   [dict(name="NEW_V10_FS_02_EXPERIENCED_BUT_NEW",
         reveal="Single state. No build.",
         draw=lambda c: L.statement(
             c, "two things at once",
             "You can be experienced and still be new to the context.",
             "Those two things can be true at the same time.", dark=True))],
   sound="One restrained accent.",
   hold="Hold four to five seconds. Let it sit before returning to camera.",
   source="Spoken, word for word."),

 F("NEW_V10_FS_03_READ_FOUR_THINGS", 10, 16,
   "The four things to pay attention to during READ, one at a time so the "
   "viewer can actually hold each one.",
   "Numbered sequence, established whole then activated one at a time.",
   [dict(name="NEW_V10_FS_03_ESTABLISH", reveal="Establish.",
         draw=lambda c: L.questions(
             c, "during read", "Pay attention to four things.",
             ["What is this team actually responsible for?",
              "Where do the important decisions sit?",
              "What does success mean here?",
              "What do people around me know that was never written in "
              "the job description?"])),
    dict(name="NEW_V10_FS_03A_RESPONSIBLE", reveal="Activate the first.",
         draw=lambda c: L.questions(
             c, "during read", "Pay attention to four things.",
             ["What is this team actually responsible for?",
              "Where do the important decisions sit?",
              "What does success mean here?",
              "What do people around me know that was never written in "
              "the job description?"], active=0)),
    dict(name="NEW_V10_FS_03B_DECISIONS", reveal="Activate the second.",
         draw=lambda c: L.questions(
             c, "during read", "Pay attention to four things.",
             ["What is this team actually responsible for?",
              "Where do the important decisions sit?",
              "What does success mean here?",
              "What do people around me know that was never written in "
              "the job description?"], active=1)),
    dict(name="NEW_V10_FS_03C_SUCCESS", reveal="Activate the third.",
         draw=lambda c: L.questions(
             c, "during read", "Pay attention to four things.",
             ["What is this team actually responsible for?",
              "Where do the important decisions sit?",
              "What does success mean here?",
              "What do people around me know that was never written in "
              "the job description?"], active=2)),
    dict(name="NEW_V10_FS_03D_UNWRITTEN", reveal="Activate the fourth.",
         draw=lambda c: L.questions(
             c, "during read", "Pay attention to four things.",
             ["What is this team actually responsible for?",
              "Where do the important decisions sit?",
              "What does success mean here?",
              "What do people around me know that was never written in "
              "the job description?"], active=3))],
   build="ESTABLISH", treatment="SEQUENCE",
   sound="One quiet accent per reveal.",
   source="Spoken, word for word, in the script's order."),

 F("NEW_V10_FS_04_FORMAL_VS_REAL", 10, 17,
   "The comparison the brief asks for: what the document says against what "
   "the first weeks show. Side by side so the difference is visible, not "
   "described.",
   "Side-by-side comparison. Two artifacts, read together.",
   [dict(name="NEW_V10_FS_04_FORMAL_VS_REAL",
         reveal="Single state. Both halves land together.",
         draw=lambda c: L.compare(
             c, "two versions of one job", "The formal job. The real one.",
             ("the formal job", "A job description",
              [("What it can tell you", "The role as written")]),
             ("the real job", "The first few weeks",
              [("What they start showing you", "The role as it works")]),
             foot="the first few weeks start showing you the real one."))],
   svg=True, treatment="COMPARISON", sound="One accent.",
   hold="Hold long enough to read both sides.",
   source="Spoken: a job description can tell you the formal job, the "
          "first few weeks start showing you the real one."),

 F("NEW_V10_FS_05_TWO_SENTENCES", 10, 20,
   "The difference between the two sentences is the whole lesson of this "
   "section, and it is easier to see than to hear.",
   "Two quoted sentences, side by side, the second activated.",
   [dict(name="NEW_V10_FS_05A_BOTH", reveal="Establish both.",
         draw=lambda c: L.compare(
             c, "two ways to bring experience in", "One assumes. One asks.",
             ("the first", "“At my old company, we did it this way.”",
              []),
             ("the second", "“I have seen a similar problem before. Can "
              "you help me understand what makes it different here?”",
              []))),
    dict(name="NEW_V10_FS_05B_SECOND", reveal="Activate the second.",
         draw=lambda c: L.compare(
             c, "two ways to bring experience in", "One assumes. One asks.",
             ("the first", "“At my old company, we did it this way.”",
              []),
             ("the second", "“I have seen a similar problem before. Can "
              "you help me understand what makes it different here?”",
              []),
             active="right",
             foot="brings your experience into the room without assuming "
                  "the room is the same."))],
   treatment="COMPARISON", sound="One accent on the second.",
   source="Both sentences are quoted from the script, word for word."),

 F("NEW_V10_FS_06_MANAGER_CONVERSATION", 10, 28,
   "The save-worthy card. These are the questions the viewer will pause "
   "and screenshot, so they are given room and no decoration.",
   "Questions card, established whole then activated one at a time.",
   [dict(name="NEW_V10_FS_06_ESTABLISH", reveal="Establish.",
         draw=lambda c: L.questions(
             c, "ask your manager", "Not “How am I doing?”",
             ["“What have you seen me pick up quickly?”",
              "“Where do I still need more context?”",
              "“Is there anything I am treating like my old "
              "environment that works differently here?”"])),
    dict(name="NEW_V10_FS_06A_PICK_UP", reveal="Activate the first.",
         draw=lambda c: L.questions(
             c, "ask your manager", "Not “How am I doing?”",
             ["“What have you seen me pick up quickly?”",
              "“Where do I still need more context?”",
              "“Is there anything I am treating like my old "
              "environment that works differently here?”"], active=0)),
    dict(name="NEW_V10_FS_06B_CONTEXT", reveal="Activate the second.",
         draw=lambda c: L.questions(
             c, "ask your manager", "Not “How am I doing?”",
             ["“What have you seen me pick up quickly?”",
              "“Where do I still need more context?”",
              "“Is there anything I am treating like my old "
              "environment that works differently here?”"], active=1)),
    dict(name="NEW_V10_FS_06C_OLD_ENVIRONMENT", reveal="Activate the third.",
         draw=lambda c: L.questions(
             c, "ask your manager", "Not “How am I doing?”",
             ["“What have you seen me pick up quickly?”",
              "“Where do I still need more context?”",
              "“Is there anything I am treating like my old "
              "environment that works differently here?”"], active=2))],
   svg=True, build="ESTABLISH", treatment="QUESTIONS",
   sound="One quiet accent per reveal.",
   hold="Hold the complete card long enough to screenshot.",
   source="All three questions are spoken, word for word."),

 F("NEW_V10_FS_07_THE_DAY_90_QUESTION", 10, 29,
   "The fourth question is the one that reframes the whole 90 days, so it "
   "gets its own card rather than a fourth line on the last one.",
   "Claim card. One question, at size.",
   [dict(name="NEW_V10_FS_07_THE_DAY_90_QUESTION",
         reveal="Single state. No build.",
         draw=lambda c: L.claim_card(
             c, "and ask", "the question that changes the 90 days",
             "“What would you want to trust me with by the end of my "
             "first 90 days that you would not have trusted me with on day "
             "one?”",
             foot="that question turns the first 90 days into development, "
                  "not performance theater.", dark=True))],
   sound="One accent.",
   hold="Hold. This is the card people will save.",
   source="Spoken, word for word."),

 F("NEW_V10_FS_08_PROVE_QUESTION", 10, 34,
   "The script replaces the quick-win question rather than repeating it. "
   "The replacement is what belongs on screen.",
   "Claim card. The different question, alone.",
   [dict(name="NEW_V10_FS_08_PROVE_QUESTION",
         reveal="Single state. No build.",
         draw=lambda c: L.claim_card(
             c, "instead of a quick win", "a different question",
             "What can I prove here by day 90 that I could not prove on "
             "day one?",
             foot="the evidence does not have to be dramatic. it needs to "
                  "be real."))],
   sound="One accent.",
   source="Spoken, word for word. The script does not require a visible "
          "win by day 90 and this card does not imply one."),

 F("NEW_V10_FS_09_PROOF_SENTENCES", 10, 38,
   "The sentences the viewer should be able to finish. Save-worthy, so "
   "they are set as a list rather than read past.",
   "Lines card, established then activated one at a time.",
   [dict(name="NEW_V10_FS_09_ESTABLISH", reveal="Establish.",
         draw=lambda c: L.questions(
             c, "what proof sounds like", "Finish a few sentences.",
             ["“I came in assuming X. I learned Y.”",
              "“The part of my previous experience that helped most "
              "was X.”",
              "“The part I had to relearn was Y.”"])),
    dict(name="NEW_V10_FS_09A_ASSUMING", reveal="Activate the first.",
         draw=lambda c: L.questions(
             c, "what proof sounds like", "Finish a few sentences.",
             ["“I came in assuming X. I learned Y.”",
              "“The part of my previous experience that helped most "
              "was X.”",
              "“The part I had to relearn was Y.”"], active=0)),
    dict(name="NEW_V10_FS_09B_HELPED_MOST", reveal="Activate the second.",
         draw=lambda c: L.questions(
             c, "what proof sounds like", "Finish a few sentences.",
             ["“I came in assuming X. I learned Y.”",
              "“The part of my previous experience that helped most "
              "was X.”",
              "“The part I had to relearn was Y.”"], active=1)),
    dict(name="NEW_V10_FS_09C_RELEARN", reveal="Activate the third.",
         draw=lambda c: L.questions(
             c, "what proof sounds like", "Finish a few sentences.",
             ["“I came in assuming X. I learned Y.”",
              "“The part of my previous experience that helped most "
              "was X.”",
              "“The part I had to relearn was Y.”"], active=2))],
   build="ESTABLISH", treatment="SEQUENCE",
   sound="One quiet accent per reveal.",
   source="Spoken, word for word."),

 F("NEW_V10_FS_10_THE_REVERSAL", 10, 41,
   "The story turn. It is the one line in the video that should feel like "
   "the ground moving, so it arrives alone, at size, after a beat of "
   "silence.",
   "Statement. Full bleed. Nothing else on screen.",
   [dict(name="NEW_V10_FS_10_THE_REVERSAL",
         reveal="Single state. Cut to it clean, on the pause.",
         draw=lambda c: L.statement(
             c, "the reversal",
             "They are not the only ones evaluating.", dark=True, size=104))],
   sound="One deliberate accent, and a subtle shift underneath it. This is "
         "the reversal: it is the strongest sound moment in the video.",
   hold="Cut to camera, hold a brief pause, then cut here. Hold five "
        "seconds. Return to Temidayo for the interpretation.",
   source="Spoken, word for word."),

 F("NEW_V10_FS_11_YOUR_EVIDENCE", 10, 42,
   "The questions the viewer is entitled to ask about the job, kept "
   "together so the point reads as evidence gathering, not grievance.",
   "Questions card, established then activated one at a time.",
   [dict(name="NEW_V10_FS_11_ESTABLISH", reveal="Establish.",
         draw=lambda c: L.questions(
             c, "you are collecting evidence too", "About the job.",
             ["Is this actually the job you accepted?",
              "Does the authority match what you were told?",
              "Are you getting access to the work you came here to do?"])),
    dict(name="NEW_V10_FS_11A_THE_JOB", reveal="Activate the first.",
         draw=lambda c: L.questions(
             c, "you are collecting evidence too", "About the job.",
             ["Is this actually the job you accepted?",
              "Does the authority match what you were told?",
              "Are you getting access to the work you came here to do?"],
             active=0)),
    dict(name="NEW_V10_FS_11B_AUTHORITY", reveal="Activate the second.",
         draw=lambda c: L.questions(
             c, "you are collecting evidence too", "About the job.",
             ["Is this actually the job you accepted?",
              "Does the authority match what you were told?",
              "Are you getting access to the work you came here to do?"],
             active=1)),
    dict(name="NEW_V10_FS_11C_ACCESS", reveal="Activate the third.",
         draw=lambda c: L.questions(
             c, "you are collecting evidence too", "About the job.",
             ["Is this actually the job you accepted?",
              "Does the authority match what you were told?",
              "Are you getting access to the work you came here to do?"],
             active=2))],
   build="ESTABLISH", treatment="QUESTIONS",
   sound="One quiet accent per reveal.",
   source="Spoken, word for word."),

 F("NEW_V10_FS_12_NOT_AUTOMATICALLY_LEAVE", 10, 45,
   "The boundary. The reversal must not read as an instruction to quit, "
   "and the script says so directly.",
   "Statement with support. Camera-adjacent in tone, deliberately quiet.",
   [dict(name="NEW_V10_FS_12_NOT_AUTOMATICALLY_LEAVE",
         reveal="Single state. No build.",
         draw=lambda c: L.statement(
             c, "the boundary",
             "That does not automatically mean leave.",
             "Roles change. Priorities change. Organizations have real "
             "constraints. But you should notice the difference.",
             size=60, support_size=42))],
   sound="No accent.",
   source="Spoken, word for word. The script protects legitimate role "
          "change here and the card carries that protection."),

 F("NEW_V10_FS_13_THE_TOOL", 10, 51,
   "The final tool, and the bridge into V11. Four lines, arriving one at "
   "a time, then complete.",
   "Numbered framework, established then activated one line at a time, "
   "ending on the complete frame.",
   [dict(name="NEW_V10_FS_13_ESTABLISH", reveal="Establish the frame.",
         draw=lambda c: L.framework(
             c, "the first-90-days read", "Keep it this simple.",
             [("READ", "What do I understand now that I did not understand "
                       "on day one?"),
              ("TEST", "What from my previous experience works here, what "
                       "needs translating, and what does not?"),
              ("PROVE", "What can I now show that I have done successfully "
                        "in this context?"),
              ("ROLE CHECK", "What have these 90 days taught me about the "
                             "job itself?")], dark=True)),
    dict(name="NEW_V10_FS_13A_READ", reveal="Activate READ.",
         draw=lambda c: L.framework(
             c, "the first-90-days read", "Keep it this simple.",
             [("READ", "What do I understand now that I did not understand "
                       "on day one?"),
              ("TEST", "What from my previous experience works here, what "
                       "needs translating, and what does not?"),
              ("PROVE", "What can I now show that I have done successfully "
                        "in this context?"),
              ("ROLE CHECK", "What have these 90 days taught me about the "
                             "job itself?")], active=0, dark=True)),
    dict(name="NEW_V10_FS_13B_TEST", reveal="Activate TEST.",
         draw=lambda c: L.framework(
             c, "the first-90-days read", "Keep it this simple.",
             [("READ", "What do I understand now that I did not understand "
                       "on day one?"),
              ("TEST", "What from my previous experience works here, what "
                       "needs translating, and what does not?"),
              ("PROVE", "What can I now show that I have done successfully "
                        "in this context?"),
              ("ROLE CHECK", "What have these 90 days taught me about the "
                             "job itself?")], active=1, dark=True)),
    dict(name="NEW_V10_FS_13C_PROVE", reveal="Activate PROVE.",
         draw=lambda c: L.framework(
             c, "the first-90-days read", "Keep it this simple.",
             [("READ", "What do I understand now that I did not understand "
                       "on day one?"),
              ("TEST", "What from my previous experience works here, what "
                       "needs translating, and what does not?"),
              ("PROVE", "What can I now show that I have done successfully "
                        "in this context?"),
              ("ROLE CHECK", "What have these 90 days taught me about the "
                             "job itself?")], active=2, dark=True)),
    dict(name="NEW_V10_FS_13D_ROLE_CHECK", reveal="Activate ROLE CHECK.",
         draw=lambda c: L.framework(
             c, "the first-90-days read", "Keep it this simple.",
             [("READ", "What do I understand now that I did not understand "
                       "on day one?"),
              ("TEST", "What from my previous experience works here, what "
                       "needs translating, and what does not?"),
              ("PROVE", "What can I now show that I have done successfully "
                        "in this context?"),
              ("ROLE CHECK", "What have these 90 days taught me about the "
                             "job itself?")], active=3, dark=True))],
   svg=True, build="ESTABLISH", treatment="FRAMEWORK",
   sound="One quiet accent per reveal.",
   hold="End on the complete frame and hold. This is the card the video "
        "is for.",
   source="All four lines are spoken, word for word, in the script's "
          "order. ROLE CHECK is the bridge into NEW V11."),

 F("NEW_V10_FS_14_THE_PLAN", 10, 53,
   "The closing instruction, four short imperatives. It is the CTA the "
   "script actually speaks: no product ask was added.",
   "Action card. Four steps, no resource.",
   [dict(name="NEW_V10_FS_14_THE_PLAN", reveal="Single state. Final tool.",
         draw=lambda c: L.action(
             c, "that is the plan", "Read the context.",
             ["Test what traveled.", "Build new proof.",
              "And read the role back."]))],
   treatment="ACTION", sound="One accent.",
   hold="Hold, then go to the Watch Next card.",
   source="Spoken, word for word. The script names no product and none "
          "appears on any card."),

 WN(10),
]


# ===================================================================== V11
V11 = [
 F("NEW_V11_FS_01_FOUR_QUESTIONS", 11, 4,
   "The framework arrives only after the mismatch is recognizable. "
   "Sequential, one word at a time.",
   "Sequence, established whole then activated one line at a time.",
   [dict(name="NEW_V11_FS_01_ESTABLISH", reveal="Establish all four.",
         draw=lambda c: L.sequence(
             c, "four questions", "For reading role drift.",
             [("EXPECTED", "What did you reasonably believe you were "
                           "accepting?"),
              ("ACTUAL", "What is the job asking from you now?"),
              ("COST", "What does the difference actually cost you?"),
              ("CHOICE", "What can you clarify, negotiate, test, or decide "
                         "next?")], dark=True)),
    dict(name="NEW_V11_FS_01A_EXPECTED", reveal="Activate EXPECTED.",
         draw=lambda c: L.sequence(
             c, "four questions", "For reading role drift.",
             [("EXPECTED", "What did you reasonably believe you were "
                           "accepting?"),
              ("ACTUAL", "What is the job asking from you now?"),
              ("COST", "What does the difference actually cost you?"),
              ("CHOICE", "What can you clarify, negotiate, test, or decide "
                         "next?")], active=0, dark=True)),
    dict(name="NEW_V11_FS_01B_ACTUAL", reveal="Activate ACTUAL.",
         draw=lambda c: L.sequence(
             c, "four questions", "For reading role drift.",
             [("EXPECTED", "What did you reasonably believe you were "
                           "accepting?"),
              ("ACTUAL", "What is the job asking from you now?"),
              ("COST", "What does the difference actually cost you?"),
              ("CHOICE", "What can you clarify, negotiate, test, or decide "
                         "next?")], active=1, dark=True)),
    dict(name="NEW_V11_FS_01C_COST", reveal="Activate COST.",
         draw=lambda c: L.sequence(
             c, "four questions", "For reading role drift.",
             [("EXPECTED", "What did you reasonably believe you were "
                           "accepting?"),
              ("ACTUAL", "What is the job asking from you now?"),
              ("COST", "What does the difference actually cost you?"),
              ("CHOICE", "What can you clarify, negotiate, test, or decide "
                         "next?")], active=2, dark=True)),
    dict(name="NEW_V11_FS_01D_CHOICE", reveal="Activate CHOICE.",
         draw=lambda c: L.sequence(
             c, "four questions", "For reading role drift.",
             [("EXPECTED", "What did you reasonably believe you were "
                           "accepting?"),
              ("ACTUAL", "What is the job asking from you now?"),
              ("COST", "What does the difference actually cost you?"),
              ("CHOICE", "What can you clarify, negotiate, test, or decide "
                         "next?")], active=3, dark=True))],
   svg=True, build="ESTABLISH", treatment="SEQUENCE",
   sound="One quiet accent per reveal.",
   hold="Hold the complete frame before the first activation.",
   source="Spoken: EXPECTED. ACTUAL. COST. CHOICE. Each support line is "
          "the script's own question for that word."),

 F("NEW_V11_FS_02_WRITE_IT_DOWN", 11, 8,
   "The parts of the offer that mattered to the decision. A list, because "
   "the viewer is being asked to actually write it down.",
   "Lines card. Established whole, no activation: all of it matters "
   "equally here.",
   [dict(name="NEW_V11_FS_02_WRITE_IT_DOWN",
         reveal="Single state. The whole list.",
         draw=lambda c: L.questions(
             c, "expected", "Write down the parts that mattered.",
             ["Scope. Authority. Reporting line.",
              "Location. Travel. Compensation. Team.",
              "The kind of work you expected to spend meaningful time "
              "doing."],
             foot="not the fantasy version of the role.", dark=False,
             size=52))],
   sound="One accent.",
   source="Spoken, word for word, in the script's order."),

 F("NEW_V11_FS_03_EXPECTED_VS_ACTUAL", 11, 15,
   "The comparison the brief asks for. The viewer needs to see the "
   "difference between what was reasonably accepted and what the "
   "recurring reality has become. Both directions are shown: the script "
   "says the actual role is sometimes better.",
   "Side-by-side comparison, the narrower reading activated second.",
   [dict(name="NEW_V11_FS_03A_BOTH_DIRECTIONS",
         reveal="Establish. Both readings are on the table.",
         draw=lambda c: L.compare(
             c, "expected against actual", "Sometimes better. Sometimes "
             "narrower.",
             ("sometimes better", "More than the description suggested",
              [("Scope", "More than expected"),
               ("Visibility", "More than expected"),
               ("Manager", "Better than the description suggested")]),
             ("sometimes narrower", "Less than the role you accepted",
              [("Hired for strategy", "Spend most of your time "
                                      "coordinating"),
               ("Expected to lead a team", "The team never arrived"),
               ("Told a decision was yours", "Discover you can only "
                                             "recommend")]))),
    dict(name="NEW_V11_FS_03B_NARROWER",
         reveal="Activate the narrower reading, which is the one the "
                "viewer came for.",
         draw=lambda c: L.compare(
             c, "expected against actual", "Sometimes better. Sometimes "
             "narrower.",
             ("sometimes better", "More than the description suggested",
              [("Scope", "More than expected"),
               ("Visibility", "More than expected"),
               ("Manager", "Better than the description suggested")]),
             ("sometimes narrower", "Less than the role you accepted",
              [("Hired for strategy", "Spend most of your time "
                                      "coordinating"),
               ("Expected to lead a team", "The team never arrived"),
               ("Told a decision was yours", "Discover you can only "
                                             "recommend")]),
             active="right",
             foot="look for the recurring pattern. do not judge it from "
                  "one bad week."))],
   svg=True, treatment="COMPARISON", sound="One accent on the second.",
   hold="Hold long enough to read both columns.",
   source="Spoken, word for word. Both directions are kept because the "
          "script keeps both: the actual role is sometimes better."),

 F("NEW_V11_FS_04_THE_REAL_QUESTION", 11, 16,
   "The script replaces the obvious question with a better one. The "
   "replacement is what belongs on screen.",
   "Struck comparison. The discarded question, then the real one.",
   [dict(name="NEW_V11_FS_04_THE_REAL_QUESTION",
         reveal="Single state. The first question is struck through.",
         draw=lambda c: L.struck(
             c, "the question", "The question is not:",
             ["Is this exactly what was written?"],
             "Is the actual role still close enough to the role I agreed "
             "to build my life and career around?"))],
   sound="One accent.",
   source="Both questions are spoken, word for word."),

 F("NEW_V11_FS_05_TEMPORARY_OR_NOT", 11, 20,
   "The difference between a temporary condition and a settled one is the "
   "heart of the cost read, and it is a contrast the viewer can see.",
   "Side-by-side comparison. Two timelines, read together.",
   [dict(name="NEW_V11_FS_05_TEMPORARY_OR_NOT",
         reveal="Single state. Both halves land together.",
         draw=lambda c: L.compare(
             c, "the same mismatch, two readings",
             "That may be temporary.",
             ("the first month", "Unusually operational",
              [("Why", "A launch is underway"),
               ("Reading", "That may be temporary")]),
             ("six months later", "The strategic work still has not "
                                  "appeared",
              [("What you are doing", "Work you already knew how to do"),
               ("Reading", "No credible path to the scope you accepted")]),
             foot="not every mismatch deserves the same response."))],
   treatment="COMPARISON", sound="One accent.",
   source="Spoken, word for word. The script offers the temporary reading "
          "first and this card keeps that order."),

 F("NEW_V11_FS_06_FOUR_COST_LENSES", 11, 24,
   "The four cost lenses. One active idea at a time, because the viewer "
   "is being asked to work out which one they are reacting to.",
   "Numbered framework, established then activated one lens at a time.",
   [dict(name="NEW_V11_FS_06_ESTABLISH", reveal="Establish all four.",
         draw=lambda c: L.framework(
             c, "the four cost lenses", "I would look at four costs.",
             [("CAPABILITY", "Is this role building judgment, scope, and "
                             "experience you want to carry forward?"),
              ("EVIDENCE", "Will you be able to prove meaningful work from "
                           "this version of the job?"),
              ("COMPENSATION", "Has the scope changed enough that the pay, "
                               "level, or agreement needs to be revisited?"),
              ("LIFE", "Did the practical cost change: travel, hours, "
                       "location, caregiving, health, or something else?")],
             dark=True)),
    dict(name="NEW_V11_FS_06A_CAPABILITY", reveal="Activate CAPABILITY.",
         draw=lambda c: L.framework(
             c, "the four cost lenses", "I would look at four costs.",
             [("CAPABILITY", "Is this role building judgment, scope, and "
                             "experience you want to carry forward?"),
              ("EVIDENCE", "Will you be able to prove meaningful work from "
                           "this version of the job?"),
              ("COMPENSATION", "Has the scope changed enough that the pay, "
                               "level, or agreement needs to be revisited?"),
              ("LIFE", "Did the practical cost change: travel, hours, "
                       "location, caregiving, health, or something else?")],
             active=0, dark=True)),
    dict(name="NEW_V11_FS_06B_EVIDENCE", reveal="Activate EVIDENCE.",
         draw=lambda c: L.framework(
             c, "the four cost lenses", "I would look at four costs.",
             [("CAPABILITY", "Is this role building judgment, scope, and "
                             "experience you want to carry forward?"),
              ("EVIDENCE", "Will you be able to prove meaningful work from "
                           "this version of the job?"),
              ("COMPENSATION", "Has the scope changed enough that the pay, "
                               "level, or agreement needs to be revisited?"),
              ("LIFE", "Did the practical cost change: travel, hours, "
                       "location, caregiving, health, or something else?")],
             active=1, dark=True)),
    dict(name="NEW_V11_FS_06C_COMPENSATION",
         reveal="Activate COMPENSATION.",
         draw=lambda c: L.framework(
             c, "the four cost lenses", "I would look at four costs.",
             [("CAPABILITY", "Is this role building judgment, scope, and "
                             "experience you want to carry forward?"),
              ("EVIDENCE", "Will you be able to prove meaningful work from "
                           "this version of the job?"),
              ("COMPENSATION", "Has the scope changed enough that the pay, "
                               "level, or agreement needs to be revisited?"),
              ("LIFE", "Did the practical cost change: travel, hours, "
                       "location, caregiving, health, or something else?")],
             active=2, dark=True)),
    dict(name="NEW_V11_FS_06D_LIFE", reveal="Activate LIFE.",
         draw=lambda c: L.framework(
             c, "the four cost lenses", "I would look at four costs.",
             [("CAPABILITY", "Is this role building judgment, scope, and "
                             "experience you want to carry forward?"),
              ("EVIDENCE", "Will you be able to prove meaningful work from "
                           "this version of the job?"),
              ("COMPENSATION", "Has the scope changed enough that the pay, "
                               "level, or agreement needs to be revisited?"),
              ("LIFE", "Did the practical cost change: travel, hours, "
                       "location, caregiving, health, or something else?")],
             active=3, dark=True))],
   svg=True, build="ESTABLISH", treatment="FRAMEWORK",
   sound="One quiet accent per reveal.",
   hold="End on the complete frame.",
   source="All four lenses are spoken, word for word, in the script's "
          "order."),

 F("NEW_V11_FS_07_CLARIFICATION_SCRIPT", 11, 32,
   "The save-worthy card. This is the sentence the viewer will screenshot "
   "and use, so it is given the whole frame and no decoration.",
   "Claim card. The sentence, at size, alone.",
   [dict(name="NEW_V11_FS_07_CLARIFICATION_SCRIPT",
         reveal="Single state. No build.",
         draw=lambda c: L.claim_card(
             c, "start with clarification before accusation",
             "what to say",
             "“When we discussed this role, I expected X. In practice, "
             "I am seeing Y. Is that temporary, or is this the role as it "
             "now exists?”",
             foot="that question gives the other person room to explain "
                  "what changed.", dark=True))],
   svg=True, sound="One accent.",
   hold="Hold the complete card long enough to screenshot.",
   source="Spoken, word for word. The question is written to invite an "
          "explanation, not to accuse."),

 F("NEW_V11_FS_08_TWO_EXTREMES", 11, 36,
   "The boundary card. Both failure modes are given equal weight so "
   "neither the employer nor the viewer is cast as the villain.",
   "Two-part card. Two extremes, held side by side.",
   [dict(name="NEW_V11_FS_08_TWO_EXTREMES",
         reveal="Single state. Both halves land together.",
         draw=lambda c: L.twopart(
             c, "what not to do", "I would avoid two extremes.",
             ("Do not convince yourself that every mismatch is a betrayal.",
              "A job can change for legitimate reasons."),
             ("Do not keep making career decisions based on the job you "
              "accepted", "when the job you are actually doing has clearly "
              "moved somewhere else."),
             joiner="and",
             foot="the problem is not that reality changed. the problem is "
                  "refusing to update your read."))],
   treatment="COMPARISON", sound="One accent.",
   source="Spoken, word for word. The first half is the script's own "
          "protection for legitimate role change."),

 F("NEW_V11_FS_09_THE_ROLE_DRIFT_READ", 11, 44,
   "The final tool. Four lines arriving one at a time, then complete.",
   "Numbered framework, established then activated one line at a time, "
   "ending on the complete frame.",
   [dict(name="NEW_V11_FS_09_ESTABLISH", reveal="Establish the frame.",
         draw=lambda c: L.framework(
             c, "the role-drift read", "Put the four lines next to each "
             "other.",
             [("EXPECTED", "What did I reasonably believe I was "
                           "accepting?"),
              ("ACTUAL", "What is true now, based on the recurring "
                         "pattern?"),
              ("COST", "What is the difference doing to my capability, "
                       "evidence, compensation, or life?"),
              ("CHOICE", "What can I clarify, negotiate, test, or decide "
                         "next?")], dark=True)),
    dict(name="NEW_V11_FS_09A_EXPECTED", reveal="Activate EXPECTED.",
         draw=lambda c: L.framework(
             c, "the role-drift read", "Put the four lines next to each "
             "other.",
             [("EXPECTED", "What did I reasonably believe I was "
                           "accepting?"),
              ("ACTUAL", "What is true now, based on the recurring "
                         "pattern?"),
              ("COST", "What is the difference doing to my capability, "
                       "evidence, compensation, or life?"),
              ("CHOICE", "What can I clarify, negotiate, test, or decide "
                         "next?")], active=0, dark=True)),
    dict(name="NEW_V11_FS_09B_ACTUAL", reveal="Activate ACTUAL.",
         draw=lambda c: L.framework(
             c, "the role-drift read", "Put the four lines next to each "
             "other.",
             [("EXPECTED", "What did I reasonably believe I was "
                           "accepting?"),
              ("ACTUAL", "What is true now, based on the recurring "
                         "pattern?"),
              ("COST", "What is the difference doing to my capability, "
                       "evidence, compensation, or life?"),
              ("CHOICE", "What can I clarify, negotiate, test, or decide "
                         "next?")], active=1, dark=True)),
    dict(name="NEW_V11_FS_09C_COST", reveal="Activate COST.",
         draw=lambda c: L.framework(
             c, "the role-drift read", "Put the four lines next to each "
             "other.",
             [("EXPECTED", "What did I reasonably believe I was "
                           "accepting?"),
              ("ACTUAL", "What is true now, based on the recurring "
                         "pattern?"),
              ("COST", "What is the difference doing to my capability, "
                       "evidence, compensation, or life?"),
              ("CHOICE", "What can I clarify, negotiate, test, or decide "
                         "next?")], active=2, dark=True)),
    dict(name="NEW_V11_FS_09D_CHOICE", reveal="Activate CHOICE.",
         draw=lambda c: L.framework(
             c, "the role-drift read", "Put the four lines next to each "
             "other.",
             [("EXPECTED", "What did I reasonably believe I was "
                           "accepting?"),
              ("ACTUAL", "What is true now, based on the recurring "
                         "pattern?"),
              ("COST", "What is the difference doing to my capability, "
                       "evidence, compensation, or life?"),
              ("CHOICE", "What can I clarify, negotiate, test, or decide "
                         "next?")], active=3, dark=True))],
   svg=True, build="ESTABLISH", treatment="FRAMEWORK",
   sound="One quiet accent per reveal.",
   hold="End on the complete frame and hold. This is the card the video "
        "is for.",
   source="All four lines are spoken, word for word, in the script's "
          "order."),

 F("NEW_V11_FS_10_THE_BOUNDARY", 11, 46,
   "The boundary, stated plainly. The framework is a read, not a verdict, "
   "and the card says exactly that.",
   "Statement with support.",
   [dict(name="NEW_V11_FS_10_THE_BOUNDARY",
         reveal="Single state. No build.",
         draw=lambda c: L.statement(
             c, "the boundary",
             "This framework does not tell you whether to leave.",
             "Sometimes the right choice is to stay. Sometimes leaving is "
             "not practical yet. And sometimes the gap is large enough "
             "that you need to plan an exit.", size=72))],
   sound="No accent.",
   source="Spoken, word for word. The script keeps every one of these "
          "options open and the card keeps them open too."),

 F("NEW_V11_FS_11_YOUR_CONSTRAINTS", 11, 50,
   "The constraints that shape what is possible. Named, because leaving "
   "them out would turn the video into advice for people with no "
   "constraints.",
   "Lines card. The whole list, no activation.",
   [dict(name="NEW_V11_FS_11_YOUR_CONSTRAINTS",
         reveal="Single state. The whole list.",
         draw=lambda c: L.questions(
             c, "your constraints are real",
             "All of this shapes what is possible.",
             ["Compensation. Health. Caregiving.",
              "Immigration. Geography. Timing.",
              "The market, and financial runway."],
             foot="make the decision from the job that actually exists.",
             dark=False, size=56))],
   sound="No accent.",
   source="Spoken, word for word."),

 F("NEW_V11_FS_12_NAME_THE_DIFFERENCE", 11, 53,
   "The closing instruction. It is the CTA the script actually speaks: "
   "no product ask was added.",
   "Action card. One instruction and the four words.",
   [dict(name="NEW_V11_FS_12_NAME_THE_DIFFERENCE",
         reveal="Single state. Final tool.",
         draw=lambda c: L.action(
             c, "before you normalize it",
             "Name the difference.",
             ["Expected.", "Actual.", "Cost.", "Choice."]))],
   treatment="ACTION", sound="One accent.",
   hold="Hold, then go to the Watch Next card.",
   source="Spoken, word for word. The script names no product and none "
          "appears on any card."),

 WN(11),
]

SETS = {10: V10, 11: V11}


def states(n):
    return [(f, s) for f in SETS[n] for s in f["states"]]
