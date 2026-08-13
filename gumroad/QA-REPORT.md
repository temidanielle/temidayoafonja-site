# QA Report — Capability Formation Field Kit Gumroad Merchandising

Production of seven approved merchandising assets built around the final,
immutable 24-page fillable Field Kit. Governing spec: the Version 2.0
merchandising brief plus the four final copy locks.

## 1. Source verification

| Item | Result |
|---|---|
| Final Field Kit PDF located and verified | `fieldkit/The_Capability_Formation_FieldKit.pdf`, 24 pages, 65 form fields, md5 `f231ad6e101e36ae821600adec3d1fd6` (committed v1.2.3) |
| Required pages exist and match the brief | Verified page-by-page (see below) |
| 2×2 Capability Formation device | Existing source asset (`favicon.svg`) + the device as it appears on the real Field Kit pages |
| Production fonts | Cormorant Garamond + DM Sans (the site's production families) instantiated and used |
| Approved live-workshop visual for Image 06 | None present in the repository → brief-permitted text-led facilitator panel used |

**Page verification against the brief (all confirmed in the final PDF):**

| Brief reference | PDF page | Actual page title | Match |
|---|---|---|---|
| Cover | 1 | Read Your Position. / Know Your Exposure. | ✔ |
| Density | 5 | Part One: Density (evidence protocol + 6 statements + total) | ✔ |
| Optionality | 6 | Part Two: Optionality | ✔ |
| Matrix | 8 | The Matrix (four states + descriptions + boundary rule) | ✔ |
| Three Misreadings | 11 | The Three Misreadings | ✔ |
| Rescore Note | 12 | The Rescore Note | ✔ |
| Self-Read Skeleton | 19 | The Self-Read Skeleton | ✔ |
| Position Card | 20 | The Position Card (quadrant + dated fields) | ✔ |
| Rescore Tracker | 22 | The Rescore Tracker | ✔ |

No page-level conflict between the brief and the actual Field Kit was found, so
no STOP condition was triggered.

**Documented resolution (precedence applied, not a conflict):** the 2×2 device
renders with the rust square in the **top-right** on the real Field Kit pages,
whereas `favicon.svg` places it bottom-right. Per the brief's precedence rule
(the actual Field Kit source governs reproduced product artwork), the device is
reproduced to match the product: rust square top-right.

## 2. Copy verification

Confirmed the four final copy locks appear exactly, in the correct assets:

| Lock | Where | Verbatim |
|---|---|---|
| Gumroad short summary | Listing field (documented for the listing; not rendered into an image) | "Twelve statements. Two scores. One evidence-led read of your current position." |
| Image 03 headline | Image 03 | "From Evidence to Position." |
| Image 05 headline (two stacked sentences, 2nd heavier) | Image 05 | "The Free Check Helps You See the Pattern." / "The Field Kit Tests Your Position." |
| Image 06 Field Kit descriptor | Image 06 | "PRIVATE SELF-ASSESSMENT" |

Retired variants — confirmed absent from every asset (visible-copy scan = 0):
- "…evidence-led view of where you stand." — 0
- "A Real Assessment, Not a Page of Prompts." — 0
- "Recognition Is Free. The Full Self-Read Is the Field Kit." — 0
- "PRIVATE SELF-DIAGNOSIS" — 0

Only approved copy is typeset. A full visible-text extraction of every master was
checked against the brief; each string maps to an approved headline, supporting
line, label, list item, callout, footer, or decision rule. No eyebrow/category
labels were invented (only the brief-approved category line on Image 01 and the
thumbnail category/identifier are present).

Guardrails (visible copy):
- Em dashes 0, en dashes 0, U+2192 arrows 0.
- Prices: `$150` appears only in Image 05 and Image 06; `$500` only in Image 06.
- No `$149`, `$499`, `$75`, `$125`, founding/compare-at/discount pricing,
  seat counts, dates, scarcity, "psychometric" or "scientifically validated",
  or fabricated social proof anywhere.

## 3. Asset verification

Color mode: all PNGs are flat RGB, rendered through Chromium with
`--force-color-profile=srgb` and saved with no non-sRGB ICC profile (standard
sRGB). Dimensions/format/integrity confirmed programmatically (all PASS).

| # | Filename | Dimensions | Mode | Source pages | Reduced test | Result |
|---|---|---|---|---|---|---|
| 1 | fieldkit_gumroad_thumbnail_600x600.png | 600×600 | RGB/sRGB | none (2×2 device only) | 240×240, 180×180 | PASS |
| 2 | fieldkit_gumroad_01_recognition_1600x900.png | 1600×900 | RGB/sRGB | p1 (cover) | 640×360 | PASS |
| 2b | fieldkit_gumroad_01_recognition_1280x720.png | 1280×720 | RGB/sRGB | p1 (cover) | — | PASS |
| 3 | fieldkit_gumroad_02_outputs_1600x900.png | 1600×900 | RGB/sRGB | p20, p19, p22 | 640×360 | PASS |
| 4 | fieldkit_gumroad_03_product_proof_1600x900.png | 1600×900 | RGB/sRGB | p5, p6, p8, p20 | 640×360 | PASS |
| 5 | fieldkit_gumroad_04_evidence_method_1600x900.png | 1600×900 | RGB/sRGB | p5, p11 | 640×360 | PASS |
| 6 | fieldkit_gumroad_05_free_vs_fieldkit_1600x900.png | 1600×900 | RGB/sRGB | p5, p8, p20 (proof strip) | 640×360 | PASS |
| 7 | fieldkit_gumroad_06_fieldkit_vs_live_1600x900.png | 1600×900 | RGB/sRGB | p20 (Position Card) | 640×360 | PASS |

**Reduced-size acceptance (visually inspected):**
- Thumbnail 240×240 and 180×180 — the question is immediately readable at both;
  the category line is readable at 240; the proprietary identifier is secondary
  at 180 without harming comprehension. PASS.
- Listing images at 640×360 — headline, core labels, and the buyer distinction
  remain readable; small reproduced page text functions as visual proof. PASS.
- Image 06 at 640×360 — headline, `$150`, `$500`, both product-level labels
  (FIELD KIT / PRIVATE SELF-ASSESSMENT and LIVE POSITION READ / HUMAN CORRECTION
  + DECISION SUPPORT), and the decision rule are all readable. PASS.

**System consistency:** one shared 96px margin system and grid, one page-card
treatment (real crop + gold hairline + one restrained shadow), a coherent
Cormorant headline scale and DM Sans label scale, and consistent rust-rule /
gold-hairline rule language across all six 16:9 images. Straight-on page crops
throughout; the only perspective is the restrained cover mockup Image 01 calls
for. Each image answers a distinct buyer question (recognition, outputs, proof,
method, free-vs-paid, paid-vs-live).

## 4. Source integrity

- The Field Kit PDF was **not** modified (git clean; md5 unchanged).
- No Field Kit source file was modified (`build_fieldkit.py`, source PDF,
  `verify.py`, `README.md` all git clean).
- No Field Kit page wording was recreated or rewritten. All product content is
  reproduced by rendering the real pages from the final PDF; no page text was
  retyped. Crops trim only trailing page whitespace and never remove a header,
  field, total, evidence line, or state description, so no crop changes meaning.
- No inaccurate substitute content was introduced. The Image 06 live-experience
  panel is text-led (approved feature list only); no workshop screenshots,
  participant testimonials, or session outputs were invented.

## 5. Boundary-claim checks

- The Field Kit is presented as a complete self-guided assessment, never as a
  reduced or incomplete version of the live experience.
- No asset implies the Field Kit tells the buyer whether to stay or leave
  (Image 06 keeps Next-Move Decision on the $500 live side; the Position Card's
  own "Diagnosis only" line is preserved in the reproduced page).
- Self-guided correction is not equated with human calibration (Image 06
  separates "Quarterly tracker" / self-read from "$500 Human correction +
  decision support").
- The free resources are shown with equal dignity (Image 05), never as weak,
  faded, crossed-out, or bait.

Result: all seven assets PASS.
