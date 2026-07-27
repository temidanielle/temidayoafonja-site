# Brief Asset Generator

A small, deterministic asset generator for **THE CAPABILITY FORMATION BRIEF**
LinkedIn newsletter brand system. It renders self-contained SVG and exports
crisp PNG. No image model is involved — every visible string is a named
constant, and each render is verified against those constants before export.

Two assets:

| Asset | What it is | Outputs |
|---|---|---|
| **`mark`** | The newsletter logo. Square, standing identity, no edition number, no headline. | `300x300` + `40x40` (the checking size) |
| **`cover`** | The per-edition article cover. 16:9, regenerated every edition. | `1920x1080` + `1200x644` (upload fallback) |

## Usage

```bash
pip install -r requirements.txt      # one time
python3 generate.py                  # uses GROUND from the file (default: navy)
python3 generate.py sand             # override the ground for this run

# Per-edition cover (headline + edition are parameters; the name line is not):
python3 generate.py navy --only cover \
  --head1 "What Your Talent" --head2 "Systems Cannot See" \
  --edition "EDITION TWO" --num 2
```

`--only mark` / `--only cover` render just one asset. The headline splits across
two lines (`--head1` / `--head2`) — pick a balanced split that keeps both lines
inside wide margins.

Every run prints a full verification report and a tuning table to stdout, and
writes PNGs + a self-contained SVG per asset into `output/`. The previous
version of any file it would overwrite is moved into `output/archive/` first —
nothing is ever clobbered.

Fonts are already committed under `fonts/`. To refresh them from Google Fonts
(needs network), run `python3 build_fonts.py`.

## How the type is rendered (important)

The brief asks for the fonts to be embedded as base64 woff2 in a `<defs><style>`
block so the SVG is self-contained. **This generator does that** — the woff2 is
embedded for provenance and editability.

But the *visible* artwork is drawn as **vector outlines** shaped from the real
font files (fontTools + HarfBuzz), **not** as live `<text>`. This is a
deliberate, load-bearing decision:

> Real rasterizers silently drop `@font-face`. Verified in this environment,
> resvg logs *"The @font-face rule is not supported. Skipped."* and then
> *"No match for 'Cormorant Garamond' font-family"*, falling back to a system
> sans — **exactly the failure the brief warns about.**

Outlining the type removes font resolution from the raster path entirely, so the
mark and cover render byte-identically in any renderer, on any machine, forever.
The embedded woff2 stays in the file as the source of record. The
font-resolution width check is kept and is meaningful: it compares the rendered
ink width against the width computed independently from the font's own metrics,
and **fails loudly** on mismatch (a wrong font file, a dropped glyph, or a scale
bug all trip it, and the generator refuses to export).

## The two faces

- **Display** — Cormorant Garamond, weight 500. The word `BRIEF` on the mark and
  the headline on the cover. A light-stemmed old-style serif; do not substitute,
  and do not switch to a heavier Cormorant cut (that is a different face).
- **Caps** — Montserrat, weight 600. Always uppercase, always letterspaced. The
  kicker, edition, and name lines.

## Palette (closed set of four)

`NAVY #0F2347` · `SAND #F5F0E8` · `GOLD #C9A84C` · `CREAM #F7F4EE`. Any fifth
value is a bug; the colour check catches it.

## Ground

`GROUND = "navy"` or `"sand"` (default navy). These are not colour swaps of one
another — reversed type on navy optically blooms and reads thinner, so navy has
its own **explicit compensation multipliers** (`NAVY_DISPLAY_SIZE_MULT`,
`NAVY_CAPS_SIZE_MULT`, `NAVY_INK_GROW_PX`) that are no-ops on sand.

## Tuning

Every number you can change without touching layout code lives in the clearly
marked **TUNING TABLE** block near the top of `generate.py`, and the full table
is printed on every run. Sizes are SVG user units (px at 1x); tracking is in em.

### When something looks wrong, move this number

| What is bothering you | The number to move |
|---|---|
| BRIEF looks thin, washed, or soft on navy | Increase `MARK_DISPLAY_SIZE` first, then `NAVY_INK_GROW_PX` / `NAVY_DISPLAY_SIZE_MULT`. Do **not** switch to a heavier weight. |
| The mark feels cramped or busy | Reduce `MARK_UPPER_SIZE`, or set `MARK_SHOW_UPPER = False` — the upper line is the least load-bearing element. |
| The mark sits high with a gap underneath | Reduce `MARK_BLOCK_OFFSET` and tighten `MARK_GAP_RULE_TO_NAME`. |
| Letters mush together at 40px | Increase `MARK_UPPER_TRACKING` / `MARK_NAME_TRACKING` before increasing their size. |
| The gold rule disappears | Increase `MARK_RULE_WEIGHT` before `MARK_RULE_LENGTH`. A longer thin rule reads weaker than a shorter heavier one. |
| The whole thing reads generic | The caps tracking is usually too tight and the display size too small. Editorial marks live on the contrast between a large serif and very small, very open caps. |
| It looks fine at 300 and bad at 40 | The 40 is the real size. Design at 40 and let the 300 follow. The contact sheet (`..._ContactSheet_40-vs-300_...png`) shows both side by side every re-render. |

## Forbidden

No icons, illustrations, photographs, borders, drop shadows, gradients,
texture, background imagery, logo lockups, or rounded containers. Flat editorial
type on a flat ground, wide margins, nothing decorative.

## Files

```
brief-generator/
├── generate.py         # the generator (constants, engine, verify, export)
├── build_fonts.py      # refresh/subset the fonts from Google Fonts (run-once)
├── requirements.txt
├── fonts/              # committed subset woff2 (offline-reproducible)
└── output/             # generated PNGs + SVGs (archive/ holds superseded ones)
```
