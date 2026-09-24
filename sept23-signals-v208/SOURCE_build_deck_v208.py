# -*- coding: utf-8 -*-
"""Stay or Leave? 60-minute flagship: add the Signals Worth Watching section.

Base is the owner's own working deck, the file uploaded as
USE_FINAL_..._v2.0.7_CANDIDATE_s12-clarifier_s20-reordered.pptx (40 slides,
Google Slides round trip). Its slide numbers are the ones the brief cites:
slide 33 is the Position Exposure Signals appendix and slide 24 is State Costs.

WHAT THIS BUILD DOES

  1. Three new slides are inserted after State Costs and before Seven
     Categories of Move, so the order is: read your position, see what each
     state costs, learn what to watch, then choose a move.

     Every new slide is cloned from slide 25, Seven Categories of Move, so the
     eyebrow, title, subtitle, numbered chips, body text and footer all inherit
     the deck's own styling rather than being drawn with guessed values. The
     source of the content is the existing appendix slide 33 and the State
     Costs line "a strong current position still requires renewal", promoted
     and expanded. No new framework terms are introduced.

  2. The Next-Move Note slide gains one line under WHAT HAPPENS NEXT:
     "Two signals I will watch before my rescore date: ______ and ______"
     The three prompt blocks are tightened by a tenth of an inch each to make
     room, so nothing is pushed off the slide and the closing navy band stays
     where it is.

  3. Footer numbers are renumbered from the insertion point on, because they
     are static text: the new slides take 22, 23 and 24, and every later
     numbered slide moves up by three.

  4. The recorded timeline is re-cut so the section fits inside the same fifty
     recorded minutes. See TIMING below.

TIMING

The brief asked for about two minutes per new slide. Six minutes do not exist
in this session. The trims the brief authorises, calibration and the corrected
read, yield two minutes, and one more comes from the close buffer:

     calibration          16:00-19:00  ->  16:00-18:00     minus 1:00
     re-total             31:00-32:30  ->  30:00-31:00     minus 0:30
     sensitivity check    32:30-34:00  ->  31:00-32:00     minus 0:30
     close buffer          2:00 long   ->   1:00 long      minus 1:00

That is three minutes, so the section runs at sixty seconds a slide. The
twelve-minute evidence block is shifted, never shortened. Q&A still starts at
50:00 and the session still ends at 60:00. Getting to six minutes would mean
taking three from the protected block or from Q&A, which this build does not do.

Each new slide's speaker note carries about two minutes of material as the
brief asked. The note states plainly which part is the sixty-second live read
and which part is there for the replay and for questions.

BOUNDARY

Every signal is phrased as something to examine. There are no forecasts, no
statistics and no claims about the job market or about any employer. The notes
say twice that noticing a signal is a reason to gather evidence, not a reason
to panic or to leave.

No em dash is introduced anywhere by this build.
"""
import copy, hashlib, os, re, shutil
from pptx import Presentation
from pptx.util import Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "INPUT_USE_FINAL_v2.0.7_working_copy.pptx")
DST = os.path.join(
    HERE,
    "PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_"
    "v2.0.8_CANDIDATE_signals.pptx")

TEMPLATE = 25          # Seven categories of move: eyebrow, title, subtitle,
                       # seven numbered rows, a rust footer line, page number
STATE_COSTS = 24
NEXT_MOVE = 26

# slide 25's shape indices, grouped
ROWS = [(3, 4, 5, 6), (7, 8, 9, 10), (11, 12, 13, 14), (15, 16, 17, 18),
        (19, 20, 21, 22), (23, 24, 25, 26), (27, 28, 29, 30)]
EYEBROW, TITLE, SUBTITLE, RUSTLINE, PAGENO = 0, 1, 2, 31, 33

ROLE = [
 "Your mandate is being absorbed, narrowed, duplicated, or redefined again.",
 "Decisions about your work are being made in rooms you are no longer in.",
 "Your role exists because of one sponsor, and that sponsor's position is changing.",
 "Few people outside your manager would notice if your function disappeared.",
 "The routine parts of your work are getting easier to automate or reproduce.",
]
FINE = [
 "You cannot name what you are learning right now.",
 "You are being praised for the same things as last year.",
 "Your last unfamiliar problem was more than 90 days ago.",
 "Your evidence has not been updated in a quarter.",
 "People outside your organization have not seen your recent work.",
]

