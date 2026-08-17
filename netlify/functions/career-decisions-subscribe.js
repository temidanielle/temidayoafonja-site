// Netlify function: /.netlify/functions/career-decisions-subscribe
//
// Serves one page only: /career-decisions, the Career Decision Evidence Check.
//
// This is a sibling of subscribe.js, not a change to it. subscribe.js resolves a
// Kit sequence from the diagnostic's quadrant and mode, and three completion
// paths in diagnostic.html depend on that contract. A plain email capture has no
// quadrant, so routing it through subscribe.js would have meant changing a
// working, verified path. Nothing in subscribe.js is touched by this file. The
// cost of that choice is that the Kit v3 call shape appears in two files.
//
// One subscription system, one durable record, no second write. There is no
// Formspree call here by design: two independent writes is exactly what produces
// a lead that exists in one system and not the other.
//
// ── Required environment variables (names only, never values) ──
//   KIT_API_KEY                  Kit (ConvertKit) v3 API key
//   KIT_SEQ_CAREER_DECISIONS     Kit sequence id that delivers the evidence check
//   KIT_TAG_CAREER_DECISIONS     Kit tag id applied to every subscriber here
//   KIT_TAG_YOUTUBE              Kit tag id applied only when the visitor
//                                actually arrived with a youtube source
//
// ── Optional, and what is lost without them ──
//   BLOBS_SITE_ID, BLOBS_TOKEN   Netlify Blobs. Without both: no durable
//                                first-party record and no rate limiting. The
//                                subscription itself still completes, and the
//                                response says which of the two happened.
//   RATE_LIMIT_SALT              Long random string. Without it the IP is still
//                                hashed, using a default salt, which is weaker
//                                but never plaintext.
//
// Node 18+ (global fetch). See docs/forms-audit.md and docs/data-inventory.md.

const crypto = require("crypto");
const { blobStore, blobsConfigured } = require("../lib/blobs");

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
};
const JSON_HEADERS = Object.assign({ "content-type": "application/json" }, CORS);

// Every variable that has to be present before a subscription can be attempted.
// Reported by name if absent. Values are never read into a response or a log.
const REQUIRED_ENV = [
  "KIT_API_KEY",
  "KIT_SEQ_CAREER_DECISIONS",
  "KIT_TAG_CAREER_DECISIONS",
  "KIT_TAG_YOUTUBE"
];

// Lower than the Scan's 25/hour. This endpoint creates a mailing list subscriber
// rather than a page of narrative, so the abuse worth stopping is list stuffing,
// and a real person needs one request, not ten.
const RATE_MAX = 10;
const RATE_WINDOW_MS = 60 * 60 * 1000;

// Field length caps. A capture form has no reason to accept a payload larger
// than this, and an unbounded free-text field is the one place a submission can
// be used to push volume into the record store.
const MAX_NAME = 120;
const MAX_EMAIL = 254;
const MAX_DECISION = 2000;
const MAX_ATTR = 300;

// Same construction as diagnose.js: the store key is a salted SHA-256 of the
// caller's IP, never the address. The limiter behaves identically because the
// same IP always hashes to the same key, and the store never becomes a list of
// visitor IP addresses.
function rateKey(ip) {
  const salt = process.env.RATE_LIMIT_SALT || "density-group-rate-limit";
  return crypto.createHash("sha256").update(salt + "|" + ip).digest("hex");
}

async function isRateLimited(ip) {
  if (!ip) return false;
  try {
    const store = blobStore("career-decisions-rate");
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
    // Fail open, and say so. A storage problem must not take the form down, but
    // silently running with no rate limit is how the Scan spent months
    // unprotected without anything anywhere reporting it.
    console.error("blobs career-decisions-rate failed, rate limiting is OFF. manual config present:", blobsConfigured(), e);
    return false;
  }
}

// America/Chicago (CST/CDT, DST aware) "YYYY-MM-DD HH:MM:SS". Same helper the
// other capture functions use, so exported rows sort together.
function chicagoStamp(d) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/Chicago",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false
  }).formatToParts(d).reduce((o, p) => { o[p.type] = p.value; return o; }, {});
  const hh = parts.hour === "24" ? "00" : parts.hour;
  return `${parts.year}-${parts.month}-${parts.day} ${hh}:${parts.minute}:${parts.second}`;
}

function str(v, max) {
  if (v === undefined || v === null) return "";
  return String(v).trim().slice(0, max);
}

