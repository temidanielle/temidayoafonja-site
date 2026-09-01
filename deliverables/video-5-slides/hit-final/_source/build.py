# -*- coding: utf-8 -*-
"""Build the Video 5 H.I.T. final recording and Shorts package."""
import os, sys, shutil, zipfile, hashlib
sys.path.insert(0, "/tmp/v5hit")
from script_text import LINES, SPOKEN, MARKERS
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY=RGBColor(0x0F,0x23,0x46); GOLD=RGBColor(0x8A,0x6D,0x1E)
DIM=RGBColor(0x5A,0x6B,0x82); INK=RGBColor(0x1A,0x1A,0x1A)
RED=RGBColor(0x9B,0x2C,0x10)
BAND_NAVY="E8EDF4"; BAND_CREAM="F3F0E8"

ROOT="/tmp/v5hit/Video_5_HIT_FINAL"
LF=os.path.join(ROOT,"LONG_FORM"); SH=os.path.join(ROOT,"SHORTS")
shutil.rmtree(ROOT, ignore_errors=True)
os.makedirs(LF); os.makedirs(SH)

TITLE="Should I Make an Internal Move? 3 Questions to Decide"
THUMB="YOU MAY NOT NEED TO LEAVE"
CTA="Career Decision Evidence Check"
CTA_SHORT="Career Decision Evidence Check"
CTA_URL="https://temidayoafonja.com/career-decisions"
NEXT="Are You Growing—or Just Being Given More Work?"

def newdoc(teleprompter=False):
    d=Document(); st=d.styles['Normal']
    st.font.name='Calibri'; st.font.size=Pt(13 if teleprompter else 11)
    ah=OxmlElement('w:autoHyphenation'); ah.set(qn('w:val'),'0')
    d.settings.element.append(ah)
    for s in d.sections:
        s.top_margin=s.bottom_margin=Inches(0.9)
        s.left_margin=s.right_margin=Inches(1.05)
    return d

def keep(p,nxt=False):
    pr=p._p.get_or_add_pPr()
    for t in ('w:keepLines',)+(('w:keepNext',) if nxt else ()):
        e=OxmlElement(t); e.set(qn('w:val'),'1'); pr.append(e)
    return p

def shade(p,fill):
    pr=p._p.get_or_add_pPr(); s=OxmlElement('w:shd')
    s.set(qn('w:val'),'clear'); s.set(qn('w:fill'),fill); pr.append(s)

def bar(p,col):
    pr=p._p.get_or_add_pPr(); b=OxmlElement('w:pBdr'); l=OxmlElement('w:left')
    l.set(qn('w:val'),'single'); l.set(qn('w:sz'),'18')
    l.set(qn('w:space'),'8'); l.set(qn('w:color'),col); b.append(l); pr.append(b)

def P(d,t,size=11,bold=False,color=None,before=0,after=8,italic=False,
      caps=False,spacing=1.3):
    p=d.add_paragraph()
    p.paragraph_format.space_before=Pt(before); p.paragraph_format.space_after=Pt(after)
    p.paragraph_format.line_spacing=spacing
    r=p.add_run(t); r.font.size=Pt(size); r.bold=bold; r.italic=italic
    if color is not None: r.font.color.rgb=color
    if caps: r.font.all_caps=True
    return p

def head(d,title,sub,note=None):
    P(d,"CAPABILITY FORMATION   |   VIDEO 5",size=10,bold=True,color=GOLD,
      after=4,caps=True)
    P(d,title,size=20,bold=True,color=NAVY,after=4,spacing=1.1)
    P(d,sub,size=11,color=DIM,after=6,spacing=1.1)
    if note: P(d,note,size=10.5,italic=True,color=DIM,after=18,spacing=1.2)

def H1(d,t,before=20):
    return keep(P(d,t,size=14,bold=True,color=NAVY,before=before,after=8),True)
def H2(d,t,before=13):
    return keep(P(d,t,size=11.5,bold=True,color=NAVY,before=before,after=5),True)

