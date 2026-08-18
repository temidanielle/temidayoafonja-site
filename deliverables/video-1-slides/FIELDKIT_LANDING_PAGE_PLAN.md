# Plan on file: a real page at /fieldkit (option C)

Status: **approved in principle, not scheduled.** Nothing here is built. This is
the record of what was agreed so it can be picked up later without re-deciding.

## Why

`/fieldkit` is currently a forced redirect, so no page is served, Plausible never
runs, and Temidayo has no visibility of the traffic the video sends. Option B,
tagging the Gumroad destination, buys attribution inside Gumroad but still shows
her nothing in her own analytics.

A real page at `/fieldkit` would:

1. Record the visit in Plausible, and because that route is promoted only in the
   video, a pageview there is a strong signal of video-driven traffic.
2. Give a cold YouTube viewer something to read before being asked to pay.
   Sending someone straight from a video to a checkout asks for the decision
   before the context.
3. Keep the deck's URL unchanged. Video 1 already says `temidayoafonja.com/fieldkit`,
   so this can ship without touching any published slide.

## What it is

A short page, not a long sales page. The Field Kit is a $150 self-diagnostic, and
the existing `book.html` section already says what it is in a few lines.

- Existing design system only: cream, navy, gold, the site's own type, the real
  Field Kit cover and real interior pages. No stock imagery, no invented
  testimonials, no fabricated screenshots.
- Says what the Field Kit is, who it is for, what the buyer does with it, and the
  price, consistent with `book.html`.
- One button through to the Gumroad product, carrying the UTM tags from option B.
- Nothing beyond the approved product boundary. It does not identify adjacent
  roles, map industries or employers, promise a Career Portability Map, promise
  an AI Role Relevance Audit, or guarantee title or compensation.

## Sequence when it is built

1. Build the page and review it before it is reachable.
2. Change the `/fieldkit` rule from a redirect to serving the page. This is why
   option B recommends dropping the status from 301 to 302 now; a cached 301
   would send returning visitors past the page.
3. Verify `/fieldkit`, `/fieldkit/`, and capitalised variants.
4. Add the page to the sitemap.
5. Point the `book.html` Field Kit section at `/fieldkit` so there is one
   destination rather than two competing ones.
6. Confirm Plausible records the pageview, and add an outbound click event on the
   buy button so the page can be judged on whether people actually continue.

## Open decisions, for Temidayo

- Does `/book` keep listing the Field Kit, or does it point at `/fieldkit` and
  stop carrying the detail itself?
- How long is the page: a tight single screen, or enough room to explain the
  Capability Position Read?
- Does the page state the price, or leave price to Gumroad?

## Not to do

No price change without approval. No new claims about what the Field Kit does.
No countdowns, scarcity language, testimonials that were not given, or metrics
that were not measured.
