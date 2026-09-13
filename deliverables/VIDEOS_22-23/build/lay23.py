# -*- coding: utf-8 -*-
"""Card layouts for the V22 and V23 assets.

Built on the house primitives, never by editing them, so every earlier batch
still renders byte for byte. What is new here is the information design the
September 13 brief asked for: a large artifact beside a narrow explainer
panel, numbered reveals that activate one at a time, and side-by-side
contrast cards used only where the contrast itself teaches.

Every stack is measured from real font metrics and centred inside a band that
stops above the caption-safe line, so a longer line pushes the rest of the
card down instead of colliding with it.
"""
import os, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")

from pptx.dml.color import RGBColor
from rdeck import (W, H, MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM,
                   NAVY_DIM, RULE_NAVY, RULE_CREAM, DISPLAY, BODY,
                   bg, rect, block, eyebrow, logomark, text_height)
from layouts import (TH, S, compose, BAND_TOP, BAND_BOT, EYE_Y, EYE_RULE_Y,
                     cta, watch_next, duo, quad, numbered)
import layouts as _house

# Bright warm yellow for the active state, kept distinct from the structural
# muted gold. Off-white for artifact surfaces that must stay readable on a
# phone. Both are sanctioned by the September 13 visual direction.
YELLOW = RGBColor(0xF2, 0xC4, 0x4C)
PAPER = RGBColor(0xFF, 0xFD, 0xF8)
YELLOW_WASH = RGBColor(0xFA, 0xEE, 0xC9)
NAVY_SOFT = RGBColor(0x1B, 0x30, 0x57)

BAND = (BAND_TOP, 860)             # text never goes below 860
# The browser occasionally sets a line a pixel or two taller than the metric
# estimate, so every fitting loop targets a slightly shorter band than the
# one the check measures against.
FIT_BOT = 850
STAMP_Y = 906


# ------------------------------------------------------------------ chrome
def _active(c, n):
    """Declare how many items this card emphasizes. QA reads it back."""
    c.active_items = n


def _foot(c, text):
    """Record a foot-band element so the geometry check knows what it is."""
    if not hasattr(c, "foot_texts"):
        c.foot_texts = []
    c.foot_texts.append(" ".join(text.upper().split()))


def _ground(c, dark, eye, badged=False):
    back = NAVY if dark else CREAM
    ink = CREAM if dark else NAVY
    dim = CREAM_DIM if dark else NAVY_DIM
    bg(c, back)
    if eye:
        # The eyebrow stops short of the synthetic-example badge rather than
        # running its box underneath it.
        ew = CW - 452 if badged else CW
        eyebrow(c, MARGIN, EYE_Y, eye, color=GOLD, w=ew)
        rect(c, MARGIN, EYE_RULE_Y, 120, 4, fill=GOLD)
    return back, ink, dim


def stamp(c, text, dark=False):
    """A quiet source or capture line along the foot of the card."""
    _foot(c, text)
    block(c, MARGIN, STAMP_Y, CW - 130,
          [(text.upper(), S(24, BODY, CREAM_DIM if dark else NAVY_DIM,
                            tracking=3.2, spacing=1.2))])


def badge(c, text="SYNTHETIC EXAMPLE"):
    """The persistent label that travels with every synthetic figure."""
    _foot(c, text)
    w, h = 402, 54
    x, y = W - MARGIN - w, EYE_Y - 8
    rect(c, x, y, w, h, fill=None, line=RUST, lw=3)
    block(c, x, y + 13, w,
          [(text, S(25, BODY, RUST, bold=True, tracking=3.0, align="c",
                    spacing=1.0))])


def mark(c, dark=False):
    logomark(c, W - MARGIN - 77, STAMP_Y - 8,
             gold=GOLD, rust=RUST if not dark else GOLD)


# --------------------------------------------------------------- artifact
def _rows_height(rows, w, label_size, body_size):
    total = 0
    for i, (lab, val) in enumerate(rows):
        if lab:
            total += TH(lab, w, BODY, label_size, True, 1.2, 2.6) + 12
        total += TH(val, w, DISPLAY, body_size, False, 1.26)
        if i < len(rows) - 1:
            total += 30
    return total


