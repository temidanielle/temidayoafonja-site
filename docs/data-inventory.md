# Data Inventory

Every data flow on temidayoafonja.com, established by reading the code rather than by
description. Prepared August 12, 2026, against `main`.

This is the factual basis for the Privacy Policy rewrite, the applicability analysis, and the
rights-request procedure. It is an internal working document, not published on the site.

**Method.** Every form handler, Netlify function, client script, storage call, and outbound
endpoint in the repository was inspected directly. Where this document contradicts an earlier
brief, this document is correct and the correction is marked.

---

## 1. Correction to a previous brief

`docs/legal-review-required.md` section 1.1 stated that IP addresses were "not collected by
first-party code, but received by Formspree, Netlify, and Anthropic in the ordinary course."

**That was wrong.** The site stores visitor IP addresses in first-party durable storage. See
flow 10 below. The legal brief is corrected in the same pass as this document.

---

## 2. First-party collection points

### Forms (nine)

| # | Page | Purpose | Endpoint |
|---|---|---|---|
| 1 | `executive-briefing.html` | Enterprise inquiry | Formspree `xqpzegoj` |
| 2 | `work.html` | Enterprise inquiry | Formspree `xqpzegoj` |
| 3 | `for-professionals.html` | Workshop priority list | Formspree `xyegkbaq` |
| 4 | `speaking.html` | Speaking inquiry | Formspree `xgawaegz` |
| 5 | `book.html` | Book and Field Kit list | Formspree `xjgapael` |
| 6 | `diagnostic.html` | Completion capture | Formspree `xjgapael` |
| 7 | `diagnostic.html` | Paper fast path | Formspree `xjgapael` |
| 8 | `organizational-diagnostic.html` | Scan results capture | Formspree `mjgndvkp` |
| 9 | `ai-capability-readiness.html` | AI readiness capture | Formspree `xjgapael` |
| 10 | `career-decisions.html` | Career Decision Evidence Check | `/.netlify/functions/career-decisions-subscribe` |

All ten post JSON by `fetch`. None uses a native form POST, so nothing is submitted on a page
navigation. Form 10, added August 17 2026, is the only one that does not post to Formspree: it
posts to its own Netlify function, which is the single write path for that page.

### Categories collected

