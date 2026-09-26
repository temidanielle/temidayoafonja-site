// Netlify function: /.netlify/functions/keep-the-proof-review
// Reached at /api/keep-the-proof-review through a 200 rewrite in netlify.toml.
//
// Receives the Keep the Proof review form at /review and does two things, in a
// fixed order:
//
//   1. Formspree, always. This is the system of record. It stores the answer,
//      emails the owner, and exports to CSV. If this fails, the visitor is told
//      and nothing else happens.
//   2. Kit, only when the visitor checked the opt in box. The check is made
//      here rather than in the browser, so a broken or scripted client cannot
//      add anybody to the list by accident.
//
// Why Kit is reached by tag rather than by sequence. The review page makes the
// same promise the Starter page already makes with its optional second box, so
// it reuses the tag that promise is already recorded against. That means no new
// Kit object and no new environment variable.
//
// Required env vars, all of them already set and proven by the working Starter
// form:
//   KIT_API_KEY                                Kit (ConvertKit) v3 API key
//   KIT_TAG_CAREER_EVIDENCE_STARTER_GUIDANCE   tag id for ongoing guidance
//
// Node 18+ (global fetch).

// The Formspree endpoint for the review form. Public by design, exactly like
// the eight in-page endpoints already used across this site, so it lives in
// code rather than in an environment variable. Keeping it here is what holds
// the owner's setup to a single step.
//
// REPLACE THE PLACEHOLDER BELOW WITH THE REAL FORM ID BEFORE LAUNCH.
// While the placeholder is present the function refuses every request with a
// 503, so a half configured page can never silently drop a review.
const FORMSPREE_ENDPOINT = "https://formspree.io/f/REPLACE_WITH_FORM_ID";

const REQUIRED_ENV = ["KIT_API_KEY", "KIT_TAG_CAREER_EVIDENCE_STARTER_GUIDANCE"];

const JSON_HEADERS = { "Content-Type": "application/json", "Cache-Control": "no-store" };
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type"
};

// Field caps. Long enough for a considered answer, short enough that the
// endpoint cannot be used to post a novel.
const CAP = {
  helpfulness: 40, how_acquired: 40, progress: 60, would_share: 12,
  quote_permission: 60, contact_name: 120, contact_title: 160, contact_email: 254,
  most_useful: 2000, confusing_or_missing: 2000, tell_a_colleague: 2000, proof_line: 2000
};

// Closed sets. Anything outside them is dropped rather than stored, so the
// export cannot be polluted with values the form never offered.
const ALLOWED = {
  helpfulness: ["Very helpful", "Somewhat helpful", "Not yet"],
  how_acquired: ["I bought it", "I received it as a gift"],
  progress: ["Read Start Here", "Finished my first session", "Wrote a full entry",
             "Wrote a Proof Line", "Used it in a real moment"],
  would_share: ["Yes", "Maybe", "No"],
  quote_permission: ["Yes, with my name and title",
                     "Yes, with my first name and last initial",
                     "No, this is private feedback"],
  used_for: ["Performance review", "Promotion", "Interview", "Resume",
             "Internal move", "Not yet", "Other"],
  work_field: ["Education", "Healthcare and life sciences", "Technology",
               "Financial services", "Consulting and professional services",
               "Government and nonprofit", "Other"],
  years_working: ["Under 5", "5 to 9", "10 to 19", "20 or more"]
};

// Builds the credit line for a quote, so the owner never has to assemble one by
// hand and never has to remember which form of the name each permission allows.
//
//   Full name permission:  name and title, or name and field when no title was
//                          given, or the name alone when neither was.
//   Initial permission:    first name, last initial, and field when one was
//                          given.
//
// "Other" is a real answer to the field question and is stored as one, but it
// credits nobody, so it is left out of the line rather than producing a credit
// reading "Jane S., Other".
function attributionLine(permission, name, title, field) {
  if (permission.indexOf("Yes") !== 0) return "";
  const full = name.trim();
  if (!full) return "";
  const usableField = field && field !== "Other" ? field : "";

  if (permission === "Yes, with my name and title") {
    if (title) return full + ", " + title;
    if (usableField) return full + ", " + usableField;
    return full;
  }

  // First name and last initial. A single-word name has no initial to add.
  const parts = full.split(/\s+/).filter(Boolean);
  let short = parts[0];
  if (parts.length > 1) {
    const last = parts[parts.length - 1];
    short = parts[0] + " " + last.charAt(0).toUpperCase() + ".";
  }
  return usableField ? short + ", " + usableField : short;
}

function str(v, max) {
  if (typeof v !== "string") return "";
  return v.trim().slice(0, max);
}
function oneOf(v, list) {
  const s = str(v, 200);
  return list.indexOf(s) >= 0 ? s : "";
}
function validEmail(v) {
  return typeof v === "string" && v.length <= 254 && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
}

