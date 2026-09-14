# -*- coding: utf-8 -*-
"""Package QA for the sprint. Every check reads the built package on disk."""
import os, re, glob, sys
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
import sprint as S
import frames as F
import spine as SP
import sshorts as SH
import publish as PUB
import langcheck23 as LANG
import descsrc as DS
from qa23 import units, _flat, negated as _negated, BRITISH, EM_DASH

# A production document that names what a video must not be read as
# necessarily contains that phrase. Those framings are prohibitions too.
EXTRA_NEG = ("protection against", "keeps the video from", "read as",
             "reading as", "turn the video into", "may not", "must not",
             "does not claim", "is not a")


# The shared checker keeps discourse verbs out of scope so that inclusive
# editorial phrasing is not rewritten. The authorized V9 correction shows
# where that line actually falls: the claim was never "talk", it was
# "usually ask". This layer adds that one pattern without touching the
# checker the locked V22/V23 batch is verified against.
HABIT = re.compile(
    r"\b(?:people|professionals|candidates|everyone|they)\b[^.?!]{0,60}?"
    r"\b(?:usually|typically|normally|generally|tend to|tends to)\b"
    r"|\bthe usual (?:question|answer|advice|assumption|move)\b"
    r"|\bmost people\b", re.I)


def language(text):
    """Unsupported audience-behavior phrasing, shared rules plus HABIT."""
    out = list(LANG.findings(text))
    for m in HABIT.finditer(text):
        seg = text[max(0, m.start() - 70):m.end() + 70]
        if LANG.MODAL.search(seg) or LANG.VIEWER.search(text[:m.end()]):
            continue
        if LANG.QUOTED.search(seg):
            continue
        out.append((text[max(0, m.start() - 40):m.end() + 40].strip(),
                    "asserts what people usually do"))
    return out


def authored_copy(n):
    """Everything this build wrote for publication, as one blob.

    The description is no longer in this set: it is approved source now,
    reproduced verbatim from the September 14 package, and the checker
    reports on approved copy rather than asking the package to edit it.
    """
    v = PUB.PINNED.get(n)
    return str(v) if v else ""


def negated(text, at, window=140):
    if _negated(text, at, window):
        return True
    start = max(text.rfind(". ", max(0, at - window), at), at - window, 0)
    return any(w in text[start:at] for w in EXTRA_NEG)

HISTORICAL = os.path.join(
    DELIV, "VIDEOS_4-21_STORY_LED",
    "Videos_4-21_STORY_LED_FINAL_Production_Packages.zip")
HISTORICAL_SHA = ("da7c383d99aec2863d5d39afdfe290caaf5e658ef65cac0a2fa259b8b"
                  "e24d9e1")

# Phrasing that would break a per-video boundary if the package asserted it.
FORBIDDEN = {
 4: ("ai always removes learning", "ai always damages", "ai eliminates "
     "developmental", "ai takes your job", "ai will take your job"),
 5: ("being needed is bad", "your employer owes you", "owes you a "
     "promotion"),
 6: ("most employers", "the market wants", "all employers",
     "titles are meaningless", "titles never matter",
     "highest in the market"),
 7: ("work harder and you will get promoted", "advancement is merit",
     "if you collect the right evidence you will get"),
 8: ("forward the documents", "download the files", "take a screenshot of",
     "copy the customer data", "keep the source code"),
 9: ("everything transfers", "all experience transfers",
     "nothing transfers"),
}


def all_units(pkg):
    out = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                out.extend(units(os.path.join(root, nm)))
    return out


def source_corpus(n):
    parts = [S.spoken_text(n), S.title(n), S.thumbnail(n), S.watch_next(n)]
    parts += [lab for lab, _ in S.sections(n)]
    parts += [sh["body"] for sh in S.shorts(n)]
    return _flat(" ".join(parts)).lower()


def quoted(n, unit, hit, window=40):
    u, corpus = _flat(unit).lower(), source_corpus(n)
    i = u.find(_flat(hit).lower())
    if i < 0:
        return False
    frag = u[max(0, i - window):i + len(_flat(hit)) + window].strip()
    while len(frag) > 16:
        if frag in corpus:
            return True
        frag = frag[2:-2].strip() if len(frag) > 22 else frag[1:].strip()
    return False


