# Keep the Proof V2: final fixes before Gumroad upload — HANDOFF

Branch: `claude/keep-the-proof-v2-finalize`. All work committed locally, not pushed, not merged.
No price was changed anywhere this round.

Handbook holds at **55 pages**. Tools holds at **11 pages**. No page-count propagation was needed.

---

## 1. Guided Handbook (`bundle/02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf`)

- **1a. New page for the chapter.** "Before You Rebuild Anything" now begins on its own page (**page 7**). Its heading and the "See what you already built" subtitle no longer sit at the bottom of the previous page.
- **1b. Contents recomputed against the rendered PDF** (page 3). "Before You Rebuild Anything" now reads **7**, not 3. The earlier 3 was the Contents page itself matching its own label; every Contents search key now uses a body phrase unique to its page, so no entry can match the Contents page again.
- **1c. Three indented Contents entries added, with page numbers:**
  - What It Costs When the Proof Is Gone — **11** (indented under Part One)
  - Match Your Proof to a Role — **49** (indented under Part Eight)
  - Put Your Record to Work — **49** (indented under Part Eight)
- **1d. Two headings title-cased** (page 49) and all references confirmed already title-case:
  - "Match your proof to a role" → **Match Your Proof to a Role**
  - "Put your record to work" → **Put Your Record to Work**
- **1e. Diagram title added** (Two-Minute Quick Capture, **page 19**): **"What Fades and What Holds"** now sits above the diagram. The label "An illustration of the idea, not data from a study." is kept.
- **1f. Three contrast constructions replaced:**
  - Part One, The opening question (**page 10**): "Not a scandal, just a change." → "Nothing dramatic happens. Something changes."
  - Part Four, corroboration (**page 33**): "It is not networking, not outreach scripting, not referral strategy, and not personal-brand building." → "Networking, outreach scripts, referral strategy, and personal branding belong to other tools."
  - Part Five, What translation is (**page 35**): "It is not a judgment about whether your experience fits a particular role, industry, or employer." → "Whether your experience fits a particular role, industry, or employer is a separate question."
- **1g. Cover subtitle serial comma** (page 1): "career pivots, re-entry, and unexpected change."
- **1h. Welcome sentence deleted** (page 4): the "When an offer I had accepted was rescinded…" sentence is removed from Welcome. The story stays in Before You Rebuild Anything (page 7). Welcome now reads exactly as specified.

## 2. Start Here (`bundle/01_START_HERE.pdf`, 1 page)

- **2a.** Handbook card: "…and closes with Put Your Record to Work." → "…and, in Put Your Record to Work, shows you how to carry one Proof Line into a resume, a LinkedIn profile, an interview, and a promotion conversation."
- **2b.** Tools card: "Eleven form pages holding the same fields" → "Eleven printable and fillable pages holding the same fields."
- **2c.** Footer, after the personal-use license line: added "Organizations providing Keep the Proof to employees or program participants can arrange a group license at temidayoafonja.com/work."
- **2d.** No price on the page. Unchanged.
- CSS spacing was tightened slightly so the page stayed one page after the added copy.

## 3. Gumroad description

Two files. The paste-ready description lives in `GUMROAD_AND_LAUNCH_HANDOFF.md` (section 2). The plain-text version is `GUMROAD_DESCRIPTION_PLAIN.txt`.

- **3a.** "It opens with Before You Rebuild Anything and closes with Put Your Record to Work, which shows how to carry" → "It opens with Before You Rebuild Anything, and its Put Your Record to Work section shows how to carry". Rest of the sentence unchanged.
- **3b.** "You keep your own account of your work, not the files." → "You keep your own account of your work and leave the files where they belong."
- **3c.** Group license sentence (from 2c) added at the end of Format & safe use.
- **3d.** "$75. One price, instant access." deleted. **No price remains in either description file.** (The buy button shows the price.)
- **3e.** `GUMROAD_DESCRIPTION_PLAIN.txt` created with no Markdown symbols. Headings and list items are on their own lines, and a top "NOT FOR PASTING" block lists which lines to set as headings, which to set as a bulleted list, and which phrases to bold.

