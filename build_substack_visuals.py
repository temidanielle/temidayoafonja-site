#!/usr/bin/env python3
"""
Build the Capability Formation Substack visual packages for October to December 2026.

Everything is generated from scratch with Pillow, in the approved house style:
cream background, gold hairline frame, navy cards with gold tracked labels and
cream serif text, white worksheet and chart panels with a gold top line.

Fonts: Cormorant Garamond (headlines and card text), DM Sans (labels, taglines,
footnotes, footers). Both are pulled from Google Fonts if they are not cached.

Usage:  python3 build_substack_visuals.py
"""

import os
import re
import shutil
import tempfile
import zipfile
import urllib.request

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.join(HERE, "substack_visual_packages_oct_dec_2026")
FONT_DIR = os.environ.get(
    "CF_FONT_DIR",
    os.path.join(tempfile.gettempdir(), "capability_formation_fonts"),
)

# The Career Evidence Starter preview is copied through unchanged rather than
# redrawn. Point CF_STARTER_PREVIEW at it, or drop it in style_reference/.
STARTER_SOURCE = os.environ.get("CF_STARTER_PREVIEW") or os.path.join(
    HERE, "style_reference", "04_career_evidence_starter_preview.png")

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------

BG = "#F5F0E8"
NAVY = "#0F2347"
NAVY_LIGHT = "#5A6C8C"          # lighter navy, used for the 2021 bar only
GOLD = "#C9A84C"
RUST = "#C1440E"
FRAME = "#D4BE82"
GRAY = "#566379"
CREAM = "#F5F0E8"
WHITE = "#FFFFFF"
RULE = "#E0D7C4"                # light writing lines
TRACK = "#EDE7DA"               # empty part of a chart scale

S = 2                            # supersampling factor

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

GOOGLE_CSS = (
    "https://fonts.googleapis.com/css2?"
    "family=Cormorant+Garamond:wght@300;400;500;600;700"
    "&family=DM+Sans:wght@400;500;700&display=swap"
)


def ensure_fonts():
    """Download Cormorant Garamond and DM Sans from Google Fonts if missing."""
    os.makedirs(FONT_DIR, exist_ok=True)
    wanted = [
        ("CormorantGaramond", w) for w in (300, 400, 500, 600, 700)
    ] + [("DMSans", w) for w in (400, 500, 700)]
    if all(
        os.path.exists(os.path.join(FONT_DIR, "%s-%d.ttf" % (f, w)))
        for f, w in wanted
    ):
        return
    req = urllib.request.Request(GOOGLE_CSS, headers={"User-Agent": "Mozilla/5.0"})
    css = urllib.request.urlopen(req).read().decode("utf-8")
    for block in css.split("@font-face")[1:]:
        fam = re.search(r"font-family: '([^']+)'", block).group(1).replace(" ", "")
        weight = re.search(r"font-weight: (\d+)", block).group(1)
        url = re.search(r"url\((https[^)]+)\)", block).group(1)
        target = os.path.join(FONT_DIR, "%s-%s.ttf" % (fam, weight))
        if not os.path.exists(target):
            urllib.request.urlretrieve(url, target)


_FONT_CACHE = {}


def serif(size, weight=400):
    return _font("CormorantGaramond", weight, size)


def sans(size, weight=500):
    return _font("DMSans", weight, size)


def _font(family, weight, size):
    key = (family, weight, round(size * S))
    if key not in _FONT_CACHE:
        path = os.path.join(FONT_DIR, "%s-%d.ttf" % (family, weight))
        _FONT_CACHE[key] = ImageFont.truetype(path, round(size * S))
    return _FONT_CACHE[key]


# ---------------------------------------------------------------------------
# Canvas: every coordinate below is in final pixels; drawing happens at S times
# that size and the page is resampled down at the end.
# ---------------------------------------------------------------------------


