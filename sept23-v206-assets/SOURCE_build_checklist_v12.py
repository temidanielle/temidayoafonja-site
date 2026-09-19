# -*- coding: utf-8 -*-
"""Manual Maven and Website Edit Checklist — v1.1 -> v1.2.

Two things changed since v1.1 and both matter operationally.

First, parts of v1.1 have already been applied on the live Maven page. The
instructor title and bio now use Career Portability language, so v1.2 marks
those sections ALREADY CURRENT and tells the operator not to paste the older
copy back over them. A checklist that instructs someone to undo a correction is
worse than no checklist.

Second, the Private Capability Position Read is retired as an offer but is still
live on the website. That is now the largest item here, with file and line
references, because nothing in this package can publish it.

maven.com and temidayoafonja.com are both blocked by this environment's egress
proxy, so nothing below was read from a live page. Every "current" value is
quoted and must be confirmed on screen before editing.
"""
import copy, hashlib, os, shutil
import docx

SRC = "sept23-v205-assets/Manual_Maven_and_Website_Edit_Checklist_v1.1.docx"
OUT = "scratchpad/sept23/out"
DST = f"{OUT}/Manual_Maven_and_Website_Edit_Checklist_v1.2.docx"
STAMP = "Saturday, September 19, 2026 at 8:30 AM CT"
OLD = "Friday, September 4, 2026 at 6:40 AM CT"

SUBS = [("v1.1", "v1.2"), (OLD, STAMP), ("deck v2.0.5", "deck v2.0.6")]

TITLE_NOTE = (
 "ALREADY CURRENT — DO NOT OVERWRITE. The live instructor title already reads "
 "Career Portability Advisor. This section is kept so the change stays on the "
 "record, not so it is applied twice. Read the live page first: if it already "
 "reads Career Portability Advisor, do nothing here.")

PARA = [
 (8, "Replace the current bio with this text exactly:",
  "ALREADY CURRENT — DO NOT OVERWRITE. The live bio already uses Career "
  "Portability language. Do not paste the version below over it. Read the live "
  "bio first, and use the text below only to check that nothing important is "
  "missing from it."),
 (16, "Bring the copy closer to experienced professionals",
  "Recognize the experienced professional before teaching anything. The reader may "
  "be performing well, trusted with important work and carrying real "
  "responsibility, and still be less certain about what the work is building for "
  "the future. Do not describe the audience as early-career and do not overclaim."),
 (18, "Reorganizations, AI and industry change are moving faster",
  "Suggested direction, to adapt rather than paste: experienced professionals can "
  "be performing well, trusted with important work and carrying real "
  "responsibility while becoming less certain about what the work is building for "
  "the future. The difficult question is not only whether the job is good or bad. "
  "It is whether the work is still expanding your judgment, what would remain "
  "useful if the context changed, and what your recent evidence supports testing "
  "next. This live assessment uses your own last 90 days of work to help you read "
  "that more clearly."),
 (21, "Event title reads",
  "Event title reads “Stay or Leave?” with “Live Career Growth Assessment”. The "
  "deck matches this. If the live page differs, the deck is wrong and must be "
  "corrected rather than the page."),
 (33, "The Private Read routing question in section F is recorded as unresolved.",
  "The Private Capability Position Read is retired as an offer but is still live on "
  "the website. Removing it is the largest item in section F and it cannot be done "
  "from this package. Career Move Review has no route at all yet, which is why deck "
  "v2.0.6 keeps it off the participant-facing continuation slide."),
]

# Section C is now the full three-outcome architecture rather than one fix.
OUTCOMES = [
 ("Field", "Value"),
 ("Outcome 3 — replace", "Decide your next career move"),
 ("Outcome 3 — with", "Identify which move is worth testing next"),
 ("Outcome 3 — supporting copy",
  "Evaluate seven move categories and leave with a Next-Move Note naming the "
  "direction your evidence supports testing next."),
 ("Outcome 1 — review",
  "See whether your current work is still building you. Supporting copy: use "
  "evidence from your last 90 days of actual work to distinguish continued "
  "formation from familiar performance."),
 ("Outcome 2 — review",
  "See what may still count when the context changes. Supporting copy: examine "
  "what may travel beyond your current role or employer, where the evidence is "
  "strong, and what may still need testing or relearning. Do not promise "
  "destination-specific portability when no destination has been named."),
 ("Why",
  "The session does not make the stay-or-leave decision for the participant and "
  "the listing must not promise that it does. This is the same boundary the deck "
  "and the SOP hold."),
]

