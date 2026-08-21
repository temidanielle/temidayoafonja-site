# Keep the Proof - QA Report v1.0.1 (build RC2)

**Build:** Version 1.0.1, internal release candidate RC2
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
