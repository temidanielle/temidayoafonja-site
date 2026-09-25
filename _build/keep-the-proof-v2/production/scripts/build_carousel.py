#!/usr/bin/env python3
"""Keep the Proof V2 Gumroad carousel, rebuilt to match the v1 design:
cream ground, navy Cormorant headlines, gold + rust accents, cream cards,
the stacked-documents mark top-left of every slide, a rust rule under each
headline. Slides 01-05 keep the current V2 wording; slide 06 uses the new
two-tools copy with no prices. V2 Handbook cover as the tilted book on 01.
Rendered via Chromium screenshot at 1600x900, downscaled to 640x360."""
import subprocess, os, sys, base64
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image

ROOT = "/home/user/temidayoafonja-site"
FONTS = f"file://{ROOT}/fonts"
PROD = f"{ROOT}/_build/keep-the-proof-v2/production"
ICONS = f"{PROD}/assets/icons"
OUT = f"{PROD}/gumroad/carousel"
RENDER = f"{PROD}/renders/carousel"
COVER = f"{ROOT}/keep-the-proof-v2-cover.png"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

PAGE="#FBF8F2"; CREAM="#F5F0E8"; CARD2="#F0EBE0"; NAVY="#0F2347"; INK="#182238"
GOLD="#C9A84C"; GOLDINK="#A5842E"; RUST="#C1440E"; SLATE="#5D6676"; HAIR="#E4DCCB"

os.makedirs(OUT, exist_ok=True)
os.makedirs(RENDER, exist_ok=True)

def datauri(path):
    with open(path,"rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()
COVER_URI = datauri(COVER)
def icon_uri(name): return datauri(f"{ICONS}/{name}.png")

# The Keep the Proof mark: two stacked document cards, a gold line on the
# front card, a rust square at the back card's top-right corner.
def ktp_mark(px=62):
    return f'''<svg width="{px}" height="{px}" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="8" width="33" height="41" rx="4" fill="{PAGE}" stroke="{NAVY}" stroke-width="2.4"/>
  <rect x="43.5" y="10.5" width="8" height="8" rx="1.5" fill="{RUST}"/>
  <rect x="9" y="16" width="33" height="41" rx="4" fill="{CREAM}" stroke="{NAVY}" stroke-width="2.4"/>
  <rect x="16" y="30" width="19" height="3" rx="1.5" fill="{GOLD}"/>
</svg>'''

def fieldkit_mark(px=44):
    return f'''<svg width="{px}" height="{px}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="6" y="6" width="14" height="14" rx="2" fill="none" stroke="{GOLD}" stroke-width="2.2"/>
  <rect x="28" y="6" width="14" height="14" rx="2" fill="{RUST}"/>
  <rect x="6" y="28" width="14" height="14" rx="2" fill="none" stroke="{GOLD}" stroke-width="2.2"/>
  <rect x="28" y="28" width="14" height="14" rx="2" fill="none" stroke="{GOLD}" stroke-width="2.2"/>
</svg>'''

FONTFACE = f'''
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-600-normal-latin-abcaa8.woff2') format('woff2');font-weight:600;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-500-normal-latin-abcaa8.woff2') format('woff2');font-weight:500;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-normal-latin-abcaa8.woff2') format('woff2');font-weight:400;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-italic-latin-4db21d.woff2') format('woff2');font-weight:400;font-style:italic;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-400-normal-latin-1c49a6.woff2') format('woff2');font-weight:400;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-500-normal-latin-1c49a6.woff2') format('woff2');font-weight:500;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-600-normal-latin-1c49a6.woff2') format('woff2');font-weight:600;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-700-normal-latin-1c49a6.woff2') format('woff2');font-weight:700;}}
'''

BASE = f'''
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:1600px;height:900px;overflow:hidden;background:{PAGE};}}
.stage{{width:1600px;height:900px;background:{PAGE};color:{INK};font-family:'DM Sans',sans-serif;
  padding:74px 95px 62px;position:relative;display:flex;flex-direction:column;overflow:hidden;}}
.mark{{margin-bottom:34px;}}
.eyebrow{{font-family:'DM Sans';font-weight:700;letter-spacing:.22em;font-size:16px;
  text-transform:uppercase;color:{GOLDINK};margin-bottom:14px;}}
.headline{{font-family:'Cormorant',serif;font-weight:600;color:{NAVY};line-height:1.04;}}
.hrule{{width:66px;height:3px;background:{RUST};margin:20px 0 0;}}
.subline{{font-family:'DM Sans';font-weight:400;color:{SLATE};line-height:1.4;}}
.grow{{flex:1 1 auto;min-height:0;}}
.footnote{{padding-top:28px;font-family:'Cormorant',serif;font-style:italic;font-size:23px;color:{SLATE};}}
.card{{background:{CREAM};border:1px solid {HAIR};border-radius:8px;}}
'''

def doc(css, inner):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>'
            f'{FONTFACE}{BASE}{css}</style></head><body>{inner}</body></html>')

