# -*- coding: utf-8 -*-
"""One resolved event sequence per video. Every map is generated from it.

The delivered packages carried two instruction layers that could disagree
and did. The Riverside prompt told the editor to stay on camera wherever
the camera map said CAMERA, while seventeen of its own teaching moments
pointed at paragraphs the camera map marked CAMERA only. Separately, a
multi-state family was treated as one scene inside one paragraph, so the
four cost lenses were all assigned to the paragraph that names two of
them, and the paragraph that names the other two was marked CAMERA.

Both faults have the same cause: a cue was a family pinned to a paragraph.
A cue is really an event. An event has its own identity, it occupies a
span of paragraphs, and it activates particular states on particular
spoken words. The same family can serve more than one event, at different
places in the video, which is why the event id and the family id are kept
apart here.

Nothing in this module invents teaching. Every span, activation word,
entry and exit phrase is checked against the reconciled master, and the
build fails if one of them is not there.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R
import sequencing as Q

CAMERA = "CAMERA"
FULL = "FULL SCREEN"


def _st(name, on, para):
    """One state, the words it activates on, and the paragraph it is in."""
    return dict(name=name, on=on, para=para)


def E(eid, section, para, mode, enter, leave, ret, para_out=None,
      family=None, states=None, sound=None, display=None, kind="TEACHING",
      note=None):
    return dict(eid=eid, section=section, para=para,
                para_out=para if para_out is None else para_out, mode=mode,
                enter=enter, leave=leave, ret=ret, family=family,
                states=states or [], sound=sound, display=display,
                kind=kind, note=note)


# --------------------------------------------------------------- V4 to V6
TEACHING = {
 4: [
  E("V4-T01", 5, 0, FULL,
    "I would watch three things.",
    "It has to be built over time.",
    "camera returns at A SIMPLE EXAMPLE",
    para_out=2, family="NEW_V4_FS_05_THREE_THINGS",
    states=[_st("NEW_V4_FS_05_THREE_THINGS",
                "I would watch three things.", 0),
            _st("NEW_V4_FS_05A_EXPOSURE", "First, exposure.", 0),
            _st("NEW_V4_FS_05B_OWNERSHIP", "Second, ownership.", 1),
            _st("NEW_V4_FS_05C_FEEDBACK", "Third, feedback.", 2)],
    sound=dict(word="Second, ownership.",
               note="S2, one quiet accent at OWNERSHIP. Not three clicks "
                    "for three bullets."),
    display="TRUE FULL-SCREEN TEACHING  |  EXPOSURE / OWNERSHIP / "
            "FEEDBACK",
    note="One term per paragraph, on the words that name it. The three "
         "were previously all assigned to the paragraph that names the "
         "first, which put the accent word outside its own scene."),
  E("V4-T02", 6, 1, FULL,
    "Now imagine AI builds the first model.",
    "the learning may have moved to a different part of the work.",
    "camera returns on 'But if the job becomes: run the tool'",
    para_out=1, family="NEW_V4_FS_06_MOVED_OR_REMOVED",
    states=[_st("NEW_V4_FS_06_MOVED_OR_REMOVED",
                "test the assumptions, challenge the answer, and explain "
                "the recommendation", 1)],
    sound=dict(word="the learning may have moved",
               note="S3, one brief stinger as the card lands"),
    display="TRUE FULL-SCREEN ILLUSTRATION  |  TEST ASSUMPTIONS / "
            "CHALLENGE THE ANSWER / EXPLAIN THE RECOMMENDATION",
    note="The brief puts this illustration on the sentence that says the "
         "learning moved. That sentence is in paragraph 2, not 3."),
 ],
 5: [
  E("V5-T02", 7, 0, FULL,
    "Do not only ask for a promotion.",
    "A chance to build proof beyond rescue work.",
    "camera returns for the request itself",
    para_out=1, family="NEW_V5_FS_06_ASK_FOR_DEVELOPMENT",
    states=[_st("NEW_V5_FS_06_ASK_FOR_DEVELOPMENT",
                "Ask for work that builds something new.", 0)],
    display="TRUE FULL-SCREEN TEACHING  |  NOT ONLY A PROMOTION"),
  E("V5-T03", 7, 2, FULL,
    "You could say:",
    "help me build a different capability?",
    "camera returns at THE ANSWER MAY STILL BE NO",
    family="NEW_V5_FS_11_THE_REQUEST",
    states=[_st("NEW_V5_FS_11_THE_REQUEST",
                "What could I own in the next six months", 2)],
    sound=dict(word="What could I own in the next six months",
               note="S3, one quiet accent as the request appears"),
    display="TRUE FULL-SCREEN CONVERSATION  |  A SPECIFIC DEVELOPMENT "
            "REQUEST",
    note="The brief asks for this treatment and no delivered state "
         "carried the request, so one was built from the spoken words."),
  E("V5-T04", 10, 0, FULL,
    "If you take on extra work because the company needs you, set a time "
    "to review it.",
    "What am I taking off my plate?",
    "camera returns on 'Without a review point'",
    para_out=2, family="NEW_V5_FS_09_REVIEW_POINT",
    states=[_st("NEW_V5_FS_09_REVIEW_POINT",
                "Let’s come back to this in 90 days.", 0)],
    sound=dict(word="Let’s come back to this in 90 days.",
               note="S4, one soft accent on the date"),
    display="TRUE FULL-SCREEN WORKING NOTE  |  REVIEW WHAT CHANGED",
    note="The review questions run across three paragraphs. The card is "
         "held under all of them and the camera returns for the warning."),
 ],
 6: [
  E("V6-T01A", 3, 1, FULL,
    "In that Senior Divisional Strategy Consultant role, the job was not "
    "simply to “be strategic.”",
    "You start matching your experience to the work.",
    "camera returns at 2 | AUTHORITY",
    family="NEW_V6_FS_06_POSTING_WALKTHROUGH",
    states=[_st("NEW_V6_FS_06A_PROBLEM",
                "The team needed a better way to review opportunities, "
                "track them, and report on them.", 1)],
    display="TRUE FULL-SCREEN POSTING WALKTHROUGH  |  THE PROBLEM",
    note="One state per teaching occurrence. The authority and proof "
         "states belong to their own sections and are not played here."),
  E("V6-T01B", 4, 1, FULL,
    "In that same posting, one of the key words was “supporting.”",
    "It tells you where the decision power may sit.",
    "camera returns on 'I found another role called Director of "
    "Enterprise Resilience'",
    family="NEW_V6_FS_06_POSTING_WALKTHROUGH",
    states=[_st("NEW_V6_FS_06B_AUTHORITY",
                "Supporting the development of strategy is not the same "
                "as setting the strategy.", 1)],
    sound=dict(word="Supporting the development of strategy is not the "
                    "same as setting the strategy.",
               note="S3, one quiet accent on the distinction"),
    display="TRUE FULL-SCREEN POSTING COMPARISON  |  SUPPORTING IS NOT "
            "SETTING"),
  E("V6-T01C", 5, 1, FULL,
    "In the first posting, they wanted experience in areas like strategic "
    "planning, market research, business analytics, and even Microsoft "
    "Access.",
    "That last detail suggests the job may be more hands-on than the "
    "title sounds.",
    "camera returns on 'Now compare the posting with your real work.'",
    family="NEW_V6_FS_06_POSTING_WALKTHROUGH",
    states=[_st("NEW_V6_FS_06C_PROOF",
                "business analytics, and even Microsoft Access", 1)],
    display="TRUE FULL-SCREEN POSTING WALKTHROUGH  |  THE PROOF THEY "
            "WOULD NEED TO SEE"),
  E("V6-T03", 10, 0, FULL,
    "Take one job description you are actually thinking about.",
    "Now you are reading the job instead of being impressed or scared by "
    "the label.",
    "camera returns at TAKEAWAY VALUE",
    para_out=1, family="NEW_V6_FS_20_CTA",
    states=[_st("NEW_V6_FS_20A_WRITE_FOUR_LINES",
                "Write four lines: Problem. Authority. Proof. Real gap.",
                0),
            _st("NEW_V6_FS_20B_STRONGEST_VERB",
                "Then circle the strongest verbs in the posting.", 1)],
    sound=dict(word="Take one job description you are actually thinking "
                    "about.",
               note="S5, one accent as the working page appears"),
    display="TRUE FULL-SCREEN WORKING PAGE  |  PROBLEM / AUTHORITY / "
            "PROOF / REAL GAP",
    note="The second instruction is spoken in the next paragraph, so the "
         "page is held rather than completed early."),
  E("V6-T02", 6, 1, FULL,
    "A global nonprofit was hiring a Director of Global Talent "
    "Acquisition.",
    "It is a work and life constraint.",
    "camera returns on 'You can be able to do the work'",
    para_out=2, family="NEW_V6_FS_17_REAL_GAP",
    states=[_st("NEW_V6_FS_17A_GEOGRAPHIC",
                "people whose recruiting experience was only in one "
                "geographic setting were unlikely to be a strong fit", 1),
            _st("NEW_V6_FS_17B_TIME_ZONE",
                "at least three hours of overlap with East Africa Time.",
                2)],
    sound=dict(word="at least three hours of overlap with East Africa "
                    "Time.",
               note="One accent as the second requirement lands"),
    display="TRUE FULL-SCREEN REQUIREMENT CARD  |  REQUIRED TIME OVERLAP",
    note="Two requirements, two paragraphs, one state each. The second "
         "is not revealed while the first is being explained."),
 ],
}

# --------------------------------------------------------------- V7 to V9
TEACHING.update({
 7: [
  E("V7-T01", 5, 0, FULL,
    "When I have seen bigger work handed out, I tend to look at four "
    "things.",
    "That last part matters.",
    "camera returns on 'Bias matters. Relationships matter.'",
    para_out=4, family="NEW_V7_FS_04_FOUR_THINGS",
    states=[_st("NEW_V7_FS_04_FOUR_THINGS",
                "I tend to look at four things.", 0),
            _st("NEW_V7_FS_04A_VISIBLE_PROOF", "First, visible proof.", 1),
            _st("NEW_V7_FS_04B_JUDGMENT", "Second, judgment.", 2),
            _st("NEW_V7_FS_04C_TRUST", "Third, trust.", 3),
            _st("NEW_V7_FS_04D_SPONSORSHIP",
                "Fourth, sponsorship and access.", 4)],
    sound=dict(word="I tend to look at four things.",
               note="S3, one accent as the four establish. Not one per "
                    "item."),
    display="TRUE FULL-SCREEN TEACHING  |  VISIBLE PROOF / JUDGMENT / "
            "TRUST / SPONSORSHIP",
    note="One item per paragraph, on the words that name it. The "
         "boundary about bias and access is hers, on camera."),
  E("V7-T02", 8, 0, FULL,
    "You could say: “I want to be ready for larger scope.",
    "“What kind of stakeholder?”",
    "camera returns on 'You are not asking for a promise.'",
    para_out=1, family="NEW_V7_FS_14_A_CLEARER_TARGET",
    states=[_st("NEW_V7_FS_14_A_CLEARER_TARGET",
                "what would you need to see me handle that you have not "
                "seen yet?", 0)],
    sound=dict(word="what would you need to see me handle that you have "
                    "not seen yet?",
               note="S4, one quiet accent as the question appears"),
    display="TRUE FULL-SCREEN CONVERSATION  |  ASK FOR A CLEARER TARGET",
    note="The brief asks for this treatment and no delivered state "
         "carried the question, so one was built from the spoken words."),
  E("V7-T03", 10, 0, FULL,
    "Write down the last three times you were trusted with something "
    "bigger than your normal role.",
    "What changed because of my work?",
    "camera returns on 'Then look for what is missing.'",
    para_out=1, family="NEW_V7_FS_11_READ_YOUR_OWN_SITUATION",
    states=[_st("NEW_V7_FS_11_READ_YOUR_OWN_SITUATION",
                "What problem was I trusted with?", 1)],
    display="TRUE FULL-SCREEN WORKING NOTE  |  PROBLEM / MY DECISION / "
            "WHO SAW IT / WHAT CHANGED",
    note="The instruction is in paragraph 1 and the four questions are "
         "in paragraph 2. The card enters with the instruction."),
 ],
 8: [
  E("V8-T02", 3, 0, FULL,
    "you can lose five useful details.",
    "Those details turn a memory into something another person can "
    "understand and judge.",
    "camera returns at THE IMPORTANT BOUNDARY",
    para_out=2, family="NEW_V8_FS_02_FIVE_KINDS",
    states=[_st("NEW_V8_FS_02_FIVE_KINDS",
                "you can lose five useful details.", 0),
            _st("NEW_V8_FS_02A_BASELINE", "The baseline.", 0),
            _st("NEW_V8_FS_02B_SCOPE", "The scope.", 0),
            _st("NEW_V8_FS_02C_DECISION", "The decision.", 1),
            _st("NEW_V8_FS_02D_RESULT", "The result.", 1),
            _st("NEW_V8_FS_02E_MECHANISM", "And the method.", 2)],
    sound=dict(word="The baseline.",
               note="S2, one soft click on the first field only"),
    display="TRUE FULL-SCREEN NOTE  |  BASELINE / SCOPE / DECISION / "
            "RESULT / METHOD",
    note="Five fields across three paragraphs, one active at a time. "
         "They were previously all assigned to the first paragraph, "
         "which showed the decision and the result before they were "
         "spoken."),
  E("V8-T03", 5, 0, FULL,
    "You can record the work in your own words.",
    "“Measured the result using Y.”",
    "camera returns on 'You are keeping the shape of the evidence.'",
    para_out=1, family="NEW_V8_FS_05_IN_YOUR_OWN_WORDS",
    states=[_st("NEW_V8_FS_05_IN_YOUR_OWN_WORDS",
                "Owned the decision on Y, but budget approval stayed with "
                "Z.", 1)],
    sound=dict(word="Owned the decision on Y, but budget approval stayed "
                    "with Z.",
               note="S4, one accent as the boundary line appears"),
    display="TRUE FULL-SCREEN EXAMPLE NOTE  |  MY DECISION: Y / BUDGET "
            "APPROVAL: Z",
    note="The examples run across two paragraphs and the boundary line "
         "is in the second."),
  E("V8-T05", 12, 0, FULL,
    "That brings us back to the login screen.",
    "The system can disappear in a day.",
    "camera returns on 'Your understanding of your own work'",
    family="NEW_V8_FS_00_ACCESS_UNAVAILABLE",
    states=[_st("NEW_V8_FS_00_ACCESS_UNAVAILABLE",
                "That brings us back to the login screen.", 0)],
    sound=dict(word=None,
               note="No accent. The hook already used the lock sound and "
                    "this is the same picture returning."),
    display="TRUE FULL-SCREEN CALLBACK, THEN CAMERA  |  ACCESS MAY END",
    note="The same illustrative login as the hook, at a second "
         "occurrence. One asset, two events."),
 ],
 9: [
  E("V9-T02", 4, 0, FULL,
    "I use four questions instead: What travels? What does not?",
    "That gives you a more honest picture of the move.",
    "camera returns at 1 | WHAT TRAVELS",
    para_out=1, family="NEW_V9_FS_03_FOUR_QUESTIONS",
    states=[_st("NEW_V9_FS_03_FOUR_QUESTIONS",
                "I use four questions instead:", 0),
            _st("NEW_V9_FS_03A_WHAT_TRAVELS", "What travels?", 0),
            _st("NEW_V9_FS_03B_WHAT_DOES_NOT", "What does not?", 0),
            _st("NEW_V9_FS_03C_WHAT_CAN_I_PROVE", "What can I prove?", 1),
            _st("NEW_V9_FS_03D_WHAT_MUST_I_RELEARN",
                "What must I relearn?", 1)],
    sound=dict(word="I use four questions instead:",
               note="S2, one accent as the four establish"),
    display="TRUE FULL-SCREEN TEACHING  |  WHAT TRAVELS? / WHAT DOES "
            "NOT? / WHAT CAN I PROVE? / WHAT MUST I RELEARN?",
    note="Two questions are spoken in paragraph 1 and two in paragraph "
         "2. The last two are not revealed early. The same family also "
         "serves the hook, which is a separate event."),
  E("V9-T03", 9, 0, FULL,
    "When I think about changing context, I do not picture a suitcase "
    "where everything fits.",
    "And some things have to be learned.",
    "camera returns on 'That is why a transferable-skills list can be too "
    "simple.'",
    para_out=1, family="NEW_V9_FS_08_SORTING",
    states=[_st("NEW_V9_FS_08_SORTING", "I picture sorting.", 0)],
    sound=dict(word="I picture sorting.",
               note="S3, one soft accent on the image"),
    display="TRUE FULL-SCREEN SORTING ILLUSTRATION  |  AS IT IS / NEEDS "
            "TRANSLATION / CONTEXT-BOUND / TO BE LEARNED"),
  E("V9-T04", 13, 1, FULL,
    "Try something more honest:",
    "The part I would need to build in your environment is Z.",
    "camera returns on 'That makes the transfer clear.'",
    family="NEW_V9_FS_13_X_Y_Z",
    states=[_st("NEW_V9_FS_13_X_Y_Z",
                "The part of my experience that is most useful here is X.",
                1)],
    sound=dict(word="The part of my experience that is most useful here "
                    "is X.",
               note="S4, one quiet accent as the sentence appears"),
    display="TRUE FULL-SCREEN CONVERSATION  |  USEFUL EXPERIENCE: X / "
            "USED TO SOLVE: Y / NEED TO BUILD: Z",
    note="The brief asks for this treatment and no delivered state "
         "carried the sentence, so one was built from the spoken words."),
 ],
})

# ------------------------------------------------------------- V10 and V11
TEACHING.update({
 10: [
  E("V10-T02", 5, 0, CAMERA,
    "READ does not mean sit quietly for 30 days and contribute nothing.",
    "The point is to understand enough context that your expertise lands "
    "in the right place.",
    "the full-screen contrast follows in paragraph 3",
    para_out=1,
    display="CAMERA  |  READ IS NOT STAY SILENT",
    note="The brief's own heading is CAMERA, THEN BRIEF FULL-SCREEN "
         "CONTRAST. This is the camera half. The contrast is the next "
         "event, and the two are no longer printed as one instruction "
         "pointing at a camera paragraph."),
  E("V10-T02B", 5, 2, FULL,
    "There is a difference between saying, “At my old company, we "
    "did it this way,”",
    "without assuming the room is the same.",
    "camera returns at 2 | TEST",
    family="NEW_V10_FS_05_TWO_SENTENCES",
    states=[_st("NEW_V10_FS_05A_BOTH",
                "At my old company, we did it this way,", 2),
            _st("NEW_V10_FS_05B_SECOND",
                "I have seen a similar problem before.", 2)],
    display="TRUE FULL-SCREEN CONTRAST  |  ONE ASSUMES. ONE ASKS."),
  E("V10-T05", 11, 0, FULL,
    "So if I were building a first-90-days plan for an experienced "
    "professional, I would keep it this simple.",
    "What have these 90 days taught me about the job itself?",
    "camera returns on 'That is the plan.'",
    para_out=1, family="NEW_V10_FS_13_THE_TOOL",
    states=[_st("NEW_V10_FS_13_ESTABLISH", "I would keep it this simple.",
                0),
            _st("NEW_V10_FS_13A_READ",
                "READ. What do I understand now that I did not understand "
                "on day one?", 0),
            _st("NEW_V10_FS_13B_TEST",
                "TEST. What from my previous experience works here", 0),
            _st("NEW_V10_FS_13C_PROVE",
                "PROVE. What can I now show that I have done successfully "
                "in this context?", 1),
            _st("NEW_V10_FS_13D_ROLE_CHECK",
                "ROLE CHECK. What have these 90 days taught me about the "
                "job itself?", 1)],
    sound=dict(word="ROLE CHECK.",
               note="S5, one accent as the fourth line is added"),
    display="TRUE FULL-SCREEN WORKING PAGE  |  READ / TEST / PROVE / ROLE "
            "CHECK",
    note="READ and TEST are spoken in paragraph 1, PROVE and ROLE CHECK "
         "in paragraph 2. The added line is not shown before it is "
         "spoken."),
 ],
 11: [
  E("V11-T03", 6, 0, FULL,
    "I would look at four costs.",
    "something else that mattered when you accepted?",
    "camera returns on 'A mismatch can be manageable in one category'",
    para_out=1, family="NEW_V11_FS_06_FOUR_COST_LENSES",
    states=[_st("NEW_V11_FS_06_ESTABLISH", "I would look at four costs.",
                0),
            _st("NEW_V11_FS_06A_CAPABILITY", "CAPABILITY.", 0),
            _st("NEW_V11_FS_06B_EVIDENCE", "EVIDENCE.", 0),
            _st("NEW_V11_FS_06C_COMPENSATION", "COMPENSATION.", 1),
            _st("NEW_V11_FS_06D_LIFE", "LIFE.", 1)],
    sound=dict(word="I would look at four costs.",
               note="S3, one accent as the four establish. Not one per "
                    "lens."),
    display="TRUE FULL-SCREEN COST LENSES  |  CAPABILITY / EVIDENCE / "
            "COMPENSATION / LIFE",
    note="Capability and evidence are spoken in paragraph 1, "
         "compensation and life in paragraph 2. Compensation and life "
         "are not revealed early and are not trimmed: they carry the "
         "pay, level, travel, caregiving and health constraints."),
  E("V11-T05A", 9, 0, FULL,
    "So put the four lines next to each other.",
    "What can I clarify, negotiate, test, or decide next?",
    "camera returns on 'That is a role-drift read.'",
    para_out=1, family="NEW_V11_FS_09_THE_ROLE_DRIFT_READ",
    states=[_st("NEW_V11_FS_09_ESTABLISH",
                "So put the four lines next to each other.", 0),
            _st("NEW_V11_FS_09A_EXPECTED", "EXPECTED.", 0),
            _st("NEW_V11_FS_09B_ACTUAL", "ACTUAL.", 0),
            _st("NEW_V11_FS_09C_COST", "COST.", 1),
            _st("NEW_V11_FS_09D_CHOICE", "CHOICE.", 1)],
    display="TRUE FULL-SCREEN RECAP  |  EXPECTED / ACTUAL / COST / CHOICE",
    note="Expected and actual are spoken in paragraph 1, cost and choice "
         "in paragraph 2. The camera returns for the interpretation that "
         "follows, which begins 'That is a role-drift read.'"),
  E("V11-T05B", 11, 0, FULL,
    "Write EXPECTED and ACTUAL side by side.",
    "or begin planning another option.",
    "camera returns at STORY LOOP PAYOFF",
    family="NEW_V11_FS_00B_COST_AND_NEXT",
    states=[_st("NEW_V11_FS_00B_COST_AND_NEXT",
                "Name one real cost.", 0)],
    sound=dict(word="Name one real cost.",
               note="S5, one accent as the cost line is added"),
    display="TRUE FULL-SCREEN WORKING PAGE, THEN CAMERA  |  ONE "
            "DIFFERENCE / ONE COST / ONE NEXT ACTION",
    note="The opening pair of documents returns with the cost and the "
         "next action added, which is the treatment the brief asks for "
         "and no delivered state carried."),
 ],
})

# The story-loop payoffs the briefs treat as camera callbacks. Each names
# a numbered accent, and none of them had an event at all, so the accent
# had nowhere to attach.
CALLBACK = {
 4: E("V4-P05", 13, 0, CAMERA,
      "So come back to the question from the beginning:",
      "you are reading what is happening to the experience underneath "
      "the task.",
      "stays on camera into TAKEAWAY VALUE",
      display="CAMERA, THEN WORKING-PAGE CALLBACK  |  WHAT AM I STILL "
              "PRACTICING?",
      kind="PAYOFF",
      note="The brief returns to the opening question on the same visual "
           "motif and shows the finished note, not a celebratory "
           "result."),
 5: E("V5-P05", 13, 0, CAMERA,
      "Are they asking for more of your capacity, or expanding your "
      "capability?",
      "you can stop confusing being needed with moving forward.",
      "stays on camera for the boundary",
      display="CAMERA  |  CAPACITY OR CAPABILITY",
      kind="PAYOFF",
      note="Pays off the opening work-request cards with the "
           "distinction, then returns to camera for the boundary."),
 7: E("V7-P05", 13, 0, CAMERA,
      "If the bigger role opened tomorrow, what could someone already "
      "point to?",
      "that tells you something about the environment too.",
      "stays on camera",
      display="CAMERA + BRIEF QUESTION CALLBACK  |  WHAT COULD THEY "
              "POINT TO?",
      kind="PAYOFF",
      note="The question from the story loop, asked again now that the "
           "viewer can answer it."),
 9: E("V9-P05", 15, 0, CAMERA,
      "The question was never simply, \u201cDo my skills transfer?\u201d",
      "what will this new context still ask me to build?",
      "stays on camera",
      display="CAMERA + WORKING-PAGE CALLBACK  |  WHAT DOES THIS CONTEXT "
              "STILL REQUIRE?",
      kind="PAYOFF",
      note="The four columns answered, rather than listed again."),
}


def _named_accents(n):
    """Every numbered accent the brief specifies, with where it lands.

    The briefs number five accents per video. Regenerating the sound map
    from the event list dropped the ones whose event was built from a
    plain cue rather than written by hand, which left four videos below
    the stated band. These are read back out of the brief, so the map
    carries the accents the brief asked for and no others.
    """
    import re as _re
    sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                       "V4-V11_EDIT_SYNC/build")
    import briefs as _B
    import locate as _LOC
    out = []
    for x in _B.read(n)["beats"]:
        m = _re.search(r"\bS(\d)\b", x["head"])
        if not m or not x["trigger"]:
            continue
        r = _LOC.resolve(n, x["trigger"], x["head"])
        if not r:
            continue
        word = _LOC.accent_word(x)
        note = None
        for y in [x["head"]] + list(x["note"]):
            if _re.search(r"stinger|accent|click|sound on|soft click",
                          y, _re.I):
                note = y
                break
        out.append(dict(s="S" + m.group(1), section=r["section"],
                        para=r["para"], word=word,
                        entry=_LOC.remap(n, x["trigger"]),
                        note=note or "One brief stinger."))
    return out


# Families whose single-paragraph cue is superseded by an event above.
def _covered(n):
    out = {}
    for e in TEACHING.get(n, []):
        if e["family"]:
            out.setdefault(e["family"], []).append(e)
    return out


def events(n):
    """Every event for this video, in spoken order."""
    out = []
    for s in Q.EARLY.get(n, []):
        out.append(E("V%d-O%02d" % (n, s["order"]), s["section"],
                     s["para"], s["mode"], s["enter"], s["leave"],
                     s["ret"], para_out=s["para_out"], family=s["asset"],
                     states=[_st(x, s["enter"], s["para"])
                             for x in s["states"]],
                     sound=dict(word=None, note=s["sound"])
                     if s["sound"] else None,
                     display=s["display"], kind="OPENING", note=s["note"]))
    out.extend(TEACHING.get(n, []))
    cov = _covered(n)
    early = {s["asset"] for s in Q.EARLY.get(n, []) if s["asset"]}
    for c in Q.anchors(n):
        if c["key"] in cov or c["key"] in early:
            continue
        secs = R.sections(n)
        p = secs[c["section"]][1][c["para"]]
        sub = Q.subrange(n, c["section"], c["para"], c["key"])
        out.append(E("V%d-C%02d" % (n, len(out) + 1), c["section"],
                     c["para"], FULL,
                     sub["enter"] if sub else (c["trigger"] or p),
                     sub["leave"] if sub else (c["trigger"] or p),
                     "camera returns at the end of the paragraph",
                     family=c["key"],
                     states=[_st(x, sub["enter"] if sub else
                                 (c["trigger"] or p), c["para"])
                             for x in c["states"]],
                     kind="END" if c["key"].endswith("WATCH_NEXT")
                     else "CUE"))
    if n in CALLBACK:
        out.append(CALLBACK[n])
    out.sort(key=lambda e: (e["section"], e["para"],
                            0 if e["kind"] == "OPENING" else 1))
    # Every accent the brief numbers is attached to the event that covers
    # its paragraph. An event that already carries a hand-written accent
    # keeps it: this only restores the ones that had nowhere to go.
    for a_ in _named_accents(n):
        cover = [e for e in out
                 if e["section"] == a_["section"]
                 and e["para"] <= a_["para"] <= e["para_out"]]
        if not cover or any(e["sound"] for e in cover):
            continue
        e = cover[-1]
        e["sound"] = dict(word=a_["word"],
                          note="%s, %s" % (a_["s"], a_["note"]))
    return out


def modes(n):
    """Every paragraph's mode, from the events that cover it."""
    out = {}
    for si, (lab, ps) in enumerate(R.sections(n)):
        for pi in range(len(ps)):
            out[(si, pi)] = CAMERA
    for e in events(n):
        if e["mode"] != FULL:
            continue
        for pi in range(e["para"], e["para_out"] + 1):
            out[(e["section"], pi)] = FULL
    return out


