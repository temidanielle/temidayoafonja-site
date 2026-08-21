# Keep the Proof - Changelog v1.0.1

**Release:** Version 1.0.1 (controlled correction pass)
**Author:** Temidayo Afonja, Founder and Principal, The Density Group
**Status:** Unpublished. No website, Gumroad, YouTube, email, or social changes.

---

## RC5 release-gate closure (Poppler 26.05+ confirmation, no product change)

The page-37 Poppler 26.05+ gate was exercised in CI (the local environment caps
Poppler at 24.02.0). A GitHub Actions job in an Arch Linux container
(`.github/workflows/poppler-p37.yml`) running Poppler 26.07.0 rendered the
shipped RC5 handbook page 37 blank and stress-filled, whole-document and
`pdfseparate` truly-isolated, annotations on and hidden. In every mode the
content top edge and bounding box matched the approved PyMuPDF reference within
1px - no clipping, no shift. VERDICT: PASS (run 32530971761).

Both release gates are now passed: Adobe Acrobat Reader field-capacity
acceptance (product owner, 2026-08-21) and Poppler 26.05+ page-37 rendering
(Poppler 26.07.0 in CI, 2026-08-21). No product PDF was modified. Public version
remains 1.0.1; nothing has been published.

---

## RC5 packaging refinement (customer bundle, no product rebuild)

A packaging-only change; neither product PDF was modified or rebuilt (both remain
byte-identical, hashes unchanged).

- Replaced the plain-text `READ_ME_FIRST.txt` with a one-page orientation PDF,
  `KEEP_THE_PROOF_START_HERE_v1.0.1.pdf`, built in the handbook visual language
  (warm ivory ground, navy type, restrained gold accents, the approved line-icon
  style; no large cover icon). It renders cleanly with no clipping, overflow, or
  broken icons across PyMuPDF, Ghostscript, Poppler, and PDFium, and carries the
  footer "Keep the Proof v1.0.1 | For the purchaser's personal use."
- The customer bundle `KEEP_THE_PROOF_CUSTOMER_BUNDLE_v1.0.1.zip` now contains
  exactly three purchaser-facing files: the handbook PDF, the Career Evidence
  Ledger PDF, and the Start Here PDF. `READ_ME_FIRST.txt` was removed. No source,
  QA, or internal materials are in the bundle.
- Public version remains 1.0.1, unpublished. No website, Gumroad, or
  live-delivery change was made.

---

## Internal build RC5 (interactive field-capacity correction, on top of RC4)

The public version stays 1.0.1 (not distributed). RC5 corrects a release blocker
in the interactive fields and adds interactive acceptance testing. It changes
field behaviour only.

Defect and acknowledgement:
- Every fillable field inherited ReportLab's default `/MaxLen` of 100, capping
  typed input at 100 characters in fields designed for 200-300+ character
  answers. The RC1-RC4 acceptance tests set values through the PDF API, which
  does not enforce `/MaxLen`, so they confirmed only that a stored value
  round-trips and never established whether a person could type the required
  amount. RC5 treats typeability as its own criterion.

Fix (source generators only; no compiled PDF patched):
- `ktp.py` assigns a deliberate per-field `/MaxLen` from a capacity map
  (`field_specs`), never a blanket value: full narrative / evidence >= 300
  (MaxLen 600); medium narrative >= 180 (360); verifier / confidentiality /
  supporting detail >= 140 (280); short single-line metadata sized per field.
  `/MaxLen` is always >= the intended acceptance length, with headroom on
  scrolling multiline fields. The full per-field map ships as the RC5
  Field-Capacity Manifest (.md and .csv).

Verification:
- Pixel-identical to RC3/RC4 on every page of both PDFs (max abs pixel diff 0);
  only interactive-field behaviour changed. Field names, rectangles, multiline
  flags, page count, bookmarks, links, extracted text and icons unchanged. The
  RC4 page-37 appearance-clip mitigation is preserved.
- All 142 fields filled at their intended acceptance length persist exactly
  after save and reopen (0 truncated). Filled page 37 renders without clip or
  shift across PyMuPDF, Ghostscript `-dPrinted`, Poppler and PDFium, whole-doc
  and `pdfseparate`-isolated.
- Adobe Acrobat Reader keystroke entry is a manual release gate and is not
  reported as passed.

