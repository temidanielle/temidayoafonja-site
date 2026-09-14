# -*- coding: utf-8 -*-
"""Employer identity in the public-facing layer, read off the drawn card.

Card copy reaches the canvas through closures, so scanning the frame
definitions misses it. This draws every state and walks the element tree
for text that actually renders, which is the only reliable audit.
"""
import os, sys, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/VIDEOS_22-23/build")
import rdeck
import frames as F
import sprint as S
from qa23 import units

# Employer identities that must not reach the public teaching layer.
EMPLOYERS = ("GiveDirectly", "Give Directly", "HCSC",
             "Health Care Service Corporation", "Health Care Service",
             "Zeta Global", "Patriot Growth Insurance Services",
             "Patriot Growth", "xAI")
URLS = ("givedirectly.org", "zetaglobal.com", "hcsc.com", "x.ai",
         "patriotgrowth.com")
RX = re.compile(r"(?<![A-Za-z])(%s)(?![A-Za-z])"
                % "|".join(re.escape(x) for x in EMPLOYERS + URLS), re.I)


def drawn_text(el, out):
    """Every string this element renders."""
    if isinstance(el, dict):
        for k, v in el.items():
            if k == "text" and isinstance(v, str):
                out.append(v)
            elif k in ("paras", "lines", "rows", "items", "cells"):
                drawn_text(v, out)
            elif isinstance(v, (dict, list, tuple)):
                drawn_text(v, out)
    elif isinstance(el, (list, tuple)):
        for x in el:
            drawn_text(x, out)
    return out


def state_text(st):
    c = rdeck.Card(1, st["name"])
    st["draw"](c)
    return drawn_text(c.els, [])


def scan(n):
    """(state name, employer found, the line it appears in)."""
    hits = []
    for f in F.SETS[n]:
        for st in f["states"]:
            for t in state_text(st):
                for m in RX.finditer(t):
                    hits.append((st["name"], m.group(0), t.strip()[:70]))
            # the filename is public too: it is printed in the Asset Index
            for m in RX.finditer(st["name"]):
                hits.append((st["name"], m.group(0), "IN THE FILENAME"))
    return hits


if __name__ == "__main__":
    total = 0
    for n in S.VIDEOS:
        hits = scan(n)
        if not hits:
            continue
        total += len(hits)
        print("=== NEW V%d: %d employer references on cards ===" % (n,
                                                                    len(hits)))
        for name, who, line in hits:
            print("  %-36s %-14s %s" % (name, who, line))
    print("\ntotal employer references drawn on public cards: %d" % total)

    print("\n=== spoken streams ===")
    sp = 0
    for n in S.VIDEOS:
        for i, p in enumerate(S.paragraphs(n)):
            for m in RX.finditer(p):
                print("  NEW V%d paragraph %d: %s" % (n, i, m.group(0)))
                sp += 1
    print("  %d spoken employer references" % sp)

    print("\n=== Shorts ===")
    sh = 0
    for n in S.VIDEOS:
        for s in S.shorts(n):
            for m in RX.finditer(s["hook"] + " " + s["body"] + " " + s["ask"]):
                print("  NEW V%d Short %s: %s" % (n, s["num"], m.group(0)))
                sh += 1
    print("  %d employer references in Shorts" % sh)
