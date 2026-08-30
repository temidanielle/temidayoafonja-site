"""Video 6 revision 2 — series contact sheet and mobile-legibility checks.

The contact sheet places the actual approved upload files for Videos 2, 3, 4
and 5 beside the revised Video 6 options, all at the same displayed size on the
same neutral cream ground, so the channel can be judged as one series rather
than as a QA board.

Every preview is a Lanczos downscale of the real file. Nothing is redrawn at
preview size.
"""
import os
from PIL import Image, ImageDraw, ImageFont
from build_thumbnails import not_equal, CREAM, GOLD, NAVY

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, "..", ".."))
INK  = (36, 46, 64)
MUTE = (118, 128, 146)
EDGE = (222, 214, 198)

FD = os.path.expanduser("~/.fonts/")
def mont(sz, w="Bold"):
    return ImageFont.truetype(FD + "MontserratTB-%s.ttf" % w, sz)
def dm(sz, w="Regular"):
    return ImageFont.truetype(FD + "DMSans-%s.ttf" % w, sz)

SERIES = [
    ("VIDEO 2", "approved upload",
     R + "/video-2-slides/thumbnail/VIDEO_2_THUMBNAIL_FINAL_3840x2160.png"),
    ("VIDEO 3", "approved upload",
     R + "/video-3-slides/thumbnail/VIDEO_3_THUMBNAIL_FINAL_A_3840x2160.png"),
    ("VIDEO 4", "approved upload",
     R + "/video-4-slides/thumbnail/Video_4_Thumbnail_A.png"),
    ("VIDEO 5", "approved upload",
     R + "/video-5-slides/thumbnail/Video_5_Thumbnail_A_Final.png"),
    ("VIDEO 6 — OPTION A", "revised, two lines",
     HERE + "/Video_6_Thumbnail_A.png"),
    ("VIDEO 6 — OPTION B", "revised, three lines",
     HERE + "/Video_6_Thumbnail_B.png"),
]

def load(p):
    im = Image.open(p).convert("RGB")
    assert abs(im.width / im.height - 16 / 9) < 1e-6, (p, im.size)
    return im

def tile(im, w):
    t = im.resize((w, round(w * 9 / 16)), Image.LANCZOS)
    o = Image.new("RGB", (t.width + 2, t.height + 2), EDGE)
    o.paste(t, (1, 1))
    return o

def mark_inline(canvas, d, x, y, sz, color):
    """'MORE WORK <mark> GROWTH' in running caption text."""
    d.text((x, y), "MORE WORK", font=dm(sz), fill=color)
    x += d.textlength("MORE WORK ", font=dm(sz))
    h = int(sz * 0.60)
    w = not_equal(canvas, int(x), int(y + sz * 0.18), h, color)
    d = ImageDraw.Draw(canvas)
    d.text((x + w + sz * 0.32, y), "GROWTH", font=dm(sz), fill=color)
    return d

# ------------------------------------------------------------- contact sheet
TW, COLS, GAP, MARG = 560, 3, 52, 64
TH = round(TW * 9 / 16)
CAP = 62
SW = MARG * 2 + COLS * TW + (COLS - 1) * GAP
TOP = 168
SH = TOP + 2 * (TH + CAP) + GAP + MARG

s = Image.new("RGB", (SW, SH), CREAM)
d = ImageDraw.Draw(s)
d.text((MARG, 56), "CAPABILITY FORMATION — THUMBNAIL SERIES",
       font=mont(38, "ExtraBold"), fill=INK)
d.text((MARG, 108), "Videos 2 to 5 are the approved upload files. Video 6 is "
       "shown in two revised options, at the same size on the same ground.",
       font=dm(23), fill=MUTE)
d.rectangle([MARG, 148, SW - MARG, 150], fill=EDGE)

for i, (lab, note, path) in enumerate(SERIES):
    x = MARG + (i % COLS) * (TW + GAP)
    y = TOP + (i // COLS) * (TH + CAP + GAP)
    s.paste(tile(load(path), TW), (x - 1, y - 1))
    d.text((x, y + TH + 14), lab, font=mont(23, "ExtraBold"), fill=INK)
    d.text((x, y + TH + 42), note, font=dm(20), fill=MUTE)

s.save(os.path.join(HERE, "Video_6_Thumbnail_Series_Contact_Sheet.png"))
print("wrote Video_6_Thumbnail_Series_Contact_Sheet.png", s.size)

# --------------------------------------------------------- mobile size checks
WIDTHS = (200, 180, 160)
ROWS = [("VIDEO 4 — approved", SERIES[2][2]),
        ("VIDEO 5 — approved", SERIES[3][2]),
        ("VIDEO 6 — OPTION A", SERIES[4][2]),
        ("VIDEO 6 — OPTION B", SERIES[5][2])]

LBL = 300
CELL = 240
MW = MARG * 2 + LBL + len(WIDTHS) * CELL
MH = 210 + len(ROWS) * 152 + MARG

m = Image.new("RGB", (MW, MH), CREAM)
d = ImageDraw.Draw(m)
d.text((MARG, 52), "MOBILE-SIZE CHECK — 200, 180 AND 160 PX",
       font=mont(36, "ExtraBold"), fill=INK)
d.text((MARG, 102), "Actual pixel widths, shown 1:1. The approved Video 4 and "
       "Video 5 uploads are included as the reference.",
       font=dm(22), fill=MUTE)
d.rectangle([MARG, 140, MW - MARG, 142], fill=EDGE)

for j, w in enumerate(WIDTHS):
    d.text((MARG + LBL + j * CELL, 164), "%d px" % w, font=mont(20, "Bold"), fill=MUTE)
for i, (lab, path) in enumerate(ROWS):
    y = 196 + i * 152
    im = load(path)
    d.text((MARG, y + 44), lab, font=mont(22, "ExtraBold"), fill=INK)
    for j, w in enumerate(WIDTHS):
        t = tile(im, w)
        m.paste(t, (MARG + LBL + j * CELL, y + 56 - t.height // 2))

m.save(os.path.join(HERE, "Video_6_Thumbnail_Mobile_Check.png"))
print("wrote Video_6_Thumbnail_Mobile_Check.png", m.size)
