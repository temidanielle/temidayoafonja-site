# -*- coding: utf-8 -*-
"""Stay or Leave? 60-minute flagship, v2.0.9 -> v2.0.10 CANDIDATE.

Six owner decisions, applied exactly.

  1  TIMING. Seventy-five seconds each for the two definition slides is accepted.
     Nothing else in the timeline moves, so this build changes no time at all.

  2  Three "not X, it is Y" constructions in notes are replaced with the wording
     the owner supplied, verbatim.

  3  BANNED WORDS. "actually" and "genuinely" are removed from every note and
     from the appendix face, with the surrounding sentence rewritten where the
     removal left it awkward. The one in the locked scored statement, "would
     have been genuinely hard for me then", is kept and recorded in the QA report
     as a deliberate exception tied to the instrument.

     The owner's brief said twelve note instances. v2.0.9 carries nine, because
     three of the twelve were in the Definitions and Matrix divider notes, which
     v2.0.9 had already replaced with "Divider. Advance immediately." The build
     asserts nine, plus one on the appendix face, plus the locked one kept.

  4  The short "X, not Y" appositives stay. Untouched.

  5  Q&A. The real Questions & Applications slide, the one that says LIVE ONLY
     and RECORDING OFF, is unhidden. The bare "Q & A" divider is hidden.

  6  POLL SLIDES. The appendix version, with the appendix eyebrow and the
     anonymity line, is kept. The other is deleted.

Footer numbers are renumbered again, because unhiding Questions & Applications
adds a numbered slide to the visible core.
"""
import hashlib, os, re, shutil
from pptx import Presentation
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(
    HERE,
    "PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_"
    "v2.0.9_CANDIDATE.pptx")
DST = os.path.join(
    HERE,
    "PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_"
    "v2.0.10_CANDIDATE.pptx")

BANNED = re.compile(r"\b(actually|genuinely|honestly)\b", re.I)
LOCKED = ("Looking back six months, the work I do now would have been "
          "genuinely hard for me then.")

# 2. the owner's three replacements. Patterns are whitespace-tolerant because
#    the stored notes wrap mid-sentence.
NOT_X = [
 (r"A participant who sees several at once is not\s+in trouble,\s*they are in a "
  r"position worth testing sooner than ninety days\.",
  "A participant who sees several at once is in a position worth testing sooner "
  "than ninety days."),
 (r"The Field Kit is not the rest of it\.\s*It is a private system they can own,"
  r"\s*revisit and rerun as conditions change\.",
  "The Field Kit is a private system they can own, revisit, and rerun as "
  "conditions change."),
 (r"It is not an offer,\s*it is not coming back under that name,\s*and it is not"
  r"\s*mentioned here, on slide 23 or in Q&A\.",
  "Leave it unmentioned here, on slide 23, and in Q&A. It does not return under "
  "that name."),
]

# 3. the banned-word rewrites, each asserted to fire an exact number of times
REWRITES = [
 ("rather than the work that actually occurred inside the evidence window",
  "rather than the work that occurred inside the evidence window", 1),
 ("It can describe someone genuinely excellent at the work.",
  "It can describe someone excellent at the work.", 1),
 ("depends on genuinely releasing the people who have enough",
  "depends on releasing the people who have enough", 1),
 ("confirm it has actually stopped before the first question",
  "confirm it has stopped before the first question", 1),
 ("point to the Field Kit if it genuinely fits the question",
  "point to the Field Kit if it fits the question", 3),
 ("Use it only if a delivery genuinely runs ahead",
  "Use it only if a delivery runs ahead", 1),
 ("What translation actually means", "What translation means", 1),
]


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


def face(slide):
    return "\n".join(s.text_frame.text for s in slide.shapes if s.has_text_frame)


def note(slide):
    return slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""


def all_runs(slide):
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    yield r


def drop_slide(prs, index):
    lst = prs.slides._sldIdLst
    entry = list(lst)[index]
    prs.part.drop_rel(entry.rId)
    lst.remove(entry)


def count_banned(prs):
    n = 0
    for s in prs.slides:
        t = face(s) + "\n" + note(s)
        n += len(BANNED.findall(t.replace(LOCKED, "")))
    return n


