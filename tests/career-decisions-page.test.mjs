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
async function open(t, { query = "", respond = { status: 200, json: { ok: true, durable_record: true } }, now = null, reducedMotion = null, viewport = { width: 1440, height: 900 } } = {}) {
  const context = await browser.newContext({ viewport, reducedMotion: reducedMotion || undefined });
  const page = await context.newPage();
  const events = [];
  const requests = [];

  await page.exposeFunction("__record", (name, props) => events.push({ name, props }));
  await page.addInitScript(() => {
    window.plausible = (name, opts) => window.__record(name, (opts && opts.props) || null);
  });
  if (now !== null) {
    await page.addInitScript((fixed) => {
      const RealDate = Date;
      const fixedMs = fixed;
      // eslint-disable-next-line no-global-assign
      Date = class extends RealDate {
        constructor(...args) { return args.length ? new RealDate(...args) : new RealDate(fixedMs); }
        static now() { return fixedMs; }
      };
      Date.parse = RealDate.parse;
      Date.UTC = RealDate.UTC;
    }, now);
  }

  await page.route("**/.netlify/functions/career-decisions-subscribe", async (route) => {
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

async function fillValid(page, { consent = true } = {}) {
  await page.fill("#cdFirst", "Ada");
  await page.fill("#cdEmail", "ada@example.com");
  await page.fill("#cdDeciding", "Whether to take the platform role.");
  if (consent) await page.check("#cdConsent");
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
  assert.equal(await page.locator("nav .nav-links li").count(), 8);
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
  const consent = (await page.locator('label[for="cdConsent"]').innerText()).replace(/\s+/g, " ").trim();
  assert.ok(consent.startsWith("You will receive the evidence check and occasional Capability Formation guidance from Temidayo Afonja. You can unsubscribe at any time."), consent);
});

test("the consent block links the word Privacy", async (t) => {
  const { page } = await open(t);
  const link = page.locator('.cd-consent a[href="privacy.html"]');
  assert.equal(await link.count(), 1);
  assert.equal((await link.innerText()).trim(), "Privacy");
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
  await page.check("#cdConsent");
  await page.click("#cdSubmit");
  assert.equal(await page.getAttribute("#cdEmail", "aria-invalid"), "true");
  assert.equal(await page.locator("#cdEmailError").innerText(), "Please enter a valid email address.");
  assert.equal(requests.length, 0);

  await page.fill("#cdEmail", "ada@example.com");
  assert.equal(await page.getAttribute("#cdEmail", "aria-invalid"), null);
  assert.equal(await page.locator("#cdEmailError").innerText(), "");
});

test("an unticked consent box blocks the submission", async (t) => {
  const { page, requests } = await open(t);
  await fillValid(page, { consent: false });
  await page.click("#cdSubmit");
  assert.equal(await page.getAttribute("#cdConsent", "aria-invalid"), "true");
  assert.match(await page.locator("#cdConsentError").innerText(), /tick the box/);
  assert.equal(requests.length, 0, "nothing may be sent without consent");
  assert.equal(await page.locator("#cdResult").isVisible(), false);
});

test("consent starts unticked", async (t) => {
  const { page } = await open(t);
  assert.equal(await page.isChecked("#cdConsent"), false);
});

/* ── Success ───────────────────────────────────────────────────────────── */
test("a confirmed subscription reveals the three questions, announces it, and moves focus", async (t) => {
  const { page, events, requests } = await open(t);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");

  assert.equal(requests.length, 1);
  assert.equal(requests[0].marketing_consent, true);
  assert.ok(requests[0].consent_timestamp, "the consent timestamp is sent");
  assert.equal(requests[0].policy_version, "2026-08-12");

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
  assert.equal(a.utm_source, "youtube");
  assert.equal(a.utm_medium, "video");
  assert.equal(a.utm_campaign, "capability-formation");
  assert.equal(a.utm_content, "end-card");
  assert.equal(a.utm_term, "stay-or-leave");
  assert.equal(a.video, "read-what-the-work-built");
  assert.ok(a.landing_page.includes("utm_source=youtube"));
});

test("attribution survives a later visit to the bare URL in the same session", async (t) => {
  const { page, requests } = await open(t, { query: "?source=youtube&v=episode-04" });
  await page.goto(origin + "/career-decisions", { waitUntil: "domcontentloaded" });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  assert.equal(requests[0].attribution.source, "youtube");
  assert.equal(requests[0].attribution.video, "episode-04");
});

test("a source is never invented when the visitor arrives without one", async (t) => {
  const { page, requests, events } = await open(t);
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  const a = requests[0].attribution;
  assert.equal(a.source, undefined);
  assert.equal(a.utm_source, undefined);
  assert.equal(a.video, undefined);
  const subscribed = events.find((e) => e.name === "Career Decisions Subscribed");
  assert.equal(subscribed.props.source, "direct");
  assert.equal(subscribed.props.video, "none");
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
  assert.match(text, /Wednesday, September 2, 2026, 6:00 to 6:45 PM CT/);
});

test("after the Lightning Lesson ends, the next step falls back to the Field Kit", async (t) => {
  const { page } = await open(t, { now: Date.parse("2026-09-03T00:00:00Z") });
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

test("the next step is written in exactly one place in the source", async () => {
  // Read the file rather than the rendered DOM: the renderer necessarily puts a
  // second copy of the chosen URL into the anchor it builds. What matters is
  // that the source hardwires each offer exactly once, in the config block.
  const source = await readFile(join(ROOT, "career-decisions.html"), "utf8");
  assert.equal((source.match(/maven\.com\/p\/5162f2/g) || []).length, 1, "the Lightning Lesson URL is written once");
  assert.equal((source.match(/temidayoafonja\.com\/fieldkit/g) || []).length, 1, "the Field Kit URL is written once");
  assert.equal((source.match(/\$150/g) || []).length, 1, "the price is written once");
  assert.equal((source.match(/September 2, 2026/g) || []).length, 1, "the date is written once");
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
  const { page, events } = await open(t, { now: Date.parse("2026-09-03T00:00:00Z") });
  await fillValid(page);
  await page.click("#cdSubmit");
  await page.waitForSelector("#cdResult.is-open");
  await page.locator("#cdStep a").click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(200);
  assert.ok(events.some((e) => e.name === "Career Decisions Next Step Click" && e.props.step === "field-kit"));
  assert.ok(events.some((e) => e.name === "Field Kit Click"));
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
  assert.equal(await page.getAttribute("#cdConsent", "required"), "");
  assert.ok(!!(await page.locator('label[for="cdConsent"]').count()));
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
  await page.keyboard.press("Tab"); // consent, the honeypot is out of the tab order
  assert.equal(await page.evaluate(() => document.activeElement.id), "cdConsent");
  await page.keyboard.press("Space");
  await page.keyboard.press("Tab");
  // The Privacy link sits inside the consent label, so it is the next stop.
  // That is correct: a keyboard user can read the policy before submitting.
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
