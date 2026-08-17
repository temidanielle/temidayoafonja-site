# Capability Formation — YouTube thumbnail 01

**Video:** *Career Change at 40: How to Move Without Starting Over*
**Thumbnail words:** WHAT STILL TRAVELS?
**Master:** [`what-still-travels.svg`](what-still-travels.svg) — 3840 × 2160, 16:9

---

## How the thumbnail and the title work together

The title names the situation: a career change at forty, made without starting
over. The thumbnail does not repeat it. It asks the question that sits
underneath the move — *what still travels?* — which is the capability-formation
premise: capability is portable, roles are not. Title supplies the circumstance,
thumbnail supplies the idea; neither is legible as a paraphrase of the other,
and the two together read as a single sentence rather than one statement said
twice.

No part of the video title appears in the artwork. There is no URL, button,
price, product image, episode number or challenge label.

---

## Portrait

| | |
|---|---|
| Source file | [`assets/source/temidayo-studio-portrait-1268x1240.png`](assets/source/temidayo-studio-portrait-1268x1240.png) |
| Source description | Approved studio portrait of Temidayo Afonja — closed-lip composed expression, direct gaze, gold sleeveless top. Supplied as a circular crop on a white field with a black surround. |
| Source size | 1268 × 1240 px, 8-bit RGB |
| Not used | `/temi-photo.jpg` (500 × 500) — the site's existing headshot is a different, older portrait and is too small for a 3840px master. No other face, and no generated or reconstructed face, appears anywhere in this artwork. |

### Crop

Keyed and cropped by [`build/prep-portrait.py`](build/prep-portrait.py):

1. **Key.** The studio ground (white field, its drop shadow, and the black
   surround) is achromatic; the subject is warm-chromatic throughout. A
   border-seeded flood fill across achromatic pixels lifts the ground without
   touching her.
2. **Edge.** The silhouette is contracted 2 px and feathered (σ 1.0) so blend
   pixels are dropped rather than carried onto navy as a bright rim; remaining
   partial pixels are un-mixed against the known white ground
   (`F = (C − (1−α)·255) / α`).
3. **Crop.** Source rectangle **x [134 : 1158], y [68 : 923]**, then trimmed to
   the silhouette → **937 × 831**
   ([`assets/temidayo-portrait-cutout.png`](assets/temidayo-portrait-cutout.png)).
   The bottom cut sits six rows above the point where her shoulder first meets
   the source's circular mask, so the composite never shows that clipped arc —
   she bleeds off the foot of the canvas instead.
4. **Scale.** Premultiplied Lanczos to the exact placement box **1600 × 1419**,
   plus a light unsharp (r 2.0, 45%, threshold 3) to recover what the 1.7×
   upscale costs
   ([`build/scale-portrait.py`](build/scale-portrait.py) →
   [`assets/temidayo-portrait-1600.png`](assets/temidayo-portrait-1600.png)).

### Correction

Only what the brief allows — exposure, colour balance, clean crop, background
separation. Nothing reshapes, smooths or repaints her: face, age, skin texture,
expression and proportions are the source photograph's.

* **Colour balance** — neutral-grey correction measured off the studio's own
  white ground.
* **Exposure** — +2% lift, 1.06 contrast around mid grey.
* **Deep-shadow lift** — +3.8% applied only below ~0.235 luma, tapered. About
  half her silhouette (dark hair, shadow-side shoulder) otherwise sits within 18
  luma of the navy ground. This lifts the darkest values enough to separate her
  from it without touching midtones or skin texture — and without any halo,
  glow, rim light or gradient behind her.

### Placement

`x 2048, y 741, 1600 × 1419` — **41.7% of the canvas width**, right-hand side,
bleeding off the bottom edge only. Her opaque silhouette covers 12.3% of the
canvas and the placement box 27.4% of its area.

> **Interpretation note.** "36–42% of the canvas" is read here as the portrait
> occupying the right-hand 36–42% *of the frame's width* (41.7%, top of the
> range). Read instead as 36–42% of canvas *area*, the box would need ~48% of
> the width, which pushes her past the right safe margin and into the headline.
> If the area reading is the intended one, it is a one-line change to the
> `<image>` element in the SVG.

---

## Typography

Both faces are the repository's self-hosted webfonts, referenced from the SVG by
relative path — no external font requests.

