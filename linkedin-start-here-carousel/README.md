# START HERE carousel

LinkedIn Featured document carousel: **START HERE: Does What You Have Already Done Still Count?**
Eight slides, 1080 x 1350 portrait.

## Version 3

Rebuilt into the shared system the rest of the carousel set uses: a cream card
floating on a navy field, DM Sans throughout, gold hairlines and tracked gold
capitals, with the cover and the close inverted to a navy card. The approved
portrait stays on the cover, and the gold pagination ring is carried over.

Two substantive changes came with the rebuild.

Nothing is set below 28px, which is the floor the later carousels hold. The
previous version ran its tracked labels at 21px, about 8.2px at LinkedIn mobile
width. The floor now sits at 10.9px there.

The body text was enlarged to fill the card rather than headlines being shrunk
to make room for it, which is what the previous version's fitting loop did.

Three lines of copy were revised on request. Everything else is the approved
wording, unchanged.

## Deliverables

| File | What it is |
| --- | --- |
| `LinkedIn_Start_Here_Capability_Formation_V3.pdf` | The upload file. Eight pages. |
| `slides/slide-01.png` to `slide-08.png` | One preview per slide, 1080 x 1350 |
| `slides/slide-01.svg` to `slide-08.svg` | The vector sources, live text |
| `contact-sheet.png` | All eight slides in order |
| `source/copy.json` | Every string that reaches a slide, plus the palette and the canvas |
| `source/lib.mjs` | Fonts, the type scale, and the measured wrapper |
| `source/build.mjs` | Renders the SVGs, the PNGs and the PDF |
| `source/contact-sheet.mjs` | Renders the contact sheet |
| `source/verify.mjs` | The quality gate |
| `source/voice.mjs` | The voice rules, with their own self test |

Earlier upload files are kept alongside: `..._V2.pdf` is the previous design and
`..._V1.pdf` the one before it.

`START_HERE_Carousel_Report.docx` and `source/build-report.js` document
**version 2** and have not been regenerated for this rebuild, so the design
decisions they describe are superseded.

## Rebuild

```
node source/build.mjs        # slides and the PDF
node source/contact-sheet.mjs
node source/verify.mjs       # exits non zero if anything is wrong
node source/voice.mjs        # proves the voice rules fire on what they claim
```

## The gate

Thirteen checks, each of which fails the build rather than warning:

- eight slides, all 1080 x 1350
- every slide carries its copy exactly, compared character for character, and carries nothing else
- all three revised lines are set, and none of the three they replaced survive
- no em dashes and no en dashes
- no "not X, it is Y" constructions, and none of the hedging adverbs "actually", "honestly", "genuinely"
- nothing below the 28px floor
- the numeral and the question sit at one height on all four question slides
- the gold pagination ring is on every slide
- the approved portrait is on slide 1 only
- the footer is on slide 8 only
- every left aligned element sits on the margin, and no ink crosses the card edge
- the PDF is eight pages at 810 by 1013 pt
- exactly one raster image, the portrait on page 1; every other page is vector text