OPENER_BODY = ("Your reading describes the last ninety days. These signals tell "
               "you what to watch between now and your next read.")

NOTE_A = """RECORDING ON.

TIMING: 36:00-37:00. SIXTY SECONDS LIVE.

FACILITATION: frame the section and move. Do not start listing signals here, the
two slides that follow carry them. Sixty seconds.

WHAT TO SAY: "Your reading describes the last ninety days. It is accurate for
that window and it will go out of date. These next two slides are what to watch
between now and your rescore date."

SAY THE BOUNDARY IN ONE LINE AND DO NOT EXPAND IT: these are questions to
investigate, not predictions. Nothing here forecasts a layoff, diagnoses an
employer or claims anything about the job market. If a participant hears a
forecast, correct it plainly: a signal tells you where to go and look, it does
not tell you what is going to happen.

WHY THIS SITS HERE AND NOT EARLIER. They have just seen what their state costs.
A cost is about the position they are in now. A signal is about the position
drifting while they are not watching. One belongs before the move categories,
the other after the read, and this is the only place both are true.

FOR THE REPLAY AND FOR QUESTIONS, NOT FOR THE LIVE SIXTY SECONDS: the honest
reason this section exists is that the instrument reads a ninety-day window.
Anything that reads a window goes stale. Signals are the cheapest way to notice
staleness early, and noticing early is the difference between choosing a move
and being handed one. None of that needs saying out loud tonight.

DO NOT turn this into a discussion. No hands, no examples from the room, no
naming of employers."""

NOTE_B = """RECORDING ON.

TIMING: 37:00-38:00. SIXTY SECONDS LIVE. About twelve seconds a signal.

FACILITATION: read the five once, in order, and stop. Do not explain any of them
and do not add an example. The footer line is the only interpretation this slide
needs, and you say it last.

FOOTER LINE, SAY IT EXACTLY: "One signal is something to examine. Several
together are worth testing a move."

THESE ARE QUESTIONS, NOT VERDICTS. Each line is something a participant can go
and check against their own last ninety days. None of them is evidence on its
own, and none of them says anything about what an employer is going to do. If
someone treats one as a prediction, say it plainly: noticing a signal is a
reason to gather evidence, never a reason to panic and never a reason to leave.

WHERE THESE COME FROM. This is the Position Exposure Signals appendix, promoted
into the recorded core and expanded. It used to be a Q&A card. It is here now
because the people who most need it are the ones who never asked the question.

FOR THE REPLAY, NOT FOR THE LIVE SIXTY SECONDS: signals one, two and three are
about where decisions and authority sit. Four and five are about how replaceable
the function looks from outside. A participant who sees several at once is not
in trouble, they are in a position worth testing sooner than ninety days.

DO NOT ask who recognises which signal. Same rule as the matrix. Their reading
stays theirs."""

NOTE_C = """RECORDING ON.

TIMING: 38:00-39:00. SIXTY SECONDS LIVE. About twelve seconds a signal.

FACILITATION: read the five once, read the footer line, then move to the move
categories. Sixty seconds.

FOOTER LINE, SAY IT EXACTLY: "Choose two signals to watch before your rescore
date." Two, not five. A watch list nobody keeps is worse than no watch list.

WHY THIS SLIDE EXISTS. Compounding is the state most likely to feel fine, which
makes it the state least likely to notice drift. The state costs slide already
says a strong current position still requires renewal. This slide is what that
sentence looks like in practice. Say the subtitle out loud, it is doing the work.

THIS IS NOT A WARNING TO PEOPLE WHO SCORED WELL. A strong reading is a real
reading. The point is that it describes ninety days that have already happened,
and renewal is what keeps it true. Noticing a signal here is a reason to gather
evidence, not a reason to doubt the score they just worked twelve minutes for.

FOR THE REPLAY, NOT FOR THE LIVE SIXTY SECONDS: the first three signals are
about formation going quiet, the last two are about evidence going stale. Both
are cheap to check and both are invisible from inside a role that is going well.

HAND OFF INTO THE MOVE CATEGORIES: "Two signals to watch. Now the seven
directions your evidence might support testing." Do not linger."""

