"""Video 5 Thumbnail A, final. One change only: the portrait.

The approved composition is preserved exactly — portrait right, text left, the
navy ground, the cream and gold type at the same sizes and hierarchy, the three
approved lines, the gold underline beneath LEAVE, the negative space, the gold
divider, the faint hairline and the 1280 x 720 canvas.

Portrait replaced with:
  deliverables/video-1-slides/assets/photo-portrait-wine.png, 1122 x 1402

Crop, Lanczos resize and position only. No reconstruction, mirroring,
beautification, smoothing, reshaping or alteration of face, skin tone,
features, hair, expression, clothing or proportions.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "video-1-slides", "assets",
                   "photo-portrait-wine.png")

W, H = 2560, 1440
OUT_W, OUT_H = 1280, 720
NAVY = (15, 35, 70); CREAM = (245, 240, 232); GOLD = (201, 168, 76)
HAIR = (255, 255, 255, 22)
FD = os.path.expanduser("~/.fonts/")

PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1122, 1402), PHOTO.size
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
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).line([(x0, y), (x1, y)], fill=HAIR, width=4)
    return layer


def headline(canvas, col_x, col_w, centre_y):
    """Unchanged from the approved Thumbnail A."""
    d = ImageDraw.Draw(canvas)
    fo, s = fit(d, L1, col_w, 240)
    fo3, s3 = fit(d, L3, col_w, int(s * 1.58))
    b1, w1, h1 = ink(d, L1, fo)
    b2, w2, h2 = ink(d, L2, fo)
    b3, w3, h3 = ink(d, L3, fo3)
    gap12 = int(s * 0.34); gap23 = int(s * 0.46)
    rule_gap = int(s3 * 0.20); rule_h = max(8, int(s3 * 0.052))
    total = h1 + gap12 + h2 + gap23 + h3 + rule_gap + rule_h
    top = centre_y - total / 2.0
    d.text((col_x - b1[0], top - b1[1]), L1, font=fo, fill=CREAM)
    y2 = top + h1 + gap12
    d.text((col_x - b2[0], y2 - b2[1]), L2, font=fo, fill=CREAM)
    y3 = y2 + h2 + gap23
    d.text((col_x - b3[0], y3 - b3[1]), L3, font=fo3, fill=GOLD)
    ry = y3 + h3 + rule_gap
    d.rectangle([col_x, ry, col_x + int(w3 * 0.74), ry + rule_h], fill=GOLD)
    return s, s3


a = Image.new("RGB", (W, H), NAVY)
box = (1470, 0, W, H)
cw, ch, sc = place(a, box, 600, 90, 1150)
a = Image.alpha_composite(a.convert("RGBA"),
                          thin_line((W, H), 150, 1370, 268)).convert("RGB")
d = ImageDraw.Draw(a)
d.rectangle([1470, 0, 1482, H], fill=GOLD)
s, s3 = headline(a, 190, 1150, H / 2 - 24)
final = a.resize((OUT_W, OUT_H), Image.LANCZOS)
final.save(os.path.join(HERE, "Video_5_Thumbnail_A_Final.png"))
print("portrait region %s   source crop %dx%d   scale %.3fx" % (box, cw, ch, sc))
print("headline sizes unchanged: setup %d / LEAVE %d" % (s, s3))
