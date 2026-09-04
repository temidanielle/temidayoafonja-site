# Accessibility QA

WCAG 2.2 Level AA as the implementation target, per section 22 of the production reconciliation
brief. Audit run and remediation applied August 13, 2026 against `main` at `ba7512b`.

**Scope.** All fifteen publicly reachable pages. `dashboard.html` is excluded: it is blocked at the
edge by `netlify.toml` and is not a public page.

**Result.** Zero automated violations across 45 page and configuration combinations. Every manual
check in section 22 passes, with the two dismissals in section 8 recorded and explained.

---

## 1. Method

Not a description of the site. Everything below was measured in a browser.

| | |
|---|---|
| Engine | Headless Chromium via Playwright |
| Automated rules | axe-core 4.x, tags `wcag2a wcag2aa wcag21a wcag21aa wcag22aa best-practice` |
| Pages | index, framework, work, executive-briefing, for-professionals, about, case-studies, speaking, book, diagnostic, organizational-diagnostic, ai-capability-readiness, privacy, terms, 404 |
| Configurations | Desktop 1440x900, mobile 375x812, and desktop with `prefers-reduced-motion: reduce` |
| Reflow | 320 CSS px viewport, per SC 1.4.10 |
| Text resize | `html { font-size: 200% }` at 1280x1024, per SC 1.4.4 |
| Focus | Real `Tab` and `Shift+Tab` traversal, forwards and backwards, on every page |
| Contrast | Computed independently in Python from the WCAG relative-luminance formula, not read off the stylesheet |

**One measurement trap worth recording.** The first automated pass reported 84 contrast failures per
run, many of them on elements carrying `.fade-up` and `.delay-N`. Those elements animate from
`opacity: 0` on load, and axe was sampling them mid-transition, so the blended colour it measured
was a colour no user ever sees. Every run below waits 2.5 seconds and then asserts that no animated
element is still below full opacity before axe runs. That assertion returned zero on every pass. The
same artifact inflated the first focus-traversal pass to 491 findings: `html { scroll-behavior:
smooth }` means an element the browser scrolls to has not arrived when the probe reads its position.
Both numbers were wrong, and both were mine, not the site's.

---

## 2. Automated results

| Rule | Impact | Before | After |
|---|---|---|---|
| `color-contrast` (1.4.3) | serious | 229 nodes across 14 pages | 0 |
| `link-in-text-block` (1.4.1) | serious | 9 nodes across 2 pages | 0 |
| `landmark-one-main` | moderate | 45 nodes, every page | 0 |
| `region` | moderate | 390 nodes, every page | 0 |

Nothing else fired, before or after: no missing alt text, no missing form labels beyond those in
section 4, no duplicate ids, no ARIA misuse, no empty links, no positive `tabindex`, no missing
`lang`, no missing page title.

---

## 3. Colour contrast, 1.4.3

Fourteen distinct colour pairs failed. The two brand accents account for most of them: gold
`#C9A84C` measures 2.29:1 on white, and rust `#C1440E` measures 4.24:1 on the warm cream band. Both
are fine as non-text colour and fail as text colour on a light ground.

**The brand palette in section 24 is unchanged.** Navy `#0F2347`, Sand `#F5F0E8`, Gold `#C9A84C` and
Rust `#C1440E` still carry every rule they carried before. Two text-safe darkened variants were
added alongside them in `styles.css`, used only where text sits on a light ground:

- `--gold-ink: #7F6A30`, which measures 5.24:1 on white, 5.16:1 on paper `#FFFDF8`, 4.62:1 on sand
- `--rust-ink: #B6400D`, which measures 5.63:1 on white, 4.66:1 on the warm band, 4.52:1 on `#F1E4D9`

Everywhere else the fix was opacity, not hue.

