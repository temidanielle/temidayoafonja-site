# -*- coding: utf-8 -*-
"""Generic v5.0 package builder. Each video supplies a config module; the
document architecture, the 14-section editor brief and the packaging are shared.

    python3 /tmp/v5/build5.py <video number>
"""
import os, sys, shutil, importlib
sys.path.insert(0,"/tmp/da")
from docxkit import *
from changereport import new_blocks

N=int(sys.argv[1])
BASE="/tmp/v5/v%d"%N
sys.path.insert(0,BASE)
C=importlib.import_module("cfg")
SHORTS=importlib.import_module("shorts_text").SHORTS

ROOT=os.path.join(BASE,"Video_%d_HIT_FINAL"%N)
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

LINES=new_blocks(os.path.join(BASE,"canonical_v5.0.txt"),
  "BEGIN APPROVED VIDEO %d v5.0 SCRIPT"%N,"END APPROVED VIDEO %d v5.0 SCRIPT"%N)
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]
WORDS=sum(len(x.split()) for x in SPOKEN)
RUNTIME="%d:%02d"%(WORDS/145*60//60, WORDS/145*60%60)

TEL="Video%dTeleprompterScriptwithslidemarkers_HIT_v5.0"%N
RDG="Video%dReadingScriptnomarkers_HIT_v5.0"%N
EDB="Video_%d_EDITOR_ONLY_HIT_Brief_v5.0.docx"%N
PUB="Video_%d_Publishing_Package_HIT_v5.0.docx"%N
SEB="Video_%d_Shorts_EDITOR_ONLY_HIT_Brief_v5.0.docx"%N
scripts(N,C.TITLE,LINES,SPOKEN,LF,TEL,RDG)

# ---------------------------------------------------------- editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO %d  ·  v5.0 BELONGING + IDENTITY"%N,size=12,bold=True,color=GOLD,
  after=2,caps=True)
P(d,C.TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in C.METADATA: keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
for line in C.METADATA_NOTES:
    keep(P(d,line,bold=True,color=RED,after=6,spacing=1.25))

H1(d,"2.  Identity promise for this video",before=14)
p=P(d,C.IDENTITY,size=11,bold=True,color=NAVY,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,C.IDENTITY_NOTE,after=8,spacing=1.25))

H1(d,"3.  Who is watching, and what they are feeling",before=14)
for para in C.RECOGNITION: P(d,para,after=6,spacing=1.25)

H1(d,"4.  Belonging and lived proof",before=14)
P(d,C.BELONGING_LEAD,after=6,spacing=1.25)
for x in C.BELONGING: keep(P(d,"—  "+x,after=5,spacing=1.25))
p=P(d,"Temidayo is evidence, not the hero. Her story is there so the viewer "
     "recognises themselves. If a cut makes her the subject rather than the "
     "proof, it is the wrong cut.",size=11,bold=True,color=RED,after=8,
     spacing=1.25)
shade(p,BAND_CREAM); keep(p)

H1(d,"5.  First 30 seconds — H.I.T. map",before=14)
hit_table(d,C.HIT_ROWS)
keep(P(d,"Hook layers:",size=10.5,bold=True,color=NAVY,before=10,after=5))
hook_block(d,*C.HOOK)

H1(d,"6.  Slide marker → slide",before=14)
P(d,C.SLIDE_NOTE,after=8)
for n,job in enumerate(C.SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"7.  Reveal-state map",before=14)
P(d,"%d reveal frames, inspected from the file. Reveal visuals unchanged."
    %C.FRAMES_TOTAL,after=8)
for n,rng,cnt in C.REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"8.  Visual assets and proof",before=14)
pairlist(d,C.ASSETS,after=4)
keep(P(d,"Slides carry structure. Artifacts carry proof. Temidayo carries the "
       "relationship and the meaning. Do not swap those jobs around.",
       bold=True,before=4,after=8,spacing=1.25))

H1(d,"9.  Factual boundaries",before=14)
for para in C.FACT_BLOCKS:
    p=P(d,para,size=11,bold=True,color=RED,after=8,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
pairlist(d,C.FACT_LIST,after=3)

H1(d,"10.  Do not use",before=14)
pairlist(d,C.DONOTUSE,after=3)

H1(d,"11.  CTA and watch next",before=14)
keep(P(d,"One resource CTA only: %s — %s"%(C.CTA,C.CTA_URL),after=5))
for line in C.CTA_NOTES: keep(P(d,line,after=6,spacing=1.25))
keep(P(d,"Watch next: %s"%C.NEXT_FULL,bold=True,after=6))
keep(P(d,"Do not leave Subscribe as the only end-screen element.",bold=True,
       color=RED,after=8))

H1(d,"12.  Identity exit — do not cut",before=14)
p=P(d,C.IDENTITY_LINE,size=11,bold=True,color=NAVY,after=6,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,C.IDENTITY_PLACEMENT,after=8,spacing=1.25))

