# -*- coding: utf-8 -*-
"""Measure every re-anchored card against the rendered DOM."""
import os, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rdeck
from rdeck import render_html
import qa as geoqa
import masters23b as M
import frames23b as F
from geocheck23 import BODY_LIMIT, FOOT_LIMIT, band_check


def cards_for(n, extra=None):
    cards, names = [], []
    for f, s in F.states(n):
        c = rdeck.Card(len(cards) + 1, s["name"] + ".png")
        s["draw"](c)
        cards.append(c)
        names.append(s["name"] + ".png")
    for f in (extra or []):
        for s in f["states"]:
            c = rdeck.Card(len(cards) + 1, s["name"] + ".png")
            s["draw"](c)
            cards.append(c)
            names.append(s["name"] + ".png")
    return cards, names


def check(n, workdir="/tmp/v2223b_geo", extra=None):
    os.makedirs(workdir, exist_ok=True)
    cards, names = cards_for(n, extra)
    html = render_html(cards, os.path.join(workdir, "_v%d.html" % n),
                       "V%d" % n)
    data = geoqa.measure(os.path.abspath(html))
    probs = [p for p in geoqa.check(data, names, 10 ** 6)
             if "below the caption line" not in p]
    probs += band_check(data, names, cards)
    return probs, html, cards, names


if __name__ == "__main__":
    total = 0
    for n in M.VIDEOS:
        probs, html, _, names = check(n)
        total += len(probs)
        print("V%-3d %2d states  %d geometry problems" % (n, len(names),
                                                          len(probs)))
        for p in probs:
            print("      %s" % p)
    print("\ntotal geometry problems: %d" % total)
