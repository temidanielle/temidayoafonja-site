# -*- coding: utf-8 -*-
"""Build the Video 2 v4.0 recording and Shorts package."""
import os, sys, shutil
sys.path.insert(0,"/tmp/da"); sys.path.insert(0,"/tmp/da/v2")
from docxkit import *
from changereport import new_blocks

BASE="/tmp/da/v2"
ROOT=os.path.join(BASE,"Video_2_HIT_FINAL")
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT,ignore_errors=True); os.makedirs(LF); os.makedirs(SH)

VID=2
TITLE="Is Your Job Making You Less Marketable?"
THUMB="VALUABLE HERE. STUCK HERE?"
PRIMARY="is your job making you less marketable"
SUPPORTING=("career stagnation · career marketability · transferable skills · "
    "career growth · transferable experience · internal mobility · "
    "career portability")
CTA="Capability Formation Field Kit"
CTA_URL="https://temidayoafonja.com/fieldkit"
NEXT="3 Things to Do Before Quitting Your Job"

CANON=os.path.join(BASE,"canonical_v4.0.txt")
LINES=new_blocks(CANON,"BEGIN APPROVED VIDEO 2 v4.0 SCRIPT",
                       "END APPROVED VIDEO 2 v4.0 SCRIPT")
SPOKEN=[x for x in LINES if not x.startswith("[SLIDE:")]

TEL="Video2TeleprompterScriptwithslidemarkers_HIT_v4.0"
RDG="Video2ReadingScriptnomarkers_HIT_v4.0"
EDB="Video_2_EDITOR_ONLY_HIT_Brief_v4.0.docx"
PUB="Video_2_Publishing_Package_HIT_v4.0.docx"
SEB="Video_2_Shorts_EDITOR_ONLY_HIT_Brief.docx"
scripts(VID,TITLE,LINES,SPOKEN,LF,TEL,RDG)
print("long-form scripts written")

SLIDE_MAP=["Title","Valuable Here / Legible Elsewhere","01 Remove the Company Nouns",
 "Test One","02 Find Outside-Context Evidence","Test Two",
 "03 Read the Last 90 Days","Test Three","The Three Tests","Read the Pattern",
 "Before You Leave","Capability Formation Field Kit","Watch Next"]
REVEAL_MAP=[(1,"1",1),(2,"2",1),(3,"3",1),(4,"4–5",2),(5,"6",1),(6,"7–10",4),
 (7,"11",1),(8,"12–15",4),(9,"16",1),(10,"17",1),(11,"18–21",4),(12,"22",1),
 (13,"23",1)]
FRAMES=[1,1,1,2,1,4,1,4,1,1,4,1,1]

# ------------------------------------------------------ long-form editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 2  ·  v4.0",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"1.  Locked metadata",before=14)
for k,v in (("Title",TITLE),("Thumbnail",THUMB),("Primary search phrase",PRIMARY),
            ("Primary CTA",CTA),("CTA URL",CTA_URL),("Watch next",NEXT),
            ("Strategic job","Recognition / diagnosis"),
            ("Core distinction","VALUABLE HERE is not automatically the same "
             "as LEGIBLE ELSEWHERE."),
            ("Memory device","The three tests. No acronym, no second "
             "framework.")):
    keep(P(d,"%-24s %s"%(k+":",v),size=11,after=5))
keep(P(d,"Do not add Keep the Proof, the Career Evidence Starter or a second "
       "framework to this video.",bold=True,color=RED,after=8,spacing=1.25))
