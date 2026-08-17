/**
 * Route-specific tests for /.netlify/functions/career-decisions-subscribe.
 *
 * Run:
 *   node --test tests/career-decisions-subscribe.test.mjs
 *
 * No npm install and no network. @netlify/blobs is intercepted below with an
 * in-memory stub, and global fetch is replaced per test, so the Kit API is
 * never actually called and no credential is ever needed to run this.
 *
 * These tests cover only the new function. Nothing here touches subscribe.js,
 * whose contract with diagnostic.html is deliberately unchanged.
 */
import test from "node:test";
import assert from "node:assert/strict";
import Module from "node:module";
import { createRequire } from "node:module";

/* ── In-memory Netlify Blobs stub ──────────────────────────────────────── */
const blobs = { stores: new Map(), failWrites: false, failReads: false };
function fakeStore(name) {
  if (!blobs.stores.has(name)) blobs.stores.set(name, new Map());
  const m = blobs.stores.get(name);
  return {
    async get(key) {
      if (blobs.failReads) throw new Error("stub read failure");
      return m.has(key) ? m.get(key) : null;
    },
    async setJSON(key, value) {
      if (blobs.failWrites) throw new Error("stub write failure");
      m.set(key, value);
    }
  };
}
const originalLoad = Module._load;
Module._load = function (request, parent, isMain) {
  if (request === "@netlify/blobs") {
    return { getStore: (arg) => fakeStore(typeof arg === "string" ? arg : arg.name) };
  }
  return originalLoad.apply(this, arguments);
};

const require_ = createRequire(import.meta.url);
const { handler } = require_("../netlify/functions/career-decisions-subscribe.js");

/* ── Helpers ───────────────────────────────────────────────────────────── */
const SECRET_VALUES = {
  KIT_API_KEY: "kit_test_key_MUST_NOT_LEAK",
  KIT_SEQ_CAREER_DECISIONS: "8801",
  KIT_TAG_CAREER_DECISIONS: "9901",
  KIT_TAG_YOUTUBE: "9902",
  RATE_LIMIT_SALT: "test-salt",
  BLOBS_SITE_ID: "site-test",
  BLOBS_TOKEN: "token_MUST_NOT_LEAK"
};

let kitCalls = [];

function configure(overrides = {}) {
  for (const k of Object.keys(SECRET_VALUES)) delete process.env[k];
  const env = { ...SECRET_VALUES, ...overrides };
  for (const [k, v] of Object.entries(env)) {
    if (v === undefined) continue;
    process.env[k] = v;
  }
}

function reset({ env = {}, kitStatus = 200, kitBody = { subscription: { subscriber: { id: 12345 } } } } = {}) {
  blobs.stores.clear();
  blobs.failWrites = false;
  blobs.failReads = false;
  kitCalls = [];
  configure(env);
  global.fetch = async (url, opts) => {
    kitCalls.push({ url: String(url), body: JSON.parse(opts.body) });
    return {
      ok: kitStatus >= 200 && kitStatus < 300,
      status: kitStatus,
      json: async () => kitBody
    };
  };
}

function payload(over = {}) {
  return {
    first_name: "Ada",
    email: "ada@example.com",
    current_decision: "Whether to take the platform role.",
    marketing_consent: true,
    consent_timestamp: "2026-08-17T12:00:00.000Z",
    policy_version: "2026-08-12",
    decision_reference: "",
    attribution: {},
    ...over
  };
}

function call(body, { method = "POST", ip = "203.0.113.7" } = {}) {
  return handler({
    httpMethod: method,
    headers: { "x-nf-client-connection-ip": ip },
    body: typeof body === "string" ? body : JSON.stringify(body)
  });
}

const parse = (res) => JSON.parse(res.body);

/* ── Method and body handling ──────────────────────────────────────────── */
test("rejects a GET", async () => {
  reset();
  const res = await call(payload(), { method: "GET" });
  assert.equal(res.statusCode, 405);
  assert.equal(kitCalls.length, 0);
});

