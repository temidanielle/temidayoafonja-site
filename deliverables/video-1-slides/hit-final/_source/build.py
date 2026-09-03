# -*- coding: utf-8 -*-
"""Build the Video 1 v4.0 recording and Shorts package."""
import os, sys, shutil
sys.path.insert(0,"/tmp/da"); sys.path.insert(0,"/tmp/v4/v1")
from docxkit import *
from changereport import new_blocks

BASE="/tmp/v4/v1"
ROOT=os.path.join(BASE,"Video_1_HIT_FINAL")
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

VID=1
TITLE="How to Change Jobs Without Starting Your Career Over"
THUMB="DON’T START FROM ZERO"
PRIMARY="how to change jobs without starting over"
DECK_TITLE="How I Changed Jobs Without Starting My Career Over"
SUPPORTING=("change jobs without starting over · transferable skills · "
    "career change · career pivot · transferable experience · "
    "career portability · career evidence · internal mobility")
CTA="Free Career Evidence Starter"
CTA_URL="https://temidayoafonja.com/career-evidence-starter"
NEXT="Is Your Job Making You Less Marketable?"

CANON=os.path.join(BASE,"canonical_v4.0.txt")
LINES=new_blocks(CANON,"BEGIN APPROVED VIDEO 1 v4.0 SCRIPT",
                       "END APPROVED VIDEO 1 v4.0 SCRIPT")
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]

TEL="Video1TeleprompterScriptwithslidemarkers_HIT_v4.0"
RDG="Video1ReadingScriptnomarkers_HIT_v4.0"
EDB="Video_1_EDITOR_ONLY_HIT_Brief_v4.0.docx"
PUB="Video_1_Publishing_Package_HIT_v4.0.docx"
SEB="Video_1_Shorts_EDITOR_ONLY_HIT_Brief.docx"
scripts(VID,TITLE,LINES,SPOKEN,LF,TEL,RDG)
print("long-form scripts written")

SLIDE_MAP=["Title","My Career Path","01 Look Underneath the Title","Move One",
 "02 Explain What the Work Changed","Move Two","One Result — 47 to 75",
 "03 Keep Evidence Before You Need It","Move Three",
 "Three Things I Learned to Do","Before Your Next Move",
 "Career Evidence Starter","Watch Next"]
REVEAL_MAP=[(1,"1",1),(2,"2",1),(3,"3",1),(4,"4–6",3),(5,"7",1),(6,"8–9",2),
 (7,"10–11",2),(8,"12",1),(9,"13–16",4),(10,"17",1),(11,"18–20",3),(12,"21",1),
 (13,"22",1)]
FRAMES=[1,1,1,3,1,2,2,1,4,1,3,1,1]

# ------------------------------------------------------ long-form editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 1  ·  v4.0",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in (("Public title",TITLE),("On-screen deck title",DECK_TITLE),
            ("Thumbnail",THUMB),("Primary search phrase",PRIMARY),
            ("Primary CTA",CTA),("CTA URL",CTA_URL),("Watch next",NEXT),
            ("Strategic job","Searchable front door + personal proof"),
            ("Core question","What has my experience built that could still "
             "be useful elsewhere?"),
            ("Memory device","The three practices. No acronym, no second "
             "framework.")):
    keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
keep(P(d,"The two titles differ intentionally. Do not change the title slide "
       "to match the public metadata title.",bold=True,after=6,spacing=1.25))
keep(P(d,"Do not add the Capability Formation Field Kit, Keep the Proof, the "
       "Career Evidence 3 Cs or any second framework to this video.",
       bold=True,color=RED,after=8,spacing=1.25))


direct_address_section(d,"2.  Direct address is part of the creative",
 ["“Let me show you three things I use…”",
  "“And I want to be clear with you about the promise.”",
  "“That is the question I want to help you answer.”",
  "“The questions on screen are the ones I use, and I want you to use them "
  "too.”",
  "“Let me show you the more useful version…”",
  "“And I want to be precise with you.”"])