def build():
    shutil.copyfile(SRC, DST)
    p = Presentation(DST)
    sl = list(p.slides)
    assert len(sl) == 43, f"base is not v2.0.9: {len(sl)} slides"
    assert count_banned(p) == 10, f"expected 10 banned words, found {count_banned(p)}"

    # 6. keep the appendix poll slide, delete the other
    polls = [(i, s) for i, s in enumerate(sl)
             if "What moved when you tested your first read" in face(s)]
    assert len(polls) == 2, f"expected two poll slides, found {len(polls)}"
    keep = [i for i, s in polls if "APPENDIX" in face(s) and "anonymous" in face(s)]
    retire = [i for i, s in polls if i not in keep]
    assert len(keep) == 1 and len(retire) == 1, "cannot tell the poll slides apart"
    drop_slide(p, retire[0])

    # 5. the real Q&A slide comes back; the bare divider goes away
    sl = list(p.slides)
    qa = [s for s in sl if "Questions & Applications" in face(s)]
    assert len(qa) == 1, "Questions & Applications not found once"
    assert qa[0]._element.get("show") == "0", "it was already visible"
    del qa[0]._element.attrib["show"]
    divider = [s for s in sl
               if face(s).strip().startswith("Q & A")
               and "Questions & Applications" not in face(s)
               and s._element.get("show") is None]
    assert len(divider) == 1, f"bare Q & A divider not found once: {len(divider)}"
    divider[0]._element.set("show", "0")

    # 2 and 3. note and face text
    fired = {pat: 0 for pat, _ in NOT_X}
    for s in p.slides:
        if not s.has_notes_slide:
            continue
        tf = s.notes_slide.notes_text_frame
        t = tf.text
        orig = t
        for pat, new in NOT_X:
            t, n = re.subn(pat, new, t)
            fired[pat] += n
        if t != orig:
            tf.text = t
    for pat, n in fired.items():
        assert n == 1, f"replacement fired {n} times: {pat[:52]!r}"

    hits = {old: 0 for old, _, _ in REWRITES}
    for s in p.slides:
        for r in all_runs(s):
            t = r.text
            for old, new, _ in REWRITES:
                if old in t:
                    hits[old] += t.count(old)
                    t = t.replace(old, new)
            if t != r.text:
                r.text = t
        if s.has_notes_slide:
            tf = s.notes_slide.notes_text_frame
            t = tf.text
            orig = t
            for old, new, _ in REWRITES:
                hits[old] += t.count(old)
                t = t.replace(old, new)
            if t != orig:
                tf.text = t
    for old, _, want in REWRITES:
        assert hits[old] == want, \
            f"{old[:46]!r}: fired {hits[old]}, expected {want}"

    # footer numbers, sequential over the visible slides that carry one
    seq = 0
    for s in p.slides:
        if s._element.get("show") == "0":
            continue
        box = [sh for sh in s.shapes
               if sh.has_text_frame and sh.left is not None
               and sh.left > Inches(8.5) and sh.text_frame.text.strip().isdigit()]
        if not box:
            continue
        seq += 1
        set_text(box[0], str(seq))

    p.save(DST)
    verify(seq)
    return DST


def verify(last):
    after = Presentation(DST)
    as_ = list(after.slides)
    assert len(as_) == 42, f"expected 42 slides, got {len(as_)}"

    # 6. one poll slide, hidden, the appendix one
    polls = [s for s in as_ if "What moved when you tested your first read" in face(s)]
    assert len(polls) == 1, f"{len(polls)} poll slides"
    assert polls[0]._element.get("show") == "0", "the poll slide is visible"
    assert "APPENDIX" in face(polls[0]) and "anonymous" in face(polls[0]), \
        "the wrong poll slide was kept"

    # 5. Q&A
    qa = [s for s in as_ if "Questions & Applications" in face(s)]
    assert len(qa) == 1 and qa[0]._element.get("show") is None, "Q&A not visible"
    assert "RECORDING OFF" in face(qa[0]) and "LIVE ONLY" in face(qa[0])
    bare = [s for s in as_ if face(s).strip().startswith("Q & A")
            and "Questions & Applications" not in face(s)]
    assert bare and all(s._element.get("show") == "0" for s in bare), \
        "a bare Q & A slide is still visible"

    # 3. one banned word left, and it is the locked statement
    left = []
    for i, s in enumerate(as_, 1):
        t = face(s) + "\n" + note(s)
        for m in BANNED.finditer(t):
            left.append((i, m.group(0), t[max(0, m.start() - 60):m.start() + 40]))
    assert len(left) == 1, f"banned words left: {[(i, w) for i, w, _ in left]}"
    assert LOCKED in face(as_[left[0][0] - 1]), "the survivor is not the locked statement"

    # 2. the three constructions are gone and the new wording is in
    body = "\n".join(face(s) + "\n" + note(s) for s in as_)
    for gone in ("is not\nin trouble", "is not the rest of it",
                 "It is not an offer"):
        assert gone not in body, f"still present: {gone!r}"
    for fresh in ("is in a position worth testing sooner than ninety days",
                  "The Field Kit is a private system they can own, revisit, and rerun",
                  "Leave it unmentioned here, on slide 23, and in Q&A."):
        assert fresh in body, f"missing: {fresh!r}"

    # nothing else regressed
    assert "—" not in body, "an em dash reappeared"
    assert not re.search(r"\b(travelled|travelling|neighbouring|centre|favourites|"
                         r"recognises|organisational|totalling)\b", body, re.I), \
        "a British spelling reappeared"
    assert "0:00-1:00 IS THE OPENING BLOCK" in body, "the opening block moved"
    assert "TIMING: 2:30-3:45. SEVENTY-FIVE SECONDS." in body
    assert "TIMING: 3:45-5:00. SEVENTY-FIVE SECONDS." in body
    assert "TIMING: 18:00-30:00. TWELVE MINUTES. PROTECTED AND NON-NEGOTIABLE." in body
    assert "Repair formation conditions" not in body
    assert "Seek an external perspective" not in body

    print("built", os.path.basename(DST))
    print(f"  slides: 43 -> {len(as_)}   numbered core slides: {last}")
    print(f"  banned words left: {len(left)} (the locked scored statement)")
    print("  sha256", hashlib.sha256(open(DST, "rb").read()).hexdigest())


if __name__ == "__main__":
    build()
