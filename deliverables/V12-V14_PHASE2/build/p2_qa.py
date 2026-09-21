# -*- coding: utf-8 -*-
"""The 20-item QA list, run against the BUILT documents on disk.

Each item either runs and reports a real result, or is recorded as NOT PERFORMED with
the reason. Nothing is marked passed that was not actually checked.
"""
import os, re, sys, docx
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p2_blocks as B, p2_shorts as S, p2_production as PR, p2_descriptions as D, p2_packaging as PK
import p2_checks_script as CH

PERFORMED, NOT_PERFORMED = "PERFORMED", "NOT PERFORMED"
VIDEOS = (12, 13, 14)

def paras(path):
    return [p.text.strip() for p in docx.Document(path).paragraphs if p.text.strip()]

def table_rows(path):
    out = []
    for t in docx.Document(path).tables:
        for r in t.rows:
            out.append([c.text.strip() for c in r.cells])
    return out

class Ctx:
    def __init__(self, root, files):
        self.root = root
        self.files = files   # {(n, kind): path}
    def p(self, n, kind):
        return os.path.join(self.root, self.files[(n, kind)])

def _spoken_from_master(path):
    """Spoken paragraphs of a built recording master.

    Section labels are found structurally: the house builder writes the label and then a
    "[NOT SPOKEN]" marker, so the label is always the paragraph directly before a marker.
    An earlier draft of this reader instead dropped short all-caps lines, which silently
    kept three long section labels ("WHAT YOU CAN STUDY AND WHAT YOU HAVE TO BE GIVEN" and
    the two V14 posting labels) inside the spoken stream and inflated two word counts.
    """
    ts = paras(path)
    marks = [i for i, t in enumerate(ts) if t.strip() == "[NOT SPOKEN]"]
    if not marks:
        return []
    drop = set()
    for i in marks:
        drop.add(i)
        drop.add(i - 1)
    start = marks[0] - 1
    out = []
    for i, t in enumerate(ts):
        if i < start or i in drop:
            continue
        if re.match(r"^\[\s*(CAMERA|ARTIFACT|SOUND)\s*\]", t):
            continue
        out.append(t)
    return out

def _label_reader_regression(path):
    """The structural reader must drop exactly one label per section, long ones included."""
    ts = paras(path)
    marks = [i for i, t in enumerate(ts) if t.strip() == "[NOT SPOKEN]"]
    labels = [ts[i - 1] for i in marks]
    kept = set(_spoken_from_master(path))
    return bool(labels) and not any(l in kept for l in labels)

def _spoken_from_blocks(path):
    """Spoken paragraphs of a built thought-block copy. Same structural rule as the master,
    plus the BLOCK nn markers. Written after the all-caps heuristic in the first draft let
    three long section labels through and inflated two counts."""
    ts = paras(path)
    marks = [i for i, t in enumerate(ts) if t.strip() == "[NOT SPOKEN]"]
    if not marks:
        return []
    drop = set()
    for i in marks:
        drop.add(i); drop.add(i - 1)
    out = []
    for i, t in enumerate(ts):
        if i < marks[0] - 1 or i in drop:
            continue
        if re.match(r"^BLOCK\s+\d+$", t.strip()):
            continue
        out.append(t)
    return out

def _printed_count(ts):
    """Read the count off a built document's header line, however kv() renders it."""
    for t in ts:
        m = re.match(r"^Spoken words[:\s]+([\d,]+)$", t.strip())
        if m:
            return int(m.group(1).replace(",", ""))
    return None

def _is_faith_header(t):
    return t.strip().upper().endswith("A FAITH ANCHOR")

ITEMS = []
def item(num, name):
    def deco(fn):
        ITEMS.append((num, name, fn)); return fn
    return deco

# ---------------------------------------------------------------- 1-5 script integrity
@item(1, "Thought blocks reproduce the recording master word for word, in order")
def q1(c):
    bad = []
    for n in VIDEOS:
        a = " ".join(_spoken_from_master(c.p(n, "master"))).split()
        b = " ".join(_spoken_from_blocks(c.p(n, "blocks"))).split()
        if a != b:
            first = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
            bad.append("V%d master %d tokens, blocks %d tokens, first divergence at token %d"
                       % (n, len(a), len(b), first))
    probe = all(_label_reader_regression(c.p(n, "master")) for n in VIDEOS)
    return PERFORMED, (not bad and probe), bad or (
        "V12, V13 and V14 all reconstruct exactly: %s tokens."
        % ", ".join(str(len(" ".join(_spoken_from_master(c.p(n, "master"))).split()))
                    for n in VIDEOS))