# ---------- Slide 01: hero ----------
def slide01():
    css = f'''
.s1-body{{display:flex;flex-direction:row;align-items:center;}}
.s1-left{{flex:1;padding-right:56px;}}
.s1 .headline{{font-size:82px;margin-top:6px;}}
.s1-accent{{font-family:'Cormorant',serif;font-weight:600;font-size:30px;color:{RUST};margin-top:30px;}}
.s1-small{{font-family:'DM Sans';font-weight:400;font-size:22px;color:{SLATE};margin-top:12px;letter-spacing:.01em;}}
.s1-right{{width:520px;display:flex;align-items:center;justify-content:center;}}
.bookwrap{{position:relative;width:400px;height:520px;}}
.bookstack{{position:absolute;top:0;left:0;width:400px;height:518px;border-radius:6px;
  transform:rotate(3.2deg);}}
.bookstack.s2{{background:#20406a;top:14px;left:20px;box-shadow:0 24px 50px rgba(15,35,71,.20);}}
.bookstack.s3{{background:#173257;top:8px;left:11px;}}
.bookimg{{position:absolute;top:0;left:0;width:400px;border-radius:6px;transform:rotate(3.2deg);
  box-shadow:0 30px 60px rgba(15,35,71,.42);outline:1px solid rgba(201,168,76,.35);}}
.website{{padding-top:18px;font-family:'DM Sans';font-weight:700;
  letter-spacing:.26em;font-size:17px;text-transform:uppercase;color:{GOLD};}}
'''
    inner = f'''<div class="stage s1">
  <div class="mark">{ktp_mark()}</div>
  <div class="s1-body">
    <div class="s1-left">
      <div class="eyebrow">Keep the Proof</div>
      <div class="headline">Build the record<br>before you need it.</div>
      <div class="hrule"></div>
      <div class="s1-accent">A guided system for building your professional record</div>
      <div class="s1-small">Capture. Clarify. Carry.</div>
    </div>
    <div class="s1-right">
      <div class="bookwrap">
        <div class="bookstack s2"></div>
        <div class="bookstack s3"></div>
        <img class="bookimg" src="{COVER_URI}">
      </div>
    </div>
  </div>
  <div class="grow"></div>
  <div class="website">Temidayoafonja.com</div>
</div>'''
    return doc(css, inner)

# ---------- Slide 02: what you receive ----------
def slide02():
    css = f'''
.s2 .headline{{font-size:52px;}}
.s2 .subline{{font-size:22px;margin-top:16px;max-width:34em;}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px;}}
.fcard{{border-top:4px solid {GOLD};padding:26px 30px 28px;display:flex;flex-direction:column;}}
.fcard img{{width:40px;height:40px;margin-bottom:14px;}}
.fk{{font-family:'Cormorant',serif;font-weight:600;font-size:26px;color:{NAVY};margin-bottom:9px;line-height:1.05;}}
.fb{{font-family:'DM Sans';font-weight:400;font-size:19px;line-height:1.42;color:{INK};}}
'''
    cards=[("about","Start Here","A short orientation and a map of the bundle."),
           ("proofline","Guided Handbook","The full method, with a completed example beside every tool."),
           ("keep","Your Professional Record","Your editable working record. Opens in Word, Google Docs, or Pages."),
           ("words","Printable &amp; Fillable Tools","The same fields, to print or type into.")]
    cs="".join(f'<div class="card fcard"><img src="{icon_uri(i)}"><div class="fk">{t}</div><div class="fb">{b}</div></div>' for i,t,b in cards)
    inner=f'''<div class="stage s2">
  <div class="mark">{ktp_mark()}</div>
  <div class="eyebrow">What You Receive</div>
  <div class="headline">Four files. One record you keep.</div>
  <div class="hrule"></div>
  <div class="subline">A guided method, and a record that lives in an account you control.</div>
  <div class="grid2">{cs}</div>
</div>'''
    return doc(css, inner)

