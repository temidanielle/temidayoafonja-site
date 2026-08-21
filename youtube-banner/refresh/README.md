# Banner refresh: new supporting line

A refresh, not a redesign. The cream field, navy and gold language, Cormorant
Garamond setting, centred structure and safe-area geometry all carry over from
the approved banner. The identity line is untouched: same face, same 84px, same
`.155em` tracking, same 1256px width with 145px clear either side.

## Copy

```
CAPABILITY FORMATION
Know what will hold when conditions change.
```

## Recommended: primary, identity-led

`banner-primary-identity-led.png`

```
Field     #F5F0E8   cream
Title     #0F2347   deep navy
Line      #0F2347   deep navy, Cormorant Garamond italic 400, 66px
Mark      #C9A84C   brand gold, 13px
```

Three changes, all in service of the new line reading faster at small sizes.

**Weight.** The old question was set in Cormorant 300. That hairline weight is
what made it feel delicate once YouTube scaled it down. The new line runs at 400
and at 66px rather than 61px. Same face, same voice, more body.

**Colour.** The line moved from gold to navy. This is the change worth
explaining, because the previous banner deliberately put gold there. The new
line is 43 characters against the old line's 27, so every glyph is doing more
work, and gold on cream is 4.62:1 against navy's 13.70:1. `comparison.png` shows
all three options at actual size on a 430pt phone, and in that column the gold
version visibly goes grey and recedes while the navy version stays crisp. That
is the "does not disappear" problem, so the line took the contrast.

**Gold.** Rather than lose the third colour, gold moved to a single 13px mark
between the two lines. It sits inside the existing 68px gap, splitting it
27.5 / 13 / 27.5, so the title and the line do not move at all. A solid mark
survives the mobile downscale where a thin gold rule would not.

`banner-variant-gold-line.png` keeps the line in gold for anyone who prefers
continuity with the previously approved banner. It is the same geometry.

## Alternate: message-led

`banner-alternate-message-led.png`

The promise becomes the headline at 80px navy italic, and the channel name drops
to a letter-spaced gold eyebrow above it. This reads fastest of the three: the
value proposition is the first thing the eye lands on, and YouTube prints the
channel name directly beneath the banner anyway, so the identity still arrives.

The cost is that the brand name stops being the banner's subject. At actual phone
size the eyebrow is legible but quiet, even at 600 weight. Worth choosing if the
channel's job is to convert strangers rather than to confirm a known name.

## Previews

- `previews/primary-mobile.png`, `previews/alternate-mobile.png`, cropped to 1546 × 423
- `previews/primary-desktop.png`, `previews/alternate-desktop.png`
- `previews/primary-tv.png`, `previews/alternate-tv.png`, full 2560 × 1440
- `comparison.png`, all three options at actual phone size and enlarged

## Verified

| | Title | Line |
| --- | --- | --- |
| Primary, navy line | 13.70:1 | 13.70:1 |
| Variant, gold line | 13.70:1 | 4.62:1 |
| Alternate | 4.62:1 eyebrow | 13.70:1 |

Geometry is identical across the identity-led options: title 1256px wide, 145px
clear either side, 225px block inside the 423px band, 99px above. The alternate
runs 1295px wide with 126px clear either side. Everything sits inside the
1546 × 423 text-safe rectangle. Each file is 2560 × 1440 and about 0.06 MB,
well inside YouTube's 6 MB ceiling, and ready to upload as is.