H1(d,"13.  Direct-address editing rule",before=14)
pairlist(d,["keep direct questions on Temidayo's face;","no keynote framing;",
 "do not overuse quote cards;","let the slides carry structure;",
 "preserve the pauses;","never cut the relational lines as filler."],after=3)
keep(P(d,"Relational beats: "+" · ".join(C.BEATS),size=10.5,after=8,spacing=1.25))

H1(d,"14.  Speaker-note update record",before=14)
pairlist(d,["Main deck: %d notes parts rewritten for the v5.0 narration."%C.SLIDES,
 "Reveal deck: %d notes parts rewritten."%C.FRAMES_TOTAL,
 C.SLIDE_XML_RECORD,
 "Timings are working estimates at 145 words per minute for the %s-word "
 "script, about %s. Replace them from the finished cut."
 %("{:,}".format(WORDS),RUNTIME)],after=3)
compress(d,*C.EDB_COMPRESS)
d.save(os.path.join(LF,EDB))

# ------------------------------------------------- publishing + description
CHAPTER_LINES=["%s %s"%(t,c) for t,c in C.CHAPTERS]
EMOJI_NOTE=("The restrained emoji system is part of the approved standard: "
 "✨ teaching points, 🧭 CTA and resource, ⏱️ chapters, ▶️ Watch Next, "
 "🔗 Connect and Explore. Do not remove it and do not add more.")
DESC=C.desc(CHAPTER_LINES)

