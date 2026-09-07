# -*- coding: utf-8 -*-
"""Riverside card sets for Videos 2, 3 and 4.

Every card carries its own placement metadata, so the deck, the PNGs and the
Riverside_Edit_Map all come from this one definition and cannot drift apart.
No em dashes anywhere in this file, in slide copy or in the metadata.
"""
import layouts as L
from rdeck import Card

# ---------------------------------------------------------------- VIDEO 2
V2 = [
 dict(file="01_Hook_Question_Would_Anyone_Outside_Understand.png",
      draw=lambda c: L.statement(c,
          "The question underneath",
          "Would anyone outside\nthis company understand\nwhat I do?",
          dark=True, size=88),
      script="\"And somewhere underneath that, there may be a question you have "
             "never said out loud. Would anyone outside this company actually "
             "understand what I do?\"",
      purpose="Puts the private question on screen so it lands as the viewer's own.",
      display="Full screen", seconds="5 to 7 seconds",
      prompt="Use this slide the moment I ask whether anyone outside the company "
             "would understand what I do. Full screen, long enough to read once, "
             "then cut back to me. Do not put captions over the text."),

 dict(file="02_Valuable_Here_Vs_Legible_Elsewhere.png",
      draw=lambda c: L.duo(c, "Two different questions",
          "Valuable here and legible elsewhere\nare different questions.",
          ("VALUABLE HERE", "Doing good work already answers this."),
          ("LEGIBLE ELSEWHERE", "Doing good work does not answer this."),
          foot="A translation problem, not a value problem."),
      script="\"Valuable here and legible elsewhere are two different questions, "
             "and doing well at work only answers the first one.\"",
      purpose="Carries the central distinction of the video in one comparison.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Bring this slide up when I say that valuable here and legible "
             "elsewhere are two different questions. Hold it full screen while I "
             "explain both sides, then return to me."),

 dict(file="03_Test_One_Remove_The_Company_Nouns.png",
      draw=lambda c: L.duo(c, "Test one",
          "Remove the company nouns.",
          ("BEFORE", "I own the QBR process for this business unit."),
          ("AFTER", "I take incomplete operating data and surface the decision "
                    "people are avoiding."),
          foot="Same person. Same work. One version travels.", dark=True),
      script="\"Here is a before. I own the QBR process for this business unit.\" "
             "through to \"Same person. Same work. One version travels.\"",
      purpose="Shows the rewrite rather than describing it, which is the whole test.",
      display="Full screen", seconds="7 to 9 seconds",
      prompt="Show this slide when I read the before and after sentence. Keep it "
             "full screen through both versions so the viewer can compare them, "
             "then cut back to me."),

 dict(file="04_Test_Two_Outside_Context_Evidence.png",
      draw=lambda c: L.statement(c, "Test two",
          "Find outside-context\nevidence.",
          "Already tested on people who owed you nothing."),
      script="\"The second test is to find outside-context evidence.\"",
      purpose="Names the test and the one reason it counts more than internal praise.",
      display="Full screen", seconds="4 to 6 seconds",
      prompt="Use this slide when I introduce the second test. Full screen for a "
             "few seconds, then back to me while I give the examples."),

 dict(file="05_Test_Three_New_Judgment_Or_Same_Work_Faster.png",
      draw=lambda c: L.duo(c, "Test three",
          "Read the last 90 days.",
          ("NEW JUDGMENT", "Your range got bigger."),
          ("SAME WORK FASTER", "You got quicker at what you knew."),
          foot="Both are fine. Know which one you have."),
      script="\"Is the main change new judgment, or are you mostly doing the same "
             "work faster?\"",
      purpose="Makes the distinction the viewer is most likely to get wrong visible.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Bring this slide in when I ask whether the change is new judgment or "
             "the same work faster. Hold it while I explain both, then return to me."),

 dict(file="06_The_Three_Tests_Read_The_Pattern.png",
      draw=lambda c: L.numbered(c, "The three tests",
          ["Remove the company nouns",
           "Find outside-context evidence",
           "Read the last 90 days"],
          foot="Read the pattern across three or four quarters, not one."),
      script="\"So those are the three. Remove the company nouns. Find "
             "outside-context evidence. Read the last 90 days.\"",
      purpose="Summarizes the teaching and corrects the one-quarter misreading in "
              "the same frame.",
      display="Full screen", seconds="7 to 9 seconds",
      prompt="Show this summary slide when I list the three tests together. Leave "
             "it up while I explain reading the pattern rather than one quarter, "
             "then cut back to me."),

 dict(file="07_None_Of_This_Means_You_Should_Leave.png",
      draw=lambda c: L.statement(c, None,
          "None of this means\nyou should leave.",
          "The most useful moves do not require going anywhere.", dark=True),
      script="\"None of this means you should leave.\"",
      purpose="Holds the nuance of the video so the section does not read as a "
              "push to quit.",
      display="Full screen", seconds="4 to 6 seconds",
      prompt="Use this slide the moment I say that none of this means you should "
             "leave. Full screen briefly, then back to me for the list of things "
             "to do from where you are."),

 dict(file="08_CTA_Capability_Formation_Field_Kit.png",
      draw=lambda c: L.cta(c, "Capability Formation Field Kit",
          "Is your job still\nbuilding you?",
          "Private. Nobody at your company sees it.",
          "temidayoafonja.com/fieldkit"),
      script="\"If you want a fuller read than three tests can give you, I made the "
             "Capability Formation Field Kit.\"",
      purpose="Supports the CTA and puts the link on screen while I say it.",
      display="CTA", seconds="6 to 8 seconds",
      prompt="Show this CTA slide while I describe the Field Kit. Keep it up until "
             "I finish saying it is linked below. Do not cover the web address."),

 dict(file="09_Watch_Next_3_Things_Before_Quitting.png",
      draw=lambda c: L.watch_next(c,
          "3 Things to Do\nBefore Quitting\nYour Job"),
      script="\"Watch 3 Things to Do Before Quitting Your Job next.\"",
      purpose="Supports the Watch Next ending, with the right of the frame left "
              "clear for the YouTube end screen.",
      display="Watch Next", seconds="6 to 10 seconds",
      prompt="Use this as the closing slide when I say to watch 3 Things to Do "
             "Before Quitting Your Job next. Keep the right side of the screen "
             "clear so the YouTube end screen can sit there."),
]

