# -*- coding: utf-8 -*-
"""One executable cue sequence per video: locations, subranges, early edit.

Three defects from the independent review are resolved here.

CUES THAT COMPETE. Eight paragraphs hosted more than one family with no
transition between them. Four of those are not sequencing problems at all:
the card was simply cued in the wrong place, and its own copy says where it
belongs. Those are moved. The rest are genuine sequences, so each family
gets an entry phrase, an exit phrase and a reveal order inside the
paragraph. One family is retired: after its authorized copy update it says
the same thing as the card beside it.

AN END SCREEN WITH COMPANY. V8 cued a teaching card on the same passage as
the Watch Next end card. The teaching card moves to the teaching it was
written for. The end card owns the closing passage and the final frame.

EARLY EDITING THAT WAS ONLY DESCRIBED. The briefs specify cutaways in the
first paragraphs that no map realized. Every opening beat now names its
mode, its entry and exit words inside the paragraph, its asset state, its
sound event and where the camera returns.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R

ANCHORS = {}
for _f in ("an_sprint.json", "an_1011.json"):
    _p = os.path.join(HERE, _f)
    if os.path.exists(_p):
        for _n, _rows in json.load(open(_p)).items():
            ANCHORS[int(_n)] = [dict(r) for r in _rows]


# ------------------------------------------------------------ relocations
# (video, family) -> (section index, paragraph index, why)
RELOCATE = {
 (4, "NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT"): (0, 1,
   "The brief's second opening beat asks for this exact cutaway on the "
   "hook, and the card's own rows are the hook's repetition, mistakes and "
   "patterns. Cueing it in THREE THINGS TO WATCH both stranded the early "
   "beat and put it on the same paragraph as FS_05."),
 (6, "NEW_V6_FS_08_READ_THE_VERBS"): (4, 0,
   "The card says READ THE VERBS and the script says 'Next, look at the "
   "verbs' in 2 | AUTHORITY. It was cued three sections later, where it "
   "competed with two other families for one paragraph."),
 (6, "NEW_V6_FS_19_FOUR_THINGS"): (11, 0,
   "A WHAT YOU GET summary belongs with TAKEAWAY VALUE, which names the "
   "four things and what ten minutes buys. It was cued on the same "
   "paragraph as FS_04, where the three questions are the teaching."),
 (8, "NEW_V8_FS_07_TEN_MINUTE_HABIT"): (7, 0,
   "The whole card is the section 8 habit. Cued in the hook it revealed "
   "the answer before the video taught it and left THE 10-MINUTE HABIT, "
   "the video's central activity, with no card at all."),
 (8, "NEW_V8_FS_08_CAREER_HYGIENE"): (8, 1,
   "Its own retained line traces to WHEN THE EXIT IS SUDDEN. On the Watch "
   "Next passage it competed with the end card for the final frame."),
 (9, "NEW_V9_FS_12_THE_AUDIT_AGAIN"): (16, 1,
   "This is the closing recap. In the hook it played the four questions "
   "before FS_03 established them, which is a callback before the thing "
   "it calls back to."),
 (11, "NEW_V11_FS_01_FOUR_QUESTIONS"): (0, 2,
   "The Riverside prompt reveals the framework in the hook, on 'EXPECTED. "
   "ACTUAL. COST. CHOICE.' It was cued only in the later recap, which "
   "FS_09 already owns."),
}

# Families whose use no longer earns its place.
RETIRE = {
 (8, "NEW_V8_FS_11_A_FACTUAL_RECORD"):
   "After the authorized copy update this card reads NOT the company's "
   "property / THIS a lawful record of your own work, which is what "
   "FS_04 already says on the same paragraph. Playing both is playing a "
   "state to retain it. The design and the update are preserved in the "
   "ledger; only the cue is withdrawn.",
}


# -------------------------------------------------------------- subranges
# Where a paragraph genuinely carries two ideas in order, each family gets
# its own words. (video, section, para) -> [(family, enter, exit)]
SUBRANGE = {
 (6, 7, 1): [
   ("NEW_V6_FS_10_DIRECTOR_COMPARE",
    "One role focused much more on running the work",
    "worked directly with a Chief Transformation Officer."),
   ("NEW_V6_FS_12_TITLE_TEST",
    "Same broad title level.",
    "It cannot finish the read.")],
 (6, 8, 1): [
   ("NEW_V6_FS_14_AUTHORITY_POSTURES",
    "But the work included leading federal authorization work",
    "serving as a subject-matter expert."),
   ("NEW_V6_FS_15_CEILING",
    "The published pay range went from $180,000 to $440,000.",
    "sat on the highest published pay ceiling.")],
 (10, 4, 3): [
   ("NEW_V10_FS_03_READ_FOUR_THINGS",
    "During READ, pay attention to four things",
    "what do people around me know that was never written in the job "
    "description?"),
   ("NEW_V10_FS_04_FORMAL_VS_REAL",
    "A job description can tell you the formal job.",
    "The first few weeks start showing you the real one.")],
}


# ------------------------------------------------------------- early edit
# One executable sequence per video. Each step names its mode, the words it
# enters and leaves on inside the paragraph, the asset state, the sound
# event and where the camera comes back.
def _s(order, section, para, mode, enter, leave, ret, display=None,
       asset=None, states=None, sound=None, note=None, para_out=None):
    """One step. para is where it enters; para_out where it leaves."""
    return dict(order=order, section=section, para=para,
                para_out=para if para_out is None else para_out, mode=mode,
                enter=enter, leave=leave, ret=ret, display=display,
                asset=asset, states=states or ([] if not asset else [asset]),
                sound=sound, note=note)


EARLY = {
 4: [
  _s(1, 0, 0, "CAMERA", "Imagine a task that takes someone hours.",
     "That sounds like progress.", "stays on camera",
     display="WHO LEARNS NOW?",
     note="The question enters over her face during the first sentence and "
          "clears. No benchmark, no figure, no timed comparison."),
  _s(2, 0, 0, "FULL SCREEN", "But those hours were not always wasted.",
     "Where they started noticing patterns.", para_out=1,
     ret="camera returns on 'So I think we are asking the wrong question'",
     display="WHAT THE TASK TAUGHT",
     asset="NEW_V4_FS_03_WHAT_THE_WORK_TAUGHT",
     sound="S1, one brief stinger on 'wasted'",
     note="Rows arrive with the sentences that name them: repetition, "
          "fixing mistakes, seeing enough examples. Her voice continues."),
  _s(3, 0, 2, "FULL SCREEN",
     "If AI takes the task, who gets the experience that used to come "
     "from doing it?", "who gets the experience that used to come from "
     "doing it?",
     "camera returns on 'Because we still need experienced people later'",
     display="WHO GETS THE EXPERIENCE?",
     asset="NEW_V4_FS_01_WHO_GETS_THE_EXPERIENCE",
     note="Reveal the question once. The consequence is hers, on camera."),
 ],
 5: [
  _s(1, 0, 0, "CAMERA",
     "Your company can need you so much that it becomes one of the "
     "reasons you stop growing.",
     "But think about what happens to the person everyone depends on.",
     "stays on camera", display="NEEDED. STILL STUCK?",
     note="The contradiction appears during the first sentence. No logo "
          "introduction."),
  _s(2, 0, 1, "FULL SCREEN", "Something breaks, they call you.",
     "A new person joins, you train them.",
     "camera returns on 'Then a bigger opportunity opens'",
     display="FIX IT / COVER IT / TRAIN THEM",
     asset="NEW_V5_FS_01_NEEDED_NOT_GROWN",
     sound="S1, one soft notification click on the first request only",
     note="Illustrative work requests, not an employer chat."),
  _s(3, 0, 2, "CAMERA", "And they choose someone else.",
     "And they choose someone else.", "stays on camera",
     display="SOMEONE ELSE",
     note="Back on her before the line, so the reaction is hers. A brief "
          "silence is enough. No rejection sound."),
 ],
 6: [
  _s(1, 0, 0, "CAMERA", "I want you to guess what this job actually is.",
     "I want you to guess what this job actually is.", "stays on camera",
     display="WHAT IS THE ACTUAL JOB?",
     note="The question lands while she speaks. No framework, no "
          "introduction first."),
  _s(2, 0, 0, "FULL SCREEN",
     "Senior Divisional Strategy Consultant, Governance.",
     "Sounds like someone setting strategy and making big decisions.",
     "holds into the next paragraph",
     display="Senior Divisional Strategy Consultant, Governance",
     asset="NEW_V6_FS_01_TITLE_ONLY",
     sound="S1, one brief stinger on the title",
     note="Anonymized employer descriptor only. Salary and requirement "
          "stay hidden until spoken."),
  _s(3, 0, 1, "FULL SCREEN",
     "But when I read the actual posting, the bottom of the pay range was "
     "$61,500", "Nothing is wrong with either of those things.",
     "camera returns on 'But they tell you something important'",
     display="PUBLISHED RANGE START: $61,500 / ACCEPT DIRECTION AND "
             "FEEDBACK",
     asset="NEW_V6_FS_02_THE_CONTRADICTION",
     sound="S2, one brief stinger on the range floor",
     note="Range floor on the first state, requirement on the second. "
          "Paraphrase unless the capture packet supplies an exact quote."),
  _s(4, 0, 2, "CAMERA",
     "But they tell you something important: The title did not tell you "
     "the job.", "The title did not tell you the job.", "stays on camera",
     display="THE TITLE IS NOT THE WHOLE JOB",
     note="Her interpretation, on camera. One observed posting, not a "
          "verdict on titles."),
  _s(5, 0, 3, "FULL SCREEN",
     "the four things I would read before deciding whether a job is "
     "actually a fit for your experience",
     "And the first thing I would do is almost ignore the title.",
     "camera returns at STORY LOOP",
     display="PROBLEM / AUTHORITY / PROOF / REAL GAP",
     asset="NEW_V6_FS_05_PARP",
     note="The sample boundary stays spoken: 15 postings, 11 employers."),
 ],
 7: [
  _s(1, 0, 0, "CAMERA", "Two people can both be good at their jobs.",
     "Two people can both be good at their jobs.",
     "cuts away within the paragraph", display="TWO CAPABLE PEOPLE",
     note="Her voice and face first. The cutaway follows inside the same "
          "thought, not after all the setup."),
  _s(2, 0, 0, "FULL SCREEN", "Both dependable.", "Both working hard.",
     "holds into the next paragraph", display="TWO CAPABLE PEOPLE",
     asset="NEW_V7_FS_00_TWO_CAPABLE_PEOPLE",
     states=["NEW_V7_FS_00_TWO_CAPABLE_PEOPLE"],
     sound="S1, one brief stinger as the pair establishes",
     note="Two identical cards. Nothing distinguishes them."),
  _s(3, 0, 1, "FULL SCREEN", "One person’s name comes up.",
     "The other person’s does not.",
     "camera returns on 'I have seen versions of that happen'",
     display="ONE NAME COMES UP",
     asset="NEW_V7_FS_00_TWO_CAPABLE_PEOPLE",
     states=["NEW_V7_FS_00B_ONE_NAME_COMES_UP"],
     sound="S2, one quiet accent as the outcome line arrives",
     note="The outcome line appears beneath the unchanged pair. No taller "
          "figure, score, trophy or better-person symbol."),
  _s(4, 0, 2, "FULL SCREEN",
     "the difference is not always who worked harder",
     "evidence people can already see at the next level.",
     "camera returns on 'And sometimes the difference has nothing to do "
     "with capability at all'",
     display="NOT ALWAYS ABOUT WORKING HARDER",
     asset="NEW_V7_FS_01_NOT_ALWAYS_WHO_WORKED_HARDER",
     note="Access, sponsorship, bias and politics stay on camera, not "
          "under a merit graphic."),
 ],
 8: [
  _s(1, 0, 0, "CAMERA",
     "Imagine tomorrow morning you try to log into your work account.",
     "Imagine tomorrow morning you try to log into your work account.",
     "cuts away within the paragraph",
     display="CAN YOU STILL EXPLAIN YOUR WORK?",
     note="She speaks first, then straight into the imagined login. No "
          "camera-only scene."),
  _s(2, 0, 0, "FULL SCREEN", "You cannot.", "Project folders gone.",
     para_out=1,
     ret="camera returns on 'Now imagine that six months later an "
         "interviewer asks'", display="ACCESS UNAVAILABLE",
     asset="NEW_V8_FS_00_ACCESS_UNAVAILABLE",
     sound="S1, one muted lock or click on 'You cannot.'",
     note="Generic and clearly illustrative. No employer interface, file, "
          "logo or customer data."),
  _s(3, 0, 2, "CAMERA",
     "Now imagine that six months later an interviewer asks: What exactly "
     "changed because of your work?",
     "What exactly changed because of your work?",
     "cuts away within the paragraph",
     display="WHAT CHANGED BECAUSE OF YOUR WORK?",
     note="The interviewer's question is the early outcome cue. No fear "
          "montage."),
  _s(4, 0, 2, "FULL SCREEN", "You remember doing good work.",
     "You remember that the project mattered.",
     "camera returns on 'But was the improvement 27% or 37%?'",
     display="YOU REMEMBER. YOU CANNOT PROVE IT CLEANLY.",
     asset="NEW_V8_FS_01_MEMORY_NOT_PROOF",
     note="The baseline and decision questions do the work from camera."),
 ],
 9: [
  _s(1, 0, 0, "CAMERA",
     "I think some transferable-skills advice gives experienced "
     "professionals false confidence.",
     "Some of it absolutely can.", "stays on camera",
     display="NOT EVERYTHING TRAVELS",
     note="'Some' stays in the spoken claim. No study, no universal "
          "indictment."),
  _s(2, 0, 1, "FULL SCREEN",
     "The problem is that we spend so much time asking, What can I take "
     "with me?", "What am I leaving behind?",
     "camera returns within the paragraph",
     display="WHAT COMES WITH ME? / WHAT STAYS BEHIND?",
     asset="NEW_V9_FS_01_INCOMPLETE_QUESTION",
     sound="S1, one quiet paper-switch",
     note="Two questions, while the source asks them. No travel imagery."),
  _s(3, 0, 2, "FULL SCREEN", "Your judgment may travel.",
     "Your knowledge of that company’s systems may not.",
     "camera returns on 'And a new industry may still require regulation'",
     display="JUDGMENT: MAY TRAVEL / RELATIONSHIPS: MAY NOT",
     asset="NEW_V9_FS_00_MAY_TRAVEL",
     note="Each side arrives with its sentence. 'May' stays visible on "
          "both."),
 ],
 10: [
  _s(1, 0, 0, "CAMERA", "You finally got the job.",
     "Maybe you changed industries.", "stays on camera",
     display="FIRST 90 DAYS",
     note="Her face and her line first. A short editorial label, not a "
          "welcome sequence."),
  _s(2, 0, 1, "FULL SCREEN",
     "And now you feel this pressure to prove they made the right "
     "decision.", "That pressure can make you do exactly the wrong thing.",
     "camera returns before the next paragraph",
     display="PROVE THEY CHOSE WELL?",
     asset="NEW_V10_FS_00_THE_PRESSURE",
     sound="S1, one subtle click",
     note="Come back quickly so the pressure stays personal."),
  _s(3, 0, 2, "FULL SCREEN",
     "You start trying to fix things before you understand why they work "
     "this way.",
     "You stay quiet because you are afraid of getting something wrong.",
     "camera returns on 'I do not think either one is the job of your "
     "first 90 days'", display="FIX TOO SOON / STAY TOO QUIET",
     asset="NEW_V10_FS_00B_TWO_DEFAULTS",
     states=["NEW_V10_FS_00B_FIX_TOO_SOON",
             "NEW_V10_FS_00C_STAY_TOO_QUIET"],
     note="One default active at a time, each with the sentence that "
          "names it. These are two incomplete defaults, not an "
          "instruction to stop contributing."),
  _s(4, 0, 3, "CAMERA",
     "I do not think either one is the job of your first 90 days.",
     "Your first job is not to prove that everything you already know "
     "works here.", "stays on camera",
     display="CONTRIBUTE WHILE LEARNING THE CONTEXT",
     note="The correction is hers, on camera. No pause icon over a 90-day "
          "calendar. The viewer must not hear 'do nothing.'"),
  _s(5, 0, 4, "FULL SCREEN", "It is to figure out three things",
     "And what can I begin to prove here?",
     "camera returns on 'I think about that as READ. TEST. PROVE.'",
     display="READ / TEST / PROVE",
     asset="NEW_V10_FS_01_READ_TEST_PROVE",
     note="Establish the three, then activate one per spoken question."),
 ],
 11: [
  _s(1, 0, 0, "CAMERA", "You accepted one job.", "You accepted one job.",
     "cuts away within the paragraph",
     display="WHAT I ACCEPTED IS NOT WHAT I AM DOING",
     note="Her sentence begins on camera."),
  _s(2, 0, 0, "FULL SCREEN", "Then you started doing another.",
     "Maybe the salary is the same.",
     "camera returns on 'But three or six weeks in'",
     display="THE JOB I ACCEPTED / THE JOB I STARTED DOING",
     asset="NEW_V11_FS_00_ACCEPTED_AND_DOING",
     sound="S1, one small click on the difference",
     note="Two plain document cards, identical on the title and salary "
          "the script says are identical. The early visual is part of the "
          "hook, not something postponed until teaching."),
  _s(3, 0, 0, "CAMERA",
     "But three or six weeks in, you are thinking: This is not the job I "
     "thought I accepted.", "This is not the job I thought I accepted.",
     "stays on camera", display="THIS ISN’T THE JOB",
     note="Show the recognition, then clear it. Keep the uncertainty."),
  _s(4, 0, 1, "CAMERA",
     "Before you call it a bait-and-switch, slow down.",
     "Companies reorganize.", "stays on camera",
     display="CHANGE IS NOT AUTOMATIC DECEPTION",
     note="Legitimate change stays on camera or a very restrained card. "
          "No lie stamp, siren, angry manager or resignation animation."),
  _s(5, 0, 2, "FULL SCREEN",
     "I use four questions for that: EXPECTED. ACTUAL. COST. CHOICE.",
     "EXPECTED. ACTUAL. COST. CHOICE.",
     "camera returns on 'By the end of this video'",
     display="EXPECTED / ACTUAL / COST / CHOICE",
     asset="NEW_V11_FS_01_FOUR_QUESTIONS",
     sound="S2, one short sound for the first reveal, not four",
     note="The hook reveal the Riverside prompt asks for. The recap at "
          "THE ROLE-DRIFT READ is FS_09's, not this card's."),
 ],
}

NEW_FAMILIES = {
 7: ["NEW_V7_FS_00_TWO_CAPABLE_PEOPLE"],
 8: ["NEW_V8_FS_00_ACCESS_UNAVAILABLE"],
 9: ["NEW_V9_FS_00_MAY_TRAVEL"],
 10: ["NEW_V10_FS_00_THE_PRESSURE", "NEW_V10_FS_00B_TWO_DEFAULTS"],
 11: ["NEW_V11_FS_00_ACCEPTED_AND_DOING"],
}

NEW_STATES = {
 "NEW_V7_FS_00_TWO_CAPABLE_PEOPLE": ["NEW_V7_FS_00_TWO_CAPABLE_PEOPLE",
                                     "NEW_V7_FS_00B_ONE_NAME_COMES_UP"],
 "NEW_V8_FS_00_ACCESS_UNAVAILABLE": ["NEW_V8_FS_00_ACCESS_UNAVAILABLE"],
 "NEW_V9_FS_00_MAY_TRAVEL": ["NEW_V9_FS_00_MAY_TRAVEL"],
 "NEW_V10_FS_00_THE_PRESSURE": ["NEW_V10_FS_00_THE_PRESSURE"],
 "NEW_V10_FS_00B_TWO_DEFAULTS": ["NEW_V10_FS_00B_FIX_TOO_SOON",
                                 "NEW_V10_FS_00C_STAY_TOO_QUIET"],
 "NEW_V11_FS_00_ACCEPTED_AND_DOING": ["NEW_V11_FS_00_ACCEPTED_AND_DOING"],
}




def _resolve_states():
    """Fill each early step's reveal order from the real state names.

    A step names an asset family. The states that family actually renders
    are what the editor cuts to, so they are read from the delivered cue
    table or, for the six new opening families, from NEW_STATES. Guessing
    the family key doubles as a state name is how a map ends up naming a
    file that was never rendered.
    """
    for n, steps in EARLY.items():
        have = {r["key"]: list(r["states"]) for r in ANCHORS.get(n, [])}
        for s_ in steps:
            if not s_["asset"] or s_.get("_fixed"):
                continue
            real = have.get(s_["asset"]) or NEW_STATES.get(s_["asset"])
            if real:
                s_["states"] = real
            s_["_fixed"] = True


def _early_row(n, step):
    lab = [l for l, _ in R.sections(n)][step["section"]]
    return dict(key=step["asset"], section=step["section"],
                para=step["para"], label=lab,
                states=step["states"], kind="EARLY EDIT",
                trigger=step["enter"])


_resolve_states()


def anchors(n):
    """Every cue for this video after relocation, retirement and addition.

    A relocated card carries its whole locator with it. Moving the section
    and paragraph while leaving the old label and the old trigger sentence
    in place is what produced stale labels in the run-of-show and stale
    EXACT TRIGGER passages in the camera map: the row pointed at the new
    paragraph and quoted the old one. Both are re-derived here from the
    reconciled script at the new location.
    """
    labs = [l for l, _ in R.sections(n)]
    rows = []
    for r in ANCHORS.get(n, []):
        if (n, r["key"]) in RETIRE:
            continue
        r = dict(r)
        move = RELOCATE.get((n, r["key"]))
        if move:
            r["section"], r["para"] = move[0], move[1]
            r["kind"] = "RE-CUED"
        if r["section"] is not None:
            r["label"] = labs[r["section"]]
            if r["para"] is not None:
                here = R.sections(n)[r["section"]][1][r["para"]]
                q = R.S._norm(r.get("trigger") or "").lower()
                if not q or q not in R.S._norm(here).lower():
                    r["trigger"] = here
        rows.append(r)
    have = {r["key"] for r in rows}
    for step in EARLY.get(n, []):
        if step["asset"] and step["asset"] not in have:
            rows.append(_early_row(n, step))
            have.add(step["asset"])
    rows.sort(key=lambda r: (r["section"] if r["section"] is not None else 99,
                             r["para"] if r["para"] is not None else 99,
                             r["key"]))
    return rows


def retired(n):
    """Families withdrawn from this video's cue map, with the reason."""
    return [dict(key=k, states=list(r["states"]), reason=RETIRE[(v, k)],
                 was_section=r["section"], was_para=r["para"])
            for (v, k), r in [((v_, k_), r_) for (v_, k_) in RETIRE
                              if v_ == n
                              for r_ in ANCHORS.get(n, [])
                              if r_["key"] == k_]]


