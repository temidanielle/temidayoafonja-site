# Keep the Proof - Changelog v1.0.1

**Release:** Version 1.0.1 (controlled correction pass)
**Author:** Temidayo Afonja, Founder and Principal, The Density Group
**Status:** Unpublished. No website, Gumroad, YouTube, email, or social changes.

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
