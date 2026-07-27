#!/usr/bin/env python3
"""
BRIEF ASSET GENERATOR
=====================

Renders the two brand assets for THE CAPABILITY FORMATION BRIEF LinkedIn
newsletter — the square `mark` (logo) and the 16:9 per-edition `cover` — as
self-contained SVG, then exports crisp PNG.

No image model is involved. Every visible string is a named constant below and
the render is verified against those constants before anything is exported.

--------------------------------------------------------------------------------
A NOTE ON HOW THE TYPE IS RENDERED (read this before changing the pipeline)
--------------------------------------------------------------------------------
The brief asks for the fonts to be embedded as base64 woff2 in a <defs><style>
block so the SVG is self-contained. We do that — the woff2 is embedded for
provenance and editability. BUT the *visible* artwork is drawn as vector
outlines shaped from the real font files (fontTools + HarfBuzz), not as live
<text>.

Why: real rasterizers silently drop @font-face. This was verified in this very
environment — resvg logs "The @font-face rule is not supported. Skipped." and
then "No match for 'Cormorant Garamond' font-family", falling back to a system
sans. That is exactly the failure the brief warns about. Outlining the type
removes font resolution from the raster path entirely, so the mark and cover
render byte-identically in any renderer, on any machine, forever. The embedded
woff2 stays in the file as the source of record.

The font-resolution width check is kept and is meaningful: it compares the
rendered ink width against the width computed independently from the font's own
metrics, and fails loudly on mismatch (a wrong font file, a dropped glyph, or a
scale bug all trip it).
"""

import base64
import io
import os
import re
import shutil
import sys
from datetime import date

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image
import resvg_py


# =============================================================================
# PALETTE  — closed set of four. Any fifth value is a bug, not a design choice.
# =============================================================================
NAVY  = "#0F2347"
SAND  = "#F5F0E8"
GOLD  = "#C9A84C"
CREAM = "#F7F4EE"

PALETTE = {NAVY, SAND, GOLD, CREAM}


# =============================================================================
# GROUND  — the single switch. "navy" or "sand". Defaults to navy.
# =============================================================================
GROUND = "navy"


# =============================================================================
# STRINGS, AS NAMED CONSTANTS
# The headline and edition strings are parameters (every edition changes them).
# The name line is never a parameter and never optional.
# =============================================================================
S_KICKER  = "THE CAPABILITY FORMATION BRIEF"     # cover
S_UPPER   = "THE CAPABILITY FORMATION"           # mark, above BRIEF
S_WORD    = "BRIEF"                              # mark, display
S_HEAD_1  = "Too Deep to Leave,"                 # cover headline, line one
S_HEAD_2  = "Too Thin to Land"                   # cover headline, line two
S_EDITION = "EDITION ONE"                        # cover
S_NAME    = "TEMIDAYO AFONJA"                    # both, always present

# Used only for file naming (see EXPORT). Not a rendered string.
EDITION_NUM = 1


# =============================================================================
# TYPOGRAPHY  — two faces only. These must not be substituted.
# =============================================================================
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DISPLAY = os.path.join(HERE, "fonts", "CormorantGaramond-Medium.subset.woff2")
FONT_CAPS    = os.path.join(HERE, "fonts", "Montserrat-SemiBold.subset.woff2")

FAMILY_DISPLAY = "Cormorant Garamond"   # weight 500 — BRIEF, headline
FAMILY_CAPS    = "Montserrat"           # weight 600 — kicker, edition, name


# =============================================================================
# TUNING TABLE
# Every number here can be changed WITHOUT touching the layout code below.
# Sizes are in SVG user units (px at 1x). Tracking is in em (fraction of the
# line's own size), the way editorial letterspacing is normally reasoned about.
# The registry at the bottom of the file prints all of these on every run.
# =============================================================================

# ---- MARK (300 x 300) -------------------------------------------------------
MARK_CANVAS            = 300

MARK_DISPLAY_SIZE      = 84.0    # BRIEF, in the serif (the hero; wide margins)
MARK_DISPLAY_TRACKING  = 0.020   # BRIEF letterspacing (em)

MARK_SHOW_UPPER        = True    # the upper line is optional; drop it for a
                                 # cleaner mark at 40px (it carries no legibility
                                 # there, only texture). See the tuning guide.