| Category | Where | Notes |
|---|---|---|
| Name | All nine forms | |
| Email address | All nine forms | Work email on enterprise forms |
| Organization | Seven forms | Optional on `work.html` |
| Job role or level | Executive Briefing, Diagnostic gate | |
| Free-text decision description | Executive Briefing, `work.html`, `speaking.html`, `for-professionals.html` | Unbounded. May contain third-party personal data |
| Diagnostic item-level answers | Three instruments | Every answer stored, not only totals |
| Computed scores and placement | Three instruments | Density, Optionality, Alumni Capital, quadrant, boundary flags |
| Self-reported demographics | `diagnostic.html` | Industry, role level, years of experience, organization size |
| Organizational profile | Scan, AI readiness | Sector, headcount, mission exposure, recent change, AI change pressure |
| Consent flags | `diagnostic.html` only | Research and marketing, as booleans |
| Timestamps | Server captures | UTC and America/Chicago |
| Submission identifier | `diagnostic.html` | Client-generated UUID, used for server-side deduplication |
| **IP address** | **`diagnose` function** | **See flow 10. First-party durable storage** |
| Two separate consents | `career-decisions.html` only | Delivery of the requested resource, and ongoing guidance. Each with its own client stamp, its own independent server stamp, and its own policy version. Guidance stamps are written only when guidance was given |
| Campaign attribution, two touches | `career-decisions.html` only | `first` and `current`, each carrying `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `source`, `video_slug`, `landing_page`, `referrer`, `seen_at`. Recorded only when the visitor actually arrives with them, never inferred |

---

## 3. Client-side storage

No cookies are set by first-party code. `document.cookie` does not appear anywhere in the
repository.

`sessionStorage`, one use, added August 17 2026:

| Key | Written by | Contents | Expiry |
|---|---|---|---|
| `cd_attribution` | `career-decisions.html` | Two touches, `first` and `current`, each holding the campaign values the visitor arrived with: `utm_*`, `source`, video slug, landing page, referrer, and the time of that visit. No name, no email, no free text | Discarded by the browser when the tab closes. Never sent anywhere except with the visitor's own submission |

It exists so that a visitor who arrives from a video and then moves around the page does not lose
the attribution before they submit.

**Two touches, not one.** `first` is the campaign visit that introduced the person to the page and
is never overwritten. `current` is the most recent explicit campaign visit in the same session. A
viewer can find the page from one video, leave it open, return later from a different video and
only then subscribe: keeping only the first attributes them to a video they had moved on from, and
keeping only the last erases the video that actually found them. Both are kept.

A bare return to `/career-decisions` with no parameters is not an explicit campaign visit and
changes neither touch. Nothing is written on a page the visitor did not actually land on.

`localStorage`, two uses:

| Key | Written by | Contents | Expiry |
|---|---|---|---|
| `cf_pending_research_<timestamp>_<random>` | `diagnostic.html` | A full research payload: item-level answers, scores, demographics, name, email, consent flags | Self-expires after 7 days, enforced in code (`RESEARCH_PENDING_MAX_AGE_MS`) |
| `cf_submissions` | `dashboard.html` | Locally entered submission records | None. Persists until the browser clears it |

The pending-research key is a delivery retry buffer: it is written only when the network call
fails, and removed once the payload is successfully resent. It nonetheless places personal data
on the visitor's own device.

`dashboard.html` is publicly reachable at `/dashboard.html` with no authentication. It reads
only the local browser's storage, so it exposes no server-side data, but it is disallowed in
`robots.txt` and should be reviewed for whether it belongs in the deployed site at all.

---

## 4. Server-side durable storage: Netlify Blobs

> **Correction, August 13 2026. These four stores are empty and always have been.**
>
> Netlify was not injecting a Blobs context into this site's functions, so every `getStore()` call
> failed with `MissingBlobsEnvironmentError`. All seven functions that use Blobs were affected. The
> three capture functions caught the error and returned a 500; the rate limiter caught it and
> returned "not limited", which is why nothing ever looked broken.
>
> The table below therefore describes **intended** behaviour, not observed behaviour. This document
> originally asserted it as fact, having been written from the code rather than from the running
> system. That was a real limitation of the method, and it is recorded here rather than quietly
> edited away.
>
> **Found by calling the export endpoints against production**, which this environment cannot
> reach; the operator ran them. The fix passes `siteID` and `token` to `getStore()` explicitly via
> `netlify/lib/blobs.js`. **Until a deploy carries that fix and the two variables are set, no
> durable record exists for any submission.**
>
> **What this means for the privacy analysis.** Everything downstream of this section that treats
> the four stores as holding personal data is, as of today, describing a risk that has not
> materialised. There is nothing to retain, export, or delete. Once the fix ships the table below
> becomes accurate, and the retention question becomes live for the first time. Counsel should read
> it that way, and setting retention periods before the stores start filling is now the cheaper
> order of operations.
>
> **Formspree is unaffected.** All nine forms post to Formspree independently, so every submission
> was still delivered by email. The lost artefact is the structured, exportable record, not the lead.

Four stores.

| Store | Written by | One record per | Contents | Retention |
|---|---|---|---|---|
| `audit-research` | `audit-research.js` | Diagnostic submission | Item-level answers, scores, demographics, name, email, consent flags, timestamps, submission id | **None enforced. Indefinite** |
| `org-diagnostic-leads` | `org-diagnostic-capture.js` | Scan completion | Lead and result fields | **None enforced. Indefinite** |
| `ai-readiness-leads` | `ai-readiness-capture.js` | AI readiness completion | Lead and result fields | **None enforced. Indefinite** |
| `diagnose-rate` | `diagnose.js` | **Salted SHA-256 of the IP**, not the address | Request count and window start | Still unbounded, but no longer personal data. Purge on the follow-up list |
| `career-decisions-leads` | `career-decisions-subscribe.js`, read back by `career-decisions-export.js` | Confirmed subscription | First name, email, optional decision text, **both** consent booleans with their own client and server timestamps and policy versions, both attribution touches, whether the youtube tag was applied, Kit subscriber id | Until the subscriber unsubscribes or asks for deletion. Stated in the policy |
| `career-decisions-rate` | `career-decisions-subscribe.js` | **Salted SHA-256 of the IP**, not the address | Request count and window start | Same construction and same open purge question as `diagnose-rate` |

The two `career-decisions` stores are subject to the same correction as the four above: without
`BLOBS_SITE_ID` and `BLOBS_TOKEN` set in Netlify, neither is written and the rate limit is off.

> **Status at launch, 2026-08-27.** Both variables are set and Blobs still fails site-wide with a
> 400 from the Blobs API, so **neither `career-decisions-leads` nor `career-decisions-rate` is
> written**. No IP hash is stored by this form, and no lead record is stored by it. Abuse protection
> does not depend on that: `netlify/edge-functions/career-decisions-rate-limit.js` enforces five
> submissions per 180 seconds per IP at the edge, and stores nothing at all, so it adds no personal
> data to this inventory. Netlify holds the request counts, not this site. See
> docs/forms-audit.md section 10.
The function logs both conditions explicitly rather than failing silently, and it reports
`durable_record: false` in its response, so the absence is visible rather than assumed.

**Records where research consent is false are still written** to `audit-research`, flagged so
they can be excluded from any aggregate. That is a defensible auditability design, but it is not
disclosed anywhere and counsel should confirm it is the intended construction.

---

## 5. Outbound third-party flows

| Provider | Triggered by | Data sent | Purpose |
|---|---|---|---|
| **Formspree** | All nine forms | Every field submitted | Owner email notification |
| **Netlify** | All traffic | All requests, plus durable storage above | Hosting, functions, storage |
| **Anthropic** | Scan and AI readiness completion | Item-level answers plus organizational context | Generates the narrative read |
| **Kit (ConvertKit)** | Diagnostic completion **with marketing consent** | Email, name, organization, quadrant, scores, result line, tags | Automated email sequence |
| **Kit (ConvertKit)** | Career Decision Evidence Check **with explicit delivery consent** | First name, email, optional decision text, both consent records, both attribution touches, tags | Delivers the evidence check, and owns deduplication and unsubscribe. Ongoing guidance is a separate tag applied only on the second, optional consent, and is the only tag a broadcast may target |
| **Plausible** | Every page load | Aggregate analytics only | Cookieless, no personal data |
| ~~Google Fonts~~ | **Removed August 12 2026.** Fonts are now self-hosted from `/fonts`, so no visitor IP reaches Google | | |
| **Gumroad** | `/fieldkit` redirect | Handled entirely on Gumroad | Field Kit purchase |
| **Maven** | Outbound links | Handled entirely on Maven | Lightning Lesson and workshop registration |
| **Amazon** | Outbound links | Handled entirely on Amazon | Book purchase |

Kit enrolment is gated on the marketing checkbox as of August 2026, verified in a browser across
all three completion paths.

No payment data is ever received or stored by this site. All paid transactions complete on
Maven, Gumroad, or Amazon. This is favourable and worth stating plainly in the Terms.

---

## 6. Third-party scripts loaded in the page

Exactly one: `https://plausible.io/js/pa-hFo9m_622E0tElKtUlVnx.js`, loaded `async` on 15 pages.

