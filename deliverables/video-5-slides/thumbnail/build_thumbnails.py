"""Video 5 thumbnail variants.

Source photograph:
  a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png, 1254 x 1254
  the verified caramel studio portrait already used for Videos 2 and 3.

Layout and background treatment only. Nothing in the photograph is
reconstructed, beautified, smoothed, reshaped or altered: no change to her
face, skin tone, features, hair, expression, clothing or proportions. Crop and
Lanczos resize, nothing else.

Built at 2560 x 1440 and exported at 1280 x 720, so the photograph stays close
to its native resolution.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = ("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
       "a55ff6e1-D85AD998016A47539E6889F2988BF6B5.png")

W, H = 2560, 1440
OUT_W, OUT_H = 1280, 720
NAVY = (15, 35, 70)
CREAM = (245, 240, 232)
GOLD = (201, 168, 76)
HAIR = (255, 255, 255, 22)          # the single abstract line, deliberately faint
FD = os.path.expanduser("~/.fonts/")

PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1254, 1254), PHOTO.size

L1, L2, L3 = "YOU MAY NOT", "NEED TO", "LEAVE"


def f(sz, w="ExtraBold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)


def ink(d, t, fo):
    b = d.textbbox((0, 0), t, font=fo)
    return b, b[2] - b[0], b[3] - b[1]


def fit(d, text, col_w, start=240):
    s = start
    while s > 40:
        fo = f(s)
        if ink(d, text, fo)[1] <= col_w:
            return fo, s
        s -= 2
    return f(40), 40


def place(canvas, box, centre_x, y0, y1):
    x0, y0b, x1, y1b = box
    tw, th = x1 - x0, y1b - y0b
    ch = y1 - y0
    cw = int(round(ch * tw / th))
    sx = max(0, min(int(round(centre_x - cw / 2)), PHOTO.width - cw))
    canvas.paste(PHOTO.crop((sx, y0, sx + cw, y1)).resize((tw, th), Image.LANCZOS),
                 (x0, y0b))
    return cw, ch, tw / cw


def thin_line(size, x0, x1, y):
    """One abstract line, low opacity, entirely inside the frame."""
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).line([(x0, y), (x1, y)], fill=HAIR, width=4)
    return layer


def headline(canvas, col_x, col_w, centre_y):
    """Two setup lines, then LEAVE larger and gold with a short gold rule."""
    d = ImageDraw.Draw(canvas)
    fo, s = fit(d, L1, col_w, 240)
    fo3, s3 = fit(d, L3, col_w, int(s * 1.58))
    b1, w1, h1 = ink(d, L1, fo)
    b2, w2, h2 = ink(d, L2, fo)
    b3, w3, h3 = ink(d, L3, fo3)
    gap12 = int(s * 0.34)
    gap23 = int(s * 0.46)
    rule_gap = int(s3 * 0.20)
    rule_h = max(8, int(s3 * 0.052))
    total = h1 + gap12 + h2 + gap23 + h3 + rule_gap + rule_h
    top = centre_y - total / 2.0

    d.text((col_x - b1[0], top - b1[1]), L1, font=fo, fill=CREAM)
    y2 = top + h1 + gap12
    d.text((col_x - b2[0], y2 - b2[1]), L2, font=fo, fill=CREAM)
    y3 = y2 + h2 + gap23
    d.text((col_x - b3[0], y3 - b3[1]), L3, font=fo3, fill=GOLD)
    ry = y3 + h3 + rule_gap
    d.rectangle([col_x, ry, col_x + int(w3 * 0.74), ry + rule_h], fill=GOLD)
    return s, s3, top, ry + rule_h


REPORT = []

# ------------------------------------------- A: portrait right, text left
a = Image.new("RGB", (W, H), NAVY)
box = (1470, 0, W, H)
cw, ch, sc = place(a, box, 712, 140, 1254)
REPORT.append(("A", box, cw, ch, sc))
a = Image.alpha_composite(a.convert("RGBA"),
                          thin_line((W, H), 150, 1370, 268)).convert("RGB")
d = ImageDraw.Draw(a)
d.rectangle([1470, 0, 1482, H], fill=GOLD)
sa, s3a, _, _ = headline(a, 190, 1150, H / 2 - 24)
a.resize((OUT_W, OUT_H), Image.LANCZOS).save(
    os.path.join(HERE, "Video_5_Thumbnail_A.png"))

# ------------------------------ B: reversed, portrait left, text right
b = Image.new("RGB", (W, H), NAVY)
box = (0, 0, 1010, H)
cw, ch, sc = place(b, box, 660, 140, 1254)
REPORT.append(("B", box, cw, ch, sc))
b = Image.alpha_composite(b.convert("RGBA"),
                          thin_line((W, H), 1160, 2410, 268)).convert("RGB")
d = ImageDraw.Draw(b)
d.rectangle([1010, 0, 1022, H], fill=GOLD)
sb, s3b, _, _ = headline(b, 1160, 1240, H / 2 - 24)
b.resize((OUT_W, OUT_H), Image.LANCZOS).save(
    os.path.join(HERE, "Video_5_Thumbnail_B.png"))

for n, box, cw, ch, sc in REPORT:
    print("Thumbnail %s: portrait %s  source crop %dx%d  scale %.3fx"
          % (n, box, cw, ch, sc))
print("headline sizes at build scale: A setup %d / LEAVE %d   B setup %d / LEAVE %d"
      % (sa, s3a, sb, s3b))