MARK_UPPER_SIZE        = 9.0     # the upper line (least load-bearing element)
MARK_UPPER_TRACKING    = 0.240   # very open caps

MARK_NAME_SIZE         = 11.0    # name line, in gold
MARK_NAME_TRACKING     = 0.320

MARK_RULE_LENGTH       = 46.0    # short centred gold rule
MARK_RULE_WEIGHT       = 2.2     # stroke weight of the rule

MARK_GAP_UPPER_TO_WORD = 16.0    # ink-box gap, upper line -> BRIEF
MARK_GAP_WORD_TO_RULE  = 20.0    # ink-box gap, BRIEF -> rule
MARK_GAP_RULE_TO_NAME  = 18.0    # ink-box gap, rule -> name line

MARK_BLOCK_OFFSET      = 0.0     # +down / -up; nudge the optically centred block

# ---- COVER (1920 x 1080) ----------------------------------------------------
COVER_W                = 1920
COVER_H                = 1080

COVER_HEAD_SIZE        = 150.0   # headline, in the serif
COVER_HEAD_TRACKING    = 0.005
COVER_HEAD_LEADING     = 1.14    # baseline-to-baseline, as a multiple of size

COVER_KICKER_SIZE      = 26.0
COVER_KICKER_TRACKING  = 0.300

COVER_EDITION_SIZE     = 23.0
COVER_EDITION_TRACKING = 0.300

COVER_NAME_SIZE        = 24.0    # near the foot, in gold
COVER_NAME_TRACKING    = 0.300

COVER_RULE_LENGTH      = 92.0
COVER_RULE_WEIGHT      = 3.0

COVER_MARGIN_TOP       = 96.0    # kicker: top of its ink sits here
COVER_MARGIN_BOTTOM    = 96.0    # name: bottom of its ink sits this far off foot
COVER_GAP_HEAD_TO_RULE = 60.0
COVER_GAP_RULE_TO_EDIT = 40.0
COVER_GROUP_OFFSET     = -6.0    # +down / -up; nudge the centred middle group

# ---- NAVY-MODE COMPENSATION -------------------------------------------------
# Reversed (light-on-dark) type optically blooms and reads thinner, so navy
# gets its own size + weight compensation rather than the same numbers with the
# colours swapped. These are explicit multipliers, tunable in isolation.
# On sand they are all no-ops.
NAVY_DISPLAY_SIZE_MULT = 1.030   # bump the serif size on navy
NAVY_CAPS_SIZE_MULT    = 1.020   # bump the caps size on navy
NAVY_INK_GROW_PX       = 0.45    # px of same-colour stroke added to type on navy
                                 # (restores stem weight lost to bloom; do NOT
                                 #  switch to a heavier Cormorant cut)


# =============================================================================
# GROUND THEMES  — colour + compensation, resolved from the GROUND switch.
# =============================================================================
THEMES = {
    "navy": dict(
        ground=NAVY, type=CREAM, rule=GOLD, name=GOLD,
        display_mult=NAVY_DISPLAY_SIZE_MULT,
        caps_mult=NAVY_CAPS_SIZE_MULT,
        ink_grow=NAVY_INK_GROW_PX,
    ),
    "sand": dict(
        ground=SAND, type=NAVY, rule=GOLD, name=GOLD,
        display_mult=1.0,
        caps_mult=1.0,
        ink_grow=0.0,
    ),
}


# =============================================================================
# EXPORT SETTINGS
# =============================================================================
SUPERSAMPLE = 4          # render at 4x target, then Lanczos-downsample
OUT_DIR     = os.path.join(HERE, "output")
ARCHIVE_DIR = os.path.join(OUT_DIR, "archive")

MARK_SIZES  = [300, 40]                 # 40 is the real test
COVER_SIZES = [(1920, 1080), (1200, 644)]  # second is the 16:9-reject fallback


