/**
 * Route-specific tests for /.netlify/functions/career-decisions-export.
 *
 * Run:
 *   node --test tests/career-decisions-export.test.mjs
 *
 * No npm install and no network. @netlify/blobs is intercepted with an
 * in-memory stub, so no credential is needed and no live store is touched.
 *
 * These tests cover only the new export endpoint. The three older export
 * functions are deliberately untouched by this work and are not exercised here.
 */
import test from "node:test";
import assert from "node:assert/strict";
import Module from "node:module";
import { createRequire } from "node:module";

/* ── In-memory Netlify Blobs stub ──────────────────────────────────────── */
// listError lets a test choose the exact error the storage layer throws, which
// is what the fault-class tests below need. failList stays for the plain
// "something broke" case.
// calls records the order of SDK calls, which is what proves connectLambda
// ran before getStore. connectError lets a test make the connect itself fail.
const blobs = {
  stores: new Map(), failList: false, listError: null,
  lastGetStoreArg: null, getStoreError: null, connectError: null,
  calls: [], lastConnectEvent: null,
  ops: { list: 0, get: 0, setJSON: 0, delete: 0 }
};
function fakeStore(name) {
  if (!blobs.stores.has(name)) blobs.stores.set(name, new Map());
  const m = blobs.stores.get(name);
  return {
    async list() {
      blobs.ops.list += 1;
      if (blobs.listError) throw blobs.listError;
      if (blobs.failList) throw new Error("stub list failure");
      return { blobs: [...m.keys()].map((key) => ({ key })) };
    },
    async get(key) {
      blobs.ops.get += 1;
      if (blobs.listError) throw blobs.listError;
      if (blobs.failList) throw new Error("stub read failure");
      // Return a copy, so a mutation by the handler cannot reach the store.
      return m.has(key) ? JSON.parse(JSON.stringify(m.get(key))) : null;
    },
    async setJSON(key, value) { blobs.ops.setJSON += 1; m.set(key, value); },
    async delete(key) { blobs.ops.delete += 1; m.delete(key); }
  };
}
const originalLoad = Module._load;
Module._load = function (request) {
  if (request === "@netlify/blobs") {
    return {
      connectLambda: (event) => {
        blobs.calls.push("connectLambda");
        blobs.lastConnectEvent = event;
        if (blobs.connectError) throw blobs.connectError;
        // The real one throws on an absent context; the stub must too, or the
        // fail-closed behaviour would only be tested in the helper.
        if (!event || !event.blobs) throw new Error("stub: no event.blobs");
      },
      getStore: (arg) => {
        blobs.calls.push("getStore");
        blobs.lastGetStoreArg = arg;
        if (blobs.getStoreError) throw blobs.getStoreError;
        return fakeStore(typeof arg === "string" ? arg : arg.name);
      }
    };
  }
  return originalLoad.apply(this, arguments);
};

const require_ = createRequire(import.meta.url);
const { handler } = require_("../netlify/functions/career-decisions-export.js");

/* ── Helpers ───────────────────────────────────────────────────────────── */
const TOKEN = "export-token-MUST-NOT-LEAK";
const STORE = "career-decisions-leads";

