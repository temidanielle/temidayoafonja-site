// Netlify function: /.netlify/functions/subscribe
// Email gate handler. Subscribes the lead to the Kit (ConvertKit) sequence that
// matches their diagnostic quadrant, so the correct nurture sequence fires.
//
// Required env vars:
//   KIT_API_KEY            Kit (ConvertKit) API key
//   KIT_SEQ_COMPOUNDING    Kit sequence id for the Compounding quadrant
//   KIT_SEQ_DEPTH_TRAP     Kit sequence id for the Depth Trap quadrant
//   KIT_SEQ_STAGNANT       Kit sequence id for the Stagnant quadrant
//   KIT_SEQ_FRAGILE        Kit sequence id for the Fragile quadrant
//
// These are Kit v3 "sequence" ids (api.convertkit.com/v3/sequences/{id}/subscribe).
// To route by tag instead, swap the endpoint to /v3/tags/{id}/subscribe and point
// the four env vars at tag ids. Node 18+ (global fetch).

const SEQ_BY_QUADRANT = {
  "Compounding": "KIT_SEQ_COMPOUNDING",
  "Depth Trap": "KIT_SEQ_DEPTH_TRAP",
  "Stagnant": "KIT_SEQ_STAGNANT",
  "Fragile": "KIT_SEQ_FRAGILE"
};

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ error: "Method not allowed" }) };
  }
  if (!process.env.KIT_API_KEY) {
    return { statusCode: 500, body: JSON.stringify({ error: "Server is missing KIT_API_KEY" }) };
  }

  let email, org, quadrant;
  try {
    const p = JSON.parse(event.body || "{}");
    email = (p.email || "").trim();
    org = (p.org || "").trim();
    quadrant = (p.quadrant || "").trim();
  } catch (e) {
    return { statusCode: 400, body: JSON.stringify({ error: "Invalid request body" }) };
  }

  if (!email || !email.includes("@")) {
    return { statusCode: 400, body: JSON.stringify({ error: "A valid email is required" }) };
  }

  const envName = SEQ_BY_QUADRANT[quadrant];
  const sequenceId = envName ? process.env[envName] : null;
  if (!sequenceId) {
    return { statusCode: 400, body: JSON.stringify({ error: "No sequence configured for quadrant: " + quadrant }) };
  }

  try {
    const res = await fetch("https://api.convertkit.com/v3/sequences/" + encodeURIComponent(sequenceId) + "/subscribe", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        api_key: process.env.KIT_API_KEY,
        email: email,
        fields: { organization: org, quadrant: quadrant }
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