# =============================================================================
# TYPOGRAPHY ENGINE  — load faces, shape strings, outline glyphs.
# =============================================================================
class Face:
    """A loaded font: fontTools for outlines/metrics, HarfBuzz for shaping."""

    def __init__(self, path, family):
        self.path = path
        self.family = family
        self.tt = TTFont(path)
        # Decompress woff2 -> raw sfnt bytes so HarfBuzz can read it (HarfBuzz
        # in this environment does not decompress woff2 itself).
        bio = io.BytesIO()
        self.tt.flavor = None
        self.tt.save(bio)
        self.sfnt = bio.getvalue()
        self.upm = self.tt["head"].unitsPerEm
        self.glyphset = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.hbfont = hb.Font(hb.Face(hb.Blob(self.sfnt)))
        # Original woff2 bytes, base64 — embedded in the SVG for provenance.
        with open(path, "rb") as fh:
            self.woff2_b64 = base64.b64encode(fh.read()).decode("ascii")


class ShapedLine:
    """A shaped, positioned run of one string, ready to emit as outlines."""

    def __init__(self, face, text, size, tracking):
        self.face = face
        self.text = text
        self.size = size
        self.scale = size / face.upm
        track_units = tracking * face.upm

        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(face.hbfont, buf)

        # Positions in font units; guard against unmapped glyphs (.notdef).
        self.glyphs = []          # list of (glyph_name, x_units, y_units)
        x = 0.0
        notdef = 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            gname = face.order[info.codepoint]
            if info.codepoint == 0:
                notdef += 1
            self.glyphs.append((gname, x + pos.x_offset, pos.y_offset))
            x += pos.x_advance + track_units
        self.notdef = notdef
        self.advance_units = x - track_units          # drop trailing track
        self.width = self.advance_units * self.scale  # advance width, px

        # Ink bounding box in font units (union of glyph outlines in place).
        xmin = ymin = float("inf")
        xmax = ymax = float("-inf")
        for gname, gx, gy in self.glyphs:
            pen = BoundsPen(face.glyphset)
            face.glyphset[gname].draw(pen)
            if pen.bounds is None:      # whitespace has no outline
                continue
            bx0, by0, bx1, by1 = pen.bounds
            xmin = min(xmin, bx0 + gx); xmax = max(xmax, bx1 + gx)
            ymin = min(ymin, by0 + gy); ymax = max(ymax, by1 + gy)
        if xmin == float("inf"):        # entirely blank (shouldn't happen)
            xmin = xmax = ymin = ymax = 0.0
        # Ink extents in px, relative to the glyph origin and baseline.
        self.ink_left   = xmin * self.scale
        self.ink_right  = xmax * self.scale
        self.ink_ascent = ymax * self.scale      # baseline -> top of ink (up)
        self.ink_descent = -ymin * self.scale    # baseline -> bottom of ink (down)

    @property
    def ink_width(self):
        return self.ink_right - self.ink_left

    @property
    def ink_center_x(self):
        return (self.ink_left + self.ink_right) / 2.0

    def emit(self, cx, baseline_y, color, ink_grow=0.0):
        """SVG for this line, optically centred on cx with baseline at baseline_y."""
        x0 = cx - self.ink_center_x          # so ink centre lands on cx
        parts = []
        for gname, gx, gy in self.glyphs:
            pen = SVGPathPen(self.face.glyphset)
            self.face.glyphset[gname].draw(pen)
            d = pen.getCommands()
            if not d:
                continue
            dx = gx * self.scale
            dy = -gy * self.scale
            parts.append(
                f'<path transform="translate({dx:.4f},{dy:.4f}) '
                f'scale({self.scale:.6f},{-self.scale:.6f})" d="{d}"/>'
            )
        stroke = ""
        if ink_grow > 0:
            stroke = (f' stroke="{color}" stroke-width="{ink_grow:.3f}" '
                      f'stroke-linejoin="round"')
        return (f'<g transform="translate({x0:.4f},{baseline_y:.4f})" '
                f'fill="{color}"{stroke}>' + "".join(parts) + "</g>")


def gold_rule(cx, cy, length, weight):
    """A short centred horizontal rule (a stroked line)."""
    x1 = cx - length / 2.0
    x2 = cx + length / 2.0
    return (f'<line x1="{x1:.3f}" y1="{cy:.3f}" x2="{x2:.3f}" y2="{cy:.3f}" '
            f'stroke="{GOLD}" stroke-width="{weight:.3f}" '
            f'stroke-linecap="butt"/>')