H1(d,"3.  First 30 seconds — H.I.T. map",before=14)
P(d,"H = Hook. I = Interest. T = Trust. The opening must work as one "
    "audiovisual unit: immediate conversational hook, meaningful visual "
    "interest, relevant lived proof and a clear payoff by 30 seconds. No "
    "title card before the promise.",after=8)
p=P(d,"This supersedes the older Video 1 opening and any earlier instruction "
     "that kept Temidayo visually static or fully off-camera in the first 30 "
     "seconds.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

def beat(t,anchor,layer,body):
    H2(d,t,before=10)
    p=P(d,"Spoken anchor:  “%s”"%anchor,size=10.5,italic=True,color=DIM,after=8)
    shade(p,BAND_CREAM)
    if layer: keep(P(d,layer,size=11,bold=True,color=GOLD,after=6))
    for b in body: keep(P(d,b,after=5))

beat("0:00–0:10","Changing jobs can make years of your experience feel as "
     "though they belong to the place you are leaving.","H = HOOK",
     ["Visual: begin on Temidayo, direct to camera.",
      "On-screen text:  DON’T START FROM ZERO",
      "Do not use a title card before this."])
beat("0:10–0:16","But a new context does not make you new to everything.",
     "I = INTEREST",
     ["The correction to the hook. Let it land before the proof arrives.",
      "Optional restrained text:  NEW CONTEXT ≠ NEW TO EVERYTHING"])
beat("0:16–0:26","Over roughly eighteen years, my career has crossed very "
     "different functions and industries, so I had to learn what actually "
     "travels.","T = TRUST",
     ["Restrained career-sequence overlay. Short labels only.",
      "“Roughly eighteen years” is APPROVED wording. It is not an open "
      "question and must not be softened or made precise.",
      "Temidayo does not recite the chapters aloud; the visual carries them."])
beat("0:26–0:33","Let me show you three things I use…","PAYOFF",
     ["Progressively reveal the three practices.",
      "Optional small text: 3 PRACTICES",
      "The viewer should understand the payoff before the teaching begins."])

H2(d,"First-30-second audit table",before=12)
keep(P(d,"Audited against the v4.0 standard. The existing opening passed on "
       "title and thumbnail match, one-breath first sentence, recognition, "
       "visual interest, trust and payoff inside 30 seconds. It failed only "
       "the direct-address register, so the beats below carry the revised "
       "wording.",size=10.5,italic=True,color=DIM,after=8))
hit_table(d,[
 ["0:00–0:10",
  "“Changing jobs can make years of your experience feel as though they belong "
  "to the place you are leaving.”",
  "A consequence the viewer may already be feeling.",
  "DON’T START FROM ZERO",
  "Open on Temidayo, direct to camera. No title card.",
  "Named as a felt experience, not a statistic.",
  "The viewer recognises the fear the video will address."],
 ["0:10–0:16",
  "“But a new context does not make you new to everything.”",
  "The correction; a defensible contradiction of the fear.",
  "NEW CONTEXT ≠ NEW TO EVERYTHING",
  "Let it land before the proof arrives.",
  "Stated as her considered position.",
  "The viewer hears that the premise is wrong."],
 ["0:16–0:26",
  "“Over roughly eighteen years, my career has crossed very different "
  "functions and industries, so I had to learn what actually travels.”",
  "Personal-story proof for the correction.",
  "ACCOUNTING → CYBERSECURITY → PEOPLE STRATEGY",
  "Restrained career-sequence overlay. Not recited aloud.",
  "Roughly eighteen years across very different functions and industries.",
  "The viewer sees why she can answer this question."],
 ["0:26–0:33",
  "“Let me show you three things I use…”",
  "Direct offer: her practices become the viewer's.",
  "3 PRACTICES",
  "Progressive reveal, then into the deck.",
  "The practices are derived from her own transitions.",
  "Payoff is explicit before 33 seconds."]])
keep(P(d,"Hook layers for the long-form:",size=10.5,bold=True,color=NAVY,
       before=10,after=5))
hook_block(d,
 "Changing jobs can make years of your experience feel as though they belong "
 "to the place you are leaving.",
 "DON’T START FROM ZERO",
 "Direct to camera, then the restrained career-sequence overlay.",
 "Roughly eighteen years across very different functions and industries, and "
 "the bounded 47 to 75 onboarding measure later in the video.",
 "Three practices for carrying experience forward, promised by 0:33.")

H1(d,"4.  Slide marker → actual slide number",before=14)
P(d,"The teleprompter carries thirteen slide markers. They map to the existing "
    "thirteen-slide deck in order, marker 1 to slide 1 through marker 13 to "
    "slide 13. Do not add, delete, redesign or reorder slides.",after=8)
for n,job in enumerate(SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"5.  Existing reveal-frame map",before=14)
P(d,"The reveal-build deck contains 22 frames. This is the inspected count "
    "from the actual file. Reveal visuals are unchanged.",after=8)
for n,rng,cnt in REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"6.  Overlay principle",before=14)
P(d,"When a visual can prove information more efficiently than Temidayo "
    "speaking it, let the visual carry it. Do not add spoken wording to "
    "duplicate slide copy, and do not add slide copy to duplicate her.",after=8)

