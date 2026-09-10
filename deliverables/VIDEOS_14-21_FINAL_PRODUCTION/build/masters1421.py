# -*- coding: utf-8 -*-
"""Read the eight locked FINAL Recording Masters.

These files are the definitive spoken source of truth. This module reads them
and never writes to them. Every checksum is matched against the manifest taken
at extraction before any content is used, so a master cannot drift underneath
the build.

Structure of each master:

    CAPABILITY FORMATION | VIDEO n
    <title>
    FINAL ... RECORDING MASTER
    [meta table: key | value]
    RECORDING SCRIPT STARTS HERE
    <section heading>
    <thought block>
    ...
    EDITOR / VISUAL PRIORITIES        (V15 to V21)
    MAJOR VISUAL AND MOTION-GRAPHIC MAP   (V14)

A section heading is all upper case before any " | " separator and short. A
thought block is anything else inside the script. Nothing is reflowed: blocks
are handed on with their internal line breaks intact.
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "_source")

VIDEOS = (14, 15, 16, 17, 18, 19, 20, 21)

FILES = {
 14: "Video_14_Which_Parts_of_Your_Experience_Actually_Transfer_FINAL_Recording_Master.docx",
 15: "Video_15_FINAL_Rebuilt_Recording_Master.docx",
 16: "Video_16_FINAL_Rebuilt_Recording_Master.docx",
 17: "Video_17_FINAL_Rebuilt_Recording_Master.docx",
 18: "Video_18_FINAL_Rebuilt_Recording_Master.docx",
 19: "Video_19_FINAL_Rebuilt_Recording_Master.docx",
 20: "Video_20_FINAL_Rebuilt_Recording_Master.docx",
 21: "Video_21_FINAL_Rebuilt_Recording_Master.docx",
}

RESEARCH = "what-really-transfers-research.md"

# Everything after one of these ends the spoken script.
SCRIPT_END = ("EDITOR / VISUAL PRIORITIES",
              "MAJOR VISUAL AND MOTION-GRAPHIC MAP",
              "RESEARCH INTEGRITY NOTES",
              "FINAL QA")

SCRIPT_START = "RECORDING SCRIPT STARTS HERE"

_cache = {}


def path(n):
    return os.path.join(SRC, FILES[n])


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


def manifest():
    """The checksums recorded when the sources were extracted."""
    out = {}
    for line in open(os.path.join(SRC, "SOURCE_HASHES.txt")):
        h, name = line.split()
        out[name] = h
    return out


def verify(n):
    """Match a master against the extraction manifest. Raises if it moved."""
    got, want = sha256(path(n)), manifest()[FILES[n]]
    if got != want:
        raise SystemExit("V%d master changed on disk: %s != %s"
                         % (n, got, want))
    return got


def verify_all():
    return {n: verify(n) for n in VIDEOS}


def research_hash():
    return sha256(os.path.join(SRC, RESEARCH))


def research_text():
    return open(os.path.join(SRC, RESEARCH), encoding="utf-8").read()


def _blocks(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield "p", Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield "t", Table(child, doc)


def _is_heading(text):
    """True when a script paragraph is a working section label, not speech."""
    if len(text) > 100 or "\n" in text:
        return False
    head = text.split(" | ", 1)[0]
    return head == head.upper() and any(c.isalnum() for c in head)


def read(n):
    if n in _cache:
        return _cache[n]
    verify(n)
    doc = Document(path(n))
    paras, meta, tables = [], {}, []
    for kind, b in _blocks(doc):
        if kind == "p":
            t = b.text.strip()
            if t:
                paras.append((b.style.name, t))
        else:
            rows = [[c.text.strip() for c in r.cells] for r in b.rows]
            tables.append(rows)
            if not meta:
                for r in rows:
                    if len(r) == 2:
                        meta[r[0]] = r[1]

    flat = [t for _, t in paras]
    start = flat.index(SCRIPT_START) + 1
    end = len(flat)
    for i in range(start, len(flat)):
        if any(flat[i].startswith(m) for m in SCRIPT_END):
            end = i
            break

    sections, cur = [], None
    for t in flat[start:end]:
        if _is_heading(t):
            cur = (t, [])
            sections.append(cur)
        else:
            if cur is None:
                cur = ("", [])
                sections.append(cur)
            cur[1].append(t)

    tail = flat[end:]
    out = dict(
        num=n, file=FILES[n], sha=sha256(path(n)),
        eyebrow=flat[0], title=flat[1], kind=flat[2],
        meta=meta, tables=tables, sections=sections,
        tail=tail,
        tail_styles=[s for s, t in paras if t in tail],
    )
    _cache[n] = out
    return out


# ---- accessors used by the rest of the build ---------------------------

def title(n):
    m = read(n)
    return m["meta"].get("Recommended title") or m["meta"].get("Title") \
        or m["title"]


def thumbnail(n):
    return read(n)["meta"]["Thumbnail"]


def framework(n):
    return read(n)["meta"].get("Framework", "")


def cta(n):
    m = read(n)["meta"]
    return m.get("Primary CTA", "")


def resource(n):
    """The resource named by the master. V14 names none, and none is added."""
    return read(n)["meta"].get("Resource", "")


def watch_next(n):
    return read(n)["meta"]["Watch Next"]


def blocks(n):
    """Every spoken thought block, in order, headings excluded."""
    return [b for _, bs in read(n)["sections"] for b in bs]


def sections(n):
    return read(n)["sections"]


def spoken_text(n):
    return "\n\n".join(blocks(n))


def word_count(n):
    return sum(len(b.split()) for b in blocks(n))


def estimate(n, fast=145.0, slow=130.0):
    w = word_count(n)
    def mmss(m):
        return "%d:%02d" % (int(m), round((m - int(m)) * 60))
    return w, mmss(w / fast), mmss(w / slow)


def final_line(n):
    return blocks(n)[-1]


def opening_line(n):
    return blocks(n)[0]


def _norm(s):
    return (s.replace("’", "'").replace("“", '"')
             .replace("”", '"').replace("–", "-")
             .replace("—", "-").replace("\n", " "))


def contains(n, sentence):
    """True when the spoken script contains this sentence, quote-normalized."""
    return _norm(sentence) in _norm(spoken_text(n))


def trigger_ok(n, sentence):
    """A sentence trigger must be a real, single spoken sentence.

    It has to appear in the script and sit inside one thought block, so a cue
    can never be built from text that spans two takes.
    """
    s = _norm(sentence)
    return any(s in _norm(b) for b in blocks(n))


if __name__ == "__main__":
    verify_all()
    print("%-4s %-58s %-30s %5s %s" % ("#", "TITLE", "THUMBNAIL", "WORDS",
                                       "ESTIMATE"))
    for n in VIDEOS:
        w, f, s = estimate(n)
        print("V%-3d %-58s %-30s %5d %s to %s"
              % (n, title(n)[:58], thumbnail(n)[:30], w, f, s))
    print()
    for n in VIDEOS:
        m = read(n)
        print("V%d  %d sections, %d blocks, resource=%r, watch next=%r"
              % (n, len(m["sections"]), len(blocks(n)),
                 resource(n), watch_next(n)))