# Speaker-note timing edits. Every entry is asserted before it is applied.
NOTE_EDITS = {
 15: [("that block is at 35:00", "that block is at 33:00")],
 18: [("TIMING: 16:00-19:00. THREE MINUTES. Sixty seconds each.",
       "TIMING: 16:00-18:00. TWO MINUTES. Forty seconds each.")],
 19: [("TIMING: 19:00-31:00. TWELVE MINUTES.",
       "TIMING: 18:00-30:00. TWELVE MINUTES."),
      ("If you are behind at minute 19, take the time from the 45:00-48:00 "
       "continuation sequence or the 48:00-50:00 buffer",
       "If you are behind at minute 18, take the time from the 46:00-48:00 "
       "continuation sequence or the 49:00-50:00 buffer"),
      ("ONE MIDPOINT CUE AT ABOUT 25:00.", "ONE MIDPOINT CUE AT ABOUT 24:00."),
      ("two-minute warning at 29:00 and a thirty-second warning at 30:30",
       "two-minute warning at 28:00 and a thirty-second warning at 29:30")],
 20: [("TIMING: 31:00-32:30. NINETY SECONDS.", "TIMING: 30:00-31:00. SIXTY SECONDS.")],
 21: [("TIMING: 32:30-34:00. NINETY SECONDS.", "TIMING: 31:00-32:00. SIXTY SECONDS.")],
 22: [("TIMING: 34:00-35:00. SIXTY SECONDS.", "TIMING: 32:00-33:00. SIXTY SECONDS.")],
 24: [("TIMING: 35:00-38:00. THREE MINUTES.", "TIMING: 33:00-36:00. THREE MINUTES."),
      ("Take it from 45:00-48:00.", "Take it from 46:00-48:00.")],
 25: [("TIMING: 38:00-41:00. THREE MINUTES.", "TIMING: 39:00-42:00. THREE MINUTES.")],
 26: [("TIMING: 41:00-45:00. FOUR MINUTES.", "TIMING: 42:00-46:00. FOUR MINUTES."),
      ("Give a sixty-second warning at 44:00.",
       "Give a sixty-second warning at 45:00.")],
 27: [("TIMING: 45:00-46:00. SIXTY SECONDS.", "TIMING: 46:00-47:00. SIXTY SECONDS.")],
 28: [("TIMING: 46:00-47:00. SIXTY SECONDS.", "TIMING: 47:00-48:00. SIXTY SECONDS.")],
 29: [("TIMING: 47:00-50:00. The close is delivered 47:00-48:00; 48:00-50:00 is "
       "FACILITATION BUFFER",
       "TIMING: 48:00-50:00. The close is delivered 48:00-49:00; 49:00-50:00 is "
       "FACILITATION BUFFER")],
}

# Static footer numbers that must move up by three, as (slide, old, new).
RENUMBER = [(25, "22", "25"), (26, "23", "26"), (27, "24", "27"),
            (28, "25", "28"), (32, "26", "29")]

NAVY = "0F2347"


# ── helpers ─────────────────────────────────────────────────────────────────
def carrier(shape):
    """The run holding a shape's text, skipping empty leading runs."""
    first = shape.text_frame.paragraphs[0]
    return next((r for r in first.runs if r.text.strip()), first.runs[0])


def set_text(shape, text):
    tf = shape.text_frame
    first = tf.paragraphs[0]
    keep = carrier(shape)
    for p in tf.paragraphs[1:]:
        p._element.getparent().remove(p._element)
    for r in list(first.runs):
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)
    keep.text = text
    return keep


def place(shape, left=None, top=None, width=None, height=None):
    if left is not None:
        shape.left = Inches(left)
    if top is not None:
        shape.top = Inches(top)
    if width is not None:
        shape.width = Inches(width)
    if height is not None:
        shape.height = Inches(height)


def drop(shape):
    shape._element.getparent().remove(shape._element)


def clone_slide(prs, index):
    """Copy a slide, shapes and all, onto the end of the deck."""
    src = prs.slides[index]
    dest = prs.slides.add_slide(src.slide_layout)
    for shp in list(dest.shapes):          # clear the layout's placeholders
        drop(shp)
    for shp in src.shapes:
        dest.shapes._spTree.append(copy.deepcopy(shp._element))
    sid = 10
    for cn in dest.shapes._spTree.iter():
        if cn.tag.endswith("}cNvPr") and cn.get("id") != "1":
            cn.set("id", str(sid))
            cn.set("name", "Signals;%d" % sid)
            sid += 1
    return dest