class Canvas(object):
    def __init__(self, w, h, bg=BG):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w * S, h * S), bg)
        self.d = ImageDraw.Draw(self.im)

    # -- primitives ---------------------------------------------------------

    def rect(self, box, fill=None, outline=None, width=1):
        x0, y0, x1, y1 = [v * S for v in box]
        self.d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline,
                         width=max(1, round(width * S)))

    def rrect(self, box, radius, fill=None, outline=None, width=1):
        x0, y0, x1, y1 = [v * S for v in box]
        self.d.rounded_rectangle([x0, y0, x1, y1], radius=radius * S, fill=fill,
                                 outline=outline, width=max(1, round(width * S)))

    def line(self, p0, p1, fill, width=1):
        self.d.line([p0[0] * S, p0[1] * S, p1[0] * S, p1[1] * S], fill=fill,
                    width=max(1, round(width * S)))

    def dashed(self, p0, p1, fill, width=2, dash=10, gap=8):
        (x0, y0), (x1, y1) = p0, p1
        dx, dy = x1 - x0, y1 - y0
        length = (dx * dx + dy * dy) ** 0.5
        if length == 0:
            return
        ux, uy = dx / length, dy / length
        pos = 0.0
        while pos < length:
            end = min(pos + dash, length)
            self.line((x0 + ux * pos, y0 + uy * pos),
                      (x0 + ux * end, y0 + uy * end), fill, width)
            pos = end + gap

    def circle(self, cx, cy, r, fill):
        self.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
                       fill=fill)

    # -- text ---------------------------------------------------------------

    def measure(self, text, font, tracking=0.0):
        if not text:
            return 0.0
        w = self.d.textlength(text, font=font) / S
        if tracking:
            w += tracking * (len(text) - 1)
        return w

    def text(self, x, cy, text, font, fill, tracking=0.0, align="left"):
        """Draw one line. `cy` is the vertical center of the line slot.
        `align` is left, center or right, applied to `x`."""
        if not text:
            return
        total = self.measure(text, font, tracking)
        if align == "center":
            x = x - total / 2.0
        elif align == "right":
            x = x - total
        if not tracking:
            self.d.text((x * S, cy * S), text, font=font, fill=fill, anchor="lm")
            return
        pen = x
        for ch in text:
            self.d.text((pen * S, cy * S), ch, font=font, fill=fill, anchor="lm")
            pen += self.d.textlength(ch, font=font) / S + tracking

    # -- wrapping -----------------------------------------------------------

    def wrap(self, text, font, max_w, tracking=0.0):
        words, lines, cur = text.split(), [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if cur and self.measure(trial, font, tracking) > max_w:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        if cur:
            lines.append(cur)
        return lines

    def wrap_balanced(self, text, font, max_w, tracking=0.0):
        """Greedy wrap for the line count, then even out the line widths."""
        n = len(self.wrap(text, font, max_w, tracking))
        if n <= 1:
            return [text]
        words = text.split()
        widths = [self.measure(w, font, tracking) for w in words]
        space = self.measure("  ", font, tracking) - self.measure(" ", font, tracking)
        space = self.measure("n n", font, tracking) - self.measure("nn", font, tracking)

        def line_w(i, j):
            return sum(widths[i:j]) + space * (j - i - 1)

        big = float("inf")
        best = {}

        def solve(i, lines_left):
            if lines_left == 0:
                return (0.0 if i == len(words) else big), []
            if (i, lines_left) in best:
                return best[(i, lines_left)]
            out = (big, [])
            for j in range(i + 1, len(words) + 1):
                w = line_w(i, j)
                if w > max_w and j > i + 1:
                    break
                rest_cost, rest = solve(j, lines_left - 1)
                if rest_cost == big:
                    continue
                cost = rest_cost + (max_w - w) ** 2
                if cost < out[0]:
                    out = (cost, [" ".join(words[i:j])] + rest)
            best[(i, lines_left)] = out
            return out

        cost, lines = solve(0, n)
        return lines if lines else self.wrap(text, font, max_w, tracking)

    # -- output -------------------------------------------------------------

    def save(self, path):
        img = self.im.resize((self.w, self.h), Image.LANCZOS)
        img.save(path)
        return path


def frame(c):
    """Thin 1 px gold frame, 26 px inside the edge."""
    c.rect((26, 26, c.w - 27, c.h - 27), outline=FRAME, width=1)


# ---------------------------------------------------------------------------
# Shared page furniture
# ---------------------------------------------------------------------------

PAGE_W, BODY_H, COVER_H = 1600, 1000, 900
MARGIN = 108                      # left and right margin for card rows
INNER_W = PAGE_W - 2 * MARGIN     # 1384

HEAD_SIZE = 56
HEAD_TOP = 112
HEAD_ADV = 72
DIV_W, DIV_H = 112, 4
FOOT_CY = 922
CONTENT_BOTTOM = 868
GRID_BOTTOM = 880


def headline_block(c, text, top=HEAD_TOP):
    """Navy uppercase serif headline plus the short rust divider.
    Returns the y at which content may begin."""
    font = serif(HEAD_SIZE, 500)
    lines = c.wrap_balanced(text.upper(), font, 1400, tracking=1.2)
    cy = top + 31
    for ln in lines:
        c.text(PAGE_W / 2, cy, ln, font, NAVY, tracking=1.2, align="center")
        cy += HEAD_ADV
    div_y = top + 62 + (len(lines) - 1) * HEAD_ADV + 38
    c.rect((PAGE_W / 2 - DIV_W / 2, div_y, PAGE_W / 2 + DIV_W / 2, div_y + DIV_H),
           fill=RUST)
    return div_y + DIV_H


def subline(c, y, text, kind="gray"):
    """One line under the divider. Returns the y at which content may begin."""
    if kind == "gray":
        font, fill, cy = sans(24, 400), GRAY, y + 40
    else:
        font, fill, cy = serif(34, 400), NAVY, y + 44
    c.text(PAGE_W / 2, cy, text, font, fill, align="center")
    return cy + 26


def footnote(c, text, cy=FOOT_CY):
    font = sans(24, 400)
    lines = c.wrap(text, font, 1300)
    cy = cy - (len(lines) - 1) * 15
    for ln in lines:
        c.text(PAGE_W / 2, cy, ln, font, GRAY, align="center")
        cy += 30


def source_note(c, text, cy=None):
    font = sans(20, 400)
    lines = c.wrap(text, font, 1320)
    cy = (cy if cy is not None else 920) - (len(lines) - 1) * 14
    for ln in lines:
        c.text(PAGE_W / 2, cy, ln, font, GRAY, align="center")
        cy += 28


# ---------------------------------------------------------------------------
# Cards
# ---------------------------------------------------------------------------

CARD_R = 18
RULE_STEP = 42.0
LABEL_SIZE = 22
LABEL_TRACK = 3.0


def card_pad(w):
    return 48 if w >= 560 else 36


def _body_lines(c, items, font, inner_w):
    """items is a list of strings; returns a list of lists of wrapped lines."""
    return [c.wrap(it, font, inner_w) for it in items]


def measure_card(c, items, w, size, kind, label_lines=1, writing=0):
    pad = card_pad(w)
    font = serif(size, 400)
    wrapped = _body_lines(c, items, font, w - 2 * pad)
    adv = round(size * 1.30)
    gap = round(size * 0.44)
    body = sum(len(g) * adv for g in wrapped) + gap * (len(wrapped) - 1)
    head = (52 + (label_lines - 1) * 28 + 56 if kind == "navy"
            else 42 + (label_lines - 1) * 26 + 44)
    tail = pad + (30 + RULE_STEP * (writing - 1) if writing else 0)
    return head + body + tail


def draw_card(c, box, label, items, size, kind, writing=0, label_color=None):
    x0, y0, x1, y1 = box
    w = x1 - x0
    pad = card_pad(w)
    if kind == "navy":
        c.rrect(box, CARD_R, fill=NAVY)
        lab_fill = label_color or GOLD
        body_fill = CREAM
        lab_y = y0 + 52
        body_top = y0 + 52 + 56
    else:
        c.rrect(box, CARD_R, fill=WHITE)
        c.rect((x0 + CARD_R, y0, x1 - CARD_R, y0 + 3), fill=GOLD)
        lab_fill = label_color or NAVY
        body_fill = NAVY
        lab_y = y0 + 42
        body_top = y0 + 42 + 44
    lab_font = sans(LABEL_SIZE, 700)
    lab_lines = c.wrap(label.upper(), lab_font, w - 2 * pad, tracking=LABEL_TRACK)
    ly = lab_y
    for ln in lab_lines:
        c.text(x0 + pad, ly, ln, lab_font, lab_fill, tracking=LABEL_TRACK)
        ly += 28
    body_top += (len(lab_lines) - 1) * 28

    font = serif(size, 400)
    adv = round(size * 1.30)
    gap = round(size * 0.44)
    cy = body_top + adv / 2.0
    for idx, item in enumerate(items):
        for ln in c.wrap(item, font, w - 2 * pad):
            c.text(x0 + pad, cy, ln, font, body_fill)
            cy += adv
        if idx != len(items) - 1:
            cy += gap
    if writing:
        # The card was measured with room for exactly this many rules, so a
        # band anchored to the bottom can never run into the prompt above it.
        step = RULE_STEP
        wy = (y1 - pad) - step * (writing - 1)
        for _ in range(writing):
            c.line((x0 + pad, wy), (x1 - pad, wy), RULE, width=1)
            wy += step


def fit_writing(c, groups, w, avail_h, size, kind, writing):
    """Most writing lines, up to `writing`, that every card in the set can hold.
    Keeps one image's worksheet cards ruled identically."""
    for n in range(writing, 0, -1):
        ok = True
        for lab, items in groups:
            lab_lines = len(c.wrap(lab.upper(), sans(LABEL_SIZE, 700),
                                   w - 2 * card_pad(w), LABEL_TRACK))
            if measure_card(c, items, w, size, kind, label_lines=lab_lines,
                            writing=n) > avail_h:
                ok = False
                break
        if ok:
            return n
    return 1


def fit_size(c, groups, w, avail_h, hi=44, lo=34, kind="navy", writing=0):
    """Largest body size from hi down to lo at which every card fits avail_h."""
    for size in range(hi, lo - 1, -2):
        heights = [
            measure_card(c, items, w, size, kind,
                         label_lines=len(c.wrap(lab.upper(), sans(LABEL_SIZE, 700),
                                                w - 2 * card_pad(w), LABEL_TRACK)),
                         writing=writing)
            for lab, items in groups
        ]
        if max(heights) <= avail_h:
            return size, max(heights)
    heights = [
        measure_card(c, items, w, lo, kind,
                     label_lines=len(c.wrap(lab.upper(), sans(LABEL_SIZE, 700),
                                            w - 2 * card_pad(w), LABEL_TRACK)),
                     writing=writing)
        for lab, items in groups
    ]
    return lo, max(heights)


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------


def build_cover(title, tagline, path):
    c = Canvas(PAGE_W, COVER_H)
    frame(c)
    cx = PAGE_W / 2
    card = (211, 142, 1389, 755)
    c.rrect(card, 26, fill=NAVY)

    inner_w = (card[2] - card[0]) - 2 * 95
    chosen, lines = None, None
    for size in range(104, 63, -2):
        f = serif(size, 400)
        ls = c.wrap_balanced(title, f, inner_w)
        if len(ls) > 4:
            continue
        adv = round(size * 1.16)
        block = 62 + 4 + 48 + 30 + len(ls) * adv
        if block <= (card[3] - card[1]) - 2 * 56:
            chosen, lines = size, ls
            break
    if chosen is None:
        chosen = 64
        lines = c.wrap_balanced(title, serif(64, 400), inner_w)

    font = serif(chosen, 400)
    adv = round(chosen * 1.16)
    # Centre on what the eye sees: the cap line of the first title line down to
    # the baseline of the tagline, not on the notional line boxes.
    ink_top = adv / 2.0 - chosen * 0.66
    ink_bottom = len(lines) * adv + 58 + DIV_H + 48 + 17
    top = card[1] + ((card[3] - card[1]) - (ink_bottom - ink_top)) / 2.0 - ink_top

    cy = top + adv / 2.0
    for ln in lines:
        c.text(cx, cy, ln, font, CREAM, align="center")
        cy += adv
    div_y = top + len(lines) * adv + 58
    c.rect((cx - DIV_W / 2, div_y, cx + DIV_W / 2, div_y + DIV_H), fill=RUST)

    # The tagline keeps its tracking but steps down a little if a long one
    # would crowd the edges of the card.
    tag_size, tag_track = 26, 4.0
    limit = (card[2] - card[0]) - 2 * 78
    while tag_size > 20 and c.measure(tagline, sans(tag_size, 700), tag_track) > limit:
        tag_size -= 1
        tag_track = max(2.6, tag_track - 0.15)
    c.text(cx, div_y + DIV_H + 48, tagline, sans(tag_size, 700), GOLD,
           tracking=tag_track, align="center")

    c.text(cx, 829, "CAPABILITY FORMATION · TEMIDAYO AFONJA", sans(20, 700),
           NAVY, tracking=3.0, align="center")
    return c.save(path), chosen, len(lines)


def build_row_cards(headline, cards, foot, path, kind="navy", writing=0,
                    gap=None, hi=44):
    """N cards in a single row, each `(label, [body items])`."""
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, headline)
    y0 = top + 62
    n = len(cards)
    gap = gap if gap is not None else (36 if n <= 2 else 24)
    w = (INNER_W - gap * (n - 1)) / float(n)
    avail = CONTENT_BOTTOM - y0
    size, need = fit_size(c, cards, w, avail, hi=hi, lo=34, kind=kind,
                          writing=writing)
    h = min(avail, max(need, avail * 0.82))
    if writing:
        writing = fit_writing(c, cards, w, h, size, kind, writing)
    y_top = y0
    for i, (label, items) in enumerate(cards):
        x = MARGIN + i * (w + gap)
        draw_card(c, (x, y_top, x + w, y_top + h), label, items, size, kind,
                  writing=writing)
    footnote(c, foot)
    return c.save(path), size


