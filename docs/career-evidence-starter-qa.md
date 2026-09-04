# Career Evidence Starter: QA report

Candidate build. **Not final, not published.** Against the twelve QA points in
the brief, in order, with what was actually run.

Re-run in full after the experience and visual refinement pass. Where the
refinement changed a result, the number below is the new one.

---

## Refinement pass: functional regression check

The brief's standard was that no functional regression is acceptable for an
aesthetic improvement. The check was made against the archived v1.0 PDF itself
rather than against the previous version of this document, by loading both
files and comparing the AcroForm tables field by field.

| | v1.0 | Revised | |
|---|---|---|---|
| Fields | 22 | 22 | unchanged |
| Text fields | 14 | 14 | unchanged |
| Checkboxes | 8 | 8 | unchanged |
| Field names | | | identical, and in the same order |
| Fields added or removed | | | none |
| Page each field sits on | | | unchanged for all 22 |
| Multiline flags | 7 | 7 | unchanged, field for field |
| Read-only fields | none | none | |
| Round trip: written / read back | 22 / 22 | 22 / 22 | no mismatches |
| Blank master still blank after a fill and save | yes | yes | |

Three fields were deliberately **enlarged**, and none was shrunk in height:

| Field | v1.0 | Revised |
|---|---|---|
| `q5_portable` | 490 x 75 pt | 490 x 94 pt |
| `plain_explanation` | 490 x 75 pt | 490 x 94 pt |
| `proof_line` | 490 x 75 pt | 490 x 150 pt |

One reduction to report: the four question fields on page 3 are now **467pt
wide rather than 490pt**, because they sit inside the guided cards and the card
padding takes 23pt of the measure. Their height is unchanged at 56pt. That is a
4.7 per cent narrower line, and it is the only place the refinement costs
anything functional. It can be recovered by reducing the card padding if you
would rather have the width than the card.

**Correction to the previous version of this report.** It recorded the text
fields as "5 multiline, 9 single line". Read from the file, v1.0 had **7
multiline and 7 single line**, which is also what the revised build has. The
earlier figure was a documentation error, not a change in the PDF.

### Page fit after the refinement

Every page still fits its 11in box and clears the running footer. The pass
also rebalanced the whitespace, so no page now carries a large dead area:

| Page | v1.0 slack | Revised slack |
|---|---|---|
| 1 | not recorded | 67px |
| 2 | 33px | 51px |
| 3 | not recorded | 61px |
| 4 | not recorded | 63px |
| 5 | not recorded | 83px |
| 6 | not recorded | 26px |

Quick Capture stayed on page 2 with the full author copy, so the shorter
fallback copy supplied for the tight case was not needed.

### One contrast defect found and fixed in this pass

