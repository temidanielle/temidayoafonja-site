# Website Current State and Career Move Review Fit Audit

**Date:** 2026-09-17
**Repository state audited:** `main` at `36ea8ac`
**Scope:** full public site, routing configuration, forms, offer architecture, and the proposed Career Move Review
**Type:** read-only audit. No file was edited, no form submitted, no deploy triggered, no external platform touched.

---

## A note on evidence classes, before anything else

Every finding below carries one of these labels. Please hold the distinction, because it matters for how much weight to put on each claim.

| Label | Meaning |
|---|---|
| **[SOURCE]** | Read directly from the deployed artifact in this repository. High confidence. |
| **[LIVE]** | Confirmed by loading the public website. |
| **[INTERPRETATION]** | My reading of what the evidence means. Arguable. |
| **[RECOMMENDATION]** | A proposed action. Not a fact. |
| **[UNVERIFIED]** | Could not be checked from here. Listed in section 13. |

**There are no [LIVE] findings in this report.** This container's network policy blocks `temidayoafonja.com`; every request returns `000` with the proxy refusing the CONNECT tunnel. The same applies to `*.netlify.app`, `app.netlify.com`, `api.convertkit.com`, `maven.com`, `gumroad.com` and `amazon.com`.

This is less damaging than it sounds, and I want to be precise about why. `netlify.toml` sets `publish = "."`, so **the repository root is the deployed artifact**. There is no build step, no framework, no server-side rendering. The HTML in this repository is the HTML the browser receives. What I cannot verify is the deployed state matching this commit, third-party destinations resolving, and anything depending on a real browser or real user.

Where that gap matters, I say so rather than papering over it.

---

## 1. Executive conclusion

The website is two businesses wearing one coat.

The enterprise business is complete and coherent. It owns the navigation, the homepage headline, every persistent call to action, and a clean path from framework to evidence to briefing to inquiry form.

The individual business, which is where the Career Move Review would live, is **structurally broken in a way that is invisible from the homepage**. Three findings carry the weight:

**Keep the Proof, a live $49 product, has zero inbound links from anywhere on the site.** [SOURCE] Across all twenty HTML files, the string `keep-the-proof` appears only in that page's own canonical tag and its own three Gumroad buttons. No navigation item, no footer link, no cross-link from any other page. It is reachable only by typing the URL or arriving from an external source. A paying product is invisible to its own website.

**The Field Kit page is orphaned, while the Field Kit product is not.** [SOURCE] `/fieldkit` has exactly one inbound link, from `keep-the-proof.html:515`, which is itself unreachable. Meanwhile `book.html` and `for-professionals.html` both send visitors **straight to the Gumroad checkout**, bypassing the sales page entirely. The $150 product's own argument for itself is never read by anyone who buys it.

**A one-to-one individual advisory service at $500 already exists.** [SOURCE] The Private Capability Position Read is sold on `for-professionals.html` and `fieldkit.html`, booked by `mailto:`. This is the single most consequential fact for the Career Move Review, because the proposed pilot price of $495 lands five dollars below an offer that is already live, and the proposed standard price of $750 sits above it with no stated reason for the gap.

**[INTERPRETATION]** The Career Move Review does not slot into an empty rung. It lands on top of an occupied one. Before it can be placed, a decision is required about what happens to the Private Capability Position Read. That decision is section 9, and it is the real finding of this audit.

A fourth finding is unrelated to the offer ladder but should not wait: **`AUDIT-REPORT.md`, a full internal strategic audit, sits at the publish root with no blocking rule and is publicly fetchable.** [SOURCE] Details in section 7.

---

## 2. Complete website and route inventory

### 2.1 How routing actually works

**[SOURCE]** `netlify.toml`, 302 lines. Redirects are evaluated top-down, first match wins, and a rule only beats a real file on disk when `force = true`.

Five force-404 rules come first, blocking `/docs/*`, `/content/*`, `/tests/*`, `/netlify/*` and `/_build/*`. These protect internal documents, the source of truth, the test suite, function source, and the print source of the Starter. All five are correctly ordered and correctly forced.

**What is not blocked:** every other file at the repository root, including `.md` files. See section 7.

### 2.2 Public pages

Twenty HTML files at the publish root. `Nav` = present in the main navigation. `Foot` = present in the footer.