| Element | Change | Before | After |
|---|---|---|---|
| `.footer-copy` (all pages) | slate 0.6 to 0.85 on navy | 2.96:1 | 4.55:1 |
| `.brand-tertiary` (all pages) | opacity 0.75 to 0.9 on navy | 4.40:1 | 5.76:1 |
| `.pillar-num` (framework) | gold 0.2 to 0.6 on navy, large text, 3:1 threshold | 1.42:1 | 3.29:1 |
| `.topic-num` (speaking) | gold 0.5 to 0.8 on navy | 2.69:1 | 4.80:1 |
| `.h-feature .n` (home) | gold to `--gold-ink` on paper | 2.24:1 | 5.16:1 |
| `.cs-principle .n` (evidence) | gold to `--gold-ink` on white | 2.28:1 | 5.24:1 |
| `.a-ladder-card .tier` (for professionals) | gold to `--gold-ink` on white | 2.28:1 | 5.24:1 |
| `.nav-cta` (diagnostic) | sand to navy on the gold button | 2.01:1 | 6.80:1 |
| `.ll-cta` (for professionals) | ink to white on the rust button | 3.09:1 | 5.12:1 |
| `.r-sub` inside `.route.org` (advisory) | warm grey to white at 0.78 on navy | 2.68:1 | 9.93:1 |
| `.live-tally-name` (scan) | resting item opacity 0.6 to 0.8 | 3.34:1 | 4.77:1 |
| `.fw-arch-label`, `.fw-separate strong` (framework) | rust to `--rust-ink` on the warm band | 4.24:1 | 4.66:1 |
| `.briefings-contexts-label` (speaking) | rust to `--rust-ink` on the warm band | 4.24:1 | 4.66:1 |
| `.legal-flag` links (privacy, terms) | rust to `--rust-ink` on `#F1E4D9` | 4.10:1 | 4.52:1 |
| Legal link strip (diagnostic, scan) | sand 0.45 to 0.56 on navy | 3.85:1 | 5.23:1 |
| `.pillars-caption`, `.intro-meta` (diagnostic) | sand 0.5 to 0.56 on navy | 4.46:1 | 5.23:1 |

### Three of these were CSS specificity accidents, not design choices

Worth separating out, because in each case the stylesheet already declared the correct colour and
something else was quietly winning:

1. **`.ll-cta` on `/for-professionals`.** The rule sets `color: #fff`. `.lean-page a { color:
   inherit }` is (0,1,1) and outranks it at (0,1,0), so the Register Free button rendered dark ink
   on rust. Restated as `a.ll-cta` at (0,1,1).
2. **`.nav-cta` on `/diagnostic`.** `body .nav-links a { color: #f5f0e8 !important }` at (0,1,2)
   outranked `body .nav-cta { color: #0f2347 !important }` at (0,1,1), and the CTA is inside
   `.nav-links`, so the gold button rendered sand on gold. Restated as `body .nav-links a.nav-cta`.
3. **`.brand-tertiary` sitewide.** The rule sets `color: var(--slate)`. `.nav-logo span` is (0,1,1)
   and outranks it, so the "Founded by Temidayo Afonja" line actually renders gold. The opacity
   change clears AA at 5.76:1 gold or 4.97:1 slate, so it holds whichever colour wins. The
   underlying specificity conflict is left alone: changing it would change the lockup's appearance,
   which is a design decision and not an accessibility one.

---

## 4. Form labels and input purpose, 1.3.1, 3.3.2, 4.1.2

Eight inputs on `/diagnostic` had a placeholder and no label: `pregateName`, `pregateEmail`,
`paperName`, `paperEmail`, `gateName`, `gateOrg`, `gateRole`, `gateEmail`. A placeholder is not a
label; it disappears on the first keystroke and is not reliably announced.

Each now carries an `aria-label` and an `autocomplete` token. The visible placeholders are unchanged,
so nothing moves on screen. `orgName` on the scan also gained `autocomplete="organization"`.

Every other form on the site already had proper `<label for>` associations. All identity fields on
`/work`, `/executive-briefing`, `/for-professionals`, `/speaking` and `/book` already carried correct
autocomplete tokens (SC 1.3.5), which was good work already in place.

---

## 5. Keyboard, focus and bypass

### 5.1 Focus Visible, 2.4.7

Six pages removed the browser's focus ring from their form fields with `outline: none` and put
nothing in its place. Measured by focusing each control and reading its computed style after
transitions had settled:

| Page | Selector | Before | After |
|---|---|---|---|
| work | `.contact-input` (input, select, textarea) | no change of any kind on focus | two-tone ring |
| for-professionals | `.a-field input`, `.a-field textarea` | no change of any kind on focus | two-tone ring |
| diagnostic | `.gate-input`, `.gate-select`, `.cta-input`, `.paper-input` | no change of any kind on focus | two-tone ring |
| speaking | `.inquiry-input` | border only, `rgba(139,160,180,.25)` to `rgba(201,168,76,.25)` | two-tone ring |
| executive-briefing | `.eb-input` | border only, to solid gold | two-tone ring |
| book | email field | browser default | two-tone ring |

