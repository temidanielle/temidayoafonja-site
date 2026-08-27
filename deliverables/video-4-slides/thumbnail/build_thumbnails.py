"""Video 4 thumbnail variants.

Source photograph:
  deliverables/video-1-slides/assets/photo-portrait-wine.png, 1122 x 1402

Layout, crop and background treatment only. Nothing in the photograph is
reconstructed, beautified, smoothed, reshaped or altered: no change to her
face, skin, features, hair, expression, clothing or proportions. Crop and
Lanczos resize, nothing else.

Built at 2560 x 1440 and exported at 1280 x 720, so the photograph is barely
enlarged from its native resolution.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "video-1-slides", "assets",
                   "photo-portrait-wine.png")

W, H = 2560, 1440                      # build size; exported at 1280 x 720
OUT_W, OUT_H = 1280, 720
NAVY = (15, 35, 70)
CREAM = (245, 240, 232)
GOLD = (201, 168, 76)
BRANCH = (255, 255, 255, 20)           # the branching line, deliberately faint
FD = os.path.expanduser("~/.fonts/")

PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1122, 1402), PHOTO.size

L1, L2 = "YOUR CAREER", "MAKES SENSE"


def f(sz, w="ExtraBold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)


def measure(d, t, fo):
    b = d.textbbox((0, 0), t, font=fo)
    return b[2] - b[0], b[3] - b[1]


def fit(d, lines, col_w, start=260):
    """One size that fits the longest line, so both lines share a scale."""
    s = start
    while s > 40:
        fo = f(s)
        if max(measure(d, t, fo)[0] for t in lines) <= col_w:
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


def branching(size, x_in, x_join, x_out, y_mid, spread):
    """Three strands resolving into one path.

    The branching itself sits in the negative space beside the headline; only
    the single resolved line passes behind the words, so nothing crosses a
    letterform. Drawn at very low opacity and kept secondary throughout.
    """
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    step = max(1, abs(x_join - x_in) // 40)
    sign = 1 if x_out > x_in else -1
    for off in (-spread, 0, spread):
        pts = []
        for i in range(41):
            t = i / 40.0
            x = x_in + (x_join - x_in) * t
            # ease the strand from its own height into the shared line
            y = y_mid + off * (1 - t) ** 2
            pts.append((x, y))
        d.line(pts, fill=BRANCH, width=5, joint="curve")
    d.line([(x_join, y_mid), (x_out, y_mid)], fill=BRANCH, width=5)
    return layer


def headline(canvas, col_x, col_w, centre_y):
    """Both lines share one size. Positions come from real ink boxes."""
    d = ImageDraw.Draw(canvas)
    fo, s = fit(d, [L1, L2], col_w, 260)
    b1 = d.textbbox((0, 0), L1, font=fo)
    b2 = d.textbbox((0, 0), L2, font=fo)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    w2 = b2[2] - b2[0]
    line_gap = int(s * 0.30)
    rule_gap = int(s * 0.26)
    rule_h = max(7, int(s * 0.055))
    total = h1 + line_gap + h2 + rule_gap + rule_h
    top = centre_y - total / 2.0
    d.text((col_x - b1[0], top - b1[1]), L1, font=fo, fill=CREAM)
    y2 = top + h1 + line_gap
    d.text((col_x - b2[0], y2 - b2[1]), L2, font=fo, fill=GOLD)
    ry = y2 + h2 + rule_gap
    d.rectangle([col_x, ry, col_x + int(w2 * 0.52), ry + rule_h], fill=GOLD)
    return s, top, ry + rule_h


REPORT = []

# ------------------------------------------------- A: portrait right, text left
a = Image.new("RGB", (W, H), NAVY)
box = (1470, 0, W, H)
cw, ch, sc = place(a, box, 620, 60, 1180)
REPORT.append(("A", box, cw, ch, sc))
a = Image.alpha_composite(a.convert("RGBA"),
                          branching((W, H), 60, 470, 1440, H / 2, 210)).convert("RGB")
d = ImageDraw.Draw(a)
d.rectangle([1470, 0, 1482, H], fill=GOLD)
size_a, _, _ = headline(a, 190, 1150, H / 2)
a.resize((OUT_W, OUT_H), Image.LANCZOS).save(
    os.path.join(HERE, "Video_4_Thumbnail_A.png"))

# ------------------------------- B: reversed, portrait left, text right, tighter
b = Image.new("RGB", (W, H), NAVY)
box = (0, 0, 1010, H)
cw, ch, sc = place(b, box, 580, 110, 1120)
REPORT.append(("B", box, cw, ch, sc))
b = Image.alpha_composite(b.convert("RGBA"),
                          branching((W, H), 2500, 2090, 1120, H / 2, 210)).convert("RGB")
d = ImageDraw.Draw(b)
d.rectangle([1010, 0, 1022, H], fill=GOLD)
size_b, _, _ = headline(b, 1160, 1230, H / 2)
b.resize((OUT_W, OUT_H), Image.LANCZOS).save(
    os.path.join(HERE, "Video_4_Thumbnail_B.png"))

for n, box, cw, ch, sc in REPORT:
    print("Thumbnail %s: portrait %s  source crop %dx%d  scale %.3fx"
          % (n, box, cw, ch, sc))
print("headline point size at build scale: A %d  B %d" % (size_a, size_b))
