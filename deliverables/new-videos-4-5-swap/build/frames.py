# -*- coding: utf-8 -*-
"""Hero teaching assets for the renumbered Videos 4 and 5.

Mobile legibility is the binding constraint. Every frame has to be understood
at normal phone size in about one to two seconds, so: very large type, one
dominant idea per state, short phrases, sequential reveals, and no four-column
layouts or dense grids anywhere.

All on-screen wording comes from the approved Recording Masters.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from rdeck import Card

# ---------------------------------------------------------------- NEW VIDEO 4
V4 = [
 dict(id="MG01", file="V4_MG01_Stop_Explaining_In_Order.png",
      draw=lambda c: L.statement(c, None,
          "STOP EXPLAINING\nYOUR CAREER\nIN ORDER.",
          "Chronology makes them build the bridge.", dark=True, size=96,
          support_size=54),
      onscreen="STOP EXPLAINING YOUR CAREER IN ORDER.",
      script="\"So here is the rule: Stop explaining your career in order.\"",
      purpose="The rule the whole video runs on, stated once at full size.",
      reveal="Three lines arriving one at a time, 0.5s apart. Supporting line "
             "at 2.2s.",
      hold="6 to 7 seconds", captions="Suppress for the full hold.",
      sound="Soft impact as the third line lands."),

 dict(id="MG02", file="V4_MG02_Chapters_Spine_Next_Direction.png",
      draw=lambda c: L.numbered(c, "One structure, three versions",
          ["CHAPTERS", "SPINE", "NEXT DIRECTION"],
          foot="The detail changes. The structure does not.", size=68),
      onscreen="CHAPTERS / SPINE / NEXT DIRECTION",
      script="\"All three versions use the same structure underneath. "
             "Chapters. Spine. Next Direction.\"",
      purpose="The hero framework. Returns briefly above each of the three "
              "versions.",
      reveal="One word at a time, 0.9s apart. Closing line at 3.2s. Hold the "
             "complete set.",
      hold="9 to 10 seconds first time, 3 seconds on each return.",
      captions="Suppress.",
      sound="One accent per word, then a resolve."),

 dict(id="MG03", file="V4_MG03_Twenty_Second_Version.png",
      draw=lambda c: L.numbered(c, "The 20 second version",
          ["I ...", "I've done that in ...", "Today I ..."],
          foot="Work pattern. Two or three contexts. Current direction.",
          size=68, dark=True),
      onscreen="I ...  /  I've done that in ...  /  Today I ...",
      script="\"Your version is: I, and then the work pattern. I've done that "
             "in, and then two or three contexts. Today I, and then your "
             "current direction.\"",
      purpose="The template a viewer will pause and copy. It has to be "
              "readable in a screenshot.",
      reveal="One stem at a time, 1.0s apart. Closing line at 3.6s.",
      hold="10 to 12 seconds. The longest hold in the video.",
      captions="Suppress. This frame gets screenshotted.",
      sound="One soft accent per stem."),

 dict(id="MG04", file="V4_MG04_Ninety_Second_Version.png",
      draw=lambda c: L.numbered(c, "The 90 second version",
          ["CHAPTERS", "SPINE", "NEXT DIRECTION"],
          foot="Three chapters, not seven. Two examples, not five.", size=68),
      onscreen="CHAPTERS / SPINE / NEXT DIRECTION",
      script="\"That is the ninety-second answer. Chapters. Spine. Next "
             "Direction.\"",
      purpose="Shows the same structure carrying a longer answer, so the "
              "viewer sees one system rather than three tricks.",
      reveal="Three words together at reduced weight, then the closing line at "
             "1.4s at full weight. Deliberately quieter than MG02.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One accent on the closing line only."),

 dict(id="MG05", file="V4_MG05_The_Objection.png",
      draw=lambda c: L.statement(c, "The objection version",
          "“WHY SO MANY\nCHANGES?”",
          "Often they just cannot see the pattern yet.", size=96,
          support_size=54),
      onscreen="WHY SO MANY CHANGES?",
      script="\"Now the harder one. Why so many changes?\"",
      purpose="Puts the actual question on screen, then reframes it before the "
              "answer is taught.",
      reveal="Question first, alone, for 1.5s. Supporting line at 2.0s.",
      hold="6 to 7 seconds", captions="Suppress.",
      sound="One restrained accent on the supporting line."),

 dict(id="MG06", file="V4_MG06_Story_Explains_Proof_Supports.png",
      draw=lambda c: L.statement(c, None,
          "A STORY EXPLAINS.\nPROOF SUPPORTS.",
          "The story gets the question. Evidence answers it.",
          dark=True, size=92, support_size=54),
      onscreen="A STORY EXPLAINS. PROOF SUPPORTS.",
      script="\"And remember: A story explains. Proof supports.\"",
      purpose="The line that earns the resource bridge without turning the "
              "ending into a pitch.",
      reveal="First line, second line at 1.0s, supporting line at 2.4s.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One clean accent between the two lines."),

 dict(id="MG07", file="V4_MG07_All_Three_Versions.png",
      draw=lambda c: L.numbered(c, "You now have all three",
          ["20 SECONDS", "90 SECONDS", "THE OBJECTION"],
          foot="Say all three out loud before you need them.", size=68),
      onscreen="20 SECONDS / 90 SECONDS / THE OBJECTION",
      script="\"So now you have all three. The twenty-second version. The "
             "ninety-second version. The objection version.\"",
      purpose="Summary before the practice instruction.",
      reveal="Three together, then the closing line at 1.6s.",
      hold="6 to 7 seconds", captions="Suppress.",
      sound="One accent as the set completes."),

 dict(id="CTA", file="V4_CTA_Career_Evidence_Starter.png",
      draw=lambda c: L.cta(c, "Free 10-Minute Career Evidence Starter",
          "Share your 20-second\nversion in the comments.",
          "Building the proof underneath the story? Start here.",
          "temidayoafonja.com/career-evidence-starter"),
      onscreen="SHARE YOUR 20-SECOND VERSION / Free 10-Minute Career Evidence "
               "Starter / temidayoafonja.com/career-evidence-starter",
      script="\"If you get your twenty-second version working, put it in the "
             "comments... start with the free 10-Minute Career Evidence Starter "
             "in the pinned comment.\"",
      purpose="Carries the spoken comment CTA and the pinned resource in one "
              "card. Keep the Proof is not on this card; it stays in the "
              "description.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Suppress. Never cover the address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="V4_WatchNext_Why_Nobody_Can_Tell.png",
      draw=lambda c: L.watch_next(c,
          "Why Nobody Can Tell\nWhat You're\nActually Good At"),
      onscreen="WATCH NEXT: WHY NOBODY CAN TELL WHAT YOU'RE ACTUALLY GOOD AT",
      script="\"Watch Why Nobody Can Tell What You're Actually Good At next.\"",
      purpose="Final visual. The right of frame is left clear for the "
              "clickable YouTube end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through both closing lines and past the last "
           "word.",
      captions="Suppress.", sound="None. Let the closing land dry."),
]

# ---------------------------------------------------------------- NEW VIDEO 5
V5 = [
 dict(id="MG01", file="V5_MG01_Respected_But_Hard_To_Place.png",
      draw=lambda c: L.statement(c, None,
          "RESPECTED.\nBUT HARD TO PLACE.",
          "They still may not know what to do with you.", dark=True, size=96,
          support_size=54),
      onscreen="RESPECTED. BUT HARD TO PLACE.",
      script="\"People can respect your experience and still have no idea what "
             "to do with you.\"",
      purpose="The tension of the video, on screen in the first thirty "
              "seconds.",
      reveal="First line alone for 1.2s, second line at 1.5s, supporting line "
             "at 2.6s.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="Soft impact on the second line."),

 dict(id="MG02", file="V5_MG02_Sorting_Mechanism.png",
      draw=lambda c: L.numbered(c, "The sorting mechanism",
          ["FIVE POSSIBLE CATEGORIES",
           "THEY PICK THE NEAREST ONE",
           "A SMALLER BOX THAN YOU"], size=58),
      onscreen="MULTIPLE POSSIBLE CATEGORIES  to  NEAREST CATEGORY  to  A "
               "SMALLER BOX THAN YOUR ACTUAL CAPABILITY",
      script="\"They grab the closest category they can see, and they put you "
             "there. And that category is often smaller than what you can "
             "actually do.\"",
      purpose="Shows the mechanism as three steps so the viewer stops reading "
              "it as unfairness and starts reading it as information they "
              "control.",
      reveal="One step at a time, 1.0s apart, each replacing the emphasis of "
             "the one before. The third step holds alone.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="One accent per step, descending."),

 dict(id="MG03", file="V5_MG03_The_One_Line_Test.png",
      draw=lambda c: L.numbered(c, "The One-Line Test",
          ["CLAIM", "SPINE", "RECEIPTS"],
          foot="Claim gets you read. Spine makes you make sense. Receipts make "
               "you believable.", size=76),
      onscreen="CLAIM / SPINE / RECEIPTS",
      script="\"That is where the One-Line Test comes in. Claim. Spine. "
             "Receipts.\"",
      purpose="The hero framework. Returns briefly at each of the three "
              "section changes.",
      reveal="One word at a time, 0.9s apart. Closing line at 3.2s.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Suppress.",
      sound="One accent per word, then a resolve."),

 dict(id="MG04", file="V5_MG04_Sharper_Versus_Defensible.png",
      draw=lambda c: L.duo(c, "Choosing your Claim",
          "Sharper is not always better.",
          ("SHARPER", "Sounds stronger."),
          ("DEFENSIBLE", "Survives “show me.”"),
          foot="Choose the one you can defend.", mobile=True),
      onscreen="SHARPER CLAIM vs DEFENSIBLE CLAIM",
      script="\"So the sharper sentence was not the more defensible sentence... "
             "Choose the one you can defend.\"",
      purpose="The judgment call at the heart of the Claim section, shown as "
              "a trade rather than a mistake.",
      reveal="SHARPER first, held alone 1.5s so it lands as attractive. "
             "DEFENSIBLE at 2.0s. Closing line at 3.4s.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="One accent as DEFENSIBLE arrives."),

 dict(id="MG05", file="V5_MG05_Remove_The_Nouns.png",
      draw=lambda c: L.struck(c, "Finding the Spine",
          "Remove the nouns.",
          ["The industry", "The system", "The title", "The employer"],
          "Look at the verbs."),
      onscreen="REMOVE THE NOUNS  /  LOOK AT THE VERBS",
      script="\"What broke it open was removing the nouns. Take out the "
             "industry. The system. The title. The employer. Look at the "
             "verbs.\"",
      purpose="Shows what to discard and what to look for. Hard to hold by ear, "
              "easy to hold on screen.",
      reveal="The four nouns strike through one at a time, 0.7s apart, then "
             "the closing line arrives at full weight at 3.4s.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="A subtle click per strike, one clean resolve on the verbs line."),

 dict(id="MG06", file="V5_MG06_Receipts.png",
      draw=lambda c: L.statement(c, "Receipts",
          "DIFFERENT CONTEXTS.\nSAME CLAIM.",
          "Each one has to make sense on its own.", dark=True, size=88,
          support_size=54),
      onscreen="DIFFERENT CONTEXTS. SAME CLAIM.",
      script="\"Different organizations. Different years. Different outputs. "
             "Each Receipt stands on its own. And all three support the same "
             "Claim.\"",
      purpose="States the rule that governs all three Receipts, rather than "
              "putting three bounded evidence claims on screen where the "
              "qualifiers would shrink to nothing on a phone.",
      reveal="First line, second line at 1.0s, supporting line at 2.2s.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One accent between the two lines."),

 dict(id="MG07", file="V5_MG07_Test_The_Claim.png",
      draw=lambda c: L.duo(c, "Test the Claim",
          "Listen to their next question.",
          ("ABOUT YOUR HISTORY", "Still decoding."),
          ("ABOUT THE PROBLEM", "It is working."),
          foot="“Tell me what you think I actually help with.”", mobile=True),
      onscreen="Does their next question ask about YOUR HISTORY or THE "
               "PROBLEM?",
      script="\"Listen to their next question.\"",
      purpose="Gives the test and how to read the result in one frame.",
      reveal="Two outcomes 1.2s apart, then the exact sentence at the bottom at "
             "3.0s and held.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="Two accents on the outcomes, one resolve on the sentence."),

 dict(id="MG08", file="V5_MG08_Real_Limits.png",
      draw=lambda c: L.statement(c, "The real limits",
          "A SENTENCE\nCANNOT ERASE THIS.",
          "A weak market. Bias. A missing credential. A real gap.",
          size=92, support_size=54),
      onscreen="A SENTENCE CANNOT ERASE: market conditions, bias, credentials, "
               "domain gaps, real experience gaps",
      script="\"A better sentence cannot erase a weak market. It cannot erase "
             "bias or age discrimination.\"",
      purpose="Keeps the promise honest. Written as one line plus one sentence "
              "rather than a dense list, so it reads on a phone.",
      reveal="Headline, then the supporting line at 1.6s. No item-by-item "
             "build; this section should not feel like a checklist.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One flat accent. No resolve. This should not feel triumphant."),

 dict(id="CTA", file="V5_CTA_Career_Evidence_Starter.png",
      draw=lambda c: L.cta(c, "Free 10-Minute Career Evidence Starter",
          "Write your one-line\nClaim in the comments.",
          "Need help finding the proof underneath it? Start here.",
          "temidayoafonja.com/career-evidence-starter"),
      onscreen="WRITE YOUR ONE-LINE CLAIM / Free 10-Minute Career Evidence "
               "Starter / temidayoafonja.com/career-evidence-starter",
      script="\"If yes, write the Claim in the comments... I put the free "
             "10-Minute Career Evidence Starter in the pinned comment.\"",
      purpose="Carries the spoken comment CTA and the pinned resource. No "
              "second product route in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Suppress. Never cover the address.",
      sound="One warm accent on the URL."),

 dict(id="WN", file="V5_WatchNext_Change_Jobs.png",
      draw=lambda c: L.watch_next(c,
          "How to Change Jobs\nWithout Starting\nYour Career Over"),
      onscreen="WATCH NEXT: HOW TO CHANGE JOBS WITHOUT STARTING YOUR CAREER "
               "OVER",
      script="\"Watch How to Change Jobs Without Starting Your Career Over "
             "next.\"",
      purpose="Final visual. Routes to Video 1, not back to Video 4. Right of "
              "frame kept clear for the clickable end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through both closing lines and past the last "
           "word.",
      captions="Suppress.", sound="None."),
]

SETS = {4: V4, 5: V5}
TITLES = {4: "How to Explain a Career That Looks All Over the Place",
          5: "Why Nobody Can Tell What You're Actually Good At"}


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