p=P(d,"THUMBNAIL COPY SUPERSEDED, 3 September 2026. The authoritative thumbnail "
     "copy is “VALUABLE HERE. STUCK HERE?”. It supersedes “YOUR SKILLS ARE "
     "STALLING”. The thumbnail artwork currently in the repository still "
     "carries the old words and is therefore SUPERSEDED — REPLACE WITH "
     "APPROVED CANVA EXPORT BEFORE PUBLISHING. No thumbnail was generated or "
     "redesigned in this pass, and the missing export does not block the "
     "recording package.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

direct_address_section(d,"2.  Direct address is part of the creative",
 ["“And you may not notice it at first, because everything around you can "
  "still look like success.”",
  "“And that is what I want to help you do here.”",
  "“Let me start you with two different questions.”",
  "“The question I want you to answer is simple…”",
  "“…here is what I want you to look at…”"])

H1(d,"3.  First 30 seconds — H.I.T. map",before=14)
P(d,"H = Hook. I = Interest. T = Trust. The opening must work as one "
    "audiovisual unit: immediate conversational hook, meaningful visual "
    "interest, relevant lived proof and a clear payoff by 30 seconds. No "
    "title card before the promise.",after=8)
p=P(d,"This supersedes the older Video 2 opening and any earlier instruction "
     "that kept Temidayo visually static or fully off-camera in the first 30 "
     "seconds.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

def beat(t,anchor,layer,body):
    H2(d,t,before=10)
    p=P(d,"Spoken anchor:  “%s”"%anchor,size=10.5,italic=True,color=DIM,after=8)
    shade(p,BAND_CREAM)
    if layer: keep(P(d,layer,size=11,bold=True,color=GOLD,after=6))
    for b in body: keep(P(d,b,after=5))

beat("0:00–0:08","You can be doing very well at work and still be narrowing "
     "your next options.","H = HOOK",
     ["Visual: begin on Temidayo, medium or tight, direct to camera.",
      "On-screen text:  DOING WELL. FEWER OPTIONS?",
      "Do not use a title card before this.",
      "The viewer bridge — “you may not notice it at first, because everything "
      "around you can still look like success” — lands on her face. Do not "
      "cover it."])
beat("0:08–0:16","My own career has crossed very different functions and "
     "industries…","T = TRUST   ·   I = INTEREST",
     ["Show a restrained visual proof of the career path. Short labels only:",
      "ACCOUNTING & AUDIT  →  CYBER / PRIVACY  →  PEOPLE / EMPLOYEE "
      "EXPERIENCE  →  TRANSFORMATION",
      "IMPORTANT: Temidayo deliberately does NOT recite these chapters aloud. "
      "The visual carries the chronology; her voice carries the meaning.",
      "Do not change the PowerPoint deck to accomplish this. Use a simple "
      "editorial overlay or approved visual treatment."])
beat("0:16–0:24","Here is what became clear to me: being valuable here is not "
     "the same as being legible somewhere else.","",
     ["Bring forward:  VALUABLE HERE  vs.  LEGIBLE ELSEWHERE",
      "This should visually establish the central idea of the video."])
beat("0:24–0:30","So let me give you three tests you can run on your own "
     "work…","PAYOFF",
     ["Return cleanly to Temidayo.",
      "Optional small text: 3 MARKETABILITY TESTS",
      "The viewer should understand the payoff before the teaching begins."])

H2(d,"First-30-second audit table",before=12)
keep(P(d,"Audited against the v4.0 standard. The existing opening passed on "
       "title and thumbnail match, one-breath first sentence, recognition, "
       "visual interest, trust and payoff inside 30 seconds; only the voice "
       "register was revised, so the beats below are the current final ones.",
       size=10.5,italic=True,color=DIM,after=8))
hit_table(d,[
 ["0:00–0:08",
  "“You can be doing very well at work and still be narrowing your next "
  "options.”",
  "Surprising but defensible statement; a consequence the viewer may already "
  "be living.",
  "DOING WELL. FEWER OPTIONS?",
  "Open on Temidayo, medium or tight, direct to camera. No title card.",
  "Named immediately as her own observation, not a statistic.",
  "The viewer hears that success and marketability are not the same question."],
 ["0:08–0:16",
  "“My own career has crossed very different functions and industries…”",
  "Personal-story turn that earns the diagnosis.",
  "ACCOUNTING & AUDIT → CYBER / PRIVACY → PEOPLE → TRANSFORMATION",
  "Restrained career-sequence overlay. Not spoken aloud.",
  "Lived cross-industry evidence; she had to learn what travels.",
  "The viewer sees why she can read this problem."],
 ["0:16–0:24",
  "“Here is what became clear to me: being valuable here is not the same as "
  "being legible somewhere else.”",
  "The specific contradiction the whole video runs on.",
  "VALUABLE HERE  vs.  LEGIBLE ELSEWHERE",
  "Bring the central contrast forward and hold it.",
  "Framed as what she came to understand, not as advice.",
  "The core distinction is stated before any teaching begins."],
 ["0:24–0:30",
  "“So let me give you three tests you can run on your own work…”",
  "Direct offer of the method.",
  "3 MARKETABILITY TESTS",
  "Return cleanly to Temidayo.",
  "The tests are hers, drawn from the same career evidence.",
  "Payoff is explicit before 30 seconds."]])
keep(P(d,"Hook layers for the long-form:",size=10.5,bold=True,color=NAVY,
       before=10,after=5))
hook_block(d,
 "You can be doing very well at work and still be narrowing your next options.",
 "DOING WELL. FEWER OPTIONS?",
 "Direct to camera, then the restrained career-sequence overlay.",
 "Temidayo's own cross-function, cross-industry career.",
 "Three tests the viewer can run on their own work, promised by 0:30.")

H1(d,"4.  Slide marker → actual slide number",before=14)
P(d,"The teleprompter carries thirteen slide markers. They map to the existing "
    "thirteen-slide deck in order, marker 1 to slide 1 through marker 13 to "
    "slide 13. Do not add, delete, redesign or reorder slides.",after=8)
for n,job in enumerate(SLIDE_MAP,1):
    keep(P(d,"Marker %-3d →  Slide %-3d %s"%(n,n,job),size=10.5,after=3))

H1(d,"5.  Existing reveal-frame map",before=14)
P(d,"The reveal-build deck contains 23 frames. This is the inspected count "
    "from the actual file. Reveal visuals are unchanged.",after=8)
for n,rng,cnt in REVEAL_MAP:
    keep(P(d,"Slide %-3d →  reveal frames %-8s (%d)"%(n,rng,cnt),size=10.5,after=3))

H1(d,"6.  Overlay principle",before=14)
P(d,"When a visual can prove information more efficiently than Temidayo "
    "speaking it, let the visual carry it. Do not add spoken wording to "
    "duplicate slide copy, and do not add slide copy to duplicate her.",after=8)

H1(d,"7.  Factual and tone boundaries",before=14)
p=P(d,"NON-ALARMIST. This video must never imply that praise, pay or internal "
     "importance are themselves warning signs, that a strong job is "
     "automatically bad, or that the viewer should quit because their "
     "marketability may be narrowing.",size=11,bold=True,color=RED,after=8,
     spacing=1.25)
shade(p,BAND_CREAM); keep(p)
pairlist(d,["no invented employer, metric or result;",
 "no diagnosis from one quarter;","no urgency graphics;",
 "no implication that context-bound value is worthless;",
 "the documentation line keeps its permitted, non-confidential boundary."],after=3)

H1(d,"8.  CTA and watch next",before=14)
keep(P(d,"One product CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"Do not add Keep the Proof or the Career Evidence Starter.",bold=True,after=6))
keep(P(d,"Watch next: %s"%NEXT,bold=True,after=5))
p=P(d,"WATCH NEXT CARD CORRECTED, 3 September 2026. Slide 13 and reveal frame "
     "23 previously carried the retired Video 3 title, “Before You Quit Your "
     "Job, Check These 3 Things”. Both now read “3 Things to Do Before "
     "Quitting Your Job”, which is the locked Video 3 title and matches what "
     "Temidayo says. The correction was text only: same 40pt Montserrat Bold, "
     "same three-line block, same text box at the same position and size, same "
     "colours, no media change and no change to the end-screen space on the "
     "right. The card can now be held on screen while she names the video.",
    size=11,bold=True,color=NAVY,before=6,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
p=P(d,"SLIDE-PREVIEW PDF IS ONE PAGE BEHIND. The two PowerPoint decks are the "
     "authoritative artifacts and both carry the corrected card. The "
     "slide-preview PDF was NOT regenerated: re-rendering it in the current "
     "build environment returns Montserrat in the wrong weight, which would "
     "change typography that must be preserved. Its page 13 therefore still "
     "shows the retired title. Work from the decks, and re-export the preview "
     "PDF cleanly before using it for review.",size=11,bold=True,color=RED,
    after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
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
 "Reveal deck: 23 notes parts rewritten, one per frame.",
 "Slide XML, geometry, typography, palette and media: unchanged.",
 "Timings are script-derived working estimates at 145 words per minute for "
 "the 1,258-word script. Replace them from the finished cut."],after=3)
compress(d, 1.10, 0.40)
d.save(os.path.join(LF,EDB))
print("editor brief written")

# --------------------------------------------------------- publishing package
CHAPTERS=[("00:00","Doing well can still narrow your options"),
 ("00:57","Valuable here vs. legible elsewhere"),
 ("02:02","Test 1: Remove the company nouns"),
 ("03:14","Test 2: Find outside-context evidence"),
 ("04:38","Test 3: Read the last 90 days"),
 ("05:58","Read the pattern"),
 ("06:50","What can you change before leaving?"),
 ("07:49","Capability Formation Field Kit"),
 ("08:21","Before you quit")]
CHAPTER_LINES=["%s   %s"%(t,c) for t,c in CHAPTERS]

DESC=[
 "Can you be doing well in your current job and still be getting less "
 "marketable?",
 "In this video I give you three practical tests for separating the value you "
 "have inside your current organization from the experience and judgment "
 "another employer, function or industry can actually recognize and use.",
 "I give you three tests you can run on your own work:",
 "✨ Remove the company nouns.",
 "✨ Find outside-context evidence.",
 "✨ Read the last 90 days.",
 "You will strip company-specific language out of the way you explain your "
 "work, look for evidence that your judgment stays useful outside the place it "
 "was formed, and read what your last 90 days have really added to what you "
 "can do.",
 "This matters to you because your company may know exactly why you are "
 "valuable while another employer cannot yet read the same evidence.",
 "Being valuable where you are matters. It just answers a different question "
 "from whether your value can travel.","",
 "🧭 CAPABILITY FORMATION FIELD KIT",
 "A private, evidence-led assessment of what your current work is building, "
 "what looks portable and what needs your attention next.",
 CTA_URL,"",
 "▶️ WATCH NEXT",
 NEXT,"[ADD VIDEO LINK WHEN LIVE]","",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "Temidayo Afonja helps experienced professionals understand what they can "
 "carry across roles, functions, employers and industries so they can make "
 "career pivots and internal moves without starting from zero."]

PINNED=["Which of the three tests is hardest for you right now?",
 "1. Remove the company nouns",
 "2. Find outside-context evidence",
 "3. Read the last 90 days",
 "And if you removed your employer, your systems and your internal language "
 "from the way you describe your work, what would still be left?"]

TAGS=("is your job making you less marketable, career marketability, "
 "transferable skills, career stagnation, am I still marketable, "
 "career growth, career portability, internal mobility, career development, "
 "transferable experience, experienced professionals, Temidayo Afonja, "
 "Capability Formation")

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
head(d,VID,TITLE,"Video 2  ·  Publishing package  ·  v4.0",
     "Everything needed to upload. Working timestamps must be replaced with "
     "real ones from the finished edit.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
H1(d,"Supporting search language",before=14); P(d,SUPPORTING,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 3)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only. Do not put the full tag field in the "
       "public description.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
d.save(os.path.join(LF,PUB))

d=newdoc()
head(d,VID,TITLE,"Video 2  ·  YouTube description",
     "Upload copy only. Everything below the end marker is internal and must "
     "not be pasted into YouTube.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14); P(d,PRIMARY,after=10)
description_block(d)
H1(d,"Pinned comment",before=14)
for para in PINNED: keep(P(d,para,after=6))
H1(d,"Watch next",before=14); keep(P(d,"%s  (Video 3)"%NEXT,bold=True,after=8))
H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,TAGS,size=10.5,after=10))
compress(d, 1.08, 0.44)
DESC_DOC=os.path.join(BASE,"Video_2_YouTube_Description_HIT.docx")
d.save(DESC_DOC)
print("publishing package and description-only document written")

# ---------------------------------------------------------------- 4. Shorts
from shorts_text import SHORTS
LABELS=["SHORT 1","SHORT 2","SHORT 3","SHORT 4"]
for (fn,role,hook,copy),label in zip(SHORTS,LABELS):
    d=newdoc(True)
    P(d,"VIDEO 2 SHORT",size=10,bold=True,color=GOLD,after=4,caps=True)
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
P(d,"VIDEO 2 — FOUR STANDALONE SHORTS",size=18,bold=True,color=NAVY,after=8,
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
 "Video 2 added as the Related Video when available."])
direct_address_section(d,"Direct address is part of the creative",
 ["“There are two questions I want you to separate.”",
  "“Let me show you what changing contexts taught me.”",
  "“Try this on one sentence from your résumé.”"])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 2",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition","DOING WELL. FEWER OPTIONS?",
 ["Visual:  VALUABLE HERE  /  LEGIBLE ELSEWHERE",
  "Non-alarmist. Do not imply that being relied on is itself a warning sign.",
  "End on:  CAN ANOTHER CONTEXT USE IT?"])
short("SHORT 2","Distinction / myth","INDISPENSABLE ≠ MARKETABLE",
 ["Restrained two-column contrast. No generic office B-roll.",
  "End on:  WHAT BELONGS TO YOU, AND WHAT BELONGS TO THE CONTEXT?"])
short("SHORT 3","Proof / personal evidence","NOT EVERYTHING TRAVELS",
 ["FACTUAL BOUNDARY: no employer, metric, role or result. The proof is that "
  "Temidayo's career crossed functions and industries and she had to learn "
  "what travels.",
  "End on:  WHAT STAYS USEFUL WHEN THE CONTEXT CHANGES?"])
short("SHORT 4","Practical test / action","REMOVE THE COMPANY NOUNS",
 ["Show the before and after sentence as restrained text, not a graphic gag.",
  "End on:  NOW IT IS EASIER TO UNDERSTAND."])

H1(d,"All Shorts — visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["stock office B-roll;","generic résumé graphics;","employer logos;",
 "red warning graphics;","fake shock expressions;","countdown motifs;",
 "constant zooms;","AI-generated scenery;","social-media template effects."],
 after=3)
compress(d, 1.12, 0.46)
d.save(os.path.join(SH,SEB))

# ---------------------------------------------------------------- 6. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 2 — FINAL RECORDING PACKAGE v4.0","",
 "Title:             %s"%TITLE,
 "Thumbnail:         %s"%THUMB,
 "                   SUPERSEDES \"YOUR SKILLS ARE STALLING\". The thumbnail",
 "                   artwork in the repository still carries the old words:",
 "                   SUPERSEDED - REPLACE WITH APPROVED CANVA EXPORT BEFORE",
 "                   PUBLISHING.",
 "Strategic job:     Recognition / diagnosis",
 "Core distinction:  Being valuable here is not the same as being legible",
 "                   somewhere else.","",
 "Voice:             Temidayo speaks to one experienced professional, not an",
 "                   abstract audience. The relationship is trusted",
 "                   practitioner to one viewer, never lecturer to a crowd.","",
 "Memory structure:",
 "  Remove the company nouns.",
 "  Find outside-context evidence.",
 "  Read the last 90 days.","",
 "Primary CTA:       %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "Watch next:        %s"%NEXT,"",
 "Slides:            Visual design and on-slide copy unchanged. 13 main",
 "                   slides.",
 "Speaker notes:     Updated for v4.0.",
 "Reveal deck:       Visual design and reveal states unchanged. 23 frames.",
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
 "This is a VOICE revision, not a rebuild. The teaching structure, every",
 "substantive claim, the factual and tone boundaries, the single CTA and the",
 "Watch Next route are all unchanged. 62 of the 105 prior spoken paragraphs",
 "are carried over verbatim; 46 were rewritten so that Temidayo is speaking",
 "to one experienced professional rather than to an abstract audience. No",
 "paragraph was deleted and no new claim was added.","",
 "Prior locked package: v2.0, spoken word count 1,131.",
 "This package:         v4.0, spoken word count 1,258.","",
 "-"*70,"","WATCH NEXT CARD — CORRECTED","",
 "Slide 13 and reveal frame 23 previously carried the retired Video 3 title,",
 "\"Before You Quit Your Job, Check These 3 Things\". Both now read \"3 Things",
 "to Do Before Quitting Your Job\", the locked Video 3 title, which is what",
 "Temidayo says in the script.","",
 "The correction was text only and was measured before it was applied: same",
 "40pt Montserrat Bold, same three-line block, same text box at the same",
 "position and size, same colours, no media change, and no change to the",
 "end-screen space on the right. The widest line went from 4.655 in to",
 "4.525 in inside a 6.667 in box, so it fits with more clearance, not less.",
 "Exactly one slide XML part changed in each deck: ppt/slides/slide13.xml in",
 "the main deck and ppt/slides/slide23.xml in the reveal deck.","",
 "The slide-preview PDF was NOT regenerated. Re-rendering it in the current",
 "build environment returns Montserrat in the wrong weight, which would change",
 "typography that must be preserved, so page 13 of the PDF still shows the",
 "retired title. The two PowerPoint decks are authoritative and both carry the",
 "corrected card. Re-export the preview PDF cleanly before using it for",
 "review.","",
 "-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_2_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256",""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))

MANIFEST=["LONG_FORM/%s.docx"%TEL,"LONG_FORM/%s.txt"%TEL,
 "LONG_FORM/%s.docx"%RDG,"LONG_FORM/%s.txt"%RDG,
 "LONG_FORM/%s"%EDB,"LONG_FORM/%s"%PUB]+\
 ["SHORTS/"+f for f,_,_,_ in SHORTS]+["SHORTS/"+SEB,"README_FINAL.txt"]
ZIP=os.path.join(BASE,"Video_2_HIT_FINAL_Recording_and_Shorts_Package.zip")
z=package(ROOT,MANIFEST,ZIP,"Video_2_HIT_FINAL",
  ["# VIDEO 2 - FINAL RECORDING PACKAGE v4.0",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
   "# checksum either; it is published in the sibling file",
   "# Video_2_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256"])
print("ZIP sha256:",z)
print("DESC-ONLY sha256:",sha256(DESC_DOC))