> Note on operational price mentions: `GUMROAD_AND_LAUNCH_HANDOFF.md` still lists `$75` in three **operational** spots (product-settings step, the ethical-influence note, and the launch-steps checklist). These are your setup instructions, not the customer description, and were left untouched per "do not change any price this round." Reconcile them once the launch price is set.

## 4. Gumroad carousel (`gumroad/carousel/`)

Rebuilt fresh in the V2 brand style using the V2 Handbook cover and the V2 icon set. **The v1 carousel from August is not in this repo or its git history**, so there were no v1 files to match filename-for-filename or to copy slide 06's "keep the v1 text" pieces from (see the note below). Layout, palette and type follow the established Keep the Proof / Field Kit system.

Deliverables, each slide at **1600x900** and **640x360**:
- `01_hero_{1600x900,640x360}_v2.png`
- `02_what_you_receive_{…}_v2.png`
- `03_how_it_works_{…}_v2.png`
- `04_before_and_after_{…}_v2.png`
- `05_who_it_is_for_{…}_v2.png`
- `06_two_tools_{…}_v2.png`
- `contact_sheet_v2.png` (all six slides)
- `gumroad_thumbnail_600x600.png` (built from slide 01; title readable at small size)

No prices and no page counts appear on any slide. All text is kept clear of the edges. Slides 01–05 use the exact copy from the brief. Slide 06 uses the exact eyebrow, headline, Keep the Proof subtitle and list, and removes both prices ($49 and $150) as instructed.

> **Slide 06, please confirm.** The brief said "keep the v1 question as is," "keep its v1 text as is" (Field Kit card) and "keep the v1 line as is" (footer). Because the v1 carousel is not in the repo, those three pieces were reconstructed from the site's own canonical Field Kit copy (the keep-the-proof.html FAQ):
> - Keep the Proof card question: "What have I done, and how do I keep the proof of it?"
> - Field Kit card: "What is my current work building in me, and will it travel?" plus "The Field Kit helps you assess what your current work is building in you and read your broader capability position. It is a different tool for a different question."
> - Footer: "Keep the honest record first. Read what it means for your direction when you are ready."
> If your v1 wording differs, send it and I will drop it in verbatim.

## 5. Career Evidence Starter (`starter/`)

Source was found in the repo at `_build/career-evidence-starter/`, so it was fixed and rebuilt. Six pages, kept.

- **5a.** Byline: "Career Portability Advisor · Founder, The Density Group" → "Founder, The Density Group" (page 1).
- **5b. Voice fixes:**
  - Page 1 promise: serial comma, "…internal move, or career pivot."
  - Page 2 quote: "what you actually contributed" → "what you contributed."
  - Page 2 safety card: "Tick each one… If you cannot tick it…" → "Check each one… If you cannot check it…"
  - Page 2 selection tests: "You exercised judgment, not just activity." → "You made a judgment call."
  - Page 3 heading: "What actually happened?" → "What happened?"
  - Page 3 pull quote: "You do not need a perfect metric. You need a truthful account of what changed." → "Start with a truthful account of what changed. A number can come later, if you have one you may keep."
  - Page 4 chipnote: "These are examples, not a checklist. What did your work require?" → "These are examples. What did your work require?"
  - Page 4 xnote: "This is an example of the distinction, not a claim that those terms are equivalent in every workplace." → "This shows the distinction. The terms will differ by workplace."
  - Page 5 scaffold note: "This is a scaffold for thinking, not a sentence to copy mechanically. Rearrange it so it sounds like you." → "Use this as a scaffold for thinking. Rearrange it so it sounds like you."
- **5c. Aligned to V2's five Proof Line ingredients, six pages kept:**
  - Cover "What you will build" preview now shows five strips: THE CONDITION, YOUR PART, THE SCOPE OR CONSTRAINT, THE OUTCOME, THE SUPPORT (last highlighted).
  - Page 2: "complete the six prompts that follow" → "complete the seven prompts that follow."
  - Page 3 is now five prompts (1 The condition, 2 Your part, 3 The scope or constraint [new], 4 The outcome, 5 The support). New prompt 3 question "How big was it, and what limits did I work within?" with the specified hint. Write boxes shortened to two lines so all five fit on the page.
  - Page 4: the two prompts renumbered to 6 and 7.
  - Page 5: navy scaffold text replaced with "Combine, in whatever order reads well, up to five ingredients into one line: the condition, your part, the scope or constraint, the outcome, and the support." BEFORE kept as "Led Project Horizon onboarding work."; PORTABLE replaced with Maya's Proof Line. Can It Travel? checklist kept.