Automated QA:
- New `qa_maxlen.py` fails the build when a field's `/MaxLen` is below its
  documented acceptance length, a narrative field is left at the default 100, a
  required multiline field is not multiline, a stress value is truncated after
  save/reopen, or field names / rectangles / multiline flags / counts drift from
  the committed baseline. PASSES on RC5; FAILS on the RC4 PDFs (148 findings).

Page 37: targeted mitigation implemented and non-regressive across tested
engines; confirmation on Poppler 26.05+ remains pending (still uninstallable in
this environment). Root cause not called conclusively confirmed until that
environment is exercised.

Release status: not yet approved for publication. Gate (1) interactive
field-capacity acceptance in Adobe Acrobat Reader is PASSED (product-owner
confirmation, 2026-08-21: long multiline and short fields, save/close/reopen
persistence, editability, and handbook page 37 all verified). The only open gate
is (2) a successful page-37 test on Poppler 26.05+. No website, Gumroad, or
live-delivery change was made.

Metrics unchanged: handbook 41 pages / 16 bookmarks / 25 unique fields (23
multiline); ledger 12 pages / 7 bookmarks / 117 unique fields (51 multiline).

---

## Internal build RC4 (page-37 PDF compatibility correction, on top of RC3)

The public version stays 1.0.1 (not distributed). RC4 is a narrowly scoped
compatibility correction. It changes one thing in the source generation and
nothing customer-facing.

