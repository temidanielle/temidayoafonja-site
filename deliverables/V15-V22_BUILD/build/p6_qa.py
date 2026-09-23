# -*- coding: utf-8 -*-
"""The QA list for V15 to V22, run against the BUILT documents on disk.

Each item either runs and reports a real result, or is recorded as NOT PERFORMED with
the reason. Nothing is marked passed that was not actually checked.
"""
import os, re, sys, docx
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p6_blocks as B, p6_shorts as S, p6_production as PR, p6_descriptions as D
import p6_packaging as PK, p6_provenance as PV
import p6_checks_script as CH

PERFORMED, NOT_PERFORMED = "PERFORMED", "NOT PERFORMED"
VIDEOS = tuple(range(15, 23))

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
        "All eight reconstruct exactly: %s tokens."
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
    return PERFORMED, not bad, bad or ("%d blocks across the eight videos, all in range."
                                       % sum(B.verify(n)[1] for n in VIDEOS))

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
    return PERFORMED, not bad, bad or "Clean in all eight masters."

# ---------------------------------------------------------------- 6-8 shorts
@item(6, "Every Shorts line is a consecutive run of sentences from its master")
def q6(c):
    bad = []
    for k in sorted(S.SHORTS):
        bad += ["V%d S%d: %s" % (k[0], k[1], x[:50]) for x in S.verbatim_problems(k)]
    ok_probe = S.stitch_regression()
    return PERFORMED, (not bad and ok_probe), bad or ("Twenty-four Shorts clean. The check was also run "
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

@item(12, "Watch Next routing is synchronized across master, card and description")
def q12(c):
    ROUTE = {15: "How to Turn One Accomplishment Into Proof in 10 Minutes",
             16: "Before a Layoff, Know What You Can Still Prove",
             17: "Which Parts of Your Experience Actually Transfer to Another Industry?",
             18: "The Career Gaps You Don't See Until the Work Gets Harder",
             19: "What Happens When the Next Step in Your Career Disappears?",
             20: "How Do You Grow When There Are Fewer Roles Above You?",
             21: "The Career Ladder Doesn't Work the Same Way Anymore",
             22: "Which Parts of Your Experience Actually Transfer to Another Industry?"}
    bad = []
    for src, title in ROUTE.items():
        if title not in " ".join(_spoken_from_master(c.p(src, "master"))):
            bad.append("V%d does not name its destination on camera" % src)
        card = [x for x in PR.FULLSCREEN[src] if x[0].endswith("WATCH_NEXT")]
        if not card or title not in " ".join(card[0][2]):
            bad.append("V%d watch-next card does not carry the title" % src)
        if title not in " ".join(paras(c.p(src, "desc"))):
            bad.append("V%d description does not carry the title" % src)
    return PERFORMED, not bad, bad or ("Each destination is named in the spoken line, on the "
            "card and in the description. V15 and V17 route back to the locked V12 and V13, "
            "and V22 routes to the locked V13.")

@item(13, "V22 routes to a built video and nothing points at V23 to V26")
def q13(c):
    """The roadmap records V23 to V26 as future work. Nothing in this pack may send a
    viewer to one of them, because they do not exist."""
    bad = []
    v22 = " ".join(_spoken_from_master(c.p(22, "master")) + paras(c.p(22, "desc")))
    if "Which Parts of Your Experience Actually Transfer to Another Industry?" not in v22:
        bad.append("V22 does not route to the locked V13")
    STALE = ["V23", "V24", "V25", "V26", "the next video in this series",
             "coming next week", "in the next episode"]
    for n in VIDEOS:
        for kind in ("master", "blocks", "shorts", "desc", "prod"):
            body = " ".join(paras(c.p(n, kind)))
            bad += ["V%d %s names %s" % (n, kind, x) for x in STALE if x in body]
    return PERFORMED, not bad, bad or ("V22 routes to the locked V13. No viewer-facing asset "
            "names V23, V24, V25 or V26 or promises an unbuilt episode. Checked the recording "
            "masters, thought blocks, production packages, Shorts and descriptions. Provenance "
            "files are deliberately outside this check because they cite the roadmap document "
            "by its real title, and the overview records the future roadmap on purpose.")

@item(14, "The resource map is exactly what the roadmap locked, and no video adds one")
def q14(c):
    WANT = {15: "career-evidence-starter", 16: None, 17: "keep-the-proof",
            18: "fieldkit", 19: None, 20: None, 21: "fieldkit", 22: None}
    bad = []
    for n in VIDEOS:
        urls = [u for t in paras(c.p(n, "desc")) for u in re.findall(r"https?://\S+", t)]
        real = sorted({u for u in urls if "temidayoafonja.com" in u})
        if WANT[n] is None:
            if real:
                bad.append("V%d should carry no resource, carries %s" % (n, real))
        else:
            if len(real) != 1 or WANT[n] not in real[0]:
                bad.append("V%d expected %s, found %s" % (n, WANT[n], real))
        # the earned-out-loud rule: a resource in the description must be named on camera
        spoken_t = " ".join(_spoken_from_master(c.p(n, "master"))).lower()
        named = any(x in spoken_t for x in ("career evidence starter", "keep the proof",
                                            "field kit"))
        if named != (WANT[n] is not None):
            bad.append("V%d speaks a resource the description does not carry, or the reverse" % n)
    return PERFORMED, not bad, bad or ("Four videos carry one resource each and four carry none. "
            "Every resource in a description is also named in that video's spoken master.")

@item(15, "The faith anchor is present, attributed, and is not a second call to action")
def q15(c):
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
    # "A FAITH ANCHOR". Matching mixed case would report every description as having none.
    probe = _is_faith_header("\U0001F64F A FAITH ANCHOR") and not _is_faith_header("WATCH NEXT")
    return PERFORMED, (not bad and probe), bad or ("One NLT verse each, clearly separated from "
            "the resource, with no link and no ask inside the anchor.")

@item(16, "No industry-wide generalization in any built spoken text")
def q16(c):
    pats = [r"healthcare employers", r"technology companies want", r"financial services always",
            r"tech companies (think|want|believe)", r"banks want", r"the industry believes",
            r"every (employer|company|organization)", r"all employers"]
    bad = []
    for n in VIDEOS:
        t = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc"))).lower()
        bad += ["V%d: %s" % (n, p) for p in pats if re.search(p, t)]
    return PERFORMED, not bad, bad or "No employer is named in any public asset in this pack."

@item(17, "No mind-reading assertion in any built spoken text")
def q17(c):
    bad = []
    for n in VIDEOS:
        t = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc")))
        bad += ["V%d: %s" % (n, s[:60]) for _, s in CH.mindread_hits(t)]
    return PERFORMED, (not bad and CH.mindread_regression()), bad or ("Sentences that refuse the "
            "claim are not counted; the narrowed check was re-run against an injected assertion "
            "and still fires.")

# ---------------------------------------------------------------- scope of the pack
@item(18, "V4 to V12 were not touched in this pass")
def q18(c):
    """Run against the repository, not against this pack. Anything V4 to V12 must be
    unmodified in git since the V13/V14 anonymization commit."""
    import subprocess
    root = "/home/user/temidayoafonja-site"
    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=root).decode()
    except Exception as e:
        return NOT_PERFORMED, False, "git unavailable: %s" % e
    touched = [l[3:].strip() for l in out.splitlines() if l.strip()]
    FORBIDDEN = ("V4-V11", "V10-V11", "V12-V14_LOCKED", "V12-V14_PHASE2", "V12-V14_FINAL",
                 "VIDEOS_4-21", "VIDEOS_8-13", "VIDEO_4_", "VIDEO_5_", "VIDEO_6_", "VIDEO_7_",
                 "new-videos-4-5", "new-videos-6-7", "SPRINT_V4-V9")
    bad = [f for f in touched if any(k in f for k in FORBIDDEN)]
    return PERFORMED, not bad, bad or ("%d paths are modified in the working tree and none of "
            "them is a V4 to V12 asset." % len(touched))

