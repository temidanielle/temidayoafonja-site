# -*- coding: utf-8 -*-
"""Verify the NEW V6 reuse claims against the former V22 package's bytes.

NEW V6 is the former V22, re-sequenced. Where the sprint script still teaches
the same thing, the card is reused. A family is only REUSE if every state
renders byte for byte identical to the file the locked V22 package shipped,
which is measured rather than asserted.
"""
import os, sys, hashlib, shutil, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.insert(0, HERE)
sys.path.append(DELIV + "riverside-build")
from rdeck import render_html, shoot
import sprint as S
import frames as F
import geocheck as G

PRIOR = os.path.join(DELIV, "VIDEOS_22-23", "V22_v3", "04_Visual_Assets")
# Three cards were renamed when they moved into the sprint. The card is the
# same; only the filename changed, so the alias is declared and the bytes are
# still what decides whether it is reuse.
ALIAS = {
 "NEW_V6_FS_08_READ_THE_VERBS": "V22_FS_08_RULE01_READ_THE_VERBS",
 "NEW_V6_FS_15B_IN_THE_SAMPLE": "V22_FS_15B_IN_THIS_SAMPLE",
 "NEW_V6_FS_16_READ_THE_WORK": "V22_FS_16_RULE02_READ_THE_WORK",
}


def former_name(name):
    return ALIAS.get(name, name.replace("NEW_V6_FS_", "V22_FS_", 1))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def check(n=6):
    tmp = tempfile.mkdtemp()
    try:
        cards, names = G.cards_for(n)
        html = render_html(cards, os.path.join(tmp, "v.html"), "v")
        made = {os.path.basename(p): p for p in shoot(html, tmp, names)}
        rows = []
        for f in F.SETS[n]:
            if f["cls"] != F.REUSE:
                continue
            same, diff, missing = [], [], []
            for st in f["states"]:
                old = os.path.join(PRIOR, former_name(st["name"]) + ".png")
                if not os.path.exists(old):
                    missing.append(former_name(st["name"]))
                elif sha256(old) == sha256(made[st["name"] + ".png"]):
                    same.append(st["name"])
                else:
                    diff.append(st["name"])
            ok = not diff and not missing
            rows.append((f["key"], ok,
                         "all %d states byte-identical to the former V22 "
                         "package" % len(same) if ok else
                         "differs: %s; missing: %s" % (diff or "none",
                                                       missing or "none")))
        return rows
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    rows = check()
    bad = [r for r in rows if not r[1]]
    for k, ok, det in rows:
        print("  %-44s %s  %s" % (k, "REUSE " if ok else "FAILED", det))
    print("\n  %d families claim reuse, %d unverified" % (len(rows),
                                                          len(bad)))
