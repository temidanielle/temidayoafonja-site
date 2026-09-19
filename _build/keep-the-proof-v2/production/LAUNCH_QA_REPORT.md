# Keep the Proof V2 — Production, QA & launch-readiness report

Prepared for Temidayo Afonja, The Density Group. Branch: `claude/keep-the-proof-v2-production`.

This is the return-before-launch report. It covers everything built in the repo and
every check that can be run without the live store. The items that genuinely require
you (Gumroad file upload, live purchase, existing-customer re-download) are listed as
owner-executed and cannot be done from this environment (no Gumroad API; the egress
proxy blocks gumroad.com and the live site).

---

## 1. Exact files created / changed (vs `origin/main`)

**Customer bundle (new):**
- `_build/keep-the-proof-v2/production/bundle/01_START_HERE.pdf`
- `_build/keep-the-proof-v2/production/bundle/02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf`
- `_build/keep-the-proof-v2/production/bundle/03_YOUR_PROFESSIONAL_RECORD.docx`
- `_build/keep-the-proof-v2/production/bundle/03_YOUR_PROFESSIONAL_RECORD.md`
- `_build/keep-the-proof-v2/production/bundle/04_PRINTABLE_FILLABLE_TOOLS.pdf`

**Production sources & records (new):**
- `.../production/FINAL_MANUSCRIPT.md` (cleaned reader-facing manuscript)
- `.../production/DESIGN_NOTES.md` (internal; extracted VISUAL guidance)
- `.../production/BUNDLE_AND_FORMAT_DECISIONS.md`
- `.../production/GUMROAD_AND_LAUNCH_HANDOFF.md`
- `.../production/LAUNCH_QA_REPORT.md` (this file)
- `.../production/scripts/*.py` (reproducible build scripts)
- `.../production/renders/*` (HTML + review contact sheets)

**V1 archived, not deleted (new):**
- `_build/keep-the-proof-v2/archive/v1_bundle/` — the three V1 files.

**Website (changed):**
- `keep-the-proof.html` (+81/−43 lines): V2 copy throughout.
- `career-evidence-starter.html` (6 lines): stale paid-product references only.
- `og-keep-the-proof.png` (regenerated for V2).
- `keep-the-proof-v2-cover.png` (new V2 cover asset at site root).

**Not shipped to web:** everything under `_build/` is blocked by the `/_build/*` → 404
rule in `netlify.toml` (verified present). Only the two HTML pages and the two root
PNGs are web-facing.

---

## 2. Final bundle inventory

| # | File | Format | Size | Pages |
|---|------|--------|------|-------|
| 1 | 01_START_HERE.pdf | PDF | 202 KB | 2 |
| 2 | 02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf | PDF | 802 KB | **47** |
| 3 | 03_YOUR_PROFESSIONAL_RECORD.docx | Word (.docx) | 42 KB | — |
| 3b| 03_YOUR_PROFESSIONAL_RECORD.md | Markdown / plain text | 22 KB | — |
| 4 | 04_PRINTABLE_FILLABLE_TOOLS.pdf | Fillable PDF | 65 KB | 8 |

## 3. Final handbook page count

**47 pages**, within the 44–56 ceiling and not padded to reach it.

## 4. Professional Record format + rationale

**`.docx` primary + `.md` plain-text mirror.** `.docx` is the most universally
*editable* rich format (Word, Google Docs, Pages, LibreOffice), built on the published
ISO OOXML standard, copyable and searchable, with no app or subscription lock-in. The
`.md`/plain-text mirror guarantees the structure survives with zero software
dependency, forever. Both are generated from one shared field model, so their fields
are identical. Full reasoning: `BUNDLE_AND_FORMAT_DECISIONS.md`.

## 5. Customer experience / labels (items 6–7)

The bundle reads as a usable system with the required labels, applied in Start Here,
on the website, and specified for Gumroad:
- **READ THIS FIRST** → Start Here
- **LEARN & BUILD** → Keep the Proof: Guided Handbook
- **KEEP USING** → Your Professional Record
- **PREFER PRINT OR A FORM?** → Printable & Fillable Tools

## 6. Career Evidence Ledger disposition (item 6)

Retired from the active bundle; its fields absorbed into the Professional Record. V1
files archived at `_build/keep-the-proof-v2/archive/v1_bundle/`, not deleted. No active
V2 artifact is a Ledger, and the V2 primary working artifact is the Professional
Record, not the Ledger.

## 7. Gumroad — before / after (owner-executed)

- **Before (V1):** "Keep the Proof: A 60-Minute Career Evidence System" — a 41-page
  handbook + a 12-page Career Evidence Ledger + a Start Here PDF.
- **After (V2):** "Keep the Proof — A guided system for building your professional
  record" — the four-component bundle above, $49, evergreen.
- Full paste-ready product description, file list, cover, ethical-influence rationale,
  and the "update the existing product, don't duplicate" steps: `GUMROAD_AND_LAUNCH_HANDOFF.md`.
- The description **leads with the reader's problem and recognition situations**, not
  with Capture / Clarify / Carry; uses only ethical influence; contains **no invented
  testimonials, urgency, discounts, scarcity, or countdowns**; one price, $49.

