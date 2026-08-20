"""Video 1 thumbnail masters. Two composition options, one real photograph.

Source photograph:
  deliverables/video-1-slides/assets/photo-headshot-cream.png, 800 x 800

Only crop, Lanczos resize and placement are applied to the photograph. The
progression graphic is drawn vector-style over the layout and is not a
photograph of anything.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "..", "assets", "photo-headshot-cream.png")

W, H = 3840, 2160
CREAM=(245,240,232); NAVY=(15,35,70); GOLD=(201,168,76); DEEP=(11,26,52)
MUTE=(60,84,118)
FD = os.path.expanduser("~/.fonts/")

def f(sz, w="Bold"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w, sz)
def measure(d,t,fo):
    b=d.textbbox((0,0),t,font=fo); return b[2]-b[0], b[3]-b[1]
def fit(d,text,target_w,weight="ExtraBold",start=470):
    s=start
    while s>40:
        fo=f(s,weight)
        if measure(d,text,fo)[0]<=target_w: return fo,s
        s-=2
    return f(40,weight),40

PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size==(800,800), PHOTO.size
# subject: head top y=132, face centre x~450, shoulders to y=800

def place(canvas, box, centre_x=450, y0=60, y1=800):
    x0,y0b,x1,y1b = box
    tw,th = x1-x0, y1b-y0b
    ch = y1-y0
    cw = int(round(ch*tw/th))
    cx0 = max(0, min(int(round(centre_x-cw/2)), PHOTO.width-cw))
    crop = PHOTO.crop((cx0,y0,cx0+cw,y1))
    canvas.paste(crop.resize((tw,th), Image.LANCZOS), (x0,y0b))
    return cw, ch, tw/cw

def headline(d, x, y, lines, col_w, base_col, accent_col, start=470):
    """lines: list of [(text, is_accent), ...] runs per line."""
    for runs in lines:
        flat = "".join(t for t,_ in runs)
        fo,s = fit(d, flat, col_w, "ExtraBold", start)
        cx = x
        for t,acc in runs:
            d.text((cx,y), t, font=fo, fill=accent_col if acc else base_col)
            cx += measure(d,t,fo)[0] if t.strip() else measure(d,"n",fo)[0]//2
            if t.endswith(" "):
                pass
        y += int(s*1.02)
    return y

def run_width(d, t, fo):
    return d.textlength(t, font=fo)

def headline2(d, x, y, lines, col_w, base_col, accent_col, start=470):
    for runs in lines:
        flat="".join(t for t,_ in runs)
        fo,s = fit(d, flat, col_w, "ExtraBold", start)
        cx=x
        for t,acc in runs:
            d.text((cx,y), t, font=fo, fill=accent_col if acc else base_col)
            cx += run_width(d,t,fo)
        y += int(s*1.02)
    return y

REPORT=[]

# ============================================================ OPTION A — RAIL
a = Image.new("RGB",(W,H),NAVY); d = ImageDraw.Draw(a)
PA=(2160,0,W,H)
cw,ch,sc = place(a,PA); REPORT.append(("Option A",PA,cw,ch,sc))
d.rectangle([2160,0,2178,H], fill=GOLD)

col = 2160-200-160
headline2(d, 200, 230,
    [[("DON'T",False)],[("START",False)],[("FROM ",False),("ZERO",True)]],
    col, CREAM, GOLD, 430)

# four nodes accumulating along a thin rising line, then continuing
bx, by = 268, 1930
step, rise = 430, 70
pts = [(bx+i*step, by-i*rise) for i in range(4)]
for i in range(3):
    d.line([pts[i], pts[i+1]], fill=GOLD, width=10)
ex,ey = pts[-1][0]+330, pts[-1][1]-96
d.line([pts[-1], (ex,ey)], fill=GOLD, width=10)
d.polygon([(ex+70,ey-26),(ex-14,ey-46),(ex-2,ey+28)], fill=GOLD)
for i,(px,py) in enumerate(pts):
    r = 32 + i*10
    if i==3:
        d.ellipse([px-r-12,py-r-12,px+r+12,py+r+12], fill=GOLD)
    else:
        d.ellipse([px-r,py-r,px+r,py+r], fill=CREAM)
a.save(os.path.join(HERE,"VIDEO_1_THUMBNAIL_OPTION_A_3840x2160.png"))

# ========================================================== OPTION B — LEDGER
b = Image.new("RGB",(W,H),CREAM); d = ImageDraw.Draw(b)
BAND = 1660
PB=(2200,0,W,BAND)
cw,ch,sc = place(b,PB,y0=60,y1=744); REPORT.append(("Option B",PB,cw,ch,sc))
d.rectangle([0,BAND,W,H], fill=NAVY)
d.rectangle([0,BAND,W,BAND+16], fill=GOLD)

col = 2200-210-170
headline2(d, 210, 290,
    [[("DON'T",False)],[("START",False)],[("FROM ",False),("ZERO",True)]],
    col, NAVY, (168,134,40), 415)

# progression accumulating inside the band, then continuing forward
bw, gap, bx0, base = 300, 110, 250, 2100
tops=[]
for i in range(4):
    hgt = 100 + i*56
    x0 = bx0 + i*(bw+gap)
    d.rectangle([x0, base-hgt, x0+bw, base], fill=MUTE if i<3 else GOLD)
    tops.append((x0+bw//2, base-hgt-34))
d.line(tops, fill=GOLD, width=9)
ex, ey = tops[-1][0]+300, tops[-1][1]-58
d.line([tops[-1], (ex,ey)], fill=GOLD, width=9)
d.polygon([(ex+76,ey-18),(ex-10,ey-44),(ex-2,ey+26)], fill=GOLD)
b.save(os.path.join(HERE,"VIDEO_1_THUMBNAIL_OPTION_B_3840x2160.png"))

for n,box,cw,ch,sc in REPORT:
    print("%s: region %s  source crop %dx%d  upscale %.3fx"%(n,box,cw,ch,sc))
