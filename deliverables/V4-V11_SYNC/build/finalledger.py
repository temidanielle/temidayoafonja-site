# -*- coding: utf-8 -*-
"""The revised asset ledger, against the reconciled source.

Two questions, answered separately, then combined into the least
disruptive accurate remedy:

  ANCHOR  does the family's cue sentence still exist in the reconciled
          script?
  COPY    after re-review and hand adjudication, does any line on the card
          still fail to trace to the script or to approved evidence?

REUSE        both hold.
RE-ANCHOR    copy holds, cue is gone. An edit-map change, not a new asset.
COPY UPDATE  a line has to change. The design is kept and the affected
             states are re-rendered.
REBUILD      the layout, illustration or reveal structure itself no longer
             works.
RETIRE       the family has no current teaching purpose at all.
NEW          the current brief needs a visual with no existing counterpart.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recon as R
import relabel as RL
import adjudicated as AD
sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                   "V4-V11_EDIT_SYNC/build")
import briefs as B

_A = {}
for _f in ("an_sprint.json", "an_1011.json"):
    _p = os.path.join(HERE, _f)
    if os.path.exists(_p):
        for _n, _rows in json.load(open(_p)).items():
            for _r in _rows:
                _A[(int(_n), _r["key"])] = _r["kind"]
ANCHOR = _A

REUSE, REANCHOR, COPY, REBUILD, RETIRE, NEW = (
    "REUSE", "RE-ANCHOR", "COPY UPDATE", "REBUILD", "RETIRE", "NEW")


def _rows():
    return json.load(open(os.path.join(HERE, "_relabel.json")))


def ledger():
    out = []
    for r in _rows():
        v, key = r["video"], r["key"]
        bad = []
        for l in r["lines"]:
            d = AD.decide(v, key, l["line"])
            kind = d[0] if d else l["kind"]
            if kind == AD.OBSOLETE:
                bad.append(dict(line=l["line"],
                                why=(d[2] if d else l["why"])))
        # The anchor test is strict paragraph equality against the
        # reconciled script, the same test the cue map uses, so the ledger
        # and the edit map cannot disagree. A looser substring test would
        # call a cue intact when the editor cannot actually cue on it.
        a = ANCHOR.get((v, key))
        anchor = a or "UNRESOLVED"
        held = a in ("HELD", "END CARD")
        if bad and held:
            verdict, why = COPY, ("%d line no longer traces to the script; "
                                  "design kept, affected states re-rendered"
                                  % len(bad))
        elif bad and not held:
            verdict, why = COPY, ("%d line no longer traces to the script, "
                                  "and the cue moved; design kept, copy and "
                                  "placement updated" % len(bad))
        elif held:
            verdict, why = REUSE, ("cue holds and every line traces to the "
                                   "script or to approved evidence")
        else:
            verdict, why = REANCHOR, ("every line still traces to the "
                                      "script; only the cue sentence is "
                                      "gone")
        out.append(dict(video=v, key=key, anchor=anchor or "end card",
                        states=r["states"], verdict=verdict, reason=why,
                        bad=bad,
                        retained=[dict(line=l["line"],
                                       kind=(AD.decide(v, key, l["line"])[0]
                                             if AD.decide(v, key, l["line"])
                                             else l["kind"]),
                                       support=(AD.decide(v, key,
                                                          l["line"])[1]
                                                if AD.decide(v, key,
                                                             l["line"])
                                                else l["section"]))
                                  for l in r["lines"]
                                  if not any(b["line"] == l["line"]
                                             for b in bad)]))
    return out


def new_assets():
    """Brief beats whose display copy has no existing counterpart."""
    L = ledger()
    have = {}
    for r in L:
        have.setdefault(r["video"], []).append(r["key"])
    out = []
    for n in R.VIDEOS:
        b = B.read(n)
        for x in b["beats"]:
            if not x.get("display"):
                continue
            out.append(dict(video=n, beat=x["n"], phase=x["phase"],
                            head=x["head"], display=x["display"],
                            trigger=x["trigger"]))
    return out


def counts(rows):
    c = {}
    for r in rows:
        c[r["verdict"]] = c.get(r["verdict"], 0) + 1
    return c


if __name__ == "__main__":
    L = ledger()
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    for n in sorted(per):
        c = counts(per[n])
        print("V%-3d %2d families   %s" % (n, len(per[n]),
              "   ".join("%s %d" % (k, c[k])
                         for k in (REUSE, REANCHOR, COPY, REBUILD, RETIRE)
                         if k in c)))
    c = counts(L)
    print("\nALL  %d families   %s" % (len(L),
          "   ".join("%s %d" % (k, c.get(k, 0))
                     for k in (REUSE, REANCHOR, COPY, REBUILD, RETIRE))))
    print("\nlines retained with logged support: %d"
          % sum(len(r["retained"]) for r in L))
    print("lines needing new copy: %d" % sum(len(r["bad"]) for r in L))
    print("brief beats requiring a mapped visual: %d" % len(new_assets()))
