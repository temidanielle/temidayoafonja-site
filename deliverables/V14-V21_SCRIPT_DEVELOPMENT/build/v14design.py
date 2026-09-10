# -*- coding: utf-8 -*-
"""The Video 14 research design.

This is a DESIGN. No postings have been collected, nothing has been coded,
and no finding exists. Every choice below that belongs to Temidayo is marked
FOR APPROVAL rather than settled here.
"""

QUESTION = ("Across three industries, how much of what a role actually "
            "requires is the same underlying work described in different "
            "language, and how much is a genuine requirement that does not "
            "carry across?")

SUB_QUESTIONS = [
 "Which requirements appear in every industry in the sample, in different "
 "words?",
 "Which requirements appear in only one industry, and what kind of "
 "requirement are they: domain knowledge, regulation, credential, tooling, "
 "or stated experience?",
 "Where a requirement looks shared, is the underlying decision the same "
 "decision, or only the same noun?",
 "How often is a stated requirement a hard requirement, and how often is it "
 "written as one but described as a preference elsewhere in the same "
 "posting?",
]

# 1 to 20, in the order the instruction lists them.
DESIGN = [
 ("1. The exact research question", QUESTION + "  This is the question the "
  "coding is built to answer. It is not a hypothesis about the answer."),

 ("2. The role family to compare",
  "PROPOSED, FOR APPROVAL. Program and project delivery roles at senior "
  "individual contributor level. Chosen because the same underlying work "
  "carries a different name in almost every industry, which is the video's "
  "subject rather than an accident of the sample. Alternative if Temidayo "
  "prefers a family closer to her own record: operational or business "
  "analysis roles. Pick one family and hold it. Comparing across families as "
  "well as across industries would make any difference impossible to "
  "attribute."),

 ("3. The three proposed industries",
  "PROPOSED, FOR APPROVAL. Healthcare, financial services, and technology."),

 ("4. Why those industries were selected",
  "They differ on the three things the comparison is trying to expose. "
  "Regulation: heavy in the first two and light in the third. Vocabulary: "
  "each has its own words for the same activity. Credentialing: two of them "
  "commonly name qualifications, one commonly does not. That spread makes "
  "both halves of the finding visible, the shared work and the genuine "
  "barrier. TO CONFIRM: at least one of the three should be an industry "
  "Temidayo can speak about credibly on camera, and if that is not true of "
  "any of these, replace one and record the substitution here. The selection "
  "is an editorial choice about what will teach well. It is not a claim that "
  "these three represent the labor market."),

 ("5. Inclusion criteria",
  "A posting is included when all of the following hold. It is a live "
  "posting or an archived posting with a recorded date. The employer sits in "
  "one of the three selected industries. The role belongs to the selected "
  "family, judged by the described work rather than by the job title. The "
  "seniority indicators fall in the band defined below. The posting is in "
  "English. The full text is captured, not a summary or a search-result "
  "snippet."),

 ("6. Exclusion criteria",
  "Excluded: agency or recruiter listings that do not name the hiring "
  "context; duplicate postings for the same role at the same employer, where "
  "the first collected instance is kept; postings shorter than roughly one "
  "hundred and fifty words, which cannot be coded on most fields; internal "
  "transfer-only postings; contract-of-convenience listings that describe no "
  "responsibilities; and any posting whose full text cannot be captured. "
  "Every exclusion is logged with its reason. The exclusion log is part of "
  "the result, not housekeeping, because the count of what was rejected is "
  "part of what makes the sample honest."),

 ("7. Seniority level",
  "Senior individual contributor. Practically: the posting expects "
  "independent ownership of work and typically names a multi-year experience "
  "expectation, and it does not make direct people management the core of "
  "the role. Where a posting includes incidental line management, record it "
  "in the notes and keep the posting, because excluding those would quietly "
  "bias the sample toward one industry's conventions."),

 ("8. Geographic scope",
  "PROPOSED, FOR APPROVAL. A single national market, so that regulation, "
  "credentialing and salary conventions are comparable across the three "
  "industries. Mixing markets would introduce a second variable and make any "
  "difference unattributable. Remote postings are included only where the "
  "employer sits in the selected market, and the work arrangement is coded "
  "either way."),

 ("9. Collection dates",
  "Not yet begun. When collection starts, record the first and last "
  "collection date and carry both into anything published. A sample is a "
  "photograph of a labor market on particular days. The date is part of the "
  "finding and belongs on screen wherever a number appears."),

 ("10. Minimum and target sample sizes",
  "Target: 30 postings, 10 per industry. Minimum for the comparison to be "
  "reportable at all: 24 postings, 8 per industry. If collection stops "
  "between those figures, the real number is what gets stated. If it stops "
  "below the minimum, the comparison is reported as partial and no headline "
  "number is used. The target is a plan. It is not a result, and it does not "
  "become one by being written down first."),

 ("11. Coding fields",
  "The thirteen coding fields named in the brief, plus provenance, "
  "requirement classification and coder notes. FIELD_TOTAL fields in all, "
  "defined in the codebook and shipped as the coding framework file. Every "
  "posting is coded on every field. Where a posting says nothing about a "
  "field, the value is NOT STATED, which is itself a finding and must not be "
  "recorded as absent or as zero."),

 ("12. How requirements will be categorized",
  "Each stated requirement is assigned to exactly one of five categories. "
  "CAPABILITY, something the person can do. DOMAIN, knowledge specific to "
  "the industry or its subject matter. CREDENTIAL, a qualification, "
  "registration or license. TOOL, a named platform or system. EXPERIENCE, a "
  "stated quantity or type of prior exposure. Where a requirement plausibly "
  "sits in two categories, the coder records the ambiguity in the notes and "
  "picks the narrower one, so that the shared-work count is conservative "
  "rather than flattering."),

 ("13. How capability overlap will be coded",
  "Two requirements count as overlapping only when the underlying decision "
  "is the same, not when the words match. The test is written out and "
  "applied the same way every time: describe what the person has to decide "
  "and what happens if they decide it badly. If those two descriptions match "
  "across postings, it is overlap. If only the noun matches, it is recorded "
  "as apparent overlap and counted separately. That distinction is the whole "
  "point of the video and it has to survive contact with the coding sheet."),

 ("14. How domain and context requirements will be coded",
  "Domain requirements are recorded verbatim, then classified by how they "
  "could be acquired: readable, meaning it can be learned from documentation "
  "or study; observable, meaning it comes from being present in the setting; "
  "or gated, meaning it requires access or authority the applicant would not "
  "have until hired. The classification is the coder's judgment and is "
  "recorded as such, with the verbatim text kept beside it so anybody can "
  "check the call."),

 ("15. How credentials and licensing will be treated",
  "Recorded verbatim, with three attributes: the issuing body if named, "
  "whether the posting presents it as required or preferred, and whether it "
  "is legally required to perform the work as described or is an employer "
  "preference. The third attribute is often not determinable from the "
  "posting alone. Where it is not, it is recorded as NOT DETERMINABLE FROM "
  "POSTING rather than guessed, and the video must not assert a legal "
  "requirement that the sample cannot establish."),

 ("16. What counts as a hard requirement versus a preference",
  "HARD when the posting uses required, must have, essential, or makes the "
  "role conditional on it. PREFERRED when it uses preferred, desirable, "
  "nice to have, or a plus. AMBIGUOUS when the same item appears in both "
  "registers within one posting, which happens often and is worth reporting "
  "on its own. The coder does not resolve an ambiguous case toward either "
  "side. It stays ambiguous and gets counted as its own category."),

 ("17. What job descriptions can establish",
  "What an employer chose to write down when advertising a role, on a "
  "specific date. The language an industry uses for the work. Which "
  "requirements employers think are worth stating. Which credentials get "
  "named. How often a stated requirement is framed as hard versus preferred. "
  "Patterns of similarity and difference in that written language across "
  "industries."),

 ("18. What job descriptions cannot establish",
  "That two roles are interchangeable. That the work described is the work "
  "actually done. That a candidate meeting the stated requirements would be "
  "interviewed, offered the role, or successful in it. What the employer "
  "would actually accept, as opposed to what they asked for. Anything about "
  "the labor market beyond the sampled postings. Anything about pay, "
  "progression or how the role is experienced. This list belongs in the "
  "video, not only in this document."),

 ("19. How the raw coded record will be preserved",
  "One row per posting in the coding framework file, with the source name, "
  "the URL, the collection date, and the full captured text stored "
  "separately and referenced by the posting identifier. The exclusion log is "
  "kept in the same place. The record is preserved so the count is "
  "reproducible by somebody else, which is the difference between having "
  "done research and having said so."),

 ("20. How any eventual numerical title will be tied to the actual sample",
  "The number in any title, thumbnail, description or spoken line is the "
  "count of postings actually coded and retained. If 26 are coded, the title "
  "says 26. The industry count is the number of industries actually "
  "represented in the retained sample. No number is used before the coded "
  "record exists, and no past-tense claim is made about work that has not "
  "been completed. Until then the planning title stands: Which Parts of Your "
  "Experience Will Transfer to Another Industry?"),
]

