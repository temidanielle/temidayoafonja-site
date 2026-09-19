# Keep the Proof V2 — Production, QA & launch-readiness report

Prepared for Temidayo Afonja, The Density Group. Branch: `claude/keep-the-proof-v2-production`.

This is the return-before-launch report, updated after the final production corrections.
It covers everything built in the repo and every check that can be run without the live
store. Items that genuinely require you (Gumroad file upload, live purchase,
existing-customer re-download) are listed as owner-executed and cannot be done from this
environment (no Gumroad API; the egress proxy blocks gumroad.com and the live site).

---

## Final corrections applied in this round (your 10 items)

1. **Ownership / legal-sounding claims removed.** The boundary page no longer says "the
   account is yours to keep, and the artifact is not," and the "Yours to keep / Not
   yours" construction is gone. It now reads behaviorally: "keep your own high-level
   account of what you did, and do not copy employer-owned artifacts into your personal
   record." The ACCOUNT (your own high-level recollection) vs ARTIFACT (employer-owned
   material) distinction is preserved with no legal ownership conclusion about the
   account. "Softening the words … not whether it is yours to keep" → "…not whether you
   are permitted to keep it."
2. **Reconstruction language.** "These are the lawful places…" removed; the section is
   now "**Possible starting points for reconstruction**," ordered safest-first: your own
   recollection → information already public → other information only when you know you
   are permitted to use or retain it. Added explicitly: "Already possessing something
   does not, by itself, settle whether you may reuse or retain it," and "This guide does
   not attempt to resolve the specific rights that vary by employer or location." No
   source is labeled "lawful."
3. **Professional Record opening.** "Make one copy that belongs only to you, keep it
   somewhere you control and your employer does not own…" → "Make one personal copy,
   keep it in a personally controlled account rather than an employer-owned system, and
   add to it over time." Equivalent ownership wording softened in the handbook
   ("home you control"), Start Here, and the website card.
4. **Brand hierarchy.** "THE DENSITY GROUP" removed as the dominant eyebrow from the
   handbook cover and the Start Here opening. Customer-facing hierarchy is now
   KEEP THE PROOF → descriptor → the "for" line → Temidayo Afonja. The Density Group
   remains in copyright, footer, and the About the Author section. Capability Formation
   visual identity preserved. Cover PNG and OG image regenerated.
5. **Bundle simplification.** The `.md` is **not** shipped. Customer bundle is exactly
   four files. The `.md` mirror is kept internally at `production/source/` for
   portability/reproducibility. The customer's choice is simply Word (editable record)
   or PDF (print/fillable).
6. **Copy proof.** The "What happened?." punctuation error is fixed at its source (the
   `.md` generator was appending a period after a "?"-ending label). A full production
   proof was run across all customer files (see §13) — no doubled punctuation, malformed
   characters, broken quotes, stray internal markers, double spaces, duplicated words, or
   stale V1 terminology in the real copy.
7. **Start Here.** Orientation, the four labels (READ THIS FIRST / LEARN & BUILD / KEEP
   USING / PREFER PRINT OR A FORM?), and the two-way-in logic preserved; inventory now
   reflects the four customer files; brand hierarchy and ownership wording corrected.
8. **Gumroad.** Not published or updated. Price unchanged ($49), existing-product /
   permalink strategy unchanged. Handoff updated to the four-file bundle; the proposed
   description remains DRAFT / ready-to-paste for your review.