The replacement is a single rule in `styles.css`:

```css
html a:focus-visible, html button:focus-visible, html input:focus-visible,
html select:focus-visible, html textarea:focus-visible, html summary:focus-visible,
html [tabindex]:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 2px;
  box-shadow: 0 0 0 2px var(--navy);
}
```

Two tones because no single brand colour works on both grounds: gold is 6.80:1 on navy and 2.01:1 on
sand, navy is 13.70:1 on sand and invisible on navy. The gold outer ring carries the indicator on the
dark pages, the navy inner ring carries it on the cream bands, and one of the two always contrasts.
This is the same construction Chromium's own default ring uses.

The `html` prefix takes the selector to (0,1,2) so it outranks the page-level `outline: none`
declarations without needing `!important`. Where a page already declared a correct ring, at (0,1,2)
or higher, that rule still wins: `/organizational-diagnostic` and `/ai-capability-readiness` keep
their existing 2px gold rings, and `/organizational-diagnostic` keeps the pattern where the visually
hidden radio input passes its ring to the adjacent `<label>`, which was verified rather than assumed.

### 5.2 Bypass Blocks, 2.4.1

No page had a skip link. Every page repeats the same eight-item nav, so a keyboard user was tabbing
through it on every page before reaching the content. Each page now opens with

```html
<a class="skip-link" href="#main">Skip to main content</a>
```

positioned off screen until focused, then pinned to the top left at `z-index: 10002`. Verified in a
browser: on first Tab it is the active element, sits at `top: 12px`, hit-tests as the topmost element
at its own centre, and renders navy on gold at 6.80:1.

### 5.3 Landmarks, 1.3.1

No page had a `<main>` element, which is why `landmark-one-main` fired on all fifteen and `region`
fired on 390 nodes. All fifteen pages now wrap their content in `<main id="main" tabindex="-1">`.

Two pages needed care rather than the pattern. `/organizational-diagnostic` and
`/ai-capability-readiness` both carry a print rule, `.wrap > *:not(#report) { display: none }`, that
depends on the direct children of `.wrap`. `<main>` was therefore placed **around** `.wrap`, never
inside it. Verified under print media emulation on the scan page: `main` is `display: block`,
`#report` is `display: block`, and zero non-report children of `.wrap` are shown. The print report
still works.

The two standalone pages carry a legal link strip outside `<main>` and outside any footer; each now
carries `role="contentinfo"` rather than being converted to a `<footer>` element, which on
`/diagnostic` would have inherited the shared footer styling and changed its appearance.

Full-page screenshots at 1280px were compared before and after on six pages. All six are identical in
height to the pixel, so the added wrapper caused no layout shift.

### 5.4 Focus Not Obscured, 2.4.11, new in WCAG 2.2

Tested by real `Tab` and `Shift+Tab` traversal in both directions on every page, checking whether the
focused element fell outside the viewport, sat entirely inside the fixed nav's band, or hit-tested as
covered by something else.

Two things were fixed:

1. **The fixed nav.** It is 83px tall on desktop and covers anything the browser scrolls to the very
   top edge, which is what backwards traversal does. `html { scroll-padding-top: 100px }` was added,
   dropping to 76px below 768px where the nav is shorter.
2. **The mobile drawer.** With the menu open, tabbing past the last of the eight menu links continued
   into the page behind it: links that were completely hidden by the overlay were still focusable.
   `nav.js` now marks every other direct child of `<body>` `inert` while the drawer is open and
   clears it on close. Verified: focus now cycles through the eight menu links and the toggle button
   and never reaches the page behind. Escape still closes the drawer, returns focus to the toggle,
   and clears `inert` from all seven body children.

The mobile nav was otherwise already correct and is worth recording as such: a real `<button>`, an
`aria-label` that flips between "Open menu" and "Close menu", `aria-expanded` that tracks state, and
`aria-controls` pointing at the drawer's id.

---

## 6. Heading order, 1.3.1

Every page has exactly one `<h1>` and no skipped levels, with one exception that was fixed:
`/ai-capability-readiness` had two `<h1>`s, because its screens are siblings in the DOM and the
intake screen opened with its own. The second is now an `<h2>` carrying the same inline font size, so
the rendered heading is unchanged.

---

## 7. Reflow and resize

