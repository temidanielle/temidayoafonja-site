# -*- coding: utf-8 -*-
"""Stay or Leave? 60-minute flagship, v2.0.8 -> v2.0.9 CANDIDATE.

Six decisions, applied in one pass. Every edit is asserted before it is made and
counted after, so the build fails rather than saves if the deck is not what this
script expects.

  1  BASE DECK. The September 23 changes are already present in the working copy:
     the four states carry their numerals, in the same colours, and the boundary
     slide already carries the bold seven-categories promise. Only the minute was
     missing, and it is now stated as minute 39 rather than the 38 of the old
     timeline, because the Signals section moved the move categories.

  2  EM DASHES. All 43 replaced, on faces and in notes, each with a period, comma
     or colon chosen for that sentence. Zero remain.

  3  TIMING FAULTS.
       - The welcome slide claimed 1:00-3:00 and overlapped four slides. The
         opening block is now stated as 0:00-1:00, with the title slide holding
         0:00-0:30 and the welcome slide 0:30-1:00, and everything up to the
         5:00 handoff is re-cut so nothing overlaps.
       - "What moved when you tested your first read" leaves the timed core and
         goes to the end of the appendix, hidden.
       - The Definitions and Matrix dividers lose their copied notes and their
         time claims.

  4  SOP AND QA are updated in their own scripts, not here.

  5  CATEGORY WORDING. Two renamed to the approved carousel wording, on the deck
     face and in the speaker note. The other five already match exactly.

  6  VOICE. The Next-Move Note band drops its "not X, it is Y" construction. US
     English throughout: 13 British spellings replaced. The other "not X, it is
     Y" constructions and every use of actually, honestly and genuinely are
     listed in the change log for the owner's decision, not changed here.

Also renumbers the static footer numbers, which is not cosmetic: the welcome
slide was inserted without renumbering, so two slides both read 1 and every
number after them was one low.
"""
import copy, hashlib, os, re, shutil
from pptx import Presentation
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(
    HERE,
    "PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_"
    "v2.0.8_CANDIDATE_signals.pptx")
DST = os.path.join(
    HERE,
    "PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_"
    "v2.0.9_CANDIDATE.pptx")

EM = "—"

# ── 2. em dashes: (old, new, how many times it must occur) ──────────────────
EMDASH = [
 ("for its own sake " + EM + " it is that", "for its own sake. It is that", 1),
 ("WORKED EXAMPLE " + EM + " use if it lands", "WORKED EXAMPLE: use if it lands", 1),
 ("RECORDING ON " + EM + " THIS IS THE LAST RECORDED SLIDE.",
  "RECORDING ON. THIS IS THE LAST RECORDED SLIDE.", 3),
 ("AT 50:00 " + EM + " STOP THE RECORDING BEFORE ADVANCING.",
  "AT 50:00, STOP THE RECORDING BEFORE ADVANCING.", 3),
 ("No evidence line yet " + EM + " that is deliberate",
  "No evidence line yet. That is deliberate", 4),
 ("expected to change " + EM + " that reveal", "expected to change. That reveal", 1),
 ("resolve to high or low " + EM + " you will read",
  "resolve to high or low, you will read", 1),
 ("Say this now, not later " + EM + " it prevents",
  "Say this now, not later. It prevents", 2),
 ("state costs here " + EM + " that block is at 33:00",
  "state costs here. That block is at 33:00", 1),
 ("state costs here " + EM + " that block is at 35:00",
  "state costs here. That block is at 35:00", 1),
 ("still being built " + EM + " it just", "still being built. It just", 2),
 ("waiting for the room " + EM + " this has to work",
  "waiting for the room. This has to work", 1),
 ("protocol is symmetric " + EM + " that is the whole point",
  "protocol is symmetric. That is the whole point", 1),
 ("work that happened " + EM + " not work that was",
  "work that happened, not work that was", 1),
 ("Do not take questions here " + EM + " hold them for minute 50.",
  "Do not take questions here. Hold them for minute 50.", 2),
 ("typical or most frequent " + EM + " this session",
  "typical or most frequent. This session", 1),
 ("Phrases, not essays " + EM + " twelve minutes",
  "Phrases, not essays. Twelve minutes", 1),
 ("when totalling " + EM + " 3? totals as 3", "when totaling: 3? totals as 3", 1),
 ("APPENDIX " + EM + " OPTIONAL, AND OUT OF THE TIMED CORE.",
  "APPENDIX. OPTIONAL, AND OUT OF THE TIMED CORE.", 2),
 ("runs ahead " + EM + " which should not happen " + EM + " or in a longer",
  "runs ahead, which should not happen, or in a longer", 2),
 ('"most people change" ' + EM + " that is a research claim",
  '"most people change." That is a research claim', 2),
 ("APPENDIX " + EM + " live-only.", "APPENDIX. Live-only.", 4),
 ("what changed " + EM + " without internal vocabulary",
  "what changed, without internal vocabulary", 1),
 ("familiar judgment " + EM + " more scope", "familiar judgment: more scope", 1),
 ("OPTIONAL INSTITUTIONAL CLOSE " + EM + " use INSTEAD of",
  "OPTIONAL INSTITUTIONAL CLOSE. Use INSTEAD of", 1),
]

