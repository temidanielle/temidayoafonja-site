# -*- coding: utf-8 -*-
"""Support and reference frames for Videos 6 and 7.

Every on-screen idea and every treatment below is taken from the visual map in
the approved Recording Master. Nothing here was invented. These are reference
frames for Riverside, not a presentation deck.

Mobile legibility is the binding constraint: large bold type, high contrast,
one dominant idea per state, and sequential reveals instead of dense grids.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from rdeck import Card

V6 = [
 dict(id="A1", file="01_Same_Company_Not_Same_Work.png", job="Opening distinction",
      draw=lambda c: L.statement(c, None,
          "SAME COMPANY\nIS NOT SAME WORK",
          "What changes is the work you can access.", dark=True, size=84),
      onscreen="SAME COMPANY IS NOT SAME WORK / What changes is the work you "
               "can access.",
      script="\"That familiarity can make the opportunity look smaller than it "
             "is, or safer than it really is.\"",
      treatment="True full-screen motion graphic after the hook.",
      reveal="Headline first, held alone for 1.2s. Supporting line at 1.8s. "
             "Gentle fade, no movement.",
      hold="6 to 7 seconds", captions="Captions off for the whole hold.",
      sound="Soft whoosh on the headline. Nothing on the second line."),

 dict(id="A2", file="02_Three_Questions_Framework.png", job="Three-question framework",
      draw=lambda c: L.numbered(c, "Before you accept",
          ["WILL THE WORK CHANGE?",
           "WILL YOUR JUDGMENT EXPAND?",
           "WILL THE EVIDENCE TRAVEL?"], size=54),
      onscreen="1 WILL THE WORK CHANGE? / 2 WILL YOUR JUDGMENT EXPAND? / "
               "3 WILL THE EVIDENCE TRAVEL?",
      script="\"Before you make an internal move, I want you to answer three "
             "questions.\"",
      treatment="True full screen. This is the hero graphic of the video and "
                "returns briefly at each section change.",
      reveal="One question at a time, 0.9s apart. Hold the complete set for a "
             "full beat before cutting away.",
      hold="9 to 11 seconds on first appearance, 3 seconds on each return.",
      captions="Captions off.",
      sound="One restrained accent per question, then a resolve on the "
            "complete set."),

 dict(id="A3", file="03_An_Ordinary_Monday.png", job="Question 1",
      draw=lambda c: L.statement(c, "Question one",
          "WHAT WILL BE DIFFERENT\nON AN ORDINARY MONDAY?",
          "Problems  ·  Systems  ·  Stakeholders  ·  Context", size=72),
      onscreen="WHAT WILL BE DIFFERENT ON AN ORDINARY MONDAY? / Problems, "
               "Systems, Stakeholders, Context",
      script="\"Start with the most concrete question: What will actually be "
             "different on an ordinary Monday?\"",
      treatment="Full-screen section graphic, then return to camera.",
      reveal="Question first. The four words arrive together at 1.5s, not one "
             "at a time.",
      hold="6 to 7 seconds", captions="Captions off.",
      sound="One soft accent as the four words land."),

 dict(id="A4", file="04_More_Tasks_Vs_More_Judgment.png", job="Tasks vs judgment",
      draw=lambda c: L.duo(c, "Question two",
          "More tasks is not more judgment.",
          ("MORE TASKS", "Volume  ·  Coordination  ·  Absorption"),
          ("MORE JUDGMENT", "Interpretation  ·  Tradeoffs  ·  Consequence"),
          dark=True),
      onscreen="MORE TASKS: Volume, Coordination, Absorption  /  MORE "
               "JUDGMENT: Interpretation, Tradeoffs, Consequence",
      script="\"More tasks can mean volume, coordination, and absorption. More "
             "judgment means you have to interpret incomplete information.\"",
      treatment="True full-screen comparison.",
      reveal="MORE TASKS first, held alone for 1.5s so it lands as the "
             "familiar one. MORE JUDGMENT second.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="Restrained click or sweep as MORE JUDGMENT arrives."),

 dict(id="A5", file="05_Portable_Evidence.png", job="Portable evidence",
      draw=lambda c: L.readings(c, "Question three",
          "Evidence that travels.",
          [("Result", "What changed?"),
           ("Judgment", "What did you notice or decide?"),
           ("Range", "What new context can you now handle?")]),
      onscreen="RESULT: What changed?  /  JUDGMENT: What did you notice or "
               "decide?  /  RANGE: What new context can you now handle?",
      script="\"I would look for three kinds of evidence: result, judgment, "
             "and range.\"",
      treatment="True full-screen three-part reveal.",
      reveal="One row at a time, 1.1s apart. Hold long enough to read all "
             "three together.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One accent on the first row only."),

 dict(id="A6", file="06_Reading_The_Three_Answers.png", job="Decision read",
      draw=lambda c: L.readings(c, "Reading the three answers",
          "How it comes out.",
          [("Three yes", "Strong growth case."),
           ("Two yes", "Investigate or negotiate."),
           ("Zero or one yes", "Movement, not much growth.")]),
      onscreen="3 YES Strong growth case  /  2 YES Investigate or negotiate  / "
               " 0-1 YES Movement, not much growth",
      script="\"Now put the three answers together.\"",
      treatment="True full-screen sequential reveal. No scorecard "
                "gamification: no ticks, crosses, scores, colour coding or "
                "progress bars.",
      reveal="One row at a time, 1.2s apart. The third row arrives at the same "
             "visual weight as the others, never dimmed or marked as failure.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One flat accent per row, same pitch. Do not resolve upward or "
            "downward."),

 dict(id="A7", file="07_Questions_To_Ask.png", job="Conversation prompts",
      draw=lambda c: L.numbered(c, "Ask before you accept",
          ["What problems will I own?",
           "Which decisions belong to me?",
           "How will success be measured?"], size=52),
      onscreen="What problems will I own? / Which decisions belong to me? / "
               "How will success be measured?",
      script="\"Before you accept the opportunity, ask...\"",
      treatment="Full-screen progressive questions.",
      reveal="One question at a time, 1.0s apart, with room to breathe. Hold "
             "all three.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One soft accent per question."),

 dict(id="CTA", file="08_CTA_Career_Decision_Evidence_Check.png", job="CTA",
      draw=lambda c: L.cta(c, "Career Decision Evidence Check",
          "Read the evidence\nbehind the choice.",
          "Free. For deciding whether to stay, move internally, or leave.",
          "temidayoafonja.com/career-decisions"),
      onscreen="CAREER DECISION EVIDENCE CHECK / "
               "temidayoafonja.com/career-decisions",
      script="\"the free Career Decision Evidence Check gives you a structured "
             "way to read the evidence behind that choice. It is linked "
             "below.\"",
      treatment="True full screen. One product route only in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds, through the whole CTA line.",
      captions="Captions off. Never cover the web address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="09_Watch_Next_Are_You_Growing.png", job="Watch Next",
      draw=lambda c: L.watch_next(c,
          "Are You Growing,\nor Just Being Given\nMore Work?"),
      onscreen="ARE YOU GROWING, OR JUST BEING GIVEN MORE WORK?",
      script="\"That is what we are testing next in Are You Growing, or Just "
             "Being Given More Work?\"",
      treatment="True full screen and the FINAL visual of the video. Right of "
                "frame kept clear for the YouTube end screen.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.",
      sound="None. Let the closing line land dry."),
]

V7 = [
 dict(id="A1", file="01_Busier_Is_Not_More_Capable.png", job="Opening consequence",
      draw=lambda c: L.statement(c, None,
          "MORE RESPONSIBILITY\nCAN MEAN GROWTH.\nIT CAN ALSO MEAN\nYOU ABSORB MORE.",
          "Busier is not more capable.", dark=True, size=62),
      onscreen="MORE RESPONSIBILITY CAN MEAN GROWTH. IT CAN ALSO MEAN YOU "
               "ABSORB MORE. / BUSIER IS NOT MORE CAPABLE.",
      script="\"Maybe it is. Or maybe the organization has simply learned that "
             "you will absorb more.\"",
      treatment="True full-screen after the opening scene.",
      reveal="First line, then the second at 1.4s, then the closing line at "
             "3.0s after a deliberate pause.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="Soft impact on the final line only."),

 dict(id="A2", file="02_CAR_Framework.png", job="CAR framework",
      draw=lambda c: L.numbered(c, "The CAR test",
          ["COMPLEXITY", "AUTHORITY", "RETURN"], size=64),
      onscreen="C COMPLEXITY / A AUTHORITY / R RETURN",
      script="\"So use the CAR test: Complexity, Authority, Return.\"",
      treatment="True full-screen hero graphic. This is the memory device of "
                "the video and returns briefly at each section change.",
      reveal="C, A and R one at a time, 0.9s apart. Hold the complete set.",
      hold="9 to 11 seconds on first appearance, 3 seconds on each return.",
      captions="Captions off.",
      sound="One accent per letter, then a resolve on the complete set."),

 dict(id="A3", file="03_Complexity_Comparison.png", job="Complexity comparison",
      draw=lambda c: L.duo(c, "C is for complexity",
          "Did the problem change, or just the volume?",
          ("MORE UNITS OF\nTHE SAME PROBLEM", "Capacity is being used."),
          ("NEW VARIABLES", "Ambiguity  ·  Tradeoffs")),
      onscreen="MORE UNITS OF THE SAME PROBLEM  vs.  NEW VARIABLES, AMBIGUITY, "
               "TRADEOFFS",
      script="\"Did the problem become more complex, or did the volume simply "
             "increase?\"",
      treatment="True full-screen comparison. The right side carries more "
                "visual weight.",
      reveal="Left side first at reduced emphasis, right side at 1.5s at full "
             "weight.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One restrained accent as the right side arrives."),

 dict(id="A4", file="04_Responsibility_Accountability_Authority.png",
      job="Authority distinction",
      draw=lambda c: L.readings(c, "A is for authority",
          "Three words people use as one.",
          [("Responsibility", "What you carry."),
           ("Accountability", "What you answer for."),
           ("Authority", "What you can influence or decide.")]),
      onscreen="RESPONSIBILITY What you carry / ACCOUNTABILITY What you answer "
               "for / AUTHORITY What you can influence or decide",
      script="\"Responsibility is what you are expected to carry. "
             "Accountability is what you will answer for. Authority is what "
             "you can influence or decide.\"",
      treatment="True full-screen stacked reveal.",
      reveal="One row at a time, 1.1s apart. Hold on the authority definition "
             "noticeably longer than the other two; it is the one that does "
             "the work.",
      hold="10 to 11 seconds", captions="Captions off.",
      sound="One accent per row, with the third slightly more present."),

 dict(id="A5", file="05_What_Did_The_Work_Return.png", job="Return",
      draw=lambda c: L.numbered(c, "R is for return",
          ["CAPABILITY", "EVIDENCE", "RECOGNITION"],
          foot="What did the work return?", size=62, dark=True),
      onscreen="WHAT DID THE WORK RETURN? / Capability, Evidence, Recognition",
      script="\"I would look for return in three places: capability, evidence, "
             "and recognition.\"",
      treatment="True full-screen three-part reveal.",
      reveal="One item at a time, 1.0s apart, then the question line beneath "
             "at 3.2s.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="Optional restrained click per item. Nothing on the question line."),

 dict(id="A6", file="06_Reading_The_CAR_Pattern.png", job="Pattern read",
      draw=lambda c: L.duo(c, "Reading the pattern",
          "Read the three together.",
          ("COMPLEXITY, AUTHORITY\nAND RETURN RISING", "Real growth."),
          ("VOLUME ONLY RISING", "More load.")),
      onscreen="COMPLEXITY, AUTHORITY, RETURN all rising = REAL GROWTH  /  "
               "VOLUME ONLY rising = MORE LOAD",
      script="\"If Complexity, Authority, and Return are all expanding, you are "
             "probably looking at real growth.\"",
      treatment="True full screen. The lower result must not be punitive or "
                "alarmist: no red, no warning icons, no downward arrows "
                "styled as failure.",
      reveal="Left side first, right side at 1.6s at the same visual weight "
             "and the same colour treatment.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One flat accent per side, same pitch. No downward resolve."),

 dict(id="A7", file="07_The_Scope_Conversation.png", job="Scope conversation",
      draw=lambda c: L.numbered(c, "The scope conversation",
          ["What should remain?",
           "What should come off my plate?",
           "Which decisions belong to me?",
           "When will this be reviewed?"], size=50),
      onscreen="What should remain? / What should come off my plate? / Which "
               "decisions belong to me? / When will this be reviewed?",
      script="\"Then take four questions into the conversation with your "
             "manager.\"",
      treatment="Full-screen progressive questions with breathing room.",
      reveal="One question at a time, 1.1s apart. Do not crowd them; this is "
             "the frame a viewer will screenshot.",
      hold="10 to 12 seconds", captions="Captions off.",
      sound="One soft accent per question."),

 dict(id="CTA", file="08_CTA_Capability_Formation_Field_Kit.png", job="CTA",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "Read what your work\nis actually building.",
          "See where your options are expanding, and where they are not.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      script="\"the Capability Formation Field Kit helps you read the evidence "
             "in your role. It is linked below.\"",
      treatment="True full screen. One product route only in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds, through the whole CTA line.",
      captions="Captions off. Never cover the web address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="09_Watch_Next_Built_It_From_Scratch.png", job="Watch Next",
      draw=lambda c: L.watch_next(c,
          "How to Show Your Impact\nat Work When You Built It\nFrom Scratch"),
      onscreen="HOW TO SHOW YOUR IMPACT AT WORK WHEN YOU BUILT IT FROM SCRATCH",
      script="\"In the next video, I will show you how to make that work "
             "visible: How to Show Your Impact at Work When You Built It From "
             "Scratch.\"",
      treatment="True full screen and the FINAL visual of the video. Right of "
                "frame kept clear for the YouTube end screen.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.",
      sound="None. Let the closing line land dry."),
]

SETS = {6: V6, 7: V7}
TITLES = {6: "Should I Make an Internal Move? 3 Questions to Decide",
          7: "Are You Growing, or Just Being Given More Work?"}


def build_cards(n):
    out = []
    for i, spec in enumerate(SETS[n], start=1):
        c = Card(i, spec["file"])
        spec["draw"](c)
        c.notes = "%s  (%s)\n\nOn screen: %s\n\nScript: %s\n\nTreatment: %s\nHold: %s" % (
            spec["file"], spec["job"], spec["onscreen"], spec["script"],
            spec["treatment"], spec["hold"])
        out.append(c)
    return out