Reported defect:
- Independent QA reported the shipped RC3 handbook page 37 ("Full Career
  Evidence Entry, page two of three") rendering with clipped or shifted top
  content in whole-document Ghostscript 10.02.1 and Poppler 26.05, while
  rendering cleanly in PyMuPDF, in isolated-page Poppler, and in Ghostscript
  with annotations disabled.

Root cause and fix:
- Clean-with-annotations-disabled locates the fault in the AcroForm widget
  appearance layer. Every blank text-field appearance ReportLab emits ends with
  the standard variable-text wrapper `/Tx BMC q <rect> re W n ... Q EMC`; for a
  blank field nothing is drawn between the clip and the restore, so that
  rectangle is a clipping path that clips nothing - a no-op, but the only active
  graphics-state construct in the annotation appearance layer, and the kind of
  construct a strict or newer renderer can mis-scope when compositing
  annotations over page content in a whole-document render.
- `ktp.py` now wraps `reportlab.pdfbase.acroform.AcroForm.txAP` and strips that
  no-op interior clip from blank appearance streams (marked-content and q/Q
  pairing stay balanced). No compiled PDF was patched; no page content was moved
  to conceal anything.

Verification:
- Pixel-identical to RC3 on every page of both PDFs (PyMuPDF at 150 dpi, max
  absolute pixel difference 0 across all 41 + 12 pages).
- All 25 handbook and 117 ledger field dictionaries are byte-identical to RC3
  (name, type, flags, rectangle, MaxLen, border style and colour); the only
  per-field change is removal of the clip operators from the appearance stream.
- Page count, bookmarks, links, extracted text, and all icons unchanged.
- The reported clip did not reproduce in this environment in any engine
  (PyMuPDF 1.28.2; Poppler 24.02.0 whole-document and pdfseparate-isolated;
  Ghostscript 10.02.1 whole/single-page/`-dPrinted`/annotations-off; PDFium
  153), blank or stress-filled. Poppler 26.05+ could not be installed here (OS
  package index caps at 24.02.0; conda-forge and binary hosts are proxy-blocked).
  The fix removes the implicated construct regardless.

QA harness upgrade (why RC3 passed despite the shipped failure):
- The RC3 harness judged engines by whole-page average pixel difference against
  a coarse threshold, used `pdftoppm -f/-l -singlefile` (a window on the full
  document, not a separated page), did not force Ghostscript to rasterise the
  annotation layer, and tested only the installed Poppler. Each is structurally
  blind to a top-edge annotation-layer clip. `qa_multiengine.py` now adds
  explicit top-edge and content-bounding-box checks, true `pdfseparate`
  isolation, Ghostscript `-dPrinted`, and a PDFium cross-check.

Metrics unchanged: handbook 41 pages / 16 bookmarks / 25 unique fields (23
multiline); ledger 12 pages / 7 bookmarks / 117 unique fields (51 multiline).

---

## Internal build RC3 (icon-system refinement, on top of RC2)

The public version stays 1.0.1 (not distributed). RC3 is a controlled visual
refinement that introduces a restrained, consistent navigation icon system. No
customer-facing copy, typography, page dimensions, page count, form definitions,
field names/flags/coordinates, bookmarks, links, headers, footers, or product
scope changed. All icons are native ReportLab vector geometry (no emoji,
Unicode, icon font, or raster), built as shared functions in `ktp.py` so the
handbook and ledger use one system, each drawn inside a canvas save/restore.

- **Cover mark.** The old three-horizontal-line motif (which read like a menu
  symbol) is replaced on both covers by a stacked evidence-card mark: two offset
  outlined record cards, a short gold proof line on the front card, and a small
  rust tab accent. Title hierarchy and all other cover positioning are unchanged.
- **Part dividers.** A rust badge (~0.43 in, cream line icon) sits above each
  PART label, left-aligned: Part One record + magnifier; Part Two shield + check;
  Part Three form + pencil; Part Four layered cards; Part Five calendar + loop.
- **Handbook tool pages.** A smaller rust chip in the same icon language sits at
  the top-right of seven pages: p16 clock + pencil, p17 form card, p23 translate
  arrow, p24 proof lines, p30 60-minute clock, p31 calendar loop, p32 record +
  magnifier. One icon per page.
- **Ledger form bands.** A small cream line icon sits at the far-right of each
  navy form-title band (Quick Capture, Full Entry, Translation, Proof Line,
  Monthly Sweep, Quarterly Review), repeated across a form's pages; the Evidence
  Index, which uses a column-header row rather than a single-title band, carries
  its record + magnifier icon at the title. The band's icon cell is sized so the
  band height, and every field coordinate below it, is unchanged.

Icons are placed with a zero-height `IconMark` flowable and a fixed-size
`IconCell`, so nothing shifts. Verified: extracted customer-facing text, every
AcroForm field name/type/flag/rectangle, page count, bookmarks, and links are
byte-identical to RC2. Blank and stress-filled/saved-and-reopened PDFs render
cleanly through PyMuPDF, Poppler (whole-document and isolated), and Ghostscript
with no blank pages and no engine divergence. An icon-review contact sheet
accompanies this build.

Metrics unchanged: handbook 41 pages / 16 bookmarks / 25 unique fields; ledger
12 pages / 7 bookmarks / 117 unique fields.

---

## Internal build RC2 (release candidate, on top of v1.0.1)

The public version stays 1.0.1 (not distributed). RC2 is an internal
release-candidate build that fixes defects independent QA found and adds
multi-engine rendering QA.

Fixed:
- **Handbook AI-prompt page (was p33).** The prompt box was a bordered
  Paragraph whose drawn box exceeded its measured height, so it overlapped the
  "The prompt" heading above it and the closing note below it. Rebuilt the box
  as a table (exact height) and moved the whole AI-prompt section onto its own
  page, so the heading, the box, and the closing note occupy three separate,
  non-overlapping regions.
- **Multiline field capacity.** Every narrative field in the Full Entry is now
  full page width, and the ledger's paired narrative fields (Translation, Proof
  Line) were made taller, so a realistic answer at the acceptance-test lengths
  (120-300 characters) is fully visible without scrolling. The Full Career
  Evidence Entry is now three pages in both the handbook and the ledger.

Copy corrections:
- p23: heading is "Eight translation moves, plus one protection rule," with a
  matching introduction and the callout "Why the last line is different"
  ("The first eight moves make your work clearer. The last one keeps you safe.")
  - the nine-row table is now correctly framed as eight moves plus one rule.
- p13: "You will lose a little detail this way. You will never lose your
  standing." is now "You may lose some detail this way, but you will keep the
  record accurate and defensible."
- p28 (Theo): "A likely exposure was prevented before the excess access could
  be used."; "The excess access was removed, and the process gap that allowed
  it was closed."; the Proof Line is a full sentence beginning "During a routine
  access review, I found and corrected..." Cautious language preserved.
- p39 (About): now opens "For eighteen years, Temidayo has worked across..."
- Ledger: "six reusable form sets" on the cover and the introductory page.

Hardening:
- The cover and every AcroForm field now draw inside a canvas save/restore, so
  no translated or dirty graphics state can leak into later content and produce
  renderer-dependent output.

QA:
- Every page of both PDFs, blank and filled-and-reopened, was rendered through
  PyMuPDF, Poppler (pdftoppm, whole-document and isolated-page), and
  Ghostscript. Zero blank pages, zero whole-document-vs-isolated divergence, and
  no engine-dependent divergence. See the QA report for details, including the
  finding that the previously reported renderer-dependent defects do not
  reproduce in this build.

