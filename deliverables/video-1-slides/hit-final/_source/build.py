# -*- coding: utf-8 -*-
"""Build the Video 1 v5.0 BELONGING + IDENTITY recording and Shorts package."""
import os, sys, shutil
sys.path.insert(0,"/tmp/da"); sys.path.insert(0,"/tmp/v5/v1")
from docxkit import *
from changereport import new_blocks
from shorts_text import SHORTS

BASE="/tmp/v5/v1"; VID=1
ROOT=os.path.join(BASE,"Video_1_HIT_FINAL")
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

TITLE="How to Change Jobs Without Starting Your Career Over"
DECK_TITLE="How I Changed Jobs Without Starting My Career Over"
THUMB="DON’T START FROM ZERO"
PRIMARY="how to change jobs without starting over"
SUPPORTING=("change jobs without starting over · transferable skills · career "
 "change · career pivot · transferable experience · career portability · "
 "career evidence · internal mobility")
CTA="Free Career Evidence Starter"
CTA_URL="https://temidayoafonja.com/career-evidence-starter"
NEXT="Is Your Job Making You Less Marketable?"
IDENTITY=("Become the professional who can enter a career change already knowing "
 "what is still theirs, what they can prove, and what they still have to learn.")

LINES=new_blocks(os.path.join(BASE,"canonical_v5.0.txt"),
  "BEGIN APPROVED VIDEO 1 v5.0 SCRIPT","END APPROVED VIDEO 1 v5.0 SCRIPT")
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]

TEL="Video1TeleprompterScriptwithslidemarkers_HIT_v5.0"
RDG="Video1ReadingScriptnomarkers_HIT_v5.0"
EDB="Video_1_EDITOR_ONLY_HIT_Brief_v5.0.docx"
PUB="Video_1_Publishing_Package_HIT_v5.0.docx"
SEB="Video_1_Shorts_EDITOR_ONLY_HIT_Brief_v5.0.docx"
scripts(VID,TITLE,LINES,SPOKEN,LF,TEL,RDG)

SLIDE_MAP=["Title","My Career Path","01 Look Underneath the Title","Move One",
 "02 Explain What the Work Changed","Move Two","One Result — 47 to 75",
 "03 Keep Evidence Before You Need It","Move Three",
 "Three Things I Learned to Do","Before Your Next Move",
 "Career Evidence Starter","Watch Next"]
REVEAL_MAP=[(1,"1",1),(2,"2",1),(3,"3",1),(4,"4–6",3),(5,"7",1),(6,"8–9",2),
 (7,"10–11",2),(8,"12",1),(9,"13–16",4),(10,"17",1),(11,"18–20",3),(12,"21",1),
 (13,"22",1)]

# ------------------------------------------------------- 1. editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 1  ·  v5.0 BELONGING + IDENTITY",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in (("Public title",TITLE),("On-screen deck title",DECK_TITLE),
  ("Thumbnail",THUMB),("Primary search phrase",PRIMARY),("Primary CTA",CTA),
  ("CTA URL",CTA_URL),("Watch next","Video 2 — "+NEXT),
  ("Memory device","The three practices. No acronym, no second framework.")):
    keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
keep(P(d,"The two titles differ intentionally. Do not change the title slide to "
       "match the public title.",bold=True,after=6,spacing=1.25))
keep(P(d,"Do not add the Capability Formation Field Kit, Keep the Proof or the "
       "Career Evidence 3 Cs to this video.",bold=True,color=RED,after=8,
       spacing=1.25))

H1(d,"2.  Identity promise for this video",before=14)
p=P(d,IDENTITY,size=11,bold=True,color=NAVY,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,"The video is not only solving one job change. It is helping the "
       "viewer become someone a change cannot erase. Everything in the edit "
       "should serve that.",after=8,spacing=1.25))

H1(d,"3.  Who is watching, and what they are feeling",before=14)
P(d,"Someone who has spent years getting good at their work, and is now facing "
    "a change of job, function or industry. Underneath the practical question "
    "is a quieter one: does what I have already done still count?",after=6,
    spacing=1.25)
keep(P(d,"They are not a beginner and they do not want to be spoken to like "
       "one. They want to be told the truth about which parts travel.",
       after=8,spacing=1.25))

