# Changed-Files Report — Gumroad Merchandising Production

Revised Monday, August 17, 2026 at 5:49 AM CT

---

## v1.1.2 amendment — Compounding recolor propagated to merch art (Field Kit v1.2.5)

The Field Kit's Compounding quadrant was recolored to the approved calm blue
(#C7D9E8) in Field Kit v1.2.5. The four merchandising images that display the
Compounding quadrant were regenerated from the updated PDF so their real-page
crops match:

- `png/fieldkit_gumroad_02_outputs_1600x900.png` + its master + 640×360 test
- `png/fieldkit_gumroad_03_product_proof_1600x900.png` + its master + 640×360 test
- `png/fieldkit_gumroad_05_free_vs_fieldkit_1600x900.png` + its master + 640×360 test
- `png/fieldkit_gumroad_06_fieldkit_vs_live_1600x900.png` + its master + 640×360 test
- `build/crops/p08_seq.png`, `build/crops/p08_matrix.png`, `build/crops/p20_card.png` (re-cut from v1.2.5)
- `contact-sheet.png` (regenerated)

**Unchanged (SHA-256 verified, 11/11 OK):** the thumbnail, Image 01, and Image
04 — PNGs, SVG masters, reduced tests, and the Image 01 1280×720 export. Those
assets do not display the Compounding quadrant. Image 06 copy is unchanged
(Private Capability Position Read; $150 and $500 only). No Field Kit text, field,
or dimension was affected by this art refresh.

---

## v1.1.1 amendment — documentation reconciliation (reports only)

Documentation-only pass. Carried-forward v1.0 sections of `QA-REPORT.md` that
still described the retired group workshop as the current `$500` offer were
reconciled to the approved v1.1 individual-offer architecture (governing-source
statement, source-verification row, copy-verification statement, reduced-size
labels, system-consistency description, source-integrity wording, and
boundary-claim section). Retired terms now appear in the report only inside the
explicitly historical audit / retired-string-verification sections, never as a
description of the current Image 06.

**Files changed in v1.1.1 (documentation only):**
- `QA-REPORT.md`
- `CHANGED-FILES.md` (this file)

**Every visual asset remained byte-for-byte unchanged.** No PNG, SVG master,
reduced-size test, contact sheet, generator source, font, page crop, or Field
Kit file was modified in this pass. Re-verified against the delivered v1.1
hashes: all 45 frozen files match (thumbnail, Images 01–06, the Image 01
1280×720 export, every reduced test, every SVG master, `assets.py` / `gumlib.py`
/ `finalize.py`, the page crops, the fonts, and the Field Kit PDF +
`build_fieldkit.py`).

**Archive:** the delivered `Capability_Formation_FieldKit_Gumroad_Assets_v1.1.zip`
is preserved; the reconciled set is delivered as
`Capability_Formation_FieldKit_Gumroad_Assets_v1.1.1.zip`, which differs from
v1.1 only in `QA-REPORT.md` and `CHANGED-FILES.md`.

---

## v1.1 amendment — Image 06 correction (individual-offer architecture)

Bounded correction to Image 06 only. The `$500` panel now describes the new
**Private Capability Position Read** individual offer.

**Right-panel stale-claim audit: YES, the old list contained stale
group-workshop claims.** Removed: `Guided evidence correction` (moved to the free
flagship), `Live facilitation`, `30-day follow-up`, `Supported 90-day rescore`
(group-workshop deliverables), and `Next-Move Decision` / `Interpreted state or
boundary` (retired with the list). These were flagged and reported before
regeneration; the approved 5-item replacement list contains only approved
private-offer claims.

**Files changed in v1.1:**
- `build/assets.py` — `build_06()` updated (offer name, descriptor, 5-item list, full decision rule)
- `masters/fieldkit_gumroad_06_fieldkit_vs_live_1600x900.svg`
- `png/fieldkit_gumroad_06_fieldkit_vs_live_1600x900.png`
- `reduced/fieldkit_gumroad_06_fieldkit_vs_live_640x360.png`
- `contact-sheet.png` (regenerated to show the corrected Image 06)
- `QA-REPORT.md`, `CHANGED-FILES.md` (this file)

**Typography:** the longer offer name fit the existing label area at the current
18px on one line — **no type-size reduction or line-break change was required**,
so no label typography adjustment needed documenting beyond this note.

**Files verified UNCHANGED (SHA-256 byte-for-byte, 22/22 OK):** the Field Kit PDF
and `build_fieldkit.py`; the thumbnail (PNG, SVG, 240, 180); Images 01–05 (PNG,
SVG, 640 each); and the Image 01 1280×720 export. No Field Kit production file
was touched.

**Archive:** the existing `Capability_Formation_FieldKit_Gumroad_Assets.zip` is
preserved; the corrected set is delivered as
`Capability_Formation_FieldKit_Gumroad_Assets_v1.1.zip`.

---

Scope: newly created production outputs only. This phase produced the Gumroad
merchandising system for the Capability Formation Field Kit. Nothing outside
`gumroad/` was created or modified.

## Source-integrity confirmation

**No existing Capability Formation Field Kit production file was modified or
overwritten.**

- `fieldkit/The_Capability_Formation_FieldKit.pdf` — untouched (git clean).
  md5 `f231ad6e101e36ae821600adec3d1fd6` (the committed v1.2.3 artifact).
- `fieldkit/build_fieldkit.py`, `fieldkit/fieldkit-source-v3.pdf`,
  `fieldkit/verify.py`, `fieldkit/README.md` — untouched (git clean).
- `diagnostic/` — untouched (git clean).

`git status` reports no modifications under `fieldkit/` or `diagnostic/`. All
entries below are new, additive files under `gumroad/`.

## Filename-conflict check

No prior Gumroad assets existed in the repository. No requested output filename
collided with an existing file, so no existing asset was preserved-and-versioned.
If a conflict had occurred, the existing file would have been preserved and the
new version created separately.

## New production outputs

### Final PNGs (`gumroad/png/`)
- `fieldkit_gumroad_thumbnail_600x600.png`
- `fieldkit_gumroad_01_recognition_1600x900.png`
- `fieldkit_gumroad_01_recognition_1280x720.png`  (Image 01 additional export)
- `fieldkit_gumroad_02_outputs_1600x900.png`
- `fieldkit_gumroad_03_product_proof_1600x900.png`
- `fieldkit_gumroad_04_evidence_method_1600x900.png`
- `fieldkit_gumroad_05_free_vs_fieldkit_1600x900.png`
- `fieldkit_gumroad_06_fieldkit_vs_live_1600x900.png`

### Editable vector masters (`gumroad/masters/`)
- `fieldkit_gumroad_thumbnail_600x600.svg`
- `fieldkit_gumroad_01_recognition_1600x900.svg`
- `fieldkit_gumroad_02_outputs_1600x900.svg`
- `fieldkit_gumroad_03_product_proof_1600x900.svg`
- `fieldkit_gumroad_04_evidence_method_1600x900.svg`
- `fieldkit_gumroad_05_free_vs_fieldkit_1600x900.svg`
- `fieldkit_gumroad_06_fieldkit_vs_live_1600x900.svg`

Masters are self-contained SVG: real Field Kit page crops are embedded as
images; type is set in the two production families (Cormorant Garamond, DM Sans),
shipped in `gumroad/fonts/` so the masters re-render exactly.

### Reduced-size readability tests (`gumroad/reduced/`)
- `fieldkit_gumroad_thumbnail_240x240.png`
- `fieldkit_gumroad_thumbnail_180x180.png`
- `fieldkit_gumroad_01_recognition_640x360.png`
- `fieldkit_gumroad_02_outputs_640x360.png`
- `fieldkit_gumroad_03_product_proof_640x360.png`
- `fieldkit_gumroad_04_evidence_method_640x360.png`
- `fieldkit_gumroad_05_free_vs_fieldkit_640x360.png`
- `fieldkit_gumroad_06_fieldkit_vs_live_640x360.png`

### Review artifact
- `gumroad/contact-sheet.png`  (all seven assets in order; review only, not a
  Gumroad production asset)

### Production fonts (`gumroad/fonts/`)
- `CormorantGaramond-Medium.ttf`, `CormorantGaramond-SemiBold.ttf`,
  `CormorantGaramond-Bold.ttf`, `DMSans-Regular.ttf`, `DMSans-Medium.ttf`,
  `DMSans-Bold.ttf`

### Build sources (`gumroad/build/`)
- `gumlib.py`, `assets.py`, `finalize.py` — the deterministic generator.
- `crops/` — real Field Kit page renders/crops used inside the masters.

No unexpected file changes occurred. If any had, they would be reported here as
a production failure rather than omitted.