def _draw_rows(c, x, y, w, rows, ink, dim, accent, active,
               label_size=25, body_size=40):
    """Preserved posting lines. The active line carries the warm emphasis."""
    for i, (lab, val) in enumerate(rows):
        on = (active is not None and i == active)
        if on:
            h = _rows_height([(lab, val)], w - 44, label_size, body_size)
            rect(c, x - 22, y - 16, w + 44, h + 32, fill=YELLOW_WASH)
            rect(c, x - 22, y - 16, 7, h + 32, fill=RUST)
        if lab:
            block(c, x, y, w, [(lab.upper(), S(label_size, BODY,
                               RUST if on else dim, bold=True, tracking=2.6,
                               spacing=1.2))])
            y += TH(lab, w, BODY, label_size, True, 1.2, 2.6) + 12
        block(c, x, y, w, [(val, S(body_size, DISPLAY,
                            ink if on else (ink if active is None else dim),
                            bold=on, spacing=1.26))])
        y += TH(val, w, DISPLAY, body_size, False, 1.26)
        if i < len(rows) - 1:
            y += 30
    return y


def artifact(c, eye, head, rows, panel=None, active=None, foot=None,
             source=None, synthetic=False, dark=False, head_size=64,
             body_size=40):
    """A large artifact, optionally beside a narrow explainer panel.

    The artifact keeps roughly two thirds of the width so its own words stay
    readable on a phone; the panel carries only the idea being taught at that
    moment, never a paragraph.
    """
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0 if active is None else 1)
    aw = 980 if panel else CW
    ax = MARGIN

    rect(c, ax, BAND[0] - 6, aw, 4, fill=GOLD)
    y = BAND[0] + 40
    block(c, ax, y, aw, [(head, S(head_size, color=ink, bold=True,
                                  spacing=1.1))])
    y += TH(head, aw, DISPLAY, head_size, True, 1.1) + 34
    y = _draw_rows(c, ax, y, aw, rows, ink, dim, GOLD, active,
                   body_size=body_size)
    if foot:
        block(c, ax, y + 30, aw, [(foot, S(30, BODY, dim, spacing=1.34))])

    if panel:
        px, pw = MARGIN + aw + 60, CW - aw - 60
        rect(c, px, BAND[0] - 6, pw, 860 - BAND[0] + 6, fill=NAVY_SOFT)
        py = BAND[0] + 34
        ptitle, pbody = panel
        block(c, px + 34, py, pw - 68,
              [(ptitle.upper(), S(26, BODY, GOLD, bold=True, tracking=3.0,
                                  spacing=1.2))])
        py += TH(ptitle, pw - 68, BODY, 26, True, 1.2, 3.0) + 24
        rect(c, px + 34, py, 74, 4, fill=GOLD)
        py += 30
        block(c, px + 34, py, pw - 68,
              [(pbody, S(38, DISPLAY, CREAM, spacing=1.3))])
    if source:
        stamp(c, source, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def hotspot_artifact(c, eye, head, rows, points, active, source=None,
                     dark=False):
    """The artifact with numbered teaching points, one active at a time.

    YouTube is not interactive, so the numbers are a reading order, never a
    button. The active point is warm and its explanation is the only
    explanation on screen. Rows are measured before anything is drawn, and
    the gaps between them absorb a long line rather than the band doing it.
    """
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 1)
    aw, ax = 980, MARGIN
    rect(c, ax, BAND[0] - 6, aw, 4, fill=GOLD)
    y = BAND[0] + 22
    hw = aw - 90
    block(c, ax, y, hw, [(head, S(52, color=ink, bold=True, spacing=1.1))])
    y += TH(head, hw, DISPLAY, 52, True, 1.1) + 26

    tw = aw - 130
    hs = [TH(lab, tw, BODY, 25, True, 1.2, 2.6) + 12
          + TH(val, tw, DISPLAY, 38, False, 1.26) for lab, val in rows]
    pad, gap = 14, 26
    while sum(hs) + 2 * pad * len(rows) + gap * (len(rows) - 1) \
            > FIT_BOT - y and gap > 6:
        gap -= 2
    while sum(hs) + 2 * pad * len(rows) + gap * (len(rows) - 1) \
            > FIT_BOT - y and pad > 4:
        pad -= 2

    ry = y
    for i, (lab, val) in enumerate(rows):
        on = (i == active)
        rowh = hs[i] + 2 * pad
        if on:
            rect(c, ax - 22, ry, aw + 22, rowh, fill=YELLOW_WASH)
            rect(c, ax - 22, ry, 7, rowh, fill=RUST)
        d = 52
        cy = ry + (rowh - d) / 2.0
        rect(c, ax + aw - d, cy, d, d, fill=RUST if on else None,
             line=None if on else NAVY_DIM, lw=3, shape="oval")
        block(c, ax + aw - d, cy + 10, d,
              [("%d" % (i + 1), S(28, BODY, CREAM if on else NAVY_DIM,
                                  bold=True, align="c", spacing=1.0))])
        block(c, ax, ry + pad, tw,
              [(lab.upper(), S(25, BODY, RUST if on else dim, bold=True,
                               tracking=2.6, spacing=1.2))])
        block(c, ax, ry + pad + TH(lab, tw, BODY, 25, True, 1.2, 2.6) + 12,
              tw, [(val, S(38, DISPLAY, ink if on else dim, bold=on,
                           spacing=1.26))])
        ry += rowh + gap

    px, pw = MARGIN + aw + 60, CW - aw - 60
    ptop, pbot = BAND[0] - 6, 860
    rect(c, px, ptop, pw, pbot - ptop, fill=NAVY_SOFT)
    ptitle, pbody = points[active]
    lead = ("%d  %s" % (active + 1, ptitle)).upper()
    lh = TH(lead, pw - 68, BODY, 26, True, 1.2, 3.0)
    bh = TH(pbody, pw - 68, DISPLAY, 38, False, 1.3)
    py = ptop + max((pbot - ptop - (lh + 24 + 4 + 30 + bh)) / 2.0, 34)
    block(c, px + 34, py, pw - 68,
          [(lead, S(26, BODY, GOLD, bold=True, tracking=3.0, spacing=1.2))])
    py += TH(lead, pw - 68, BODY, 26, True, 1.2, 3.0) + 24
    rect(c, px + 34, py, 74, 4, fill=GOLD)
    py += 30
    block(c, px + 34, py, pw - 68, [(pbody, S(38, DISPLAY, CREAM,
                                              spacing=1.3))])
    if source:
        stamp(c, source, dark)
    mark(c, dark)