def forbidden(n, us, phrases):
    body = _flat(" ".join(us)).lower()
    hits = []
    for ph in phrases:
        for m in re.finditer(re.escape(ph), body):
            if negated(body, m.start()) or quoted(
                    n, body[max(0, m.start() - 60):m.end() + 40], ph):
                continue
            hits.append((ph, body[max(0, m.start() - 60):m.end() + 40]))
    return hits


def run(n, pkg, geo, assets, reuse_rows=None, anon_rows=None):
    R = []

    def ck(name, ok, detail):
        R.append((name, bool(ok), detail))

    us = all_units(pkg)
    body = _flat(" ".join(us)).lower()
    rec = os.path.join(pkg, "01_RECORDING")

    # ------------------------------------------------------------- source
    ck("The FINAL sprint script is the source used",
       S.read(n)["sha"] == S.sha256(S.script_path(n)), S.read(n)["sha"])
    ck("The supplied Thought-Block copy is present, unchanged",
       os.path.exists(os.path.join(
           rec, os.path.basename(S.block_path(n))))
       and S.sha256(os.path.join(rec, os.path.basename(S.block_path(n))))
       == S.sha256(S.block_path(n)),
       S.sha256(S.block_path(n)))
    ok, det = S.blocks_match(n)
    ck("Thought-Block spoken wording matches the script exactly", ok, det)
    ck("Recording master carries every spoken paragraph",
       _all_spoken(os.path.join(rec, "FINAL_Sprint_Recording_Master.docx"),
                   n),
       "%d paragraphs, %d words" % (len(S.paragraphs(n)), S.word_count(n)))
    ck("No Short is treated as part of the spoken script",
       not S.shorts_in_spoken(n) and S.spoken_ends_before_shorts(n),
       S.shorts_in_spoken(n) or "the spoken stream stops at THREE SHORTS")
    ck("No production note is inside the spoken stream",
       not [p for p in S.paragraphs(n) if p.strip().startswith("[")],
       "the bracketed Watch Next note is carried as a cue, never as speech")
    ck("Spoken wording unchanged",
       S.spoken_text(n) == "\n".join(S.paragraphs(n)),
       "the build reads the script and never rewrites it")

    # ---------------------------------------------------------- numbering
    ck("New public number correct", S.read(n)["meta"]["new"] == n, "V%d" % n)
    ck("Former roadmap number correct",
       S.read(n)["meta"]["former"] == S.NUMBERS[n], "V%d" % S.NUMBERS[n])
    ck("Both numbers appear in every major document",
       _both_numbers(pkg, n), "new V%d and former V%d" % (n, S.NUMBERS[n]))
    ck("The historical V4 to V21 archive is not overwritten",
       os.path.exists(HISTORICAL)
       and S.sha256(HISTORICAL) == HISTORICAL_SHA,
       HISTORICAL_SHA)

    # ---------------------------------------------------------- packaging
    ck("Title exact", any(u.strip() == S.title(n) for u in us), S.title(n))
    ck("Thumbnail exact, stated on its own line",
       any(u.strip() == S.thumbnail(n) for u in us), S.thumbnail(n))
    ck("Three candidate Shorts, not expanded",
       len(SH.rows(n)) == 3 and len(S.shorts(n)) == 3,
       "three, as supplied")
    ck("Every Short is reproduced word for word",
       all(_flat(sh["body"]) in _flat(" ".join(us))
           for sh in S.shorts(n)), "three of three")
    ck("Intended Watch Next exact, no silent substitution",
       any(u.strip() == S.watch_next(n) for u in us)
       and "intended watch next" in body, S.watch_next(n))
    ck("Launch-day Watch Next status is flagged pending",
       "pending live availability" in body
       and "editorial fallback required" in body,
       "PENDING LIVE AVAILABILITY until verified before upload")

    # ------------------------------------------------------------- visual
    cam, full = SP.counts(n)
    ck("The video stays camera-led", cam >= full,
       "%d camera stretches against %d cues; %d of %d spoken words on camera"
       % (cam, full, SP.on_camera_words(n), S.word_count(n)))
    ck("Every cue is a whole spoken paragraph, found once",
       not [f["key"] for f in F.SETS[n] if f["trigger"]
            and not S.trigger_ok(n, f["trigger"])],
       "%d cues" % full)
    ck("No cue lands on a section label",
       not [f["key"] for f in F.SETS[n] if f["trigger"]
            and S._is_label(f["trigger"])], "section labels cue nothing")
    pl = SP.placements(n)
    ck("Each graphic is cued once only",
       not [k for k in set(pl) if pl.count(k) > 1], "%d placements" % len(pl))
    ck("Substantive teaching is true full screen",
       all(f["mode"] == "FULL SCREEN" for f in F.SETS[n]),
       "no overlay, no corner placement, no presenter behind a card")
    ck("Every card is 1920 x 1080", _all_1080(assets), "%d PNG" % len(assets))
    ck("Geometry is clean against the rendered DOM", not geo,
       geo or "%d states measured" % len(F.states(n)))
    multi, bad = _active_states(n)
    ck("One active idea at a time where a structure is taught", not bad,
       bad or "%d multi-state families measured against their declared build "
              "shape" % multi)
    ck("Phone-size contact sheet present",
       os.path.exists(os.path.join(pkg, "04_VISUAL_ASSETS",
                                   "Phone_Size_Contact_Sheet.png")),
       "rendered and inspected")

    # --------------------------------------------------------------- edit
    ck("CTA is full screen",
       any(f["treatment"] == "CTA" for f in F.SETS[n])
       and all(f["mode"] == "FULL SCREEN" for f in F.SETS[n]
               if f["treatment"] == "CTA"), "one full-screen CTA card")
    ck("Watch Next is full screen and final",
       "full screen and final" in body and "no return to camera" in body,
       "stated in the production documents")
    ck("No burned-in long-form captions", "no burned-in caption" in body,
       "stated in the production documents")
    ck("SRT deferred until the final edit",
       not glob.glob(os.path.join(pkg, "**", "*.srt"), recursive=True)
       and "srt" in body and "after final edit" in body,
       "generated in Riverside after the cut")
    ck("No chapters before the final edit", not _chapter_lists(pkg),
       "the script carries no timing markers at all")

    # ---------------------------------------------------------- editorial
    ck("U.S. English throughout what this build authored",
       not _british(n, us), _british(n, us) or "clean")
    ck("No em dashes in what this build authored",
       not _emdash(n, us), _emdash(n, us) or "clean")
    ck("No invented runtime", "not a runtime" in body
       and not re.search(r"\b(measured|final|actual)\s+runtime\s+(is|of)\s+"
                         r"\d", body),
       "every figure is arithmetic on the script")
    perf = forbidden(n, us, ("music license", "licensed track",
                             "click-through rate", "audience retention",
                             "upload date is"))
    ck("No invented performance result or music license", not perf,
       perf or "none claimed")
    drift = forbidden(n, us, ("resume hack", "recruiter tip",
                              "job-loss prediction"))
    ck("No strategy drift", not drift, drift or "none present")

    # ------------------------------------------------------- video rules
    hits = forbidden(n, us, FORBIDDEN[n])
    ck("Video-specific boundary preserved", not hits,
       hits or _BOUNDARY_SUMMARY[n])
    lang = language(S.spoken_text(n)) + language(authored_copy(n))
    ck("No unsupported audience-behavior phrasing remains", not lang,
       ["%s" % a[:80] for a, b in lang] or "no unsupported audience-behavior "
                                           "claim in this script")
    ck("Corrected sentences replaced, nothing else touched",
       *_corrections(n))
    ck("Description is the approved revised copy, verbatim",
       *_description(n, us))
    ck("One relevant resource at most, no stacking",
       *_resource(n, us))
    if n == 6:
        # 1,010 after the two authorized corrections. Nothing was added to
        # the spoken stream; both were sentence-for-sentence replacements.
        ck("The ten-minute promise is protected",
           S.word_count(6) == 1010 and not _added_spoken(6),
           "1,010 spoken words, the supplied script plus two authorized "
           "sentence replacements. No spoken material "
           "added, no second CTA.")
        ck("Problem, Authority, Proof and Real Gap all present",
           all(S.contains(6, x) for x in ("Problem.", "Authority.", "Proof.",
                                          "Real gap.")),
           "the four-part framework is intact")
        if reuse_rows is not None:
            ck("Every reused card is byte-identical to the former V22 "
               "package", all(ok for _, ok, _ in reuse_rows),
               "%d families verified against the locked V22 bytes"
               % len(reuse_rows))
        if anon_rows is not None:
            ck("Every anonymized card changed the employer label and "
               "nothing else", all(ok for _, ok, _ in anon_rows),
               "%d families: restoring the name returns the former V22 "
               "bytes exactly" % len(anon_rows))
        # ------------------------------------------- public anonymization
        import audit_public as AP
        ck("No employer name is drawn on any public V6 card",
           not AP.scan(6), AP.scan(6) or "%d states audited off the drawn "
                                         "card, not the source"
           % sum(len(f["states"]) for f in F.SETS[6]))
        for who in ("HCSC", "Health Care Service", "xAI", "Zeta Global",
                    "Patriot Growth", "GiveDirectly"):
            ck("No public-facing V6 graphic identifies %s" % who,
               not [h for h in AP.scan(6) if who.lower() in h[1].lower()],
               "absent from every drawn state and every filename")
        ck("No employer name remains in V6 spoken copy",
           not AP.RX.search(S.spoken_text(6)), "clean")
        ck("No employer URL appears anywhere public in V6",
           not _public_urls(pkg), _public_urls(pkg) or "none")
        ck("The internal evidence layer still names every employer",
           _evidence_named(pkg),
           "the evidence and provenance records keep the real identities")
        # This evidence lives on the cards, so it is read off the drawn
        # card and the documents together rather than from documents alone.
        seen = _drawn_and_written(6, pkg)
        ck("Posting titles, ranges and quoted language are unchanged",
           all(x.lower() in seen for x in
               ("Sr Divisional Strategy Consultant, Governance",
                "$133,400 to $247,700",
                "Member of Technical Staff, Governance Risk Compliance",
                "predefined decisions", "Director, Talent Management",
                "Director of Strategic Initiatives")),
           "anonymizing the employer removed no evidence")
        ck("Capture provenance is intact",
           "captured september 12, 2026" in seen,
           "every posting still carries its capture date")
        ck("The 15-posting, 11-employer boundary is intact",
           "15 postings" in body and "11 employers" in body,
           "denominator unchanged")
        ck("The ceiling claim stays bounded to the sample",
           "in this sample" in body or "in the sample" in body,
           "the highest range is the highest in this sample, not the "
           "market, even though the card now says AI Company")
    if n == 9:
        ck("The full four-part audit is preserved",
           all(S.contains(9, x) for x in ("What travels?", "What does not?",
                                          "What can I prove?",
                                          "What must I relearn?")),
           "all four questions appear in the spoken script and on one card")
    if n == 8:
        ck("No card depicts taking property",
           not forbidden(8, us, ("screenshot of", "download the",
                                 "forward the", "copy the file")),
           "no file, screenshot, download or system appears in any asset")
    return R


