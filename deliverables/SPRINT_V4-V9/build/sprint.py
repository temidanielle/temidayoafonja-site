# -*- coding: utf-8 -*-
"""The six FINAL sprint scripts and their supplied Thought-Block copies.

Nothing here writes. The FINAL sprint script is authoritative for spoken
wording; the Thought-Block copy is a recording-format derivative that must
carry the same words exactly and in order. Where they disagree the script
wins, and QA reports rather than repairs.

A script document also carries three candidate Shorts after the long-form
script. They are not spoken material and never enter the spoken stream.
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source")
SCRIPTS = os.path.join(SRC, "sprint_scripts")
BLOCKS = os.path.join(SRC, "thought_blocks")

# new public number -> former roadmap number
NUMBERS = {4: 26, 5: 33, 6: 22, 7: 24, 8: 28, 9: 27}
VIDEOS = tuple(sorted(NUMBERS))

PAIRS = (("What work is doing to you", (4, 5)),
         ("Read the system", (6, 7)),
         ("Protect what travels", (8, 9)))

SCRIPT_START = "FINAL LONG-FORM SCRIPT"
SHORTS_START = "THREE SHORTS"
NOT_SPOKEN = "[NOT SPOKEN]"
BLOCK_LABEL = re.compile(r"^BLOCK \d+\b")
SHORT_HEAD = re.compile(r"^SHORT (\d+)\s*\|\s*(.+)$")
ASK = "Primary ask:"

ZIP_SHA = {
 "sprint_scripts.zip":
   "72ffcb09ae7b1dac351be089bf5ec5e0650305271d6701053b5cbcddf917609a",
 "thought_blocks.zip":
   "55e7ad9f4cb79ddcdb3643b62fe45b56533f257fe5bfc1e04dc4583053a41360",
}


def script_path(n):
    return os.path.join(SCRIPTS, "NEW_V%d_FORMER_V%d_Final_Sprint_Script_"
                                 "and_3_Shorts.docx" % (n, NUMBERS[n]))


def block_path(n):
    return os.path.join(BLOCKS, "NEW_V%d_FORMER_V%d_Thought_Block_Recording_"
                                "Copy.docx" % (n, NUMBERS[n]))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _paras(path):
    d = Document(path)
    out = []
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:p"):
            t = Paragraph(c, d).text.rstrip()
            if t.strip():
                out.append(t)
    return out


def _is_label(t):
    """An all-capitals production heading, never a spoken line."""
    s = t.strip()
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return False
    return (s == s.upper() and len(s) < 60
            and not s.endswith((".", "?", "!")))


_CACHE = {}


def read(n):
    if n in _CACHE:
        return _CACHE[n]
    ps = _paras(script_path(n))
    meta = {"title": ps[3]}
    for t in ps[:8]:
        if t.startswith("THUMBNAIL:"):
            meta["thumbnail"] = t.split(":", 1)[1].strip()
        elif t.startswith("Watch Next:"):
            meta["watch_next"] = t.split(":", 1)[1].strip()
        elif t.startswith("NEW PUBLIC VIDEO NUMBER:"):
            meta["new"] = int(t.split("V")[-1])
        elif t.startswith("FORMER ROADMAP NUMBER:"):
            meta["former"] = int(t.split("V")[-1])
        elif t.startswith("Source note:"):
            meta["source_note"] = t.split(":", 1)[1].strip()
    i0 = ps.index(SCRIPT_START) + 1
    i1 = ps.index(SHORTS_START)
    sections, cur, notes = [], None, []
    for t in ps[i0:i1]:
        if t.startswith("[") and t.endswith("]"):
            notes.append(t)
            continue
        if _is_label(t):
            cur = (t.strip(), [])
            sections.append(cur)
        elif cur is not None:
            cur[1].append(t)
    shorts = []
    for t in ps[i1 + 1:]:
        m = SHORT_HEAD.match(t)
        if m:
            shorts.append(dict(num=int(m.group(1)), hook=m.group(2).strip(),
                               body=None, ask=None))
        elif shorts and t.startswith(ASK):
            shorts[-1]["ask"] = t.split(":", 1)[1].strip()
        elif shorts and shorts[-1]["body"] is None:
            shorts[-1]["body"] = t
    _CACHE[n] = dict(meta=meta, sections=sections, notes=notes,
                     shorts=shorts, sha=sha256(script_path(n)),
                     file=os.path.basename(script_path(n)))
    return _CACHE[n]


def title(n):
    return read(n)["meta"]["title"]


def thumbnail(n):
    return read(n)["meta"]["thumbnail"]


def watch_next(n):
    return read(n)["meta"]["watch_next"]


def former(n):
    return read(n)["meta"]["former"]


def sections(n):
    return read(n)["sections"]


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return sum(len(p.split()) for p in paragraphs(n))


def shorts(n):
    return read(n)["shorts"]


def estimate(n, low=130, high=145):
    w = word_count(n)

    def mmss(wpm):
        s = int(round(w / float(wpm) * 60))
        return "%d:%02d" % (s // 60, s % 60)
    return mmss(high), mmss(low)


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def trigger_ok(n, t):
    q = _norm(t)
    return sum(1 for p in paragraphs(n) if _norm(p) == q) == 1


def contains(n, phrase):
    return _norm(phrase) in _norm(spoken_text(n))


# ------------------------------------------------------- thought blocks
def block_words(n):
    """The spoken word stream of the supplied Thought-Block copy.

    Anything marked [NOT SPOKEN], and the document's own header, is excluded.
    """
    out, started = [], False
    for t in _paras(block_path(n)):
        if NOT_SPOKEN in t:
            started = True
            continue
        if not started:
            continue
        out.extend(t.split())
    return out


def blocks_match(n):
    """Does the supplied copy carry the script's spoken words exactly?"""
    a = block_words(n)
    b = spoken_text(n).split()
    if a == b:
        return True, "%d words, identical and in order" % len(a)
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return False, ("diverges at word %d: block %r against script %r"
                           % (i, " ".join(a[max(0, i - 6):i + 6]),
                              " ".join(b[max(0, i - 6):i + 6])))
    return False, ("length differs: block %d words, script %d words; first "
                   "extra: %r" % (len(a), len(b),
                                  " ".join((a if len(a) > len(b) else b)
                                           [min(len(a), len(b)):][:12])))