# -------------------------------------------------------------- framework
def framework(c, eye, headline, items, active=None, foot=None, dark=False,
              synthetic=False):
    """A whole structure established once, then one component at a time.

    active=None draws the complete structure. An index activates one row and
    quiets the others, so four ideas never compete while one is being taught.
    Rows are measured individually and the gap between them is what gives way
    when the band is tight. Type size never moves.
    """
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
    avail = FIT_BOT - y
    gap = 26
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and gap > 6:
        gap -= 2
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and pad > 6:
        pad -= 2
    total = sum(hs) + 2 * pad * n + gap * (n - 1)
    ry = y + max((avail - total) / 2.0, 0)
    for i, (label, line) in enumerate(items):
        on = (active is None) or (i == active)
        rowh = hs[i] + 2 * pad
        if active is not None and i == active:
            rect(c, MARGIN, ry, CW, rowh, fill=YELLOW_WASH)
        rect(c, MARGIN, ry, 8, rowh, fill=RUST if on else
             (RULE_NAVY if dark else RULE_CREAM))
        tx = MARGIN + 40
        block(c, tx, ry + pad, tw,
              [(label.upper(), S(40, color=ink if on else dim, bold=True,
                                 tracking=1.4, spacing=1.1))])
        if line:
            block(c, tx, ry + pad
                  + TH(label, tw, DISPLAY, 40, True, 1.1, 1.4) + 12, tw,
                  [(line, S(33, BODY, ink if on else dim, spacing=1.3))])
        ry += rowh + gap
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def sequence(c, eye, headline, items, active=None, foot=None, dark=False):
    """Short numbered reveals, one active. For lists of postures or steps."""
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
        ry = y + i * (rowh + gap)
        if active is not None and i == active:
            rect(c, MARGIN - 22, ry - 8, CW + 44, rowh + 16, fill=YELLOW_WASH)
        d = 56
        rect(c, MARGIN, ry + (rowh - d) / 2.0, d, d,
             fill=RUST if on else None,
             line=None if on else (RULE_NAVY if dark else RULE_CREAM), lw=3,
             shape="oval")
        block(c, MARGIN, ry + (rowh - d) / 2.0 + 13, d,
              [("%d" % (i + 1), S(29, BODY, CREAM if on else dim, bold=True,
                                  align="c", spacing=1.0))])
        tx = MARGIN + d + 34
        tw = CW - d - 34
        lh = TH(label, tw, DISPLAY, 46, True, 1.1, 1.2)
        sh = TH(line, tw, BODY, 32, False, 1.3) if line else 0
        ty = ry + (rowh - lh - (sh + 10 if line else 0)) / 2.0
        block(c, tx, ty, tw, [(label.upper(), S(46, color=ink if on else dim,
                              bold=True, tracking=1.2, spacing=1.1))])
        if line:
            block(c, tx, ty + lh + 10, tw,
                  [(line, S(32, BODY, dim, spacing=1.3))])
    if foot:
        stamp(c, foot, dark)
    mark(c, dark)


