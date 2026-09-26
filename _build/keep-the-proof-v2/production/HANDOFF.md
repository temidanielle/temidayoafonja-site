# Keep the Proof V2: Read It Back, Permission to Pause, Words That Hold, review link — HANDOFF

Branch: `claude/keep-the-proof-v2-finalize`. Committed locally, not pushed, not merged.
No prices changed. The /review page is being built in a separate session; it was not built here.

Handbook is now **58 pages** (was 55). Tools is now **12 pages** (was 11).

---

## 1. Rename "Words to Stand On" to "Words That Hold" (everywhere)

- Handbook: the section heading (page 8) and the Contents entry it feeds; the panel keeps the six lines and the fill-in.
- Professional Record (.docx): the cream box title (WORDS THAT HOLD) and the icon alt text.
- Printable & Fillable Tools: the panel title on Before You Begin (page 2), and the Before You Begin line "then read the words you can stand on" is now "then read the words that hold".
- Both Gumroad description files: the phrase did not appear as a title, so nothing to rename there (item 9 adds "Words That Hold" to the handbook line).
- Website: the phrase did not appear on /keep-the-proof.
- Source constant `WORDS_TITLE` and the internal .md mirror updated; icon label and code comments updated.
- **Confirmed: "Stand On" appears nowhere** in the four files, the two description files, or the changed website lines.

## 2. Handbook: "Read It Back" (Before You Rebuild Anything)

New `###` section placed after "Why these words work" and before "A note on confidentiality before you begin". The heading lands on **page 8** (the section runs pages 8–9). Exact copy as supplied.

## 3. Handbook: "Permission to Pause" (Part Eight)

New `##` section placed directly before "Match Your Proof to a Role", on **page 50**. Exact copy as supplied, with the four lines after "decide on your next move:" as a bulleted list in the handbook's list style.

## 4. Handbook: Contents

Recomputed by locating each heading in the rendered PDF (ordered scan, not a body phrase). Final numbers:

Before You Rebuild Anything 7 · **Read It Back 8** (indented) · Part One 10 · What It Costs When the Proof Is Gone 12 · Your First 60 Minutes 17 · Part Two 20 · Part Three 26 · Part Four 31 · Part Five 36 · Part Six 40 · Part Seven 45 · Part Eight 48 · **Permission to Pause 50** (indented) · Match Your Proof to a Role 51 · Put Your Record to Work 51 · Part Nine 54 · Closing 56. The two new indented entries are in place; the Contents fits on one page (page 3).

## 5. Handbook: review link

- a. At the end of Your First 60 Minutes (**page 19**): "Finished your first session? Tell me how it went at temidayoafonja.com/review. It takes two minutes."
- b. On the last Closing page (**page 58**): a navy box titled "Tell me how it went." with the supplied body, the link temidayoafonja.com/review, and a QR code. The QR was decoded from the rendered PDF and resolves to `https://temidayoafonja.com/review` — it scans.

## 6. Printable & Fillable Tools: Read-Back Card

New fillable page directly after Before You Begin (**page 3**). Title READ-BACK CARD; intro "Read this each morning for 30 days. Keep it where you will see it." Left column Words That Hold (the six lines, then the fill-in "One thing I did that someone relied on:"). Right column My evidence: three "A moment or Proof Line from my record" fields; "The line I am learning to believe" with "The entry that supports it" below; "A sentence that shrinks my work" with "What would have been different if I had not been there?" below. Bottom: a row of 30 numbered "Mornings read." checkboxes. The last Tools page (Maintenance, **page 12**) carries "Tell me how it went: temidayoafonja.com/review."

Field counts after rebuild: **75 text fields and 49 checkboxes** (was 67 and 19; the Read-Back Card adds 8 text fields and 30 checkboxes, plus 1 fill-in already counted). All fields fill and save (the form is not flattened).

## 7. Your Professional Record (.docx)

- a. Directly after the Words That Hold box, a "Read It Back" workspace with four prompts and write space: "A sentence that shrinks my work," "What would have been different if I had not been there?", "The line I am learning to believe," "The entries that support it."
- b. After the final section: "Tell me how it went: temidayoafonja.com/review."
- c. Footer page numbers kept (the `PAGE` field in `word/footer1.xml` is intact).
- The internal .md mirror was updated to match. (LibreOffice cannot render .docx in this sandbox, so the screenshot for this file is a clearly-labeled facsimile of the added content.)

## 8. Page counts updated (Handbook 58, Tools 12)

- Start Here: "The 58-page teaching guide"; "Twelve printable and fillable pages".
- Both Gumroad description files: "(58 pages)" and "(12 pages)" (and the existing-customer note "now 58 pages").
- Website /keep-the-proof: "58-page guided handbook", the doc-meta "58 pages", "12 pages of printable and fillable tools", and the doc-meta "12 pages".

## 9. Gumroad description files (both)

- a. Handbook line now reads: "It opens with Before You Rebuild Anything, with Words That Hold and a 30-day Read It Back practice, and its Put Your Record to Work section shows how to carry..."
- b. Tools line: "the same fields as your Professional Record, plus a Read-Back Card, ..."
- c. Before the Career Evidence Starter line: "Some early reviewers received a complimentary copy."

## 10. Website (/keep-the-proof)

One small line added near the bottom of the final section: "Already have Keep the Proof? Tell me how it went." with "Tell me how it went." linking to /review. Nothing else changed except the page counts in item 8.

## 11. Checks

- Voice scan of all four bundle files, both description files, and the changed website lines: clean. **"Stand On" appears nowhere.** No em or en dashes, no "actually / honestly / genuinely", no accented "résumé" (the two "resume" instances are the plain US spelling), no British spellings, no "it is not X, it is Y" constructions. (The scan flags "analyst," a correct US word, and the heading "What it is not"; both are false positives, not violations.)
- Everything re-rendered; Contents numbers confirmed against the rendered PDF.
- Tools fields confirmed present and fillable (75 text, 49 checkboxes); Professional Record footer page numbers confirmed.

## Deliverable

`KEEP_THE_PROOF_V2_FINAL_3.zip`:
- `bundle/` — the four customer files (Start Here, 58-page Handbook, Professional Record .docx, 12-page Tools)
- `gumroad/` — the six carousel slides in both sizes, the thumbnail, the contact sheet, and both updated description files
- `starter/` — the Career Evidence Starter (v1.1, unchanged this round)
- `screenshots/` — every changed page: Contents, Read It Back, Permission to Pause, the First 60 review line, the Closing review box with QR, the Read-Back Card, the Tools review line, Start Here, the Professional Record Read It Back (facsimile), and the website review line
- `HANDOFF.md` — this file
