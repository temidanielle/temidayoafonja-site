#!/usr/bin/env python3
"""Build the Capability Formation editorial plates.

One layout source (the HTML) produces all three deliverables. The SVG master is
exported from the laid-out page by the exporter inside the HTML, and the PNGs
are then rasterised from that SVG -- so the vector master and the bitmaps are
provably the same artwork rather than two drawings kept in step by hand.

    ./design/build.py

Uses headless_shell rather than the full chrome binary: chrome reserves roughly
85px of window chrome out of --window-size, silently clipping the bottom of the
canvas. Override with CHROME=/path/to/binary.
"""

import base64
import os
import pathlib
import re
import subprocess
import sys

DIR = pathlib.Path(__file__).resolve().parent
FONTS = DIR.parent / "fonts"
CHROME = os.environ.get(
    "CHROME", "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
)

FLAGS = ["--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         "--force-color-profile=srgb", "--font-render-hinting=none"]

# (file, family, weight, style) -- every face the plate actually uses.
FACES = [
    ("CormorantGaramond-500-normal-latin-abcaa8.woff2", "Cormorant Garamond", 500, "normal"),
    ("CormorantGaramond-500-italic-latin-4db21d.woff2", "Cormorant Garamond", 500, "italic"),
    ("DMSans-300-normal-latin-1c49a6.woff2", "DM Sans", 300, "normal"),
    ("DMSans-400-normal-latin-1c49a6.woff2", "DM Sans", 400, "normal"),
    ("DMSans-500-normal-latin-1c49a6.woff2", "DM Sans", 500, "normal"),
]

PLATES = [("four-states-organizational.html", "Four_States_Organizational_Distribution_FINAL")]


def run(args):
    return subprocess.run(args, capture_output=True, text=False, check=True).stdout


def font_faces():
    """@font-face rules with the woff2 inlined, so the SVG stands alone."""
    out = []
    for name, family, weight, style in FACES:
        data = base64.b64encode((FONTS / name).read_bytes()).decode("ascii")
        out.append(
            f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}"
        )
    return "\n".join(out)


def export_svg(src, out):
    """Load the plate, read the SVG its exporter wrote onto <body data-svg>."""
    dom = run([CHROME, *FLAGS, "--virtual-time-budget=8000", "--dump-dom",
               f"file://{src}"]).decode("utf-8", "replace")
    m = re.search(r'data-svg="([A-Za-z0-9+/=]+)"', dom)
    if not m:
        sys.exit(f"{src.name}: no data-svg on <body> -- exporter did not run")
    svg = base64.b64decode(m.group(1)).decode("utf-8")
    if "FONT_FACE_PLACEHOLDER" not in svg:
        sys.exit(f"{src.name}: exported SVG has no font placeholder")
    svg = svg.replace("FONT_FACE_PLACEHOLDER", font_faces())
    out.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg, encoding="utf-8")
    return out


def render(svg, w, h, scale, out):
    run([CHROME, *FLAGS, f"--window-size={w},{h}",
         f"--force-device-scale-factor={scale}", "--virtual-time-budget=4000",
         f"--screenshot={out}", f"file://{svg}"])
    return out


def main():
    for src_name, stem in PLATES:
        print(src_name)
        svg = export_svg(DIR / src_name, DIR / f"{stem}_Source.svg")
        print(f"  {svg.name}  ({svg.stat().st_size // 1024} KB, fonts embedded)")
        for scale in (1, 2):
            png = render(svg, 1200, 630, scale, DIR / f"{stem}_{1200 * scale}x{630 * scale}.png")
            print(f"  {png.name}  ({png.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
