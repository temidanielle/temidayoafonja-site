# -*- coding: utf-8 -*-
"""Measure every V22 and V23 card against the rendered DOM, not a prediction."""
import os, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rdeck
from rdeck import render_html
import qa as geoqa
import masters23 as M
import frames23 as F

# These two videos carry no burned-in captions, so the body band runs lower
# than the V4-V21 standard. The foot band below it is where a source stamp or
# a synthetic-example badge is meant to sit, and only those may go there: a
# body block that spills past 880 is still a failure, because the check knows
# which strings the layout registered as foot elements.
BODY_LIMIT = 880
FOOT_LIMIT = 960


def cards_for(n):
    cards, names = [], []
    for i, (f, s) in enumerate(F.states(n), 1):
        c = rdeck.Card(i, s["name"] + ".png")
        s["draw"](c)
        cards.append(c)
        names.append(s["name"] + ".png")
    return cards, names


def _norm(t):
    return " ".join(t.upper().replace("|", " ").split())


def band_check(data, names, cards):
    """Body copy above BODY_LIMIT; registered foot elements above FOOT_LIMIT."""
    problems = []
    for sl in data:
        i = sl["slide"] - 1
        name = names[i]
        feet = [_norm(t) for t in getattr(cards[i], "foot_texts", [])]
        for e in sl["els"]:
            if not e["isText"] or not e["text"].strip():
                continue
            t = _norm(e["text"])
            is_foot = any(t == f or t in f or f in t for f in feet)
            limit = FOOT_LIMIT if is_foot else BODY_LIMIT
            bottom = e["y"] + e["h"]
            if bottom > limit:
                problems.append(
                    "%s: %s text reaches y=%.0f, past its %d limit: %r"
                    % (name, "foot" if is_foot else "body", bottom, limit,
                       e["text"][:44]))
    return problems


def check(n, workdir="/tmp/v2223_geo"):
    os.makedirs(workdir, exist_ok=True)
    cards, names = cards_for(n)
    html = render_html(cards, os.path.join(workdir, "_v%d.html" % n),
                       "V%d" % n)
    data = geoqa.measure(os.path.abspath(html))
    # geoqa's own caption test is replaced by the two-band test above; its
    # overlap and safe-margin tests still apply unchanged.
    probs = [p for p in geoqa.check(data, names, 10 ** 6)
             if "below the caption line" not in p]
    probs += band_check(data, names, cards)
    return probs, html, cards, names


if __name__ == "__main__":
    total = 0
    for n in M.VIDEOS:
        probs, html, _, names = check(n)
        total += len(probs)
        print("V%-3d %2d states  %d geometry problems  %s"
              % (n, len(names), len(probs), html))
        for p in probs:
            print("      %s" % p)
    print("\ntotal geometry problems: %d" % total)
