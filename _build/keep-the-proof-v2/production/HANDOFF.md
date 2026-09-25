# Keep the Proof V2: carousel redesign and one Contents fix — HANDOFF

Branch: `claude/keep-the-proof-v2-finalize`. Committed locally, not pushed, not merged.
No prices were changed anywhere.

---

## 1. Guided Handbook, Contents (`bundle/02_KEEP_THE_PROOF_GUIDED_HANDBOOK.pdf`, page 3)

- **Match Your Proof to a Role corrected to 48** (was 49). Its heading sits at the foot
  of page 48; only its body wrapped onto page 49, so the old body-phrase lookup had
  reported 49.
- The Contents builder now locates **each entry by its section heading**, scanning pages
  in document order from a cursor that starts after the Contents page. This skips the
  Contents page itself and any earlier body reference to the same words.
- Every other number was rechecked against its heading and is unchanged:
  Before You Rebuild Anything 7 · Part One 9 · What It Costs When the Proof Is Gone 11 ·
  Your First 60 Minutes 16 · Part Two 18 · Part Three 24 · Part Four 29 · Part Five 34 ·
  Part Six 38 · Part Seven 43 · Part Eight 46 · Match Your Proof to a Role **48** ·
  Put Your Record to Work 49 · Part Nine 52 · Closing 54.
- Handbook holds at 55 pages. Nothing else in the Handbook changed.

## 2. Gumroad carousel, rebuilt to match the v1 design (`gumroad/carousel/`)

Rebuilt all six slides against the attached August v1 set:

- **Cream ground (#FBF8F2), navy Cormorant headlines, gold and rust accents**, matching v1.
- **Cream cards**, the **stacked-documents mark** top-left of every slide, and the **rust
  rule** under every headline.
- **Slide 01** follows v1's layout: mark top-left, eyebrow, headline, rust rule, the accent
  line in rust, the small line, and the website at bottom-left. On the right, the **V2
  Handbook cover** sits as a tilted book with a stacked-page shadow. The navy cover reads
  clearly against the cream (the defect on the previous all-navy set).
- **Slides 01–05 keep the current V2 wording, word for word.** On slide 01 the accent line
  "A guided system for building your professional record" takes the v1 accent position and
  rust color, and "Capture. Clarify. Carry." takes the v1 small-line position.
- **Slide 06** uses the new two-tools copy:
  - Eyebrow "TWO TOOLS, TWO QUESTIONS"; headline "Different questions. Different tools."
  - Keep the Proof card (cream, gold border): title KEEP THE PROOF; subtitle "A GUIDED
    SYSTEM FOR BUILDING YOUR PROFESSIONAL RECORD"; question "What have I done, what changed,
    and what does it prove I can do?"; list: Guided Handbook with worked examples · Your
    Professional Record, editable for years · Printable and fillable tools.
  - Field Kit card (navy): title THE CAPABILITY FORMATION FIELD KIT; subtitle "AN
    EVIDENCE-LED CAREER POSITION ASSESSMENT"; question "What is my current work building in
    me?"; list: Reads your last 90 days · Density and Optionality scores · A dated position
    you can rescore.
  - **No prices** on either card; the cards are rebalanced so the old price space does not
    show. Footer: "Choose Keep the Proof when you want to capture evidence of what you have
    already done."

Output, with the current V2 file names:
- Each slide at **1600x900** and **640x360** (`0X_..._1600x900_v2.png`, `0X_..._640x360_v2.png`)
- `contact_sheet_v2.png`
- `gumroad_thumbnail_600x600.png`, built from the new slide 01, title readable small
- No prices and no page counts on any slide; important text kept clear of the edges.

## 3. Checks

- **Voice scan of all six slides and the Handbook Contents page:** clean. No em or en
  dashes, no "actually / honestly / genuinely", no accented "résumé" (both "resume"
  instances are the plain US spelling), no standalone "CV", no British spellings, no
  "it is not X, it is Y" constructions.
- The three unchanged bundle files (Start Here, Professional Record, Printable & Fillable
  Tools) and both Gumroad description files are carried through unchanged. The Starter is
  unchanged (v1.1).

## Deliverable

`KEEP_THE_PROOF_V2_FINAL_2.zip`:
- `bundle/` — the four customer files, with the corrected Handbook
- `gumroad/` — the six slides in both sizes, the thumbnail, the contact sheet, and both
  description files (unchanged)
- `starter/` — the rebuilt Starter (v1.1, unchanged this round)
- `screenshots/` — the corrected Contents page and each new slide beside its v1 counterpart
- `HANDOFF.md` — this file
