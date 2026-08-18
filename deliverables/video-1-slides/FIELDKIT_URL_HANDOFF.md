# Request for the website channel: verify /fieldkit before Video 1 publishes

Copy everything below the line into the session that has the website build.

---

The Video 1 YouTube deck now sends viewers to `temidayoafonja.com/fieldkit` as the
single paid route for the Capability Formation Field Kit. Before the video
publishes, please verify that route on the live site. This is a verification
request. Do not change any file unless a check below fails, and if one fails,
report it before changing anything.

**Verify, in this order:**

1. `netlify.toml` still contains the redirect `from = "/fieldkit"` to
   `https://temidayoafonja.gumroad.com/l/czmqp`, status 301, `force = true`, and no
   later rule in the file shadows it.
2. The redirect is live in production, not just in the repository. Request
   `https://temidayoafonja.com/fieldkit` and confirm it lands on the Gumroad
   product page.
3. Confirm `https://temidayoafonja.gumroad.com/l/czmqp` is the current Capability
   Formation Field Kit listing, that it is published and purchasable, and that the
   price shown there matches the $150 stated on `book.html`. If Gumroad and
   `book.html` disagree, report the mismatch and do not edit either.
4. Confirm the behaviour of `https://temidayoafonja.com/fieldkit/` with a trailing
   slash. If it does not redirect the same way, report it.
5. Netlify redirect paths are matched case sensitively. Confirm whether
   `/FieldKit` or `/FIELDKIT` resolve. If they do not, report it. A viewer typing
   the URL from a video may capitalise it.
6. Confirm `book.html` still lists the Field Kit with a working "Get the Field Kit"
   button to the same Gumroad product. The video does not link to `/book`, but the
   page should stay consistent with what the video promises.

**One decision to confirm, not a change to make:**

`/fieldkit` is a forced 301 to an external URL, so no page on the site is served
and the Plausible script never runs. Clicks driven by the video will not appear in
site analytics; only Gumroad will see them. Confirm that is intended. If Temidayo
wants the video's traffic visible in Plausible, say so and propose options for her
to approve. Do not implement anything for this without approval.

**Out of scope, do not touch:** the Field Kit price, `book.html` layout or copy,
any other redirect, the sitemap, any other page, and anything in
`deliverables/video-1-slides/`.

**Report back:** each check as pass or fail, the exact response code and final URL
you observed for `/fieldkit`, and any mismatch found, with no changes made unless
you were told to make them.