| # | Page | Live URL | Nav | Foot | Audience | Primary promise | Primary CTA | Price | Destination | State |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Home | `/` | — | — | Both | Build capability that holds when conditions change | Bring a Consequential Decision | $2M+, 30% | `executive-briefing.html#inquiry` | Active |
| 2 | Capability Formation | `/framework.html` | Yes | Yes | Both | The proprietary framework | Read the Framework | — | internal | Active |
| 3 | Advisory | `/work.html` | Yes | Yes | Enterprise | Enterprise advisory ladder | Contact form | $2M+ | Formspree `xqpzegoj` | Active |
| 4 | Executive Briefing | `/executive-briefing.html` | Yes | Yes | Enterprise | Evidence-led decision review | Inquiry form | Not shown | Formspree `xqpzegoj` | Active |
| 5 | Evidence | `/case-studies.html` | Yes | Yes | Enterprise | Selected enterprise results | — | $2M+ | internal | Active |
| 6 | The Firm | `/about.html` | Yes | Yes | Both | Who Temidayo is | — | — | internal | Active |
| 7 | For Professionals | `/for-professionals.html` | **Yes** | Yes | Individual | Is your work still building you | Register Free | $150, $500 | Maven, Gumroad, mailto | Active |
| 8 | Speaking | `/speaking.html` | No | Yes | Enterprise | Keynotes and sessions | Inquiry form | — | Formspree `xgawaegz` | Active |
| 9 | Books & Tools | `/book.html` | No | Yes | Individual | The book and the Field Kit | Get the Field Guide | $150 | Amazon, Gumroad | Active |
| 10 | Capability Formation Diagnostic | `/diagnostic` | No | Yes | Both | 12 or 17 statements, ~12 min | Take the diagnostic | — | Formspree `xjgapael`, `/.netlify/functions/subscribe` | Active |
| 11 | Organizational Scan | `/organizational-diagnostic` | No | Yes | Enterprise | Free organizational Scan | Run the Scan | — | Formspree `mjgndvkp`, `/.netlify/functions/diagnose` | Active |
| 12 | AI Capability Readiness | `/ai-capability-readiness` | No | No | Enterprise | 15 behavioral statements on AI change | Run the diagnostic | — | Formspree, `ai-readiness-narrative` | **noindex, in sitemap** |
| 13 | Career Evidence Starter | `/career-evidence-starter` | No | No | Individual | Free 6-page fillable tracker | Get the Starter | Free | `/api/career-evidence-starter-subscribe` | Active |
| 14 | Career Decision Evidence Check | `/career-decisions` | No | No | Individual | Three-question evidence check | Submit | Free | `/api/career-decisions-subscribe` | **1 inbound link, from privacy** |
| 15 | Keep the Proof | `/keep-the-proof` | No | No | Individual | 60-minute career evidence system | Buy on Gumroad | **$49** | `gumroad.com/l/keep-the-proof` | **ORPHANED, 0 inbound** |
| 16 | Field Kit | `/fieldkit` | No | No | Individual | Evidence-led position assessment | Get the Field Kit | **$150** | `gumroad.com/l/czmqp` | **1 inbound, from an orphan** |
| 17 | Privacy | `/privacy.html` | No | Yes | Both | Data handling | — | — | internal | noindex, follow |
| 18 | Terms | `/terms.html` | No | Yes | Both | Terms of use | — | — | internal | noindex, follow |
| 19 | 404 | `/404.html` | — | — | Both | Page not found | Home | — | internal | noindex |
| 20 | Dashboard | `/dashboard` | No | No | Internal | Operator working view | — | — | localStorage only | **Force-404'd, correctly** |

### 2.3 Redirects

**[SOURCE]** All permanent and correct as far as static analysis can determine.

| From | To | Status |
|---|---|---|
| `/organizational-diagnostic.html` | `/organizational-diagnostic` | 301 forced |
| `/principles`, `/principles.html` | `/framework` | 301 |
| `/institutional-diagnostic`, `.html` | `/organizational-diagnostic` | 301 |
| `/diagnostic?audience=org` | `/organizational-diagnostic` | 301 forced, query-conditioned |
| `/audit` | `/diagnostic` | 301 forced |
| `/career-evidence-starter.html` | `/career-evidence-starter` | 301 forced |
| `/career-decisions.html` | `/career-decisions` | 301 forced |
| `/dashboard`, `/dashboard.html` | `/404.html` | 404 forced |
| `/docs/*`, `/content/*`, `/tests/*`, `/netlify/*`, `/_build/*` | `/404.html` | 404 forced |

**[SOURCE]** `/framework` and `/work` have **no explicit rewrite rule**. The navigation links to `framework.html` and `work.html`, but `404.html` and several in-page links use the extensionless `/framework` and `/work`. These rely on Netlify's default behavior of serving `foo.html` at `/foo`. **[UNVERIFIED]** whether that default is active on this site. If it is not, `/principles` 301s to a 404, and the 404 page's own navigation is broken.

### 2.4 External destinations

**[SOURCE]** Counted across all HTML.

| Destination | Occurrences | What it sells |
|---|---|---|
| `temidayoafonja.substack.com` | 18 | Writing, free |
| `gumroad.com/l/czmqp` | 5 | Field Kit, $150 |
| `amazon.com/dp/B0H4QY5GWY` | 3 | The Capability Audit |
| `gumroad.com/l/keep-the-proof` | 3 | Keep the Proof, $49 |
| `maven.com/p/8b3c40/...` | 3 | Stay or Leave assessment, free |
| `maven.com/terms` | 1 | Legal reference |

Five Formspree endpoints and six internal API paths handle the rest.

### 2.5 Repository files that are not pages

`/docs/` (11 internal documents), `/content/` (source of truth), `/tests/` (3 suites), `/netlify/functions/` (12 functions), `/_build/` (Starter print source), `/resources/` (the delivered PDF), `/images/`, `/fonts/`. All are force-404'd except `/resources/` and `/images/`, both deliberately.

---

## 3. Current offer ladder

### 3.1 What actually exists

**[SOURCE]**

**Individual, free:** Career Evidence Starter (6-page PDF, email-gated), Career Decision Evidence Check, Capability Formation Diagnostic, Stay or Leave assessment on Maven (23 September 2026), Substack.