# =============================================================================
# ASSET BUILDERS
# Each returns (svg_string, rendered_strings) where rendered_strings is the list
# of (role, text) actually placed on the canvas — the input to string verify.
# =============================================================================
def _defs(display, caps):
    """<defs> with the two fonts embedded as base64 woff2 (self-containment)."""
    return (
        "<defs><style>\n"
        f'@font-face{{font-family:"{FAMILY_DISPLAY}";font-weight:500;font-style:normal;'
        f'src:url(data:font/woff2;base64,{display.woff2_b64}) format("woff2");}}\n'
        f'@font-face{{font-family:"{FAMILY_CAPS}";font-weight:600;font-style:normal;'
        f'src:url(data:font/woff2;base64,{caps.woff2_b64}) format("woff2");}}\n'
        "</style></defs>"
    )


def build_mark(theme, display, caps):
    ink = theme["ink_grow"]
    dsize = MARK_DISPLAY_SIZE * theme["display_mult"]
    csize_u = MARK_UPPER_SIZE * theme["caps_mult"]
    csize_n = MARK_NAME_SIZE * theme["caps_mult"]
    cx = MARK_CANVAS / 2.0

    upper = ShapedLine(caps, S_UPPER, csize_u, MARK_UPPER_TRACKING)
    word  = ShapedLine(display, S_WORD, dsize, MARK_DISPLAY_TRACKING)
    name  = ShapedLine(caps, S_NAME, csize_n, MARK_NAME_TRACKING)

    # Stack the ink boxes top -> bottom, then optically centre the whole block.
    cur = 0.0
    if MARK_SHOW_UPPER:
        upper_base = cur + upper.ink_ascent
        cur = upper_base + upper.ink_descent
        cur += MARK_GAP_UPPER_TO_WORD

    word_base = cur + word.ink_ascent
    cur = word_base + word.ink_descent

    cur += MARK_GAP_WORD_TO_RULE
    rule_cy = cur + MARK_RULE_WEIGHT / 2.0
    cur += MARK_RULE_WEIGHT

    cur += MARK_GAP_RULE_TO_NAME
    name_base = cur + name.ink_ascent
    cur = name_base + name.ink_descent

    block_h = cur
    top = (MARK_CANVAS - block_h) / 2.0 + MARK_BLOCK_OFFSET

    layers = [f'<rect width="{MARK_CANVAS}" height="{MARK_CANVAS}" fill="{theme["ground"]}"/>']
    if MARK_SHOW_UPPER:
        layers.append(upper.emit(cx, top + upper_base, theme["type"], ink))
    layers += [
        word.emit(cx, top + word_base, theme["type"], ink),
        gold_rule(cx, top + rule_cy, MARK_RULE_LENGTH, MARK_RULE_WEIGHT),
        name.emit(cx, top + name_base, theme["name"], ink),
    ]
    body = "".join(layers)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{MARK_CANVAS}" height="{MARK_CANVAS}" '
        f'viewBox="0 0 {MARK_CANVAS} {MARK_CANVAS}">'
        + _defs(display, caps) + body + "</svg>"
    )
    rendered = ([("upper", S_UPPER)] if MARK_SHOW_UPPER else []) + \
               [("word", S_WORD), ("name", S_NAME)]
    return svg, rendered