**Reflow, 1.4.10.** At 320 CSS px, fourteen of fifteen pages produced no horizontal scrolling. The
scan page pushed the document to 354px: `.live-tally-label` was `flex: 0 0 auto`, which held it at
its max-content width and stopped the text wrapping. It is now `flex: 1 1 100%; min-width: 0` below
560px. Re-measured at 320px: no horizontal scrolling on any page.

**Text resize, 1.4.4.** With root font size forced to 200%, no page produces horizontal scrolling and
no text is clipped. One dismissal is recorded in section 8.

**Reduced motion, 2.3.3.** Under `prefers-reduced-motion: reduce`, across the nine animated pages, 39
elements carry `.fade-up` or `.delay-N`: zero resolve below full opacity and zero are still running
an animation. The reduced-motion axe run is also clean. This was already correct before this pass.

---

## 8. Checked and dismissed

Two findings surfaced by the tooling that are not defects. Recorded rather than deleted, so a later
run does not spend time rediscovering them.

1. **`.founder-photo-wrap` on `/about` clips at 200% text zoom.** `scrollHeight` 286 against
   `clientHeight` 276. It is a fixed 280px circular frame with `overflow: hidden` that crops a
   photograph. SC 1.4.4 governs text, and the element contains none. No change made.
2. **The skip link reports as sitting inside the fixed nav's band when focused.** It does, by design,
   and it is painted above it: `z-index` 10002 against the nav's 100, and it hit-tests as the topmost
   element at its own centre. The heuristic that flagged it was mine.

---

## 9. Files changed

| File | Change |
|---|---|
| `styles.css` | `--gold-ink` and `--rust-ink` tokens, `.skip-link`, `main` rules, the `:focus-visible` ring, `scroll-padding-top`, `.footer-copy` and `.brand-tertiary` opacity |
| `nav.js` | `inert` on the backdrop while the mobile drawer is open |
| all 15 pages | skip link, `<main id="main" tabindex="-1">` |
| `index.html` | `--gold-ink` on the feature numerals |
| `framework.html` | `.pillar-num` opacity, `--rust-ink` on two warm-band labels |
| `work.html` | `.route.org .r-sub` colour |
| `for-professionals.html` | `--gold-ink` on the tier label, `a.ll-cta` colour |
| `case-studies.html` | `--gold-ink` on the principle numerals |
| `speaking.html` | `.topic-num` opacity, `--rust-ink` on the contexts label |
| `about.html` | underline on the Substack link in body copy |
| `privacy.html`, `terms.html` | `--rust-ink` on warm-section links |
| `diagnostic.html` | nav CTA specificity, eight `aria-label` and `autocomplete` pairs, caption and meta alpha, `.brand-tertiary` opacity, legal strip alpha and underline and `role="contentinfo"` |
| `organizational-diagnostic.html` | live-tally opacity and reflow, `.brand-tertiary` opacity, skip-link and `main` CSS restated locally, `autocomplete` on `orgName`, legal strip alpha and underline and `role="contentinfo"` |
| `ai-capability-readiness.html` | second `<h1>` demoted to `<h2>` |

`organizational-diagnostic.html` does not link `/styles.css`, so the shared accessibility rules do
not reach it and are restated in its own `<style>` block. That duplication is a standing hazard on
that page: anything added to the shared sheet has to be added there too.

---

## 10. Open items

Not failures at AA, but the honest list of what a further pass would take on.

1. **No AAA work was attempted.** SC 2.4.13 Focus Appearance, 1.4.6 Contrast Enhanced and 1.4.8
   Visual Presentation are out of scope for a AA target and were not measured.
2. **No screen reader was run.** No JAWS, NVDA or VoiceOver is available in this environment. The
   ARIA and semantics are correct by inspection and by axe, but the announced experience has not been
   heard. A single pass with VoiceOver on the diagnostic and scan flows would be worth an hour.
3. **No testing with real assistive technology users**, which is the only test that finds the
   problems automation and inspection both miss.
4. **The scan and readiness pages duplicate the shared CSS.** See section 9.
5. **Production is unverified.** This container cannot reach `temidayoafonja.com` or the Netlify
   deploy previews: the egress proxy blocks both. Everything above was measured against the
   repository served locally, which is the deployed artifact byte for byte, since `netlify.toml` sets
   `publish = "."` and there is no build step. It is still not the same as checking the live site.
6. **`role="contentinfo"` on the two legal strips is a workaround.** The semantically cleaner form is
   a real `<footer>` element, which those two pages should get if they ever adopt the shared footer.
