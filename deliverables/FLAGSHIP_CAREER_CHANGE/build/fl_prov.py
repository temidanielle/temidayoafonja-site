# -*- coding: utf-8 -*-
"""Private provenance. Maps every public slide line back to the source read.

Not published. Not included in any public asset.
"""

# (public display text, original source language, slide, classification, note)
MAP = [
# ---------------------------------------------------------------- slide 1
("Senior Manager / Program Management", "Senior Manager, Program Management",
 "1", "ROLE TITLE",
 "Role A title, exactly as given in the source read. No employer."),
("Director / Enterprise Transformation", "Director, Enterprise Transformation",
 "1", "ROLE TITLE",
 "Role B title, exactly as given in the source read. No employer."),

# ---------------------------------------------------------------- slide 2
("Complex programs", "leads complex programs", "2", "RESPONSIBILITY (Role A)",
 "Verb dropped for a card. Meaning unchanged."),
("Governance", "manages governance", "2", "RESPONSIBILITY (Role A)",
 "Verb dropped. Sits opposite Role B's enterprise governance, which is a "
 "wider scope and is why the split slide exists."),
("Risk and dependencies", "manages timelines, risks and dependencies",
 "2", "RESPONSIBILITY (Role A)",
 "Timelines dropped for length. Risk and dependencies are the two the "
 "destination also names, so the row compares like with like."),
("Budgets", "manages resources and budgets", "2", "RESPONSIBILITY (Role A)",
 "Resources dropped for length. Budget is the item the destination also "
 "names."),
("Executive updates", "provides executive updates", "2",
 "RESPONSIBILITY (Role A)", "Verb dropped."),
("Cross-functional influence",
 "works across Product, Technology and Operations; communicates with senior "
 "stakeholders", "2", "RESPONSIBILITY (Role A)",
 "Two source items compressed into the capability they share. Named "
 "functions dropped because they are employer-specific."),
("Enterprise transformation",
 "owns enterprise transformation / maturity roadmap", "2",
 "RESPONSIBILITY (Role B)", "Maturity roadmap dropped for length."),
("Governance", "enterprise governance", "2", "RESPONSIBILITY (Role B)",
 "Shortened to the shared word on purpose, because the slide's teaching is "
 "that the same word covers different scope. The difference is then shown on "
 "slide 5 rather than asserted here."),
("Enterprise risk and dependencies", "enterprise risk and dependencies",
 "2", "RESPONSIBILITY (Role B)", "Verbatim."),
("Budget tracking", "financial and operational planning", "2",
 "RESPONSIBILITY (Role B)",
 "NARROWED. The source is wider than budget tracking. Kept narrow here so "
 "the row does not overstate the overlap with Role A's budgets, and the "
 "fuller financial scope appears on slides 5 and 6 where it belongs."),
("Executive and board reporting", "executive and board reporting", "2",
 "RESPONSIBILITY (Role B)", "Verbatim."),
("C-suite alignment", "C-suite alignment", "2", "RESPONSIBILITY (Role B)",
 "Verbatim. The source also says C-suite alignment without direct authority "
 "under experience; that qualifier is carried on slide 5."),

# ---------------------------------------------------------------- slide 4
("Cross-functional influence / Moving work across people you do not directly "
 "control",
 "works across Product, Technology and Operations (Role A); C-suite "
 "alignment without direct authority (Role B)", "4", "OVERLAP READ",
 "A capability both postings describe. Stated as looks portable, not as "
 "proven transfer."),
("Program judgment / Managing risk, dependencies and complex execution",
 "manages timelines, risks and dependencies (Role A); enterprise risk and "
 "dependencies (Role B)", "4", "OVERLAP READ",
 "Both postings name risk and dependencies. The slide does not claim the "
 "risks are the same kind."),
("Executive communication / Turning work into decisions for senior leaders",
 "communicates with senior stakeholders, provides executive updates (Role A); "
 "executive and board reporting (Role B)", "4", "OVERLAP READ",
 "Board reporting is Role B only and is deliberately not claimed here. It "
 "appears on slide 5 as a difference."),
("Governance rhythm / Milestones, escalation, reporting and accountability",
 "manages governance (Role A); enterprise governance, executive steering "
 "committees (Role B)", "4", "OVERLAP READ",
 "Milestones and escalation are the mechanics both describe."),

# ---------------------------------------------------------------- slide 5
("People leadership", "leads and develops project-management staff", "5",
 "RESPONSIBILITY (Role A)", "Role A names direct staff leadership. Role B "
 "does not, which is the point of the slide."),
("Program delivery", "leads complex programs", "5", "RESPONSIBILITY (Role A)",
 "Restated for the column."),
("Team development", "leads and develops project-management staff", "5",
 "RESPONSIBILITY (Role A)", "The develops half of the same source item."),
("Execution governance", "manages governance; uses metrics to support "
 "decisions", "5", "RESPONSIBILITY (Role A)",
 "Governance at the execution layer, as against Role B's enterprise layer."),
("Enterprise judgment", "owns enterprise transformation / maturity roadmap; "
 "integrated planning", "5", "RESPONSIBILITY (Role B)",
 "Summary of the enterprise-level ownership the posting describes."),
("C-suite alignment", "C-suite alignment; C-suite alignment without direct "
 "authority", "5", "RESPONSIBILITY + EXPERIENCE (Role B)", "Verbatim."),
("Operating infrastructure", "experience building operational "
 "infrastructure", "5", "EXPERIENCE (Role B)",
 "LEVEL NOT MARKED IN SOURCE. Presented as where seniority shows up, not as "
 "a hard requirement."),
("Controls and reporting", "operational controls; executive and board "
 "reporting", "5", "RESPONSIBILITY (Role B)", "Two source items joined."),
("Board-level communication", "board-level communication", "5",
 "EXPERIENCE (Role B)", "Verbatim. LEVEL NOT MARKED IN SOURCE."),
("A higher title doesn't just mean more of the same work.", "n/a", "5",
 "EDITORIAL",
 "The brief offered two bottom lines and said to prefer this one if "
 "uncertain. The other, same career level doesn't mean same judgment, would "
 "be inaccurate here: Role A asks for 8+ years at Senior Manager and Role B "
 "for 10+ at Director, so these are not the same career level."),

# ---------------------------------------------------------------- slide 6
("PE or public-company operating context",
 "PE-backed or publicly traded environments", "6", "EXPERIENCE (Role B)",
 "LEVEL NOT MARKED IN SOURCE. Shown as context the destination is built "
 "around, not as a stated hard requirement."),
("Financial reporting and controls",
 "financial and operational acumen; enterprise controls", "6",
 "EXPERIENCE (Role B)", "LEVEL NOT MARKED IN SOURCE."),
("Major corporate milestones and audits", "major corporate milestones / "
 "audits", "6", "EXPERIENCE (Role B)", "Verbatim. LEVEL NOT MARKED IN SOURCE."),
("Finance, accounting and legal partnership",
 "Finance / Accounting / Legal partnership", "6", "EXPERIENCE (Role B)",
 "Verbatim. LEVEL NOT MARKED IN SOURCE."),
("Board-level operating rhythm", "board-level communication; executive "
 "steering committees", "6", "EXPERIENCE + RESPONSIBILITY (Role B)",
 "Two source items joined into the operating pattern they describe."),
("Context the destination role is built around.", "n/a", "6", "EDITORIAL",
 "Used instead of the word requirements, because the source read does not "
 "mark these items required or preferred and calling them requirements would "
 "turn unmarked into required."),
("Better resume language doesn't create experience you haven't had.", "n/a",
 "6", "EDITORIAL", "From the brief. Says nothing about whether the viewer "
 "can make the move."),

# ---------------------------------------------------------------- slide 7
("Complex program delivery", "leads complex programs", "7", "OVERLAP READ",
 "Restated from slide 2."),
("Internal relationships / Company-specific systems / Existing reputation / "
 "Positional authority", "n/a", "7", "EDITORIAL",
 "Not from either posting. These are context-dependent items the spoken "
 "script names, listed as what does not automatically travel."),
("People leadership as the same source of seniority",
 "leads and develops project-management staff (Role A), absent from Role B",
 "7", "SOURCE-DERIVED READ",
 "Derived from the difference between the two postings, not from a claim in "
 "either."),
("Programs owned / Decisions made / Risks managed / Stakeholders influenced / "
 "Outcomes delivered", "n/a", "7", "EDITORIAL",
 "Evidence categories from the spoken script, not posting language."),
("Enterprise controls / Financial-reporting rigor / Public or PE operating "
 "context / Audit and milestone readiness / Board-level operating rhythm",
 "see slide 6 rows", "7", "EXPERIENCE (Role B)",
 "Carried from slide 6. MAY need is used because the individual's prior "
 "history is unknown."),
]

