# Capability Formation Brief covers

Editorial covers for The Capability Formation Brief, generated from code so every
edition stays in the same publication system as the July/August/September covers.

## Files

| File | What it is |
| --- | --- |
| `editions.json` | The copy. Publication line, title lines, edition, date, byline. |
| `brief-cover.html` | The cover itself: one parameterised page, live DOM text. |
| `build-covers.mjs` | Renders each edition to `output/` with Playwright. |
| `verify-covers.mjs` | Reads the exported PNGs back and checks they are one family. |
| `output/*.png` | The exported covers, 1664 × 936. |

## Build

```sh
node covers/build-covers.mjs                 # all editions, pure typographic
node covers/build-covers.mjs --motif         # also write the faint-motif variants
node covers/build-covers.mjs --scale=2       # 3328 × 1872, for print or retina
node covers/build-covers.mjs edition-four    # a single edition, matched by slug
```

Requires `playwright` (`npm i -D playwright`). The script serves the repo over a
local http port so the `/fonts/` URLs inside `fonts.css` resolve to the site's
self-hosted woff2 files; nothing is fetched from the network.

## Verify

```sh
node covers/verify-covers.mjs
```

This reads the pixels back out of every exported PNG and reports where the title
ink actually landed, failing if one cover is off the group. Run it after every
build. A cover is a single image with no test around it, so a bad export looks
exactly like a design decision — this is what tells the difference.

Do not pipe the build's output through `head`; the render can be killed partway
and leave a stale PNG behind that still looks plausible. That failure is the
reason this check exists.

## The system

- Deep navy `#0f2347`, warm cream `#f5f0e8`, muted gold `#c9a84c` — the same
  tokens as `styles.css`, so the covers and the site cannot drift apart.
- Cormorant Garamond for the title, Montserrat for the small tracked lines. Both
  are already self-hosted in `fonts/`.
- Title case, never all caps. No subtitle on the cover. No labels, diagrams,
  icons, or teaching devices — the title is the visual event.
- Text is real text until the export, so any line can be edited in
  `editions.json` and re-rendered.

**One title size across the family.** `build-covers.mjs` measures every edition,
finds the size each one fits at inside the 1250px title measure, and re-renders
the whole set at the smallest of those. That is what makes three different
titles read as three issues of one publication rather than three designs. Adding
a fourth edition with a longer title will step the whole family down — which is
the intent; check the other covers after adding one.

## Motif variants

Every edition is exported twice: a pure typographic cover and a `-motif` variant.
The motif is a low-opacity drift of hairlines and points along the bottom edge,
below the byline, carrying no labels and nothing to decode. It reads as paper
texture, not content. **The pure typographic covers are the default choice** — the
motif is there when an edition wants a little more warmth, not because the
article needs illustrating.

## Crop safety

At 1664 × 936 (16:9), LinkedIn's 1.91:1 feed crop takes about 32px off the top
and bottom. The publication line (y 92) and byline (y 848) both clear it. The
motif runs to y 930 and can be clipped without loss, which is why it carries
nothing meaningful.
