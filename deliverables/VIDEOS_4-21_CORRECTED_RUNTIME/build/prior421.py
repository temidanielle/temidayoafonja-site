# -*- coding: utf-8 -*-
"""The prior-asset audit: what is genuinely reused, and what only looks it.

Three bodies of earlier work exist:

  SEP09_V4_V7   the Videos 4 to 7 handoff package
  SEP09_V8_V13  the Videos 8 to 13 production packages
  SEP10_V14_V21 the September 10 final production packages

A new asset counts as REUSE only when a prior rendered asset exists and the
newly rendered PNG is byte-identical to it. That is the whole test. A similar
visual topic, a similar headline or a shared layout is not reuse, and neither
is a card that was regenerated after its copy changed.

Everything else is reported as what it is: copy updated, rebuilt, new, or a
prior asset that has no successor and is superseded.
"""
import hashlib, os, sys
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import masters421 as M
from frames421 import SETS

DELIV = "/home/user/temidayoafonja-site/deliverables/"
# The packages themselves, in the repository, rather than an extracted copy
# in a temporary directory. The audit has to be reproducible later.
V47 = [DELIV + d for d in (
  "VIDEO_4_How_To_Explain_A_Career_That_Looks_All_Over_The_Place_FINAL",
  "VIDEO_5_Why_Nobody_Can_Tell_What_Youre_Actually_Good_At_FINAL",
  "VIDEO_6_Before_You_Take_An_Internal_Role_FINAL",
  "VIDEO_7_Are_You_Growing_Or_Just_Being_Given_More_Work_FINAL")]

BODIES = [
  ("SEP09_V4_V7", V47,
   "Videos 4 to 7 handoff package, September 9, 2026"),
  ("SEP09_V8_V13", [DELIV + "VIDEOS_8-13_LOCKED_MASTER_BUILD"],
   "Videos 8 to 13 production packages, September 9, 2026"),
  ("SEP10_V14_V21", [DELIV + "VIDEOS_14-21_FINAL_PRODUCTION"],
   "Videos 14 to 21 final production packages, September 10, 2026"),
]


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def index():
    """{sha: [(body, relative path)]} over every prior rendered PNG."""
    out = {}
    for name, roots, _ in BODIES:
        for root in roots:
            if not os.path.isdir(root):
                raise SystemExit("prior body missing: %s" % root)
            base = os.path.dirname(root.rstrip("/"))
            for dirpath, _, files in os.walk(root):
                for fn in files:
                    if not fn.lower().endswith(".png"):
                        continue
                    p = os.path.join(dirpath, fn)
                    out.setdefault(sha(p), []).append(
                        (name, os.path.relpath(p, base)))
    return out


def audit(png_dirs):
    """png_dirs: {video number: directory of the newly rendered PNGs}."""
    prior = index()
    rows = []
    for n in M.VIDEOS:
        for f in SETS[n]:
            p = os.path.join(png_dirs[n], f["key"] + ".png")
            if not os.path.exists(p):
                raise SystemExit("not rendered: %s" % p)
            h = sha(p)
            match = prior.get(h, [])
            rows.append(dict(
                video=n, key=f["key"], declared=f["status"], sha=h,
                identical=bool(match),
                matched=match[0] if match else None,
                why=f["why"]))
    return rows, prior


def contradictions(rows):
    """A declared status that the bytes do not support, in either direction."""
    out = []
    for r in rows:
        if r["declared"] == "REUSE" and not r["identical"]:
            out.append((r["video"], r["key"],
                        "declared REUSE but no prior rendered asset is "
                        "byte-identical"))
        if r["declared"] in ("NEW",) and r["identical"]:
            out.append((r["video"], r["key"],
                        "declared NEW but is byte-identical to %s/%s"
                        % r["matched"]))
    return out


def superseded(rows, prior):
    """Prior rendered assets with no byte-identical successor in this build."""
    kept = {r["sha"] for r in rows if r["identical"]}
    out = []
    for h, places in sorted(prior.items(), key=lambda kv: kv[1][0]):
        if h in kept:
            continue
        for body, rel in places:
            out.append((body, rel, h))
    return out
