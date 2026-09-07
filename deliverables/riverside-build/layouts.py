# -*- coding: utf-8 -*-
"""Card layouts for the Riverside edit assets.

Every layout composes a vertical stack whose height is measured from the real
font metrics, then centres that stack inside a band that stops above the
caption-safe line. Nothing is positioned by hand, so a longer headline pushes
the rest of the card down instead of colliding with it.
"""
from rdeck import (W, H, MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM,
                   NAVY_DIM, RULE_NAVY, RULE_CREAM, DISPLAY, BODY,
                   bg, rect, block, eyebrow, logomark, text_height)

EYE_Y, EYE_RULE_Y = 168, 224
BAND_TOP, BAND_BOT = 250, 806          # lifted clear of the caption zone


FIT = 0.94          # measure against a narrower box than the browser gets


def TH(text, w, font=DISPLAY, size=40, bold=False, spacing=1.14, tracking=0):
    """Conservative text height: never fewer lines than the browser will use."""
    return text_height(text, w * FIT, font, size, bold, spacing, tracking)


def _theme(dark):
    if dark:
        return NAVY, CREAM, CREAM_DIM, GOLD
    return CREAM, NAVY, NAVY_DIM, GOLD


def _head(c, dark, eyebrow_text):
    back, ink, dim, accent = _theme(dark)
    bg(c, back)
    if eyebrow_text:
        eyebrow(c, MARGIN, EYE_Y, eyebrow_text, color=accent)
        rect(c, MARGIN, EYE_RULE_Y, 120, 4, fill=accent)
    return back, ink, dim, accent


# ------------------------------------------------------------------ stack
def _height(row):
    if row[0] == "text":
        _, text, w, st, gap = row
        return TH(text, w, st["font"], st["size"], st["bold"],
                           st["spacing"], st.get("tracking", 0))
    if row[0] == "rule":
        return row[2]
    return row[1]                                   # ("space", px)


def _draw(c, row, x, y):
    if row[0] == "text":
        _, text, w, st, gap = row
        block(c, x, y, w, [(text, st)])
    elif row[0] == "rule":
        _, rw, rh, color = row
        rect(c, x, y, rw, rh, fill=color)


def compose(c, x, rows, band=(BAND_TOP, BAND_BOT), gaps=None):
    """Centre a list of rows inside the band and draw them."""
    gaps = gaps or [0] * (len(rows) - 1)
    total = sum(_height(r) for r in rows) + sum(gaps)
    top, bot = band
    y = top + max((bot - top - total) / 2.0, 0)
    for i, r in enumerate(rows):
        _draw(c, r, x, y)
        y += _height(r)
        if i < len(gaps):
            y += gaps[i]
    return y


def S(size, font=DISPLAY, color=NAVY, bold=False, spacing=1.14, tracking=0,
      align="l", strike=False):
    return dict(size=size, font=font, color=color, bold=bold, italic=False,
                spacing=spacing, tracking=tracking, align=align,
                space_before=0, space_after=0, strike=strike)


# ---------------------------------------------------------------- layouts
def statement(c, eye, headline, support=None, dark=False, size=88):
    """One strong statement or question, and at most one short line under it."""
    back, ink, dim, accent = _head(c, dark, eye)
    rows = [("text", headline, CW, S(size, color=ink, bold=True, spacing=1.12), 0)]
    gaps = []
    if support:
        rows.append(("text", support, CW, S(46, BODY, dim, spacing=1.35), 0))
        gaps.append(46)
    compose(c, MARGIN, rows, gaps=gaps)


def _columns(c, x, y, col_w, gap, cells, ink, dim, accent,
             label_size=52, sub_size=42, tracking=0):
    """A row of label-and-line columns, each under its own hairline."""
    heights = []
    for i, (label, sub) in enumerate(cells):
        cx = x + i * (col_w + gap)
        rect(c, cx, y, col_w, 4, fill=accent)
        block(c, cx, y + 34, col_w,
              [(label, S(label_size, color=ink, bold=True, spacing=1.14,
                         tracking=tracking))])
        lh = TH(label, col_w, DISPLAY, label_size, True, 1.14, tracking)
        block(c, cx, y + 34 + lh + 20, col_w,
              [(sub, S(sub_size, BODY, dim, spacing=1.34))])
        sh = TH(sub, col_w, BODY, sub_size, False, 1.34)
        heights.append(34 + lh + 20 + sh)
    return max(heights)


