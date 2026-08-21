# SPY Group — website prototype

A design prototype for a federal-contracting website for SPY Group: a
service-disabled veteran-owned small business focused on procurement,
supply chain, and logistics.

**Nothing here is live.** Every identifier is a placeholder, and the pages
carry `noindex` plus a visible "prototype" strip so they cannot be mistaken
for a published site.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The full one-page site. Open it in any browser — no build step. |
| `capability-statement.html` | The one-page capability statement, laid out for Letter. "Print / save as PDF" produces the single document contracting officers actually ask for. |

## Design direction

Deliberately unlike temidayoafonja.com. That site is warm advisory —
navy, gold, cream, Cormorant Garamond. This one is procurement-grade: the
visual language of a manifest, a dispatch board, a government form.

**Color.** Deep spruce-black (`#14201B`) as the dark ground, bone
(`#EDEDE5`) for the light bands, and one accent — stencil ochre
(`#D08A22`), the color of crate markings and hi-vis. Green reads supply
chain and military-adjacent without resorting to flag red-white-blue,
which every other veteran-owned contractor site already uses. All text
pairs clear WCAG AA contrast on their grounds.

**Type.** Three faces, each doing one job:

- **Archivo** (semi-condensed, 800) for headlines — utilitarian grotesque,
  plate-like, not the Inter/Space Grotesk default.
- **Public Sans** for body copy — the typeface of the U.S. Web Design
  System. The site literally speaks the federal buyer's visual language.
- **IBM Plex Mono** for every identifier: UEI, CAGE, NAICS, dollar
  ceilings. Codes read as data, not prose.

**Structure.** The devices carry information rather than decorate:
capability cards are tagged with the NAICS code each is bid under, so a
buyer can match the page to a solicitation without a phone call. "Paths
to award" is ordered because it is genuinely ordered — each rung is a
higher dollar ceiling and a different acquisition authority. The
build-out track is a real sequence and shows exactly which rung the
company is standing on.

No fade-ins or scroll animation. Hover states are the only motion.

## Real vs. placeholder

**Real and defensible as written:** the capability copy, the NAICS
mapping, the acquisition-pathway explanations, the differentiators, and
the honest handling of a company with no past performance yet.

**Placeholder — must be replaced before anything goes live:**

- UEI and CAGE (both shown as `Pending`)
- Founder name, title, phone, email, city/state
- Legal entity name (`SPY Group LLC` is a guess)
- The product-supply category list (that section is written as
  "in definition" on purpose, since product lines aren't settled)
- `spygroup.com` as the domain, and `contracts@spygroup.com`

**Verify before publishing:** the dollar thresholds in "Paths to award"
reflect current FAR small-business rules ($10K micro-purchase, $250K
simplified acquisition threshold, $4.5M SDVOSB sole-source ceiling for
services and supplies with a higher ceiling for manufacturing). These
figures are adjusted periodically for inflation — confirm the current
numbers before they appear on a live site.

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
5. Product lines, once decided, to replace the fourth capability card
6. Point-of-contact details and a business address
7. Logo. The prototype uses a boxed "S" as a stand-in.

Worth discussing with a small-business advisor, not assumed:

- **8(a) Business Development.** Potentially relevant given the founder's
  background, but the presumption of social disadvantage was enjoined in
  2023 — applicants now submit a written social-disadvantage narrative.
  Eligibility and the application burden should be assessed properly.
- **MBE certification** (NMSDC) opens corporate supplier-diversity
  programs, which is a different buyer than the federal one and may be
  the faster first revenue.
- **State and local** veteran/DBE programs, which often have lower
  barriers than federal set-asides.

## Open questions

- Is the name **SPY Group** and the domain **spygroup.com**? Confirm
  spelling and whether SPY is an acronym — if it stands for something, it
  belongs in the letterhead.
- Services-only, or products too? The site is built to work either way,
  but the fourth capability card and the reseller NAICS codes depend on
  the answer.
- Home state and geographic reach — the prototype claims CONUS with
  OCONUS through partners.

## Hosting note

These files sit in this repository for review convenience only. They are
excluded from `robots.txt` and marked `noindex`. When the direction is
approved, SPY Group's site should move to its own repository and its own
domain rather than living under temidayoafonja.com.
