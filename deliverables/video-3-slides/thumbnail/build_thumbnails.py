"""Video 3 thumbnail masters, built from the approved caramel-outfit portrait.

Source photograph:
  a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png, 1254 x 1254, RGB PNG

Only crop, Lanczos resize and placement are applied to the photograph. Nothing in
it is reconstructed, retouched, beautified or synthetically extended.
"""
import os, shutil
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
        "a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png")

W, H = 3840, 2160
CREAM=(245,240,232); NAVY=(15,35,70); GOLD=(201,168,76); DEEP=(11,26,52)
DIM=(120,132,150)
FD = os.path.expanduser("~/.fonts/")

def f(sz, w="Bold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)

def measure(d, t, fo):
    b = d.textbbox((0,0), t, font=fo); return b[2]-b[0], b[3]-b[1]

def fit(d, text, target_w, weight="ExtraBold", start=460):
    s = start
    while s > 40:
        fo = f(s, weight)
        if measure(d, text, fo)[0] <= target_w:
            return fo, s
        s -= 2
    return f(40, weight), 40

# --------------------------------------------------------------- photograph
PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1254, 1254), PHOTO.size

def crop_to(aspect, centre_x, y0=120, y1=1254):
    """Crop the real photograph to `aspect` (w/h), centred on centre_x."""
    ch = y1 - y0
    cw = int(round(ch * aspect))
    x0 = int(round(centre_x - cw/2))
    x0 = max(0, min(x0, PHOTO.width - cw))
    return PHOTO.crop((x0, y0, x0+cw, y1)), cw, ch

def place(canvas, box, centre_x):
    x0,y0,x1,y1 = box
    tw, th = x1-x0, y1-y0
    crop, cw, ch = crop_to(tw/th, centre_x)
    canvas.paste(crop.resize((tw,th), Image.LANCZOS), (x0,y0))
    return cw, ch, tw/cw

REPORT = []

# ------------------------------------------------------------------ FINAL A
# Portrait right, headline left on cream. Gold rule on the seam.
a = Image.new("RGB", (W,H), CREAM); d = ImageDraw.Draw(a)
PA = (2040, 0, W, H)
cw,ch,sc = place(a, PA, 712)
REPORT.append(("Final A", PA, cw, ch, sc))
d.rectangle([2040, 0, 2058, H], fill=GOLD)

col = 2040 - 200 - 150
y = 470
for line, colr in (("WAIT", NAVY), ("BEFORE", NAVY), ("YOU QUIT", NAVY)):
    fo, s = fit(d, line, col, "ExtraBold", 460)
    d.text((200, y), line, font=fo, fill=colr)
    y += int(s*1.02)
# gold underscore, weight-matched to the type
d.rectangle([206, y+70, 206+760, y+70+34], fill=GOLD)
a.save(os.path.join(HERE, "VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png"))

# ------------------------------------------------------------------ FINAL B
# Portrait left, navy panel right, WAIT carried in gold.
b = Image.new("RGB", (W,H), NAVY); d = ImageDraw.Draw(b)
PB = (0, 0, 1760, H)
cw,ch,sc = place(b, PB, 615)
REPORT.append(("Final B", PB, cw, ch, sc))
d.rectangle([1760, 0, 1778, H], fill=GOLD)

bx = 1930; colb = W - bx - 170
y = 520
for line, colr in (("WAIT", GOLD), ("BEFORE", CREAM), ("YOU QUIT", CREAM)):
    fo, s = fit(d, line, colb, "ExtraBold", 460)
    d.text((bx, y), line, font=fo, fill=colr)
    y += int(s*1.02)
b.save(os.path.join(HERE, "VIDEO_3_THUMBNAIL_FINAL_B_3840x2160.png"))

for name, box, cw, ch, sc in REPORT:
    print("%s: region %s  source crop %dx%d  upscale %.3fx" % (name, box, cw, ch, sc))
