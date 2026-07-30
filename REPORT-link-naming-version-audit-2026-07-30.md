# Link, Naming & Version Audit — temidayoafonja.com
**Date:** 2026-07-30 · **Author:** Claude Code · **Status:** Report only. No copy changed. Awaiting go-ahead on fixes.

## Method & one limitation
This is a static site deployed on Netlify. Served status for every path is fully determined by `netlify.toml` (redirects) plus which `*.html` files exist (Netlify serves `/foo` from `foo.html` at 200 by default). I derived items 1–3 from those two authoritative sources.

**Limitation:** I could **not** hit the live origin over the network — the environment's egress policy returns `403` at the proxy gateway for `temidayoafonja.com:443` (both `curl` and WebFetch). So the HTTP statuses below are *predicted from config*, not observed live. They should be spot-checked with a real browser/curl before you rely on them. Everything else (grep, file/line, instrument logic, version inventory) is observed directly.

---

## Items 1–11

| # | File & line | Current state | Proposed change | Risk |
|---|---|---|---|---|
| **1. Every URL / status** | `netlify.toml`; all `*.html` | **200 (static, pretty-URL):** `/`, `/framework`, `/about`, `/principles`, `/work`, `/speaking`, `/book`, `/case-studies`, `/ai-capability-readiness`, `/dashboard`, `/diagnostic` (200 rewrite→`diagnostic.html`), `/organizational-diagnostic` (200 rewrite). **301:** `/audit`→`/diagnostic`; `/institutional-diagnostic`→`/organizational-diagnostic.html`; `/institutional-diagnostic.html`→same; `/diagnostic?audience=org`→`/organizational-diagnostic`; `/fieldkit`→`gumroad.com/l/czmqp`. **No 404s** among referenced paths. | None (inventory). Confirm live once egress allows. | Low |
| **2. Named paths** | `netlify.toml`, files | `/audit`→**301**→`/diagnostic`→200 (resolves, *not* 404). `/diagnostic`→200. `/organizational-diagnostic`→200. `/institutional-diagnostic`→**301**→`/organizational-diagnostic.html` (intentional retirement). `/fieldkit`→**301**→Gumroad. `/book`→200. `/case-studies`→200. `/work`→200. `/speaking`→200. `/principles`→200. | None. | Low |
| **3. `/audit` resolves?** | `netlify.toml:40–46` | **Yes.** A permanent `301 → /diagnostic` (`force=true`) **already exists** and is commented "never remove." The book's four `/audit` references resolve to the diagnostic. | **No change needed** — the smallest-possible change is already in place, in `netlify.toml`. Do not remove it. | None (removing it later would break sold books) |
| **4. `/case-studies` exists / contents** | `case-studies.html:93–191` | Exists (200). Six **qualitative** cases (quadrant-transition narratives: 2 org, 4 individual). Outcomes are soft ("14 senior positions," "90-day plan," "moved up a full pay band," "four months"). A testimonial block (`:185–191`) renders nothing. **It contains none of the retention/effectiveness numbers.** The paid Field Kit points here as "the home of full case studies including retention and effectiveness numbers" — **that promise is unmet**; those numbers live on `/work` instead. | Decide: add the numbered case ledgers to `/case-studies`, or change the Field Kit's pointer. | **Med** — paid buyers were promised numbers not on the page |
| **5. Retired/unruled strings** | see rows below | | | |
| — "Capability Formation Audit" | `netlify/functions/audit-research.js:1` | In a code comment only (not rendered). Also the name of several **Drive** short-form PDFs (see item 12). | Rename comment on next touch; retire the Drive short-forms. | Low (non-rendered) |
| — "AI Capability Readiness Diagnostic" | `ai-capability-readiness.html:7,15,19,306,914,938`; `diagnostic.html:647–648`; `work.html:133`; `netlify/functions/ai-readiness-*.js` | **A whole unruled named instrument** (27-item, "The Density Group" brand) — its own page, plus a "Your Next Step" CTA on `/diagnostic` and a link on `/work`. Not in the canon. Also introduces "Institutional Resilience" (`diagnostic.html:648`). | Rule on it: name/keep/retire, and whether `/diagnostic` should promote it. | **High** — largest naming exposure on the site |
| — "the audit" as instrument (reader-facing) | `work.html:295` ("subject line \"Capability audit inquiry\""); `work.html:267` ("Optionality audit") | Reader-facing uses of *audit* as a service/instrument. | Rename to "Capability read"/"inquiry" per NOUN rule. | Med |
| — "audit" as instrument (internal, non-rendered) | `diagnostic.html:1406,1597,1751` (Plausible "Audit Started/Completed"), `:1545,1587` (`source:"capability_audit"`), `#audit`/`.audit-*` ids & classes; `dashboard.html:218,222` | Retired instrument naming persists in analytics event names, form `source` tags, CSS ids/classes, and the `audit-research` endpoint. Non-rendered but will keep leaking into analytics/exports. | Optional cleanup; low urgency. | Low |
| — "the audit"/"audit" as **verb** | `diagnostic.html:955,1011,1095`; `book.html:184` | Verb usage ("audit whether…"), not the instrument. Likely acceptable. | Judgment call; probably leave. | Low |
| — "Institutional Diagnostic" / "institutional-diagnostic" | `netlify.toml:14,19` (redirect *source* rules) | No reader-facing hits. The strings survive only as the retirement redirects (intentional). Adjacent term "Institutional Resilience" at `diagnostic.html:648`. | Keep redirects; rule on "Institutional Resilience." | Low |
| — "Individual Capability Coaching" | `work.html:256`; `index.html:273` | A service name not in the canon list. | Rule: keep/rename/retire. | Med |
| — "digital audit", "web audit", "Take the Audit" | — | **No hits** anywhere. | None. | — |
| **6. Forward-looking / priority language** | see rows below | | | |
| — Book "Density" waitlist | `book.html:274–281,328,331`; linked from `index.html:291` | "When Density has a publication date, **the people on this list hear it first**…"; confirm note "**you will know before anyone**"; "Join the list." First-notice promise to a named list (POSTs `source:'book-waitlist'`). | Decide if the priority promise stays. | Med |
| — Coaching waitlist + scarcity | `work.html:257,260` | "Individual Capability Coaching · 90-Day Engagement · **Limited Spots**" + "**Waitlist Open**" tag. Priority + scarcity to a named group. | Decide; also resolve contradiction below. | Med |
| — Contradiction | `work.html:286` | "**No intake process. No waiting list pitch.**" — directly contradicts the "Waitlist Open" tag 26 lines above. | Pick one. | Med |
| — Dead style / stray | `work.html:65–68,94` (`.cohort-strip` CSS, no markup instance); `diagnostic.html:1078` ("next cohort," generic question text); `ai-capability-readiness.html:307` ("a few pilots in flight," generic) | Not live promises: unused CSS + generic prose. | None needed. | Low |
| — "workshop", "coming soon", "early access", "first notice", "hear first" | — | **No hits.** The in-build unnamed workshop has not leaked anywhere. | None. | — |
| **7. What `/diagnostic` claims it measures** | `diagnostic.html:8/16/20`, `334–344`, `359`, `852–854` | Meta: *"maps your capability across Density, Optionality, **and Alumni Capital**."* Pillars row shows all three. **But the body already corrects it:** caption `:344` — "**Density and Optionality are the two axes you are scored on. Alumni Capital is measured separately and does not move your placement.**"; `:359` repeats it. Code: `IND_HIGH=19`, boundary `17–21`, 12 statements (1–6 Density, 7–12 Optionality). So the instrument matches your canon; the only three-pillar implication is the **meta description + pillars visual**. No third pillar feeds placement. | Copy fix, not a build: align the meta description/pillars visual to "two scored axes + Alumni Capital read separately," or build the third pillar. Your call. | Low–Med |
| **8. Four-states matrix orientation** | `diagnostic.html:462–472`; `organizational-diagnostic.html:320–326,421–427,438–443`; `index.html:213–217`; `framework.html:200–221`; Drive Diagnostic PDF | **All corners match canon** everywhere: Depth Trap TL, Compounding TR, Stagnant BL, Fragile BR; Density low at bottom, Optionality low at left. **Axis direction stated:** `/diagnostic` ("Density ↑", "← Low / High Optionality →"), `/organizational-diagnostic` ("Low/High optionality" + "High/Low density," live and report), and the Diagnostic PDF. `framework.html` states it per-card ("High Density · Low Optionality" tags). **Weak spot:** `index.html:213–217` renders the four quadrants with **no axis labels** — direction only *implied*. | Add X/Y axis labels to the `index.html` matrix. | Low |
| **9. The five numbers + attribution** | `work.html:132,160`; `book.html:270` | The specific numbers appear **only on `/work`**. `:132` — "30% retention improvement, $2M+ … turnover costs, and 46-point onboarding NPS" attributed to *"Delivered as **Senior Director, Employee Experience at a global B2B SaaS company**."* `:160` — "**450+ managers** … **22% improvement in leadership effectiveness**" attributed to *"Delivered as **AVP at a global life sciences organization**."* `book.html:270` gives qualitative versions attributed collectively to "Big 4 consulting, a global life sciences company … and high-growth enterprise technology." **Attribution is explicit at every occurrence — but to SaaS / life-sciences roles, NOT to Deloitte/EY/PwC** as your item 9 requires. (Set deliberately by commit #46.) | **Reconcile the conflict:** either your canon (Big 4) or the live copy (SaaS/life-sciences roles) is wrong. I did not change it — you rule. | **High** — public claims about where numbers were earned |
| **10. Org instrument defaults unknown quadrant → Compounding?** | `organizational-diagnostic.html:315–327,633–653,713` | **No — already fixed** (commit #40). Placement is computed client-side by `quadrantFor(dHigh,oHigh)` (a total function over the four canonical strings); the model no longer emits a quadrant; `FALLBACK` is keyed by that computed string and has all four keys. **There is no unrecognised-string path, so no default-to-Compounding.** (A retry message already exists for the *live-read/API* failure at `:691` and for rate-limit 429.) | None needed. Optional defence-in-depth guard, but the failure it targets can no longer occur. | None |
| **11. Row-level completion capture (both, email-independent)** | Individual: `diagnostic.html:1488–1536,1688,1693`; `netlify/functions/audit-research.js`. Org: `organizational-diagnostic.html:534–544,678–718`; `netlify/functions/diagnose.js` | **Individual = yes.** `captureResearch()` POSTs a durable payload (per-question `responses[]` — n, section, score, scored — for all 12 + reflective, plus scores/quadrant/demographics/consent) to the `audit-research` store, with retry + `localStorage` resend. It fires on completion at **both** the email-gate submit (`:1688`) **and** the skip button (`:1693`), so it is **independent of the email gate.** **Org = no.** `/diagnose` receives answers only to write the narrative — **it never persists them.** The only email-independent completion signal is the client-side Plausible "Diagnostic Completed" event (`:717`: quadrant/reflection/boundary/standard — no rows). Per-question rows reach the server only if the user submits the **email-gated** `/subscribe` (`:537`), and even then only quadrant+reflection+boundary+standard, **not** the rows. | To match the individual instrument, add a durable, email-independent row capture to the org flow (e.g. POST answers to a store from `run()`). | Med (org research data is being lost) |

---

## Item 12 — Version inventory

**In this repo / git history:** none of the requested source artifacts exist. `card.py`, `covers.py`, and `CANON_editorial_constants.md` are **absent from the working tree, from all branches, and from the entire git history** (searched every blob). The repo holds only PNG cover *images* (`book-cover.png`, `capability-audit-cover.png`, `density-book-cover.png`), never a `covers.py`. No PDFs are in the repo.

**In my working directories (this container):** none of them. So `card.py`, `covers.py`, and `CANON_editorial_constants.md` exist **nowhere I can reach** — they must be local to your machine. I cannot compare against or share those three back; if you drop them in the repo I'll diff them.

**In your Google Drive (accessible, owner `temidayoluwo@gmail.com`):** the PDFs and the ruling docs are there, in multiple versions. Newest of each is flagged. *Times are modifiedTime (UTC).*

### Book interior PDF
| File | Modified | Note |
|---|---|---|
| **`CapabilityAudit_Interior_5x8 (4).pdf`** (121,987 B) | **2026-07-11 21:03** | **Newest interior.** 5×8 print interior, "(4)". |
| `The_Capability_Audit_Reader_Version.pdf` (150,500 B) | 2026-06-17 00:28 | Earlier reader-format version. |
| `The_Capability_Audit.epub` | 2026-06-17 02:36 | EPUB build. |
| `CapabilityAudit_Cover_Wrap.pdf` (2.68 MB) | 2026-07-06 19:04 | Cover wrap, not interior. |
| `The_Capability_Audit (11).docx` / `(10)` / `(6)` | 2026-06-17 | Manuscript sources. |

⚠️ The site calls the book **"forty-eight pages"** (`book.html:199,202`, `index.html:181`), but your brief says **34pp**. One is stale — worth resolving.

### Field Kit PDF (six+ versions — highest staleness risk)
| File | Modified | Note |
|---|---|---|
| **`The_Capability_Formation_FieldKit.pdf`** (121,987 B) | **2026-07-28 20:11** | **Newest.** Sits in the same folder as the newest Diagnostic — likely your current working set. |
| `The Capability Formation FieldKit.pdf` (95,266 B) | 2026-07-20 22:34 | Prior build, different size. |
| `The Capability Formation Field Kit.pdf` (59,567 B) | 2026-07-20 15:12 | 59 KB build. |
| `The Capability Formation Field Kit (1).pdf` (59,567 B) | 2026-07-20 15:12 | Duplicate of above. |
| `The_20Capability_20Formation_20Field_20Kit.pdf` (59,567 B) | 2026-07-20 15:12 | URL-encoded-name duplicate. |
| `The Capability Formation Field Kit.pdf` (other folder) | 2026-07-19 20:17 | Oldest 59 KB build. |

### Capability Formation Diagnostic PDF (three versions)
| File | Modified | Note |
|---|---|---|
| **`The_Capability_Formation_Diagnostic_final (6).pdf`** (532,994 B) | **2026-07-29 01:00** | **Newest.** Content confirms canon: 12 statements, Density(1–6)/Optionality(7–12), high 19–30, low 6–18, boundary 17–21, matrix orientation correct. |
| `The_Capability_Formation_Diagnostic (3).pdf` | 2026-07-29 00:48 | 12 min earlier. |
| `Capability Formation Diagnostic.pdf` | 2026-07-27 18:23 | Two days older. |

### `card.py`, `covers.py`, `CANON_editorial_constants.md`
**Not found** in repo, git history, this container, or Drive. Drive has *card/cover assets* (`JULY 2026 … BRAND CARDS/` folder; `FourStates_*_SpotlightCard_*.svg/png`; `LinkedIn_Card_Diagnostic_*.png`; `cover-1280x720.svg/png`, `cover-1200x644.svg/png`) and *editorial notes* (`EDITORIAL NOTES/` folder, `JULY: Editorial Notes` doc) — but not the three code/constants files. They appear to live only on your machine.

### Retired-name artifacts still in Drive (item-5 relevant)
| File | Modified | Note |
|---|---|---|
| `The Capability Formation Audit Short Form.pdf` (+ 3 near-duplicates) | 2026-07-19 → 07-21 | Use the **retired** name "Capability Formation Audit." |
| `Capability_Formation_Audit_Short_Form.docx` | 2026-07-13 | Same retired name. |

### Naming ruling docs (so you can confirm which governs)
| File | Modified | Note |
|---|---|---|
| **`Naming_Architecture_Ruling_July29_2026.docx`** | **2026-07-30 01:25** | The 2026-07-29 ruling you referenced — newest naming authority. |
| `Capability_Formation_Naming_Ruling_v1_July24_2026.docx` | 2026-07-24 18:42 | Superseded v1. |
| `Capability Formation Funnel Audit and Revised Deployment Pack July29 2026.docx` | 2026-07-29 14:48 | Related deployment pack. |

**Note:** this Drive listing is not exhaustive — the query paginated and I stopped after capturing the newest of each requested artifact. I did **not** assume any file you hold is current; I can't see your local copies. **On your word I'll download and send back any of the newest PDFs above** (Field Kit `07-28`, Diagnostic `final (6)` `07-29`, interior `(4)` `07-11`), or diff `card.py`/`covers.py`/`CANON_editorial_constants.md` if you add them to the repo.

---

## Flagged for your ruling (no edits made)
1. **Item 9** — numbers attributed to SaaS/life-sciences roles on `/work`, not to Deloitte/EY/PwC. Canon vs. live copy conflict.
2. **Item 5** — the entire "AI Capability Readiness Diagnostic" instrument is unruled and promoted from `/diagnostic`.
3. **Item 4** — paid Field Kit promises numbered case studies that `/case-studies` doesn't contain.
4. **Item 6** — book waitlist ("hear it first"/"know before anyone") and coaching "Waitlist Open" vs. "No waiting list" contradiction.
5. **Item 7** — meta/pillars imply three scored pillars; body copy already says two. Fix copy or build pillar three.
6. **Book length** — "48 pages" on site vs. "34pp" in your brief.
