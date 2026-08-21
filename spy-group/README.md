# SPY Group — website prototype, three directions

Design prototypes for a federal-contracting website for SPY Group: a
service-disabled veteran-owned small business focused on procurement,
supply chain, and logistics.

**Nothing here is live.** Every identifier is a placeholder, every page
carries `noindex`, and a visible "prototype" strip runs across the top so
none of it can be mistaken for a published site.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | Comparison page. Open this one first — it shows all three directions side by side with thumbnails and links. |
| `manifest/` | **Option 1 — Manifest.** Technical, understated, operator-grade. |
| `signal/` | **Option 2 — Signal.** Bold, commercial, high-contrast. |
| `record/` | **Option 3 — The Record.** Formal, institutional, document-like. |

Each option directory holds an `index.html` (the full one-page site) and a
`capability-statement.html` that prints to a single Letter page — the one
document contracting officers actually ask a small business for.

No build step. Open any file in a browser.

## The three directions

All three carry identical content. They differ only in identity.

### Option 1 — Manifest

Archivo semi-condensed for headlines, **Public Sans** for body (the U.S.
Web Design System typeface, so the page speaks the federal buyer's own
idiom), IBM Plex Mono for every identifier.

Reads as: disciplined, technical, understated. Looks like it was built by
someone who has run a warehouse.

**The color is still open.** The page carries a colorway picker in its top
bar — a review-only control that comes out once one is chosen. Every
colorway is a complete token set covering the dark grounds, the light
bands, the accent, and the rgb triplets behind every `rgba()`, and every
text pair in every colorway clears WCAG AA (the tightest is 4.7:1 against
a 4.5 requirement).

| Colorway | Ground | Accent | Character |
| --- | --- | --- | --- |
| **Ink** (default) | `#1C2128` charcoal | `#D98552` copper | Industrial, neutral, warm metal |
| **Harbor** | `#163542` blue-teal | `#E7A860` sand | Ports and container yards |
| **Slate** | `#232C38` blue-gray | `#6BB2E8` utility blue | Corporate, cool, no warm cast |
| **Field** | `#20362C` spruce | `#DFA03A` ochre | The original; reads military |

Field is kept only for comparison. Deep green plus veteran-owned reads as
army whether or not that is intended, which is why it is no longer the
default.

### Option 2 — Signal

White ground, heavy black rules, hi-vis orange (`#E1481F`), hazard-stripe
dividers. Saira Condensed set very large, Barlow for reading, DM Mono for
codes.

Reads as: bold, energetic, commercial. Works hardest with primes and
corporate supplier-diversity teams.

### Option 3 — The Record

Warm white paper (`#FBFAF7`), hairline and double rules, graphite ink
with an oxblood accent (`#7B2C2C`) and brass hairlines. Source Serif 4
and Source Sans 3 — again the federal design system's own pairing.
Centered masthead, numbered sections, ruled tables.

Reads as: formal, established, careful. Suits a conservative contracting
officer, and will not look dated in five years.

None of the three reuses the navy/gold/cream and Cormorant Garamond of
temidayoafonja.com. This is a separate business and should look like one.

## Shared decisions worth keeping

- **NAICS codes tag every competency**, so a buyer can match the page to a
  solicitation without a phone call.
- **Paths to award are ordered by dollar ceiling** because the authorities
  genuinely are: purchase card, simplified acquisition, SDVOSB set-aside
  or sole source, uncapped subcontracting. SDVOSB status is presented as
  an acquisition authority rather than a badge.
- **The build-out track states which registration rung the company is on**
  instead of implying past performance it does not have.
- **Product supply is marked "in definition"** — the one competency still
  being decided, said out loud.
- **Fonts are embedded in each page** as woff2 data URIs. No request to
  Google, so no visitor's IP address is disclosed to a third party — the
  same standard `fonts.css` applies on temidayoafonja.com. For production
  these would be separate `.woff2` files rather than inlined, which would
  cut each page from roughly 250 KB to about 30 KB of markup.

## Real vs. placeholder

**Real and defensible as written:** the capability copy, the NAICS
mapping, the acquisition-pathway explanations, the differentiators, and
the honest handling of a company with no past performance yet.

**Placeholder — must be replaced before anything goes live:**

- UEI and CAGE (both shown as `Pending`)
- Founder name, title, phone, email, city/state
- Legal entity name (`SPY Group LLC` is a guess)
- The product-supply category list
- `spygroup.com` as the domain, and `contracts@spygroup.com`
- The logo. All three use a boxed or circled "S" as a stand-in.

**Verify before publishing:** the dollar thresholds in "Paths to award"
reflect current FAR small-business rules ($10K micro-purchase, $250K
simplified acquisition threshold, $4.5M SDVOSB sole-source ceiling for
services and supplies, higher for manufacturing). These figures are
adjusted periodically for inflation — confirm the current numbers before
they appear on a live site.

## What SPY Group needs to supply

1. Legal entity name and formation state
2. SAM.gov registration → UEI issued, CAGE assigned via DLA
3. SDVOSB certification through SBA's Veteran Small Business
   Certification program (VetCert). Since January 2023, SDVOSB
   self-certification is no longer sufficient for set-aside awards —
   certification runs through SBA, not the old VA CVE process. A 100%
   disability rating supports the "service-disabled" element; ownership
   and control still have to be documented.
4. Final NAICS code selections and PSC codes
5. Product lines, once decided, to replace the fourth competency
6. Point-of-contact details and a business address
7. A logo

Worth discussing with a small-business advisor, not assumed:

- **8(a) Business Development.** Potentially relevant given the founder's
  background, but the presumption of social disadvantage was enjoined in
  2023 — applicants now submit a written social-disadvantage narrative.
  Eligibility and the application burden should be assessed properly.
- **MBE certification** (NMSDC) opens corporate supplier-diversity
  programs, a different buyer than the federal one and possibly the
  faster first revenue.
- **State and local** veteran and DBE programs, which often have lower
  barriers than federal set-asides.

## Open questions

- Is the name **SPY Group** and the domain **spygroup.com**? Confirm the
  spelling, and whether SPY is an acronym — if it stands for something, it
  belongs in the letterhead.
- Services only, or products too? All three are built to work either way,
  but the fourth competency and the reseller NAICS codes depend on it.
- Home state and geographic reach — the prototypes claim CONUS with
  OCONUS through partners.

## Hosting note

These files sit in this repository for review convenience only. They are
excluded in `robots.txt` and marked `noindex`. Once a direction is
approved, SPY Group's site should move to its own repository and its own
domain rather than living under temidayoafonja.com.
