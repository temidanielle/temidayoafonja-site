"""Side-by-side comparison of the two Video 4 thumbnail variants."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.expanduser("~/.fonts/")
NAVY = (15, 35, 70); DIM = (120, 132, 150); GOLD = (201, 168, 76)
CREAM = (250, 247, 241)

def f(s, w="Bold"): return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, s)

A = Image.open(os.path.join(HERE, "Video_4_Thumbnail_A.png")).convert("RGB")
B = Image.open(os.path.join(HERE, "Video_4_Thumbnail_B.png")).convert("RGB")
PREV = 160                                   # 12.5 per cent of 1280

PH = PREV * 9 // 16
Wd = 1280 * 2 + 60 * 3
TOP, BIG = 176, PH * 4
Hd = TOP + 720 + 210 + 60 + BIG + 150
s = Image.new("RGB", (Wd, Hd), CREAM); d = ImageDraw.Draw(s)
d.text((60, 44), "VIDEO 4 THUMBNAIL — A AND B", font=f(46), fill=NAVY)
d.text((60, 100), "How to Explain Your Career Change   ·   1280 x 720   ·   "
                  "same wording in both", font=f(26, "Regular"), fill=DIM)
d.rectangle([60, 140, Wd - 60, 144], fill=GOLD)

y = 176
for i, (im, lab, note) in enumerate([
        (A, "A  —  strongest", "Portrait right, text left. She faces toward the words."),
        (B, "B  —  reversed alternate", "Portrait left, text right, tighter crop.")]):
    x = 60 + i * (1280 + 60)
    s.paste(im, (x, y)); d.rectangle([x, y, x + 1280, y + 720],
                                     outline=(214, 204, 186), width=3)
    d.text((x, y + 738), lab, font=f(34), fill=NAVY)
    d.text((x, y + 782), note, font=f(24, "Regular"), fill=DIM)

y2 = y + 720 + 210
d.text((60, y2 - 62), "AT 12.5 PER CENT  —  160 PX WIDE", font=f(32), fill=NAVY)
for i, im in enumerate([A, B]):
    x = 60 + i * (1280 + 60)
    t = im.resize((PREV, PREV * 9 // 16), Image.LANCZOS)
    s.paste(t, (x, y2)); d.rectangle([x, y2, x + t.width, y2 + t.height],
                                     outline=(214, 204, 186), width=2)
    big = t.resize((t.width * 4, t.height * 4), Image.NEAREST)
    s.paste(big, (x + PREV + 40, y2))
    d.rectangle([x + PREV + 40, y2, x + PREV + 40 + big.width, y2 + big.height],
                outline=(214, 204, 186), width=2)
    d.text((x, y2 + BIG + 18), "A" if i == 0 else "B", font=f(28), fill=GOLD)

d.text((60, Hd - 78), "Photograph: photo-portrait-wine.png, 1122 x 1402. Crop, "
       "Lanczos resize and placement only. Nothing in the photograph was "
       "reconstructed, beautified, smoothed, reshaped or altered.",
       font=f(24, "Regular"), fill=DIM)
out = os.path.join(HERE, "Video_4_Thumbnail_Comparison.png")
s.save(out); print("comparison", s.size)
