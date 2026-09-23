# -*- coding: utf-8 -*-
"""Layout surface for the V1-V3 sticky-realization decks.

Nothing new is invented here. The flagship module is imported whole, which in
turn imports the house library, so V1's eight approved slides render from the
same code that produced the approved flagship assets and V2 and V3 sit on the
same visual system.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "FLAGSHIP_CAREER_CHANGE/build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

from fl_lay import *                                    # noqa: F401,F403
from fl_lay import compare_rows, matrix, beat, BAND, FIT_BOT
from fl_lay import (MARGIN, CW, GOLD, RULE_CREAM, RULE_NAVY, PAPER,
                    NAVY_SOFT, S, TH, BODY, DISPLAY, block, rect)
from lay23 import (artifact, framework, sequence, compare, twopart, lines,
                   watch_next, statement, claim_card, questions, rule_card,
                   action, stamp, mark, badge, _active, _ground)


def paired(c, eye, headline, cells, shown=4, foot=None, dark=False):
    """A four-way paired read where no quadrant is marked better than another.

    Two differences from the flagship matrix, both deliberate:

    1. The flagship version measures `label` but draws `label.upper()`.
       Uppercase is wider, so a label that fits on one line in mixed case can
       wrap to two when drawn, and the body text is then written on top of the
       second line. The flagship's own labels are short enough that this never
       surfaced there, so its approved assets are unaffected and that module is
       left alone. Here the labels are full sentences, so the measurement has
       to be taken from the string that is actually drawn.

    2. The flagship version tints two quadrants gold and two rust. On this
       slide that would read as two good outcomes and two bad ones, and the
       brief for V2 says explicitly that this is a paired read and NOT a score.
       Every quadrant gets the same rule colour here, so the card describes
       four situations and ranks none of them.
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
    lsz, lgap, tpad, labsz = 29, 12, 22, 24

    def label_h(label, ls):
        return TH(label.upper(), iw, BODY, ls, True, 1.2, 2.6)

    def cell_h(label, items, ls, lg, tp, lb):
        h = tp + label_h(label, lb) + 16
        for line in items:
            h += TH(line, iw, BODY, ls, False, 1.26) + lg
        return h - lg + tp

    def tallest(ls, lg, tp, lb):
        return max(cell_h(l, it, ls, lg, tp, lb) for l, it in cells)

    # Relief order: spacing, then padding, then body size, then label size.
    while tallest(lsz, lgap, tpad, labsz) > rh and lgap > 6:
        lgap -= 1
    while tallest(lsz, lgap, tpad, labsz) > rh and tpad > 14:
        tpad -= 2
    while tallest(lsz, lgap, tpad, labsz) > rh and lsz > 24:
        lsz -= 1
    while tallest(lsz, lgap, tpad, labsz) > rh and labsz > 20:
        labsz -= 1

    rule = GOLD
    quiet = RULE_CREAM if not dark else RULE_NAVY
    for i, (label, items) in enumerate(cells):
        col, row = i % 2, i // 2
        x = MARGIN + col * (cw + gap)
        ty = y + row * (rh + gap)
        on = i < shown
        rect(c, x, ty, cw, rh,
             fill=(PAPER if not dark else NAVY_SOFT) if on else None,
             line=None if on else quiet, lw=2)
        rect(c, x, ty, cw, 6, fill=rule if on else quiet)
        if not on:
            continue
        ix = x + 28
        py = ty + tpad
        block(c, ix, py, iw, [(label.upper(), S(labsz, BODY, rule, bold=True,
                                                tracking=2.6, spacing=1.2))])
        py += label_h(label, labsz) + 16
        for line in items:
            block(c, ix, py, iw, [(line, S(lsz, BODY, ink, spacing=1.26))])
            py += TH(line, iw, BODY, lsz, False, 1.26) + lgap
    if foot:
        stamp(c, foot, dark)
    mark(c, dark)


def ask(c, eye, headline, items, active=None, foot=None, dark=True,
        synthetic=False, max_size=62, min_size=40):
    """questions(), auto-sized so the rows breathe evenly.

    The house questions() layout splits the band into equal rows and centres
    each question inside its own row. It has no relief ladder, so a question
    that wraps to two lines fills its row edge to edge while a one-line
    question beside it looks airy, and the card reads as unevenly spaced even
    though nothing has overflowed. Rather than change the shared layout, this
    picks the largest type size at which every question still fits its row with
    room to spare, then calls questions() unchanged.
    """
    n = len(items)
    y = BAND[0] + 20
    if headline:
        y += TH(headline, CW, DISPLAY, 50, True, 1.1) + 46
    gap = 24
    rowh = (860 - y - gap * (n - 1)) / float(n)
    size = max_size
    while size > min_size:
        tall = max(TH(q, CW - 76, DISPLAY, size, True, 1.12) for q in items)
        if tall <= rowh - 26:
            break
        size -= 2
    questions(c, eye, headline, items, active=active, foot=foot, dark=dark,
              synthetic=synthetic, size=size)
