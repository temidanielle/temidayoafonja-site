# -*- coding: utf-8 -*-
"""Batch-local layout extension for NEW V10 and V11.

lay23.py is shared with locked packages and is never edited: every earlier
batch must keep rendering byte for byte. This module imports it whole and
adds only the two shapes this pair needs, so V10 and V11 get what they need
without disturbing anything already shipped.

Both additions declare their emphasis state through lay23._active, so QA can
read the active-idea count back off the drawn card exactly as it does for
every house layout.
"""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

from lay23 import *                                            # noqa: F401,F403
import lay23 as _L
import layouts as _house
from lay23 import (_active, _ground, stamp, mark, badge, PAPER,
                   NAVY_SOFT, YELLOW, YELLOW_WASH, FIT_BOT as _FB)
from rdeck import (MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM,
                   NAVY_DIM, RULE_NAVY, RULE_CREAM, DISPLAY, BODY,
                   rect, block, text_height)
from layouts import TH, S, BAND_TOP, BAND_BOT

BAND = (BAND_TOP, BAND_BOT)
FIT_BOT = BAND_BOT


def compare(c, eye, headline, left, right, foot=None, dark=False,
            divider="VS.", synthetic=False, source=None, active=None):
    """lay23.compare, with one side optionally activated.

    The house comparison shows both halves at equal weight, which is right
    when the contrast itself is the teaching. Where the script leads the
    viewer to one side, that side is raised and the other is held but
    quieted, so there is still only one active idea.

    active is None, "left" or "right". With active=None this draws exactly
    what lay23.compare draws.
    """
    if active is None:
        return _L.compare(c, eye, headline, left, right, foot=foot,
                          dark=dark, divider=divider, synthetic=synthetic,
                          source=source)
    if active not in ("left", "right"):
        raise ValueError("active must be None, 'left' or 'right'")
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 1)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(52, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 52, True, 1.1) + 34

    gap = 108
    cw = (CW - gap) / 2.0
    iw = cw - 64
    pad = 30
    live = 0 if active == "left" else 1

    def content_h(side):
        label, title, rows = side
        h = TH(label, iw, BODY, 25, True, 1.2, 3.0) + 18
        h += TH(title, iw, DISPLAY, 42, True, 1.14) + 24
        for rl, rv in rows:
            if rl:
                h += TH(rl, iw, BODY, 23, True, 1.2, 2.4) + 8
            h += TH(rv, iw, BODY, 33, False, 1.3) + 22
        return h

    ch = max(content_h(left), content_h(right)) + pad * 2
    ch = min(ch, FIT_BOT - y)
    top = y + max((FIT_BOT - y - ch) / 2.0, 0)

    for side, (label, title, rows) in enumerate((left, right)):
        on = side == live
        x = MARGIN + side * (cw + gap)
        rect(c, x, top, cw, ch,
             fill=(YELLOW_WASH if not dark else NAVY_SOFT) if on
             else (PAPER if not dark else NAVY_SOFT))
        rect(c, x, top, cw, 7,
             fill=(GOLD if side == 0 else RUST) if on
             else (CREAM_DIM if dark else NAVY_DIM))
        ix = x + 32
        py = top + pad
        lab_col = ((GOLD if side == 0 else RUST) if on
                   else (CREAM_DIM if dark else NAVY_DIM))
        body_col = ink if on else (CREAM_DIM if dark else NAVY_DIM)
        block(c, ix, py, iw, [(label.upper(), S(25, BODY, lab_col, bold=True,
                                                tracking=3.0, spacing=1.2))])
        py += TH(label, iw, BODY, 25, True, 1.2, 3.0) + 18
        block(c, ix, py, iw, [(title, S(42, color=body_col, bold=True,
                                        spacing=1.14))])
        py += TH(title, iw, DISPLAY, 42, True, 1.14) + 24
        for rl, rv in rows:
            if rl:
                block(c, ix, py, iw, [(rl.upper(), S(23, BODY,
                                       lab_col if on else body_col,
                                       bold=True, tracking=2.4,
                                       spacing=1.2))])
                py += TH(rl, iw, BODY, 23, True, 1.2, 2.4) + 8
            block(c, ix, py, iw, [(rv, S(33, BODY, body_col, spacing=1.3))])
            py += TH(rv, iw, BODY, 33, False, 1.3) + 22

    if divider:
        block(c, MARGIN + cw, top + ch / 2.0 - 24, gap,
              [(divider, S(30, BODY, dim, bold=True, align="c",
                           spacing=1.0))])
    if foot:
        stamp(c, foot, dark)
    if source:
        stamp(c, source, dark)
    mark(c, dark)


def struck(c, eye, headline, crossed, question, dark=False):
    """The house struck card, declaring that it emphasizes one idea.

    layouts.struck is called unchanged so the card is identical to every
    other batch's; only the declaration is added here.
    """
    _house.struck(c, eye, headline, crossed, question, dark)
    _active(c, 1)

# ---------------------------------------------------------------------
# The active row on a dark ground.
#
# lay23 fills the active row with YELLOW_WASH, a light cream, and draws its
# text in the card's ink. On a light card that is dark text on a cream chip
# and reads well. On a dark card the ink is cream, so the one row the viewer
# is meant to read becomes the only unreadable one.
#
# No locked package hits that path: V10 and V11 are the first cards to
# combine dark=True with an active index. Rather than edit lay23, which is
# shared with packages that must keep rendering byte for byte, the three
# affected layouts are reproduced here with the same measurements and one
# correction: on a dark ground the active row's text is drawn in navy, over
# the cream chip, exactly as it would be on a light card.
# ---------------------------------------------------------------------


