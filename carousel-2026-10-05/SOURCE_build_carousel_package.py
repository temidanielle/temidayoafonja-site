# -*- coding: utf-8 -*-
"""Upload-ready package for the Stay or Leave? Seven Moves carousel.

WHAT THIS DOES NOT DO. It does not edit the carousel. The uploaded PDF already
carries both wording changes: slide 5 reads "the people who make hiring and
promotion decisions cannot yet see what you are good at", with no trace of "the
people with the power", and slide 9 is already the rewrite, titled "Seek an
outside perspective" with the WHO TO ASK block. Both were verified by text
search across all ten pages before anything here was built. The carousel's type
is set as Type3 outlines, so the PDF is not text-editable anyway: changing a
word means rebuilding it in the tool that made it.

WHAT IT DOES.

  1  Exports the ten carousel pages as PNGs at exactly 1080 x 1350, LinkedIn's
     native document size. The source page is 810 x 1013.04pt, which is 4:5, so
     the export is a clean scale with no crop and no letterbox.

  2  Builds the START HERE Featured cover at 1600 x 900 and 800 x 450. Those are
     the sizes the repository's existing Featured assets already use, in
     linkedin-featured-assets/, so this follows the house spec rather than
     inventing one.

     ITS COPY IS TAKEN ENTIRELY FROM THE CAROUSEL'S OWN COVER. Nothing is
     written here that the owner has not already approved somewhere: the title,
     the two lines under it and the byline are lifted from page 1 and page 10.
     The only new words are the eyebrow START HERE, which is what the brief asks
     the cover to say.

     Colors are sampled from the carousel itself: navy 112345 ground, cream
     F5F1E8 card, gold C9A84C, body 182238, muted gold 7F6A30. Type is DM Sans
     and Montserrat, the brand faces, because the carousel's own font is
     embedded as outlines and cannot be reused.

  3  Zips everything with a README naming what each file is for.
"""
import hashlib, os, shutil, zipfile
import pymupdf
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "2026-10-05_Stay_or_Leave_Seven_Moves.pdf")
OUT = os.path.join(HERE, "upload")
ZIP = os.path.join(HERE, "2026-10-05_Stay_or_Leave_Seven_Moves_UPLOAD_READY.zip")
G = "/tmp/gf/"

NAVY = (0x11, 0x23, 0x45)
CREAM = (0xF5, 0xF1, 0xE8)
GOLD = (0xC9, 0xA8, 0x4C)
BODY = (0x18, 0x22, 0x38)
MUTED = (0x7F, 0x6A, 0x30)

CARD_W, CARD_H = 1080, 1350          # LinkedIn document native


def font(name, size):
    return ImageFont.truetype(G + name + ".ttf", size)


def tracked(draw, xy, text, fnt, fill, extra):
    """Letterspaced caps, the way the carousel sets its eyebrows."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + extra
    return x - extra


def tracked_width(draw, text, fnt, extra):
    return sum(draw.textlength(c, font=fnt) for c in text) + extra * (len(text) - 1)


def featured_cover(w, h):
    """START HERE cover, at the size the repo's other Featured assets use."""
    scale = w / 1600.0
    img = Image.new("RGB", (w, h), NAVY)
    d = ImageDraw.Draw(img)

    pad = int(34 * scale)
    r = int(26 * scale)
    d.rounded_rectangle([pad, pad, w - pad - 1, h - pad - 1], radius=r, fill=CREAM)

    left = int(104 * scale)
    eyebrow = font("Montserrat-Bold", max(8, int(26 * scale)))
    title = font("DMSans-Bold", max(14, int(112 * scale)))
    sub = font("DMSans-Regular", max(9, int(40 * scale)))
    byline = font("Montserrat-Bold", max(7, int(22 * scale)))

    y = int(250 * scale)
    tracked(d, (left, y), "START HERE", eyebrow, MUTED, 6 * scale)

    y += int(70 * scale)
    d.text((left, y), "Stay or Leave?", font=title, fill=NAVY)

    y += int(150 * scale)
    d.text((left, y), "Most career advice gives you two options.",
           font=sub, fill=BODY)
    y += int(54 * scale)
    d.text((left, y), "Here are seven.", font=sub, fill=BODY)

    # the gold rule the carousel uses to mark a block
    ry = int(258 * scale)
    d.rectangle([left - int(28 * scale), ry, left - int(22 * scale),
                 ry + int(330 * scale)], fill=GOLD)

    by = h - pad - int(86 * scale)
    tracked(d, (left, by), "TEMIDAYO AFONJA   ·   CAPABILITY FORMATION",
            byline, MUTED, 3 * scale)
    return img