def compress(d, line_spacing=1.18, after_scale=0.80):
    """Tighten one document's vertical rhythm without touching type size,
    weight, colour or wording. Keeps editor briefs off a near-empty last page."""
    for p in d.paragraphs:
        pf=p.paragraph_format
        if pf.line_spacing and 1.0 < pf.line_spacing < 1.4 and pf.line_spacing > line_spacing:
            pf.line_spacing = line_spacing
        if pf.space_after is not None:
            pf.space_after = Pt(round(pf.space_after.pt*after_scale,1))
        if pf.space_before is not None and pf.space_before.pt:
            pf.space_before = Pt(round(pf.space_before.pt*after_scale,1))
    return d

def pairlist(d, items, indent="—  ", gap="        ", after=4, budget=78):
    """Lay short bullet items several to a line, packed by width.

    Every item is kept verbatim; nothing is removed, reworded or reordered,
    and neither type size nor leading changes. This reclaims the unused
    right-hand part of a short-bullet line, which is what keeps the Shorts
    editor brief to two pages. The width budget is measured against the
    inspection renderer's font, which is wider than Calibri, so Word fits at
    least as much per line and never less."""
    lines, cur = [], []
    for it in items:
        trial = cur + [it]
        width = sum(len(indent) + len(x) for x in trial) + len(gap) * (len(trial) - 1)
        if cur and width > budget:
            lines.append(cur); cur = [it]
        else:
            cur = trial
    if cur: lines.append(cur)
    for group in lines:
        keep(P(d, gap.join(indent + x for x in group), after=after))



# ------------------------------------------------- 1. teleprompter DOCX + TXT
d=newdoc(True)
head(d,TITLE,"Video 5  ·  Teleprompter script with slide markers",
     "Spoken script is the large text. A slide marker in a tinted band tells "
     "the editor which slide to bring up; it is not spoken.")
for line in LINES:
    if line.startswith("[SLIDE:"):
        name=line[len("[SLIDE:"):-1].strip()
        p=P(d,"SLIDE  —  %s"%name,size=11,bold=True,color=NAVY,
            before=14,after=14,spacing=1.1)
        shade(p,BAND_NAVY); bar(p,"0F2346"); keep(p,True)
    else:
        keep(P(d,line,size=13.5,color=INK,after=12,spacing=1.5))
d.save(os.path.join(LF,"Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.docx"))
tel=[TITLE,"Video 5  ·  Teleprompter script with slide markers",""]
for line in LINES:
    if line.startswith("[SLIDE:"):
        tel += ["", "SLIDE  —  %s"%line[len("[SLIDE:"):-1].strip(), ""]
    else: tel += [line, ""]
open(os.path.join(LF,"Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.txt"),
     "w").write("\n".join(tel).strip()+"\n")

# ------------------------------------------------- 2. reading script DOCX+TXT
d=newdoc(True)
head(d,TITLE,"Video 5  ·  Reading script, no markers",
     "Spoken language only. No slide markers, no timestamps, no production "
     "directions.")
for line in SPOKEN:
    keep(P(d,line,size=13.5,color=INK,after=12,spacing=1.5))
d.save(os.path.join(LF,"Video5ReadingScriptnomarkers_HIT_v2.0.docx"))
open(os.path.join(LF,"Video5ReadingScriptnomarkers_HIT_v2.0.txt"),
     "w").write("\n\n".join(SPOKEN)+"\n")
print("long-form scripts written")

# --------------------------------------------------- 3. long-form editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 5",size=12,bold=True,color=GOLD,after=2,caps=True)
P(d,TITLE,size=20,bold=True,color=NAVY,after=6,spacing=1.1)
p=P(d,"This document is for the editor. It is NOT Temidayo's teleprompter and "
     "must not be placed on the recording screen.",size=11,italic=True,
     color=DIM,after=16,spacing=1.25)
shade(p,BAND_CREAM)

H1(d,"Locked metadata",before=14)
for k,v in (("Title",TITLE),("Thumbnail",THUMB),("Primary CTA",CTA),
            ("CTA URL",CTA_URL),("Watch next",NEXT),
            ("Core distinction",
             "Movement is not automatically growth. The test is whether an "
             "internal move changes the work, expands judgment and creates "
             "evidence that can travel.")):
    keep(P(d,"%-18s %s"%(k+":",v),size=11,after=5))
