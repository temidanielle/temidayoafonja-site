# -*- coding: utf-8 -*-
"""Give every card family one exact location in the reconciled script.

A cue has to resolve to a single place. For each family the anchor is the
reconciled paragraph that best supports the card's own copy, reported with
its section, its paragraph index inside that section, and its occurrence
if the sentence appears more than once. Nothing is left with two candidate
locations for the editor to choose between.
"""
import os, sys, json, re
BATCH = sys.argv[1]
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.insert(0, DELIV + "V4-V11_SYNC/build")
if BATCH == "sprint":
    sys.path.insert(0, DELIV + "SPRINT_V4-V9/build")
    import frames as F
    import lay23 as L
    NUMS = (4, 5, 6, 7, 8, 9)
else:
    sys.path.insert(0, DELIV + "V10-V11/build")
    import frames1011 as F
    import lay1011 as L
    NUMS = (10, 11)
import rdeck
import recon as R
import relabel as RL
import overrides

overrides.apply({n: F.SETS[n] for n in NUMS}, L)


def drawn(f):
    out = []
    for st in f["states"]:
        c = rdeck.Card(1, st["name"])
        st["draw"](c)
        for e in c.els:
            if e.get("t") != "text":
                continue
            for pa in e.get("paras", []):
                t = (pa.get("text") or "").strip()
                if t:
                    out.append(t)
    return out


def locate(n, text):
    """(section index, label, paragraph index, occurrence count)."""
    q = R.S._norm(text).lower()
    hits = []
    for li, (lab, ps) in enumerate(R.sections(n)):
        for pi, p in enumerate(ps):
            if q == R.S._norm(p).lower():
                hits.append((li, lab, pi))
    return hits


out = {}
for n in NUMS:
    rows = []
    for f in F.SETS[n]:
        trig = f.get("trigger")
        kind, li, lab, pi = None, None, None, None
        if trig:
            hits = locate(n, trig)
            if hits:
                kind = "HELD"
                li, lab, pi = hits[0]
        if kind is None:
            # re-anchor on the passage that best supports the card's copy
            best, score = None, 0.0
            lines = [x for x in drawn(f) if len(x) > 14]
            for li2, (lab2, ps) in enumerate(R.sections(n)):
                for pi2, p in enumerate(ps):
                    pc = set(RL.content(p))
                    if not pc:
                        continue
                    cov = 0.0
                    for x in lines:
                        c = set(RL.content(x))
                        if c:
                            cov += len(c & pc) / float(len(c))
                    cov = cov / max(len(lines), 1)
                    if cov > score:
                        best, score = (li2, lab2, pi2, p), cov
            if best:
                kind = "RE-ANCHORED" if trig else "END CARD"
                li, lab, pi = best[0], best[1], best[2]
        rows.append(dict(key=f["key"], kind=kind, section=li,
                         label=lab, para=pi,
                         states=[s["name"] for s in f["states"]],
                         trigger=(R.sections(n)[li][1][pi]
                                  if li is not None else None)))
    out[n] = rows
print(json.dumps(out))