def description_block(d):
    H1(d,"INTERNAL NOTE — DO NOT PASTE INTO YOUTUBE",before=14)
    p=P(d,EMOJI_NOTE,size=10.5,italic=True,color=RED,after=12,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    p=keep(P(d,"COPY-READY YOUTUBE DESCRIPTION — BEGIN",size=11,bold=True,
             color=NAVY,before=14,after=12,spacing=1.2))
    shade(p,BAND_NAVY)
    for para in DESC: keep(P(d,para if para else " ",after=7 if para else 3))
    keep(P(d,"— END OF THE COPY-READY DESCRIPTION —",size=10,bold=True,
           color=DIM,before=14,after=12,spacing=1.2))
    H1(d,"Internal note — do not paste into YouTube",before=14)
    p=P(d,"WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT",size=11,
        bold=True,color=RED,after=6,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    p=P(d,"These timestamps are script-derived, not measured from the finished "
        "edit. Replace every one before publication.",size=10.5,bold=True,
        italic=True,color=RED,after=10,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    H1(d,"Working chapters — reference copy",before=14)
    keep(P(d,"Identical to the %d chapter lines inside the description above."
           %len(CHAPTER_LINES),size=10.5,italic=True,color=DIM,after=8))
    for line in CHAPTER_LINES: keep(P(d,line,size=11,after=4))

for kind in ("pub","desc"):
    d=newdoc()
    head(d,N,C.TITLE,"Video %d  ·  %s  ·  v5.0"%(N,"Publishing package"
         if kind=="pub" else "YouTube description"),
         "Everything needed to upload. Working timestamps must be replaced with "
         "real ones from the finished edit." if kind=="pub" else
         "Upload copy only. Everything below the end marker is internal and "
         "must not be pasted into YouTube.")
    H1(d,"Title",before=14); P(d,C.TITLE,size=12,after=10)
    for extra in C.TITLE_EXTRA:
        keep(P(d,extra,size=10.5,color=DIM,after=10))
    H1(d,"Thumbnail",before=14); P(d,C.THUMB,size=12,bold=True,after=10)
    for extra in C.THUMB_EXTRA:
        p=P(d,extra,size=10.5,bold=True,color=RED,after=10,spacing=1.25)
        shade(p,BAND_CREAM); keep(p)
    H1(d,"Primary search phrase",before=14); P(d,C.PRIMARY,after=10)
    if kind=="pub":
        H1(d,"Supporting search language",before=14); P(d,C.SUPPORTING,after=10)
    description_block(d)
    H1(d,"Pinned comment",before=14)
    for para in C.PINNED: keep(P(d,para,after=6))
    H1(d,"Watch next",before=14)
    keep(P(d,C.NEXT_FULL,bold=True,after=8))
    for line in C.PUB_EXTRA if kind=="pub" else []:
        keep(P(d,line,bold=True,after=8,spacing=1.25))
    H1(d,"YouTube tag field",before=14)
    keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
    keep(P(d,C.TAGS,size=10.5,after=10))
    compress(d,*C.PUB_COMPRESS)
    d.save(os.path.join(LF,PUB) if kind=="pub"
           else os.path.join(BASE,"Video_%d_YouTube_Description_HIT.docx"%N))

# ---------------------------------------------------------------- Shorts
for (fn,role,hook,copy),label in zip(SHORTS,["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]):
    d=newdoc(True)
    P(d,"VIDEO %d SHORT  ·  v5.0"%N,size=10,bold=True,color=GOLD,after=4,caps=True)
    P(d,label,size=20,bold=True,color=NAVY,after=8,spacing=1.1)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    keep(P(d,"Opening line:  “%s”"%hook,size=11,color=DIM,after=5))
    keep(P(d,"Related long-form:  %s"%C.TITLE,size=11,color=DIM,after=10))
    H1(d,"RECORDING COPY",before=12)
    for line in copy: keep(P(d,line,size=13.5,color=INK,after=10,spacing=1.5))
    d.save(os.path.join(SH,fn))

d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO %d — FOUR STANDALONE SHORTS  ·  v5.0"%N,size=18,bold=True,
  color=NAVY,after=8,spacing=1.1)
p=P(d,"This document is for the editor. It is separate from the four Short "
     "recording documents and must not be placed on Temidayo's recording "
     "screen.",size=11,italic=True,color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)
H1(d,"How these are produced",before=14)
keep(P(d,"Separately recorded 9:16 Shorts. NOT excerpts cut from the long-form "
       "video. All four were rewritten for v5.0.",bold=True,after=10))
P(d,"Each Short needs:",after=6)
pairlist(d,["recognition before any teaching;","one simple idea;",
 "an exact verbal hook;","an exact on-screen hook;",
 "accurate mobile-safe captions;",
 "Video %d as the Related Video when available."%N])
direct_address_section(d,"Direct address is part of the creative",C.SHORT_BEATS)
for label,role,onscreen,body in C.SHORT_BLOCKS:
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video %d"%N,size=10.5,color=DIM,before=4,after=6))
H1(d,"All Shorts — boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,C.DONOTUSE,after=3)
p=P(d,"And no generic motivation. Every Short has to leave the viewer with one "
     "thing they can actually check in their own work.",size=11,bold=True,
     color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
compress(d,*C.SEB_COMPRESS)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO %d — v5.0 BELONGING + IDENTITY FINAL RECORDING PACKAGE"%N,""]
R+=C.readme_head(WORDS,RUNTIME)
R+=["-"*70,"","WHAT EACH FILE IS","","LONG_FORM/","",
 "  %s.docx"%TEL,"  %s.txt"%TEL,
 "      Temidayo's recording copy. Spoken script in large text; slide markers",
 "      in tinted bands. The markers are not spoken.","",
 "  %s.docx"%RDG,"  %s.txt"%RDG,
 "      The same spoken words with the slide markers removed.","",
 "  %s"%EDB,
 "      For the editor. Fourteen sections, from the locked metadata and the",
 "      identity promise through the belonging beat, the first-30 H.I.T. map,",
 "      the slide and reveal maps, factual boundaries, the identity exit and",
 "      the notes record.","",
 "  %s"%PUB,
 "      Title, thumbnail, search language, the copy-ready description,",
 "      working chapter estimates, pinned comment and tag field.","",
 "SHORTS/","",
 "  Four recording documents. Recording copy only, no editor directions.","",
 "  %s"%SEB,
 "      For the editor. Hooks and visual treatment for all four.","",
 "-"*70,"","ALL FILES IN THIS PACKAGE",""]
for f in FILES: R.append("  "+f)
R+=["  README_FINAL.txt","  SHA256SUMS.txt",""]
R+=C.readme_tail()
R+=["-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_%d_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"%N,""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))

MANIFEST=["LONG_FORM/%s.docx"%TEL,"LONG_FORM/%s.txt"%TEL,
 "LONG_FORM/%s.docx"%RDG,"LONG_FORM/%s.txt"%RDG,
 "LONG_FORM/%s"%EDB,"LONG_FORM/%s"%PUB]+\
 ["SHORTS/"+f for f,_,_,_ in SHORTS]+["SHORTS/"+SEB,"README_FINAL.txt"]
ZIP=os.path.join(BASE,"Video_%d_HIT_FINAL_Recording_and_Shorts_Package.zip"%N)
z=package(ROOT,MANIFEST,ZIP,"Video_%d_HIT_FINAL"%N,
  ["# VIDEO %d - v5.0 BELONGING + IDENTITY FINAL RECORDING PACKAGE"%N,
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot carry its own",
   "# checksum either; it is published in the sibling file",
   "# Video_%d_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"%N])
print("V%d  %d words  %s  ZIP %s"%(N,WORDS,RUNTIME,z))
print("     DESC %s"%sha256(os.path.join(BASE,"Video_%d_YouTube_Description_HIT.docx"%N)))
