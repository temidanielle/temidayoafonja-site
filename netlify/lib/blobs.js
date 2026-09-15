// Shared Netlify Blobs accessor.
//
// ── Why this file looks the way it does ──
//
// These functions use the Lambda-compatible signature, `exports.handler =
// async (event) => ...`. In that mode Netlify does **not** put the Blobs
// context in the environment. It arrives on `event.blobs`, as base64 JSON,
// alongside the `x-nf-site-id` and `x-nf-deploy-id` request headers, and
// `connectLambda(event)` is what unpacks it into the context the client reads.
// Until that call runs, `getStore()` has nothing to find.
//
// That is the whole of the site-wide Blobs failure that began on 2026-08-13 and
// was confirmed by Netlify support case #1099659 on 2026-09-15, who reproduced
// it against this repository's own export function: it fails without
// connectLambda(event) and succeeds with it. There was no project flag, no
// provisioning defect, no bundler problem and no credential problem. The
// earlier manual `{ siteID, token }` configuration in this file was a workaround
// for a cause that had been misdiagnosed, and it is gone.
//
// ── Fail closed ──
//
// If the Lambda context is absent, these functions throw. They do not fall back
// to manual credentials. A silent fallback is what hid this fault for a month:
// every call took a route that could not work, reported a plausible-looking
// error, and nothing anywhere said the real route had never been attempted.
// BLOBS_SITE_ID and BLOBS_TOKEN are no longer read here at all.
const { connectLambda, getStore } = require("@netlify/blobs");

// One connect per invocation. connectLambda sets a module-global context, so
// repeating it is harmless, but the event object is a reliable identity for
// "this invocation" and a WeakSet keeps no reference alive after it.
const connected = new WeakSet();

/**
 * Unpacks the Blobs context carried on a Lambda event. Must run before any
 * getStore() call in the same invocation.
 *
 * Throws rather than returning a flag: a caller that has not connected cannot
 * do anything useful with a store, so there is no correct way to continue.
 */
function connectBlobs(event) {
  if (!event || typeof event !== "object") {
    throw new Error("blobs_event_missing");
  }
  if (connected.has(event)) return;
  if (!event.blobs) {
    // Netlify did not attach a Blobs context to this invocation. Nothing about
    // the event is logged or thrown: the message is a fixed code.
    throw new Error("blobs_context_missing");
  }
  connectLambda(event);
  connected.add(event);
}

/**
 * A store handle, on the connected zero-configuration path.
 *
 * `event` is required. Every call site passes the event of the invocation it is
 * serving, including helpers that previously took only their own arguments.
 */
function blobStore(name, event) {
  connectBlobs(event);
  return getStore(name);
}

/**
 * Whether this invocation can reach Blobs at all, without throwing. For
 * diagnostics and for branching on best-effort writes. Never reports anything
 * about the context beyond its presence.
 */
function blobsAvailable(event) {
  return Boolean(event && typeof event === "object" && event.blobs);
}

module.exports = { blobStore, connectBlobs, blobsAvailable };
