# -*- coding: utf-8 -*-
"""Support/reference assets for Videos 4 to 7, synchronized to the
September 9 locked Recording Masters.

Every asset carries a `status` and a `why`, which become the reuse/change
table in each package. The statuses are the ones the brief names:

  REUSE        unchanged, and its trigger still exists in the locked script
  REORDER      unchanged artwork, different position in the running order
  COPY UPDATE  same design, wording corrected against the locked script
  REBUILD      the frame's job changed, so the frame was rebuilt
  REMOVE       dropped, with the reason recorded

Reuse is proved rather than asserted: the build hashes every rendered PNG
against the pre-synchronization package and reports any REUSE asset whose
bytes moved.

Mobile legibility remains the binding constraint. Very large type, one
dominant idea per state, short phrases, sequential reveals, no dense grids.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from rdeck import Card

STARTER = "temidayoafonja.com/career-evidence-starter"

# ------------------------------------------------------------------- VIDEO 4
V4 = [
 dict(id="MG01", file="V4_MG01_Introduction_Or_Defense.png",
      status="REBUILD", was="V4_MG01_Stop_Explaining_In_Order.png",
      why="The old frame carried STOP EXPLAINING YOUR CAREER IN ORDER, which "
          "the locked script no longer says and now actively contradicts: the "
          "ninety-second answer uses compressed Chapters on purpose. Rebuilt "
          "on the opening beat the script does have.",
      draw=lambda c: L.statement(c, None,
          "LESS LIKE AN\nINTRODUCTION.\nMORE LIKE A DEFENSE.",
          "And you still have not said what the work built in you.",
          dark=True, size=88, support_size=52),
      onscreen="LESS LIKE AN INTRODUCTION. MORE LIKE A DEFENSE.",
      script="Now your answer feels less like an introduction and more like a "
             "defense.",
      purpose="Names the problem the whole video solves, in the viewer's own "
              "experience, inside the first thirty seconds.",
      reveal="Three lines one at a time, 0.5s apart. Supporting line at 2.2s.",
      hold="6 to 7 seconds",
      captions="Suppress for the full hold.",
      sound="Soft impact as the third line lands.",
      after="Cut back to camera for the scripted [Pause.] The pause is "
            "performed on camera, not over this graphic."),

 dict(id="MG02", file="V4_MG02_Chapters_Spine_Next_Direction.png",
      status="COPY UPDATE", was="V4_MG02_Chapters_Spine_Next_Direction.png",
      why="Design unchanged. The closing line said \"The detail changes. The "
          "structure does not.\", which asserts a fixed order. The locked "
          "script says the ingredients stay the same while the order and the "
          "amount of detail depend on the question.",
      draw=lambda c: L.numbered(c, "One set of ingredients",
          ["CHAPTERS", "SPINE", "NEXT DIRECTION"],
          foot="The ingredients stay the same. The order depends on the "
               "question.", size=68),
      onscreen="CHAPTERS / SPINE / NEXT DIRECTION",
      script="All three answers use the same ingredients:",
      purpose="The hero framework, stated as ingredients rather than as a "
              "fixed running order.",
      reveal="One word at a time, 0.9s apart. Closing line at 3.2s. Hold the "
             "complete set.",
      hold="9 to 10 seconds first time, 3 seconds on each return.",
      captions="Suppress.",
      sound="One accent per word, then a resolve.",
      after="Cut back to camera."),

 dict(id="MG03", file="V4_MG03_Order_Depends_On_The_Question.png",
      status="REBUILD", was=None,
      why="New. The locked script draws a distinction the previous package had "
          "no asset for and its framework card actively denied: the quick "
          "introduction leads with the Spine, the longer answer uses Chapters "
          "to make the Spine visible. This is the correction the brief asks "
          "for, carried as one frame rather than a note.",
      draw=lambda c: L.duo(c, "Same ingredients, different order",
          "The order depends on the question.",
          ("QUICK INTRODUCTION", "Lead with the Spine."),
          ("LONGER ANSWER", "Use Chapters to make the Spine visible."),
          foot="Your Spine does not change depending on who is asking.",
          mobile=True),
      onscreen="QUICK INTRODUCTION: lead with the Spine / LONGER ANSWER: use "
               "Chapters to make the Spine visible",
      script="For a quick introduction, I lead with the Spine.",
      purpose="Replaces the retired fixed-order rule with what the script "
              "actually teaches.",
      reveal="Left column first, held alone 1.4s. Right column at 1.8s. "
             "Closing line at 3.4s.",
      hold="9 to 10 seconds",
      captions="Suppress.",
      sound="One accent as the right column arrives, one resolve on the "
            "closing line.",
      after="Cut back to camera."),

 dict(id="MG04", file="V4_MG04_Twenty_Second_Version.png",
      status="REUSE", was="V4_MG03_Twenty_Second_Version.png",
      why="Artwork unchanged. Renumbered only, because the rebuilt opening and "
          "the new order frame sit ahead of it.",
      draw=lambda c: L.numbered(c, "The 20 second version",
          ["I ...", "I've done that in ...", "Today I ..."],
          foot="Work pattern. Two or three contexts. Current direction.",
          size=68, dark=True),
      onscreen="I ...  /  I've done that in ...  /  Today I ...",
      script="“I…” and then the work pattern.",
      purpose="The template a viewer will pause and screenshot.",
      reveal="One stem at a time, 1.0s apart. Closing line at 3.6s.",
      hold="10 to 12 seconds. The longest hold in the video.",
      captions="Suppress. This frame gets screenshotted.",
      sound="One soft accent per stem.",
      after="Cut back to camera."),

 dict(id="MG05", file="V4_MG05_Ninety_Second_Version.png",
      status="REUSE", was="V4_MG04_Ninety_Second_Version.png",
      why="Artwork unchanged. Both closing claims are still spoken: three "
          "chapters rather than seven, two examples rather than five.",
      draw=lambda c: L.numbered(c, "The 90 second version",
          ["CHAPTERS", "SPINE", "NEXT DIRECTION"],
          foot="Three chapters, not seven. Two examples, not five.", size=68),
      onscreen="CHAPTERS / SPINE / NEXT DIRECTION",
      script="That is the ninety-second answer.",
      purpose="Shows the same ingredients carrying a longer answer, so the "
              "viewer sees one system rather than three tricks.",
      reveal="Three words together at reduced weight, then the closing line at "
             "1.4s at full weight. Deliberately quieter than MG02.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One accent on the closing line only.",
      after="Cut back to camera."),

 dict(id="MG06", file="V4_MG06_The_Objection.png",
      status="REUSE", was="V4_MG05_The_Objection.png",
      why="Artwork unchanged and the question is still spoken verbatim. Its "
          "position moved: the acquisition beat now opens the objection "
          "section, so this frame lands after that beat rather than cold.",
      draw=lambda c: L.statement(c, "The objection version",
          "“WHY SO MANY\nCHANGES?”",
          "Often they just cannot see the pattern yet.", size=96,
          support_size=54),
      onscreen="WHY SO MANY CHANGES?",
      script="“Why so many changes?”",
      purpose="Puts the actual question on screen, then reframes it before the "
              "answer is taught.",
      reveal="Question first, alone, for 1.5s. Supporting line at 2.0s.",
      hold="6 to 7 seconds", captions="Suppress.",
      sound="One restrained accent on the supporting line.",
      after="Cut back to camera."),

 dict(id="MG07", file="V4_MG07_Story_Explains_Proof_Supports.png",
      status="REUSE", was="V4_MG06_Story_Explains_Proof_Supports.png",
      why="Artwork unchanged. Both lines are spoken verbatim in the locked "
          "script.",
      draw=lambda c: L.statement(c, None,
          "A STORY EXPLAINS.\nPROOF SUPPORTS.",
          "The story gets the question. Evidence answers it.",
          dark=True, size=92, support_size=54),
      onscreen="A STORY EXPLAINS. PROOF SUPPORTS.",
      script="A story explains.",
      purpose="The line that earns the resource bridge without turning the "
              "ending into a pitch.",
      reveal="First line, second line at 1.0s, supporting line at 2.4s.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One clean accent between the two lines.",
      after="Cut back to camera."),

 dict(id="MG08", file="V4_MG08_All_Three_Versions.png",
      status="REUSE", was="V4_MG07_All_Three_Versions.png",
      why="Artwork unchanged. The summary and the say-it-out-loud instruction "
          "are both still spoken.",
      draw=lambda c: L.numbered(c, "You now have all three",
          ["20 SECONDS", "90 SECONDS", "THE OBJECTION"],
          foot="Say all three out loud before you need them.", size=68),
      onscreen="20 SECONDS / 90 SECONDS / THE OBJECTION",
      script="So now you have all three.",
      purpose="Summary before the practice instruction.",
      reveal="Three together, then the closing line at 1.6s.",
      hold="6 to 7 seconds", captions="Suppress.",
      sound="One accent as the set completes.",
      after="Cut back to camera."),

 dict(id="CTA", file="V4_CTA_Career_Evidence_Starter.png",
      status="REUSE", was="V4_CTA_Career_Evidence_Starter.png",
      why="Artwork unchanged. The spoken participation CTA and the pinned "
          "resource are both unchanged in the locked script. Keep the Proof "
          "stays off this card and remains a description link only.",
      draw=lambda c: L.cta(c, "Free 10-Minute Career Evidence Starter",
          "Share your 20-second\nversion in the comments.",
          "Building the proof underneath the story? Start here.", STARTER),
      onscreen="SHARE YOUR 20-SECOND VERSION / Free 10-Minute Career Evidence "
               "Starter / " + STARTER,
      script="If you get your twenty-second version working, put it in the "
             "comments.",
      purpose="Carries the spoken comment CTA and the pinned resource in one "
              "card.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Suppress. Never cover the address.",
      sound="One warm accent on the URL.",
      after="Cut back to camera for the bridge into Watch Next."),

 dict(id="WN", file="V4_WatchNext_Why_Nobody_Can_Tell.png",
      status="REUSE", was="V4_WatchNext_Why_Nobody_Can_Tell.png",
      why="Artwork unchanged. Routing is unchanged: Video 4 to Video 5.",
      draw=lambda c: L.watch_next(c,
          "Why Nobody Can Tell\nWhat You're\nActually Good At"),
      onscreen="WATCH NEXT: WHY NOBODY CAN TELL WHAT YOU'RE ACTUALLY GOOD AT",
      script="Watch “Why Nobody Can Tell What You’re Actually Good "
             "At” next.",
      purpose="Final visual. The right of frame is left clear for the "
              "clickable end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through both closing lines and past the last "
           "word.",
      captions="Suppress.", sound="None. Let the closing land dry.",
      after="NONE. Final visual."),
]

# ------------------------------------------------------------------- VIDEO 5
V5 = [
 dict(id="MG01", file="V5_MG01_Two_Versions_Of_The_Same_Career.png",
      status="REBUILD", was="V5_MG01_Respected_But_Hard_To_Place.png",
      why="The locked script now opens by demonstrating the two versions of "
          "the same career, and the brief asks for that comparison early. No "
          "existing asset served it, so this slot was adapted rather than "
          "added, which keeps the set compact. The retired frame's line, "
          "\"People can respect your experience and still have no idea what "
          "to do with you\", is still spoken and is now carried as a short "
          "single-line callout over camera.",
      draw=lambda c: L.duo(c, "Two versions of the same career",
          "Same career. Two ways to hear it.",
          ("THE RESUME VERSION", "Where I have been."),
          ("THE CLAIM", "What I get brought in to do."),
          foot="One makes them work out the connection. The other does not.",
          mobile=True),
      onscreen="THE RESUME VERSION: where I have been / THE CLAIM: what I get "
               "brought in to do",
      script="One describes where I have been.",
      purpose="The demonstration the video now opens on. The viewer hears both "
              "versions and sees the difference named.",
      reveal="Left column while the resume version is read, held alone. Right "
             "column arrives on the Claim. Closing line 1.4s after that.",
      hold="10 to 12 seconds, across both spoken versions.",
      captions="Suppress.",
      sound="One accent as the Claim column arrives.",
      after="Cut back to camera."),

 dict(id="MG02", file="V5_MG02_The_One_Line_Test.png",
      status="REORDER", was="V5_MG03_The_One_Line_Test.png",
      why="Artwork unchanged. It moves ahead of the sorting mechanism, because "
          "the locked script names the framework before it explains why people "
          "keep putting you in the old box.",
      draw=lambda c: L.numbered(c, "The One-Line Test",
          ["CLAIM", "SPINE", "RECEIPTS"],
          foot="Claim gets you read. Spine makes you make sense. Receipts make "
               "you believable.", size=76),
      onscreen="CLAIM / SPINE / RECEIPTS",
      script="Claim. Spine. Receipts.",
      purpose="The hero framework. Returns briefly at each of the three "
              "section changes.",
      reveal="One word at a time, 0.9s apart. Closing line at 3.2s.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Suppress.",
      sound="One accent per word, then a resolve.",
      after="Cut back to camera."),

 dict(id="MG03", file="V5_MG03_Sharper_Versus_Defensible.png",
      status="REORDER", was="V5_MG04_Sharper_Versus_Defensible.png",
      why="Artwork unchanged. It moves earlier with the Claim section, which "
          "the locked script now reaches before the sorting mechanism.",
      draw=lambda c: L.duo(c, "Choosing your Claim",
          "Sharper is not always better.",
          ("SHARPER", "Sounds stronger."),
          ("DEFENSIBLE", "Survives “show me.”"),
          foot="Choose the one you can defend.", mobile=True),
      onscreen="SHARPER CLAIM vs DEFENSIBLE CLAIM",
      script="So the sharper sentence was not the more defensible sentence.",
      purpose="The judgment call at the heart of the Claim section, shown as a "
              "trade rather than a mistake.",
      reveal="SHARPER first, held alone 1.5s so it lands as attractive. "
             "DEFENSIBLE at 2.0s. Closing line at 3.4s.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="One accent as DEFENSIBLE arrives.",
      after="Cut back to camera."),

 dict(id="MG04", file="V5_MG04_Sorting_Mechanism.png",
      status="REORDER", was="V5_MG02_Sorting_Mechanism.png",
      why="Artwork unchanged and every step is still spoken, including the "
          "five categories and picking the nearest one. It now follows the "
          "Claim section rather than preceding the framework.",
      draw=lambda c: L.numbered(c, "The sorting mechanism",
          ["FIVE POSSIBLE CATEGORIES",
           "THEY PICK THE NEAREST ONE",
           "A SMALLER BOX THAN YOU"], size=58),
      onscreen="MULTIPLE POSSIBLE CATEGORIES  to  NEAREST CATEGORY  to  A "
               "SMALLER BOX THAN YOUR ACTUAL CAPABILITY",
      script="If your career gives them five categories, they normally do not "
             "keep all five.",
      purpose="Shows the mechanism as three steps, so the viewer reads it as "
              "information they control rather than as unfairness.",
      reveal="One step at a time, 1.0s apart, each replacing the emphasis of "
             "the one before. The third step holds alone.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="One accent per step, descending.",
      after="Cut back to camera."),

 dict(id="MG05", file="V5_MG05_Remove_The_Nouns.png",
      status="REUSE", was="V5_MG05_Remove_The_Nouns.png",
      why="Artwork and position unchanged. Every struck noun is still spoken "
          "in the Spine section.",
      draw=lambda c: L.struck(c, "Finding the Spine",
          "Remove the nouns.",
          ["The industry", "The system", "The title", "The employer"],
          "Look at the verbs."),
      onscreen="REMOVE THE NOUNS  /  LOOK AT THE VERBS",
      script="What broke it open was removing the nouns.",
      purpose="Shows what to discard and what to look for. Hard to hold by "
              "ear, easy to hold on screen.",
      reveal="The four nouns strike through one at a time, 0.7s apart, then "
             "the closing line arrives at full weight at 3.4s.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="A subtle click per strike, one clean resolve on the verbs line.",
      after="Cut back to camera."),

 dict(id="MG06", file="V5_MG06_Receipts.png",
      status="REUSE", was="V5_MG06_Receipts.png",
      why="Artwork and position unchanged. The frame carries the rule that "
          "governs all three Receipts. The bounded figures stay spoken, with "
          "their qualifiers, and deliberately never appear on screen where the "
          "qualifiers would shrink below phone-readable size.",
      draw=lambda c: L.statement(c, "Receipts",
          "DIFFERENT CONTEXTS.\nSAME CLAIM.",
          "Each one has to make sense on its own.", dark=True, size=88,
          support_size=54),
      onscreen="DIFFERENT CONTEXTS. SAME CLAIM.",
      script="Each Receipt stands on its own.",
      purpose="States the rule rather than putting three bounded evidence "
              "claims on screen.",
      reveal="First line, second line at 1.0s, supporting line at 2.2s.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One accent between the two lines.",
      after="Cut back to camera."),

 dict(id="MG07", file="V5_MG07_Test_The_Claim.png",
      status="COPY UPDATE", was="V5_MG07_Test_The_Claim.png",
      why="Design unchanged. The two outcomes read \"Still decoding.\" and "
          "\"It is working.\", which is a pass/fail verdict. The locked script "
          "says the Claim MAY still be making them decode, and that a question "
          "about the problem is A BETTER SIGN. The frame now matches that, and "
          "the eyebrow records that this is a practical signal rather than a "
          "scientific test.",
      draw=lambda c: L.duo(c, "Test the Claim, practically",
          "Listen to their next question.",
          ("ABOUT YOUR HISTORY", "May still be decoding."),
          ("ABOUT THE PROBLEM", "A better sign."),
          foot="“Tell me what you think I actually help with.”", mobile=True),
      onscreen="Does their next question ask about YOUR HISTORY or THE "
               "PROBLEM?",
      script="Listen to their next question.",
      purpose="Gives the test and how to read the result in one frame, without "
              "turning a practical signal into a verdict.",
      reveal="Two outcomes 1.2s apart, then the exact sentence at the bottom "
             "at 3.0s and held.",
      hold="9 to 10 seconds", captions="Suppress.",
      sound="Two accents on the outcomes, one resolve on the sentence.",
      after="Cut back to camera."),

 dict(id="MG08", file="V5_MG08_Real_Limits.png",
      status="REUSE", was="V5_MG08_Real_Limits.png",
      why="Artwork and position unchanged. Every limit named is still spoken "
          "in the section on when the Claim does not land.",
      draw=lambda c: L.statement(c, "The real limits",
          "A SENTENCE\nCANNOT ERASE THIS.",
          "A weak market. Bias. A missing credential. A real gap.",
          size=92, support_size=54),
      onscreen="A SENTENCE CANNOT ERASE: market conditions, bias, credentials, "
               "domain gaps, real experience gaps",
      script="A better sentence cannot erase a weak market.",
      purpose="Keeps the promise honest, as one line plus one sentence rather "
              "than a dense list.",
      reveal="Headline, then the supporting line at 1.6s. No item-by-item "
             "build; this section should not feel like a checklist.",
      hold="7 to 8 seconds", captions="Suppress.",
      sound="One flat accent. No resolve. This should not feel triumphant.",
      after="Cut back to camera."),

 dict(id="CTA", file="V5_CTA_Career_Evidence_Starter.png",
      status="REUSE", was="V5_CTA_Career_Evidence_Starter.png",
      why="Artwork unchanged. One resource route only, and the locked script's "
          "spoken CTA is unchanged.",
      draw=lambda c: L.cta(c, "Free 10-Minute Career Evidence Starter",
          "Write your one-line\nClaim in the comments.",
          "Need help finding the proof underneath it? Start here.", STARTER),
      onscreen="WRITE YOUR ONE-LINE CLAIM / Free 10-Minute Career Evidence "
               "Starter / " + STARTER,
      script="If yes, write the Claim in the comments.",
      purpose="Carries the spoken comment CTA and the pinned resource. No "
              "second product route in this video.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Suppress. Never cover the address.",
      sound="One warm accent on the URL.",
      after="Cut back to camera for the bridge into Watch Next."),

 dict(id="WN", file="V5_WatchNext_Change_Jobs.png",
      status="REUSE", was="V5_WatchNext_Change_Jobs.png",
      why="Artwork unchanged. Routing is unchanged: Video 5 to Video 1.",
      draw=lambda c: L.watch_next(c,
          "How to Change Jobs\nWithout Starting\nYour Career Over"),
      onscreen="WATCH NEXT: HOW TO CHANGE JOBS WITHOUT STARTING YOUR CAREER "
               "OVER",
      script="Watch “How to Change Jobs Without Starting Your Career "
             "Over” next.",
      purpose="Final visual. Routes to Video 1. Right of frame kept clear for "
              "the clickable end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through both closing lines and past the last "
           "word.",
      captions="Suppress.", sound="None.",
      after="NONE. Final visual."),
]

# ------------------------------------------------------------------- VIDEO 6
V6 = [
 dict(id="MG01", file="V6_MG01_New_Title_Same_Work.png",
      status="COPY UPDATE", was="V6_MG01_New_Title_Same_Work.png",
      why="Headline unchanged. The support line said \"Same company does not "
          "automatically mean useful growth\", which paraphrased the retired "
          "logo opening. The locked script opens on the offer itself and the "
          "one-year question, which is what the master's own visual map row 1 "
          "now carries.",
      draw=lambda c: L.statement(c, None,
          "NEW TITLE,\nSAME WORK?",
          "A year from now, what can you do, decide, or prove?",
          dark=True, size=112, support_size=52),
      onscreen="NEW TITLE, SAME WORK? / A YEAR FROM NOW, WHAT CAN YOU DO, "
               "DECIDE, OR PROVE?",
      script="A year from now, what will I be able to do, decide, or prove "
             "that I cannot do today?",
      purpose="The central tension and the thumbnail line, landing on the "
              "decision moment rather than on the concept of internal "
              "mobility.",
      reveal="Headline alone for 1.4s, then the question at 1.8s. Gentle "
             "fade, no movement.",
      hold="6 to 7 seconds", captions="Captions off for the full hold.",
      sound="Soft whoosh on the headline. Nothing on the question.",
      after="Cut back to camera.",
      person_note="The card poses the test to the viewer, so it uses the "
                  "master's own map wording in the second person. Temidayo "
                  "speaks the same question in the first person, modelling it. "
                  "Neither the script nor the map was changed."),

 dict(id="MG02", file="V6_MG02_Three_Questions.png",
      status="REUSE", was="V6_MG02_Three_Questions.png",
      why="Artwork unchanged. All three questions are still spoken verbatim in "
          "the hook.",
      draw=lambda c: L.numbered(c, "Before you take the role",
          ["WILL THE WORK CHANGE?",
           "WILL MY JUDGMENT EXPAND?",
           "WILL THE EVIDENCE TRAVEL?"], size=56),
      onscreen="1 WILL THE WORK CHANGE? / 2 WILL MY JUDGMENT EXPAND? / "
               "3 WILL THE EVIDENCE TRAVEL?",
      script="Before you take it, test three things:",
      purpose="The hero framework. Returns briefly at each section change.",
      reveal="One question at a time, 0.9s apart. Hold the complete set for a "
             "full beat before cutting away.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Captions off.",
      sound="One restrained accent per question, then a resolve on the set.",
      after="Cut back to camera.",
      person_note="This card reproduces the spoken triad, which Temidayo says "
                  "in the first person, so it keeps MY. The master's visual "
                  "map writes YOUR in that row and its own section heading "
                  "reads QUESTION 2: WILL YOUR JUDGMENT EXPAND?, so the master "
                  "alternates by context. Matching the sentence being "
                  "illustrated is the rule applied here. No speech changed."),

 dict(id="MG03", file="V6_MG03_Ordinary_Monday.png",
      status="REUSE", was="V6_MG03_Ordinary_Monday.png",
      why="Artwork unchanged. The question and all four support terms match "
          "the locked script and the master's map row 3 exactly.",
      draw=lambda c: L.statement(c, "Question one",
          "WHAT WILL BE DIFFERENT\nON AN ORDINARY MONDAY?",
          "Problems  ·  Systems  ·  Stakeholders  ·  Context",
          size=76, support_size=52),
      onscreen="WHAT WILL BE DIFFERENT ON AN ORDINARY MONDAY? / Problems · "
               "Systems · Stakeholders · Context",
      script="Start with the most concrete question: What will actually be "
             "different on an ordinary Monday?",
      purpose="Turns question one into something the viewer can actually test.",
      reveal="Question first for 1.6s, then the four terms together at 2.0s.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="One soft accent as the terms arrive.",
      after="Cut back to camera."),

 dict(id="MG04", file="V6_MG04_Tasks_Vs_Judgment.png",
      status="REUSE", was="V6_MG04_Tasks_Vs_Judgment.png",
      why="Artwork unchanged. Both columns match the master's map row 4 and "
          "the spoken definitions.",
      draw=lambda c: L.duo(c, "Question two",
          "More tasks is not more judgment.",
          ("MORE TASKS", "Volume  ·  Coordination  ·  Absorption"),
          ("MORE JUDGMENT", "Interpretation  ·  Tradeoffs  ·  Consequence"),
          dark=True, mobile=True),
      onscreen="MORE TASKS: Volume, Coordination, Absorption / MORE JUDGMENT: "
               "Interpretation, Tradeoffs, Consequence",
      script="More tasks can mean volume, coordination, and absorption.",
      purpose="The distinction question two turns on.",
      reveal="MORE TASKS first, held alone 1.5s. MORE JUDGMENT at 2.0s with "
             "the accent.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One restrained accent as MORE JUDGMENT arrives.",
      after="Cut back to camera."),

 dict(id="MG05", file="V6_MG05_Portable_Evidence.png",
      status="REUSE", was="V6_MG05_Portable_Evidence.png",
      why="Artwork unchanged. All three terms and their questions are spoken "
          "verbatim as bullets in the locked script.",
      draw=lambda c: L.readings(c, "Question three", "Evidence that travels.",
          [("RESULT", "What changed?"),
           ("JUDGMENT", "What did you notice or decide?"),
           ("RANGE", "What new context can you handle?")]),
      onscreen="RESULT: what changed? / JUDGMENT: what did you notice or "
               "decide? / RANGE: what new context can you handle?",
      script="I would look for three kinds of evidence: result, judgment, and "
             "range.",
      purpose="The three kinds of evidence, each with the question that "
              "produces it.",
      reveal="One row at a time, 1.0s apart. Hold the complete set.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One subtle click per row.",
      after="Cut back to camera."),

 dict(id="MG06", file="V6_MG06_Decision_Read.png",
      status="COPY UPDATE", was="V6_MG06_Decision_Read.png",
      why="Design unchanged. The first row read \"Strong growth case\"; the "
          "locked script now says the developmental case is strong, which is "
          "also what the master's map row 6 says. The third row deliberately "
          "keeps the spoken qualification MAY BE, rather than the map's "
          "shorter \"Movement, limited growth\", because the script is "
          "explicit that zero or one yes does not make a move wrong.",
      draw=lambda c: L.readings(c, "Reading the three answers",
          "How it comes out.",
          [("THREE YES", "Strong developmental case."),
           ("TWO YES", "Investigate or negotiate."),
           ("ZERO OR ONE YES", "May be movement without much growth.")]),
      onscreen="3 YES: Strong developmental case / 2 YES: Investigate or "
               "negotiate / 0-1 YES: May be movement without much growth",
      script="If all three are yes, different work, expanded judgment, and "
             "evidence that travels, the developmental case is strong.",
      purpose="The read, in the script's own language, without turning a "
              "judgment call into a score.",
      reveal="One row at a time, 1.2s apart. The third row holds alone before "
             "the cut.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One flat accent per row. No triumphant resolve.",
      after="Cut back to camera.",
      treatment_note="No scorecard gamification: no ticks, crosses, scores, "
                     "color coding, progress bars or pass-fail styling. The "
                     "master's own treatment column says the same."),

 dict(id="MG07", file="V6_MG07_Questions_To_Ask.png",
      status="COPY UPDATE", was="V6_MG07_Questions_To_Ask.png",
      why="Design unchanged. The second question read \"Which decisions belong "
          "to me?\"; the locked script asks \"Which decisions belong to this "
          "role?\" during the interview. Corrected so every question on the "
          "card is a sentence the viewer actually hears.",
      draw=lambda c: L.numbered(c, "Ask before you accept",
          ["What problems will I own?",
           "Which decisions belong to this role?",
           "How will success be measured?"], size=54),
      onscreen="What problems will I own? / Which decisions belong to this "
               "role? / How will success be measured?",
      script="Ask the internal hiring manager three things:",
      purpose="Turns the video into something the viewer can take into a "
              "conversation.",
      reveal="One question at a time, 1.1s apart.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One soft accent per question.",
      after="Cut back to camera."),

 dict(id="CTA", file="V6_CTA_Career_Decision_Evidence_Check.png",
      status="REUSE", was="V6_CTA_Career_Decision_Evidence_Check.png",
      why="Artwork unchanged. One product route only, unchanged in the locked "
          "script and in the master's cover table.",
      draw=lambda c: L.cta(c, "Free Career Decision Evidence Check",
          "Read the evidence\nbehind the choice.",
          "For deciding whether to stay, move internally, or leave.",
          "temidayoafonja.com/career-decisions"),
      onscreen="FREE CAREER DECISION EVIDENCE CHECK / "
               "temidayoafonja.com/career-decisions",
      script="the free Career Decision Evidence Check gives you a structured "
             "way to read the evidence behind that choice",
      purpose="The single product route, full screen, with the address large "
              "enough to read on a phone.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Captions off. Never cover the address.",
      sound="One warm accent on the URL.",
      after="Cut back to camera for the bridge into Watch Next."),

 dict(id="WN", file="V6_WATCH_NEXT_Are_You_Growing.png",
      status="REUSE", was="V6_WATCH_NEXT_Are_You_Growing.png",
      why="Artwork unchanged. Routing is unchanged: Video 6 to Video 7.",
      draw=lambda c: L.watch_next(c,
          "Are You Growing,\nor Just Being Given\nMore Work?"),
      onscreen="WATCH NEXT: ARE YOU GROWING, OR JUST BEING GIVEN MORE WORK?",
      script="That is what we are testing next in “Are You Growing, or Just "
             "Being Given More Work?”",
      purpose="Final visual. Right of frame kept clear for the clickable "
              "end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.", sound="None. Let the closing land dry.",
      after="NONE. Final visual."),
]

# ------------------------------------------------------------------- VIDEO 7
V7 = [
 dict(id="MG01", file="V7_MG01_Opening_Consequence.png",
      status="REUSE", was="V7_MG01_Opening_Consequence.png",
      why="Artwork unchanged, and it now matches the master's map row 1 "
          "exactly. The alternate line BUSIER IS NOT BETTER, which the "
          "previous master's map listed on this row and which was dropped for "
          "phone legibility, is no longer in the master's map at all.",
      draw=lambda c: L.statement(c, None,
          "MORE RESPONSIBILITY\nCAN MEAN GROWTH.\n\nIT CAN ALSO MEAN\nYOU ABSORB MORE.",
          None, dark=True, size=76),
      onscreen="MORE RESPONSIBILITY CAN MEAN GROWTH. / IT CAN ALSO MEAN YOU "
               "ABSORB MORE.",
      script="Or maybe the organization has simply learned that you will "
             "absorb more.",
      purpose="The consequence the whole video turns on, before the CAR test "
              "is named.",
      reveal="First statement alone for 1.6s, then the second at 2.2s with a "
             "soft impact.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="Soft impact as the second statement lands.",
      after="Cut back to camera."),

 dict(id="MG02", file="V7_MG02_CAR_Framework.png",
      status="REORDER", was="V7_MG02_CAR_Framework.png",
      why="Artwork unchanged. It moves earlier: the locked script names the "
          "CAR test inside the hook rather than after the setup section, so "
          "this hero frame now lands in the first ninety seconds.",
      draw=lambda c: L.numbered(c, "The CAR test",
          ["COMPLEXITY", "AUTHORITY", "RETURN"], size=76),
      onscreen="C COMPLEXITY / A AUTHORITY / R RETURN",
      script="That is the CAR test: Complexity, Authority, Return.",
      purpose="The hero framework. Returns briefly at each of the three "
              "section changes.",
      reveal="One term at a time, 0.9s apart. Hold the complete set before "
             "cutting away.",
      hold="9 to 11 seconds first time, 3 seconds on each return.",
      captions="Captions off.",
      sound="One restrained accent per term, then a resolve on the set.",
      after="Cut back to camera."),

 dict(id="MG03", file="V7_MG03_Complexity.png",
      status="COPY UPDATE", was="V7_MG03_Complexity.png",
      why="Design unchanged. The left column read \"MORE UNITS OF THE SAME "
          "PROBLEM\" with a support line. The master's map row 3 now simplifies "
          "it to MORE OF THE SAME, which reads faster on a phone and matches "
          "the spoken contrast.",
      draw=lambda c: L.duo(c, "C is for Complexity",
          "Did the problem change, or just the volume?",
          ("MORE OF THE SAME", "Capacity is being used."),
          ("NEW VARIABLES", "Ambiguity · Tradeoffs"),
          mobile=True),
      onscreen="MORE OF THE SAME vs NEW VARIABLES · AMBIGUITY · TRADEOFFS",
      script="First: Did the problem become more complex, or did the volume "
             "simply increase?",
      purpose="The first test, as a comparison the viewer can run on their own "
              "week.",
      reveal="Left column first, held alone 1.4s. Right column at 1.8s with "
             "more visual weight.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One accent as the right column arrives.",
      after="Cut back to camera.",
      treatment_note="The right side carries more visual weight."),

 dict(id="MG04", file="V7_MG04_Authority.png",
      status="REUSE", was="V7_MG04_Authority.png",
      why="Artwork unchanged. All three definitions are spoken verbatim and "
          "match the master's map row 4.",
      draw=lambda c: L.readings(c, "A is for Authority",
          "Three words people use as one.",
          [("RESPONSIBILITY", "What you carry."),
           ("ACCOUNTABILITY", "What you answer for."),
           ("AUTHORITY", "What you can influence or decide.")]),
      onscreen="RESPONSIBILITY: what you carry / ACCOUNTABILITY: what you "
               "answer for / AUTHORITY: what you can influence or decide",
      script="Responsibility is what you are expected to carry. Accountability "
             "is what you will answer for. Authority is what you can influence "
             "or decide.",
      purpose="The distinction the second test turns on.",
      reveal="One row at a time, 1.1s apart. Hold the authority definition "
             "longest.",
      hold="9 to 10 seconds", captions="Captions off.",
      sound="One subtle click per row.",
      after="Cut back to camera."),

 dict(id="MG05", file="V7_MG05_Return.png",
      status="REBUILD", was="V7_MG05_Return.png",
      why="The three return categories are unchanged, but the brief and the "
          "master's map row 5 both require \"Praise alone is not role design\" "
          "to be a large, readable payoff inside this treatment. It was "
          "previously only spoken. The frame now carries it as a final reveal "
          "state at display weight rather than as a quiet footer, which is why "
          "this is a rebuild and not a copy update.",
      draw=lambda c: L.numbered(c, "R is for Return",
          ["CAPABILITY", "EVIDENCE", "RECOGNITION"],
          foot="Praise alone is not role design.",
          foot_size=66, foot_strong=True, size=56, dark=True),
      onscreen="WHAT DID THE WORK RETURN? Capability · Evidence · Recognition "
               "/ PRAISE ALONE IS NOT ROLE DESIGN.",
      script="I would look in three places: capability, evidence, and "
             "recognition.",
      purpose="The third test, ending on the line the brief names as the major "
              "payoff of the section.",
      reveal="One term at a time, 1.0s apart. Then a clear beat, then the "
             "payoff line at display weight at 4.2s. The payoff is its own "
             "reveal state, not a footer that arrives with the list.",
      hold="11 to 13 seconds. The payoff line needs time to land.",
      captions="Captions off.",
      sound="One restrained click per term, then a single soft impact on the "
            "payoff line.",
      after="Cut back to camera.",
      treatment_note="Praise alone is not role design is the emphasis of this "
                     "frame. If the animation cannot hold it as a separate "
                     "reveal state, hold the built frame longer rather than "
                     "shrinking the line."),

 dict(id="MG06", file="V7_MG06_Pattern_Read.png",
      status="COPY UPDATE", was="V7_MG06_Pattern_Read.png",
      why="Design unchanged. The left column read \"Real growth.\", an "
          "unconditional verdict. The locked script says the career case for "
          "growth is visible, and the master's map row 6 says GROWTH CASE "
          "VISIBLE. Corrected.",
      draw=lambda c: L.duo(c, "Reading the pattern",
          "Read the three together.",
          ("COMPLEXITY,\nAUTHORITY\nAND RETURN UP", "Growth case visible."),
          ("VOLUME ONLY UP", "More load."),
          mobile=True),
      onscreen="CAR UP = GROWTH CASE VISIBLE / VOLUME ONLY UP = MORE LOAD",
      script="If Complexity, Authority, and Return are all expanding, the "
             "career case for growth is visible.",
      purpose="The read, in the script's own conditional language.",
      reveal="Left column first, held 1.6s. Right column at 2.0s at equal "
             "weight, not as a penalty.",
      hold="8 to 9 seconds", captions="Captions off.",
      sound="One flat accent per column.",
      after="Cut back to camera.",
      treatment_note="Neutral, not punitive. No red, no warning icons, no "
                     "scoring. The master's own treatment column says keep the "
                     "treatment non-punitive."),

 dict(id="MG07", file="V7_MG07_Scope_Conversation_A.png",
      status="REUSE", was="V7_MG07_Scope_Conversation_A.png",
      why="Artwork unchanged. Both questions are spoken verbatim as bullets in "
          "the scope conversation.",
      draw=lambda c: L.numbered(c, "The scope conversation",
          ["What should remain?",
           "What should come off my plate?"], size=68),
      onscreen="What should remain? / What should come off my plate?",
      script="Which of these responsibilities should remain with me?",
      purpose="The first half of the manager conversation, kept to two "
              "questions so each stays large enough to read on a phone.",
      reveal="One question at a time, 1.2s apart.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="One soft accent per question.",
      after="Cut back to camera."),

 dict(id="MG08", file="V7_MG08_Scope_Conversation_B.png",
      status="REUSE", was="V7_MG08_Scope_Conversation_B.png",
      why="Artwork unchanged. Both questions are spoken verbatim as bullets in "
          "the scope conversation.",
      draw=lambda c: L.numbered(c, "The scope conversation",
          ["Which decisions belong to me?",
           "When will this be reviewed?"], size=68),
      onscreen="Which decisions belong to me? / When will this be reviewed?",
      script="Which decisions need to belong to me for these outcomes?",
      purpose="The second half of the same conversation. Two frames rather "
              "than one four-question grid, for phone readability.",
      reveal="One question at a time, 1.2s apart.",
      hold="7 to 8 seconds", captions="Captions off.",
      sound="One soft accent per question.",
      after="Cut back to camera."),

 dict(id="CTA", file="V7_CTA_Capability_Formation_Field_Kit.png",
      status="REUSE", was="V7_CTA_Capability_Formation_Field_Kit.png",
      why="Artwork unchanged. One product route only, unchanged in the locked "
          "script and in the master's cover table.",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "Read what your work\nis actually building.",
          "See where your options are expanding, and where they are not.",
          "temidayoafonja.com/fieldkit"),
      onscreen="CAPABILITY FORMATION FIELD KIT / temidayoafonja.com/fieldkit",
      script="the Capability Formation Field Kit helps you read the evidence "
             "in your role",
      purpose="The single product route, full screen.",
      reveal="Logomark, headline at 0.6s, URL at 2.0s.",
      hold="8 to 9 seconds", captions="Captions off. Never cover the address.",
      sound="One warm accent on the URL.",
      after="Cut back to camera for the bridge into Watch Next."),

 dict(id="WN", file="V7_WATCH_NEXT_Built_It_From_Scratch.png",
      status="REUSE", was="V7_WATCH_NEXT_Built_It_From_Scratch.png",
      why="Artwork unchanged. Routing is unchanged: Video 7 to Video 8, and "
          "the locked script names that title in the handoff.",
      draw=lambda c: L.watch_next(c,
          "How to Show Your\nImpact at Work\nWhen You Built It\nFrom Scratch"),
      onscreen="WATCH NEXT: HOW TO SHOW YOUR IMPACT AT WORK WHEN YOU BUILT IT "
               "FROM SCRATCH",
      script="In the next video, I will show you how to make that work "
             "visible: “How to Show Your Impact at Work When You Built It "
             "From Scratch.”",
      purpose="Final visual. Right of frame kept clear for the clickable "
              "end-screen element.",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the closing line and past the last word.",
      captions="Captions off.", sound="None.",
      after="NONE. Final visual."),
]

SETS = {4: V4, 5: V5, 6: V6, 7: V7}
TITLES = {
 4: "How to Explain a Career That Looks All Over the Place",
 5: "Why Nobody Can Tell What You're Actually Good At",
 6: "Before You Take an Internal Role, Ask These 3 Questions",
 7: "Are You Growing, or Just Being Given More Work?",
}

# Beats that are deliberately NOT graphics. These are editorial cues, not
# spoken triggers, and the QA pass checks that they are labelled as such.
CAMERA_BEATS = {
4: [("Opening pause",
     "The scripted [Pause.] after \"more like a defense\" is performed on "
     "camera. Hold the frame. It is not dead air and it is not a graphic."),
    ("The modeled 20-second answer",
     "Stay on camera through the whole modeled answer, then hold the scripted "
     "[Hold a short silence.] on camera before \"And stop.\" The silence "
     "demonstrates the point of the section. Do not cut it, do not fill it "
     "with a graphic, and do not shorten it."),
    ("The acquisition beat",
     "The acquisition that eliminated an accepted role now introduces the "
     "objection section. Play it on camera or as one restrained full-screen "
     "B-roll moment. Do not name an employer, invent a loss, or show a "
     "document. MG06 follows on the spoken question.")],
5: [("Opening introduction scene",
     "The outdated-title introduction is a camera and B-roll beat, including "
     "the scripted [Pause.] Do not put a graphic over it."),
    ("Respected but hard to place",
     "\"People can respect your experience and still have no idea what to do "
     "with you\" is carried as a short single-line callout over camera. It is "
     "no longer a full-screen frame, because the two-versions comparison now "
     "occupies that slot."),
    ("The three Receipts",
     "Each Receipt and its qualifier are spoken over camera or restrained "
     "B-roll. The figures and their scope qualifiers never go on screen, "
     "where the qualifier would shrink below phone-readable size.")],
6: [("The offer",
     "The opening offer is a camera beat. MG01 follows it.")],
7: [("The absorption scene",
     "The colleague leaving, the unowned project and \"Can you take this "
     "too?\" are camera and B-roll beats. MG01 follows them.")],
}


def build_cards(n):
    out = []
    for i, s in enumerate(SETS[n], start=1):
        c = Card(i, s["file"])
        s["draw"](c)
        c.notes = "%s  (%s)\n\nStatus: %s\n\nOn screen: %s\n\nScript: %s\n\n" \
                  "Purpose: %s\nHold: %s" % (
            s["file"], s["id"], s["status"], s["onscreen"], s["script"],
            s["purpose"], s["hold"])
        out.append(c)
    return out