function record(over = {}) {
  return {
    received_at_cst: "2026-08-19 09:15:00",
    received_at_utc: "2026-08-19T14:15:00.000Z",
    timezone: "America/Chicago",
    form: "career-decision-evidence-check",
    page: "/career-decisions",
    first_name: "Ada",
    email: "ada@example.com",
    current_decision: "Whether to take the platform role.",
    delivery_consent: true,
    delivery_consent_timestamp_client: "2026-08-19T14:14:58.000Z",
    delivery_consent_timestamp_server: "2026-08-19T14:15:00.000Z",
    delivery_policy_version: "2026-08-18",
    guidance_consent: false,
    guidance_consent_timestamp_client: "",
    guidance_consent_timestamp_server: "",
    guidance_policy_version: "",
    attribution: {
      first: {
        utm_source: "youtube", utm_medium: "video", utm_campaign: "launch",
        utm_content: "end-card", utm_term: "", source: "youtube",
        video_slug: "episode-01", landing_page: "/career-decisions?v=episode-01",
        referrer: "https://www.youtube.com/watch?v=abc", seen_at: "2026-08-19T14:10:00.000Z"
      },
      current: {
        utm_source: "youtube", utm_medium: "video", utm_campaign: "followup",
        utm_content: "", utm_term: "", source: "youtube",
        video_slug: "episode-04", landing_page: "/career-decisions?v=episode-04",
        referrer: "", seen_at: "2026-08-19T14:14:00.000Z"
      }
    },
    youtube_tagged: true,
    kit_sequence_env: "KIT_SEQ_CAREER_DECISIONS",
    kit_subscriber_id: 12345,
    ...over
  };
}

function seed(records) {
  blobs.stores.clear();
  const store = fakeStore(STORE);
  for (const [key, rec] of Object.entries(records)) store.setJSON(key, rec);
}

function reset({ token = TOKEN, seedRecords = null } = {}) {
  blobs.failList = false;
  blobs.listError = null;
  // The manual Blobs configuration is present in every test unless a test
  // deliberately removes it. Without this, every storage fault would classify
  // as blobs_not_configured and the other fault classes would never be reached.
  // No BLOBS_SITE_ID or BLOBS_TOKEN anywhere. The manual path is gone.
  blobs.getStoreError = null;
  blobs.connectError = null;
  blobs.calls = [];
  blobs.lastConnectEvent = null;
  // No injected context by default, so the default route is manual, which is
  // what production and the deploy previews have been using.
  delete process.env.NETLIFY_BLOBS_CONTEXT;
  blobs.lastGetStoreArg = null;
  // null is the sentinel for "the server has no token configured". undefined
  // would hit the default parameter above and silently set the real token,
  // which is exactly the mistake this comment exists to prevent repeating.
  if (token === null) delete process.env.RESEARCH_EXPORT_TOKEN;
  else process.env.RESEARCH_EXPORT_TOKEN = token;
  seed(seedRecords || { "2026-08-19T14-15-00-000Z__aaa": record() });
  // After seeding: seed() writes through the fake store, so zeroing earlier
  // would count the fixture's own write against the handler.
  blobs.ops = { list: 0, get: 0, setJSON: 0, delete: 0 };
}

// A Lambda event shaped like the real one: the Blobs context arrives as
// base64 JSON on event.blobs, never in the environment.
const CONTEXT = Buffer.from(JSON.stringify({ url: "https://blobs.example", token: "x" })).toString("base64");

function call({ token = null, bearer = null, query = {}, method = "GET", blobsContext = CONTEXT } = {}) {
  // null means "Netlify attached no context". undefined would hit the default
  // above and quietly supply one, so the fail-closed path would never be tested.
  const q = Object.assign({}, query);
  if (token !== null) q.token = token;
  return handler({
    httpMethod: method,
    blobs: blobsContext,
    headers: bearer === null ? {} : { authorization: "Bearer " + bearer },
    queryStringParameters: q
  });
}

function res_includes(body, needle) {
  return JSON.stringify(body).includes(needle);
}

/* ── Authentication ────────────────────────────────────────────────────── */
test("refuses a request with no token", async () => {
  reset();
  const res = await call();
  assert.equal(res.statusCode, 401);
  const body = JSON.parse(res.body);
  assert.equal(body.error, "unauthorized");
  assert.equal(body.reason, "no_token_supplied");
  assert.equal(body.token_source, "none");
});

test("refuses a wrong token, including one that is a prefix of the real one", async () => {
  reset();
  for (const bad of ["", "wrong", TOKEN.slice(0, -1), TOKEN + "x", TOKEN.toUpperCase()]) {
    const res = await call({ token: bad });
    assert.equal(res.statusCode, 401, `expected ${JSON.stringify(bad)} to be refused`);
  }
});

