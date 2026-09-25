# -*- coding: utf-8 -*-
"""The exact slide list from Section 3 of the production brief.

9 slides for Video 1, 8 for Video 2, 7 for Video 3. The "text on slide" column
is reproduced as written; it is split into a headline and supporting lines so
one idea sits on each slide with the headline at 60 pt or more.

kind drives the layout:
  title     title card, two stacked lines
  roadmap   numbered or listed steps
  step      headline plus supporting lines
  list      headline plus a plain list
  quote     headline plus a quoted script
  rapid     the rapid-fire questions, one per beat
  end       end card, statement plus link plus next
"""

SLIDES = {
1: [
 dict(no=1, name="V1_01_TITLE_CARD", kind="title", at="0:00",
      when="0:00, behind the hook or right after it",
      label="Title card",
      head="How to Get a New Job in 2027",
      sub="When You Have 10+ Years of Experience"),
 dict(no=2, name="V1_02_ROADMAP", kind="roadmap", at="0:30",
      when="During the roadmap", label="Roadmap",
      head="5 steps before your résumé",
      items=["Decide the move.", "Build your evidence.",
             "Translate what travels.", "Become referable.",
             "Name the gap."],
      foot="+ Rapid-fire round"),
 dict(no=3, name="V1_03_STEP_1", kind="list", at="2:00", when="2:00",
      label="Step 1",
      head="Decide what kind of move you are making",
      sub="Seven options",
      items=["Remain and deepen", "Translate what is built",
             "Widen exposure", "Test portability",
             "Repair the conditions", "Prepare for exit",
             "Seek an outside perspective"]),
 dict(no=4, name="V1_04_STEP_2", kind="list", at="3:30", when="3:30",
      label="Step 2",
      head="Build your evidence before your résumé",
      sub="A Proof Line has five parts",
      items=["The situation", "Your part", "The scope", "What changed",
             "The evidence you may keep"]),
 dict(no=5, name="V1_05_STEP_3", kind="list", at="5:30", when="5:30",
      label="Step 3", head="Translate what travels", sub=None,
      items=["What travels?", "What does not?", "What can you prove?",
             "What must you relearn?"]),
 dict(no=6, name="V1_06_STEP_4", kind="step", at="7:00", when="7:00",
      label="Step 4", head="Become referable",
      lines=["Write one sentence someone else could repeat for you.",
             "Send it to five people who have seen your work."]),
 dict(no=7, name="V1_07_STEP_5", kind="quote", at="8:45", when="8:45",
      label="Step 5", head="Name the gap before they do",
      quote="Here is what I have done that this role asks for. Here is what "
            "I would still need to learn, and how."),
 dict(no=8, name="V1_08_RAPID_FIRE", kind="rapid", at="10:00",
      when="10:00, one question per beat", label="Rapid-fire round",
      head="Rapid-fire round",
      items=["My company may be sold.", "I survived two reorgs.",
             "Should I take a lower title?",
             "“You need direct experience.”",
             "My offer was rescinded."]),
 dict(no=9, name="V1_09_END_CARD", kind="end", at="11:30", when="11:30",
      label="End card",
      head="Starting as a learner is not the same as starting from zero.",
      link="Free Career Evidence Starter: "
           "temidayoafonja.com/career-evidence-starter",
      nxt="Next: Video 2"),
],
2: [
 dict(no=1, name="V2_01_TITLE_CARD", kind="title", at="0:00", when="0:00",
      label="Title card",
      head="How to Answer “You Don’t Have Direct Experience”",
      sub="When You Have 10+ Years"),
 dict(no=2, name="V2_02_ROADMAP", kind="roadmap", at="0:20",
      when="During the roadmap", label="Roadmap", head="What we will cover",
      items=["What the employer is deciding.",
             "Why transferable skills are not enough.",
             "The four questions.", "One Proof Line.", "Name the gap.",
             "Your script."],
      foot=None),
 dict(no=3, name="V2_03_WHAT_THEY_DECIDE", kind="step", at="0:40",
      when="0:40", label="What they are deciding",
      head="Can enough of your experience be trusted here?",
      lines=[]),
 dict(no=4, name="V2_04_SAME_LABEL", kind="step", at="2:00", when="2:00",
      label="Same label, different experience",
      head="“Strategic thinking” could mean",
      lines=["Prepared the analysis,",
             "or made the trade-off and carried the consequence."]),
 dict(no=5, name="V2_05_FOUR_QUESTIONS", kind="list", at="3:30",
      when="3:30", label="The four questions",
      head="The four questions", sub=None,
      items=["What travels?", "What does not?", "What can you prove?",
             "What must you relearn?"]),
 dict(no=6, name="V2_06_ONE_PROOF_LINE", kind="list", at="5:30",
      when="5:30", label="One Proof Line", head="One Proof Line",
      sub="Show one completed example",
      items=["Situation", "Your part", "Scope", "What changed", "Evidence"]),
 dict(no=7, name="V2_07_THE_SCRIPT", kind="script", at="8:15", when="8:15",
      label="The script", head="The script",
      rows=[("Acknowledge",
             "“You’re right that I haven’t held this exact "
             "title.”"),
            ("Prove",
             "“Here’s what I have done that this role asks "
             "for.”"),
            ("Name the gap",
             "“Here’s what I would still need to learn, and how I "
             "would learn it in the first 90 days.”")]),
 dict(no=8, name="V2_08_END_CARD", kind="end", at="8:45", when="End",
      label="End card",
      head="Adjacent experience still has to be read.",
      link="Career Evidence Starter: "
           "temidayoafonja.com/career-evidence-starter",
      nxt="Next: Video 3"),
],
3: [
 dict(no=1, name="V3_01_TITLE_CARD", kind="title", at="0:00", when="0:00",
      label="Title card", head="How to Get Referred",
      sub="When Your Network Is Thin"),
 dict(no=2, name="V3_02_ROADMAP", kind="roadmap", at="0:20",
      when="During the roadmap", label="Roadmap", head="Three steps",
      items=["Become easy to describe.", "Tell five people.",
             "Reconnect with people who saw your work."],
      foot="For leaders: who referrals leave out."),
 dict(no=3, name="V3_03_WHAT_A_REFERRAL_NEEDS", kind="list", at="1:00",
      when="1:00", label="What a referral needs",
      head="What a referral needs", sub=None,
      items=["Trust in you.",
             "A way to describe what you do well."]),
 dict(no=4, name="V3_04_STEP_1", kind="step", at="2:15", when="2:15",
      label="Step 1", head="Become easy to describe",
      lines=["Write one sentence someone else could repeat for you.",
             "Drop the internal title and company language."]),
 dict(no=5, name="V3_05_STEP_2", kind="quote", at="3:45", when="3:45",
      label="Step 2", head="Tell five people",
      quote="I’m exploring roles where I can [problem you solve]. "
            "Recently I [Proof Line]. If you hear of something close, "
            "I’d value a referral."),
 dict(no=6, name="V3_06_STEP_3", kind="list", at="5:00", when="5:00",
      label="Step 3", head="Reconnect", sub=None,
      items=["Former managers", "Peers", "Clients", "Classmates",
             "Community and church leaders who watched you lead"]),
 dict(no=7, name="V3_07_END_CARD", kind="end", at="7:30", when="7:30",
      label="End card",
      head="You need a few people who can describe what you do well.",
      link="Career Evidence Starter: "
           "temidayoafonja.com/career-evidence-starter",
      nxt="Share the playlist"),
],
}

