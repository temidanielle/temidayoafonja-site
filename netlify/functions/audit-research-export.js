// Token-gated CSV export of the audit research store.
//
// Access:  https://temidayoafonja.com/.netlify/functions/audit-research-export?token=YOUR_TOKEN
// The token must equal the RESEARCH_EXPORT_TOKEN environment variable (set in Netlify).
// Returns every stored submission as CSV (opens straight into Excel / Google Sheets).
// Add &format=json to get raw JSON instead.
const { getStore } = require("@netlify/blobs");

function csvCell(v) {
  if (v === null || v === undefined) return "";
  const s = typeof v === "object" ? JSON.stringify(v) : String(v);
  return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

const COLUMNS = [
  "key",
  "received_at_cst", "received_at_utc", "timezone",
  "consent", "consent_flag",
  "mode", "quadrant",
  "density", "optionality", "alumni_capital",
  "industry", "role_level", "years_experience", "organization_size",
  "name", "email",
  "client_completed_at", "responses"
];

function flatten(r) {
  const s = r.scores || {};
  return {
    key: r._key,
    received_at_cst: r.received_at_cst,
    received_at_utc: r.received_at_utc,
    timezone: r.timezone,
    consent: r.consent,
    consent_flag: r.consent_flag,
    mode: r.mode,
    quadrant: r.quadrant,
    density: s.density,
    optionality: s.optionality,
    alumni_capital: s.alumni_capital,
    industry: r.industry,
    role_level: r.role_level,
    years_experience: r.years_experience,
    organization_size: r.organization_size,
    name: r.name,
    email: r.email,
    client_completed_at: r.client_completed_at,
    responses: r.responses
  };
}

exports.handler = async (event) => {
  const q = event.queryStringParameters || {};
  const token = q.token || "";
  const expected = process.env.RESEARCH_EXPORT_TOKEN || "";
  if (!expected || token !== expected) {
    return { statusCode: 401, body: "Unauthorized" };
  }

  // Token-gated delete of a single record by key:
  //   ...audit-research-export?token=YOUR_TOKEN&delete=THE_RECORD_KEY
  // Used to remove test records after verification.
  if (q.delete) {
    try {
      const store = getStore("audit-research");
      await store.delete(q.delete);
      return { statusCode: 200, headers: { "Content-Type": "application/json" }, body: JSON.stringify({ ok: true, deleted: q.delete }) };
    } catch (e) {
      return { statusCode: 500, body: "delete_failed" };
    }
  }

  let records = [];
  try {
    const store = getStore("audit-research");
    const listing = await store.list();
    const blobs = (listing && listing.blobs) || [];
    for (const b of blobs) {
      const rec = await store.get(b.key, { type: "json" });
      if (rec) { rec._key = b.key; records.push(rec); }
    }
  } catch (e) {
    return { statusCode: 500, body: "export_failed" };
  }

  // newest first
  records.sort((a, b) => String(b.received_at_utc).localeCompare(String(a.received_at_utc)));

  if (((event.queryStringParameters || {}).format || "") === "json") {
    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ count: records.length, records }, null, 2)
    };
  }

  const rows = [COLUMNS.join(",")];
  for (const r of records) {
    const f = flatten(r);
    rows.push(COLUMNS.map((c) => csvCell(f[c])).join(","));
  }

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "text/csv; charset=utf-8",
      "Content-Disposition": 'attachment; filename="capability-audit-research.csv"'
    },
    body: rows.join("\n")
  };
};
