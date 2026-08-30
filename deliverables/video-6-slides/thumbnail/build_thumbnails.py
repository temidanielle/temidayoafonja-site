"""Video 6 thumbnail masters — Compositions A and B.

Source photograph:
  deliverables/video-6-slides/assets/photo-selfie-caramel.jpg
  1536 x 1536 JPEG, a byte-identical copy of the supplied upload
  7b293c91-78BFE8B3F16F408A8ACE6572F92B19F0.jpeg
  (sha256 2d0869d55156fbb671965f2b78a582e084e7b7350cfade3049b3e86ea6cdb4d4).
  A real supplied photograph of Temidayo Afonja.
  Not used in the final thumbnail for Video 1, 2, 3, 4 or 5.

Only crop and Lanczos downscale are applied to the photograph. No generation,
reconstruction, beautification, smoothing, reshaping or mirroring. No colour
or exposure adjustment is applied at all in this build.

The not-equal mark has no glyph in any repository font, so it is drawn as
vector geometry (two bars plus a rotated slash) in brand gold, the same
treatment approved for the Video 6 deck.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "assets", "photo-selfie-caramel.jpg")

W, H = 2560, 1440                      # 2x master, downscaled to 1280x720
NAVY  = (15, 35, 70)
CREAM = (245, 241, 232)
GOLD  = (201, 168, 76)

FD = "/root/.fonts/"
def f(sz, w="ExtraBold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)

def cap(d, t, fo):
    """Ink box of a string: (w, h, x_off, y_off)."""
    b = d.textbbox((0, 0), t, font=fo)
    return b[2] - b[0], b[3] - b[1], b[0], b[1]

def draw_at(d, x, y, t, fo, fill):
    """Draw so that the ink box's top-left lands exactly on (x, y)."""
    b = d.textbbox((0, 0), t, font=fo)
    d.text((x - b[0], y - b[1]), t, font=fo, fill=fill)
    return b[2] - b[0], b[3] - b[1]

# ---------------------------------------------------------------- photograph
PHOTO = Image.open(SRC).convert("RGB")
assert PHOTO.size == (1536, 1536), PHOTO.size

def photo_panel(pw, ph, left):
    """Crop to the panel aspect at native resolution, then downscale only."""
    ch = PHOTO.height
    cw = int(round(ch * pw / ph))
    assert cw <= PHOTO.width, (cw, PHOTO.width)
    left = max(0, min(left, PHOTO.width - cw))
    crop = PHOTO.crop((left, 0, left + cw, ch))
    assert crop.size[0] >= pw and crop.size[1] >= ph, "would upscale"
    return crop.resize((pw, ph), Image.LANCZOS)

