# START HERE carousel

LinkedIn Featured document carousel: **START HERE: Does What You Have Already Done Still Count?**
Eight slides, 1080 x 1350 portrait, 96px margins.

## Deliverables

| File | What it is |
| --- | --- |
| `LinkedIn_Start_Here_Capability_Formation_V2.pdf` | The upload file. Eight pages, vector text. |
| `slides/slide-01.png` to `slide-08.png` | One preview per slide, 1080 x 1350 |
| `contact-sheet.png` | All eight slides in order |
| `source/copy.json` | Editable copy, exactly as supplied |
| `source/carousel.html` | Editable layout, live DOM text, no outlined type |
| `source/build-carousel.mjs` | Renders the PNGs, the PDF and the contact sheet |
| `source/verify-carousel.mjs` | The quality gate |
| `START_HERE_Carousel_Report.docx` | Status and overview as a Word document |
| `source/build-report.js` | Regenerates that report (`npm install docx`, then `node build-report.js`) |

Rebuild after a copy edit:

```sh
node linkedin-start-here-carousel/source/build-carousel.mjs
node linkedin-start-here-carousel/source/verify-carousel.mjs
```

## Design system

Canvas 1080 x 1350 with 96px margins on all four sides, cream forward with a
single deep navy closing slide, exactly as the brief asks.

Palette: four values only. Navy `#112345`, cream `#F5F1E8`, gold `#C9A84C` and
bright warm yellow `#F2C44C`. No fifth colour appears anywhere. Gold carries the
structural marks: the large section numerals, the rules and the pagination ring.
Small tracked text takes whichever of navy or gold reads better against its own
background, so it is navy on the cream slides and gold on the navy slide. The
bright yellow is used once, on the closing line. Type is Cormorant Garamond for
display and DM Sans for body, labels and navigation, both self hosted in the
repository and both the faces the Career Evidence Starter itself uses.

Navigation is a gold ringed page number bottom right on every slide, with an
arrow on slide 1 only. The ring is the same gold mark throughout; only the
figures inside and beside it change colour with the background.

The approved portrait is the real photograph at
`images/temidayo-gold-ivory.png`, circularly cropped and placed once, on slide
1, at 264px. It is scaled down from 1254px, never up, and nothing about the
photograph itself is altered.

## What was missing from the workspace

Three things the brief refers to were not present when this was built. None was
invented or substituted.

1. **The carousel foundation build kit.** It lived outside the repository and
   this container was reset, so the files were gone. The system was rebuilt from
   its specification as established earlier in this project: canvas, margins,
   type pairing, palette, circular portrait treatment, gold ringed counter and
   the render and verify export process. The original was not overwritten,
   because there was nothing left to overwrite.
2. **The Density Group logo files.** Also gone with that directory. No logo
   appears on these slides, because redrawing or approximating one is not
   acceptable. The footer supplied in the brief carries the attribution on the
   closing slide. Send the logo zip and it drops into the template in one edit.
3. **`final 3(1).pdf`.** Not in the workspace or the uploads, so it could not be
   used as a starting point. The carousel is built from the slide sequence and
   copy supplied in the brief.

## Palette correction, applied in V2

V2 runs on the four approved values and nothing else. Every rust rule is now
gold, and the separate on cream gold that V1 used for small labels is gone.

A colour audit of the eight rendered pages confirms it: each page carries only
those values, no orange or rust pixel appears outside the photograph, and the
bright yellow appears on the closing slide alone.

## Accessibility pass, applied after approval

Gold `#C9A84C` on cream `#F5F1E8` measures 2.03 to 1. That is comfortable for
the 96px numerals and faint for the two smallest items on cream, the START HERE
label and the page number, both of which land near 8px at LinkedIn mobile width.
Those two are now navy `#112345`, which measures 13.8 to 1. No colour was added:
navy was already in the palette.

Everything else keeps its gold. The section numerals, the rules, the ruled serif
line and the pagination ring are unchanged, and slide 8 is untouched, because
gold on navy measures 6.81 to 1 and already passes.

In `source/carousel.html` the ring is pinned to `var(--gold)` rather than
`currentColor`. That matters: the digits sit inside the ring, so a counter set in
navy would otherwise drag the ring to navy with it.

Measured against the previous exports pixel by pixel: slide 8 has zero changed
pixels, slides 2 to 7 changed only inside the page number, and slide 1 changed
only at the label and the page number. Nothing else moved.

Contrast across the finished set:

| Pairing | Ratio | Where |
| --- | --- | --- |
| Navy on cream | 13.8 : 1 | Headlines, body, labels and page numbers, slides 1 to 7 |
| Cream on navy | 13.8 : 1 | Headline, body and footer, slide 8 |
| Gold on navy | 6.81 : 1 | Page number, slide 8 |
| Bright yellow on navy | 9.46 : 1 | Closing line, slide 8 |

Gold on cream now appears only as structure: the numerals, the rules and the
ring, none of which is reading text.

No em dash or en dash characters appear anywhere in this package.
