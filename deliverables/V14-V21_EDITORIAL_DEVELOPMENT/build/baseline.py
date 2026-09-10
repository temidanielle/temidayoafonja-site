# -*- coding: utf-8 -*-
"""Read the two sources for the V14 to V21 refinement.

Both files are read only. Nothing in this batch writes to either of them.

  ROADMAP    the September 9 locked roadmap already filed in this workspace.
             Its SHA-256 is checked against the sibling .sha256 before use.
  REFINEMENT the uploaded September 9 TubeBuddy-informed refinement document.
             There is no lock file for it, so its hash is recorded, not matched.

Every roadmap slot line printed in the deliverables is taken from here, so a
title, thumbnail line or status label cannot drift from the locked source.
"""
import os, re, hashlib
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

DELIV = "/home/user/temidayoafonja-site/deliverables/"
ROADMAP = DELIV + "roadmap/YouTube_Roadmap_1-30_LOCKED_Sep09_2026.docx"
REFINEMENT = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
              "719cf7b4-YouTube_V14V21_Proposed_Refinement_Sep09_2026.docx")
REFINEMENT_NAME = "YouTube_V14-V21_Proposed_Refinement_Sep09_2026.docx"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_roadmap():
    """Match the locked roadmap against its own recorded checksum."""
    got = sha256(ROADMAP)
    want = open(ROADMAP + ".sha256").read().split()[0]
    if got != want:
        raise SystemExit("roadmap checksum moved: %s != %s" % (got, want))
    return got


def _blocks(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield Table(child, doc)


def _rows(path):
    """Every table row in the file, as a list of cell strings."""
    out = []
    for b in _blocks(Document(path)):
        if isinstance(b, Table):
            for r in b.rows:
                out.append([c.text.strip() for c in r.cells])
    return out


def _paras(path):
    return [b.text.strip() for b in _blocks(Document(path))
            if isinstance(b, Paragraph) and b.text.strip()]


def roadmap_slots():
    """{number: (title, thumbnail, status)} for every numbered roadmap slot."""
    slots = {}
    for r in _rows(ROADMAP):
        if len(r) == 4 and re.fullmatch(r"V\d+", r[0]):
            slots[int(r[0][1:])] = (r[1], r[2], r[3])
    return slots


def roadmap_routes():
    """The two carried resource-route sentences, verbatim from the roadmap."""
    return [p for p in _paras(ROADMAP)
            if p.startswith("V1: Career Evidence Starter")
            or p.startswith("V8 and V10: Keep the Proof")]


def refinement_slots():
    """{number: (working title, treatment)} from the refinement proposal table."""
    slots = {}
    for r in _rows(REFINEMENT):
        if len(r) == 3 and re.fullmatch(r"V\d+", r[0]):
            slots[int(r[0][1:])] = (r[1], r[2])
    return slots


def refinement_themes():
    """[(theme, proposed handling)] from the five-theme table."""
    out = []
    for r in _rows(REFINEMENT):
        if len(r) == 2 and r[0] not in ("Theme",) and r[0]:
            out.append((r[0], r[1]))
    return out


def refinement_says(fragment):
    """True when the refinement document contains this sentence."""
    norm = lambda s: (s.replace("’", "'").replace("“", '"')
                       .replace("”", '"').replace("–", "-"))
    body = norm(" ".join(_paras(REFINEMENT) +
                         [" ".join(r) for r in _rows(REFINEMENT)]))
    return norm(fragment) in body


if __name__ == "__main__":
    print("roadmap  ", verify_roadmap())
    print("refinement", sha256(REFINEMENT))
    for n in sorted(roadmap_slots()):
        t, th, st = roadmap_slots()[n]
        print("V%-2d | %-62s | %-30s | %s" % (n, t[:62], th[:30], st))
    print()
    for n in sorted(refinement_slots()):
        print("V%-2d | %s | %s" % ((n,) + refinement_slots()[n]))
    print()
    for t, hnd in refinement_themes():
        print("* %s :: %s" % (t, hnd[:70]))
