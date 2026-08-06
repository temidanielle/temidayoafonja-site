# Handback — Session Workbook visual rebuild

Deliverables per the handoff spec, section 8:

1. **Generator script**, committed (`build_workbook.py`) so the workbook can be
   regenerated and versioned like the Field Kit.
2. **Rendered PDF** with all form fields and calculations intact
   (`Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf`).
3. **Page-by-page confirmation** that each page was rendered and inspected
   (below).
4. **Flagged disagreements** between the spec and the Field Kit, resolved
   openly rather than silently (below).

The output is **24 pages**: the 20 content pages of the frozen sequence, plus
the four navy section openers the spec asks the rebuild to insert. 104 AcroForm
fields (84 text, 20 checkbox), names identical to the v5.3 set.

## Acceptance criteria (section 7)

Every page was rendered at full size and inspected. `verify_workbook.py`
re-checks the mechanical criteria on each build; all pass.

| Criterion | Result |
|---|---|
| No text clipped, overlapped, or cut by a field | **Pass** — 0 overlapping text spans across all 24 pages |
| No hollow-box glyphs (U+2192, U+25A1) | **Pass** — 0 of each; axes read "low at left to high at right", checkboxes are vector rectangles |
| No navy emphasis bands | **Pass** — every emphasis line is rust italic Cormorant, set on the page with no container |
| Section openers present and consistent with the Field Kit | **Pass** — 4 full-navy openers (brand mark, `SECTION N`, Cormorant word, gold italic standfirst) |
| Fields visibly fillable (pale blue fill, tan border) | **Pass** — `#E9F0F8` fill, `#CDAE70` 0.75pt border on all fields |
| Pass-one pages contain no evidence fields | **Pass** — pages 4 and 5 carry only score fields; no `ev_*` field appears before the protocol page |
| All twelve statements match the frozen wording | **Pass** — all twelve found verbatim (each in pass one and pass two) |
| Totals calculate in Acrobat, including `3?` | **Pass (structural)** — 10/10 computed fields are read-only with tolerant calc JS; `/CO` populated; `NeedAppearances` set. See note below. |
| No page more than ~1/3 empty | **Pass** — content pages 12–33% → tuned to ≤27%; section openers are intentionally sparse, matching the Field Kit |
| Next-Move Decision is the strongest page | **Pass** — rust accent rule under the header, large rust numerals, ten full-width fields filling the page |
| No em dashes | **Pass** — 0 em dashes (U+2014) and 0 en dashes (U+2013); hyphens only |
| Page count reported, every page inspected | **Pass** — 24 pages, each inspected (log below) |

**Note on calculation:** this environment cannot run Acrobat's JavaScript, so
"calculates in Acrobat" is verified structurally — the calculation action
(`/AA /C`), the tolerant summing script (`replace(/[^0-9.\-]/g,'')` so `3?`
counts as 3), the `/CO` calculation-order array, and `NeedAppearances` are all
present and correct. As the spec's delivery note requires: calculation runs in
Acrobat and most desktop readers, and degrades to plain typeable fields in some
browser viewers (where the totals then need a desktop reader to recompute).

## Page-by-page inspection log