p=P(d,"CTA PRODUCTION GATE: SATISFIED. The Career Decision Evidence Check page "
     "is live and the core production journey has been verified. Video 5 is "
     "NOT blocked on this CTA page. One normal signed-out link check is "
     "retained in the final upload SOP.",size=11,bold=True,color=NAVY,
     before=8,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

H1(d,"First 30 seconds — H.I.T.",before=14)
P(d,"H = Hook. I = Interest. T = Trust. The opening must work as one "
    "audiovisual unit: immediate conversational hook, meaningful visual "
    "interest, relevant personal proof, and a clear viewer payoff by roughly "
    "20 to 30 seconds. No generic welcome before the promise. No résumé "
    "recital. No forced statistic.",after=8)
p=P(d,"The older Video 5 exception that delayed personal proof until roughly "
     "1:35 is SUPERSEDED by this H.I.T. rebuild. The proof now sits in the "
     "opening.",size=11,bold=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

def beat(t,anchor,layer,body):
    H2(d,t,before=10)
    p=P(d,"Spoken anchor:  “%s”"%anchor,size=10.5,italic=True,color=DIM,after=8)
    shade(p,BAND_CREAM)
    if layer: keep(P(d,layer,size=11,bold=True,color=GOLD,after=6))
    for b in body: keep(P(d,b,after=5))

beat("0:00–0:05","You may not need to leave your company.","H = HOOK",
     ["Visual: begin direct to camera.",
      "On-screen text:  YOU MAY NOT NEED TO LEAVE",
      "No title card before this."])
beat("0:05–0:10","You may need access to different work inside it.",
     "I = INTEREST",
     ["Visual:  SAME COMPANY  /  DIFFERENT WORK",
      "Do not use office-building, doorway, transfer-arrow or org-chart stock "
      "imagery."])
beat("0:10–0:20",
     "I’ve had my own scope expand inside an organization before…","T = TRUST",
     ["Visual progression:  MORE WORK?  then  DIFFERENT WORK"])
p=P(d,"FACTUAL BOUNDARY. The confirmed evidence is only that Temidayo's scope "
     "expanded after roughly six months and trust extended beyond the original "
     "box. Do not add an employer, an exact role, an exact assignment, a "
     "causal claim, a quote, a metric or an unsupported result.",size=11,
     bold=True,color=RED,before=6,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
beat("0:20–0:30","So before you accept an internal move…","PAYOFF",
     ["Progressively reveal:",
      "     WILL THE WORK CHANGE?",
      "     WILL YOUR JUDGMENT EXPAND?",
      "     WILL THE EVIDENCE TRAVEL?",
      "Then move into the existing deck."])

H1(d,"Editorial rhythm after the opening",before=14)
P(d,"After the first 30 seconds:",after=6)
for x in ["preserve natural pacing;",
 "use the existing slides as teaching support;","avoid constant motion;",
 "avoid decorative B-roll;","avoid unnecessary text duplication;",
 "avoid constant punch-ins;","allow reflective pauses."]:
    keep(P(d,"—  "+x,after=4))

H1(d,"Existing slides — unchanged",before=14)
P(d,"Use exactly the existing 12-slide sequence. The reveal-build deck is "
    "unchanged. Do not add, delete, redesign or reorder slides.",after=8)
for n,job in enumerate(["Core Distinction","The Three Questions",
 "1 — Will the Work Change?",
 "Access Test / New Problems, Systems, Stakeholders, Context",
 "2 — Will Your Judgment Expand?","More Tasks / More Judgment",
 "3 — Will the Evidence Travel?","Result / Judgment / Range","Decision Read",
 "Conversation Prompts","Career Decision Evidence Check","Watch Next"],1):
    keep(P(d,"Slide %-3d %s"%(n,job),size=10.5,after=3))

H1(d,"Let the visual carry information",before=14)
P(d,"Do not add spoken wording to compensate for slide copy.",after=6)
for s_,note in [("Slide 2","carries the three-question preview."),
 ("Slide 4","carries new problems / systems / stakeholders / context."),
 ("Slide 6","carries MORE TASKS vs MORE JUDGMENT."),
 ("Slide 8","carries RESULT / JUDGMENT / RANGE."),
 ("Slide 9","carries the 3 / 2 / 0–1 decision read."),
 ("Slide 10","carries the conversation prompts.")]:
    keep(P(d,"%s %s"%(s_,note),after=5))

H1(d,"Visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["generic office B-roll;","org-chart animation;","transfer arrows;",
 "employer logos;","résumé graphics;","fake promotion visuals;",
 "constant zooms;","red warning graphics;","fake shock expressions;",
 "AI-generated scenery;","social-media template effects."],after=3)

H1(d,"Safety and decision boundary",before=14)
P(d,"Preserve the script's explicit acknowledgment that:",after=6)
for x in ["a lower-formation move may still be right for pay, flexibility, "
 "benefits, stability or manager fit;","health and safety take priority;",
 "harassment or discrimination is not a situation to optimise around before "
 "seeking appropriate support;",
 "caregiving, immigration status, location, energy and timing may change the "
 "decision."]:
    keep(P(d,"—  "+x,after=4))

H1(d,"CTA and watch next",before=14)
keep(P(d,"One product or resource CTA only: %s — %s"%(CTA,CTA_URL),after=5))
keep(P(d,"Do not add the Capability Formation Field Kit or Keep the Proof.",
       bold=True,after=6))
keep(P(d,"The production gate is satisfied.",bold=True,color=NAVY,after=8))
keep(P(d,"Watch next: %s"%NEXT,bold=True,after=5))
for x in ["use direct Video 6 end-screen routing once Video 6 is public;",
 "before Video 6 is public, use the Career Portability playlist if it is "
 "functioning;",
 "otherwise use an appropriate currently public video or YouTube's "
 "best-for-viewer option temporarily."]:
    keep(P(d,"—  "+x,after=4))
keep(P(d,"Do not leave Subscribe as the only end-screen element.",bold=True,
       color=RED,before=4,after=8))
compress(d)
d.save(os.path.join(LF,"Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx"))
print("editor brief written")

# The nine working chapter lines, defined once so the copy-ready description
# and the reference section cannot drift apart.
CHAPTERS=[("00:00","You May Not Need to Leave"),
 ("01:15","The 3 Questions for an Internal Move"),
 ("01:35","Will the Work Change?"),
 ("03:20","Will Your Judgment Expand?"),
 ("04:55","Will the Evidence Travel?"),
 ("06:15","Read the Pattern"),
 ("07:15","What to Ask Before You Move"),
 ("08:50","Career Decision Evidence Check"),
 ("09:15","Are You Growing—or Just Being Given More Work?")]
CHAPTER_LINES=["%s %s"%(t,c) for t,c in CHAPTERS]

# ----------------------------------------------------- 4. publishing package
d=newdoc()
head(d,TITLE,"Video 5  ·  Publishing package",
     "Everything needed to upload. Working timestamps must be replaced with "
     "real ones from the finished edit.")
H1(d,"Title",before=14); P(d,TITLE,size=12,after=10)
H1(d,"Thumbnail",before=14); P(d,THUMB,size=12,bold=True,after=10)
H1(d,"Primary search phrase",before=14)
P(d,"should I make an internal move",after=10)
H1(d,"Supporting search language",before=14)
P(d,"internal move · internal mobility · internal job transfer · career "
    "growth · career decision · should I leave my company · internal career "
    "move · career portability",after=10)

H1(d,"Description",before=14)
keep(P(d,"The restrained emoji treatment on the section labels and the three "
       "teaching bullets is part of the approved standard. Do not remove it, "
       "and do not add more.",size=10.5,italic=True,color=DIM,after=10))
DESC=[
 "You may not need to leave your company to find work that expands your career.",
 "A well-designed internal move can give you access to different problems, "
 "broader judgment and evidence you can carry into future roles.",
 "But movement is not automatically growth.",
 "In this video, I give you three questions to test an internal role, "
 "transfer, team change or stretch opportunity:",
 "✨ Will the work change?",
 "✨ Will your judgment expand?",
 "✨ Will the evidence travel?",
 "You will also learn how to read your three answers, what to ask an internal "
 "hiring manager, and when an external move may still be the better decision.",
 "The real question is not simply whether you moved. It is whether the move "
 "increased what you can carry afterward.","",
 "🧭 CAREER DECISION EVIDENCE CHECK",
 "A structured next step for an active stay, internal-move or leave decision:",
 CTA_URL,"",
 "⏱️ CHAPTERS"]+CHAPTER_LINES+["",
 "▶️ WATCH NEXT", NEXT, "[ADD VIDEO 6 LINK WHEN LIVE]","",
 "🔗 CONNECT AND EXPLORE",
 "Website:","https://temidayoafonja.com",
 "LinkedIn:","https://www.linkedin.com/in/temidayo-afonja",
 "Substack:","https://temidayoafonja.substack.com","",
 "#InternalMobility #CareerGrowth #CareerDecision"]
for para in DESC:
    keep(P(d,para if para else " ",after=7 if para else 3))

keep(P(d,"— END OF THE COPY-READY DESCRIPTION —",size=10,bold=True,color=DIM,
       before=14,after=12,spacing=1.2))

H1(d,"Internal note — do not paste into YouTube",before=14)
p=P(d,"WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT",size=11,
    bold=True,color=RED,after=6,spacing=1.25)
shade(p,BAND_CREAM); keep(p)
p=P(d,"These timestamps were estimated from the script, not measured from the "
    "finished edit. Replace every timestamp using the finished cut before "
    "publication. Do not force the edit to match these estimates.",size=10.5,
    bold=True,italic=True,color=RED,after=10,spacing=1.25)
shade(p,BAND_CREAM); keep(p)

H1(d,"Working chapters — reference copy",before=14)
keep(P(d,"Identical to the nine chapter lines inside the description above.",
       size=10.5,italic=True,color=DIM,after=8))
for line in CHAPTER_LINES: keep(P(d,line,size=11,after=4))

H1(d,"Pinned comment",before=14)
for para in ["Which answer is least clear in the internal opportunity you are "
 "considering?",
 "1. Will the work change?","2. Will my judgment expand?",
 "3. Will the evidence travel?",
 "You do not need to share confidential details. Just reply with 1, 2 or 3 "
 "and the question you still need answered.",
 "If you are actively deciding whether to stay, move internally or leave, the "
 "Career Decision Evidence Check is here:", CTA_URL]:
    keep(P(d,para,after=6))

H1(d,"YouTube tag field",before=14)
keep(P(d,"Paste into the tag field only. Do not place the full tag field in "
       "the public description.",size=10.5,italic=True,color=DIM,after=6))
keep(P(d,"should I make an internal move, internal move, internal mobility, "
       "internal job transfer, career growth, career decision, should I leave "
       "my company, internal career move, career portability, career "
       "transition, experienced professionals, Temidayo Afonja, Capability "
       "Formation",size=10.5,after=10))

H1(d,"CTA production gate",before=14)
keep(P(d,"SATISFIED. The Career Decision Evidence Check page is live and the "
       "core production journey has been verified. Video 5 is not blocked on "
       "it. Retain one normal signed-out link check in the final upload SOP.",
       bold=True,after=8,spacing=1.25))
compress(d)
d.save(os.path.join(LF,"Video_5_Publishing_Package_HIT_v2.0.docx"))

# ---------------------------------------------------------------- 5. Shorts
SHORTS=[
 ("Video_5_Short_1_You_May_Not_Need_To_Leave.docx","SHORT 1","Recognition",
  "You may not need to leave your company.",
  ["You may not need to leave your company.",
   "You may need access to different work inside it.",
   "A good internal move can give you a different problem, function, customer "
   "or level of responsibility without making you surrender all of the "
   "context and credibility you have already built.",
   "But movement is not automatically growth.",
   "Before you move internally, ask:",
   "Will the work actually change?",
   "Because a new title with the same problems may move you on the org chart "
   "without increasing what you can carry next."]),
 ("Video_5_Short_2_More_Tasks_Not_More_Judgment.docx","SHORT 2",
  "Distinction / myth",
  "More responsibility is not the same as more judgment.",
  ["More responsibility is not the same as more judgment.",
   "More tasks can mean volume, coordination and work that no longer has an "
   "owner.",
   "Judgment grows when you have to interpret incomplete information, weigh "
   "tradeoffs, recommend a direction or own the consequence.",
   "So before you accept an internal opportunity, ask:",
   "What will I be trusted to decide that I am not trusted to decide now?",
   "If the only answer is, “You’ll have more to manage,” keep investigating."]),
 ("Video_5_Short_3_More_Scope_Not_Automatic_Growth.docx","SHORT 3",
  "Proof / personal evidence",
  "My scope expanded—but that was not what made it growth.",
  ["My scope expanded in one chapter of my career.",
   "But that was not what made it meaningful.",
   "The important part was not simply that I had more on my plate.",
   "It was that people were trusting me with work beyond the original box.",
   "That distinction matters.",
   "More volume can make you busier.",
   "Different work can expose you to new problems.",
   "Greater judgment can change what you are able to carry into the next "
   "context.",
   "So when your scope expands, do not ask only:",
   "“How much more am I doing?”","Ask:",
   "“What am I becoming trusted to do?”"]),
 ("Video_5_Short_4_Three_Questions_Before_You_Move.docx","SHORT 4",
  "Practical test / action",
  "Before you accept an internal move, ask these three questions.",
  ["Before you accept an internal move, ask these three questions.",
   "Will the work change?","Will my judgment expand?",
   "Will the evidence travel?",
   "Three yeses give you a strong formation case.",
   "Two yeses mean investigate or negotiate the missing dimension.",
   "Zero or one may mean you are moving without adding very much to what you "
   "can carry next.",
   "That does not automatically make the move wrong.",
   "Pay, flexibility, stability or a better manager may still make it worth "
   "taking.",
   "Just make the trade deliberately."])]

for fn,label,role,hook,copy in SHORTS:
    d=newdoc(True)
    P(d,"VIDEO 5 SHORT",size=10,bold=True,color=GOLD,after=4,caps=True)
    P(d,label,size=20,bold=True,color=NAVY,after=8,spacing=1.1)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    keep(P(d,"Verbal hook:  “%s”"%hook,size=11,color=DIM,after=5))
    keep(P(d,"Related long-form:  %s"%TITLE,size=11,color=DIM,after=10))
    H1(d,"RECORDING COPY",before=12)
    for line in copy:
        keep(P(d,line,size=13.5,color=INK,after=10,spacing=1.5))
    d.save(os.path.join(SH,fn))
print("publishing package and %d Shorts written"%len(SHORTS))

# ------------------------------------------------------ 6. Shorts editor brief
d=newdoc()
P(d,"EDITOR ONLY",size=22,bold=True,color=RED,after=2)
P(d,"VIDEO 5 — FOUR STANDALONE SHORTS",size=18,bold=True,color=NAVY,
  after=8,spacing=1.1)
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
 "restrained editorial pacing;",
 "Video 5 added as the Related Video when available."])

