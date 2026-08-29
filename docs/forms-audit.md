# Forms Audit

Every public form on temidayoafonja.com: what it collects, where it sends, and what consent
it carries. Prepared August 11, 2026.

All forms post JSON to Formspree by `fetch`. None use a native HTML form POST, so no form
data is submitted on a page navigation.

---

## Summary

| # | Page | Form | Endpoint | Marketing consent | Research consent | Privacy link |
|---|---|---|---|---|---|---|
| 1 | `executive-briefing.html` | Executive Briefing inquiry | `xqpzegoj` | Not collected | Not collected | Yes |
| 2 | `work.html` | Organizational inquiry | `xqpzegoj` | Not collected | Not collected | Yes |
| 3 | `for-professionals.html` | Workshop priority list | `xyegkbaq` | Not collected | Not collected | Yes |
| 4 | `speaking.html` | Speaking inquiry | `xgawaegz` | Not collected | Not collected | Yes |
| 5 | `book.html` | Book and Field Kit list | `xjgapael` | Not collected | Not collected | Yes |
| 6 | `diagnostic.html` | Diagnostic completion capture | `xjgapael` | **Separate checkbox** | **Separate checkbox** | Yes |
| 7 | `diagnostic.html` | Paper fast-path capture | `xjgapael` | **Separate checkbox** | **Separate checkbox** | Yes |
| 8 | `organizational-diagnostic.html` | Scan results capture | `mjgndvkp` | Not collected | Not collected | Yes |
| 9 | `ai-capability-readiness.html` | AI readiness capture | `xjgapael` | Not collected | Not collected | Yes |
| 10 | `career-decisions.html` | Career Decision Evidence Check | **No Formspree.** `/.netlify/functions/career-decisions-subscribe` | **Two separate boxes, both unchecked. Delivery required, guidance optional** | Not collected | Yes, in the consent block |

Four endpoints are now separated. `xjgapael` still carries four submission types
(book, two diagnostic captures, AI readiness), so any autoresponder attached to it fires for
all four.

Form 10 is the first form on the site that does not post to Formspree at all. It is also the
first to record a consent timestamp and a policy version.

---

## 1. Executive Briefing inquiry (new, August 11)

- **Page and location** — `executive-briefing.html`, section 9, anchor `#inquiry`
- **Fields** — Name, Role, Organization, Work email, Decision category (select), Expected
  decision timing (select), Short description of the decision (textarea)
- **Required** — Name and a work email containing `@`. Client-side validated before send
- **Endpoint** — `https://formspree.io/f/xqpzegoj`
- **Payload** — `name`, `role`, `organization`, `email`, `decision_category`,
  `decision_timing`, `decision_description`, `source: "executive-briefing-inquiry"`
- **Storage** — Formspree only. No Netlify Blobs capture, no Kit enrollment
- **Consent** — None collected. This is an inbound business inquiry, not a marketing signup
- **Sensitive-data warning** — **Yes, explicit.** "Please do not include confidential employee
  information, personal data, or sensitive internal documents in this initial form."
- **Privacy link** — Yes, in the fine print beneath the submit button

---

## 2. Organizational inquiry

- **Page and location** — `work.html`, `#get-in-touch`
- **Fields** — I am reaching out as (select), First name, Last name, Email, Organization
  (optional), What changed and what decision is in front of you (textarea)
- **Required** — First name, last name, email
- **Endpoint** — `https://formspree.io/f/xqpzegoj`
- **Payload** — `name`, `first_name`, `last_name`, `email`, `organization`, `reaching_out_as`,
  `message`, `source: "work-page"`
- **Storage** — Formspree only
- **Consent** — None collected
- **Privacy link** — Yes

**Note.** This form shares `xqpzegoj` with the Executive Briefing inquiry. The two are
distinguishable by the `source` field. The nav CTA now routes to the Executive Briefing form,
so this one receives less traffic than before.

---

## 3. Workshop priority list

- **Page and location** — `for-professionals.html`, `#priority-list`
- **Fields** — First name, Last name, Email, What are you deciding (textarea)
- **Required** — First name, last name, email
- **Endpoint** — `https://formspree.io/f/xyegkbaq`
- **Payload** — `name`, `first_name`, `last_name`, `email`, `deciding`,
  `tag: "paid_workshop_interest"`, `source: "for-professionals-priority-list"`
