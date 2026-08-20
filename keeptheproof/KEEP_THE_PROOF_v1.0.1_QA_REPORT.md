# Keep the Proof - QA Report v1.0.1

**Build:** Version 1.0.1
**Author:** Temidayo Afonja, Founder and Principal, The Density Group
**Tooling:** ReportLab 5.0.1 (build), PyMuPDF 1.28.2 (render + inspect)
**Method:** Both PDFs were rebuilt from the generators, then inspected with
automated harnesses (`qa_content.py`, `qa_acroform.py`) and rendered page by
page for visual inspection. Blank and filled versions were both rendered and
inspected. No compiled PDF was hand-edited.

## Summary

| Area | Handbook | Ledger |
| --- | --- | --- |
| Pages | 39 | 11 |
| Bookmarks | 16 | 7 |
| AcroForm fields | 25 (all unique) | 117 (all unique) |
| Multiline fields | 22 | 50 |
| Content QA | PASS | PASS |
| AcroForm QA | PASS | PASS |
| Navigation / packaging QA | PASS | PASS |

All required checks passed. Nothing is labeled final with an open check.

## Visual QA

- Every page of both PDFs was rendered to PNG at readable resolution and
  inspected.
- **Covers:** both covers now display their full text in the existing visual
  system (motif, gold eyebrow, Cormorant title, rust rule, subtitle, byline,
  URL). The v1.0.0 blank-navy defect is resolved. Cover text is present in the
  source PDF, extracted text, and rendered PNG.
- No clipping, overlap, broken tables, missing glyphs, stranded headings,
  blank unintended pages, misplaced fields, or footer collisions were found.
- The warm-cream / deep-navy / muted-gold / restrained-rust system, Cormorant
  Garamond and DM Sans, and the ledger-mark motif are unchanged.

## Content QA

- Zero em dashes (U+2014) in customer-facing copy of either PDF.
- "resume" spelling preserved; no accented "résumé".
- No stale $75 Field Kit reference; no product pricing introduced.
- Permission rule consistent everywhere: "Permission comes before protection,"
  "A secure personal device does not make information yours to retain," the new
  CARE instruction, and "Generalizing information does not create permission"
  all present; the old "Generalize, seek permission" CARE wording is gone.
- Author positioning: "where talent decisions get made" present; "decide what
  people are worth" removed; "eighteen years" used, no "18 years"; boundary
  reads "a separate tool from The Density Group."
- Verifier wording: "Verifier role or permitted public reference" with the
  colleague-details helper present; old wording removed; the permitted-evidence
  helper present.
- Targeted voice replacements applied; "Permission comes first. Everything else
  is craft." appears exactly once (operating summary).
- All six composite examples present (Devin, Maya, Theo, Grace, Priya, Sam).
- No prohibited diagnostic, stay-or-leave advice, Career Portability Map, AI
  Role Relevance Audit, resume system, Density/Optionality scoring, or Four
  Career States content introduced. (The boundary page still correctly names
  these as out of scope.)
- No hard "page N" cross-references that could go stale after repagination.

## AcroForm QA

For each PDF: the field tree and every page widget were enumerated.

- Every widget belongs to a named field; every field name is unique
  (25 handbook, 117 ledger).
- Narrative fields carry the multiline flag (22 handbook, 50 ledger).
- Every widget sits within its page boundary.
- The print flag is set on every widget.
- Every field was filled with field-specific test content, using realistic
  multiline answers of roughly 150-300 characters in the principal narrative
  fields.
- The filled PDFs were saved and reopened: every value persists in the field,
  and every filled field has a valid appearance stream.
- Entering a value in one field never populated any unrelated field (unique
  names; verified with per-field sentinels - zero cross-field bleed).
- The filled pages were rendered and inspected: no clipping, unreadably small
  type, text collisions, or values in the wrong field. Principal narrative
  answers of ~300 characters display within their boxes without relying on
  scrolling.

## Navigation and packaging QA

- All bookmarks resolve to the correct pages (handbook 16, ledger 7).
- Web links work as PDF link annotations (handbook 39, ledger 11), all to
  https://temidayoafonja.com.
- Selectable text is intact (52,690 handbook characters; 7,058 ledger).
- The customer ZIP opens successfully and contains only the handbook PDF, the
  ledger PDF, and READ_ME_FIRST.txt. No test-filled or internal QA files are
  included.

## Determinism

Re-running the build with the same build-time stamp produces the same content.
The PDF's internal ModDate reflects the generation moment, so two builds with
identical content can differ at the byte level; compare at the content level.
