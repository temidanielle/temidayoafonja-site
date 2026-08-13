#!/usr/bin/env python3
"""Shared design system + SVG->PNG render pipeline for the Capability Formation
Field Kit Gumroad merchandising assets. Editable masters are authored as SVG
(vector) with real Field Kit page crops embedded as images. Rasterized via the
pre-installed Chromium at device_scale_factor=1 for exact pixel dimensions."""
import base64, os, glob, html
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CROPS = os.path.join(HERE, "crops")

# ---- palette (established Capability Formation editorial system) ----
NAVY = "#0F2347"; SAND = "#F5F0E8"; GOLD = "#C9A84C"; RUST = "#C1440E"
CREAM = "#FBF8F2"; INK = "#0F2347"
NAVY_SOFT = "#4A5A72"      # secondary text on light grounds
CREAM_SOFT = "#C9C7C0"     # secondary text on navy grounds (kept legible)
GOLD_SOFT = "#C9A84C"

CG = "Cormorant Garamond"; DM = "DM Sans"

def esc(s): return html.escape(str(s), quote=True)

# ---- precise text metrics (match the render fonts) -----------------------
from PIL import ImageFont
_FONTDIR = os.path.expanduser("~/.fonts")
_FF = {
    ("Cormorant Garamond", 500): "CG-Medium.ttf",
    ("Cormorant Garamond", 600): "CG-SemiBold.ttf",
    ("Cormorant Garamond", 700): "CG-Bold.ttf",
    ("DM Sans", 400): "DM-Regular.ttf",
    ("DM Sans", 500): "DM-Medium.ttf",
    ("DM Sans", 700): "DM-Bold.ttf",
}
_fcache = {}
def _font(family, weight, size):
    key = (family, weight, int(size))
    if key not in _fcache:
        _fcache[key] = ImageFont.truetype(os.path.join(_FONTDIR, _FF[(family, weight)]), int(size))
    return _fcache[key]

def measure(s, size, family=DM, weight=400, spacing=0):
    f = _font(family, weight, size)
    w = f.getlength(s)
    if spacing: w += spacing*max(0, len(s)-1)
    return w

def fit_size(s, max_w, family=DM, weight=400, start=80, lo=8, spacing=0):
    sz = start
    while sz > lo and measure(s, sz, family, weight, spacing) > max_w:
        sz -= 0.5
    return sz

def wrap_words(words_text, max_w, size, family=DM, weight=400, spacing=0):
    out, cur = [], ""
    for w in words_text.split():
        t = (cur+" "+w).strip()
        if measure(t, size, family, weight, spacing) <= max_w: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out

def img_datauri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

def img_size(path):
    with Image.open(path) as im: return im.size

# ---- primitives ----------------------------------------------------------
def text(x, y, s, size, family=DM, weight=400, fill=NAVY, spacing=None,
         anchor="start", italic=False, opacity=None):
    st = f"font-family:'{family}';font-size:{size}px;font-weight:{weight};"
    if spacing is not None: st += f'letter-spacing:{spacing}px;'
    if italic: st += 'font-style:italic;'
    if opacity is not None: st += f'opacity:{opacity};'
    return (f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" '
            f'fill="{fill}" style="{st}">{esc(s)}</text>')

def tlines(x, y, lines, size, leading, **kw):
    return "\n".join(text(x, y + i*leading, ln, size, **kw) for i, ln in enumerate(lines))

def rect(x, y, w, h, fill="none", stroke="none", sw=0, rx=0, opacity=1):
    return (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

def line(x1, y1, x2, y2, stroke=GOLD, sw=1, dash=None):
    d = f'stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{sw}" {d}/>'

def device(cx, cy, S, stroke=GOLD, fill=RUST):
    """2x2 Capability Formation device, rust square TOP-RIGHT (matches the
    Field Kit product). cx,cy = top-left origin. S = total device width."""
    sq = S*0.405; gap = S - 2*sq; sw = max(1.4, sq*0.11)
    p = [(0,0),(sq+gap,0),(0,sq+gap),(sq+gap,sq+gap)]  # TL,TR,BL,BR
    out = [f'<g transform="translate({cx:.2f},{cy:.2f})">']
    for i,(dx,dy) in enumerate(p):
        if i==1:  # top-right rust filled
            out.append(rect(dx,dy,sq,sq,fill=fill))
        else:
            out.append(rect(dx,dy,sq,sq,fill="none",stroke=stroke,sw=sw))
    out.append('</g>')
    return "".join(out)

def page_card(x, y, w, crop, border=GOLD, bw=1.6, shadow="soft", radius=3, label=None):
    """Place a page crop scaled to width w with hairline border + restrained
    shadow. Returns (svg, height)."""
    iw, ih = img_size(os.path.join(CROPS, crop))
    h = w*ih/iw
    filt = f'filter="url(#{shadow})"' if shadow else ""
    uri = img_datauri(os.path.join(CROPS, crop))
    svg = (f'<g {filt}>'
           f'<clipPath id="clip_{crop.replace(".","_")}_{int(x)}_{int(y)}"><rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{radius}"/></clipPath>'
           f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{radius}" fill="#ffffff"/>'
           f'<image x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" href="{uri}" '
           f'preserveAspectRatio="xMidYMin slice" clip-path="url(#clip_{crop.replace(".","_")}_{int(x)}_{int(y)})"/>'
           f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{radius}" '
           f'fill="none" stroke="{border}" stroke-width="{bw}"/>'
           f'</g>')
    return svg, h

def svg_doc(W, H, body, bg=NAVY, extra_defs=""):
    defs = f'''<defs>
      <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
        <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#0F2347" flood-opacity="0.20"/>
      </filter>
      <filter id="lift" x="-40%" y="-40%" width="180%" height="180%">
        <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#0A1830" flood-opacity="0.34"/>
      </filter>
      {extra_defs}
    </defs>'''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{defs}'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{bg}"/>'
            f'{body}</svg>')

# ---- render -----------------------------------------------------------------
_CHROME = None
def _chrome():
    for p in glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'):
        return p
    return None

def render_svgs(items):
    """items: list of (svg_path, png_path, W, H). Renders each exactly."""
    from playwright.sync_api import sync_playwright
    exe = _chrome()
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=exe,
                               args=['--no-sandbox','--force-color-profile=srgb','--hide-scrollbars'])
        for svg_path, png_path, W, H in items:
            with open(svg_path) as f: svg = f.read()
            wrap = ('<!doctype html><html><head><meta charset="utf-8">'
                    '<style>*{margin:0;padding:0}html,body{background:#fff}</style></head>'
                    f'<body>{svg}</body></html>')
            hp = svg_path + ".html"
            with open(hp, "w") as f: f.write(wrap)
            pg = b.new_page(viewport={'width':W,'height':H}, device_scale_factor=1)
            pg.goto('file://'+os.path.abspath(hp)); pg.wait_for_timeout(350)
            pg.screenshot(path=png_path, clip={'x':0,'y':0,'width':W,'height':H})
            pg.close()
            os.remove(hp)
        b.close()

def to_srgb_png(path):
    """Ensure sRGB, strip alpha to a flat RGB PNG (Gumroad-friendly)."""
    from PIL import Image, PngImagePlugin
    im = Image.open(path).convert("RGB")
    im.save(path, "PNG")
    return im.size