def duo(c, eye, headline, left, right, foot=None, dark=False):
    """A two-way comparison. Each side is a label and one short line.

    Type steps down through a small ladder until the whole card fits inside the
    band, so a longer right-hand quotation shrinks the set rather than pushing
    the closing line into the caption zone.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    col_w, gap = 760, 80
    band_h = BAND_BOT - BAND_TOP
    gap_head, gap_foot = 64, 58

    for head_s, lab_s, sub_s in ((72, 52, 42), (68, 48, 40), (64, 46, 38),
                                 (60, 44, 36), (56, 42, 34)):
        hh = TH(headline, CW, DISPLAY, head_s, True, 1.12)
        cell_h = 0
        for label, sub in (left, right):
            lh = TH(label, col_w, DISPLAY, lab_s, True, 1.14)
            sh = TH(sub, col_w, BODY, sub_s, False, 1.34)
            cell_h = max(cell_h, 34 + lh + 20 + sh)
        fh = TH(foot, CW, DISPLAY, 42, True, 1.2) if foot else 0
        total = hh + gap_head + cell_h + (gap_foot + fh if foot else 0)
        if total <= band_h:
            break

    y = BAND_TOP + max((band_h - total) / 2.0, 0)
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
    """A four-part framework as four columns, each a label and a short question."""
    back, ink, dim, accent = _head(c, dark, eye)
    col_w, gap = 370, 40
    hh = TH(headline, CW, DISPLAY, 72, True, 1.12)
    cell_h = 0
    for label, sub in items:
        lh = TH(label, col_w, DISPLAY, 40, True, 1.14, 2.0)
        sh = TH(sub, col_w, BODY, 36, False, 1.34)
        cell_h = max(cell_h, 34 + lh + 20 + sh)
    fh = TH(foot, CW, DISPLAY, 42, True, 1.2) if foot else 0
    gap_head, gap_foot = 62, 58
    total = hh + gap_head + cell_h + (gap_foot + fh if foot else 0)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    block(c, MARGIN, y, CW, [(headline, S(72, color=ink, bold=True, spacing=1.12))])
    y += hh + gap_head
    _columns(c, MARGIN, y, col_w, gap, items, ink, dim, accent,
             label_size=40, sub_size=36, tracking=2.0)
    y += cell_h
    if foot:
        block(c, MARGIN, y + gap_foot, CW,
              [(foot, S(42, color=accent, bold=True, spacing=1.2))])


def numbered(c, eye, items, foot=None, dark=False, size=62, headline=None):
    """Named steps or questions, numbered. No explanatory copy under each one."""
    back, ink, dim, accent = _head(c, dark, eye)
    gutter, row_gap = 132, 40
    tw = CW - gutter
    hh = TH(headline, CW, DISPLAY, 60, True, 1.12) if headline else 0
    hs = [TH(t, tw, DISPLAY, size, True, 1.12) for t in items]
    fh = TH(foot, CW, BODY, 42, False, 1.34) if foot else 0
    gap_head, gap_foot = 56, 62
    total = ((hh + gap_head) if headline else 0) + sum(hs) \
        + row_gap * (len(items) - 1) + (gap_foot + fh if foot else 0)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW,
              [(headline, S(60, color=ink, bold=True, spacing=1.12))])
        y += hh + gap_head
    for i, (t, h) in enumerate(zip(items, hs), start=1):
        block(c, MARGIN, y + 12, 110,
              [("%02d" % i, S(40, color=accent, bold=True, tracking=1.5))])
        block(c, MARGIN + gutter, y, tw,
              [(t, S(size, color=ink, bold=True, spacing=1.12))])
        y += h + row_gap
    if foot:
        block(c, MARGIN, y - row_gap + gap_foot, CW,
              [(foot, S(42, BODY, dim, spacing=1.34))])


def readings(c, eye, headline, rows_, dark=False):
    """Condition rows: a short label on the left, what it means on the right."""
    back, ink, dim, accent = _head(c, dark, eye)
    lab_w, split = 560, 620
    mean_w = CW - split
    hh = TH(headline, CW, DISPLAY, 68, True, 1.12)
    hs = [max(TH(l.upper(), lab_w, DISPLAY, 34, True, 1.2, 3.0),
              TH(m, mean_w, DISPLAY, 48, True, 1.16)) for l, m in rows_]
    row_gap, gap_head = 46, 64
    total = hh + gap_head + sum(hs) + row_gap * (len(rows_) - 1)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    block(c, MARGIN, y, CW, [(headline, S(68, color=ink, bold=True, spacing=1.12))])
    y += hh + gap_head
    for (label, meaning), h in zip(rows_, hs):
        block(c, MARGIN, y + 10, lab_w,
              [(label.upper(), S(34, color=accent, bold=True, spacing=1.2,
                                 tracking=3.0))])
        block(c, MARGIN + split, y, mean_w,
              [(meaning, S(48, color=ink, bold=True, spacing=1.16))])
        y += h + row_gap


def struck(c, eye, headline, crossed, question, dark=False):
    """Words to look past, struck through, and the question that replaces them."""
    back, ink, dim, accent = _head(c, dark, eye)
    hh = TH(headline, CW, DISPLAY, 72, True, 1.12)
    wh = [TH(w.upper(), CW, DISPLAY, 44, True, 1.2, 3.0) for w in crossed]
    qh = TH(question, CW, DISPLAY, 52, True, 1.16)
    word_gap, gap_head, gap_rule, gap_q = 26, 58, 44, 46
    total = hh + gap_head + sum(wh) + word_gap * (len(crossed) - 1) \
        + gap_rule + 4 + gap_q + qh
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    block(c, MARGIN, y, CW, [(headline, S(72, color=ink, bold=True, spacing=1.12))])
    y += hh + gap_head
    for word, h in zip(crossed, wh):
        block(c, MARGIN, y, CW,
              [(word.upper(), S(44, color=dim, bold=True, spacing=1.2,
                                tracking=3.0, strike=True))])
        y += h + word_gap
    y += gap_rule - word_gap
    rect(c, MARGIN, y, 120, 4, fill=accent)
    block(c, MARGIN, y + 4 + gap_q, CW,
          [(question, S(52, color=ink, bold=True, spacing=1.16))])


def cta(c, eye, headline, support, url):
    """The approved CTA card. Navy, restrained, the URL as the last line."""
    bg(c, NAVY)
    logomark(c, MARGIN, 156)
    rows = [
        ("text", eye.upper(), CW, S(30, color=GOLD, bold=True, tracking=5.0,
                                    spacing=1.0), 0),
        ("text", headline, CW, S(84, color=CREAM, bold=True, spacing=1.12), 0),
        ("text", support, CW, S(44, BODY, CREAM_DIM, spacing=1.34), 0),
        ("rule", 120, 4, GOLD),
        ("text", url, CW, S(48, color=GOLD, bold=True, spacing=1.2), 0),
    ]
    compose(c, MARGIN, rows, band=(300, 856), gaps=[36, 42, 54, 44])


def watch_next(c, title, playlist=None):
    """Watch Next. Copy stays left so a YouTube end screen can sit on the right."""
    bg(c, NAVY)
    col_w = 1020 - MARGIN            # keep the right of the frame clear
    rows = [
        ("text", "WATCH NEXT", col_w, S(30, color=GOLD, bold=True, tracking=5.0,
                                        spacing=1.0), 0),
        ("rule", 120, 4, GOLD),
        ("text", title, col_w, S(68, color=CREAM, bold=True, spacing=1.16), 0),
    ]
    gaps = [30, 48]
    if playlist:
        rows.append(("text", playlist, col_w,
                     S(32, BODY, CREAM_DIM, spacing=1.34), 0))
        gaps.append(56)
    compose(c, MARGIN, rows, gaps=gaps)


def bignumber(c, eye, headline, before, after, labels, foot=None, dark=False):
    """One result, shown as the two numbers with an arrow between them."""
    back, ink, dim, accent = _head(c, dark, eye)
    hh = TH(headline, CW, DISPLAY, 56, True, 1.14)
    num_h, lab_h = 190, 40
    fh = TH(foot, CW, BODY, 40, False, 1.34) if foot else 0
    gap_head, gap_lab, gap_foot = 66, 26, 62
    total = hh + gap_head + num_h + gap_lab + lab_h + (gap_foot + fh if foot else 0)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    block(c, MARGIN, y, CW, [(headline, S(56, color=ink, bold=True, spacing=1.14))])
    y += hh + gap_head
    col_w, arrow_w = 640, 200
    for i, (num, lab) in enumerate(((before, labels[0]), (after, labels[1]))):
        x = MARGIN + i * (col_w + arrow_w)
        block(c, x, y, col_w, [(num, S(168, color=ink, bold=True,
                                       spacing=1.0, align="c"))])
        block(c, x, y + num_h + gap_lab, col_w,
              [(lab.upper(), S(30, color=dim, bold=True, spacing=1.2,
                               tracking=3.0, align="c"))])
    ax = MARGIN + col_w
    rect(c, ax + 40, y + 90, 120, 8, fill=accent)   # a plain bar reads as "to"
    if foot:
        block(c, MARGIN, y + num_h + gap_lab + lab_h + gap_foot, CW,
              [(foot, S(40, BODY, dim, spacing=1.34))])


def grid4(c, eye, headline, cells, dark=False):
    """A four-part record in two rows of two, each a label and one sentence."""
    back, ink, dim, accent = _head(c, dark, eye)
    col_w, col_gap, row_gap = 760, 80, 52
    hh = TH(headline, CW, DISPLAY, 56, True, 1.14)
    lab_s, txt_s = 34, 32

    def cell_h(label, text):
        return (TH(label.upper(), col_w, DISPLAY, lab_s, True, 1.2, 3.0)
                + 18 + TH(text, col_w, BODY, txt_s, False, 1.34))

    rows = [cells[0:2], cells[2:4]]
    rh = [max(cell_h(l, t) for l, t in r) for r in rows]
    total = hh + 58 + sum(rh) + row_gap
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    block(c, MARGIN, y, CW, [(headline, S(56, color=ink, bold=True, spacing=1.14))])
    y += hh + 58
    for row, h in zip(rows, rh):
        for i, (label, text) in enumerate(row):
            x = MARGIN + i * (col_w + col_gap)
            rect(c, x, y - 22, col_w, 3, fill=accent)
            block(c, x, y, col_w, [(label.upper(),
                  S(lab_s, color=accent, bold=True, spacing=1.2, tracking=3.0))])
            lh = TH(label.upper(), col_w, DISPLAY, lab_s, True, 1.2, 3.0)
            block(c, x, y + lh + 18, col_w,
                  [(text, S(txt_s, BODY, ink, spacing=1.34))])
        y += h + row_gap