def move_slide(prs, from_pos, to_pos):
    lst = prs.slides._sldIdLst
    entry = list(lst)[from_pos]
    lst.remove(entry)
    lst.insert(to_pos, entry)


def signal_slide(prs, title, subtitle, items, footer, note):
    """Five numbered signals on the seven-categories layout."""
    s = clone_slide(prs, TEMPLATE - 1)
    shp = list(s.shapes)
    for chip, num, label, desc in ROWS[5:]:   # rows six and seven go
        for i in (chip, num, label, desc):
            drop(shp[i])

    set_text(shp[EYEBROW], "SIGNALS")
    set_text(shp[TITLE], title)
    if subtitle is None:
        drop(shp[SUBTITLE])
        tops = [1.80, 2.45, 3.10, 3.75, 4.40]
    else:
        set_text(shp[SUBTITLE], subtitle)
        tops = [1.94, 2.54, 3.14, 3.74, 4.34]

    for (chip, num, label, desc), top, text in zip(ROWS[:5], tops, items):
        place(shp[chip], top=top)
        place(shp[num], top=top)
        place(shp[label], left=1.08, top=top - 0.02, width=8.30, height=0.30)
        run = set_text(shp[label], text)
        run.font.bold = False
        drop(shp[desc])

    set_text(shp[RUSTLINE], footer)
    s.notes_slide.notes_text_frame.text = note
    return s


def opener_slide(prs, next_move_slide, note):
    """Title, subtitle and one framing line in a panel."""
    s = clone_slide(prs, TEMPLATE - 1)
    shp = list(s.shapes)
    for chip, num, label, desc in ROWS:
        for i in (chip, num, label, desc):
            drop(shp[i])
    drop(shp[RUSTLINE])

    set_text(shp[EYEBROW], "SIGNALS")
    set_text(shp[TITLE], "Signals Worth Watching")
    set_text(shp[SUBTITLE], "Questions to investigate, not predictions.")

    # the pale panel, its gold accent and the body line, taken from the
    # Next-Move Note slide so the treatment is one the deck already uses
    src = list(next_move_slide.shapes)
    for el, geom in ((src[25], (0.62, 2.85, 8.76, 0.92)),
                     (src[26], (0.62, 2.85, 0.045, 0.92))):
        new = copy.deepcopy(el._element)
        s.shapes._spTree.append(new)
        place(s.shapes[-1], *geom)
    body = copy.deepcopy(src[27]._element)
    s.shapes._spTree.append(body)
    shape = s.shapes[-1]
    place(shape, 0.90, 3.11, 8.20, 0.42)
    run = set_text(shape, OPENER_BODY)
    run.font.bold = False
    run.font.size = Pt(12.5)

    s.notes_slide.notes_text_frame.text = note
    return s


def set_pageno(slide, old, new):
    hits = [sh for sh in slide.shapes
            if sh.has_text_frame and sh.text_frame.text.strip() == old
            and sh.left > Inches(8.5)]
    assert len(hits) == 1, f"page number {old} not found once: {len(hits)}"
    set_text(hits[0], new)