def short(label,role,onscreen,body):
    H1(d,label,before=14)
    keep(P(d,"Role:  %s"%role,size=11,color=DIM,after=5))
    p=keep(P(d,"On-screen hook:  %s"%onscreen,size=11,bold=True,color=GOLD,after=8))
    shade(p,BAND_CREAM)
    for b in body: keep(P(d,b,after=5))
    keep(P(d,"Related Video:  Video 5",size=10.5,color=DIM,before=4,after=6))

short("SHORT 1","Recognition","YOU MAY NOT NEED TO LEAVE",
 ["Visual:  SAME COMPANY  →  DIFFERENT WORK",
  "End on:  WILL THE WORK CHANGE?"])
short("SHORT 2","Distinction / myth","MORE TASKS ≠ MORE JUDGMENT",
 ["Use a restrained two-column contrast:  MORE TASKS  vs  MORE JUDGMENT",
  "No generic office B-roll.",
  "End on:  WHAT WILL YOU BE TRUSTED TO DECIDE?"])
short("SHORT 3","Proof / personal evidence","MORE SCOPE ≠ AUTOMATIC GROWTH",
 ["FACTUAL BOUNDARY: do not add an employer, role, assignment, metric or "
  "unsupported result. Do not imply the scope expansion itself proves growth.",
  "End on:  WHAT ARE YOU BECOMING TRUSTED TO DO?"])