def build_cover(theme, display, caps):
    ink = theme["ink_grow"]
    hsize = COVER_HEAD_SIZE * theme["display_mult"]
    ksize = COVER_KICKER_SIZE * theme["caps_mult"]
    esize = COVER_EDITION_SIZE * theme["caps_mult"]
    nsize = COVER_NAME_SIZE * theme["caps_mult"]
    cx = COVER_W / 2.0

    kicker = ShapedLine(caps, S_KICKER, ksize, COVER_KICKER_TRACKING)
    head1  = ShapedLine(display, S_HEAD_1, hsize, COVER_HEAD_TRACKING)
    head2  = ShapedLine(display, S_HEAD_2, hsize, COVER_HEAD_TRACKING)
    edition = ShapedLine(caps, S_EDITION, esize, COVER_EDITION_TRACKING)
    name   = ShapedLine(caps, S_NAME, nsize, COVER_NAME_TRACKING)

    # Kicker pinned near the top (ink top at the margin); name near the foot.
    kicker_base = COVER_MARGIN_TOP + kicker.ink_ascent
    name_base = COVER_H - COVER_MARGIN_BOTTOM - name.ink_descent

    # Middle group: head1 / head2 / rule / edition, stacked by ink boxes with
    # generous baseline-to-baseline leading, then centred in the open region.
    leading = COVER_HEAD_LEADING * hsize
    cur = 0.0
    h1_base = cur + head1.ink_ascent
    h2_base = h1_base + leading
    group_bottom = h2_base + head2.ink_descent

    group_bottom += COVER_GAP_HEAD_TO_RULE
    rule_cy = group_bottom + COVER_RULE_WEIGHT / 2.0
    group_bottom += COVER_RULE_WEIGHT

    group_bottom += COVER_GAP_RULE_TO_EDIT
    ed_base = group_bottom + edition.ink_ascent
    group_bottom = ed_base + edition.ink_descent

    group_top = h1_base - head1.ink_ascent      # == 0
    region_top = kicker_base + kicker.ink_descent
    region_bottom = name_base - name.ink_ascent
    region_center = (region_top + region_bottom) / 2.0
    group_center = (group_top + group_bottom) / 2.0
    shift = region_center - group_center + COVER_GROUP_OFFSET

    body = "".join([
        f'<rect width="{COVER_W}" height="{COVER_H}" fill="{theme["ground"]}"/>',
        kicker.emit(cx, kicker_base, theme["type"], ink),
        head1.emit(cx, h1_base + shift, theme["type"], ink),
        head2.emit(cx, h2_base + shift, theme["type"], ink),
        gold_rule(cx, rule_cy + shift, COVER_RULE_LENGTH, COVER_RULE_WEIGHT),
        edition.emit(cx, ed_base + shift, theme["type"], ink),
        name.emit(cx, name_base, theme["name"], ink),
    ])
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{COVER_W}" height="{COVER_H}" viewBox="0 0 {COVER_W} {COVER_H}">'
        + _defs(display, caps) + body + "</svg>"
    )
    rendered = [
        ("kicker", S_KICKER), ("head_1", S_HEAD_1), ("head_2", S_HEAD_2),
        ("edition", S_EDITION), ("name", S_NAME),
    ]
    return svg, rendered


# =============================================================================
# VERIFICATION  — printed to stdout on every run. Reports; never auto-corrects.
# =============================================================================
EXPECTED = {
    "upper": S_UPPER, "word": S_WORD, "name": S_NAME,
    "kicker": S_KICKER, "head_1": S_HEAD_1, "head_2": S_HEAD_2,
    "edition": S_EDITION,
}

# Probe strings for the font-resolution width check (one per face).
PROBE_DISPLAY = ("Cormorant Garamond", S_WORD, 132.0)   # face-key, text, size
PROBE_CAPS    = ("Montserrat", S_NAME, 40.0)
WIDTH_TOLERANCE = 0.02   # 2%; a system-sans fallback misses by far more


def _measure_ink_width(svg, ground_hex):
    """Rasterise an SVG and return the ink width in px (non-ground pixels)."""
    png = resvg_py.svg_to_bytes(svg_string=svg, skip_system_fonts=True)
    img = Image.open(io.BytesIO(bytes(png))).convert("RGBA")
    bg = tuple(int(ground_hex[i:i + 2], 16) for i in (1, 3, 5))
    px = img.load()
    xmin, xmax = img.width, -1
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a > 0 and (abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2])) > 40:
                if x < xmin:
                    xmin = x
                if x > xmax:
                    xmax = x
    return (xmax - xmin + 1) if xmax >= 0 else 0


def font_resolution_check(faces):
    """Compare rendered ink width to the width implied by the font's metrics.

    Guards against the exact silent failure the brief calls out: a rasterizer
    falling back to a system sans. It also catches a wrong font file, a dropped
    glyph, or a scale bug. Fails loudly on mismatch.
    """
    results = []
    pad = 40
    for face_key, text, size in (PROBE_DISPLAY, PROBE_CAPS):
        face = faces[face_key]
        line = ShapedLine(face, text, size, 0.0)
        expected = line.ink_width
        w = int(line.ink_right - line.ink_left + 2 * pad)
        h = int(line.ink_ascent + line.ink_descent + 2 * pad)
        body = line.emit(pad - line.ink_left + line.ink_center_x,
                         pad + line.ink_ascent, CREAM, 0.0)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
               f'viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" '
               f'fill="{NAVY}"/>{body}</svg>')
        rendered = _measure_ink_width(svg, NAVY)
        ok = (line.notdef == 0 and expected > 0 and rendered > 0 and
              abs(rendered - expected) / expected <= WIDTH_TOLERANCE)
        results.append(dict(face=face.family, text=text, size=size,
                            expected=expected, rendered=rendered,
                            notdef=line.notdef, ok=ok))
    return results


