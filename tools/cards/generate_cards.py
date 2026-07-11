#!/usr/bin/env python3
"""
Capability Audit quote cards + Density teaser card generator.

Self-contained: renders all seven brand cards from one template system using
Pillow and the bundled Cormorant Garamond / Montserrat font files.

Run:  python3 tools/cards/generate_cards.py
Output: seven PNGs written to the repository root.

Cards
  Six portrait quote cards (2160 x 2700) — sand ground, navy Cormorant
  Garamond quote centered as a group with a gold rule and a navy
  "THE CAPABILITY AUDIT" attribution line, and a gold "TEMIDAYO AFONJA"
  signature anchored near the bottom.

  One landscape Density teaser card (2245 x 1587).
"""

import os
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- paths
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "output")  # cards render here, kept out of the live site
os.makedirs(OUT, exist_ok=True)

CORMORANT_MED = os.path.join(FONTS, "CormorantGaramond-Medium.ttf")
CORMORANT_SB = os.path.join(FONTS, "CormorantGaramond-SemiBold.ttf")
MONTSERRAT_MED = os.path.join(FONTS, "Montserrat-Medium.ttf")
MONTSERRAT_SB = os.path.join(FONTS, "Montserrat-SemiBold.ttf")

# ---------------------------------------------------------------- palette
SAND = "#F5F0E8"
NAVY = "#0F2347"
GOLD = "#C9A84C"
WHITE = "#FFFFFF"

SS = 2  # supersample factor for crisp antialiased text, downsampled at save


def font(path, size):
    return ImageFont.truetype(path, int(round(size * SS)))


# ---------------------------------------------------------------- helpers
def line_width(draw, text, fnt, tracking):
    """Total advance width of a single line rendered with per-char tracking."""
    if not text:
        return 0
    w = sum(draw.textlength(ch, font=fnt) for ch in text)
    return w + tracking * SS * (len(text) - 1)