short("SHORT 4","Practical test / action","3 QUESTIONS BEFORE YOU MOVE",
 ["Reveal progressively:",
  "     WILL THE WORK CHANGE?",
  "     WILL YOUR JUDGMENT EXPAND?",
  "     WILL THE EVIDENCE TRAVEL?",
  "Then show the 3 / 2 / 0–1 read in a restrained way. Do not turn it into a "
  "gamified scorecard."])

H1(d,"All Shorts — visual boundaries",before=14)
P(d,"Do not use:",after=5)
pairlist(d,["org-chart animations;","transfer-arrow clichés;",
 "employer logos;","generic office B-roll;","flashy transitions;",
 "constant zooms;","fake shock expressions;","red warning graphics;",
 "AI-generated scenery;","social-media template effects."],after=3)
compress(d, 1.18, 0.62)
d.save(os.path.join(SH,"Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx"))

# ---------------------------------------------------------------- 7. README
FILES=(["LONG_FORM/"+f for f in sorted(os.listdir(LF))]
      +["SHORTS/"+f for f in sorted(os.listdir(SH))])
R=["VIDEO 5 — H.I.T. FINAL RECORDING PACKAGE","",
 "Title:             %s"%TITLE,
 "Thumbnail:         %s"%THUMB,
 "CTA:               %s"%CTA,
 "CTA URL:           %s"%CTA_URL,
 "CTA production",
 "gate:              SATISFIED",
 "Watch next:        %s"%NEXT,"",
 "Long-form:         Revised under H.I.T.",
 "Slides:            UNCHANGED. 12 main slides.",
 "Reveal deck:       UNCHANGED.",
 "Thumbnail:         UNCHANGED.",
 "Shorts:            Four separately recorded vertical scripts.",
 "Editor directions: Separated from recording copy.","",
 "-"*70,"","WHAT EACH FILE IS","",
 "LONG_FORM/","",
 "  Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.docx",
 "  Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
 "      Temidayo's recording copy. Spoken script in large text; slide markers",
 "      in tinted bands. The markers are not spoken.","",
 "  Video5ReadingScriptnomarkers_HIT_v2.0.docx",
 "  Video5ReadingScriptnomarkers_HIT_v2.0.txt",
 "      The same spoken words with the slide markers removed.","",
 "  Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx",
 "      For the editor. The H.I.T. first-30-second plan, the factual boundary",
 "      on the scope-expansion proof, editorial rhythm after 0:30, the",
 "      existing 12-slide map, the let-the-visual-carry principle, and the",
 "      visual and safety boundaries. Not for the teleprompter.","",
 "  Video_5_Publishing_Package_HIT_v2.0.docx",
 "      Title, thumbnail, search language, the copy-ready description with",
 "      its approved emoji treatment, working chapter estimates, pinned",
 "      comment and the tag field.","",
 "SHORTS/","",
 "  Four recording documents, one per Short. These contain Temidayo's",
 "  recording copy and no editor directions.","",
 "  Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "      For the editor. On-screen hooks and visual treatment for all four.","",
 "-"*70,"","ALL FILES IN THIS PACKAGE","",]