**Individual, paid:** The Capability Audit on Amazon (price not shown), Keep the Proof $49, Field Kit $150, **Private Capability Position Read $500** (mailto booking).

**Enterprise, free:** Organizational Scan, AI Capability Readiness Diagnostic.

**Enterprise, paid:** Executive Briefing (price not shown), Advisory ladder (price not shown), Speaking (price not shown).

### 3.2 The ladder as a visitor can actually climb it

**[INTERPRETATION]** The designed ladder is Starter free → Keep the Proof $49 → Field Kit $150 → Private Read $500. The traversable ladder is:

```
Starter (free)  →  [ Keep the Proof $49 ]  →  Field Kit $150  →  Private Read $500
   3 inbound         ZERO INBOUND              via Gumroad        via mailto
   reachable         UNREACHABLE               page bypassed      no form
```

Only the Starter and the two top rungs are reachable, and the $150 rung is reached by skipping its own sales page.

### 3.3 The source of truth has drifted

**[SOURCE]** `content/site-source-of-truth.json` governs names, prices and claims. It records five offers: enterprise pathway, professional workshop, Private Capability Position Read, Lightning Lesson, Field Kit.

**It contains zero mentions of Keep the Proof and zero mentions of the Career Evidence Starter.** Two live products, one of them paid, are absent from the document the project treats as authoritative.

Its `routes.canonical` array lists fifteen routes and omits `/career-evidence-starter`, `/keep-the-proof` and `/fieldkit`. Its `external_urls` block omits the Keep the Proof Gumroad URL and still lists the retired Lightning Lesson Maven URL.

**[INTERPRETATION]** This is why Keep the Proof was never linked. It was never entered into the register that governs the site, so nothing downstream, including the navigation and the sitemap, ever knew to account for it.

---

## 4. Current navigation and information architecture

### 4.1 The navigation is enterprise-only

**[SOURCE]** Identical on all pages carrying a nav. Seven items:

Capability Formation · Advisory · Executive Briefing · Evidence · The Firm · For Professionals · **Bring a Consequential Decision** (CTA → `executive-briefing.html#inquiry`)

Six of seven serve the enterprise buyer. One serves the individual. The persistent CTA is enterprise.

**[INTERPRETATION]** An experienced professional arriving cold sees a firm that sells to their employer. Nothing in the navigation names their problem. "For Professionals" is the only door, and it is a category label rather than a question, sitting sixth in a row of six enterprise items.

### 4.2 The footer carries more than the nav

**[SOURCE]** Fourteen links: Capability Formation, Advisory, Executive Briefing, Evidence, Speaking, The Firm, Organizational Scan, Bring a Consequential Decision, Free Diagnostic, Career Growth Assessment, Books & Tools, Writing, Privacy, Terms.

**Absent: Keep the Proof, Field Kit, Career Evidence Starter, Career Decision Evidence Check.** Every individual product and lead magnet is missing from the footer.

### 4.3 Four pages have no footer at all

**[SOURCE]** `diagnostic.html`, `organizational-diagnostic.html`, `dashboard.html`, `404.html`.

The first two are the free instruments, the highest-intent individual and enterprise entry points on the site. A visitor who completes the diagnostic and does not accept the in-page offer has **no navigation out of the page except the browser back button**. [INTERPRETATION] This is a dead end at the moment of highest engagement.

### 4.4 URL form is inconsistent

**[SOURCE]** The nav links `framework.html` and `work.html`. `404.html` links `/framework` and `/work`. The sitemap mixes both conventions. Canonical tags mix both.

### 4.5 The sitemap does not match the site

**[SOURCE]** Sixteen URLs. Omits `/keep-the-proof` and `/fieldkit`, both live commercial pages. Includes `/ai-capability-readiness`, which carries `<meta name="robots" content="noindex, nofollow">`.

**[INTERPRETATION]** Two paid products are excluded from search, and one page is simultaneously submitted to search engines and told not to be indexed. The second is a direct contradiction and will be reported as such in Search Console.

---

## 5. Individual customer journey

### 5.1 New experienced professional, arrives at the homepage

**[SOURCE]** H1: "Build capability that holds when conditions change." Three of the homepage's primary buttons read "Bring a Consequential Decision."

The individual fork lives in a section titled "Start with the decision in front of you," roughly two-thirds down. Its card is labelled "For Professionals · Separate track" and asks "Is my work still building me?" with a button, "See What Is Available," and a link to the Starter.

**[INTERPRETATION]** The stated front door is "I help experienced professionals make career pivots and internal moves without starting over." The homepage does not say this anywhere. A professional must scroll past the framework, the enterprise entry point and the capability-position section to find a card acknowledging they exist. "See What Is Available" describes an inventory, not an outcome.

**Friction:** headline speaks to their employer; must scroll to be recognized; the label "Separate track" reads as secondary.

### 5.2 Considering a career pivot

**Entry:** `/for-professionals`. **[SOURCE]** Offered: the free 23 September Maven assessment, a link to the free Starter, the Field Kit at $150 via direct Gumroad, and the Private Capability Position Read at $500 via mailto.

**Friction:** the Field Kit button leaves the site for checkout without the visitor ever seeing the Field Kit page. The $500 offer has no booking form, no availability, no scope document and no scheduling link, only an email address. **[INTERPRETATION]** For a $500 commitment that is a significant ask. Keep the Proof at $49, the natural intermediate step between free and $150, is not offered here at all.

