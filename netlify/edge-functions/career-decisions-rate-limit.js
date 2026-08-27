// Per-IP rate limit for the Career Decision Evidence Check submission.
//
// Why this exists. The submission function has always had a rate limiter, but
// it is built on Netlify Blobs, and Blobs has been failing site-wide since
// 2026-08-20 with an unexplained 400 from the Blobs API. That limiter is
// deliberately fail-open, so a storage fault cannot take the form down, which
// means the form currently has no working rate limit at all. This one is
// enforced by Netlify at the edge, before any function runs, and depends on
// nothing this site configures. It stands whether or not Blobs is ever fixed.
//
// The function body is empty on purpose. Returning nothing passes the request
// straight through to the submission function. The whole behaviour is in the
// config below, applied by Netlify before this code is reached, so a rejected
// request costs no function invocation.
export default async () => {
  // Deliberately empty. See above.
};

export const config = {
  // The clean path, not /.netlify/functions/..., because Netlify reserves that
  // prefix for its own routing. netlify.toml rewrites this path to the function
  // with status 200, so the URL the page posts to is the one carrying the
  // limit.
  path: "/api/career-decisions-subscribe",

  rateLimit: {
    // Five submissions per three minutes from one address. A real visitor
    // submits once; five leaves room for a retry after a network error and for
    // two people behind one office address, while stopping a flood.
    //
    // Netlify caps windowSize at 180 seconds, so the hour-long window the
    // Blobs limiter uses cannot be expressed here. These are different tools:
    // this one stops bursts, and the Blobs limiter, once storage works again,
    // is what enforces a sustained hourly ceiling. Both are kept.
    windowLimit: 5,
    windowSize: 180,

    // Per address, scoped to this domain, so one visitor's quota is their own.
    aggregateBy: ["ip", "domain"],

    // Refuse with 429 rather than rewriting to a page. This path is only ever
    // reached by the form's fetch, which reads a status, not a document.
    action: "rate_limit"
  }
};
