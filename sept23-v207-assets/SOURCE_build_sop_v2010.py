# -*- coding: utf-8 -*-
"""Free Flagship SOP — v2.0.9 -> v2.0.10 CANDIDATE. Version strings only.

Not an editorial pass. The deck moved to v2.0.7, and the SOP names the deck in
its pre-session checklist and its source-of-truth map. Left at v2.0.6 it would
tell a facilitator to open a superseded file, which is the one thing a
source-of-truth map must never do.

Nothing else changes: no prose, no rules, no tables, no ordering. The document
is a pure substitution, so its approved eight-page pagination cannot move.
"""
import hashlib, os, shutil
import docx

SRC = ("sept23-v206-assets/"
       "Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.9_CANDIDATE.docx")
OUT = "scratchpad/sept23/out"
DST = (f"{OUT}/"
       "Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.10_CANDIDATE.docx")
STAMP = "Saturday, September 19, 2026 at 11:20 AM CT"
OLD = "Saturday, September 19, 2026 at 8:30 AM CT"
SUBS = [("v2.0.6", "v2.0.7"), ("v2.0.9", "v2.0.10"), (OLD, STAMP)]


def iter_runs(d):
    for p in d.paragraphs:
        for r in p.runs:
            yield r
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        yield r


def build():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)
    counts = {a: 0 for a, _ in SUBS}
    for r in iter_runs(d):
        t = r.text
        for a, b in SUBS:
            if a in t:
                counts[a] += t.count(a)
                t = t.replace(a, b)
        if t != r.text:
            r.text = t
    missing = [a for a, n in counts.items() if n == 0]
    assert not missing, f"substitution never matched: {missing}"
    d.save(DST)

    # prove nothing but the version strings moved
    def text(p):
        x = docx.Document(p)
        out = [q.text for q in x.paragraphs]
        for t in x.tables:
            for row in t.rows:
                out += [c.text for c in row.cells]
        return "\n".join(out)
    before, after = text(SRC), text(DST)
    expect = before
    for a, b in SUBS:
        expect = expect.replace(a, b)
    assert expect == after, "the SOP changed by something other than a version string"
    return DST, counts


if __name__ == "__main__":
    path, counts = build()
    print("built", os.path.basename(path))
    for k, v in counts.items():
        print(f"    {v:>2}x  {k}")
    print("  sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