### 5.3 Considering an internal move

**[INTERPRETATION]** No page addresses internal moves distinctly. `/career-decisions` frames "stay, leave or reposition," which is closest, and it is reachable only from the privacy policy. The public front door promises "career pivots **and internal moves**"; the site treats them as one undifferentiated question. This is the clearest unserved intent on the site, and it is precisely the intent the Career Move Review proposes to serve.

### 5.4 Needs to preserve career evidence

**[SOURCE]** Best-served journey. `/career-evidence-starter` is linked from the homepage, `/for-professionals` and `/keep-the-proof`. Email capture through a Netlify function with consent handling and an edge rate limit.

**Friction:** the Starter's own next step is Keep the Proof, which is unreachable from everywhere else. **[INTERPRETATION]** The one healthy funnel on the individual side terminates at a product nothing else links to.

### 5.5 Wants a self-guided product

**[SOURCE]** `book.html`, in the footer as "Books & Tools," offers the Amazon book and a direct Field Kit Gumroad link. Keep the Proof is absent. **[INTERPRETATION]** The page named for tools omits one of the two tools.

### 5.6 Wants personalized help

**[SOURCE]** One option: Private Capability Position Read, $500, mailto, on two pages, in neither nav nor footer nor sitemap. **[INTERPRETATION]** The highest-value individual offer is the least discoverable and has the weakest conversion mechanism on the site. **This is the gap the Career Move Review is really being proposed to fill,** and it is worth being clear that the gap is one of packaging and routing, not of absence.

### 5.7 Newsletter reader and book buyer

**[SOURCE]** Substack, 18 links, healthy. The book links to Amazon from three pages; no price shown, deliberately per the source of truth. **[INTERPRETATION]** Neither audience is routed toward any paid individual service on return.

---

## 6. Enterprise customer journey

**[SOURCE]** Entry at the homepage, whose H1 and CTAs address this buyer. Path: Framework → Advisory → Executive Briefing → inquiry form (Formspree `xqpzegoj`). Evidence and Speaking support it. The free Organizational Scan and AI Capability Readiness Diagnostic feed in.

**[INTERPRETATION]** Coherent and complete. Three observations.

No price is shown at any point, appropriate for the engagement type but meaning qualification happens entirely in the inquiry.

The Organizational Scan has no footer, the same dead end as the individual diagnostic.

The AI Capability Readiness Diagnostic is `noindex, nofollow`, absent from nav and footer, and in the sitemap. **[UNVERIFIED]** whether it is a deliberate unlisted asset used in outbound work or an unfinished page. This materially changes whether it should be preserved or retired, and I cannot tell from the repository.

---

## 7. Broken, stale or confusing elements

### 7.1 Internal audit publicly served — highest priority

**[SOURCE]** `AUDIT-REPORT.md` sits at the publish root. It opens:

> "# Capability Formation Platform: Strategic Audit / Prepared as an external review by a boutique executive-advisory brand studio / Date: 2026-06-03 · Scope: full site (11 HTML pages, design system, IA, conversion, credibility)"

No redirect rule blocks `.md` files at the root. `robots.txt` does not disallow it. It is therefore fetchable at `https://temidayoafonja.com/AUDIT-REPORT.md`. `README.md` is exposed the same way, though it contains only a title.

**[INTERPRETATION]** This is the same class of exposure as the `/_build/*` finding: an internal strategic document readable by anyone who guesses a filename, including competitors and prospects mid-evaluation. It is the most consequential non-commercial finding in this audit.

**Note on this report:** for exactly this reason, the file you are reading was written to `docs/`, which is force-404'd, rather than to the root where it was nominally requested. Placing it at the root would have published it.

### 7.2 Stray photograph at the publish root

**[SOURCE]** `DSCF4781 1 (1).jpg`, 871 KB, added in commit `c0f3fc4` ("Add files via upload") through the GitHub web interface. Referenced by no page. Publicly fetchable. **[UNVERIFIED]** whether intentional staging or accidental.

### 7.3 Keep the Proof is unreachable

Covered in sections 1 and 3. The single most commercially costly finding.

### 7.4 The Field Kit page is bypassed

**[SOURCE]** `book.html:230` and `for-professionals.html:250` link directly to Gumroad. `/fieldkit` has one inbound link, from an orphaned page. **[INTERPRETATION]** Every argument on the Field Kit page is unread by the people who buy it, and unreadable by the people who do not.

### 7.5 A claim drops its required qualifier

**[SOURCE]** `docs/claims-ledger.md` sets the approved wording as "$2M+ estimated turnover cost avoidance" and notes: "'Estimated' is doing important work in this claim and should not be dropped."

Three of four public occurrences carry it. One does not: `index.html:342` reads "30% retention improvement · $2M+ turnover cost avoidance." **[INTERPRETATION]** One word, on the homepage, against an explicit written instruction. Low effort to fix, disproportionate exposure if left.

### 7.6 Sitemap and robots contradictions

Covered in 4.5.

### 7.7 Stale next-step configuration

**[SOURCE]** `career-evidence-starter.html:620` stores a session dated "Wednesday, September 2, 2026" with `available_until` of `2026-09-02T18:45:00-05:00`. The September reschedule updated `career-decisions.html` to 9 September and missed this page. Both have expired and serve the Field Kit fallback, so **nothing incorrect renders**. The stored data is wrong; the visible behavior is correct.