@item(2, "Section labels are marked NOT SPOKEN in every recording master")
def q2(c):
    bad = []
    for n in VIDEOS:
        ts = paras(c.p(n, "master"))
        labels = [t for t in ts if t.endswith("[NOT SPOKEN]")]
        import importlib
        m = importlib.import_module(B.MODS[n])
        if len(labels) != len(m.SECTIONS):
            bad.append("V%d: %d labels for %d sections" % (n, len(labels), len(m.SECTIONS)))
    return PERFORMED, not bad, bad or "Every section carries the marker."

@item(3, "Every thought block is between 2 and 5 sentences")
def q3(c):
    bad = []
    for n in VIDEOS:
        _, _, b = B.verify(n)
        bad += ["V%d %s" % (n, s) for s, _ in b]
    return PERFORMED, not bad, bad or "132 blocks across the three videos, all in range."

@item(4, "The printed word count matches the spoken text in the same file")
def q4(c):
    """The house kv() helper renders \u201cSpoken words  1,266\u201d with no colon, so the first
    draft of this check looked for a colon and reported all three files as having no printed
    count. That was a checker-scope error, not a missing number. printed_count_regression()
    below proves the corrected reader still catches a count that does not match the text."""
    bad = []
    for n in VIDEOS:
        stated = _printed_count(paras(c.p(n, "master")))
        counted = len(" ".join(_spoken_from_master(c.p(n, "master"))).split())
        if stated is None:
            bad.append("V%d has no printed count" % n); continue
        if stated != counted:
            bad.append("V%d printed %d, file contains %d" % (n, stated, counted))
    ok_probe = (_printed_count(["Spoken words  1,266"]) == 1266
                and _printed_count(["x"]) is None
                and all(_label_reader_regression(c.p(n, "master")) for n in VIDEOS))
    for n in VIDEOS:
        mod = sum(len(p.split()) for _, p in CH.spoken(n))
        doc = len(" ".join(_spoken_from_master(c.p(n, "master"))).split())
        if mod != doc:
            bad.append("V%d script module %d, built document %d" % (n, mod, doc))
    return PERFORMED, (not bad and ok_probe), bad or (
        "Printed, read back from the file, and recomputed from the script module all agree: "
        + ", ".join("V%d %d" % (n, _printed_count(paras(c.p(n, "master")))) for n in VIDEOS) + ".")

@item(5, "No em dashes or en dashes anywhere in spoken text")
def q5(c):
    bad = []
    for n in VIDEOS:
        for t in _spoken_from_master(c.p(n, "master")):
            if "—" in t or "–" in t:
                bad.append("V%d: %s" % (n, t[:60]))
    return PERFORMED, not bad, bad or "Clean in all three masters."

# ---------------------------------------------------------------- 6-8 shorts
@item(6, "Every Shorts line is a consecutive run of sentences from its master")
def q6(c):
    bad = []
    for k in sorted(S.SHORTS):
        bad += ["V%d S%d: %s" % (k[0], k[1], x[:50]) for x in S.verbatim_problems(k)]
    ok_probe = S.stitch_regression()
    return PERFORMED, (not bad and ok_probe), bad or ("Nine Shorts clean. The check was also run "
            "against a deliberately stitched pair of non-adjacent master sentences and rejected it.")

@item(7, "Each Short carries exactly one ask")
def q7(c):
    bad = ["V%d S%d has %d" % (k[0], k[1], S.actions(k)) for k in sorted(S.SHORTS)
           if S.actions(k) != 1]
    return PERFORMED, not bad, bad or ("Counted as instructions, not verbs. A bare “and” "
            "keeps two steps of one task together; a new imperative sentence or a “Then” "
            "starts another.")

@item(8, "Every Short is under 150 words and inside 55 seconds at 165 wpm")
def q8(c):
    bad = ["V%d S%d %dw %.1fs" % (k[0], k[1], S.words(k), S.seconds(k, 165))
           for k in sorted(S.SHORTS)
           if S.words(k) >= 150 or S.seconds(k, 165) > 55]
    over150 = ["V%d S%d %.0fs" % (k[0], k[1], S.seconds(k, 150)) for k in sorted(S.SHORTS)
               if S.seconds(k, 150) > 55]
    note = "Range %d to %d words." % (min(S.words(k) for k in S.SHORTS),
                                      max(S.words(k) for k in S.SHORTS))
    if over150:
        note += " At the slower 150 wpm planning rate these cross 55 seconds and are flagged in " \
                "the Shorts documents: " + ", ".join(over150) + "."
    return PERFORMED, not bad, bad or note

