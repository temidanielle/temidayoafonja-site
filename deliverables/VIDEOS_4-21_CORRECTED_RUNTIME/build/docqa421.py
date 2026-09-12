# -*- coding: utf-8 -*-
"""Structural QA across every Word document in every package.

Rendering 255 documents and looking at each one is slower and shallower than
measuring them, because the failure modes are structural and measurable:

  table wider than the text column        content runs off the page
  a cell with no text                     a row that renders as a gap
  a run below 7pt or above 30pt           unreadable, or a broken heading
  a paragraph over 1200 characters        a block that was never split
  a document with no body text            a file that generated empty
  a table row with the wrong cell count   a table that renders ragged

Anything flagged here is opened and looked at. A sample covering every
document type is looked at regardless, because a measurement cannot see
that a page is ugly.
"""
import os, sys, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Inches

MIN_PT, MAX_PT = 7.0, 30.0
MAX_PARA_CHARS = 1200


def check(path):
    out = []
    try:
        d = Document(path)
    except Exception as e:
        return ["will not open: %s" % e]

    # The text column is read from the document, not assumed. The supplied
    # recording masters set 0.65in margins where this build's own documents
    # set 0.9in, and measuring them against the wrong page makes every
    # supplied master look broken when it fits perfectly.
    sec = d.sections[0]
    text_width = sec.page_width - sec.left_margin - sec.right_margin

    body = [p.text.strip() for p in d.paragraphs if p.text.strip()]
    cells = [c.text.strip() for t in d.tables for r in t.rows for c in r.cells]
    if not body and not cells:
        out.append("no text at all")

    for i, t in enumerate(d.tables, 1):
        widths = [c.width for c in t.rows[0].cells] if t.rows else []
        if widths and all(w is not None for w in widths):
            total = sum(widths)
            if total > text_width + Inches(0.02):
                out.append("table %d is %.2fin wide, past this document's "
                           "%.2fin text column"
                           % (i, total / 914400.0, text_width / 914400.0))
        counts = {len(r.cells) for r in t.rows}
        if len(counts) > 1:
            out.append("table %d has rows of differing cell counts %s"
                       % (i, sorted(counts)))
        for ri, r in enumerate(t.rows, 1):
            if ri == 1:
                continue
            if all(not c.text.strip() for c in r.cells):
                out.append("table %d row %d is entirely empty" % (i, ri))

    for p in d.paragraphs:
        if len(p.text) > MAX_PARA_CHARS:
            out.append("paragraph of %d characters: %s…"
                       % (len(p.text), p.text[:50]))
        for r in p.runs:
            if r.font.size is None or not r.text.strip():
                continue
            pt = r.font.size.pt
            if pt < MIN_PT or pt > MAX_PT:
                out.append("%.1fpt run: %s…" % (pt, r.text[:40]))
    return out


def doc_type(path):
    """Group documents by what they are, so a sample can cover every kind."""
    base = os.path.basename(path)
    if base.startswith("SUPERSEDED_"):
        return "superseded master"
    for key, name in (
        ("Script_Only", "script-only recording copy"),
        ("Approved_Recording_Master_Reference", "reading reference"),
        ("Recording_Run_of_Show", "run of show"),
        ("Six_Short_Form_Scripts", "shorts, combined"),
        ("Publishing_Materials", "publishing materials"),
        ("Viewer_Exercise", "viewer exercise"),
        ("Editorial_Check", "editorial check"),
        ("Delivery_Summary", "delivery summary"),
        ("Restoration_Report", "restoration report"),
    ):
        if key in base:
            return name
    if os.sep + "Individual" + os.sep in path:
        return "short, individual"
    if "Recording_Master" in base:
        return "recording master"
    return "other"


def all_docs(root):
    return sorted(p for p in
                  glob.glob(os.path.join(root, "**", "*.docx"), recursive=True)
                  if "_source" not in p)


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    docs = all_docs(root)
    kinds = Counter(doc_type(p) for p in docs)
    bad = 0
    for p in docs:
        probs = check(p)
        if probs:
            bad += 1
            print("%s" % os.path.relpath(p, root))
            for x in probs:
                print("    %s" % x)
    print("\n%d documents checked, %d with structural problems"
          % (len(docs), bad))
    print("\ndocument types found:")
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        print("    %-30s %d" % (k, v))
    raise SystemExit(1 if bad else 0)