### 7.8 Two diagnostics with adjacent names

**[SOURCE]** "Capability Formation Diagnostic" at `/diagnostic`, "Organizational Capability Formation Scan" at `/organizational-diagnostic`, "AI Capability Readiness Diagnostic" at `/ai-capability-readiness`, plus "Career Decision Evidence Check" at `/career-decisions`. **[INTERPRETATION]** Four free instruments with overlapping names. The source of truth carries a naming canon (Scan, Diagnostic, Read) that the page titles do not consistently follow.

### 7.9 Dead ends on the instrument pages

Covered in 4.3.

---

## 8. Conversion and UX gaps

**[INTERPRETATION]** throughout this section.

**Free does not lead to paid.** The Starter leads to Keep the Proof, which nothing else links to. The Diagnostic ends without a footer. The Career Decision Evidence Check is reachable only from the privacy policy.

**Paid self-guided does not lead to personalized.** `/fieldkit` presents the $500 Private Read, and `/for-professionals` presents both. But `/fieldkit` is orphaned, so the bridge is only crossed by visitors who arrive at `/for-professionals` and scroll past the free session.

**The $500 offer has no conversion mechanism.** A `mailto:` link, no form, no scheduling, no availability, no scope document. Every other significant offer on the site has a form.

**Price visibility is uneven.** $49, $150 and $500 are shown. The book, the Executive Briefing, the Advisory ladder and Speaking show nothing.

**Terminology is unexplained at the point of decision.** Capability Formation, Capability Position Read, Proof Line, Density, Optionality, Alumni Capital, Four States. `/framework` explains them; the product pages assume them. **A visitor cannot pick between Keep the Proof, the Field Kit and the Private Read without already understanding the method.**

**Competing calls to action.** `/for-professionals` presents a free Maven session, a free Starter, a $150 Gumroad checkout and a $500 email inquiry in one scroll, with no stated basis for choosing.

**Mobile.** [SOURCE] `nav.js` builds an accessible overlay menu with `inert` backdrop handling and Escape support, which is better than most. Two mobile defects were found and fixed this month, both invisible on desktop, which suggests desktop-only review has been the norm.

**Trust and proof.** [SOURCE] Enterprise evidence is strong. **No named individual testimonial, outcome or review appears for any individual product.** [INTERPRETATION] A $500 one-to-one service with no individual proof is a hard sell, and this applies with equal force to the Career Move Review.

**No analytics claims are made in this report.** Plausible is installed; this container cannot reach it and no exported data exists in the repository.

---

## 9. Exact recommended fit for the Career Move Review

### 9.1 The blocking question

**[SOURCE]** The Private Capability Position Read already exists at $500, one-to-one, individual, for professionals, sold on `for-professionals.html` and `fieldkit.html`.

Compare:

| | Private Capability Position Read | Career Move Review (proposed) |
|---|---|---|
| Price | $500 | $495 pilot, $750 standard |
| Format | One-to-one session | 90-minute advisory session |
| Deliverable | Personalized Next-Move Note | Written Career Move Summary |
| Input | Your evidence | Résumé or LinkedIn, one target role |
| Question | Where am I positioned? | Does my experience fit this move? |
| Booking | mailto | proposed form and checkout |

**[INTERPRETATION]** These are not the same service. The Read interprets a position; the Review tests a specific intended move against evidence. That is a real and defensible distinction. But it is a distinction a buyer cannot make from a price list, and $495 against $500 is indistinguishable in practice.

**[RECOMMENDATION]** Resolve this before building anything. Three options:

**Option A, replace.** The Career Move Review supersedes the Private Capability Position Read. One individual advisory service, clearly named after the decision it serves, with a real booking flow. Cleanest. Loses the Read's positioning language, which is well written.

**Option B, differentiate by input.** Keep both, and separate them on what the client brings: the Read interprets Field Kit evidence the client has already produced, and is sold only to Field Kit owners; the Review takes a résumé and a target role and is sold cold. Requires a visible price gap. $500 and $750 is defensible; $500 and $495 is not.

**Option C, reposition the Read upward.** The Review becomes the entry advisory service at $495 to $750, and the Read becomes a deeper follow-on at a higher price.

**My recommendation is Option A.** [INTERPRETATION] The Read has been live for months with no form, no scheduling link and no page of its own, which is not the shape of an offer being actively sold. The Review is better specified, matches the stated front door ("pivots and internal moves") far more closely, and names a decision rather than a method. Two near-identically priced one-to-one services on a site that cannot currently route traffic to either is the wrong problem to take on.

### 9.2 Placement, assuming Option A

**[RECOMMENDATION]**

**Proposed URL:** `/career-move-review`
Clean route, 200 rewrite to `career-move-review.html`, plus a forced 301 from the `.html` form. This matches the pattern already used for `/career-evidence-starter` and `/career-decisions` and is the established convention.

**Its own page: yes.** A $495 to $750 service with an intake, a session, a written deliverable and a follow-up cannot be sold from a card. It needs scope, exclusions, process, who it is not for, and a booking mechanism.

**Navigation label:** do not add a top-level item. The navigation has seven items and is already enterprise-heavy; adding an individual service directly would muddle the separation the homepage deliberately maintains.

