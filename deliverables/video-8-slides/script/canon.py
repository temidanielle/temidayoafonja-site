# -*- coding: utf-8 -*-
"""Canonical spoken-word count for the Capability Formation recording scripts.

ONE definition, used by the script generator, by the QA checks and by the
package README, so the number cannot disagree between them.

Counted   the spoken paragraphs only, in teleprompter order.
Excluded  document title and header lines, the Target/length statement, timed
          block headers (0:00-0:25 | ...), slide markers (SLIDE 4 - ...), and
          any other production direction.
Method    str.split() on whitespace, summed across those paragraphs. A
          hyphenated or contracted word counts as one word, which is how a
          person reading aloud experiences it.
"""
import re

HDR = re.compile(r"^\d+:\d\d[\u2013\u2014-]\d+:\d\d\s*\|")
MARKER = re.compile(r"^SLIDE \d+\s+[\u2013\u2014-]")
NOT_SPOKEN_PREFIX = ("Target",)


def is_spoken(paragraph):
    p = (paragraph or "").strip()
    if not p:
        return False
    if HDR.match(p) or MARKER.match(p):
        return False
    if p.startswith(NOT_SPOKEN_PREFIX):
        return False
    return True


def spoken_paragraphs(blocks):
    return [b.strip() for b in blocks if is_spoken(b)]


def count(blocks):
    """Canonical spoken-word count over an iterable of paragraphs."""
    return sum(len(p.split()) for p in spoken_paragraphs(blocks))
