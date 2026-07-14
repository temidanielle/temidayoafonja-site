// Durable lead capture for the AI Capability Readiness Diagnostic (self-serve).
//
// Stores one Netlify Blob per lead (store: "ai-readiness-leads"). This is the
// record you control; the page ALSO posts to Formspree for the email ping.
// No Kit here: follow-up on these leads is personal, not an automated sequence.
const { getStore } = require("@netlify/blobs");

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
};

// America/Chicago (CST/CDT, DST-aware) "YYYY-MM-DD HH:MM:SS".
function chicagoStamp(d) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false
  }).formatToParts(d).reduce((o, p) => { o[p.type] = p.value; return o; }, {});
  const hh = parts.hour === "24" ? "00" : parts.hour;
  return `${parts.year}-${parts.month}-${parts.day} ${hh}:${parts.minute}:${parts.second}`;
}

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: CORS, body: JSON.stringify({ error: "Method Not Allowed" }) };
  }

  let d;
  try { d = JSON.parse(event.body || "{}"); }
  catch (e) { return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Invalid JSON" }) }; }

  if (!d.email || String(d.email).indexOf("@") < 0) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "A valid email is required" }) };
  }

  const now = new Date();
  const record = {
    received_at_cst: chicagoStamp(now),
    received_at_utc: now.toISOString(),
    timezone: "America/Chicago",
    email: d.email || "",
    organization: d.org || "",
    sector: d.sector || "",
    headcount: d.headcount || "",
    ai_change_pressure: d.pressure || "",
    mission_exposure: d.mission || "",
    recent_change: d.change || "",
    quadrant: d.quadrant || "",
    density: d.density != null ? d.density : "",
    optionality: d.optionality != null ? d.optionality : "",
    alumni_capital: d.alumni_capital != null ? d.alumni_capital : "",
    alumni_band: d.alumni_band || "",
    contested: d.contested === true,
    adjacent: d.adjacent || "",
    source: d.source || "ai_readiness_assessment"
  };

  try {
    const store = getStore("ai-readiness-leads");
    const id = (globalThis.crypto && crypto.randomUUID)
      ? crypto.randomUUID()
      : `${now.getTime()}-${Math.floor(Math.random() * 1e9)}`;
    const key = `${now.toISOString().replace(/[:.]/g, "-")}__${id}`;
    await store.setJSON(key, record);
    return { statusCode: 200, headers: CORS, body: JSON.stringify({ ok: true, key }) };
  } catch (e) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: "storage_failed" }) };
  }
};