# ----------------------------------------------------------------- compare
def compare(c, eye, headline, left, right, foot=None, dark=False,
            divider="VS.", synthetic=False, source=None):
    """Two cards side by side, used only where the contrast teaches.

    Each side is (label, title, [(row label, row value)]). Rows appear in the
    same order on both sides so the eye can travel across them. Both cards
    take the height of the taller one and the pair is centred in the band, so
    a short comparison does not leave a card hanging from the top rail.
    """
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(52, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 52, True, 1.1) + 34

    gap = 108
    cw = (CW - gap) / 2.0
    iw = cw - 64
    pad = 30

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
        x = MARGIN + side * (cw + gap)
        rect(c, x, top, cw, ch, fill=PAPER if not dark else NAVY_SOFT)
        rect(c, x, top, cw, 7, fill=GOLD if side == 0 else RUST)
        ix = x + 32
        py = top + pad
        block(c, ix, py, iw, [(label.upper(), S(25, BODY,
                              GOLD if side == 0 else RUST, bold=True,
                              tracking=3.0, spacing=1.2))])
        py += TH(label, iw, BODY, 25, True, 1.2, 3.0) + 18
        block(c, ix, py, iw, [(title, S(42, color=ink, bold=True,
                                        spacing=1.14))])
        py += TH(title, iw, DISPLAY, 42, True, 1.14) + 24
        for rl, rv in rows:
            if rl:
                block(c, ix, py, iw, [(rl.upper(), S(23, BODY, dim, bold=True,
                                       tracking=2.4, spacing=1.2))])
                py += TH(rl, iw, BODY, 23, True, 1.2, 2.4) + 8
            block(c, ix, py, iw, [(rv, S(33, BODY, ink, spacing=1.3))])
            py += TH(rv, iw, BODY, 33, False, 1.3) + 22

    if divider:
        block(c, MARGIN + cw, top + ch / 2.0 - 24, gap,
              [(divider, S(30, BODY, dim, bold=True, align="c", spacing=1.0))])
    if foot:
        stamp(c, foot, dark)
    if source:
        stamp(c, source, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def twopart(c, eye, headline, left, right, joiner="+", foot=None, dark=False,
            synthetic=False):
    """Two halves of one idea, joined rather than opposed."""
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(54, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 54, True, 1.1) + 36
    gap = 108
    cw = (CW - gap) / 2.0
    iw = cw - 64
    pad = 34
    ch = max(TH(l, iw, BODY, 27, True, 1.2, 3.0) + 22
             + TH(b, iw, DISPLAY, 38, False, 1.28) for l, b in (left, right))
    ch = min(ch + pad * 2, FIT_BOT - y)
    top = y + max((FIT_BOT - y - ch) / 2.0, 0)
    for side, (label, body) in enumerate((left, right)):
        x = MARGIN + side * (cw + gap)
        rect(c, x, top, cw, ch, fill=PAPER if not dark else NAVY_SOFT)
        rect(c, x, top, cw, 7, fill=GOLD)
        ix, py = x + 32, top + pad
        block(c, ix, py, iw, [(label.upper(), S(27, BODY, GOLD, bold=True,
                              tracking=3.0, spacing=1.2))])
        py += TH(label, iw, BODY, 27, True, 1.2, 3.0) + 22
        block(c, ix, py, iw, [(body, S(38, DISPLAY, ink, spacing=1.28))])
    block(c, MARGIN + cw, top + ch / 2.0 - 30, gap,
          [(joiner, S(54, color=RUST, bold=True, align="c", spacing=1.0))])
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


# ----------------------------------------------------------------- figures
def stat(c, eye, figure, label, foot=None, dark=True, support=None,
         size=210):
    """One number held large, with the denominator or limit always visible."""
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 0)
    rows = [("text", figure, CW, S(size, color=GOLD, bold=True, spacing=1.0),
             0),
            ("text", label, CW, S(58, color=ink, bold=True, spacing=1.14), 0)]
    gaps = [22]
    if support:
        rows.append(("text", support, CW, S(36, BODY, dim, spacing=1.34), 0))
        gaps.append(34)
    compose(c, MARGIN, rows, band=BAND, gaps=gaps)
    if foot:
        stamp(c, foot, dark)
    mark(c, dark)


