"""Editable SVG source for the approved Video 4 thumbnail A.

Reproduces Video_4_Thumbnail_A.png exactly: same photograph crop, same
geometry, same type, same colours. The design is locked; this file only
re-expresses it in an editable vector format.

The photograph is embedded as a base64 PNG of the exact crop used in the
raster. A photograph cannot be vectorised without altering it, and altering it
is not permitted, so it stays a raster inside the SVG. Everything else — the
navy ground, the gold divider, the branching motif, both headline lines and the
gold underline — is editable vector.
"""
import base64, io, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "video-1-slides", "assets",
                   "photo-portrait-wine.png")
FD = os.path.expanduser("~/.fonts/")
FONT_TTF = FD + "MontserratTB-ExtraBold.ttf"

W, H = 2560, 1440                       # authoring space; SVG renders at 1280x720
NAVY = "#0F2346"; CREAM = "#F5F0E8"; GOLD = "#C9A84C"
L1, L2 = "YOUR CAREER", "MAKES SENSE"

# geometry, identical to build_thumbnails.py variant A
PANEL_X, DIV_W = 1470, 12
CROP_CX, CROP_Y0, CROP_Y1 = 620, 60, 1180
COL_X, COL_W = 190, 1150
BR_IN, BR_JOIN, BR_OUT, BR_SPREAD = 60, 470, 1440, 210

d = ImageDraw.Draw(Image.new("RGB", (8, 8)))


def fit(lines, col_w, start=260):
    s = start
    while s > 40:
        fo = ImageFont.truetype(FONT_TTF, s)
        if max(d.textbbox((0, 0), t, font=fo)[2]
               - d.textbbox((0, 0), t, font=fo)[0] for t in lines) <= col_w:
            return fo, s
        s -= 2
    return ImageFont.truetype(FONT_TTF, 40), 40


def b64(data):
    return base64.b64encode(data).decode("ascii")


def photo_href():
    im = Image.open(SRC).convert("RGB")
    th = CROP_Y1 - CROP_Y0
    tw_ = W - PANEL_X
    cw = int(round(th * tw_ / H))
    sx = max(0, min(int(round(CROP_CX - cw / 2)), im.width - cw))
    crop = im.crop((sx, CROP_Y0, sx + cw, CROP_Y1))
    buf = io.BytesIO(); crop.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + b64(buf.getvalue()), crop.size


def strand(off, y_mid):
    pts = []
    for i in range(41):
        t = i / 40.0
        x = BR_IN + (BR_JOIN - BR_IN) * t
        y = y_mid + off * (1 - t) ** 2
        pts.append("%.2f,%.2f" % (x, y))
    return " ".join(pts)


def main():
    href, (cw, ch) = photo_href()
    fo, size = fit([L1, L2], COL_W, 260)
    ascent, _ = fo.getmetrics()
    b1 = d.textbbox((0, 0), L1, font=fo)
    b2 = d.textbbox((0, 0), L2, font=fo)
    h1, h2 = b1[3] - b1[1], b2[3] - b2[1]
    w2 = b2[2] - b2[0]
    line_gap = int(size * 0.30)
    rule_gap = int(size * 0.26)
    rule_h = max(7, int(size * 0.055))
    total = h1 + line_gap + h2 + rule_gap + rule_h
    top = H / 2.0 - total / 2.0
    y1_base = (top - b1[1]) + ascent
    y2_top = top + h1 + line_gap
    y2_base = (y2_top - b2[1]) + ascent
    rule_y = y2_top + h2 + rule_gap
    y_mid = H / 2.0

    font_b64 = b64(open(FONT_TTF, "rb").read())
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="1280" height="720" viewBox="0 0 %(W)d %(H)d">
  <title>Video 4 thumbnail A — YOUR CAREER MAKES SENSE</title>
  <defs>
    <style type="text/css"><![CDATA[
      @font-face {
        font-family: 'Montserrat ExtraBold';
        src: url(data:font/ttf;base64,%(font)s) format('truetype');
        font-weight: 800; font-style: normal;
      }
      .headline { font-family: 'Montserrat ExtraBold', Montserrat, sans-serif;
                  font-weight: 800; font-size: %(size)dpx; }
    ]]></style>
    <clipPath id="panel">
      <rect x="%(px)d" y="0" width="%(pw)d" height="%(H)d"/>
    </clipPath>
  </defs>

  <g id="background">
    <rect x="0" y="0" width="%(W)d" height="%(H)d" fill="%(navy)s"/>
  </g>

  <g id="branching-motif" stroke="#FFFFFF" stroke-opacity="0.078"
     stroke-width="5" fill="none" stroke-linecap="round">
    <polyline points="%(s1)s"/>
    <polyline points="%(s2)s"/>
    <polyline points="%(s3)s"/>
    <line x1="%(join)d" y1="%(ymid).2f" x2="%(out)d" y2="%(ymid).2f"/>
  </g>

  <g id="portrait" clip-path="url(#panel)">
    <image x="%(px)d" y="0" width="%(pw)d" height="%(H)d"
           preserveAspectRatio="xMidYMid slice" xlink:href="%(href)s"/>
  </g>

  <g id="divider">
    <rect x="%(px)d" y="0" width="%(dw)d" height="%(H)d" fill="%(gold)s"/>
  </g>

  <g id="headline">
    <text class="headline" x="%(tx1).2f" y="%(y1).2f" fill="%(cream)s">%(l1)s</text>
    <text class="headline" x="%(tx2).2f" y="%(y2).2f" fill="%(gold)s">%(l2)s</text>
    <rect x="%(rx)d" y="%(ry).2f" width="%(rw)d" height="%(rh)d" fill="%(gold)s"/>
  </g>
</svg>
""" % dict(W=W, H=H, font=font_b64, size=size, navy=NAVY, cream=CREAM, gold=GOLD,
           px=PANEL_X, pw=W - PANEL_X, dw=DIV_W, href=href,
           s1=strand(-BR_SPREAD, y_mid), s2=strand(0, y_mid),
           s3=strand(BR_SPREAD, y_mid), join=BR_JOIN, out=BR_OUT, ymid=y_mid,
           tx1=COL_X - b1[0], y1=y1_base, l1=L1,
           tx2=COL_X - b2[0], y2=y2_base, l2=L2,
           rx=COL_X, ry=rule_y, rw=int(w2 * 0.52), rh=rule_h)

    out = os.path.join(HERE, "Video_4_Thumbnail_A.svg")
    open(out, "w").write(svg)
    print("svg written: %s bytes" % f"{os.path.getsize(out):,}")
    print("embedded photo crop: %dx%d   headline: %dpx" % (cw, ch, size))


if __name__ == "__main__":
    main()