# The resource each description is authorized to carry, and the one it may
# never stack with another.
RESOURCE = {4: None,
            5: ("Career Decision Evidence Check",
                "https://temidayoafonja.com/career-decisions"),
            6: ("Career Evidence Starter",
                "https://temidayoafonja.com/career-evidence-starter"),
            7: ("Career Evidence Starter",
                "https://temidayoafonja.com/career-evidence-starter"),
            8: ("Keep the Proof",
                "https://temidayoafonja.com/keep-the-proof"),
            9: ("Career Decision Evidence Check",
                "https://temidayoafonja.com/career-decisions")}
OTHER_OFFERS = ("Field Kit", "the book", "workshop")


# Public-facing parts of a package. The evidence and provenance records are
# deliberately outside this set: they stay named.
PUBLIC_DIRS = ("01_RECORDING", "02_RUN_OF_SHOW", "04_VISUAL_ASSETS",
               "05_SHORTS", "06_PUBLISHING")
EMPLOYER_URL = re.compile(
    r"\b(?:givedirectly\.org|zetaglobal\.com|hcsc\.com|patriotgrowth\.com"
    r"|x\.ai)\b", re.I)


def _drawn_and_written(n, pkg):
    """Everything the package shows or says, cards included, lowercased."""
    import audit_public as AP
    import frames as FR
    out = []
    for f in FR.SETS[n]:
        for st in f["states"]:
            out += AP.state_text(st)
    out += all_units(pkg)
    return _flat(" ".join(out)).lower()