def build():
    assert os.path.exists(SRC), f"carousel not found: {SRC}"
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    doc = pymupdf.open(SRC)
    assert doc.page_count == 10, f"expected 10 pages, got {doc.page_count}"

    # the two wording changes must already be in the source
    text = "".join(doc[i].get_text() for i in range(doc.page_count))
    assert "people with the power" not in text, "slide 5 still has the old wording"
    assert "Seek an outside perspective" in text, "slide 9 is not the rewrite"
    assert "Seek an external perspective" not in text
    assert "Repair the conditions" in text and "Repair formation" not in text
    assert "W HO TO A SK" in text or "WHO TO ASK" in text, "the Who to ask block is missing"

    # 1. slide PNGs at exactly 1080 x 1350
    page = doc[0].rect
    m = pymupdf.Matrix(CARD_W / page.width, CARD_H / page.height)
    for i in range(doc.page_count):
        pix = doc[i].get_pixmap(matrix=m, alpha=False)
        assert (pix.width, pix.height) == (CARD_W, CARD_H), \
            f"page {i + 1} exported at {pix.width}x{pix.height}"
        pix.save(os.path.join(OUT, f"slide_{i + 1:02d}_1080x1350.png"))

    # 2. the Featured cover, at the house sizes
    for w, h in ((1600, 900), (800, 450)):
        featured_cover(w, h).save(
            os.path.join(OUT, f"featured_START_HERE_{w}x{h}.png"))

    # 3. the carousel itself, named for the upload
    shutil.copyfile(SRC, os.path.join(
        OUT, "2026-10-05_Stay_or_Leave_Seven_Moves.pdf"))

    readme = (
     "STAY OR LEAVE? SEVEN MOVES - UPLOAD READY\n"
     "=========================================\n\n"
     "2026-10-05_Stay_or_Leave_Seven_Moves.pdf\n"
     "    The carousel. Upload this one file to LinkedIn as a document post.\n"
     "    Ten pages, 4:5. LinkedIn renders a PDF document post directly, so the\n"
     "    PNGs below are not needed for that route.\n\n"
     "slide_01_1080x1350.png ... slide_10_1080x1350.png\n"
     "    The same ten pages as images, at LinkedIn's native document size.\n"
     "    Use these if you post as an image carousel instead of a document, or\n"
     "    for scheduling tools that will not take a PDF.\n\n"
     "featured_START_HERE_1600x900.png\n"
     "featured_START_HERE_800x450.png\n"
     "    Cover for the LinkedIn Featured section. Both sizes match the ones\n"
     "    already in linkedin-featured-assets/. Use 1600x900 unless a tool asks\n"
     "    for something smaller.\n\n"
     "WORDING, VERIFIED BEFORE PACKAGING\n"
     "    Slide 5 reads: the people who make hiring and promotion decisions\n"
     "    cannot yet see what you are good at. The old 'people with the power'\n"
     "    wording appears nowhere in the file.\n"
     "    Slide 9 is the rewrite: Seek an outside perspective, with the WHO TO\n"
     "    ASK block.\n"
     "    Move 5 reads Repair the conditions, matching the deck and workbook.\n")
    with open(os.path.join(OUT, "README.txt"), "w") as fh:
        fh.write(readme)

    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(OUT)):
            z.write(os.path.join(OUT, name), name)

    with zipfile.ZipFile(ZIP) as z:
        names = z.namelist()
    assert len(names) == 14, f"zip holds {len(names)} files: {names}"

    print("built", os.path.basename(ZIP))
    print("  files:", len(names))
    print("  sha256", hashlib.sha256(open(ZIP, "rb").read()).hexdigest())


if __name__ == "__main__":
    build()