H1(d,"4.  Belonging and lived proof",before=14)
P(d,"Recognition comes first and the framework waits. The order is: the "
    "viewer's situation, then “I know that question, I have had to answer it "
    "more than once”, then Temidayo's own crossings, then the interpretation, "
    "and only then the three practices at about 3:10.",after=6,spacing=1.25)
for x in ["Accounting and audit, then cybersecurity and privacy, then people "
 "and employee experience, then enterprise transformation.",
 "The December 2008 accounting degree and the financial crisis, exactly as "
 "spoken and no further detail.",
 "Going back to school, and preparing for a professional certification and "
 "not passing on the first attempt. This is the honest-relearning beat and it "
 "earns the “not everything transfers” boundary. Do not cut it.",
 "The onboarding redesign and the 47 to 75 measure, bounded as below."]:
    keep(P(d,"—  "+x,after=5,spacing=1.25))
p=P(d,"Temidayo is evidence, not the hero. Her story is there so the viewer "
     "recognises themselves. If a cut makes her the subject rather than the "
     "proof, it is the wrong cut.",size=11,bold=True,color=RED,after=8,
     spacing=1.25)
shade(p,BAND_CREAM); keep(p)

H1(d,"5.  First 30 seconds — H.I.T. map",before=14)
hit_table(d,[
 ["0:00–0:09","“You have spent years getting good at something. And now the "
  "job might change, or the function, or the whole industry.”",
  "Recognition. The viewer's exact situation, before any teaching.",
  "DON’T START FROM ZERO",
  "Open on Temidayo, direct to camera. No title card.",
  "None yet, by design. The first job is being seen.",
  "The viewer knows this video is about them."],
 ["0:09–0:16","“So a quiet question shows up: does what I have already done "
  "still count?”","Names the feeling under the practical problem.","—",
  "Stay on her face. Let the question sit.",
  "The question is put plainly, not sold.",
  "The viewer hears their own private question said out loud."],
 ["0:16–0:22","“I know that question. I have had to answer it more than "
  "once.”","Belonging. She has stood where the viewer is standing.","—",
  "No cutaway. This line only works on her face.",
  "Lived: several career changes of her own.",
  "The viewer feels understood before being taught."],
 ["0:22–0:33","“The honest answer is that some of it travels. Not all of it. "
  "Let me show you the three things I use to tell the difference.”",
  "The honest promise, then the payoff.","3 PRACTICES",
  "Restrained reveal of the three practices, then into the deck.",
  "She refuses the easy reassurance, which is why the rest is believable.",
  "Payoff is explicit by 33 seconds."]])
keep(P(d,"Hook layers:",size=10.5,bold=True,color=NAVY,before=10,after=5))
hook_block(d,
 "You have spent years getting good at something.",
 "DON’T START FROM ZERO",
 "Direct to camera, then a restrained career-sequence overlay at the career "
 "path section. No decorative B-roll anywhere.",
 "Roughly eighteen years across very different functions and industries, the "
 "certification she did not pass first time, and the bounded 47 to 75 measure.",
 "Three practices for telling what travels from what does not, by 0:33.")

H1(d,"6.  Slide marker → slide",before=14)
P(d,"Thirteen markers, mapping to the existing thirteen-slide deck in order. "
    "The v5.0 script was mapped against the deck and every slide still serves "
    "the new story, so NO slide text was changed in this rebuild.",after=8)
for n,job in enumerate(SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"7.  Reveal-state map",before=14)
P(d,"22 reveal frames, inspected from the file. Reveal visuals unchanged.",after=8)
for n,rng,cnt in REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"8.  Visual assets and proof",before=14)
pairlist(d,["the career-sequence overlay at the career-path section;",
 "slide 7, the 47 to 75 before and after;",
 "slide 9, the four-line evidence record;",
 "slide 12, the real Career Evidence Starter artifact — cover in front, "
 "Portable Proof Line page behind."],after=4)
keep(P(d,"Slides carry structure. Artifacts carry proof. Temidayo carries the "
       "relationship and the meaning. Do not swap those jobs around.",
       bold=True,before=4,after=8,spacing=1.25))

