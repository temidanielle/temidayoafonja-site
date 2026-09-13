# -*- coding: utf-8 -*-
"""Verify each asset's reuse class against the previous package's bytes.

A card is only REUSE if it renders byte for byte identical to the file the
first package shipped. Anything else is COPY UPDATE, REBUILD or NEW, and a
family that claims REUSE but renders differently is a failure, not a nuance.
"""
import os, re, sys, hashlib, shutil, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.append("/home/user/temidayoafonja-site/deliverables/riverside-build")
from rdeck import render_html, shoot
import masters23b as M
import frames23b as F
import geocheck23b as G

PREV = {n: os.path.join(OUT, "V%d" % n, "04_Visual_Assets")
        for n in M.VIDEOS}


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def render_all(n, outdir):
    cards, names = G.cards_for(n)
    html = render_html(cards, os.path.join(outdir, "_v%d.html" % n),
                       "V%d" % n)
    made = shoot(html, outdir, names)
    os.remove(html)
    return {os.path.basename(p): p for p in made}


FAM = re.compile(r"^(V2[23]_FS_\d+)[A-Z]?_")

# The layout function a card is drawn with. REBUILD means the design changed,
# which is a different question from a file being renamed or its copy edited,
# so it is measured by watching which layout each family actually calls.
LAYOUTS = ("artifact", "hotspot_artifact", "framework", "sequence", "lines",
           "questions", "compare", "twopart", "stat", "rule_card", "action",
           "claim_card", "statement", "watch_next")


def layouts_used(family_states):
    import lay23
    seen = []
    orig = {k: getattr(lay23, k) for k in LAYOUTS}

    def wrap(name, fn):
        def inner(*a, **kw):
            seen.append(name)
            return fn(*a, **kw)
        return inner
    for k, fn in orig.items():
        setattr(lay23, k, wrap(k, fn))
    try:
        import rdeck
        for st in family_states:
            st["draw"](rdeck.Card(1, "probe"))
    finally:
        for k, fn in orig.items():
            setattr(lay23, k, fn)
    return tuple(sorted(set(seen)))


def family(name):
    m = FAM.match(name)
    return m.group(1) if m else name


def old_files(n):
    """Previous package PNGs, grouped by family number.

    A family that was renamed still belongs to its number, so renaming a rule
    card is measured as a copy update rather than reported as a new asset.
    """
    d, out = PREV[n], {}
    if not os.path.isdir(d):
        return out
    for nm in sorted(os.listdir(d)):
        if nm.endswith(".png"):
            out.setdefault(family(nm[:-4]), []).append(os.path.join(d, nm))
    return out


def _old_layouts():
    """Which layout each previous family was drawn with."""
    import importlib
    prev = importlib.import_module("frames23")
    out = {}
    for n in (22, 23):
        for f in prev.SETS[n]:
            out[family(f["key"])] = layouts_used(f["states"])
    return out


OLD_LAYOUTS = None


def classify(n, outdir):
    """[(family, declared class, measured class, detail)]"""
    new = render_all(n, outdir)
    olds = old_files(n)
    rows = []
    for f in F.SETS[n]:
        prev = olds.get(family(f["key"]), [])
        if not prev:
            rows.append((f["key"], f["cls"], F.NEW,
                         "no card of this family in the previous package"))
            continue
        prev_sha = {sha256(p): os.path.basename(p) for p in prev}
        same, changed = [], []
        for s in f["states"]:
            nm = s["name"] + ".png"
            if sha256(new[nm]) in prev_sha:
                same.append(nm)
            else:
                changed.append(nm)
        renamed = sorted({s["name"] + ".png" for s in f["states"]}
                         - {os.path.basename(p) for p in prev})
        now_lay = layouts_used(f["states"])
        was_lay = OLD_LAYOUTS.get(family(f["key"]), ())
        if not changed and len(same) == len(prev):
            measured, detail = F.REUSE, (
                "all %d states byte-identical to the previous package"
                % len(same))
        elif was_lay and now_lay != was_lay:
            measured, detail = F.REBUILD, (
                "drawn with %s, previously %s"
                % (" + ".join(now_lay), " + ".join(was_lay)))
        else:
            measured, detail = F.COPY, (
                "same layout (%s); %d of %d states differ, %d before"
                % (" + ".join(now_lay), len(changed), len(f["states"]),
                   len(prev)))
        if renamed:
            detail += "; renamed: %s" % ", ".join(x[:-4] for x in renamed)
        rows.append((f["key"], f["cls"], measured, detail))
    return rows


def run():
    global OLD_LAYOUTS
    if OLD_LAYOUTS is None:
        OLD_LAYOUTS = _old_layouts()
    tmp = tempfile.mkdtemp()
    try:
        out = []
        for n in M.VIDEOS:
            d = os.path.join(tmp, "V%d" % n)
            os.makedirs(d)
            out += [(n,) + r for r in classify(n, d)]
        return out
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    rows = run()
    bad = 0
    for n, key, declared, measured, detail in rows:
        # REBUILD and NEW both mean the bytes changed; only REUSE is a
        # byte-level claim, so that is the one held to the bytes.
        ok = measured == declared
        bad += 0 if ok else 1
        print("  %-6s %-42s declared %-11s measured %-11s %s"
              % ("V%d" % n, key, declared, measured,
                 "" if ok else "<-- MISMATCH"))
        print("         %s" % detail)
    print("\n  %d families, %d reuse-class mismatches" % (len(rows), bad))