# Codebook: (field, type, definition, allowed values or format)
CODEBOOK = [
 ("posting_id", "identifier",
  "Unique identifier for the posting within this study.",
  "Industry prefix and a sequence number, for example HC-01."),
 ("industry", "category",
  "Which of the three selected industries the employer sits in.",
  "One of the three approved industry labels."),
 ("source", "text", "Where the posting was found.", "Site or platform name."),
 ("source_url", "text", "Direct link to the posting.", "Full URL."),
 ("collection_date", "date", "The date the posting text was captured.",
  "YYYY-MM-DD."),
 ("employer_type", "category",
  "The kind of organization, not its name.",
  "For example: public sector, large private, small private, nonprofit."),
 ("job_title", "text", "The posting's own title, verbatim.", "Verbatim."),
 ("problem_the_role_solves", "text",
  "In the coder's words, what this role exists to fix or produce.",
  "One or two sentences."),
 ("decisions_the_role_owns", "text",
  "What the person would decide, as opposed to perform. Where the posting "
  "does not say, record NOT STATED.",
  "List, or NOT STATED."),
 ("core_responsibilities", "text",
  "The main duties, condensed but not reinterpreted.",
  "List."),
 ("assumed_domain_knowledge", "text",
  "Industry or subject knowledge the posting assumes, verbatim where "
  "possible, then classified.",
  "Verbatim text plus readable, observable or gated."),
 ("tools_platforms", "text",
  "Named systems, platforms or software.",
  "List, or NOT STATED."),
 ("credentials", "text",
  "Qualifications or certifications named.",
  "Verbatim, plus issuing body if named, or NOT STATED."),
 ("licensing", "text",
  "Registration or license named, and whether the posting presents it as "
  "legally required.",
  "Verbatim, plus required, preferred, or NOT DETERMINABLE FROM POSTING."),
 ("years_of_experience", "text",
  "Stated quantity or type of prior experience.",
  "Verbatim figure or range, or NOT STATED."),
 ("stakeholder_scope", "text",
  "Who the role works across: teams, functions, external parties, "
  "seniority of the people involved.",
  "List, or NOT STATED."),
 ("accountability", "text",
  "What the person is answerable for if it goes wrong.",
  "Text, or NOT STATED."),
 ("decision_authority", "text",
  "What the posting says the person may decide without approval.",
  "Text, or NOT STATED."),
 ("work_arrangement", "category",
  "On site, hybrid, remote, or not stated.",
  "One of four values."),
 ("industry_terminology", "text",
  "Industry-specific words used for activities that exist elsewhere under "
  "other names. This field feeds the central comparison.",
  "List of terms with the plain-language equivalent."),
 ("requirement_categories", "text",
  "Each stated requirement assigned to exactly one category.",
  "CAPABILITY, DOMAIN, CREDENTIAL, TOOL or EXPERIENCE."),
 ("hard_or_preferred", "text",
  "How each requirement is framed by the posting.",
  "HARD, PREFERRED or AMBIGUOUS, per requirement."),
 ("overlap_test_note", "text",
  "For any requirement that looks shared with another industry: what the "
  "person has to decide, and what happens if they decide it badly.",
  "Free text. Feeds the real-overlap versus apparent-overlap count."),
 ("coder_notes", "text",
  "Ambiguities, judgment calls, and anything a second reader should check.",
  "Free text."),
]