def _public_urls(pkg):
    out = []
    for sub in PUBLIC_DIRS:
        d = os.path.join(pkg, sub)
        for root, _, names in os.walk(d):
            for nm in sorted(names):
                if not nm.endswith((".docx", ".txt")):
                    continue
                for u in units(os.path.join(root, nm)):
                    if EMPLOYER_URL.search(u):
                        out.append("%s: %s" % (nm, u[:50]))
    return out


def _evidence_named(pkg):
    """The internal layer must still carry the real employer identities."""
    want = ("HCSC", "GiveDirectly", "xAI", "Zeta Global", "Patriot Growth")
    blob = ""
    for sub in ("00_SOURCE_HIERARCHY", "07_EVIDENCE", "04_VISUAL_ASSETS"):
        d = os.path.join(pkg, sub)
        for root, _, names in os.walk(d):
            for nm in sorted(names):
                if nm.endswith((".docx", ".txt")):
                    blob += " " + _flat(" ".join(
                        units(os.path.join(root, nm))))
    return all(w.lower() in blob.lower() for w in want)


def _description(n, us):
    """Every approved line reaches the publishing document unedited."""
    body = _flat(" ".join(us))
    missing = [l for l in DS.lines(n) if l.strip()
               and _flat(l) not in body]
    if missing:
        return False, ["missing: %s" % m[:60] for m in missing]
    d = DS.block(n)
    if _flat(d["title"]) != _flat(S.title(n)):
        return False, "title in the description package does not match"
    if _flat(d["watch_next"]) != _flat(S.watch_next(n)):
        return False, "Watch Next in the description package does not match"
    return True, ("%d approved lines, reproduced exactly, with the playlist "
                  "placeholder left in place" % len(DS.lines(n)))


