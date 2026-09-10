# -*- coding: utf-8 -*-
"""Render every frame and measure its geometry against the rendered DOM.

DOM measurement is the ground truth. The PIL measurement inside the layout
code is deliberately conservative, so a frame can pass there and still overflow
in the browser. Nothing is accepted on font-size metadata.
"""
import os, sys
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import rdeck
from rdeck import render_html, render_pptx, shoot
import qa as geoqa
import masters1421 as M
from frames1421 import SETS


def cards_for(n):
    cards, names = [], []
    for i, f in enumerate(SETS[n], 1):
        c = rdeck.Card(i, f["key"] + ".png")
        f["draw"](c)
        cards.append(c)
        names.append(f["key"] + ".png")
    return cards, names


def check(n, workdir):
    os.makedirs(workdir, exist_ok=True)
    cards, names = cards_for(n)
    html = render_html(cards, os.path.join(workdir, "_v%d.html" % n),
                       "V%d" % n)
    return geoqa.check(geoqa.measure(os.path.abspath(html)), names), html, \
        cards, names


if __name__ == "__main__":
    work = sys.argv[1] if len(sys.argv) > 1 else "/tmp/v1421_geo"
    total = 0
    for n in M.VIDEOS:
        probs, _, _, names = check(n, work)
        total += len(probs)
        print("V%-3d %2d frames  %d geometry problems" % (n, len(names),
                                                          len(probs)))
        for p in probs:
            print("      %s" % p)
    print("\ntotal geometry problems: %d" % total)
