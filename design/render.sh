#!/usr/bin/env bash
# Render the Capability Formation editorial plates to PNG.
#
# Chromium ships with the container image (Playwright's build). Each plate is a
# self-contained HTML file sized to its exact canvas, screenshotted at 1x for
# the Substack/OG slot and 2x for retina display.
set -euo pipefail

# headless_shell, not the full chrome binary: the full binary reserves ~85px of
# window chrome out of --window-size, which silently clips the bottom of the
# plate. headless_shell maps --window-size to the viewport exactly.
CHROME="${CHROME:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

render() {
  local name="$1" w="$2" h="$3" scale="$4" out="$5"
  "$CHROME" \
    --headless \
    --no-sandbox \
    --disable-gpu \
    --hide-scrollbars \
    --force-color-profile=srgb \
    --font-render-hinting=none \
    --window-size="${w},${h}" \
    --force-device-scale-factor="${scale}" \
    --virtual-time-budget=4000 \
    --screenshot="${DIR}/${out}" \
    "file://${DIR}/${name}" >/dev/null 2>&1
  echo "  ${out}"
}

echo "Rendering four-states-organizational:"
render four-states-organizational.html 1200 630 1 four-states-organizational-1200x630.png
render four-states-organizational.html 1200 630 2 four-states-organizational-2400x1260.png
