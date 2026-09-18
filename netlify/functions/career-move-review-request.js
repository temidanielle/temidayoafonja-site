/* ─────────────────────────────────────────────────────────────────────────────
   Career Move Review: qualification request
   POST /api/career-move-review-request

   This endpoint does one thing. It accepts a request to be considered for a
   Career Move Review and forwards it to Temidayo. It does not take payment, it
   does not issue a booking link, and it does not enrol anyone in anything.
   Qualification precedes payment, so nothing here can result in a charge.

   What it deliberately does NOT do, and why:

   - No Netlify Blobs. Both other forms on this site carry a Blobs-based
     limiter, and Blobs has been failing site-wide since 2026-08-20, so those
     limiters are currently inert. Rather than add an inert limiter to a path
     that carries personal career information, this endpoint has no store at
     all. Rate limiting is enforced at the edge in netlify.toml, by Netlify
     itself, and depends on nothing this site configures.

   - No file uploads. The site has no authenticated storage. A public upload
     endpoint for resumes would put personal documents somewhere that could be
     enumerated. The form takes a LinkedIn URL or a short written summary, and
     a resume is requested by reply after acceptance, when there is a named
     person on the other end. This is the "safest next step" the brief asks for
     rather than a workaround.

   - No secrets in client code. The destination endpoint lives in a Netlify
     environment variable and is never sent to the browser. Every other inquiry
     form on this site posts to a Formspree endpoint written into page source;
     this one does not.

   - No submission data is written anywhere the site serves. Nothing from this
     form touches the publish root.
   ───────────────────────────────────────────────────────────────────────────── */

// Same reasoning as career-evidence-starter-subscribe.js. The page that calls
// this is same origin, so these headers only ever matter to a cross-origin
// caller, and there is no legitimate one. Deploy previews are unaffected: the
// page and the function share the preview origin, so the header is never
// consulted there.
const CORS = {
  "Access-Control-Allow-Origin": "https://temidayoafonja.com",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Vary": "Origin"
};
const JSON_HEADERS = Object.assign({ "content-type": "application/json" }, CORS);

// The destination for a qualification request. Absent means the form is not
// live yet, and the endpoint says so plainly rather than accepting a submission
// it cannot deliver. The value is never read into a response or a log.
const REQUIRED_ENV = ["FORMSPREE_CAREER_MOVE_REVIEW"];

// Field caps. A qualification form has no reason to accept more than this, and
// an unbounded free-text field is where volume gets pushed into a destination.
const MAX_NAME = 120;
const MAX_EMAIL = 254;
const MAX_SHORT = 300;
const MAX_LONG = 2000;

function str(v, max) {
  if (typeof v !== "string") return "";
  const s = v.trim();
  return s.length > max ? s.slice(0, max) : s;
}

function validEmail(e) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }

// Accepts a LinkedIn profile URL. Deliberately permissive about the shape of
// the path and the subdomain, because country subdomains and vanity paths vary,
// and a person who pastes a working profile URL should not be told it is wrong.
function looksLikeLinkedIn(u) {
  return /^https?:\/\/([a-z0-9-]+\.)?linkedin\.com\/.+/i.test(u);
}

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: JSON_HEADERS, body: JSON.stringify({ error: "method_not_allowed" }) };
  }

  // ── Configuration gate ──
  // Before anything else, and before any submission is accepted. Reports which
  // variables are missing by NAME only. No value is ever returned.
  const missing = REQUIRED_ENV.filter((name) => !process.env[name]);
  if (missing.length) {
    return {
      statusCode: 503,
      headers: JSON_HEADERS,
      body: JSON.stringify({
        error: "not_configured",
        missing_env_vars: missing,
        note: "Set this in the Netlify environment, Runtime scope, then redeploy so the function sees it."
      })
    };
  }

  let p;
  try { p = JSON.parse(event.body || "{}"); }
  catch (e) { return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "invalid_body" }) }; }

  // ── Honeypot ──
  // A hidden field no human sees or tabs into. Anything in it means an
  // automated submission, refused before anything else is validated and without
  // contacting the destination.
  if (str(p.review_reference, 50)) {
    return { statusCode: 422, headers: JSON_HEADERS, body: JSON.stringify({ error: "rejected" }) };
  }

  const firstName = str(p.first_name, MAX_NAME);
  const email = str(p.email, MAX_EMAIL);
  const yearsExperience = str(p.years_experience, MAX_SHORT);
  const targetMove = str(p.target_move, MAX_LONG);
  const evidenceLink = str(p.evidence_link, MAX_SHORT);
  const evidenceSummary = str(p.evidence_summary, MAX_LONG);
  const timing = str(p.timing, MAX_LONG);

  if (!firstName) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "first_name_required" }) };
  }
  if (!validEmail(email)) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "valid_email_required" }) };
  }
  if (!targetMove) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "target_move_required" }) };
  }

  // ── Evidence ──
  // The Review reads evidence against an intended move, so a request without
  // any evidence cannot be assessed for fit. Either a LinkedIn profile or a
  // written summary satisfies this. A link that is present but is not LinkedIn
  // is refused with its own message rather than being silently accepted, so the
  // person can correct it instead of wondering why they heard nothing.
  if (evidenceLink && !looksLikeLinkedIn(evidenceLink)) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "linkedin_url_invalid" }) };
  }
  if (!evidenceLink && !evidenceSummary) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "evidence_required" }) };
  }

  // ── Consent ──
  // One consent, and it fails closed. Anything other than a literal true is no
  // consent: not a string, not a 1, not a missing field. It authorises Temidayo
  // to read the request and reply about it, and nothing else. There is no
  // marketing consent on this form, because a qualification request is not a
  // newsletter signup and should not quietly become one.
  if (p.contact_consent !== true) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "consent_required" }) };
  }

  const now = new Date();
  // Stamped by the server. The client sends its own timestamp and policy
  // version, and both are recorded, but the server's values are the record: a
  // consent stamped only by the submitting browser is not evidence of anything.
  const policyVersion = str(p.policy_version, 40);
  const consentStampClient = str(p.consent_timestamp, 40);

  const payload = {
    _subject: "Career Move Review request: " + firstName,
    first_name: firstName,
    email: email,
    years_experience: yearsExperience,
    target_move: targetMove,
    linkedin_url: evidenceLink,
    experience_summary: evidenceSummary,
    timing_and_constraints: timing,
    contact_consent: "true",
    contact_consent_timestamp_server: now.toISOString(),
    contact_consent_timestamp_client: consentStampClient,
    policy_version_client: policyVersion,
    submitted_at: now.toISOString(),
    // Recorded so the pilot can be reconciled later. The page does not take
    // payment and this function never issues a booking link.
    stage: "qualification_request",
    payment_taken: "no"
  };

  try {
    const res = await fetch(process.env.FORMSPREE_CAREER_MOVE_REVIEW, {
      method: "POST",
      headers: { "content-type": "application/json", accept: "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) {
      // The destination's response body is deliberately not forwarded. It can
      // carry the endpoint identifier, and that belongs in the environment, not
      // in a browser.
      return { statusCode: 502, headers: JSON_HEADERS, body: JSON.stringify({ error: "request_failed" }) };
    }
  } catch (e) {
    return { statusCode: 502, headers: JSON_HEADERS, body: JSON.stringify({ error: "request_failed" }) };
  }

  return {
    statusCode: 200,
    headers: JSON_HEADERS,
    body: JSON.stringify({ ok: true, stage: "qualification_request" })
  };
};