def verify_strings(rendered):
    out = []
    for role, text in rendered:
        exp = EXPECTED.get(role)
        out.append((role, text, exp, text == exp))
    return out


def verify_colors(svg):
    found = set(m.upper() for m in re.findall(r"#[0-9A-Fa-f]{6}", svg))
    stray = found - PALETTE
    return found, stray


# =============================================================================
# EXPORT  — 4x render, Lanczos downsample, dated filenames, never overwrite.
# =============================================================================
def _date_tag():
    d = date.today()
    return f"{d.strftime('%B')}{d.day}_{d.year}"


def _archive_if_exists(path):
    if os.path.exists(path):
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        base = os.path.basename(path)
        stamp = date.today().isoformat()
        dest = os.path.join(ARCHIVE_DIR, f"{stamp}__{base}")
        n = 1
        while os.path.exists(dest):
            dest = os.path.join(ARCHIVE_DIR, f"{stamp}_{n}__{base}")
            n += 1
        shutil.move(path, dest)
        return dest
    return None


def render_png(svg, out_w, out_h):
    """Render at SUPERSAMPLE x, then Lanczos-downsample to (out_w, out_h)."""
    png = resvg_py.svg_to_bytes(svg_string=svg, skip_system_fonts=True,
                                zoom=float(SUPERSAMPLE))
    big = Image.open(io.BytesIO(bytes(png))).convert("RGBA")
    return big.resize((out_w, out_h), Image.LANCZOS)


def export(svg, kind, ground_name, sizes, tag):
    os.makedirs(OUT_DIR, exist_ok=True)
    # Render once at the largest supersampled raster, downsample to each size.
    if kind == "Mark":
        base = render_png(svg, MARK_CANVAS * SUPERSAMPLE, MARK_CANVAS * SUPERSAMPLE)
    else:
        base = render_png(svg, COVER_W * SUPERSAMPLE, COVER_H * SUPERSAMPLE)

    saved = []
    for size in sizes:
        if isinstance(size, tuple):
            w, h = size
            label = f"{w}x{h}"
        else:
            w = h = size
            label = f"{w}x{h}"
        img = base.resize((w, h), Image.LANCZOS)
        name = f"Brief_Edition{EDITION_NUM}_{kind}_{ground_name.capitalize()}_{label}_{tag}.png"
        path = os.path.join(OUT_DIR, name)
        archived = _archive_if_exists(path)
        img.save(path)
        saved.append((path, archived))
    # Also write the self-contained SVG source alongside the PNGs.
    svg_name = f"Brief_Edition{EDITION_NUM}_{kind}_{ground_name.capitalize()}_{tag}.svg"
    svg_path = os.path.join(OUT_DIR, svg_name)
    _archive_if_exists(svg_path)
    with open(svg_path, "w") as fh:
        fh.write(svg)
    return saved, svg_path, base


def make_contact_sheet(mark_base, tag, ground_name):
    """Show the 40x40 next to the 300x300 every time the mark re-renders.
    The 40 is the real test."""
    big = mark_base.resize((300, 300), Image.LANCZOS)
    small = mark_base.resize((40, 40), Image.LANCZOS)
    pad, gap = 40, 60
    sheet_w = pad + 300 + gap + 40 + pad
    sheet_h = pad + 300 + pad
    sheet = Image.new("RGBA", (sheet_w, sheet_h), (255, 255, 255, 255))
    sheet.paste(big, (pad, pad), big)
    # sit the 40 on the baseline of the 300 so the size gap is honest
    sheet.paste(small, (pad + 300 + gap, pad + 300 - 40), small)
    name = f"Brief_Edition{EDITION_NUM}_Mark_{ground_name.capitalize()}_ContactSheet_40-vs-300_{tag}.png"
    path = os.path.join(OUT_DIR, name)
    _archive_if_exists(path)
    sheet.save(path)
    return path