Instead, **make `/for-professionals` the individual hub it already almost is**, and surface the Review as its primary paid call to action. If a navigation change is wanted, the higher-value change is relabelling "For Professionals" to something that names the question, but that is a copy decision and outside this audit.

**Homepage:** replace the button on the existing individual card. "See What Is Available" becomes a route to the Review, with the free Starter retained as the secondary link already present. One line of change, on the card that already exists, in the section already built to fork the two audiences.

**Pages that should link to it:**

| Page | Placement | Why |
|---|---|---|
| `/for-professionals` | Replaces the $500 card in "Continue the Read Privately" | The only individual hub |
| `/` homepage | Primary CTA on the existing individual card | Existing fork, no new section |
| `/fieldkit` | Replaces the $500 private band | Self-guided to personalized bridge |
| `/keep-the-proof` | Next step after the system | Completes the ladder, **once Keep the Proof is reachable** |
| `/career-evidence-starter` | Secondary, below the Keep the Proof step | Free to paid, without jumping $0 to $495 |
| `/career-decisions` | After results | Highest-intent individual moment |
| `/diagnostic` | In the individual results box | Highest-intent moment, **needs a footer too** |
| `/about` | One line, "work with Temidayo directly" | Trust to action |
| `/book` | Card alongside the Field Kit | Tools page should list services |

**Pages it should link back to:** `/framework` for method, `/career-evidence-starter` for the free preparatory step, `/keep-the-proof` and `/fieldkit` as self-guided alternatives for those not ready, and `/executive-briefing` as a single quiet line for anyone who arrives with an organizational question.

**Relationship to the Field Kit:** complementary, not sequential. The Field Kit is the method run alone; the Review is the method run with Temidayo against a specific target role. Do not require one before the other. **[SOURCE]** `/fieldkit` already carries this framing for the $500 Read and it can be inherited directly.

**Relationship to Keep the Proof:** preparatory. Keep the Proof produces the evidence record; the Review tests that evidence against a target move. **[INTERPRETATION]** This is the most natural ladder on the site, and it is currently unbuildable because Keep the Proof is orphaned. **Fixing that is a prerequisite, not a nice-to-have.**

**Relationship to the Executive Briefing:** none, beyond a single de-routing line. Different buyer, different budget, different question.

**Who should not be routed to it:** organizational, talent and business leaders; anyone seeking résumé writing, job placement, interview preparation, therapy or ongoing coaching; anyone below roughly ten years of experience. **[RECOMMENDATION]** State the exclusions on the page. They protect the positioning and pre-qualify better than any form field.

**Qualification form:** yes, and it should precede payment. The decision intake described in the proposal is the qualification form. **[RECOMMENDATION]** Intake first, then a booking and payment link issued on acceptance. This protects against mismatched clients during the five-client pilot, when a single bad fit is twenty percent of the evidence base.

**Direct checkout:** not for the pilot. **[INTERPRETATION]** Gumroad is already the checkout for both self-guided products and could carry this. But an advisory service with a qualification step should not be self-serve at the start.

**Should an existing page be repurposed?** **[RECOMMENDATION]** No new page is needed for the Read's content, but a new page is needed for the Review. The nearest repurposing candidate is the $500 block on `/for-professionals`, and under Option A it is replaced rather than repurposed. `/career-decisions` is not a candidate: the source of truth states explicitly that it "is a URL and nothing else" and "must never be presented as" a paid offer.

### 9.3 What must be true before the Review is added

**[RECOMMENDATION]** In order.

1. **Decide the fate of the Private Capability Position Read.** Everything else depends on it.
2. **Make Keep the Proof reachable.** Without this the ladder below the Review does not exist.
3. **Link the Field Kit page, or retire it and sell from `/for-professionals`.** Either is defensible; the current state is not.
4. **Add the Review to the source of truth before writing the page,** so it does not repeat Keep the Proof's history.
5. **Give `/diagnostic` and `/organizational-diagnostic` footers.** High-intent dead ends.
6. **Decide what individual proof can honestly be shown.** A $750 service with no individual evidence is a hard sell, and nothing may be invented.
7. **Remove `AUDIT-REPORT.md` from the publish root.** Unrelated, but do not ship a new commercial page while an internal strategic audit is publicly readable.

---

## 10. Proposed future sitemap

**[RECOMMENDATION]** Structural only. No copy.

```
/                                    Homepage, two clear audience doors
│
├── ENTERPRISE
│   ├── /framework
│   ├── /work
│   ├── /executive-briefing
│   ├── /case-studies
│   ├── /speaking
│   ├── /organizational-diagnostic          + footer
│   └── /ai-capability-readiness            resolve status first
│
├── INDIVIDUAL  ← /for-professionals becomes the hub
│   ├── /for-professionals
│   │
│   ├── Free
│   │   ├── /career-evidence-starter
│   │   ├── /career-decisions               link from the hub, not privacy
│   │   └── /diagnostic                     + footer
│   │
│   ├── Self-guided
│   │   ├── /keep-the-proof    $49          MUST become reachable
│   │   ├── /fieldkit          $150         link it or retire it
│   │   └── /book
│   │
│   └── Advisory
│       └── /career-move-review   $495 → $750      NEW
│
└── SHARED
    ├── /about
    ├── /privacy
    └── /terms
```

