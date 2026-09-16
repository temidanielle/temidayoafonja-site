# -*- coding: utf-8 -*-
"""The September 16 recording scripts, thought blocks and editing briefs.

This is the current source for NEW PUBLIC V4 to V11. It supersedes the
script lineage the existing packages were built from, so nothing here is
assumed to match what shipped: every difference is measured.

Nothing in this module writes. The recording script is authoritative for
spoken wording; the thought-block copy is a recording-format derivative
that must carry the same words exactly and in order; the editing brief
carries production direction and never spoken wording.
"""
import os, re, json, hashlib
from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "_source", "files")
INTAKE_SHA = "021529cab2c761046242a83a743adf0c2f2777328179e064d6ec19b302e8ceb0"

VIDEOS = (4, 5, 6, 7, 8, 9, 10, 11)
SCRIPT_START = "SCRIPT STARTS HERE"
NOT_SPOKEN = "[NOT SPOKEN]"
BLOCK_LABEL = re.compile(r"^BLOCK \d+\b", re.I)

_CACHE = {}
_MAN = None


def manifest():
    global _MAN
    if _MAN is None:
        _MAN = json.load(open(os.path.join(SRC, "00_Read_First",
                                           "SOURCE_MANIFEST.json")))
    return _MAN


def script_path(n):
    return os.path.join(SRC, "01_Recording_Scripts",
                        "V%02d_Recording_Script.docx" % n)


def block_path(n):
    return os.path.join(SRC, "02_Thought_Blocks",
                        "V%02d_Thought_Block_Recording_Copy.docx" % n)


def brief_path(n):
    return os.path.join(SRC, "03_Editing_Briefs",
                        "V%02d_Early_Curiosity_Outcome_Editing_Brief.docx" % n)


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


def _norm(t):
    return " ".join(t.replace("’", "'").replace("‘", "'")
                    .replace("“", '"').replace("”", '"')
                    .split()).strip()


def read(n):
    """Sections and spoken paragraphs of the current recording script."""
    if n in _CACHE:
        return _CACHE[n]
    ps = _paras(script_path(n))
    meta = {"title": ps[1],
            "thumbnail": ps[2].split(":", 1)[1].strip(),
            "new": int(re.search(r"V(\d+)", ps[0]).group(1))}
    m = re.search(r"FORMER ROADMAP V(\d+)", ps[0])
    meta["former"] = int(m.group(1)) if m else None
    i0 = next(i for i, t in enumerate(ps) if t.startswith(SCRIPT_START)) + 1
    sections, cur, notes = [], None, []
    for t in ps[i0:]:
        if NOT_SPOKEN in t:
            notes.append(t)
            lab = t.replace(NOT_SPOKEN, "").strip()
            cur = (lab, [])
            sections.append(cur)
            continue
        if cur is None:
            cur = ("OPEN", [])
            sections.append(cur)
        cur[1].append(t)
    _CACHE[n] = dict(meta=meta, sections=sections, notes=notes,
                     sha=sha256(script_path(n)),
                     file=os.path.basename(script_path(n)))
    return _CACHE[n]


def title(n):
    return read(n)["meta"]["title"]


def thumbnail(n):
    return read(n)["meta"]["thumbnail"]


def former(n):
    return read(n)["meta"]["former"]


def sections(n):
    return read(n)["sections"]


def paragraphs(n):
    return [p for _, ps in sections(n) for p in ps]


def spoken_text(n):
    return "\n".join(paragraphs(n))


def word_count(n):
    return len(spoken_text(n).split())


DIRECTION = "Read one block silently"


def block_paragraphs(n):
    """The spoken stream of the thought-block copy.

    The copy carries no SCRIPT STARTS HERE marker, so everything above the
    recording direction is front matter and is skipped by finding that line
    and starting after it. Block and section labels carry [NOT SPOKEN].
    """
    ps = _paras(block_path(n))
    for i, t in enumerate(ps):
        if t.startswith(DIRECTION):
            ps = ps[i + 1:]
            break
    else:
        raise SystemExit("V%d: no recording direction line" % n)
    return [t for t in ps
            if NOT_SPOKEN not in t and not BLOCK_LABEL.match(t.strip())]


def blocks_match(n):
    a = [_norm(x) for x in paragraphs(n)]
    b = [_norm(x) for x in block_paragraphs(n)]
    if a == b:
        return True, "%d paragraphs, identical and in order" % len(a)
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return False, ("paragraph %d differs:\n  script: %s\n  block : %s"
                           % (i, x[:90], y[:90]))
    return False, "length differs: script %d, block %d" % (len(a), len(b))


def brief(n):
    """The editing brief, as ordered paragraphs and tables."""
    d = Document(brief_path(n))
    out = []
    for c in d.element.body.iterchildren():
        if c.tag == qn("w:p"):
            t = Paragraph(c, d).text.rstrip()
            if t.strip():
                out.append(("p", t))
        elif c.tag == qn("w:tbl"):
            t = Table(c, d)
            rows = [[x.text.strip() for x in r.cells] for r in t.rows]
            out.append(("tbl", rows))
    return out


if __name__ == "__main__":
    man = manifest()
    print("intake.zip %s" % ("verified" if sha256(
        os.path.join(OUT, "_source", "intake.zip")) == INTAKE_SHA
        else "MISMATCH"))
    bad = 0
    for n in VIDEOS:
        v = man["videos"][str(n)]
        for o in v["outputs"]:
            p = os.path.join(SRC, o["file"])
            if sha256(p) != o["sha256"]:
                print("  MISMATCH %s" % o["file"])
                bad += 1
    print("  24 documents against the manifest: %s"
          % ("all verified" if not bad else "%d MISMATCH" % bad))
    for n in VIDEOS:
        v = man["videos"][str(n)]
        ok, det = blocks_match(n)
        w = word_count(n)
        print("\nV%-2d  %s" % (n, title(n)))
        print("    thumbnail : %s" % thumbnail(n))
        print("    former    : %s" % (("V%d" % former(n)) if former(n)
                                      else "none"))
        print("    sections  : %d   paragraphs: %d" % (len(sections(n)),
                                                       len(paragraphs(n))))
        print("    words     : %d   manifest %d   %s"
              % (w, v["spoken_words"],
                 "match" if w == v["spoken_words"] else "DIFFERS"))
        print("    blocks    : %s" % det)
