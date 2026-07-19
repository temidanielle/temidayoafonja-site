// Netlify function: /.netlify/functions/save-score
//
// Durable store for paper scores from The Capability Formation Audit Short Form.
// A reader who scored the twelve statements on paper enters them at /audit/save;
// this endpoint stores the twelve individual scores plus totals, state, and date,
// then tags the subscriber in Kit (ConvertKit) and sets the custom fields a Kit
// automation uses to email the result.
//
// Storage is authoritative and happens first (Netlify Blobs, store "audit-paper-save",
// one blob per submission so concurrent saves cannot clobber each other). The Kit
// step is best effort: a Kit failure never fails the save. The response reports the
// Kit outcome so it can be checked, but the reader always gets their result.
//
// Env vars:
//   KIT_API_KEY            Kit (ConvertKit) API key (already set for /audit).
//   KIT_TAG_INDIVIDUAL     Kit tag id for the "Individual" tag.
//   KIT_TAG_PAPER_SAVE     Kit tag id for the "audit-paper-save" source tag.
//
// The email itself is sent by a Kit automation triggered by the audit-paper-save
// tag, using the custom fields set below (results_line is pre-rendered for it).
const { getStore } = require("@netlify/blobs");

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
};

const PER_AXIS = 6;
const MAX_PER_AXIS = 30;
const HIGH_AT = 19;
const BOUNDARY_LOW = 17;
const BOUNDARY_HIGH = 21;

function stateFor(density, optionality) {
  const dHigh = density >= HIGH_AT;
  const oHigh = optionality >= HIGH_AT;
  if (dHigh && oHigh) return "Compounding";
  if (dHigh && !oHigh) return "Depth Trap";
  if (!dHigh && !oHigh) return "Stagnant";
  return "Fragile";
}

// The two neighboring states to read, or null when not on a boundary.
function neighborsFor(density, optionality) {
  const dOnB = density >= BOUNDARY_LOW && density <= BOUNDARY_HIGH;
  const oOnB = optionality >= BOUNDARY_LOW && optionality <= BOUNDARY_HIGH;
  if (!dOnB && !oOnB) return null;

  let axis;
  if (dOnB && oOnB) {
    axis = Math.abs(density - HIGH_AT) <= Math.abs(optionality - HIGH_AT) ? "D" : "O";
  } else {
    axis = dOnB ? "D" : "O";
  }
  const dHigh = density >= HIGH_AT;
  const oHigh = optionality >= HIGH_AT;
  if (axis === "D") {
    return oHigh ? ["Compounding", "Fragile"] : ["Depth Trap", "Stagnant"];
  }
  return dHigh ? ["Compounding", "Depth Trap"] : ["Stagnant", "Fragile"];
}

// Format an instant as America/Chicago "YYYY-MM-DD HH:MM:SS" (matches audit-research.js).
function chicagoStamp(d) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false
  }).formatToParts(d).reduce((o, p) => { o[p.type] = p.value; return o; }, {});
  const hh = parts.hour === "24" ? "00" : parts.hour;
  return `${parts.year}-${parts.month}-${parts.day} ${hh}:${parts.minute}:${parts.second}`;
}

// Render a YYYY-MM-DD as "19 July 2026" without timezone drift.
function humanDate(iso) {
  const parts = String(iso || "").split("-");
  if (parts.length !== 3) return String(iso || "");
  const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  const mi = parseInt(parts[1], 10) - 1;
  return parseInt(parts[2], 10) + " " + (months[mi] || "") + " " + parts[0];
}

function isValidScoreDate(s) {
  return typeof s === "string" && /^\d{4}-\d{2}-\d{2}$/.test(s);
}

