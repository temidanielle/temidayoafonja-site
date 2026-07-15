// Netlify function: /.netlify/functions/subscribe
// Email gate handler. Subscribes the lead to the Kit (ConvertKit) sequence that
// matches their diagnostic quadrant, so the correct nurture sequence fires.
//
// Required env vars (Kit v3 sequence ids):
//   KIT_API_KEY                Kit (ConvertKit) API key
//   Org sequences (audit org mode + the institutional diagnostic):
//     KIT_SEQ_COMPOUNDING, KIT_SEQ_DEPTH_TRAP, KIT_SEQ_STAGNANT, KIT_SEQ_FRAGILE
//   Individual sequences (audit individual mode):
//     KIT_SEQ_IND_COMPOUNDING, KIT_SEQ_IND_DEPTH_TRAP, KIT_SEQ_IND_STAGNANT, KIT_SEQ_IND_FRAGILE
//
// api.convertkit.com/v3/sequences/{id}/subscribe. Node 18+ (global fetch).

// Maps a quadrant to its env-var suffix. Accepts both the institutional
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

  let email, org, quadrant, name, source, mode;
  try {
    const p = JSON.parse(event.body || "{}");
    email = (p.email || "").trim();
    org = (p.org || "").trim();
    quadrant = (p.quadrant || "").trim();
    name = (p.name || "").trim();
    source = (p.source || "").trim();
    mode = (p.mode || "").trim();
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

  try {
    const res = await fetch("https://api.convertkit.com/v3/sequences/" + encodeURIComponent(sequenceId) + "/subscribe", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        api_key: process.env.KIT_API_KEY,
        email: email,
        first_name: name || undefined,
        fields: { organization: org, quadrant: quadrant, source: source || undefined, mode: mode || undefined }
      })
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
