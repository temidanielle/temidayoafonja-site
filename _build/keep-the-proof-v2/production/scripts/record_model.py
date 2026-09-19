#!/usr/bin/env python3
"""Shared field model for the Keep the Proof V2 Professional Record.
Drives the primary .docx, the portable .md mirror, and the fillable PDF,
so the underlying fields are identical across all three formats."""

TITLE = "YOUR PROFESSIONAL RECORD"
SUBTITLE = "A companion to Keep the Proof"

INTRO_LEAD = ("This is your record, not a form to submit. Make one copy that belongs only to you, "
    "keep it somewhere you control and your employer does not own, and add to it over time. "
    "It holds everything the guide produces, in one searchable place.")

INTRO_BULLETS = [
    ("Make it yours.", "Save your own copy in a personal account, protected with a unique password and multifactor authentication."),
    ("Keep it in one place.", "One record you maintain beats four you abandon."),
    ("Permission first.", "Everything here follows the one rule: your own recollection and what you are permitted to keep. Never paste in employer-owned files or confidential detail."),
    ("Fill only what applies.", "A short, honest entry beats a padded one. Blank fields are fine."),
]

INTRO_SECTIONS = ("Your record has six sections: a Capture Log, Full Entries, a Corroboration list, "
    "a Translation and Proof Line workspace, a running index, and two optional maintenance checklists.")

FORMATS_NOTE = ("Two formats, the same record. This copyable document is the recommended long-term home, "
    "because it stays searchable and easy to maintain over years. The Printable & Fillable Tools PDF in "
    "your bundle holds the same fields for anyone who prefers to write by hand or type into a form. Use "
    "whichever you will actually keep up. You do not need to complete both.")

# ---- Section 1: Capture Log ----
CAPTURE_FIELDS = [
    ("What happened?", "The event or piece of work, in a line.", 2),
    ("Your specific contribution or judgment", "Your part, not the team's.", 2),
    ("What changed, improved, became possible, or was prevented", "The consequence.", 2),
    ("Who could confirm this, or what public source supports it", "For a person, note their role and what they directly observed. Do not store private contact details. Any use of a public source stays subject to the permission rules.", 2),
    ("Confidential detail to keep out", "Name it, so you remember to leave it out.", 1),
    ("Date (optional)", "", 1),
    ("Trigger tag (optional)", "e.g. project ended, scope changed, praise or feedback, risk prevented, decision under uncertainty, measurable result, responsibility expanded.", 1),
]

# ---- Section 2: Full Entries ----
FULL_ENTRY_CLUSTERS = [
    ("Cluster A. When and what", [
        ("Date or period", "", 1),
        ("Project or work event", "", 1),
        ("Situation or need", "The problem or condition you were responding to.", 2),
        ("Why it mattered", "What was at stake if it went unaddressed.", 2),
    ]),
    ("Cluster B. What was actually yours", [
        ("Formal responsibility", "What you were assigned on paper.", 2),
        ("Actual ownership", "What you truly drove, which is often different.", 2),
        ("Scope and constraint", "Scale, complexity, or the limits you worked within.", 2),
        ("People and functions involved", "Who you worked with or influenced, by role.", 2),
    ]),
    ("Cluster C. The judgment inside it", [
        ("Decision or judgment exercised", "The call you made, and the options you weighed.", 3),
        ("Actions taken", "What you actually did.", 2),
    ]),
    ("Cluster D. What changed, and what supports it", [
        ("Outcome or observable change", "What was observably different afterward.", 2),
        ("Problem prevented", "The cost, delay, or risk that did not land. Use “would likely have,” not “definitely would have.”", 2),
        ("Quantitative evidence, accurate and permitted", "Numbers only when accurate and permitted. Never invented.", 2),
        ("Qualitative evidence or validation", "Feedback, recognition, or credible validation.", 2),
        ("Team result versus your honest part", "The shared outcome, and your honest share of it.", 2),
    ]),
    ("Cluster E. How you would say it, and who could confirm it", [
        ("Internal wording, before translation", "", 2),
        ("Portable-language version", "", 2),
        ("Who could corroborate this, by role, and what they directly observed", "Role and observation only; no personal contact details.", 2),
        ("Permitted evidence reference", "Name the permitted source or location. Do not paste the artifact or confidential content.", 2),
        ("Confidentiality and permission check", "Confirm nothing restricted is being kept.", 1),
        ("Retrieval tags", "Review, promotion, compensation, resume, interview, biography, transition.", 1),
    ]),
]
RECON_MARKER = ("Reconstruction marker (only when rebuilding after access loss): label the entry, or any "
    "field in it, as Known / Supported / Remembered but not verified / Uncertain, so a memory is never "
    "presented as a fact.")

# ---- Section 3: Corroboration list ----
CORROB_FIELDS = [
    ("The work it refers to", "A short label linking to the Full Entry.", 1),
    ("Who could confirm it, by role", "For example, “the operations manager I partnered with.” Not a stored personal contact record.", 1),
    ("What they directly observed", "The specific thing this person saw or worked on with you.", 2),
]
CORROB_NOTE = ("Keep this to role and observation. Do not store private contact details or personal "
    "information about the colleague inside your record. This list prepares you to reach the right person "
    "with specifics later, through your own means, if a moment ever calls for it.")

# ---- Section 4: Translation and Proof Line workspace ----
TRANSLATION_MOVES = [
    "Name to function.",
    "Assignment to contribution.",
    "Activity to consequence.",
    "Team to your part.",
    "Acronym to meaning.",
    "“Helped with” to real role.",
    "No number to credible detail.",
    "Number to scale.",
]
TRANSLATION_PROTECTION = ("Sensitive to permitted (protection rule): if the only accurate version would "
    "expose something you may not keep, omit it rather than reword it. Keep any team result separate from "
    "your own part throughout.")
PROOFLINE_INGREDIENTS = [
    ("The condition", "The problem or situation you were responding to.", 1),
    ("Your part", "The contribution, decision, or judgment that was yours.", 1),
    ("The scope or constraint", "The size or limits you worked within.", 1),
    ("The outcome", "What changed, or what was prevented.", 1),
    ("The support", "Permitted evidence or validation, when you have it.", 1),
]
PROOFLINE_RULE = ("A Proof Line does not need a number, must never contain an invented one, and never "
    "claims sole credit for a shared result.")

# ---- Section 5: Index ----
INDEX_COLUMNS = ["Title", "Date / period", "Function or role", "Retrieval tags", "Certainty (when rebuilding)"]

# ---- Section 6: Maintenance ----
MONTHLY = [
    "Look back over the month's projects, decisions, feedback, changes, and problems you helped prevent.",
    "Add Quick Captures for anything worth keeping.",
    "Expand the single most significant item into a Full Entry.",
    "Run the confidentiality check: is everything here permitted?",
    "Tag each item for retrieval.",
]
QUARTERLY = [
    "Read the quarter's entries in one sitting.",
    "Remove duplicates and anything too vague to be useful.",
    "Correct overstatement and add missing context while you still remember.",
    "Translate the strongest entries into Proof Lines.",
    "Note where evidence is thin, without drawing any conclusion about your career from the gap.",
    "Update your index.",
]
MAINT_NOTE = ("This is housekeeping, not a verdict. It organizes and translates what happened; it does not "
    "tell you what your career means.")
