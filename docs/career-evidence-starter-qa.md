# Career Evidence Starter: QA report

Candidate build. **Not final, not published.** Against the twelve QA points in
the brief, in order, with what was actually run.

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
clear the running footer. Tightest is page 2 with 33px of slack.

## 11. Every fillable field tested

Round-tripped programmatically: every field filled, saved to disk, reopened from
disk, values read back.

| | |
|---|---|
| Text fields | 14 (5 multiline, 9 single line) |
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

Run at 1440, 834 and 390 against the page served locally.

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
| 1 | **PDF hosting decision.** No PDFs are stored in this repository by existing convention, so where the file lives, and what the email download link points at, is undecided. | Open |
| 2 | **Kit setup.** The sequence and both tags do not exist yet: `KIT_SEQ_CAREER_EVIDENCE_STARTER`, `KIT_TAG_CAREER_EVIDENCE_STARTER`, `KIT_TAG_CAREER_EVIDENCE_STARTER_GUIDANCE`. The function refuses to run without them and returns 503. | Open |
| 3 | **Social share image.** No Starter-specific card exists; the page falls back to `og-default.png`. | Open |
| 4 | **Acrobat Reader test on a Mac.** Cannot be done here. | Open |
| 5 | **The three source PDFs**, for QA point 1. | Open |
| 6 | **`noindex` removal** on the landing page, and the preview note in `netlify.toml`, at launch. | Deliberate |

Nothing on the site links to `/career-evidence-starter`. It is reachable only by
typing the URL.

Production and the deploy preview could not be checked: the egress proxy in this
container blocks `temidayoafonja.com` and `*.netlify.app`.