def build_split(headline, left, right, foot, path):
    """White card on the left, navy card on the right."""
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, headline)
    y0 = top + 62
    gap = 36
    w = (INNER_W - gap) / 2.0
    avail = CONTENT_BOTTOM - y0
    s_left, h_left = fit_size(c, [left], w, avail, hi=42, lo=34, kind="white")
    s_right, h_right = fit_size(c, [right], w, avail, hi=42, lo=34, kind="navy")
    size = min(s_left, s_right)
    h_left = measure_card(c, left[1], w, size, "white")
    h_right = measure_card(c, right[1], w, size, "navy")
    h = min(avail, max(h_left, h_right, avail * 0.82))
    y_top = y0
    draw_card(c, (MARGIN, y_top, MARGIN + w, y_top + h), left[0], left[1], size,
              "white")
    draw_card(c, (MARGIN + w + gap, y_top, MARGIN + 2 * w + gap, y_top + h),
              right[0], right[1], size, "navy")
    footnote(c, foot)
    return c.save(path), size


def build_grid(headline, cards, foot, path, kind="white", writing=0, sub=None):
    """Four cards in a 2 x 2 grid."""
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, headline, top=104)
    if sub:
        top = subline(c, top, sub, "gray")
        y0 = top + 40
    else:
        y0 = top + 56
    gap_x, gap_y = 36, 24
    w = (INNER_W - gap_x) / 2.0
    avail = GRID_BOTTOM - y0
    h = (avail - gap_y) / 2.0
    size, need = fit_size(c, cards, w, h, hi=40, lo=34, kind=kind, writing=writing)
    if writing:
        writing = fit_writing(c, cards, w, h, size, kind, writing)
    for i, (label, items) in enumerate(cards):
        x = MARGIN + (i % 2) * (w + gap_x)
        y = y0 + (i // 2) * (h + gap_y)
        draw_card(c, (x, y, x + w, y + h), label, items, size, kind,
                  writing=writing)
    footnote(c, foot)
    return c.save(path), size


# ---------------------------------------------------------------------------
# The three data graphics and the org chart
# ---------------------------------------------------------------------------


def org_box(c, box, fill=None, outline=NAVY, width=2):
    c.rrect(box, 4, fill=fill, outline=outline, width=width)


def build_org_chart_page(path):
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, "WHERE THE WORK SITS. WHERE THE HARD CALLS SIT.")
    gap = 36
    w = (INNER_W - gap) / 2.0
    h = 466
    y0 = top + 52 + max(0.0, (CONTENT_BOTTOM - (top + 52) - h) / 2.0)

    for side in (0, 1):
        px = MARGIN + side * (w + gap)
        c.rrect((px, y0, px + w, y0 + h), CARD_R, fill=WHITE)
        c.rect((px + CARD_R, y0, px + w - CARD_R, y0 + 3), fill=GOLD)
        label = "WHERE THE WORK SITS" if side == 0 else "WHERE THE HARD CALLS SIT"
        c.text(px + 44, y0 + 46, label, sans(LABEL_SIZE, 700), NAVY,
               tracking=LABEL_TRACK)

        cx = px + w / 2.0
        lead = (cx - 76, y0 + 104, cx + 76, y0 + 152)
        org_box(c, lead)

        mgr_y0, mgr_y1 = y0 + 214, y0 + 262
        mgr_w = 130
        inset = 52
        step = (w - 2 * inset) / 3.0
        mgr_cx = [px + inset + step * (i + 0.5) for i in range(3)]
        for mx in mgr_cx:
            org_box(c, (mx - mgr_w / 2, mgr_y0, mx + mgr_w / 2, mgr_y1))
        bus = y0 + 183
        c.line((cx, lead[3]), (cx, bus), NAVY, 2)
        c.line((mgr_cx[0], bus), (mgr_cx[2], bus), NAVY, 2)
        for mx in mgr_cx:
            c.line((mx, bus), (mx, mgr_y0), NAVY, 2)

        team_y0, team_y1 = y0 + 324, y0 + 372
        tw, tgap = 76, 16
        bus2 = y0 + 293
        boxes = []
        for i, mx in enumerate(mgr_cx):
            left = mx - (tw + tgap / 2.0)
            centers = [left + tw / 2.0, left + tw + tgap + tw / 2.0]
            c.line((mx, mgr_y1), (mx, bus2), NAVY, 2)
            c.line((centers[0], bus2), (centers[1], bus2), NAVY, 2)
            for tx in centers:
                c.line((tx, bus2), (tx, team_y0), NAVY, 2)
                boxes.append((tx, (tx - tw / 2, team_y0, tx + tw / 2, team_y1)))
        highlight = {0: [], 1: [0, 4]}[side]
        for idx, (tx, box) in enumerate(boxes):
            if idx in highlight:
                org_box(c, box, fill=GOLD, outline=GOLD, width=2)
            else:
                org_box(c, box)

        if side == 1:
            mid = mgr_cx[1]
            for idx, caption in ((0, "Long-tenured expert"), (4, "Informal co-carrier")):
                tx, box = boxes[idx]
                c.dashed((tx, box[1] - 4), (mid, mgr_y1 + 6), GOLD, width=2,
                         dash=9, gap=7)
                cap_font = sans(18, 500)
                for j, ln in enumerate(c.wrap(caption, cap_font, 150)):
                    c.text(tx, team_y1 + 26 + j * 24, ln, cap_font, NAVY,
                           align="center")

    footnote(c, "The org chart shows ownership. The hard calls often follow experience.")
    return c.save(path)


