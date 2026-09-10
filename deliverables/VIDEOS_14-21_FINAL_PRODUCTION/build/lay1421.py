# -*- coding: utf-8 -*-
"""Batch-local layouts for Videos 14 to 21.

Built on the shared primitives rather than by editing layouts.py, so every
earlier batch keeps rendering byte-identically. Shapes the earlier batches
already have are imported unchanged; only the shapes these eight masters
actually need are added here.

Everything is designed to be read at phone size first: one dominant idea per
state, very large type, short phrases, and no essential text in a footer.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from layouts import compose, S, TH, BAND_TOP, BAND_BOT, _head, _columns
from rdeck import (W, H, MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM,
                   NAVY_DIM, DISPLAY, BODY, bg, rect, block, eyebrow)

# reused unchanged
statement = L.statement
duo = L.duo
quad = L.quad
numbered = L.numbered
readings = L.readings
struck = L.struck
cta = L.cta
watch_next = L.watch_next


def trio(c, eye, headline, cells, foot=None, dark=False,
         label_size=50, sub_size=40):
    """Three columns of label and one short line. Used for three-way sorts."""
    back, ink, dim, accent = _head(c, dark, eye)
    gap = 60
    col_w = (CW - gap * 2) // 3
    rows = [("text", headline, CW, S(56, color=ink, bold=True, spacing=1.12),
             0)] if headline else []
    y = compose(c, MARGIN, rows, band=(BAND_TOP, BAND_TOP + 170)) if rows \
        else BAND_TOP
    y += 44 if rows else 0
    h = _columns(c, MARGIN, y, col_w, gap, cells, ink, dim, accent,
                 label_size=label_size, sub_size=sub_size)
    if foot:
        block(c, MARGIN, y + h + 54, CW,
              [(foot, S(38, BODY, dim, spacing=1.34))])


def shared_then_split(c, eye, heads, shared, splits, dark=True):
    """Three headings, one shared line beneath all three, then what differs.

    This is the V14 opening argument in one frame: the same words sit over
    three columns, and the consequence underneath them is not the same.
    Built as one card so the reveal order can do the teaching.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    gap = 54
    col_w = (CW - gap * 2) // 3
    y = BAND_TOP + 6
    for i, htext in enumerate(heads):
        cx = MARGIN + i * (col_w + gap)
        rect(c, cx, y, col_w, 4, fill=accent)
        block(c, cx, y + 30, col_w,
              [(htext, S(40, color=ink, bold=True, spacing=1.14,
                         tracking=1.5))])
    hh = max(TH(t, col_w, DISPLAY, 40, True, 1.14, 1.5) for t in heads)
    y += 30 + hh + 46

    rect(c, MARGIN, y, CW, 4, fill=accent)
    block(c, MARGIN, y + 26, CW,
          [(shared, S(92, color=ink, bold=True, spacing=1.06))])
    y += 26 + TH(shared, CW, DISPLAY, 92, True, 1.06) + 54

    for i, s in enumerate(splits):
        cx = MARGIN + i * (col_w + gap)
        block(c, cx, y, col_w, [(s, S(44, BODY, dim, spacing=1.32))])


