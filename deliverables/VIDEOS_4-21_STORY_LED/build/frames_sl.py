# -*- coding: utf-8 -*-
"""The story-led visual asset set for Videos 4 to 21.

Built at import time from the pre-story-led set plus the re-anchoring in
genframes_sl, so the drawing code for every carried card stays the single
copy it always was and cannot drift from the version that was rendered and
approved. What this module adds is the story-led cue, the classification and
the delivery mode.

MODE says who carries the moment:

  CAMERA      Temidayo on camera. A recognition moment, a lived experience,
              a reflective transition, or bringing it back to the viewer
  FULL SCREEN a framework, comparison, decision test, distinction, worked
              artifact or proof structure the viewer now needs to see
  CALLOUT     a short overlay on an otherwise camera-led moment
  B-ROLL      substantive full-screen footage
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
import masters_sl as M
import genframes_sl
from handmap_sl import DROP

SETS = {}
for _n, _seq in genframes_sl.build():
    out = []
    for _s in _seq:
        _o = _s["old"]
        _f = dict(_o)
        _f["key"] = _s["src"]
        _f["trigger"] = _s["trigger"]
        _f["status"] = _s["status"]
        _f["why"] = _s["why"]
        _f["mode"] = _s["mode"] or _o.get("mode", "FULL SCREEN")
        out.append(_f)
    SETS[_n] = out

REMOVED = dict(DROP)


def section_of(n, trigger):
    """Which story-led section a cue lands in."""
    q = M._norm(trigger)
    for label, ps in M.sections(n):
        if any(q in M._norm(p) for p in ps):
            return label
    return None


def position(n, trigger):
    """How far into the spoken script the cue lands, 0 to 1."""
    q = M._norm(trigger)
    ps = M.paragraphs(n)
    words = 0
    total = M.word_count(n)
    for p in ps:
        if q in M._norm(p):
            return words / float(total)
        words += len(p.split())
    return 1.0


if __name__ == "__main__":
    from collections import Counter
    print(Counter(f["status"] for n in SETS for f in SETS[n]),
          " removed:", len(REMOVED))
    print("frames per video:", {n: len(SETS[n]) for n in sorted(SETS)})
    bad = [(n, f["key"]) for n in M.VIDEOS for f in SETS[n]
           if not M.trigger_ok(n, f["trigger"])]
    print("trigger misses:", len(bad))
    early = [(n, f["key"], round(position(n, f["trigger"]), 2))
             for n in M.VIDEOS for f in SETS[n]
             if position(n, f["trigger"]) < 0.06]
    print("\ncues landing in the first 6 percent of the script, where a "
          "graphic risks covering the opening scene:")
    for n, k, p in early:
        print("   V%-2d %-36s at %.0f%%  [%s]" % (n, k, p * 100,
              section_of(n, [f for f in SETS[n] if f["key"] == k][0]["trigger"])))