// Deliberately lenient, matching the check the diagnostic uses, so an unusual
// but valid address is not refused.
function validEmail(e) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }

// The youtube tag is applied only when the visitor genuinely arrived with a
// youtube source. It is never inferred from a referrer, a campaign name or the
// absence of a parameter. An unattributed subscriber stays unattributed.
function isYoutubeSource(attr) {
  const candidates = [attr.source, attr.utm_source];
  return candidates.some((v) => typeof v === "string" && v.trim().toLowerCase() === "youtube");
}

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: JSON_HEADERS, body: JSON.stringify({ error: "method_not_allowed" }) };
  }

  // ── Configuration gate ──
  // Reports which variables are missing, by name. It never reads, echoes,
  // truncates or fingerprints a value, so the response is safe to show a
  // visitor and safe to paste into an issue.
  const missing = REQUIRED_ENV.filter((name) => !process.env[name]);
  if (missing.length) {
    console.error("career-decisions-subscribe is not configured. Missing env var names:", missing.join(", "));
    return {
      statusCode: 503,
      headers: JSON_HEADERS,
      body: JSON.stringify({
        error: "not_configured",
        message: "This endpoint is not configured yet. No subscription was created and nothing was stored.",
        missing_env_vars: missing,
        checklist: [
          "Create the Kit sequence that delivers the Career Decision Evidence Check, then set KIT_SEQ_CAREER_DECISIONS to its numeric id.",
          "Create the Kit tag for this page, then set KIT_TAG_CAREER_DECISIONS to its numeric id.",
          "Create the Kit tag for YouTube arrivals, then set KIT_TAG_YOUTUBE to its numeric id.",
          "Set KIT_API_KEY to the Kit v3 API key.",
          "Create these Kit custom fields so the attribution is stored rather than dropped: current_decision, marketing_consent, consent_timestamp, policy_version, utm_source, utm_medium, utm_campaign, utm_content, utm_term, source, video_slug, referrer, landing_page.",
          "Optional but recommended: set BLOBS_SITE_ID and BLOBS_TOKEN for the durable first-party record and the rate limit, and RATE_LIMIT_SALT to a long random string.",
          "Confirm in Kit whether double opt in is on for this sequence. It is an account level setting and cannot be set or read from this repository."
        ]
      })
    };
  }

  const h = event.headers || {};
  const ip = (h["x-nf-client-connection-ip"] || (h["x-forwarded-for"] || "").split(",")[0] || "").trim();
  if (await isRateLimited(ip)) {
    return { statusCode: 429, headers: JSON_HEADERS, body: JSON.stringify({ error: "rate_limited" }) };
  }

  let p;
  try { p = JSON.parse(event.body || "{}"); }
  catch (e) { return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "invalid_body" }) }; }

  // ── Honeypot ──
  // A hidden field no human ever sees or tabs into. Anything in it means an
  // automated submission. Refused before the address is validated, before the
  // rate window matters, and without a Kit call.
  if (str(p.decision_reference, 50)) {
    return { statusCode: 422, headers: JSON_HEADERS, body: JSON.stringify({ error: "rejected" }) };
  }

  const firstName = str(p.first_name, MAX_NAME);
  const email = str(p.email, MAX_EMAIL);
  const currentDecision = str(p.current_decision, MAX_DECISION);

  if (!firstName) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "first_name_required" }) };
  }
  if (!validEmail(email)) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "valid_email_required" }) };
  }

  // ── Consent, fail closed ──
  // Anything other than a literal true is no consent. Same ruling as the
  // diagnostic gate. No consent means no Kit call, no record, no delivery.
  if (p.marketing_consent !== true) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "consent_required" }) };
  }

  const attrIn = p.attribution && typeof p.attribution === "object" ? p.attribution : {};
  const attr = {
    utm_source: str(attrIn.utm_source, MAX_ATTR),
    utm_medium: str(attrIn.utm_medium, MAX_ATTR),
    utm_campaign: str(attrIn.utm_campaign, MAX_ATTR),
    utm_content: str(attrIn.utm_content, MAX_ATTR),
    utm_term: str(attrIn.utm_term, MAX_ATTR),
    source: str(attrIn.source, MAX_ATTR),
    video_slug: str(attrIn.video, MAX_ATTR),
    referrer: str(attrIn.referrer, MAX_ATTR),
    landing_page: str(attrIn.landing_page, MAX_ATTR)
  };

  // The client stamps the moment the visitor submitted with the box ticked. The
  // server stamps its own receipt independently, so a wrong or spoofed client
  // clock cannot be the only record of when consent was given. Both are kept.
  const now = new Date();
  const consentTimestampClient = str(p.consent_timestamp, 40);
  const policyVersion = str(p.policy_version, 40);

  const tags = [process.env.KIT_TAG_CAREER_DECISIONS];
  if (isYoutubeSource(attr)) tags.push(process.env.KIT_TAG_YOUTUBE);

  // Kit custom fields. Every one of these must exist in the Kit account or Kit
  // drops it silently; the list is in the configuration checklist above.
  const fields = {
    current_decision: currentDecision,
    marketing_consent: "true",
    consent_timestamp: consentTimestampClient || now.toISOString(),
    policy_version: policyVersion,
    utm_source: attr.utm_source,
    utm_medium: attr.utm_medium,
    utm_campaign: attr.utm_campaign,
    utm_content: attr.utm_content,
    utm_term: attr.utm_term,
    source: attr.source,
    video_slug: attr.video_slug,
    referrer: attr.referrer,
    landing_page: attr.landing_page
  };

  // ── Kit is authoritative ──
  // Kit owns the subscriber record, the deduplication (it upserts on the email
  // address), the sequence that delivers the evidence check, and the unsubscribe
  // link in every message. If this call does not succeed, the visitor is not a
  // subscriber and the response must not say otherwise.
  let kitSubscriberId = null;
  try {
    const res = await fetch(
      "https://api.convertkit.com/v3/sequences/" + encodeURIComponent(process.env.KIT_SEQ_CAREER_DECISIONS) + "/subscribe",
      {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          api_key: process.env.KIT_API_KEY,
          email: email,
          first_name: firstName,
          fields: fields,
          tags: tags
        })
      }
    );
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      // Kit's message is logged for the operator but never returned, because it
      // can echo the submitted address back into a public response body.
      console.error("Kit subscribe failed for career-decisions. status:", res.status, "message:", data && data.message ? data.message : "(none)");
      return { statusCode: 502, headers: JSON_HEADERS, body: JSON.stringify({ error: "subscribe_failed" }) };
    }
    kitSubscriberId = (data && data.subscription && data.subscription.subscriber && data.subscription.subscriber.id) || null;
  } catch (err) {
    console.error("Request to Kit failed for career-decisions:", err && err.message ? err.message : err);
    return { statusCode: 502, headers: JSON_HEADERS, body: JSON.stringify({ error: "subscribe_failed" }) };
  }

  // ── Durable first-party record ──
  // Written only after Kit has confirmed, so the store never contains a lead
  // that is not also a subscriber. Best effort: a storage failure is reported in
  // the response and logged, and does not turn a real subscription into an
  // error the visitor sees. durable_record says which of the two happened, so
  // there is no ambiguity about what was stored.
  let durableRecord = false;
  let recordKey = null;
  if (blobsConfigured()) {
    try {
      const store = blobStore("career-decisions-leads");
      const id = (globalThis.crypto && crypto.randomUUID) ? crypto.randomUUID() : `${now.getTime()}-${Math.floor(Math.random() * 1e9)}`;
      recordKey = `${now.toISOString().replace(/[:.]/g, "-")}__${id}`;
      await store.setJSON(recordKey, {
        received_at_cst: chicagoStamp(now),
        received_at_utc: now.toISOString(),
        timezone: "America/Chicago",
        form: "career-decision-evidence-check",
        page: "/career-decisions",
        first_name: firstName,
        email: email,
        current_decision: currentDecision,
        marketing_consent: true,
        consent_timestamp_client: consentTimestampClient,
        consent_timestamp_server: now.toISOString(),
        policy_version: policyVersion,
        attribution: attr,
        youtube_tagged: isYoutubeSource(attr),
        kit_sequence_env: "KIT_SEQ_CAREER_DECISIONS",
        kit_subscriber_id: kitSubscriberId
      });
      durableRecord = true;
    } catch (e) {
      console.error("blobs career-decisions-leads write failed. manual config present:", blobsConfigured(), e);
      recordKey = null;
    }
  } else {
    console.error("BLOBS_SITE_ID / BLOBS_TOKEN are not set: no durable first-party record was written for a confirmed subscriber.");
  }

  // ok:true means one thing: Kit confirmed the subscription. The page reveals
  // the evidence check on this and on nothing else.
  return {
    statusCode: 200,
    headers: JSON_HEADERS,
    body: JSON.stringify({ ok: true, durable_record: durableRecord, record_key: recordKey })
  };
};