test("refuses everything when the server has no token configured", async () => {
  reset({ token: null });
  // An unset expected token must never mean "let everyone in", including a
  // caller who supplies an empty token to match an empty expectation.
  for (const attempt of [{}, { token: "" }, { token: TOKEN }, { bearer: TOKEN }]) {
    const res = await call(attempt);
    assert.equal(res.statusCode, 503, "refused, and named as a server-side gap");
    assert.equal(JSON.parse(res.body).reason, "server_token_not_configured");
  }
});

test("a refusal never carries any part of the token, or its length", async () => {
  reset();
  for (const attempt of [{}, { token: "wrong" }, { token: TOKEN.slice(0, -1) }, { bearer: "wrong" }]) {
    const res = await call(attempt);
    const body = res.body;
    assert.ok(!body.includes(TOKEN), "the expected token never appears");
    assert.ok(!body.includes(TOKEN.slice(0, 8)), "no prefix of it appears either");
    assert.ok(!/length|chars|\b\d{2,}\b/.test(body), "no length is disclosed: " + body);
  }
});

test("a wrong token is named as a mismatch, and says which form carried it", async () => {
  reset();
  const viaQuery = await call({ token: "wrong" });
  assert.equal(viaQuery.statusCode, 401);
  assert.equal(JSON.parse(viaQuery.body).reason, "token_mismatch");
  assert.equal(JSON.parse(viaQuery.body).token_source, "query");

  const viaHeader = await call({ bearer: "wrong" });
  assert.equal(JSON.parse(viaHeader.body).token_source, "bearer");
});

test("a header reports itself as the source even when a query token was also sent", async () => {
  reset();
  // The failure mode this exists to make visible: a client, proxy or extension
  // attaches an Authorization header, it takes precedence, and the token typed
  // into the address bar is never consulted.
  const res = await handler({
    httpMethod: "GET",
    blobs: CONTEXT,
    headers: { authorization: "Bearer wrong" },
    queryStringParameters: { token: TOKEN }
  });
  assert.equal(res.statusCode, 401);
  assert.equal(JSON.parse(res.body).token_source, "bearer");
});

test("surrounding whitespace on a copied token does not refuse it", async () => {
  reset();
  // A value copied out of a settings screen arrives with a trailing space or
  // newline far more often than anyone expects.
  for (const padded of [" " + TOKEN, TOKEN + " ", "\n" + TOKEN + "\n", "  " + TOKEN + "\t"]) {
    const res = await call({ token: padded });
    assert.equal(res.statusCode, 200, `expected ${JSON.stringify(padded)} to be accepted`);
  }
});

test("a token that is only whitespace counts as no token at all", async () => {
  reset();
  const res = await call({ token: "   " });
  assert.equal(JSON.parse(res.body).reason, "no_token_supplied");
});

test("whitespace inside the token is still a mismatch", async () => {
  reset();
  // A "+" in a query string decodes to a space, so a token containing one and
  // sent in the query would arrive altered. That must fail, not be repaired.
  const res = await call({ token: TOKEN.replace(/-/, " ") });
  assert.equal(res.statusCode, 401);
  assert.equal(JSON.parse(res.body).reason, "token_mismatch");
});

test("accepts the correct token as a query parameter", async () => {
  reset();
  const res = await call({ token: TOKEN });
  assert.equal(res.statusCode, 200);
});

test("accepts the correct token as a bearer header", async () => {
  reset();
  const res = await call({ bearer: TOKEN });
  assert.equal(res.statusCode, 200);
  const lower = await handler({ httpMethod: "GET", blobs: CONTEXT, headers: { Authorization: "Bearer " + TOKEN }, queryStringParameters: {} });
  assert.equal(lower.statusCode, 200, "a capitalised header name works too");
});