test("answers a CORS preflight", async () => {
  reset();
  const res = await call("", { method: "OPTIONS" });
  assert.equal(res.statusCode, 204);
});

test("rejects a body that is not JSON", async () => {
  reset();
  const res = await call("not json at all");
  assert.equal(res.statusCode, 400);
  assert.equal(parse(res).error, "invalid_body");
  assert.equal(kitCalls.length, 0);
});

/* ── Configuration gate ────────────────────────────────────────────────── */
test("missing configuration returns 503 with the names of the missing variables and a checklist", async () => {
  reset({ env: { KIT_SEQ_CAREER_DECISIONS: undefined, KIT_TAG_YOUTUBE: undefined } });
  const res = await call(payload());
  assert.equal(res.statusCode, 503);
  const body = parse(res);
  assert.equal(body.error, "not_configured");
  assert.deepEqual(body.missing_env_vars.sort(), ["KIT_SEQ_CAREER_DECISIONS", "KIT_TAG_YOUTUBE"]);
  assert.ok(Array.isArray(body.checklist) && body.checklist.length >= 5);
  assert.equal(kitCalls.length, 0, "no Kit call may be attempted while unconfigured");
});

test("no response body ever contains a secret value", async () => {
  const bodies = [];
  reset({ env: { KIT_API_KEY: undefined } });
  bodies.push((await call(payload())).body);
  reset();
  bodies.push((await call(payload())).body);
  reset({ kitStatus: 401, kitBody: { message: "Authorization failed: kit_test_key_MUST_NOT_LEAK is invalid" } });
  bodies.push((await call(payload())).body);
  reset();
  bodies.push((await call(payload({ decision_reference: "bot" }))).body);

  for (const body of bodies) {
    for (const secret of [SECRET_VALUES.KIT_API_KEY, SECRET_VALUES.BLOBS_TOKEN, SECRET_VALUES.RATE_LIMIT_SALT]) {
      assert.ok(!body.includes(secret), `response leaked a secret value: ${body}`);
    }
  }
});

/* ── Honeypot ──────────────────────────────────────────────────────────── */
test("a filled honeypot is refused and never reaches Kit", async () => {
  reset();
  const res = await call(payload({ decision_reference: "https://spam.example" }));
  assert.equal(res.statusCode, 422);
  assert.equal(parse(res).error, "rejected");
  assert.equal(kitCalls.length, 0);
  assert.equal(blobs.stores.get("career-decisions-leads"), undefined);
});

/* ── Validation ────────────────────────────────────────────────────────── */
test("a missing first name is refused", async () => {
  reset();
  const res = await call(payload({ first_name: "   " }));
  assert.equal(res.statusCode, 400);
  assert.equal(parse(res).error, "first_name_required");
  assert.equal(kitCalls.length, 0);
});

test("an invalid email is refused", async () => {
  reset();
  for (const bad of ["", "ada", "ada@example", "ada @example.com"]) {
    const res = await call(payload({ email: bad }));
    assert.equal(res.statusCode, 400, `expected ${bad} to be refused`);
    assert.equal(parse(res).error, "valid_email_required");
  }
  assert.equal(kitCalls.length, 0);
});

/* ── Consent, fail closed ──────────────────────────────────────────────── */
test("consent must be a literal true", async () => {
  reset();
  for (const value of [false, undefined, null, "true", 1, "on", {}]) {
    const res = await call(payload({ marketing_consent: value }));
    assert.equal(res.statusCode, 400, `expected ${JSON.stringify(value)} to be refused`);
    assert.equal(parse(res).error, "consent_required");
  }
  assert.equal(kitCalls.length, 0, "no consent means no Kit call");
  assert.equal(blobs.stores.get("career-decisions-leads"), undefined, "no consent means no record");
});

