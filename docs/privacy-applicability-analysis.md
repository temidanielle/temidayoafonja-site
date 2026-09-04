# Privacy Applicability Analysis

Which privacy laws plausibly apply to temidayoafonja.com, and what each requires of the site as
built. Prepared August 12, 2026.

**This is an internal working analysis, not legal advice.** It is prepared to give counsel a
factual starting point and to make the published policy defensible in the meantime. Scope
conclusions are provisional and marked for confirmation.

Facts come from `docs/data-inventory.md`. Where this document states a legal conclusion, treat it
as a question for counsel rather than an answer.

---

## 1. The operative decision

The operator has decided: **assume EU and UK visitors are possible.** The site is publicly
accessible, and the policy is drafted to cover GDPR basics even though the primary audience is
US. Counsel is asked to confirm actual scope.

That decision is the reason sections 4 and 5 below are treated as live rather than hypothetical.

---

## 2. Business facts relevant to scope

| Fact | Value | Source |
|---|---|---|
| Entity | The Density Group LLC | Site footer, Terms |
| Operating location | United States | Operator |
| Governing law chosen | Texas | Operator decision |
| Audience | Primarily US enterprise and professional | Operator |
| Site accessibility | Public, unrestricted | Observed |
| Goods or services offered to EU/UK residents | **Not deliberately targeted.** No EU/UK language options, currencies, or country targeting | Observed |
| Behavioural monitoring of EU/UK residents | **No.** Analytics is aggregate and cookieless | `docs/data-inventory.md` §6, §7 |
| Payment data processed | None. All transactions on Maven, Gumroad, Amazon | `docs/data-inventory.md` §5 |
| Annual revenue | Not established here | Operator to confirm |
| Consumers whose data is processed annually | Not established here | Operator to confirm |
| Sale or sharing of personal information | None | `docs/data-inventory.md` §5 |

The last three rows matter for the US state thresholds in section 3 and are the main open facts.

---

## 3. United States

### 3.1 Texas Data Privacy and Security Act

**Likely the most directly relevant regime**, given the entity operates from Texas and has chosen
Texas law.

TDPSA applies to a person who conducts business in Texas or produces products or services
consumed by Texas residents, processes or engages in the sale of personal data, and is not a
small business as defined by the US Small Business Administration.

**Provisional assessment:** The Density Group is very likely a small business by SBA standards,
which would place it outside the general applicability threshold. However, the small-business
exemption is **not complete**: a small business must still obtain consent before selling
sensitive personal data. The site does not sell any personal data, so that residual obligation is
not triggered as built.

**For counsel:** confirm small-business status and confirm that no processing constitutes a
"sale" as defined.

### 3.2 California, CCPA as amended by CPRA

Applies to a for-profit business meeting one of: gross annual revenue over 25 million dollars;
buying, selling, or sharing the personal information of 100,000 or more consumers or households
annually; or deriving 50 percent or more of annual revenue from selling or sharing personal
information.

**Provisional assessment: none of the three thresholds is plausibly met.** Revenue and volume are
well below, and there is no sale or sharing. CCPA very likely does not apply.

**Nonetheless**, the published policy grants access, correction, and deletion rights to everyone
rather than by jurisdiction. That is simpler to operate and avoids a scope error becoming a
compliance error.

### 3.3 Other US state regimes

Virginia, Colorado, Connecticut, Utah, Oregon, Montana, and others use similar
volume-and-revenue thresholds, generally 100,000 consumers or 25,000 plus revenue share from
sale. **None is plausibly met.**

### 3.4 CAN-SPAM

**Applies.** The site sends marketing email through Kit.

| Requirement | Status |
|---|---|
| No false or misleading headers or subject lines | Operational, outside this repository |
| Identify the message as an advertisement | Kit sequences, to confirm |
| Include a valid physical postal address | **Open.** Kit requires one. The operator has decided not to publish a residential address on the site; a mailbox or registered-agent address is the usual solution |
| Clear unsubscribe mechanism, honoured within 10 business days | Kit provides this |

The physical-address requirement applies to the email itself rather than the website, so it does
not block the policy, but it does need an answer.

### 3.5 COPPA

**Does not apply as built.** The site is not directed to children, workshops require participants
to be 18 or older, and no age-gated collection occurs. The policy states this.

---

## 4. United Kingdom and European Economic Area

### 4.1 Whether GDPR applies at all

GDPR Article 3(2) reaches a non-EU controller only where it either offers goods or services to
data subjects in the Union, or monitors their behaviour within the Union.

**Provisional assessment: neither limb is clearly met.**

- **Offering goods or services.** Mere accessibility of a website is expressly insufficient under
  Recital 23. There is no EU-language version, no euro or sterling pricing, no EU country
  targeting, and no EU-directed marketing. Workshops are scheduled in Central Time.
- **Monitoring behaviour.** Plausible is aggregate and cookieless. There is no profiling, no
  behavioural advertising, no cross-site tracking, and no session recording.

**However**, the operator has directed that the policy cover GDPR basics regardless. That is a
conservative and defensible posture: it costs little, and it removes the risk of being wrong
about scope. The analysis below therefore proceeds as if GDPR applied.

### 4.2 Lawful basis, per purpose

