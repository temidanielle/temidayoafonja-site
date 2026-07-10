# Capability Audit card generator

One template system that renders all seven social cards to the repo root.

## Run

```bash
# Playwright + a Chromium build must be available on the machine.
node card-generator/generate.mjs
```

This writes, at the repo root:

**Quote cards** — 2160 x 2700 (portrait 4:5), sand `#F5F0E8`:

- `quote_look_safe.png`
- `quote_compounding_corner.png`
- `quote_advice_kindness.png`
- `quote_retention_risk.png`
- `quote_competitor_twice.png`
- `quote_title_travel.png`

**Density teaser** — 2245 x 1587 (landscape):

- `teaser_density.png`

## Design

- Serif: **Cormorant Garamond** (regular). Sans: **Montserrat** (medium).
  Both are bundled under `fonts/` as woff2 and embedded as base64 at render
  time, so the cards never fall back to a system font.
- Palette: sand `#F5F0E8`, navy `#0F2347`, gold `#C9A84C`.
- Quote cards share one fixed quote size (`QUOTE_FONT_PX`) so the set stays
  visually consistent. The quote + gold rule + attribution are centered as a
  single group, both vertically and horizontally.

## Editing the cards

All copy and layout live in `generate.mjs`. Change the `quoteCards` array or the
`teaserHTML()` block, then re-run the command above.
