// Netlify function: /.netlify/functions/diagnose
// Receives the questionnaire answers, calls the Anthropic Messages API with the
// Capability Formation Framework system prompt (kept server-side so the IP is not
// visible in page source), and returns the Anthropic response for the front end
// to parse. Requires env var ANTHROPIC_API_KEY. Node 18+ (global fetch).

const SYSTEM = `You are the narrative layer for The Density Group's Capability Formation Framework. You are given an organization's self-reported answers and a placement that has already been computed deterministically: a quadrant, and a level (high, moderate, or low) for each of Density, Optionality, and Alumni Capital. Your job is to write the read for that placement, in the founder's voice. You never assign, change, second-guess, or contradict the placement. If the answers seem to you to point somewhere else, you still write for the placement you were given.

The three pillars:
1. Density: how high-challenge the environment actually is. Intensity, not tenure. Real density pushes people into consequential decisions early and keeps raising the bar. Volume of work without growth is not density, it is burnout, and you must tell them apart.
2. Optionality: how portable the capability people build is across functions and industries. Skills bound to internal systems and politics are low optionality. Skills sought after elsewhere are high.
3. Alumni Capital: what the organization retains and circulates after people leave. Maintained relationships, returning talent and clients, knowledge that stays usable, and rehiring without stigma all signal high alumni capital.

Density and Optionality are the two axes that set the quadrant. Alumni Capital is measured separately and does not move the placement. It is the realization layer: it decides whether the organization compounds the position it holds or leaks the value out the door. A Compounding organization with low Alumni Capital is a free training ground for its competitors.

Name the cost. Somewhere in the read or the leaders paragraph, state what this position is costing the organization in concrete terms: the time to rebuild lost capability, the expense and lag of replacing people, the momentum and knowledge that walk out with them. Do not invent precise dollar figures you cannot know for this organization. Keep it concrete but honest.

Voice rules, enforce strictly:
- No em dashes under any circumstances. Use periods, commas, colons, parentheses.
- Prose only. No bullet lists. Direct, lived-in, practitioner-grounded. Address the organization as "you".
- Do not use "it is not X, it is Y" constructions, tidy summarizing pivots, mirrored clause structures, or hedging.
- Close on organizational responsibility, what the leadership owes the organization, never on a score or personal triumph.

Return ONLY a JSON object. No markdown, no code fences, no preamble. Exactly these keys:
{"headline": one plain sentence giving a directional read of the pattern the answers most closely resemble, not a definitive label of what the organization is, "read": two short paragraphs diagnosing the organization across the three pillars, "leaders": one paragraph on what this means for leaders, closing on organizational responsibility}
Keep the prose tight and economical.`;

// Per-IP rate limit: 25 calls per rolling hour, backed by Netlify Blobs (already a
// project dependency; used by the other functions). No auth, no captcha, no new
// dependency. Fails open on any store error so a legitimate read is never blocked.
// 25/hour lets a full leadership team run the instrument from one shared corporate
// IP in a sitting, while capping abuse at roughly fifty cents an hour per IP.
const { getStore } = require("@netlify/blobs");
const crypto = require("crypto");
const RATE_MAX = 25;
const RATE_WINDOW_MS = 60 * 60 * 1000;

// The rate-limit key is a salted SHA-256 of the caller's IP, never the address
// itself. The limiter behaves identically, because the same IP always produces
// the same key, but the store stops being a list of visitor IP addresses and
// the hash cannot be reversed to one.
//
// RATE_LIMIT_SALT should be set to a long random string in the Netlify
// environment. Without a salt an attacker who guessed the scheme could hash a
// candidate IP and test for its presence; with one, they cannot. If the
// variable is absent the function still hashes rather than storing plaintext,
// which is degraded but never worse than the previous behaviour.
function rateKey(ip) {
  const salt = process.env.RATE_LIMIT_SALT || "density-group-rate-limit";
  return crypto.createHash("sha256").update(salt + "|" + ip).digest("hex");
}

// Note on retention: records are reset when the window lapses but are not
// deleted, so the store still grows one entry per distinct caller. That is
// acceptable now only because an entry is a salted hash and a counter, which is
// not personal data. Adding a purge remains on the follow-up list.
async function isRateLimited(ip) {
  if (!ip) return false;
  try {
    const store = getStore("diagnose-rate");
    const key = rateKey(ip);
    const now = Date.now();
    const rec = await store.get(key, { type: "json" });
    let windowStart = rec && rec.windowStart ? rec.windowStart : now;
    let count = rec && rec.count ? rec.count : 0;
    if (now - windowStart > RATE_WINDOW_MS) { windowStart = now; count = 0; }
    count += 1;
    await store.setJSON(key, { windowStart, count });
    return count > RATE_MAX;
  } catch (e) {
    return false;
  }
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ error: "Method not allowed" }) };
  }
  if (!process.env.ANTHROPIC_API_KEY) {
    return { statusCode: 500, body: JSON.stringify({ error: "Server is missing ANTHROPIC_API_KEY" }) };
  }

  const h = event.headers || {};
  const ip = (h["x-nf-client-connection-ip"] || (h["x-forwarded-for"] || "").split(",")[0] || "").trim();
  if (await isRateLimited(ip)) {
    // The front end shows the standard retry message on 429.
    return { statusCode: 429, body: JSON.stringify({ error: "Rate limit exceeded. Try again later." }) };
  }

  let answers = [];
  let placement = null;
  try {
    const payload = JSON.parse(event.body || "{}");
    answers = Array.isArray(payload.answers) ? payload.answers : [];
    placement = payload.placement && typeof payload.placement === "object" ? payload.placement : null;
  } catch (e) {
    return { statusCode: 400, body: JSON.stringify({ error: "Invalid request body" }) };
  }
  if (!answers.length) {
    return { statusCode: 400, body: JSON.stringify({ error: "No answers provided" }) };
  }

  // The placement is computed client-side and is authoritative. Give it to the
  // model as the fixed frame it must write for; the model never reassigns it.
  const placementLine = placement
    ? "Placement (already computed, do not change): quadrant " + placement.quadrant +
      ", Density " + placement.density + ", Optionality " + placement.optionality +
      ", Alumni Capital " + placement.alumniCapital + ".\n\n"
    : "";
  const userContent =
    placementLine +
    "Here are the organization's answers:\n\n" + answers.join("\n") +
    "\n\nWrite the read for the given placement, as specified.";

  try {
    const res = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 1000,
        system: SYSTEM,
        messages: [{ role: "user", content: userContent }]
      })
    });

    const data = await res.json();
    if (!res.ok) {
      return { statusCode: 502, body: JSON.stringify({ error: "Upstream error", detail: data && data.error ? data.error : null }) };
    }
    // Pass the Anthropic response through; the front end parses content[].text exactly as before.
    return {
      statusCode: 200,
      headers: { "content-type": "application/json" },
      body: JSON.stringify(data)
    };
  } catch (err) {
    return { statusCode: 502, body: JSON.stringify({ error: "Request to model failed" }) };
  }
};
