#!/usr/bin/env python3
"""Check the built plate against the brief it was commissioned from.

Reads the SVG master (the artwork the PNGs are rasterised from) and asserts the
things that must not drift: exact copy, quadrant placement, axis direction,
marker distribution, equal treatment across the four states, a legend that
cannot read as a colour key, and contrast for the text that has to survive a
phone.

    ./design/verify.py
"""

import pathlib
import re
import struct
import sys

DIR = pathlib.Path(__file__).resolve().parent
STEM = "Four_States_Organizational_Distribution_FINAL"
NAVY = (15, 35, 71)

# Grid geometry, from the layout source.
GX0, GY0, GX1, GY1 = 706, 96, 1154, 512
MIDX, MIDY = 930, 304

COPY = [
    ("eyebrow", ["CAPABILITY FORMATION FRAMEWORK · ORGANIZATIONAL CAPSTONE"]),
    ("title", ["THE FOUR", "STATES"]),
    ("statement", ["A team is a distribution across all four states."]),
    ("principle", ["Strong performance does not tell you", "where capability is forming."]),
    ("legend-text", ["EACH MARK IS ONE PERSON ON THE SAME TEAM"]),
    ("state", ["DEPTH TRAP", "COMPOUNDING", "STAGNANT", "FRAGILE"]),
    ("desc", ["Deep capability.", "Narrow reach.", "Deep capability.", "Widening reach.",
              "Little new depth.", "Little new reach.",
              "Broad reach.", "Too little depth beneath it."]),
    ("axis-name", ["DENSITY", "OPTIONALITY"]),
    ("axis-end", ["HIGH", "LOW", "LOW", "HIGH"]),
    ("foot-left", ["CAPABILITY FORMATION · TEMIDAYO AFONJA"]),
    ("foot-right", ["TEMIDAYOAFONJA.COM"]),
]

QUADRANTS = {"DEPTH TRAP": "TL", "COMPOUNDING": "TR", "STAGNANT": "BL", "FRAGILE": "BR"}

# Text that has to survive a phone screen, and so is held to WCAG AA body text.
MUST_READ = ["statement", "principle", "desc", "state", "axis-name", "legend-text"]

results = []


def check(ok, label, detail=""):
    results.append((bool(ok), label, detail))


def rgb(spec):
    """Composite an SVG fill over the navy field."""
    n = [float(x) for x in re.findall(r"[\d.]+", spec)]
    if len(n) == 3:
        n.append(1.0)
    return tuple(n[i] * n[3] + NAVY[i] * (1 - n[3]) for i in range(3))


def contrast(spec):
    def lum(c):
        ch = []
        for v in c:
            v /= 255
            ch.append(v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4)
        return .2126 * ch[0] + .7152 * ch[1] + .0722 * ch[2]
    a, b = lum(rgb(spec)) + .05, lum(NAVY) + .05
    return round(max(a, b) / min(a, b), 2)


svg = (DIR / f"{STEM}_Source.svg").read_text(encoding="utf-8")
style, body = svg.split("</style>")
texts = re.findall(r'<text class="([^"]+)"[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*>(.*?)</text>', body)
circles = [(float(x), float(y), float(r), f) for x, y, r, f in
           re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="([^"]+)"', body)]
rects = re.findall(r"<rect [^>]*/>", body)
rules = dict(re.findall(r"\.([\w-]+)\{([^}]+)\}", style))

# --- exact copy, in document order ---------------------------------------
for cls, expected in COPY:
    got = [t[3] for t in texts if t[0] == cls]
    check(got == expected, f"copy: {cls}", "" if got == expected else f"{got!r} != {expected!r}")

# --- quadrant placement --------------------------------------------------
for name, want in QUADRANTS.items():
    hit = [t for t in texts if t[0] == "state" and t[3] == name]
    if not hit:
        check(False, f"placement: {name}", "state name missing")
        continue
    x, y = float(hit[0][1]), float(hit[0][2])
    got = ("T" if y < MIDY else "B") + ("L" if x < MIDX else "R")
    check(got == want, f"placement: {name} {want}", "" if got == want else f"found in {got}")

# --- axis direction ------------------------------------------------------
vert = [t for t in texts if t[0] == "axis-end" and float(t[1]) < GX0]
horiz = sorted([t for t in texts if t[0] == "axis-end" and float(t[1]) >= GX0], key=lambda t: float(t[1]))
vy = {t[3]: float(t[2]) for t in vert}
check(len(vert) == 2 and vy.get("HIGH", 9e9) < vy.get("LOW", -9e9),
      "axis: DENSITY runs low (bottom) to high (top)", str(vy))