| Element | Face | Size | Tracking | Colour |
|---|---|---|---|---|
| `CAPABILITY FORMATION` | DM Sans 500 — `fonts/DMSans-500-normal-latin-1c49a6.woff2` | 52 px | 12.5 px (0.24em) | `#C9A84C` |
| `WHAT / STILL / TRAVELS?` | Cormorant Garamond 600 — `fonts/CormorantGaramond-600-normal-latin-abcaa8.woff2` | 350 px | 5 px | `#F5F0E8` |

Three lines, flush left at x = 260, baselines 908 / 1233 / 1558. Tracking on the
identifier matches `.eyebrow` in `/styles.css` (0.24em). The headline uses
Cormorant 600 rather than the site's display weight of 300: at 200 px wide a
300-weight stem falls below one device pixel and greys out, while 600 holds.

---

## Colour

| Role | Hex | Contrast on navy |
|---|---|---|
| Ground | `#0F2347` deep navy | — |
| Headline | `#F5F0E8` warm cream | 13.70 : 1 |
| Identifier + rule | `#C9A84C` muted gold | 6.80 : 1 |

One accent only: a single 240 × 8 px gold rule beneath the headline. **Rust
`#C1440E` is deliberately unused** — it reaches only 3.03 : 1 on this navy and
would read muddy rather than warm at feed size. The brief permits rust at most
once, not at least once.

The navy carries the site's `feTurbulence` film grain at `opacity 0.02`
(`/styles.css` `body::before`). Base ground is exactly `#0F2347`; grain lifts the
mean to `rgb(16.6, 36.3, 72.0)` — under two levels. No gradients anywhere in the
artwork.

---

## Safe area and platform overlays

* 5% safe margin = 192 px. The identifier, all three headline lines, the gold
  rule and the whole of her face sit inside it. The portrait's right edge lands
  exactly on the 192 px line; the portrait bleeds off the bottom edge by
  intent.
* The duration pill (bottom-right, roughly 15% × 12%) falls over the shoulder of
  her top — no words, no face, nothing lost.
* Desktop hover controls (top-right) fall on empty navy.

---

## Exports

Everything in [`exports/`](exports) is regenerated from the SVG by
`python3 build/build.py`.

| File | What it is | Settings |
|---|---|---|
| `what-still-travels-3840x2160.png` | Full-resolution master | PNG-24, RGB, no alpha, sRGB. Chromium screenshot of the SVG at deviceScaleFactor 1. 6.1 MB |
| `what-still-travels-1920x1080-upload.jpg` | **The file to upload** | JPEG q92, 4:4:4 chroma, optimized, non-progressive, Lanczos from the master. 226 KB — YouTube caps custom thumbnails at 2 MB, which the PNG master exceeds |
| `preview-360.png` | 360 px preview | Lanczos from the master |
| `preview-200.png` | 200 px preview | Lanczos from the master |
| `sim-mobile-home-feed.png` | Mobile home feed | 412 × 915 CSS px @ 2× |
| `sim-desktop-home-feed.png` | Desktop home feed | 1280 × 720 CSS px @ 2× |
| `sim-right-column.png` | Right-column recommendations | 402 × 640 CSS px @ 2×, thumbnail at 168 px |

The simulations use neutral grey stand-in cards and generic UI furniture. They
are layout tests for the thumbnail, not reproductions of any platform's
branding, and contain no stock photography.

At 200 px wide the three headline lines and her face both stay unmistakable; the
identifier is a gold tick of text by design, and is legible from 360 px up.

---

## Rebuilding

```sh
cd youtube/what-still-travels
python3 build/build.py        # portrait → master → previews → upload file → simulations
```

Needs Python with `pillow`, `numpy`, `scipy`, and Playwright's Chromium on
`NODE_PATH` (see the constant at the top of `build/build.py`).

| File | Role |
|---|---|
| `what-still-travels.svg` | **Editable source of truth.** Type, colour, geometry |
| `build/prep-portrait.py` | Source portrait → keyed, corrected cutout |
| `build/scale-portrait.py` | Cutout → exact placement asset |
| `build/render.mjs` | Serves the repo over HTTP and screenshots with Chromium, so the SVG's relative font and image paths resolve exactly as they do on the site |
| `build/build.py` | Runs all of the above and writes `exports/` |
| `build/sim-*.html`, `build/sim-common.css` | The three placement simulations |
