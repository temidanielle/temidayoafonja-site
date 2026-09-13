# -*- coding: utf-8 -*-
"""Re-anchor the existing visual assets to the story-led scripts.

An asset is not rebuilt because its trigger sentence was reworded. Most of
these visuals still teach exactly what the new script teaches; what moved is
the sentence they land on. So for every existing asset this finds the
sentence in the story-led script that its old trigger became, and reports
what could not be found.

Matching is on the trigger's own words against every spoken paragraph, and
the score is reported so a weak match is visible rather than silently
accepted.
"""
import difflib, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
import masters_sl as M
from frames421 import SETS as OLD

STRONG = 0.72      # the same sentence, lightly reworded
WEAK = 0.45        # recognizably the same moment, materially rewritten


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ",
                  s.lower().replace("’", "'")).split()


def sentences(n):
    """Every spoken sentence, with the paragraph it belongs to."""
    out = []
    for p in M.paragraphs(n):
        for s in re.split(r"(?<=[.?!])\s+", p):
            s = s.strip()
            if len(s.split()) >= 4:
                out.append((s, p))
    return out


def best(n, trigger):
    """(sentence, paragraph, score) for the closest sentence in the script."""
    t = norm(trigger)
    top = (None, None, 0.0)
    for s, p in sentences(n):
        r = difflib.SequenceMatcher(None, t, norm(s)).ratio()
        if r > top[2]:
            top = (s, p, r)
    # A long trigger may now be split across sentences; try the paragraph.
    for p in M.paragraphs(n):
        r = difflib.SequenceMatcher(None, t, norm(p)).ratio()
        if r > top[2]:
            top = (p, p, r)
    return top


def audit(n):
    rows = []
    for i, f in enumerate(OLD[n], 1):
        alive = M.trigger_ok(n, f["trigger"])
        if alive:
            rows.append(dict(key=f["key"], order=i, state="ALIVE",
                             trigger=f["trigger"], score=1.0,
                             new_trigger=f["trigger"]))
            continue
        s, p, r = best(n, f["trigger"])
        state = ("RETRIGGER" if r >= STRONG else
                 "MOMENT MOVED" if r >= WEAK else "GONE")
        rows.append(dict(key=f["key"], order=i, state=state,
                         trigger=f["trigger"], score=r, new_trigger=s))
    return rows


if __name__ == "__main__":
    from collections import Counter
    tally = Counter()
    for n in M.VIDEOS:
        rows = audit(n)
        tally.update(r["state"] for r in rows)
        bad = [r for r in rows if r["state"] != "ALIVE"]
        if not bad:
            continue
        print("=== V%d" % n)
        for r in bad:
            print("  %-13s %.2f  %s" % (r["state"], r["score"], r["key"]))
            print("        was: %s" % r["trigger"][:96])
            print("        now: %s" % (r["new_trigger"] or "")[:96])
    print()
    print(dict(tally))
