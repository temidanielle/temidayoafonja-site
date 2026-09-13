# -*- coding: utf-8 -*-
"""Recording master and thought-block copy for the new scripts."""
import os, re
import masters23b as M
import spine23b as SP
from docs23 import (base_doc, title_block, h, kv, para, callout, footer_note,
                    spoken, marker, cue)

WPM_LOW, WPM_HIGH = 130, 145


def header(d, n, kind, stamp):
    title_block(d, "capability formation | v%d" % n, M.title(n), kind)
    kv(d, "Thumbnail", M.script_header_thumbnail(n))
    kv(d, "Spoken words", "%s by whitespace count, %s as supplied"
       % (format(M.word_count(n), ","), format(M.DECLARED_WORDS[n], ",")))
    lo, hi = M.estimate(n)
    kv(d, "Arithmetic estimate", "%s to %s at %d to %d words per minute"
       % (lo, hi, WPM_LOW, WPM_HIGH))
    kv(d, "Source", M.read(n)["file"])
    kv(d, "Source SHA-256", M.read(n)["sha"])
    kv(d, "Generated", stamp)


def master(n, path, stamp):
    d = base_doc()
    header(d, n, "Recording master", stamp)
    callout(d, "This is the approved script, word for word. The bracketed "
               "headings are section labels, not timing markers: this script "
               "carries no timestamps at all. Nothing in a bracketed cue is "
               "spoken.")
    for kind, *rest in SP.spine(n):
        if kind == "SECTION":
            seq, label = rest
            marker(d, "%d" % seq, label)
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


ABBR = ("a.m", "p.m", "u.s", "e.g", "i.e", "mr", "mrs", "ms", "dr", "vs",
        "st", "no")


def _units(text, limit=165):
    """Delivery-sized thought blocks. Words and order never change.

    The script already shapes some paragraphs with internal line breaks; those
    are delivery units and are kept as written.
    """
    out = []
    for hard in text.split("\n"):
        hard = hard.strip()
        if not hard:
            continue
        ends = []
        for m in re.finditer(r"[.!?]+[”’\"']?(?=\s|$)", hard):
            head_ = hard[:m.start()]
            word = re.split(r"[\s(“\"']", head_)[-1].lower().rstrip(".")
            if word in ABBR or len(word) == 1:
                continue
            rest = hard[m.end():].lstrip()
            if rest and not (rest[0].isupper()
                             or rest[0] in "“\"'‘"):
                continue
            ends.append(m.end())
        parts, prev = [], 0
        for e in ends + ([len(hard)] if not ends or ends[-1] < len(hard)
                         else []):
            chunk = hard[prev:e].strip()
            if chunk:
                parts.append(chunk)
            prev = e
        cur = ""
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
    for i, (label, ps) in enumerate(M.sections(n), 1):
        marker(d, "%d" % i, label)
        for p in ps:
            for u in _units(p):
                spoken(d, u)
    footer_note(d, "Read the blocks, not the page. A break is a breath.")
    d.save(path)
    return path


def block_words(n):
    out = []
    for label, ps in M.sections(n):
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
