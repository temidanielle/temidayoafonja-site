# Capability Formation Platform — Strategic Audit
**Prepared as an external review by a boutique executive-advisory brand studio**
Date: 2026-06-03 · Scope: full site (11 HTML pages, design system, IA, conversion, credibility)

---

## 1. Executive Summary

This is already a *good* site. The visual language — navy/gold/cream, Cormorant Garamond display over DM Sans body, the noise-grain texture, generous whitespace — is genuinely premium and coherent. The intellectual property (the Density → Optionality → Alumni Capital framework, the Career Strategy Matrix, the interactive audit) is differentiated and well-articulated. Voice is consistent and confident.

What separates this from a *world-class* executive-advisory platform is not taste — it's **rigor in the unglamorous layers**: there is no mobile navigation at all, no analytics to measure conversion, no social/SEO metadata (shared links render bare), no third-party credibility (zero named clients, testimonials, logos, or media), and an information architecture with orphaned pages and inconsistent navigation. The brand *looks* like a $50k-engagement firm; the plumbing reads like a personal site.

The 20 recommendations below close that gap. Five are **critical** (they are actively costing reach, conversion, or credibility right now). The rest are sequenced by impact-to-effort.

**The single most damaging finding:** on mobile, the navigation menu is `display:none` with no hamburger replacement. Mobile visitors can reach *only* the homepage and whatever is linked in the body. For a thought-leadership brand where 50–70% of traffic from Substack/LinkedIn is mobile, this alone is likely capping conversion severely.

---

## 2. What's Working (preserve these)

- **Visual identity** is distinctive and disciplined — the gold-on-navy editorial system would not look out of place next to Ideo, Feld, or a boutique like Reforge/August.
- **The framework as IP.** Naming the model, the four quadrants, and the equation gives the brand a proprietary spine most consultants lack.
- **The interactive audit** is a real lead magnet with a thoughtful flow: hook → email gate → audience fork → scored questions → quadrant result → contact. This is the conversion engine and it's well-built.
- **Dual-audience positioning** (organizational leaders + individuals) is handled cleanly without diluting either.
- **Copy voice** — declarative, slightly literary, never hype. Right register for the buyer.

---

## 3. Top 20 Recommendations (prioritized)

### TIER 1 — CRITICAL (do first; these are bleeding now)

**1. Build a real mobile navigation. [Impact: Very High · Effort: Low]**
Every page does `.nav-links { display:none }` below ~768–960px with **no hamburger**. Mobile users have no way to reach Framework, About, Work, Book, Audit, etc. Add an accessible hamburger → slide-in/overlay menu with all links + the "Take the Audit" CTA. This is the highest ROI fix on the site.

**2. Add Open Graph + Twitter Card metadata to every page. [Impact: Very High · Effort: Low]**
Zero pages have `og:*` or `twitter:card` tags. When the audit, an essay, or the book is shared on LinkedIn/Substack/iMessage, it renders as a bare blue link — devastating for a brand whose entire growth loop is *sharing ideas*. Add `og:title`, `og:description`, `og:image` (a designed 1200×630 card per key page), `og:type`, `twitter:card=summary_large_image`. Create 2–3 branded share images using the existing navy/gold system.

**3. Install analytics + conversion tracking. [Impact: Very High · Effort: Low]**
No analytics on any page (no GA4, Plausible, Fathom). You currently cannot answer: how many start the audit, where they drop, which audience fork converts, which page drives "Work With Me." Add a privacy-light tool (Plausible/Fathom fit the premium, low-clutter aesthetic) plus event tracking on: audit start, email gate, audit complete, each contact-form submit. You cannot optimize a funnel you can't see.

**4. Fix the broken information architecture: surface or retire orphan pages. [Impact: High · Effort: Low]**
`speaking.html` is a complete, polished page that is **not linked from any navigation or footer** — it's invisible. `dashboard.html` and `capability-formation-audit-v3.html` are also unreferenced (look like staging/dev artifacts). Decision needed: (a) add **Speaking** to the primary nav (it's a core revenue line and credibility surface), and (b) delete or `noindex` the dev artifacts so they don't get crawled and dilute the brand.