for f in FILES: R.append("  "+f)
R+=["  README_FINAL.txt","  SHA256SUMS.txt","",
 "-"*70,"","WORKING CHAPTER TIMESTAMPS","",
 "The chapter timestamps in the publishing package are WORKING ESTIMATES",
 "derived from the script. They were not measured from an edit. The editor",
 "must replace every one of them from the finished cut before publishing.","",
 "-"*70,"","FACTUAL BOUNDARY ON THE PERSONAL PROOF","",
 "The confirmed evidence is only that Temidayo's scope expanded after roughly",
 "six months and that trust extended beyond the original box. No employer,",
 "exact role, exact assignment, causal claim, quote, metric or unsupported",
 "result is added anywhere in this package.","",
 "-"*70,"","CHECKSUMS","",
 "SHA256SUMS.txt covers the other 12 user-facing files in this package. It",
 "does not hash itself, and it carries no ZIP checksum. The archive's own",
 "SHA-256 is in the sibling file:",
 "  Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256","",
 "-"*70,"","WHAT WAS NOT CHANGED","",
 "The existing Video 5 PowerPoint deck (12 slides), the reveal-build deck, the",
 "approved thumbnail, the Career Decision Evidence Check page, every website",
 "file, every product and every other video are unchanged. This revision is",
 "spoken script, editor instruction and publishing copy only.","",
 "The 12-slide deck remains authoritative. The teleprompter's 12 slide markers",
 "map to it in order, slide 1 to slide 12.",""]