Plus Google Fonts stylesheets and font files from `fonts.googleapis.com` and
`fonts.gstatic.com`.

No tag manager, no advertising pixel, no session recorder, no chat widget, no A/B tool.

---

## 7. Cookie and tracker inventory

| Name | Set by | Type | Purpose |
|---|---|---|---|
| (none) | First-party code | | No cookies are set by this site |

Plausible is cookieless by design, which the current privacy policy already states correctly.

Google Fonts sets no cookie but does receive the visitor's IP address on every page load, which
is a data transfer rather than a cookie question.

**Consequence for the policy:** a cookie banner is not required on the current implementation.
If that changes, this table must change with it.

---

## 8. Secrets and access control

| Item | Storage | Note |
|---|---|---|
| `ANTHROPIC_API_KEY` | Netlify environment variable | Never in page source |
| `KIT_API_KEY` | Netlify environment variable | Never in page source |
| `RESEARCH_EXPORT_TOKEN` | Netlify environment variable | **Passed as a URL query parameter** |

No secrets appear in the repository. The export token is the weak point: it is transmitted as
`?token=...`, and query strings are routinely written to server logs, proxy logs, and browser
history. A bearer header would be the safer construction. This gates access to the full research
and lead stores, so it is the highest-value credential on the site.

---

## 9. Data subject request feasibility

