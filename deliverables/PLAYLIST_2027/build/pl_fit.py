# -*- coding: utf-8 -*-
"""Estimate the printed height of a .docx so the one-page sheets can be proved
to be one page. LibreOffice will not open python-docx output in this container,
so the height is computed from the document's own paragraph and table metrics
rather than guessed.
"""
import os
from docx import Document
from docx.shared import Pt
from PIL import ImageFont

FONTS = {(False, False): "/root/.fonts/DMSans-Regular.ttf",
         (True, False): "/root/.fonts/DMSans-Bold.ttf",
         (False, True): "/root/.fonts/DMSans-Regular.ttf",
         (True, True): "/root/.fonts/DMSans-Bold.ttf"}
_cache = {}

def _font(bold, italic, pt):
    key = (bold, italic, round(pt))
    if key not in _cache:
        # 1 pt of type is 1 pt; PIL wants pixels, so render at 4x and divide.
        _cache[key] = ImageFont.truetype(FONTS[(bool(bold), bool(italic))],
                                         max(1, int(round(pt * 4))))
    return _cache[key]

def _width(text, bold, italic, pt):
    if not text:
        return 0.0
    f = _font(bold, italic, pt)
    return f.getlength(text) / 4.0

def para_height(p, avail_pt, default_pt=10.5):
    pf = p.paragraph_format
    before = pf.space_before.pt if pf.space_before is not None else 0
    after = pf.space_after.pt if pf.space_after is not None else 6
    ls = pf.line_spacing if isinstance(pf.line_spacing, float) else 1.18
    ind = (pf.left_indent.pt if pf.left_indent is not None else 0)
    w = avail_pt - ind
    runs = p.runs
    if not runs:
        return before + after + default_pt * ls
    size = max((r.font.size.pt if r.font.size else default_pt) for r in runs)
    total = sum(_width(r.text, r.bold, r.italic,
                       r.font.size.pt if r.font.size else default_pt)
                for r in runs)
    lines = max(1, int(total / max(1.0, w)) + (1 if total % max(1.0, w) else 0))
    return before + after + lines * size * ls

def height_pt(path, page_w_in=8.5, margin_in=0.85):
    d = Document(path)
    sec = d.sections[0]
    margin = sec.left_margin.inches
    avail = (page_w_in - 2 * margin) * 72.0
    total = 0.0
    body = d.element.body
    tbl_i = 0
    tables = d.tables
    for child in body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "p":
            from docx.text.paragraph import Paragraph
            total += para_height(Paragraph(child, d), avail)
        elif tag == "tbl":
            t = tables[tbl_i]; tbl_i += 1
            ncol = len(t.columns)
            for row in t.rows:
                rh = 0.0
                for c in row.cells:
                    cw = c.width.pt if c.width else avail / ncol
                    ch = 0.0
                    for p in c.paragraphs:
                        ch += para_height(p, max(24.0, cw - 10), 9)
                    rh = max(rh, ch)
                total += rh + 4
    return total, (11.0 - 2 * margin) * 72.0

def pages(path):
    h, per = height_pt(path)
    return h, per, max(1, int(h / per) + (1 if h % per else 0))
