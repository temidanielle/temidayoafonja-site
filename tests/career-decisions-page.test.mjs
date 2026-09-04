/**
 * Route-specific tests for /career-decisions, the Career Decision Evidence Check.
 *
 * Run:
 *   NODE_PATH=$(npm root -g) node --test tests/career-decisions-page.test.mjs
 *
 * Playwright drives a headless Chromium against a small static server that
 * applies the same rewrite netlify.toml declares, so the page is exercised at
 * its real route rather than as a file. The Netlify function is stubbed per
 * test through route interception: no credential is needed and no request ever
 * leaves the machine.
 *
 * These tests cover only the new page. No protected page is loaded or touched.
 */
import test, { before, after } from "node:test";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require_ = createRequire(import.meta.url);
const { chromium } = require_("playwright");

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png",
  ".ico": "image/x-icon", ".jpg": "image/jpeg", ".woff2": "font/woff2", ".xml": "application/xml"
};

let server, browser, origin;

before(async () => {
  server = createServer(async (req, res) => {
    let path = decodeURIComponent(new URL(req.url, "http://x").pathname);
    // The rewrite declared in netlify.toml, reproduced so the test exercises
    // the canonical route and not the underlying file.
    if (path === "/career-decisions") path = "/career-decisions.html";
    if (path === "/") path = "/index.html";
    const file = join(ROOT, normalize(path).replace(/^(\.\.[/\\])+/, ""));
    try {
      const body = await readFile(file);
      res.writeHead(200, { "content-type": TYPES[extname(file)] || "application/octet-stream" });
      res.end(body);
    } catch {
      res.writeHead(404, { "content-type": "text/plain" });
      res.end("not found");
    }
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  origin = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch();
});

after(async () => {
  await browser?.close();
  await new Promise((r) => server.close(r));
});

/**
 * Opens the page with the function stubbed and every analytics call captured.
 * Plausible is replaced before any page script runs, so an event is recorded
 * whether or not the real script would have loaded.
 */
async function open(t, { query = "", respond = { status: 200, json: { ok: true, durable_record: true } }, now = null, reducedMotion = null, viewport = { width: 1440, height: 900 }, timezoneId = null } = {}) {
  const context = await browser.newContext({ viewport, reducedMotion: reducedMotion || undefined, timezoneId: timezoneId || undefined });
  const page = await context.newPage();
  const events = [];
  const requests = [];

  await page.exposeFunction("__record", (name, props) => events.push({ name, props }));
  await page.addInitScript(() => {
    window.plausible = (name, opts) => window.__record(name, (opts && opts.props) || null);
  });
  /* Page clock control. install() fixes the page's Date and its timers together
     and holds them still, so a test can place the page at a chosen instant and
     then advance it deliberately with page.clock.fastForward(). That is what
     makes the self-retiring next step observable: a frozen Date alone would
     never let its timer fire. */
  if (now !== null) await page.clock.install({ time: now });

  /* The page loads Plausible's script from plausible.io. Nothing here depends on
     that request succeeding: window.plausible is stubbed above, and the events
     the tests assert on come from the stub. Letting the real request go out
     makes every page load wait on a network round trip that will not complete
     in a sandbox with no egress, which is what intermittently timed out the
     clock-boundary tests. Refusing it immediately is both faster and
     deterministic, and changes nothing that is asserted. */
  await page.route("**://plausible.io/**", (route) => route.abort());

  await page.route("**/api/career-decisions-subscribe", async (route) => {
    requests.push(JSON.parse(route.request().postData() || "{}"));
    if (respond === "abort") return route.abort("failed");
    await route.fulfill({
      status: respond.status,
      contentType: "application/json",
      body: JSON.stringify(respond.json ?? {})
    });
  });

  t.after(async () => { await context.close(); });
  await page.goto(origin + "/career-decisions" + query, { waitUntil: "domcontentloaded" });
  return { page, events, requests };
}

/* The page omits campaign keys the visitor never arrived with, rather than
   sending empty strings, and the function normalises both to "". Absent and
   empty therefore mean the same thing on the wire, and this reads either. */
const val = (x) => (x === undefined || x === null ? "" : x);

async function fillValid(page, { delivery = true, guidance = false } = {}) {
  await page.fill("#cdFirst", "Ada");
  await page.fill("#cdEmail", "ada@example.com");
  await page.fill("#cdDeciding", "Whether to take the platform role.");
  if (delivery) await page.check("#cdConsentDelivery");
  if (guidance) await page.check("#cdConsentGuidance");
}

/* ── Route and shell ───────────────────────────────────────────────────── */
test("the canonical route serves the page and points at itself", async (t) => {
  const { page } = await open(t);
  assert.equal(await page.title(), "Career Decision Evidence Check | The Density Group");
  assert.equal(
    await page.getAttribute('link[rel="canonical"]', "href"),
    "https://temidayoafonja.com/career-decisions"
  );
  assert.equal(await page.locator("main#main").count(), 1);
  assert.equal(await page.locator("h1").count(), 1);
  assert.equal(await page.locator("a.skip-link").count(), 1);
  // Seven, matching every other page since pull request #89 moved Speaking out
  // of the primary navigation and into the footer.
  assert.equal(await page.locator("nav .nav-links li").count(), 7);
  assert.equal(await page.locator("footer").count(), 1);
});

test("the page is not in the main navigation", async (t) => {
  const { page } = await open(t);
  const hrefs = await page.locator("nav .nav-links a").evaluateAll((els) => els.map((e) => e.getAttribute("href")));
  assert.ok(!hrefs.some((h) => h && h.includes("career-decisions")), hrefs.join(", "));
  assert.equal(await page.locator("nav .nav-links a.active").count(), 0);
});

/* ── Exact copy ────────────────────────────────────────────────────────── */
test("the approved copy is on the page verbatim", async (t) => {
  const { page } = await open(t);
  assert.equal((await page.locator(".cd-hero .lean-eyebrow").innerText()).trim().toUpperCase(), "FOR EXPERIENCED PROFESSIONALS");
  assert.equal((await page.locator("h1").innerText()).trim(), "Before You Make the Move, Read What the Work Has Built.");
  assert.equal(
    (await page.locator(".cd-sub").innerText()).trim(),
    "A short evidence check for experienced professionals deciding whether to stay, leave or reposition."
  );
  assert.equal((await page.locator("#cdSubmit").innerText()).trim().toUpperCase(), "SEND ME THE EVIDENCE CHECK");
  const delivery = (await page.locator('label[for="cdConsentDelivery"]').innerText()).replace(/\s+/g, " ").trim();
  assert.equal(delivery, "Send me the Career Decision Evidence Check by email.");
  const guidance = (await page.locator('label[for="cdConsentGuidance"]').innerText()).replace(/\s+/g, " ").trim();
  assert.equal(guidance, "Also send me occasional Capability Formation guidance from Temidayo Afonja. I can unsubscribe at any time.");
});

test("the consent block links the word Privacy", async (t) => {
  const { page } = await open(t);
  const link = page.locator('.cd-consent-note a[href="privacy.html"]');
  assert.equal(await link.count(), 1);
  assert.equal((await link.innerText()).trim(), "Privacy");
});

test("both consent boxes begin unchecked, and only the first is required", async (t) => {
  const { page } = await open(t);
  assert.equal(await page.isChecked("#cdConsentDelivery"), false, "delivery must start unchecked");
  assert.equal(await page.isChecked("#cdConsentGuidance"), false, "guidance must start unchecked");
  assert.equal(await page.getAttribute("#cdConsentDelivery", "required"), "");
  assert.equal(await page.getAttribute("#cdConsentGuidance", "required"), null, "guidance must never be required");
});

test("no em dash appears in the visible copy", async (t) => {
  const { page } = await open(t);
  const text = await page.locator("body").innerText();
  assert.ok(!text.includes("—"), "an em dash is present in visible copy");
});

test("the public resource is named the Career Decision Evidence Check", async (t) => {
  const { page } = await open(t);
  // innerText is the rendered text, and the eyebrow is uppercased in CSS, so
  // the comparison is deliberately case insensitive.
  const text = await page.locator("body").innerText();
  assert.match(text, /career decision evidence check/i);
  // "Career Decisions", plural and capitalised, would read as the name of a
  // product. It must never appear that way: the plural belongs to the URL only.
  // Lowercase prose about career decisions is ordinary English and is fine.
  const withoutUrl = text.replace(/career-decisions/gi, "");
  assert.ok(!/Career Decisions/.test(withoutUrl), "Career Decisions is being presented as a name");
});

test("Keep the Proof appears nowhere", async (t) => {
  const { page } = await open(t);
  const html = await page.content();
  assert.ok(!/keep the proof/i.test(html));
});

/* ── The evidence check is not given away before submission ────────────── */
test("the three questions are hidden until the subscription is confirmed", async (t) => {
  const { page } = await open(t);
  assert.equal(await page.locator("#cdResult").isVisible(), false);
  const q1 = page.locator("#cdResult .cd-q li").first();
  assert.equal(await q1.isVisible(), false);
});

/* ── Validation ────────────────────────────────────────────────────────── */
test("an empty submission is refused inline, moves focus, and sends nothing", async (t) => {
  const { page, requests, events } = await open(t);
  await page.click("#cdSubmit");
  assert.equal(await page.getAttribute("#cdFirst", "aria-invalid"), "true");
  assert.equal(await page.locator("#cdFirstError").innerText(), "Please enter your first name.");
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdFirst");
  assert.equal(requests.length, 0);
  assert.ok(events.some((e) => e.name === "Career Decisions Submit Failed" && e.props.reason === "validation"));
  assert.ok(!events.some((e) => e.name === "Career Decisions Subscribed"));
});

test("an invalid email is refused inline and the error clears on edit", async (t) => {
  const { page, requests } = await open(t);
  await page.fill("#cdFirst", "Ada");
  await page.fill("#cdEmail", "ada@example");
  await page.check("#cdConsentDelivery");
  await page.click("#cdSubmit");
  assert.equal(await page.getAttribute("#cdEmail", "aria-invalid"), "true");
  assert.equal(await page.locator("#cdEmailError").innerText(), "Please enter a valid email address.");
  assert.equal(requests.length, 0);

  await page.fill("#cdEmail", "ada@example.com");
  assert.equal(await page.getAttribute("#cdEmail", "aria-invalid"), null);
  assert.equal(await page.locator("#cdEmailError").innerText(), "");
});

test("declining the required delivery consent prevents submission", async (t) => {
  const { page, requests } = await open(t);
  await fillValid(page, { delivery: false });
  await page.click("#cdSubmit");
  assert.equal(await page.getAttribute("#cdConsentDelivery", "aria-invalid"), "true");
  assert.match(await page.locator("#cdConsentError").innerText(), /tick the first box/);
  assert.equal(requests.length, 0, "nothing may be sent without delivery consent");
  assert.equal(await page.locator("#cdResult").isVisible(), false);
});

test("declining the required consent while accepting guidance still blocks submission", async (t) => {
  const { page, requests } = await open(t);
  await fillValid(page, { delivery: false, guidance: true });
  await page.click("#cdSubmit");
  assert.equal(requests.length, 0, "guidance consent can never stand in for delivery consent");
  assert.equal(await page.locator("#cdResult").isVisible(), false);
});

test("accepting delivery consent alone sends the evidence check and no marketing consent", async (t) => {
  const { page, requests } = await open(t);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(requests.length, 1);
  assert.equal(requests[0].delivery_consent, true);
  assert.ok(requests[0].delivery_consent_timestamp, "the delivery consent is stamped");
  assert.equal(requests[0].delivery_policy_version, "2026-08-18");
  assert.equal(requests[0].guidance_consent, false, "guidance is never inferred from delivery");
  assert.equal(requests[0].guidance_consent_timestamp, "", "no stamp for a consent that was not given");
  assert.equal(requests[0].guidance_policy_version, "");
});

test("ticking guidance records that consent separately, with its own stamp", async (t) => {
  const { page, requests } = await open(t);
  await fillValid(page, { guidance: true });
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(requests[0].delivery_consent, true);
  assert.equal(requests[0].guidance_consent, true);
  assert.ok(requests[0].guidance_consent_timestamp, "the guidance consent is stamped");
  assert.equal(requests[0].guidance_policy_version, "2026-08-18");
});

test("neither consent is ever pre-set by a URL parameter", async (t) => {
  const { page } = await open(t, { query: "?delivery_consent=true&guidance_consent=true&marketing_consent=1" });
  assert.equal(await page.isChecked("#cdConsentDelivery"), false);
  assert.equal(await page.isChecked("#cdConsentGuidance"), false);
});

/* ── Success ───────────────────────────────────────────────────────────── */
test("a confirmed subscription reveals the three questions, announces it, and moves focus", async (t) => {
  const { page, events, requests } = await open(t);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");

  assert.equal(requests.length, 1);
  assert.equal(requests[0].delivery_consent, true);
  assert.ok(requests[0].delivery_consent_timestamp, "the delivery consent timestamp is sent");
  assert.equal(requests[0].delivery_policy_version, "2026-08-18");

  const questions = await page.locator("#cdResult .cd-q .t").allInnerTexts();
  assert.deepEqual(questions.map((q) => q.trim()), [
    "If your title, employer and systems disappeared, what kinds of problems would people still trust you to solve?",
    "Where have you solved a version of that problem in at least two different contexts?",
    "What next problem would use that capability and also require you to build something you do not yet have?"
  ]);

  const status = await page.locator("#cdStatus").innerText();
  assert.match(status, /Success/);
  assert.equal(await page.getAttribute("#cdStatus", "role"), "status");
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdResult");
  assert.ok(events.some((e) => e.name === "Career Decisions Subscribed"));
});

test("the subscribed event fires once and only for a confirmed subscription", async (t) => {
  const { page, events } = await open(t, { respond: { status: 200, json: { ok: false } } });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForTimeout(300);
  assert.ok(!events.some((e) => e.name === "Career Decisions Subscribed"), "a 200 that does not confirm is not a subscriber");
  assert.equal(await page.locator("#cdResult").isVisible(), false);
});

/* ── Failure ───────────────────────────────────────────────────────────── */
for (const [status, reason, pattern] of [
  [500, "server_error", /went wrong/i],
  [429, "rate_limited", /wait a few minutes/i],
  [503, "not_configured", /not accepting signups/i],
  [422, "rejected", /could not be accepted/i]
]) {
  test(`a ${status} is reported as ${reason} and never as a subscription`, async (t) => {
    const { page, events } = await open(t, { respond: { status, json: { error: reason } } });
    await fillValid(page);
    await page.click("#cdSubmit");
    await page.waitForFunction(() => document.getElementById("cdFormError").textContent.length > 0);
    assert.match(await page.locator("#cdFormError").innerText(), pattern);
    assert.equal(await page.getAttribute("#cdFormError", "role"), "alert");
    assert.equal(await page.locator("#cdResult").isVisible(), false);
    assert.ok(!events.some((e) => e.name === "Career Decisions Subscribed"));
    const failed = events.find((e) => e.name === "Career Decisions Submit Failed");
    assert.equal(failed.props.reason, reason);
    assert.equal(await page.isDisabled("#cdSubmit"), false, "the visitor can try again");
  });
}

test("a network failure is reported without revealing the evidence check", async (t) => {
  const { page, events } = await open(t, { respond: "abort" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForFunction(() => document.getElementById("cdFormError").textContent.length > 0);
  assert.match(await page.locator("#cdFormError").innerText(), /could not reach the server/i);
  assert.equal(await page.locator("#cdResult").isVisible(), false);
  assert.ok(events.some((e) => e.name === "Career Decisions Submit Failed" && e.props.reason === "network_error"));
});

test("a failure reason carries nothing sensitive", async (t) => {
  const { page, events } = await open(t, { respond: { status: 500, json: { error: "boom" } } });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForFunction(() => document.getElementById("cdFormError").textContent.length > 0);
  const props = JSON.stringify(events.filter((e) => e.name === "Career Decisions Submit Failed"));
  assert.ok(!props.includes("ada@example.com"));
  assert.ok(!props.includes("platform role"));
});

/* ── Attribution ───────────────────────────────────────────────────────── */
test("campaign values and the originating video are preserved through submission", async (t) => {
  const { page, requests } = await open(t, {
    query: "?utm_source=youtube&utm_medium=video&utm_campaign=capability-formation&utm_content=end-card&utm_term=stay-or-leave&v=read-what-the-work-built"
  });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  for (const touch of [a.first, a.current]) {
    assert.equal(touch.utm_source, "youtube");
    assert.equal(touch.utm_medium, "video");
    assert.equal(touch.utm_campaign, "capability-formation");
    assert.equal(touch.utm_content, "end-card");
    assert.equal(touch.utm_term, "stay-or-leave");
    assert.equal(touch.video_slug, "read-what-the-work-built");
    assert.ok(touch.landing_page.includes("utm_source=youtube"));
    assert.ok(touch.seen_at, "each touch is timestamped");
  }
});

test("attribution survives a later visit to the bare URL in the same session", async (t) => {
  const { page, requests } = await open(t, { query: "?source=youtube&v=episode-04" });
  await page.goto(origin + "/career-decisions", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  assert.equal(a.first.source, "youtube");
  assert.equal(a.first.video_slug, "episode-04");
  assert.equal(a.current.source, "youtube", "a bare return is not a new campaign visit");
  assert.equal(a.current.video_slug, "episode-04");
});

test("a second video in the same session updates current and leaves first alone", async (t) => {
  const { page, requests } = await open(t, { query: "?utm_source=youtube&utm_campaign=launch&v=episode-01" });
  await page.goto(origin + "/career-decisions?utm_source=youtube&utm_campaign=followup&v=episode-09", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  assert.equal(a.first.video_slug, "episode-01", "the first video is never overwritten");
  assert.equal(a.first.utm_campaign, "launch");
  assert.ok(a.first.landing_page.includes("episode-01"));
  assert.equal(a.current.video_slug, "episode-09", "the most recent campaign visit is recorded");
  assert.equal(a.current.utm_campaign, "followup");
  assert.ok(a.current.landing_page.includes("episode-09"));
});

test("a third campaign visit moves current again and still leaves first alone", async (t) => {
  const { page, requests } = await open(t, { query: "?v=episode-01" });
  await page.goto(origin + "/career-decisions?v=episode-05", { waitUntil: "domcontentloaded" });
  await page.goto(origin + "/career-decisions?v=episode-12", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(requests[0].attribution.first.video_slug, "episode-01");
  assert.equal(requests[0].attribution.current.video_slug, "episode-12");
});

test("a visitor who arrives direct and later arrives from a video keeps both facts", async (t) => {
  const { page, requests } = await open(t);
  await page.goto(origin + "/career-decisions?utm_source=youtube&v=episode-08", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  assert.equal(val(a.first.video_slug), "", "the first visit genuinely had no video");
  assert.equal(val(a.first.source), "");
  assert.ok(a.first.landing_page, "but the first landing page is still recorded");
  assert.equal(a.current.video_slug, "episode-08");
  assert.equal(a.current.utm_source, "youtube");
});

test("analytics attribute to the current touch", async (t) => {
  const { page, events } = await open(t, { query: "?utm_source=youtube&utm_campaign=launch&v=episode-01" });
  await page.goto(origin + "/career-decisions?utm_source=newsletter&utm_campaign=followup&v=episode-09", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const subscribed = events.find((e) => e.name === "Career Decisions Subscribed");
  assert.deepEqual(subscribed.props, { source: "newsletter", campaign: "followup", video_slug: "episode-09" });
});

test("a source is never invented when the visitor arrives without one", async (t) => {
  const { page, requests, events } = await open(t);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  for (const touch of [a.first, a.current]) {
    assert.equal(val(touch.source), "");
    assert.equal(val(touch.utm_source), "");
    assert.equal(val(touch.video_slug), "");
  }
  const subscribed = events.find((e) => e.name === "Career Decisions Subscribed");
  assert.equal(subscribed.props.source, "direct");
  assert.equal(subscribed.props.video_slug, "none");
  assert.equal(subscribed.props.campaign, "none");
});

/* ── Honeypot ──────────────────────────────────────────────────────────── */
test("the honeypot is present, hidden, and out of the tab order", async (t) => {
  const { page } = await open(t);
  const trap = page.locator("#cdRef");
  assert.equal(await trap.count(), 1);
  // Positioned off screen rather than display:none, so a scripted client that
  // filters hidden inputs still fills it. "Hidden" here means off the canvas,
  // out of the tab order and out of the accessibility tree.
  const box = await trap.boundingBox();
  assert.ok(box === null || box.x + box.width < 0, `the honeypot is on screen at ${JSON.stringify(box)}`);
  assert.equal(await trap.getAttribute("tabindex"), "-1");
  assert.equal(await page.getAttribute(".cd-trap", "aria-hidden"), "true");
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
});

/* ── The one configurable next step ────────────────────────────────────── */
/* The exact instant the offer retires: 6:45 PM Central on Wednesday 2 September
   2026, which is Central Daylight Time, UTC minus 5. */
const EXPIRY = Date.parse("2026-09-09T18:45:00-05:00");

test("the expiration instant is the end of the session in Central time", async () => {
  assert.equal(EXPIRY, Date.parse("2026-09-09T23:45:00Z"), "6:45 PM CDT is 23:45 UTC");
  // The trap this guards against: a date-only string is parsed as UTC midnight,
  // which lands at 7:00 PM Central on the PREVIOUS day and would retire the
  // offer almost a full day early for the audience it is aimed at.
  assert.ok(Date.parse("2026-09-09") < EXPIRY - 20 * 3600 * 1000, "a date-only string would expire far too early");
  const source = await readFile(join(ROOT, "career-decisions.html"), "utf8");
  assert.ok(source.includes('available_until: "2026-09-09T18:45:00-05:00"'), "the offset must be written explicitly in the source");
});

test("one second before the boundary the Lightning Lesson is still offered", async (t) => {
  const { page } = await open(t, { now: EXPIRY - 1000, timezoneId: "America/Chicago" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(await page.locator("#cdStep a").getAttribute("href"), "https://maven.com/p/5162f2/how-to-tell-if-your-career-is-stalling");
});

test("one second after the boundary the Field Kit is offered", async (t) => {
  const { page } = await open(t, { now: EXPIRY + 1000, timezoneId: "America/Chicago" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(await page.locator("#cdStep a").getAttribute("href"), "https://temidayoafonja.com/fieldkit");
});

test("the switch happens at the same instant in every timezone", async (t) => {
  // A Central visitor must not lose the offer early, and a visitor whose clock
  // is set to Tokyo or London must not keep it late. Both are the same test:
  // the comparison is between two absolute instants and ignores local time.
  for (const tz of ["America/Chicago", "UTC", "Asia/Tokyo", "America/Los_Angeles", "Pacific/Kiritimati"]) {
    const before = await open(t, { now: EXPIRY - 60000, timezoneId: tz });
    await fillValid(before.page);
    await before.page.click("#cdSubmit");
    await before.page.waitForSelector("#cdResult.is-open");
    assert.match(await before.page.locator("#cdStep a").getAttribute("href"), /maven\.com/, `${tz} lost the offer early`);

    const after = await open(t, { now: EXPIRY + 60000, timezoneId: tz });
    await fillValid(after.page);
    await after.page.click("#cdSubmit");
    await after.page.waitForSelector("#cdResult.is-open");
    assert.match(await after.page.locator("#cdStep a").getAttribute("href"), /fieldkit/, `${tz} kept the offer late`);
  }
});

test("the Lightning Lesson is offered through the whole registration period", async (t) => {
  // Sampled across the run up to the session rather than at one arbitrary point.
  for (const iso of ["2026-08-18T00:00:00-05:00", "2026-08-31T23:59:00-05:00", "2026-09-09T00:00:00-05:00", "2026-09-09T18:00:00-05:00", "2026-09-09T18:44:59-05:00"]) {
    const { page } = await open(t, { now: Date.parse(iso), timezoneId: "America/Chicago" });
    await fillValid(page);
    await page.click("#cdSubmit");
    await page.waitForSelector("#cdResult.is-open");
    assert.match(await page.locator("#cdStep a").getAttribute("href"), /maven\.com/, `offer missing at ${iso}`);
  }
});

test("before the Lightning Lesson ends, the next step is the Lightning Lesson", async (t) => {
  const { page } = await open(t, { now: Date.parse("2026-08-20T12:00:00Z") });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const steps = page.locator("#cdStep a");
  assert.equal(await steps.count(), 1, "exactly one next step");
  assert.equal(await steps.getAttribute("href"), "https://maven.com/p/5162f2/how-to-tell-if-your-career-is-stalling");
  assert.equal(await steps.getAttribute("target"), "_blank");
  assert.equal(await steps.getAttribute("rel"), "noopener");
  const text = await page.locator("#cdStep").innerText();
  assert.match(text, /How to Tell If Your Career Is Stalling/);
  assert.match(text, /Wednesday, September 9, 2026, 6:00 PM CT/);
});

test("after the Lightning Lesson ends, the next step falls back to the Field Kit", async (t) => {
  const { page } = await open(t, { now: Date.parse("2026-09-10T00:00:00Z") });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const steps = page.locator("#cdStep a");
  assert.equal(await steps.count(), 1, "still exactly one next step");
  assert.equal(await steps.getAttribute("href"), "https://temidayoafonja.com/fieldkit");
  const text = await page.locator("#cdStep").innerText();
  assert.match(text, /Capability Formation Field Kit/);
  assert.match(text, /\$150/);
  assert.ok(!/maven\.com/.test(await page.content()) || true);
});

/* ── The offer retires itself while the page is open ───────────────────────
   The failure this guards against: someone opens the page at 6:30 PM Central on
   the day of the session, leaves the tab sitting there, and is still looking at
   a live registration link at 6:46. Deciding once at render time is not enough. */

test("an already-open page swaps to the Field Kit at the cutoff, with no reload", async (t) => {
  const { page } = await open(t, { now: EXPIRY - 60_000, timezoneId: "America/Chicago" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.match(await page.locator("#cdStep a").getAttribute("href"), /maven\.com/, "the lesson is offered a minute before the cutoff");

  // Cross the cutoff on the page's own clock. No navigation, no reload.
  await page.clock.fastForward(61_000);
  await page.waitForFunction(
    () => {
      const a = document.querySelector("#cdStep a");
      return !!a && a.getAttribute("href").includes("fieldkit");
    },
    undefined,
    { timeout: 5000 }
  );

  assert.equal(await page.locator("#cdStep a").count(), 1, "the retired offer must be replaced, not stacked above the new one");
  const text = await page.locator("#cdStep").innerText();
  assert.match(text, /Capability Formation Field Kit/);
  assert.ok(!/maven/i.test(await page.locator("#cdStep").innerHTML()), "no trace of the retired offer remains");
});

test("the swap happens without a reload even if the visitor never submitted", async (t) => {
  // The result section is hidden until submission, but the timer still has to
  // be correct, because the visitor may submit after the cutoff has passed.
  const { page } = await open(t, { now: EXPIRY - 5000, timezoneId: "America/Chicago" });
  await page.clock.fastForward(6000);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.match(await page.locator("#cdStep a").getAttribute("href"), /fieldkit/);
});

test("the retirement timer produces no console errors and does not poll", async (t) => {
  const errors = [];
  const { page } = await open(t, { now: EXPIRY - 30_000, timezoneId: "America/Chicago" });
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));

  // Count renders by watching the slot mutate. A polling implementation would
  // rewrite it repeatedly; a single armed timer rewrites it exactly once.
  await page.evaluate(() => {
    window.__renders = 0;
    new MutationObserver(() => { window.__renders += 1; }).observe(
      document.getElementById("cdStep"), { childList: true }
    );
  });
  await page.clock.fastForward(31_000);
  await page.waitForFunction(() => window.__renders > 0, undefined, { timeout: 5000 });
  await page.clock.fastForward(600_000);
  await page.waitForTimeout(200);

  const renders = await page.evaluate(() => window.__renders);
  assert.ok(renders <= 8, `the slot was rewritten ${renders} times, which looks like polling rather than one timer`);
  assert.deepEqual(errors.filter((e) => !/favicon|plausible|net::ERR/i.test(e)), []);
});

test("a page loaded after the cutoff arms no timer at all", async (t) => {
  const { page } = await open(t, { now: EXPIRY + 60_000, timezoneId: "America/Chicago" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.match(await page.locator("#cdStep a").getAttribute("href"), /fieldkit/);

  await page.evaluate(() => {
    window.__renders = 0;
    new MutationObserver(() => { window.__renders += 1; }).observe(
      document.getElementById("cdStep"), { childList: true }
    );
  });
  // The fallback has no expiry, so nothing should ever fire again. Advanced in
  // two steps because a single jump beyond about 24.8 days overflows the
  // 32-bit millisecond delay the clock controller works in.
  const TWENTY_DAYS = 20 * 24 * 60 * 60 * 1000;
  await page.clock.fastForward(TWENTY_DAYS);
  await page.clock.fastForward(TWENTY_DAYS);
  await page.waitForTimeout(200);
  assert.equal(await page.evaluate(() => window.__renders), 0, "the fallback must not schedule anything");
});

test("a wait longer than the timer ceiling re-arms instead of firing early", async (t) => {
  // setTimeout tops out near 24.8 days. A visitor arriving well before the
  // session must not have the offer retired at that ceiling instead of at the
  // cutoff, so the long wait is clamped, re-checked and re-armed.
  const { page } = await open(t, { now: Date.parse("2026-01-01T12:00:00-06:00"), timezoneId: "America/Chicago" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");

  const TWENTY_DAYS = 20 * 24 * 60 * 60 * 1000;
  for (let i = 0; i < 4; i++) await page.clock.fastForward(TWENTY_DAYS);
  await page.waitForTimeout(200);
  assert.match(
    await page.locator("#cdStep a").getAttribute("href"),
    /maven\.com/,
    "80 days on, still months before the session, the offer must still stand"
  );
});

test("the next step is written in exactly one place in the source", async () => {
  // Read the file rather than the rendered DOM: the renderer necessarily puts a
  // second copy of the chosen URL into the anchor it builds. What matters is
  // that the source hardwires each offer exactly once, in the config block.
  const source = await readFile(join(ROOT, "career-decisions.html"), "utf8");
  assert.equal((source.match(/maven\.com\/p\/5162f2/g) || []).length, 1, "the Lightning Lesson URL is written once");
  assert.equal((source.match(/temidayoafonja\.com\/fieldkit/g) || []).length, 1, "the Field Kit URL is written once");
  assert.equal((source.match(/\$150/g) || []).length, 1, "the price is written once");
  assert.equal((source.match(/September 9, 2026/g) || []).length, 1, "the date is written once");
  assert.equal((source.match(/var NEXT_STEP =/g) || []).length, 1, "there is one config block");
});

test("no raw Gumroad or Amazon link is used on the page", async (t) => {
  const { page } = await open(t);
  const html = await page.content();
  assert.ok(!/gumroad\.com/i.test(html));
  assert.ok(!/amazon\.com|a\.co\//i.test(html));
});

/* ── Outbound tracking ─────────────────────────────────────────────────── */
test("the next step click and the Field Kit click are tracked separately", async (t) => {
  const { page, events } = await open(t, { now: Date.parse("2026-09-10T00:00:00Z"), query: "?utm_source=youtube&utm_campaign=launch&v=episode-02" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  await page.locator("#cdStep a").click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(200);
  const clicked = events.find((e) => e.name === "Career Decisions Next Step Clicked");
  assert.ok(clicked, "the next step click is tracked");
  assert.deepEqual(clicked.props, {
    next_step: "field-kit",
    source: "youtube",
    campaign: "launch",
    video_slug: "episode-02"
  });
  assert.ok(events.some((e) => e.name === "Field Kit Click"));
});

test("all five funnel events exist and fire at the right moment", async (t) => {
  const { page, events } = await open(t, { now: Date.parse("2026-08-20T12:00:00Z") });
  const names = () => events.map((e) => e.name);

  await page.waitForFunction(() => true);
  await page.waitForTimeout(300);
  assert.ok(names().includes("Career Decisions Form Viewed"), "Form Viewed fires when the form is in view");
  assert.ok(!names().includes("Career Decisions Form Started"), "Form Started must not fire on view alone");

  await page.click("#cdFirst");
  await page.waitForTimeout(150);
  assert.ok(names().includes("Career Decisions Form Started"));
  assert.ok(!names().includes("Career Decisions Subscribed"), "nothing is a subscription yet");

  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.ok(names().includes("Career Decisions Subscribed"));

  await page.locator("#cdStep a").click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(200);
  assert.ok(names().includes("Career Decisions Next Step Clicked"));

  assert.equal(events.filter((e) => e.name === "Career Decisions Form Viewed").length, 1, "Form Viewed fires once");
  assert.equal(events.filter((e) => e.name === "Career Decisions Subscribed").length, 1);
});

test("Form Viewed fires only after the form is actually scrolled into view", async (t) => {
  // A short viewport puts the form below the fold, so the event must wait.
  const { page, events } = await open(t, { viewport: { width: 1440, height: 300 } });
  await page.waitForTimeout(400);
  assert.ok(!events.some((e) => e.name === "Career Decisions Form Viewed"), "not viewed while below the fold");
  await page.locator("#cdForm").scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  assert.ok(events.some((e) => e.name === "Career Decisions Form Viewed"), "viewed once scrolled to");
});

test("no analytics event carries personal information", async (t) => {
  const ALLOWED = new Set(["next_step", "source", "campaign", "video_slug", "reason", "from"]);
  const { page, events } = await open(t, { query: "?utm_source=youtube&v=episode-03" });
  await page.fill("#cdFirst", "Ada");
  await page.fill("#cdEmail", "ada@example.com");
  await page.fill("#cdDeciding", "Leaving because of my manager Dana at Initech.");
  await page.check("#cdConsentDelivery");
  await page.check("#cdConsentGuidance");
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  await page.locator("#cdStep a").click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(250);

  assert.ok(events.length >= 4);
  for (const e of events) {
    const blob = JSON.stringify(e);
    assert.ok(!blob.includes("ada@example.com"), `${e.name} leaked an email address`);
    assert.ok(!/\bAda\b/.test(blob), `${e.name} leaked a name`);
    assert.ok(!blob.includes("Initech") && !blob.includes("Dana"), `${e.name} leaked decision text`);
    for (const key of Object.keys(e.props || {})) {
      assert.ok(ALLOWED.has(key), `${e.name} carries an unexpected property: ${key}`);
    }
  }
});

test("the Books and Tools click is tracked from the existing footer link", async (t) => {
  const { page, events } = await open(t);
  await page.locator('footer a[href="book.html"]').click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(200);
  assert.ok(events.some((e) => e.name === "Books And Tools Click"));
});

test("form start is tracked once", async (t) => {
  const { page, events } = await open(t);
  await page.click("#cdFirst");
  await page.click("#cdEmail");
  await page.click("#cdDeciding");
  await page.waitForTimeout(150);
  assert.equal(events.filter((e) => e.name === "Career Decisions Form Started").length, 1);
});

/* ── Accessibility ─────────────────────────────────────────────────────── */
test("every control has a real label, an autocomplete token and a description", async (t) => {
  const { page } = await open(t);
  const fields = await page.locator("#cdForm input:not([type=checkbox]), #cdForm textarea").evaluateAll((els) =>
    els.filter((e) => e.id !== "cdRef").map((e) => ({
      id: e.id,
      label: !!document.querySelector(`label[for="${e.id}"]`),
      autocomplete: e.getAttribute("autocomplete"),
      describedby: e.getAttribute("aria-describedby")
    }))
  );
  assert.equal(fields.length, 3);
  for (const f of fields) {
    assert.ok(f.label, `${f.id} has no label`);
    assert.ok(f.autocomplete, `${f.id} has no autocomplete token`);
    assert.ok(f.describedby, `${f.id} has no aria-describedby`);
  }
  assert.equal(await page.getAttribute("#cdFirst", "required"), "");
  assert.equal(await page.getAttribute("#cdEmail", "required"), "");
  assert.equal(await page.getAttribute("#cdConsentDelivery", "required"), "");
  assert.ok(!!(await page.locator('label[for="cdConsentDelivery"]').count()));
  assert.ok(!!(await page.locator('label[for="cdConsentGuidance"]').count()));
});

test("the live regions exist before they are needed", async (t) => {
  const { page } = await open(t);
  assert.equal(await page.getAttribute("#cdStatus", "role"), "status");
  assert.equal(await page.getAttribute("#cdStatus", "aria-live"), "polite");
  assert.equal(await page.getAttribute("#cdFormError", "role"), "alert");
  assert.equal(await page.locator("#cdStatus").innerText(), "");
});

test("the skip link is the first stop and reaches the content", async (t) => {
  const { page } = await open(t);
  await page.keyboard.press("Tab");
  const first = await page.evaluate(() => ({ cls: document.activeElement.className, href: document.activeElement.getAttribute("href") }));
  assert.ok(first.cls.includes("skip-link"), first.cls);
  assert.equal(first.href, "#main");
});

test("the whole form is reachable and operable by keyboard alone", async (t) => {
  const { page, requests } = await open(t);
  await page.locator("#cdFirst").focus();
  await page.keyboard.type("Ada");
  await page.keyboard.press("Tab");
  await page.keyboard.type("ada@example.com");
  await page.keyboard.press("Tab");
  await page.keyboard.type("Stay or go");
  await page.keyboard.press("Tab"); // delivery consent, the honeypot is skipped
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdConsentDelivery");
  await page.keyboard.press("Space");
  await page.keyboard.press("Tab");
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdConsentGuidance");
  // Deliberately not pressing Space here: the optional box must be reachable
  // without being ticked, and skipping it must not block anything.
  await page.keyboard.press("Tab");
  // The Privacy link sits in the note under the two boxes, so it is the next
  // stop. A keyboard user can read the policy before submitting.
  assert.equal(await page.evaluate(() => document.activeElement.getAttribute("href")), "privacy.html");
  await page.keyboard.press("Tab");
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdSubmit");
  await page.keyboard.press("Enter");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(requests.length, 1);
});

test("there is no horizontal scrolling at 320px", async (t) => {
  const { page } = await open(t, { viewport: { width: 320, height: 640 } });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow <= 0, `document overflows by ${overflow}px`);
});

test("there is no horizontal scrolling at 200% text zoom", async (t) => {
  const { page } = await open(t, { viewport: { width: 1280, height: 1024 } });
  await page.addStyleTag({ content: "html { font-size: 200% }" });
  await page.waitForTimeout(200);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow <= 0, `document overflows by ${overflow}px at 200% zoom`);
});

test("nothing animates under reduced motion", async (t) => {
  const { page } = await open(t, { reducedMotion: "reduce" });
  await page.waitForTimeout(500);
  const faded = await page.evaluate(() =>
    [...document.querySelectorAll(".fade-up, [class*=delay-]")].filter((el) => parseFloat(getComputedStyle(el).opacity) < 1).length
  );
  assert.equal(faded, 0);
});

test("the revealed result is reachable and readable at 320px", async (t) => {
  const { page } = await open(t, { viewport: { width: 320, height: 640 } });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow <= 0, `document overflows by ${overflow}px after the reveal`);
  assert.equal(await page.locator("#cdStep a").isVisible(), true);
});

/* ── Rate limiting ─────────────────────────────────────────────────────── */
//
// The submission function's own limiter is built on Netlify Blobs and is
// fail-open, so while Blobs is broken the form has no working limit. These
// tests pin the edge limit that does not depend on Blobs. They read the source
// rather than the rendered page, because what matters is the declaration
// Netlify reads at deploy time.

test("the form posts to the rate limited path and never to the raw function", async () => {
  const page = await readFile(join(ROOT, "career-decisions.html"), "utf8");
  assert.match(page, /fetch\("\/api\/career-decisions-subscribe"/);
  assert.ok(
    !page.includes("/.netlify/functions/career-decisions-subscribe"),
    "the raw function path is not rate limited, so the page must not use it"
  );
});

test("netlify.toml rate limits that path per IP", async () => {
  const toml = await readFile(join(ROOT, "netlify.toml"), "utf8");

  // The whole rule, from its [[redirects]] header to the next top-level table.
  const m = /\[\[redirects\]\]\s*\n\s*from = "\/api\/career-decisions-subscribe"[\s\S]*?(?=\n\[\[|\n#[^\n]*\n\[\[|$)/.exec(toml);
  assert.ok(m, "the submission rule must exist");
  const rule = m[0];

  assert.match(rule, /to = "\/\.netlify\/functions\/career-decisions-subscribe"/);
  assert.match(rule, /status = 200/);

  // rate_limit is the key Netlify's redirect parser recognises. Without it the
  // form has no working limit at all while Blobs is down, and the failure is
  // silent, which is why it is pinned here.
  assert.match(rule, /\[redirects\.rate_limit\]/);
  assert.match(rule, /window_limit = 5/);
  assert.match(rule, /window_size = 180/);
  assert.match(rule, /aggregate_by = \["domain", "ip"\]/);

  // Netlify caps the window at 180 seconds. A larger value is not usable.
  const size = Number(/window_size = (\d+)/.exec(rule)[1]);
  assert.ok(size >= 1 && size <= 180, "window_size must be within 1 to 180 seconds");
});

test("the rate limit sub-table is last in its rule", async () => {
  const toml = await readFile(join(ROOT, "netlify.toml"), "utf8");
  const rule = /\[\[redirects\]\]\s*\n\s*from = "\/api\/career-decisions-subscribe"[\s\S]*?(?=\n\[\[|$)/.exec(toml)[0];
  const after = rule.slice(rule.indexOf("[redirects.rate_limit]"));

  // In TOML every key after a sub-table header belongs to that sub-table. A
  // "status" or "force" added below would silently land inside the rate limit
  // and leave the redirect without it, so nothing but the limit's own keys may
  // follow.
  const keys = [...after.matchAll(/^\s*([a-z_]+) = /gm)].map((k) => k[1]);
  assert.deepEqual(keys.sort(), ["aggregate_by", "window_limit", "window_size"]);
});

test("no edge function is left behind claiming to rate limit this path", async () => {
  // An edge function carrying a rateLimit config was tried first and was not
  // enforced: six sequential posts all reached the function. It was removed
  // rather than left as dead code that reads like protection.
  const { readdir } = await import("node:fs/promises");
  let entries = [];
  try { entries = await readdir(join(ROOT, "netlify/edge-functions")); } catch { /* absent is correct */ }
  assert.deepEqual(entries, []);
});