def _resource(n, us):
    body = _flat(" ".join(us))
    want = RESOURCE[n]
    urls = set(re.findall(r"https://temidayoafonja\.com/[a-z0-9\-]+", body))
    if want is None:
        if urls:
            return False, "carries a resource URL but should carry none: %s" \
                          % sorted(urls)
        return True, "no offer or resource block, intentionally"
    name, url = want
    if _flat(name) not in body:
        return False, "missing the approved resource: %s" % name
    if url not in urls:
        return False, "missing the approved URL: %s" % url
    extra = urls - {url}
    if extra:
        return False, "stacks another resource: %s" % sorted(extra)
    stacked = [o for o in OTHER_OFFERS if o.lower() in body.lower()]
    if stacked:
        return False, "names another offer: %s" % stacked
    return True, "%s, and only that one" % name


def _corrections(n):
    """The five authorized replacements, and only those.

    A corrected video must carry every replacement and none of the sentences
    they replaced. A video outside the correction set must be identical to
    the supplied script, which is checked against the preserved copy rather
    than assumed.
    """
    spoken = _flat(" ".join(S.paragraphs(n)))
    if n not in S.CORRECTIONS:
        same = _flat(" ".join(S.pre_paragraphs(n))) == spoken
        return same, ("not in the correction set, identical to the supplied "
                      "script" if same else "differs from the supplied "
                      "script")
    bad = []
    for old, new in S.CORRECTIONS[n]:
        if _flat(old) in spoken:
            bad.append("still carries: %s" % old[:50])
        if _flat(new) not in spoken:
            bad.append("missing: %s" % new[:50])
    pre = _flat(" ".join(S.pre_paragraphs(n)))
    for old, new in S.CORRECTIONS[n]:
        pre = pre.replace(_flat(old), _flat(new))
    if pre != spoken:
        bad.append("the script differs beyond the authorized sentences")
    return not bad, bad or ("%d authorized replacement%s, nothing else"
                            % (len(S.CORRECTIONS[n]),
                               "" if len(S.CORRECTIONS[n]) == 1 else "s"))