# ------------------------------------------------------------ not-equal mark
def not_equal(d, x, y, h, color):
    """Draw a not-equal mark whose ink box is (w, h) with top-left at (x, y).

    Bars are sized to the stem weight of the adjacent ExtraBold capitals so the
    mark reads as part of the same typeface rather than as an applied graphic.
    """
    w = int(round(h * 1.02))
    bar = int(round(h * 0.185))              # matches EB stem weight
    gap = int(round(h * 0.250))
    top = y + int(round(h * 0.30))
    d.rectangle([x, top, x + w, top + bar], fill=color)
    d.rectangle([x, top + gap + bar, x + w, top + gap + 2 * bar], fill=color)

    # slash: a rotated bar rendered on its own layer for clean edges
    sl_h = int(round(h * 1.14))
    lay = Image.new("RGBA", (w * 3, sl_h * 3), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    cx, cy = lay.width // 2, lay.height // 2
    sb = int(round(bar * 1.06))
    ld.rectangle([cx - sb // 2, cy - sl_h // 2, cx + sb - sb // 2,
                  cy + sl_h - sl_h // 2], fill=color + (255,))
    lay = lay.rotate(24, resample=Image.BICUBIC, center=(cx, cy))
    return lay, (x + w // 2 - lay.width // 2,
                 y + int(round(h * 0.5)) - lay.height // 2), w

# --------------------------------------------------------------- composition
PANEL_X = 1470                     # navy panel 0..1470, photo 1470..2560
MARGIN  = 150
GUTTER  = 86                       # clear space before the photo seam
MAXW    = PANEL_X - MARGIN - GUTTER

_D = ImageDraw.Draw(Image.new("RGB", (10, 10)))

def fit(text, target, lo=60, hi=400, weight="ExtraBold"):
    """Largest size whose ink width is <= target."""
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        w, _, _, _ = cap(_D, text, f(mid, weight))
        if w <= target:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best

def base():
    im = Image.new("RGB", (W, H), NAVY)
    panel = photo_panel(W - PANEL_X, H, 310)
    im.paste(panel, (PANEL_X, 0))
    return im

# ---- Composition A: single-line equation, gold payoff with rule
def comp_a():
    im = base()
    d = ImageDraw.Draw(im)

    s1 = fit("MORE WORK", MAXW)
    f_top = f(s1)
    tw, th, _, _ = cap(d, "MORE WORK", f_top)

    # line 2 is the mark plus GROWTH, fitted as one unit
    s2 = s1 + 40
    while True:
        fg = f(s2)
        gw, gh, _, _ = cap(d, "GROWTH", fg)
        ne_h = int(round(gh * 0.86))
        ne_w = int(round(ne_h * 1.02))
        if MARGIN + ne_w + int(ne_h * 0.42) + gw <= PANEL_X - GUTTER:
            break
        s2 -= 2

    fg = f(s2)
    gw, gh, _, _ = cap(d, "GROWTH", fg)
    ne_h = int(round(gh * 0.86))
    ne_w = int(round(ne_h * 1.02))

    gapv, rule_gap, rule_h = 86, 40, 15
    block = th + gapv + gh + rule_gap + rule_h
    y = (H - block) // 2

    draw_at(d, MARGIN, y, "MORE WORK", f_top, CREAM)

    y2 = y + th + gapv
    lay, pos, _ = not_equal(d, MARGIN, y2 + int((gh - ne_h) * 0.5), ne_h, GOLD)
    im.paste(lay, pos, lay)
    d = ImageDraw.Draw(im)

    gx = MARGIN + ne_w + int(ne_h * 0.42)
    draw_at(d, gx, y2, "GROWTH", fg, GOLD)
    d.rectangle([gx, y2 + gh + rule_gap, gx + gw, y2 + gh + rule_gap + rule_h],
                fill=GOLD)
    return im

# ---- Composition B: mark on its own line, GROWTH inverted in a gold block
def comp_b():
    im = base()
    d = ImageDraw.Draw(im)

    s1 = fit("MORE WORK", MAXW)
    f_top = f(s1)
    tw, th, _, _ = cap(d, "MORE WORK", f_top)

    padx, padt, padb = 46, 44, 50
    s3 = fit("GROWTH", MAXW - 2 * padx)
    fg = f(s3)
    gw, gh, _, _ = cap(d, "GROWTH", fg)

    ne_h = int(round(th * 1.02))
    gap1, gap2 = 74, 74
    block = th + gap1 + ne_h + gap2 + padt + gh + padb
    y = (H - block) // 2

    draw_at(d, MARGIN, y, "MORE WORK", f_top, CREAM)

    y2 = y + th + gap1
    lay, pos, _ = not_equal(d, MARGIN, y2, ne_h, GOLD)
    im.paste(lay, pos, lay)
    d = ImageDraw.Draw(im)

    y3 = y2 + ne_h + gap2 + padt
    d.rectangle([MARGIN - padx, y3 - padt,
                 MARGIN + gw + padx, y3 + gh + padb], fill=GOLD)
    draw_at(d, MARGIN, y3, "GROWTH", fg, NAVY)
    return im
if __name__ == "__main__":
    for name, im in (("A", comp_a()), ("B", comp_b())):
        im.save(os.path.join(HERE, "Video_6_Thumbnail_%s_2560x1440.png" % name))
        im.resize((1280, 720), Image.LANCZOS).save(
            os.path.join(HERE, "Video_6_Thumbnail_%s.png" % name))
        print("wrote", name)
