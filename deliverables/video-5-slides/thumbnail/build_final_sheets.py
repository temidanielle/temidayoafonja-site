"""Mobile-legibility check and updated comparison for the final Video 5 thumbnail."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.expanduser("~/.fonts/")
NAVY = (15, 35, 70); DIM = (120, 132, 150); GOLD = (201, 168, 76)
CREAM = (250, 247, 241)

def f(s, w="Bold"): return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, s)

T = Image.open(os.path.join(HERE, "Video_5_Thumbnail_A_Final.png")).convert("RGB")

# ---------------------------------------------------------- mobile check
sizes = [(320, 2, "320 px  ·  phone feed"),
         (200, 3, "200 px  ·  recommendation column"),
         (160, 4, "160 px  ·  12.5 per cent")]
pad = 60
rows = [(px, k, lab, int(px * 9 / 16), int(px * 9 / 16) * k) for px, k, lab in sizes]
Wd = pad * 2 + max(px + 40 + px * k for px, k, _, _, _ in rows)
Hd = 190 + sum(bh + 120 for *_, bh in rows) + 80
m = Image.new("RGB", (Wd, Hd), CREAM); d = ImageDraw.Draw(m)
d.text((pad, 46), "VIDEO 5 THUMBNAIL A — MOBILE LEGIBILITY", font=f(44), fill=NAVY)
d.text((pad, 104), "Native size on the left, the same pixels enlarged on the right.",
       font=f(26, "Regular"), fill=DIM)
d.rectangle([pad, 152, Wd - pad, 156], fill=GOLD)
y = 190
for px, k, lab, ph, bh in rows:
    t = T.resize((px, ph), Image.LANCZOS)
    m.paste(t, (pad, y)); d.rectangle([pad, y, pad + px, y + ph],
                                      outline=(214, 204, 186), width=2)
    big = t.resize((px * k, bh), Image.NEAREST)
    m.paste(big, (pad + px + 40, y))
    d.rectangle([pad + px + 40, y, pad + px + 40 + big.width, y + bh],
                outline=(214, 204, 186), width=2)
    d.text((pad, y + bh + 22), lab, font=f(26), fill=NAVY)
    y += bh + 120
d.text((pad, Hd - 52), "All three lines and the gold underline remain legible at every size.",
       font=f(24, "Regular"), fill=DIM)
m.save(os.path.join(HERE, "Video_5_Thumbnail_A_Final_Mobile_Check.png"))
print("mobile check", m.size)

# ------------------------------------------------------------ comparison
PREV = 160; PH = PREV * 9 // 16; BIG = PH * 4
Wd2 = 1280 + pad * 2
Hd2 = 170 + 720 + 150 + BIG + 140
c = Image.new("RGB", (Wd2, Hd2), CREAM); d = ImageDraw.Draw(c)
d.text((pad, 44), "VIDEO 5 THUMBNAIL A — FINAL", font=f(46), fill=NAVY)
d.text((pad, 100), "Should I Make an Internal Move? 3 Questions to Decide   ·   "
                   "1280 x 720   ·   portrait replaced, composition unchanged",
       font=f(26, "Regular"), fill=DIM)
d.rectangle([pad, 140, Wd2 - pad, 144], fill=GOLD)
c.paste(T, (pad, 170)); d.rectangle([pad, 170, pad + 1280, 890],
                                    outline=(214, 204, 186), width=3)
d.text((pad, 908), "Full size  —  1280 x 720", font=f(32), fill=NAVY)
y2 = 170 + 720 + 150
d.text((pad, y2 - 46), "AT 12.5 PER CENT  —  160 PX WIDE", font=f(32), fill=NAVY)
t = T.resize((PREV, PH), Image.LANCZOS)
c.paste(t, (pad, y2)); d.rectangle([pad, y2, pad + PREV, y2 + PH],
                                   outline=(214, 204, 186), width=2)
big = t.resize((PREV * 4, BIG), Image.NEAREST)
c.paste(big, (pad + PREV + 40, y2))
d.rectangle([pad + PREV + 40, y2, pad + PREV + 40 + big.width, y2 + BIG],
            outline=(214, 204, 186), width=2)
d.text((pad, Hd2 - 62), "Photograph: photo-portrait-wine.png, 1122 x 1402. Crop, "
       "Lanczos resize and position only. Not mirrored, not altered.",
       font=f(24, "Regular"), fill=DIM)
c.save(os.path.join(HERE, "Video_5_Thumbnail_A_Final_Comparison.png"))
print("comparison", c.size)
