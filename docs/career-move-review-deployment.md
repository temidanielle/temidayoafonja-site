# Career Move Review: deployment and outstanding decisions

Internal. This file lives in `docs/`, which `netlify.toml` force-404s, so it is
never served. Last updated 2026-09-18.

---

## 1. Environment variable

One variable has to exist before the request form works.

| Name | `FORMSPREE_CAREER_MOVE_REVIEW` |
|---|---|
| Scope | Runtime (the function reads it at request time) |
| Contexts | Production and Deploy previews. Set both, or the preview test below cannot pass. |
| Expected format | A full HTTPS Formspree endpoint URL, `https://formspree.io/f/` followed by the eight-character form ID |
| Example shape | `https://formspree.io/f/xxxxxxxx` |
| Where it is read | `netlify/functions/career-move-review-request.js`, once, at the point of forwarding |

**The real value is not recorded here and must not be.** The site keeps secrets
in the Netlify environment, never in the repository and never in page source.
The line above is the shape of the value, not the value.

Note that this is already an improvement on the site's other inquiry forms.
Every other Formspree endpoint on this site is written directly into page
source, where anyone can read it. This one is held in the environment and the
browser never sees it.

### After setting it

Environment changes do not reach a running function until the site is
redeployed. Set the variable, redeploy, then run the end-to-end test below.

### Until it is set

`/api/career-move-review-request` returns `503 not_configured`, naming only the
missing variable and never a value. The page shows:

> The request form is temporarily unavailable. Please email your name and the
> move you are considering to temidayo@thedensitygroup.com. Do not send a resume
> or confidential information yet.

That address is the one already published elsewhere on this site. No new
address was introduced.

---

## 2. Launch gate

**The Career Move Review is not launch ready and must not be described as such,
announced, or linked from any outbound channel, until both of these are true.**

1. `FORMSPREE_CAREER_MOVE_REVIEW` is configured and the site has been
   redeployed.
2. A real end-to-end submission has passed **in a controlled deploy preview**:
   the form submitted, the function reached, the destination received it, and
   the success panel shown.

Local tests cover the function's logic and every form state, including a mocked
success. They cannot prove that the live destination accepts a real request.
Only the preview test does that.

Do not run that test against production.

---

## 3. Legal review, a pre-deployment gate

`docs/legal-review-required.md` is parked by operator instruction. A paid
one-to-one advisory service with a written deliverable sits inside what that
document was opened to handle.

**No legal language has been drafted, and none may be invented.** The following
are decisions for Temidayo or counsel, not copy questions. Each is listed
because the service cannot responsibly take money until it has an answer, not
because a particular answer is expected.

### Service scope

What the Career Move Review does and does not commit to. The page already
states the exclusions and says plainly that it does not promise anyone will
qualify for, obtain or succeed in a role. Whether that is sufficient as a
contractual limitation, or whether terms of engagement are needed, is a counsel
question.

### Cancellation

What happens if the client cancels. How much notice, and whether there is a
point after which the fee is retained.

### Rescheduling

Whether a session can be moved, how much notice is required, and whether there
is a limit.

### Refunds

Whether any refund is offered, under what conditions, and up to what point.
This interacts with the delivery promises: the Summary is committed within five
business days of the session, so a refund position taken after delivery is a
different question from one taken before.

### Privacy

The intake collects a name, an email address, a LinkedIn profile or written
career summary, an intended move, and timing and constraints. Two questions
follow. Whether `privacy.html` as written already covers this category of
collection, and how long submissions are retained at the destination.

The current `POLICY_VERSION` stamped on every submission is `2026-08-18`, which
matches the "Last updated" date on `privacy.html`. **If the privacy policy is
revised for this service, that constant must move in the same commit.** A
consent record whose policy version predates the wording the person actually
read is not evidence of anything.

### Handling of the written deliverable

Who owns the Career Move Summary, whether the client may share it, and whether
Temidayo may reference the work. Also whether any part of it may be used, in
anonymized form, as evidence for the service itself. Note that no individual
testimonial or outcome currently exists and none may be invented, so the pilot
is the only route to that evidence and the permission needs to be settled
before, not after.

### Resume handling, once accepted

The public form deliberately accepts no files. After acceptance a resume is
requested by reply, which puts it in an ordinary mailbox. Whether that is an
acceptable resting place for the document, and for how long, is worth a
decision rather than a default.

---

## 4. Testing without production

Every check in this implementation was run locally or against a local server.

- The function was exercised directly with a stubbed `fetch`, so no request ever
  left the machine.
- The form's success and error states were produced by replacing `window.fetch`
  in the page, not by submitting anything.
- The screenshots of the success state and the 503 state were produced the same
  way.

**No production submission was made at any point, and none should be made to
produce documentation.**