H1(d,"7.  Factual boundaries",before=14)
p=P(d,"THE 47 TO 75 MEASURE IS BOUNDED. It is ONE measure of how well new "
     "hires felt integrated, after an onboarding redesign Temidayo LED WITH "
     "HER TEAM. It is not a claim about everything the redesign affected and "
     "not something she did alone. The script states both qualifiers out loud; "
     "do not trim either.",size=11,bold=True,color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
p=P(d,"EXCLUDED CLAIMS. The ~30% retention improvement and the >$2M avoided "
     "turnover figure are NOT in this video and must never be added to it or "
     "to any graphic, caption or thumbnail.",size=11,bold=True,color=RED,
     after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,"“Roughly eighteen years” is approved wording and is not an open "
       "question. Do not make it precise and do not soften it.",bold=True,
       after=6,spacing=1.25))
P(d,"Also hold:",after=5)
pairlist(d,["the relearning boundary — not everything transfers;",
 "December 2008 accounting degree and financial-crisis context as spoken;",
 "no employer named;","no invented assignment, quote or conversation;",
 "the permitted, non-confidential record boundary;",
 "the narrowest-capability rule on the what-this-shows line."],after=3)

H1(d,"8.  CTA and watch next",before=14)
keep(P(d,"One product CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"Use the direct public landing-page URL only. Do not expose a PDF "
       "link, and do not restore the Capability Formation Field Kit.",
       bold=True,after=6))
keep(P(d,"Slide 12 and reveal frame 21 carry the REAL Career Evidence Starter "
       "artifact: the cover in front, the Portable Proof Line page behind. No "
       "Field Kit imagery remains anywhere in either deck. Do not restore it.",
       bold=True,color=NAVY,after=8,spacing=1.25))
keep(P(d,"Watch next: %s"%NEXT,bold=True,after=5))
keep(P(d,"Slide 13 carries the correct Video 2 title, “Is Your Job Making You "
       "Less Marketable?”. It was inspected in this pass and matches the "
       "spoken route.",size=10.5,color=DIM,after=8,spacing=1.25))
keep(P(d,"Do not leave Subscribe as the only end-screen element.",bold=True,
       color=RED,after=8))

H1(d,"9.  Editing rhythm after 0:30",before=14)
P(d,"The opening is intentionally more visually active than the rest of the "
    "video. Do NOT read H.I.T. as permission to keep that density running. "
    "Once the viewer is inside the teaching, the edit should feel premium, "
    "calm and editorial.",after=8)
