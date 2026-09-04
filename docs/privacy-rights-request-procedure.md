# Privacy Rights Request Procedure

How to handle a request from someone who wants to see, correct, delete, or stop the use of their
information. Internal operating procedure, not published on the site.

Prepared August 12, 2026. Written against the systems described in `docs/data-inventory.md`.

**Requests arrive at** temidayo@thedensitygroup.com, which is the address published on `/privacy`.
There is no separate privacy inbox.

---

## 1. Response clock

| Regime | Deadline | Extension |
|---|---|---|
| GDPR and UK GDPR | 1 month from receipt | A further 2 months for complex requests, if the requester is told within the first month |
| Texas TDPSA | 45 days | A further 45 days with notice |
| CCPA, if it ever applies | 45 days | A further 45 days with notice |

**Operating rule: acknowledge within 5 business days, resolve within 30 calendar days.** That
satisfies every regime above without needing to work out which one applies first.

---

## 2. Step 1: log it

Record, in whatever tracker the firm keeps:

- Date received
- Requester name and email as given
- What they are asking for
- Which of the rights in section 4 it maps to
- Date acknowledged
- Date resolved, and what was done

Keep this log. If a request is ever disputed, the log is the evidence that it was handled.

---

## 3. Step 2: verify who they are

Do not skip this. Disclosing one person's data to another is a breach in itself.

**Standard verification.** The request must come from, or be confirmed from, the email address
the data is held under. Reply to that address and ask them to confirm. If they wrote from a
different address, ask them to send from the one they used on the site.

**For a deletion or access request covering diagnostic results**, additionally ask for one
detail that matches the stored record: approximate date of completion, the organization they
entered, or the result they were shown.

**If identity cannot be established**, say so plainly and explain what would establish it. Do not
guess. A request you cannot verify is one you must refuse, and refusing for that reason is
correct.

**Do not collect more identity data than the request requires.** Never ask for a government ID
for a request about an email address on a mailing list.

---

## 4. Step 3: identify the right being exercised

| They are asking to | Right | Section |
|---|---|---|
| See what you hold | Access | 6.1 |
| Fix something wrong | Rectification | 6.2 |
| Be deleted | Erasure | 6.3 |
| Stop marketing | Withdrawal of consent, objection | 6.4 |
| Be removed from research | Withdrawal of research consent | 6.5 |
| Get their data in a file | Portability | 6.6 |
| Pause use while a complaint is resolved | Restriction | 6.7 |

A single email often contains more than one. Handle each.

---

## 5. Where to look: the five locations

A single person's data can be in up to five places. **Check all five, every time.**

| # | System | How to search | How to delete |
|---|---|---|---|
| 1 | **Formspree** | Search submissions by email address in the Formspree dashboard | Delete the submission in the dashboard |
| 2 | **`audit-research` blob** | Export via `/.netlify/functions/audit-research-export?token=...&format=json`, search the JSON for the email | Re-call the export endpoint with `&delete=THE_KEY` |
| 3 | **`org-diagnostic-leads` and `ai-readiness-leads` blobs** | Corresponding export endpoints, same pattern | Same `&delete=THE_KEY` parameter |
| 4 | **Kit** | Search subscribers by email | Unsubscribe, or delete the subscriber outright for an erasure request |
| 5 | **The requester's own browser** | Not accessible to you | Tell them: clearing site data for temidayoafonja.com removes it. It self-expires after 7 days regardless |

**The sixth location, and its limit.** The `diagnose-rate` store is keyed by IP address, not by
identity. It cannot be searched by name or email, and it holds nothing that identifies a person
by itself. If a requester asks about it, explain that the record is keyed by an IP address the
firm cannot link to them, and that it holds only a request count. If the salted-hash change
recommended in `docs/data-inventory.md` section 10 is made, this stops being a question at all.

---

## 6. What to do for each right

### 6.1 Access

Provide a copy of what is held across locations 1 to 4, in a readable form. For a diagnostic
record that means their answers, scores, placement, the demographics they entered, their consent
flags, and the timestamps.

Also tell them, because access requests carry these obligations: the purposes, the categories of
recipient, the retention period, their other rights, and the right to complain to a supervisory
authority.

Send it to the verified email address.

### 6.2 Rectification

Correct the field in each location that holds it. If the incorrect data was shared with Kit,
correct it there too.

Diagnostic answers are a special case: they are a record of what the person said at a point in
time. If they now disagree with their own answers, that is not an inaccuracy to correct. Explain
this and offer erasure or a fresh completion instead.

### 6.3 Erasure

Delete from locations 1 to 4. Tell them about location 5 and its 7-day expiry.

**Before deleting, check whether anything must be kept.** If there is an unresolved dispute, a
payment record needed for tax purposes, or an ongoing engagement, that portion may need to be
retained. Say what you are keeping and why. Payment records are held by Maven, Gumroad, or
Amazon rather than by the firm, so this rarely applies.

Confirm in writing when it is done.

### 6.4 Stop marketing

The fastest route is the unsubscribe link in any email, and it is fine to say so. If they ask you
to do it, unsubscribe them in Kit and confirm.

Withdrawal is not retroactive: it stops future email, it does not undo email already sent.

### 6.5 Withdraw research consent

Set the flag to false, or delete the record. Because aggregates are computed from records where
the flag is true, flipping the flag removes them from all future aggregates. Tell them that
anything already published in aggregate form cannot be un-aggregated, which is why the aggregate
is anonymized in the first place.

### 6.6 Portability

Applies to data they provided, held on consent or contract, and processed by automated means:
their form submissions and diagnostic answers. Send JSON or CSV, not a PDF.

### 6.7 Restriction

Rare. Mark the record so it is not used or exported while the underlying issue is resolved, and
tell them when the restriction lifts.

---

## 7. When to refuse, and how

You may refuse a request that is manifestly unfounded or excessive, or where identity cannot be
verified. Refusal is legitimate; a silent refusal is not.

If you refuse:

1. Say so within the same 30-day window
2. Give the reason plainly
3. Tell them they can complain to a supervisory authority, and that they can seek a judicial
   remedy

Do not charge a fee for a first request.

---

## 8. If a request suggests a breach

If a request reveals that data has gone somewhere it should not have, stop and treat it as a
security incident rather than a rights request. Breach notification has its own, much shorter
clock: 72 hours to the supervisory authority under GDPR where the breach is reportable. Contact
counsel first, before responding to the requester.

---

## 9. Template acknowledgement

> Thank you for your message. This confirms we have received your request about your personal
> information, dated [date].
>
> So that we send information only to the right person, please confirm this request from the
> email address you used on our site. [If needed: it would also help if you could tell us
> approximately when you completed the diagnostic.]
>
> We will respond within 30 days. If your request turns out to be complex and we need longer, we
> will let you know before that deadline and explain why.
>
> Temidayo Afonja
> The Density Group LLC

---

## 10. Known weaknesses in this procedure

Recorded honestly, because a procedure that hides its gaps is worse than none.

1. **It is entirely manual.** Four systems, searched by hand. It works at current volume and
   will not scale.
2. **No consent timestamp or policy version is stored** alongside the consent flags. If someone
   disputes what they agreed to and when, the record shows only a boolean.
3. **Blob stores cannot be searched by email natively.** Each request requires a full export and a
   scan of the JSON. The export token travels in a URL query string, so avoid pasting those URLs
   into anything that logs them.
4. **No automated deletion.** Nothing expires on its own except the 7-day browser buffer.
5. **The IP store cannot serve a subject request** in any meaningful way, as explained in
   section 5.

Items 2, 3, and 4 are worth fixing before volume grows.