A single individual's data can sit in up to five places:

1. Formspree submissions
2. `audit-research` blob, keyed by submission id
3. Kit subscriber record, if they consented
4. Their own browser `localStorage`, for up to 7 days
5. `diagnose-rate`, keyed by IP, if they used the Scan

Deletion is technically feasible. Blob keys are addressable and the export endpoints accept
`&delete=THE_KEY`, **with one exception**: `career-decisions-export.js`, added August 2026, is
read only and refuses that parameter. Deleting a `career-decisions-leads` record for a rights
request therefore has to be done deliberately rather than through the reporting endpoint, which
is the intended construction. There is no automated process; each request would be handled manually across
at least three systems.

**The IP store is the hardest.** It is keyed by IP with no link to any identity, so responding to
a request about it requires the requester's IP at the time of use, which they are unlikely to
know and which the site does not link to their submission.

---

## 10. The finding that needs a decision

### Visitor IP addresses are stored in first-party durable storage

`netlify/functions/diagnose.js` rate-limits the Scan's narrative generation at 25 requests per
hour. It does this by writing a record to the `diagnose-rate` Netlify Blobs store **keyed by the
visitor's IP address**:

```
const store = getStore("diagnose-rate");
const rec = await store.get(ip, { type: "json" });
await store.setJSON(ip, { windowStart, count });
```

Facts:

- The IP is the blob key, so the store is a list of IP addresses that used the Scan
- Records are overwritten on each request but **never deleted**, so the store accumulates
  indefinitely even though the rate window is only one hour
- Nothing purges records once the window has elapsed
- This is the only rate limiter on the site; no other function does this
- It is disclosed nowhere: not in the privacy policy, not on the page

An IP address is personal data under GDPR, and is treated as personal information under several
US state regimes. The rate limiter itself is a legitimate security measure and worth keeping.
The problems are retention and disclosure, not the purpose.

**Three options, none applied:**

1. **Hash the key.** Store a salted hash of the IP instead of the IP. The rate limiter works
   identically; the store stops being a list of visitor IPs. Smallest change, largest benefit.
2. **Purge on read.** Delete records older than the rate window. Keeps plain IPs but bounds
   retention to one hour.
3. **Disclose and retain.** Leave the code alone and describe it in the privacy policy.

Recommendation: option 1, with option 2 as well. It preserves the security function, removes the
personal data, and needs no policy language beyond a general security statement.

This is a code change to a live function, so it is flagged rather than applied.

---

## 11. Open questions for the operator

These block the applicability analysis, not this inventory.

1. **Are EU or UK visitors in scope?** This determines whether GDPR and UK GDPR apply, which in
   turn determines the lawful-basis analysis, the rights set, the transfer analysis for Anthropic
   and Kit, and whether the Google Fonts IP disclosure needs remediation. It is a business fact
   about audience and marketing reach that cannot be derived from the repository.
2. **Where should the 18+ minimum appear?** Terms of Use only, or also on `for-professionals.html`
   where people register. Placement affects whether it functions as a condition of sale or only
   as a term.
3. **Is `dashboard.html` intended to be publicly deployed?** It is reachable without
   authentication and disallowed in `robots.txt`.

---

## 12. What this inventory establishes for the policy

The Privacy Policy must describe, at minimum:

- Nine forms and the categories each collects
- Item-level diagnostic answers stored durably, including for non-consenting research subjects
- Four durable stores with no retention limits
- Local storage of personal data on the visitor's device for up to 7 days
- Nine service providers, of which the policy currently names one
- Transmission of diagnostic answers to an AI provider
- IP address storage, subject to the decision in section 10
- Marketing enrolment as a distinct purpose, currently undisclosed
- That no payment data is received or stored
