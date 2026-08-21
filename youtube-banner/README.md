# Capability Formation: YouTube channel banner

Built from the positioning already published on this site, not from a fresh brief.
The colours, faces and editorial habits come from `styles.css` and
`content/site-source-of-truth.json`, so the channel art and the site read as one
identity: navy `#0F2347`, cream `#F5F0E8`, gold `#C9A84C`, Cormorant Garamond
over DM Sans, self-hosted from `/fonts`.

## Recommended banner

**`/youtube-banner.png`** (repository root, alongside `linkedin-banner.png`)

Exact text on the banner, and nothing else:

```
CAPABILITY FORMATION
What is your work building?
```

Set as `Capability Formation` in Cormorant Garamond 400, uppercase, gold, with
`.155em` letter-spacing, over `What is your work building?` in Cormorant
Garamond 300 italic, cream. No third line, no name, no icons, no contact detail.

### Why this one

The channel name renders directly beneath the banner on every YouTube surface,
so putting *Temidayo Afonja* in the artwork would say the same thing twice and
cost the composition its air. It was tested and left out.

The question carries both audiences without naming either. A professional reads
it as *what is my current work building in me*; a leader reads it as *what is our
work environment building in our people*. Neither reading is signposted, so the
banner stays true to Capability Formation as the umbrella rather than narrowing
to the career content the channel may lead with at launch.

Gold on the title and cream on the question puts the warm accent on the idea and
leaves the question quiet, which is the right order when the title is the thing a
new viewer has to learn. The two lines sit alone on the navy with nothing between
them. A rule was tried and cut: at the mobile crop a 1px hairline scales to a
quarter of a pixel and reads as a smudge rather than a mark, and the spacing does
the separating on its own.

## Alternates

| File | Direction |
| --- | --- |
| `alternates/option-b-inverted.png` | Cream title, gold question, with the small gold diamond that already marks the LinkedIn banner. Leans further toward the individual by warming the line they are asked to answer. Closest continuity with existing channel art. |
| `alternates/option-c-masthead.png` | Asymmetric. A gold vertical hairline anchors the block to the left of the safe area. Reads as a masthead rather than a title card, and is the most contemporary of the three. |

## Previews

| File | Shows |
| --- | --- |
| `previews/safe-areas.png` | All four YouTube crops mapped over the artwork, with everything outside the text-safe rectangle dimmed |
| `previews/mobile.png` | Channel page on a phone, cropped to 1546 × 423 |
| `previews/desktop.png` | Channel page on desktop, the 2560 × 423 band |
| `previews/tv.png` | Full 2560 × 1440, no crop |
| `previews/supporting-lines.png` | The seven supporting lines considered, each at the mobile crop |
| `previews/mobile-option-{b,c}.png`, `previews/desktop-option-{b,c}.png` | The alternates in the same two contexts |

## Supporting lines considered

1. **What is your work building?** Reads in both directions without naming either audience. **Chosen.**
2. *Is your work still building you?* The site's own professional question. Sharper, but individual only.
3. *What is your work building in you?* Warmer and more personal. Closes off the organizational reading.
4. *Capability that holds when conditions change.* The site headline verbatim. True, but a statement rather than an opening, and the longest of the seven at the mobile crop.
5. *What still travels when the work changes.* Captures durability. Asks nothing of the viewer.
6. *What your work is forming.* Closest to the framework language. Reads abstract on its own.
7. *Build capability that travels.* Active and short, but tips toward advice rather than enquiry.

## Verified

- **2560 × 1440**, 2.77 MB, inside YouTube's 6 MB ceiling.
- All text inside the **1546 × 423** text-safe rectangle: the title is 1256 px
  wide leaving 145 px either side, and the two lines occupy 225 px of the 423 px
  band with 99 px above.
- Contrast measured off the rendered pixels, not the swatches: gold on its local
  background **5.80:1**, cream **11.68:1**. Both clear WCAG AA for body text, so
  they clear it comfortably at banner size.
- The navy falls smoothly to all four edges, checked by sampling the render
  rather than by eye.

## Rebuilding

```sh
bash youtube-banner/build.sh
```

Sources are in `src/`. Two things worth keeping in mind if you change the build:

- Render with `headless_shell`, not the full `chrome` binary. Chrome's new
  headless mode reserves about 87 px of the window for browser chrome, so the
  viewport is shorter than `--window-size` and the bottom of the screenshot gets
  padded with flat canvas colour. That lands as a visible seam across the banner.
- Pass targets as `file://` URLs. A bare path with a `#fragment` appended is read
  as a literal filename, and the page silently renders blank.

`src/render-*.png` are intermediates, ignored by git; the published copies are
the root banner, `alternates/` and `previews/`.

## Colour treatments

A colour-only refinement of this banner lives in `color/`. Same layout,
typography, spacing and copy; flat fields instead of the navy ground. See
`color/README.md`.

## Refresh

The supporting line was later replaced with "Know what will hold when
conditions change." See `refresh/README.md`.
