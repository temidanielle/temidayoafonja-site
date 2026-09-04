// Token-gated CSV/JSON export of the Organizational Diagnostic lead store.
//
// Access:  /.netlify/functions/org-diagnostic-export?token=YOUR_TOKEN
//          add &format=json for JSON, or &delete=THE_KEY to remove a test record.
// Uses the same RESEARCH_EXPORT_TOKEN env var as the other exports.
const { blobStore, blobsConfigured } = require("../lib/blobs");

function csvCell(v) {
  if (v === null || v === undefined) return "";
  const s = typeof v === "object" ? JSON.stringify(v) : String(v);
  return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

const COLUMNS = [
  "key", "received_at_cst", "received_at_utc",
  "email", "organization",
  "quadrant", "placement_type", "label",
  "density", "optionality", "alumni_capital",
  "boundary", "standard", "reflection", "source"
];

exports.handler = async (event) => {
  const q = event.queryStringParameters || {};
  const expected = process.env.RESEARCH_EXPORT_TOKEN || "";
  if (!expected || (q.token || "") !== expected) {
    return { statusCode: 401, body: "Unauthorized" };
  }

  const store = blobStore("org-diagnostic-leads");

  if (q.delete) {
    try { await store.delete(q.delete); return { statusCode: 200, headers: { "Content-Type": "application/json" }, body: JSON.stringify({ ok: true, deleted: q.delete }) }; }
    catch (e) { return { statusCode: 500, body: "delete_failed" }; }
  }

  let records = [];
  try {
    const listing = await store.list();
    for (const b of (listing && listing.blobs) || []) {
      const rec = await store.get(b.key, { type: "json" });
      if (rec) { rec.key = b.key; records.push(rec); }
    }
  } catch (e) {
    console.error("blobs org-diagnostic-leads list failed. manual config present:", blobsConfigured(), e);
    return { statusCode: 500, body: "export_failed" };
  }

  records.sort((a, b) => String(b.received_at_utc).localeCompare(String(a.received_at_utc)));

  if ((q.format || "") === "json") {
    return { statusCode: 200, headers: { "Content-Type": "application/json" }, body: JSON.stringify({ count: records.length, records }, null, 2) };
  }

  const rows = [COLUMNS.join(",")];
  for (const r of records) rows.push(COLUMNS.map((c) => csvCell(r[c])).join(","));
  return {
    statusCode: 200,
    headers: { "Content-Type": "text/csv; charset=utf-8", "Content-Disposition": 'attachment; filename="org-diagnostic-leads.csv"' },
    body: rows.join("\n")
  };
};