The new gold descriptor badge put `--gold-ink` (#7F6A30) on the gold ground
(#EFE4C6), which measures **4.13:1 and fails AA**. Both the PDF cover badge and
the landing page badge now use #756025, the same hue two steps darker, at
**4.80:1**. The site-wide `--gold-ink` was left alone.

---

## 1. Method statements compared against the approved Keep the Proof source

**Not done. This is the one QA item that could not be performed.**

The three named source files are not in this repository and were not supplied:

- Keep the Proof, A 60-Minute Career Evidence System v1.0.1 FINAL
- Keep the Proof Career Evidence Ledger v1.0.1 FINAL
- KEEP THE PROOF START HERE v1.0.1

Only the cover images exist (`keep-the-proof-cover.png`,
`keep-the-proof-ledger-cover.png`). No PDF of any kind is stored in the
repository.

Every method statement in the Starter therefore comes from the brief's own
copy, which is operator-written and was followed closely, and from the live
`/keep-the-proof` page. **Nothing was invented.** But consistency with the paid
PDFs has not been verified, and cannot be until those files are supplied.

## 2. No new claims about career outcomes or organizational decision-making

Checked. The Starter makes no claim about promotions, interviews, offers,
salary, placement or employer behaviour. Page 6 lists where the entry can be
used and explicitly says to adapt it rather than reuse it word for word.

## 3. No prevalence or validation language

Swept for "most people", "most common", "proven", "validated", "research shows",
"studies", "guaranteed". **Zero occurrences** in the PDF text and on the landing
page. The nearest thing is "That happens often" in the follow-up email, which is
an invitation to reflect rather than a claim about a population; flagged here in
case even that is unwanted.

## 4. Paid Keep the Proof files unchanged

`keep-the-proof.html` is untouched on this branch. Diff against `main` covers
only new files plus `netlify.toml`.

## 5. Field Kit files unchanged

`fieldkit.html` untouched. Confirmed by diff.

## 6. Public URLs confirmed against the site

| URL used | Verified against |
|---|---|
| `temidayoafonja.com/keep-the-proof` | live canonical in `keep-the-proof.html` |
| `/career-evidence-starter` | new route added to `netlify.toml` |
| `/api/career-evidence-starter-subscribe` | new function, route added |

The Keep the Proof Gumroad URL is **not** used anywhere in the Starter or on the
landing page, deliberately: the free product must never route to the paid
checkout.

## 7. The product is clearly free

"Free Career Accomplishment Tracker" appears on the PDF cover, in the page
title, in the meta description, in the hero eyebrow and on the submit button.
**No price appears in the PDF at all**, per the instruction that the website
remains the source of truth for pricing.

## 8. It does not contain the paid product's reusable system

No Career Evidence Ledger, no multiple Quick Capture records, no Full Evidence
Entry, no monthly or quarterly routines, no Evidence Index, no complete
translation system, no 60-minute method. One capture, six prompts, one line.
See the architecture note.

## 9. No employer-confidential information requested

Every field asks for the user's own recollection. Page 2 carries a permission
checklist that must be ticked before writing, and page 5 repeats the check
before the line is used. The optional free-text box on the landing page warns
against including anything confidential. **Nothing is uploaded**: the PDF is a
local file and the site stores only name, email, consent stamps and the optional
note.

## 10. Every PDF page rendered and inspected

Done, all six. Poppler and LibreOffice are both unavailable in this container
(LibreOffice fails to convert even a plain text file), so the PDF was rendered
through pdf.js in Chromium and each page screenshotted from the canvas. That is
a render of the real PDF, not of the HTML source.

Two defects were found this way and fixed:

- **Checkboxes drew as broken squares.** The AcroForm widget was overlapping a
  square drawn in the HTML. The widget now draws the only box.
- **A label lost its styling.** `.lbl` was scoped to `.inline-flds`, so the
  standalone "Why it mattered" label rendered as body text.

Overflow was checked separately: no page overflows its 11in box, and all six
clear the running footer. After the refinement pass the tightest is page 6 with
26px of slack. See the refinement table above.

Two further defects were found by rendering during the refinement pass and
fixed: page 3 overflowed its box by 32px when the four guided cards were first
laid in, and the gold badge failed AA. Both are described above.

## 11. Every fillable field tested

Round-tripped programmatically: every field filled, saved to disk, reopened from
disk, values read back.

| | |
|---|---|
| Text fields | 14 (7 multiline, 7 single line) |
| Checkboxes | 8 |
| Fields written | 22 |
| Read back correctly | 22 |
| Mismatches | none |
| Read-only fields | none |
| Blank master still blank afterwards | yes |

**What this does not prove.** It does not prove how Adobe Acrobat Reader,
Preview.app, or a phone viewer renders or saves them. There is no Mac and no
Acrobat in this container. **Testing in Acrobat Reader on a Mac remains an open
item before this is marked final.** Text remains selectable, the fields sit on
printed rules so the sheet can be printed and completed by hand, and nothing on
any page depends on JavaScript.

## 12. Comparison of free versus paid

Written as a separate one-page note:
`docs/career-evidence-starter-architecture.md`.

---

## Landing page verification

Re-run at 1440, 834 and 390 against the page served locally after the
refinement pass.

- **axe, WCAG 2.1 AA: 0 violations** at all three widths
- One `h1`, no skipped heading levels, 8 sections
- No horizontal overflow, no em dashes
- Honeypot present; two separate consent checkboxes; two live regions
- Result section hidden until the server confirms
- **0 console errors** after fixing one found during the check

One real bug was caught here: a renamed variable left two stragglers, which
threw `ReferenceError: decidingEl is not defined` on every page load and would
have broken the form. Fixed and re-verified.

Submit path smoke-tested with the endpoint mocked: an empty submit is correctly
refused client side, and a valid submit posts exactly the shape the function
expects, including both consent timestamps, the policy version, the honeypot
field and the attribution object.

---

## Launch blockers

| | Blocker | State |
|---|---|---|
| 0 | **The page 2 author portrait.** **Closed.** `images/temidayo-gold-ivory.png` was committed by the operator and is byte-identical to the supplied file (1254x1254, sha256 cce004872f...). Used on PDF page 2 and in the landing page WHO MADE THIS section. | Closed |
| 1 | **PDF hosting.** **Closed.** The PDF is committed at `/resources/keep-the-proof-career-evidence-starter-v1-0-5ee610a6d0d4.pdf`, under a filename carrying a random token. `/resources/*` carries `X-Robots-Tag: noindex, nofollow` and is disallowed in `robots.txt`. This deliberately breaks the no-PDFs convention, on operator approval. It is lead-magnet gating, not access control. | Closed |
| 2 | **Kit setup.** Objects created manually and verified: sequence 2880104, resource tag 23001964, guidance tag 23001968, YouTube tag 22590237, and the `current_situation` custom field. **Still open:** the four Netlify environment variables are not set, so the function still returns 503, and the Kit delivery email is deliberately unpublished until the PDF URL above is pasted into it. | Partly open |
| 3 | **Social share image.** **Closed.** `og-career-evidence-starter.png`, 1200x630 at the site convention, rendered with the site's own faces and built from the real cover render. `og:image` and `twitter:image` both point at it, with width, height and alt declared. | Closed |
| 4 | **Acrobat Reader test on a Mac.** Cannot be done here. | Open |
| 5 | **The three source PDFs**, for QA point 1. | Open |
| 6 | **`noindex` removal** on the landing page, and the preview note in `netlify.toml`, at launch. | Deliberate |

Nothing on the site links to `/career-evidence-starter`. It is reachable only by
typing the URL.

Production and the deploy preview could not be checked: the egress proxy in this
container blocks `temidayoafonja.com` and `*.netlify.app`.