/* ── The happy path ────────────────────────────────────────────────────── */
test("a consented submission subscribes through Kit and confirms only then", async () => {
  reset();
  const res = await call(payload());
  assert.equal(res.statusCode, 200);
  const body = parse(res);
  assert.equal(body.ok, true);
  assert.equal(body.durable_record, true);

  assert.equal(kitCalls.length, 1);
  const kit = kitCalls[0];
  assert.ok(kit.url.includes("/v3/sequences/8801/subscribe"), kit.url);
  assert.equal(kit.body.email, "ada@example.com");
  assert.equal(kit.body.first_name, "Ada");
  assert.equal(kit.body.fields.current_decision, "Whether to take the platform role.");
  assert.equal(kit.body.fields.consent_timestamp, "2026-08-17T12:00:00.000Z");
  assert.equal(kit.body.fields.policy_version, "2026-08-12");
  assert.equal(kit.body.fields.marketing_consent, "true");
});

test("the durable record is written only after Kit confirms, and carries both consent stamps", async () => {
  reset();
  await call(payload());
  const store = blobs.stores.get("career-decisions-leads");
  assert.equal(store.size, 1);
  const rec = [...store.values()][0];
  assert.equal(rec.email, "ada@example.com");
  assert.equal(rec.first_name, "Ada");
  assert.equal(rec.marketing_consent, true);
  assert.equal(rec.consent_timestamp_client, "2026-08-17T12:00:00.000Z");
  assert.ok(rec.consent_timestamp_server, "the server stamps its own receipt time");
  assert.equal(rec.policy_version, "2026-08-12");
  assert.equal(rec.kit_subscriber_id, 12345);
  assert.equal(rec.page, "/career-decisions");
});

test("a Kit failure is not reported as a subscription and writes no record", async () => {
  reset({ kitStatus: 422, kitBody: { message: "Sequence not found" } });
  const res = await call(payload());
  assert.equal(res.statusCode, 502);
  const body = parse(res);
  assert.equal(body.error, "subscribe_failed");
  assert.equal(body.ok, undefined);
  assert.ok(!res.body.includes("Sequence not found"), "Kit's message must not be echoed to the client");
  assert.ok(!res.body.includes("ada@example.com"), "the submitted address must not be echoed back");
  assert.equal(blobs.stores.get("career-decisions-leads"), undefined);
});

test("a network failure reaching Kit is not reported as a subscription", async () => {
  reset();
  global.fetch = async () => { throw new Error("socket hang up"); };
  const res = await call(payload());
  assert.equal(res.statusCode, 502);
  assert.equal(parse(res).error, "subscribe_failed");
});

test("a storage failure after a confirmed subscription still confirms, and says the record is missing", async () => {
  reset();
  blobs.failWrites = true;
  const res = await call(payload());
  assert.equal(res.statusCode, 200);
  const body = parse(res);
  assert.equal(body.ok, true, "the subscriber exists in Kit, so the visitor must not see an error");
  assert.equal(body.durable_record, false, "and the response must say the record was not stored");
});

test("with Blobs unconfigured the subscription still completes and durable_record is false", async () => {
  reset({ env: { BLOBS_SITE_ID: undefined, BLOBS_TOKEN: undefined } });
  const res = await call(payload());
  assert.equal(res.statusCode, 200);
  assert.equal(parse(res).durable_record, false);
});

/* ── Tagging ───────────────────────────────────────────────────────────── */
test("every subscriber gets the page tag", async () => {
  reset();
  await call(payload());
  assert.deepEqual(kitCalls[0].body.tags, ["9901"]);
});