H1(d,"9.  Factual boundaries",before=14)
p=P(d,"THE 47 TO 75 MEASURE IS BOUNDED. One measure of how well new hires felt "
     "integrated, after an onboarding redesign Temidayo LED WITH HER TEAM. Not "
     "a claim about everything the redesign touched, and not solo work. The "
     "script says both out loud. Do not trim either.",size=11,bold=True,
     color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
p=P(d,"EXCLUDED. The ~30% retention improvement and the >$2M avoided-turnover "
     "figure are not in this video and must never be added to it, to a "
     "graphic, a caption or a thumbnail.",size=11,bold=True,color=RED,after=8,
     spacing=1.25)
shade(p,BAND_CREAM); keep(p)
pairlist(d,["“roughly eighteen years” is approved wording, not an open question;",
 "December 2008 accounting degree and financial crisis exactly as spoken;",
 "the certification non-pass stays a non-pass — no later result is implied;",
 "no employer named;","no invented assignment, quote or conversation;",
 "the permitted, non-confidential record boundary;",
 "the smallest-claim rule on the what-this-shows line."],after=3)

H1(d,"10.  Do not use",before=14)
pairlist(d,["stock office B-roll;","generic résumé graphics;","employer logos;",
 "Field Kit imagery;","fake shock expressions;","countdown motifs;",
 "constant zooms;","AI-generated scenery;","social-media template effects;",
 "anything that makes a career change look like a crisis."],after=3)

H1(d,"11.  CTA and watch next",before=14)
keep(P(d,"One resource CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"It arrives after the identity bridge, so it reads as the next step "
       "in what she has just described rather than an advert. Keep that order.",
       after=6,spacing=1.25))
keep(P(d,"Use the direct public landing-page URL only. No PDF link.",bold=True,after=6))
keep(P(d,"Watch next: Video 2 — %s. Slide 13 carries the correct title."%NEXT,
       bold=True,after=6))
keep(P(d,"Do not leave Subscribe as the only end-screen element.",bold=True,
       color=RED,after=8))

H1(d,"12.  Identity exit — do not cut",before=14)
p=P(d,"“I am not only trying to help you get through one job change. I want "
     "you to get to the point where a new context does not make you forget "
     "what you already know how to do.”",size=11,bold=True,color=NAVY,after=6,
     spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,"It sits just before the Before Your Next Move slide, after the two "
       "mistakes and the honest limits. It is the point of the video. If the "
       "edit runs long, cut something else.",after=8,spacing=1.25))

H1(d,"13.  Direct-address editing rule",before=14)
pairlist(d,["keep direct questions on Temidayo's face;",
 "no keynote framing;","do not overuse quote cards;",
 "let the slides carry structure;","preserve the pauses;",
 "never cut the relational lines as filler."],after=3)
keep(P(d,"Relational beats: “I know that question.” · “Let me show you how "
       "this came up for me.” · “I am not being modest. I have paid for that "
       "lesson.” · “I do not want you to stretch yours either.”",size=10.5,
       after=8,spacing=1.25))

H1(d,"14.  Speaker-note update record",before=14)
pairlist(d,["Main deck: 13 notes parts rewritten for the v5.0 narration.",
 "Reveal deck: 22 notes parts rewritten.",
 "Slide XML, geometry, typography, palette and media: UNCHANGED.",
 "Timings are working estimates at 145 words per minute for the 1,727-word "
 "script, about 11:54. Replace them from the finished cut."],after=3)
compress(d, 1.04, 0.30)
d.save(os.path.join(LF,EDB))
print("editor brief written")

# ------------------------------------------- 2. publishing + description
CHAPTERS=[("00:00","Does What You Have Already Done Still Count?"),
 ("00:39","The Honest Promise: Not Everything Transfers"),
 ("01:31","What Actually Carried Across My Career Changes"),
 ("03:09","Practice 1: Look Underneath the Title"),
 ("04:57","Practice 2: Explain What the Work Changed"),
 ("06:09","One Result, Stated Precisely: 47 to 75"),
 ("06:52","Practice 3: Keep Evidence Before You Need It"),
 ("08:26","The Two Mistakes, and What This Cannot Do"),
 ("09:22","Who You Are Becoming"),
 ("09:50","Three Questions Before Your Next Move"),
 ("10:48","Free Career Evidence Starter"),
 ("11:10","Is Your Job Making You Less Marketable?")]
