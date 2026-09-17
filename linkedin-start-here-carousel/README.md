# START HERE carousel

LinkedIn Featured document carousel: **START HERE: Does What You Have Already Done Still Count?**
Eight slides, 1080 x 1350 portrait, 96px margins.

## Deliverables

| File | What it is |
| --- | --- |
| `LinkedIn_Start_Here_Capability_Formation.pdf` | The upload file. Eight pages, vector text. |
| `slides/slide-01.png` to `slide-08.png` | One preview per slide, 1080 x 1350 |
| `contact-sheet.png` | All eight slides in order |
| `source/copy.json` | Editable copy, exactly as supplied |
| `source/carousel.html` | Editable layout, live DOM text, no outlined type |
| `source/build-carousel.mjs` | Renders the PNGs, the PDF and the contact sheet |
| `source/verify-carousel.mjs` | The quality gate |
| `START_HERE_Carousel_Report.docx` | The delivery and QA report as a Word document |
| `source/build-report.js` | Regenerates that report (`npm install docx`, then `node build-report.js`) |

Rebuild after a copy edit:

```sh
node linkedin-start-here-carousel/source/build-carousel.mjs
node linkedin-start-here-carousel/source/verify-carousel.mjs
```

## Design system

Canvas 1080 x 1350 with 96px margins on all four sides, cream forward with a
single deep navy closing slide, exactly as the brief asks.

Palette: navy `#0F2347`, cream `#F5F0E8`, gold `#C9A84C` on navy and `#B8952E`
on cream, rust `#C1440E` for the short rules, bright warm yellow `#F2C44C` used
once, on the closing slide. Type is Cormorant Garamond for display and DM Sans
for body, labels and navigation, both self hosted in the repository and both the
faces the Career Evidence Starter itself uses.

Navigation is a gold ringed page number bottom right on every slide, with an
arrow on slide 1 only. The approved portrait is the real photograph at
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

## One palette decision

The brief names navy `#112345` and cream `#F5F1E8`. The real Capability
Formation artifacts, including the Career Evidence Starter, are drawn in
`#0F2347` and `#F5F0E8`, which is what these slides use, so the carousel sits
beside the existing assets without a visible shade mismatch. The cream values
differ by one unit in the green channel and are indistinguishable. Say the word
and both re-render on the values in the brief.

Gold is `#C9A84C` exactly as specified wherever it sits on navy. On cream it
drops to `#B8952E`, the brand value for gold on a light field, because
`#C9A84C` measures about 2 to 1 against cream and is too weak for small labels.

No em dash or en dash characters appear anywhere in this package.