UNAVAILABLE = """
EMPLOYER NAMES AND SOURCE URLS ARE NOT IN THIS WORKSPACE.

The brief says to keep the real employer names and original source URLs in this
private file. They were not supplied with the task and they do not appear in
the flagship recording master, the thought blocks, the candidate Shorts, the
advisor handoff, or anywhere else in the workspace. They were not invented.

Every row above therefore maps public display text to the source language as
the build brief stated it, which is the strongest link available today. Before
these slides are published, three fields have to be filled in for both roles:

  EMPLOYER
  EXACT POSTING TITLE AS ADVERTISED
  SOURCE URL, COLLECTION DATE, REQUISITION OR WINDOW, CAPTURE ROUTE

Until those exist, the on-slide line "Two real U.S. job postings" rests on the
brief's statement that these are based on real U.S. job postings reviewed in
September 2026, and not on a record anyone can re-check.
"""

CLASSIFICATION = """
REQUIRED AGAINST PREFERRED

The source read marks exactly one item as preferred: Role A's
"regulated-industry / transformation experience preferred". Everything else
under "Experience includes" is stated without a required or preferred marker.

No slide turns an unmarked item into a required one, and no slide turns the one
preferred item into a requirement. Where destination experience appears on
slide 6 it is introduced as "context the destination role is built around"
rather than as "requirements", which is why that wording was chosen.

Role A's 8+ years and PMP or comparable certification, and Role B's 10+ years,
are all unmarked in the source read. None of them appears on any slide, so no
classification is asserted about them anywhere in the public assets.
"""
