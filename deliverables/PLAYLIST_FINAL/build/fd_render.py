# -*- coding: utf-8 -*-
"""Render the slides at 1920 x 1080 through headless Chromium.

No thumbnail is produced. Temidayo builds those in Canva from the stills the
Riverside sheet asks for, so this module draws slides only.

Montserrat 700 is the heaviest real Montserrat in the repository. ExtraBold 800
is not present, so 700 is used rather than faking a heavier weight by stroking
the glyphs.
"""
import os, sys, base64, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SITE = "/home/user/temidayoafonja-site"
sys.path.insert(0, HERE)
import fd_data as D, fd_slides as SL

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FONT = os.path.join(SITE, "fonts")
W, H = 1920, 1080

def _b64(path, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())

def _faces():
    out = []
    for wgt, f in ((400, "Montserrat-400-normal-latin-49e242.woff2"),
                   (600, "Montserrat-600-normal-latin-49e242.woff2"),
                   (700, "Montserrat-700-normal-latin-49e242.woff2")):
        out.append("@font-face{font-family:Mont;font-weight:%d;font-style:normal;"
                   "src:url(%s) format('woff2');}"
                   % (wgt, _b64(os.path.join(FONT, f), "font/woff2")))
    return "\n".join(out)

def e(s):
    return html.escape(s, quote=False)

# ------------------------------------------------------------ slide CSS
CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#222;font-family:Mont,sans-serif;-webkit-font-smoothing:antialiased;}
.card{width:1920px;height:1080px;position:relative;overflow:hidden;
      background:%(navy)s;color:%(sand)s;display:flex;flex-direction:column;
      justify-content:center;padding:88px 112px;}
.card.light{background:%(sand)s;color:%(navy)s;}
.label{font-size:44px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
       color:%(gold)s;margin-bottom:30px;}
/* 60 pt floor = 120 px. Nothing below .sm. */
h1{font-size:132px;font-weight:700;line-height:1.05;letter-spacing:-.02em;
   text-wrap:balance;}
h1.big{font-size:148px;}
h1.sm{font-size:120px;}
.sub{font-size:58px;font-weight:400;line-height:1.16;margin-top:24px;opacity:.92;}
.rule{width:180px;height:9px;background:%(gold)s;margin:38px 0 0;}
.lines{margin-top:40px;}
.lines p{font-size:52px;font-weight:400;line-height:1.32;margin-bottom:16px;}
ol,ul{margin-top:40px;list-style:none;}
li{font-size:54px;font-weight:400;line-height:1.24;margin-bottom:20px;
   display:flex;align-items:baseline;}
li .n{color:%(gold)s;font-weight:700;min-width:88px;flex:0 0 88px;}
li .d{color:%(gold)s;font-weight:700;min-width:44px;flex:0 0 44px;}
li.tight{margin-bottom:12px;font-size:48px;}
.foot{margin-top:34px;font-size:46px;font-weight:600;color:%(gold)s;}
.quote{margin-top:38px;font-size:54px;font-weight:400;line-height:1.3;
       border-left:9px solid %(gold)s;padding-left:40px;}
.srow{display:flex;align-items:baseline;margin-bottom:28px;}
.srow .k{flex:0 0 400px;padding-right:28px;font-size:44px;font-weight:700;
         color:%(gold)s;letter-spacing:.06em;text-transform:uppercase;}
.srow .v{font-size:46px;font-weight:400;line-height:1.26;}
.link{margin-top:36px;font-size:44px;font-weight:600;color:%(gold)s;
      word-break:break-word;}