CHAPTER_LINES=["%s %s"%(t,c) for t,c in CHAPTERS]
EMOJI_NOTE=("The restrained emoji system is part of the approved standard: "
 "✨ teaching points, 🧭 CTA and resource, ⏱️ chapters, ▶️ Watch Next, "
 "🔗 Connect and Explore. Do not remove it and do not add more.")
TAGS=("how to change jobs without starting over, transferable skills, career "
 "change, career pivot, changing careers, transferable experience, career "
 "portability, career evidence, starting over, experienced professionals, "
 "Temidayo Afonja, Capability Formation")

DESC=[
 "You have spent years getting good at your work. Now the job, the function or "
 "the whole industry might change — and a quiet question shows up: does what I "
 "have already done still count?",
 "Some of it does. Not all of it. This video is about telling the difference, "
 "before you need to.",
 "I have crossed accounting and audit, cybersecurity and privacy, people and "
 "employee experience, and enterprise transformation. Every move meant real "
 "relearning. Something else came with me every time.",
 "Three practices I use:",
 "✨ Look underneath the title — name what the work trained you to notice, "
 "decide and solve.",
 "✨ Explain what the work changed — in words someone outside your company can "
 "understand.",
 "✨ Keep evidence before you need it — a permitted, high-level record in your "
 "own words.",
 "I also share one bounded example of my own: an onboarding redesign I led "
 "with my team, where one measure of how well new hires felt integrated moved "
 "from 47 to 75.",
 "This will not stop a restructure or decide a hiring market for you. What it "
 "changes is what you are holding when those things happen — so a new context "
 "stops making you forget what you already know how to do.","",
 "🧭 FREE CAREER EVIDENCE STARTER",
 "Turn one accomplishment into a portable proof line you can use in a "
 "performance review, an interview, an internal move or a career pivot:",
 CTA_URL,"",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "▶️ WATCH NEXT", NEXT,"[ADD VIDEO 2 LINK WHEN LIVE]","",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "#CareerGrowth #CareerChange #TransferableSkills"]

PINNED=["Which part of this is happening in your situation right now?",
 "1. You are about to change context and are not sure what still counts",
 "2. You know what you can do but cannot explain what changed because of you",
 "3. You have done good work and the evidence for it is already fading",
 "Tell me which one, and what you would put in the “what this shows” line for "
 "one piece of your work.",
 "If you want to try it on one real accomplishment, the free Career Evidence "
 "Starter is here:", CTA_URL]

def description_block(d, heading_before=14):
    H1(d,"INTERNAL NOTE — DO NOT PASTE INTO YOUTUBE",before=heading_before)
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
    keep(P(d,"Identical to the twelve chapter lines inside the description "
           "above.",size=10.5,italic=True,color=DIM,after=8))
    for line in CHAPTER_LINES: keep(P(d,line,size=11,after=4))

for doc_kind in ("pub","desc"):
    d=newdoc()
    head(d,VID,TITLE,
         "Video 1  ·  %s  ·  v5.0"%("Publishing package" if doc_kind=="pub"
                                    else "YouTube description"),
         "Everything needed to upload. Working timestamps must be replaced with "
         "real ones from the finished edit." if doc_kind=="pub" else
         "Upload copy only. Everything below the end marker is internal and "
         "must not be pasted into YouTube.")
    H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
    keep(P(d,"On-screen deck title (intentionally different): %s"%DECK_TITLE,
           size=10.5,color=DIM,after=10))
    H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
    H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
    if doc_kind=="pub":
        H1(d,"Supporting search language",before=14); P(d,SUPPORTING,after=10)
    description_block(d)
    H1(d,"Pinned comment",before=14)
    for para in PINNED: keep(P(d,para,after=6))
    H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 2)"%NEXT,bold=True,after=8))
    H1(d,"YouTube tag field",before=14)
    keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
    keep(P(d,TAGS,size=10.5,after=10))
    compress(d, 1.04, 0.34)
    d.save(os.path.join(LF,PUB) if doc_kind=="pub"
           else os.path.join(BASE,"Video_1_YouTube_Description_HIT.docx"))
print("publishing package and description written")