def build_dot_grid(path):
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, "FEWER THAN 1 IN 700.", top=100)
    y = subline(c, top,
                "hires in 2023 reflected added opportunity from employers "
                "dropping degree requirements.", "navy")

    cols, rows = 35, 20
    cell = 21.5
    grid_w, grid_h = cols * cell, rows * cell
    panel_pad = 48
    pw, ph = grid_w + 2 * panel_pad, grid_h + 2 * panel_pad
    px = (PAGE_W - pw) / 2.0
    py = y + 34
    c.rrect((px, py, px + pw, py + ph), CARD_R, fill=WHITE)
    c.rect((px + CARD_R, py, px + pw - CARD_R, py + 3), fill=GOLD)

    faint = blend(NAVY, WHITE, 0.25)
    gold_index = (7 * cols) + 18            # row 8, column 19: not a corner
    n = 0
    for r in range(rows):
        for col in range(cols):
            cx = px + panel_pad + cell * (col + 0.5)
            cy = py + panel_pad + cell * (r + 0.5)
            if n == gold_index:
                c.circle(cx, cy, 8.8, GOLD)
            else:
                c.circle(cx, cy, 7.0, faint)
            n += 1
    assert n == 700

    source_note(c,
                "Source: Sigelman, Fuller and Martin, Skills-Based Hiring: "
                "The Long Road from Pronouncements to Practice, Burning Glass "
                "Institute and Harvard Business School, February 2024.",
                cy=916)
    return c.save(path), n