// Subscribe the email to a Kit tag by id, carrying the custom fields.
async function kitTag(tagId, email, fields) {
  const res = await fetch("https://api.convertkit.com/v3/tags/" + encodeURIComponent(tagId) + "/subscribe", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ api_key: process.env.KIT_API_KEY, email: email, fields: fields })
  });
  if (!res.ok) {
    const data = await res.json().catch(() => ({}));
    throw new Error((data && data.message) ? data.message : ("Kit tag " + tagId + " failed"));
  }
  return true;
}

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: CORS, body: JSON.stringify({ error: "Method Not Allowed" }) };
  }

  let data;
  try { data = JSON.parse(event.body || "{}"); }
  catch (e) { return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Invalid JSON" }) }; }

  const email = (data.email || "").trim();
  if (!email || email.indexOf("@") < 0) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "A valid email is required" }) };
  }

  // Validate the twelve responses: integers 1 to 5.
  const responses = Array.isArray(data.responses) ? data.responses : null;
  if (!responses || responses.length !== PER_AXIS * 2) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Twelve scores are required" }) };
  }
  for (const r of responses) {
    if (!Number.isInteger(r) || r < 1 || r > 5) {
      return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: "Each score must be an integer from 1 to 5" }) };
    }
  }

  // Compute server-side. Never trust client totals.
  const density = responses.slice(0, PER_AXIS).reduce((a, b) => a + b, 0);
  const optionality = responses.slice(PER_AXIS, PER_AXIS * 2).reduce((a, b) => a + b, 0);
  const state = stateFor(density, optionality);
  const neighbors = neighborsFor(density, optionality);

  const now = new Date();
  const scoreDate = isValidScoreDate(data.date) ? data.date : chicagoStamp(now).slice(0, 10);
  const resultsLine = "Your score on " + humanDate(scoreDate) +
    ": Density " + density + " of " + MAX_PER_AXIS +
    ", Optionality " + optionality + " of " + MAX_PER_AXIS + ". State: " + state + ".";

  // Paper scorers entered numbers from the printed Short Form; flow scorers
  // answered the twelve statements in the individual audit. Both are Individuals.
  const isPaper = data.paper === true || (data.source || "") === "audit-paper-save";

  const record = {
    received_at_cst: chicagoStamp(now),
    received_at_utc: now.toISOString(),
    timezone: "America/Chicago",
    score_date: scoreDate,
    name: (data.name || "").trim(),
    email: email,
    responses: responses,
    reflection: typeof data.reflection === "string" ? data.reflection : null,
    density: density,
    optionality: optionality,
    max_per_axis: MAX_PER_AXIS,
    state: state,
    neighbors: neighbors,
    results_line: resultsLine,
    paper: isPaper,
    source: (data.source || (isPaper ? "audit-paper-save" : "audit-individual"))
  };

  // 1. Store authoritatively.
  let key;
  try {
    const store = getStore("audit-paper-save");
    const id = (globalThis.crypto && crypto.randomUUID)
      ? crypto.randomUUID()
      : `${now.getTime()}-${Math.floor(Math.random() * 1e9)}`;
    key = `${now.toISOString().replace(/[:.]/g, "-")}__${id}`;
    await store.setJSON(key, record);
  } catch (e) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: "storage_failed" }) };
  }

  // 2. Tag in Kit (best effort). Set the fields the Kit results email reads.
  // Every result tags Individual; only paper scorers additionally get audit-paper-save.
  let kit = "skipped";
  if (process.env.KIT_API_KEY && (process.env.KIT_TAG_INDIVIDUAL || (isPaper && process.env.KIT_TAG_PAPER_SAVE))) {
    const fields = {
      density_score: String(density),
      optionality_score: String(optionality),
      capability_state: state,
      score_date: scoreDate,
      results_line: resultsLine,
      source: record.source
    };
    try {
      const tagIds = [
        process.env.KIT_TAG_INDIVIDUAL,
        isPaper ? process.env.KIT_TAG_PAPER_SAVE : null
      ].filter(Boolean);
      for (const tagId of tagIds) {
        await kitTag(tagId, email, fields);
      }
      kit = "tagged";
    } catch (e) {
      kit = "failed";
    }
  }

  return {
    statusCode: 200,
    headers: { ...CORS, "Content-Type": "application/json" },
    body: JSON.stringify({ ok: true, key, density, optionality, state, neighbors, kit })
  };
};
