# -*- coding: utf-8 -*-
"""Watch Next destinations for the story-led set.

Where the script speaks the destination, that governs. Where it does not,
the destination is the one the production deck already carries, and the card
must show that destination's exact story-led title.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
import rdeck
import masters_sl as M
from frames_sl import SETS


def card(n):
    for i, f in enumerate(SETS[n], 1):
        if not f["key"].endswith("_watch_next"):
            continue
        c = rdeck.Card(i, "x.png")
        f["draw"](c)
        lines = [p["text"] for el in c.els if el.get("t") == "text"
                 for p in el["paras"] if p.get("text")]
        dest = [x for x in lines if re.fullmatch(r"Video \d+", x.strip())]
        title = [x for x in lines
                 if x.strip().upper() != "WATCH NEXT" and x not in dest]
        return int(dest[0].split()[1]), " ".join(" ".join(title).split())
    return None, ""


def destination(n):
    d, t = card(n)
    return d, t, "the Watch Next card in the production deck"


def check():
    rows, bad, typo = [], [], []
    for n in M.VIDEOS:
        d, shown = card(n)
        want = M.title(d)
        if shown == want:
            v = "OK"
        elif shown.replace("’", "'") == want.replace("’", "'"):
            v = "TYPOGRAPHY"
            typo.append((n, d))
        else:
            v = "MISMATCH"
            bad.append((n, d, shown, want))
        rows.append((n, d, v, shown, want))
    return rows, bad, typo


if __name__ == "__main__":
    rows, bad, typo = check()
    for n, d, v, shown, want in rows:
        print("%-11s V%-2d -> Video %-2d  %s" % (v, n, d, shown))
        if v != "OK":
            print("%-11s %s story-led title: %s" % ("", " " * 14, want))
    print("\n%d cards, %d mismatches, %d typographic variances"
          % (len(rows), len(bad), len(typo)))