pairlist(d,["preserve Temidayo's natural pacing;","use the slides as support;",
 "avoid decorative motion;","avoid constant punch-ins;",
 "avoid stock office footage;","avoid generic résumé B-roll;",
 "avoid red warning graphics;","avoid fake urgency;",
 "avoid flashy transitions."],after=3)

H1(d,"10.  Visual “do not use” list",before=14)
pairlist(d,["stock office B-roll;","generic résumé graphics;",
 "employer logos;","red warning graphics;","fake shock expressions;",
 "countdown or alarm motifs;","constant zooms;","AI-generated scenery;",
 "social-media template effects."],after=3)

H1(d,"11.  Speaker-note update record",before=14)
P(d,"Both decks ship with speaker notes rewritten for the v3.0 direct-address "
    "script. Nothing on any slide was changed.",after=8)
pairlist(d,["Main deck: 13 notes parts rewritten, one per slide.",
 "Reveal deck: 22 notes parts rewritten, one per frame.",
 "Slide XML, geometry, typography, palette and media: unchanged.",
 "Timings are script-derived working estimates at 145 words per minute for "
 "the 1,409-word script. Replace them from the finished cut."],after=3)
compress(d, 1.10, 0.40)
d.save(os.path.join(LF,EDB))
print("editor brief written")

# --------------------------------------------------------- publishing package
CHAPTERS=[("00:00","Change Jobs Without Starting Over"),
 ("01:09","What My Career Shifts Taught Me"),
 ("02:15","Look Beyond Job Titles"),
 ("02:19","Three Questions That Reveal Transferable Skills"),
 ("04:03","Translate Your Impact"),
 ("05:45","Preserve Career Evidence Early"),
 ("07:51","Three Questions Before Your Next Move"),
 ("08:43","Free Career Evidence Starter"),
 ("09:01","Is Your Job Making You Less Marketable?")]
CHAPTER_LINES=["%s %s"%(t,c) for t,c in CHAPTERS]

DESC=[
 "I’m Temidayo Afonja, founder of The Density Group and creator of Capability "
 "Formation. I help experienced professionals understand what they can carry "
 "across roles, functions, employers and industries so they can make career "
 "pivots and internal moves without starting from zero.",
 "In this video I share three things that helped me change jobs without "
 "treating every transition as a return to zero:",
 "✨ Look underneath the job title and identify what your work trained you to "
 "notice, decide and solve.",
 "✨ Explain what your work changed in language another employer can "
 "understand.",
 "✨ Preserve permitted evidence before you need a résumé, interview story or "
 "promotion case.",
 "Not everything transfers. A new role, employer or industry may require real "
 "relearning. But a new context does not make you new to everything.",
 "I also share one carefully bounded example from my own work: an onboarding "
 "redesign I led with my team, where one measure of how well new hires felt "
 "integrated moved from 47 to 75.",
 "What has your work built in you—and what could you still do if the title, "
 "employer or industry changed?","",
 "🧭 FREE CAREER EVIDENCE STARTER",
 "Turn one accomplishment into a portable Proof Line you can use in a "
 "performance review, interview, internal move or career pivot:",
 CTA_URL,"",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "▶️ WATCH NEXT",
 NEXT,"[ADD VIDEO 2 LINK WHEN LIVE]","",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "#CareerGrowth #CareerChange #TransferableSkills"]

PINNED=["Which of the three practices is hardest for you right now?",
 "1. Look underneath the title",
 "2. Explain what the work changed",
 "3. Keep evidence before you need it",
 "Try the third one today. Write four lines about one piece of work: the "
 "situation, your role, what changed, and what it shows — in your own words, "
 "nothing confidential.",
 "And if you want to turn one accomplishment into a portable Proof Line, the "
 "free Career Evidence Starter is here:", CTA_URL]

