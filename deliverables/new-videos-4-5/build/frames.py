# -*- coding: utf-8 -*-
"""Visual reference frames for the new Videos 4 and 5.

True full-screen motion-graphic reference frames, 1920 x 1080, built on the
approved Capability Formation system. Eight teaching frames per video, plus a
CTA and a Watch Next, exactly as briefed. Callouts are marked as callouts;
everything multi-part is full screen.
"""
import sys, os
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from rdeck import Card

# ------------------------------------------------------------------ VIDEO 4
V4 = [
 dict(id="V01", file="01_Interesting_Background_Hard_To_Place.png",
      draw=lambda c: L.duo(c, "The moment",
          "“Interesting background.”",
          ("SOMETIMES A COMPLIMENT", "Somebody is genuinely interested."),
          ("SOMETIMES NOT", "Somebody cannot quite place you."),
          foot="Experienced. Still hard to categorize.", dark=True),
      script="\"And sometimes it is the sound of a person who cannot quite place "
             "you, buying themselves a second to work out what to do with what "
             "you just said.\"",
      purpose="Names the recognizable moment and the tension underneath it, "
              "without claiming the phrase is always a bad sign.",
      mode="Full-screen motion graphic",
      reveal="Headline first. Left column at 0.6s. Right column at 1.4s. "
             "Bottom line at 2.4s.",
      hold="6 to 8 seconds", captions="Suppress captions for the full hold.",
      sound="One low soft accent on the right column."),

 dict(id="V02", file="02_Category_Compression.png",
      draw=lambda c: L.readings(c, "How range gets misread",
          "They are not reading it.\nThey are sorting it.",
          [("One clear category", "They find it and move on."),
           ("Five possible categories", "They pick the simplest one."),
           ("The one they pick", "Is smaller than you are.")]),
      script="\"When somebody meets your career for the first time, they are not "
             "reading it. They are sorting it.\" through to \"the audit person "
             "gets filed as an audit person, ten years after the audit.\"",
      purpose="Explains the mechanism, so the viewer stops treating this as "
              "somebody else's unfairness and starts treating it as information "
              "they control.",
      mode="Full-screen motion graphic",
      reveal="Headline. Then the three rows one at a time, 0.8s apart. Hold on "
             "the third row.",
      hold="9 to 11 seconds",
      captions="Suppress captions. The right column is the payoff and must not "
               "be covered.",
      sound="One accent per row, descending."),

 dict(id="V03", file="03_The_One_Line_Test.png",
      draw=lambda c: L.numbered(c, "The One-Line Test",
          ["CLAIM   the problem you are the answer to",
           "SPINE   what kept being true underneath",
           "RECEIPTS   three proofs that stand alone"],
          foot="Claim gets you read. Spine makes you make sense. Receipts make "
               "you believable.", size=44),
      script="\"It's called the One-Line Test. Claim. Spine. Receipts.\"",
      purpose="The one named framework in the video. Everything after this "
              "hangs off it.",
      mode="Full-screen motion graphic",
      reveal="Three lines in sequence, 0.7s apart, then the closing line at "
             "3.0s. This frame returns briefly at each section change.",
      hold="8 to 10 seconds on first appearance, 3 seconds on each return.",
      captions="Suppress captions for the full hold.",
      sound="Three ascending accents, then one resolve on the closing line."),

 dict(id="V04", file="04_Claim_Resume_List_Vs_Problem.png",
      draw=lambda c: L.duo(c, "Part one: the Claim",
          "Not a summary. A problem.",
          ("THE RESUME VERSION",
           "Accounting, audit, IT audit, federal governance, privacy, "
           "capability, employee experience."),
          ("THE CLAIM",
           "I get brought in when the evidence is incomplete and a decision "
           "still has to be made."),
          foot="One of these makes the listener sort. One does not."),
      script="\"A Claim is not a summary of your resume. Watch what happens when "
             "I do that version.\" through to \"You need to know what I'm for.\"",
      purpose="The live demonstration. The viewer sees the bad version and the "
              "better version side by side, in Temidayo's own career.",
      mode="Full-screen motion graphic",
      reveal="Left column first, held alone for 3s so it lands as the wrong "
             "answer. Right column at 3.5s. Bottom line at 5.5s.",
      hold="11 to 13 seconds. This is the longest hold in the video.",
      captions="Suppress captions. Both columns are read on screen.",
      sound="Flat on the left column. One clear accent when the right arrives."),

 dict(id="V05", file="05_Spine_Different_Rooms_Same_Work.png",
      draw=lambda c: L.quad(c, "Part two: the Spine",
          "Four rooms. One kind of work.",
          [("AUDIT", "Follow evidence to what the story is missing."),
           ("FEDERAL GOVERNANCE", "Work out what a system cannot see about itself."),
           ("PRIVACY AND CYBER", "Translate exposure into something people can act on."),
           ("LIFE SCIENCES", "Build what nobody has defined yet.")],
          foot="Find what the obvious story is missing. Build enough structure "
               "to decide.", dark=True),
      script="\"The better question is this. What kept being true about the "
             "difficult work people trusted you with?\" through the four rooms.",
      purpose="Shows several contexts at once and then reveals the repeated "
              "work, instead of narrating a chronology.",
      mode="Full-screen motion graphic",
      reveal="All four columns appear together at low opacity, then the nouns "
             "dim and the four descriptions brighten. Bottom line at 4.0s, "
             "which is the actual reveal.",
      hold="10 to 12 seconds",
      captions="Suppress captions for the full hold.",
      sound="One soft accent as the four columns settle, one resolve on the "
            "bottom line."),

 dict(id="V06", file="06_Receipts_Three_Eras.png",
      draw=lambda c: L.readings(c, "Part three: Receipts",
          "Three proofs. Each stands alone.",
          [("Enterprise technology", "Onboarding: one integration measure moved 47 to 75."),
           ("Post-acquisition", "No critical-role departures in the first 90 days."),
           ("Capability work", "1,000+ managers through programs I built or led.")]),
      script="\"A Receipt has to make sense on its own.\" through the three "
             "receipts.",
      purpose="Proves the Claim with evidence from different eras, and models "
              "the scoping language that keeps each one defensible.",
      mode="Full-screen motion graphic",
      reveal="One row at a time, 1.2s apart, each held long enough to read the "
             "scope wording.",
      hold="11 to 13 seconds",
      captions="Suppress captions. The scope qualifiers must be readable.",
      sound="One accent per row, same pitch, deliberately unshowy."),

 dict(id="V07", file="07_Practical_Test_History_Or_Problem.png",
      draw=lambda c: L.duo(c, "A practical test",
          "Listen to their next question.",
          ("IF THEY ASK ABOUT YOUR HISTORY",
           "The Claim is still making them decode."),
          ("IF THEY ASK ABOUT THE PROBLEM", "The Claim is doing its job."),
          foot="“Can I try one sentence on you? Tell me what you think I "
               "actually help with.”"),
      script="\"Say this. Can I try one sentence on you? Tell me what you think "
             "I actually help with.\" through both outcomes.",
      purpose="Hands the viewer an exact sentence to use tonight and a way to "
              "read the result.",
      mode="Full-screen motion graphic",
      reveal="Headline, then the two outcomes 1.0s apart, then the exact "
             "sentence at the bottom at 3.0s and held.",
      hold="9 to 11 seconds",
      captions="Suppress captions. The bottom line is the takeaway sentence.",
      sound="Two accents on the outcomes, one resolve on the sentence."),

 dict(id="V08", file="08_Failure_Modes.png",
      draw=lambda c: L.numbered(c, "When it still does not land",
          ["The Claim is too broad",
           "The Spine is a trait, not a capability",
           "The category does not value your range"],
          foot="None of this erases a weak market, bias, or a real gap in your "
               "experience.", dark=True),
      script="\"Three reasons a Claim doesn't land, and they get fixed in "
             "different ways.\" through the honest limits.",
      purpose="Keeps the promise honest and gives the viewer somewhere to go if "
              "the exercise does not work first time.",
      mode="Full-screen motion graphic",
      reveal="Three lines 0.8s apart. The limits line arrives last, at 3.4s, "
             "and holds alone for two beats.",
      hold="9 to 11 seconds",
      captions="Suppress captions on the limits line in particular.",
      sound="Three flat accents. No resolve. This section should not feel "
            "triumphant."),

 dict(id="V09", file="09_CTA_Write_Your_Claim_Below.png",
      draw=lambda c: L.statement(c, "One thing to do",
          "Write your one-line Claim\nin the comments.",
          "What kind of problem are you the answer to?", dark=True, size=76),
      script="\"And then put it in the comments. I mean that literally. Write "
             "your one-line Claim below.\"",
      purpose="The single CTA. No product ask anywhere in this video.",
      mode="Full screen",
      reveal="Headline, then the question at 1.2s.",
      hold="8 to 10 seconds", captions="Suppress captions.",
      sound="One warm accent."),

 dict(id="V10", file="10_Watch_Next_Change_Jobs.png",
      draw=lambda c: L.watch_next(c,
          "How to Change Jobs\nWithout Starting\nYour Career Over"),
      script="\"Watch How to Change Jobs Without Starting Your Career Over "
             "next.\"",
      purpose="Final visual. Right of frame kept clear for the YouTube end "
              "screen.",
      mode="Full screen, final visual",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the outro lines and past the last word.",
      captions="Suppress captions.", sound="None. Let the outro land dry."),
]