def lines(c, eye, headline, items, active=None, foot=None, dark=False,
          synthetic=False, size=44):
    """A finished set of lines, shown whole, then one line at a time."""
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0 if active is None else 1)
    y = BAND[0] + 6
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(50, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 50, True, 1.1) + 34
    n = len(items)
    tw = CW - 76
    avail = FIT_BOT - y
    gap, pad = 20, 12
    hs = [TH(l, tw, BODY, 27, True, 1.2, 2.8) + 12
          + TH(b, tw, DISPLAY, size, False, 1.24) for l, b in items]
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and gap > 8:
        gap -= 2
    while sum(hs) + 2 * pad * n + gap * (n - 1) > avail and pad > 4:
        pad -= 2
    total = sum(hs) + 2 * pad * n + gap * (n - 1)
    y = y + max((avail - total) / 2.0, 0)
    rowh = None
    for i, (label, body) in enumerate(items):
        on = (active is None) or (i == active)
        rowh = hs[i] + 2 * pad
        ry = y + sum(hs[:i]) + 2 * pad * i + gap * i
        if active is not None and i == active:
            rect(c, MARGIN, ry, CW, rowh, fill=YELLOW_WASH)
        rect(c, MARGIN, ry, 8, rowh, fill=RUST if on else
             (RULE_NAVY if dark else RULE_CREAM))
        tx = MARGIN + 38
        block(c, tx, ry + pad, tw,
              [(label.upper(), S(27, BODY, RUST if (active is not None and on)
                                 else (GOLD if on else dim), bold=True,
                                 tracking=2.8, spacing=1.2))])
        lh = TH(label, tw, BODY, 27, True, 1.2, 2.8)
        block(c, tx, ry + pad + lh + 12, tw,
              [(body, S(size, DISPLAY, ink if on else dim, spacing=1.24))])
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def statement(c, eye, headline, support=None, dark=False, size=88,
              support_size=46):
    """The house statement card, declaring that it emphasizes nothing.

    layouts.statement is called unchanged so the card is identical to every
    other batch's statement; only the declaration is added here.
    """
    _house.statement(c, eye, headline, support, dark, size, support_size)
    _active(c, 0)