test("the header wins over a wrong query parameter, and a wrong header is not rescued by a right query", async () => {
  reset();
  const good = await handler({ httpMethod: "GET", blobs: CONTEXT, headers: { authorization: "Bearer " + TOKEN }, queryStringParameters: { token: "wrong" } });
  assert.equal(good.statusCode, 200);
  const bad = await handler({ httpMethod: "GET", blobs: CONTEXT, headers: { authorization: "Bearer wrong" }, queryStringParameters: { token: TOKEN } });
  assert.equal(bad.statusCode, 401, "a supplied header is the token, and a bad one is not silently ignored");
});

/* ── Read only ─────────────────────────────────────────────────────────── */
test("refuses any method other than GET", async () => {
  reset();
  for (const method of ["POST", "PUT", "DELETE", "PATCH"]) {
    const res = await call({ token: TOKEN, method });
    assert.equal(res.statusCode, 405, `expected ${method} to be refused`);
  }
});

test("refuses a delete parameter loudly, and deletes nothing", async () => {
  reset();
  const res = await call({ token: TOKEN, query: { delete: "2026-08-19T14-15-00-000Z__aaa" } });
  assert.equal(res.statusCode, 400);
  assert.equal(JSON.parse(res.body).error, "read_only");
  assert.equal(blobs.stores.get(STORE).size, 1, "the record must still be there");
});

test("a successful export never mutates the store", async () => {
  reset();
  const before = JSON.stringify([...blobs.stores.get(STORE).entries()]);
  await call({ token: TOKEN });
  await call({ token: TOKEN, query: { format: "json" } });
  assert.equal(JSON.stringify([...blobs.stores.get(STORE).entries()]), before);
});

/* ── Response hygiene ──────────────────────────────────────────────────── */
test("no response is cacheable, and none is indexable", async () => {
  reset();
  const responses = [
    await call(),
    await call({ token: TOKEN }),
    await call({ token: TOKEN, query: { format: "json" } }),
    await call({ token: TOKEN, query: { delete: "x" } }),
    await call({ token: TOKEN, method: "POST" })
  ];
  for (const res of responses) {
    assert.equal(res.headers["Cache-Control"], "no-store");
    assert.equal(res.headers["X-Robots-Tag"], "noindex, nofollow");
    assert.equal(res.headers["X-Content-Type-Options"], "nosniff");
  }
});

test("no response body ever contains the export token", async () => {
  reset();
  const bodies = [
    (await call()).body,
    (await call({ token: "wrong" })).body,
    (await call({ token: TOKEN })).body,
    (await call({ token: TOKEN, query: { format: "json" } })).body,
    (await call({ token: TOKEN, query: { delete: "x" } })).body
  ];
  for (const body of bodies) assert.ok(!String(body).includes(TOKEN), "a response leaked the token");
});

/* ── CSV output ────────────────────────────────────────────────────────── */
test("the CSV carries a header row and one row per record", async () => {
  reset();
  const res = await call({ token: TOKEN });
  assert.match(res.headers["Content-Type"], /text\/csv/);
  assert.match(res.headers["Content-Disposition"], /career-decisions-leads\.csv/);
  const rows = res.body.split("\n");
  assert.equal(rows.length, 2);
  assert.ok(rows[0].startsWith("key,received_at_cst,received_at_utc,first_name,email"));
});

test("both attribution touches are flattened into their own columns", async () => {
  reset();
  const res = await call({ token: TOKEN });
  const [head, row] = res.body.split("\n");
  const cols = head.split(",");
  const cells = row.split(",");
  const at = (name) => cells[cols.indexOf(name)];

  assert.ok(cols.includes("first_video_slug") && cols.includes("current_video_slug"));
  assert.equal(at("first_video_slug"), "episode-01");
  assert.equal(at("current_video_slug"), "episode-04");
  assert.equal(at("first_utm_campaign"), "launch");
  assert.equal(at("current_utm_campaign"), "followup");
  assert.equal(at("first_seen_at"), "2026-08-19T14:10:00.000Z");
  // The nested object itself must not survive into a column.
  assert.ok(!cols.includes("attribution"));
  assert.ok(!res.body.includes('{"first"'));
});