# ── 6. US English: (word, replacement, how many) ────────────────────────────
USENGLISH = [
 ("travelled", "traveled", 1),
 ("travelling", "traveling", 1),
 ("neighbouring", "neighboring", 6),
 ("centre", "center", 1),
 ("favourites", "favorites", 1),
 ("recognises", "recognizes", 1),
 ("organisational", "organizational", 1),
]

# ── 5. category wording ─────────────────────────────────────────────────────
CATEGORIES = [
 ("Repair formation conditions", "Repair the conditions", 2),
 ("Seek an external perspective", "Seek an outside perspective", 1),
]
CAROUSEL = ["Remain and deepen", "Translate what is built", "Widen exposure",
            "Test portability", "Repair the conditions", "Prepare for exit",
            "Seek an outside perspective"]

# ── 3. timing: (slide, old, new) ────────────────────────────────────────────
TIMING = [
 (2, "TIMING: 1:00-3:00.",
     "TIMING: 0:00-1:00 IS THE OPENING BLOCK. Slide 1 holds 0:00-0:30 and this "
     "slide holds 0:30-1:00. Two sentences of biography, then the question, then "
     "advance. If you are still talking at 1:00 you have taken the reframe's time."),
 (3, "TIMING: 0:30-1:20. FIFTY SECONDS.", "TIMING: 1:00-1:50. FIFTY SECONDS."),
 (4, "Deliver it here, at minute 1:20.", "Deliver it here, at minute 1:50."),
 (4, "TIMING: 1:20-2:00. FORTY SECONDS.", "TIMING: 1:50-2:30. FORTY SECONDS."),
 (6, "TIMING: 2:00-3:30. NINETY SECONDS.",
     "TIMING: 2:30-3:45. SEVENTY-FIVE SECONDS."),
 (7, "TIMING: 3:30-5:00. NINETY SECONDS.",
     "TIMING: 3:45-5:00. SEVENTY-FIVE SECONDS."),
]
DIVIDER_NOTE = "Divider. Advance immediately."
DIVIDERS = [(5, "Definitions"), (14, "Matrix")]

WHAT_MOVED = 23          # leaves the timed core
BOUNDARY = 4
MATRIX = 15
SEVEN = 28
NEXT_MOVE = 29

BAND_OLD = ("This is a note, not a decision. It records what your evidence "
            "supports testing next.")
BAND_NEW = "This note records what your evidence supports testing next."

TEASE_OLD = "Give you a defensible reading of your current position, and "
TEASE_NEW = ("Give you a defensible reading of your current position, and at "
             "minute 39, ")


# ── helpers ─────────────────────────────────────────────────────────────────
def carrier(shape):
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


def all_runs(slide):
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    yield r