Metrics after RC2: handbook 41 pages / 16 bookmarks / 25 unique fields;
ledger 12 pages / 7 bookmarks / 117 unique fields.

---

## v1.0.1 (initial correction pass)

This is a controlled correction and QA pass on top of v1.0.0. The product's
scope, five-part architecture, five-step workflow, six composite examples,
visual identity, fonts, and central teaching are unchanged. The v1.0.0 files
are preserved unchanged; every v1.0.1 change ships in new, separately named
files rebuilt from the generators (no compiled PDF was hand-patched).

## Fixed

- **Both covers were rendering as blank dark-navy pages.** Root cause: the
  cover flowable drew at absolute page coordinates while ReportLab's
  `Flowable.drawOn` translated the canvas to the frame cursor, pushing every
  string a full page height off the top. Fixed by drawing the cover on the
  untranslated canvas. Both covers now show their full approved hierarchy in
  the existing visual system, verified in extracted text and rendered PNG.

## Changed - permission language

- CARE tier instruction is now "Seek permission, use only what is already
  public, or leave it out." The prior wording that presented generalizing as
  an independent solution was removed.
- Added near the tiers: "Generalizing information does not create permission.
  Use generalized wording only after you have confirmed that you are permitted
  to retain the underlying information."
- Permission-before-protection is reinforced consistently across the handbook,
  ledger, worked forms, operating summary, and READ_ME.

## Changed - author positioning

- "organizations decide what people are worth" is replaced with "where talent
  decisions get made" in the Welcome and the About copy.
- "eighteen years" is used in prose (no "18 years"). About copy now reads that
  Temidayo has spent eighteen years across Big Four consulting, life sciences,
  and technology, close to where talent decisions get made.
- Boundary page: "a separate tool of Temidayo's" is now "a separate tool from
  The Density Group." The Capability Formation Field Kit is referenced without
  a price (no stale $75; no new pricing introduced).

## Changed - verifier and evidence-reference wording

- The verifier prompt is now "Verifier role or permitted public reference,"
  with helper text "Use a role or public source. Do not store a colleague's
  personal details." The old "A person or public fact that could verify this"
  wording is gone.
- The Full Entry's permitted-evidence field now reads "Name the permitted
  source or location. Do not paste the artifact or confidential content here."

## Rebuilt - forms

- **Quick Capture** is now one per page with five true-multiline fields: the
  first three have generous space; the verifier and confidential-detail fields
  hold at least two lines. The ledger's old A/B two-per-page layout is removed.
- **Full Career Evidence Entry** is now a two-page, twenty-field form with each
  taught field separated (no forbidden combinations). It is identical in
  wording, order, and logic in the handbook and the ledger, built from one
  shared definition in the engine.
- **Every reusable ledger form** had its narrative fields converted to tall
  multiline fields (Translation, Proof Line support, Monthly and Quarterly
  reflections, and others). Short metadata fields remain single-line.

## Added - navigation

- Real PDF bookmarks. Handbook: cover, Welcome, Orientation, the five Parts,
  and the principal tools and summaries (16 total, two levels). Ledger: the
  seven reusable forms (7 total). Working web links preserved.

## Changed - voice (targeted only)

- "Evidence survives scrutiny. Bragging does not." -> "Evidence holds up when
  it gives someone else something concrete to examine."
- "Effort is input. Outcome is evidence." -> "When recording the work, include
  the effort where it adds useful context and describe the outcome or
  observable change."
- "Permission comes first. Everything else is craft." is kept once, in the
  operating summary.

## Versioning

- All visible and internal version references moved from 1.0.0 to 1.0.1:
  copyright/version lines, PDF metadata keywords, READ_ME, master manuscript,
  build documentation, and this changelog and QA report. No stale page
  references remain after the pagination changes.

## Metrics

| Deliverable | Pages (was) | Bookmarks (was) | Form fields (was) |
| --- | --- | --- | --- |
| Handbook | 39 (38) | 16 (0) | 25 unique, 22 multiline (18 unique, 0 multiline) |
| Ledger | 11 (8) | 7 (0) | 117 unique, 50 multiline (109 unique, 5 multiline) |

Page and field counts grew because usability (one capture per page, a real
two-page Full Entry, multiline narrative fields) was prioritized over the old
38-page and 8-page limits, as the brief allows.