test("both consent records appear, and an absent guidance consent reads as empty", async () => {
  reset();
  const res = await call({ token: TOKEN });
  const [head, row] = res.body.split("\n");
  const cols = head.split(",");
  const cells = row.split(",");
  const at = (name) => cells[cols.indexOf(name)];
  assert.equal(at("delivery_consent"), "true");
  assert.equal(at("delivery_policy_version"), "2026-08-18");
  assert.equal(at("guidance_consent"), "false");
  assert.equal(at("guidance_consent_timestamp_client"), "");
  assert.equal(at("guidance_policy_version"), "");
});

test("free text containing commas, quotes and newlines does not break the CSV", async () => {
  reset({ seedRecords: { k1: record({ current_decision: 'Stay, go, or "reshape"?\nA second line.' }) } });
  const res = await call({ token: TOKEN });
  const head = res.body.split("\n")[0];
  const cols = head.split(",");
  // The quoted cell contains a newline, so the row count alone cannot be
  // asserted. Parse the field back out instead.
  const body = res.body.slice(head.length + 1);
  const quoted = /"((?:[^"]|"")*)"/.exec(body);
  assert.ok(quoted, "the dangerous cell should have been quoted");
  assert.equal(quoted[1].replace(/""/g, '"'), 'Stay, go, or "reshape"?\nA second line.');
  assert.ok(cols.includes("current_decision"));
});

test("records are returned newest first", async () => {
  reset({ seedRecords: {
    older: record({ received_at_utc: "2026-08-01T00:00:00.000Z", email: "older@example.com" }),
    newer: record({ received_at_utc: "2026-08-19T00:00:00.000Z", email: "newer@example.com" })
  } });
  const res = await call({ token: TOKEN });
  const rows = res.body.split("\n");
  assert.ok(rows[1].includes("newer@example.com"));
  assert.ok(rows[2].includes("older@example.com"));
});

test("an empty store returns a header row and nothing else", async () => {
  reset({ seedRecords: {} });
  const res = await call({ token: TOKEN });
  assert.equal(res.statusCode, 200);
  assert.equal(res.body.split("\n").length, 1);
});

/* ── JSON output ───────────────────────────────────────────────────────── */
test("the JSON format returns the records with their nesting intact", async () => {
  reset();
  const res = await call({ token: TOKEN, query: { format: "json" } });
  assert.match(res.headers["Content-Type"], /application\/json/);
  const body = JSON.parse(res.body);
  assert.equal(body.store, "career-decisions-leads");
  assert.equal(body.count, 1);
  assert.equal(body.records[0].attribution.first.video_slug, "episode-01");
  assert.equal(body.records[0].attribution.current.video_slug, "episode-04");
  assert.equal(body.records[0].key, "2026-08-19T14-15-00-000Z__aaa");
});

/* ── Failure handling ──────────────────────────────────────────────────── */
//
// These exist because the first live run of this endpoint returned a bare
// export_failed with a correct token, and there was no way to tell from the
// response which of four unrelated conditions had occurred.

// A Blobs API error exactly as @netlify/blobs 8.x builds it. Verified against
// the client source: the constructor takes the x-nf-error response header when
// the API sends one, falls back to "<status> status code" when it does not, and
// appends ", ID: <request id>" when x-nf-request-id is present. The status also
// appears on the error object on some releases, hence onObject.
function blobsApiError(status, { detail = null, requestId = null, onObject = false } = {}) {
  let inner = detail || status + " status code";
  if (requestId) inner += ", ID: " + requestId;
  const e = new Error("Netlify Blobs has generated an internal error (" + inner + ")");
  e.name = "BlobsInternalError";
  if (onObject) e.status = status;
  return e;
}