TAGS=("how to change jobs without starting over, transferable skills, "
 "career change, career pivot, changing careers, transferable experience, "
 "career portability, career evidence, internal mobility, starting over, "
 "experienced professionals, Temidayo Afonja, Capability Formation")

def description_block(d, heading_before=14):
    H1(d,"INTERNAL NOTE — DO NOT PASTE INTO YOUTUBE",before=heading_before)
    p=P(d,"The restrained emoji system is part of the approved v4.0 standard: "
         "✨ teaching points, 🧭 CTA and resource, ⏱️ chapters, ▶️ Watch Next, "
         "🔗 Connect and Explore. Do not remove it and do not add more.",
        size=10.5,italic=True,color=RED,after=12,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    p=keep(P(d,"COPY-READY YOUTUBE DESCRIPTION — BEGIN",size=11,bold=True,
             color=NAVY,before=14,after=12,spacing=1.2))
    shade(p,BAND_NAVY)
    for para in DESC: keep(P(d,para if para else " ",after=7 if para else 3))
    keep(P(d,"— END OF COPY-READY DESCRIPTION —",size=10,bold=True,color=DIM,
           before=14,after=12,spacing=1.2))
    H1(d,"Internal note — do not paste into YouTube",before=14)
    p=P(d,"WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT",size=11,
        bold=True,color=RED,after=6,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    p=P(d,"These timestamps are script-derived, not measured from the finished "
        "edit. Replace every one of them before publication. Do not force the "
        "edit to match them.",size=10.5,bold=True,italic=True,color=RED,
        after=10,spacing=1.25)
    shade(p,BAND_CREAM); keep(p)
    H1(d,"Working chapters — reference copy",before=14)
    keep(P(d,"Identical to the nine chapter lines inside the description above.",
           size=10.5,italic=True,color=DIM,after=8))
    for line in CHAPTER_LINES: keep(P(d,line,size=11,after=4))

d=newdoc()
head(d,VID,TITLE,"Video 1  ·  Publishing package  ·  v4.0",
     "Everything needed to upload. Working timestamps must be replaced with "
     "real ones from the finished edit.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
keep(P(d,"On-screen deck title (intentionally different): %s"%DECK_TITLE,
       size=10.5,color=DIM,after=10))
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
H1(d,"Supporting search language",before=14); P(d,SUPPORTING,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 2)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only. Do not put the full tag field in the "
       "public description.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
d.save(os.path.join(LF,PUB))

d=newdoc()
head(d,VID,TITLE,"Video 1  ·  YouTube description",
     "Upload copy only. Everything below the end marker is internal and must "
     "not be pasted into YouTube.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
keep(P(d,"On-screen deck title (intentionally different): %s"%DECK_TITLE,
       size=10.5,color=DIM,after=10))
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 2)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
DESC_DOC=os.path.join(BASE,"Video_1_YouTube_Description_HIT.docx")
d.save(DESC_DOC)
print("publishing package and description-only document written")

# ---------------------------------------------------------------- 4. Shorts
from shorts_text import SHORTS
LABELS=["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]
for (fn,role,hook,copy),label in zip(SHORTS,LABELS):
    d=newdoc(True)
    P(d,"VIDEO 1 SHORT",size=10,bold=True,color=GOLD,after=4,caps=True)
    P(d,label,size=20,bold=True,color=NAVY,after=8,spacing=1.1)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    keep(P(d,"Verbal hook:  “%s”"%hook,size=11,color=DIM,after=5))
    keep(P(d,"Related long-form:  %s"%TITLE,size=11,color=DIM,after=10))
    H1(d,"RECORDING COPY",before=12)
    for line in copy:
        keep(P(d,line,size=13.5,color=INK,after=10,spacing=1.5))
    d.save(os.path.join(SH,fn))

# ------------------------------------------------------ 5. Shorts editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 1 — FOUR STANDALONE SHORTS",size=18,bold=True,color=NAVY,after=8,
  spacing=1.1)
p=P(d,"This document is for the editor. It is separate from the four Short "
     "recording documents and must not be placed on Temidayo's recording "
     "screen.",size=11,italic=True,color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)
H1(d,"How these are produced",before=14)
keep(P(d,"These are separately recorded 9:16 Shorts. They are NOT excerpts cut "
       "from the long-form video.",bold=True,after=10))
P(d,"Each Short needs:",after=6)
pairlist(d,["an immediate verbal hook;","a corresponding on-screen hook;",
 "meaningful visual movement;","accurate mobile-safe captions;",
 "premium, restrained editorial pacing;",
 "Video 1 added as the Related Video when available."])
direct_address_section(d,"Direct address is part of the creative",
 ["“So before you call yourself a beginner, ask…”",
  "“I want you to ask…”",
  "“Let me show you why a project name is not proof of your value.”",
  "“Underneath it, I want you to answer three questions.”"])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 1",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition","NEW CONTEXT ≠ NEW TO EVERYTHING",
 ["Visual:  NEW COMPANY  /  NOT NEW TO EVERY PROBLEM",
  "Keep the relearning boundary. This Short must not promise that everything "
  "transfers.",
  "End on:  WHAT CAN I CARRY?"])
short("SHORT 2","Distinction / myth","EXPERIENCE ≠ EVIDENCE",
 ["Restrained two-column contrast. No résumé-scroll animation.",
  "End on:  WHERE HAVE I DEMONSTRATED IT?"])
short("SHORT 3","Proof / personal evidence","47 → 75",
 ["FACTUAL BOUNDARY: ONE measure of new-hire integration, from a redesign "
  "Temidayo LED WITH HER TEAM. No employer named, no 30% retention figure, no "
  "$2M figure, no extra outcome.",
  "Show the before and after as restrained text, exactly as on slide 7.",
  "End on:  ONE MEASURE. TEAM WORK. STATED PRECISELY."])
short("SHORT 4","Practical test / action","LOOK UNDER THE TITLE",
 ["Reveal the three questions one at a time.",
  "Then the repeating-verb step. Do not turn the verb list into a personality "
  "quiz.",
  "End on:  ATTACH IT TO EVIDENCE."])

H1(d,"All Shorts — visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["stock office B-roll;","generic résumé graphics;","employer logos;",
 "Field Kit imagery;","fake shock expressions;","countdown motifs;",
 "constant zooms;","AI-generated scenery;","social-media template effects."],
 after=3)
compress(d, 1.12, 0.46)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- 6. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 1 — FINAL RECORDING PACKAGE v4.0","",
 "Title:             %s"%TITLE,
 "Thumbnail:         %s"%THUMB,
 "                   SUPERSEDES \"YOUR SKILLS ARE STALLING\". The thumbnail",
 "                   artwork in the repository still carries the old words:",
 "                   SUPERSEDED - REPLACE WITH APPROVED CANVA EXPORT BEFORE",
 "                   PUBLISHING.",
 "Public title:      %s"%TITLE,
 "On-screen",
 "deck title:        %s"%DECK_TITLE,
 "                   The two differ intentionally. Do not change the title",
 "                   slide to match the public metadata title.",
 "Strategic job:     Searchable front door + personal proof",
 "Core question:     What has my experience built that could still be useful",
 "                   elsewhere?","",
 "Voice:             Temidayo speaks to one experienced professional, not an",
 "                   abstract audience. The relationship is trusted",
 "                   practitioner to one viewer, never lecturer to a crowd.","",
 "Personal proof:    Roughly eighteen years across very different functions",
 "                   and industries, and one bounded result: ONE measure of",
 "                   how well new hires felt integrated moved from 47 to 75",
 "                   after an onboarding redesign Temidayo LED WITH HER TEAM.",
 "                   No 30% retention figure. No $2M figure. No employer",
 "                   named.","",
 "Memory structure:",
 "  Look underneath the title.",
 "  Explain what the work changed.",
 "  Keep evidence before you need it.","",
 "Primary CTA:       %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "Watch next:        %s"%NEXT,"",
 "Slides:            Visual design and on-slide copy unchanged. 13 main",
 "                   slides.",
 "Speaker notes:     Updated for v4.0.",
 "Reveal deck:       Visual design and reveal states unchanged. 22 frames.",
 "Shorts:            Four separately recorded scripts, revised for direct",
 "                   address.",
 "Description-only",
 "document:          Separate from this ZIP.",
 "Editor directions: Separated from recording copy.","",
 "-"*70,"","WHAT EACH FILE IS","","LONG_FORM/","",
 "  %s.docx"%TEL,"  %s.txt"%TEL,
 "      Temidayo's recording copy. Spoken script in large text; slide markers",
 "      in tinted bands. The markers are not spoken.","",
 "  %s.docx"%RDG,"  %s.txt"%RDG,
 "      The same spoken words with the slide markers removed.","",
 "  %s"%EDB,
 "      For the editor. Locked metadata, the direct-address register, the",
 "      H.I.T. first-30-second map, the slide and reveal maps, the overlay",
 "      principle, the factual and tone boundaries, CTA and watch-next",
 "      routing, editing rhythm, the visual do-not-use list and the",
 "      speaker-note record. Not for the teleprompter.","",
 "  %s"%PUB,
 "      Title, thumbnail, search language, the copy-ready description,",
 "      working chapter estimates and the pinned comment.","",
 "SHORTS/","",
 "  Four recording documents, one per Short. These contain Temidayo's",
 "  recording copy and no editor directions.","",
 "  %s"%SEB,
 "      For the editor. On-screen hooks and visual treatment for all four.","",
 "-"*70,"","ALL FILES IN THIS PACKAGE",""]
