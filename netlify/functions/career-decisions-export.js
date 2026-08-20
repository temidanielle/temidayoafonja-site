// Token-gated, READ-ONLY export of the Career Decision Evidence Check lead store.
//
// Access:  /.netlify/functions/career-decisions-export?token=YOUR_TOKEN
//          add &format=json for the full nested records.
//          Or send the token as a header:  Authorization: Bearer YOUR_TOKEN
//
// Uses the same RESEARCH_EXPORT_TOKEN env var as the three older exports, so
// there is one credential to hold rather than four.
//
// ── How this differs from the three existing export endpoints, deliberately ──
//
// 1. READ ONLY. The others accept &delete=THE_KEY to remove a record. This one
//    does not, and refuses the parameter loudly rather than ignoring it, so a
//    copied URL cannot quietly destroy a record. Deletion for a rights request
//    is a deliberate act and should not ride along on a reporting endpoint.
//
// 2. The token may be sent as a bearer header, not only as a query parameter.
//    docs/data-inventory.md section 8 flags the query-string form as the weak
//    point on this site, because query strings are written to server logs, proxy
//    logs and browser history. The query form still works, because it is what
//    makes the endpoint usable from a browser address bar, but the header is the
//    better habit and is what any script should use.
//
// 3. The token comparison is constant time. A timing-safe compare costs three
//    lines and removes a whole class of guessing attack against the one
//    credential that opens every lead store on this site.
//
// 4. Cache-Control: no-store on every response. This endpoint returns names,
//    email addresses and free text, and none of it should sit in an
//    intermediate cache.
//
// 5. A failure names its class. The others answer every storage fault with a
//    bare export_failed, which is undiagnosable from outside; this one returns
//    a short fault code, and treats a store that does not exist yet as an empty
//    export rather than a server error. See the classification block below.
//
// These five are confined to this file. The three existing exports are
// untouched, and nothing here changes how any record is written.
//
// Node 18+. See docs/forms-audit.md section 10 and docs/data-inventory.md.

const crypto = require("crypto");
const { blobStore, blobsConfigured } = require("../lib/blobs");

const STORE = "career-decisions-leads";

// Every response carries these. Text, never HTML, so a browser renders it as
// data rather than executing anything, and never cached.
const BASE_HEADERS = {
  "Cache-Control": "no-store",
  "X-Content-Type-Options": "nosniff",
  "X-Robots-Tag": "noindex, nofollow"
};

function headers(extra) {
  return Object.assign({}, BASE_HEADERS, extra || {});
}

