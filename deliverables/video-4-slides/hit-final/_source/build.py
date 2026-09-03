# -*- coding: utf-8 -*-
"""Build the Video 4 v4.0 recording and Shorts package."""
import os, sys, shutil
sys.path.insert(0,"/tmp/da"); sys.path.insert(0,"/tmp/da/v4")
from docxkit import *
from changereport import new_blocks

BASE="/tmp/da/v4"
ROOT=os.path.join(BASE,"Video_4_HIT_FINAL")
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

VID=4
TITLE="How to Explain Your Career Change"
THUMB="YOUR CAREER MAKES SENSE"
PRIMARY="how to explain your career change"
SUPPORTING=("how to explain a nonlinear career · nonlinear career path · "
    "career pivot · career story · transferable skills · career transition · "
    "career portability")
CTA="Free Career Evidence Starter"
CTA_URL="https://temidayoafonja.com/career-evidence-starter"
NEXT="Should I Make an Internal Move? 3 Questions to Decide"

CANON=os.path.join(BASE,"canonical_v4.0.txt")
LINES=new_blocks(CANON,"BEGIN APPROVED VIDEO 4 v4.0 SCRIPT",
                       "END APPROVED VIDEO 4 v4.0 SCRIPT")
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]

TEL="Video4TeleprompterScriptwithslidemarkers_HIT_v4.0"
RDG="Video4ReadingScriptnomarkers_HIT_v4.0"
EDB="Video_4_EDITOR_ONLY_HIT_Brief_v4.0.docx"
PUB="Video_4_Publishing_Package_HIT_v4.0.docx"
SEB="Video_4_Shorts_EDITOR_ONLY_HIT_Brief.docx"
scripts(VID,TITLE,LINES,SPOKEN,LF,TEL,RDG)
print("long-form scripts written")

SLIDE_MAP=["Career Path","Chronology / Portability","1 Name the Chapters Briefly",
 "2 Find the Repeated Work","Look Beneath the Nouns","3 Explain the Direction",
 "Three-Sentence Structure","Do Not Invent a Perfect Plan","Explanation Test",
 "Career Evidence Starter","Watch Next"]
REVEAL_MAP=[(1,"1–4",4),(2,"5–6",2),(3,"7",1),(4,"8–12",5),(5,"13–14",2),
 (6,"15–17",3),(7,"18–20",3),(8,"21",1),(9,"22–24",3),(10,"25",1),(11,"26",1)]
FRAMES=[4,2,1,5,2,3,3,1,3,1,1]

# ------------------------------------------------------ long-form editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 4  ·  v4.0",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in (("Title",TITLE),("Thumbnail",THUMB),("Primary search phrase",PRIMARY),
            ("Primary CTA",CTA),("CTA URL",CTA_URL),("Watch next",NEXT),
            ("Strategic job","Searchable problem + personal evidence"),
            ("Core distinction","CHRONOLOGY tells where you have been. A "
             "PORTABILITY EXPLANATION shows what travelled."),
            ("Memory device","The three-sentence career explanation. No "
             "acronym, no second framework.")):
    keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
keep(P(d,"Do not restore Keep the Proof as the CTA. Do not add the Capability "
       "Formation Field Kit, CAR, the Career Evidence 3 Cs or any second "
       "framework to this video.",bold=True,color=RED,after=8,spacing=1.25))

direct_address_section(d,"2.  Direct address is part of the creative",
 ["“So if your career looks disconnected on paper, let me show you how I "
  "learned to explain mine.”",
  "“There are three parts, and I want to walk you through each one.”",
  "“Your first sentence only has one job…”",
  "“In the second sentence, I want you to look underneath the titles.”",
  "“Now try the same three sentences on your own career.”",
  "“There is an honesty test here, and here is what I would not do.”"])
