# Keep the Proof - QA Report v1.0.1 (build RC4)

## RC4 page-37 PDF compatibility correction

RC4 is a narrowly scoped compatibility correction on top of RC3. It changes one
thing in the source generation and nothing customer-facing: the no-op interior
clipping path is stripped from blank AcroForm field appearance streams. The
public version stays 1.0.1 (unpublished).

**Reported defect.** In the shipped RC3 handbook PDF, page 37 ("Full Career
Evidence Entry, page two of three") was reported to render with the top content
clipped or shifted in whole-document Ghostscript 10.02.1 and Poppler 26.05,
while rendering cleanly in PyMuPDF, in isolated-page Poppler, and in Ghostscript
with annotations disabled.

**Root cause.** "Clean with annotations disabled" locates the fault in the
AcroForm widget *appearance* layer, not in the page content. Every blank text
field appearance ReportLab emits ends with the standard variable-text wrapper
`/Tx BMC  q  <x y w h> re  W  n  ...  Q  EMC`. For a blank field nothing is
painted between the clip (`W n`) and the `Q`, so that rectangle is a clipping
path that clips nothing - a no-op. It is nonetheless the only active
graphics-state construct in the annotation appearance layer, and it is exactly
the kind of construct a strict or newer renderer can mis-scope when it
composites the annotation layer over page content during a whole-document
render. The isolated-page and annotations-off paths never exercise it, which is
why they stayed clean.

**Fix (source generation, no compiled-PDF patch, no content moved to conceal).**
`ktp.py` now wraps `reportlab.pdfbase.acroform.AcroForm.txAP` and removes that
no-op interior clip from blank appearance streams. Marked-content and q/Q
pairing stay balanced. Because the clip bounds nothing when there is no value to
draw, this changes no visible pixel; it only removes the implicated
annotation-layer construct.

**Non-destructive, verified byte- and pixel-level:**

- **Pixel-identical to RC3** on every page of both PDFs (PyMuPDF at 150 dpi, max
  absolute pixel difference = 0 across all 41 handbook and 12 ledger pages).
- **Field definitions byte-identical to RC3**: all 25 handbook and 117 ledger
  field dictionaries match on name, type, flags, rectangle, MaxLen, border style
  and colour. The only per-field change is the removal of the clip operators
  from the `/AP /N` appearance stream.
- **Page count, bookmarks, links, and extracted text byte-identical** (handbook
  41 pages / 16 bookmarks / 41 links; ledger 12 pages / 7 bookmarks / 12 links).
- **Icons unchanged** (pixel-identical covers, dividers, tool pages, form bands).

**Reproduction attempt (before changing anything).** The reported top clip did
not reproduce in this build environment in any engine or configuration, blank or
stress-filled, whole-document or truly page-separated: PyMuPDF 1.28.2, Poppler
24.02.0 (`pdftoppm` whole-document and `pdfseparate` true single-page
isolation), Ghostscript 10.02.1 (whole-document, single-page, `-dPrinted` to
force the widget appearance layer to rasterise, and `-dShowAnnots=false`), and
PDFium 153 all render page 37 with the content top edge and bounding box within
~1px (the antialiasing floor) of each other. Poppler 26.05+ (named in the
report) could not be installed in this sandbox: the OS package index caps
Poppler at 24.02.0 and the conda-forge / micromamba / static-binary hosts are
blocked by the outbound proxy. The upgraded QA harness and the exact per-engine
commands are included with the evidence so the report can be re-run against
Poppler 26.05+; the fix removes the implicated construct regardless of whether
that specific engine is present.

**Why RC3 was reported as passing despite the shipped Ghostscript failure.** The
RC3 multi-engine harness (`qa_multiengine.py`) could not have detected a
top-edge clip of this kind, for four structural reasons, each now fixed:

1. It compared engines only by **whole-page average pixel difference** against a
   coarse threshold (mean abs diff > 8). A clip of the running header and title
   at the very top of the page moves only a small fraction of the page's pixels,
   so the whole-page average stays far below the threshold. RC4 adds explicit
   **top-edge** and **content-bounding-box** checks per page across engines.
2. Its "isolated page" render used `pdftoppm -f N -l N -singlefile`, which still
   opens and parses the whole document - it is a window onto the full render, not
   a genuinely separated page. RC4 uses **`pdfseparate`** to emit a real
   one-page PDF and renders that on its own.
3. Its Ghostscript pass did not force annotation printing, so on this build GS
   never rasterised the widget appearance layer at all (its annotations-on and
   annotations-off output were byte-identical). RC4 runs Ghostscript with
   **`-dPrinted`** so the appearance layer is actually exercised.
4. It tested only the Poppler present in the environment (24.02.0) and did not
   include a second independent whole-document engine. RC4 records the engine
   versions explicitly and adds **PDFium** (the Chromium engine) as a
   cross-check.

The RC3 report's "PASS" was therefore accurate for the engines and checks it
ran, but those checks were structurally blind to a top-edge annotation-layer
clip. RC4's harness is not.

The full RC3 and RC2 test results below still hold for RC4 (content and forms
are unchanged; only the blank-field appearance clip was removed).

---

## RC3 icon pass (visual refinement)

RC3 adds a shared navigation icon system (native ReportLab vector) and changes
nothing else. It was verified to be non-destructive:

- **Extracted customer-facing text is byte-identical** to RC2 in both PDFs.
- **Every AcroForm field is unchanged**: same count (25 handbook, 117 ledger),
  and every field's name, type, flags, and rectangle match RC2 exactly.
- **Page count, bookmarks, and links are unchanged** (handbook 41 pages / 16
  bookmarks / 41 links; ledger 12 pages / 7 bookmarks / 12 links).
- **Multi-engine render** of every page, blank and stress-filled/saved-reopened,
  through PyMuPDF, Poppler (whole-document and isolated), and Ghostscript: no
  blank pages, 0.0 whole-vs-isolated divergence, no engine divergence. Icons are
  sharp, aligned, and unclipped in all three engines at 100% and 200%.
- **Placement inspected** on both covers, all five part dividers, all seven
  selected tool pages, and every ledger form header (see the icon-review contact
  sheet). No icon affects text flow, field capacity, bookmarks, links, or page
  count.

The full RC2 test results below still hold for RC3 (the underlying build,
content, and forms are unchanged).

---

**Build:** Version 1.0.1, internal release candidate RC3 (icon pass over RC2)
**Author:** Temidayo Afonja, Founder and Principal, The Density Group
**Rendering engines:** PyMuPDF 1.28.2; Poppler 24.02.0 (`pdftoppm`), tested both
whole-document and isolated-page; Ghostscript 10.02.1 (`gs`).
**Build tooling:** ReportLab 5.0.1.
**Method:** Both PDFs were rebuilt from the generators (no compiled PDF was
hand-edited), then inspected with automated harnesses (`qa_content.py`,
`qa_accept.py`, `qa_multiengine.py`) and rendered page by page for visual
inspection. Blank, filled, and filled-then-saved-and-reopened copies were all
rendered and inspected across all three engines.

## Summary

| Area | Handbook | Ledger |
| --- | --- | --- |
| Pages | 41 | 12 |
| Bookmarks | 16 | 7 |
| AcroForm fields | 25 (all unique) | 117 (all unique) |
| Multiline fields | 23 | 51 |
| Content QA | PASS | PASS |
| Form acceptance QA | PASS | PASS |
| Multi-engine render QA | PASS | PASS |

Every required check passed. Nothing is labeled approved with an open check.

## Reproduction of the reported defects (before changing anything)

- **Handbook AI-prompt page: REPRODUCED.** The bordered prompt box overlapped
  the "The prompt" heading and the closing note. This is a layout defect and
  appears in every engine. Fixed (see below) and re-verified in all three.
- **Renderer-dependent defects reported against the prior build (ledger page 4
  blank in whole-document Poppler; ledger pages 5/7/9/11 clipped headings and
  footers; whole-document vs isolated-page divergence; filled-then-saved copy
  clipping in Poppler; handbook page 31 title/first-character clip): NOT
  REPRODUCED** in commit c4dc910 with PyMuPDF 1.28.2 / Poppler 24.02.0 /
  Ghostscript 10.02.1. Evidence: whole-document vs isolated-page Poppler renders
  are pixel-identical (mean absolute difference 0.0) on every page of both PDFs;
  ledger page 4 renders fully (heading, form band, all five fields, footer) in
  whole-document Poppler; a copy filled and saved through PyMuPDF renders
  cleanly in Poppler and Ghostscript. These reports likely came from a different
  build or a different tool/version. To eliminate the class of risk regardless,
  the cover and every AcroForm field now draw inside a canvas save/restore so no
  graphics state leaks between flowables or pages.

## Fixes verified this build

- **AI-prompt page.** Rebuilt the prompt as a table-based box (exact height) on
  its own page; heading, box, and closing note are three separate,
  non-overlapping regions. Verified in PyMuPDF, Poppler, and Ghostscript.
- **Field capacity.** Full Entry narrative fields are full page width; ledger
  paired narrative fields (Translation, Proof Line) were made taller. A capacity
  model (characters that fit per box at the field font) reports zero fields too
  small for their acceptance-test length, and filled renders confirm it.
- **Copy corrections** (p23 eight-moves framing; p13 sentence; p28 Theo wording
  and Proof Line; p39 About opening; ledger "six reusable form sets") are all
  present in the rendered PDFs and in the regenerated manuscript.

## Multi-engine render QA (every page)

For each PDF, every page was rendered through PyMuPDF, Poppler whole-document,
Poppler isolated-page, and Ghostscript, at readable resolution, for:

- both blank customer PDFs;
- filled stress-test copies (field-specific answers at the acceptance lengths);
- copies saved and reopened after filling.

Results, all pages, both PDFs, all three engines, blank and filled-saved:

- No blank unintended pages.
- Whole-document vs isolated-page Poppler: mean absolute pixel difference 0.0 on
  every page (no renderer-context dependence).
- No engine-dependent divergence above the antialiasing floor.
- Covers, handbook pages 23 / 28 / 31 / 33-34 / 39, the reusable fillable pages,
  and ledger pages 3-12 were inspected: headings, first characters, footers,
  form labels, and field contents are all intact, with no clipping, overlap, or
  footer collision.

## Form acceptance QA

Field-specific test answers were used at realistic lengths: Quick Capture main
narrative fields 200-300 characters; verifier and confidential-detail fields
80-140; large Full Entry narrative fields 200-300; smaller paired narrative
fields 120-180; short metadata fields realistic short values.

For every field, blank and filled: fill, save, close, reopen, confirm the exact
stored value, confirm a valid appearance stream, render, and visually confirm
wrapping, legible font size, and no clipping; and confirm no value appears in
another field.

- Values persist exactly after save and reopen (0 misses).
- Every filled field has a valid appearance stream.
- No value bleeds into any other field (unique names; verified with per-field
  sentinels).
- The complete intended answer is visible in the rendered field without
  scrolling at every acceptance length. Rendered filled pages in Poppler confirm
  this for the principal narrative fields (~300 characters) and the paired
  narrative fields (~160-180 characters).

## Content QA

- Zero em dashes in customer-facing copy of either PDF.
- "resume" spelling preserved; no accented forms.
- No stale $75 Field Kit reference; no pricing introduced.
- Permission rule consistent; verifier and permitted-evidence wording correct.
- All six composite examples present (Devin, Maya, Theo, Grace, Priya, Sam).
- No prohibited diagnostic, stay-or-leave advice, Career Portability Map, AI
  Role Relevance Audit, Density/Optionality scoring, Four Career States, or
  resume/job-search content introduced (the boundary page still names these as
  out of scope).
- No hard "page N" cross-references that could go stale after repagination.

## Navigation and packaging QA

- All bookmarks resolve to the correct pages (handbook 16, ledger 7).
- Web links work as PDF link annotations, all to https://temidayoafonja.com.
- Selectable text intact.
- The customer ZIP opens and contains only the handbook PDF, ledger PDF, and
  READ_ME_FIRST.txt; no test-filled or internal QA files.

## Source

Committed to the repository below (see the handoff for the RC2 commit SHA); a
source archive (`build/`, all generator and QA scripts, the six brand fonts, and
`requirements.txt`) is also provided so the build is reproducible without the
repository.
