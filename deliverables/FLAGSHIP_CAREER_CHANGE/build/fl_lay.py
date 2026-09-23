# -*- coding: utf-8 -*-
"""Batch-local layout extension for the flagship career-change assets.

lay23.py is shared with locked packages and is never edited. This module
imports it whole and adds only the three shapes this sequence needs: a
comparison that can mark matching rows, a 2x2 read, and a short beat card.
Each addition declares its emphasis state through lay23._active so QA can
read the active-idea count back off the drawn card.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

from lay23 import *                                            # noqa: F401,F403
from lay23 import _active, _ground, stamp, mark, PAPER, NAVY_SOFT, YELLOW
from rdeck import (MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM, NAVY_DIM,
                   RULE_NAVY, RULE_CREAM, DISPLAY, BODY, rect, block)
from layouts import TH, S, BAND_TOP, BAND_BOT, compose

BAND = (BAND_TOP, BAND_BOT)
FIT_BOT = BAND_BOT


def compare_rows(c, eye, headline, left, right, match=(), foot=None,
                 banner=None, dark=False, divider="VS.", source=None,
                 shown=2):
    """lay23.compare, with two additions this sequence needs.

    match marks the row indexes where the two sides use the same or adjacent
    language, so the viewer can see the overlap without being told the jobs
    are equivalent. banner draws one line across the bottom at statement
    weight rather than as a small stamp, for the beat the script lands on.
    shown=1 draws the left card only, for the first reveal state.
    """
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 1 if match else 0)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(52, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 52, True, 1.1) + 34

    # The banner lives in the footer zone, where the small stamp would
    # otherwise sit, rather than being carved out of the band. Taking it out
    # of the band leaves too little room for a six-row comparison, and the
    # cards matter more than the line does.
    bot = FIT_BOT

    gap = 108
    cw = (CW - gap) / 2.0
    iw = cw - 64
    pad = 30
    rgap = 22

    rsz, tsz = 33, 42

    def content_h(side, rg, rs, ts):
        label, title, rows = side
        h = TH(label, iw, BODY, 25, True, 1.2, 3.0) + 18
        h += TH(title, iw, DISPLAY, ts, True, 1.14) + 24
        for rl, rv in rows:
            if rl:
                h += TH(rl, iw, BODY, 23, True, 1.2, 2.4) + 8
            h += TH(rv, iw, BODY, rs, False, 1.3) + rg
        return h

    def tallest(rg, rs, ts):
        return max(content_h(left, rg, rs, ts), content_h(right, rg, rs, ts))

    # The banner takes its space out of the band first. Then the row gap, the
    # card padding, the row size and finally the title size give way in that
    # order, so a six-row comparison never draws over the line the script
    # lands on and the type only shrinks once spacing has run out.
    avail = bot - y
    while tallest(rgap, rsz, tsz) + pad * 2 > avail and rgap > 10:
        rgap -= 2
    while tallest(rgap, rsz, tsz) + pad * 2 > avail and pad > 14:
        pad -= 2
    while tallest(rgap, rsz, tsz) + pad * 2 > avail and rsz > 27:
        rsz -= 1
    while tallest(rgap, rsz, tsz) + pad * 2 > avail and tsz > 34:
        tsz -= 2
    ch = min(tallest(rgap, rsz, tsz) + pad * 2, avail)
    top = y + max((avail - ch) / 2.0, 0)

    sides = (left, right)[:shown]
    for side, (label, title, rows) in enumerate(sides):
        x = MARGIN + side * (cw + gap)
        rect(c, x, top, cw, ch, fill=PAPER if not dark else NAVY_SOFT)
        rect(c, x, top, cw, 7, fill=GOLD if side == 0 else RUST)
        ix = x + 32
        py = top + pad
        block(c, ix, py, iw, [(label.upper(), S(25, BODY,
                              GOLD if side == 0 else RUST, bold=True,
                              tracking=3.0, spacing=1.2))])
        py += TH(label, iw, BODY, 25, True, 1.2, 3.0) + 18
        block(c, ix, py, iw, [(title, S(tsz, color=ink, bold=True,
                                        spacing=1.14))])
        py += TH(title, iw, DISPLAY, tsz, True, 1.14) + 24
        for i, (rl, rv) in enumerate(rows):
            on = (i in match)
            if rl:
                block(c, ix, py, iw, [(rl.upper(), S(23, BODY, dim, bold=True,
                                       tracking=2.4, spacing=1.2))])
                py += TH(rl, iw, BODY, 23, True, 1.2, 2.4) + 8
            rh = TH(rv, iw, BODY, rsz, False, 1.3)
            if on:
                # A thin marker, not a fill. The overlap is shown, not
                # asserted, because a heavy highlight reads as equivalence.
                rect(c, ix - 18, py, 5, rh, fill=GOLD)
            block(c, ix, py, iw,
                  [(rv, S(rsz, BODY, ink, spacing=1.3))])
            py += rh + rgap

    if divider and shown == 2:
        dz = 62 if divider in ("\u2192", "\u2794") else 30
        block(c, MARGIN + cw, top + ch / 2.0 - dz * 0.8, gap,
              [(divider, S(dz, BODY, GOLD if dark else RUST, bold=True,
                           align="c", spacing=1.0))])
    if banner:
        block(c, MARGIN, FIT_BOT + 44, CW - 260,
              [(banner, S(46, color=GOLD if dark else RUST, bold=True,
                          spacing=1.16))])
    if foot:
        stamp(c, foot, dark)
    if source:
        stamp(c, source, dark)
    mark(c, dark)


def matrix(c, eye, headline, cells, shown=4, foot=None, dark=False):
    """A 2x2 read. cells is four (label, [line, ...]) in reading order.

    shown reveals the quadrants one at a time in the same order, so the
    complete read arrives as the fifth state rather than all at once.
    """
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 1 if shown < 4 else 0)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(46, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 46, True, 1.1) + 26

    gap = 40
    cw = (CW - gap) / 2.0
    avail = FIT_BOT - y
    rh = (avail - gap) / 2.0
    iw = cw - 56
    lsz, lgap, tpad = 29, 12, 22

    def cell_h(items, ls, lg, tp):
        h = tp + TH("X", iw, BODY, 24, True, 1.2, 2.6) + 16
        for line in items:
            h += TH(line, iw, BODY, ls, False, 1.26) + lg
        return h - lg + tp

    def tallest(ls, lg, tp):
        return max(cell_h(it, ls, lg, tp) for _, it in cells)

    # Same relief order as the comparison: spacing first, then type size, so
    # a five-line quadrant stays inside its panel at phone size.
    while tallest(lsz, lgap, tpad) > rh and lgap > 6:
        lgap -= 1
    while tallest(lsz, lgap, tpad) > rh and tpad > 14:
        tpad -= 2
    while tallest(lsz, lgap, tpad) > rh and lsz > 24:
        lsz -= 1

    for i, (label, items) in enumerate(cells):
        col, row = i % 2, i // 2
        x = MARGIN + col * (cw + gap)
        ty = y + row * (rh + gap)
        on = i < shown
        rect(c, x, ty, cw, rh,
             fill=(PAPER if not dark else NAVY_SOFT) if on else None,
             line=None if on else (RULE_CREAM if not dark else RULE_NAVY),
             lw=2)
        rect(c, x, ty, cw, 6, fill=(GOLD if i % 2 == 0 else RUST) if on
             else (RULE_CREAM if not dark else RULE_NAVY))
        if not on:
            continue
        ix = x + 28
        py = ty + tpad
        block(c, ix, py, iw, [(label.upper(), S(24, BODY, GOLD if i % 2 == 0
                              else RUST, bold=True, tracking=2.6,
                              spacing=1.2))])
        py += TH(label, iw, BODY, 24, True, 1.2, 2.6) + 16
        for line in items:
            block(c, ix, py, iw, [(line, S(lsz, BODY, ink, spacing=1.26))])
            py += TH(line, iw, BODY, lsz, False, 1.26) + lgap
    if foot:
        stamp(c, foot, dark)
    mark(c, dark)


def beat(c, eye, big, small=None, dark=True):
    """One short visual beat. The statement in cream, the question in gold."""
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 0)
    rows = [("text", big, CW, S(96, color=ink, bold=True, spacing=1.1), 0)]
    gaps = []
    if small:
        rows.append(("text", small, CW, S(46, BODY, GOLD, spacing=1.32), 0))
        gaps.append(54)
    compose(c, MARGIN, rows, band=(BAND[0], FIT_BOT), gaps=gaps)
    mark(c, dark)
