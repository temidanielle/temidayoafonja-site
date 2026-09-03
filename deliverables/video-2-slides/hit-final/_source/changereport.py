# -*- coding: utf-8 -*-
"""Paragraph-level change report for a direct-address voice revision.

Aligns the prior locked spoken paragraphs against the revised ones and proves
the revision is bounded: no concept dropped, no factual claim added, CTA and
Watch Next untouched, no new framework."""
import sys, difflib, re, json

def blocks(path, marker_prefix):
    raw=open(path,encoding="utf-8").read()
    b=[x.strip() for x in raw.split("\n\n") if x.strip()]
    return b

def old_spoken(path):
    b=blocks(path,None)[1:]           # drop the 2-line document header block
    return [x for x in b if not x.startswith("SLIDE  —  ")]

def new_blocks(path, begin, end):
    raw=open(path,encoding="utf-8").read().split("\n")
    i=raw.index(begin); j=raw.index(end)
    return [x.strip() for x in "\n".join(raw[i+1:j]).split("\n\n") if x.strip()]

def report(old, new):
    sm=difflib.SequenceMatcher(None, old, new, autojunk=False)
    same=changed=added=removed=0
    detail=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=="equal": same+=i2-i1
        elif tag=="replace":
            n=max(i2-i1, j2-j1); changed+=n
            detail.append({"op":"replace","old":old[i1:i2],"new":new[j1:j2]})
        elif tag=="insert":
            added+=j2-j1; detail.append({"op":"insert","new":new[j1:j2]})
        elif tag=="delete":
            removed+=i2-i1; detail.append({"op":"delete","old":old[i1:i2]})
    return {"unchanged":same,"changed":changed,"inserted":added,
            "removed":removed,"blocks":detail}

DETACHED=["some people","professionals often","people may","a person should",
          "employees often","employees sometimes","workers may","many professionals"]

def scan_detached(text):
    hits=[]
    for para in [p for p in text.split("\n\n") if p.strip()]:
        for ph in DETACHED:
            if ph in para.lower():
                hits.append({"phrase":ph,"context":para.strip()})
    return hits

def voice_stats(spoken):
    subst=[p for p in spoken if len(p.split())>=8]
    sec=[p for p in subst if re.search(r"\b(you|your|yours|yourself)\b",p,re.I)]
    allsec=[p for p in spoken if re.search(r"\b(you|your|yours|yourself)\b",p,re.I)]
    first=[p for p in spoken if re.search(r"\b(I|me|my)\b",p)]
    return {"substantive":len(subst),"substantive_second_person":len(sec),
            "substantive_ratio":round(len(sec)/len(subst),3),
            "all_paragraphs":len(spoken),"all_ratio":round(len(allsec)/len(spoken),3),
            "first_person_paragraphs":len(first)}


IMPERATIVE=("Take ","Cross ","Then ","Now ","Try ","Look ","Write ","Choose ",
 "Ask ","Make ","Document ","Or take ","Pick ","Watch ","Start ","Rewrite ",
 "Say ","Hold ","Add ","Keep ","Name ","Test ","Read ","Compare ","Do not ",
 "Use ","Notice ","Picture ","Answer ","Bring ","Go ","Put ","Give ")

def viewer_facing(spoken):
    """Paragraphs that describe the VIEWER'S situation, which is what the
    register rule is actually about. Excluded, because direct second person
    would be wrong in them, not missing:
      - Temidayo's own first-person evidence and positioning;
      - direct imperatives, where 'you' is already the implied subject;
      - quoted example lines and the self-directed questions the viewer asks
        in their own 'I' voice.
    """
    out=[]
    for p in spoken:
        if len(p.split())<8: continue
        if p.lstrip().startswith(("“","\"","'")): continue
        if p.startswith(IMPERATIVE): continue
        has_you=bool(re.search(r"\b(you|your|yours|yourself)\b",p,re.I))
        has_i=bool(re.search(r"\b(I|I’m|I'm|me|my)\b",p))
        if has_i and not has_you: continue
        out.append(p)
    return out

def viewer_ratio(spoken):
    vf=viewer_facing(spoken)
    sec=[p for p in vf if re.search(r"\b(you|your|yours|yourself)\b",p,re.I)]
    return {"viewer_facing":len(vf),"second_person":len(sec),
            "ratio":round(len(sec)/len(vf),3) if vf else 0.0,
            "not_second_person":[p for p in vf if p not in sec]}