def sweep(prs, pairs, regex=False):
    """Apply (old, new, count) across every face run and every note, counting."""
    done = {old: 0 for old, _, _ in pairs}
    for s in prs.slides:
        for r in all_runs(s):
            t = r.text
            for old, new, _ in pairs:
                if regex:
                    t2, n = re.subn(r"\b%s\b" % old, new, t)
                else:
                    n = t.count(old)
                    t2 = t.replace(old, new)
                if n:
                    done[old] += n
                    t = t2
            if t != r.text:
                r.text = t
        if s.has_notes_slide:
            tf = s.notes_slide.notes_text_frame
            t = tf.text
            orig = t
            for old, new, _ in pairs:
                if regex:
                    t, n = re.subn(r"\b%s\b" % old, new, t)
                else:
                    n = t.count(old)
                    t = t.replace(old, new)
                done[old] += n
            if t != orig:
                tf.text = t
    for old, _, want in pairs:
        assert done[old] == want, \
            f"{old[:48]!r}: replaced {done[old]}, expected {want}"
    return sum(done.values())


def note_edit(slide, old, new):
    tf = slide.notes_slide.notes_text_frame
    t = tf.text
    assert old in t, f"note text not found: {old[:60]!r}"
    tf.text = t.replace(old, new)


def move_slide(prs, from_pos, to_pos):
    lst = prs.slides._sldIdLst
    entry = list(lst)[from_pos]
    lst.remove(entry)
    lst.insert(to_pos, entry)


def count_em(prs):
    n = 0
    for s in prs.slides:
        n += "\n".join(sh.text_frame.text for sh in s.shapes
                       if sh.has_text_frame).count(EM)
        if s.has_notes_slide:
            n += s.notes_slide.notes_text_frame.text.count(EM)
    return n


def build():
    shutil.copyfile(SRC, DST)
    p = Presentation(DST)
    sl = list(p.slides)
    assert len(sl) == 43, "base is not the 43-slide v2.0.8"
    assert count_em(p) == 43, f"expected 43 em dashes, found {count_em(p)}"

    # 1. the boundary tease gains its minute
    run = carrier(sl[BOUNDARY - 1].shapes[5])
    assert run.text == TEASE_OLD, f"boundary IT WILL reads {run.text!r}"
    run.text = TEASE_NEW
    assert sl[BOUNDARY - 1].shapes[5].text_frame.text.startswith(TEASE_NEW)

    # the four states already carry their numerals, in the right colours
    labels = [sl[MATRIX - 1].shapes[i].text_frame.text for i in (10, 4, 13, 7)]
    assert labels == ["1   STAGNANT", "2   DEPTH TRAP", "3   FRAGILE",
                      "4   COMPOUNDING"], labels

    # 2. em dashes
    n_em = sweep(p, EMDASH)
    assert count_em(p) == 0, f"{count_em(p)} em dashes left"

    # 6. US English, then the voice change on the Next-Move Note band
    n_us = sweep(p, USENGLISH, regex=True)
    band = [sh for sh in sl[NEXT_MOVE - 1].shapes
            if sh.has_text_frame and sh.text_frame.text.strip() == BAND_OLD]
    assert len(band) == 1, "Next-Move Note band not found once"
    set_text(band[0], BAND_NEW)

    # 5. category wording
    n_cat = sweep(p, CATEGORIES)
    face = "\n".join(sh.text_frame.text for sh in sl[SEVEN - 1].shapes
                     if sh.has_text_frame)
    for nm in CAROUSEL:
        assert face.count(nm) == 1, f"category not on slide 28 once: {nm}"

    # 3. timing and dividers
    for idx, old, new in TIMING:
        note_edit(sl[idx - 1], old, new)
    for idx, name in DIVIDERS:
        s = sl[idx - 1]
        txt = "\n".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
        assert name in txt, f"slide {idx} is not the {name} divider"
        s.notes_slide.notes_text_frame.text = DIVIDER_NOTE

    # 3b. the poll slide leaves the timed core for the end of the appendix
    wm = sl[WHAT_MOVED - 1]
    assert "What moved when you tested your first read" in \
        "\n".join(sh.text_frame.text for sh in wm.shapes if sh.has_text_frame)
    move_slide(p, WHAT_MOVED - 1, len(sl) - 1)
    wm._element.set("show", "0")

    # footer numbers, sequential over the visible slides that carry one
    seq = 0
    renumbered = []
    for s in p.slides:
        if s._element.get("show") == "0":
            continue
        box = [sh for sh in s.shapes
               if sh.has_text_frame and sh.left is not None
               and sh.left > Inches(8.5) and sh.text_frame.text.strip().isdigit()]
        if not box:
            continue
        seq += 1
        old = box[0].text_frame.text.strip()
        if old != str(seq):
            renumbered.append((old, seq))
        set_text(box[0], str(seq))

    p.save(DST)
    verify(n_em, n_us, n_cat, renumbered, seq)
    return DST


