# -*- coding: utf-8 -*-
"""Per-video audit text: what survived the reduction, what did not, and why."""

ORIGINALS = {2: (13, 23), 3: (13, 27), 4: (11, 26)}

AUDIT = {
2: dict(
  keep=[
    ("Main 2  Two different questions", "KEEP", "02_Valuable_Here_Vs_Legible_Elsewhere.png",
     "The central distinction of the video. Kept as a two-way comparison."),
    ("Main 4  Test one, before and after", "KEEP", "03_Test_One_Remove_The_Company_Nouns.png",
     "The rewrite is the teaching. Shown as one completed before and after."),
    ("Main 6  Test two, three evidence types", "MERGE", "04_Test_Two_Outside_Context_Evidence.png",
     "The three examples are spoken clearly on camera. The card keeps only the "
     "name of the test and the one reason it counts."),
    ("Main 8  Test three, three questions", "MERGE", "05_Test_Three_New_Judgment_Or_Same_Work_Faster.png",
     "Reduced to the comparison a viewer is most likely to get wrong."),
    ("Main 9  The three tests", "MERGE", "06_The_Three_Tests_Read_The_Pattern.png",
     "Merged with main 10 so the summary and the pattern correction hold the "
     "screen together instead of changing after about twenty seconds."),
    ("Main 10  Reading the pattern", "MERGE", "06_The_Three_Tests_Read_The_Pattern.png",
     "Merged into the summary card, above."),
    ("Main 11  Before you leave, four actions", "MERGE", "07_None_Of_This_Means_You_Should_Leave.png",
     "All four actions are spoken. The card carries only the reassurance, so "
     "the section cannot read as a push to quit."),
    ("Main 12  Field Kit", "CTA", "08_CTA_Capability_Formation_Field_Kit.png", "Approved CTA and URL."),
    ("Main 13  Watch Next", "WATCH NEXT", "09_Watch_Next_3_Things_Before_Quitting.png",
     "Approved destination. Right of frame kept clear for the end screen."),
  ],
  removed=[
    ("Main 1  Title card", "REMOVE",
     "A title card is presentation furniture. Temidayo on camera opens the video."),
    ("Main 3, 5, 7  Section title cards for tests one, two and three", "REMOVE",
     "Three near-identical THREE MARKETABILITY TESTS cards that differ only by "
     "which test is highlighted. Each test now has one card that does the work."),
    ("Reveal 4 to 5  Test one build", "REMOVE", "Partial before-only state. Only the completed version is kept."),
    ("Reveal 7 to 10  Test two build", "REMOVE", "Progressive one, two and three item states, plus a repeat of the final state."),
    ("Reveal 12 to 15  Test three build", "REMOVE", "Progressive question-by-question states."),
    ("Reveal 18 to 21  Before you leave build", "REMOVE", "Progressive action-by-action states."),
  ],
  added=[
    ("01_Hook_Question_Would_Anyone_Outside_Understand.png",
     "The hook question had no slide in the presentation deck because Temidayo "
     "asked it straight to camera over a title card. As a Riverside cutaway it "
     "makes the private question land as the viewer's own. Wording is verbatim "
     "from the approved script."),
  ],
  conflicts=[
    ("Main 4, the after sentence",
     "The deck reads \"I combine incomplete operating data, surface the decision "
     "leaders are avoiding, and create a shared view of what needs to happen.\" "
     "The approved v5.1.1 script reads \"I take incomplete operating data, "
     "surface the decision leaders are avoiding, and get a group to a shared "
     "view of what happens next.\" The two have never matched.",
     "The Riverside card uses a shortened form of the script wording, because "
     "24 words does not read in six seconds on video: \"I take incomplete "
     "operating data and surface the decision people are avoiding.\" Temidayo "
     "says the full sentence on camera. If you would rather the card carried "
     "her exact words in full, say so and I will set it at a smaller size."),
  ]),

3: dict(
  keep=[
    ("Main 2  Once you leave, access changes", "KEEP", "01_Once_You_Leave_Access_Changes.png",
     "The premise the whole video rests on."),
    ("Main 2  Safety exception", "KEEP", "02_If_Your_Safety_Is_At_Risk_Do_Not_Wait.png",
     "Split onto its own card. A viewer in that situation should not have to "
     "catch it as a footnote under another point."),
    ("Main 4  Check one, yours to keep and not yours to take", "MERGE", "03_Check_One_Preserve_The_Evidence.png",
     "The deck lists eleven items across the two columns. Reduced to the "
     "principle on each side, because Temidayo reads the detail aloud."),
    ("Main 6  Check two, four-part framework", "KEEP", "04_Check_Two_Name_What_The_Work_Built.png",
     "A named four-part framework, kept whole. Four columns rather than bullets."),
    ("Main 8  Check three", "MERGE", "05_Check_Three_Test_The_Next_Move.png",
     "Kept as the two-way test. The three sub-questions are spoken."),
    ("Main 9  The three checks", "KEEP", "06_The_Three_Checks.png", "Summary, in the order she says it."),
    ("Main 10  Reading the evidence", "MERGE", "07_How_The_Evidence_Reads.png",
     "Rebuilt from the approved script. See the conflict noted below."),
    ("Main 12  Career Decision Evidence Check", "CTA", "08_CTA_Career_Decision_Evidence_Check.png",
     "Approved CTA and URL. Gating architecture unchanged."),
    ("Main 13  Watch Next", "WATCH NEXT", "09_Watch_Next_Change_Jobs_Without_Starting_Over.png",
     "Approved destination. Right of frame kept clear for the end screen."),
  ],
  removed=[
    ("Main 1  Title card", "REMOVE", "Presentation furniture."),
    ("Main 3, 5, 7  Section title cards for checks one, two and three", "REMOVE",
     "Three near-identical THREE CHECKS BEFORE YOU RESIGN cards."),
    ("Main 11  Answer these three first", "REMOVE",
     "A third restatement of the same three checks, after main 9 and main 10. "
     "One summary card is enough."),
    ("Reveal builds across checks one, two and three", "REMOVE",
     "Fourteen progressive states. Only completed versions are kept."),
  ],
  added=[],
  conflicts=[
    ("Main 10, Reading the evidence",
     "The existing deck offers three outcomes: Leave, Reposition inside, and "
     "Build a bridge. The approved v5.1.1 script offers three different ones: "
     "if all three come out clear you are leaving with a case; if the evidence "
     "is there but the next move does not use it, the problem may be the "
     "direction; and if you cannot fill in the evidence at all, sit with that "
     "for a week. These are not the same taxonomy.",
     "The Riverside card follows the approved script, because the script is the "
     "locked v5.1.1 artifact and the deck predates it. This needs your decision: "
     "either the deck is stale and should be corrected separately, or the "
     "Leave / Reposition / Bridge framing is still wanted and the script is the "
     "one that moved. I have changed nothing in either original."),
  ]),

4: dict(
  keep=[
    ("Main 1  The four chapters", "KEEP", "01_The_Chapters_The_Titles_Changed.png",
     "The lived-story anchor. All four chapters now listed, rather than three "
     "with the fourth in a caption."),
    ("Main 2  Chronology and portability", "KEEP", "02_Chronology_Vs_Portability.png",
     "The distinction the rest of the video depends on."),
    ("Main 8  Do not invent a perfect plan", "KEEP", "03_Do_Not_Invent_The_Plan.png",
     "The strongest warning in the video, reduced to the line itself."),
    ("Main 7  The three sentence stems", "KEEP", "04_The_Three_Sentences.png",
     "The most reusable thing in the video. Kept verbatim."),
    ("Main 5  Look past the nouns", "KEEP", "05_Sentence_Two_Look_Past_The_Nouns.png",
     "Kept as the struck-through visual, which is hard to hold by ear."),
    ("Main 3, 4, 6  Numbered sentence-one, sentence-two, sentence-three cards", "MERGE",
     "04_The_Three_Sentences.png",
     "Three separate build cards for a three-sentence framework. The completed "
     "framework card replaces all three."),
    ("Main 10  Career Evidence Starter", "CTA", "08_CTA_Career_Evidence_Starter.png",
     "Approved CTA and URL."),
    ("Main 11  Watch Next", "WATCH NEXT", "09_Watch_Next_Should_I_Make_An_Internal_Move.png",
     "Approved destination and playlist. Right of frame kept clear."),
  ],
  removed=[
    ("Reveal builds across the three sentences", "REMOVE",
     "Progressive states that differ by one line each."),
    ("Main 9  Three checking questions", "REMOVE",
     "Replaced by a card built from the approved script. See the conflict below."),
  ],
  added=[
    ("06_Two_Things_Not_To_Claim.png",
     "The honesty boundary is a substantial passage in the approved script with "
     "no slide in the existing deck. It is the argument that makes the rest "
     "credible, and it reads well as a two-way card."),
    ("07_The_Test_What_Am_I_Good_At.png",
     "The approved script's test, which the existing deck does not carry."),
  ],
  conflicts=[
    ("Main 9, the three checking questions",
     "The deck asks: can a stranger hear why the next move follows; does it show "
     "ability, not only interest; is there evidence behind each verb. None of "
     "these three appears in the approved v5.1.1 script. The script's test is "
     "to say the three sentences to somebody outside your field and ask them "
     "\"what do you think I am good at?\", then read whether the answer is a "
     "list of industries or a kind of problem.",
     "The Riverside card follows the approved script. If you want the deck's "
     "three questions kept as well, they need to go back into the script first, "
     "and that is an editorial decision I have not made. The original deck is "
     "untouched."),
    ("Main 1, chapter labels",
     "The deck labels the second chapter CYBERSECURITY and the third PEOPLE "
     "STRATEGY. The approved script says \"cybersecurity and privacy\" and "
     "\"people and employee experience\".",
     "The Riverside card uses the script wording, which is the fuller and more "
     "recent form. Flagging it because the two artifacts differ."),
  ]),
}

BRAND_NOTE = """
BRAND VALUE WORTH ONE DECISION

Your brief specifies deep navy #112345, and that is the value the standing brand
rules and the roadmap README both carry, so these Riverside assets use it.

Every existing slide deck in the repository, Videos 1 through 8, is built with
#0F2346 instead. The two differ by two points of red and one of blue and are
indistinguishable on screen, but they are not the same value, and the divergence
predates this work.

Nothing has been changed in any existing deck. If you want the two reconciled,
say which value wins and it can be done as a separate pass.
"""