test("a storage failure is a 500 that says nothing about the store's contents", async () => {
  reset();
  blobs.failList = true;
  const res = await call({ token: TOKEN });
  assert.equal(res.statusCode, 500);
  const body = JSON.parse(res.body);
  assert.equal(body.error, "export_failed");
  assert.ok(!res.body.includes("ada@example.com"));
  assert.ok(!res.body.includes(TOKEN));
});

test("an unrecognised storage failure classifies as blobs_error", async () => {
  reset();
  blobs.listError = new Error("something unexpected");
  const res = await call({ token: TOKEN });
  assert.equal(JSON.parse(res.body).reason, "blobs_error");
});

/* ── The upstream detail ───────────────────────────────────────────────── */
//
// Netlify explains some refusals in an x-nf-error header. That text is the only
// thing separating one 400 from another, and it is otherwise visible only in a
// function log.

test("a bare status carries the request ID, which is what Netlify support needs", async () => {
  reset();
  blobs.listError = blobsApiError(400, { requestId: "01JABCDEF" });
  const body = JSON.parse((await call({ token: TOKEN })).body);
  assert.equal(body.reason, "blobs_api_400");
  assert.equal(body.detail, "400 status code, ID: 01JABCDEF");
});

test("only a BlobsInternalError has its message returned", async () => {
  reset();
  // An arbitrary error's message is unconstrained, so it is never echoed.
  blobs.listError = new Error("connection to 10.0.0.4 failed for ada@example.com");
  const body = JSON.parse((await call({ token: TOKEN })).body);
  assert.equal(body.detail, null);
  assert.ok(!res_includes(body, "ada@example.com"));
});

test("a long upstream string is truncated", async () => {
  reset();
  blobs.listError = blobsApiError(400, { detail: "x".repeat(5000) });
  const body = JSON.parse((await call({ token: TOKEN })).body);
  assert.equal(body.detail.length, 200);
});

test("the export token is redacted from an upstream string too", async () => {
  reset();
  blobs.listError = blobsApiError(400, { detail: "saw " + TOKEN + " in the request" });
  const res = await call({ token: TOKEN });
  assert.ok(!res.body.includes(TOKEN));
});

/* ── Which route the call took ─────────────────────────────────────────── */

test("the failure body names the store so the fault is attributable", async () => {
  reset();
  blobs.failList = true;
  const res = await call({ token: TOKEN });
  assert.equal(JSON.parse(res.body).store, "career-decisions-leads");
});

/* ── The Lambda connect contract ───────────────────────────────────────── */
//
// Netlify support case #1099659, 2026-09-15: these functions run in Lambda
// compatibility mode, the Blobs context arrives on event.blobs rather than in
// the environment, and connectLambda(event) must run before getStore(). These
// tests pin that, and pin the two defects the same investigation exposed in
// this file's own diagnostics.

test("connectLambda runs before getStore, every time", async () => {
  reset();
  await call({ token: TOKEN });
  const first = blobs.calls.indexOf("connectLambda");
  const store = blobs.calls.indexOf("getStore");
  assert.ok(first !== -1, "connectLambda must be called at all");
  assert.ok(store !== -1, "getStore must be called at all");
  assert.ok(first < store, `connectLambda must precede getStore, got ${blobs.calls.join(" then ")}`);
});

test("the event handed to connectLambda is the invocation's own", async () => {
  reset();
  const marker = Buffer.from(JSON.stringify({ url: "https://marker", token: "t" })).toString("base64");
  await call({ token: TOKEN, blobsContext: marker });
  assert.equal(blobs.lastConnectEvent.blobs, marker,
    "a stale or synthesised event would connect to the wrong deploy");
});