def verify():
    """Every span, activation word and boundary, against the master."""
    bad = []
    for n in R.VIDEOS:
        secs = R.sections(n)
        labs = [l for l, _ in secs]
        seen = set()
        for e in events(n):
            tag = "%s" % e["eid"]
            if e["eid"] in seen:
                bad.append("%s: duplicate event id" % tag)
            seen.add(e["eid"])
            if e["section"] >= len(secs):
                bad.append("%s: no such section" % tag)
                continue
            ps = secs[e["section"]][1]
            if e["para"] >= len(ps) or e["para_out"] >= len(ps):
                bad.append("%s: paragraph outside the section" % tag)
                continue
            if e["para_out"] < e["para"]:
                bad.append("%s: exits before it enters" % tag)
            a = R.S._norm(ps[e["para"]]).lower()
            b = R.S._norm(ps[e["para_out"]]).lower()
            if R.S._norm(e["enter"]).lower() not in a:
                bad.append("%s: enter wording is not in section %d "
                           "paragraph %d" % (tag, e["section"] + 1,
                                             e["para"] + 1))
            if R.S._norm(e["leave"]).lower() not in b:
                bad.append("%s: leave wording is not in section %d "
                           "paragraph %d" % (tag, e["section"] + 1,
                                             e["para_out"] + 1))
            if "..." in e["enter"] or "..." in e["leave"]:
                bad.append("%s: boundary wording is truncated" % tag)
            if e["mode"] == FULL and not e["family"]:
                bad.append("%s: full screen with no asset family" % tag)
            if e["mode"] == CAMERA and e["family"]:
                bad.append("%s: camera with an asset family" % tag)
            last = -1
            for s in e["states"]:
                if not (e["para"] <= s["para"] <= e["para_out"]):
                    bad.append("%s: state %s is outside the event's span"
                               % (tag, s["name"]))
                    continue
                q = R.S._norm(ps[s["para"]]).lower()
                if R.S._norm(s["on"]).lower() not in q:
                    bad.append("%s: state %s activates on wording that is "
                               "not in section %d paragraph %d"
                               % (tag, s["name"], e["section"] + 1,
                                  s["para"] + 1))
                if s["para"] < last:
                    bad.append("%s: state %s reveals before the one "
                               "before it" % (tag, s["name"]))
                last = s["para"]
            if e["sound"] and e["sound"].get("word"):
                w = R.S._norm(e["sound"]["word"]).lower()
                if not any(w in R.S._norm(ps[i]).lower()
                           for i in range(e["para"], e["para_out"] + 1)):
                    bad.append("%s: the accent word is not spoken inside "
                               "the event" % tag)
        m = modes(n)
        for e in events(n):
            if e["mode"] != FULL:
                continue
            for pi in range(e["para"], e["para_out"] + 1):
                if m[(e["section"], pi)] != FULL:
                    bad.append("%s: covers section %d paragraph %d but "
                               "the map calls it camera"
                               % (e["eid"], e["section"] + 1, pi + 1))
    return bad


if __name__ == "__main__":
    bad = verify()
    for n in R.VIDEOS:
        ev = events(n)
        fam = len({e["family"] for e in ev if e["family"]})
        reuse = len([e for e in ev if e["family"]]) - fam
        print("V%-3d %3d events, %2d families, %d reused at a second "
              "occurrence, %d spanning paragraphs"
              % (n, len(ev), fam, reuse,
                 len([e for e in ev if e["para_out"] > e["para"]])))
    print("\nchecks failed: %d" % len(bad))
    for b in bad:
        print("   %s" % b)
