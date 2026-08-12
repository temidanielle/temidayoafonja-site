# Legal Review Required

Briefs for counsel covering the Privacy Policy and Terms of Use on temidayoafonja.com.
Prepared August 11, 2026.

**No new legal text has been published.** This document describes what the current pages say,
what the site actually does, and where the two do not line up. Counsel writes the replacement
language; this repository does not.

Both live pages carry a self-declared limitation:

- `privacy.html` — "This policy will be updated as the firm's data practices develop. It has
  not been reviewed by legal counsel."
- `terms.html` — "These terms will be updated as the firm's services develop. They have not
  been reviewed by legal counsel."

Those two sentences are currently the site's only protection on this point. They should stay
in place until counsel supplies replacement text.

---

## Part 1. Privacy Policy

### What the page says today

Five paragraphs, in full:

1. "The Density Group LLC collects information through inquiry forms and diagnostic
   instruments on this website."
2. "Information submitted through inquiry forms is used only to respond to your inquiry and to
   determine whether a conversation would be useful."
3. "Diagnostic responses are processed in your browser. Your individual responses are not
   stored on our servers unless you choose to submit them."
4. "This site uses Plausible Analytics, which does not use cookies and does not collect
   personal data."
5. "For questions about your data, contact temidayo@thedensitygroup.com."

### 1.1 Categories of information collected

Needs to be enumerated. What the site actually collects, gathered from the code:

| Category | Where collected | Notes |
|---|---|---|
| Name (first, last, or combined) | All nine forms | |
| Work or personal email address | All nine forms | |
| Organization name | Seven forms | Optional on `work.html` |
| Job role or level | Executive Briefing, Diagnostic gate | |
| Free-text description of a decision or situation | Executive Briefing, `work.html`, `speaking.html`, `for-professionals.html` | Unbounded free text. May contain third-party personal data |
| Diagnostic item-level responses | `diagnostic.html`, `organizational-diagnostic.html`, `ai-capability-readiness.html` | Every answer is stored, not only the totals |
| Computed scores and quadrant placement | Same three instruments | Density, Optionality, Alumni Capital, quadrant, boundary flags |
| Self-reported demographics | `diagnostic.html` | Industry, role level, years of experience, organization size |
| Organizational profile | `organizational-diagnostic.html`, `ai-capability-readiness.html` | Sector, headcount, mission exposure, recent change, AI change pressure |
| Consent flags | `diagnostic.html` only | Research consent and marketing consent, stored as booleans |
| Timestamps | Server-side captures | Recorded in both UTC and America/Chicago |
| Submission identifier | `diagnostic.html` | Client-generated UUID used for server-side deduplication |
| IP address and user agent | Implicitly, by every service provider | Not collected by first-party code, but received by Formspree, Netlify, and Anthropic in the ordinary course |

The current wording, "information through inquiry forms and diagnostic instruments," is true
but far less specific than the enumeration above.

### 1.2 Purposes of processing

Paragraph 2 states a single purpose: responding to an inquiry. The site has at least four.

1. **Responding to an inquiry.** Accurately described today.
2. **Delivering a diagnostic result.** Not currently described.
3. **Automated marketing sequences.** `diagnostic.html` enrolls completers into a Kit
   (ConvertKit) email sequence selected by their quadrant, via
   `/.netlify/functions/subscribe`. **This purpose is not disclosed anywhere on the privacy
   page.** See the finding at 1.10 below.
4. **Research aggregate.** `diagnostic.html` captures a research record, with a separate
   consent flag, into a durable store. Not currently described.

### 1.3 Diagnostic data handling

Paragraph 3 says: "Diagnostic responses are processed in your browser. Your individual
responses are not stored on our servers unless you choose to submit them."

The first sentence is accurate for scoring. All three instruments compute the quadrant
deterministically client-side.

The second sentence needs counsel's attention, because "unless you choose to submit them"
covers more paths than a reader is likely to assume:

