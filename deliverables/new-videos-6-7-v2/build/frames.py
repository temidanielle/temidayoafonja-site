# -*- coding: utf-8 -*-
"""Hero teaching assets for the v2.0 Videos 6 and 7.

On-screen wording follows the visual map inside each v2.0 Recording Master,
with the two wording choices from the production brief applied where they
differ from the master's table. Both differences are recorded in the QA report.

Mobile legibility is the binding constraint: very large type, one dominant idea
per state, short phrases, sequential reveals, no four-box grids.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from rdeck import Card

V6 = [
 dict(id="MG01", file="V6_MG01_New_Title_Same_Work.png", job="Opening distinction",
      draw=lambda c: L.statement(c, None,
          "NEW TITLE,\nSAME WORK?",
          "Same company does not automatically mean useful growth.",
          dark=True, size=112, support_size=54),
      onscreen="NEW TITLE, SAME WORK? / Same company does not automatically "
               "mean useful growth.",
      script="\"An internal move can look safe because the logo does not "
             "change. That is exactly why it can fool you.\"",
      purpose="The central tension, and the thumbnail line, on screen in the "
              "first thirty seconds.",
      reveal="Headline alone for 1.4s, then the supporting line at 1.8s. "
             "Gentle fade, no movement.",
      hold="6 to 7 seconds", captions="Captions off for the full hold.",
      sound="Soft whoosh on the headline. Nothing on the second line."),

 dict(id="MG02", file="V6_MG02_Three_Questions.png", job="Three-question framework",
      draw=lambda c: L.numbered(c, "Before you take the role",
          ["WILL THE WORK CHANGE?",
           "WILL MY JUDGMENT EXPAND?",
           "WILL THE EVIDENCE TRAVEL?"], size=56),
      onscreen="1 WILL THE WORK CHANGE? / 2 WILL MY JUDGMENT EXPAND? / "
               "3 WILL THE EVIDENCE TRAVEL?",
      script="\"Before you take an internal role, ask three questions.\"",
      purpose="The hero framework. Returns briefly at each section change.",
      reveal="One question at a time, 0.9s apart. Hold the complete set for a "
             "full beat before cutting away.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Captions off.",
      sound="One restrained accent per question, then a resolve on the set."),

 dict(id="MG03", file="V6_MG03_Ordinary_Monday.png", job="Question 1",
      draw=lambda c: L.statement(c, "Question one",
          "WHAT WILL BE DIFFERENT\nON AN ORDINARY MONDAY?",
          "Problems  ·  Systems  ·  Stakeholders  ·  Context",
          size=76, support_size=52),
      onscreen="WHAT WILL BE DIFFERENT ON AN ORDINARY MONDAY? / Problems, "
               "Systems, Stakeholders, Context",
      script="\"Start with the most concrete question: What will actually be "
             "different on an ordinary Monday?\"",
      purpose="The most concrete question in the video, with the four things to "
              "look for as one readable line rather than four small boxes.",
      reveal="Question first. The four words arrive together at 1.6s as a "
             "single line, never as separate boxes.",
      hold="6 to 7 seconds", captions="Captions off.",
      sound="One soft accent as the four words land."),

 dict(id="MG04", file="V6_MG04_Tasks_Vs_Judgment.png", job="Tasks vs judgment",
      draw=lambda c: L.duo(c, "Question two",
          "More tasks is not more judgment.",
          ("MORE TASKS", "Volume  ·  Coordination  ·  Absorption"),
          ("MORE JUDGMENT", "Interpretation  ·  Tradeoffs  ·  Consequence"),
          dark=True, mobile=True),
      onscreen="MORE TASKS: Volume, Coordination, Absorption  /  MORE "
               "JUDGMENT: Interpretation, Tradeoffs, Consequence",
      script="\"More tasks can mean volume, coordination, and absorption. More "
             "judgment means you have to interpret incomplete information.\"",
      purpose="The distinction dependable people most often get wrong.",
      reveal="MORE TASKS first, held alone 1.5s so it lands as the familiar "
             "one. MORE JUDGMENT second.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="Restrained click or sweep as MORE JUDGMENT arrives."),

 dict(id="MG05", file="V6_MG05_Portable_Evidence.png", job="Portable evidence",
      draw=lambda c: L.readings(c, "Question three",
          "Evidence that travels.",
          [("Result", "What changed?"),
           ("Judgment", "What did you notice or decide?"),
           ("Range", "What new context can you handle?")]),
      onscreen="RESULT: What changed?  /  JUDGMENT: What did you notice or "
               "decide?  /  RANGE: What new context can you now handle?",
      script="\"I would look for three kinds of evidence: result, judgment, "
             "and range.\"",
      purpose="Defines portable evidence without suggesting anything "
              "confidential is taken.",
      reveal="One row at a time, 1.1s apart. Hold long enough to read all "
             "three together.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One accent on the first row only."),

 dict(id="MG06", file="V6_MG06_Decision_Read.png", job="Decision read",
      draw=lambda c: L.readings(c, "Reading the three answers",
          "How it comes out.",
          [("Three yes", "Strong growth case."),
           ("Two yes", "Investigate or negotiate."),
           ("Zero or one yes", "May be movement without much growth.")]),
      onscreen="3 YES: Strong growth case / 2 YES: Investigate or negotiate / "
               "0-1 YES: May be movement without much growth",
      script="\"Now put the three answers together.\"",
      purpose="Gives the viewer a way to read their own result.",
      treatment_note="No scorecard gamification: no ticks, crosses, scores, "
                     "color coding, progress bars or pass-fail styling.",
      reveal="One row at a time, 1.2s apart. The third row arrives at the same "
             "visual weight as the others, never dimmed or marked as failure.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One flat accent per row, same pitch. Do not resolve upward or "
            "downward."),

 dict(id="MG07", file="V6_MG07_Questions_To_Ask.png", job="Conversation prompts",
      draw=lambda c: L.numbered(c, "Ask before you accept",
          ["What problems will I own?",
           "Which decisions belong to me?",
           "How will success be measured?"], size=54),
      onscreen="What problems will I own? / Which decisions belong to me? / "
               "How will success be measured?",
      script="\"Before you accept the opportunity, ask...\"",
      purpose="The questions to take into the internal conversation.",
      reveal="One question at a time, 1.0s apart, with room to breathe.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One soft accent per question."),

 dict(id="CTA", file="V6_CTA_Career_Decision_Evidence_Check.png", job="CTA",
      draw=lambda c: L.cta(c, "Free Career Decision Evidence Check",
          "Read the evidence\nbehind the choice.",
          "For deciding whether to stay, move internally, or leave.",
          "temidayoafonja.com/career-decisions"),
      onscreen="FREE CAREER DECISION EVIDENCE CHECK / "
               "temidayoafonja.com/career-decisions",
      script="\"the free Career Decision Evidence Check gives you a structured "
             "way to read the evidence behind that choice. It is linked "
             "below.\"",
      purpose="The single product route in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Captions off. Never cover the address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="V6_WATCH_NEXT_Are_You_Growing.png", job="Watch Next",
      draw=lambda c: L.watch_next(c,
          "Are You Growing,\nor Just Being Given\nMore Work?"),
      onscreen="WATCH NEXT: ARE YOU GROWING, OR JUST BEING GIVEN MORE WORK?",
      script="\"That is what we are testing next in Are You Growing, or Just "
             "Being Given More Work?\"",
      purpose="Final visual. Right of frame kept clear for the clickable "
              "YouTube end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.", sound="None. Let the closing land dry."),
]

V7 = [
 dict(id="MG01", file="V7_MG01_Opening_Consequence.png", job="Opening consequence",
      draw=lambda c: L.statement(c, None,
          "MORE RESPONSIBILITY\nCAN MEAN GROWTH.\n\nIT CAN ALSO MEAN\nYOU ABSORB MORE.",
          None, dark=True, size=76),
      onscreen="MORE RESPONSIBILITY CAN MEAN GROWTH. IT CAN ALSO MEAN YOU "
               "ABSORB MORE.",
      script="\"Maybe it is. Or maybe the organization has simply learned that "
             "you will absorb more.\"",
      purpose="The distinction the whole video rests on.",
      treatment_note="BUSIER IS NOT BETTER is deliberately not on this frame. "
                     "Adding a third line forced all three down to a size that "
                     "fails on a phone, and the brief says not to force it in "
                     "if it creates too much copy. It is retained as the "
                     "alternate thumbnail line only.",
      reveal="First block, then the second at 1.6s after a deliberate pause. "
             "Two states only.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="Soft impact on the second block."),

 dict(id="MG02", file="V7_MG02_CAR_Framework.png", job="CAR framework",
      draw=lambda c: L.numbered(c, "The CAR test",
          ["COMPLEXITY", "AUTHORITY", "RETURN"], size=76),
      onscreen="C COMPLEXITY / A AUTHORITY / R RETURN",
      script="\"So use the CAR test: Complexity, Authority, Return.\"",
      purpose="The hero graphic and the memory device. Returns briefly at each "
              "section change.",
      reveal="C, A and R one at a time, 0.9s apart. Hold the complete set.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Captions off.",
      sound="One accent per letter, then a resolve on the complete set."),

 dict(id="MG03", file="V7_MG03_Complexity.png", job="Complexity comparison",
      draw=lambda c: L.duo(c, "C is for complexity",
          "Did the problem change, or just the volume?",
          ("MORE UNITS OF\nTHE SAME PROBLEM", "Capacity is being used."),
          ("NEW VARIABLES", "Ambiguity  ·  Tradeoffs"),
          dark=False, mobile=True),
      onscreen="MORE UNITS OF THE SAME PROBLEM  vs.  NEW VARIABLES, AMBIGUITY, "
               "TRADEOFFS",
      script="\"Did the problem become more complex, or did the volume simply "
             "increase?\"",
      purpose="Separates capacity use from a genuine change in the class of "
              "problem.",
      treatment_note="The right side carries more visual weight.",
      reveal="Left side first at reduced emphasis, right side at 1.5s at full "
             "weight.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One restrained accent as the right side arrives."),

 dict(id="MG04", file="V7_MG04_Authority.png", job="Authority distinction",
      draw=lambda c: L.readings(c, "A is for authority",
          "Three words people use as one.",
          [("Responsibility", "What you carry."),
           ("Accountability", "What you answer for."),
           ("Authority", "What you can influence or decide.")]),
      onscreen="RESPONSIBILITY: What you carry / ACCOUNTABILITY: What you "
               "answer for / AUTHORITY: What you can influence or decide",
      script="\"Responsibility is what you are expected to carry. "
             "Accountability is what you will answer for. Authority is what "
             "you can influence or decide.\"",
      purpose="The distinction the section turns on.",
      reveal="One row at a time, 1.1s apart. Never all three at once. Hold on "
             "the authority definition noticeably longer than the other two.",
      hold="10 to 11 seconds", captions="Captions off.",
      sound="One accent per row, with the third slightly more present."),

 dict(id="MG05", file="V7_MG05_Return.png", job="Return",
      draw=lambda c: L.numbered(c, "R is for return",
          ["CAPABILITY", "EVIDENCE", "RECOGNITION"],
          foot="What did the work return?", size=68, dark=True),
      onscreen="WHAT DID THE WORK RETURN? / Capability, Evidence, Recognition",
      script="\"I would look for return in three places: capability, evidence, "
             "and recognition.\"",
      purpose="Names what should be coming back, without implying every "
              "assignment must produce immediate promotion or pay.",
      reveal="One item at a time, 1.0s apart, then the question line at 3.2s.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="Optional restrained click per item. Nothing on the question line."),

 dict(id="MG06", file="V7_MG06_Pattern_Read.png", job="Pattern read",
      draw=lambda c: L.duo(c, "Reading the pattern",
          "Read the three together.",
          ("COMPLEXITY, AUTHORITY\nAND RETURN UP", "Real growth."),
          ("VOLUME ONLY UP", "More load."), dark=False, mobile=True),
      onscreen="COMPLEXITY UP, AUTHORITY AND RETURN UP = REAL GROWTH  /  "
               "VOLUME ONLY UP = MORE LOAD",
      script="\"If Complexity, Authority, and Return are all expanding, you are "
             "probably looking at real growth.\"",
      purpose="Lets the viewer read their own pattern.",
      treatment_note="Neutral, not punitive. No red, no warning icons, no "
                     "downward arrows styled as failure. More load is a "
                     "description, not a verdict.",
      reveal="Left side first, right side at 1.6s at the same visual weight "
             "and the same color treatment.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One flat accent per side, same pitch. No downward resolve."),

 dict(id="MG07", file="V7_MG07_Scope_Conversation_A.png", job="Scope conversation, part one",
      draw=lambda c: L.numbered(c, "The scope conversation",
          ["What should remain?",
           "What should come off my plate?"], size=68),
      onscreen="What should remain? / What should come off my plate?",
      script="\"Then take four questions into the conversation with your "
             "manager.\"",
      purpose="First half of the four questions. Split into two frames so each "
              "question stays large enough to read on a phone.",
      reveal="One question at a time, 1.1s apart.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="One soft accent per question."),

 dict(id="MG08", file="V7_MG08_Scope_Conversation_B.png", job="Scope conversation, part two",
      draw=lambda c: L.numbered(c, "The scope conversation",
          ["Which decisions belong to me?",
           "When will this be reviewed?"], size=68),
      onscreen="Which decisions belong to me? / When will this be reviewed?",
      script="\"Which decisions need to belong to me for these outcomes? And "
             "how and when will the expanded scope be formally reviewed?\"",
      purpose="Second half of the four questions. This is the frame a viewer "
              "will screenshot before a manager conversation.",
      reveal="One question at a time, 1.1s apart. Hold both.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One soft accent per question."),

 dict(id="CTA", file="V7_CTA_Capability_Formation_Field_Kit.png", job="CTA",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "Read what your work\nis actually building.",
          "See where your options are expanding, and where they are not.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      script="\"the Capability Formation Field Kit helps you read the evidence "
             "in your role. It is linked below.\"",
      purpose="The single primary product route in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Captions off. Never cover the address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="V7_WATCH_NEXT_Built_It_From_Scratch.png", job="Watch Next",
      draw=lambda c: L.watch_next(c,
          "How to Show Your\nImpact at Work\nWhen You Built It\nFrom Scratch"),
      onscreen="WATCH NEXT: HOW TO SHOW YOUR IMPACT AT WORK WHEN YOU BUILT IT "
               "FROM SCRATCH",
      script="\"In the next video, I will show you how to make that work "
             "visible: How to Show Your Impact at Work When You Built It From "
             "Scratch.\"",
      purpose="Final visual. Right of frame kept clear for the clickable "
              "end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.", sound="None."),
]

SETS = {6: V6, 7: V7}
TITLES = {6: "Before You Take an Internal Role, Ask These 3 Questions",
          7: "Are You Growing, or Just Being Given More Work?"}


def build_cards(n):
    out = []
    for i, s in enumerate(SETS[n], start=1):
        c = Card(i, s["file"])
        s["draw"](c)
        c.notes = "%s  (%s)\n\nOn screen: %s\n\nScript: %s\n\nPurpose: %s\nHold: %s" % (
            s["file"], s["id"], s["onscreen"], s["script"], s["purpose"],
            s["hold"])
        out.append(c)
    return out
