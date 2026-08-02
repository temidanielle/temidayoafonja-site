# Capability Position Read — v4.10 / v5.7 delivery

Surgical final-production pass over Deck v4.9 / Workbook v5.6. No redesign, no new teaching content.
The Instrument remains frozen at **Capability Formation Instrument Version 1.1**.

## Contents

**Deck**
- `Should_I_Stay_or_Should_I_Move_WORKSHOP_DECK_v4.10_Instrument_v1.1.pptx` — 43 slides, fonts embedded (DM Sans + Cormorant Garamond)
- `Should_I_Stay_or_Should_I_Move_WORKSHOP_DECK_v4.10_BACKUP.pdf` — PDF backup (43 pages)
- `Deck_v4.10_slide_montage.png` — rendered slide montage (real fonts)
- `Deck_v4.10_fallback_font_stress_montage.png` — same deck rendered with a wide fallback font (overlap stress test)

**Workbooks** (fillable = auto-totalling AcroForm; print = same layout, no fields)
- `..._SESSION_WORKBOOK_v5.7_..._FILLABLE.pdf` / `..._PRINT.pdf` — complete record (26 pp, 107 fields)
- `Capability_Position_Read_INITIAL_READ_v1.2_FILLABLE.pdf` / `..._PRINT.pdf` — Part A (7 pp, 24 fields)
- `Capability_Position_Read_CALIBRATION_AND_DECISION_v1.2_FILLABLE.pdf` / `..._PRINT.pdf` — Part B (20 pp, 83 fields)
- `Workbook_v5.7_FILLABLE_montage.png`, `Workbook_v5.7_PRINT_montage.png`, `InitialRead_v1.2_FILLABLE_montage.png`, `Calibration_v1.2_FILLABLE_montage.png`

**Supporting documents**
- `Facilitator_Protocol_v3.3_Instrument_v1.1.docx`
- `Anonymous_Poll_Setup_and_Backup_v1.1.docx`
- `Capability_Position_Read_Timing_and_Rehearsal_v1.3.docx`
- `Deck_Workbook_Cross_Asset_QA_Report_v4.10_v5.7.docx`
- `Deck_Workbook_Change_Log_v4.10_v5.7.docx`
- `Deck_Workbook_Crosswalk_v4.10_v5.7.docx`
- `Workbook_Fillable_vs_Print_Page_Comparison_v1.1.docx`
- `Opening_Story_Script_v2.1_DRAFT.docx`, `Story_Evidence_Table_v1.1.docx`, `Workbook_Acrobat_Runtime_Test_v1.1.docx`

## What changed (summary; full detail in the change log)

1. **Renderer-safe deck** — DM Sans (regular/bold) and Cormorant Garamond embedded; `normAutofit` shrink-to-fit added to every text box. Slide 24 (promotion) title reduced to 30 pt shrink-to-fit so it never wraps or overlaps, even under a fallback serif. Verified collision-free at real metrics and under a wide fallback. PDF backup produced.
2. **Workbook order** — the psychological-safety page now precedes the first placement in Part A and the complete record; folios 06/07 corrected; page references reconciled.
3. **Part A identity** — cover reads `PART A · INITIAL READ v1.2 · INSTRUMENT VERSION 1.1`; "Workbook v5.6" removed; "two-hour session" wording; privacy sentence corrected to "Room-level totals are recorded without names, individual scores, or identifiable responses."
4. **Part B release** — visible "Open Part B now" transition slide (deck slide 19); a two-minute release band in the timing sheet; Part B cover carries "Keep Part A available. You will need your initial totals, state, and confidence."
5. **Anonymous polling** — numbered cards withdrawn; QR/web poll or unnumbered folded slips; Boundary and Incomplete-axis options added; initial state distribution not shown before the corrected placement; "Whose…?" → "Did your…?"; movement = "Did at least one of your two axis totals change by two or more points?"; confidence = Down / No change / Up.
6. **State-cost logic** — Compounding and Fragile immediate-cost wording corrected on the deck and in the workbook.
7. **Speaker notes** — biased/unsupported lines removed or softened.
8. **Deterministic language** — slide 5 header and the flagged lines tightened.
9. **Opening story** — "only person who ever held it" → "first person appointed into the remit and its sole holder"; employer unnamed; CONFIRMED/HELD markup removed from the live deck notes (audit kept in the Story Evidence Table).
10. **QA** — page-comparison and test language corrected; only Pass / Fail / Not yet tested / Requires user confirmation used.

## Two interpretation calls to confirm

- **Version numbers.** The brief said the Part A cover should read `v1.1` but also asked for the deliverables as `Initial Read v1.2` / `Calibration v1.2` / `Complete v5.7`. To avoid a file whose name and cover disagree, the document versions were advanced consistently (cover reads v1.2); the Instrument stays v1.1. If you want the cover to read v1.1 literally, it is a one-word change.
- **Slide 5 header.** "WHAT YOU NEED TO READ FIRST" was applied to slide 5's kicker/eyebrow (over "The question underneath the question"). If you meant a different slide or the main title, say which.

## Not launch-ready

Six gates remain open and none may be marked Pass until done:
Acrobat runtime test · anonymous-polling method selected and tested · staged-release test · two full rehearsals inside the two-hour block · PowerPoint **and** LibreOffice slideshow sign-off · founder confirmation of the held story beats.

> Environment note: PowerPoint was unavailable and LibreOffice would not run in the build environment, so the deck could not be opened in either application's slideshow mode here. Slide geometry was verified with an independent text-metrics renderer (real fonts and a wide fallback). A human still needs to open the deck in PowerPoint and LibreOffice to close that gate.