# ---------- Slide 03: how it works ----------
def slide03():
    css = f'''
.s3 .headline{{font-size:52px;}}
.s3 .subline{{font-size:22px;margin-top:16px;}}
.steps{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;margin-top:44px;}}
.step{{background:{CREAM};border:1px solid {HAIR};border-radius:8px;padding:26px 28px 30px;position:relative;}}
.step.b1{{border-top:4px solid {GOLD};}}
.step.b2{{border-top:4px solid {GOLD};}}
.step.b3{{border-top:4px solid {RUST};}}
.step-top{{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;}}
.step-top img{{width:42px;height:42px;}}
.step-n{{font-family:'Cormorant',serif;font-weight:600;font-size:34px;color:{RUST};line-height:1;}}
.step-t{{font-family:'Cormorant',serif;font-weight:600;font-size:27px;color:{NAVY};margin-bottom:11px;line-height:1.05;}}
.step-b{{font-family:'DM Sans';font-weight:400;font-size:19px;line-height:1.44;color:{INK};}}
'''
    steps=[("capture","1","Capture","Catch the work in two minutes, before the details fade.","b1"),
           ("clarify","2","Clarify","Separate your part from the team's result, and name the judgment and the scope.","b2"),
           ("carry","3","Carry","Put it in language an outsider can follow, then into a resume, an interview, or a promotion note.","b3")]
    cs="".join(f'<div class="step {bc}"><div class="step-top"><img src="{icon_uri(i)}"><span class="step-n">{n}</span></div><div class="step-t">{t}</div><div class="step-b">{b}</div></div>' for i,n,t,b,bc in steps)
    inner=f'''<div class="stage s3">
  <div class="mark">{ktp_mark()}</div>
  <div class="eyebrow">How It Works</div>
  <div class="headline">Capture. Clarify. Carry.</div>
  <div class="hrule"></div>
  <div class="subline">Three steps you return to whenever the work is fresh.</div>
  <div class="steps">{cs}</div>
  <div class="grow"></div>
  <div class="footnote">Sixty minutes is a guide. Take it in one sitting or several.</div>
</div>'''
    return doc(css, inner)

# ---------- Slide 04: before and after ----------
def slide04():
    css = f'''
.s4 .headline{{font-size:50px;}}
.s4 .subline{{font-size:21px;margin-top:15px;max-width:44em;}}
.ba{{display:flex;align-items:stretch;gap:0;margin-top:40px;}}
.ba-card{{flex:1;min-height:358px;background:{CARD2};border:1px solid {HAIR};border-radius:8px;padding:30px 34px;display:flex;flex-direction:column;}}
.ba-card.after{{background:{CREAM};border:1px solid {GOLD};border-left:6px solid {RUST};}}
.ba-lbl{{font-family:'DM Sans';font-weight:700;letter-spacing:.14em;font-size:15px;text-transform:uppercase;color:{SLATE};margin-bottom:18px;}}
.ba-card.after .ba-lbl{{color:{RUST};}}
.ba-quote{{font-family:'Cormorant',serif;font-weight:600;font-size:38px;line-height:1.14;color:{NAVY};}}
.ba-body{{font-family:'Cormorant',serif;font-weight:500;font-size:27px;line-height:1.28;color:{NAVY};}}
.ba-cap{{font-family:'DM Sans';font-weight:400;font-size:18px;line-height:1.42;color:{SLATE};margin-top:auto;padding-top:22px;}}
.arrow{{width:56px;flex:0 0 auto;display:flex;align-items:center;justify-content:center;}}
.arrow-c{{width:44px;height:44px;border-radius:50%;border:2px solid {GOLD};display:flex;align-items:center;justify-content:center;color:{RUST};font-size:22px;line-height:1;}}
.footnote{{color:{SLATE};}}
'''
    proof="Redesigned new-hire onboarding for a growing operations team, cutting time to full productivity and reducing early attrition, with the model later adopted by two other departments."
    inner=f'''<div class="stage s4">
  <div class="mark">{ktp_mark()}</div>
  <div class="eyebrow">From Memory to Evidence</div>
  <div class="headline">A vague line becomes portable evidence.</div>
  <div class="hrule"></div>
  <div class="subline">The system pushes every entry past what you did to what became different because you did it.</div>
  <div class="ba">
    <div class="ba-card"><div class="ba-lbl">Before</div>
      <div class="ba-quote">&ldquo;Helped with onboarding.&rdquo;</div>
      <div class="ba-cap">Vague. Easy to forget. It claims nothing a reader can examine.</div></div>
    <div class="arrow"><div class="arrow-c">&rsaquo;</div></div>
    <div class="ba-card after"><div class="ba-lbl">A Proof Line</div>
      <div class="ba-body">&ldquo;{proof}&rdquo;</div>
      <div class="ba-cap">Maya&rsquo;s Proof Line, from the Guided Handbook.</div></div>
  </div>
  <div class="grow"></div>
  <div class="footnote">A Proof Line does not need a number to be strong, and it must never contain an invented one.</div>
</div>'''
    return doc(css, inner)

