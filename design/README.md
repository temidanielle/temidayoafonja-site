# Editorial plates

Source files for Capability Formation essay artwork. Each plate is a
self-contained HTML file sized to its exact canvas and screenshotted with the
Chromium build already present in the container.

## Rendering

```bash
./design/render.sh
```

Each plate is written twice: at its native pixel size for the Substack/OG slot,
and at 2x for retina display.

Two things the render depends on:

- **`headless_shell`, not `chrome`.** The full Chromium binary reserves roughly
  85px of window chrome out of `--window-size`, which silently clips the bottom
  of the canvas. `headless_shell` maps `--window-size` to the viewport exactly.
  Override the binary with `CHROME=/path/to/binary ./design/render.sh`.
- **The site's own fonts.** The plates load Cormorant Garamond and DM Sans from
  `../fonts/` by relative path, so the artwork matches temidayoafonja.com
  typography exactly and no network fetch happens at render time.

The HTML sources carry `noindex` — `publish = "."` deploys this directory with
the site, but these are build sources, not pages.

## Plates

### `four-states-organizational.html` — 1200 × 630

The Week 6 organizational capstone image for *The Two Lists That Rarely Match*.
It sits in the essay immediately after "A team is a distribution."

The argument the plate has to carry is that a team is not in one box: sixteen
markers spread across all four quadrants, at least three in every one, so the
distribution reads before any of the labels do. Deliberate constraints, so
future edits do not undo them:

- Markers carry no ranking. Tone varies (cream, gold, pale blue-gray, and rust
  twice) for texture only, and rust stays off the cell corners — at an edge it
  reads as a flagged outlier rather than one more person.
- Stagnant holds the most markers, Fragile the fewest. Compounding is one step
  more resolved than its neighbours (a faint gold wash and border) and no more.
  It must not read as the winning box.
- No arrows, no staged progression between quadrants, no fifth state.
