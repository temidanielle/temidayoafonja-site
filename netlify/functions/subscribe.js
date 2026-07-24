// Netlify function: /.netlify/functions/subscribe
// Email gate handler. Subscribes the lead to the Kit (ConvertKit) sequence that
// matches their diagnostic quadrant, so the correct nurture sequence fires.
//
// Required env vars (Kit v3 sequence ids):
//   KIT_API_KEY                Kit (ConvertKit) API key
//   Org sequences (audit org mode + the organizational diagnostic):
//     KIT_SEQ_COMPOUNDING, KIT_SEQ_DEPTH_TRAP, KIT_SEQ_STAGNANT, KIT_SEQ_FRAGILE
//   Individual sequences (audit individual mode):
//     KIT_SEQ_IND_COMPOUNDING, KIT_SEQ_IND_DEPTH_TRAP, KIT_SEQ_IND_STAGNANT, KIT_SEQ_IND_FRAGILE
//   Optional tag ids (applied when present; tagging is skipped silently if unset):
//     KIT_TAG_INDIVIDUAL       tag id for "Individual" (all individual-mode takers)
//     KIT_TAG_PAPER_SAVE       tag id for "audit-paper-save" (paper fast-path takers)
//
// The client may also send a `fields` object (merged into Kit custom fields, e.g. the
// dated `audit_result` line so the reader's sequence email can echo their score).
//
// api.convertkit.com/v3/sequences/{id}/subscribe. Node 18+ (global fetch).

// Maps a quadrant to its env-var suffix. Accepts both the organizational
// diagnostic's display names ("Compounding", "Depth Trap", ...) and the /audit
// page's quadrant keys ("compound", "depth", "fragile", "stagnant"). Case-insensitive.
const QUADRANT_SUFFIX = {
  "compounding": "COMPOUNDING",
  "compound": "COMPOUNDING",
  "depth trap": "DEPTH_TRAP",
  "depth": "DEPTH_TRAP",
  "stagnant": "STAGNANT",
  "fragile": "FRAGILE"
};

// Some sources pin a single sequence regardless of quadrant (a lead-magnet
// acknowledgment/nurture sequence). The AI Capability Readiness Diagnostic's
// leads all go into one sequence rather than the four quadrant sequences.
const SEQ_BY_SOURCE = {
  "ai_readiness_diagnostic": "KIT_SEQ_AI_READINESS"
};

// Individuals (audit individual mode) get the plain sequences; org leaders
// (audit org mode, and the diagnostic which sends no mode) get the "— Org" ones.
function sequenceEnvName(quadrant, mode) {
  const suffix = QUADRANT_SUFFIX[(quadrant || "").toLowerCase().trim()];
  if (!suffix) return null;
  const isIndividual = (mode || "").toLowerCase().trim() === "individual";
  return isIndividual ? ("KIT_SEQ_IND_" + suffix) : ("KIT_SEQ_" + suffix);
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ error: "Method not allowed" }) };
  }
  if (!process.env.KIT_API_KEY) {
    return { statusCode: 500, body: JSON.stringify({ error: "Server is missing KIT_API_KEY" }) };
  }

  let email, org, quadrant, name, source, mode, tags, extraFields;
  try {
    const p = JSON.parse(event.body || "{}");
    email = (p.email || "").trim();
    org = (p.org || "").trim();
    quadrant = (p.quadrant || "").trim();
    name = (p.name || "").trim();
    source = (p.source || "").trim();
    mode = (p.mode || "").trim();
    tags = Array.isArray(p.tags) ? p.tags.map((t) => String(t).trim()).filter(Boolean) : [];
    extraFields = p.fields && typeof p.fields === "object" ? p.fields : {};
  } catch (e) {
    return { statusCode: 400, body: JSON.stringify({ error: "Invalid request body" }) };
  }

  if (!email || !email.includes("@")) {
    return { statusCode: 400, body: JSON.stringify({ error: "A valid email is required" }) };
  }

  const envName = SEQ_BY_SOURCE[source] || sequenceEnvName(quadrant, mode);
  const sequenceId = envName ? process.env[envName] : null;
  if (!sequenceId) {
    return { statusCode: 400, body: JSON.stringify({ error: "No sequence configured for source/quadrant/mode: " + (source || "-") + "/" + quadrant + "/" + (mode || "org") }) };
  }

  // Resolve requested tag names to Kit tag ids via env vars, when configured.
  // Known tags: "Individual" -> KIT_TAG_INDIVIDUAL, "audit-paper-save" -> KIT_TAG_PAPER_SAVE.
  // Missing env ids are skipped silently so tagging never blocks the subscribe.
  const TAG_ENV = { "individual": "KIT_TAG_INDIVIDUAL", "audit-paper-save": "KIT_TAG_PAPER_SAVE" };
  const tagIds = tags
    .map((t) => TAG_ENV[t.toLowerCase()])
    .filter(Boolean)
    .map((envName) => process.env[envName])
    .filter(Boolean);

  // Merge caller-supplied custom fields (e.g. the dated result line) over the base fields.
  const kitFields = Object.assign(
    { organization: org, quadrant: quadrant, source: source || undefined, mode: mode || undefined },
    extraFields
  );

  try {
    const subscribeBody = {
      api_key: process.env.KIT_API_KEY,
      email: email,
      first_name: name || undefined,
      fields: kitFields
    };
    if (tagIds.length) subscribeBody.tags = tagIds;
    const res = await fetch("https://api.convertkit.com/v3/sequences/" + encodeURIComponent(sequenceId) + "/subscribe", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(subscribeBody)
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      return { statusCode: 502, body: JSON.stringify({ error: "Kit subscribe failed", detail: data && data.message ? data.message : null }) };
    }
    return { statusCode: 200, headers: { "content-type": "application/json" }, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    return { statusCode: 502, body: JSON.stringify({ error: "Request to Kit failed" }) };
  }
};