# ------------------------------------------------------ 3. Shorts + brief
LABELS=["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]
for (fn,role,hook,copy),label in zip(SHORTS,LABELS):
    d=newdoc(True)
    P(d,"VIDEO 1 SHORT  ·  v5.0",size=10,bold=True,color=GOLD,after=4,caps=True)
    P(d,label,size=20,bold=True,color=NAVY,after=8,spacing=1.1)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    keep(P(d,"Opening line:  “%s”"%hook,size=11,color=DIM,after=5))
    keep(P(d,"Related long-form:  %s"%TITLE,size=11,color=DIM,after=10))
    H1(d,"RECORDING COPY",before=12)
    for line in copy:
        keep(P(d,line,size=13.5,color=INK,after=10,spacing=1.5))
    d.save(os.path.join(SH,fn))

d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 1 — FOUR STANDALONE SHORTS  ·  v5.0",size=18,bold=True,color=NAVY,
  after=8,spacing=1.1)
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
 "accurate mobile-safe captions;","Video 1 as the Related Video when available."])
direct_address_section(d,"Direct address is part of the creative",
 ["“I know that feeling.”","“You are not starting from zero.”",
  "“Let me show you the difference between naming a project and showing what "
  "changed.”","“Put your job title aside for one minute and try this.”"])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 1",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition / story","DOES IT STILL COUNT?",
 ["Open on Temidayo. The first job is recognition, not teaching.",
  "Visual:  NEW TO A PLACE  ≠  NEW TO EVERY PROBLEM",
  "Keep the relearning boundary. Do not let it promise that everything "
  "transfers.",
  "End on:  YOU ARE NOT STARTING FROM ZERO."])
short("SHORT 2","Distinction / myth","A WORD IS NOT EVIDENCE",
 ["Restrained contrast. No résumé-scroll animation.",
  "End on:  WHERE HAVE YOU ALREADY SHOWN IT?"])
short("SHORT 3","Proof / personal evidence","47 → 75",
 ["FACTUAL BOUNDARY: ONE measure of how well new hires felt integrated, from "
  "a redesign Temidayo LED WITH HER TEAM. No employer named, no 30% retention "
  "figure, no $2M figure, no additional outcome.",
  "Show the before and after as restrained text, matching slide 7.",
  "The closing beat is about honesty, not the number. Give it room.",
  "End on:  ONE MEASURE. TEAM WORK. SAID PRECISELY."])
short("SHORT 4","Practical test / action","LOOK UNDER THE TITLE",
 ["Reveal the instruction, then the repeated-verb step.",
  "Three moments, not three projects. That distinction is the whole Short.",
  "End on:  THE MOMENTS ARE WHY ANYONE BELIEVES YOU."])

H1(d,"All Shorts — boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["stock office B-roll;","generic résumé graphics;","employer logos;",
 "Field Kit imagery;","fake shock expressions;","countdown motifs;",
 "constant zooms;","AI-generated scenery;","social-media template effects."],
 after=3)
p=P(d,"And no generic motivation. Every Short has to leave the viewer with one "
     "thing they can actually check in their own work.",size=11,bold=True,
     color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
compress(d, 1.06, 0.34)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- 4. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 1 — v5.0 BELONGING + IDENTITY FINAL RECORDING PACKAGE","",
 "Public title:      %s"%TITLE,
 "On-screen",
 "deck title:        %s"%DECK_TITLE,
 "                   The two differ intentionally. Do not change the title",
 "                   slide to match the public title.",
 "Thumbnail:         %s"%THUMB,"",
 "Identity promise:  Become the professional who can enter a career change",
 "                   already knowing what is still theirs, what they can",
 "                   prove, and what they still have to learn.","",
 "Viewer recognition:Someone who has spent years getting good at their work",
 "                   and is now facing a change of job, function or industry,",
 "                   privately asking whether any of it still counts.","",
 "Memory structure:",
 "  Look underneath the title.",
 "  Explain what the work changed.",
 "  Keep evidence before you need it.","",
 "Primary CTA:       %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "Watch next:        %s (Video 2)"%NEXT,"",
 "Script:            Freshly written for v5.0. 1,727 spoken words, about",
 "                   11:54 at 145 words per minute.",
 "Slides:            UNCHANGED. All 13 slides were mapped against the new",
 "                   script and every one still serves it, so no slide text",
 "                   was changed.",
 "Reveal deck:       UNCHANGED. 22 frames.",
 "Speaker notes:     Rewritten for the v5.0 narration.",
 "Shorts:            All four rewritten for v5.0.",
 "Editor directions: Separated from recording copy.","",
 "-"*70,"","WHAT EACH FILE IS","","LONG_FORM/","",
 "  %s.docx"%TEL,"  %s.txt"%TEL,
 "      Temidayo's recording copy. Spoken script in large text; slide markers",
 "      in tinted bands. The markers are not spoken.","",
 "  %s.docx"%RDG,"  %s.txt"%RDG,
 "      The same spoken words with the slide markers removed.","",
 "  %s"%EDB,
 "      For the editor. Fourteen sections: locked metadata, the identity",
 "      promise, who is watching, belonging and lived proof, the first-30",
 "      H.I.T. map, hook layers, slide and reveal maps, visual assets,",
 "      factual boundaries, the do-not-use list, CTA and watch next, the",
 "      identity exit, the direct-address rule and the notes record.","",
 "  %s"%PUB,
 "      Title, thumbnail, search language, the copy-ready description,",
 "      working chapter estimates, pinned comment and tag field.","",
 "SHORTS/","",
 "  Four recording documents. Recording copy only, no editor directions.","",
 "  %s"%SEB,
 "      For the editor. Hooks and visual treatment for all four.","",
 "-"*70,"","ALL FILES IN THIS PACKAGE",""]
