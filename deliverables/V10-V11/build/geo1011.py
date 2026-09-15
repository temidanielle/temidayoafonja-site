# -*- coding: utf-8 -*-
"""Measure every V10 and V11 card against the rendered DOM.

The DOM is ground truth: predicted text metrics and browser metrics diverge,
so nothing is accepted on a prediction."""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rdeck
from rdeck import render_html
import qa as geoqa
import v1011 as S
import frames1011 as F
from geocheck23 import BODY_LIMIT, FOOT_LIMIT, band_check


def cards_for(n):
    cards, names = [], []
    for f, st in F.states(n):
        c = rdeck.Card(len(cards) + 1, st["name"] + ".png")
        st["draw"](c)
        cards.append(c)
        names.append(st["name"] + ".png")
    return cards, names


def check(n, workdir="/tmp/claude-0/-home-user-temidayoafonja-site/f121668d-e262-5eb8-9b22-0eaa1006a361/scratchpad/geo1011"):
    os.makedirs(workdir, exist_ok=True)
    cards, names = cards_for(n)
    html = render_html(cards, os.path.join(workdir, "_v%d.html" % n),
                       "NEW V%d" % n)
    data = geoqa.measure(os.path.abspath(html))
    probs = [p for p in geoqa.check(data, names, 10 ** 6)
             if "below the caption line" not in p]
    probs += band_check(data, names, cards)
    return probs, html, cards, names


if __name__ == "__main__":
    total = 0
    for n in S.VIDEOS:
        probs, _, _, names = check(n)
        total += len(probs)
        print("NEW V%-3d %2d states  %d geometry problems" % (n, len(names),
                                                              len(probs)))
        for p in probs:
            print("      %s" % p)
    print("\ntotal geometry problems: %d" % total)