open(os.path.join(ROOT,"README_FINAL.txt"),"w").write("\n".join(R))
print("shorts editor brief and README written")

# ------------------------------------------- 8. checksums and the master ZIP
MANIFEST=[
 "LONG_FORM/Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.docx",
 "LONG_FORM/Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
 "LONG_FORM/Video5ReadingScriptnomarkers_HIT_v2.0.docx",
 "LONG_FORM/Video5ReadingScriptnomarkers_HIT_v2.0.txt",
 "LONG_FORM/Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx",
 "LONG_FORM/Video_5_Publishing_Package_HIT_v2.0.docx",
 "SHORTS/Video_5_Short_1_You_May_Not_Need_To_Leave.docx",
 "SHORTS/Video_5_Short_2_More_Tasks_Not_More_Judgment.docx",
 "SHORTS/Video_5_Short_3_More_Scope_Not_Automatic_Growth.docx",
 "SHORTS/Video_5_Short_4_Three_Questions_Before_You_Move.docx",
 "SHORTS/Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "README_FINAL.txt",
]
SUMS="SHA256SUMS.txt"
ZIP="/tmp/v5hit/Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip"

def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as fh:
        for b in iter(lambda: fh.read(1<<20), b""): h.update(b)
    return h.hexdigest()

for m in MANIFEST:
    assert os.path.isfile(os.path.join(ROOT,m)), "missing from build: "+m