# Section F, rewritten around what is actually on the live site.
WEBSITE = [
 ("Item", "Change"),
 ("Private Read removal — LARGEST ITEM",
  "The retired offer is still live. fieldkit.html carries a Private Capability "
  "Position Read section with an “Enquire about the Private Read” CTA pointing at "
  "work.html#get-in-touch. for-professionals.html carries a Private Capability "
  "Position Read block with a mailto CTA. content/site-source-of-truth.json still "
  "describes it as a current offer. All three need a decision and a deployment. "
  "Nothing in this package publishes them."),
 ("Career Move Review — DOES NOT EXIST YET",
  "No page, no route, no copy, on any branch. Until a verified "
  "individual-professional route exists, it stays off the participant-facing "
  "continuation slide and is not sold from the stage. Do not route it to the "
  "enterprise Advisory page and do not reuse a retired Private Read link."),
 ("For Professionals page — outcome language",
  "Change any equivalent of “decide your next move” to “identify which move is "
  "worth testing next”. Same boundary as the Maven listing."),
 ("Field Kit route",
  "temidayoafonja.com/fieldkit is the participant-facing route on the deck face, "
  "the QR target and the prebuilt chat message. Confirm the page is live, resolves "
  "without a redirect chain, and shows the current $150 price."),
 ("Keep the Proof and Career Evidence Starter",
  "Both are live and both are deliberately absent from the recorded continuation "
  "sequence. Keep the Proof at $49 belongs in follow-up, matched to the person who "
  "has done the work but has no record of it."),
 ("Preserve unchanged",
  "September 23, free, 60 minutes, current live time, Field Kit $150."),
 ("Verify every individual-professional CTA",
  "Each one should reach an individual path. The enterprise Advisory page is a "
  "different audience and a different offer."),
]


def set_para(para, text):
    runs = para.runs
    keep = next((r for r in runs if r.text.strip()), runs[0])
    keep.text = text
    for r in runs:
        if r._r is not keep._r:
            r._r.getparent().remove(r._r)


def set_cell(cell, text):
    p = cell.paragraphs[0]
    for extra in cell.paragraphs[1:]:
        extra._element.getparent().remove(extra._element)
    set_para(p, text)


def fill(table, rows):
    template = copy.deepcopy(table.rows[1]._element)
    while len(table.rows) > 1:
        table._element.remove(table.rows[-1]._element)
    for ci, v in enumerate(rows[0]):
        set_cell(table.rows[0].cells[ci], v)
    for row in rows[1:]:
        table._element.append(copy.deepcopy(template))
        for ci, v in enumerate(row):
            set_cell(table.rows[-1].cells[ci], v)


def build():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SRC, DST)
    d = docx.Document(DST)

    for p in d.paragraphs:
        for r in p.runs:
            t = r.text
            for a, b in SUBS:
                t = t.replace(a, b)
            if t != r.text:
                r.text = t
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    for r in p.runs:
                        s = r.text
                        for a, b in SUBS:
                            s = s.replace(a, b)
                        if s != r.text:
                            r.text = s

    # Section A has no prose line of its own, so the already-current notice is
    # inserted after its heading rather than replacing something.
    heading_a = d.paragraphs[3]
    assert "A. Maven — instructor title" in heading_a.text, "section A moved"
    el = copy.deepcopy(d.paragraphs[7]._element)
    heading_a._element.addnext(el)
    from docx.text.paragraph import Paragraph
    set_para(Paragraph(el, heading_a._parent), TITLE_NOTE)

    for idx, expect, new in PARA:
        para = d.paragraphs[idx]
        assert expect in para.text, \
            f"P{idx}: expected {expect[:38]!r}, found {para.text[:70]!r}"
        set_para(para, new)

    assert "Decide your next career move" in d.tables[2].rows[1].cells[1].text
    fill(d.tables[2], OUTCOMES)
    assert "Private Read" in d.tables[3].rows[2].cells[0].text
    fill(d.tables[3], WEBSITE)

    d.save(DST)
    return DST


if __name__ == "__main__":
    path = build()
    print("built", os.path.basename(path))
    print("  sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())