def blend(fg, bg, alpha):
    def rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    f, b = rgb(fg), rgb(bg)
    return tuple(round(f[i] * alpha + b[i] * (1 - alpha)) for i in range(3))


def build_hbars(path):
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c, "AI USE IS OUTPACING AI TRAINING.")
    pw = 1240
    px = (PAGE_W - pw) / 2.0
    ph = 500
    py = top + 62 + max(0.0, (CONTENT_BOTTOM - (top + 62) - ph) / 2.0)
    c.rrect((px, py, px + pw, py + ph), CARD_R, fill=WHITE)
    c.rect((px + CARD_R, py, px + pw - CARD_R, py + 3), fill=GOLD)

    pad = 62
    x0 = px + pad
    scale = pw - 2 * pad - 96          # room for the value at the end
    series = [
        ("Regularly use AI", 55, NAVY),
        ("Took part in employer-provided AI training in the past six months",
         33, GOLD),
    ]
    bar_h = 54
    row_top = py + 92
    for label, value, color in series:
        c.text(x0, row_top, label, sans(28, 500), NAVY)
        by = row_top + 34
        c.rect((x0, by, x0 + scale, by + bar_h), fill=TRACK)
        c.rect((x0, by, x0 + scale * value / 100.0, by + bar_h), fill=color)
        c.text(x0 + scale * value / 100.0 + 22, by + bar_h / 2.0, "%d%%" % value,
               sans(34, 700), NAVY)
        row_top = by + bar_h + 112

    axis_y = py + ph - 62
    c.line((x0, axis_y), (x0 + scale, axis_y), FRAME, 1)
    for tick in (0, 25, 50, 75, 100):
        tx = x0 + scale * tick / 100.0
        c.line((tx, axis_y), (tx, axis_y + 8), FRAME, 1)
        c.text(tx, axis_y + 28, "%d%%" % tick, sans(18, 400), GRAY, align="center")

    source_note(c, "Source: The Conference Board, July 2026. Global survey of "
                   "nearly 1,300 workers.", cy=906)
    return c.save(path)


def build_vbars(path):
    c = Canvas(PAGE_W, BODY_H)
    frame(c)
    top = headline_block(c,
                         "CREDENTIALS ARE USED MORE. THEIR QUALITY IS STILL "
                         "HARD TO JUDGE.", top=104)
    py = top + 54
    pw = 1300
    px = (PAGE_W - pw) / 2.0
    ph = 480
    c.rrect((px, py, px + pw, py + ph), CARD_R, fill=WHITE)
    c.rect((px + CARD_R, py, px + pw - CARD_R, py + 3), fill=GOLD)

    base = py + ph - 154
    plot_h = 274                      # 100% on one shared scale
    lighter = blend(NAVY, WHITE, 0.62)

    groups = [
        ("HR professionals who use skilled credentials in hiring",
         [("2021", 72, lighter), ("2025", 78, NAVY)]),
        ("Say skill quality from credentials is too hard to judge (2025)",
         [("HR professionals", 24, GOLD), ("Supervisors", 33, GOLD)]),
    ]

    # faint gridlines across the shared scale
    for tick in (0, 25, 50, 75, 100):
        gy = base - plot_h * tick / 100.0
        c.line((px + 70, gy), (px + pw - 70, gy), TRACK if tick else FRAME, 1)
        c.text(px + 56, gy, "%d%%" % tick, sans(17, 400), GRAY, align="right")

    bar_w, inner_gap = 116, 56
    group_w = 2 * bar_w + inner_gap
    centers = [px + pw * 0.31, px + pw * 0.73]
    for (gtitle, bars), gcx in zip(groups, centers):
        left = gcx - group_w / 2.0
        for i, (blabel, value, color) in enumerate(bars):
            bx = left + i * (bar_w + inner_gap)
            bh = plot_h * value / 100.0
            c.rect((bx, base - bh, bx + bar_w, base), fill=color)
            c.text(bx + bar_w / 2.0, base - bh - 26, "%d%%" % value,
                   sans(30, 700), NAVY, align="center")
            c.text(bx + bar_w / 2.0, base + 28, blabel, sans(20, 500), NAVY,
                   align="center")
        gfont = sans(21, 400)
        gy = base + 72
        for ln in c.wrap(gtitle, gfont, group_w + 150):
            c.text(gcx, gy, ln, gfont, GRAY, align="center")
            gy += 28
    c.line((px + 70, base), (px + pw - 70, base), NAVY, 1)

    source_note(c, "Source: SHRM, The Skills-First Movement: Redefining How "
                   "Organizations Hire and Grow, 2026 (surveyed 2025).", cy=902)
    return c.save(path)


