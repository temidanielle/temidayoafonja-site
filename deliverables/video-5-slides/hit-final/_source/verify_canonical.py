# -*- coding: utf-8 -*-
"""Literal comparison of the built v3.0 scripts against the canonical prompt."""
import sys, difflib
sys.path.insert(0,"/tmp/v5v3")

CANON="/tmp/v5v3/canonical.txt"
raw=open(CANON,encoding="utf-8").read().split("\n")
i=raw.index("BEGIN APPROVED VIDEO 5 v3.0 SCRIPT")
j=raw.index("END APPROVED VIDEO 5 v3.0 SCRIPT")
body=[l.rstrip() for l in raw[i+1:j]]
blocks=[b.strip() for b in "\n".join(body).split("\n\n") if b.strip()]
print("canonical blocks:", len(blocks))

markers=[b for b in blocks if b.startswith("[SLIDE:")]
spoken =[b for b in blocks if not b.startswith("[SLIDE:")]
print("canonical markers:", len(markers), " spoken paragraphs:", len(spoken))
words=sum(len(b.split()) for b in spoken)
print("canonical spoken word count:", words)

# ---- teleprompter TXT: strip only the 2-line header block, compare literally
tel_raw=open("/tmp/v5v3/Video_5_HIT_FINAL/LONG_FORM/"
  "Video5TeleprompterScriptwithslidemarkers_HIT_v3.0.txt",encoding="utf-8").read()
tel_blocks=[b.strip() for b in tel_raw.split("\n\n") if b.strip()][1:]
tel_norm=[]
for b in tel_blocks:
    if b.startswith("SLIDE  —  "):
        tel_norm.append("[SLIDE: %s]"%b[len("SLIDE  —  "):])
    else:
        tel_norm.append(b)
ok_tel = tel_norm == blocks
print("teleprompter TXT == canonical (markers restored):", ok_tel)
if not ok_tel:
    for op in difflib.SequenceMatcher(None,blocks,tel_norm,autojunk=False).get_opcodes():
        if op[0]!="equal": print("  ",op, blocks[op[1]:op[2]][:1], tel_norm[op[3]:op[4]][:1])

# ---- reading TXT
rdg=[b.strip() for b in open("/tmp/v5v3/Video_5_HIT_FINAL/LONG_FORM/"
  "Video5ReadingScriptnomarkers_HIT_v3.0.txt",encoding="utf-8").read().split("\n\n") if b.strip()]
ok_rdg = rdg == spoken
print("reading TXT == canonical spoken:", ok_rdg)
if not ok_rdg:
    for op in difflib.SequenceMatcher(None,spoken,rdg,autojunk=False).get_opcodes():
        if op[0]!="equal": print("  ",op)

# ---- teleprompter minus markers == reading script
ok_minus = [b for b in tel_norm if not b.startswith("[SLIDE:")] == rdg
print("teleprompter minus markers == reading script:", ok_minus)

# ---- DOCX text equality
from docx import Document
def paras(p):
    return [x.text.strip() for x in Document(p).paragraphs if x.text.strip()]
teld=paras("/tmp/v5v3/Video_5_HIT_FINAL/LONG_FORM/"
  "Video5TeleprompterScriptwithslidemarkers_HIT_v3.0.docx")[4:]
teld_norm=["[SLIDE: %s]"%x[len("SLIDE  —  "):] if x.startswith("SLIDE  —  ") else x
           for x in teld]
print("teleprompter DOCX == canonical:", teld_norm==blocks)
rdgd=paras("/tmp/v5v3/Video_5_HIT_FINAL/LONG_FORM/"
  "Video5ReadingScriptnomarkers_HIT_v3.0.docx")[4:]
print("reading DOCX == canonical spoken:", rdgd==spoken)

# ---- 12 markers ordered one-to-one
names=[m[len("[SLIDE:"):-1].strip() for m in markers]
print("marker count:", len(markers))
for n,nm in enumerate(names,1): print("   %2d  %s"%(n,nm))
pos=[k for k,b in enumerate(blocks) if b.startswith("[SLIDE:")]
tpos=[k for k,b in enumerate(tel_norm) if b.startswith("[SLIDE:")]
print("marker positions identical:", pos==tpos)

# ---- Shorts verbatim against canonical
lines=raw
def short_copy(fname):
    a=lines.index("Filename:")
    start=lines.index("FOUR STANDALONE SHORTS — v3.0")
    idx=[k for k,l in enumerate(lines) if l.strip()==fname and k>start]
    assert idx, fname
    k=idx[0]
    s=lines.index("Spoken copy:",k)
    e=k
    for t in range(s+1,len(lines)):
        if lines[t].startswith("---------") or lines[t].startswith("========"):
            e=t; break
    return [b.strip() for b in "\n".join(lines[s+1:e]).split("\n\n") if b.strip()]

from shorts_text import SHORTS
allok=True
for fn,role,hook,copy in SHORTS:
    canon_copy=short_copy(fn)
    ok = canon_copy==copy
    allok &= ok
    built=paras("/tmp/v5v3/Video_5_HIT_FINAL/SHORTS/"+fn)
    body=built[built.index("RECORDING COPY")+1:]
    ok2 = body==copy
    allok &= ok2
    print("%-52s canon:%s docx:%s (%d paras)"%(fn,ok,ok2,len(copy)))
print("ALL SHORTS VERBATIM:", allok)
