/**
 * Tests for /.netlify/functions/blobs-roundtrip-check.
 *
 * Run:  node --test tests/blobs-roundtrip-check.test.mjs
 *
 * @netlify/blobs is intercepted with an in-memory stub. No credential is needed
 * and no live store is touched.
 */
import test from "node:test";
import assert from "node:assert/strict";
import Module from "node:module";
import { createRequire } from "node:module";

const blobs = { stores: new Map(), calls: [], failAt: null };

function fakeStore(name) {
  if (!blobs.stores.has(name)) blobs.stores.set(name, new Map());
  const m = blobs.stores.get(name);
  const guard = (op) => { if (blobs.failAt === op) throw new Error("stub failure at " + op); };
  return {
    async list() { guard("list"); return { blobs: [...m.keys()].map((key) => ({ key })) }; },
    async get(key) { guard("get"); return m.has(key) ? JSON.parse(JSON.stringify(m.get(key))) : null; },
    async setJSON(key, value) { guard("setJSON"); m.set(key, value); },
    async delete(key) { guard("delete"); m.delete(key); }
  };
}

const originalLoad = Module._load;
Module._load = function (request) {
  if (request === "@netlify/blobs") {
    return {
      connectLambda: (event) => {
        blobs.calls.push("connectLambda");
        if (!event || !event.blobs) throw new Error("stub: no event.blobs");
      },
      getStore: (arg) => {
        blobs.calls.push("getStore");
        return fakeStore(typeof arg === "string" ? arg : arg.name);
      }
    };
  }
  return originalLoad.apply(this, arguments);
};

const require_ = createRequire(import.meta.url);
const { handler } = require_("../netlify/functions/blobs-roundtrip-check.js");

const TOKEN = "roundtrip-token-MUST-NOT-LEAK";
const CONTEXT = Buffer.from(JSON.stringify({ url: "https://blobs.example", token: "x" })).toString("base64");

function reset() {
  blobs.stores.clear();
  blobs.calls = [];
  blobs.failAt = null;
  process.env.RESEARCH_EXPORT_TOKEN = TOKEN;
}

// null is the sentinel for "no context"; undefined would hit the default.
function call({ token = TOKEN, blobsContext = CONTEXT, method = "GET" } = {}) {
  return handler({
    httpMethod: method,
    blobs: blobsContext,
    headers: token === null ? {} : { authorization: "Bearer " + token },
    queryStringParameters: {}
  });
}

test("a full round trip reports every step true", async () => {
  reset();
  const res = await call();
  assert.equal(res.statusCode, 200);
  const body = JSON.parse(res.body);
  assert.equal(body.ok, true);
  assert.deepEqual(body.steps, {
    connected: true, wrote: true, listed: true,
    read_back: true, deleted: true, gone_after_delete: true
  });
});

test("connectLambda runs before getStore", async () => {
  reset();
  await call();
  assert.ok(blobs.calls.indexOf("connectLambda") < blobs.calls.indexOf("getStore"));
});

test("it cleans up after itself, leaving the store empty", async () => {
  reset();
  await call();
  assert.equal(blobs.stores.get("blobs-roundtrip-check").size, 0,
    "the disposable key must not survive the check");
});

test("it only ever touches its own store, never a lead store", async () => {
  reset();
  await call();
  assert.deepEqual([...blobs.stores.keys()], ["blobs-roundtrip-check"]);
  const src = (await import("node:fs")).readFileSync("netlify/functions/blobs-roundtrip-check.js", "utf8");
  for (const lead of ["career-decisions-leads", "audit-research", "org-diagnostic-leads", "ai-readiness-leads"]) {
    assert.ok(!src.includes(lead), `must not name the ${lead} store`);
  }
});

test("a missing Blobs context fails closed and writes nothing", async () => {
  reset();
  const res = await call({ blobsContext: null });
  assert.equal(res.statusCode, 500);
  const body = JSON.parse(res.body);
  assert.equal(body.reason, "blobs_context_missing");
  assert.equal(body.steps.connected, false);
  assert.equal(body.steps.wrote, false);
});

test("a failure part-way through is reported as a partial step map", async () => {
  reset();
  blobs.failAt = "list";
  const body = JSON.parse((await call()).body);
  assert.equal(body.ok, false);
  assert.equal(body.steps.wrote, true);
  assert.equal(body.steps.listed, false);
});

test("it refuses without the token, and refuses a wrong one", async () => {
  reset();
  assert.equal((await call({ token: null })).statusCode, 401);
  assert.equal((await call({ token: "wrong" })).statusCode, 401);
  assert.equal(blobs.calls.length, 0, "no storage call before authentication");
});

test("it answers GET only", async () => {
  reset();
  assert.equal((await call({ method: "POST" })).statusCode, 405);
});

test("no response carries the token, a key, or record content", async () => {
  reset();
  const res = await call();
  assert.ok(!res.body.includes(TOKEN));
  // The store name legitimately contains "roundtrip". What must not appear is
  // the generated key, which carries a UUID after that prefix.
  assert.ok(!/roundtrip-[0-9a-f]{8}/.test(res.body), "the disposable key is not disclosed");
  assert.ok(!res.body.includes("written_at"), "no record content");
});

test("it is refused outright in the production context, token or not", async () => {
  reset();
  process.env.CONTEXT = "production";
  try {
    // A valid token must not be enough. This endpoint has no business running
    // against the live site.
    const res = await call();
    assert.equal(res.statusCode, 404);
    assert.equal(JSON.parse(res.body).error, "not_found");
    assert.equal(blobs.calls.length, 0, "no storage call in production, ever");
  } finally {
    delete process.env.CONTEXT;
  }
});

test("it runs on a deploy preview", async () => {
  reset();
  process.env.CONTEXT = "deploy-preview";
  try {
    assert.equal((await call()).statusCode, 200);
  } finally {
    delete process.env.CONTEXT;
  }
});