// Constant-time string comparison. Returns false for a length mismatch without
// comparing further, which is the one thing length necessarily leaks anyway.
function tokenMatches(supplied, expected) {
  if (!expected || !supplied) return false;
  const a = Buffer.from(String(supplied));
  const b = Buffer.from(String(expected));
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

// Accepts "Authorization: Bearer xxx" or "?token=xxx", in that order of
// preference. Header names arrive lowercased from Netlify, but a direct
// invocation in a test may not, so both are read.
//
// Returns the source alongside the value. Which of the two the token came from
// is the difference between "the query parameter was ignored" and "the query
// parameter was wrong", and those need different fixes. It is also the one way
// to see that a header sent by a client, a proxy or an extension has quietly
// taken precedence over the token typed into the address bar.
//
// Both forms are trimmed. A credential does not have meaningful leading or
// trailing whitespace, and a value copied out of a settings screen very easily
// arrives with a trailing space or newline attached.
function suppliedToken(event) {
  const h = event.headers || {};
  const auth = h.authorization || h.Authorization || "";
  const m = /^Bearer\s+(.+)$/i.exec(String(auth).trim());
  if (m) return { value: m[1].trim(), source: "bearer" };
  const q = event.queryStringParameters || {};
  const t = String(q.token || "").trim();
  return t ? { value: t, source: "query" } : { value: "", source: "none" };
}

function csvCell(v) {
  if (v === null || v === undefined) return "";
  const s = typeof v === "object" ? JSON.stringify(v) : String(v);
  return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

// The record stores attribution as two nested objects, first and current. CSV
// has no nesting, so each touch is flattened to its own prefixed columns. The
// JSON format returns the record exactly as stored, nesting intact.
const TOUCH_FIELDS = [
  "utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term",
  "source", "video_slug", "landing_page", "referrer", "seen_at"
];

const COLUMNS = [
  "key",
  "received_at_cst", "received_at_utc",
  "first_name", "email", "current_decision",
  "delivery_consent", "delivery_consent_timestamp_client", "delivery_consent_timestamp_server", "delivery_policy_version",
  "guidance_consent", "guidance_consent_timestamp_client", "guidance_consent_timestamp_server", "guidance_policy_version",
  "youtube_tagged", "kit_subscriber_id"
].concat(
  TOUCH_FIELDS.map((f) => "first_" + f),
  TOUCH_FIELDS.map((f) => "current_" + f)
);

// Flattens one stored record into the flat shape the CSV columns expect. The
// stored record is never modified.
function flatten(rec) {
  const flat = Object.assign({}, rec);
  delete flat.attribution;
  const attr = (rec && rec.attribution) || {};
  for (const which of ["first", "current"]) {
    const touch = attr[which] || {};
    for (const f of TOUCH_FIELDS) flat[which + "_" + f] = touch[f];
  }
  return flat;
}

// ── Blobs failure classification ───────────────────────────────────────────
//
// Added 2026-08-20 after a Deploy Preview run of this endpoint returned a bare
// export_failed. The token was correct, so the fault was inside the storage
// read, but the response said only that something went wrong, and the Netlify
// log for that invocation had already rolled past by the time it was opened.
// An endpoint that can fail for four unrelated reasons and reports all four
// identically cannot be diagnosed from outside, so it now names the class.
//
// Nothing here is sensitive. A fault class, a store name and a boolean saying
// whether the two Blobs variables are present are all that is returned, and
// only to a caller who has already presented the token. No credential, no email
// address and no record content appears in any of these paths.

// @netlify/blobs raises BlobsInternalError when the Blobs API answers with a
// non-200. Which version puts the status on the error object and which only
// writes it into the message text has changed across releases, so both forms
// are read and an unrecognised error yields null rather than a wrong number.
function blobsErrorStatus(e) {
  if (!e) return null;
  if (typeof e.status === "number") return e.status;
  const m = /\b([1-5]\d\d)\b/.exec(String(e.message || ""));
  return m ? Number(m[1]) : null;
}

// A short, stable code for the fault class. Order matters: an absent pair of
// Blobs variables is the explanation for everything downstream of it, so it is
// checked first.
function blobsFailureCode(e) {
  if (!blobsConfigured()) return "blobs_not_configured";
  if (e && e.name === "MissingBlobsEnvironmentError") return "blobs_env_missing";
  const status = blobsErrorStatus(e);
  if (status) return "blobs_api_" + status;
  return "blobs_error";
}

exports.handler = async (event) => {
  // Read only, in the plainest sense: nothing but GET is answered at all.
  if (event.httpMethod && event.httpMethod !== "GET") {
    return { statusCode: 405, headers: headers({ "Content-Type": "text/plain" }), body: "Method Not Allowed" };
  }

  // ── Why a refusal now says which refusal it is ──
  //
  // Added 2026-08-20, alongside the storage fault codes, for the same reason:
  // one word covered three unrelated conditions. A token that authenticated on
  // one deploy and was refused on the next could mean the server has no token
  // at all, or that the value never reached the request, or that it reached it
  // and did not match, and those have three different fixes.
  //
  // None of this weakens the gate. The reason names the condition, never the
  // credential: no part of the expected or supplied token is returned, and
  // neither is its length, so nothing here helps anyone guess it. Saying that
  // the server has no token configured tells an attacker only that no token
  // would work, and it is the one condition an operator cannot otherwise see.
  const supplied = suppliedToken(event);

  if (!process.env.RESEARCH_EXPORT_TOKEN) {
    return {
      statusCode: 503,
      headers: headers({ "Content-Type": "application/json" }),
      body: JSON.stringify({
        error: "unauthorized",
        reason: "server_token_not_configured",
        message: "RESEARCH_EXPORT_TOKEN is not set in this deploy context."
      })
    };
  }

  if (!tokenMatches(supplied.value, process.env.RESEARCH_EXPORT_TOKEN)) {
    return {
      statusCode: 401,
      headers: headers({ "Content-Type": "application/json" }),
      body: JSON.stringify({
        error: "unauthorized",
        reason: supplied.source === "none" ? "no_token_supplied" : "token_mismatch",
        token_source: supplied.source
      })
    };
  }

  const q = event.queryStringParameters || {};

  // Refused rather than ignored. Somebody who copies a delete URL from one of
  // the older endpoints should be told plainly that it does nothing here,
  // rather than seeing a 200 and assuming the record is gone.
  if (q.delete) {
    return {
      statusCode: 400,
      headers: headers({ "Content-Type": "application/json" }),
      body: JSON.stringify({
        error: "read_only",
        message: "This endpoint cannot delete. Deleting a record is a deliberate act and is not available here."
      })
    };
  }

  let records = [];
  let storeExists = true;
  try {
    const store = blobStore(STORE);
    const listing = await store.list();
    for (const b of (listing && listing.blobs) || []) {
      const rec = await store.get(b.key, { type: "json" });
      if (rec) { rec.key = b.key; records.push(rec); }
    }
  } catch (e) {
    const code = blobsFailureCode(e);
    console.error("blobs " + STORE + " read failed:", code, "manual config present:", blobsConfigured(), e);

    // A store that has never had a blob written to it does not exist, and the
    // Blobs API answers 404 for it. That is an empty export, not a server
    // error. Reporting it as a 500 is precisely what made the first live run of
    // this endpoint impossible to interpret: a store with nothing in it and a
    // store that could not be reached produced the same response. Only 404 is
    // treated this way. Every other fault is still a 500.
    if (code !== "blobs_api_404") {
      return {
        statusCode: 500,
        headers: headers({ "Content-Type": "application/json" }),
        body: JSON.stringify({
          error: "export_failed",
          reason: code,
          store: STORE,
          blobs_manual_config: blobsConfigured()
        })
      };
    }
    storeExists = false;
    records = [];
  }

  records.sort((a, b) => String(b.received_at_utc).localeCompare(String(a.received_at_utc)));

  if ((q.format || "") === "json") {
    return {
      statusCode: 200,
      headers: headers({ "Content-Type": "application/json" }),
      body: JSON.stringify({ store: STORE, store_exists: storeExists, count: records.length, records }, null, 2)
    };
  }

  const rows = [COLUMNS.join(",")];
  for (const r of records) {
    const flat = flatten(r);
    rows.push(COLUMNS.map((c) => csvCell(flat[c])).join(","));
  }
  return {
    statusCode: 200,
    headers: headers({
      "Content-Type": "text/csv; charset=utf-8",
      "Content-Disposition": 'attachment; filename="career-decisions-leads.csv"'
    }),
    body: rows.join("\n")
  };
};
