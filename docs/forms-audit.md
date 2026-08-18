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
  2. **Netlify Blobs**, store `career-decisions-leads`, written **only after Kit confirms**, so
     the store can never hold a lead that is not also a subscriber. Best effort: a storage
     failure is logged and reported in the response as `durable_record: false`, and does not
     turn a real subscription into an error the visitor sees
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
    durable record. Guidance stamps are written only when guidance was actually given, so an empty
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