for f in FILES: R.append("  "+f)
R+=["  README_FINAL.txt","  SHA256SUMS.txt","",
 "-"*70,"","WHAT v5.0 CHANGED","",
 "This is a genuine editorial rebuild, not a patch. The spoken script was",
 "written fresh under the belonging-first, identity-transformation register:",
 "the viewer's situation and the question underneath it come first, Temidayo's",
 "own crossings follow as recognition rather than autobiography, and the three",
 "practices do not arrive until about 3:10, after the viewer has been seen.",
 "The video now ends on who the viewer is becoming, not only on what to do.","",
 "The prior v4.0 package is superseded. Its hashes are preserved in the",
 "change record:",
 "  package ZIP fe9d1d6a59705ff0fd212bc1cac038e9a32e1cf8fb49741477abf0edda3e3c41",
 "  main deck  bf3dee5f6ae946e1f25219bf13ca4d91250d52c18726e6f855c7bb4f97b490a1",
 "  reveal deck 27e575044b35348aa112aaeebf09ab50b65b22ba430cb5bd3905f3e998dcf955","",
 "-"*70,"","BOUNDARIES THAT DID NOT MOVE","",
 "The 47 to 75 figure is ONE measure of how well new hires felt integrated,",
 "from an onboarding redesign Temidayo LED WITH HER TEAM. Both qualifiers are",
 "spoken. The ~30% retention improvement and the >$2M avoided turnover figure",
 "are excluded and must never be added. \"Roughly eighteen years\" is approved",
 "wording. The December 2008 accounting degree and financial-crisis context",
 "stay exactly as spoken. The professional-certification non-pass stays a",
 "non-pass; no later result is implied. Not everything transfers, and the",
 "script says so.","",
 "The Free Career Evidence Starter is the only CTA. Slide 12 and reveal frame",
 "21 carry the real Starter artifact. No Field Kit imagery remains.","",
 "-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256",""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))

MANIFEST=["LONG_FORM/%s.docx"%TEL,"LONG_FORM/%s.txt"%TEL,
 "LONG_FORM/%s.docx"%RDG,"LONG_FORM/%s.txt"%RDG,
 "LONG_FORM/%s"%EDB,"LONG_FORM/%s"%PUB]+\
 ["SHORTS/"+f for f,_,_,_ in SHORTS]+["SHORTS/"+SEB,"README_FINAL.txt"]
ZIP=os.path.join(BASE,"Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip")
z=package(ROOT,MANIFEST,ZIP,"Video_1_HIT_FINAL",
  ["# VIDEO 1 - v5.0 BELONGING + IDENTITY FINAL RECORDING PACKAGE",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot carry its own",
   "# checksum either; it is published in the sibling file",
   "# Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"])
print("ZIP sha256:",z)
print("DESC sha256:",sha256(os.path.join(BASE,"Video_1_YouTube_Description_HIT.docx")))