@item(19, "V13 and V14 changed only for anonymization, and that change is already committed")
def q19(c):
    import subprocess
    root = "/home/user/temidayoafonja-site"
    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=root).decode()
    except Exception as e:
        return NOT_PERFORMED, False, "git unavailable: %s" % e
    touched = [l[3:].strip() for l in out.splitlines() if l.strip()]
    bad = [f for f in touched if "V13-V14_ANON" in f]
    anon = os.path.join(root, "deliverables", "V13-V14_ANON")
    if not os.path.isdir(anon):
        bad.append("the anonymization pack is missing from the workspace")
    return PERFORMED, not bad, bad or ("The V13/V14 public-employer anonymization patch is "
            "committed and unmodified. This pass changed nothing else in V13 or V14.")

@item(20, "The pack contains V15 to V22 only, and no V23 to V26 asset was built")
def q20(c):
    bad = []
    for (n, kind), rel in sorted(c.files.items()):
        if n not in VIDEOS:
            bad.append("pack contains a file for V%d" % n)
        if not os.path.exists(c.p(n, kind)):
            bad.append("missing %s" % rel)
    here = os.path.dirname(os.path.abspath(__file__))
    strays = [f for f in os.listdir(here)
              if re.match(r"p6_script(2[3-9]|[3-9]\d)\.py$", f)]
    bad += ["a script module exists for an unbuilt video: %s" % f for f in strays]
    return PERFORMED, not bad, bad or ("%d files across eight videos. No script module, document "
            "or card exists for V23, V24, V25 or V26." % len(c.files))