on_disk=set()
for dp,dn,fn in os.walk(ROOT):
    dn[:]=[x for x in dn if x!="__pycache__"]
    for f in fn:
        if f.endswith(".pyc"): continue
        on_disk.add(os.path.relpath(os.path.join(dp,f),ROOT).replace(os.sep,"/"))
unexpected=sorted(on_disk-set(MANIFEST)-{SUMS})
assert not unexpected, "unexpected files in package directory: %r"%unexpected

L=["# VIDEO 5 - H.I.T. FINAL RECORDING PACKAGE",
   "# SHA-256 of the 12 user-facing files in this package.",
   "# SHA256SUMS.txt cannot hash itself. The master ZIP cannot contain its own",
   "# checksum either; it is published in the sibling file",
   "# Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip.sha256",""]
for m in MANIFEST: L.append("%s  %s"%(sha256(os.path.join(ROOT,m)),m))
open(os.path.join(ROOT,SUMS),"w").write("\n".join(L)+"\n")

if os.path.exists(ZIP): os.remove(ZIP)
with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED) as z:
    for m in MANIFEST+[SUMS]:
        z.write(os.path.join(ROOT,m), "Video_5_HIT_FINAL/"+m)
zsha=sha256(ZIP)
open(ZIP+".sha256","w").write("%s  %s\n"%(zsha,os.path.basename(ZIP)))

PROV="/tmp/v5hit/_source"
shutil.rmtree(PROV,ignore_errors=True); os.makedirs(PROV)
import shutil as _sh
for f in ("script_text.py","build.py","qa.py"):
    src="/tmp/v5hit/"+f
    if os.path.isfile(src): _sh.copy2(src, os.path.join(PROV,f))
CANON="/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/95568f64-Video_5_Code_Prompt_HIT_Final.txt"
if os.path.isfile(CANON):
    _sh.copy2(CANON, os.path.join(PROV,"Video_5_Code_Prompt_HIT_Final.txt"))
print("ZIP sha256:",zsha)
