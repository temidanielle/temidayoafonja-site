// Durable research capture for the Capability Formation Audit.
//
// This is intentionally SEPARATE from the existing Formspree -> Zapier -> Kit wire.
// The audit page still POSTs to Formspree exactly as before; this endpoint only
// stores an anonymizable research record in Netlify Blobs. It never touches Kit.
//
// One blob per submission (store: "audit-research"), so concurrent completions
// cannot clobber each other. Records where consent is false are STILL stored, but
// flagged so they can be excluded from any research aggregate.
const { getStore } = require("@netlify/blobs");

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
};

// Format an instant as America/Chicago (CST/CDT, DST-aware) "YYYY-MM-DD HH:MM:SS".
function chicagoStamp(d) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false
  }).formatToParts(d).reduce((o, p) => { o[p.type] = p.value; return o; }, {});
  // en-US hour24 can emit "24" at midnight; normalize to "00"
  const hh = parts.hour === "24" ? "00" : parts.hour;
  return `${parts.year}-${parts.month}-${parts.day} ${hh}:${parts.minute}:${parts.second}`;
}

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: CORS, body: JSON.stringify({ error: "Method Not Allowed" }) };
  }

  let data;
  try { data = JSON.parse(event.body || "{}"); }
  catch (e) { return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Invalid JSON" }) }; }

  const now = new Date();
  const consented = data.consent === true;

  const record = {
    // ── timestamps ────────────────────────────────────────────────
    received_at_cst: chicagoStamp(now),   // date + time, America/Chicago (CST/CDT)
    received_at_utc: now.toISOString(),
    timezone: "America/Chicago",
    client_completed_at: typeof data.client_completed_at === "string" ? data.client_completed_at : null,
    // ── consent ───────────────────────────────────────────────────
    consent: consented,
    consent_flag: consented ? "consented" : "no_consent_exclude_from_research",
    // ── audit result (computed state; questions/scoring unchanged) ─
    mode: data.mode || null,
    quadrant: data.quadrant || null,
    state: data.state || null,
    boundary: Array.isArray(data.boundary) ? data.boundary : null,
    paper: data.paper === true,
    scores: data.scores && typeof data.scores === "object" ? data.scores : null,
    responses: Array.isArray(data.responses) ? data.responses : null,
    // ── optional demographics (blank when not chosen) ─────────────
    industry: data.industry || "",
    role_level: data.role_level || "",
    years_experience: data.years_experience || "",
    organization_size: data.organization_size || "",
    // ── identity (only if the user gave it at the gate) ───────────
    name: data.name || "",
    email: data.email || ""
  };

  try {
    const store = getStore("audit-research");
    const id = (globalThis.crypto && crypto.randomUUID)
      ? crypto.randomUUID()
      : `${now.getTime()}-${Math.floor(Math.random() * 1e9)}`;
    // Key sorts chronologically and stays unique per submission.
    const key = `${now.toISOString().replace(/[:.]/g, "-")}__${id}`;
    await store.setJSON(key, record);
    return { statusCode: 200, headers: CORS, body: JSON.stringify({ ok: true, key }) };
  } catch (e) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: "storage_failed" }) };
  }
};