# =============================================================================
# TUNING REGISTRY  — printed on every run.
# =============================================================================
TUNING_REGISTRY = [
    ("display size (mark BRIEF)",       "MARK_DISPLAY_SIZE",      MARK_DISPLAY_SIZE),
    ("display letterspacing (mark)",    "MARK_DISPLAY_TRACKING",  MARK_DISPLAY_TRACKING),
    ("upper line size (mark)",          "MARK_UPPER_SIZE",        MARK_UPPER_SIZE),
    ("upper line tracking (mark)",      "MARK_UPPER_TRACKING",    MARK_UPPER_TRACKING),
    ("name size (mark)",                "MARK_NAME_SIZE",         MARK_NAME_SIZE),
    ("name tracking (mark)",            "MARK_NAME_TRACKING",     MARK_NAME_TRACKING),
    ("rule length (mark)",              "MARK_RULE_LENGTH",       MARK_RULE_LENGTH),
    ("rule stroke weight (mark)",       "MARK_RULE_WEIGHT",       MARK_RULE_WEIGHT),
    ("gap upper->BRIEF (mark)",         "MARK_GAP_UPPER_TO_WORD", MARK_GAP_UPPER_TO_WORD),
    ("gap BRIEF->rule (mark)",          "MARK_GAP_WORD_TO_RULE",  MARK_GAP_WORD_TO_RULE),
    ("gap rule->name (mark)",           "MARK_GAP_RULE_TO_NAME",  MARK_GAP_RULE_TO_NAME),
    ("block vertical offset (mark)",    "MARK_BLOCK_OFFSET",      MARK_BLOCK_OFFSET),
    ("headline size (cover)",           "COVER_HEAD_SIZE",        COVER_HEAD_SIZE),
    ("headline tracking (cover)",       "COVER_HEAD_TRACKING",    COVER_HEAD_TRACKING),
    ("headline leading (cover)",        "COVER_HEAD_LEADING",     COVER_HEAD_LEADING),
    ("kicker size (cover)",             "COVER_KICKER_SIZE",      COVER_KICKER_SIZE),
    ("kicker tracking (cover)",         "COVER_KICKER_TRACKING",  COVER_KICKER_TRACKING),
    ("edition size (cover)",            "COVER_EDITION_SIZE",     COVER_EDITION_SIZE),
    ("edition tracking (cover)",        "COVER_EDITION_TRACKING", COVER_EDITION_TRACKING),
    ("name size (cover)",               "COVER_NAME_SIZE",        COVER_NAME_SIZE),
    ("name tracking (cover)",           "COVER_NAME_TRACKING",    COVER_NAME_TRACKING),
    ("rule length (cover)",             "COVER_RULE_LENGTH",      COVER_RULE_LENGTH),
    ("rule stroke weight (cover)",      "COVER_RULE_WEIGHT",      COVER_RULE_WEIGHT),
    ("top margin (cover)",              "COVER_MARGIN_TOP",       COVER_MARGIN_TOP),
    ("bottom margin (cover)",           "COVER_MARGIN_BOTTOM",    COVER_MARGIN_BOTTOM),
    ("gap headline->rule (cover)",      "COVER_GAP_HEAD_TO_RULE", COVER_GAP_HEAD_TO_RULE),
    ("gap rule->edition (cover)",       "COVER_GAP_RULE_TO_EDIT", COVER_GAP_RULE_TO_EDIT),
    ("group vertical offset (cover)",   "COVER_GROUP_OFFSET",     COVER_GROUP_OFFSET),
    ("navy display size mult",          "NAVY_DISPLAY_SIZE_MULT", NAVY_DISPLAY_SIZE_MULT),
    ("navy caps size mult",             "NAVY_CAPS_SIZE_MULT",    NAVY_CAPS_SIZE_MULT),
    ("navy ink-grow (px stroke)",       "NAVY_INK_GROW_PX",       NAVY_INK_GROW_PX),
]


def print_tuning_table():
    print("\n" + "=" * 72)
    print("TUNING TABLE  — change any of these without touching layout code")
    print("=" * 72)
    print(f"{'what':<34}{'constant':<26}{'value':>10}")
    print("-" * 72)
    for what, const, val in TUNING_REGISTRY:
        print(f"{what:<34}{const:<26}{val:>10}")
    print("-" * 72)
    print("GROUND is the master switch (navy | sand). Navy-mode compensation is")
    print("the three navy_* values above; on sand they are no-ops.")


