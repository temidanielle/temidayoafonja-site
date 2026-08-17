# QA Report — Capability Formation Field Kit Gumroad Merchandising

Revised Monday, August 17, 2026 at 5:49 AM CT

> v1.1.2 note: Field Kit v1.2.5 recolored the Compounding quadrant to calm blue
> (#C7D9E8). Images 02, 03, 05, and 06 (which show the Matrix / Position Card)
> were regenerated from the updated PDF; the thumbnail and Images 01 and 04 are
> unchanged (SHA-256 verified). Image 06 copy is unchanged.

Production of seven approved merchandising assets built around the final,
immutable 24-page fillable Field Kit. Governing sources: the approved Version 2.0
merchandising brief and four copy locks govern the thumbnail and Images 01
through 05. The subsequently approved individual-offer architecture governs
Image 06 and supersedes all retired group-workshop language.

---

## v1.1 amendment — Image 06 reconciled to the individual-offer architecture

Scope: Image 06 only. All other assets and the Field Kit are unchanged (SHA-256
verified below). The `$500` right panel now describes the new individual offer
**Private Capability Position Read** instead of the retired group workshop.

**Right-panel audit result — stale group-workshop claims WERE found.** The prior
`$500` feature list contained claims that do not belong to the new private offer:

| Prior feature | Verdict |
|---|---|
| Guided evidence correction | Superseded — correction now sits in the free flagship |
| Interpreted state or boundary | Retired with the list (interpretation now expressed by the new items) |
| Next-Move Decision | Removed — risked implying the offer makes the employment decision |
| Live facilitation | Stale — group-room language, not a private 1:1 claim |
| 30-day follow-up | Stale — matches retired "30-Day Evidence Review / workshop follow-through" |
| Supported 90-day rescore | Stale — matches retired "90-day rescore included" |

Per the brief, this was flagged and reported before regenerating; the replacement
list was approved by the client and contains only the approved private-offer
claims (no invented deliverables).

**Authorized text changes applied (Image 06 right panel):**
- Offer name: `LIVE POSITION READ` → `PRIVATE CAPABILITY POSITION READ`
- Descriptor: `HUMAN CORRECTION + DECISION SUPPORT` → `HUMAN INTERPRETATION + DECISION SUPPORT`
- Feature list (5, approved): Private, one-to-one interpretation · Evidence
  interpreted in your actual context · Constraints and options clarified ·
  Stakes and timing examined · Support applying the reading to your decision
- Decision rule (full approved version): "Choose the Field Kit when you want to
  continue the read privately. Choose the Private Capability Position Read when
  the evidence is clearer but the decision still needs context and human
  interpretation."

**Typography note:** the longer offer name fits the existing right-panel label
area at the current 18px on a single line (measured 354px in 492px available),
so no type-size reduction or panel redesign was required. The full decision rule
fits at the existing 19px footer size (two balanced lines). No layout shift.

**Required-string verification (Image 06 v1.1):**
- Present: `PRIVATE CAPABILITY POSITION READ`, `HUMAN INTERPRETATION + DECISION
  SUPPORT`, and the full approved decision rule (exact match).
- Absent: `LIVE POSITION READ`, `HUMAN CORRECTION + DECISION SUPPORT`, the retired
  decision rule, a bare `THE CAPABILITY POSITION READ` used as the paid label, and
  every flagged stale feature (Guided evidence correction, Live facilitation,
  30-day follow-up, Supported 90-day rescore, Next-Move Decision).
- Prices: `$150` and `$500` only. No `$499`, `$650`, `Starting at`, `$500+`,
  coupons, bundles, upgrade credits, or attendee/crossed-out pricing.
- Field Kit left panel, headline, Position Card crop, dimensions, colors,
  typography, and hierarchy unchanged.

**Reduced-size acceptance (Image 06 640×360):** headline, `$150`, `$500`, both
product-level labels, and the decision-rule footer are readable; offer name is a
single clean line with no clipping or 3-line overflow.

**SHA-256 immutability (re-verified against pre-change baseline):** the Field
Kit PDF, `build_fieldkit.py`, the thumbnail (PNG/SVG/240/180), and Images 01–05
(PNG/SVG/640) all verify byte-for-byte unchanged (22/22 OK).

---

## 1. Source verification

| Item | Result |
|---|---|
| Final Field Kit PDF located and verified | `fieldkit/The_Capability_Formation_FieldKit.pdf`, 24 pages, 65 form fields, md5 `f231ad6e101e36ae821600adec3d1fd6` (committed v1.2.3) |
| Required pages exist and match the brief | Verified page-by-page (see below) |
| 2×2 Capability Formation device | Existing source asset (`favicon.svg`) + the device as it appears on the real Field Kit pages |
| Production fonts | Cormorant Garamond + DM Sans (the site's production families) instantiated and used |
| Private Capability Position Read visual for Image 06 | No service screenshot or separate visual was required. The approved text-led private-offer panel was used. |

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
checked: every current visible string maps either to the approved Version 2.0
merchandising brief or to the approved v1.1 individual-offer amendment governing
Image 06 — each to an approved headline, supporting line, label, list item,
callout, footer, or decision rule. No eyebrow/category labels were invented
(only the brief-approved category line on Image 01 and the thumbnail
category/identifier are present).

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
  (FIELD KIT / PRIVATE SELF-ASSESSMENT and PRIVATE CAPABILITY POSITION READ /
  HUMAN INTERPRETATION + DECISION SUPPORT), and the decision rule are all
  readable. PASS.

**System consistency:** one shared 96px margin system and grid, one page-card
treatment (real crop + gold hairline + one restrained shadow), a coherent
Cormorant headline scale and DM Sans label scale, and consistent rust-rule /
gold-hairline rule language across all six 16:9 images. Straight-on page crops
throughout; the only perspective is the restrained cover mockup Image 01 calls
for. Each image answers a distinct buyer question (recognition, outputs, proof,
method, free-vs-Field Kit, and Field Kit versus private human interpretation and
decision support).

## 4. Source integrity

- The Field Kit PDF was **not** modified (git clean; md5 unchanged).
- No Field Kit source file was modified (`build_fieldkit.py`, source PDF,
  `verify.py`, `README.md` all git clean).
- No Field Kit page wording was recreated or rewritten. All product content is
  reproduced by rendering the real pages from the final PDF; no page text was
  retyped. Crops trim only trailing page whitespace and never remove a header,
  field, total, evidence line, or state description, so no crop changes meaning.
- No inaccurate substitute content was introduced. The Image 06 private-offer
  panel is text-led (approved feature list only); no service screenshots,
  participant testimonials, or session outputs were invented.

## 5. Boundary-claim checks

- The Field Kit is presented as a complete self-guided assessment, never as a
  reduced or incomplete version of the live experience.
- No asset implies the Field Kit tells the buyer whether to stay or leave. Image
  06 presents the Private Capability Position Read as human interpretation and
  decision support applied to the person's evidence and context. It does not
  claim that the service makes the employment decision for the participant. The
  Position Card's own "Diagnosis only" line is preserved in the reproduced page.
- Self-guided correction is not equated with human calibration: the Field Kit's
  private self-read is clearly separated from the Private Capability Position
  Read's human interpretation and decision support.
- The free resources are shown with equal dignity (Image 05), never as weak,
  faded, crossed-out, or bait.

Result: all seven assets PASS.
