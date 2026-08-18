#!/usr/bin/env bash
# Builds the Capability Formation YouTube banner and its previews.
#
# Chromium is the renderer so the banner sets in the same self-hosted brand
# faces the site uses. Use headless_shell, not the full chrome binary: chrome's
# "new headless" reserves ~87px of the window for browser chrome and pads the
# bottom of the screenshot with flat canvas colour, which lands as a visible
# seam across the banner. headless_shell's --window-size is the real viewport.
#
# Run from anywhere:  bash youtube-banner/build.sh
set -euo pipefail
# bash 4+ for the associative array in the colour section
BIN=${CHROMIUM:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/youtube-banner/src"

# Targets are passed as file:// URLs. A bare path with an appended #fragment is
# read as a literal filename, so the page silently fails to load and the preview
# renders blank.
shot() { # shot <html-with-optional-#hash> <out.png> <w> <h> [scale]
  "$BIN" --headless --disable-gpu --no-sandbox --hide-scrollbars \
         --force-device-scale-factor="${5:-1}" --virtual-time-budget=6000 \
         --screenshot="$2" --window-size="$3,$4" "file://$1" >/dev/null 2>&1
}

echo "· banners"
for v in a b c; do shot "$SRC/option-$v.html" "$SRC/render-$v.png" 2560 1440; done

echo "· deliverables"
cp "$SRC/render-a.png" "$ROOT/youtube-banner.png"
cp "$SRC/render-b.png" "$ROOT/youtube-banner/alternates/option-b-inverted.png"
cp "$SRC/render-c.png" "$ROOT/youtube-banner/alternates/option-c-masthead.png"

echo "· previews"
P="$ROOT/youtube-banner/previews"
shot "$SRC/preview-safe.html#a"    "$P/safe-areas.png"  2560 1440
shot "$SRC/preview-tv.html#a"      "$P/tv.png"          2880 1760
shot "$SRC/preview-desktop.html#a" "$P/desktop.png"     1600 1000 1.5
shot "$SRC/preview-mobile.html#a"  "$P/mobile.png"       900 1240 2
for v in b c; do
  shot "$SRC/preview-mobile.html#$v"  "$P/mobile-option-$v.png"   900 1240 2
  shot "$SRC/preview-desktop.html#$v" "$P/desktop-option-$v.png" 1600 1000 1.5
done
shot "$SRC/explore-lines.html" "$P/supporting-lines.png" 1040 2330 1.4

# ── Colour treatments ───────────────────────────────────────────────────────
# Every treatment renders from the one source, src/color.html, so the approved
# layout, typography, spacing and copy cannot drift between them: only the
# colour field changes. Fields are flat, with no gradient, vignette or grain.
echo "· colour treatments"
C="$ROOT/youtube-banner/color"
declare -A NAMES=(
  [a]="option-a-cream-gold"
  [aink]="option-a-refined-cream-goldink"
  [b]="option-b-cream-navy"
  [c]="option-c-ink-cream"
)
for v in a aink b c; do
  shot "$SRC/color.html#$v" "$SRC/render-color-$v.png" 2560 1440
  cp "$SRC/render-color-$v.png" "$C/${NAMES[$v]}.png"
  shot "$SRC/preview-mobile.html#color-$v"       "$C/previews/$v-mobile.png"       900 1240 2
  shot "$SRC/preview-desktop.html#color-$v"      "$C/previews/$v-desktop.png"     1600 1000 1.5
  shot "$SRC/preview-desktop.html#color-$v,dark" "$C/previews/$v-desktop-dark.png" 1600 1000 1.5
done
shot "$SRC/compare.html" "$C/comparison.png" 1800 880 1.4
echo "done"