# ---------------------------------------------------------------- VIDEO 3
V3 = [
 dict(file="01_Once_You_Leave_Access_Changes.png",
      draw=lambda c: L.statement(c, "Before you resign",
          "The day you leave,\naccess changes.",
          "Systems close. Files close. People scatter.", dark=True),
      script="\"The day you leave, a lot of things go at once.\"",
      purpose="Establishes the premise the whole video rests on.",
      display="Full screen", seconds="5 to 7 seconds",
      prompt="Bring this slide up when I say that the day you leave, a lot of "
             "things go at once. Full screen while I list what closes, then back "
             "to me."),

 dict(file="02_If_Your_Safety_Is_At_Risk_Do_Not_Wait.png",
      draw=lambda c: L.statement(c, "One exception first",
          "If your safety is at risk,\nthis is not a reason to wait.",
          "Protect yourself and get proper support first.", size=76),
      script="\"If your health or your safety is at risk, or you are facing "
             "harassment or discrimination, none of this is a reason to wait.\"",
      purpose="Puts the safety exception on screen, where a viewer in that "
              "situation will not miss it.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Show this slide for the whole safety exception, from health and "
             "safety through to getting proper support. Do not shorten it and do "
             "not put captions over the text."),

 dict(file="03_Check_One_Preserve_The_Evidence.png",
      draw=lambda c: L.duo(c, "Check one",
          "Preserve the evidence.",
          ("YOURS TO KEEP", "Your own account of your own work, in your own words."),
          ("NOT YOURS TO TAKE", "Anything belonging to your employer or anyone else."),
          foot="If you have to think about it, it is not yours."),
      script="\"So the first thing is to preserve the evidence.\"",
      purpose="Draws the line clearly, which matters because this is the part that "
              "gets misread in both directions.",
      display="Full screen", seconds="7 to 9 seconds",
      prompt="Use this slide across the whole first check, while I explain what you "
             "are entitled to keep and what you never take. Hold it long enough to "
             "read both sides."),

 dict(file="04_Check_Two_Name_What_The_Work_Built.png",
      draw=lambda c: L.quad(c, "Check two",
          "Name what the work built.",
          [("PROBLEM", "What was being solved?"),
           ("CONSTRAINT", "What made it hard?"),
           ("JUDGMENT", "What did you decide?"),
           ("OUTCOME", "What changed?")],
          foot="Judgment is the one almost everybody leaves out.", dark=True),
      script="\"So for each piece of work you wrote down, answer four things.\"",
      purpose="Holds the four-part framework in view while I work through it.",
      display="Full screen", seconds="8 to 10 seconds",
      prompt="Show this framework slide while I go through the four questions. "
             "Keep it up for all four, then return to me for the warning about "
             "claiming only what you can support."),

 dict(file="05_Check_Three_Test_The_Next_Move.png",
      draw=lambda c: L.duo(c, "Check three",
          "Test the next move.",
          ("USES SOMETHING PROVEN", "Otherwise it is a restart, not a move."),
          ("BUILDS SOMETHING NEW", "Otherwise you repeat this chapter elsewhere."),
          foot="The moves that work do both."),
      script="\"The third thing is to test the next move.\"",
      purpose="Shows both halves of the test at once, which is the point of it.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Bring this slide in when I introduce the third check and hold it "
             "while I explain both questions, then cut back to me."),

 dict(file="06_The_Three_Checks.png",
      draw=lambda c: L.numbered(c, "The three checks",
          ["Preserve the evidence",
           "Name what the work built",
           "Test the next move"],
          foot="Do them while you still have access."),
      script="\"So those are the three. Preserve the evidence. Name what the work "
             "built. Test the next move.\"",
      purpose="Summarizes the teaching in the order I say it.",
      display="Full screen", seconds="5 to 7 seconds",
      prompt="Use this summary slide when I list the three checks together. A few "
             "seconds full screen, then back to me."),

 dict(file="07_How_The_Evidence_Reads.png",
      draw=lambda c: L.readings(c, "How it reads",
          "Three ways this comes out.",
          [("All three clear", "You are leaving with a case."),
           ("Evidence but no fit", "The problem may be the direction."),
           ("Cannot fill it in", "Sit with that for a week.")]),
      script="\"And here is how they tend to read.\"",
      purpose="Gives the viewer a way to read their own result without me repeating "
              "all three outcomes on camera.",
      display="Full screen", seconds="8 to 10 seconds",
      prompt="Show this slide while I explain the three ways the checks tend to "
             "read. Keep it up for all three, then return to me."),

 dict(file="08_CTA_Career_Decision_Evidence_Check.png",
      draw=lambda c: L.cta(c, "Career Decision Evidence Check",
          "Read what this chapter\nactually built.",
          "It is private, and it is yours.",
          "temidayoafonja.com/career-decisions"),
      script="\"If you want help doing this properly, I made the Career Decision "
             "Evidence Check.\"",
      purpose="Supports the CTA and shows the link while I say it.",
      display="CTA", seconds="6 to 8 seconds",
      prompt="Show this CTA slide while I describe the Career Decision Evidence "
             "Check, through to it being linked below. Do not cover the web address."),

 dict(file="09_Watch_Next_Change_Jobs_Without_Starting_Over.png",
      draw=lambda c: L.watch_next(c,
          "How to Change Jobs\nWithout Starting\nYour Career Over"),
      script="\"Watch How to Change Jobs Without Starting Your Career Over next.\"",
      purpose="Supports the Watch Next ending, with the end-screen area kept clear.",
      display="Watch Next", seconds="6 to 10 seconds",
      prompt="Use this as the closing slide when I say to watch How to Change Jobs "
             "Without Starting Your Career Over next. Keep the right side clear for "
             "the YouTube end screen."),
]