test("the store is asked for by name only, with no credentials", async () => {
  reset();
  await call({ token: TOKEN });
  // A string is the zero-configuration form. An object carrying siteID and
  // token would be the manual path this repair removed.
  assert.equal(typeof blobs.lastGetStoreArg, "string");
  assert.equal(blobs.lastGetStoreArg, "career-decisions-leads");
});

test("a missing Blobs context fails closed, and says so", async () => {
  reset();
  const res = await call({ token: TOKEN, blobsContext: null });
  assert.equal(res.statusCode, 500);
  const body = JSON.parse(res.body);
  assert.equal(body.reason, "blobs_context_missing");
  assert.equal(body.blobs_context_present, false);
  // No silent fallback: nothing may be read or written without a context.
  assert.equal(blobs.ops.list, 0);
  assert.equal(blobs.ops.get, 0);
});

test("no manual credential path exists to fall back to", async () => {
  reset();
  process.env.BLOBS_SITE_ID = "should-be-ignored";
  process.env.BLOBS_TOKEN = "should-be-ignored";
  try {
    const res = await call({ token: TOKEN, blobsContext: null });
    // Even with both variables set, an absent context is still a hard failure.
    assert.equal(res.statusCode, 500);
    assert.equal(JSON.parse(res.body).reason, "blobs_context_missing");
  } finally {
    delete process.env.BLOBS_SITE_ID;
    delete process.env.BLOBS_TOKEN;
  }
});

/* ── The fabricated-status defect ──────────────────────────────────────── */
//
// blobsErrorStatus used to scan any message for the first three-digit number.
// Netlify confirmed that is where the reported blobs_api_400 came from: their
// API never received a request. These are the messages that used to lie.

test("a plain error mentioning 300, 400 or 404 is never a Blobs API status", async () => {
  for (const message of [
    "connect ECONNREFUSED 400",
    "timeout of 300 ms exceeded",
    "no route to host 404",
    "site 6a90-400-abc is unavailable",
    "404"
  ]) {
    reset();
    blobs.listError = new Error(message);
    const body = JSON.parse((await call({ token: TOKEN })).body);
    assert.equal(body.reason, "blobs_error",
      `"${message}" must not be classified as an API status, got ${body.reason}`);
  }
});

test("a status is read only from a structured source", async () => {
  reset();
  blobs.listError = blobsApiError(500, { onObject: true });
  assert.equal(JSON.parse((await call({ token: TOKEN })).body).reason, "blobs_api_500",
    "a numeric status property is structured and is trusted");

  reset();
  blobs.listError = blobsApiError(503);
  assert.equal(JSON.parse((await call({ token: TOKEN })).body).reason, "blobs_api_503",
    "the exact anchored BlobsInternalError shape is trusted");

  reset();
  // Same words, but a plain Error rather than one BlobsInternalError raised.
  blobs.listError = new Error("Netlify Blobs has generated an internal error (401 status code)");
  assert.equal(JSON.parse((await call({ token: TOKEN })).body).reason, "blobs_error",
    "the message shape alone is not a structured source");
});

/* ── The false-success defect ──────────────────────────────────────────── */

test("no error can produce a successful empty export", async () => {
  for (const err of [
    new Error("404"),
    new Error("not found 404"),
    blobsApiError(404),
    blobsApiError(404, { onObject: true }),
    Object.assign(new Error("nope"), { status: 404 })
  ]) {
    reset();
    blobs.listError = err;
    const res = await call({ token: TOKEN, query: { format: "json" } });
    assert.equal(res.statusCode, 500,
      "a storage fault must never be reported as an empty but successful export");
    assert.equal(JSON.parse(res.body).error, "export_failed");
  }
});

test("a genuinely empty store is still a normal empty export", async () => {
  // The legitimate empty case comes from a successful list, not from an error.
  reset({ seedRecords: {} });
  const res = await call({ token: TOKEN, query: { format: "json" } });
  assert.equal(res.statusCode, 200);
  assert.equal(JSON.parse(res.body).count, 0);
});