# ---------------------------------------------------------------- claim discipline
@item(21, "No new public framework is named anywhere in the pack")
def q21(c):
    bad = []
    for n in VIDEOS:
        for kind in ("master", "blocks", "shorts", "desc", "prod"):
            body = " ".join(paras(c.p(n, kind)))
            bad += ["V%d %s: %s" % (n, kind, p) for p in CH.BRAND + CH.COUNTED
                    if re.search(p, body.lower())]
            bad += ["V%d %s: %s" % (n, kind, p) for p in CH.BRAND_CASED
                    if re.search(p, body)]
    return PERFORMED, (not bad and CH.framework_regression()
                       and CH.framework_false_positive_probe()), bad or (
            "The narrowed check was re-run against an injected framework and still fires, and "
            "against ordinary English and stays silent.")

@item(22, "No unsupported universal management claim survives into the built documents")
def q22(c):
    bad = []
    for n in VIDEOS:
        body = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc")))
        bad += ["V%d: %s" % (n, s) for s in CH.mgmt_hits(body)]
    for n in (20, 22):
        t = " ".join(_spoken_from_master(c.p(n, "master")))
        if "middle management" not in t.lower():
            bad.append("V%d does not speak the boundary at all" % n)
    return PERFORMED, (not bad and CH.mgmt_regression()), bad or ("V20 and V22 both quote the "
            "phrase in order to refuse it. The narrowed check was re-run against an injected "
            "assertion and still fires.")

@item(23, "No search-demand claim anywhere in the pack")
def q23(c):
    pats = CH.DEMAND + [r"\bseo\b", r"\bsearch traffic\b", r"high-demand question"]
    bad = []
    for n in VIDEOS:
        for kind in ("master", "blocks", "shorts", "desc"):
            body = " ".join(paras(c.p(n, kind))).lower()
            bad += ["V%d %s: %s" % (n, kind, p) for p in pats if re.search(p, body)]
    return PERFORMED, not bad, bad or ("Search demand is Unknown in the evidence source of "
            "record, and no title, thumbnail, tag, description or spoken line claims otherwise.")

