# Editorial plates

Source files for Capability Formation essay artwork.

## Building

```bash
./design/build.py
```

One layout source produces all three deliverables. `four-states-organizational.html`
is the layout; an exporter inside it measures the laid-out page and emits the
SVG master; the PNGs are then rasterised from that SVG. So the vector master and
the bitmaps are the same artwork by construction, not two drawings kept in step
by hand.

Three things the build depends on:

- **`headless_shell`, not `chrome`.** The full Chromium binary reserves roughly
  85px of window chrome out of `--window-size`, which silently clips the bottom
  of the canvas. `headless_shell` maps `--window-size` to the viewport exactly.
  Override with `CHROME=/path/to/binary ./design/build.py`.
- **The site's own fonts.** The layout loads Cormorant Garamond and DM Sans from
  `../fonts/`, so the artwork matches temidayoafonja.com typography exactly and
  no network fetch happens at build time. `build.py` inlines those same files
  into the SVG as base64, which is most of its ~350KB and makes it portable.
- **Real baselines, not `dominant-baseline`.** SVG's `central` resolves against
  the font's ascent/descent rather than the CSS line box, which dropped every
  line by one to two pixels. The exporter measures each baseline with a
  zero-height inline-block strut instead. Text now lands pixel-identical to the
  HTML render; the only remaining difference between the two is antialiasing on
  the circles.

The HTML carries `noindex` — `publish = "."` deploys this directory with the
site, but these are build sources, not pages.

## Plates

### `Four_States_Organizational_Distribution_FINAL` — 1200 × 630

The Week 6 organizational capstone image for *The Two Lists That Rarely Match*.
It sits in the essay immediately after "A team is a distribution."

The argument the plate has to carry is that a team is not in one box: sixteen
markers spread across all four quadrants, at least three in every one, so the
distribution reads before any of the labels do. Deliberate constraints, so
future edits do not undo them:

- **No quadrant is the destination.** All four cells share one background rect,
  one border, and one type treatment, and the dividing cross is drawn once
  rather than as borders belonging to two of the cells. Compounding gets no
  tint, no accent, and no extra weight. The plate reads a distribution, not a
  ranking.
- **Marker colour is not a variable.** Tone varies for texture only. The legend
  therefore shows four marks held close in value and no rust, so it reads
  *mark = person* rather than as a colour key. Rust appears twice on the map and
  stays off the cell corners — at an edge it reads as a flagged outlier rather
  than one more person.
- **Stagnant holds the most markers, Fragile the fewest.** An honest reading,
  and it keeps the eye off Compounding.
- No arrows, no staged progression between quadrants, no fifth state, no essay
  title, no book branding.

Type sizes are set for the smallest realistic display. The build was checked at
1200, 800, 600 and 430px wide; at 430 the eyebrow and footer go secondary by
design, but the title, statement, principle line, all four state names and
descriptors, both axis names, and the legend all still read.