.nxt{margin-top:18px;font-size:44px;font-weight:400;opacity:.9;}
""" % dict(navy=D.NAVY, sand=D.SAND, gold=D.GOLD)

# Headline point sizes, for the QA report. px / 2 = pt at this canvas size.
HEAD_PT = {"big": 74, "": 66, "sm": 60}

def slide_html(s):
    k = s["kind"]
    lab = ('<div class="label">%s</div>' % e(s["label"])
           if SL.shows_label(s["label"]) else "")
    if k == "title":
        return ('<div class="card">%s<h1 class="big">%s</h1>'
                '<div class="sub">%s</div><div class="rule"></div></div>'
                % ("", e(s["head"]), e(s["sub"])))
    if k == "roadmap":
        li = "".join('<li><span class="n">%d</span><span>%s</span></li>'
                     % (i, e(t)) for i, t in enumerate(s["items"], 1))
        foot = '<div class="foot">%s</div>' % e(s["foot"]) if s.get("foot") else ""
        return ('<div class="card">%s<h1 class="sm">%s</h1><ol>%s</ol>%s</div>'
                % (lab, e(s["head"]), li, foot))
    if k == "list":
        sub = '<div class="sub">%s</div>' % e(s["sub"]) if s.get("sub") else ""
        cls = " tight" if len(s["items"]) > 5 else ""
        li = "".join('<li class="%s"><span class="d">·</span><span>%s</span></li>'
                     % (cls.strip(), e(t)) for t in s["items"])
        return ('<div class="card">%s<h1 class="sm">%s</h1>%s<ul>%s</ul></div>'
                % (lab, e(s["head"]), sub, li))
    if k == "step":
        ln = "".join("<p>%s</p>" % e(t) for t in s.get("lines") or [])
        body = '<div class="lines">%s</div>' % ln if ln else '<div class="rule"></div>'
        return ('<div class="card">%s<h1>%s</h1>%s</div>'
                % (lab, e(s["head"]), body))
    if k == "quote":
        return ('<div class="card">%s<h1 class="sm">%s</h1>'
                '<div class="quote">“%s”</div></div>'
                % (lab, e(s["head"]), e(s["quote"])))
    if k == "rapid":
        li = "".join('<li class="tight"><span class="d">·</span><span>%s</span></li>'
                     % e(t) for t in s["items"])
        return ('<div class="card">%s<h1 class="sm">%s</h1><ul>%s</ul></div>'
                % (lab, e(s["head"]), li))
    if k == "script":
        rows = "".join('<div class="srow"><div class="k">%s</div>'
                       '<div class="v">%s</div></div>' % (e(a), e(b))
                       for a, b in s["rows"])
        return ('<div class="card">%s<h1 class="sm">%s</h1>'
                '<div style="margin-top:56px">%s</div></div>'
                % (lab, e(s["head"]), rows))
    if k == "end":
        return ('<div class="card light">%s<h1 class="sm">%s</h1>'
                '<div class="rule"></div><div class="link">%s</div>'
                '<div class="nxt">%s</div></div>'
                % (lab, e(s["head"]), e(s["link"]), e(s["nxt"])))
    raise ValueError(k)

def deck_html(n):
    cards = "".join('<div id="s%d">%s</div>' % (i, slide_html(s))
                    for i, s in enumerate(SL.SLIDES[n], 1))
    return ("<!doctype html><meta charset='utf-8'><style>%s\n%s</style>%s"
            % (_faces(), CSS, cards))

# --------------------------------------------------------------- shoot
def shoot(html_text, path, sel, w, h):
    from playwright.sync_api import sync_playwright
    tmp = path + ".html"
    open(tmp, "w", encoding="utf-8").write(html_text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(tmp), wait_until="load")
        pg.wait_for_timeout(700)
        if isinstance(sel, list):
            for s, p in sel:
                pg.query_selector(s).screenshot(path=p)
        else:
            pg.query_selector(sel).screenshot(path=path)
        b.close()
    os.remove(tmp)

def render_deck(n, png_dir):
    os.makedirs(png_dir, exist_ok=True)
    names = [s["name"] for s in SL.SLIDES[n]]
    pairs = [("#s%d" % i, os.path.join(png_dir, nm + ".png"))
             for i, nm in enumerate(names, 1)]
    shoot(deck_html(n), os.path.join(png_dir, "_deck"), pairs, W, H)
    return [p for _s, p in pairs]

