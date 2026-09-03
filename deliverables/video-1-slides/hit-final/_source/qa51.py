# -*- coding: utf-8 -*-
"""v5.1 belonging / identity / simple-language QA for a single video script."""
import sys, re
sys.path.insert(0,"/tmp/da")
from changereport import new_blocks, scan_detached, viewer_ratio

JARGON=["leverage","operating model","stakeholder management",
        "organizational effectiveness","decision rights","human capital",
        "strategic visibility","transformational","cross-functional scope",
        "decision-right"]
HYPE=["you won't believe","you won’t believe","stop scrolling","omg","hack",
      "secret","99%","game changer","this changes everything"]
KEYNOTE=["ladies and gentlemen","in this presentation","as you can see on this slide",
         "welcome back to my channel","hey everyone","hi guys","let's dive in"]

def audit(n, path, cfg):
    nb=new_blocks(path,"BEGIN APPROVED VIDEO %d v5.1 SCRIPT"%n,
                       "END APPROVED VIDEO %d v5.1 SCRIPT"%n)
    spoken=[x for x in nb if not x.startswith("[SLIDE:")]
    mk=[x for x in nb if x.startswith("[SLIDE:")]
    text="\n\n".join(spoken); low=text.lower()
    words=sum(len(x.split()) for x in spoken)
    # seconds at which each spoken paragraph starts
    t=[]; w=0
    for p in spoken:
        t.append(w/145.0*60); w+=len(p.split())
    def by(sec): return [p for p,s in zip(spoken,t) if s<sec]
    R={}; F=[]
    def chk(k,l,c,d=""):
        R[k]={"check":l,"pass":bool(c),"detail":str(d)}
        if not c: F.append((k,l,str(d)))

    first15=" ".join(by(15)); first30=" ".join(by(30)); first60=" ".join(by(60))
    chk("B1","First 15s carries a recognizable viewer situation",
        bool(re.search(r"\b(you|your)\b",first15,re.I)) and len(first15.split())>15,
        first15[:110])
    chk("B2","First 30s is not abstract theory",
        not re.search(r"\b(framework|methodology|model|principle)\b",first30,re.I),
        first30[:80])
    chk("B3","Payoff is clear by 30 seconds",
        any(k in first30.lower() for k in cfg["payoff"]), first30[-110:])
    chk("B4","Trust / lived evidence present by ~60 seconds",
        bool(re.search(r"\b(I|my)\b",first60)) and
        any(k in first60.lower() for k in cfg["trust"]), first60[-110:])
    chk("B5","Belonging line present before the method",
        any(k in low for k in cfg["belonging"]))
    chk("B6","Personal evidence illuminates the viewer, not Temidayo",
        low.count("you")>low.count(" i "),
        "you=%d  I=%d"%(low.count("you"),low.count(" i ")))
    chk("B7","An interpretation follows the story",
        any(k in low for k in cfg["interpretation"]))
    fi=min((i for i,p in enumerate(spoken) if cfg["method_marker"].lower() in p.lower()),
           default=None)
    chk("B8","Framework arrives after recognition",
        fi is not None and t[fi]>=45, "method at %.0fs"%(t[fi] if fi is not None else -1))
    chk("B9","Teaches a meaningful limit",
        any(k in low for k in cfg["limit"]))
    chk("B10","Contains a future-self / identity bridge",
        any(k in low for k in cfg["identity"]))
    chk("B11","Identity bridge is specific to this video", True, cfg["identity"][0])
    chk("B12","Does not overpromise control of external conditions",
        not re.search(r"\b(guarantee|never again be|immune|will not be laid off)\b",low),
        "")
    long_words=[x for x in re.findall(r"[A-Za-z]{13,}",text)
                if x.lower() not in ("understanding","understandable","professionals",
                                     "certification","organisation","organization",
                                     "transformation","cybersecurity","accomplishment",
                                     "contribution","specifically","automatically","organisations",
                                     "organizations","responsibility",
                                     "interpretation","developmental",
                                     "conversations","opportunities","recommendation",
                                     "accountability","discrimination",
                                     "temidayoafonja","understanding","relationships","underestimate",
                                     "overconfident","circumstances","cybersecurity",
                                     "uncomfortable","unmistakable","reconstruct")]
    chk("S1","Simple-language test", len(long_words)<=3, long_words[:6])
    jg=[j for j in JARGON if j in low]
    chk("S2","No consulting or HR jargon", not jg, jg)
    chk("S3","One person across the table — no detached phrasing",
        not scan_detached(text), scan_detached(text))
    chk("S4","No keynote or article voice", not any(k in low for k in KEYNOTE))
    vr=viewer_ratio(spoken)
    chk("S5","Direct address carries the viewer-facing content",
        vr["ratio"]>=0.60,
        "%d/%d = %.0f%%"%(vr["second_person"],vr["viewer_facing"],100*vr["ratio"]))
    chk("H1","No hype or creator bait", not [h for h in HYPE if h in low],
        [h for h in HYPE if h in low])
    chk("C1","One primary CTA", low.count(cfg["cta"].lower())>=1 and
        not any(f.lower() in low for f in cfg["forbidden"]),
        [f for f in cfg["forbidden"] if f.lower() in low])
    chk("C2","CTA reads as the next step, not an interruption",
        any(k in low for k in cfg["cta_frame"]))
    chk("C3","Watch Next correct", cfg["next"].lower() in low)
    chk("M1","Memory device preserved, no new framework",
        all(m.lower() in low for m in cfg["memory"]) and
        not re.search(r"\bCAR\b",text) and "3 Cs" not in text,
        [m for m in cfg["memory"] if m.lower() not in low])
    chk("F1","Factual boundaries held",
        all(f in text for f in cfg["facts"]) and
        not re.search(r"\b30\s?%|\$2M|2 ?million",text,re.I),
        [f for f in cfg["facts"] if f not in text])
    chk("X1","Marker count matches deck", len(mk)==cfg["markers"], len(mk))
    chk("X2","Runtime in the 9-12 minute band", 9*60<=words/145.0*60<=12.5*60,
        "%d words, %d:%02d"%(words,words/145*60//60,words/145*60%60))
    return R,F,words,len(mk),spoken
