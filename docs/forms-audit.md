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

Four endpoints are now separated. `xjgapael` still carries four submission types
(book, two diagnostic captures, AI readiness), so any autoresponder attached to it fires for
all four.

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
- **Privacy link** — Yes

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

**Consent construction: best on the site, but it does not gate.** The two-checkbox design is
the model the other forms should follow. However, `subscribeToKit()` is called after every
completion with a valid email and is **not conditional on the marketing checkbox**. All three
completion paths behave this way: the gated completion, the skip-gate path, and the paper fast
path. A visitor who leaves the box unchecked is still enrolled in the Kit sequence, and the
stored record shows that they declined. See finding 6 below and
`docs/legal-review-required.md` section 1.10.

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
6. **The marketing consent checkbox on `diagnostic.html` does not gate the Kit sequence.**
   Enrolment fires on any valid email regardless of the checkbox, while the stored record
   preserves the visitor's "no". This is the highest-exposure finding in this audit. It is a
   code behaviour, not a wording problem, and it has not been changed here because it alters
   live lead capture. Operator decision.
7. **Diagnostic answers are sent to a third-party AI provider.** `organizational-diagnostic.html`
   and `ai-capability-readiness.html` both post item-level answers and organizational context
   to the Anthropic API through a Netlify function, to generate the narrative read. Neither
   page nor the privacy policy discloses this.
