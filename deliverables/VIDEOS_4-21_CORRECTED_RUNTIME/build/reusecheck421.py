# -*- coding: utf-8 -*-
"""Verify that every frame's drawn copy is supported by the corrected master.

A frame is not REUSE because its topic sounds similar. It is REUSE only when
the copy on the card is still the copy the corrected script supports. This
check pulls the actual text out of each rendered Card and measures how much of
its distinctive vocabulary appears in the corrected spoken script.

Low overlap is not proof of a defect. It is a reading list: every frame below
the threshold is read against the master by hand before its status stands.
Words that are house furniture rather than content are excluded, so a card
cannot pass on its eyebrow and its call to action alone.
"""
import os, re, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import rdeck
import masters421 as M
from frames421 import SETS

THRESHOLD = 0.60

STOP = set("""a an and are as at be been but by can could did do does for from
had has have he her here his how i if in is it its me my no not of on one only
or our out she so some than that the their them then there these they this
those to up was we were what when where which who will with would you your
about after all also any because before both did does doing down during each
few more most other over same such too very just now into under again""".split())

# House furniture. Present on many cards, says nothing about the script.
FURNITURE = set("""capability formation video temidayo afonja watch next
comment comments subscribe channel link below""".split())


def card_text(n, i, f):
    c = rdeck.Card(i, f["key"] + ".png")
    f["draw"](c)
    out = []
    for el in c.els:
        if el.get("t") == "text":
            out += [p["text"] for p in el["paras"] if p.get("text")]
    return " ".join(out)


def words(s):
    ws = re.findall(r"[a-z0-9']+", s.lower().replace("’", "'"))
    return [w for w in ws if w not in STOP and w not in FURNITURE and len(w) > 2]


def overlap(n, text):
    script = set(words(M.spoken_text(n)))
    ws = words(text)
    if not ws:
        return 1.0, []
    miss = [w for w in ws if w not in script]
    return 1.0 - len(miss) / float(len(ws)), sorted(set(miss))


def audit():
    rows = []
    for n in M.VIDEOS:
        for i, f in enumerate(SETS[n], 1):
            t = card_text(n, i, f)
            score, miss = overlap(n, t)
            rows.append((n, f["key"], f["status"], score, miss, t))
    return rows


def main():
    rows = audit()
    low = [r for r in rows if r[3] < THRESHOLD]
    for n, key, status, score, miss, t in sorted(low, key=lambda r: r[3]):
        print("%.2f  %-34s %-22s" % (score, key, status))
        print("       card: %s" % t[:190].replace("\n", " "))
        print("       not in script: %s" % ", ".join(miss[:14]))
    print("\n%d frames, %d below %.2f overlap with the corrected script"
          % (len(rows), len(low), THRESHOLD))
    reuse_low = [r for r in low if r[2] == "REUSE"]
    print("%d of those are currently marked REUSE" % len(reuse_low))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
