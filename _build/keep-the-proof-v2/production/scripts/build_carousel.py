#!/usr/bin/env python3
"""Build the Keep the Proof V2 Gumroad carousel: 6 slides at 1600x900 and 640x360,
a contact sheet, and a 600x600 thumbnail from slide 01. V2 Handbook cover + V2 icons.
No prices, no page counts. Rendered via Chromium screenshot, downscaled with PIL."""
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

NAVY="#112345"; CREAM="#F5F1E8"; GOLD="#C9A84C"; INK="#1c2333"; DIM="#c9d0dd"; RUST="#C1440E"

os.makedirs(OUT, exist_ok=True)
os.makedirs(RENDER, exist_ok=True)

def datauri(path):
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mt = "image/png" if ext=="png" else "image/jpeg"
    with open(path,"rb") as f:
        return f"data:{mt};base64," + base64.b64encode(f.read()).decode()

COVER_URI = datauri(COVER)
def icon_uri(name): return datauri(f"{ICONS}/{name}.png")

FONTFACE = f'''
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-600-normal-latin-abcaa8.woff2') format('woff2');font-weight:600;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-500-normal-latin-abcaa8.woff2') format('woff2');font-weight:500;}}
@font-face{{font-family:'Cormorant';src:url('{FONTS}/CormorantGaramond-400-italic-latin-4db21d.woff2') format('woff2');font-weight:400;font-style:italic;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-400-normal-latin-1c49a6.woff2') format('woff2');font-weight:400;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-500-normal-latin-1c49a6.woff2') format('woff2');font-weight:500;}}
@font-face{{font-family:'DM Sans';src:url('{FONTS}/DMSans-600-normal-latin-1c49a6.woff2') format('woff2');font-weight:600;}}
'''

BASE_CSS = f'''
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:1600px;height:900px;overflow:hidden;background:{NAVY};}}
.stage{{width:1600px;height:900px;background:{NAVY};color:{CREAM};font-family:'DM Sans',sans-serif;
  padding:96px 104px;position:relative;display:flex;flex-direction:column;overflow:hidden;}}
.eyebrow{{font-family:'DM Sans';font-weight:600;letter-spacing:.34em;font-size:20px;color:{GOLD};}}
.headline{{font-family:'Cormorant',serif;font-weight:600;color:{CREAM};line-height:1.03;}}
.subline{{font-family:'Cormorant',serif;font-style:italic;color:{DIM};line-height:1.32;}}
.footer{{margin-top:auto;padding-top:36px;font-family:'DM Sans';font-weight:500;
  letter-spacing:.16em;font-size:19px;color:{GOLD};}}
.footer.plain{{letter-spacing:0;font-weight:400;font-style:italic;font-family:'Cormorant',serif;
  font-size:26px;color:{DIM};}}
.grule{{width:72px;height:4px;background:{GOLD};}}
.card{{background:{CREAM};color:{INK};border-radius:14px;border-top:5px solid {GOLD};}}
.card .cico{{width:46px;height:46px;display:block;}}
.card .ck{{font-family:'DM Sans';font-weight:600;font-size:23px;color:{NAVY};letter-spacing:.01em;}}
.card .cb{{font-family:'DM Sans';font-weight:400;font-size:20px;line-height:1.42;color:{INK};}}
'''

