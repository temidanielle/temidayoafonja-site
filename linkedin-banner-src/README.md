# LinkedIn banner source

Generator for the LinkedIn personal-profile banner (`../linkedin-banner.png`).
The banner is rendered from `banner.html` — edit the copy/styling there and
re-render; never edit the PNG directly.

## Files

- `banner.html` — the full 1584×396 layout, palette, and copy (single source of truth).
- `render.js` — screenshots `banner.html` to PNG via headless Chromium at 2× scale.

## Editing the copy

All text lives in `banner.html`:

| Element    | Selector   | Text |
|------------|------------|------|
| Kicker     | `.kicker`  | `Capability Formation` |
| Headline   | `.headline`| `Capability that outlasts volatility.` |
| Support    | `.support` | `Enterprise advisory for CHROs and CPOs leading AI-era workforce transformation in regulated and mission-critical organizations.` |
| Signature  | `.sig-word`| `The Density Group` |

## Canon brand tokens (already wired in)

- Navy background `#0F2347`
- Gold accents `#C9A84C`
- Rust mark square `#C1440E`
- Cream headline `#F5F0E8`

Type: **Cormorant Garamond** (serif headline) + **DM Sans** (sans).

## Fonts

Install the two families so Chromium can render them (variable TTFs from
Google Fonts work). On this Debian-based environment:

```sh
mkdir -p ~/.fonts
# CormorantGaramond[wght].ttf, CormorantGaramond-Italic[wght].ttf, DMSans[opsz,wght].ttf
cp *.ttf ~/.fonts/ && fc-cache -f
```

## Render

```sh
npm i playwright                 # if not already available
node render.js                   # -> ../linkedin-banner.png at 3168×792
# or explicit:
node render.js banner.html ../linkedin-banner.png 2
```

If the environment ships its own Chromium binary, point at it with
`CHROMIUM_PATH=/path/to/chrome node render.js`.

## Output

3168 × 792 PNG (2× of the 1584 × 396 LinkedIn banner canvas).
