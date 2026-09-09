# -*- coding: utf-8 -*-
"""Batch-local layouts for Videos 8 to 13.

Built on the shared primitives rather than by editing layouts.py, so the
V4 to V7 packages keep rendering byte-identically. Everything the shared module
already does well is imported and reused unchanged.
"""
import sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
import layouts as L
from layouts import compose, S, TH, BAND_TOP, BAND_BOT, _head
from rdeck import (W, MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM, NAVY_DIM,
                   DISPLAY, BODY, bg, rect, block, eyebrow)

# reused unchanged
statement = L.statement
duo = L.duo
numbered = L.numbered
readings = L.readings
struck = L.struck
cta = L.cta
watch_next = L.watch_next
quad = L.quad

LABEL_Y = 150         # the label takes the eyebrow row, clear of the band


def _stamp(c, label, accent=RUST, ink=CREAM):
    """A provenance stamp that stays readable at phone size.

    Used where the brief requires a visible SYNTHETIC DATA or ILLUSTRATION
    label. It is deliberately not a small footer.
    """
    if not label:
        return
    pad_x, pad_y, size = 26, 14, 30
    h = TH(label, CW, DISPLAY, size, True, 1.1, 3.0) + pad_y * 2
    rect(c, MARGIN, LABEL_Y, CW, h, fill=accent)
    block(c, MARGIN + pad_x, LABEL_Y + pad_y, CW - pad_x * 2,
          [(label, S(size, DISPLAY, ink, bold=True, spacing=1.1, tracking=3.0))])


# A labelled frame gives its eyebrow row to the provenance stamp. The stamp has
# to be readable at phone size, which a 30px gold eyebrow sharing the row with a
# section name would not be, and the brief forbids putting a required label in a
# small footer. The section context lives in the headline instead.
def labeled(c, label, eye, headline, support=None, dark=False, size=76,
            support_size=46):
    """A statement card carrying a prominent provenance stamp."""
    statement(c, None, headline, support, dark=dark, size=size,
              support_size=support_size)
    _stamp(c, label)


def labeled_duo(c, label, eye, headline, left, right, foot=None, dark=False,
                mobile=True):
    duo(c, None, headline, left, right, foot=foot, dark=dark, mobile=mobile)
    _stamp(c, label)


def labeled_readings(c, label, eye, headline, rows_, dark=False):
    readings(c, None, headline, rows_, dark=dark)
    _stamp(c, label)


def labeled_numbered(c, label, eye, items, foot=None, dark=False, size=62,
                     headline=None):
    numbered(c, None, items, foot=foot, dark=dark, size=size, headline=headline)
    _stamp(c, label)


def trio(c, eye, headline, rows_, foot=None, dark=False, size=54):
    """Three short labelled rows plus an optional closing line.

    readings() with room for a foot, used for the three-level and three-status
    frames where the closing line matters as much as the rows.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    lab_w, split = 520, 580
    hh = TH(headline, CW, DISPLAY, 56, True, 1.14) if headline else 0
    hs = [max(TH(a, lab_w, DISPLAY, 34, True, 1.2, 2.0),
              TH(b, CW - split, DISPLAY, size, True, 1.16)) for a, b in rows_]
    fh = TH(foot, CW, DISPLAY, 46, True, 1.2) if foot else 0
    gap_head, row_gap, gap_foot = 54, 38, 58
    total = ((hh + gap_head) if headline else 0) + sum(hs) \
        + row_gap * (len(rows_) - 1) + ((gap_foot + fh) if foot else 0)
    y = BAND_TOP + max((BAND_BOT - BAND_TOP - total) / 2.0, 0)
    if headline:
        block(c, MARGIN, y, CW, [(headline, S(56, color=ink, bold=True,
                                              spacing=1.14))])
        y += hh + gap_head
    for (a, b), h in zip(rows_, hs):
        block(c, MARGIN, y + 8, lab_w,
              [(a, S(34, color=accent, bold=True, spacing=1.2, tracking=2.0))])
        block(c, MARGIN + split, y, CW - split,
              [(b, S(size, color=ink, bold=True, spacing=1.16))])
        y += h + row_gap
    if foot:
        block(c, MARGIN, y - row_gap + gap_foot, CW,
              [(foot, S(46, color=accent, bold=True, spacing=1.2))])