def page(inner, extra_css=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{extra_css}</style></head><body><div class="stage">{inner}</div></body></html>'''

# ---------- Slide 01: hero ----------
def slide01():
    css = f'''
.s1-body{{display:flex;flex-direction:row;align-items:center;flex:1;gap:0;}}
.s1-left{{flex:1;padding-right:60px;}}
.s1 .eyebrow{{margin-bottom:30px;}}
.s1 .headline{{font-size:96px;margin-bottom:26px;}}
.s1 .grule{{margin-bottom:30px;}}
.s1-accent{{font-family:'Cormorant',serif;font-style:italic;font-size:38px;color:#e8e0cf;line-height:1.24;margin-bottom:40px;max-width:14em;}}
.s1-small{{font-family:'DM Sans';font-weight:600;letter-spacing:.14em;font-size:26px;color:{GOLD};}}
.s1-right{{width:470px;display:flex;align-items:center;justify-content:center;}}
.s1-cover{{width:430px;border-radius:8px;box-shadow:0 30px 70px rgba(0,0,0,.5),0 0 0 1px rgba(201,168,76,.35);}}
.s1-foot{{letter-spacing:.28em;}}
'''
    inner = f'''
<div class="stage s1">
  <div class="s1-body">
    <div class="s1-left">
      <div class="eyebrow">KEEP THE PROOF</div>
      <div class="headline">Build the record<br>before you need it.</div>
      <div class="grule"></div>
      <div class="s1-accent">A guided system for building your professional record</div>
      <div class="s1-small">Capture. Clarify. Carry.</div>
    </div>
    <div class="s1-right"><img class="s1-cover" src="{COVER_URI}"></div>
  </div>
  <div class="footer s1-foot">TEMIDAYOAFONJA.COM</div>
</div>'''
    # note: stage already wraps; return raw full body
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

# ---------- Slide 02: what you receive ----------
def slide02():
    css = f'''
.head-wrap{{margin-bottom:44px;}}
.s2 .eyebrow{{margin-bottom:22px;}}
.s2 .headline{{font-size:66px;margin-bottom:16px;}}
.s2 .subline{{font-size:30px;max-width:30em;}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:26px;}}
.grid2 .card{{padding:30px 34px 32px;display:flex;flex-direction:column;}}
.grid2 .cico{{margin-bottom:16px;}}
.grid2 .ck{{margin-bottom:10px;}}
'''
    cards = [
        ("about","Start Here","A short orientation and a map of the bundle."),
        ("proofline","Guided Handbook","The full method, with a completed example beside every tool."),
        ("keep","Your Professional Record","Your editable working record. Opens in Word, Google Docs, or Pages."),
        ("words","Printable &amp; Fillable Tools","The same fields, to print or type into."),
    ]
    cardhtml = "".join(
        f'<div class="card"><img class="cico" src="{icon_uri(ic)}"><div class="ck">{k}</div><div class="cb">{b}</div></div>'
        for ic,k,b in cards)
    inner = f'''
<div class="stage s2">
  <div class="head-wrap">
    <div class="eyebrow">WHAT YOU RECEIVE</div>
    <div class="headline">Four files. One record you keep.</div>
    <div class="subline">A guided method, and a record that lives in an account you control.</div>
  </div>
  <div class="grid2">{cardhtml}</div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

# ---------- Slide 03: how it works ----------
def slide03():
    css = f'''
.s3 .eyebrow{{margin-bottom:22px;}}
.s3 .headline{{font-size:66px;margin-bottom:16px;}}
.s3 .subline{{font-size:30px;margin-bottom:46px;}}
.grid3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;}}
.grid3 .card{{padding:32px 30px 34px;display:flex;flex-direction:column;}}
.grid3 .cnum{{font-family:'Cormorant',serif;font-weight:600;font-size:30px;color:{GOLD};margin-bottom:6px;}}
.grid3 .cico{{margin-bottom:16px;}}
.grid3 .ck{{font-size:27px;margin-bottom:12px;letter-spacing:.02em;}}
.footer.plain{{max-width:none;}}
'''
    cards = [
        ("capture","01","Capture","Catch the work in two minutes, before the details fade."),
        ("clarify","02","Clarify","Separate your part from the team's result, and name the judgment and the scope."),
        ("carry","03","Carry","Put it in language an outsider can follow, then into a resume, an interview, or a promotion note."),
    ]
    cardhtml = "".join(
        f'<div class="card"><div class="cnum">{n}</div><img class="cico" src="{icon_uri(ic)}"><div class="ck">{k}</div><div class="cb">{b}</div></div>'
        for ic,n,k,b in cards)
    inner = f'''
<div class="stage s3">
  <div class="eyebrow">HOW IT WORKS</div>
  <div class="headline">Capture. Clarify. Carry.</div>
  <div class="subline">Three steps you return to whenever the work is fresh.</div>
  <div class="grid3">{cardhtml}</div>
  <div class="footer plain">Sixty minutes is a guide. Take it in one sitting or several.</div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

# ---------- Slide 04: before and after ----------
def slide04():
    css = f'''
.s4 .eyebrow{{margin-bottom:20px;}}
.s4 .headline{{font-size:60px;margin-bottom:14px;}}
.s4 .subline{{font-size:27px;max-width:38em;margin-bottom:40px;}}
.ba{{display:flex;flex-direction:column;gap:22px;}}
.ba-row{{background:{CREAM};color:{INK};border-radius:14px;padding:26px 34px;border-left:6px solid #b9bec8;}}
.ba-row.after{{border-left:6px solid {GOLD};}}
.ba-tag{{font-family:'DM Sans';font-weight:600;letter-spacing:.12em;font-size:17px;color:#8a8f9a;margin-bottom:10px;}}
.ba-row.after .ba-tag{{color:{GOLD};}}
.ba-txt{{font-family:'Cormorant',serif;font-weight:500;font-size:33px;line-height:1.22;color:{NAVY};}}
.ba-cap{{font-family:'DM Sans';font-weight:400;font-size:18px;color:#5f636e;margin-top:10px;line-height:1.4;}}
.footer.plain{{max-width:none;font-size:24px;}}
'''
    inner = f'''
<div class="stage s4">
  <div class="eyebrow">FROM MEMORY TO EVIDENCE</div>
  <div class="headline">A vague line becomes portable evidence.</div>
  <div class="subline">The system pushes every entry past what you did to what became different because you did it.</div>
  <div class="ba">
    <div class="ba-row"><div class="ba-tag">BEFORE</div>
      <div class="ba-txt">&ldquo;Helped with onboarding.&rdquo;</div>
      <div class="ba-cap">Vague. Easy to forget. It claims nothing a reader can examine.</div></div>
    <div class="ba-row after"><div class="ba-tag">A PROOF LINE</div>
      <div class="ba-txt">&ldquo;Redesigned new-hire onboarding for a growing operations team, cutting time to full productivity and reducing early attrition, with the model later adopted by two other departments.&rdquo;</div>
      <div class="ba-cap">Maya&rsquo;s Proof Line, from the Guided Handbook.</div></div>
  </div>
  <div class="footer plain">A Proof Line does not need a number to be strong, and it must never contain an invented one.</div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

# ---------- Slide 05: who it is for ----------
def slide05():
    css = f'''
.s5 .eyebrow{{margin-bottom:20px;}}
.s5 .headline{{font-size:60px;margin-bottom:16px;}}
.s5 .subline{{font-size:26px;max-width:40em;margin-bottom:40px;}}
.grid2b{{display:grid;grid-template-columns:1fr 1fr;gap:24px;}}
.grid2b .card{{padding:26px 32px 28px;display:flex;gap:22px;align-items:flex-start;}}
.grid2b .cico{{flex-shrink:0;margin-top:2px;}}
.grid2b .ck{{font-size:23px;margin-bottom:8px;}}
'''
    cards = [
        ("quarterly","Before a performance review","Walk in able to account for the whole year, accurately."),
        ("promotion","Before a promotion case","Bring specific evidence of what changed because of your work."),
        ("interview","Before an interview or a new resume","Have portable, specific language ready to reuse."),
        ("reconstruct","Before a reorg or a career move","Know what your work built and what can travel with you."),
    ]
    cardhtml = "".join(
        f'<div class="card"><img class="cico" src="{icon_uri(ic)}"><div><div class="ck">{k}</div><div class="cb">{b}</div></div></div>'
        for ic,k,b in cards)
    inner = f'''
<div class="stage s5">
  <div class="eyebrow">WHO IT IS FOR</div>
  <div class="headline">For people who do the work and lose the proof.</div>
  <div class="subline">The work was constant. You solved the problem, absorbed the lesson, and moved to the next thing before the last one had a name.</div>
  <div class="grid2b">{cardhtml}</div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

# ---------- Slide 06: two tools ----------
def slide06():
    css = f'''
.s6 .eyebrow{{margin-bottom:18px;}}
.s6 .headline{{font-size:58px;margin-bottom:40px;}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:28px;flex:1;}}
.tcard{{background:{CREAM};color:{INK};border-radius:16px;padding:34px 38px 36px;display:flex;flex-direction:column;border-top:6px solid {GOLD};}}
.tcard.fk{{border-top:6px solid #6b7180;background:#f1f0ec;}}
.tname{{font-family:'Cormorant',serif;font-weight:600;font-size:38px;color:{NAVY};line-height:1.02;margin-bottom:8px;}}
.tsub{{font-family:'DM Sans';font-weight:600;letter-spacing:.09em;font-size:15px;color:{GOLD};margin-bottom:20px;}}
.tcard.fk .tsub{{color:#6b7180;}}
.tq{{font-family:'Cormorant',serif;font-style:italic;font-size:27px;color:{INK};line-height:1.28;margin-bottom:22px;}}
.tlist{{list-style:none;margin:0;padding:0;}}
.tlist li{{font-family:'DM Sans';font-weight:400;font-size:20px;line-height:1.4;color:{INK};padding-left:26px;position:relative;margin-bottom:12px;}}
.tlist li:before{{content:"";position:absolute;left:0;top:11px;width:9px;height:9px;background:{GOLD};border-radius:2px;}}
.fkbody{{font-family:'DM Sans';font-weight:400;font-size:20px;line-height:1.5;color:{INK};}}
.footer.plain{{font-size:24px;max-width:none;}}
'''
    ktp = f'''<div class="tcard">
      <div class="tname">Keep the Proof</div>
      <div class="tsub">A GUIDED SYSTEM FOR BUILDING YOUR PROFESSIONAL RECORD</div>
      <div class="tq">&ldquo;What have I done, and how do I keep the proof of it?&rdquo;</div>
      <ul class="tlist">
        <li>Guided Handbook with worked examples</li>
        <li>Your Professional Record, editable for years</li>
        <li>Printable and fillable tools</li>
      </ul>
    </div>'''
    fk = f'''<div class="tcard fk">
      <div class="tname">The Capability<br>Formation Field Kit</div>
      <div class="tsub">READ WHAT YOUR WORK IS BUILDING</div>
      <div class="tq">&ldquo;What is my current work building in me, and will it travel?&rdquo;</div>
      <div class="fkbody">The Field Kit helps you assess what your current work is building in you and read your broader capability position. It is a different tool for a different question.</div>
    </div>'''
    inner = f'''
<div class="stage s6">
  <div class="eyebrow">TWO TOOLS, TWO QUESTIONS</div>
  <div class="headline">Different questions. Different tools.</div>
  <div class="two">{ktp}{fk}</div>
  <div class="footer plain">Keep the honest record first. Read what it means for your direction when you are ready.</div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
{FONTFACE}{BASE_CSS}{css}</style></head><body>{inner}</body></html>'''

SLIDES = [
    ("01_hero", slide01),
    ("02_what_you_receive", slide02),
    ("03_how_it_works", slide03),
    ("04_before_and_after", slide04),
    ("05_who_it_is_for", slide05),
    ("06_two_tools", slide06),
]

def render(name, htmlfn):
    hp = f"{RENDER}/{name}.html"
    open(hp,"w",encoding="utf-8").write(htmlfn())
    big = f"{OUT}/{name}_1600x900_v2.png"
    r = subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1600,900",
        f"--screenshot={big}", f"file://{hp}"], capture_output=True, text=True)
    if not os.path.exists(big):
        print("FAIL", name, r.stderr[-800:]); return None
    im = Image.open(big).convert("RGB")
    if im.size != (1600,900):
        im = im.crop((0,0,1600,900))
    im.save(big)
    small = f"{OUT}/{name}_640x360_v2.png"
    im.resize((640,360), Image.LANCZOS).save(small)
    print("OK", name, im.size, "->", os.path.getsize(big), "bytes")
    return big

bigs = []
for name, fn in SLIDES:
    b = render(name, fn)
    if b: bigs.append((name,b))

# ---------- thumbnail 600x600 from slide 01 ----------
if bigs:
    hero = Image.open(f"{OUT}/01_hero_1600x900_v2.png").convert("RGB")
    # center-crop the left portion where the title lives, to keep title readable at 600px
    # crop a square from the left 900px region, then resize to 600
    crop = hero.crop((0,0,900,900))
    crop.resize((600,600), Image.LANCZOS).save(f"{OUT}/gumroad_thumbnail_600x600.png")
    print("thumbnail 600x600 written")

# ---------- contact sheet: 2 cols x 3 rows of the 1600x900 slides ----------
if bigs:
    tw, th = 800, 450  # each cell
    pad = 24
    cols, rows = 2, 3
    W = cols*tw + pad*(cols+1)
    H = rows*th + pad*(rows+1)
    sheet = Image.new("RGB",(W,H),(17,35,69))
    for i,(name,b) in enumerate(bigs):
        im = Image.open(b).convert("RGB").resize((tw,th), Image.LANCZOS)
        c = i % cols; r = i // cols
        x = pad + c*(tw+pad); y = pad + r*(th+pad)
        sheet.paste(im,(x,y))
    sheet.save(f"{OUT}/contact_sheet_v2.png")
    print("contact sheet written", sheet.size)

print("DONE. files in", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f, os.path.getsize(f"{OUT}/{f}"))