EXCLUSION_FIELDS = [
 ("posting_id", "Identifier assigned before the exclusion decision."),
 ("source_url", "Direct link."),
 ("collection_date", "YYYY-MM-DD."),
 ("industry", "Intended industry."),
 ("exclusion_reason", "Which stated exclusion criterion applied."),
 ("notes", "Anything a second reader should be able to check."),
]

INTEGRITY = [
 "No job description is written, paraphrased into an example, or invented "
 "for illustration. Every posting in the record is a real posting that was "
 "found and captured.",
 "No finding is written before the coding exists. This document contains no "
 "results section for that reason.",
 "No number appears in any title, thumbnail, description or spoken line "
 "until it is the count of postings actually coded and retained.",
 "No past-tense claim is made about research that has not been completed.",
 "Similar language across postings is never reported as evidence that roles "
 "are equivalent, that an applicant is ready, or that a hiring decision "
 "would go a particular way.",
 "Where the posting does not say, the record says NOT STATED. Silence is "
 "never coded as absence.",
 "Employers are described by type, not named, unless there is a specific "
 "editorial reason to name one and it has been approved.",
 "If the completed comparison turns out to be uninteresting, that is "
 "reportable. A weak or mixed result is published as a weak or mixed "
 "result, or the video does not get made. It does not get improved.",
]

SEQUENCE = [
 ("Step 1", "Approve the role family, the three industries, and the "
            "geographic scope. Nothing collects until those three are "
            "settled, because changing them later invalidates the sample."),
 ("Step 2", "Pilot code three postings, one per industry, using the "
            "codebook as written. The pilot exists to find fields that do "
            "not work in practice."),
 ("Step 3", "Revise the codebook once, based on the pilot, and record what "
            "changed. After this point the codebook is fixed for the "
            "study."),
 ("Step 4", "Collect and code to the target, logging every exclusion as it "
            "happens rather than reconstructing the log afterward."),
 ("Step 5", "Second-pass check on a subset. Re-code a handful of postings "
            "without looking at the first pass and compare, to see whether "
            "the judgment calls are stable."),
 ("Step 6", "Count. Real overlap, apparent overlap, and requirements that "
            "do not carry. Hard versus preferred versus ambiguous. What was "
            "excluded and why."),
 ("Step 7", "Only now decide whether there is a video, what its title is, "
            "and whether any number belongs in that title."),
]


# The total is derived from the codebook rather than typed, so item 11 cannot
# disagree with the table that follows it.
DESIGN = [(h, b.replace("FIELD_TOTAL", str(len(CODEBOOK)))) for h, b in DESIGN]