# ---------------------------------------------------------------------------
# Package sheets
# ---------------------------------------------------------------------------

SHEET_W = 1240
SHEET_MARGIN = 53
SHEET_IMG_W = SHEET_W - 2 * SHEET_MARGIN


def build_package_sheet(title, subtitle, entries, path):
    """entries: list of (image path, file name, caption)."""
    thumbs = []
    for src, name, caption in entries:
        im = Image.open(src)
        h = round(SHEET_IMG_W * im.height / float(im.width))
        thumbs.append((im.resize((SHEET_IMG_W, h), Image.LANCZOS), name,
                       "%d x %d" % im.size, caption))

    top = 132
    total = top + sum(t[0].height + 62 for t in thumbs) + 10
    sheet = Image.new("RGB", (SHEET_W, total), WHITE)
    d = ImageDraw.Draw(sheet)

    t_font = ImageFont.truetype(os.path.join(FONT_DIR, "DMSans-700.ttf"), 22)
    s_font = ImageFont.truetype(os.path.join(FONT_DIR, "DMSans-400.ttf"), 14)
    n_font = ImageFont.truetype(os.path.join(FONT_DIR, "DMSans-700.ttf"), 13)
    c_font = ImageFont.truetype(os.path.join(FONT_DIR, "DMSans-400.ttf"), 13)

    d.text((SHEET_MARGIN, 56), title, font=t_font, fill=NAVY, anchor="lm")
    d.text((SHEET_MARGIN, 88), subtitle, font=s_font, fill=GRAY, anchor="lm")

    y = top
    for im, name, size, caption in thumbs:
        sheet.paste(im, (SHEET_MARGIN, y))
        cy = y + im.height + 28
        d.text((SHEET_MARGIN, cy), name, font=n_font, fill=NAVY, anchor="lm")
        x = SHEET_MARGIN + d.textlength(name, font=n_font)
        tail = "   ·   %s   ·   %s" % (size, caption)
        d.text((x, cy), tail, font=c_font, fill=GRAY, anchor="lm")
        y = cy + 34
    sheet.save(path)
    return path


# ---------------------------------------------------------------------------
# Copy for every image
# ---------------------------------------------------------------------------

COVERS = {
    "2026-10-06": ("How to Find the Value You Can Carry When Your Work Is "
                   "Company-Specific",
                   "WHAT MOVED · WHAT STAYED · WHAT YOU CARRY"),
    "2026-10-20": ("If Your Work Is Being Reorganized, Ask These 4 Questions "
                   "Before It Moves",
                   "THE HARD CALLS · WHO CARRIES THEM · "
                   "WHAT STAYS REACHABLE"),
    "2026-11-10": ("How to Tell Which Parts of Your Experience Another "
                   "Employer Will Count",
                   "WHAT TRAVELS · WHAT YOU CAN PROVE · "
                   "WHAT YOU RELEARN"),
    "2026-11-17": ("How to Keep Building Judgment When AI Starts Doing the "
                   "Work You Learned From",
                   "WHAT AI REMOVES · WHAT IT TAUGHT · "
                   "WHAT TO REBUILD"),
    "2026-12-01": ("Before You Get Another Credential, Find Out What the "
                   "Employer Still Needs to Believe",
                   "THE TRUST QUESTION · THE CREDENTIAL’S JOB · "
                   "THE EXPERIENCE GAP"),
}

ESSAY_TITLES = {
    "2026-10-06": "How to Find the Value You Can Carry When Your Work Is Company-Specific",
    "2026-10-20": "If Your Work Is Being Reorganized, Ask These 4 Questions Before It Moves",
    "2026-11-10": "How to Tell Which Parts of Your Experience Another Employer Will Count",
    "2026-11-17": "How to Keep Building Judgment When AI Starts Doing the Work You Learned From",
    "2026-12-01": "Before You Get Another Credential, Find Out What the Employer Still Needs to Believe",
}

LONG_DATE = {
    "2026-10-06": "October 6, 2026",
    "2026-10-20": "October 20, 2026",
    "2026-11-10": "November 10, 2026",
    "2026-11-17": "November 17, 2026",
    "2026-12-01": "December 1, 2026",
}

COVER_CAPTION = "cover and social preview only"
BODY_CAPTION = "in body"