# ---------- Slide 05: who it is for ----------
def slide05():
    css = f'''
.s5 .headline{{font-size:52px;}}
.s5 .subline{{font-size:21px;margin-top:15px;max-width:46em;}}
.grid4{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:40px;}}
.wcard{{background:{CREAM};border:1px solid {HAIR};border-left:4px solid {GOLD};border-radius:6px;padding:24px 30px 26px;}}
.wcard.r{{border-left-color:{RUST};}}
.wt{{font-family:'Cormorant',serif;font-weight:600;font-size:25px;color:{NAVY};margin-bottom:8px;line-height:1.05;}}
.wb{{font-family:'DM Sans';font-weight:400;font-size:19px;line-height:1.44;color:{INK};}}
'''
    cards=[("Before a performance review","Walk in able to account for the whole year, accurately.",""),
           ("Before a promotion case","Bring specific evidence of what changed because of your work.","r"),
           ("Before an interview or a new resume","Have portable, specific language ready to reuse.","r"),
           ("Before a reorg or a career move","Know what your work built and what can travel with you.","")]
    cs="".join(f'<div class="wcard {c}"><div class="wt">{t}</div><div class="wb">{b}</div></div>' for t,b,c in cards)
    inner=f'''<div class="stage s5">
  <div class="mark">{ktp_mark()}</div>
  <div class="eyebrow">Who It Is For</div>
  <div class="headline">For people who do the work and lose the proof.</div>
  <div class="hrule"></div>
  <div class="subline">The work was constant. You solved the problem, absorbed the lesson, and moved to the next thing before the last one had a name.</div>
  <div class="grid4">{cs}</div>
</div>'''
    return doc(css, inner)