exports.handler = async function (event) {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: CORS, body: "" };
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "method_not_allowed" }) };
  }

  // Configuration gate, before anything else is read.
  const missing = REQUIRED_ENV.filter((n) => !process.env[n]);
  const placeholder = FORMSPREE_ENDPOINT.indexOf("REPLACE_WITH_FORM_ID") >= 0;
  if (missing.length || placeholder) {
    console.error("keep-the-proof-review not configured.",
      missing.length ? "Missing env: " + missing.join(", ") + "." : "",
      placeholder ? "Formspree endpoint is still the placeholder." : "");
    return { statusCode: 503, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "not_configured" }) };
  }

  let p;
  try { p = JSON.parse(event.body || "{}"); }
  catch (e) {
    return { statusCode: 400, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "invalid_body" }) };
  }

  // Spam, both checks invisible to a real visitor.
  // The honeypot is a field only a script fills in. The elapsed time rejects a
  // submission that arrived faster than a person could have answered. Both
  // answer 422 so a bot learns nothing about which one caught it.
  if (str(p.company, 200) !== "") {
    return { statusCode: 422, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "rejected" }) };
  }
  const elapsed = Number(p.elapsed_ms);
  if (Number.isFinite(elapsed) && elapsed < 2000) {
    return { statusCode: 422, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "rejected" }) };
  }

  // The only required answer.
  const howAcquired = oneOf(p.how_acquired, ALLOWED.how_acquired);
  if (!howAcquired) {
    return { statusCode: 400, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "how_acquired_required" }) };
  }

  const quotePermission = oneOf(p.quote_permission, ALLOWED.quote_permission);
  const quoteIsYes = quotePermission.indexOf("Yes") === 0;
  const wantsFullName = quotePermission === "Yes, with my name and title";
  const optIn = p.email_optin === true;

  const contactName = str(p.contact_name, CAP.contact_name);
  const contactTitle = str(p.contact_title, CAP.contact_title);
  const contactEmail = str(p.contact_email, CAP.contact_email);

  // A quote cannot be published without a way to check it with its author, and
  // an email cannot be sent to an address that was never collected. Both are
  // enforced here as well as in the page.
  if (quoteIsYes && !contactName) {
    return { statusCode: 400, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "contact_name_required" }) };
  }
  // The job title is deliberately optional. A quote without one is credited
  // with the reader's field instead, which attributionLine handles.
  if ((quoteIsYes || optIn) && !validEmail(contactEmail)) {
    return { statusCode: 400, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "valid_email_required" }) };
  }

  const usedFor = Array.isArray(p.used_for)
    ? p.used_for.map((v) => oneOf(v, ALLOWED.used_for)).filter(Boolean).slice(0, ALLOWED.used_for.length)
    : [];

  const workField = oneOf(p.work_field, ALLOWED.work_field);
  const yearsWorking = oneOf(p.years_working, ALLOWED.years_working);

  const now = new Date();
  const record = {
    form: "keep-the-proof-review",
    page: "/review",
    submitted_at: now.toISOString(),
    helpfulness:          oneOf(p.helpfulness, ALLOWED.helpfulness),
    how_acquired:         howAcquired,
    progress:             oneOf(p.progress, ALLOWED.progress),
    used_for:             usedFor.join(", "),
    would_share:          oneOf(p.would_share, ALLOWED.would_share),
    work_field:           workField,
    years_working:        yearsWorking,
    most_useful:          str(p.most_useful, CAP.most_useful),
    confusing_or_missing: str(p.confusing_or_missing, CAP.confusing_or_missing),
    tell_a_colleague:     str(p.tell_a_colleague, CAP.tell_a_colleague),
    quote_permission:     quotePermission,
    // Only kept when the visitor gave a reason to keep it.
    contact_name:         (quoteIsYes || optIn) ? contactName : "",
    contact_title:        (quoteIsYes && wantsFullName) ? contactTitle : "",
    contact_email:        (quoteIsYes || optIn) ? contactEmail : "",
    // The credit line, ready to paste. Empty unless a quote was permitted.
    attribution:          attributionLine(
                            quotePermission,
                            quoteIsYes ? contactName : "",
                            wantsFullName ? contactTitle : "",
                            workField
                          ),
    proof_line:           str(p.proof_line, CAP.proof_line),
    email_optin:          optIn ? "true" : "false",
    // A gift review has to carry a disclosure wherever it is published. Marking
    // it on the record means the owner does not have to remember the rule.
    disclosure_required:  howAcquired === "I received it as a gift" ? "Received a complimentary copy" : ""
  };

  // 1. Formspree. The system of record, so a failure here is a failure overall.
  try {
    const res = await fetch(FORMSPREE_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(record)
    });
    if (!res.ok) {
      // Never echo the upstream body. It can repeat the submitted address.
      console.error("keep-the-proof-review: Formspree returned " + res.status);
      return { statusCode: 502, headers: { ...JSON_HEADERS, ...CORS },
               body: JSON.stringify({ error: "store_failed" }) };
    }
  } catch (e) {
    console.error("keep-the-proof-review: Formspree request threw.");
    return { statusCode: 502, headers: { ...JSON_HEADERS, ...CORS },
             body: JSON.stringify({ error: "store_failed" }) };
  }

  // 2. Kit, only on an explicit true. Best effort: the answer is already safely
  // stored, so a Kit failure must not turn a saved review into an error the
  // visitor sees. It is logged and reported in the response instead.
  let kitSubscribed = false;
  if (optIn) {
    try {
      const res = await fetch(
        "https://api.convertkit.com/v3/tags/" +
          encodeURIComponent(process.env.KIT_TAG_CAREER_EVIDENCE_STARTER_GUIDANCE) + "/subscribe",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            api_key: process.env.KIT_API_KEY,
            email: contactEmail,
            first_name: contactName ? contactName.split(/\s+/)[0] : undefined
          })
        }
      );
      kitSubscribed = res.ok;
      if (!res.ok) console.error("keep-the-proof-review: Kit returned " + res.status);
    } catch (e) {
      console.error("keep-the-proof-review: Kit request threw.");
    }
  }

  return {
    statusCode: 200,
    headers: { ...JSON_HEADERS, ...CORS },
    body: JSON.stringify({ ok: true, email_optin: optIn, kit_subscribed: kitSubscribed })
  };
};