def claim_card(c, eye, label, text, foot=None, dark=False,
               synthetic=False, size=64):
    """One sentence a reader would actually meet, given the whole screen."""
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0)
    rows = [("text", label.upper(), CW, S(27, BODY, GOLD, bold=True,
                                          tracking=3.0, spacing=1.2), 0),
            ("rule", CW, 4, GOLD),
            ("text", text, CW, S(size, color=ink, bold=True, spacing=1.18),
             0)]
    compose(c, MARGIN, rows, band=(BAND[0], FIT_BOT), gaps=[22, 40])
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def questions(c, eye, headline, items, active=None, foot=None, dark=True,
              synthetic=False, size=62):
    """Questions arriving one at a time, earlier ones held but quiet."""
    back, ink, dim = _ground(c, dark, eye, synthetic)
    _active(c, 0 if active is None else 1)
    y = BAND[0] + 20
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(50, color=ink, bold=True,
                                              spacing=1.1))])
        y += TH(headline, CW, DISPLAY, 50, True, 1.1) + 46
    n = len(items)
    avail = 860 - y
    gap = 24
    rowh = (avail - gap * (n - 1)) / float(n)
    for i, q in enumerate(items):
        if active is not None and i > active:
            continue
        on = (active is None) or (i == active)
        ry = y + i * (rowh + gap)
        rect(c, MARGIN, ry + 8, 8, rowh - 16,
             fill=RUST if on else (RULE_NAVY if dark else RULE_CREAM))
        qh = TH(q, CW - 76, DISPLAY, size, True, 1.12)
        block(c, MARGIN + 38, ry + (rowh - qh) / 2.0, CW - 76,
              [(q, S(size, color=GOLD if on and active is not None else ink,
                     bold=True, spacing=1.12))])
    if foot:
        stamp(c, foot, dark)
    if synthetic:
        badge(c)
    mark(c, dark)


def rule_card(c, eye, number, rule_text, support=None, dark=True):
    """A numbered rule the video actually states out loud."""
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 0)
    rows = [("text", number.upper(), CW, S(30, BODY, GOLD, bold=True,
                                           tracking=4.0, spacing=1.1), 0),
            ("text", rule_text, CW, S(82, color=ink, bold=True,
                                      spacing=1.12), 0)]
    gaps = [30]
    if support:
        rows.append(("text", support, CW, S(38, BODY, dim, spacing=1.34), 0))
        gaps.append(38)
    compose(c, MARGIN, rows, band=BAND, gaps=gaps)
    mark(c, dark)


def action(c, eye, headline, steps, resource=None, dark=True):
    """The one ask, full screen. A resource line only where the script says one."""
    back, ink, dim = _ground(c, dark, eye)
    _active(c, 0)
    y = BAND[0] + 10
    block(c, MARGIN, y, CW, [(headline, S(62, color=ink, bold=True,
                                          spacing=1.12))])
    y += TH(headline, CW, DISPLAY, 62, True, 1.12) + 40
    for i, s in enumerate(steps):
        rect(c, MARGIN + 4, y + 46 * 1.2 / 2.0 - 8, 15, 15, fill=GOLD)
        block(c, MARGIN + 58, y, CW - 58,
              [(s, S(46, color=ink, spacing=1.2))])
        y += TH(s, CW - 58, DISPLAY, 46, False, 1.2) + 22
    if resource:
        y += 26
        rect(c, MARGIN, y, CW, 4, fill=RULE_NAVY if dark else RULE_CREAM)
        y += 34
        label, url = resource
        block(c, MARGIN, y, CW, [(label, S(44, color=GOLD, bold=True,
                                           spacing=1.14))])
        if url:
            y += TH(label, CW, DISPLAY, 44, True, 1.14) + 14
            block(c, MARGIN, y, CW, [(url, S(34, BODY, dim, spacing=1.2))])
    mark(c, dark)
