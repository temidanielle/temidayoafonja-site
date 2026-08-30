# Career Evidence Starter: delivery and follow-up email copy

Draft copy for the two Kit emails. **Not yet built in Kit.** Both are sent by the
sequence identified by `KIT_SEQ_CAREER_EVIDENCE_STARTER`, which every subscriber
who ticks the delivery consent enters. Neither is sent to the guidance tag.

Two emails only, as instructed. No longer nurture sequence yet.

---

## Email 1: immediate delivery

**Subject:** Your Career Evidence Starter

**Preview text:** One accomplishment, one focused sitting.

**Body:**

Hi {{ subscriber.first_name }},

Here is your Career Evidence Starter.

**[Download the Career Evidence Starter (PDF)]**

Before you open it, pick one piece of work. One project, decision, problem,
improvement or piece of work where something changed because you were involved.

Do not try to complete your whole career history. The Starter is built for a
single accomplishment, and it works because it is narrow. You can run it again
later on something else.

Set aside about 10–15 focused minutes.

Two practical notes:

- The PDF has fillable fields. It works best in Adobe Acrobat Reader, which is
  free. Some browser PDF viewers will let you type but will not save what you
  typed.
- You can also print it and write on it by hand. The fields sit on printed rules
  for exactly that reason.

One thing to keep in mind as you fill it in: record only your own recollection
and information you are permitted to retain. There is a permission checklist on
page 2. If you are unsure whether you can keep something, leave it out.

Temidayo

Temidayo Afonja
Career Portability Advisor
Founder, The Density Group

---

## Email 2: follow-up, two to three days later

**Subject:** Did you find one that was more useful than you remembered?

**Preview text:** That reaction is the point of the exercise.

**Body:**

Hi {{ subscriber.first_name }},

A question about the Career Evidence Starter: did you find one piece of work
that turned out to be more useful than you remembered?

That happens often. The work looked ordinary at the time, and only became
visible once you had to say what changed and which part was yours.

If it did happen, it is worth noticing why. The detail was still recoverable
because you went looking while it was close enough to reconstruct accurately.
That gets harder every month.

One entry is useful on its own. It is enough for a review or an interview
answer. What it does not give you is a record: a place where the next one goes,
and the one after that, so you are not doing this from memory when something
urgent arrives.

That is what Keep the Proof is for. It is the complete 60-minute Career Evidence
System, plus the reusable Career Evidence Ledger for capturing, translating,
organising and maintaining the whole record over time.

**[Keep the Proof: A 60-Minute Career Evidence System]**
temidayoafonja.com/keep-the-proof

If the Starter was all you needed, that is a good outcome too. You can keep
using it on one piece of work at a time.

Temidayo

---

## Notes for whoever builds these in Kit

- **The download link is not yet decided.** The PDF is not stored in this
  repository: no PDFs are, by existing convention. Where the file is hosted, and
  therefore what the link points at, is an open decision. See the QA report.
- **No urgency, no scarcity, no discount.** As instructed. The follow-up asks a
  question and names the next product once.
- **Do not send either email to the guidance tag.** Delivery consent and
  guidance consent are separate choices on the page and are recorded separately.
  Ongoing marketing is filtered on `KIT_TAG_CAREER_EVIDENCE_STARTER_GUIDANCE`
  only, never on the delivery tag.
- **The price is not stated in either email**, and is not stated in the PDF. The
  website remains the source of truth for pricing.
