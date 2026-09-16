# -*- coding: utf-8 -*-
"""Audit the three candidate Shorts per video against the reconciled source.

A Short may only carry approved spoken wording. Every line of every
existing candidate is checked sentence by sentence against the reconciled
master. A line that is no longer in the master has to be replaced from
approved wording, never invented.
"""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R

BATCH = sys.argv[1] if len(sys.argv) > 1 else None
DELIV = "/home/user/temidayoafonja-site/deliverables/"


def load(batch):
    if batch == "sprint":
        sys.path.insert(0, DELIV + "SPRINT_V4-V9/build")
        import sprint as S
        return {n: [dict(num=s["num"], lines=_split(s["hook"])
                         + _split(s["body"]) + _split(s["ask"]))
                    for s in S.shorts(n)] for n in (4, 5, 6, 7, 8, 9)}
    sys.path.insert(0, DELIV + "V10-V11/build")
    import shorts1011 as SH
    return {n: [dict(num=r["num"], lines=r["stop"] + r["hold"] + r["ask"])
                for r in SH.rows(n)] for n in (10, 11)}


def _split(t):
    return [x.strip() for x in re.split(r"(?<=[.?!”])\s+", t or "")
            if x.strip()]


if __name__ == "__main__":
    data = load(BATCH)
    out = {}
    for n, shorts in data.items():
        body = R.S._norm(R.spoken_text(n)).lower()
        rows = []
        for s in shorts:
            gone = [l for l in s["lines"]
                    if R.S._norm(l).lower() not in body]
            rows.append(dict(num=s["num"], lines=len(s["lines"]),
                             gone=gone))
        out[n] = rows
    print(json.dumps(out))