**5. Add third-party credibility / social proof. [Impact: Very High · Effort: Medium]**
There is **not a single testimonial, named client, logo, media mention, or attributed quote** anywhere. Case studies are fully anonymized and the metrics ($2M+ savings, 30% retention, 46-pt NPS, AI Innovation Award) are unverifiable assertions. Premium buyers de-risk with proof. Add, in priority order: (1) 2–3 attributed testimonials (even "CHRO, Fortune 500 life sciences" with a real name/title where permissible), (2) a logo strip of industries/firms worked with (the hero already name-drops Deloitte/PwC/EY as *employers* — clarify that vs. *clients*), (3) any podcast/publication/speaking logos. This is the biggest credibility lever after the mobile fix.

---

### TIER 2 — HIGH IMPACT

**6. Per-page meta descriptions + canonical + sitemap/robots. [Impact: High · Effort: Low]**
Only `index.html` has a meta description; 10/11 pages have none. No `rel=canonical`, no `sitemap.xml`, no `robots.txt`. Write a unique 150–160 char description per page, add canonicals, generate a sitemap, add robots.txt. Foundational SEO for discoverability of the framework terms.

**7. Add JSON-LD structured data (Person + Organization). [Impact: Medium-High · Effort: Low]**
No structured data anywhere. Add `Person` schema (Temidayo Afonja, jobTitle, sameAs → Substack/LinkedIn) and `Organization` schema (The Density Group LLC). Drives rich results and entity recognition — important for a named thought leader.

**8. Replace the slow "within one business week" contact path with scheduling. [Impact: High · Effort: Low]**
A premium advisory buyer who fills the form expects momentum. "Response within one business week" signals low availability/low priority. Add an embedded Calendly/Savvycal "Book a diagnostic conversation" option alongside the form, at least for qualified org leaders. Speed of first response is a top differentiator for boutique firms.

**9. Strengthen the homepage hero's proof and clarity of offer. [Impact: High · Effort: Medium]**
The hero is beautiful but the credentials row ("Deloitte / PwC / EY / 16 Years") reads ambiguously as clients vs. employers. Tighten: a one-line positioning statement of *who she helps and what changes*, then a clearly-labeled credibility row ("16 years across Deloitte, PwC, EY · Life Sciences · SaaS"). Consider a single hero stat that quantifies outcome (e.g., "$2M+ workforce cost reduced · 30% retention lift").

