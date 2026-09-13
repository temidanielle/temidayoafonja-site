# -*- coding: utf-8 -*-
"""The camera and full-screen spine of each video, in spoken order.

Each card is anchored to the first spoken occurrence of its trigger and cued
once, which QA checks rather than assumes. The new scripts carry section
labels and no timing markers, so nothing here can be mistaken for a runtime.
"""
import masters23b as M
import frames23b as F


def spine(n):
    """[(kind, ...)] over the whole script: SECTION, CAMERA, FRAME."""
    cue = {}
    for f in F.SETS[n]:
        q = M._norm(f["trigger"])
        placed = False
        for li, (label, ps) in enumerate(M.sections(n)):
            for pi, p in enumerate(ps):
                if q == M._norm(p):
                    cue.setdefault((li, pi), []).append(f)
                    placed = True
                    break
            if placed:
                break
    out = []
    for li, (label, ps) in enumerate(M.sections(n)):
        out.append(("SECTION", li + 1, label))
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
        print("V%d  %d camera stretches  %d full-screen cues  %d families"
              % (n, cam, full, len(F.SETS[n])))
        print("    cued more than once:",
              sorted({k for k in pl if pl.count(k) > 1}) or "none")
        print("    never cued:",
              [f["key"] for f in F.SETS[n] if f["key"] not in pl] or "none")
        print("    words on camera: %d of %d"
              % (sum(len(p.split()) for x in spine(n) if x[0] == "CAMERA"
                     for p in x[1]), M.word_count(n)))