def statfacts(c, eye, number, unit, rows_, foot, dark=False):
    """One large count, its breakdown, and the collection date.

    Deliberately not a research table. The number carries the frame and the
    breakdown sits under it in three short lines.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    # Every element here is a fact that has to stay readable, so the frame is
    # tightened rather than having any of it cut. Measured against the DOM.
    y = BAND_TOP - 6
    block(c, MARGIN, y, CW, [(number, S(210, color=accent, bold=True,
                                        spacing=1.0))])
    y += TH(number, CW, DISPLAY, 210, True, 1.0) + 4
    block(c, MARGIN, y, CW, [(unit, S(52, color=ink, bold=True, spacing=1.12,
                                      tracking=1.5))])
    y += TH(unit, CW, DISPLAY, 52, True, 1.12, 1.5) + 38
    rect(c, MARGIN, y, CW, 4, fill=accent)
    y += 28
    for label, val in rows_:
        block(c, MARGIN, y, CW - 340,
              [(label, S(44, BODY, dim, spacing=1.2))])
        block(c, MARGIN + CW - 320, y, 320,
              [(val, S(44, color=ink, bold=True, spacing=1.2, align="r"))])
        y += 58
    block(c, MARGIN, y + 14, CW, [(foot, S(36, BODY, dim, spacing=1.3))])


def two_questions(c, eye, q1, q2, foot=None, dark=True):
    """Two questions at equal weight. Neither is a subtitle of the other."""
    back, ink, dim, accent = _head(c, dark, eye)
    rows = [
      ("rule", 120, 5, accent),
      ("text", q1, CW, S(80, color=ink, bold=True, spacing=1.1), 0),
      ("rule", 120, 5, accent),
      ("text", q2, CW, S(80, color=ink, bold=True, spacing=1.1), 0),
    ]
    gaps = [40, 60, 40]
    if foot:
        rows.append(("text", foot, CW, S(38, BODY, dim, spacing=1.3), 0))
        gaps.append(56)
    compose(c, MARGIN, rows, gaps=gaps)


def word_vs_work(c, eye, word, left_label, left_line, right_label, right_line,
                 dark=False):
    """One word held above two different jobs underneath it.

    The V14 same-word-different-decision comparison, one example at a time.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    y = BAND_TOP + 20
    block(c, MARGIN, y, CW, [(word, S(104, color=accent, bold=True,
                                      spacing=1.06))])
    y += TH(word, CW, DISPLAY, 104, True, 1.06) + 50
    gap = 70
    col_w = (CW - gap) // 2
    for i, (lab, line) in enumerate(((left_label, left_line),
                                     (right_label, right_line))):
        cx = MARGIN + i * (col_w + gap)
        rect(c, cx, y, col_w, 4, fill=accent)
        block(c, cx, y + 30, col_w,
              [(lab, S(46, color=ink, bold=True, spacing=1.12))])
        lh = TH(lab, col_w, DISPLAY, 46, True, 1.12)
        block(c, cx, y + 30 + lh + 22, col_w,
              [(line, S(40, BODY, dim, spacing=1.34))])


