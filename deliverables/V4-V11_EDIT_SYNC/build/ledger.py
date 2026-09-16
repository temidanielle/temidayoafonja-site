# -*- coding: utf-8 -*-
"""The reuse / re-anchor / copy-update / rebuild ledger, with reasons.

Two independent questions are asked of every existing card family and never
conflated:

  ANCHOR  does its exact trigger sentence still exist in the current
          September 16 script?
  COPY    does every word of its teaching copy still exist there?

The editorial label tier, the small all-capitals headings and column
labels, is judged separately: it was never required to be verbatim speech,
and the September 16 briefs supply display copy of their own.

A family keeping both gets REUSE. Losing only the anchor gets RE-ANCHOR,
which is an edit-map change and not a new asset. Losing body copy gets
COPY UPDATE, which does need the card redrawn. Losing both gets REBUILD.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_ledger.json")

REUSE = "REUSE"
REANCHOR = "RE-ANCHOR"
COPY = "COPY UPDATE"
REBUILD = "REBUILD"


def rows(refresh=False):
    if not refresh and os.path.exists(CACHE):
        return json.load(open(CACHE))
    out = []
    for batch in ("sprint", "v1011"):
        r = subprocess.check_output(
            [sys.executable, os.path.join(HERE, "audit_one.py"), batch],
            cwd=HERE)
        out += json.loads(r.decode())
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


def classify(r):
    anchor_ok = r["anchor"] in ("HELD", None)
    copy_ok = not r["missing"]
    if anchor_ok and copy_ok:
        return REUSE, ("trigger still in the script and every word of the "
                       "teaching copy still traces to it"
                       if r["anchor"] else
                       "end card, no trigger, copy unchanged")
    if anchor_ok and not copy_ok:
        return COPY, ("trigger holds, but %d teaching line%s no longer "
                      "appear%s in the current script"
                      % (len(r["missing"]),
                         "" if len(r["missing"]) == 1 else "s",
                         "s" if len(r["missing"]) == 1 else ""))
    if not anchor_ok and copy_ok:
        return REANCHOR, ("teaching copy still traces to the script, but the "
                          "cue sentence is gone: the card is fine, its "
                          "placement is not")
    return REBUILD, ("the cue sentence is gone and %d teaching line%s no "
                     "longer appear in the current script"
                     % (len(r["missing"]),
                        "" if len(r["missing"]) == 1 else "s"))


def ledger(refresh=False):
    out = []
    for r in rows(refresh):
        cls, why = classify(r)
        out.append(dict(r, verdict=cls, reason=why))
    return out


def counts(rows_):
    c = {}
    for r in rows_:
        c[r["verdict"]] = c.get(r["verdict"], 0) + 1
    return c


if __name__ == "__main__":
    L = ledger("--refresh" in sys.argv)
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    for n in sorted(per):
        c = counts(per[n])
        print("V%-3d %2d families   %s" % (n, len(per[n]),
              "   ".join("%s %d" % (k, c[k])
                         for k in (REUSE, REANCHOR, COPY, REBUILD)
                         if k in c)))
    c = counts(L)
    print("\nALL  %d families   %s" % (len(L),
          "   ".join("%s %d" % (k, c.get(k, 0))
                     for k in (REUSE, REANCHOR, COPY, REBUILD))))