p=P(d,"This video is about explaining yourself to another person, so it should "
     "feel the most conversational of the series. Temidayo repeatedly stands in "
     "as the listener across the table — “Chronology tells me where you have "
     "been”, “I still may not know what you became able to do”. Keep her on "
     "camera for those lines; they only work as an exchange.",size=11,
    bold=True,color=NAVY,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

H1(d,"3.  First 30 seconds — H.I.T. map",before=14)
P(d,"H = Hook. I = Interest. T = Trust. The opening must work as one "
    "audiovisual unit: immediate conversational hook, meaningful visual "
    "interest, relevant lived proof and a clear payoff by 30 seconds. No "
    "title card before the promise.",after=8)
p=P(d,"This supersedes the older Video 4 opening and any earlier instruction "
     "that kept Temidayo visually static or fully off-camera in the first 30 "
     "seconds.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

def beat(t,anchor,layer,body):
    H2(d,t,before=10)
    p=P(d,"Spoken anchor:  “%s”"%anchor,size=10.5,italic=True,color=DIM,after=8)
    shade(p,BAND_CREAM)
    if layer: keep(P(d,layer,size=11,bold=True,color=GOLD,after=6))
    for b in body: keep(P(d,b,after=5))

beat("0:00–0:10","A senior colleague once called me a cat with nine lives.",
     "H = HOOK",
     ["Visual: begin on Temidayo, direct to camera.",
      "On-screen text:  YOUR CAREER MAKES SENSE",
      "Do not use a title card before this.",
      "FACTUAL BOUNDARY: the joke is the whole fact. Do not name the employer "
      "publicly, do not invent the original conversation, do not script the "
      "colleague's words beyond “a cat with nine lives”, and do not use cat "
      "imagery of any kind."])
beat("0:10–0:20","When I explained it as a list of jobs, the path sounded more "
     "disconnected than it was.","I = INTEREST",
     ["Restrained text treatment of a plain job list, then the turn.",
      "On-screen:  CHRONOLOGY  vs.  PORTABILITY",
      "No résumé-scroll animation, no timeline graphic gag."])
beat("0:20–0:26","The career wasn’t the problem. The explanation was.",
     "T = TRUST",
     ["This is the line the video turns on. Let it sit.",
      "Stay on Temidayo. Do not cover it."])
beat("0:26–0:32","So if your career looks disconnected on paper, let me show "
     "you how I learned to explain mine…","PAYOFF",
     ["This is the relational turn: her evidence becomes the viewer's method.",
      "Optional small text: 3 STEPS",
      "The payoff, and the honesty boundary — “without pretending every move "
      "was planned” — must both be clear before the teaching starts."])

H2(d,"First-30-second audit table",before=12)
keep(P(d,"Audited against the v4.0 standard. The existing opening passed on "
       "every criterion, so only the voice register was revised and the "
       "viewer turn was sharpened.",size=10.5,italic=True,color=DIM,after=8))
hit_table(d,[
 ["0:00–0:10",
  "“A senior colleague once called me a cat with nine lives.”",
  "Personal-story opening; a real remark, not a claim.",
  "YOUR CAREER MAKES SENSE",
  "Open on Temidayo, direct to camera. No title card. NO cat imagery.",
  "A real thing a colleague said about her real career.",
  "The viewer recognises the nonlinear-career problem immediately."],
 ["0:10–0:20",
  "“When I explained it as a list of jobs, the path sounded more disconnected "
  "than it was.”",
  "The specific contradiction: the career was fine, the explanation was not.",
  "CHRONOLOGY  vs.  PORTABILITY",
  "Restrained text treatment of a plain job list, then the turn. No "
  "résumé-scroll animation.",
  "Her own failed explanation, named as a failure.",
  "The viewer sees the problem is fixable and is about explanation."],
 ["0:20–0:26",
  "“The career wasn’t the problem. The explanation was.”",
  "The line the video turns on.",
  "—",
  "Stay on Temidayo. Let it sit. Do not cover it.",
  "A relearning moment, stated plainly.",
  "The viewer knows what will actually be taught."],
 ["0:26–0:32",
  "“So if your career looks disconnected on paper, let me show you how I "
  "learned to explain mine…”",
  "Direct offer: her case becomes the viewer's method.",
  "3 STEPS",
  "Return cleanly to Temidayo.",
  "The method is derived from her own case, not from advice.",
  "Payoff and the honesty boundary are both clear before 30 seconds."]])
keep(P(d,"Hook layers for the long-form:",size=10.5,bold=True,color=NAVY,
       before=10,after=5))
hook_block(d,
 "A senior colleague once called me a cat with nine lives.",
 "YOUR CAREER MAKES SENSE",
 "Direct to camera, then the chronology-versus-portability contrast.",
 "Her own nonlinear career and the explanation that kept failing.",
 "A three-sentence method for explaining a career change, promised by 0:32.")

H1(d,"4.  Slide marker → actual slide number",before=14)
P(d,"The teleprompter carries eleven slide markers. They map to the existing "
    "eleven-slide deck in order, marker 1 to slide 1 through marker 11 to "
    "slide 11. Do not add, delete, redesign or reorder slides.",after=8)
for n,job in enumerate(SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"5.  Existing reveal-frame map",before=14)
P(d,"The reveal-build deck contains 26 frames. This is the inspected count "
    "from the actual file. Reveal visuals are unchanged.",after=8)
for n,rng,cnt in REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"6.  Overlay principle",before=14)
P(d,"When a visual can prove information more efficiently than Temidayo "
    "speaking it, let the visual carry it. Do not add spoken wording to "
    "duplicate slide copy, and do not add slide copy to duplicate her.",after=8)

H1(d,"7.  Factual boundaries",before=14)
p=P(d,"THE CAT-WITH-NINE-LIVES FACT IS BOUNDED. A senior colleague once "
     "called Temidayo a cat with nine lives, meaning her career kept moving "
     "into work that looked unrelated. That is the entire approved fact. Do "
     "not name the employer publicly, invent the original conversation, add "
     "dialogue, or use cat imagery anywhere in the edit or the thumbnail.",
    size=11,bold=True,color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
p=P(d,"THE HONESTY BOUNDARY IS THE POINT OF THE VIDEO. Never imply every move "
     "was planned, and never imply everything transfers. Different roles, "
     "functions and industries can require real relearning, and the script "
     "says so twice. Do not trim either instance.",size=11,bold=True,
     color=RED,after=8,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
pairlist(d,["2008 financial-crisis context stays as spoken, no more;",
 "no invented employer, client, metric or result;",
 "no claim that the three chapters are one profession;",
 "no forced connection the evidence does not support;",
 "permitted evidence only in the written exercise."],after=3)

H1(d,"8.  CTA and watch next",before=14)
keep(P(d,"One product CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"Use the direct public landing-page URL only. Do not expose a PDF "
       "link, and do not restore Keep the Proof.",bold=True,after=6))
keep(P(d,"Watch next: %s"%NEXT,bold=True,after=5))
keep(P(d,"Slide 11 carries the correct Video 5 title, “Should I Make an "
       "Internal Move? 3 Questions to Decide”, and the playlist line. It was "
       "inspected in this pass and matches the spoken route.",size=10.5,
       color=DIM,after=8,spacing=1.25))
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
pairlist(d,["Main deck: 11 notes parts rewritten, one per slide.",
 "Reveal deck: 26 notes parts rewritten, one per frame.",
 "Slide XML, geometry, typography, palette and media: unchanged.",
 "Timings are script-derived working estimates at 145 words per minute for "
 "the 1,355-word script. Replace them from the finished cut."],after=3)
compress(d, 1.04, 0.30)
d.save(os.path.join(LF,EDB))
print("editor brief written")

# --------------------------------------------------------- publishing package
CHAPTERS=[("00:00","When a Career Looks Disconnected"),
 ("01:21","Chronology vs. Portability"),
 ("02:09","Name the Chapters Briefly"),
 ("03:11","Find the Repeated Work"),
 ("03:40","Look Beneath the Job Titles"),
 ("04:52","Explain Why the Direction Follows"),
 ("05:11","The Three-Sentence Career Explanation"),
 ("06:17","Do Not Invent a Perfect Plan"),
 ("07:08","Test Your Career Explanation"),
 ("08:31","Free Career Evidence Starter"),
 ("08:48","Should You Make an Internal Move?")]
CHAPTER_LINES=["%s %s"%(t,c) for t,c in CHAPTERS]

EMOJI_NOTE=("The restrained emoji system is part of the approved v4.0 standard: "
 "✨ teaching points, 🧭 CTA and resource, ⏱️ chapters, ▶️ Watch Next, "
 "🔗 Connect and Explore. Do not remove it and do not add more.")

DESC=[
 "Does your career path look disconnected on paper?",
 "In this video I show you how to explain your career change without "
 "pretending every move was part of a perfect plan.",
 "One of my senior-manager friends at EY used to joke that I was a “cat with "
 "nine lives” because my career kept moving into work that looked unrelated. "
 "Over time I realized the problem was not necessarily the career. It was how "
 "I was explaining what had traveled between the chapters.",
 "I will walk you through a simple three-part method:",
 "✨ Name your major career chapters briefly.",
 "✨ Find the repeated work beneath the titles.",
 "✨ Explain why your next direction follows from what you have already built.",
 "A chronology tells people where you have been. A portability explanation "
 "tells them what traveled with you.",
 "Not everything transfers. Different roles, functions and industries can "
 "require real relearning. The goal is not to invent a perfect career story. "
 "It is to make the continuity you can actually support easier to hear.","",
 "🧭 FREE CAREER EVIDENCE STARTER",
 "Turn one accomplishment into a portable Proof Line you can use in a "
 "performance review, interview, internal move or career pivot:",
 CTA_URL,"",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "▶️ WATCH NEXT",
 NEXT,"[ADD VIDEO 5 LINK WHEN LIVE]","",
 "PLAYLIST",
 "Career Portability: Career Pivots, Internal Moves & Growth",
 "[ADD PLAYLIST LINK]","",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "Temidayo Afonja helps experienced professionals understand what they can "
 "carry across roles, functions, employers and industries so they can make "
 "career pivots and internal moves without starting from zero."]

PINNED=["Which part of your career is hardest for you to explain?",
 "1. Naming the chapters without sounding defensive",
 "2. Finding the work that repeated beneath the titles",
 "3. Explaining why your next direction follows",
 "Try the three sentences on your own career and see which one you cannot "
 "finish yet:",
 "“My career has moved across…”",
 "“Across those chapters, I kept being asked to…”",
 "“That is why I am now focused on…”",
 "And if you want to try it on one real accomplishment, the free Career "
 "Evidence Starter is here:", CTA_URL]

TAGS=("how to explain your career change, nonlinear career, career pivot, "
 "career change explanation, career story, transferable skills, "
 "career transition, career portability, explain career gap, "
 "experienced professionals, Temidayo Afonja, Capability Formation")

def description_block(d, heading_before=14):
    H1(d,"INTERNAL NOTE — DO NOT PASTE INTO YOUTUBE",before=heading_before)
    p=P(d,EMOJI_NOTE,size=10.5,italic=True,color=RED,after=12,spacing=1.25)
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
head(d,VID,TITLE,"Video 4  ·  Publishing package  ·  v4.0",
     "Everything needed to upload. Working timestamps must be replaced with "
     "real ones from the finished edit.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
H1(d,"Supporting search language",before=14); P(d,SUPPORTING,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 5)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only. Do not put the full tag field in the "
       "public description.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
d.save(os.path.join(LF,PUB))

d=newdoc()
head(d,VID,TITLE,"Video 4  ·  YouTube description",
     "Upload copy only. Everything below the end marker is internal and must "
     "not be pasted into YouTube.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 5)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
DESC_DOC=os.path.join(BASE,"Video_4_YouTube_Description_HIT.docx")
d.save(DESC_DOC)
print("publishing package and description-only document written")

# ---------------------------------------------------------------- 4. Shorts
from shorts_text import SHORTS
LABELS=["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]
for (fn,role,hook,copy),label in zip(SHORTS,LABELS):
    d=newdoc(True)
    P(d,"VIDEO 4 SHORT",size=10,bold=True,color=GOLD,after=4,caps=True)
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
P(d,"VIDEO 4 — FOUR STANDALONE SHORTS",size=18,bold=True,color=NAVY,after=8,
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
 "Video 4 added as the Related Video when available."])
direct_address_section(d,"Direct address is part of the creative",
 ["“That is what changed for me, and it is what I want to help you change.”",
  "“So after the chronology, I want you to ask…”",
  "“Let me show you why my career was not a carefully designed portfolio "
  "career.”",
  "“But there is one rule I want you to keep.”"])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 4",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition / story","A CAT WITH NINE LIVES",
 ["FACTUAL BOUNDARY: the joke is the whole fact. No employer named, no "
  "invented conversation, no scripted dialogue for the colleague, and NO CAT "
  "IMAGERY of any kind.",
  "Visual:  CHRONOLOGY  →  WHAT TRAVELED",
  "End on:  MAKE THE CONTINUITY EASIER TO HEAR."])
short("SHORT 2","Distinction / myth","CHRONOLOGY ≠ EXPLANATION",
 ["Restrained two-column contrast. No résumé-scroll animation.",
  "Temidayo speaks as the listener here — “Chronology tells me where you have "
  "been.” Keep her on camera for it.",
  "End on:  WHAT TRAVELED WITH YOU?"])
short("SHORT 3","Proof / honesty","NOT A PERFECT PLAN",
 ["FACTUAL BOUNDARY: the approved facts are the accounting degree, December "
  "2008 and the financial crisis. No employer, no metric, no result, and no "
  "implication that the move was strategic.",
  "“Let me show you why my career was not a carefully designed portfolio "
  "career” opens the Short. Stay on her face for it.",
  "End on:  CONTEXT IS NOT AN APOLOGY."])
short("SHORT 4","Practical test / action","3 SENTENCES",
 ["Reveal the three sentence stems one at a time as restrained text.",
  "The evidence rule is the payoff, not a throwaway. Give it room.",
  "End on:  EVIDENCE BEHIND EVERY VERB."])

H1(d,"All Shorts — visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["cat imagery of any kind;","stock office B-roll;",
 "résumé-scroll animations;","employer logos;","timeline graphic gags;",
 "fake shock expressions;","constant zooms;","AI-generated scenery;",
 "social-media template effects."],after=3)
compress(d, 1.12, 0.46)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- 6. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 4 — FINAL RECORDING PACKAGE v4.0","",
 "Title:             %s"%TITLE,
 "Thumbnail:         %s"%THUMB,
 "Strategic job:     Searchable problem + personal evidence",
 "Core distinction:  Chronology tells where you have been. A portability",
 "                   explanation shows what travelled.","",
 "Voice:             Temidayo speaks to one experienced professional, not an",
 "                   abstract audience. This video is about explaining",
 "                   yourself to another person, so it is the most",
 "                   conversational in the series.","",
 "Personal proof:    A senior colleague once called Temidayo a cat with nine",
 "                   lives, meaning her career kept moving into work that",
 "                   looked unrelated. That is the whole approved fact. The",
 "                   employer is not named publicly, the original",
 "                   conversation is not invented, and no cat imagery is used",
 "                   anywhere.","",
 "Memory structure:  The three-sentence career explanation.",
 "  “My career has moved across…”",
 "  “Across those chapters, I kept being asked to…”",
 "  “That is why I am now focused on…”","",
 "Primary CTA:       %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "Watch next:        %s"%NEXT,"",
 "Slides:            Visual design and on-slide copy unchanged. 11 main",
 "                   slides.",
 "Speaker notes:     Updated for v4.0.",
 "Reveal deck:       Visual design and reveal states unchanged. 26 frames.",
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
 "This is a VOICE revision, not a rebuild. The three-sentence method, every",
 "substantive claim, the cat-with-nine-lives boundary, the honesty boundary,",
 "the single CTA and the Watch Next route are all unchanged. 78 of the 120",
 "prior spoken paragraphs are carried over verbatim; 44 were rewritten and 1",
 "coaching line was added so that Temidayo is speaking to one experienced",
 "professional rather than to an abstract audience. No paragraph was deleted",
 "and no new claim was added.","",
 "Prior locked package: v2.1, spoken word count 1,261,",
 "                      ZIP 6d9e8339a83a463ad231db8d180f6bb27025b07f41fd4bfc914778ea5f602684.",
 "This package:         v4.0, spoken word count 1,355.","",
 "-"*70,"","BOUNDARIES THAT DID NOT MOVE","",
 "Not everything transfers. Different roles, functions and industries can",
 "require real relearning, and the script says so more than once. Coherence is",
 "never a claim that every move was strategic. The 2008 financial-crisis",
 "context stays exactly as spoken and no further detail is added.","",
 "The Free Career Evidence Starter is the only CTA. Keep the Proof is NOT",
 "restored. Only the direct public landing-page URL is used; no PDF link is",
 "exposed.","",
 "-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_4_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256",""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))

MANIFEST=["LONG_FORM/%s.docx"%TEL,"LONG_FORM/%s.txt"%TEL,
 "LONG_FORM/%s.docx"%RDG,"LONG_FORM/%s.txt"%RDG,
 "LONG_FORM/%s"%EDB,"LONG_FORM/%s"%PUB]+\
 ["SHORTS/"+f for f,_,_,_ in SHORTS]+["SHORTS/"+SEB,"README_FINAL.txt"]
ZIP=os.path.join(BASE,"Video_4_HIT_FINAL_Recording_and_Shorts_Package.zip")
z=package(ROOT,MANIFEST,ZIP,"Video_4_HIT_FINAL",
  ["# VIDEO 4 - FINAL RECORDING PACKAGE v4.0",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
   "# checksum either; it is published in the sibling file",
   "# Video_4_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"])
print("ZIP sha256:",z)
print("DESC-ONLY sha256:",sha256(DESC_DOC))
