# -*- coding: utf-8 -*-
"""The camera and full-screen spine of each sprint video, in spoken order."""
import sprint as S
import frames as F


def spine(n):
    cue = {}
    for f in F.SETS[n]:
        if not f["trigger"]:
            continue
        q = S._norm(f["trigger"])
        placed = False
        for li, (label, ps) in enumerate(S.sections(n)):
            for pi, p in enumerate(ps):
                if q == S._norm(p):
                    cue.setdefault((li, pi), []).append(f)
                    placed = True
                    break
            if placed:
                break
    out = []
    for li, (label, ps) in enumerate(S.sections(n)):
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
    cam = sum(1 for x in s if x[0] == "CAMERA")
    full = sum(1 for x in s if x[0] == "FRAME")
    return cam, full


def placements(n):
    return [x[1]["key"] for x in spine(n) if x[0] == "FRAME"]


def on_camera_words(n):
    return sum(len(p.split()) for x in spine(n) if x[0] == "CAMERA"
               for p in x[1])


if __name__ == "__main__":
    for n in S.VIDEOS:
        cam, full = counts(n)
        pl = placements(n)
        cued = set(pl)
        never = [f["key"] for f in F.SETS[n]
                 if f["trigger"] and f["key"] not in cued]
        print("NEW V%d (former V%d)  %2d camera stretches  %2d full-screen "
              "cues  %3d of %3d words on camera"
              % (n, S.NUMBERS[n], cam, full, on_camera_words(n),
                 S.word_count(n)))
        print("     cued twice:", sorted({k for k in pl if pl.count(k) > 1})
              or "none", "  never cued:", never or "none")