def shorts_in_spoken(n):
    """Has any Short material been treated as part of the spoken script?

    A Short quoting a sentence from its own video is normal and is not a
    leak. What would be a leak is Short apparatus reaching the spoken
    stream: a SHORT heading, a "Primary ask" line, or a Short's closing
    call to watch the full video, none of which the presenter says in the
    long-form recording.
    """
    bad = []
    for p in paragraphs(n):
        t = p.strip()
        if SHORT_HEAD.match(t) or t.startswith(ASK):
            bad.append(t[:60])
        if _norm(t) in ("watch the full video.", "watch the related full "
                        "video."):
            bad.append(t[:60])
    return bad


def spoken_ends_before_shorts(n):
    """The spoken stream must stop at the THREE SHORTS marker."""
    ps = _paras(script_path(n))
    cut = ps.index(SHORTS_START)
    after = {_norm(x) for x in ps[cut:]}
    return not [p for p in paragraphs(n) if _norm(p) in after]


def manifest():
    rows = []
    for n in VIDEOS:
        rows.append((n, NUMBERS[n], os.path.basename(script_path(n)),
                     sha256(script_path(n)),
                     os.path.basename(block_path(n)),
                     sha256(block_path(n))))
    return rows


if __name__ == "__main__":
    for n in VIDEOS:
        r = read(n)
        ok, det = blocks_match(n)
        print("NEW V%d  (former V%d)  %s" % (n, NUMBERS[n], title(n)))
        print("    thumbnail   %s" % thumbnail(n))
        print("    watch next  %s" % watch_next(n))
        print("    sections    %d   paragraphs %d   words %d"
              % (len(sections(n)), len(paragraphs(n)), word_count(n)))
        print("    estimate    %s to %s" % estimate(n))
        print("    shorts      %d  %s"
              % (len(shorts(n)),
                 "all complete" if all(s["body"] and s["ask"]
                                       for s in shorts(n)) else "INCOMPLETE"))
        print("    block match %s  %s" % (ok, det))
        print("    shorts leaked into the spoken script:",
              shorts_in_spoken(n) or "none")
        print("    number map in the document: new V%d, former V%d"
              % (r["meta"]["new"], r["meta"]["former"]))