def ladder(c, eye, headline, steps, foot=None, dark=False, size=52):
    """An ordered stack where the order is the teaching.

    Each step carries its number in the accent colour and one short line.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    rows = []
    gaps = []
    if headline:
        rows.append(("text", headline, CW, S(54, color=ink, bold=True,
                                             spacing=1.12), 0))
        gaps.append(40)
    y = compose(c, MARGIN, rows, band=(BAND_TOP, BAND_TOP + 150), gaps=gaps) \
        if rows else BAND_TOP + 10
    num_w = 96
    for i, (label, line) in enumerate(steps, 1):
        block(c, MARGIN, y, num_w,
              [("%d" % i, S(size, color=accent, bold=True, spacing=1.1))])
        block(c, MARGIN + num_w, y, CW - num_w,
              [(label, S(size, color=ink, bold=True, spacing=1.14))])
        h = TH(label, CW - num_w, DISPLAY, size, True, 1.14)
        if line:
            block(c, MARGIN + num_w, y + h + 8, CW - num_w,
                  [(line, S(36, BODY, dim, spacing=1.3))])
            h += 8 + TH(line, CW - num_w, BODY, 36, False, 1.3)
        y += h + 30
    if foot:
        block(c, MARGIN, y + 20, CW, [(foot, S(36, BODY, dim, spacing=1.3))])


def four_bucket(c, eye, headline, cells, dark=False):
    """Four labelled buckets in two rows. The V14 audit."""
    back, ink, dim, accent = _head(c, dark, eye)
    gap_x, gap_y = 70, 48
    col_w = (CW - gap_x) // 2
    y = BAND_TOP + 4
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(50, color=ink, bold=True,
                                              spacing=1.12))])
        y += TH(headline, CW, DISPLAY, 50, True, 1.12) + 40
    row_h = 0
    for i, (label, line) in enumerate(cells):
        cx = MARGIN + (i % 2) * (col_w + gap_x)
        cy = y + (i // 2) * (row_h + gap_y)
        rect(c, cx, cy, col_w, 4, fill=accent)
        block(c, cx, cy + 28, col_w,
              [(label, S(50, color=ink, bold=True, spacing=1.1, tracking=1.2))])
        lh = TH(label, col_w, DISPLAY, 50, True, 1.1, 1.2)
        block(c, cx, cy + 28 + lh + 20, col_w,
              [(line, S(38, BODY, dim, spacing=1.32))])
        sh = TH(line, col_w, BODY, 38, False, 1.32)
        row_h = max(row_h, 28 + lh + 20 + sh)


def cta_action(c, eye, headline, support, action=None):
    """A CTA card for a video whose master names no resource.

    Video 14 names no resource route, so nothing is added. The card carries
    the action instead of a URL, and the gold row that normally holds a link
    holds the instruction.
    """
    from rdeck import logomark
    bg(c, NAVY)
    logomark(c, MARGIN, 156)
    rows = [
        ("text", eye.upper(), CW, S(30, color=GOLD, bold=True, tracking=5.0,
                                    spacing=1.0), 0),
        ("text", headline, CW, S(84, color=CREAM, bold=True, spacing=1.12), 0),
        ("text", support, CW, S(44, BODY, CREAM_DIM, spacing=1.34), 0),
    ]
    gaps = [36, 42]
    if action:
        rows += [("rule", 120, 4, GOLD),
                 ("text", action, CW, S(46, color=GOLD, bold=True,
                                        spacing=1.2), 0)]
        gaps += [54, 44]
    compose(c, MARGIN, rows, band=(300, 856), gaps=gaps)


# ---------------------------------------------------------------------------
# Local variants of four shared layouts.
#
# The shared versions require a headline and centre the whole card around it.
# Several frames in this batch put the section context in the eyebrow instead,
# so the headline row has to be omitted rather than left empty: an empty string
# still measures as one line and would push the card off centre. These are
# faithful copies of the shared geometry with the headline row made optional,
# written here so layouts.py stays untouched and every earlier batch keeps
# rendering byte-identically.
# ---------------------------------------------------------------------------

def duo(c, eye, headline, left, right, foot=None, dark=False, mobile=False):
    back, ink, dim, accent = _head(c, dark, eye)
    col_w, gap = 760, 80
    band_h = BAND_BOT - BAND_TOP
    gap_head, gap_foot = 64, 58
    ladder = ((78, 58, 50), (74, 54, 48), (70, 52, 46), (66, 50, 44)) \
        if mobile else ((72, 52, 42), (68, 48, 40), (64, 46, 38),
                        (60, 44, 36), (56, 42, 34))
    for head_s, lab_s, sub_s in ladder:
        hh = TH(headline, CW, DISPLAY, head_s, True, 1.12) if headline else 0
        cell_h = 0
        for label, sub in (left, right):
            lh = TH(label, col_w, DISPLAY, lab_s, True, 1.14)
            sh = TH(sub, col_w, BODY, sub_s, False, 1.34)
            cell_h = max(cell_h, 34 + lh + 20 + sh)
        fh = TH(foot, CW, DISPLAY, 42, True, 1.2) if foot else 0
        total = hh + (gap_head if headline else 0) + cell_h \
            + (gap_foot + fh if foot else 0)
        if total <= band_h:
            break
    y = BAND_TOP + max((band_h - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(head_s, color=ink, bold=True,
                                              spacing=1.12))])
        y += hh + gap_head
    _columns(c, MARGIN, y, col_w, gap, (left, right), ink, dim, accent,
             label_size=lab_s, sub_size=sub_s)
    y += cell_h
    if foot:
        block(c, MARGIN, y + gap_foot, CW,
              [(foot, S(42, color=accent, bold=True, spacing=1.2))])


def quad(c, eye, headline, items, foot=None, dark=False):
    back, ink, dim, accent = _head(c, dark, eye)
    col_w, gap = 370, 40
    hh = TH(headline, CW, DISPLAY, 72, True, 1.12) if headline else 0
    cell_h = 0
    for label, sub in items:
        lh = TH(label, col_w, DISPLAY, 40, True, 1.14, 2.0)
        sh = TH(sub, col_w, BODY, 36, False, 1.34)
        cell_h = max(cell_h, 34 + lh + 20 + sh)
    fh = TH(foot, CW, DISPLAY, 42, True, 1.2) if foot else 0
    gap_head, gap_foot = 62, 58
    total = hh + (gap_head if headline else 0) + cell_h \
        + (gap_foot + fh if foot else 0)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW,
              [(headline, S(72, color=ink, bold=True, spacing=1.12))])
        y += hh + gap_head
    _columns(c, MARGIN, y, col_w, gap, items, ink, dim, accent,
             label_size=40, sub_size=36, tracking=2.0)
    y += cell_h
    if foot:
        block(c, MARGIN, y + gap_foot, CW,
              [(foot, S(42, color=accent, bold=True, spacing=1.2))])


def readings(c, eye, headline, rows_, dark=False):
    back, ink, dim, accent = _head(c, dark, eye)
    lab_w, split = 560, 620
    mean_w = CW - split
    hh = TH(headline, CW, DISPLAY, 68, True, 1.12) if headline else 0
    hs = [max(TH(l.upper(), lab_w, DISPLAY, 34, True, 1.2, 3.0),
              TH(m, mean_w, DISPLAY, 48, True, 1.16)) for l, m in rows_]
    row_gap, gap_head = 46, 64
    total = hh + (gap_head if headline else 0) + sum(hs) \
        + row_gap * (len(rows_) - 1)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW,
              [(headline, S(68, color=ink, bold=True, spacing=1.12))])
        y += hh + gap_head
    for (label, meaning), h in zip(rows_, hs):
        block(c, MARGIN, y + 10, lab_w,
              [(label.upper(), S(34, color=accent, bold=True, spacing=1.2,
                                 tracking=3.0))])
        block(c, MARGIN + split, y, mean_w,
              [(meaning, S(48, color=ink, bold=True, spacing=1.16))])
        y += h + row_gap


def struck(c, eye, headline, crossed, question, dark=False):
    """As the shared version, but the headline is optional and `crossed`
    accepts one string as well as a list."""
    if isinstance(crossed, str):
        crossed = [crossed]
    back, ink, dim, accent = _head(c, dark, eye)
    hh = TH(headline, CW, DISPLAY, 72, True, 1.12) if headline else 0
    wh = [TH(w, CW, DISPLAY, 52, True, 1.2, 0) for w in crossed]
    qh = TH(question, CW, DISPLAY, 60, True, 1.16)
    word_gap, gap_head, gap_rule, gap_q = 26, 58, 44, 46
    total = hh + (gap_head if headline else 0) + sum(wh) \
        + word_gap * (len(crossed) - 1) + gap_rule + 4 + gap_q + qh
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW,
              [(headline, S(72, color=ink, bold=True, spacing=1.12))])
        y += hh + gap_head
    for word, h in zip(crossed, wh):
        block(c, MARGIN, y, CW,
              [(word, S(52, color=dim, bold=True, spacing=1.2, strike=True))])
        y += h + word_gap
    y += gap_rule - word_gap
    rect(c, MARGIN, y, 120, 4, fill=accent)
    block(c, MARGIN, y + 4 + gap_q, CW,
          [(question, S(60, color=ink, bold=True, spacing=1.16))])