| Pg | Page | Fields | Notes |
|---:|---|---:|---|
| 1 | Cover | 2 | Full navy, brand mark, category line, two-line Cormorant title, rust rule, gold standfirst, name/date fields, author, version, fillable notice. |
| 2 | Before you start | 0 | Four numbered steps, first-score reassurance callout, session note, rust disclaimer (the standing boundary). |
| 3 | SECTION 1 opener | 0 | Navy. "Your initial read". |
| 4 | Pass one — Density 1–6 | 7 | Score fields only, no evidence. Auto-total `dens_initial`. |
| 5 | Pass one — Optionality 7–12 | 7 | Score fields only. Auto-total `opt_initial`. |
| 6 | First placement | 8 | Carried totals (`*_copy`), 2×2 matrix with checkboxes (rust Compounding), state + confidence. |
| 7 | Read this before you go further | 0 | Four distinctions, rust emphasis close. |
| 8 | SECTION 2 opener | 0 | Navy. "Calibration". |
| 9 | The evidence protocol | 0 | Three score bands, uncertainty callout, provisional/incomplete rules, rust emphasis. |
| 10 | What has to change (correction map) | 5 | Five entering/exiting belief pairs with checkboxes, closing callout. |
| 11 | SECTION 3 opener | 0 | Navy. "Evidence-backed read". |
| 12 | Evidence-backed read 1–3 | 6 | Corrected score + evidence per statement. |
| 13 | Evidence-backed read 4–6 | 6 | Same. |
| 14 | Evidence-backed read 7–9 | 6 | Same. |
| 15 | Evidence-backed read 10–12 | 6 | Same. |
| 16 | Re-total and place again | 9 | Auto totals (`*_corr`), five-step sensitivity check, matrix, corrected state/confidence/date. |
| 17 | What moved | 11 | Initial vs corrected table (four mirrors auto), three reflection fields, rust emphasis. |
| 18 | SECTION 4 opener | 0 | Navy. "Decide". |
| 19 | What each state costs | 0 | Four state cards — Compounding rust, others navy — rust emphasis. |
| 20 | What my state costs me | 5 | Four cost areas + one-line summary, rust emphasis. |
| 21 | Seven categories of move | 7 | Checkboxes; seventh is "Seek an external perspective". |
| 22 | The Next-Move Decision | 10 | Hero page: rust accent, large numerals, ten fields. |
| 23 | Thirty-day evidence log | 9 | Four-week grid, rescore date, routes to Field Kit Section 7. |
| 24 | Where you go from here | 0 | Three routes, rust emphasis close. |

## Flagged disagreements (resolved openly, not silently)

1. **Cover version string — resolved to "WORKBOOK V5.2".** The v5.3 fillable
   PDF's cover copy literally read `WORKBOOK V5.0`, while the handoff
   front-matter says "Workbook content v5.2" and the source filename says v5.3 —
   three different numbers for the same field. Since the handoff spec is first
   in the authority order and states the workbook **content** version as v5.2,
   the cover now reads **`WORKBOOK V5.2`** (the stale `V5.0` stamp was almost
   certainly an oversight). If the intended value is instead the file-revision
   number v5.3, that is a one-line change — say the word.

2. **Body-text colour.** The palette is emphatic — "do not introduce any colour
   not in this list" — and lists navy for "body headings" but assigns no colour
   to body text. The Field Kit's own PDF sets body text in near-black
   (`#1a1a1a`), which is off-palette. I chose the palette-disciplined reading
   and set **all body text in navy `#0F2347`**. It reads cleanly and keeps the
   document strictly on-palette; if you'd rather match the Field Kit's exact
   near-black body ink, that's a one-line change.

3. **Pale-blue field fill vs "no new colours".** The palette says introduce no
   colour outside the list, but the same spec (section 2 *and* the acceptance
   criteria) explicitly requires form fields to have a **pale-blue fill with a
   tan border**. I read this as the spec's deliberate, functional exception for
   form widgets (so fields are visibly fillable) and implemented it — pale blue
   `#E9F0F8`, tan `#CDAE70`. Flagging it only because it is, strictly, a colour
   outside the palette list; the spec calls for it in two places, so I did not
   treat it as a conflict to resolve against.

4. **Fonts.** The spec requires Cormorant Garamond + DM Sans; the published
   Field Kit PDF actually renders in base-14 Times/Helvetica (its generator
   replays base-14). Per the authority order (spec wins on what it states
   explicitly), the workbook embeds **Cormorant Garamond + DM Sans** (OFL,
   subset). This is an intentional, spec-directed improvement over the Field
   Kit's current rendering, not a silent deviation — noting it so the two
   documents' type is understood to differ on purpose.

5. **Section-opener standfirsts.** The spec says the openers are additions in
   the rebuild and does not freeze their standfirst copy. The four openers use
   the section names exactly as given in the spec's page sequence ("Your initial
   read", "Calibration", "Evidence-backed read", "Decide"); the one-line gold
   standfirsts under them are newly composed from the workbook's own language
   (no new claims introduced). Happy to adjust that wording.