9. **Website.** Still staged (PR #120, not merged). Applied only the corrections above
   that touch V2 copy/bundle description (removed the "plain-text copy included" mention;
   softened "you own and control" → "you keep in a personally controlled account").
   Internal routing, $49, free/paid boundary, Field Kit seam, Starter seam, and the
   not-a-resume/interview positioning all preserved.
10. This report (§ below) is the final QA return.

---

## 1. Files created / changed (vs `origin/main`)

**Customer bundle (4 files, new):** `01_START_HERE.pdf`, `02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf`,
`03_YOUR_PROFESSIONAL_RECORD.docx`, `04_PRINTABLE_FILLABLE_TOOLS.pdf`.

**Internal (not shipped):** `production/source/03_YOUR_PROFESSIONAL_RECORD.md`,
`production/FINAL_MANUSCRIPT.md`, `DESIGN_NOTES.md`, `BUNDLE_AND_FORMAT_DECISIONS.md`,
`GUMROAD_AND_LAUNCH_HANDOFF.md`, this report, `scripts/*.py`, `renders/*`, and
`archive/v1_bundle/` (the three retired V1 files, archived not deleted). All under
`_build/`, which `netlify.toml` serves as 404.

**Website:** `keep-the-proof.html`, `career-evidence-starter.html`,
`og-keep-the-proof.png` (regenerated), `keep-the-proof-v2-cover.png` (regenerated).

## 2. Final bundle inventory (four files)

| # | File | Customer label | Format | Pages |
|---|------|----------------|--------|-------|
| 1 | 01_START_HERE.pdf | READ THIS FIRST | PDF | 2 |
| 2 | 02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf | LEARN & BUILD | PDF | **47** |
| 3 | 03_YOUR_PROFESSIONAL_RECORD.docx | KEEP USING | Word (.docx) | — |
| 4 | 04_PRINTABLE_FILLABLE_TOOLS.pdf | PREFER PRINT OR A FORM? | Fillable PDF | 8 |

The `.md` mirror is **internal only** (`production/source/`), not in the bundle.

## 3. Final handbook page count

**47 pages**, within the 44–56 ceiling, not padded.

## 4. Professional Record format + rationale

Shipped as **`.docx` only** (Word / Google Docs / Pages / LibreOffice; ISO OOXML;
copyable, searchable, no app or subscription lock-in). A `.md` plain-text mirror is kept
**internally** as source/backup and reproducibility artifact, generated from the same
field model, but is **not** shipped so the customer never has to choose among three
formats. Full reasoning: `BUNDLE_AND_FORMAT_DECISIONS.md`.

## 5. Career Evidence Ledger disposition

Retired from the active bundle; fields absorbed into the Professional Record. V1 files
archived at `_build/keep-the-proof-v2/archive/v1_bundle/`, not deleted.

## 6. Gumroad — before / after (owner-executed, not done here)

Before: "A 60-Minute Career Evidence System" (41-page handbook + 12-page Ledger + Start
Here). After: "A guided system for building your professional record" — the four-file
bundle, $49, evergreen. Paste-ready description, four-file upload list, cover, ethical-
influence rationale, and update-existing-product steps: `GUMROAD_AND_LAUNCH_HANDOFF.md`.
No invented testimonials, urgency, discounts, or scarcity; one price, $49.

## 7. Website — before / after

`/keep-the-proof` updated to V2 with design and internal routing preserved (on-page CTAs
still go to the Gumroad checkout; no other page's internal links converted to direct
Gumroad links). Hero, "What you receive" (four components), FAQ, format block, and CTAs
updated; before/after example uses the honest, number-free Proof Line. Free/paid and
not-a-resume/interview boundaries and the Field Kit seam preserved.

## 8. Starter page changes

Only stale paid-product references updated (dropped "60-minute system", "Career Evidence
System", "reusable Career Evidence Ledger"). Not redesigned or weakened.

## 9. All pricing occurrences

**$49** everywhere (three CTA buttons + hero price line on the website; Gumroad in the
handoff). No other price, discount, or "was $X" anywhere.

## 10. Old-descriptor occurrences — dispositioned

`keep-the-proof.html` and the body of `career-evidence-starter.html`: **0** remaining
V1 descriptors. Remaining "60-minute" matches elsewhere refer to the free live session
(a different offering) and are left as-is. Old cover images are unreferenced.

## 11. Existing-customer update method

Replace the V1 files on the **existing** Gumroad product (same permalink) so buyers'
libraries update to V2 at no charge, and opt into Gumroad's update notification with the
factual release note provided. No re-charge, no new permalink. Steps + draft email:
`GUMROAD_AND_LAUNCH_HANDOFF.md` §4.

## 12. Confirmations requested

- **`.md` is internal only:** confirmed — bundle contains exactly the four files above;
  the `.md` lives at `production/source/`.
- **Ownership claims dispositioned:** confirmed — "lawful places," "account is yours to
  keep," "Yours to keep / Not yours," "belongs only to you," and "you own and control"
  are removed from customer-facing copy. The only remaining "yours to keep" is the
  approved closing line "Keep the record while the facts are still yours to keep."
  (retained verbatim by your instruction); the only remaining "belongs to your employer"
  correctly describes employer-owned systems.
- **Punctuation / copy proof passed:** confirmed (see §13).

## 13. End-to-end QA results

**Automated (all PASS):**
- Bundle is exactly 4 files; page counts 2 / 47 / — / 8; `.md` absent from bundle,
  present internally.
- Content + copy proof on every customer file (both PDFs, the docx): **no** internal
  artifacts (LEGAL REVIEW / VISUAL / Stage 2 / counsel / "end of manuscript"), **no**
  stale V1 descriptors, **no** bracketed placeholders, **no** ownership/"lawful"
  phrases (beyond the approved closing line), **no** mojibake, **no** real doubled
  punctuation, space-before-punctuation, double spaces, or duplicated words. (The proof
  script's only flags were extraction artifacts from letter-spaced display headings and
  name initials like "Devin A.,"; confirmed against the manuscript source.)
- Fillable PDF: AcroForm present; 50 text fields + 19 checkboxes across 8 pages.
- `.docx` opens and validates (index table + fillable lines render).
- Website: 0 stale descriptors, 0 ownership phrases, no `.md`/plain-text mention, 3
  visible Gumroad CTAs (+1 JS constant), $49 present, V2 cover referenced.
- `netlify.toml`: `/keep-the-proof` rewrite and `/_build/*` 404 both present.
- Rendering verified by image: corrected cover (no Density Group eyebrow), the
  reconstruction page (conservative hierarchy), boundary copy (behavioral), Start Here
  (KEEP THE PROOF eyebrow, corrected KEEP USING card), website hero + bundle cards.
- Mobile: same responsive system as the live sibling pages.

**Owner-executed (cannot run here):** live Gumroad product state; real test purchase →
confirmation → download of all four files; existing-customer free re-download; live
`/keep-the-proof` after the PR is merged (a deploy preview is available now).

## Status

No material product issue is outstanding. Nothing was published; the $49 price and the
existing-product/permalink strategy are unchanged; PR #120 remains a draft and is not
merged. Awaiting your review of the final customer files and the actual Gumroad page
before launch.