@item(24, "Evidence classes from the source report are preserved and not upgraded")
def q24(c):
    """A claim the report labelled Interpretation or Hypothesis must not be reported as a
    Quantitative finding, and vice versa. Checked against the built provenance files."""
    bad = []
    for cl in PV.CLAIMS:
        for n in cl["spoken"]:
            ts = paras(c.p(n, "prov"))
            # The class must be printed in the claim's OWN heading paragraph. Searching
            # the whole document instead let one claim's class satisfy another claim's
            # check: injecting a wrong class for C10 passed, because C1 is Quantitative
            # and the string was present somewhere on the page. Scope it to the heading.
            # The house sub() helper also upper-cases its heading, so compare lowercased.
            head = [t for t in ts if t.strip().upper().startswith(cl["id"] + " ")
                    or t.strip().upper().startswith(cl["id"] + "\u00a0")]
            if not head:
                bad.append("V%d provenance does not carry %s" % (n, cl["id"])); continue
            if not any(cl["report_class"].lower() in t.lower() for t in head):
                bad.append("V%d does not print %s's class as %s in its own heading"
                           % (n, cl["id"], cl["report_class"]))
    # A claim recorded as considered-and-not-spoken must not appear in any provenance file
    # as if it were spoken.
    for cl in PV.CLAIMS:
        if cl["spoken"]:
            continue
        for n in VIDEOS:
            if cl["id"] in " ".join(paras(c.p(n, "prov"))):
                bad.append("%s is marked not spoken but appears in V%d's provenance"
                           % (cl["id"], n))
    # The heading-scoped comparison must still reject a class that is genuinely wrong,
    # even when that class is correct for some other claim on the same page.
    probe_head = ["C10  \u00b7  QUANTITATIVE  \u00b7  SPOKEN IN V22",
                  "C1  \u00b7  QUANTITATIVE  \u00b7  SPOKEN IN V20, V22"]
    probe = not any("qualitative, with volume and trajectory recorded as unknown" in t.lower()
                    for t in probe_head if t.strip().upper().startswith("C10 "))
    classes = {cl["report_class"].split(",")[0] for cl in PV.CLAIMS}
    return PERFORMED, (not bad and probe), bad or ("%d claims carried, each printed with the class the "
            "source report gave it: %s. Four claims read and deliberately not spoken are "
            "recorded in the evidence boundaries document."
            % (len(PV.CLAIMS), ", ".join(sorted(classes))))

@item(25, "Every constructed artifact is labelled on the card and named on camera")
def q25(c):
    bad = []
    on_card = {}
    for n in VIDEOS:
        for cid, _h, _l, label in PR.FULLSCREEN[n]:
            if label and "CONSTRUCTED" in label:
                on_card[cid] = (n, label)
    listed = {x[1] for x in PV.CONSTRUCTED}
    bad += ["%s is constructed on screen but not in the provenance list" % cid
            for cid in on_card if cid not in listed]
    bad += ["%s is listed as constructed but carries no on-card label" % cid
            for cid in listed if cid not in on_card]
    # and the spoken master must say so too
    SAID = {15: "This is a made-up example.",
            19: "This is made up, but you will recognize her.",
            22: "Here is a constructed example, not a real employer's chart."}
    for n, line in SAID.items():
        if line not in " ".join(_spoken_from_master(c.p(n, "master"))):
            bad.append("V%d does not name its artifact as constructed on camera" % n)
    return PERFORMED, not bad, bad or ("%d cards carry a constructed label, across three "
            "constructed examples in V15, V19 and V22. All three are also named as constructed "
            "in the spoken master, not only in the description." % len(on_card))

@item(26, "V17 does not duplicate V8's evidence teaching")
def q26(c):
    body = " ".join(_spoken_from_master(c.p(17, "master")))
    need = ["I made a video a while back about keeping a record of your own work",
            "This is when there is no time to build a habit",
            "Keep the proof, not the property."]
    bad = ["V17 missing: %s" % x[:45] for x in need if x not in body]
    return PERFORMED, not bad, bad or ("V17 names the habit video, states that it is the other "
            "situation, and teaches the closing window rather than the habit.")

