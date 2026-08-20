"""Video 3 thumbnail: composition studies.

The portrait region is left empty and clearly labelled. No photograph is placed,
substituted or generated. Everything else is final: words, type, scale, colour,
the three-check device, and how the whole thing behaves at 200 pixels wide.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 3840, 2160
CREAM=(245,240,232); NAVY=(15,35,70); GOLD=(168,134,40); DIM=(120,132,150)
PLACE=(228,220,206)
FD = os.path.expanduser("~/.fonts/")

def f(sz, w="Bold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)

def measure(d, t, fo):
    b = d.textbbox((0,0), t, font=fo); return b[2]-b[0], b[3]-b[1]

def fit(d, text, target_w, weight="ExtraBold", start=400):
    """Largest size at which the line fits the column."""
    s = start
    while s > 40:
        fo = f(s, weight)
        if measure(d, text, fo)[0] <= target_w:
            return fo, s
        s -= 4
    return f(40, weight), 40

def portrait_region(d, box, note):
    x0,y0,x1,y1 = box
    d.rectangle(box, fill=PLACE)
    for i in range(0, (x1-x0)+(y1-y0), 90):
        d.line([(x0+i, y0), (x0, y0+i)], fill=(238,232,220), width=10)
    d.rectangle(box, outline=(196,184,164), width=6)
    cx = (x0+x1)//2; yy = (y0+y1)//2 - 120
    for t, s, wt in (("PORTRAIT PLACES HERE",64,"Bold"),
                     ("gold-outfit photograph",50,"Regular"), (note,40,"Regular")):
        fo = f(s, wt); w,_ = measure(d, t, fo)
        d.text((cx-w//2, yy), t, font=fo, fill=(150,138,120)); yy += int(s*1.9)

def checks(d, x, y, n=3, wide=560, gap=130, tick=GOLD, bar=NAVY, tw=17):
    for i in range(n):
        yy = y + i*gap
        d.line([(x+10, yy+38), (x+36, yy+64)], fill=tick, width=tw)
        d.line([(x+36, yy+64), (x+88, yy+6)], fill=tick, width=tw)
        d.rectangle([x+140, yy+24, x+140+wide, yy+50], fill=bar)

# ------------------------------------------------------------------ FINAL A
a = Image.new("RGB", (W,H), CREAM); d = ImageDraw.Draw(a)
portrait_region(d, (2040, 0, W, H), "about 47 percent of the canvas")
d.rectangle([2040, 0, 2054, H], fill=GOLD)
col = 2040 - 200 - 120
y = 400
for line in ["WAIT","BEFORE","YOU QUIT"]:
    fo, s = fit(d, line, col, "ExtraBold", 420)
    d.text((200, y), line, font=fo, fill=NAVY)
    y += int(s*1.06)
checks(d, 208, y + 90)
a.save("layout-A-composition-study.png")

# ------------------------------------------------------------------ FINAL B
b = Image.new("RGB", (W,H), CREAM); d = ImageDraw.Draw(b)
portrait_region(d, (0, 0, 1760, H), "about 46 percent of the canvas")
d.rectangle([1760, 0, 1774, H], fill=GOLD)
d.rectangle([1774, 0, W, H], fill=NAVY)
bx = 1900; colb = W - bx - 160
n3 = f(520, "ExtraBold"); d.text((bx, 210), "3", font=n3, fill=GOLD)
w3,_ = measure(d, "3", n3)
checks(d, bx + w3 + 110, 330, wide=330, gap=120, tick=GOLD, bar=(60,84,118), tw=15)
y = 980
for line in ["WAIT","BEFORE","YOU QUIT"]:
    fo, s = fit(d, line, colb, "ExtraBold", 380)
    d.text((bx, y), line, font=fo, fill=CREAM)
    y += int(s*1.06)
b.save("layout-B-composition-study.png")

# ------------------------------------------------------------- contact sheet
SW, SH = 3400, 2320
s = Image.new("RGB", (SW,SH), (250,247,241)); d = ImageDraw.Draw(s)
d.text((90,66), "THUMBNAIL COMPOSITION STUDIES", font=f(60,"Bold"), fill=NAVY)
d.text((90,152), "Words, type, scale, colour and the three-check device are final. The portrait "
                 "region is empty and labelled; no photograph was placed.",
       font=f(34,"Regular"), fill=DIM)
d.rectangle([90,232,SW-90,236], fill=GOLD)
tw_, th_ = 1520, 855
for i,(img,label,note) in enumerate([
    (a,"FINAL A, recommended","Portrait right, headline left, three neutral check rows."),
    (b,"FINAL B, alternate","Portrait left, navy panel right, restrained 3 with three ticks.")]):
    x = 90 + i*(tw_+120); y = 310
    s.paste(img.resize((tw_,th_), Image.LANCZOS), (x,y))
    d.rectangle([x,y,x+tw_,y+th_], outline=(214,204,186), width=3)
    d.text((x, y+th_+30), label, font=f(44,"Bold"), fill=NAVY)
    d.text((x, y+th_+92), note, font=f(30,"Regular"), fill=DIM)
d.text((90,1400), "AT 200 PIXELS WIDE", font=f(44,"Bold"), fill=NAVY)
d.text((90,1462), "Native 200 px on the left, then enlarged four times so you can judge what survives.",
       font=f(28,"Regular"), fill=DIM)
for i,img in enumerate([a,b]):
    x = 90 + i*(tw_+120); y = 1545
    small = img.resize((200,113), Image.LANCZOS)
    s.paste(small, (x,y)); d.rectangle([x,y,x+200,y+113], outline=(214,204,186), width=2)
    s.paste(small.resize((800,452), Image.NEAREST), (x+250,y))
    d.rectangle([x+250,y,x+1050,y+452], outline=(214,204,186), width=2)
d.text((90,SH-140), "No photograph of Temidayo appears in these studies. Nothing was generated, "
                    "substituted or altered.", font=f(30,"Regular"), fill=DIM)
s.save("composition-studies-contact-sheet.png")
print("rebuilt with instanced weights")
