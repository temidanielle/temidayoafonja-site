// Shared Netlify Blobs accessor.
//
// Why this file exists. Netlify normally injects a Blobs context into the
// function environment, and getStore("name") picks it up with no configuration.
// On this site that injection does not happen: every getStore() call threw
// MissingBlobsEnvironmentError in production, across all seven functions that
// use Blobs, and a fresh deploy did not resolve it. Found August 13 2026 by
// calling the export endpoints against the live site.
//
// The error message names the remedy: supply siteID and token when creating the
// store. That is Blobs' documented manual mode, and it is what this helper does.
//
// It falls back to automatic mode when the two variables are absent, so if
// Netlify's injection starts working, or this runs somewhere that already has a
// context, nothing here has to change. The fallback is also what keeps local
// development and any future Netlify CLI use working.
//
// Environment variables, both set in Netlify:
//   BLOBS_SITE_ID  the project's API ID
//   BLOBS_TOKEN    a Netlify personal access token
//
// The names deliberately avoid the NETLIFY_ prefix, which Netlify reserves and
// will not let you set as a project variable.
// ── Revised 2026-08-26 ──
//
// Manual mode stopped working. Every Blobs read on this site now fails, on
// production and on deploy previews alike, on stores that demonstrably exist:
// the Netlify UI lists org-diagnostic-leads holding a record while the function
// that reads it returns an error. The cause is not credentials. A fresh
// personal access token moved the failure from 401 to 400, and the site ID is a
// well formed project UUID, so the token is being accepted and the request
// itself is being refused.
//
// The two modes take different routes. Manual mode calls
// https://api.netlify.com/api/v1/blobs/... with the personal access token, and
// that is the request being refused. The injected context instead gives the
// client a per-deploy edge endpoint and a signed token, and never touches the
// API host at all. So the supported path avoids the failing request entirely.
//
// The order below is therefore reversed: the injected context first, manual
// only as a fallback. When no context is injected, which was the situation on
// 13 August 2026 that made manual mode necessary, behaviour is exactly what it
// was, so this cannot regress into a worse state than the current one.
//
// Both modes address the same site-scoped namespace, so this changes the route
// to the data and not the location of it. That mattered when choosing this
// remedy over supplying a region by hand: a guessed region would have pointed
// at a different namespace and returned an empty result that looked like
// success.
const { getStore } = require("@netlify/blobs");

// Netlify injects the context as base64 JSON, read by the client from
// globalThis.netlifyBlobsContext or NETLIFY_BLOBS_CONTEXT. Verified against
// getEnvironmentContext in @netlify/blobs 8.2.0 rather than assumed.
function hasInjectedContext() {
  return Boolean(globalThis.netlifyBlobsContext || process.env.NETLIFY_BLOBS_CONTEXT);
}

function blobStore(name) {
  if (hasInjectedContext()) {
    return getStore(name);
  }
  const siteID = process.env.BLOBS_SITE_ID;
  const token = process.env.BLOBS_TOKEN;
  if (siteID && token) {
    return getStore({ name, siteID, token });
  }
  // Neither route is available. This throws MissingBlobsEnvironmentError, which
  // is what it did before and is the honest outcome.
  return getStore(name);
}

// Which route a call would take. Diagnostics only, and the single most useful
// fact when a Blobs call fails, because the two routes fail for unrelated
// reasons and nothing in the error distinguishes them.
function blobsMode() {
  if (hasInjectedContext()) return "auto";
  return blobsConfigured() ? "manual" : "unconfigured";
}

// True when manual configuration is present. Used only for diagnostics, so a
// failure can be attributed to a missing variable rather than guessed at.
function blobsConfigured() {
  return Boolean(process.env.BLOBS_SITE_ID && process.env.BLOBS_TOKEN);
}

module.exports = { blobStore, blobsConfigured, blobsMode };
