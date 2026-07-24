# The Capability Formation Brief — edition assets

A single self-contained script renders two SVG assets and exports each to PNG
at 2x. The only runtime requirement is a headless renderer (Playwright +
Chromium); both display fonts (Cormorant Garamond and a geometric sans) are
embedded as base64 woff2 inside the SVGs, so the render never falls back to a
system font and nothing is fetched at runtime.

## Regenerate

```bash
npm install            # installs the playwright devDependency
node brief-assets/generate-assets.mjs
```

If Playwright's bundled Chromium is not at the default download location, point
the script at an existing binary with `CHROMIUM_PATH=/path/to/chrome`.

## Palette (sand / navy / gold only)

| Token | Hex       | Use                                  |
| ----- | --------- | ------------------------------------ |
| sand  | `#F5F0E8` | background, both assets              |
| navy  | `#0F2347` | display type                         |
| gold  | `#C9A84C` | rules, edition label, name line      |

## Editing an edition

Only two constants change between editions — `HEADLINE` and `EDITION_LABEL` at
the top of `generate-assets.mjs`. The masthead, mark, and name are standing
strings and must not be edited. The mark (Asset B) carries no edition-specific
text; it outlives every edition.

## Outputs

| File                 | Size (SVG) | PNG @2x   | Notes                                   |
| -------------------- | ---------- | --------- | --------------------------------------- |
| `cover-1280x720.png` | 1280×720   | 2560×1440 | Asset A — edition cover (landscape)     |
| `cover-1200x644.png` | 1200×644   | 2400×1288 | Asset A — LinkedIn frame variant        |
| `mark-300x300.png`   | 300×300    | 600×600   | Asset B — standing newsletter mark      |
| `mark-40x40.png`     | 40×40      | 80×80     | Asset B — subscriber-list downscale     |

The `.svg` source for each is written alongside the `.png`.
