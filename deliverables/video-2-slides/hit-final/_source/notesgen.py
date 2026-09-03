# -*- coding: utf-8 -*-
"""Compose v5.1 speaker/editor notes for one video from the canonical script,
the slide/reveal maps in cfg.py and a per-slide DIRECTIONS list.

Every note carries: a working timing estimate at 145 wpm derived from the
canonical script itself, the exact spoken cue line that lands on the slide, the
hand-written editorial direction for that slide, and the reveal-state count."""
import os, sys, importlib

def build(n):
    B="/tmp/v51/v%d"%n
    sys.path.insert(0,B)
    C=importlib.import_module("cfg")
    D=importlib.import_module("directions").DIRECTIONS
    txt=open(os.path.join(B,"canonical_v5.1.1.txt"),encoding="utf-8").read()
    body=txt.split("BEGIN APPROVED VIDEO %d v5.1.1 SCRIPT"%n)[1].split("END APPROVED")[0]
    ps=[x.strip() for x in body.split("\n\n") if x.strip()]
    marks=[]; w=0; cue=None
    for i,p in enumerate(ps):
        if p.startswith("[SLIDE:"):
            nxt=next((q for q in ps[i+1:] if not q.startswith("[SLIDE:")),"")
            marks.append((w/145.0*60, nxt.split(". ")[0].rstrip(".")+"."))
        else: w+=len(p.split())
    assert len(marks)==len(C.SLIDE_MAP)==len(D), (len(marks),len(C.SLIDE_MAP),len(D))
    NOTES=[]
    for (sec,cueline),title,(sn,rng,cnt),direction in zip(marks,C.SLIDE_MAP,
                                                          C.REVEAL_MAP,D):
        head="Timing: approximately %d:%02d."%(sec//60,sec%60)
        cueb="Cue — the line that lands on this slide:\n“%s”"%cueline
        rev=("Reveal states: %d. Reveal frame %s in the build deck."%(cnt,rng)
             if cnt>1 else "Single state. Reveal frame %s in the build deck."%rng)
        NOTES.append("\n\n".join([head,"Slide %d — %s."%(sn,title),cueb,
                                  direction.strip(),rev]))
    FRAMES=[c for _,_,c in C.REVEAL_MAP]
    return NOTES,FRAMES
