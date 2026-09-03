# -*- coding: utf-8 -*-
"""Build the Video 3 v4.0 recording and Shorts package."""
import os, sys, shutil
sys.path.insert(0,"/tmp/da"); sys.path.insert(0,"/tmp/da/v3")
from docxkit import *
from changereport import new_blocks

BASE="/tmp/da/v3"
ROOT=os.path.join(BASE,"Video_3_HIT_FINAL")
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

VID=3
TITLE="3 Things to Do Before Quitting Your Job"
THUMB="WAIT BEFORE YOU QUIT"
PRIMARY="things to do before quitting your job"
SUPPORTING=("before quitting your job · before you resign · career change · "
    "should I quit my job · career transition · career decision · "
    "transferable experience · career evidence · career portability")
CTA="Career Decision Evidence Check"
CTA_URL="https://temidayoafonja.com/career-decisions"
NEXT="How to Change Jobs Without Starting Your Career Over"

CANON=os.path.join(BASE,"canonical_v4.0.txt")
LINES=new_blocks(CANON,"BEGIN APPROVED VIDEO 3 v4.0 SCRIPT",
                       "END APPROVED VIDEO 3 v4.0 SCRIPT")
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]

TEL="Video3TeleprompterScriptwithslidemarkers_HIT_v4.0"
RDG="Video3ReadingScriptnomarkers_HIT_v4.0"
EDB="Video_3_EDITOR_ONLY_HIT_Brief_v4.0.docx"
PUB="Video_3_Publishing_Package_HIT_v4.0.docx"
SEB="Video_3_Shorts_EDITOR_ONLY_HIT_Brief.docx"
scripts(VID,TITLE,LINES,SPOKEN,LF,TEL,RDG)
print("long-form scripts written")

SLIDE_MAP=["Title","Once You Leave, Access Changes","01 Preserve the Evidence",
 "What to Keep / What Not to Take","02 Name What Your Work Built",
 "Problem / Constraint / Judgment / Outcome","03 Test the Next Move",
 "Uses Something Proven / Builds Something New","The Three Checks",
 "Decision Reading","Before You Resign","Career Decision Evidence Check",
 "Watch Next"]
REVEAL_MAP=[(1,"1",1),(2,"2",1),(3,"3",1),(4,"4–7",4),(5,"8",1),(6,"9–13",5),
 (7,"14",1),(8,"15–18",4),(9,"19",1),(10,"20–22",3),(11,"23–25",3),(12,"26",1),
 (13,"27",1)]
FRAMES=[1,1,1,4,1,5,1,4,1,3,3,1,1]

# ------------------------------------------------------ long-form editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 3  ·  v4.0",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in (("Title",TITLE),("Thumbnail",THUMB),("Primary search phrase",PRIMARY),
            ("Primary CTA",CTA),("CTA URL",CTA_URL),("Watch next",NEXT),
            ("Strategic job","Consequential decision / evidence check"),
            ("Core promise","Help the viewer make a cleaner decision before "
             "access changes."),
            ("Memory device","The three checks. No acronym, no second "
             "framework."),
            ("CTA production gate","SATISFIED")):
    keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
keep(P(d,"Do not add the Capability Formation Field Kit, Keep the Proof, the "
       "Career Evidence Starter or a second framework to this video.",
       bold=True,color=RED,after=8,spacing=1.25))