# ── build ───────────────────────────────────────────────────────────────────
def build():
    shutil.copyfile(SRC, DST)
    p = Presentation(DST)
    assert len(p.slides._sldIdLst) == 40, "base deck is not the 40-slide copy"
    sl = list(p.slides)
    assert "What each state costs" in sl[STATE_COSTS - 1].shapes[1].text_frame.text
    assert "Seven categories of move" in sl[TEMPLATE - 1].shapes[1].text_frame.text
    assert "The Next-Move Note" in sl[NEXT_MOVE - 1].shapes[1].text_frame.text

    # 1. speaker-note timings, on the original numbering
    for idx, edits in NOTE_EDITS.items():
        tf = sl[idx - 1].notes_slide.notes_text_frame
        text = tf.text
        for old, new in edits:
            assert old in text, f"slide {idx}: not found: {old[:60]!r}"
            text = text.replace(old, new)
        tf.text = text

    # 2. static footer numbers
    for idx, old, new in RENUMBER:
        set_pageno(sl[idx - 1], old, new)

    # 3. the Next-Move Note gains the signals line
    nm = sl[NEXT_MOVE - 1]
    ns = list(nm.shapes)
    assert ns[17].text_frame.text.strip() == "WHAT HAPPENS NEXT"
    for i, dy in ((3, -0.02), (4, -0.02), (5, -0.02), (6, -0.02), (7, -0.02), (8, -0.02),
                  (9, -0.06), (10, -0.06), (11, -0.06), (12, -0.06), (13, -0.06), (14, -0.06),
                  (15, -0.10), (16, -0.10), (17, -0.10), (18, -0.10), (19, -0.10), (20, -0.10),
                  (21, 0.10), (22, 0.10)):
        ns[i].top = ns[i].top + Inches(dy)
    ns[15].height = Inches(1.06)     # WHAT HAPPENS NEXT panel
    ns[16].height = Inches(1.06)     # and its gold accent
    line = copy.deepcopy(ns[18]._element)
    nm.shapes._spTree.append(line)
    place(nm.shapes[-1], 0.86, 4.32, 8.28, 0.24)
    set_text(nm.shapes[-1],
             "Two signals I will watch before my rescore date: ______ and ______")

    # 4. the three new slides, built at the end then moved into place
    opener = opener_slide(p, nm, NOTE_A)
    slide_b = signal_slide(p, "Signals around your role", None, ROLE,
                           "One signal is something to examine. Several together "
                           "are worth testing a move.", NOTE_B)
    slide_c = signal_slide(
        p, "Signals when things feel fine",
        "Compounding is the state most likely to feel fine. A strong position "
        "still needs renewal.", FINE,
        "Choose two signals to watch before your rescore date.", NOTE_C)
    for n, (slide, pageno) in enumerate(((opener, "22"), (slide_b, "23"),
                                         (slide_c, "24"))):
        hits = [sh for sh in slide.shapes
                if sh.has_text_frame and sh.left > Inches(8.5)]
        assert len(hits) == 1, "page number box missing on a new slide"
        set_text(hits[0], pageno)
        move_slide(p, 40 + n, STATE_COSTS + n)

    p.save(DST)
    verify()
    return DST


def verify():
    before, after = Presentation(SRC), Presentation(DST)
    bs, as_ = list(before.slides), list(after.slides)
    assert len(as_) == 43, f"expected 43 slides, got {len(as_)}"

    def face(x):
        return "\n".join(s.text_frame.text for s in x.shapes if s.has_text_frame)

    def note(x):
        return x.notes_slide.notes_text_frame.text if x.has_notes_slide else ""

    titles = [as_[i].shapes[1].text_frame.text for i in (24, 25, 26)]
    assert titles[0].startswith("Signals Worth Watching"), titles
    assert titles[1] == "Signals around your role", titles
    assert titles[2] == "Signals when things feel fine", titles
    assert "What each state costs" in face(as_[23]), "State Costs is not before"
    assert "Seven categories of move" in face(as_[27]), "Move Categories not after"

    # the three new slides are the only new content; everything else maps 1:1
    pairs = [(bs[i], as_[i]) for i in range(24)] + \
            [(bs[i], as_[i + 3]) for i in range(24, 40)]
    changed = sorted({i + 1 for i, (b, a) in enumerate(pairs) if face(b) != face(a)} |
                     {i + 1 for i, (b, a) in enumerate(pairs) if note(b) != note(a)})
    expect = sorted(set(NOTE_EDITS) | {i for i, _, _ in RENUMBER} | {NEXT_MOVE})
    assert changed == expect, f"changed {changed}, expected {expect}"

    # nothing this build wrote contains an em dash
    new_text = "\n".join(face(as_[i]) + note(as_[i]) for i in (24, 25, 26))
    new_text += face(as_[NEXT_MOVE + 2])
    assert "—" not in new_text, "an em dash was introduced"

    # the protected block is shifted, never shortened
    n = note(as_[18])
    assert "TIMING: 18:00-30:00. TWELVE MINUTES. PROTECTED AND NON-NEGOTIABLE." in n
    # Q&A still starts at 50:00
    assert "TIMING: 50:00-60:00" in note(as_[34])

    # every signal is on the face, once
    for item in ROLE:
        assert face(as_[25]).count(item) == 1, f"missing: {item[:40]}"
    for item in FINE:
        assert face(as_[26]).count(item) == 1, f"missing: {item[:40]}"
    assert "Two signals I will watch before my rescore date" in face(as_[NEXT_MOVE + 2])

    print("built", os.path.basename(DST))
    print("  slides:", len(bs), "->", len(as_))
    print("  changed pre-existing slides:", changed)
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())


if __name__ == "__main__":
    build()