# --------------------------------------------------------------- shorts
# The four clips named in the playlist document. Video 1 gets two, Videos 2
# and 3 get one each, which sits inside the brief's 1 to 2 per video.
SHORTS = {
1: [
 dict(no=1, name="V1_SHORT_1_MEMORY_IS_NOT_A_RECORD",
      source="Video 1, Step 2: Build your evidence before your résumé",
      pull="around 3:30 to 4:15", target="about 45 seconds",
      spoken="“Your memory is not a record. Write one entry this "
             "week.”",
      captions=["YOUR MEMORY IS NOT A RECORD",
                "A PROOF LINE HAS FIVE PARTS",
                "SITUATION. YOUR PART. SCOPE.",
                "WHAT CHANGED. THE EVIDENCE YOU MAY KEEP.",
                "WRITE ONE ENTRY THIS WEEK"]),
 dict(no=2, name="V1_SHORT_2_LOWER_TITLE",
      source="Video 1, rapid-fire round",
      pull="around 10:00 to 10:30", target="about 30 seconds",
      spoken="“Should I take a lower title?” Look at what the work "
             "will make you practice. A smaller title with bigger practice "
             "can be the stronger move.",
      captions=["“SHOULD I TAKE A LOWER TITLE?”",
                "LOOK AT WHAT THE WORK WILL MAKE YOU PRACTICE",
                "A SMALLER TITLE WITH BIGGER PRACTICE",
                "CAN BE THE STRONGER MOVE"]),
],
2: [
 dict(no=1, name="V2_SHORT_1_THE_SCRIPT",
      source="Video 2, Your script",
      pull="around 8:15 to 8:55", target="about 40 seconds",
      spoken="“You’re right that I haven’t held this exact "
             "title. Here’s what I have done that this role asks for. "
             "The part I would still need to learn is this, and here is how "
             "I would learn it in the first ninety days.”",
      captions=["“YOU’RE RIGHT THAT I HAVEN’T HELD THIS "
                "EXACT TITLE.”",
                "“HERE’S WHAT I HAVE DONE THAT THIS ROLE ASKS "
                "FOR.”",
                "“THE PART I WOULD STILL NEED TO LEARN IS THIS,”",
                "“AND HERE IS HOW I WOULD LEARN IT IN THE FIRST "
                "NINETY DAYS.”",
                "MOST PEOPLE SKIP THE LAST PART"]),
],
3: [
 dict(no=1, name="V3_SHORT_1_A_FEW_PEOPLE",
      source="Video 3, close",
      pull="around 7:30 to 8:15", target="about 45 seconds",
      spoken="You do not need a big network. You need a few people who can "
             "describe what you do well.",
      captions=["YOU DO NOT NEED A BIG NETWORK",
                "YOU NEED A FEW PEOPLE",
                "WHO CAN DESCRIBE WHAT YOU DO WELL",
                "WRITE ONE SENTENCE THEY COULD REPEAT",
                "SEND IT TO FIVE PEOPLE"]),
],
}

# ------------------------------------------------------- b-roll, takes
BROLL = [
 "Hands writing a Proof Line on paper.",
 "The Career Evidence Starter page on a laptop.",
 "A notebook with the four questions.",
 "A quiet desk shot for the rapid-fire round transitions.",
]
