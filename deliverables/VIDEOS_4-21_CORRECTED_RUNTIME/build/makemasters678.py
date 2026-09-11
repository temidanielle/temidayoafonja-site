# -*- coding: utf-8 -*-
"""Write the restored V6, V7 and V8 masters as derivatives.

The supplied September 11 masters are not modified. They stay in _source/
with their original checksums. These derivatives are written beside them in
_source_restored/ and become the spoken source of truth for V6, V7 and V8.

Each derivative keeps the corrected master's own metadata table, apparatus
and guardrails, and replaces only the spoken script with the restored
full-depth version. Two metadata rows change because the restored script
changes the fact they record, and each change is stated in the document
itself rather than made quietly.
"""
import os, sys, hashlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import masters421 as M
import restore678 as R
import verifyrestore as V

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "_source_restored")

NAVY = RGBColor(0x11, 0x23, 0x45)
GOLD = RGBColor(0xB4, 0x88, 0x2B)
DIM = RGBColor(0x5A, 0x60, 0x6A)

FILES = {6: "Video_6_RESTORED_Regular_Length_Recording_Master.docx",
         7: "Video_7_RESTORED_Regular_Length_Recording_Master.docx",
         8: "Video_8_RESTORED_Regular_Length_Recording_Master.docx"}

# The rows whose fact the restoration changes. Anything not listed here is
# copied from the corrected master unchanged.
ROW_CHANGES = {
 6: {"Resource route":
     ("Career Decision Evidence Check (spoken once, after the teaching, "
      "then description and pinned comment)",
      "The restored master speaks the resource, as the September 9 approved "
      "master did. The compressed master had routed it to the description "
      "only because the spoken CTA had been cut."),
     "Length plan":
     ("Regular long-form. Restored to the approved September 9 depth: "
      "approximately 8:17 to 9:14 speech-only.",
      "The compressed master stated no runtime target.")},
 7: {"Resource route":
     ("Capability Formation Field Kit (spoken once, after the teaching, "
      "then description and pinned comment)",
      "The restored master speaks the resource, as the September 9 approved "
      "master did. The compressed master had routed it to the description "
      "only because the spoken CTA had been cut."),
     "Length plan":
     ("Regular long-form. Restored to the approved September 9 depth: "
      "approximately 8:28 to 9:27 speech-only.",
      "The compressed master stated no runtime target.")},
 8: {"Resource route":
     ("Keep the Proof (spoken once, after the teaching, then description "
      "and pinned comment)",
      "The restored master speaks the resource, as the September 9 approved "
      "master did. The compressed master had routed it to the description "
      "only because the spoken CTA had been cut."),
     "Length plan":
     ("Regular long-form. Restored to the approved September 9 depth: "
      "approximately 8:53 to 9:54 speech-only.",
      "The compressed master stated no runtime target.")},
}


def _base():
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.left_margin = s.right_margin = Inches(0.9)
    s.top_margin = s.bottom_margin = Inches(0.8)
    n = d.styles["Normal"]
    n.font.name = "Calibri"
    n.font.size = Pt(11)
    return d


def _p(d, text, size=11, bold=False, color=None, before=0, after=8,
       spacing=1.25, align=None, italic=False):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = spacing
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color is not None:
        r.font.color.rgb = color
    return p


def _table(d, rows, widths=(1.9, 4.8)):
    t = d.add_table(rows=0, cols=2)
    t.autofit = False
    pr = t._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement("w:%s" % edge)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:color"), "C8CCD2")
        borders.append(e)
    # w:tblBorders must precede w:tblLayout and w:tblLook in tblPr, or the
    # file is rejected as schema-invalid.
    pr.append(borders)
    for k, v in rows:
        row = t.add_row()
        for i, (cell, txt, bold) in enumerate(
                ((row.cells[0], k, True), (row.cells[1], v, False))):
            cell.width = Inches(widths[i])
            para = cell.paragraphs[0]
            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(3)
            r = para.add_run(txt)
            r.font.size = Pt(9.5)
            r.bold = bold
    return t


def build(n, stamp):
    src = M.read(n)
    changes = ROW_CHANGES[n]
    w, fast, slow = V.estimate(n)
    d = _base()

    _p(d, src["eyebrow"], size=9, bold=True, color=GOLD, after=2)
    _p(d, M.title(n), size=19, bold=True, color=NAVY, after=4, spacing=1.1)
    _p(d, "RESTORED FULL-DEPTH RECORDING MASTER  |  %s" % stamp,
       size=9, bold=True, color=DIM, after=12)

    _p(d, "This document is a derivative. The supplied September 11 master "
          "is unchanged and is retained in _source/ with its original "
          "checksum. That master had been compressed to roughly half the "
          "approved teaching; this one restores it. The spoken script below "
          "is the source of truth for Video %d." % n,
       size=9.5, italic=True, color=DIM, after=14)

    rows = []
    for k, v in src["meta"].items():
        if k in changes:
            rows.append((k, changes[k][0]))
        else:
            rows.append((k, v))
    for k in changes:
        if k not in src["meta"]:
            rows.append((k, changes[k][0]))
    _table(d, rows)

    _p(d, "WHAT CHANGED IN THIS DERIVATIVE", size=9, bold=True, color=GOLD,
       before=18, after=6)
    _p(d, "The spoken script is restored to the approved September 9 depth. "
          "%d spoken words against %d in the previously approved master. "
          "The corrected master's title, thumbnail, hook, framework and "
          "architecture are kept exactly as supplied."
          % (w, R.PREV_WORDS[n]), size=9.5, after=6)
    for k, (_, why) in changes.items():
        _p(d, "%s: %s" % (k, why), size=9.5, after=4)
    _p(d, "No new teaching was authored. Every restored line is approved "
          "speech from the September 9 master. The per-line provenance "
          "record travels with the package.", size=9.5, after=4)

    _p(d, M.SCRIPT_START, size=11, bold=True, color=NAVY, before=22,
       after=12)
    for sec, paras in R.SCRIPTS[n]:
        _p(d, sec, size=10, bold=True, color=GOLD, before=16, after=8)
        for p in paras:
            _p(d, p["text"], size=11.5, spacing=1.34, after=10)

    _p(d, "END OF SPOKEN SCRIPT", size=10, bold=True, color=NAVY, before=20,
       after=10)
    _p(d, "Do not read this line or anything below it.", size=9,
       italic=True, color=DIM, after=14)

    for t in src["tail"]:
        heading = t.isupper() and len(t) < 80
        _p(d, t, size=9.5 if not heading else 9,
           bold=heading, color=GOLD if heading else None,
           before=12 if heading else 0, after=6 if heading else 4)

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, FILES[n])
    d.save(path)
    return path


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 16), b""):
            h.update(c)
    return h.hexdigest()


if __name__ == "__main__":
    import subprocess
    o = subprocess.check_output(["env", "TZ=America/Chicago", "date",
                                 "+%A, %B %d, %Y | %-I:%M %p CT"])
    stamp = o.decode().strip()
    lines = []
    for n in sorted(R.SCRIPTS):
        bad, bridges, adj = V.check(n)
        if bad or bridges:
            raise SystemExit("V%d is not clean; not writing a master" % n)
        p = build(n, stamp)
        h = sha256(p)
        lines.append("%s  %s" % (h, os.path.basename(p)))
        print("V%-3d %-58s %s" % (n, os.path.basename(p), h[:16]))
    with open(os.path.join(OUT, "RESTORED_SOURCE_HASHES.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