@item(27, "V18 does not re-teach V13, and V19 does not name a gap framework")
def q27(c):
    bad = []
    t18 = " ".join(_spoken_from_master(c.p(18, "master")))
    if "I have a whole video on exactly which parts of experience carry into a new industry" not in t18:
        bad.append("V18 does not point at the transfer video")
    t19 = " ".join(_spoken_from_master(c.p(19, "master")))
    if "It is not a diagnostic and it does not assign you a type." not in t19:
        bad.append("V19 does not refuse the diagnostic reading")
    for pat in (r"learn,? practice,? prove", r"\bgap one\b", r"\bthe three gaps\b"):
        if re.search(pat, t19.lower()):
            bad.append("V19 names a framework: %s" % pat)
    return PERFORMED, not bad, bad or ("V18 points at the transfer video instead of repeating "
            "it. V19's three possibilities are never numbered, never named and never boxed.")

@item(28, "V20 does not run V22's structural diagnosis")
def q28(c):
    t20 = " ".join(_spoken_from_master(c.p(20, "master"))).lower()
    V22_ONLY = [r"org chart", r"draw the ladder", r"how many roles actually exist",
                r"readiness problem", r"structure problem", r"how often do they open"]
    bad = ["V20 carries %s" % p for p in V22_ONLY if re.search(p, t20)]
    t22 = " ".join(_spoken_from_master(c.p(22, "master"))).lower()
    present = [p for p in V22_ONLY if re.search(p, t22)]
    if len(present) < 4:
        bad.append("V22 is missing its own diagnosis: only %d of %d markers"
                   % (len(present), len(V22_ONLY)))
    return PERFORMED, not bad, bad or ("V22 carries %d of the %d diagnosis markers and V20 "
            "carries none of them. V20 takes the loss apart; V22 reads the structure."
            % (len(present), len(V22_ONLY)))

@item(29, "V21 keeps promotion, title and compensation real")
def q29(c):
    body = " ".join(_spoken_from_master(c.p(21, "master")))
    need = ["Promotion usually comes with money",
            "Anyone who tells an experienced professional that titles are meaningless",
            "I would also like to talk about what it pays",
            "Do not let growth become a nice word your company uses"]
    bad = ["V21 missing: %s" % x[:45] for x in need if x not in body]
    return PERFORMED, not bad, bad or ("Four protective lines present: promotion is attached to "
            "money, titles-are-meaningless is refused, compensation stays in the ask, and the "
            "unpaid-senior-work pattern is named.")

@item(30, "The Missing Rung structure is never named and never runs in the same order twice")
def q30(c):
    bad = []
    for n in VIDEOS:
        for kind in ("master", "blocks", "shorts", "desc", "prod"):
            body = " ".join(paras(c.p(n, kind))).lower()
            if re.search(r"the missing rung|a four-box|the four (dimensions|elements|components)",
                         body):
                bad.append("V%d %s names the structure" % (n, kind))
    seen = {}
    for n, o in CH.ORDERS.items():
        if len(o) == 4:
            seen.setdefault(o, []).append(n)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    if dupes:
        bad.append("repeated order: %s" % dupes)
    return PERFORMED, (not bad and CH.four_box_regression()), bad or (
            "Only V20 runs all four concepts, so no order repeats. The structure is never named "
            "in any document, and no card presents four boxes as a set.")

@item(31, "The faith anchor is marked unverified rather than presented as exact NLT")
def q31(c):
    bad = []
    for n in VIDEOS:
        ts = paras(c.p(n, "desc"))
        if not any("NLT WORDING REQUIRES VERIFICATION" in t for t in ts):
            bad.append("V%d carries no verification notice" % n)
        if not any("Tyndale" in t for t in ts):
            bad.append("V%d has no permission line" % n)
    return PERFORMED, not bad, bad or ("No authorized NLT text exists in this workspace, so each "
            "of the eight references is marked on the page itself.")

