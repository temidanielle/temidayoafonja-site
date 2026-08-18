# Video 1 slide deck: URL change record and QA

**Version 2.3**
**Revised Tuesday, August 18, 2026 at 10:46 AM CT**

Build timezone: America/Chicago (CDT, UTC-05:00).

Deck: **How I Changed Jobs Without Starting My Career Over**
Revision type: single approved URL change on the version 2.2 deck. One line of
copy on one slide. Nothing else changed. Version 2.2 and every earlier version
remain untouched. No website, product or unrelated asset was modified.

---

## 1. Change log

| Slide | Change | Reason |
|---|---|---|
| 9, Field Kit invitation | URL band text `temidayoafonja.com/book` becomes `temidayoafonja.com/fieldkit`. Same band, same position, same size, weight, colour and alignment. | Approved after the version 2.2 URL check. `/fieldkit` is the route `netlify.toml` already defines for the Field Kit, so a viewer typing the URL from the video lands on the Field Kit itself rather than on a three-product page. |

Nothing else on slide 9 changed: kicker, headline, body copy, product artwork,
band geometry and speaker notes are all as approved. Slides 1 through 8 and 10
are pixel-identical to version 2.2.

---

## 2. What the URL now points at

`temidayoafonja.com/fieldkit` resolves through the redirect defined in
`netlify.toml`:

```
[[redirects]]
  from = "/fieldkit"
  to = "https://temidayoafonja.gumroad.com/l/czmqp"
  status = 301
  force = true
```

That is the same Gumroad product `book.html` links to with its "Get the Field Kit"
button, listed there at $150 with instant digital access. `docs/data-inventory.md`
and `docs/legal-review-required.md` both describe Field Kit purchase as happening
through this redirect.

**Verification still owed by the website side.** This deck was checked against the
repository, not against production. Before publishing the video, confirm on the
live site that `/fieldkit` resolves and that the Gumroad product is the current
Field Kit listing. A ready-to-send request is in `FIELDKIT_URL_HANDOFF.md`.

One thing that request raises, flagged here because it affects measurement rather
than correctness: `/fieldkit` is a forced 301 straight to Gumroad, so no page on
the site is served and the Plausible script never runs. Clicks driven by the video
will therefore not appear in site analytics. That may be exactly what you want,
since Gumroad has its own reporting, but it is worth deciding deliberately rather
than discovering later.

---

## 3. QA results

Raw output: `out/v2.3/qa-raw-v2.3.json` and `out/v2.3/qa-raw-main-v2.3.json`.

| # | Check | Result |
|---|---|---|
| 1 | Slide 9 shows `temidayoafonja.com/fieldkit` | Pass. |
| 2 | `temidayoafonja.com/book` no longer appears anywhere | Pass. Zero occurrences in visible copy or notes. |
| 3 | The URL appears on one slide only | Pass. Slide 9. The title slide still carries the bare domain in its footer, unchanged since version 1. |
| 4 | URL fits its band with margin | Pass. The line uses 593 px of the 720 px band, a 17.7 percent margin, so a font substitution in PowerPoint cannot break it onto a second line. |
| 5 | No unintended change anywhere | Pass. Nine of ten rendered slides are pixel-identical to version 2.2, and slide 9 differs only within x 183 to 777, y 874 to 916, which is the URL text itself. The band, the artwork and every other element are unmoved. |
| 6 | Main deck is exactly 10 slides | Pass. 10 slides, 10 PDF pages at 13.333 x 7.5 in. |
| 7 | Recording deck | Pass. 21 slides, same running order, 0 frames dropping a permanent element, last build of each slide content-identical to the main slide. |
| 8 | Camera safe areas preserved | Pass. 0 hits in the main deck, 0 across all 21 recording frames. |
| 9 | End-screen area preserved | Pass. Slide 10 is pixel-identical to version 2.2. |
| 10 | No clipped, crowded or unexpectedly wrapped text | Pass. 0 findings in either deck. |
| 11 | Voice standard holds | Pass. 0 em dash and 0 en dash characters. No price, no Maven, no Keep the Proof, no Career Portability Map, no AI relevance claim. |
| 12 | Timings unchanged | Pass. Contiguous 0:00 to 9:00. |
| 13 | Version 2.2 and earlier remain unchanged | Pass. All prior files byte-identical. Version 2.3 writes only `*_v2.3` files and `out/v2.3/`. |
| 14 | No unrelated assets or website files changed | Pass. The working tree contains only new files under `deliverables/video-1-slides/`. `netlify.toml` was read, never edited. |

---

## 4. Output paths

All paths relative to `deliverables/video-1-slides/`.

**Version 2.3 deliverables**

- `out/Video-1-Reveal-Builds_v2.3.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.3.pptx`
- `out/Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.3.pdf`
- `VIDEO_1_SLIDE_QA_v2.3.md` (this file)
- `FIELDKIT_URL_HANDOFF.md` (request to send to the website channel)

**Supporting version 2.3 output**

- `out/v2.3/png/slide-01 ... slide-10`, `out/v2.3/reveals/frame-01 ... frame-21`
- `out/v2.3/Video-1-Reveal-Builds_v2.3.pdf`
- `out/v2.3/contact-sheet-v2.3.png`, `out/v2.3/recording-deck-order-v2.3.png`
- `out/v2.3/guides/`, `out/v2.3/qa-raw-v2.3.json`, `out/v2.3/qa-raw-main-v2.3.json`

**Source**

- `build/slides_v2_3.py`, copied from `slides_v2_2.py` with the one URL line changed
- `build/build_v2_3.py`, build and QA pass
- `build/deck.py`, shared primitives, unchanged since version 1

Rebuild with `python3 build/build_v2_3.py` from `deliverables/video-1-slides/`.

**Archive, untouched**

Versions 2.2, 2.1, 2 and 1, with their QA records, decks, PDFs and frame sets.