**Sitemap.xml changes:** add `/keep-the-proof`, `/fieldkit`, `/career-move-review`. Remove `/ai-capability-readiness` or remove its `noindex`, but do not keep both. Settle on one URL convention.

---

## 11. Page-by-page change plan

**[RECOMMENDATION]** throughout. No page is recommended for removal merely for being outside the navigation.

### Preserve

| Page | Why |
|---|---|
| `/framework` | Load-bearing for both audiences. Every term routes here. |
| `/work`, `/executive-briefing`, `/case-studies` | The enterprise path is coherent and converting. Do not disturb. |
| `/about` | Serves both audiences. Add one line to the Review. |
| `/career-evidence-starter` | Best-built individual page. Only its next step needs to become reachable. |
| `/privacy`, `/terms`, `/404` | Correct as they are. |
| `/dashboard` | Correctly force-404'd. Keep in repo, keep blocked. |
| `/speaking` | Outside nav but footer-linked and serving a real enterprise function. |

### Revise

| Page | Change | Evidence |
|---|---|---|
| `/` | Individual card CTA routes to the Review; restore "estimated" at line 342 | §5.1, §7.5 |
| `/for-professionals` | Becomes the individual hub: add Keep the Proof, link the Field Kit page rather than Gumroad, replace the $500 card with the Review | §3.2, §5.2 |
| `/keep-the-proof` | No page change needed. It needs **inbound links** | §1, §7.3 |
| `/fieldkit` | Link it from the hub and the book page; add the Review as the personalized step | §7.4 |
| `/diagnostic` | **Add a footer.** Add the Review to the individual results box | §4.3, §5.6 |
| `/organizational-diagnostic` | **Add a footer** | §4.3 |
| `/book` | Add Keep the Proof; link the Field Kit page rather than Gumroad; card for the Review | §5.5 |
| `/career-decisions` | Link from the individual hub, not only from privacy | §5.3 |
| `sitemap.xml` | Add the two missing products; resolve the noindex contradiction | §4.5 |
| `content/site-source-of-truth.json` | Add Keep the Proof, the Starter and the Review; refresh routes and external URLs | §3.3 |

### Consolidate

| What | Recommendation |
|---|---|
| Private Read and Career Move Review | One service, per §9.1 Option A |
| Field Kit purchase paths | All Field Kit links go to `/fieldkit`; only `/fieldkit` links to Gumroad |
| Four free instruments | Not a merge. Apply the source of truth's naming canon so the names stop competing |

### Remove or retire

| What | Recommendation | Why |
|---|---|---|
| `AUDIT-REPORT.md` at root | **Remove from the publish root** | Internal strategic document, publicly fetchable. §7.1 |
| `DSCF4781 1 (1).jpg` | Remove or relocate, after confirming intent | Unreferenced 871 KB file publicly served. §7.2 |
| Stale `NEXT_STEP` date on the Starter | Correct the stored date | Wrong data, currently invisible. §7.7 |
| `/ai-capability-readiness` | **Decide, do not default** | Cannot determine from the repository whether it is a deliberate unlisted asset. §6 |

**Nothing else is recommended for removal.** `/speaking`, `/book`, `/career-decisions`, `/diagnostic` and `/fieldkit` are all outside the navigation and all serve real journeys. Their problem is routing, not existence.

---

## 12. Career Move Review page requirements

**[RECOMMENDATION]** Requirements only, no copy, per instruction.

**Route.** `/career-move-review` rewriting to `career-move-review.html` at 200, plus `/career-move-review.html` → `/career-move-review` at 301 forced. Insert after the Starter rules in `netlify.toml`, before the API rules.

**Structural requirements.**

The page must state the decision it serves before it states the method. The buyer arrives with "should I make this move," not "what is Capability Formation."

It must show the price, and during the pilot must state plainly that the pilot price is limited to the first five clients and what the price becomes afterwards. **[INTERPRETATION]** Publishing "$495 for the first five, $750 after" is honest scarcity, verifiable, and it pre-commits the increase.

It must carry the exclusions verbatim: not résumé writing, not job placement, not interview preparation, not therapy, not ongoing career coaching. These protect the positioning better than any qualifying question.

It must state what the client brings (résumé or LinkedIn, one target role or intended move) and what they receive (90-minute session, written Career Move Summary, one clarification follow-up), with a timeline for the summary.

It must name the audience: experienced professionals, roughly ten or more years. And it must de-route the enterprise buyer in one quiet line.

It must explain its relationship to Keep the Proof and the Field Kit without requiring either.

**Form requirements.** The decision intake is the qualification step and must precede payment. Follow the established pattern: post to a Netlify function under `/api/*`, add an edge rate limit in `netlify.toml` mirroring the two existing ones (`window_limit = 5`, `window_size = 180`, `aggregate_by = ["domain", "ip"]`), keep all secrets in Netlify environment variables, and carry the same explicit consent handling and `POLICY_VERSION` stamping the Starter uses.

**[SOURCE]** Netlify Blobs has been failing site-wide since 2026-08-20, which is why the edge rate limit is not optional: the function-level limiter both existing forms rely on is currently inert.

**Governance requirements.** Add to `content/site-source-of-truth.json` **before** the page is written: name, price, pilot terms, deliverables, exclusions, audience, route, and relationship to the other offers. Add to `sitemap.xml`. Add inbound links per §9.2 in the same change, so it does not launch orphaned.

