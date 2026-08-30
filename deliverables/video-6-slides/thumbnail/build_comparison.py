"""Video 6 thumbnail comparison and mobile-legibility sheets.

Every preview is produced by Lanczos-downscaling the same 1280 x 720 upload
master. Nothing is redrawn at preview size, so what the sheets show is exactly
what a viewer's feed would serve.

The headline's not-equal mark has no glyph in any repository font, so where a
sheet needs it in running text it is drawn with the same vector routine used
in the thumbnails themselves.
"""
import os
from PIL import Image, ImageDraw, ImageFont
from build_thumbnails import not_equal

HERE = os.path.dirname(os.path.abspath(__file__))
CREAM = (245, 241, 232)
GOLD  = (201, 168, 76)
DIM   = (150, 162, 180)
BG    = (26, 30, 38)

FD = "/root/.fonts/"
def f(sz, w="Bold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)
def dm(sz):
    return ImageFont.truetype(FD + "DMSans-Regular.ttf", sz)

A = Image.open(os.path.join(HERE, "Video_6_Thumbnail_A.png"))
B = Image.open(os.path.join(HERE, "Video_6_Thumbnail_B.png"))
assert A.size == B.size == (1280, 720)

WIDTHS = (200, 180, 160)

def px(im, w):
    return im.resize((w, round(w * 9 / 16)), Image.LANCZOS)

def frame(im, c=(70, 78, 92), t=2):
    o = Image.new("RGB", (im.width + 2 * t, im.height + 2 * t), c)
    o.paste(im, (t, t))
    return o

def headline_run(im, d, x, y, sz):
    """Draw 'MORE WORK <mark> GROWTH' in running text at size sz."""
    d.text((x, y), "MORE WORK ", font=dm(sz), fill=DIM)
    x += d.textlength("MORE WORK ", font=dm(sz))
    h = int(sz * 0.62)
    lay, pos, w = not_equal(d, int(x), int(y + sz * 0.16), h, DIM)
    im.paste(lay, pos, lay)
    d = ImageDraw.Draw(im)
    d.text((x + w + sz * 0.34, y), "GROWTH", font=dm(sz), fill=DIM)
    return d, x + w + sz * 0.34 + d.textlength("GROWTH", font=dm(sz))

# ------------------------------------------------------------ comparison sheet
FW = 900
SW = 60 + FW + 60 + FW + 60
SH = 252 + round(FW * 9 / 16) + 70 + 110 + 36 + round(max(WIDTHS) * 9 / 16) + 4 + 56

s = Image.new("RGB", (SW, SH), BG)
d = ImageDraw.Draw(s)
d.text((60, 46), "VIDEO 6 THUMBNAIL — COMPOSITION A vs COMPOSITION B",
       font=f(40, "ExtraBold"), fill=CREAM)
d, xe = headline_run(s, d, 60, 106, 26)
d.text((xe + 16, 106), "   |   1280 x 720, exact 16:9   |   not-equal mark "
       "drawn as vector geometry", font=dm(26), fill=DIM)

NOTES = ("single-line equation; GROWTH in gold with a gold rule",
         "mark on its own line; GROWTH reversed out of a solid gold block")
for i, (lab, im, note) in enumerate((("COMPOSITION A", A, NOTES[0]),
                                     ("COMPOSITION B", B, NOTES[1]))):
    x = 60 + i * (FW + 60)
    d.text((x, 168), lab, font=f(32, "ExtraBold"), fill=GOLD)
    d.text((x, 212), note, font=dm(23), fill=DIM)
    s.paste(frame(px(im, FW)), (x - 2, 252))

y0 = 252 + round(FW * 9 / 16) + 70
d.text((60, y0), "MOBILE-SIZE PREVIEWS — actual pixel widths, shown at 1:1",
       font=f(32, "ExtraBold"), fill=CREAM)
d.text((60, y0 + 46), "A phone feed serves a thumbnail at roughly 160-200 px wide.",
       font=dm(23), fill=DIM)

y1 = y0 + 110
for i, (lab, im) in enumerate((("A", A), ("B", B))):
    x = 60 + i * (FW + 60)
    for j, w in enumerate(WIDTHS):
        cx = x + j * 300
        d.text((cx, y1), "%s at %d px" % (lab, w), font=dm(22), fill=DIM)
        s.paste(frame(px(im, w)), (cx - 2, y1 + 36))

s.save(os.path.join(HERE, "Video_6_Thumbnail_Comparison.png"))
print("wrote Video_6_Thumbnail_Comparison.png", s.size)

# ------------------------------------------------- mobile legibility check 3x
COL = 950
MW = 60 + COL + 40 + COL + 60
col_h = 56 + sum(round(w * 9 / 16) * 3 + 4 + 30 for w in WIDTHS)
MH = 216 + col_h + 60

m = Image.new("RGB", (MW, MH), BG)
d = ImageDraw.Draw(m)
d.text((60, 46), "VIDEO 6 THUMBNAIL — MOBILE LEGIBILITY CHECK",
       font=f(40, "ExtraBold"), fill=CREAM)
d.text((60, 104), "Left: the master downscaled to the stated phone-feed width, shown 1:1.",
       font=dm(24), fill=DIM)
d.text((60, 138), "Right: that same downscale magnified 3x nearest-neighbour — "
       "no detail added, only enlarged for inspection.", font=dm(24), fill=DIM)

for i, (lab, im) in enumerate((("COMPOSITION A", A), ("COMPOSITION B", B))):
    x = 60 + i * (COL + 40)
    y = 216
    d.text((x, y), lab, font=f(32, "ExtraBold"), fill=GOLD)
    y += 56
    for w in WIDTHS:
        small = px(im, w)
        big = small.resize((w * 3, small.height * 3), Image.NEAREST)
        d.text((x, y + small.height // 2 - 14), "%d px" % w, font=dm(24), fill=CREAM)
        m.paste(frame(small), (x + 84, y))
        m.paste(frame(big), (x + 84 + 210, y))
        y += big.height + 34

m.save(os.path.join(HERE, "Video_6_Thumbnail_Mobile_Check.png"))
print("wrote Video_6_Thumbnail_Mobile_Check.png", m.size)
