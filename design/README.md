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
  therefore shows four marks within 2.6:1 of each other, in cream and pale
  blue-gray only, so it reads *mark = person* rather than as a colour key.
  Muted gold is excluded from the legend on purpose: on navy it sits at 6.8:1
  against cream's 13.7:1, and a step that large reads as a category. Rust is
  absent for the same reason; on the map it appears twice and stays off the
  cell corners, where an edge position reads as a flagged outlier rather than
  one more person.
- **Stagnant holds the most markers, Fragile the fewest.** An honest reading,
  and it keeps the eye off Compounding.
- No arrows, no staged progression between quadrants, no fifth state, no essay
  title, no book branding.

Type sizes are set for the smallest realistic display. The build was checked at
1200, 800, 600 and 430px wide; at 430 the eyebrow and footer go secondary by
design, but the title, statement, principle line, all four state names and
descriptors, both axis names, and the legend all still read.

## Verifying

```bash
./design/verify.py
```

Reads the built SVG and asserts what must not drift: exact copy, quadrant
placement, axis direction, at least two markers per quadrant, one shared rect
and one shared type rule across the four states, a legend whose marks stay
close in value, WCAG AA contrast for every run that has to survive a phone, and
the guardrails (no gradient, filter, shadow, raster image or arrow marker). It
exits non-zero on failure, so it can gate a change to the plate. It is what
caught the legend's gold mark sitting 10:1 away from its cream neighbour.
