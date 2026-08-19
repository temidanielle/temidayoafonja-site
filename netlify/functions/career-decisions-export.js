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
// These four are confined to this file. The three existing exports are
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
function suppliedToken(event) {
  const h = event.headers || {};
  const auth = h.authorization || h.Authorization || "";
  const m = /^Bearer\s+(.+)$/i.exec(String(auth).trim());
  if (m) return m[1].trim();
  const q = event.queryStringParameters || {};
  return q.token || "";
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

exports.handler = async (event) => {
  // Read only, in the plainest sense: nothing but GET is answered at all.
  if (event.httpMethod && event.httpMethod !== "GET") {
    return { statusCode: 405, headers: headers({ "Content-Type": "text/plain" }), body: "Method Not Allowed" };
  }

  if (!tokenMatches(suppliedToken(event), process.env.RESEARCH_EXPORT_TOKEN)) {
    return { statusCode: 401, headers: headers({ "Content-Type": "text/plain" }), body: "Unauthorized" };
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
  try {
    const store = blobStore(STORE);
    const listing = await store.list();
    for (const b of (listing && listing.blobs) || []) {
      const rec = await store.get(b.key, { type: "json" });
      if (rec) { rec.key = b.key; records.push(rec); }
    }
  } catch (e) {
    // The likeliest cause by far is the two Blobs variables being unset, which
    // is exactly the condition that left the older stores empty for months. Say
    // which it is in the log rather than leaving it to be guessed at.
    console.error("blobs " + STORE + " list failed. manual config present:", blobsConfigured(), e);
    return { statusCode: 500, headers: headers({ "Content-Type": "text/plain" }), body: "export_failed" };
  }

  records.sort((a, b) => String(b.received_at_utc).localeCompare(String(a.received_at_utc)));

  if ((q.format || "") === "json") {
    return {
      statusCode: 200,
      headers: headers({ "Content-Type": "application/json" }),
      body: JSON.stringify({ store: STORE, count: records.length, records }, null, 2)
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
