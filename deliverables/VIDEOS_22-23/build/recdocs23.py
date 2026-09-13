# -*- coding: utf-8 -*-
"""The recording documents: the master, and the thought-block copy.

The master is the approved script, unchanged, with production cues placed
beside it rather than inside it. The thought-block copy carries the same
spoken words in delivery-sized units and nothing else, so nothing an editor
needs can be read aloud by mistake.
"""
import os
import masters23 as M
import frames23 as F
import spine23 as SP
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    footer_note, page_break, spoken, marker, cue, caption,
                    notspoken, table)

WPM_LOW, WPM_HIGH = 130, 145


def header(d, n, kind, stamp):
    title_block(d, "capability formation | v%d" % n, M.title(n), kind)
    kv(d, "Thumbnail", M.thumbnail(n))
    kv(d, "Spoken words", "%s" % format(M.word_count(n), ","))
    lo, hi = M.estimate(n)
    kv(d, "Arithmetic estimate", "%s to %s at %d to %d words per minute"
       % (lo, hi, WPM_LOW, WPM_HIGH))
    kv(d, "Source", os.path.basename(M.path(n)))
    kv(d, "Generated", stamp)


def master(n, path, stamp):
    d = base_doc()
    header(d, n, "Recording master", stamp)
    callout(d, "This is the approved script, word for word. The timestamps "
               "are the editorial navigation markers supplied with it. They "
               "are not runtime, not chapters, not Riverside timing and not "
               "SRT timing. Nothing in a bracketed cue is spoken.")
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            mk, label = rest
            marker(d, mk, label)
        elif kind == "CAMERA":
            for p in rest[0]:
                spoken(d, p)
        else:
            f, p = rest
            cue(d, "full screen", f["states"][0]["name"],
                "%d state%s. %s" % (len(f["states"]),
                                    "" if len(f["states"]) == 1 else "s",
                                    f["purpose"]))
            spoken(d, p)
    footer_note(d, "Runtime is observed at Temidayo's natural delivery pace. "
                   "Chapters are created after the final edit, from real "
                   "export timing.")
    d.save(path)
    return path


def _units(text, limit=165):
    """Split one paragraph into delivery-sized thought blocks.

    The split is on sentence ends only. A period inside an abbreviation is
    not a sentence end: "7 or 8 a.m. meetings" is one phrase, and an earlier
    version of this splitter cut it in half. The words never change and their
    order never changes.
    """
    import re
    ABBR = ("a.m", "p.m", "u.s", "e.g", "i.e", "mr", "mrs", "ms", "dr", "vs",
            "st", "no")
    ends = []
    for m in re.finditer(r"[.!?]+[\u201d\u2019\"']?(?=\s|$)", text):
        head = text[:m.start()]
        word = re.split(r"[\s(\u201c\"']", head)[-1].lower().rstrip(".")
        if word in ABBR or len(word) == 1:
            continue
        rest = text[m.end():].lstrip()
        if rest and not (rest[0].isupper() or rest[0] in "\u201c\"'\u2018"):
            continue
        ends.append(m.end())
    parts, prev = [], 0
    for e in ends + ([len(text)] if not ends or ends[-1] < len(text) else []):
        chunk = text[prev:e].strip()
        if chunk:
            parts.append(chunk)
        prev = e
    out, cur = [], ""
    for s in parts:
        trial = (cur + " " + s).strip() if cur else s
        if len(trial) > limit and cur:
            out.append(cur)
            cur = s
        else:
            cur = trial
    if cur:
        out.append(cur)
    return out


def blocks(n, path, stamp):
    d = base_doc()
    header(d, n, "Thought-block recording copy", stamp)
    callout(d, "Spoken words only. Every word below is in the approved "
               "script, in the approved order. Line breaks mark delivery "
               "units, not new sentences, and no editor note appears on "
               "this page.")
    for mk, label, ps in M.sections(n):
        marker(d, mk, label)
        for p in ps:
            for u in _units(p):
                spoken(d, u)
    footer_note(d, "Read the blocks, not the page. A break is a breath.")
    d.save(path)
    return path


def block_words(n):
    """Every word this document will carry, in order."""
    out = []
    for mk, label, ps in M.sections(n):
        for p in ps:
            for u in _units(p):
                out.extend(u.split())
    return out


def matches_script(n):
    a = block_words(n)
    b = M.spoken_text(n).split()
    if a == b:
        return True, "%d words, identical and in order" % len(a)
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return False, "diverges at word %d: %r against %r" % (i, x, y)
    return False, "length differs: %d against %d" % (len(a), len(b))


if __name__ == "__main__":
    for n in M.VIDEOS:
        print("V%d  %s" % (n, matches_script(n)))
