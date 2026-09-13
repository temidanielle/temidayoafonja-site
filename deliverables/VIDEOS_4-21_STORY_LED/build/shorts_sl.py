# -*- coding: utf-8 -*-
"""The Shorts, audited against the story-led scripts.

A Short is a standalone idea, not a trailer for the long-form structure. It
still follows stop scroll, hold, payoff, one ask. So a Short is not broken
because the long-form reworded a supporting sentence; it is broken when the
framework it rests on is gone, or when its hook is framework-first in a way
the story-led pass moved away from.

Both questions are asked here, and they are asked separately.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_4-21_CORRECTED_RUNTIME/build")
import masters_sl as M
from shorts421 import SHORTS

SUPPORT = 0.75

# The framework term each Short rests on, for the ones whose supporting
# vocabulary drifted. Checked against the story-led script, not assumed.
ANCHOR = {
 "v4_a2_remove_the_title": "title",
 "v4_b1_name_the_gap": "gap",
 "v4_b2_what_it_does_not_guarantee": "choose you",
 "v5_a2_carry": "carry",
 "v5_a3_translate": "translat",
 "v5_a4_prove_the_level": "level",
 "v5_b1_relearn": "relearn",
 "v5_b2_both_directions": "erase your past",
 "v15_b2_not_a_verdict": "not a diagnostic",
 "v16_b1_trusted_vs_considered": "trusted",
 "v19_a3_deliverable": "deliverable",
 "v20_a2_unproven_is_not_absent": "unproven",
 "v20_a4_put_a_date_on_it": "date",
 "v21_a4_easiest_layer_trap": "systems and tooling",
 "v21_b2_read_or_practice": "read",
}


def _words(s):
    return [w for w in re.sub(r"[^a-z0-9 ]+", " ",
                              s.lower().replace("’", "'")).split()
            if len(w) > 3]


def support(n, short):
    txt = " ".join(short["lines"]) if isinstance(short.get("lines"),
                                                 list) else ""
    ws = _words(txt)
    if not ws:
        return 1.0
    script = set(_words(M.spoken_text(n)))
    return 1.0 - len([w for w in ws if w not in script]) / float(len(ws))


def audit(n):
    rows = []
    script = M.spoken_text(n).lower()
    for s in SHORTS[n]:
        ov = support(n, s)
        if ov >= SUPPORT:
            rows.append((s, "REUSE", ov,
                         "The story-led script still carries this Short's "
                         "language. Nothing to change."))
            continue
        anchor = ANCHOR.get(s["slug"])
        held = anchor is not None and anchor in script
        if held:
            rows.append((s, "COPY UPDATE", ov,
                         "The framework this Short rests on is still taught, "
                         "but the story-led script rewords the supporting "
                         "lines, so the Short's wording is brought to the "
                         "current script. The standalone idea is unchanged."))
        else:
            rows.append((s, "REBUILD", ov,
                         "The idea this Short rested on is no longer taught "
                         "in this form."))
    return rows


def all_rows():
    return [(n, r) for n in M.VIDEOS for r in audit(n)]


if __name__ == "__main__":
    from collections import Counter
    rows = all_rows()
    print(dict(Counter(r[1][1] for r in rows)), " total:", len(rows))
    for n, (s, state, ov, why) in rows:
        if state != "REUSE":
            print("  %-12s %.2f V%-2d %s" % (state, ov, n, s["slug"]))