# ---------- Slide 06: two tools ----------
def slide06():
    css = f'''
.s6 .headline{{font-size:50px;}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:44px;}}
.tcard{{border-radius:10px;padding:34px 38px;display:flex;flex-direction:column;min-height:436px;}}
.tcard.ktp{{background:{CREAM};border:1.5px solid {GOLD};}}
.tcard.fk{{background:{NAVY};}}
.tmark{{margin-bottom:26px;}}
.ttitle{{font-family:'DM Sans';font-weight:700;letter-spacing:.1em;font-size:20px;text-transform:uppercase;color:{NAVY};margin-bottom:7px;}}
.tcard.fk .ttitle{{color:{PAGE};}}
.tsub{{font-family:'DM Sans';font-weight:700;letter-spacing:.09em;font-size:13.5px;text-transform:uppercase;color:{GOLDINK};margin-bottom:22px;}}
.tcard.fk .tsub{{color:{GOLD};}}
.tq{{font-family:'Cormorant',serif;font-weight:600;font-size:29px;line-height:1.24;color:{NAVY};margin-bottom:28px;}}
.tcard.fk .tq{{color:{PAGE};}}
.tlist{{list-style:none;margin:auto 0 0;padding:0;}}
.tlist li{{font-family:'DM Sans';font-weight:400;font-size:20px;line-height:1.4;color:{INK};padding-left:20px;position:relative;margin-bottom:15px;}}
.tcard.fk .tlist li{{color:#DDE4EE;}}
.tlist li:last-child{{margin-bottom:0;}}
.tlist li:before{{content:"";position:absolute;left:0;top:9px;width:5px;height:16px;border-radius:1px;background:{GOLD};}}
.tcard.fk .tlist li:before{{background:{RUST};}}
.footnote{{color:{NAVY};}}
'''
    ktp=f'''<div class="tcard ktp">
      <div class="tmark">{ktp_mark(46)}</div>
      <div class="ttitle">Keep the Proof</div>
      <div class="tsub">A guided system for building your professional record</div>
      <div class="tq">&ldquo;What have I done, what changed, and what does it prove I can do?&rdquo;</div>
      <ul class="tlist">
        <li>Guided Handbook with worked examples</li>
        <li>Your Professional Record, editable for years</li>
        <li>Printable and fillable tools</li>
      </ul>
    </div>'''
    fk=f'''<div class="tcard fk">
      <div class="tmark">{fieldkit_mark(44)}</div>
      <div class="ttitle">The Capability Formation Field Kit</div>
      <div class="tsub">An evidence-led career position assessment</div>
      <div class="tq">&ldquo;What is my current work building in me?&rdquo;</div>
      <ul class="tlist">
        <li>Reads your last 90 days</li>
        <li>Density and Optionality scores</li>
        <li>A dated position you can rescore</li>
      </ul>
    </div>'''
    inner=f'''<div class="stage s6">
  <div class="mark">{ktp_mark()}</div>
  <div class="eyebrow">Two Tools, Two Questions</div>
  <div class="headline">Different questions. Different tools.</div>
  <div class="hrule"></div>
  <div class="two">{ktp}{fk}</div>
  <div class="grow"></div>
  <div class="footnote">Choose Keep the Proof when you want to capture evidence of what you have already done.</div>
</div>'''
    return doc(css, inner)

SLIDES = [
    ("01_hero", slide01),
    ("02_what_you_receive", slide02),
    ("03_how_it_works", slide03),
    ("04_before_and_after", slide04),
    ("05_who_it_is_for", slide05),
    ("06_two_tools", slide06),
]

def render(name, fn):
    hp=f"{RENDER}/{name}.html"; open(hp,"w",encoding="utf-8").write(fn())
    big=f"{OUT}/{name}_1600x900_v2.png"
    # Capture taller than 900 then crop: a window sized exactly 1600x900 clips the
    # bottom band of content in this headless build, so render with headroom.
    r=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1600,1010",
        f"--screenshot={big}", f"file://{hp}"], capture_output=True, text=True)
    if not os.path.exists(big):
        print("FAIL", name, r.stderr[-600:]); return None
    im=Image.open(big).convert("RGB").crop((0,0,1600,900))
    im.save(big)
    Image.open(big).convert("RGB").resize((640,360),Image.LANCZOS).save(f"{OUT}/{name}_640x360_v2.png")
    print("OK",name)
    return big

bigs=[render(n,f) for n,f in SLIDES]

# thumbnail 600x600 from slide 01 (left title region, square)
hero=Image.open(f"{OUT}/01_hero_1600x900_v2.png").convert("RGB")
hero.crop((0,0,900,900)).resize((600,600),Image.LANCZOS).save(f"{OUT}/gumroad_thumbnail_600x600.png")
print("thumbnail 600x600 written")

# contact sheet 2x3
tw,th,pad=800,450,24
W=2*tw+pad*3; H=3*th+pad*4
sheet=Image.new("RGB",(W,H),(251,248,242))
for i,(n,_) in enumerate(SLIDES):
    im=Image.open(f"{OUT}/{n}_1600x900_v2.png").convert("RGB").resize((tw,th),Image.LANCZOS)
    c=i%2; r=i//2
    sheet.paste(im,(pad+c*(tw+pad), pad+r*(th+pad)))
sheet.save(f"{OUT}/contact_sheet_v2.png")
print("contact sheet written", sheet.size)
for f in sorted(os.listdir(OUT)): print("  ",f)
