# Request for the website channel: tag the /fieldkit destination (option B)

Approved by Temidayo. Copy everything below the line into the session that has
the website build.

Already verified on the live site, so do not re-litigate it: `/fieldkit` and
`/fieldkit/` both land on the Gumroad product, and `czmqp` is the correct
Capability Formation Field Kit listing.

---

The Video 1 YouTube deck sends viewers to `temidayoafonja.com/fieldkit`. That
route is a forced 301 to Gumroad, so no page is served, the Plausible script
never runs, and nothing on our side records the visit. Gumroad sees it, but a
typed URL carries no referrer, so Gumroad will most likely file it as direct.
Temidayo has approved tagging the destination so Gumroad can attribute it.

**Change 1, approved. Add tracking parameters to the redirect destination.**

In `netlify.toml`, change only the `to` value of the existing `/fieldkit` rule:

```
from:  to = "https://temidayoafonja.gumroad.com/l/czmqp"
to:    to = "https://temidayoafonja.gumroad.com/l/czmqp?utm_source=temidayoafonja.com&utm_medium=redirect&utm_campaign=fieldkit-link"
```

Leave `from`, `status` and `force` alone except for change 2 below. Do not
create a second route, do not touch any other redirect.

The campaign value is deliberately `fieldkit-link` rather than `video-1`.
`/fieldkit` is promoted only in Video 1 today, so every hit is video traffic
right now, but the tag should not claim more than it knows. If Temidayo later
promotes `/fieldkit` in a newsletter or on LinkedIn and wants those separated,
the pattern is a sibling route per source, each with its own campaign value.
Do not build that now.

**Change 2, recommended, flag it if you disagree. Make the redirect a 302.**

A 301 tells browsers the move is permanent and they cache it, sometimes
indefinitely. A future plan, already approved in principle, replaces this
redirect with a real Field Kit page at `/fieldkit`. Anyone whose browser cached
the 301 would skip that page and keep going straight to Gumroad. Changing
`status = 301` to `status = 302` now costs nothing, since the destination is an
external store with no SEO value to preserve, and it keeps that door open.

**Verify after deploying:**

1. `https://temidayoafonja.com/fieldkit` still lands on the Gumroad product, and
   the UTM parameters are present in the final URL.
2. `https://temidayoafonja.com/fieldkit/` with the trailing slash behaves the same.
3. A request with its own query string, for example `/fieldkit?x=1`, does not
   break the redirect or lose the UTM parameters. Report exactly what arrives at
   Gumroad if the two query strings collide.
4. **Gumroad actually surfaces the tags.** This is the check that decides whether
   the change was worth making. Visit through the redirect, then look at
   Gumroad's analytics for that product and confirm the visit is attributed to
   the source rather than filed as direct. If Gumroad ignores UTM parameters,
   say so plainly and stop; do not invent a workaround. That result changes the
   recommendation and Temidayo needs to hear it.

**Out of scope, do not touch:** the Field Kit price, `book.html`, any other
redirect, the sitemap, any page, and anything in `deliverables/video-1-slides/`.

**Report back:** each check as pass or fail, the exact final URL you observed
after the redirect, and what Gumroad's analytics showed for the test visit.