def draw_tracked(draw, cx, baseline_y, text, fnt, fill, tracking):
    """Draw a single line of letterspaced text, horizontally centered on cx.

    baseline_y is in supersampled pixels and is the text baseline.
    """
    total = line_width(draw, text, fnt, tracking)
    x = cx - total / 2.0
    ascent, _ = fnt.getmetrics()
    top = baseline_y - ascent
    for ch in text:
        draw.text((x, top), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking * SS


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a max pixel width (supersampled)."""
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def new_canvas(w, h, bg):
    img = Image.new("RGB", (w * SS, h * SS), bg)
    return img, ImageDraw.Draw(img)


def finalize(img, w, h, path):
    img = img.resize((w, h), Image.LANCZOS)
    img.save(path, "PNG")
    return path


# ---------------------------------------------------------------- quote cards
QW, QH = 2160, 2700

QUOTES = [
    ("quote_look_safe.png",
     "The people who look safe and the people who are safe are rarely the same list."),
    ("quote_compounding_corner.png",
     "You don’t hire compounding people. You build the corner they grow in."),
    ("quote_advice_kindness.png",
     "The most dangerous career advice sounds like kindness."),
    ("quote_retention_risk.png",
     "Your best expert may be your quietest retention risk."),
    ("quote_competitor_twice.png",
     "What a competitor will pay for twice."),
    ("quote_title_travel.png",
     "A title doesn’t travel."),
]

# Type sizes (design pixels, pre-supersample)
QUOTE_SIZE = 132          # Cormorant Garamond, navy, one size for all six
QUOTE_LINEGAP = 158       # baseline-to-baseline
ATTR_SIZE = 40            # THE CAPABILITY AUDIT
ATTR_TRACK = 10           # letterspacing (design px added between chars)
SIG_SIZE = round(ATTR_SIZE * 0.82)   # ~82% of attribution line
SIG_TRACK = round(ATTR_TRACK * 0.82)
QUOTE_MAX_W = 1640        # wrap width for the quote block

GAP_QUOTE_RULE = 96
RULE_W = 108
RULE_H = 4
GAP_RULE_ATTR = 66
SIG_BASELINE_FRAC = 0.93  # baseline near bottom


def render_quote(filename, text):
    img, d = new_canvas(QW, QH, SAND)
    cx = (QW * SS) / 2.0

    quote_font = font(CORMORANT_MED, QUOTE_SIZE)
    attr_font = font(MONTSERRAT_SB, ATTR_SIZE)
    sig_font = font(MONTSERRAT_SB, SIG_SIZE)

    lines = wrap(d, text, quote_font, QUOTE_MAX_W * SS)

    q_ascent, q_descent = quote_font.getmetrics()
    linegap = QUOTE_LINEGAP * SS
    # visual height of the quote block: cap of first line to descent of last
    quote_block_h = (len(lines) - 1) * linegap + q_ascent + q_descent

    a_ascent, a_descent = attr_font.getmetrics()
    attr_h = a_ascent + a_descent

    total_h = (quote_block_h + GAP_QUOTE_RULE * SS + RULE_H * SS
               + GAP_RULE_ATTR * SS + attr_h)

    top = (QH * SS - total_h) / 2.0

    # --- quote lines (centered) ---
    baseline = top + q_ascent
    for ln in lines:
        d.text((cx, baseline), ln, font=quote_font, fill=NAVY, anchor="ms")
        baseline += linegap
    quote_bottom = baseline - linegap + q_descent

    # --- gold rule ---
    rule_y = quote_bottom + GAP_QUOTE_RULE * SS
    rw = RULE_W * SS
    d.rectangle([cx - rw / 2, rule_y, cx + rw / 2, rule_y + RULE_H * SS], fill=GOLD)

    # --- attribution ---
    attr_baseline = rule_y + RULE_H * SS + GAP_RULE_ATTR * SS + a_ascent
    draw_tracked(d, cx, attr_baseline, "THE CAPABILITY AUDIT", attr_font, NAVY, ATTR_TRACK)

    # --- signature footer (fixed position, independent of block) ---
    s_ascent, _ = sig_font.getmetrics()
    sig_baseline = QH * SS * SIG_BASELINE_FRAC
    draw_tracked(d, cx, sig_baseline, "TEMIDAYO AFONJA", sig_font, GOLD, SIG_TRACK)

    return finalize(img, QW, QH, os.path.join(OUT, filename))


# ---------------------------------------------------------------- teaser card
TW, TH = 2245, 1587


def render_teaser():
    img, d = new_canvas(TW, TH, SAND)
    cx = (TW * SS) / 2.0

    # --- kicker ~12% from top ---
    kicker_font = font(MONTSERRAT_SB, 34)
    k_ascent, _ = kicker_font.getmetrics()
    kicker_baseline = TH * SS * 0.12
    draw_tracked(d, cx, kicker_baseline, "TOWARD THE NEXT BOOK", kicker_font, NAVY, 12)

    # --- centered navy rectangle: ~55% width, ~45% height ---
    rw = 0.55 * TW * SS
    rh = 0.45 * TH * SS
    rcx, rcy = cx, (TH * SS) / 2.0
    d.rectangle([rcx - rw / 2, rcy - rh / 2, rcx + rw / 2, rcy + rh / 2], fill=NAVY)

    # --- DENSITY + subtitle grouped, centered in the rectangle ---
    density_font = font(CORMORANT_SB, 168)
    sub_font = font(CORMORANT_MED, 46)
    D_TRACK = 14

    d_ascent, d_descent = density_font.getmetrics()
    s_ascent, s_descent = sub_font.getmetrics()
    gap_ds = 40 * SS

    density_h = d_ascent + d_descent
    sub_h = s_ascent + s_descent
    group_h = density_h + gap_ds + sub_h
    g_top = rcy - group_h / 2.0

    density_baseline = g_top + d_ascent
    draw_tracked(d, rcx, density_baseline, "DENSITY", density_font, WHITE, D_TRACK)

    sub_baseline = density_baseline + d_descent + gap_ds + s_ascent
    d.text((rcx, sub_baseline), "The mechanism behind The Capability Audit.",
           font=sub_font, fill=GOLD, anchor="ms")

    # --- footer ~10% from bottom, two colors around a centered middle dot ---
    foot_font = font(MONTSERRAT_SB, 34)
    f_ascent, _ = foot_font.getmetrics()
    foot_baseline = TH * SS * 0.90
    F_TRACK = 8

    left = "TEMIDAYO AFONJA"
    sep = "·"  # middle dot
    right = "THE DENSITY GROUP"
    space = foot_font.getbbox(" ")  # measure a space
    space_w = d.textlength(" ", font=foot_font)

    w_left = line_width(d, left, foot_font, F_TRACK)
    w_sep = d.textlength(sep, font=foot_font)
    w_right = line_width(d, right, foot_font, F_TRACK)
    gap = space_w  # one space on each side of the dot
    total = w_left + gap + w_sep + gap + w_right

    x = cx - total / 2.0
    top = foot_baseline - f_ascent
    # left (gold), tracked
    for ch in left:
        d.text((x, top), ch, font=foot_font, fill=GOLD)
        x += d.textlength(ch, font=foot_font) + F_TRACK * SS
    x -= F_TRACK * SS  # no trailing track after last char
    x += gap
    d.text((x, top), sep, font=foot_font, fill=NAVY)
    x += w_sep + gap
    for ch in right:
        d.text((x, top), ch, font=foot_font, fill=NAVY)
        x += d.textlength(ch, font=foot_font) + F_TRACK * SS

    return finalize(img, TW, TH, os.path.join(OUT, "teaser_density.png"))


# ---------------------------------------------------------------- main
def main():
    made = []
    for fn, txt in QUOTES:
        made.append(render_quote(fn, txt))
    made.append(render_teaser())
    for p in made:
        print("wrote", os.path.relpath(p, OUT))


if __name__ == "__main__":
    main()