def verify(n_em, n_us, n_cat, renumbered, last):
    before, after = Presentation(SRC), Presentation(DST)
    bs, as_ = list(before.slides), list(after.slides)
    assert len(as_) == 43, f"slide count moved: {len(as_)}"
    assert count_em(after) == 0, "an em dash survived"

    def face(x):
        return "\n".join(s.text_frame.text for s in x.shapes if s.has_text_frame)

    # the poll slide is last and hidden; nothing else changed position
    assert "What moved when you tested your first read" in face(as_[-1])
    assert as_[-1]._element.get("show") == "0", "the poll slide is not hidden"

    # no British spelling survives
    brit = re.compile(r"\b(travelled|travelling|neighbouring|centre|favourites|"
                      r"recognises|organisational|totalling)\b", re.I)
    for i, s in enumerate(as_, 1):
        t = face(s) + (s.notes_slide.notes_text_frame.text
                       if s.has_notes_slide else "")
        m = brit.search(t)
        assert not m, f"slide {i} still British: {m.group(0)}"

    # the retired category names are gone everywhere
    for i, s in enumerate(as_, 1):
        t = face(s) + (s.notes_slide.notes_text_frame.text
                       if s.has_notes_slide else "")
        assert "Repair formation conditions" not in t, f"slide {i}"
        assert "Seek an external perspective" not in t, f"slide {i}"

    # the opening no longer overlaps: the six delivery windows must tile
    # 0:00 to 5:00 exactly, with no gap and no overlap. Slide 2 states the
    # parent block as well as its own window, so its window is read from the
    # sentence that names it rather than from the first pair of times.
    def secs(t):
        m, s = t.split(":")
        return int(m) * 60 + int(s)

    def window(slide, pat):
        n = slide.notes_slide.notes_text_frame.text
        m = re.search(pat, n)
        assert m, f"window not found: {pat}"
        return secs(m.group(1)), secs(m.group(2))

    wins = [window(as_[0], r"TIMING: (\d+:\d\d)-(\d+:\d\d)"),
            window(as_[1], r"this slide holds (\d+:\d\d)-(\d+:\d\d)"),
            window(as_[2], r"TIMING: (\d+:\d\d)-(\d+:\d\d)"),
            window(as_[3], r"TIMING: (\d+:\d\d)-(\d+:\d\d)"),
            window(as_[5], r"TIMING: (\d+:\d\d)-(\d+:\d\d)"),
            window(as_[6], r"TIMING: (\d+:\d\d)-(\d+:\d\d)")]
    assert wins[0][0] == 0, f"the opening does not start at 0:00: {wins}"
    for (a1, b1), (a2, b2) in zip(wins, wins[1:]):
        assert b1 == a2, f"gap or overlap in the opening: {b1} then {a2} ({wins})"
    assert wins[-1][1] == 300, f"the opening does not hand off at 5:00: {wins}"
    # the welcome slide's parent block is the first minute and nothing else
    assert "0:00-1:00 IS THE OPENING BLOCK" in as_[1].notes_slide.notes_text_frame.text
    # the dividers make no time claim
    for idx, _ in DIVIDERS:
        assert as_[idx - 1].notes_slide.notes_text_frame.text == DIVIDER_NOTE
        assert not re.search(r"\d+:\d\d", DIVIDER_NOTE)

    # located by title, because moving the poll slide shifted every index after it
    nm = [s for s in as_ if "The Next-Move Note" in face(s)]
    assert len(nm) == 1, "the Next-Move Note slide is not there once"
    assert BAND_NEW in face(nm[0])
    assert BAND_OLD not in face(nm[0])
    assert "Two signals I will watch before my rescore date" in face(nm[0])

    print("built", os.path.basename(DST))
    print(f"  em dashes replaced: {n_em}   remaining: {count_em(after)}")
    print(f"  British spellings replaced: {n_us}")
    print(f"  category renames applied: {n_cat}")
    print(f"  footer numbers renumbered: {len(renumbered)}, last is {last}")
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())


if __name__ == "__main__":
    build()
