# -*- coding: utf-8 -*-
"""Render the built Word documents so they can be looked at.

LibreOffice cannot load any file in this environment, including a plain text
file, so the usual DOCX to PDF route is unavailable. This renders instead from
the saved .docx XML itself, not from the source data that produced it, so what
gets inspected is what is actually inside the delivered file: every run's size,
weight, colour value, every paragraph's indent and spacing, and every table's
column widths, borders and cell shading.

Pagination is Chromium's, not Word's, so page counts are indicative. What this
check is for is clipping, table overflow, unreadable type and broken layout.

  python3 render_check.py            writes PDF and PNG page images
"""
import os, sys, html, subprocess, glob
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: 8.5in 11in; margin: 0.8in 0.9in; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Calibri, Carlito, "DejaVu Sans", sans-serif;
       font-size: 11pt; line-height: 1.18; color: #000; }
p { margin: 0; }
table { border-collapse: collapse; width: 100%; table-layout: fixed;
        margin-bottom: 6pt; }
td { vertical-align: top; padding: 3pt 4pt; word-wrap: break-word; }
.pb { break-before: page; }
"""


def _blocks(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield Table(child, doc)


def _twips(el, attr):
    v = el.get(qn(attr)) if el is not None else None
    return int(v) if v is not None else None


def _run_html(r):
    txt = html.escape(r.text).replace("\n", "<br>")
    if not txt:
        return ""
    st = []
    if r.font.size is not None:
        st.append("font-size:%.2fpt" % (r.font.size.pt))
    if r.bold:
        st.append("font-weight:700")
    if r.italic:
        st.append("font-style:italic")
    try:
        if r.font.color is not None and r.font.color.rgb is not None:
            st.append("color:#%s" % str(r.font.color.rgb))
    except Exception:
        pass
    return "<span style='%s'>%s</span>" % (";".join(st), txt)


def _para_html(p, in_cell=False):
    pf = p.paragraph_format
    st = []
    if pf.space_before is not None:
        st.append("margin-top:%.1fpt" % pf.space_before.pt)
    if pf.space_after is not None:
        st.append("margin-bottom:%.1fpt" % pf.space_after.pt)
    if pf.line_spacing is not None and not in_cell:
        st.append("line-height:%.2f" % pf.line_spacing)
    if pf.left_indent is not None:
        st.append("padding-left:%.3fin" % pf.left_indent.inches)
    if pf.first_line_indent is not None:
        st.append("text-indent:%.3fin" % pf.first_line_indent.inches)
    if p.alignment is not None and str(p.alignment).startswith("CENTER"):
        st.append("text-align:center")
    # bottom rule paragraphs
    pr = p._p.find(qn("w:pPr"))
    cls = ""
    if pr is not None:
        bdr = pr.find(qn("w:pBdr"))
        if bdr is not None:
            if bdr.find(qn("w:bottom")) is not None:
                st.append("border-bottom:1px solid #8A6D1E")
            if bdr.find(qn("w:left")) is not None:
                st.append("border-left:3px solid #9B2C10;padding-left:8pt")
    body = "".join(_run_html(r) for r in p.runs)
    # Only a break whose type is "page" starts a new page. A plain w:br is a
    # line break inside a thought block, and the masters use those to shape
    # delivery.
    for br in p._p.findall(".//" + qn("w:br")):
        if br.get(qn("w:type")) == "page":
            cls = " class='pb'"
            break
    if not body.strip() and not st:
        return "<p>&nbsp;</p>"
    return "<p%s style='%s'>%s</p>" % (cls, ";".join(st), body or "&nbsp;")


def _table_html(t):
    tblPr = t._tbl.tblPr
    bdr = tblPr.find(qn("w:tblBorders")) if tblPr is not None else None
    border = "1px solid #C9BFA8" if bdr is not None else "none"
    rows = []
    cols = None
    for r in t.rows:
        cells = []
        for c in r.cells:
            tcPr = c._tc.find(qn("w:tcPr"))
            fill = None
            if tcPr is not None:
                shd = tcPr.find(qn("w:shd"))
                if shd is not None:
                    fill = shd.get(qn("w:fill"))
            w = c.width.inches if c.width is not None else None
            style = ["border:%s" % border]
            if fill and fill.lower() not in ("auto",):
                style.append("background:#%s" % fill)
            if w:
                style.append("width:%.3fin" % w)
            inner = "".join(_para_html(p, in_cell=True) for p in c.paragraphs)
            cells.append("<td style='%s'>%s</td>" % (";".join(style), inner))
        if cols is None:
            cols = len(cells)
        rows.append("<tr>%s</tr>" % "".join(cells))
    return "<table>%s</table>" % "".join(rows)


def to_html(path):
    d = Document(path)
    parts = []
    for b in _blocks(d):
        parts.append(_para_html(b) if isinstance(b, Paragraph)
                     else _table_html(b))
    return ("<meta charset='utf-8'><style>%s</style>%s"
            % (CSS, "".join(parts)))


def render(docx_path, outdir):
    name = os.path.splitext(os.path.basename(docx_path))[0]
    os.makedirs(outdir, exist_ok=True)
    hpath = os.path.join(outdir, name + ".html")
    with open(hpath, "w") as f:
        f.write(to_html(docx_path))
    pdf = os.path.join(outdir, name + ".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf,
                    "file://" + hpath], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return pdf


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "_render")
    import fnmatch
    targets = sorted(glob.glob(os.path.join(OUT, "*.docx")))
    for root, _, names in os.walk(OUT):
        for nm in names:
            if nm.endswith(".docx") and "_CORRECTED_RUNTIME_PACKAGE" in root:
                targets.append(os.path.join(root, nm))
    for f in sorted(set(targets)):
        tag = os.path.basename(os.path.dirname(os.path.dirname(f)))
        sub = os.path.join(outdir, tag if "PACKAGE" in tag else "_batch")
        print(render(f, sub))