- On `diagnostic.html`, item-level responses are posted to
  `/.netlify/functions/audit-research` and stored one blob per submission in Netlify Blobs.
  Records where research consent is **false are still stored**, flagged so they can be
  excluded from any aggregate. That is a defensible design for auditability, but the page does
  not say it and the policy does not say it.
- If the network call fails, the payload is written to the browser's `localStorage` and retried
  on a later visit. Stashed payloads self-expire after seven days
  (`RESEARCH_PENDING_MAX_AGE_MS`). This is local storage of personal data on the visitor's own
  device and is not mentioned anywhere.
- On `organizational-diagnostic.html` and `ai-capability-readiness.html`, the answers are sent
  to an Anthropic API endpoint through a Netlify function to generate the narrative prose. See
  1.5.

### 1.4 Research consent

Only `diagnostic.html` collects research consent, and it does so well: a dedicated checkbox,
unchecked by default, separate from the marketing checkbox, recorded as an explicit boolean in
the stored payload, and not a condition of receiving the result.

Points for counsel:

- Non-consented records are retained and flagged rather than discarded. Confirm this is the
  intended and permissible construction.
- No consent timestamp and no policy-version identifier is recorded alongside the flag. If
  consent is ever challenged, the record shows only the boolean.
- The two organizational instruments capture item-level responses with **no research consent
  step at all**, though their data is organizational rather than personal in character.
- The exact on-page consent wording should be reviewed against whatever standard counsel
  applies. It is not reproduced here because counsel will want to read it in place.

### 1.5 Service providers and international transfers

Not disclosed today beyond Plausible. The full list:

| Provider | Purpose | Data reaching them |
|---|---|---|
| **Formspree** | Email notification for all nine forms | Every field on every form |
| **Netlify** | Hosting, serverless functions, Blobs storage | All traffic. Durable storage of diagnostic and lead records |
| **Anthropic** | Narrative generation for the two organizational instruments | Item-level answers plus organizational context, via `diagnose.js` and `ai-readiness-narrative.js` |
| **Kit (ConvertKit)** | Automated email sequences | Email, name, organization, quadrant, scores, result line, tags |
| **Plausible Analytics** | Site analytics | Aggregate only. Correctly described on the page as cookieless |
| **Google Fonts** | Webfont delivery on all 16 pages | Visitor IP address, at request time, to Google servers |
| **Gumroad** | Field Kit purchase, via the `/fieldkit` redirect | Handled entirely on Gumroad |
| **Maven** | Lightning Lesson and paid workshop registration | Handled entirely on Maven |
| **Amazon** | Book purchase | Handled entirely on Amazon |

Two of these deserve specific attention:

- **Anthropic.** Diagnostic answers are transmitted to a third-party AI provider. This is not
  disclosed on the page, and it is the kind of processing a careful reader would expect to see
  named.
- **Google Fonts.** Loaded from `fonts.googleapis.com` on every page, which discloses visitor
  IP addresses to Google on each page load. This has been the subject of adverse rulings in the
  EU. If EU visitors are in scope, counsel may prefer self-hosted fonts. That is a technical
  change, not a policy change, and is not made here.

### 1.6 Retention

No retention period is stated anywhere, and none is enforced in code, with one exception:

- Netlify Blobs records (`audit-research`, `org-diagnostic-leads`, `ai-readiness-leads`) are
  retained indefinitely. There is no expiry or purge routine.
- Formspree submissions are retained per Formspree's own policy and plan settings, which are
  not documented in this repository.
- Kit subscribers are retained until unsubscribed.
- The only enforced expiry is the seven-day `localStorage` TTL on unsent diagnostic payloads,
  which is a delivery mechanism rather than a retention policy.

Counsel should set retention periods per category. Engineering can then implement them.

### 1.7 Marketing preferences

The site has no unsubscribe language, no preference centre, and no description of how to opt
out. Kit supplies an unsubscribe link in its own emails, which is the actual mechanism, but the
policy does not say so.

### 1.8 Rights and requests