| Purpose | Basis relied on | Note |
|---|---|---|
| Responding to an inquiry | Legitimate interests, Art 6(1)(f) | The visitor initiated contact. Could alternatively be pre-contractual steps, Art 6(1)(b) |
| Delivering a diagnostic result | Performance of a service requested, Art 6(1)(b) | The visitor asked for the result |
| Marketing email | **Consent, Art 6(1)(a)** | Unticked by default, and now genuinely gates enrolment |
| Research aggregate | **Consent, Art 6(1)(a)** | Separate checkbox, unticked by default |
| Rate limiting by IP | Legitimate interests, Art 6(1)(f) | Security and abuse prevention. See section 6 |

The two consent bases are the strongest part of the current implementation: both boxes are
unticked by default, both are recorded, and marketing enrolment was verified in a browser to fire
only on an affirmative tick.

### 4.3 Special category data

**None is deliberately collected.** No health, biometric, racial or ethnic origin, political
opinion, religious belief, trade union membership, sex life, or sexual orientation data is
requested by any form.

**One residual risk.** The free-text decision fields on the enterprise inquiry forms are
unbounded, and a sponsor could type something about a named employee that constitutes special
category data. The Executive Briefing form now warns against exactly this, naming medical,
compensation, and performance information. The `work.html` inquiry form carries a shorter warning
and could be brought into line.

### 4.4 International transfers

All processing is in the United States. For EU or UK data subjects this is a restricted transfer
requiring an Article 46 safeguard.

| Provider | Transfer mechanism | Status |
|---|---|---|
| Netlify | Standard contractual clauses via their DPA | To verify and countersign if required |
| Formspree | SCCs via their DPA | To verify |
| Anthropic | SCCs via their commercial terms and DPA | To verify |
| Kit | SCCs via their DPA | To verify |
| Plausible | EU-hosted, aggregate only | Likely no transfer issue. Plausible is EU-based, which is favourable |
| Google Fonts | No DPA in place | **See section 6** |

**Action:** the DPAs need to be located, reviewed, and countersigned where required. That is an
operator task, not a drafting task. The published policy currently says the firm relies on the
transfer mechanisms offered by each provider and is confirming the specific mechanism, which is
accurate and not overclaiming.

### 4.5 Data subject rights

The published policy grants access, rectification, erasure, restriction, objection, portability,
and withdrawal of consent, plus the right to complain to a supervisory authority. The operational
procedure is in `docs/privacy-rights-request-procedure.md`.

### 4.6 Records, DPO, representative

- **Article 30 records.** `docs/data-inventory.md` substantially serves this function. Not
  formally structured as an Art 30 record; counsel to advise whether that matters at this scale.
- **Data Protection Officer.** Not required. No large-scale systematic monitoring, no large-scale
  special category processing.
- **EU or UK representative, Art 27.** Would be required only if Art 3(2) applies. Given the
  provisional assessment in 4.1 that it likely does not, no representative is appointed. **This is
  the single most consequential open question in this document:** if counsel concludes GDPR does
  apply, a representative is a hard requirement, not an optional one.

---

## 5. What the site does well already

Worth recording, because it materially narrows exposure:

- No cookies set by first-party code, so no consent banner is required
- Cookieless, aggregate analytics
- No advertising, profiling, or cross-site tracking
- No sale or sharing of personal information
- No payment data ever received or stored
- Marketing consent unticked by default and genuinely gating enrolment
- Research consent separate from marketing consent
- Secrets held in environment variables, never in page source

---

## 6. Open items that affect the analysis

### 6.1 IP address storage

`netlify/functions/diagnose.js` stores visitor IP addresses as blob keys with no purge. See
`docs/data-inventory.md` section 10. The recommendation is a salted hash, which removes the
personal data while preserving the rate limit. Under GDPR the current form is defensible as
legitimate interests but fails data minimisation and storage limitation. **Not yet applied.**

### 6.2 Google Fonts

Fonts load from Google servers on every page, disclosing visitor IP addresses. German courts have
found this an unlawful transfer absent consent, and it is the most-cited example of a small
technical choice creating a GDPR problem. **If counsel concludes GDPR applies, self-hosting the
fonts is the clean fix**, and it is a contained change.

### 6.3 Retention

Four durable stores have no enforced retention. This is a live gap under any regime that requires
storage limitation. Counsel should set periods; engineering can then implement them.

### 6.4 Non-consenting research records

`audit-research` retains records where research consent is false, flagged for exclusion from
aggregates. The retention is defensible for auditability but is undisclosed and should be either
disclosed or stopped.

### 6.5 Export token

`RESEARCH_EXPORT_TOKEN` is passed as a URL query parameter and gates the full research and lead
stores. Query strings land in logs and browser history. A bearer header is the safer construction.

---

## 7. Recommended sequence for counsel

1. Confirm or reject the Article 3(2) assessment in 4.1. Everything in section 4 depends on it,
   including whether an Art 27 representative is required.
2. Confirm small-business status under TDPSA and that no processing is a "sale".
3. Decide the CAN-SPAM postal address.
4. Set retention periods.
5. Review the two published drafts, `/privacy` and `/terms`.
6. Advise on the four technical items in section 6.

---

## 8. Status

**Counsel review pending.** Neither published page claims to have been reviewed by an attorney,
and neither carries a public self-disqualifying statement. This document is the internal record
that review has not yet happened.