for f in FILES: R.append("  "+f)
R+=["  README_FINAL.txt","  SHA256SUMS.txt","",
 "-"*70,"","WORKING CHAPTER TIMESTAMPS","",
 "The chapter timestamps in the publishing package are WORKING ESTIMATES",
 "derived from the script. They were not measured from an edit. The editor",
 "must replace every one of them from the finished cut before publishing.","",
 "-"*70,"","WHAT THIS REVISION CHANGED","",
 "This is a VOICE revision, not a rebuild. The three practices, every",
 "substantive claim, the 47 to 75 boundary, the relearning boundary, the",
 "single CTA and the Watch Next route are all unchanged. 70 of the 111 prior",
 "spoken paragraphs are carried over verbatim; 41 were rewritten so that",
 "Temidayo is speaking to one experienced professional rather than to an",
 "abstract audience. No paragraph was deleted and no new claim was added.","",
 "Prior locked package: v3.1, spoken word count 1,329,",
 "                      ZIP 17e881ea97774f0d4a9e080f2077b093b6367f6f3ce14e22fe119ceb17a793e6.",
 "This package:         v4.0, spoken word count 1,409.","",
 "-"*70,"","BOUNDARIES THAT DID NOT MOVE","",
 "The 47 to 75 figure is ONE measure of how well new hires felt integrated,",
 "from an onboarding redesign Temidayo LED WITH HER TEAM. Both qualifiers are",
 "spoken out loud. The ~30% retention improvement and the >$2M avoided",
 "turnover figure are excluded from this video and must never be added.",
 "\"Roughly eighteen years\" is approved wording and is not an open question.",
 "Not everything transfers; the relearning boundary stays.","",
 "The Free Career Evidence Starter is the only CTA. Slide 12 and reveal frame",
 "21 carry the real Starter artifact. No Field Kit imagery remains anywhere.","",
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
  ["# VIDEO 1 - FINAL RECORDING PACKAGE v4.0",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
   "# checksum either; it is published in the sibling file",
   "# Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"])
print("ZIP sha256:",z)
print("DESC-ONLY sha256:",sha256(DESC_DOC))
