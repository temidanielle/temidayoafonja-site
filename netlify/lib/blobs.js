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
const { getStore } = require("@netlify/blobs");

function blobStore(name) {
  const siteID = process.env.BLOBS_SITE_ID;
  const token = process.env.BLOBS_TOKEN;
  if (siteID && token) {
    return getStore({ name, siteID, token });
  }
  return getStore(name);
}

// True when manual configuration is present. Used only for diagnostics, so a
// failure can be attributed to a missing variable rather than guessed at.
function blobsConfigured() {
  return Boolean(process.env.BLOBS_SITE_ID && process.env.BLOBS_TOKEN);
}

module.exports = { blobStore, blobsConfigured };