- **5d. Page 6 upsell box:** v1 cover thumbnail → V2 Handbook cover; "A 60-Minute Career Evidence System" → "A guided system for building your professional record."; paragraph replaced with the specified upsell copy.
- **5e.** Title and everything else unchanged. **Version bumped to v1.1** in the file name. Kept on the branch. The live copy is now `resources/keep-the-proof-career-evidence-starter-v1-1-dac91eea9ebf.pdf` (the v1-0 file was removed and the two docs that named it were updated). Delivery is by email through Kit, so this file is the source artifact and goes live with the website merge.
- Fillable fields after rebuild: **15 text fields, 8 checkboxes** (was 6 text prompts; the added scope prompt makes 7 numbered prompts plus the quick-capture and internal-language fields).

## 6. Website images (branch only)

- No page on the site uses a v1 carousel image (either size). The carousel is a Gumroad-only asset and was never referenced by the site.
- The only live use of the v1 Keep the Proof cover was the Starter's page 6 upsell thumbnail, which now points to `/keep-the-proof-v2-cover.png` (see 5d).
- `keep-the-proof.html` already uses the V2 cover (`/keep-the-proof-v2-cover.png`) and the V2 social image (`/og-keep-the-proof.png`).
- `keep-the-proof-cover.png` and `keep-the-proof-ledger-cover.png` were **not deleted**: a historical QA doc (`docs/career-evidence-starter-qa.md`) still names them, so per "delete only if nothing else references them" they were left in place.
- No website prices were changed.

## 7. Checks

- **Re-rendered:** Handbook (two-pass TOC), Start Here, Professional Record docx (+ internal .md mirror), Tools PDF, the six carousel slides at both sizes, and the Starter.
- **Page counts:** Handbook **55**, Tools **11**. Unchanged, so no count needed updating in Start Here, the description files, or the website.
- **Voice / spelling scan** across all four bundle files, both description files, all six carousel slides, and the Starter:
  - Em dashes and en dashes used as dashes: **none.**
  - "actually," "honestly," "genuinely": **none.**
  - Accented "résumé" / accented characters in copy: **none** (all instances are the plain US "resume"). One "×" multiplication sign in an operator note was normalized to "x".
  - Standalone "CV": **none.**
  - British spellings (organise/-isation, -our, -re, -ogue, etc.): **none.** ("analyst," "exercise," "enterprise," "advise," "promise" and similar are US-valid and were not changed. "Actual ownership" is a field name and was left.)
  - "it is not X, it is Y" and split forms: **none** in customer copy. ("What it is not" is a section heading, not a contrast construction.)
- **Tools PDF fields:** **67 text fields and 19 checkboxes** confirmed present after rebuild (via widget inspection), all still fillable and re-savable (form not flattened).
- **Starter fields:** 15 text fields and 8 checkboxes confirmed present, fillable and re-savable.
- **Professional Record footer page numbers:** `word/footer1.xml` contains a proper Word `PAGE` field, the standard mechanism that survives a LibreOffice round trip. A **live** LibreOffice round trip could not be run: `soffice` in this sandbox fails with "source file could not be loaded" for any document, so this specific check could not be executed here and should be spot-checked on your machine.
- **"Item 4" question:** In the earlier formatting-and-navigation request, the five items were 1 labels bold, 2 page numbers + TOC, 3 AI-prompt consistency, 4 the voice **rules**, 5 the report. Item 4 was the rules to apply, not a separate deliverable, and those rules were applied throughout; the handoff listing 1, 2, 3 and 5 simply omitted the rules line. **Nothing was skipped.**

## Deliverable

`KEEP_THE_PROOF_V2_FINAL.zip` contains:
- `bundle/` — the four customer files
- `gumroad/` — the six slides in both sizes, the 600x600 thumbnail, the contact sheet, and both description files
- `starter/` — the rebuilt Starter (v1.1)
- `screenshots/` — every changed page
- `HANDOFF.md` — this file