def main():
    ensure_fonts()
    if os.path.isdir(OUT_ROOT):
        shutil.rmtree(OUT_ROOT)
    made = {}

    def folder(date):
        p = os.path.join(OUT_ROOT, date)
        os.makedirs(p, exist_ok=True)
        return p

    notes = []

    # ---------------- OCT 6 ----------------
    d = folder("2026-10-06")
    oct6 = []
    p, size, nl = build_cover(*COVERS["2026-10-06"],
                              path=os.path.join(d, "capability_formation_cover_2026-10-06.png"))
    notes.append(("cover 2026-10-06", "title %d px over %d lines" % (size, nl)))
    oct6.append((p, os.path.basename(p), COVER_CAPTION))

    p, s = build_row_cards(
        "THE WORK MOVED. THE KNOW-HOW DID NOT.",
        [("WHAT MOVES IN A HANDOFF",
          ["Tasks", "Access", "Ownership", "Systems", "Reporting lines"]),
         ("WHAT CAN STAY WITH ONE PERSON",
          ["Which signal deserves a second look",
           "Why an exception exists",
           "Which local habit only looks like a requirement",
           "Which relationship needs different handling"])],
        "A handoff can be complete on paper and still leave the know-how in one place.",
        os.path.join(d, "capability_formation_work_moved_know_how_didn_t.png"),
        kind="navy", hi=44)
    notes.append(("work moved / know-how", "card text %d px" % s))
    oct6.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_split(
        "LIGHT HANDOFF OR DEEPER TRANSFER?",
        ("A LIGHT HANDOFF IS USUALLY ENOUGH WHEN",
         ["The work is standardized",
          "Mistakes are low-consequence",
          "Exceptions are easy to escalate"]),
        ("PLAN A DEEPER TRANSFER WHEN",
         ["The difficult cases are consequential",
          "History changes the answer",
          "Only a few people can resolve exceptions",
          "Relationships shape the outcome",
          "The experienced person will be hard to reach"]),
        "Most transitions can stay light. The skill is knowing where a light handoff is safe.",
        os.path.join(d, "capability_formation_oct06_graphic_a_light_handoff_or_deeper_transfer.png"))
    notes.append(("light handoff or deeper transfer", "card text %d px" % s))
    oct6.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_grid(
        "BEFORE THE HANDOFF CLOSES.",
        [("01", ["If the difficult version of this work arrived next month, "
                 "who besides you could handle it?"]),
         ("02", ["What do you know that the process document does not show?"]),
         ("03", ["Who is practicing that now?"]),
         ("04", ["What context or relationship needs to stay reachable after "
                 "the move?"])],
        "Answer these while the experienced person is still here.",
        os.path.join(d, "capability_formation_oct06_graphic_b_before_the_handoff_closes.png"),
        kind="white", writing=2)
    notes.append(("before the handoff closes", "prompt text %d px" % s))
    oct6.append((p, os.path.basename(p), BODY_CAPTION))
    made["2026-10-06"] = oct6

    # ---------------- OCT 20 ----------------
    d = folder("2026-10-20")
    oct20 = []
    p, size, nl = build_cover(*COVERS["2026-10-20"],
                              path=os.path.join(d, "capability_formation_cover_2026-10-20.png"))
    notes.append(("cover 2026-10-20", "title %d px over %d lines" % (size, nl)))
    oct20.append((p, os.path.basename(p), COVER_CAPTION))

    p = build_org_chart_page(
        os.path.join(d, "capability_formation_oct20_graphic_a_where_the_work_sits.png"))
    oct20.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_row_cards(
        "FOUR QUESTIONS BEFORE YOUR WORK MOVES.",
        [("01", ["Which important decisions are moving?"]),
         ("02", ["Who carries the hard calls today?"]),
         ("03", ["What evidence says someone else can carry them?"]),
         ("04", ["What must stay reachable after the move?"])],
        "Ask them before the boxes around your work are final.",
        os.path.join(d, "capability_formation_oct20_image_1_four_questions_before_your_work_moves.png"),
        kind="navy", gap=22, hi=40)
    notes.append(("four questions before your work moves", "card text %d px" % s))
    oct20.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_grid(
        "ONE DECISION, FOUR QUESTIONS.",
        [("WHICH DECISIONS ARE MOVING?",
          ["Approving service exceptions, requiring specialist review, and "
           "customer concessions that set precedent"]),
         ("WHO CARRIES THE HARD CALLS?",
          ["Two central experts carry most ambiguous cases and the history "
           "behind past exceptions"]),
         ("WHAT EVIDENCE SAYS SOMEONE ELSE CAN?",
          ["Several managers have watched these decisions. Few have owned "
           "the trade-offs."]),
         ("WHAT MUST STAY REACHABLE?",
          ["A dual-carrier period, an exception review, and one escalation "
           "route for high-consequence cases"])],
        "The move can still go ahead. Leadership now knows what rests on evidence.",
        os.path.join(d, "capability_formation_oct20_graphic_b_worked_example_escalation.png"),
        kind="white", writing=0,
        sub="An illustrative composite: customer escalation authority moves to "
            "business-unit managers.")
    notes.append(("one decision, four questions", "card text %d px" % s))
    oct20.append((p, os.path.basename(p), BODY_CAPTION))
    made["2026-10-20"] = oct20

    # ---------------- NOV 10 ----------------
    d = folder("2026-11-10")
    nov10 = []
    p, size, nl = build_cover(*COVERS["2026-11-10"],
                              path=os.path.join(d, "capability_formation_cover_2026-11-10.png"))
    notes.append(("cover 2026-11-10", "title %d px over %d lines" % (size, nl)))
    nov10.append((p, os.path.basename(p), COVER_CAPTION))

    p, dots = build_dot_grid(
        os.path.join(d, "capability_formation_nov10_graphic_a_1_in_700_hires.png"))
    notes.append(("1 in 700 hires", "%d circles drawn, one gold" % dots))
    nov10.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_row_cards(
        "WHAT THE OTHER SIDE NEEDS TO SEE.",
        [("A COMPARABLE PROBLEM", ["Have you handled something like this before?"]),
         ("YOUR JUDGMENT", ["What did you decide, and why?"]),
         ("EVIDENCE", ["What can someone who was not there inspect?"]),
         ("THE REAL GAP", ["Where does your experience stop?"])],
        "Specific proof does the work that familiarity used to do.",
        os.path.join(d, "capability_formation_what_the_other_side_needs_to_see.png"),
        kind="navy", gap=22, hi=40)
    notes.append(("what the other side needs to see", "card text %d px" % s))
    nov10.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_grid(
        "A ONE-EXPERIENCE READ.",
        [("WHAT TRAVELS?", ["What judgment or problem-solving would still "
                            "matter elsewhere?"]),
         ("WHAT DOES NOT?", ["What depended on this company, industry or "
                             "relationship?"]),
         ("WHAT CAN I PROVE?", ["What evidence could someone who was not "
                                "there inspect?"]),
         ("WHAT MUST I RELEARN?", ["What will the next context make me earn "
                                   "again?"])],
        "Take one piece of work from the last year.",
        os.path.join(d, "capability_formation_nov10_graphic_b_one_experience_read.png"),
        kind="white", writing=2)
    notes.append(("a one-experience read", "prompt text %d px" % s))
    nov10.append((p, os.path.basename(p), BODY_CAPTION))
    made["2026-11-10"] = nov10

    # ---------------- NOV 17 ----------------
    d = folder("2026-11-17")
    nov17 = []
    p, size, nl = build_cover(*COVERS["2026-11-17"],
                              path=os.path.join(d, "capability_formation_cover_2026-11-17.png"))
    notes.append(("cover 2026-11-17", "title %d px over %d lines" % (size, nl)))
    nov17.append((p, os.path.basename(p), COVER_CAPTION))

    p = build_hbars(
        os.path.join(d, "capability_formation_nov17_graphic_a_ai_use_vs_training.png"))
    nov17.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_split(
        "AUTOMATE THE TASK. REBUILD THE PRACTICE.",
        ("WHEN AI REMOVES THE TASK",
         ["Faster output", "Fewer routine steps",
          "Less time on the common case"]),
        ("REBUILD WHAT IT TAUGHT",
         ["Exposure to unusual cases",
          "Reasoning explained before correction",
          "Supported ownership of a real decision",
          "Review of what was noticed and missed"]),
        "Ask what people learned while doing the work you are removing.",
        os.path.join(d, "capability_formation_ai_task_vs_practice.png"))
    notes.append(("automate the task / rebuild the practice", "card text %d px" % s))
    nov17.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_grid(
        "ONE TASK TO INSPECT THIS WEEK.",
        [("01", ["The task AI now helps me do faster"]),
         ("02", ["What it used to require from me"]),
         ("03", ["What I am happy to stop doing"]),
         ("04", ["What I still need a way to practice"])],
        "Separate what you are glad to stop doing from what you still need to practice.",
        os.path.join(d, "capability_formation_nov17_graphic_b_one_task_to_inspect.png"),
        kind="white", writing=3)
    notes.append(("one task to inspect this week", "prompt text %d px" % s))
    nov17.append((p, os.path.basename(p), BODY_CAPTION))
    made["2026-11-17"] = nov17

    # ---------------- DEC 1 ----------------
    d = folder("2026-12-01")
    dec1 = []
    p, size, nl = build_cover(*COVERS["2026-12-01"],
                              path=os.path.join(d, "capability_formation_cover_2026-12-01.png"))
    notes.append(("cover 2026-12-01", "title %d px over %d lines" % (size, nl)))
    assert size >= 64, "December 1 cover title fell below 64 px"
    dec1.append((p, os.path.basename(p), COVER_CAPTION))

    p = build_vbars(
        os.path.join(d, "capability_formation_dec01_graphic_a_credentials_used_quality_unclear.png"))
    dec1.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_row_cards(
        "BEFORE YOU BUY THE CREDENTIAL.",
        [("WHAT THEY NEED TO BELIEVE",
          ["What does the other side still need to believe?"]),
         ("WHAT IT WILL PROVE", ["What will this credential prove?"]),
         ("WHAT STILL TAKES EXPERIENCE",
          ["What will still require real experience?"])],
        "A credential is most useful when you can name the doubt it is supposed to reduce.",
        os.path.join(d, "capability_formation_before_you_buy_the_credential.png"),
        kind="navy", gap=34, hi=44)
    notes.append(("before you buy the credential", "card text %d px" % s))
    dec1.append((p, os.path.basename(p), BODY_CAPTION))

    p, s = build_grid(
        "FOUR LINES BEFORE YOU ENROLL.",
        [("TARGET MOVE", ["The role or context you want"]),
         ("TRUST QUESTION", ["What the other side still needs to believe"]),
         ("CREDENTIAL JOB", ["What this program or certification would prove"]),
         ("EXPERIENCE GAP", ["What you will still need to practice after you "
                             "finish"])],
        "If you cannot fill these yet, pause before paying for reassurance.",
        os.path.join(d, "capability_formation_dec01_graphic_b_four_lines_before_you_enroll.png"),
        kind="white", writing=3)
    notes.append(("four lines before you enroll", "prompt text %d px" % s))
    dec1.append((p, os.path.basename(p), BODY_CAPTION))

    starter_target = os.path.join(d, "career_evidence_starter_artifact.png")
    if STARTER_SOURCE and os.path.exists(STARTER_SOURCE):
        shutil.copyfile(STARTER_SOURCE, starter_target)
        dec1.append((starter_target, os.path.basename(starter_target), BODY_CAPTION))
    else:
        notes.append(("career_evidence_starter_artifact.png",
                      "MISSING: no Career Evidence Starter preview supplied"))
    made["2026-12-01"] = dec1

    # ---------------- package sheets ----------------
    for date, entries in made.items():
        covers = sum(1 for e in entries if e[2] == COVER_CAPTION)
        body = len(entries) - covers
        count = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}[len(entries)]
        sub = ("Substack visual package, %s. %s assets: one cover, %s in body."
               % (LONG_DATE[date], count,
                  {1: "one", 2: "two", 3: "three", 4: "four"}[body]))
        build_package_sheet(ESSAY_TITLES[date], sub, entries,
                            os.path.join(OUT_ROOT, date,
                                         "package_sheet_%s.png" % date))

    # ---------------- text checks ----------------
    problems = check_text()
    zip_path = OUT_ROOT + ".zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(OUT_ROOT):
            for f in sorted(files):
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, os.path.dirname(OUT_ROOT)))

    print("Built into %s" % OUT_ROOT)
    for k, v in notes:
        print("  %-42s %s" % (k, v))
    print("Text checks: %s" % ("clean" if not problems else problems))
    print("Zip: %s" % zip_path)


BANNED = re.compile(r"\b(actually|honestly|genuinely)\b", re.I)
DASHES = re.compile(r"[–—]")


def check_text():
    """Every string of visible copy in this file is checked for long dashes
    and for the three banned words."""
    import io
    src = io.open(__file__, encoding="utf-8").read()
    problems = []
    src = "\n".join(ln for ln in src.split("\n")
                     if not ln.startswith(("BANNED =", "DASHES =")))
    for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', src):
        s = m.group(1)
        if DASHES.search(s):
            problems.append("long dash in %r" % s)
        if BANNED.search(s):
            problems.append("banned word in %r" % s)
    return problems


if __name__ == "__main__":
    main()