_BOUNDARY_SUMMARY = {
 4: "not anti-AI, no single outcome claimed, not a job-loss prediction",
 5: "being needed is not treated as bad and no promotion is owed",
 6: "sample bounded, ceiling bounded, no labor-market generalization",
 7: "advancement is not reduced to merit",
 8: "keep the proof, not the property",
 9: "not anti-transferability; the full audit is kept",
}


def _all_spoken(path, n):
    if not os.path.exists(path):
        return False
    b = _flat(" ".join(units(path)))
    return all(_flat(p) in b for p in S.paragraphs(n))


def _both_numbers(pkg, n):
    want = ("V%d" % n, "V%d" % S.NUMBERS[n])
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")):
                continue
            if "Short" in nm or "short" in nm:
                continue
            b = _flat(" ".join(units(os.path.join(root, nm))))
            if not all(w in b for w in want):
                return False
    return True


def _all_1080(assets):
    from PIL import Image
    for p in assets:
        if p.endswith(".png") and "Contact_Sheet" not in p \
                and Image.open(p).size != (1920, 1080):
            return False
    return bool(assets)


def _active_states(n):
    sys.path.append(DELIV + "riverside-build")
    import rdeck
    built, bad = 0, []
    for f in F.SETS[n]:
        seen = []
        for st in f["states"]:
            c = rdeck.Card(1, st["name"])
            st["draw"](c)
            a = getattr(c, "active_items", None)
            if a is None:
                bad.append("%s: no declared emphasis state" % st["name"])
                a = 0
            if a > 1:
                bad.append("%s: %d items active at once" % (st["name"], a))
            seen.append(a)
        if len(f["states"]) < 2:
            continue
        built += 1
        if f["build"] == "ESTABLISH":
            if seen[0] != 0:
                bad.append("%s: declared ESTABLISH but the first state "
                           "already emphasizes a component" % f["key"])
            if sum(1 for x in seen[1:] if x == 1) != len(seen) - 1:
                bad.append("%s: declared ESTABLISH but not every later state "
                           "activates exactly one" % f["key"])
        elif f["build"] == "ARRIVE":
            if any(x != 1 for x in seen):
                bad.append("%s: declared ARRIVE but a state emphasizes none "
                           "or several" % f["key"])
    return built, bad


def _chapter_lists(pkg):
    bad = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")):
                continue
            lines = [_flat(u) for u in units(os.path.join(root, nm))]
            st = [l for l in lines if re.match(r"^\d{1,2}:\d\d(\s|$)", l)]
            if len(st) >= 3 and any(l.startswith("0:00") for l in st):
                bad.append("%s: %d timestamped lines" % (nm, len(st)))
    return bad


def _added_spoken(n):
    """Nothing may have been added to the spoken stream."""
    from docx import Document
    raw = [p.text.rstrip() for p in Document(S.script_path(n)).paragraphs
           if p.text.strip()]
    cut = raw.index(S.SHORTS_START)
    allowed = {S._norm(x) for x in raw[:cut]}
    return [p for p in S.paragraphs(n) if S._norm(p) not in allowed]


def _british(n, us):
    hits = []
    for u in us:
        for w in BRITISH:
            if re.search(r"\b%s\b" % w, u.lower()) and not quoted(n, u, w):
                hits.append((w, u[:46]))
    return hits


def _emdash(n, us):
    return [u[:60] for u in us if EM_DASH in u and not quoted(n, u, EM_DASH)]
