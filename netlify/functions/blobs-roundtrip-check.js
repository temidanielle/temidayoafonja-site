// Token-gated proof that the connected zero-configuration Blobs path works.
//
// Netlify support case #1099659 established that these Lambda-compatible
// functions need connectLambda(event) before getStore(). Tests prove the call
// order against a stub; only a real deploy proves the round trip. This does
// that: connect, write, list, read, delete.
//
// ── Safety ──
//
// It uses its own store, "blobs-roundtrip-check", never a lead store. It writes
// one disposable key it generates itself and deletes only that key. **No
// subscriber record can be read, modified or deleted by this endpoint**, because
// it never names a store that holds one.
//
// It is gated on the same RESEARCH_EXPORT_TOKEN as the export endpoints, answers
// GET only, and returns booleans and counts. No record content, no context, no
// credential and no exception text ever appears in the response.
//
// It is refused outright in the production context, so it cannot run on the
// live site even with a valid token. It should still be deleted once the repair
// is merged and confirmed; it is not part of the site.
const crypto = require("crypto");
const { blobStore } = require("../lib/blobs");

const STORE = "blobs-roundtrip-check";

const BASE_HEADERS = {
  "Cache-Control": "no-store",
  "Content-Type": "application/json",
  "X-Content-Type-Options": "nosniff",
  "X-Robots-Tag": "noindex, nofollow"
};

function tokenMatches(supplied, expected) {
  if (!expected || !supplied) return false;
  const a = Buffer.from(String(supplied));
  const b = Buffer.from(String(expected));
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

function suppliedToken(event) {
  const h = event.headers || {};
  const auth = h.authorization || h.Authorization || "";
  const m = /^Bearer\s+(.+)$/i.exec(String(auth).trim());
  if (m) return m[1].trim();
  const q = event.queryStringParameters || {};
  return String(q.token || "").trim();
}

exports.handler = async (event) => {
  if (event.httpMethod && event.httpMethod !== "GET") {
    return { statusCode: 405, headers: BASE_HEADERS, body: JSON.stringify({ error: "method_not_allowed" }) };
  }
  // Never available on the live site, whatever token is presented. Netlify sets
  // CONTEXT to "production", "deploy-preview" or "branch-deploy". This endpoint
  // exists to verify a repair on a preview; it has no business running against
  // the production site, and a token alone should not be enough to let it.
  if (process.env.CONTEXT === "production") {
    return { statusCode: 404, headers: BASE_HEADERS, body: JSON.stringify({ error: "not_found" }) };
  }
  if (!process.env.RESEARCH_EXPORT_TOKEN) {
    return { statusCode: 503, headers: BASE_HEADERS, body: JSON.stringify({ error: "server_token_not_configured" }) };
  }
  if (!tokenMatches(suppliedToken(event), process.env.RESEARCH_EXPORT_TOKEN)) {
    return { statusCode: 401, headers: BASE_HEADERS, body: JSON.stringify({ error: "unauthorized" }) };
  }

  // Generated here, so the key cannot collide with anything and cannot be
  // chosen by the caller.
  const key = "roundtrip-" + (crypto.randomUUID ? crypto.randomUUID() : Date.now() + "-" + Math.random());
  const stamp = new Date().toISOString();

  const steps = { connected: false, wrote: false, listed: false, read_back: false, deleted: false, gone_after_delete: false };
  let listedCount = null;

  try {
    const store = blobStore(STORE, event);
    steps.connected = true;

    await store.setJSON(key, { diagnostic: true, written_at: stamp });
    steps.wrote = true;

    const listing = await store.list();
    const keys = ((listing && listing.blobs) || []).map((b) => b.key);
    listedCount = keys.length;
    steps.listed = keys.includes(key);

    const back = await store.get(key, { type: "json" });
    steps.read_back = Boolean(back && back.diagnostic === true && back.written_at === stamp);

    await store.delete(key);
    steps.deleted = true;

    const after = await store.get(key, { type: "json" });
    steps.gone_after_delete = after === null || after === undefined;
  } catch (e) {
    // The step map already shows how far it got. The exception itself is never
    // returned: a fault class is enough, and anything more risks disclosure.
    const reason = (e && (e.message === "blobs_context_missing" || e.message === "blobs_event_missing"))
      ? e.message
      : "blobs_error";
    console.error("blobs roundtrip failed at", JSON.stringify(steps), reason, e);
    return {
      statusCode: 500,
      headers: BASE_HEADERS,
      body: JSON.stringify({ ok: false, reason, steps, store: STORE })
    };
  }

  const ok = Object.values(steps).every(Boolean);
  return {
    statusCode: ok ? 200 : 500,
    headers: BASE_HEADERS,
    body: JSON.stringify({ ok, steps, store: STORE, keys_seen_in_store: listedCount })
  };
};