## 8. Website — before / after

`/keep-the-proof` updated to V2 while preserving the approved design (band rhythm,
rust rules, cards) and **internal routing** (on-page CTAs still go to the Gumroad
checkout; no other page's internal links were converted to direct Gumroad links).
- Title/description/OG/Twitter → V2 descriptor; OG image regenerated.
- Hero kicker + lede → V2; single V2 cover (ledger cover card removed).
- "What you receive" → the four V2 components (was handbook + ledger).
- First-hour outcomes, how-it-works step 3, format block, FAQ, final CTA → V2.
- Before/after example now uses the honest, number-free Proof Line (consistent with
  the product's "never invent a number" rule).
- Free/paid boundary and not-a-resume/interview boundary preserved; the quiet Field
  Kit hand-off preserved.

## 9. Starter page changes (item 10)

Only stale paid-product references updated (dropped "60-minute system", "Career
Evidence System", "reusable Career Evidence Ledger"). The Starter is otherwise
unchanged: not redesigned, not weakened, still finishes one real accomplishment.

## 10. All pricing occurrences

Price is **$49** everywhere, consistent:
- `keep-the-proof.html`: hero CTA, "What you receive" CTA, final CTA (button labels
  "Get Keep the Proof - $49"), and the hero price line "$49 · Instant digital access".
- Gumroad: $49 (handoff doc). No other price appears anywhere; no "was $X", discount,
  or pay-what-you-want.

## 11. Old-descriptor occurrences — dispositioned

Site-wide scan for `60-minute career evidence` / `Career Evidence System` / `Career
Evidence Ledger` / `reusable ledger` / `41-page`:
- `keep-the-proof.html`: **0 remaining** (all updated).
- `career-evidence-starter.html` body: **0 remaining** (updated).
- Remaining `60-minute` matches elsewhere (`for-professionals.html`, `diagnostic.html`)
  refer to the **free live 60-minute session**, a different offering — correctly left
  unchanged.
- Old cover images (`keep-the-proof-cover.png`, `keep-the-proof-ledger-cover.png`) are
  no longer referenced by any page (left in place, harmless, unserved to any visitor).

## 12. Existing-customer update method (item 11)

Replace the V1 files on the **existing** Gumroad product (same product/permalink), so
buyers' libraries point at V2 automatically at **no charge**, and opt into Gumroad's
"notify customers of update" with the factual release note provided. No re-charge, no
new permalink, no stranding. Full steps + draft email: `GUMROAD_AND_LAUNCH_HANDOFF.md` §4.

## 13. End-to-end QA results

**Automated checks run (all PASS):**
- Bundle: all 5 files present; page counts correct (2 / 47 / — / — / 8).
- Content scan of every customer file (both PDFs, the docx, the md): **no** LEGAL
  REVIEW / VISUAL / Stage 2 / "wording withheld" / counsel / "end of manuscript" /
  bracketed placeholders / stale 60-Minute or Ledger language.
- Fillable PDF: AcroForm present; **50 text fields + 19 checkboxes** across 8 pages,
  covering the same fields as the Professional Record.
- Professional Record `.docx` opens and validates (305 paragraphs + the index table);
  fields and fillable lines render.
- Website: `keep-the-proof.html` has 0 stale descriptors, 3 visible Gumroad checkout
  CTAs (+1 JS checkout constant), $49 present, V2 cover referenced, ledger cover not
  referenced. `netlify.toml` `/keep-the-proof` rewrite and `/_build/*` 404 both present.
- Rendering verified by image on: handbook cover, part dividers, spine, Keep/Care/Never,
  example cards, closing; Start Here; fillable pages; website hero + 3-card bundle
  section + first-hour outcomes.
- Mobile: the page uses the same responsive system as the live sibling pages
  (`.ktp-hero-grid` collapses to one column ≤900px, `min-width:0` guards, clamp fonts);
  a mobile render matches the live `fieldkit.html` behavior exactly.

**Owner-executed checks (cannot run here — no Gumroad API, egress blocks the live
store and site):**
- Live Gumroad product shows $49, V2 description, V2 cover, four files.
- Real test purchase → confirmation → download of all four components.
- File names/rendering as delivered by Gumroad; links in the store.
- Existing-customer re-download receives V2 free.
- Live `/keep-the-proof` after the website PR is merged (a deploy preview is available
  from the PR before merge).

## Unresolved / decisions made

- **Item 4 (closing line).** Handled cleanly, not flagged: the exact line "Keep the
  record while the facts are still yours to keep." is retained verbatim, with a
  clarifying sentence added immediately before it so it reads as *your own account of
  your work, within the permission rules* — not legal ownership of employer materials.
  No awkward legal qualifier was needed.
- **No invented legal guidance.** The former "Lawful ways to rebuild the record" page
  was rewritten to a behavioral safe-default page ("Rebuilding the record: what you can
  safely use") with no jurisdiction, personnel-record, or ownership claims.
- **No material issue is blocking the product itself.** The only remaining work is the
  owner-executed Gumroad update + live purchase QA, then merging the website PR in step
  with the store.
