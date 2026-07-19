// Token-gated CSV export of the paper-score store (store: "audit-paper-save").
//
// Access:  https://temidayoafonja.com/.netlify/functions/save-score-export?token=YOUR_TOKEN
// The token must equal the RESEARCH_EXPORT_TOKEN environment variable (same token
// used by audit-research-export). Add &format=json for raw JSON.
// Delete a single record:  ...save-score-export?token=YOUR_TOKEN&delete=THE_RECORD_KEY
const { getStore } = require("@netlify/blobs");

function csvCell(v) {
  if (v === null || v === undefined) return "";
  const s = typeof v === "object" ? JSON.stringify(v) : String(v);
  return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

const COLUMNS = [
  "key",
  "received_at_cst", "received_at_utc", "timezone", "score_date",
  "email",
  "density", "optionality", "max_per_axis", "state", "neighbors",
  "results_line", "source", "responses"
];

function flatten(r) {
  return {
    key: r._key,
    received_at_cst: r.received_at_cst,
    received_at_utc: r.received_at_utc,
    timezone: r.timezone,
    score_date: r.score_date,
    email: r.email,
    density: r.density,
    optionality: r.optionality,
    max_per_axis: r.max_per_axis,
    state: r.state,
    neighbors: r.neighbors,
    results_line: r.results_line,
    source: r.source,
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

  if (q.delete) {
    try {
      const store = getStore("audit-paper-save");
      await store.delete(q.delete);
      return { statusCode: 200, headers: { "Content-Type": "application/json" }, body: JSON.stringify({ ok: true, deleted: q.delete }) };
    } catch (e) {
      return { statusCode: 500, body: "delete_failed" };
    }
  }

  let records = [];
  try {
    const store = getStore("audit-paper-save");
    const listing = await store.list();
    const blobs = (listing && listing.blobs) || [];
    for (const b of blobs) {
      const rec = await store.get(b.key, { type: "json" });
      if (rec) { rec._key = b.key; records.push(rec); }
    }
  } catch (e) {
    return { statusCode: 500, body: "export_failed" };
  }

  records.sort((a, b) => String(b.received_at_utc).localeCompare(String(a.received_at_utc)));

  if ((q.format || "") === "json") {
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
      "Content-Disposition": 'attachment; filename="capability-audit-paper-saves.csv"'
    },
    body: rows.join("\n")
  };
};
