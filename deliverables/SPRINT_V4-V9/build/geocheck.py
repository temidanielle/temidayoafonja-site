# -*- coding: utf-8 -*-
"""Measure every sprint card against the rendered DOM."""
import os, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rdeck
from rdeck import render_html
import qa as geoqa
import sprint as S
import frames as F
from geocheck23 import BODY_LIMIT, FOOT_LIMIT, band_check


def cards_for(n):
    cards, names = [], []
    for f, st in F.states(n):
        c = rdeck.Card(len(cards) + 1, st["name"] + ".png")
        st["draw"](c)
        cards.append(c)
        names.append(st["name"] + ".png")
    return cards, names


def check(n, workdir="/tmp/sprint_geo"):
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
