# Keep the Proof — QA Report

Version 1.0.0 · Revised Monday, August 17, 2026 at 1:45 PM CT (America/Chicago)
Author: Temidayo Afonja, Founder and Principal, The Density Group

QA was run against the two shipping PDFs after the final build. Every page of both documents was rendered to image and inspected, and the automated checks below were run on the extracted text and structure.

---

## 1. Structural QA

| Check | Handbook | Ledger | Target | Result |
|---|---|---|---|---|
| Page count | 38 | 8 | 30–38 / 5–8 | PASS |
| Page size | 612×792 (US Letter portrait) | 612×792 | US Letter portrait | PASS |
| Selectable text | Yes (51,191 chars) | Yes (5,215 chars) | Selectable | PASS |
| Fillable form fields | 18 | 109 | Fillable | PASS |
| Duplicate field names | 0 | 0 | 0 | PASS |
| Working hyperlinks | 38 | 8 | Working links | PASS |
| Blank / stray pages | 0 | 0 | 0 | PASS |
| Stranded section headings | 0 | 0 | 0 | PASS |
| Orphaned table fragments | 0 | 0 | 0 | PASS |

Notes:
- The handbook's page count sits at the top of the 30–38 range. Five page breaks were converted to soft section gaps (keeping headings bound to their bodies via `keepWithNext`) to bring the document into range without crowding.
- One defect found and fixed during QA: the 20-row "what the full entry holds" table spilled two rows to a near-empty page; it was tightened onto a single page.
- One defect found and fixed during QA: two-column fillable fields (`two_up`) were placed at the wrong page coordinates because AcroForm ignores the Platypus canvas transform. Fixed by mapping each field's position through the current transformation matrix. Verified: all two-column fields now sit directly beneath their labels in both documents.

## 2. Voice and spelling QA

| Check | Handbook | Ledger | Result |
|---|---|---|---|
| Em dashes (—) | 0 | 0 | PASS |
| "résumé" / accented é | 0 | 0 | PASS (uses "resume" throughout) |
| Gendered pronouns for the author or personas | 0 | 0 | PASS (name + they/them; no guessed pronouns) |

En dashes appear only in numeric time ranges in the 60-minute setup table (e.g., "0–10 min"), which is correct typographic usage and not an em-dash substitute.

## 3. Content-requirement QA (handbook)

| Requirement | Result |
|---|---|
| Opening question (verbatim) | PRESENT |
| Category = "career evidence" | PRESENT |
| Five-part workflow Capture / Clarify / Translate / Protect / Retrieve | PRESENT (recurring strip, no acronym) |
| Two-Minute Quick Capture + Full Career Evidence Entry | PRESENT |
| Internal-to-portable translation + Proof Line builder | PRESENT |
| Six completed examples across the required functions | PRESENT (Devin, Maya, Theo, Grace, Priya, Sam) |
| At least two examples run through the full sequence | PRESENT (Maya; Theo runs Quick Capture → Full Entry → Proof Line → Retrieval Tag) |
| Confidentiality standard (verbatim) | PRESENT |
| Three visual tiers (KEEP / CARE / NEVER) | PRESENT |
| 60-minute setup | PRESENT |
| Monthly and quarterly routines | PRESENT |
| Retrieval guidance | PRESENT |
| Optional privacy-conscious AI prompt (rule-gated) | PRESENT |

## 4. Confidentiality / security coverage (handbook)

All fourteen required teachings verified present, including: personal-device/off-hours does not create permission; no forward/download/screenshot/print/upload/photograph/copy of employer material; never retain source code, credentials, security settings, customer or employee data, internal financials, privileged material, trade secrets, internal decks, or client materials; never paste confidential material into an AI system; when uncertain, omit and seek qualified advice; the guide is not legal advice; ask a manager, HR, or an attorney where permission matters.

## 5. Boundary / prohibited-content scan (handbook)

Zero occurrences of: Density/Optionality scoring, the Four Career States or their names (Compounding / Stagnant / Fragile / Depth Trap) used as a framework, career-state assessment, stay-or-leave or move-plan advice (the phrase "stay or leave" appears only inside the explicit "does not answer" exclusion list), resume-writing system, interview coaching, networking scripts, salary or job-search content.

## 6. Originality scan (handbook)

Zero occurrences of the referenced competitor work's distinctive phrases ("Responsibilities vs. Results," "Task vs. Ownership," "Career Playbook") and prohibited frameworks. "brag document" appears once, within its allowance. See the Originality Reconciliation for detail.

## 7. Metadata QA

| Field | Handbook | Ledger |
|---|---|---|
| Title | Keep the Proof: A 60-Minute Career Evidence System | Career Evidence Ledger: The reusable companion to Keep the Proof |
| Author | Temidayo Afonja | Temidayo Afonja |
| Subject / keywords | Set | Set |
| Version + timestamp | On the copyright page, not the cover | On the how-to-use page, not the cover |

## 8. Form-function QA

- All 18 handbook fields and 109 ledger fields are AcroForm text fields with the print flag set, unique names, gold borders, and a soft fill.
- Field positions were verified against their printed labels page by page after the coordinate fix.
- Note on limitation: the fields are standard interactive text fields. They accept typing and print with the page. They are not scripted to auto-calculate totals (there are no numeric totals in these forms), so no viewer-dependent JavaScript is relied upon.

## 9. Legal-review flags

These are content decisions an advisor or attorney may wish to confirm before sale, none of which are defects:

1. The product makes confidentiality claims about what a purchaser may and may not retain. The language is deliberately conservative and repeatedly defers to the purchaser's own agreements, HR, and counsel, but it is general and cannot account for every jurisdiction or contract.
2. The "not legal advice" disclaimer appears on the copyright page and again in the information-risk section. Confirm placement and wording meet the seller's preference.
3. The six personas are fictional composites. Confirm the disclaimer that examples are illustrative is sufficient for the seller's comfort.
4. The optional AI prompt is gated by an explicit rule against entering confidential material. Confirm the seller is comfortable including any AI guidance at all.

## 10. Overall

Both documents pass structural, voice, content, confidentiality, boundary, originality, metadata, and form-function QA. No open defects. The items in section 9 are review flags for a human decision-maker, not build errors.