- **Storage** — Formspree only
- **Consent** — None collected. **Flagged:** joining a priority list is closer to a marketing
  signup than an inbound inquiry, and the payload carries a marketing tag. Counsel should
  advise whether an explicit opt-in is required
- **Privacy link** — **Correction, August 17 2026. No.** This row previously read "Yes". Read
  against the markup, the consent paragraph at `for-professionals.html:242` carries no link of
  any kind, and the only privacy link on the page is the one in the shared footer. The error
  is recorded rather than silently edited because the original claim was carried into the
  privacy work. Nothing on `for-professionals.html` was changed to fix this: the page is out of
  scope for the change that found it, and the finding is left open for the operator

---

## 4. Speaking inquiry

- **Page and location** — `speaking.html`, inquiry section
- **Fields** — Name, Organization, Email, Message
- **Required** — Email containing `@`
- **Endpoint** — `https://formspree.io/f/xgawaegz`
- **Payload** — `name`, `org`, `email`, `message`, `source: "speaking-inquiry"`
- **Storage** — Formspree only
- **Consent** — None collected
- **Privacy link** — Yes

---

## 5. Book and Field Kit list

- **Page and location** — `book.html`
- **Endpoint** — `https://formspree.io/f/xjgapael`
- **Storage** — Formspree only
- **Consent** — None collected. **Flagged:** this is a notification list, so an explicit
  marketing opt-in is the safer construction
- **Privacy link** — Yes

---

## 6 and 7. Individual Diagnostic captures

- **Page** — `diagnostic.html`. Two capture points: completion, and the paper fast path
- **Fields** — Name, role, organization, email, plus the scored payload (mode, quadrant, state,
  density, optionality, alumni capital, result, completed timestamp)
- **Endpoint** — `https://formspree.io/f/xjgapael`
- **Storage and downstream systems** — four, not one:
  1. Formspree, for the owner notification
  2. `/.netlify/functions/audit-research`, one Netlify Blob per submission, storing every
     item-level answer. Records with research consent false are **still stored**, flagged
  3. `/.netlify/functions/subscribe`, which enrols the address in the Kit (ConvertKit) sequence
     matching the quadrant
  4. `localStorage`, for pending payloads when the network call fails. Expire after 7 days
- **Consent** — **Both separated, and both unchecked by default.** `researchConsent` and
  `marketingConsent`, with a third pair on the paper fast path. `marketing_consent` is sent as
  an explicit boolean in the payload
- **Privacy link** — Yes

**Consent construction: best on the site, and it now gates.** The two-checkbox design is the
model the other forms should follow. As of August 2026 `subscribeToKit()` requires an explicit
opt-in and fails closed, so an unchecked box means no Kit enrolment on any of the three
completion paths. The research payload still records the checkbox state either way, so a
declined opt-in remains visible in the record.

A third marketing checkbox previously sat on the pre-start screen (`marketingConsentPregate`).
It was never read by any code, so it collected clicks and did nothing. It was removed rather
than wired up, because the operative consent is the one on the screen the visitor submits.

---

## 8. Organizational Scan results capture

- **Page** — `organizational-diagnostic.html`
- **Endpoint** — `https://formspree.io/f/mjgndvkp`
- **Storage** — Formspree, plus `/.netlify/functions/org-diagnostic-capture` (Netlify Blobs)
- **Third party** — item-level answers and organizational context are also sent to
  `/.netlify/functions/diagnose`, which calls the Anthropic API to generate the narrative
- **Consent** — None collected. No research consent step, unlike `diagnostic.html`
- **Privacy link** — Yes

---

## 9. AI readiness capture

- **Page** — `ai-capability-readiness.html`
- **Endpoint** — `https://formspree.io/f/xjgapael`
- **Storage** — Formspree, plus `/.netlify/functions/ai-readiness-capture` (Netlify Blobs)
- **Third party** — item-level answers and organizational context are also sent to
  `/.netlify/functions/ai-readiness-narrative`, which calls the Anthropic API
- **Consent** — None collected
- **Privacy link** — Yes

---

## 10. Career Decision Evidence Check

- **Page and location** — `career-decisions.html`, section `#evidence-check`. Reached at the
  permanent URL `/career-decisions`
- **Public name** — the Career Decision Evidence Check. `/career-decisions` is the URL only, and
  is never presented as a product, a course or a paid offer
- **Fields** — First name, Email, "What are you currently deciding?" (optional), **two** consent
  checkboxes, both unchecked by default, plus a hidden honeypot (`decision_reference`)
