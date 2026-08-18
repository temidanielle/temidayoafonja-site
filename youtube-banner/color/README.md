# Colour treatments

Colour only. The layout, typography, spacing and copy are the approved ones and
are not touched here. All four treatments render from a single source,
`src/color.html`, so they cannot drift from each other: the only thing that
changes between them is the colour field. Verified identical in every render,
title 1256 px wide, 145 px clear either side, 225 px block in the 423 px band.

Fields are flat. No gradient, no vignette, no grain, which is also why these
files are 0.05 MB rather than 2.77 MB and will survive YouTube's re-encode
without banding.

## Recommended: Option A refined

`option-a-refined-cream-goldink.png`

```
Field     #F5F0E8   cream
Title     #0F2347   deep navy
Question  #7F6A30   gold, the site's text-safe variant
```

This is Option A as briefed, with one change: the question is set in `#7F6A30`
rather than `#C9A84C`.

Brand gold on cream measures **2.01:1**. That is not a close call. It is below
AA, below AA Large, and below the 3:1 floor for non-text, and at the mobile crop
the question visibly dissolves into the field. The site already ran into this and
solved it: `styles.css` carries `--gold-ink: #7F6A30`, added in August 2026
specifically so gold-toned type can sit on white, paper, sand and the warm band.
`content/site-source-of-truth.json` records that the four brand colours are
unchanged and that this variant exists for exactly this use. So the refinement
uses an approved token rather than a new colour, and the treatment still reads as
gold. It measures **4.62:1**.

Both versions are included so the difference can be judged directly:
`option-a-cream-gold.png` is the brief as written.

## Why this treatment over the others

**Immediate readability.** Navy on cream is 13.70:1, the strongest title contrast
of any option, and the gold question is legibly secondary rather than faint.

**Sharpness.** A flat cream field with no gradient gives the type a hard edge.
Against the navy original the letterforms gain noticeably in definition.

**Distinction in the interface.** This is where the options separate. On
YouTube's light theme the cream field reads as a warm panel against the white
page, clearly a designed object. On the dark theme it is striking, a bright card
against near black. Option C fails this test in the other direction: at
`#161719` against YouTube's `#0f0f0f` the banner nearly dissolves into the page
and stops reading as a banner at all. See `previews/c-desktop-dark.png`.

**Fit for the audience.** Cream and navy reads as paper and ink. It is warmer and
more human than the navy field, which is the direction the channel needs for
professionals, without giving up the seriousness the organizational work depends
on. It is also the least generic choice available: almost nothing on YouTube is
cream.

## The other treatments

| File | Notes |
| --- | --- |
| `option-a-cream-gold.png` | Option A exactly as briefed. Included for comparison. The question measures 2.01:1 and is not recommended for use. |
| `option-b-cream-navy.png` | Both levels navy, gold held to a single small mark. The most restrained and highest contrast of the set. The mark sits inside the existing 74 px gap, splitting it 30.5 / 13 / 30.5, so the title and question do not move. Strong, slightly cooler and more institutional than A refined. |
| `option-c-ink-cream.png` | Near-black ink field. Sophisticated and the sharpest on light theme, but loses its edges on dark theme. |

## Previews

For each treatment (`a`, `aink`, `b`, `c`):

- `previews/<v>-mobile.png`, cropped to the 1546 × 423 safe area
- `previews/<v>-desktop.png`, YouTube light theme
- `previews/<v>-desktop-dark.png`, YouTube dark theme

`comparison.png` puts all four side by side at the mobile crop with measured
contrast on each.

## Measured

| Treatment | Title | Question |
| --- | --- | --- |
| A as briefed | 13.70:1 | **2.01:1**, fails |
| A refined | 13.70:1 | 4.62:1 |
| B | 13.70:1 | 13.70:1 |
| C | 15.81:1 | 7.85:1 |

Ratios are computed from the specified hex values and confirmed against the
rendered pixels.