def shared(n):
    """Paragraphs still hosting more than one family, after the changes."""
    g = {}
    for r in anchors(n):
        g.setdefault((r["section"], r["para"]), []).append(r["key"])
    return {k: v for k, v in g.items() if len(v) > 1}


def subrange(n, section, para, key):
    """(enter, leave, order) for a family sharing a paragraph, or None."""
    rows = SUBRANGE.get((n, section, para))
    if not rows:
        return None
    for i, (k, a, b) in enumerate(rows, 1):
        if k == key:
            return dict(enter=a, leave=b, order=i, of=len(rows))
    return None


def verify():
    """Every claim this module makes, checked against the script."""
    bad = []

    def has(n, text):
        q = R.S._norm(text).lower()
        return any(q in R.S._norm(p).lower()
                   for _, ps in R.sections(n) for p in ps)

    for (n, key), (si, pi, why) in sorted(RELOCATE.items()):
        secs = R.sections(n)
        if si >= len(secs):
            bad.append("%s: section %d does not exist in V%d"
                       % (key, si + 1, n))
        elif pi >= len(secs[si][1]):
            bad.append("%s: V%d section %d has no paragraph %d"
                       % (key, n, si + 1, pi + 1))
    for n in sorted(EARLY):
        secs = R.sections(n)
        seen = set()
        for s in EARLY[n]:
            tag = "V%d early %d" % (n, s["order"])
            if s["section"] >= len(secs):
                bad.append("%s: no such section" % tag)
                continue
            ps = secs[s["section"]][1]
            if s["para"] >= len(ps):
                bad.append("%s: no such paragraph" % tag)
                continue
            if s["para_out"] >= len(ps):
                bad.append("%s: no such exit paragraph" % tag)
                continue
            p = R.S._norm(ps[s["para"]]).lower()
            q = R.S._norm(ps[s["para_out"]]).lower()
            if R.S._norm(s["enter"]).lower() not in p:
                bad.append("%s: enter wording is not in that paragraph"
                           % tag)
            if R.S._norm(s["leave"]).lower() not in q:
                bad.append("%s: leave wording is not in the exit paragraph"
                           % tag)
            if (s["para"] == s["para_out"]
                    and R.S._norm(s["enter"]).lower() in p
                    and R.S._norm(s["leave"]).lower() in p
                    and p.index(R.S._norm(s["leave"]).lower())
                    < p.index(R.S._norm(s["enter"]).lower())):
                bad.append("%s: leaves before it enters" % tag)
            if s["para_out"] < s["para"]:
                bad.append("%s: exits in an earlier paragraph" % tag)
            if s["mode"] == "FULL SCREEN" and not s["asset"]:
                bad.append("%s: full screen with no asset" % tag)
            if s["mode"] == "CAMERA" and s["asset"]:
                bad.append("%s: camera with an asset" % tag)
            if s["order"] in seen:
                bad.append("%s: duplicate order" % tag)
            seen.add(s["order"])
        order = [s["order"] for s in EARLY[n]]
        if order != sorted(order):
            bad.append("V%d early: steps are out of order" % n)
    for (n, si, pi), rows in sorted(SUBRANGE.items()):
        p = R.S._norm(R.sections(n)[si][1][pi]).lower()
        last = -1
        for key, a, b in rows:
            for field, text in (("enter", a), ("exit", b)):
                if R.S._norm(text).lower() not in p:
                    bad.append("%s: subrange %s wording is not in that "
                               "paragraph" % (key, field))
            if R.S._norm(a).lower() in p:
                i = p.index(R.S._norm(a).lower())
                if i < last:
                    bad.append("%s: subranges overlap or run backwards"
                               % key)
                last = i
    for n in R.VIDEOS:
        sh = shared(n)
        for (si, pi), keys in sorted(sh.items()):
            if not SUBRANGE.get((n, si, pi)):
                bad.append("V%d section %d paragraph %d: %s share one "
                           "paragraph with no sequence"
                           % (n, si + 1, pi + 1, ", ".join(keys)))
        wn = [r for r in anchors(n) if r["key"].endswith("WATCH_NEXT")]
        for w in wn:
            others = [r["key"] for r in anchors(n)
                      if r["section"] == w["section"]
                      and r["para"] == w["para"]
                      and r["key"] != w["key"]]
            if others:
                bad.append("V%d: %s shares the end screen with %s"
                           % (n, w["key"], ", ".join(others)))
    return bad


if __name__ == "__main__":
    bad = verify()
    for n in R.VIDEOS:
        print("V%-3d  %2d cues, %d early steps, %d shared paragraphs"
              % (n, len(anchors(n)), len(EARLY.get(n, [])), len(shared(n))))
    print("\nrelocated %d, retired %d, new families %d, new states %d"
          % (len(RELOCATE), len(RETIRE),
             sum(len(v) for v in NEW_FAMILIES.values()),
             sum(len(v) for v in NEW_STATES.values())))
    print("checks failed: %d" % len(bad))
    for b in bad:
        print("   %s" % b)