def framework(c, eye, headline, items, active=None, foot=None, dark=False,
              synthetic=False):
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0 if active is None else 1)
    y = BAND[0] + 10
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(56, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 56, True, 1.1) + 40
    n = len(items)
    tw = CW - 80
    pad = 18
    hs = [TH(l, tw, DISPLAY, 40, True, 1.1, 1.4)
          + (12 + TH(t, tw, BODY, 33, False, 1.3) if t else 0)
          for l, t in items]
    avail = _FB - y
    gap = 26
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and gap > 6:
        gap -= 2
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and pad > 6:
        pad -= 2
    total = sum(hs) + 2 * pad * n + gap * (n - 1)
    ry = y + max((avail - total) / 2.0, 0)
    for i, (label, line) in enumerate(items):
        on = (active is None) or (i == active)
        lit = active is not None and i == active
        rowh = hs[i] + 2 * pad
        if lit:
            rect(c, MARGIN, ry, CW, rowh, fill=YELLOW_WASH)
        rect(c, MARGIN, ry, 8, rowh, fill=RUST if on else
             (RULE_NAVY if dark else RULE_CREAM))
        col = NAVY if (lit and dark) else (ink if on else dim)
        tx = MARGIN + 40
        block(c, tx, ry + pad, tw,
              [(label.upper(), S(40, color=col, bold=True, tracking=1.4,
                                 spacing=1.1))])
        if line:
            block(c, tx, ry + pad
                  + TH(label, tw, DISPLAY, 40, True, 1.1, 1.4) + 12, tw,
                  [(line, S(33, BODY, col, spacing=1.3))])
        ry += rowh + gap
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def sequence(c, eye, headline, items, active=None, foot=None, dark=False):
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 0 if active is None else 1)
    y = BAND[0] + 10
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(56, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 56, True, 1.1) + 44
    n = len(items)
    avail = 860 - y
    gap = 22
    rowh = (avail - gap * (n - 1)) / float(n)
    for i, (label, line) in enumerate(items):
        on = (active is None) or (i == active)
        lit = active is not None and i == active
        ry = y + i * (rowh + gap)
        if lit:
            rect(c, MARGIN - 22, ry - 8, CW + 44, rowh + 16,
                 fill=YELLOW_WASH)
        d = 56
        rect(c, MARGIN, ry + (rowh - d) / 2.0, d, d,
             fill=RUST if on else None,
             line=None if on else (RULE_NAVY if dark else RULE_CREAM), lw=3,
             shape="oval")
        block(c, MARGIN, ry + (rowh - d) / 2.0 + 13, d,
              [("%d" % (i + 1), S(29, BODY, CREAM if on else dim, bold=True,
                                  align="c", spacing=1.0))])
        col = NAVY if (lit and dark) else (ink if on else dim)
        sub_col = NAVY if (lit and dark) else dim
        tx = MARGIN + d + 34
        tw = CW - d - 34
        lh = TH(label, tw, DISPLAY, 46, True, 1.1, 1.2)
        sh = TH(line, tw, BODY, 32, False, 1.3) if line else 0
        ty = ry + (rowh - lh - (sh + 10 if line else 0)) / 2.0
        block(c, tx, ty, tw, [(label.upper(), S(46, color=col, bold=True,
                                                tracking=1.2, spacing=1.1))])
        if line:
            block(c, tx, ty + lh + 10, tw,
                  [(line, S(32, BODY, sub_col, spacing=1.3))])
    if foot:
        stamp(c, foot, dark)
    mark(c, dark)


def lines(c, eye, headline, items, active=None, foot=None, dark=False,
          synthetic=False, size=44):
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0 if active is None else 1)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(50, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 50, True, 1.1) + 34
    n = len(items)
    tw = CW - 76
    avail = _FB - y
    gap, pad = 20, 12
    hs = [TH(l, tw, BODY, 27, True, 1.2, 2.8) + 12
          + TH(b, tw, DISPLAY, size, False, 1.24) for l, b in items]
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and gap > 8:
        gap -= 2
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and pad > 4:
        pad -= 2
    total = sum(hs) + 2 * pad * n + gap * (n - 1)
    y = y + max((avail - total) / 2.0, 0)
    for i, (label, body) in enumerate(items):
        on = (active is None) or (i == active)
        lit = active is not None and i == active
        rowh = hs[i] + 2 * pad
        ry = y + sum(hs[:i]) + 2 * pad * i + gap * i
        if lit:
            rect(c, MARGIN, ry, CW, rowh, fill=YELLOW_WASH)
        rect(c, MARGIN, ry, 8, rowh, fill=RUST if on else
             (RULE_NAVY if dark else RULE_CREAM))
        tx = MARGIN + 38
        lab = RUST if (active is not None and on) else (GOLD if on else dim)
        col = NAVY if (lit and dark) else (ink if on else dim)
        block(c, tx, ry + pad, tw,
              [(label.upper(), S(27, BODY, lab, bold=True, tracking=2.8,
                                 spacing=1.2))])
        lh = TH(label, tw, BODY, 27, True, 1.2, 2.8)
        block(c, tx, ry + pad + lh + 12, tw,
              [(body, S(size, DISPLAY, col, spacing=1.24))])
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)