# ---------------------------------------------------------------- VIDEO 4
V4 = [
 dict(file="01_The_Chapters_The_Titles_Changed.png",
      draw=lambda c: L.numbered(c, "Roughly eighteen years",
          ["Accounting and audit",
           "Cybersecurity and privacy",
           "People and employee experience",
           "Enterprise transformation"],
          foot="The titles changed. The capability kept accumulating.",
          dark=True, size=58),
      script="\"Accounting and audit. Then cybersecurity and privacy. Then people "
             "and employee experience. Then enterprise transformation.\"",
      purpose="Lets the viewer see the chapters while I say them, so the story does "
              "not have to be held by ear.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Show this slide while I name my four chapters. Keep it up until I "
             "finish saying enterprise transformation, then cut back to me."),

 dict(file="02_Chronology_Vs_Portability.png",
      draw=lambda c: L.duo(c, "Two different things",
          "Chronology is not portability.",
          ("CHRONOLOGY", "Where you have been."),
          ("PORTABILITY", "What traveled with you."),
          foot="Told as a list, every move sounds like a departure."),
      script="\"Chronology is where you have been. Portability is what traveled "
             "with you. They are not the same thing.\"",
      purpose="Carries the distinction the rest of the video depends on.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Bring this slide up when I say chronology is where you have been and "
             "portability is what traveled with you. Hold it while I explain the "
             "difference, then return to me."),

 dict(file="03_Do_Not_Invent_The_Plan.png",
      draw=lambda c: L.statement(c, None,
          "Do not invent the plan.",
          "It does not survive a follow-up question.", dark=True),
      script="\"We go back and invent the plan, a fifteen-year strategy that you "
             "were absolutely not running at the time. Do not do that.\"",
      purpose="Makes the single strongest warning in the video memorable.",
      display="Full screen", seconds="4 to 6 seconds",
      prompt="Use this slide when I warn against inventing the plan. Full screen "
             "for a few seconds, then straight back to me."),

 dict(file="04_The_Three_Sentences.png",
      draw=lambda c: L.numbered(c, "The three sentences",
          ["My career has moved across...",
           "Across those chapters, I kept being asked to...",
           "That is why I am now focused on..."],
          foot="Where you have been. What repeated. Where that leads.", size=52),
      script="\"Three sentences do that. Not a story. Three sentences.\"",
      purpose="Gives the viewer the actual template, which is the most reusable "
              "thing in the video.",
      display="Full screen", seconds="8 to 10 seconds",
      prompt="Show this slide when I introduce the three sentences, and bring it "
             "back at the end when I say the whole thing out loud. Hold it long "
             "enough to read all three."),

 dict(file="05_Sentence_Two_Look_Past_The_Nouns.png",
      draw=lambda c: L.struck(c, "Sentence two",
          "Look past the nouns.",
          ["Job titles", "Company language", "Industry vocabulary"],
          "What did you notice, decide, solve or change?"),
      script="\"Look past the nouns. Underneath the industries and the job titles, "
             "what were you actually doing?\"",
      purpose="Shows what to discard and what to look for, which is hard to hold "
              "by ear.",
      display="Full screen", seconds="7 to 9 seconds",
      prompt="Use this slide when I say to look past the nouns. Keep it up while I "
             "explain how to find the repeated work, then cut back to me."),

 dict(file="06_Two_Things_Not_To_Claim.png",
      draw=lambda c: L.duo(c, "The honesty boundary",
          "Two things not to claim.",
          ("EVERY MOVE WAS INTENTIONAL", "Some of mine were not."),
          ("EVERYTHING TRANSFERRED", "Every move came with real learning."),
          foot="Saying so is what makes the rest of it credible."),
      script="\"Do not claim every move was intentional.\" through to \"And do not "
             "claim that everything transferred, because it did not.\"",
      purpose="Holds both halves of the honesty boundary side by side.",
      display="Full screen", seconds="7 to 9 seconds",
      prompt="Show this slide across the honesty boundary section, while I say not "
             "to claim every move was intentional and not to claim everything "
             "transferred."),

 dict(file="07_The_Test_What_Am_I_Good_At.png",
      draw=lambda c: L.readings(c, "Test it before you need it",
          "Ask: what do you think\nI am good at?",
          [("A list of industries", "Sentence two is not working yet."),
           ("A kind of problem", "It is working.")]),
      script="\"Then ask them one question. What do you think I am good at?\"",
      purpose="Gives the viewer the test and how to read the answer in one frame.",
      display="Full screen", seconds="6 to 8 seconds",
      prompt="Bring this slide up when I tell you to ask somebody what they think "
             "you are good at. Hold it while I explain both answers, then return "
             "to me."),

 dict(file="08_CTA_Career_Evidence_Starter.png",
      draw=lambda c: L.cta(c, "Free Career Evidence Starter",
          "One accomplishment.\nOne portable proof line.",
          "About 10 to 15 focused minutes.",
          "temidayoafonja.com/career-evidence-starter"),
      script="\"That is what the free Career Evidence Starter is for. About 10 to "
             "15 focused minutes, one real accomplishment, turned into a proof line "
             "you can use.\"",
      purpose="Supports the CTA and shows the link while I say it.",
      display="CTA", seconds="6 to 8 seconds",
      prompt="Show this CTA slide while I describe the Career Evidence Starter, "
             "through to it being linked below. Do not cover the web address."),

 dict(file="09_Watch_Next_Should_I_Make_An_Internal_Move.png",
      draw=lambda c: L.watch_next(c,
          "Should I Make an\nInternal Move?\n3 Questions to Decide",
          playlist="Playlist: Career Portability: Career Pivots, "
                   "Internal Moves and Growth"),
      script="\"Watch Should I Make an Internal Move? 3 Questions to Decide next.\"",
      purpose="Supports the Watch Next ending, with the end-screen area kept clear.",
      display="Watch Next", seconds="6 to 10 seconds",
      prompt="Use this as the closing slide when I say to watch Should I Make an "
             "Internal Move? next. Keep the right side clear for the YouTube end "
             "screen."),
]

SETS = {2: V2, 3: V3, 4: V4}

TITLES = {2: "Is Your Job Making You Less Marketable?",
          3: "3 Things to Do Before Quitting Your Job",
          4: "How to Explain Your Career Change"}


def build_cards(n):
    out = []
    for i, spec in enumerate(SETS[n], start=1):
        c = Card(i, spec["file"])
        spec["draw"](c)
        c.notes = "%s\n\nScript match: %s\n\nPurpose: %s\nDisplay: %s\nScreen time: %s" % (
            spec["file"], spec["script"], spec["purpose"], spec["display"],
            spec["seconds"])
        out.append(c)
    return out