Not addressed. The page offers a contact address for questions but names no rights: no access,
correction, deletion, portability, or objection, and no response timeframe. Whether these
rights must be offered depends on the jurisdictions counsel determines are in scope.

Practical note for the deletion right: a single individual's data can currently sit in
Formspree, Netlify Blobs, Kit, and the visitor's own `localStorage`. A deletion request
requires action in at least three systems. Blob keys are addressable and the export endpoints
support a `&delete=THE_KEY` parameter, so deletion is technically feasible.

### 1.9 Security approach

Not addressed. What is true today:

- All traffic is served over HTTPS.
- `X-Content-Type-Options: nosniff` is set for all routes; `diagnostic.html` additionally
  carries a Content-Security-Policy restricting `script-src`.
- API keys (Anthropic, Kit) are held in Netlify environment variables and never appear in page
  source.
- The research and lead export endpoints are gated by a shared secret in the
  `RESEARCH_EXPORT_TOKEN` environment variable, passed as a **URL query parameter**. Query
  strings are commonly written to server and proxy logs and to browser history. Counsel and
  engineering should jointly decide whether a bearer header is required instead.
- `dashboard.html` is publicly reachable at `/dashboard.html` with no authentication. It reads
  only the local browser's `localStorage`, so it exposes no server-side data, but it is an
  internal-looking page on a public URL. Flagged for a decision on whether it should ship at
  all.

### 1.10 Resolved: marketing consent now gates the marketing sequence

**Previously:** `subscribeToKit()` was called after every completion where a valid email was
supplied, regardless of the `marketingConsent` checkbox. A visitor who deliberately left the box
unchecked was still enrolled in an automated email sequence, and the stored record showed that
they declined. This was the highest-exposure privacy finding on the site.

**Now:** gated by operator ruling, August 2026. `subscribeToKit()` takes an explicit consent
argument and fails closed, so anything other than an affirmative opt-in returns without
enrolling. Each of the three completion paths passes the checkbox belonging to the screen it
submits. Verified in a browser across all three paths and both checkbox states: unchecked never
enrols, checked enrols exactly once.

The research payload continues to record the checkbox state either way, so a declined opt-in
remains visible in the record.

A fourth marketing checkbox on the pre-start screen (`marketingConsentPregate`) was never read
by any code. It was removed at the same time rather than wired up, so the site no longer
presents a control that implies a consent it does not act on.

**Still for counsel.** Enrolment is now consent-gated, but no consent timestamp or policy
version is recorded alongside the flag, and the six other forms still collect an email address
with no explicit opt-in.

### 1.11 Contact details

The page gives `temidayo@thedensitygroup.com`. It does not give the registered legal entity's
address or a named contact for data requests. Counsel should confirm what identification is
required for the jurisdictions in scope.

---

## Part 2. Terms of Use

### What the page says today

Four paragraphs, in full:

1. "This website is operated by The Density Group LLC."
2. "The content on this site, including the Capability Formation framework, diagnostic
   instruments, and related materials, is the intellectual property of The Density Group LLC."
3. "The free diagnostic instruments on this site provide a self-assessed, directional reading.
   They do not constitute professional advice, organizational assessment, or validated
   psychometric evaluation."
4. "Results should be interpreted alongside professional judgment and organizational context."

Paragraphs 3 and 4 are a well-drafted limitation and should survive counsel's redraft. The
gaps below are all things the page does not say.

### 2.1 Payment and refunds

Not addressed. Paid offerings currently named on the site:

| Offering | Price | Where transacted |
|---|---|---|
| Career Growth Workshop | $500 | Maven |
| Capability Formation Field Kit | $75 | Gumroad |
| Books | Amazon list price | Amazon |
| Capability Position Read | Not published | Direct |
| Executive Briefing | Not published | Direct |

Every transaction currently happens on an external platform, which limits exposure. See 2.7.

### 2.2 Cancellations and rescheduling

