# Keep the Proof - Changelog v1.0.1

**Release:** Version 1.0.1 (controlled correction pass)
**Author:** Temidayo Afonja, Founder and Principal, The Density Group
**Status:** Unpublished. No website, Gumroad, YouTube, email, or social changes.

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