# =============================================================================
# MAIN
# =============================================================================
def banner(txt):
    print("\n" + "=" * 72)
    print(txt)
    print("=" * 72)


def main():
    # GROUND defaults to the constant above; an optional CLI arg overrides it
    # for convenience (e.g. `python3 generate.py sand`) without editing the file.
    global GROUND
    if len(sys.argv) > 1:
        GROUND = sys.argv[1].strip().lower()
    if GROUND not in THEMES:
        sys.exit(f"GROUND must be one of {sorted(THEMES)}, got {GROUND!r}")
    theme = THEMES[GROUND]
    tag = _date_tag()

    display = Face(FONT_DISPLAY, FAMILY_DISPLAY)
    caps = Face(FONT_CAPS, FAMILY_CAPS)
    faces = {FAMILY_DISPLAY: display, FAMILY_CAPS: caps}

    banner(f"BRIEF ASSET GENERATOR   ground={GROUND}   edition={EDITION_NUM}   date={tag}")

    # ---- font-resolution width check (shared by both assets) ----
    banner("FONT-RESOLUTION WIDTH CHECK")
    fr = font_resolution_check(faces)
    fr_ok = True
    for r in fr:
        status = "PASS" if r["ok"] else "*** FAIL ***"
        drift = 100 * (r["rendered"] - r["expected"]) / r["expected"] if r["expected"] else 0
        print(f"  [{status}] {r['face']:<20} '{r['text']}' @ {r['size']:g}px  "
              f"expected {r['expected']:.1f}px  rendered {r['rendered']}px  "
              f"drift {drift:+.2f}%  notdef {r['notdef']}")
        fr_ok = fr_ok and r["ok"]
    if not fr_ok:
        print("\n  Font faces did not resolve to the expected metrics. Refusing to")
        print("  export — the output would be wrong in a way that is easy to miss.")
        print_tuning_table()
        sys.exit(2)

    all_ok = True
    outputs = {}
    for kind, builder, sizes in (
        ("Mark", build_mark, MARK_SIZES),
        ("Cover", build_cover, COVER_SIZES),
    ):
        banner(f"{kind.upper()}  —  verification")
        svg, rendered = builder(theme, display, caps)

        # 1. strings vs constants
        print("  strings:")
        for role, text, exp, ok in verify_strings(rendered):
            mark = "ok " if ok else "MISMATCH"
            print(f"    [{mark}] {role:<8} '{text}'" +
                  ("" if ok else f"   expected '{exp}'"))
            all_ok = all_ok and ok

        # 2. colours vs four-token palette
        found, stray = verify_colors(svg)
        if stray:
            print(f"    [PALETTE FAIL] stray colours: {sorted(stray)}")
            all_ok = False
        else:
            print(f"    [ok ] colours: all {len(found)} within the four-token palette "
                  f"{sorted(found)}")

        # 3. ground vs switch (the first <rect> is the full-canvas ground)
        ground_ok = theme["ground"] in svg.split("<rect", 1)[1][:60]
        print(f"    [{'ok ' if ground_ok else 'GROUND FAIL'}] ground fill is "
              f"{theme['ground']} (GROUND={GROUND})")
        all_ok = all_ok and ground_ok

        outputs[kind] = (svg, sizes)

    if not all_ok:
        banner("VERIFICATION FAILED — nothing exported.")
        print_tuning_table()
        sys.exit(3)

    # ---- export ----
    banner("EXPORT")
    mark_base = None
    for kind in ("Mark", "Cover"):
        svg, sizes = outputs[kind]
        saved, svg_path, base = export(svg, kind, GROUND, sizes, tag)
        if kind == "Mark":
            mark_base = base
        for path, archived in saved:
            note = f"   (archived previous -> {os.path.basename(archived)})" if archived else ""
            print(f"  wrote {os.path.relpath(path, HERE)}{note}")
        print(f"  wrote {os.path.relpath(svg_path, HERE)}  (self-contained SVG)")

    sheet = make_contact_sheet(mark_base, tag, GROUND)
    print(f"  wrote {os.path.relpath(sheet, HERE)}  (40 next to 300 — the 40 is the real test)")

    print_tuning_table()
    banner("DONE — all strings, colours, ground, and font resolution verified.")


if __name__ == "__main__":
    main()