**10. Consolidate the design system into one shared stylesheet. [Impact: Medium (high for consistency) · Effort: Medium]**
~250 lines of near-identical CSS are duplicated inline in all 11 pages. This is why nav order and footers have already drifted (see #11). Extract to a single `styles.css`. Reduces page weight, guarantees visual consistency, and makes every future change one edit instead of eleven. This is the foundation that makes the rest cheap to maintain.

**11. Fix navigation/footer inconsistencies and bugs. [Impact: Medium · Effort: Low]**
- `principles.html` nav reorders items (Work With Me before Principles) — inconsistent with every other page.
- `principles.html` footer has a **duplicate "Principles" link** (one even carries `class="active"`) — a visible bug.
- `book.html` footer is missing Principles and Case Studies.
- Nav omits **Speaking** everywhere (see #4).
Standardize one nav and one footer (trivial once #10 is done).

**12. Make the credibility metrics verifiable and consistent. [Impact: High · Effort: Medium]**
The same numbers recur (30% retention, $2M+, 46-pt NPS, 450+ managers, 22% leadership effectiveness, 90-day integration). Anchor each to a case study and, where possible, a method or source ("measured over 18 months, B2B SaaS, ~1,200 employees"). Unsourced precision reads as marketing; sourced precision reads as evidence. This converts the existing case-studies page from claims into proof.

---

### TIER 3 — ELEVATION & POLISH

**13. Add a "Featured In / As Seen" and media-kit surface. [Impact: Medium-High · Effort: Medium]**
World-class thought leaders centralize proof of authority: podcast appearances, articles, talks, a downloadable speaker one-sheet + headshots. The Speaking page is close — add a press/media-kit block and a downloadable PDF capability statement (already referenced as "available upon request" — make it self-serve).

**14. Introduce a lightweight scroll-reveal + interaction system. [Impact: Medium · Effort: Low-Medium]**
Current animations are CSS `fadeUp` with fixed delays that fire on load regardless of viewport — content below the fold has often already "animated" before it's seen. Add `IntersectionObserver`-based reveals so sections animate as they enter view. Subtle, but it's the kind of motion polish that signals craft on premium sites.

**15. Elevate the audit results into a shareable, gated asset. [Impact: High · Effort: Medium]**
The audit is the crown jewel. Two upgrades: (a) make the result **shareable** ("I'm in the Compounding quadrant" → pre-built OG card) to turn the diagnostic into a growth loop; (b) offer a **PDF results report** delivered by email — increases perceived value and gives a reason for the email capture beyond "results." This compounds #2 and #3.

**16. Add an accessibility & contrast pass. [Impact: Medium · Effort: Low-Medium]**
`--cream-70`/`--slate` body text on navy, plus 9–13px uppercase labels with wide letter-spacing, likely fail WCAG AA in places. Form inputs use placeholders as labels (no `<label>`), which hurts screen readers and disappears on focus. Add visible/`aria` labels, check contrast ratios, ensure focus states on all interactive elements, add `prefers-reduced-motion`. Accessibility is now a baseline credibility signal for enterprise buyers (procurement increasingly asks).

**17. Add a real favicon/OG image asset audit and a 404 page. [Impact: Low-Medium · Effort: Low]**
Favicons are wired up well. Missing: a designed `og-image`, an `apple-touch-icon` color check, and a branded **404 page** (default Netlify 404 breaks the spell). Small touches that boutique firms never skip.

**18. Differentiate the two audiences earlier in the journey. [Impact: Medium · Effort: Medium]**
The org-leader buyer (5-figure+ engagements) and the individual (coaching/waitlist) have very different intent and value. Consider an explicit homepage fork ("I lead an organization" / "I'm navigating my own career") that routes each to a tailored path. The audit already forks internally; doing it at the top of funnel raises relevance and qualified conversion. Validate against #3 data before committing.

**19. Add an email-capture / newsletter strategy beyond Substack embeds. [Impact: Medium-High · Effort: Medium]**
The growth engine is the Substack, but the site treats it as an external link. Add a native inline subscribe (single field, branded) on high-traffic pages (framework, principles, case studies), feeding the same list. Owning the capture point — rather than bouncing to Substack — measurably lifts subscribe rates and keeps the brand experience intact.

**20. Harden the contact/form layer and trust microcopy. [Impact: Medium · Effort: Low]**
All forms post to a single Formspree endpoint with `source` tags (good), but: no spam protection (honeypot/reCAPTCHA), no success page for no-JS users, and no privacy reassurance near the email gate ("We send your results and the occasional essay. No spam. Unsubscribe anytime."). Premium buyers hesitate at email capture without a privacy signal. Add it everywhere you ask for an email.

---

## 4. Prioritization Matrix (impact × effort)

| Priority | Recommendation | Impact | Effort |
|---|---|---|---|
| 1 | Mobile navigation | Very High | Low |
| 2 | OG/Twitter social cards | Very High | Low |
| 3 | Analytics + funnel events | Very High | Low |
| 4 | Fix orphan pages / surface Speaking | High | Low |
| 5 | Testimonials & social proof | Very High | Medium |
| 6 | Meta descriptions / sitemap / robots | High | Low |
| 7 | JSON-LD structured data | Med-High | Low |
| 8 | Scheduling link (Calendly) | High | Low |
| 9 | Hero clarity + proof | High | Medium |
| 10 | Shared stylesheet | Medium | Medium |
| 11 | Nav/footer consistency + bug fixes | Medium | Low |
| 12 | Verifiable, sourced metrics | High | Medium |
| 13 | Media kit / "Featured in" | Med-High | Medium |
| 14 | IntersectionObserver reveals | Medium | Low-Med |
| 15 | Shareable + PDF audit results | High | Medium |
| 16 | Accessibility & contrast pass | Medium | Low-Med |
| 17 | OG image + branded 404 | Low-Med | Low |
| 18 | Top-of-funnel audience fork | Medium | Medium |
| 19 | Native newsletter capture | Med-High | Medium |
| 20 | Form hardening + trust microcopy | Medium | Low |

---

## 5. Suggested Sequencing

- **Sprint 1 (a day or two, mostly low-effort, highest impact):** #1, #2, #3, #4, #6, #11. Stops the bleeding on mobile, sharing, measurement, and IA hygiene.
- **Sprint 2 (credibility):** #5, #12, #9, #8, #13. Turns a beautiful brochure into a proof-backed advisory platform.
- **Sprint 3 (foundation + growth loops):** #10, #15, #19, #7, #18. Consolidate the system, then build the compounding growth mechanics.
- **Sprint 4 (polish):** #14, #16, #17, #20.

---

## 6. The One-Sentence Verdict

You have the taste, the IP, and the voice of a premium boutique firm — what's missing is the **mobile experience, the proof, and the measurement** that let serious buyers trust it and let the ideas travel. Fix Tier 1 and this stops reading as a personal site and starts reading as a platform.