p=P(d,"THIS IS NOT “THREE REASONS NOT TO QUIT”. If leaving is right for this "
     "viewer, the video's job is to help them leave with clearer evidence and "
     "a better read of the next move. Never edit it into a case for staying.",
    size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

direct_address_section(d,"2.  Direct address is part of the creative",
 ["“If you’re going to quit your job…”",
  "“And that is what I want to help you do before you hand in your notice.”",
  "“Before I take you any further, I want to be very clear about one "
  "boundary.”",
  "“I am not trying to make you hesitate. I am trying to make sure you do not "
  "leave the meaning of your own experience behind.”",
  "“I am not trying to make your decision slow. I am trying to make it "
  "legible to you.”"])

H1(d,"3.  First 30 seconds — H.I.T. map",before=14)
P(d,"H = Hook. I = Interest. T = Trust. The opening must work as one "
    "audiovisual unit: immediate conversational hook, meaningful visual "
    "interest, relevant lived proof and a clear payoff by 30 seconds. No "
    "title card before the promise.",after=8)
p=P(d,"This supersedes the older Video 3 opening and any earlier instruction "
     "that kept Temidayo visually static or fully off-camera in the first 30 "
     "seconds.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

def beat(t,anchor,layer,body):
    H2(d,t,before=10)
    p=P(d,"Spoken anchor:  “%s”"%anchor,size=10.5,italic=True,color=DIM,after=8)
    shade(p,BAND_CREAM)
    if layer: keep(P(d,layer,size=11,bold=True,color=GOLD,after=6))
    for b in body: keep(P(d,b,after=5))

beat("0:00–0:12","If you’re going to quit your job, don’t wait until after "
     "you leave to work out what your work actually built in you.","H = HOOK",
     ["Visual: begin on Temidayo, direct to camera.",
      "On-screen text:  WAIT BEFORE YOU QUIT",
      "Do not use a title card before this.",
      "Then:  ACCESS CHANGES  ·  SYSTEMS CLOSE  ·  PEOPLE MOVE ON"])
beat("0:12–0:25","Before you resign, check three things: what you can "
     "preserve, what your work proved you can do, and what your next move "
     "needs to build.","I = INTEREST",
     ["Restrained three-item reveal. This is the promise of the video.",
      "Do not turn it into a countdown or a warning graphic."])
beat("0:25–0:31","I’ve worked inside systems where performance and talent "
     "decisions are documented, so I know how quickly that context can "
     "disappear.","T = TRUST",
     ["Stay on Temidayo. This is lived perspective, not a credential recital.",
      "FACTUAL BOUNDARY: no employer, client, system name, metric or result."])
beat("0:31–0:40","And if your health or safety is at risk, this is not a "
     "reason to wait.","SAFETY",
     ["This lands in the opening and it is not optional.",
      "Deliver it plainly and humanely. No legal-notice treatment, no fine "
      "print, no red alarm graphic, no cutaway.",
      "It is restated in full on slide 2. Do not cut either instance."])

H2(d,"First-30-second audit table",before=12)
keep(P(d,"Audited against the v4.0 standard. The existing opening passed on "
       "every criterion — the safety line already sits inside the first 30 "
       "seconds — so only the voice register was revised.",size=10.5,
       italic=True,color=DIM,after=8))
hit_table(d,[
 ["0:00–0:12",
  "“If you’re going to quit your job, don’t wait until after you leave to work "
  "out what your work actually built in you.”",
  "A real consequence the viewer is about to walk into.",
  "WAIT BEFORE YOU QUIT",
  "Open on Temidayo, direct to camera. No title card. Then ACCESS CHANGES · "
  "SYSTEMS CLOSE · PEOPLE MOVE ON.",
  "Spoken as a practitioner's warning, not a scare line.",
  "The viewer learns there is something to do before resigning."],
 ["0:12–0:25",
  "“Before you resign, check three things: what you can preserve, what your "
  "work proved you can do, and what your next move needs to build.”",
  "Direct offer of the method.",
  "3 CHECKS BEFORE YOU RESIGN",
  "Restrained three-item reveal. No countdown, no warning graphic.",
  "The three checks are the video's whole promise.",
  "Payoff is explicit by 25 seconds."],
 ["0:25–0:31",
  "“I’ve worked inside systems where performance and talent decisions are "
  "documented, so I know how quickly that context can disappear.”",
  "Lived organizational vantage point.",
  "—",
  "Stay on Temidayo. No B-roll.",
  "Observed evidence from inside performance and talent systems. No employer, "
  "client, metric or result.",
  "The viewer sees why she can read what disappears on exit."],
 ["0:31–0:40",
  "“And if your health or safety is at risk, this is not a reason to wait.”",
  "Boundary stated before any advice can be misapplied.",
  "—",
  "Plain and humane, on camera, with captions. No red alarm graphic, no fine "
  "print, no cutaway.",
  "She gives up the advice rather than risk harm.",
  "The viewer knows immediately whether the video applies to them."]])
keep(P(d,"Hook layers for the long-form:",size=10.5,bold=True,color=NAVY,
       before=10,after=5))
hook_block(d,
 "If you’re going to quit your job, don’t wait until after you leave to work "
 "out what your work actually built in you.",
 "WAIT BEFORE YOU QUIT",
 "Direct to camera, then the three-loss line, then the three checks.",
 "Temidayo's work inside documented performance and talent systems.",
 "Three checks to run before resigning, promised by 0:25.")

H1(d,"4.  Slide marker → actual slide number",before=14)
P(d,"The teleprompter carries thirteen slide markers. They map to the existing "
    "thirteen-slide deck in order, marker 1 to slide 1 through marker 13 to "
    "slide 13. Do not add, delete, redesign or reorder slides.",after=8)
for n,job in enumerate(SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"5.  Existing reveal-frame map",before=14)
P(d,"The reveal-build deck contains 27 frames. This is the inspected count "
    "from the actual file. Reveal visuals are unchanged.",after=8)
for n,rng,cnt in REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"6.  Overlay principle",before=14)
P(d,"When a visual can prove information more efficiently than Temidayo "
    "speaking it, let the visual carry it. Do not add spoken wording to "
    "duplicate slide copy, and do not add slide copy to duplicate her.",after=8)

H1(d,"7.  Safety and factual boundaries",before=14)
p=P(d,"SAFETY BOUNDARY — EXACT MEANING, EXACT PROMINENCE. If the viewer's "
     "health or safety is at risk, or they are dealing with harassment, "
     "discrimination or another urgent threat, nothing in this video is a "
     "reason to delay leaving. It appears in the opening, in full on slide 2, "
     "again in the decision reading and again in the pinned comment. Do not "
     "soften it, shorten it, move it later or cut any instance.",size=11,
     bold=True,color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
keep(P(d,"Deliver it humanely and directly. It is not a legal disclaimer and "
       "must not be edited to look like one.",bold=True,after=8,spacing=1.25))
p=P(d,"EVIDENCE BOUNDARY. “Preserve” never means taking company material. "
     "Confidential information, customer or employee data, proprietary "
     "documents and employer-owned material stay with the employer. The rule "
     "spoken on screen is: if you do not have the right to keep it, do not "
     "take it. Never edit around that line.",size=11,bold=True,color=RED,
     after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
pairlist(d,["no invented employer, client, metric or result;",
 "no pressure to stay;","no urgency or alarm graphics;",
 "no direction presented as a diagnosis;",
 "pay, benefits, caregiving and timing remain legitimate constraints."],after=3)

H1(d,"8.  CTA and watch next",before=14)
keep(P(d,"One product CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"Do not add the Capability Formation Field Kit, Keep the Proof or the "
       "Career Evidence Starter.",bold=True,after=6))
keep(P(d,"CTA production gate: SATISFIED. The page is live. One signed-out "
       "production check is still required before Video 3 is uploaded or "
       "scheduled: confirm it loads for a visitor who is not signed in and is "
       "not holding a preview link.",bold=True,color=NAVY,after=8,spacing=1.25))
keep(P(d,"Watch next: %s"%NEXT,bold=True,after=5))
keep(P(d,"Slide 13 carries the correct Video 1 title, “How to Change Jobs "
       "Without Starting Your Career Over”. It was inspected in this pass and "
       "matches the spoken route.",size=10.5,color=DIM,after=8,spacing=1.25))
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
 "Reveal deck: 27 notes parts rewritten, one per frame.",
 "Slide XML, geometry, typography, palette and media: unchanged.",
 "Timings are script-derived working estimates at 145 words per minute for "
 "the 1,251-word script. Replace them from the finished cut."],after=3)
compress(d, 1.04, 0.30)
d.save(os.path.join(LF,EDB))
print("editor brief written")

# --------------------------------------------------------- publishing package
CHAPTERS=[("00:00","Do not wait until after you leave"),
 ("00:31","The safety boundary"),
 ("00:55","Once you leave, access changes"),
 ("02:01","Check 1: Preserve the evidence"),
 ("03:07","Check 2: Name what your work built in you"),
 ("04:23","Check 3: Test the next move"),
 ("05:32","The three checks together"),
 ("05:51","Reading your decision"),
 ("07:07","Before you resign"),
 ("07:50","Career Decision Evidence Check"),
 ("08:14","Watch next")]
CHAPTER_LINES=["%s   %s"%(t,c) for t,c in CHAPTERS]

DESC=[
 "If you are seriously thinking about quitting your job, there are three "
 "things worth checking before you resign.",
 "In this video I show you how to preserve permitted evidence of your work, "
 "name what that work actually built in you, and test whether your next move "
 "uses something you have already proved while asking you to build something "
 "genuinely new.",
 "Your three checks are:",
 "✨ Preserve the evidence.",
 "✨ Name what the work built in you.",
 "✨ Test the next move.",
 "This is not advice to delay leaving an unsafe or harmful situation. If your "
 "health or safety is at risk, or you are facing harassment, discrimination "
 "or another urgent threat, act on that first.",
 "And preserving career evidence does not mean taking confidential, "
 "proprietary, customer, employee or employer-owned material. Keep only what "
 "you are entitled to retain.","",
 "🧭 CAREER DECISION EVIDENCE CHECK",
 "If you want a structured way to read the evidence behind a stay, move or "
 "leave decision:",
 CTA_URL,"",
 "▶️ WATCH NEXT",
 NEXT,"[ADD VIDEO 1 LINK]","",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "Temidayo Afonja helps experienced professionals understand what they can "
 "carry across roles, functions, employers and industries so they can make "
 "career pivots and internal moves without starting from zero."]

PINNED=["Before you resign, which of these three questions is hardest for you "
 "to answer?",
 "1. What evidence do I need to preserve now?",
 "2. What does my strongest evidence prove I can do?",
 "3. What must the next move use — and what must it build?",
 "And if your health or safety is at risk, you do not need to delay leaving "
 "in order to finish a career exercise."]

TAGS=("things to do before quitting your job, before you resign, should I "
 "quit my job, career change, career transition, career decision, "
 "quitting your job, career evidence, career portability, "
 "experienced professionals, Temidayo Afonja, Capability Formation")

def description_block(d, heading_before=14):
    H1(d,"INTERNAL NOTE — DO NOT PASTE INTO YOUTUBE",before=heading_before)
    p=P(d,"The restrained emoji system is part of the approved v4.0 standard: "
         "✨ teaching points, 🧭 CTA and resource, ⏱️ chapters, ▶️ Watch Next, "
         "🔗 Connect and Explore. Do not remove it and do not add more. The "
         "safety paragraph and the permitted-evidence paragraph are part of the "
         "public copy and must be pasted with it.",
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
    keep(P(d,"Identical to the eleven chapter lines inside the description above.",
           size=10.5,italic=True,color=DIM,after=8))
    for line in CHAPTER_LINES: keep(P(d,line,size=11,after=4))

d=newdoc()
head(d,VID,TITLE,"Video 3  ·  Publishing package  ·  v4.0",
     "Everything needed to upload. Working timestamps must be replaced with "
     "real ones from the finished edit.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
H1(d,"Supporting search language",before=14); P(d,SUPPORTING,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 1)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only. Do not put the full tag field in the "
       "public description.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
H1(d,"Publication gate",before=14)
keep(P(d,"The Career Decision Evidence Check page is confirmed live, so the "
       "gate is SATISFIED. One signed-out production check of the page is "
       "still required before Video 3 is uploaded or scheduled: confirm it "
       "loads for a visitor who is not signed in and is not holding a preview "
       "link.",bold=True,after=8,spacing=1.25))
compress(d, 1.04, 0.34)
d.save(os.path.join(LF,PUB))

d=newdoc()
head(d,VID,TITLE,"Video 3  ·  YouTube description",
     "Upload copy only. Everything below the end marker is internal and must "
     "not be pasted into YouTube.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 1)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.04, 0.34)
DESC_DOC=os.path.join(BASE,"Video_3_YouTube_Description_HIT.docx")
d.save(DESC_DOC)
print("publishing package and description-only document written")

# ---------------------------------------------------------------- 4. Shorts
from shorts_text import SHORTS
LABELS=["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]
for (fn,role,hook,copy),label in zip(SHORTS,LABELS):
    d=newdoc(True)
    P(d,"VIDEO 3 SHORT",size=10,bold=True,color=GOLD,after=4,caps=True)
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
P(d,"VIDEO 3 — FOUR STANDALONE SHORTS",size=18,bold=True,color=NAVY,after=8,
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
 "Video 3 added as the Related Video when available."])
direct_address_section(d,"Direct address is part of the creative",
 ["“So before you leave, write down the evidence you are permitted to keep.”",
  "“The better habit is the one I want you to build.”",
  "“Let me show you what working around performance and talent systems taught "
  "me.”",
  "“Before you resign, answer these three questions.”"])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 3",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition","BEFORE YOU LOSE THE CONTEXT",
 ["Visual:  ACCESS CHANGES  ·  SYSTEMS CLOSE  ·  PEOPLE MOVE ON",
  "Calm, not ominous. This is a recognition Short, not a warning.",
  "End on:  WRITE IT DOWN WHILE YOU CAN."])
short("SHORT 2","Distinction / myth","KEEP THE PROOF, NOT THE FILES",
 ["EVIDENCE BOUNDARY: this Short exists to draw the line. Nothing in the "
  "visual treatment may suggest copying, exporting or removing employer "
  "material.",
  "Show the four prompts as restrained text.",
  "End on:  IF YOU CANNOT KEEP IT, DO NOT TAKE IT."])
short("SHORT 3","Proof / perspective","CONTEXT DISAPPEARS FAST",
 ["FACTUAL BOUNDARY: no employer, client, system name, metric or result. The "
  "proof is only that Temidayo has worked around performance and talent "
  "systems.",
  "“Let me show you what working around performance and talent systems taught "
  "me” opens the Short. Stay on her face for it.",
  "End on:  CAPTURE WHAT IT PROVED YOU CAN DO."])
short("SHORT 4","Practical test / action","3 QUESTIONS BEFORE YOU RESIGN",
 ["Reveal the three questions one at a time.",
  "The closing safety line is not optional and is not fine print. Deliver it "
  "plainly, on camera, with captions.",
  "End on:  DO YOU KNOW WHAT YOU ARE LEAVING WITH?"])

H1(d,"All Shorts — visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["stock office B-roll;","resignation-letter or exit-door clichés;",
 "employer logos;","red warning graphics;","fake shock expressions;",
 "countdown or alarm motifs;","constant zooms;","AI-generated scenery;",
 "social-media template effects."],after=3)
p=P(d,"And nothing in any Short may read as pressure to stay, or as "
     "encouragement to take employer material.",size=11,bold=True,color=RED,
     after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
compress(d, 1.06, 0.34)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- 6. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 3 — FINAL RECORDING PACKAGE v4.0","",
 "Title:             %s"%TITLE,
 "Thumbnail:         %s"%THUMB,
 "Strategic job:     Consequential decision / evidence check",
 "Core promise:      Help you make a cleaner decision before access changes.","",
 "Voice:             Temidayo speaks to one experienced professional, not an",
 "                   abstract audience. The relationship is trusted",
 "                   practitioner to one viewer, never lecturer to a crowd.","",
 "Safety boundary:   If your health or safety is at risk, or you are facing",
 "                   harassment, discrimination or another urgent threat,",
 "                   nothing in this video is a reason to delay leaving. It",
 "                   is spoken in the opening, in full on slide 2, again in",
 "                   the decision reading and again in the pinned comment.",
 "                   Do not soften, shorten, move or cut any instance.","",
 "Evidence boundary: Preserve never means taking company material. Keep only",
 "                   what you are entitled to keep.","",
 "Memory structure:",
 "  Preserve the evidence.",
 "  Name what the work built in you.",
 "  Test the next move.","",
 "Primary CTA:       %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "CTA production",
 "gate:              SATISFIED",
 "Watch next:        %s (Video 1)"%NEXT,"",
 "Slides:            Visual design and on-slide copy unchanged. 13 main",
 "                   slides.",
 "Speaker notes:     Updated for v4.0.",
 "Reveal deck:       Visual design and reveal states unchanged. 27 frames.",
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
 "This is a VOICE revision, not a rebuild. The three checks, every substantive",
 "claim, the safety boundary, the permitted-evidence boundary, the single CTA",
 "and the Watch Next route are all unchanged. 65 of the 108 prior spoken",
 "paragraphs are carried over verbatim; 44 were rewritten so that Temidayo is",
 "speaking to one experienced professional rather than to an abstract",
 "audience. No paragraph was deleted and no new claim was added.","",
 "Prior locked package: v2.0, spoken word count 1,205,",
 "                      ZIP 2455a0d08105e3148215191e62ead6204c8e4cdf896525592a2983b8c14ea177.",
 "This package:         v4.0, spoken word count 1,251.","",
 "-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_3_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256",""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))

MANIFEST=["LONG_FORM/%s.docx"%TEL,"LONG_FORM/%s.txt"%TEL,
 "LONG_FORM/%s.docx"%RDG,"LONG_FORM/%s.txt"%RDG,
 "LONG_FORM/%s"%EDB,"LONG_FORM/%s"%PUB]+\
 ["SHORTS/"+f for f,_,_,_ in SHORTS]+["SHORTS/"+SEB,"README_FINAL.txt"]
ZIP=os.path.join(BASE,"Video_3_HIT_FINAL_Recording_and_Shorts_Package.zip")
z=package(ROOT,MANIFEST,ZIP,"Video_3_HIT_FINAL",
  ["# VIDEO 3 - FINAL RECORDING PACKAGE v4.0",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
   "# checksum either; it is published in the sibling file",
   "# Video_3_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"])
print("ZIP sha256:",z)
print("DESC-ONLY sha256:",sha256(DESC_DOC))
