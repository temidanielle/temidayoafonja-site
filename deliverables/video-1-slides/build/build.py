"""Build the deck.

  PPTX  - native editable PowerPoint (12 slides + a separate reveal-builds deck)
  PDF   - printed from Chromium at true 16:9 slide size
  PNG   - exact 1920 x 1080 frames, plus every progressive-reveal state
  Sheets- contact sheet, phone-thumbnail legibility check, safe-area guides

    python3 build/build.py
"""
import os, sys, shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck import (W, H, SAFE, SAFE_CLEAR, ENDCARD_CLEAR, Canvas,
                  render_pptx, render_html)
import slides as S
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
PNG = os.path.join(OUT, "png")
REV = os.path.join(OUT, "reveals")
GUIDES = os.path.join(OUT, "guides")
RENDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_render")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

DECK = "Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over"
BUILDS = "Video-1-Reveal-Builds"


def canvases(plan):
    out = []
    for n, step in plan:
        cv = Canvas(n, step)
        S.BUILDERS[n](cv, step)
        out.append(cv)
    return out


def shoot(html_path, png_dir, names, pdf_path=None):
    """Rasterise each .slide to an exact 1920x1080 PNG; optionally print a PDF."""
    from playwright.sync_api import sync_playwright
    os.makedirs(png_dir, exist_ok=True)
    url = "file://" + os.path.abspath(html_path)
    made = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto(url, wait_until="load")
        pg.wait_for_timeout(600)          # let the woff2 faces settle
        for i, name in enumerate(names, start=1):
            el = pg.query_selector("#s%d" % i)
            p = os.path.join(png_dir, name)
            el.screenshot(path=p)
            made.append(p)
        if pdf_path:
            pg.pdf(path=pdf_path, width="13.333in", height="7.5in",
                   print_background=True, scale=0.66665,
                   margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    return made


def font(size, bold=False):
    return ImageFont.truetype(
        os.path.expanduser("~/.fonts/Montserrat-%s.ttf" % ("Bold" if bold else "Regular")),
        size)


def contact_sheet(paths, out_path):
    cols, rows, tw = 4, 3, 560
    th = int(tw * H / W)
    gx, gy, pad, top = 44, 92, 60, 176
    cw = pad * 2 + cols * tw + (cols - 1) * gx
    ch = top + rows * (th + gy) + pad - 24
    sheet = Image.new("RGB", (cw, ch), (245, 241, 232))
    d = ImageDraw.Draw(sheet)
    d.text((pad, 60), "HOW I CHANGED JOBS WITHOUT STARTING MY CAREER OVER",
           font=font(34, True), fill=(15, 35, 70))
    d.text((pad, 108), "Video 1 presentation deck   ·   12 slides   ·   1920 x 1080   ·   16:9",
           font=font(23), fill=(90, 107, 130))
    d.rectangle([pad, 152, cw - pad, 154], fill=(201, 168, 76))
    for i, p in enumerate(paths):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + gx), top + r * (th + gy)
        sheet.paste(Image.open(p).resize((tw, th), Image.LANCZOS), (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(224, 217, 200))
        d.text((x, y + th + 14), "%02d  %s" % (i + 1, S.TITLES[i + 1]),
               font=font(20, True), fill=(15, 35, 70))
    sheet.save(out_path)
    return out_path


def thumbnail_check(paths, out_path):
    """Every slide at literal phone-thumbnail size for a legibility check."""
    cols, tw = 4, 320
    th = int(tw * H / W)
    rows = (len(paths) + cols - 1) // cols
    gx, gy, pad, top = 32, 58, 48, 152
    cw = pad * 2 + cols * tw + (cols - 1) * gx
    ch = top + rows * (th + gy) + pad - 18
    sheet = Image.new("RGB", (cw, ch), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    d.text((pad, 46), "PHONE-THUMBNAIL LEGIBILITY CHECK", font=font(28, True),
           fill=(15, 35, 70))
    d.text((pad, 88), "Each slide at 320 x 180 - the one idea on the slide must still read.",
           font=font(18), fill=(90, 107, 130))
    d.rectangle([pad, 128, cw - pad, 130], fill=(201, 168, 76))
    for i, p in enumerate(paths):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + gx), top + r * (th + gy)
        sheet.paste(Image.open(p).resize((tw, th), Image.LANCZOS), (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(208, 208, 208))
        d.text((x, y + th + 10), "%02d" % (i + 1), font=font(16, True), fill=(15, 35, 70))
    sheet.save(out_path)
    return out_path


def guide_overlay(paths, outdir):
    os.makedirs(outdir, exist_ok=True)
    for i, p in enumerate(paths, start=1):
        im = Image.open(p).convert("RGB")
        d = ImageDraw.Draw(im, "RGBA")
        d.rectangle([0, 0, SAFE_CLEAR["w"], SAFE_CLEAR["h"]],
                    fill=(193, 68, 14, 38), outline=(193, 68, 14, 200), width=3)
        d.rectangle([SAFE["x"], SAFE["y"], SAFE["x"] + SAFE["w"],
                     SAFE["y"] + SAFE["h"]], outline=(193, 68, 14, 255), width=4)
        d.text((SAFE["x"] + 18, SAFE["y"] + 18),
               "CAMERA\n480 x 270 px\n25% of frame width", font=font(24, True),
               fill=(193, 68, 14))
        d.text((16, SAFE_CLEAR["h"] - 42), "KEEP-CLEAR ZONE  620 x 440",
               font=font(20, True), fill=(193, 68, 14))
        if i == 12:
            z = ENDCARD_CLEAR
            d.rectangle([z["x"], z["y"], z["x"] + z["w"], z["y"] + z["h"]],
                        fill=(201, 168, 76, 45), outline=(201, 168, 76, 230), width=4)
            d.text((z["x"] + 20, z["y"] + 20), "YOUTUBE END-SCREEN ELEMENT",
                   font=font(24, True), fill=(160, 128, 40))
        im.save(os.path.join(outdir, "guide-%02d.png" % i))


def main():
    for d in (OUT, PNG, REV, GUIDES, RENDER):
        os.makedirs(d, exist_ok=True)
    for d in (PNG, REV, GUIDES):
        shutil.rmtree(d); os.makedirs(d)

    # --- main 12-slide deck -------------------------------------------------
    main_plan = [(n, S.STEPS[n]) for n in range(1, 13)]
    cvs = canvases(main_plan)
    render_pptx(cvs, os.path.join(OUT, DECK + ".pptx"))
    html = render_html(cvs, os.path.join(RENDER, "deck.html"),
                       "How I Changed Jobs Without Starting My Career Over")
    names = ["slide-%02d-%s.png" % (n, S.SLUGS[n]) for n in range(1, 13)]
    pngs = shoot(html, PNG, names, pdf_path=os.path.join(OUT, DECK + ".pdf"))
    print("deck: %d slides" % len(pngs))

    # --- progressive reveal builds -----------------------------------------
    rev_plan, rev_names = [], []
    for n in range(1, 13):
        if S.STEPS[n] > 1:
            for s in range(1, S.STEPS[n] + 1):
                rev_plan.append((n, s))
                rev_names.append("slide-%02d-build-%d.png" % (n, s))
    rcvs = canvases(rev_plan)
    render_pptx(rcvs, os.path.join(OUT, BUILDS + ".pptx"))
    rhtml = render_html(rcvs, os.path.join(RENDER, "builds.html"), "Reveal builds")
    shoot(rhtml, REV, rev_names, pdf_path=os.path.join(OUT, BUILDS + ".pdf"))
    print("reveal builds: %d frames" % len(rev_names))

    contact_sheet(pngs, os.path.join(OUT, "contact-sheet.png"))
    thumbnail_check(pngs, os.path.join(OUT, "phone-thumbnail-check.png"))
    guide_overlay(pngs, GUIDES)
    print("contact sheet, thumbnail check and safe-area guides done")


if __name__ == "__main__":
    main()