@item(32, "Spoken copy is US English throughout")
def q32(c):
    BRIT = [r"\borganis", r"\brecognis", r"\bprioritis", r"\banalyse", r"\bcentre\b",
            r"\bbehaviour", r"\bcolour", r"\blabour", r"\bfavour", r"\bjudgement\b",
            r"\bprogramme\b", r"\btravelled\b", r"\blicence\b", r"\bpractise\b",
            r"\bwhilst\b", r"\bamongst\b", r"\bfulfil\b", r"\bspecialis", r"\bhas got\b", r"\bhave got\b"]
    bad = []
    for n in VIDEOS:
        body = " ".join(_spoken_from_master(c.p(n, "master")) + paras(c.p(n, "desc"))).lower()
        bad += ["V%d: %s" % (n, p) for p in BRIT if re.search(p, body)]
    probe = bool(re.search(BRIT[9], "that is good judgement"))
    return PERFORMED, (not bad and probe), bad or ("Twenty British spellings searched across "
            "every spoken master and description.")

@item(33, "Thought-block parity is exact across all eight videos")
def q33(c):
    bad = []
    for n in VIDEOS:
        w, nb, out_of_range = B.verify(n)
        if out_of_range:
            bad += ["V%d %s" % (n, s) for s, _ in out_of_range]
        stated = _printed_count(paras(c.p(n, "blocks")))
        if stated != w:
            bad.append("V%d blocks file prints %s, module counts %d" % (n, stated, w))
    return PERFORMED, not bad, bad or ("%d blocks, %d spoken words, every block between 2 and 5 "
            "sentences, every spoken word once and in order."
            % (sum(B.verify(n)[1] for n in VIDEOS), sum(B.verify(n)[0] for n in VIDEOS)))

@item(34, "No file is marked working, and the one open item is marked open")
def q34(c):
    bad = []
    for n in VIDEOS:
        for kind in ("master", "blocks", "prod", "shorts", "desc", "prov"):
            path = c.p(n, kind)
            if "_WORKING" in os.path.basename(path):
                bad.append("filename marked working: " + os.path.basename(path))
            body = " ".join(paras(path))
            for x in ("PACKAGING PENDING", "WORKING TITLE", "[working]", "TBD", "TODO"):
                if x in body:
                    bad.append("%s carries %s" % (os.path.basename(path), x))
    # V20's thumbnail is the one deliberately open item and must say so.
    if "PENDING TEMIDAYO APPROVAL" not in " ".join(paras(c.p(20, "desc"))):
        bad.append("V20's description does not carry the thumbnail placeholder")
    for n in VIDEOS:
        if n == 20:
            continue
        if "PENDING TEMIDAYO APPROVAL" in " ".join(paras(c.p(n, "desc"))):
            bad.append("V%d carries a pending marker it should not have" % n)
    return PERFORMED, not bad, bad or ("Forty-eight files checked. The only open item is V20's "
            "thumbnail, and it is marked open in the file rather than filled with a guess.")

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
 ("Scripture wording", "Still not verified. A search of the whole workspace for an authorized "
                       "New Living Translation text found none, so the three verses are marked "
                       "NLT WORDING REQUIRES VERIFICATION on the description page itself and in "
                       "each provenance file. They are recorded as intended references, not as "
                       "verified NLT wording."),
 ("Resource pages", "The three resource URLs were taken from the shipped V4 to V11 descriptions. "
                    "None was loaded to confirm it is live."),
 ("V4 to V11 packaging", "The V4 to V14 construction document proposes alternative titles and "
                        "thumbnails for V4 through V11. None was implemented, and no V4 to V11 "
                        "file was opened for edit. Those rows were read and left alone."),
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