**Legal.** **[SOURCE]** `docs/legal-review-required.md` is parked by operator instruction. A paid one-to-one advisory service with a written deliverable raises questions that document was opened to handle. **[RECOMMENDATION]** This is a counsel question, not a copy question, and I am flagging it rather than answering it.

**Proof.** **[RECOMMENDATION]** Decide in advance what can honestly be shown. Nothing may be invented. If no individual outcome can yet be cited, the pilot is the mechanism for producing one, and the page should stand on scope and specificity until then.

---

## 13. Questions that cannot be answered from the live site or repository

**Blocked by this container's network policy:**

1. Does the live site match `36ea8ac`? Is there an unmerged or failed deploy?
2. Do the Gumroad pages load, and do they show $49 and $150?
3. Does the Amazon listing resolve, and at what price?
4. Does the Maven page show 23 September 2026?
5. Does `/framework` resolve, given it has no explicit rewrite rule? If not, `/principles` 301s to a 404 and the 404 page's own nav is broken.
6. Is `AUDIT-REPORT.md` actually fetchable in production? Static analysis says yes; only a request confirms it.
7. Do the five Formspree endpoints still accept submissions?

**Requires information outside the repository:**

8. **Is the Private Capability Position Read actively selling?** How many have been sold, at what close rate? This determines §9.1 entirely.
9. **Is `/ai-capability-readiness` deliberate or abandoned?** Determines preserve or retire.
10. **Was `DSCF4781 1 (1).jpg` intentional?**
11. Does a source document exist tying the 30% and $2M+ figures to a population, baseline and method? `docs/claims-ledger.md` says none is on file.
12. Has the Career Move Review been delivered informally already? Any prior client evidence?
13. Is there capacity for five pilot clients plus existing enterprise work?
14. Do the Career Move Review and the Keep the Proof Gumroad products need to share a checkout?
15. What does Plausible show about `/keep-the-proof` traffic? **[INTERPRETATION]** If it has non-zero traffic while having zero inbound links, that traffic is entirely external and worth understanding.

---

## 14. Evidence appendix

### 14.1 Method

Read-only inspection of `main` at `36ea8ac`. No file modified, no form submitted, no deploy, no external platform contacted beyond connectivity tests that were refused by the proxy.

Because `netlify.toml` declares `publish = "."` with no build step, the repository root is the deployed artifact and static inspection is a high-fidelity proxy for the live site. It is not a substitute for it.

### 14.2 Files inspected in full

`netlify.toml` (302 lines) · `sitemap.xml` · `robots.txt` · `nav.js` · `content/site-source-of-truth.json` · `package.json`

### 14.3 HTML files inspected

All twenty at the publish root: `404` · `about` · `ai-capability-readiness` · `book` · `career-decisions` · `career-evidence-starter` · `case-studies` · `dashboard` · `diagnostic` · `executive-briefing` · `fieldkit` · `for-professionals` · `framework` · `index` · `keep-the-proof` · `organizational-diagnostic` · `privacy` · `speaking` · `terms` · `work`

Extracted per file: title, meta description, canonical, robots, navigation links, footer links, headings, calls to action, prices, external destinations, form elements and endpoints.

### 14.4 Internal documents consulted

`docs/claims-ledger.md` · `docs/forms-audit.md` · `docs/career-evidence-starter-architecture.md` · `docs/legal-review-required.md` (parked, not revised) · `docs/data-inventory.md` · `docs/final-reconciliation-report.md`

### 14.5 Key queries and results

| Query | Result |
|---|---|
| `href` containing `keep-the-proof` | 4 hits, all inside `keep-the-proof.html` |
| `href` containing `fieldkit` | 2 hits: own canonical, `keep-the-proof.html:515` |
| `href` containing `career-evidence-starter` | 4 hits: own canonical, `index:322`, `for-professionals:222`, `keep-the-proof:483` |
| `href` containing `career-decisions` | 2 hits: own canonical, `privacy.html:108` |
| Prices in HTML | $49 ×4, $150 ×6, $500 ×2, $2M ×4 |
| External destinations | Substack 18, Gumroad czmqp 5, Amazon 3, Gumroad keep-the-proof 3, Maven 3, Maven terms 1 |
| Pages without a footer | `diagnostic`, `organizational-diagnostic`, `dashboard`, `404` |
| Root `.md` blocked by redirect | No rule matches; publicly served |
| "Keep the Proof" in source of truth | 0 occurrences |
| "Career Evidence Starter" in source of truth | 0 occurrences |
| `$2M+` without "Estimated" | 1 of 4: `index.html:342` |
| Live site reachability | `000`, proxy refused CONNECT |

### 14.6 Live pages inspected

**None.** The network policy blocked every attempt. This is stated plainly rather than implied, because a reader would reasonably assume a website audit included loading the website.

---

## Closing note

Three findings would change what a visitor experiences tomorrow, independently of the Career Move Review: Keep the Proof cannot be reached, the Field Kit page is bypassed by its own buy buttons, and an internal strategic audit is publicly readable at the root.

The Career Move Review is a good fit for this business and matches the stated front door more closely than anything currently on the site. It should not be added to a ladder whose middle rung is missing.

**No website file was changed in producing this report.**