# ---------------------------------------------------------------- 9-11 production
@item(9, "Every production cue is anchored to a real sentence in the master")
def q9(c):
    bad = PR.anchors_ok()
    return PERFORMED, not bad, bad or "All camera, artifact and sound cues resolve."

@item(10, "Camera, artifact and sound counts sit inside the brief's guide ranges")
def q10(c):
    bad = []
    for n in VIDEOS:
        if not 3 <= len(PR.CAMERA[n]) <= 5: bad.append("V%d camera %d" % (n, len(PR.CAMERA[n])))
        if not 2 <= len(PR.BROLL[n]) <= 4: bad.append("V%d artifact %d" % (n, len(PR.BROLL[n])))
        if not 4 <= len(PR.SOUND[n]) <= 7: bad.append("V%d sound %d" % (n, len(PR.SOUND[n])))
    detail = "; ".join("V%d %d/%d/%d" % (n, len(PR.CAMERA[n]), len(PR.BROLL[n]), len(PR.SOUND[n]))
                       for n in VIDEOS)
    return PERFORMED, not bad, bad or detail

@item(11, "Watch Next is a full-screen card and the last card listed for every video")
def q11(c):
    bad = []
    for n in VIDEOS:
        ids = [x[0] for x in PR.FULLSCREEN[n]]
        if not ids[-1].endswith("WATCH_NEXT"):
            bad.append("V%d last card is %s" % (n, ids[-1]))
        if sum(1 for i in ids if i.endswith("WATCH_NEXT")) != 1:
            bad.append("V%d has %d watch-next cards" % (n, sum(1 for i in ids if i.endswith("WATCH_NEXT"))))
    return PERFORMED, not bad, bad or "One card each, final in every list."

@item(12, "Watch Next routing is V12 to V13, V13 to V14, V14 to V12")
def q12(c):
    t12 = " ".join(_spoken_from_master(c.p(12, "master"))).lower()
    t13 = " ".join(_spoken_from_master(c.p(13, "master"))).lower()
    t14 = " ".join(_spoken_from_master(c.p(14, "master"))).lower()
    ok = ("which parts of your experience actually transfer to another industry?" in t12
          and "two real postings side by side" in t13
          and "turn one accomplishment into proof in 10 minutes" in t14)
    return PERFORMED, ok, ("V13 points forward by description rather than by title, because V14's "
            "title is not approved. The V13 Watch Next card carries the title and is re-settable "
            "without a re-record.")

# ---------------------------------------------------------------- 13-14 publishing
@item(13, "Exactly one resource link in every description")
def q13(c):
    bad = []
    for n in VIDEOS:
        urls = [u for t in paras(c.p(n, "desc")) for u in re.findall(r"https?://\S+", t)]
        real = [u for u in urls if "temidayoafonja.com" in u]
        if len(real) != 1:
            bad.append("V%d has %d resource links: %s" % (n, len(real), real))
    return PERFORMED, not bad, bad or "One each: career-evidence-starter, fieldkit, career-decisions."

@item(14, "The faith anchor is present, attributed, and is not a second call to action")
def q14(c):
    bad = []
    for n in VIDEOS:
        ts = paras(c.p(n, "desc"))
        try:
            i = [j for j, t in enumerate(ts) if _is_faith_header(t)][0]
        except IndexError:
            bad.append("V%d has no faith anchor" % n); continue
        tail = ts[i:]
        if not any("NLT" in t for t in tail): bad.append("V%d anchor is not attributed" % n)
        if not any("Tyndale" in t for t in tail): bad.append("V%d has no copyright line" % n)
        if any(re.search(r"https?://", t) for t in tail): bad.append("V%d anchor carries a link" % n)
        if sum(1 for t in tail if re.search(r"\(NLT", t)) != 1:
            bad.append("V%d does not carry exactly one scripture reference" % n)
    # The house sub() helper upper-cases its heading, so the header renders as
    # "A FAITH ANCHOR". The first draft matched mixed case and reported all three
    # descriptions as having no anchor: a checker-scope error, not a missing anchor.
    probe = _is_faith_header("\U0001F64F A FAITH ANCHOR") and not _is_faith_header("WATCH NEXT")
    return PERFORMED, (not bad and probe), bad or ("One NLT verse each, clearly separated from "
            "the resource, with no link and no ask inside the anchor.")

# ---------------------------------------------------------------- 15-19 claim discipline
@item(15, "V13's sample numbers survive into the built documents unchanged")
def q15(c):
    body = " ".join(_spoken_from_master(c.p(13, "master")) + paras(c.p(13, "desc"))).lower()
    need = ["fifty-five", "forty", "twenty-eight", "eighteen entries",
            "ten healthcare", "ten financial services", "eight technology",
            "55", "40", "28", "18", "september 10, 2026"]
    miss = [x for x in need if x not in body]
    return PERFORMED, not miss, miss or "All of ~55, 40, 28, 18 and 10/10/8 present, with the date."

