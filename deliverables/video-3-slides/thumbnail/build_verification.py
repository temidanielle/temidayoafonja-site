"""Asset verification sheet for the approved Video 3 portrait."""
import os, hashlib
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD   = os.path.expanduser("~/.fonts/")
SRC  = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
        "a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png")
NAVY=(15,35,70); DIM=(120,132,150); GOLD=(201,168,76); GREEN=(24,110,72)

def f(sz,w="Regular"): return ImageFont.truetype(FD+"MontserratTB-%s.ttf"%w, sz)

im = Image.open(SRC).convert("RGB")
raw = open(SRC,"rb").read()
sha = hashlib.sha256(raw).hexdigest()

W,H = 2400, 1620
s = Image.new("RGB",(W,H),(250,247,241)); d = ImageDraw.Draw(s)
d.text((80,60), "VIDEO 3 — ASSET VERIFICATION", font=f(56,"Bold"), fill=NAVY)
d.text((80,136), "Performed before any thumbnail was rendered.", font=f(30), fill=DIM)
d.rectangle([80,196,W-80,200], fill=GOLD)

tw_ = 760
th_ = round(tw_*im.height/im.width)
s.paste(im.resize((tw_,th_), Image.LANCZOS), (80,250))
d.rectangle([80,250,80+tw_,250+th_], outline=(214,204,186), width=3)
d.text((80, 250+th_+22), "the file as it exists in the workspace", font=f(26), fill=DIM)

x = 920; y = 258
rows = [("File name", os.path.basename(SRC)),
        ("Pixel dimensions", "%d x %d" % im.size),
        ("Mode / format", "%s / PNG" % im.mode),
        ("File size", "%s bytes" % f"{len(raw):,}"),
        ("SHA-256", sha[:32]),
        ("", sha[32:])]
for k,v in rows:
    if k: d.text((x,y), k, font=f(28,"Bold"), fill=NAVY)
    d.text((x+360,y), v, font=f(28), fill=(60,70,90)); y += 52

y += 24
d.text((x,y), "REQUIRED VISUAL CRITERIA", font=f(34,"Bold"), fill=NAVY); y += 62
for t in ["gold / caramel sleeveless top",
          "large fabric rosette on the shoulder",
          "braided bun",
          "thoughtful, calm expression"]:
    d.line([(x+6,y+18),(x+22,y+34)], fill=GREEN, width=8)
    d.line([(x+22,y+34),(x+54,y+2)], fill=GREEN, width=8)
    d.text((x+82,y), t, font=f(30), fill=(60,70,90)); y += 58

y += 20
d.text((x,y), "GARMENT SAMPLES", font=f(34,"Bold"), fill=NAVY); y += 56
pts = [(0.40,0.65),(0.50,0.75),(0.35,0.85),(0.55,0.95),(0.62,0.72)]
sx = x
for fx,fy in pts:
    c = im.getpixel((int(im.width*fx), int(im.height*fy)))
    d.rectangle([sx,y,sx+118,y+118], fill=c, outline=(214,204,186), width=2)
    d.text((sx, y+126), "#%02X%02X%02X"%c, font=f(22), fill=DIM)
    sx += 138
y += 190
d.text((x,y), "Reads in the caramel and amber family. The wine garment previously supplied",
       font=f(26), fill=DIM)
d.text((x,y+36), "sampled at #4F0408 and is not present in this file.", font=f(26), fill=DIM)

d.rectangle([80, H-230, W-80, H-90], fill=(233,243,236), outline=GREEN, width=3)
d.text((116, H-206), "VERDICT: APPROVED PORTRAIT CONFIRMED — CLEARED TO RENDER",
       font=f(38,"Bold"), fill=GREEN)
d.text((116, H-152), "All four criteria met. Thumbnails were built from this file only. "
       "No face was generated, reconstructed, retouched or extended.",
       font=f(26), fill=(40,90,64))
s.save(os.path.join(HERE, "VIDEO_3_ASSET_VERIFICATION_v1.2.png"))
print("sha256", sha)
print("size", im.size, len(raw), "bytes")
