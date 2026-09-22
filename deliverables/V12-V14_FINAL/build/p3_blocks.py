# -*- coding: utf-8 -*-
"""Thought blocks, derived from the FINAL spoken script only.

Rule: a block is 2-5 sentences of consecutive spoken text inside one section.
Every spoken word appears exactly once, in order. Labels are not spoken.
"""
import re, importlib

MODS = {12: "p3_script12", 13: "p3_script13", 14: "p3_script14"}

def sentences(p):
    parts = re.split(r'(?<=[.?!])\s+(?=[“"A-Z0-9])', p.strip())
    return [s for s in parts if s]

def build(n):
    m = importlib.import_module(MODS[n])
    out = []          # list of (section, [block_text, ...])
    for sec, paras in m.SECTIONS:
        sents = []
        for p in paras:
            sents.extend(sentences(p))
        blocks, cur = [], []
        i = 0
        while i < len(sents):
            cur.append(sents[i])
            i += 1
            left = len(sents) - i
            # close at 3 sentences when doing so cannot strand a 1-sentence tail
            if len(cur) >= 3 and (left == 0 or left >= 2):
                blocks.append(" ".join(cur)); cur = []
            elif len(cur) == 5:
                blocks.append(" ".join(cur)); cur = []
        if cur:
            if blocks and len(sentences(blocks[-1])) + len(cur) <= 5:
                blocks[-1] = blocks[-1] + " " + " ".join(cur)
            else:
                blocks.append(" ".join(cur))
        out.append((sec, blocks))
    return out

def verify(n):
    """Every spoken word exactly once, in order; 2-5 sentences per block."""
    m = importlib.import_module(MODS[n])
    spoken = " ".join(p for _, ps in m.SECTIONS for p in ps).split()
    rebuilt = " ".join(b for _, bs in build(n) for b in bs).split()
    assert spoken == rebuilt, "V%d thought blocks do not reconstruct the spoken stream" % n
    bad = [(sec, b) for sec, bs in build(n) for b in bs if not (2 <= len(sentences(b)) <= 5)]
    return len(spoken), sum(len(bs) for _, bs in build(n)), bad

if __name__ == "__main__":
    for n in MODS:
        w, nb, bad = verify(n)
        print("V%d  %d words  %d blocks  out-of-range blocks: %d" % (n, w, nb, len(bad)))
        for sec, b in bad:
            print("   ", sec, "|", len(sentences(b)), "sent |", b[:110])