check([t[3] for t in horiz] == ["LOW", "HIGH"],
      "axis: OPTIONALITY runs low (left) to high (right)", str([t[3] for t in horiz]))

# --- marker distribution -------------------------------------------------
counts = {"TL": 0, "TR": 0, "BL": 0, "BR": 0}
rust_map = rust_legend = 0
legend = []
for x, y, r, fill in circles:
    on_map = GX0 <= x <= GX1 and GY0 <= y <= GY1
    is_rust = rgb(fill)[0] > 150 and rgb(fill)[1] < 110  # the only warm-red in the palette
    if on_map:
        counts[("T" if y < MIDY else "B") + ("L" if x < MIDX else "R")] += 1
        rust_map += is_rust
    else:
        legend.append(fill)
        rust_legend += is_rust
for q, n in counts.items():
    check(n >= 2, f"markers: {q} holds more than one person", f"{n} marker(s)")
check(sum(counts.values()) >= 14, "markers: 14-18 across the team", f"{sum(counts.values())} total")
check(rust_map <= 2, "palette: rust stays limited on the map", f"{rust_map} rust marker(s)")

# --- legend cannot read as a colour key ----------------------------------
check(3 <= len(legend) <= 4, "legend: three or four marks", f"{len(legend)} marks")
check(rust_legend == 0, "legend: no rust mark", f"{rust_legend} rust")
if legend:
    spread = max(contrast(f) for f in legend) - min(contrast(f) for f in legend)
    check(spread < 3.0, "legend: marks held close in value (no implied categories)",
          f"contrast spread {spread:.2f}")

# --- equal status across the four states ---------------------------------
per_cell = [r for r in rects if re.search(r'x="(7[1-9]\d|8\d\d|9[0-2]\d)', r) and 'height="4' not in r]
check(len(rects) == 9, "states: no quadrant carries its own rect", f"{len(rects)} rects total")
check(len([t for t in texts if t[0] == "state"]) == 4 and len(re.findall(r"\.state\{", style)) == 1,
      "states: all four names share one type rule")
check("desc" in rules and len(re.findall(r"\.desc\{", style)) == 1,
      "states: all four descriptors share one type rule")

# --- hierarchy: descriptors must not compete with state names ------------
size = lambda c: float(re.search(r"font-size:([\d.]+)", rules[c]).group(1))
check(size("desc") < size("state") * 0.6, "hierarchy: descriptors stay under the state names",
      f'desc {size("desc")}px vs state {size("state")}px')
check(size("principle") < size("title") * 0.5, "hierarchy: principle line stays under the title",
      f'principle {size("principle")}px vs title {size("title")}px')

# --- contrast for the text that has to survive a phone -------------------
for cls in MUST_READ:
    fill = re.search(r"fill:([^;}]+)", rules[cls]).group(1)
    c = contrast(fill)
    check(c >= 4.5, f"contrast: {cls} >= 4.5:1 on navy", f"{c}:1")
for cls in ("eyebrow", "axis-end", "foot-left", "foot-right"):
    fill = re.search(r"fill:([^;}]+)", rules[cls]).group(1)
    results.append((True, f"contrast: {cls} (secondary)", f"{contrast(fill)}:1"))

# --- guardrails ----------------------------------------------------------
banned = [("gradient", "Gradient"), ("filter", "<filter"), ("shadow", "feDropShadow"),
          ("raster image", "<image"), ("arrow marker", "<marker")]
for label, token in banned:
    check(token not in svg, f"guardrail: no {label}")

# --- exported files ------------------------------------------------------
for w, h in ((1200, 630), (2400, 1260)):
    p = DIR / f"{STEM}_{w}x{h}.png"
    if not p.exists():
        check(False, f"export: {p.name}", "missing")
        continue
    gw, gh = struct.unpack(">II", p.read_bytes()[16:24])
    check((gw, gh) == (w, h), f"export: {p.name}", f"{gw}x{gh}")

# --- report --------------------------------------------------------------
width = max(len(r[1]) for r in results)
for ok, label, detail in results:
    print(f'{"PASS" if ok else "FAIL"}  {label:<{width}}  {detail}')
failed = [r for r in results if not r[0]]
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
sys.exit(1 if failed else 0)
