# -*- coding: utf-8 -*-
"""Compare a new card's copy to the prior batch's card copy, not its pixels.

Byte identity answers one question: is the delivered file the same file?
It cannot answer the other one, which is whether the words changed, because
the three earlier batches were drawn by three different layout modules. The
same sentence rendered by lay813 and by lay421 produces two different PNGs.

So a REUSE claim is tested twice:

  IDENTICAL  the newly rendered PNG is byte-identical to the prior file
  SAME COPY  the words on the card are unchanged, but this build rendered
             them, so the bytes differ

Anything that is neither had its copy changed and is not reuse under any
reading.
"""
import os, re, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_8-13_LOCKED_MASTER_BUILD/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "VIDEOS_14-21_FINAL_PRODUCTION/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "new-videos-4-5-swap/build")
sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                "new-videos-6-7/build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import rdeck
import masters421 as M
from frames421 import SETS


def _text(draw):
    c = rdeck.Card(1, "x.png")
    draw(c)
    return " ".join(p["text"] for el in c.els if el.get("t") == "text"
                    for p in el["paras"] if p.get("text"))


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def prior_texts():
    """{video: [prior card copy, in order]} across all four earlier batches.

    Every batch is required to load. A batch that fails to import would make
    its videos look like they had no prior copy, and every card in them would
    then be reported as changed, which is the wrong answer arrived at
    quietly. So an import failure stops the run.
    """
    out = {}
    try:
        import frames as F45
        for n, fs in F45.SETS.items():
            out[n] = [_text(f["draw"]) for f in fs]
    except Exception as e:
        raise SystemExit("cannot read the V4 and V5 frames: %s" % e)
    try:
        import frames67 as F67
        for n, fs in F67.SETS.items():
            out[n] = [_text(f["draw"]) for f in fs]
    except Exception as e:
        raise SystemExit("cannot read the V6 and V7 frames: %s" % e)
    try:
        import frames813
        for n, fs in frames813.SETS.items():
            out[n] = [_text(f["draw"]) for f in fs]
    except Exception as e:
        raise SystemExit("cannot read the V8 to V13 frames: %s" % e)
    try:
        import frames1421
        for n, fs in frames1421.SETS.items():
            out[n] = [_text(f["draw"]) for f in fs]
    except Exception as e:
        raise SystemExit("cannot read the V14 to V21 frames: %s" % e)
    return out


def classify(identical_keys):
    """(video, key, verdict) for every asset.

    identical_keys: the set of keys whose rendered PNG is byte-identical to a
    prior rendered file, as established by prior421.
    """
    prior = prior_texts()
    rows = []
    for n in M.VIDEOS:
        pool = [norm(t) for t in prior.get(n, [])]
        for f in SETS[n]:
            t = norm(_text(f["draw"]))
            if f["key"] in identical_keys:
                v = "IDENTICAL"
            elif pool and t in pool:
                v = "SAME COPY"
            else:
                v = "CHANGED"
            rows.append((n, f["key"], f["status"], v))
    return rows