# ------------------------------------------------------------------ VIDEO 5
V5 = [
 dict(id="V01", file="01_Chronology_Dump_Vs_Selected_Story.png",
      draw=lambda c: L.duo(c, "Stop explaining in order",
          "Chronology is not an answer.",
          ("THE CHRONOLOGY DUMP", "Every job, in order, and they build the bridge."),
          ("THE SELECTED STORY", "Only the chapters that make the pattern visible."),
          foot="More detail does not fix a sorting problem.", dark=True),
      script="\"So here's the rule this whole video runs on. Stop explaining "
             "your career in order.\"",
      purpose="Names the failure mode in the first minute and sets the rule the "
              "rest of the video follows.",
      mode="Full-screen motion graphic",
      reveal="Headline, left column at 0.8s, right column at 1.8s, bottom line "
             "at 3.0s.",
      hold="7 to 9 seconds", captions="Suppress captions.",
      sound="One accent on the right column."),

 dict(id="V02", file="02_One_Structure_Chapters_Spine_Next.png",
      draw=lambda c: L.numbered(c, "One structure, three versions",
          ["CHAPTERS   where you have been, compressed",
           "SPINE   what kept being true underneath",
           "NEXT DIRECTION   why the next thing follows"],
          foot="The order never changes. The Spine never changes.", size=44),
      script="\"Chapters. Spine. Next direction.\"",
      purpose="The only structure in the video. It returns above each of the "
              "three scripts.",
      mode="Full-screen motion graphic",
      reveal="Three lines 0.7s apart, closing line at 3.0s. Returns as a short "
             "callout above each script section.",
      hold="8 to 10 seconds first time, 3 seconds on each return.",
      captions="Suppress captions.",
      sound="Three ascending accents, one resolve."),

 dict(id="V03", file="03_Three_Real_Moments.png",
      draw=lambda c: L.readings(c, "Three moments",
          "Same story. Three lengths.",
          [("20 seconds", "“So what do you do?”"),
           ("90 seconds", "“Walk me through your background.”"),
           ("The objection", "“Why so many changes?”")]),
      script="Appears at each version change: \"Version one. Twenty seconds.\" "
             "\"Version two. Ninety seconds.\" \"Version three. The objection.\"",
      purpose="Anchors each script to the actual sentence a viewer will hear in "
              "a room.",
      mode="Full-screen motion graphic",
      reveal="All three rows visible. The active row is at full strength, the "
             "other two dimmed, so the same frame marks all three sections.",
      hold="4 to 6 seconds at each section change.",
      captions="Suppress captions.",
      sound="One accent as the active row brightens."),

 dict(id="V04", file="04_Twenty_Second_Structure.png",
      draw=lambda c: L.numbered(c, "The 20 second version",
          ["I ...   the work pattern",
           "I've done that in ...   two or three contexts",
           "Right now I'm ...   current direction"],
          foot="No title. No employers. Then stop talking.", size=46, dark=True),
      script="\"Here's the template. I ... and then your work pattern.\"",
      purpose="The template is the deliverable. A viewer can fill this in while "
              "watching.",
      mode="Full-screen motion graphic",
      reveal="Three lines 0.9s apart. Bottom line at 3.6s.",
      hold="9 to 11 seconds. Long enough to write down.",
      captions="Suppress captions. This frame gets copied.",
      sound="Three soft accents."),

 dict(id="V05", file="05_Ninety_Second_Structure.png",
      draw=lambda c: L.numbered(c, "The 90 second version",
          ["I started in ..., moved into ..., and then into ...",
           "The thread through all of it is ...   plus two short examples",
           "That's why I'm now focused on ..."],
          foot="Three chapters, not seven. Two examples, not five.", size=40),
      script="\"Here's the template to fill in. Sentence one ...\" through "
             "sentence three.",
      purpose="The second template, in the same shape as the first, so the "
              "viewer sees it is one system and not three tricks.",
      mode="Full-screen motion graphic",
      reveal="Three lines 1.0s apart. Bottom line at 4.0s.",
      hold="11 to 13 seconds. The longest hold in the video.",
      captions="Suppress captions. This frame gets paused and copied.",
      sound="Three soft accents, one resolve."),

 dict(id="V06", file="06_Coherence_Is_Not_A_Perfect_Plan.png",
      draw=lambda c: L.statement(c, None,
          "Do not pretend\nit was planned.",
          "Coherence is not the same thing as inevitability.", dark=True,
          size=82),
      script="\"And do not pretend it was planned.\"",
      purpose="Protects the video from teaching a rehearsed-sounding answer, "
              "and gives the viewer permission not to have had a plan.",
      mode="Full-screen motion graphic",
      reveal="Headline, supporting line at 1.4s.",
      hold="5 to 7 seconds", captions="Suppress captions.",
      sound="One low accent. No resolve."),

 dict(id="V07", file="07_Objection_Structure.png",
      draw=lambda c: L.quad(c, "The objection version",
          "Four parts. No apology.",
          [("HONEST CONTEXT", "One clause. Do not defend."),
           ("THE SPINE", "The same sentence as always."),
           ("WHAT IT BUILT", "The part almost everybody skips."),
           ("WHY THIS NEXT", "The current direction follows.")],
          foot="The changes are not the weak part of the answer. They are the "
               "evidence."),
      script="\"Four parts. Honest context, briefly. The Spine. What the changes "
             "built. Why the current direction follows.\"",
      purpose="Gives a defensible shape for the hardest question, without "
              "teaching apology or concealment.",
      mode="Full-screen motion graphic",
      reveal="Four columns 0.7s apart. Bottom line at 3.6s and held.",
      hold="10 to 12 seconds", captions="Suppress captions.",
      sound="Four flat accents, one resolve on the bottom line."),

 dict(id="V08", file="08_Story_Explains_Proof_Supports.png",
      draw=lambda c: L.duo(c, "Where the story runs out",
          "A story explains. Proof supports.",
          ("THE STORY", "Gets you the next question."),
          ("THE EVIDENCE", "Answers it."),
          foot="A story cannot substitute for evidence you do not have.",
          dark=True),
      script="\"A story explains. Proof supports.\"",
      purpose="Earns the CTA through the teaching instead of bolting it on.",
      mode="Full-screen motion graphic",
      reveal="Headline, two columns 0.9s apart, bottom line at 2.8s.",
      hold="7 to 9 seconds", captions="Suppress captions.",
      sound="Two accents, one resolve."),

 dict(id="V09", file="09_CTA_Keep_The_Proof.png",
      draw=lambda c: L.cta(c, "Keep the Proof",
          "A 60-minute career\nevidence system.",
          "Reconstruct what you did. Name what it built. Record what it "
          "returned.",
          "temidayoafonja.com/keep-the-proof"),
      script="\"It's at temidayoafonja.com/keep-the-proof, and it's linked "
             "below.\"",
      purpose="The single CTA, placed after the teaching that earns it.",
      mode="Full screen",
      reveal="Logomark, then the headline at 0.6s, then the URL at 2.0s.",
      hold="9 to 11 seconds. Hold through the whole CTA line.",
      captions="Suppress captions. Never cover the web address.",
      sound="One warm accent on the URL."),

 dict(id="V10", file="10_Watch_Next_Why_Nobody_Can_Tell.png",
      draw=lambda c: L.watch_next(c,
          "Why Nobody Can Tell\nWhat You're\nActually Good At"),
      script="\"Watch Why Nobody Can Tell What You're Actually Good At next.\"",
      purpose="Final visual. Right of frame kept clear for the YouTube end "
              "screen.",
      mode="Full screen, final visual",
      reveal="Static. No animation on the final card.",
      hold="10 to 14 seconds, through the outro and past the last word.",
      captions="Suppress captions.", sound="None."),
]

SETS = {4: V4, 5: V5}
TITLES = {4: "Why Nobody Can Tell What You're Actually Good At",
          5: "How to Explain a Career That Looks All Over the Place"}


def build_cards(n):
    out = []
    for i, spec in enumerate(SETS[n], start=1):
        c = Card(i, spec["file"])
        spec["draw"](c)
        c.notes = "%s  (%s)\n\nScript match: %s\n\nPurpose: %s\nMode: %s\nHold: %s" % (
            spec["file"], spec["id"], spec["script"], spec["purpose"],
            spec["mode"], spec["hold"])
        out.append(c)
    return out