Not addressed. Material for the workshop, which is a dated live session, capped at 12
participants, currently scheduled for September 16, 2026. Counsel should state who may cancel,
by when, what happens if the session is rescheduled or does not run, and whether a seat is
transferable.

### 2.3 Participant conduct and recording

Not addressed. Needed for the workshop and the Lightning Lesson: whether sessions are recorded,
whether participants may record, what happens to a recording afterwards, and what conduct
grounds removal without refund. Whether other participants appear in a recording is a privacy
question as well as a terms question.

### 2.4 Digital-product licence

Not addressed. The Field Kit is a downloadable digital product. Terms should state that the
purchase grants a personal, non-transferable licence, name whether internal organizational use
by a purchaser's employer is permitted, and set out what a purchaser may not do.

### 2.5 Prohibited redistribution

Not addressed. Should cover: reselling or redistributing the Field Kit; reproducing the
diagnostic instruments; administering the instruments to third parties, including inside the
reader's own organization; and republishing framework materials. The site actively invites
leaders to run the Scan on their organization, so the boundary between permitted internal use
and prohibited redistribution needs to be drawn deliberately.

### 2.6 Intellectual property

Paragraph 2 asserts ownership of the framework, instruments, and materials. Not addressed:
trademark status of "Capability Formation," "The Density Group," "Density," "Optionality," and
"Alumni Capital"; what limited use is permitted with attribution; and how infringement is
reported.

### 2.7 External platform transactions

Not addressed, and this is the largest structural gap. Every paid transaction on the site today
completes on Maven, Gumroad, or Amazon. Terms should state that those transactions are governed
by the platform's own terms, that refunds and payment disputes are handled there, and that The
Density Group does not receive or store payment card data. That last point is accurate and
worth stating explicitly, because it is favourable.

### 2.8 Limitation of liability

Not addressed at all. Paragraphs 3 and 4 disclaim the diagnostic instruments specifically, but
there is no general limitation, no cap, and no exclusion of consequential damages. Given that
the site invites organizations to act on a capability read, this is the most significant
omission on the page.

### 2.9 Governing law

Not addressed. No governing law, no venue, no dispute-resolution mechanism, and no position on
arbitration or class-action waiver.

### 2.10 Enterprise engagements governed by separate agreements

Not addressed, and it should be, now that `executive-briefing.html` is live and takes inbound
enterprise inquiries. The terms should say that paid advisory engagements are governed by a
separate written agreement between the parties, that nothing on the site constitutes an offer
or forms a contract, and that the separate agreement controls in the event of conflict.

Related: the Executive Briefing form is the only form that warns against submitting
confidential material ("Please do not include confidential employee information, personal data,
or sensitive internal documents in this initial form"). Counsel should consider whether an
equivalent warning belongs on `work.html`, which also invites a description of an
organizational decision, and whether the terms should state that unsolicited submissions create
no confidentiality obligation.

---

## Priority for counsel

Ordered by exposure, highest first.

1. **Limitation of liability** (2.8). Currently absent. Now the highest-exposure item, since
   the consent gating in 1.10 has been resolved.
2. **Undisclosed service providers**, in particular Anthropic (1.5).
3. **Retention periods** (1.6). None stated, none enforced.
4. **Rights and requests** (1.8). None named.
5. **Enterprise engagement disclaimer** (2.10). Newly material as of this build.
6. **Export token in a query string** (1.9). A technical fix, pending counsel's view on the
   sensitivity of the data behind it.
7. **Google Fonts and EU visitor IPs** (1.5). Depends on whether EU visitors are in scope.
8. **Workshop cancellation, recording, and conduct terms** (2.2, 2.3).
9. **Digital-product licence and redistribution** (2.4, 2.5).

---

## What was deliberately not done

- No new privacy or terms language was written or published.
- The two "not been reviewed by legal counsel" notices were left in place.
- The Kit consent-gating behaviour was changed by operator ruling. See 1.10.
- Google Fonts were left externally hosted.
- `dashboard.html` was left published.

Each of these is an operator or counsel decision, not a build decision.
