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

   Four things fail closed here. Each refuses the submission rather than
   accepting a degraded version of it, and each says which one it was:

     consent          Anything other than a literal true is no consent. Not a
                      string, not a 1, not a missing field.        400
     policy version   Missing, or not the version in force. A consent is a
                      consent to specific published wording, so a submission
                      that cannot name that wording is not recorded against it.
                                                     400 missing, 409 stale
     consent stamp    Must parse as an instant.                    400
     field length     Over a cap is refused, never truncated, so nothing the
                      person wrote is silently altered before being forwarded.
                                                                   400
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

// The version of the privacy policy in force. It is the "Last updated" date at
// the top of privacy.html, and three places have to move together in the same
// commit: this constant, that date, and POLICY_VERSION in
// career-move-review.html. The consent below is a consent to a specific set of
// published wording, so a submission that does not name the wording in force is
// refused rather than filed against wording the person may never have seen.
const POLICY_VERSION = "2026-08-18";

// Field caps. A qualification form has no reason to accept more than this, and
// an unbounded free-text field is where volume gets pushed into a destination.
// Every one of these is also a maxlength attribute on the matching field in
// career-move-review.html, and the two have to be edited together.
const MAX_NAME = 120;
const MAX_EMAIL = 254;
const MAX_SHORT = 300;
const MAX_LONG = 2000;

// For values the site generates rather than the visitor writes, where trimming
// to fit is the right answer: the honeypot, the policy version, the client's
// consent stamp. None of these is forwarded as the person's own words.
function str(v, max) {
  if (typeof v !== "string") return "";
  const s = v.trim();
  return s.length > max ? s.slice(0, max) : s;
}

// For everything the visitor writes. Returns null when the value is over its
// cap, so the caller can refuse it. Truncating instead would quietly alter what
// the person wrote and then forward the altered text to Temidayo as though it
// were theirs, which is worse than declining it and saying so. A browser cannot
// produce an over-length value here, because every field carries a maxlength;
// anything that arrives over a cap did not come from the form.
function bounded(v, max) {
  if (typeof v !== "string") return "";
  const s = v.trim();
  return s.length > max ? null : s;
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

  // ── Policy version ──
  // Fails closed, and before the submission is read. A missing version is
  // refused. A version that is not the one in force means the page was opened
  // before the wording changed, which its own status distinguishes so the page
  // can tell the person to reload instead of showing a generic failure. The
  // expected value is returned because it is a published date on privacy.html,
  // not a secret.
  const clientPolicyVersion = str(p.policy_version, 40);
  if (!clientPolicyVersion) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "policy_version_required" }) };
  }
  if (clientPolicyVersion !== POLICY_VERSION) {
    return {
      statusCode: 409,
      headers: JSON_HEADERS,
      body: JSON.stringify({ error: "policy_version_stale", expected: POLICY_VERSION })
    };
  }

  // ── Length ──
  // Refused as a set, naming every field that is over, so a caller fixes all of
  // them at once instead of one per round trip.
  const fields = {
    first_name: bounded(p.first_name, MAX_NAME),
    email: bounded(p.email, MAX_EMAIL),
    years_experience: bounded(p.years_experience, MAX_SHORT),
    target_move: bounded(p.target_move, MAX_LONG),
    evidence_link: bounded(p.evidence_link, MAX_SHORT),
    evidence_summary: bounded(p.evidence_summary, MAX_LONG),
    timing: bounded(p.timing, MAX_LONG)
  };
  const tooLong = Object.keys(fields).filter((k) => fields[k] === null);
  if (tooLong.length) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "field_too_long", fields: tooLong }) };
  }

  const firstName = fields.first_name;
  const email = fields.email;
  const yearsExperience = fields.years_experience;
  const targetMove = fields.target_move;
  const evidenceLink = fields.evidence_link;
  const evidenceSummary = fields.evidence_summary;
  const timing = fields.timing;

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

  // The browser's own stamp for the moment the consent was given. It is
  // corroboration, not the record: the server's stamp below is the record,
  // because a consent stamped only by the submitting browser is not evidence of
  // anything. A value that cannot be parsed as an instant is refused rather
  // than stored as text, since a timestamp nobody can read is not a timestamp.
  const consentStampClient = str(p.consent_timestamp, 40);
  if (!consentStampClient || isNaN(Date.parse(consentStampClient))) {
    return { statusCode: 400, headers: JSON_HEADERS, body: JSON.stringify({ error: "consent_timestamp_invalid" }) };
  }

  const now = new Date();

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
    // Verified against the gate above, so this is the wording in force and the
    // wording the page showed, not merely what a client claimed.
    policy_version: POLICY_VERSION,
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