@item(16, "No industry-wide generalization in any built spoken text")
def q16(c):
    pats = [r"healthcare employers", r"technology companies want", r"financial services always",
            r"tech companies (think|want|believe)", r"banks want", r"the industry believes"]
    bad = []
    for n in VIDEOS:
        t = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc"))).lower()
        bad += ["V%d: %s" % (n, p) for p in pats if re.search(p, t)]
    return PERFORMED, not bad, bad or "Employers are named only at the level of what a posting says."

@item(17, "No mind-reading assertion in any built spoken text")
def q17(c):
    bad = []
    for n in VIDEOS:
        t = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc")))
        bad += ["V%d: %s" % (n, s[:60]) for _, s in CH.mindread_hits(t)]
    return PERFORMED, (not bad and CH.mindread_regression()), bad or ("Sentences that refuse the "
            "claim are not counted; the narrowed check was re-run against an injected assertion "
            "and still fires.")

@item(18, "Neither V13 nor V14 describes the postings as live or open")
def q18(c):
    pats = [r"currently hiring", r"still open", r"go apply to (these|them)",
            r"you can apply to (these|them)", r"these (jobs|roles|postings) are (open|live)"]
    bad = []
    for n in (13, 14):
        t = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc"))).lower()
        bad += ["V%d: %s" % (n, p) for p in pats if re.search(p, t)]
        if "closed" not in t and "past their posted dates" not in t:
            bad.append("V%d does not disclose staleness" % n)
    return PERFORMED, not bad, bad or "Both state the collection date and that postings were closed."

@item(19, "V12 does not turn the four questions into a named framework")
def q19(c):
    t = " ".join(_spoken_from_master(c.p(12, "master")) + paras(c.p(12, "desc"))).lower()
    pats = [r"the \w+ (framework|method|formula|system|model)", r"i call (this|it) the",
            r"\bthe four-line\b", r"my (framework|method|formula)", r"\bacronym\b"]
    bad = [p for p in pats if re.search(p, t)]
    return PERFORMED, not bad, bad or ("The four questions are asked in plain sentences and never "
            "named, abbreviated, or capitalized into a label. The artifact carries the teaching.")

@item(20, "Every V14 deliverable is labelled working and packaging-pending")
def q20(c):
    bad = []
    for kind in ("master", "blocks", "prod", "shorts", "desc", "prov"):
        path = c.p(14, kind)
        if "_WORKING" not in os.path.basename(path):
            bad.append("filename not marked: " + os.path.basename(path))
        if not any("PACKAGING PENDING TEMIDAYO APPROVAL" in t for t in paras(path)):
            bad.append("no in-document label: " + os.path.basename(path))
    return PERFORMED, not bad, bad or "Six V14 files, each marked in the filename and on page one."

# ---------------------------------------------------------------- honestly not performed
NOT_DONE = [
 ("Runtime", "No footage exists. Every duration in this pack is arithmetic on the word count at a "
             "stated words-per-minute rate. Nothing was measured."),
 ("Thumbnails", "No thumbnail was designed or rendered. Thumbnail text is specified, not produced."),
 ("Full-screen card art", "Card copy and labels are specified. No PNG or SVG was rendered for "
                          "V12, V13 or V14 in this pass."),
 ("Posting URLs", "The four posting URLs were not re-fetched. Every posting detail is read from "
                  "the September 10, 2026 research record, which is checksummed in each provenance "
                  "document. No new external research was performed."),
 ("Scripture wording", "The three NLT verses were written from the translation as known, not "
                       "checked against a licensed NLT text in this pass. Confirm each against an "
                       "NLT edition before publishing. The Tyndale permission line is included."),
 ("Resource pages", "The three resource URLs were taken from the shipped V4 to V11 descriptions. "
                    "None was loaded to confirm it is live."),
 ("V14 packaging", "Not chosen. Five options are presented and one is recommended. The working "
                   "script is built on the recommendation so a complete episode exists to react to."),
 ("Reading level", "No readability score was computed. Voice was written to the brief and checked "
                   "by reading, not measured."),
]

def run(ctx):
    rows = []
    for num, name, fn in sorted(ITEMS):
        state, ok, detail = fn(ctx)
        rows.append(dict(n=num, name=name, state=state, ok=ok,
                         detail=detail if isinstance(detail, str) else "; ".join(map(str, detail))))
    return rows