- **Required** — First name, a valid email, and the **delivery** consent box. The guidance box is
  never required and is never validated: leaving it unticked is a complete, valid submission.
  Validated inline in the page and again on the server
- **Endpoint** — `/.netlify/functions/career-decisions-subscribe`. **There is no Formspree write
  and no second destination of any kind**
- **Payload** — `first_name`, `email`, `current_decision`, `decision_reference` (honeypot), the
  two consent records (`delivery_consent`, `delivery_consent_timestamp`, `delivery_policy_version`,
  `guidance_consent`, `guidance_consent_timestamp`, `guidance_policy_version`), and an
  `attribution` object of two touches, `first` and `current`, each carrying `utm_source`,
  `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `source`, `video_slug`, `landing_page`,
  `referrer` and `seen_at`
- **Storage and downstream systems** — two, in a fixed order:
  1. **Kit (ConvertKit)**, the authoritative system. Enrols the subscriber in the sequence named
     by `KIT_SEQ_CAREER_DECISIONS`, which is what delivers the requested resource. Tags with
     `KIT_TAG_CAREER_DECISIONS` always, `KIT_TAG_CAREER_DECISIONS_GUIDANCE` **only** on explicit
     guidance consent, and `KIT_TAG_YOUTUBE` only when the visitor genuinely arrived with a
     youtube source. Kit owns deduplication (it upserts on the email address), delivery, and the
     unsubscribe link
  2. **Netlify Blobs**, store `career-decisions-leads`, readable through the token-gated
     `/.netlify/functions/career-decisions-export` (see the note below), written **only after
     Kit confirms**, so
     the store can never hold a lead that is not also a subscriber. Best effort: a storage
     failure is logged and reported in the response as `durable_record: false`, and does not
     turn a real subscription into an error the visitor sees. **At launch this is expected to
     read `false` on every submission.** See the launch limitation below
- **Consent** — **Two purposes, two choices, recorded separately.** This is the construction the
  rest of the site should move to.
  - *Delivery* ("Send me the Career Decision Evidence Check by email.") is required and gates
    everything. Anything other than a literal `true` returns 400: no Kit call, no record, no
    delivery. It authorises the requested resource and the messages needed to deliver it, and
    nothing else.
  - *Guidance* ("Also send me occasional Capability Formation guidance ... I can unsubscribe at
    any time.") is optional, starts unchecked, and is the only thing that enrols anyone in ongoing
    marketing. It is never inferred: a missing field, a string, a `1` or any other truthy value is
    treated as absent, so a sloppy client cannot enrol someone by accident.
  - Each consent carries **its own timestamp and its own policy version**, in Kit and in the
    durable record. The version recorded is `2026-08-18`, which is the "Last updated" date on
    `privacy.html`. **The two must always move together in the same commit.** A consent record
    stamped with a policy version older than the wording the person actually read is not evidence
    of anything, which is why the version was raised from `2026-08-12` when the policy was revised
    to distinguish delivery of a requested resource from ongoing guidance. Guidance stamps are written only when guidance was actually given, so an empty
    stamp is unambiguous evidence that consent was withheld rather than that it was lost. The
    server stamps its own receipt time independently of the client's clock.
- **Broadcast audience** — `KIT_TAG_CAREER_DECISIONS_GUIDANCE`, never `KIT_TAG_CAREER_DECISIONS`.
  The first tag means "consented to ongoing guidance". The second only means "asked for the
  evidence check" and must never be used as the audience for a broadcast. If a guidance nurture
  sequence is wanted, build it in Kit as an automation triggered by the guidance tag being added.
- **Attribution** — Two touches. `first` is the campaign visit that introduced the person to the
  page and is never overwritten. `current` is the most recent explicit campaign visit in the same
  session. A bare return to `/career-decisions` with no parameters is not a new campaign visit and
  changes nothing. The youtube tag is applied when either touch carries an exact `source` or
  `utm_source` of `youtube`; a campaign name that merely contains the word, or a youtube referrer,
  tags nobody
- **Offer retirement** — the single next step shown after submission retires itself at
  `2026-09-02T18:45:00-05:00`, the end of the session in Central time, and does so **while the
  page is open**. A visitor who loads the page before the cutoff and leaves the tab sitting there
  sees the Field Kit fallback take over at the cutoff without reloading. One timer is armed for
  exactly the remaining milliseconds; there is no polling, and the fallback arms nothing at all
  because it has no expiry
- **Rate limiting** — 10 requests per rolling hour per caller, keyed by a **salted SHA-256 of the
  IP address**, never the address. Same construction as `diagnose.js`. Fails open on a storage
  error and logs loudly when it does
- **Privacy link** — Yes, inside the consent block itself, not only in the footer
- **Double opt in** — **Unverified, and it cannot be verified from this repository.** Whether Kit
  sends a confirmation email is an account level setting on the sequence. It must be checked in
  the Kit account and recorded here

**What this form fixes, relative to findings 1 and 5 below.** It is the first form on the site to
collect an explicit opt-in *and* to record when it was given and against which version of the
policy. It is the model the remaining seven consent-free forms should follow.

**Reading the store back.** `/.netlify/functions/career-decisions-export` returns the store as
CSV, or as JSON with `&format=json`. It is gated on the same `RESEARCH_EXPORT_TOKEN` as the three
older exports, and it is **read only**: it answers `GET` alone, and it refuses the `&delete=` the
other three accept, with a 400 rather than by ignoring it. It also accepts the token as
`Authorization: Bearer`, compares it in constant time, and sets `Cache-Control: no-store`.

A fifth difference was added on 2026-08-20, after the first live run of the endpoint returned a
bare `export_failed` on a Deploy Preview with a correct token and there was no way to tell from
the response which of four unrelated conditions had occurred. The three older exports answer every
storage fault with that same bare string. This endpoint now names the fault class instead:

| Response | Meaning |
| --- | --- |
| `200`, `store_exists: false`, `count: 0` | The store has never been written to, so it does not exist yet. An empty export, not an error. This is the expected reading after a submission whose `durable_record` came back `false`. |
| `500`, `reason: blobs_not_configured` | `BLOBS_SITE_ID` and `BLOBS_TOKEN` are not both present in this deploy context. A configuration fault, not a code fault. |
| `500`, `reason: blobs_env_missing` | The two variables are present but Blobs still refused to initialise. |
| `500`, `reason: blobs_api_<status>` | The Blobs API answered with that status. `401` or `403` means the token is wrong or lacks access to the site. |
| `500`, `reason: blobs_error` | Anything else, including a refusal Netlify explained in words rather than by status. Read `detail`. |

A `500` also carries `detail`, which is the text Netlify's API put in its `x-nf-error` response header, or the bare status when it sent no header, plus the request ID when one is present. That request ID is what Netlify support needs to trace a refusal. Only a `BlobsInternalError` has its message returned, because its shape is built by the client itself and is bounded; an arbitrary error's message is never echoed. The text is truncated to 200 characters, and the values of `BLOBS_TOKEN` and `RESEARCH_EXPORT_TOKEN` are redacted from it, which is belt and braces rather than a known risk.

A refusal at the gate is classified the same way, added the same day for the same reason. `401`
with `reason: no_token_supplied` means no token reached the request at all, `401` with
`reason: token_mismatch` means one did and it did not match, and `503` with
`reason: server_token_not_configured` means `RESEARCH_EXPORT_TOKEN` is not set in that deploy
context, which is a configuration gap an operator cannot otherwise see. A refusal also reports
`token_source`, either `query` or `bearer`, because the bearer header takes precedence and a header
attached by a client, proxy or browser extension will otherwise silently override a token typed
into the address bar. **No refusal returns any part of the token or its length**, and a test asserts
that, so nothing here helps anyone guess it.

Both token forms are trimmed of surrounding whitespace, since a value copied out of a settings
screen commonly arrives with a trailing space or newline. Whitespace *inside* the value is still a
mismatch and is not repaired, which matters because a `+` in a query string decodes to a space; a
token containing one must be sent as `Authorization: Bearer` rather than in the query.

The failure body carries the fault code, the store name and a boolean saying whether the two Blobs
variables are present. It never carries the token, an email address or any record content, and it
is only reachable by a caller who has already presented the token.

These five differences are confined to that file; the three older exports are unchanged.

### Accepted limitation at launch: no durable first-party record

Netlify Blobs has been failing site-wide since 2026-08-20. Every read and write returns HTTP 400
from the Blobs API, on production and on deploy previews, on stores that demonstrably exist. The
credential is accepted, the project ID is a well formed UUID, and no Blobs context is injected into
this site's functions, so the manual API route is the only one available and it is the one being
refused. A Netlify support ticket is open. **It is not a release gate**, by the site owner's
decision on 2026-08-27.

What this means for the Career Decision Evidence Check at launch:

- The Kit subscription, the delivery email, the two consent records in Kit's custom fields and the
  attribution fields **all work**. Nothing a person asked for is affected, and consent is still
  recorded, in Kit.
- The **durable first-party copy is not written**. `durable_record` will read `false` on every
  submission and `career-decisions-leads` will not exist. This is the pre-existing site-wide fault,
  not a defect in this form.
- Two production capture endpoints have been in exactly this state for longer: `audit-research` and
  `ai-readiness-leads` have never been created, so the Diagnostic and AI Capability Readiness forms
  have never durably recorded a submission either. That is the same incident.
- Nothing is lost silently. The failure is reported in the response, logged, and the export endpoint
  names the fault class, so the gap is visible rather than assumed.
- **Repair requires a code change, not only a fix on Netlify's side.** This was previously recorded
  as resuming with no code change, which was wrong. Netlify support case #1099659 states the Blobs
  context is injected when the function runs, and that the remedy is zero-configuration
  `getStore("name")` rather than the manual `{ name, siteID, token }` form. `netlify/lib/blobs.js`
  prefers manual configuration whenever `BLOBS_SITE_ID` and `BLOBS_TOKEN` are both set, which they
  are, so zero-configuration is never reached. Changing that preference touches a file shared by all
  nine Blobs functions and is tracked as a separate incident, not as part of this work.
- Submissions taken before that repair are not recoverable into the store. There is no backfill, and
  Kit remains the record for them.

### On Netlify's proposed cause, and why it was not acted on

Netlify support case #1099659 proposed that esbuild replaces the runtime environment reference with
`undefined` during bundling, and described this as likely rather than established. **It was checked
before any shared code was touched, and the mechanism does not hold.** Three findings, 2026-08-29:

1. **The client never uses a statically replaceable reference.** `getEnvironmentContext` in
   `@netlify/blobs` 8.2.0 reads `globalThis.netlifyBlobsContext` or calls `getEnvironment().get(...)`,
   and `getEnvironment` destructures `process` off `globalThis` and reads `process?.env[key]`, a
   dynamic computed access. No esbuild `define` can match that shape.
2. **Netlify's own bundler passes no `define`.** The `build()` call in `@netlify/zip-it-and-ship-it`,
   in `runtimes/node/bundlers/esbuild/bundler.js`, sets `bundle`, `entryPoints`, `external`,
   `format`, `platform`, `plugins`, `target` and related options. There is no `define` key, so no
   compile-time environment substitution occurs.
3. **The compiled bundle preserves everything.** Bundling this repository's
   `career-decisions-subscribe.js` with esbuild leaves `NETLIFY_BLOBS_CONTEXT` intact as a string
   literal passed to a runtime lookup, leaves `globalThis.netlifyBlobsContext` intact, and leaves all
   nine `process.env.*` reads unreplaced.

A fourth point comes from live behaviour rather than inspection: if `process.env` reads were being
replaced, `BLOBS_SITE_ID` and `BLOBS_TOKEN` would be `undefined` too. The export endpoint reported
`blobs_manual_config: true` in production, so those reads demonstrably work at runtime.

**What is established** is narrower, and is in this repository's own code: `blobStore()` selects the
manual form whenever both variables are set, so zero-configuration is never attempted. That is a real
and sufficient explanation for which mode is used. It is **not** established that zero-configuration
would succeed: a probe on 2026-08-26 found no Blobs context present at runtime, which would make that
call throw instead. That question is open and must be answered by observation before the shared
helper is changed.

### Rate limiting does not depend on Blobs

Added 2026-08-27, for the same incident. The submission function's own limiter, ten per hour per
salted IP hash, is built on Blobs and is deliberately fail-open, so while Blobs is broken **the form
has no working limit from that limiter at all**. That is not an acceptable state to launch in.

`netlify.toml` therefore carries a Netlify-native limit on the submission rule, depending on nothing
this site configures: **five submissions per 180 seconds, aggregated by domain and IP.** No `action`
is declared, so the default applies and an exceeded limit is refused with 429 rather than rewritten
to a page, which is right for a path only ever reached by the form's fetch. **As of launch this rule
is accepted by Netlify but has not been observed to fire.** See the status below before relying on
it. Netlify caps the window at 180 seconds, so the hour-long ceiling the Blobs limiter expresses
cannot be reproduced here. The two are complementary and both are kept: this one stops bursts now,
and the Blobs limiter enforces the sustained hourly ceiling again once storage is repaired, which
needs the shared-helper change described above and not only a fix on Netlify's side.

Because Netlify reserves the `/.netlify/` prefix for its own routing, the page posts to
`/api/career-decisions-subscribe`, which is rewritten to the function with status 200 and is the
path the limit sits on. **The raw `/.netlify/functions/career-decisions-subscribe` path remains
reachable and is not rate limited**, as is true of every function on this site. The page does not
use it. Closing that would mean either a shared secret injected at the edge or a path check inside
the function, and neither was worth adding without first confirming the mechanism against a real
deploy.

**An edge function was tried first and did not work.** On 2026-08-27 the limit was declared as a
`rateLimit` config on a Netlify edge function bound to that path. Six sequential posts from one
address all reached the function and returned 400, with no 429, so the rule was not being enforced.
It was removed rather than left as dead code that reads like protection. The `rate_limit` key used
now is the one Netlify's own redirect parser recognises, confirmed by reading
`netlify-redirect-parser` 14.4.0, which carries it through to the backend for validation.

**Status at launch: accepted, not enforced.** This is the second mechanism tried, and neither has
been observed to work.

Netlify validates rate limit rules at the end of each deploy, in the post-processing stage, and
prints the details of valid rules in the deploy log under that stage. For deploy
`6a90bd2325e48400074b8e50` that stage shows the rule compiled: a path condition with value
`/api/career-decisions-subscribe` and `"regex": false`, an aggregate entry of `"type": "ip"`, and
`"status_code": 429`. Post processing completed and the site went live.

The rule nonetheless did not fire. Six sequential empty-body POSTs from one browser and one IP to
that path returned `[400, 400, 400, 400, 400, 400]`. Every request reached the function.

**What the evidence establishes is only that Netlify accepted the rule and did not enforce it on
Deploy Preview #92.** It does not establish why. One hypothesis is that rate limiting is not
enforced on deploy previews, which would mean production behaves correctly; that is **unconfirmed
and must not be assumed**. Another is that a limit on a redirect does not apply when that redirect
is a 200 rewrite to a Netlify Function, which would mean production behaves the same way. Both are
open questions in the Netlify support ticket.

**Until the production probe demonstrates otherwise, treat this form as having no per-IP rate
limit.** The probe is six sequential empty-body POSTs to
`https://temidayoafonja.com/api/career-decisions-subscribe`; the sixth must return 429. A green
deploy alone establishes nothing: the earlier edge attempt deployed green and did nothing.

