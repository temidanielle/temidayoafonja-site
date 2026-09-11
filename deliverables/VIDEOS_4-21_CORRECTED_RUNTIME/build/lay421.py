# -*- coding: utf-8 -*-
"""Layouts for the corrected-runtime batch.

Reuses the shapes built and geometry-tested for the September 10 batch rather
than restating them, and adds the shapes these eighteen masters need. Nothing
in layouts.py or rdeck.py is edited, so every earlier batch keeps rendering
byte-identically.
"""
import sys, os
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                   "VIDEOS_14-21_FINAL_PRODUCTION/build")

from lay1421 import (statement, duo, quad, numbered, readings, struck, cta,
                     watch_next, trio, shared_then_split, statfacts,
                     two_questions, word_vs_work, ladder, four_bucket,
                     cta_action, S, TH, compose)
from layouts import BAND_TOP, BAND_BOT, _head, _columns
from rdeck import (W, H, MARGIN, CW, NAVY, CREAM, GOLD, RUST, CREAM_DIM,
                   NAVY_DIM, DISPLAY, BODY, bg, rect, block, eyebrow)


def three_lines(c, eye, headline, lines, foot=None, dark=False, size=64):
    """A short numbered set of lines, each one a complete instruction.

    Used for the three- and four-line artifacts several of these masters end
    on, where each line is a sentence the viewer writes rather than a label.
    """
    back, ink, dim, accent = _head(c, dark, eye)
    rows, gaps = [], []
    if headline:
        rows.append(("text", headline, CW, S(52, color=ink, bold=True,
                                             spacing=1.12), 0))
        gaps.append(38)
    for i, t in enumerate(lines):
        rows.append(("text", t, CW, S(size, color=ink, bold=True,
                                      spacing=1.14), 0))
        if i < len(lines) - 1:
            gaps.append(30)
    if foot:
        gaps.append(44)
        rows.append(("text", foot, CW, S(38, BODY, dim, spacing=1.32), 0))
    compose(c, MARGIN, rows, gaps=gaps)


def labeled_rows(c, eye, headline, rows_, dark=False):
    """Short label on the left, the sentence it names on the right."""
    return readings(c, eye, headline, rows_, dark=dark)
