# -*- coding: utf-8 -*-
"""Audit one batch's existing cards against the September 16 scripts.

Run per batch in its own process: the sprint and V10-V11 builds each import
their own parser module and cannot share an interpreter.

For every card family this answers two separate questions, and never
conflates them:

  ANCHOR   does the exact trigger sentence still exist in the new script?
  COPY     does every word drawn on the card still exist in the new script?

A family can keep its anchor and still need new copy, or keep its copy and
need a new anchor. The ledger records both.
"""
import os, sys, json, re

BATCH = sys.argv[1]
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "riverside-build")
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.insert(0, DELIV + "V4-V11_EDIT_SYNC/build")
if BATCH == "sprint":
    sys.path.insert(0, DELIV + "SPRINT_V4-V9/build")
    import frames as F
    NUMS = (4, 5, 6, 7, 8, 9)
else:
    sys.path.insert(0, DELIV + "V10-V11/build")
    import frames1011 as F
    NUMS = (10, 11)
import src916 as NEW
import rdeck


def drawn(st):
    c = rdeck.Card(1, st["name"])
    st["draw"](c)
    out = []
    for e in c.els:
        if e.get("t") != "text":
            continue
        for pa in e.get("paras", []):
            t = (pa.get("text") or "").strip()
            if t:
                out.append(t)
    return out


def norm(t):
    return NEW._norm(t).lower()


# The visual system has two tiers and they are judged differently.
#
# The label tier is editorial display copy: eyebrows, column labels,
# connectives, the small all-capitals headings above a card. It was never
# required to be verbatim speech, and the September 16 briefs confirm that
# by supplying display copy of their own.
#
# The body tier is teaching copy. Under the standing rule, every word of it
# has to be the script's own, so a body line that no longer exists in the
# current script is a genuine copy defect.
FURNITURE = re.compile(r"^(vs\.?|and|\+|[0-9]+)$", re.I)


def is_label(line):
    s = line.strip()
    letters = [c for c in s if c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters) and len(s) < 70


def in_script(n, line):
    body = norm(NEW.spoken_text(n))
    return norm(line) in body


rows = []
for n in NUMS:
    body = norm(NEW.spoken_text(n))
    for f in F.SETS[n]:
        trig = f.get("trigger")
        anchor = None
        if trig:
            anchor = "HELD" if norm(trig) in body else "LOST"
        miss, lab = [], []
        for st in f["states"]:
            for line in drawn(st):
                if FURNITURE.match(line.strip()):
                    continue
                if norm(line) in body:
                    continue
                (lab if is_label(line) else miss).append(line[:70])
        rows.append(dict(video=n, key=f["key"], anchor=anchor,
                         states=len(f["states"]),
                         treatment=f.get("treatment"),
                         missing=sorted(set(miss)),
                         labels=sorted(set(lab))))
print(json.dumps(rows))
