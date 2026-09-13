# -*- coding: utf-8 -*-
"""The camera and full-screen spine of each video, in spoken order.

A map that lists only graphics cannot show where the camera-led moments are,
so this walks the whole script and marks every stretch. Each card is anchored
to the first spoken occurrence of its trigger and is cued once, which QA
checks rather than assumes.
"""
import masters23 as M
import frames23 as F


def spine(n):
    """[(kind, ...)] over the whole script: SECTION, CAMERA, FRAME."""
    cue = {}
    for f in F.SETS[n]:
        q = M._norm(f["trigger"])
        placed = False
        for li, (mk, label, ps) in enumerate(M.sections(n)):
            for pi, p in enumerate(ps):
                if q == M._norm(p):
                    cue.setdefault((li, pi), []).append(f)
                    placed = True
                    break
            if placed:
                break
    out = []
    for li, (mk, label, ps) in enumerate(M.sections(n)):
        out.append(("SECTION", mk, label))
        run = []
        for pi, p in enumerate(ps):
            if (li, pi) in cue:
                if run:
                    out.append(("CAMERA", run))
                    run = []
                for f in cue[(li, pi)]:
                    out.append(("FRAME", f, p))
            else:
                run.append(p)
        if run:
            out.append(("CAMERA", run))
    return out


def counts(n):
    s = spine(n)
    return (sum(1 for x in s if x[0] == "CAMERA"),
            sum(1 for x in s if x[0] == "FRAME"))


def placements(n):
    return [x[1]["key"] for x in spine(n) if x[0] == "FRAME"]


if __name__ == "__main__":
    for n in M.VIDEOS:
        cam, full = counts(n)
        pl = placements(n)
        print("V%d  %d camera stretches  %d full-screen cues  %d cards"
              % (n, cam, full, len(F.SETS[n])))
        dup = sorted({k for k in pl if pl.count(k) > 1})
        print("    cued more than once:", dup or "none")
        print("    never cued:",
              [f["key"] for f in F.SETS[n] if f["key"] not in pl] or "none")