test("the youtube tag is applied only for a real youtube arrival", async () => {
  const cases = [
    [{ source: "youtube" }, true],
    [{ utm_source: "youtube" }, true],
    [{ utm_source: "YouTube" }, true],
    [{ utm_source: "  youtube  " }, true],
    [{ utm_source: "twitter" }, false],
    [{ utm_campaign: "youtube-launch" }, false],
    [{ referrer: "https://www.youtube.com/watch?v=abc" }, false],
    [{}, false]
  ];
  for (const [attribution, expected] of cases) {
    reset();
    await call(payload({ attribution }));
    const tags = kitCalls[0].body.tags;
    assert.equal(
      tags.includes("9902"),
      expected,
      `attribution ${JSON.stringify(attribution)} should ${expected ? "" : "not "}be tagged youtube`
    );
  }
});

/* ── Attribution ───────────────────────────────────────────────────────── */
test("campaign values are passed through to Kit and stored, and absent ones stay empty", async () => {
  reset();
  await call(payload({
    attribution: {
      utm_source: "youtube",
      utm_medium: "video",
      utm_campaign: "capability-formation",
      utm_content: "end-card",
      utm_term: "stay-or-leave",
      source: "youtube",
      video: "read-what-the-work-built",
      referrer: "https://www.youtube.com/watch?v=abc123",
      landing_page: "/career-decisions?utm_source=youtube"
    }
  }));
  const f = kitCalls[0].body.fields;
  assert.equal(f.utm_source, "youtube");
  assert.equal(f.utm_medium, "video");
  assert.equal(f.utm_campaign, "capability-formation");
  assert.equal(f.utm_content, "end-card");
  assert.equal(f.utm_term, "stay-or-leave");
  assert.equal(f.video_slug, "read-what-the-work-built");
  assert.equal(f.referrer, "https://www.youtube.com/watch?v=abc123");

  const rec = [...blobs.stores.get("career-decisions-leads").values()][0];
  assert.equal(rec.attribution.video_slug, "read-what-the-work-built");
  assert.equal(rec.youtube_tagged, true);

  reset();
  await call(payload());
  assert.equal(kitCalls[0].body.fields.utm_source, "", "an unattributed visit stays unattributed");
  assert.equal(kitCalls[0].body.fields.video_slug, "");
});

test("oversized input is capped rather than stored whole", async () => {
  reset();
  await call(payload({
    first_name: "A".repeat(500),
    current_decision: "D".repeat(9000),
    attribution: { utm_campaign: "C".repeat(900) }
  }));
  assert.equal(kitCalls[0].body.first_name.length, 120);
  assert.equal(kitCalls[0].body.fields.current_decision.length, 2000);
  assert.equal(kitCalls[0].body.fields.utm_campaign.length, 300);
});

/* ── Rate limiting ─────────────────────────────────────────────────────── */
test("the eleventh request from one caller in an hour is refused", async () => {
  reset();
  for (let i = 0; i < 10; i++) {
    const res = await call(payload({ email: `ada${i}@example.com` }), { ip: "198.51.100.4" });
    assert.equal(res.statusCode, 200, `request ${i + 1} should have been allowed`);
  }
  const limited = await call(payload(), { ip: "198.51.100.4" });
  assert.equal(limited.statusCode, 429);
  assert.equal(parse(limited).error, "rate_limited");
  assert.equal(kitCalls.length, 10, "the refused request must not reach Kit");

  const other = await call(payload(), { ip: "198.51.100.99" });
  assert.equal(other.statusCode, 200, "a different caller is unaffected");
});

test("the rate-limit key is a hash, never the address", async () => {
  reset();
  await call(payload(), { ip: "198.51.100.4" });
  const keys = [...blobs.stores.get("career-decisions-rate").keys()];
  assert.equal(keys.length, 1);
  assert.match(keys[0], /^[0-9a-f]{64}$/, "the key must be a SHA-256 hex digest");
  assert.ok(!keys[0].includes("198.51.100.4"));
});

test("a storage failure turns the rate limit off rather than the endpoint", async () => {
  reset();
  blobs.failReads = true;
  const res = await call(payload());
  assert.equal(res.statusCode, 200, "a legitimate submission must still succeed");
});
