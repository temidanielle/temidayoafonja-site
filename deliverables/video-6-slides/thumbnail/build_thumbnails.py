"""Video 6 thumbnail masters, revision 2 — built on the approved series geometry.

Every layout constant below is taken from the approved Video 4A and Video 5A
build scripts, not from a description of them:

    canvas          2560 x 1440, exported at 1280 x 720
    portrait box    (1470, 0, 2560, 1440)
    gold divider    rectangle [1470, 0, 1482, 1440]
    text column     col_x 190, col_w 1150
    headline centre H/2 - 24                       (Video 5A)
    line gap        s * 0.34                       (Video 5A gap12)
    payoff gap      s * 0.46                       (Video 5A gap23)
    rule gap        s3 * 0.20, rule height s3*0.052 (Video 5A)
    underline       0.74 x the payoff word's width  (Video 5A)
    hairline        x 150..1370 at y 268, white at alpha 22 (Video 5A)

Palette sampled from the approved masters themselves rather than retyped:
    NAVY  #0F2346  — identical across Videos 2, 3, 4A, 5A
    CREAM #F5F0E8  — identical across Videos 2, 3, 4A, 5A
    GOLD  #C9A84C  — identical across Videos 2, 3, 4A, 5A

Source photograph:
  deliverables/video-6-slides/assets/photo-selfie-caramel.jpg
  1536 x 1536 JPEG, a byte-identical copy of the supplied upload
  7b293c91-78BFE8B3F16F408A8ACE6572F92B19F0.jpeg
  (sha256 2d0869d55156fbb671965f2b78a582e084e7b7350cfade3049b3e86ea6cdb4d4).
  Chosen because Video 6 requires a photograph not used in the final Video 4 or
  Video 5 thumbnail. Crop and Lanczos resize only — no background replacement,
  retouching, expression change or any other alteration.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "assets", "photo-selfie-caramel.jpg")

W, H = 2560, 1440
OUT_W, OUT_H = 1280, 720
NAVY  = (15, 35, 70)
CREAM = (245, 240, 232)
GOLD  = (201, 168, 76)
HAIR  = (255, 255, 255, 22)

SEAM, DIV_W = 1470, 12
COL_X, COL_W = 190, 1150
CENTRE_Y = H / 2 - 24

# Crop: full source height, so the top of her head stays in frame. See the QA
# README for why the horizontal offset is 240 and why the portrait scale cannot
# be brought down to the Video 4 / Video 5 figure by cropping.
CROP_LEFT, CROP_TOP = 240, 0
CROP_H = 1536

FD = os.path.expanduser("~/.fonts/")
PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1536, 1536), PHOTO.size

L1, MARK, L3 = "MORE WORK", "≠", "GROWTH"


def f(sz, w="ExtraBold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)


def ink(d, t, fo):
    b = d.textbbox((0, 0), t, font=fo)
    return b, b[2] - b[0], b[3] - b[1]


def fit(d, text, col_w, start=240):
    s = start
    while s > 40:
        if ink(d, text, f(s))[1] <= col_w:
            return f(s), s
        s -= 2
    return f(40), 40


def draw_at(d, x, y, t, fo, fill):
    b = d.textbbox((0, 0), t, font=fo)
    d.text((x - b[0], y - b[1]), t, font=fo, fill=fill)
    return b[2] - b[0], b[3] - b[1]


def place(canvas):
    """Crop and downscale only; never upscaled, never altered."""
    tw, th = W - SEAM, H
    cw = int(round(CROP_H * tw / th))
    crop = PHOTO.crop((CROP_LEFT, CROP_TOP, CROP_LEFT + cw, CROP_TOP + CROP_H))
    canvas.paste(crop.resize((tw, th), Image.LANCZOS), (SEAM, 0))
    return cw, CROP_H, tw / cw


def hairline(canvas):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).line([(150, 268), (1370, 268)], fill=HAIR, width=4)
    return Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")


def not_equal(canvas, x, y, h, color=GOLD):
    """The not-equal mark as vector geometry: two bars and a rotated slash.

    No repository font contains U+2260. Bar weight is set to the ExtraBold stem
    weight so the mark reads as part of the same typeface, not as an applied
    graphic. Ink box is (w, h) with its top-left at (x, y).
    """
    w = int(round(h * 1.02))
    bar = int(round(h * 0.185))
    gap = int(round(h * 0.250))
    d = ImageDraw.Draw(canvas)
    top = y + int(round(h * 0.30))
    d.rectangle([x, top, x + w, top + bar], fill=color)
    d.rectangle([x, top + gap + bar, x + w, top + gap + 2 * bar], fill=color)

    sl_h = int(round(h * 1.14))
    sb = int(round(bar * 1.06))
    lay = Image.new("RGBA", (w * 3, sl_h * 3), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    cx, cy = lay.width // 2, lay.height // 2
    ld.rectangle([cx - sb // 2, cy - sl_h // 2, cx + sb - sb // 2,
                  cy + sl_h - sl_h // 2], fill=color + (255,))
    lay = lay.rotate(24, resample=Image.BICUBIC, center=(cx, cy))
    canvas.paste(lay, (x + w // 2 - lay.width // 2,
                       y + int(round(h * 0.5)) - lay.height // 2), lay)
    return w


def frame():
    im = Image.new("RGB", (W, H), NAVY)
    place(im)
    im = hairline(im)
    ImageDraw.Draw(im).rectangle([SEAM, 0, SEAM + DIV_W, H], fill=GOLD)
    return im


def rule(d, x, y, w3, s3):
    """The restrained short underline: 0.74 of the payoff word, as in Video 5A."""
    rh = max(8, int(s3 * 0.052))
    d.rectangle([x, y, x + int(w3 * 0.74), y + rh], fill=GOLD)
    return rh


# ---- Composition A — two lines, the Video 4A structure in the Video 5A palette
def comp_a():
    im = frame()
    d = ImageDraw.Draw(im)
    fo, s = fit(d, L1, COL_W, 240)
    _, w1, h1 = ink(d, L1, fo)

    # the gold line is the mark plus the payoff word, fitted as one unit
    s3 = int(s * 1.58)
    while s3 > 40:
        fo3 = f(s3)
        _, w3, h3 = ink(d, L3, fo3)
        mh = int(round(h3 * 0.86))
        mw = int(round(mh * 1.02))
        if mw + int(mh * 0.42) + w3 <= COL_W:
            break
        s3 -= 2
    fo3 = f(s3)
    _, w3, h3 = ink(d, L3, fo3)
    mh = int(round(h3 * 0.86))
    mw = int(round(mh * 1.02))

    gap = int(s * 0.34)
    rule_gap = int(s3 * 0.20)
    rule_h = max(8, int(s3 * 0.052))
    total = h1 + gap + h3 + rule_gap + rule_h
    top = CENTRE_Y - total / 2.0

    draw_at(d, COL_X, top, L1, fo, CREAM)
    y2 = top + h1 + gap
    not_equal(im, COL_X, int(y2 + (h3 - mh) * 0.5), mh)
    d = ImageDraw.Draw(im)
    gx = COL_X + mw + int(mh * 0.42)
    draw_at(d, gx, y2, L3, fo3, GOLD)
    rule(d, gx, y2 + h3 + rule_gap, w3, s3)
    return im, s, s3, h1, h3, mh, gx + w3


# ---- Composition B — three lines, the Video 5A structure line for line
def comp_b():
    im = frame()
    d = ImageDraw.Draw(im)
    fo, s = fit(d, L1, COL_W, 240)
    _, w1, h1 = ink(d, L1, fo)
    fo3, s3 = fit(d, L3, COL_W, int(s * 1.58))
    _, w3, h3 = ink(d, L3, fo3)

    gap12 = int(s * 0.34)
    gap23 = int(s * 0.46)
    rule_gap = int(s3 * 0.20)
    rule_h = max(8, int(s3 * 0.052))
    mh = h1
    total = h1 + gap12 + mh + gap23 + h3 + rule_gap + rule_h
    top = CENTRE_Y - total / 2.0

    draw_at(d, COL_X, top, L1, fo, CREAM)
    y2 = top + h1 + gap12
    not_equal(im, COL_X, int(y2), mh)
    d = ImageDraw.Draw(im)
    y3 = y2 + mh + gap23
    draw_at(d, COL_X, y3, L3, fo3, GOLD)
    rule(d, COL_X, y3 + h3 + rule_gap, w3, s3)
    return im, s, s3, h1, h3, mh, COL_X + w3


if __name__ == "__main__":
    for name, (im, s, s3, h1, h3, mh, right) in (("A", comp_a()), ("B", comp_b())):
        im.save(os.path.join(HERE, "Video_6_Thumbnail_%s_2560x1440.png" % name))
        im.resize((OUT_W, OUT_H), Image.LANCZOS).save(
            os.path.join(HERE, "Video_6_Thumbnail_%s.png" % name))
        print("%s: setup %d / payoff %d   caps %d / %d   mark %d   "
              "right edge %d (seam %d)" % (name, s, s3, h1, h3, mh, right, SEAM))
    cw, ch, sc = place(Image.new("RGB", (W, H)))
    print("portrait: crop %dx%d at (%d,%d) -> 1090x1440, scale %.3fx"
          % (cw, ch, CROP_LEFT, CROP_TOP, sc))