**On the consequences of abuse.** Junk Kit subscribers can be removed. Not everything downstream of
a flood can be undone that easily: sustained submissions consume Kit API quota and generate outbound
email, and volumes of unwanted mail can affect sender reputation, which is slow to repair. Kit
should be watched closely while this is unresolved rather than relied on to be tidied up afterwards.

**What it deliberately does not do.** It does not touch the existing `xyegkbaq` priority-list
records. Those were collected with no opt-in, so moving them into Kit is a consent question and
not a technical one. Nothing in this change migrates them.

---

## Findings for counsel

1. **Only the Diagnostic separates marketing and research consent.** Six other forms collect an
   email address with no explicit opt-in. Whether that is acceptable depends on the
   jurisdictions in scope and how the addresses are subsequently used.
2. **Only the Executive Briefing form warns against sensitive data.** It is the form most
   likely to attract it, so that is the right priority, but the organizational inquiry form on
   `work.html` invites a description of an organizational decision and carries no such warning.
3. **`xjgapael` carries four submission types.** Retention and deletion policy will apply
   unevenly across them unless they are separated.
4. **Netlify Blobs storage** is used for the AI readiness and Scan captures. Retention there is
   not currently governed by any published policy.
5. **No form currently records a consent timestamp or the policy version in force.** If
   consent is later required, that record becomes necessary.
6. **Resolved.** The marketing checkbox on `diagnostic.html` did not gate the Kit sequence:
   enrolment fired on any valid email while the record preserved the visitor's "no". Gated by
   operator ruling in August 2026, verified in a browser across all three completion paths and
   both checkbox states. The dead pre-start checkbox was removed at the same time.
7. **Diagnostic answers are sent to a third-party AI provider.** `organizational-diagnostic.html`
   and `ai-capability-readiness.html` both post item-level answers and organizational context
   to the Anthropic API through a Netlify function, to generate the narrative read. Neither
   page nor the privacy policy discloses this.
