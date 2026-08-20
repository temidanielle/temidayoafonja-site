"""Video 2 thumbnail master.

Source photograph:
  a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png, 1254 x 1254
  the same verified studio portrait used for Video 3.

Only crop, Lanczos resize and placement are applied to the photograph. The
paused-progression cue is drawn vector-style and is an abstract editorial
graphic. It carries no numbers and represents no measured statistic.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
        "a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png")

W, H = 3840, 2160
CREAM=(245,240,232); NAVY=(15,35,70); GOLD=(201,168,76)
RISE=(44,88,140); FLAT=(33,60,97)
FD = os.path.expanduser("~/.fonts/")

def f(sz,w="Bold"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w, sz)
def measure(d,t,fo):
    b=d.textbbox((0,0),t,font=fo); return b[2]-b[0], b[3]-b[1]
def fit(d,text,tw,weight="ExtraBold",start=470):
    s=start
    while s>40:
        fo=f(s,weight)
        if measure(d,text,fo)[0]<=tw: return fo,s
        s-=2
    return f(40,weight),40

PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size==(1254,1254), PHOTO.size

def place(canvas, box, centre_x=615, y0=120, y1=1254):
    x0,y0b,x1,y1b = box
    tw,th = x1-x0, y1b-y0b
    ch=y1-y0; cw=int(round(ch*tw/th))
    cx0=max(0, min(int(round(centre_x-cw/2)), PHOTO.width-cw))
    canvas.paste(PHOTO.crop((cx0,y0,cx0+cw,y1)).resize((tw,th), Image.LANCZOS),(x0,y0b))
    return cw,ch,tw/cw

# ------------------------------------------------------------------- build
b = Image.new("RGB",(W,H),NAVY); d = ImageDraw.Draw(b)
PB=(0,0,1700,H)
cw,ch,sc = place(b,PB)
d.rectangle([1700,0,1718,H], fill=GOLD)

bx = 1870; col = W-bx-170
y = 190
for line,acc in (("YOUR",False),("SKILLS",False),("ARE",False),("STALLING",True)):
    fo,s = fit(d,line,col,"ExtraBold",345)
    d.text((bx,y), line, font=fo, fill=GOLD if acc else CREAM)
    y += int(s*1.02)

# paused progression: it climbs, then it stops climbing
bw, gap, base = 180, 116, 2072
hs = [76,124,172,220,220,220]
tops=[]
for i,hgt in enumerate(hs):
    x0 = bx + i*(bw+gap)
    d.rectangle([x0, base-hgt, x0+bw, base], fill=RISE if i<4 else FLAT)
    tops.append((x0+bw//2, base-hgt-32))
d.line(tops, fill=GOLD, width=9)

# the pause, sitting exactly where the climb stops
px = (tops[3][0]+tops[4][0])//2
py = tops[4][1]-104
d.rectangle([px-36, py-52, px-11, py+52], fill=GOLD)
d.rectangle([px+11, py-52, px+36, py+52], fill=GOLD)

b.save(os.path.join(HERE,"VIDEO_2_THUMBNAIL_FINAL_3840x2160.png"))
print("Video 2: region %s  source crop %dx%d  upscale %.3fx" % (PB,cw,ch,sc))
