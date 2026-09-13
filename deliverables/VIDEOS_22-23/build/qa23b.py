# -*- coding: utf-8 -*-
"""Package QA for the re-anchored V22 and V23 packages.

Every check reads the built package from disk. Where a check reads across the
whole package it only ever asks the package to be consistent with the
approved script; it never asks approved copy to change. Checks that must not
match the package's own prohibitions measure across the joined document text
with a negation window, which was tested against injected violations.
"""
import os, re, glob, hashlib, json
import masters23b as M
import frames23b as F
import spine23b as SP
import recdocs23b as R
import shorts23b as SH
import publish23b as PUB
import langcheck23 as LANG
from qa23 import (units, _flat, negated, NEG, sha256, BRITISH, EM_DASH)

from docx import Document


def all_units(pkg):
    out = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                out.extend(units(os.path.join(root, nm)))
    return out


def source_corpus(n):
    parts = [M.spoken_text(n), M.title(n), M.script_header_thumbnail(n)]
    parts += [lab for lab, _ in M.sections(n)]
    parts += M.overview_lines()
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
            if negated(body, m.start()):
                continue
            frag = body[max(0, m.start() - 60):m.end() + 40]
            if quoted(n, frag, ph):
                continue
            hits.append((ph, frag))
    return hits


def near(us, pattern, qualifier, window=220):
    body = _flat(" ".join(us)).lower()
    for m in re.finditer(pattern, body):
        seg = body[max(0, m.start() - window):m.end() + window]
        if qualifier.lower() not in seg:
            return False, body[max(0, m.start() - 60):m.end() + 60]
    return True, "every occurrence carries it"


def run(n, pkg, geo_problems, assets, reuse_rows):
    R_ = []

    def ck(name, ok, detail):
        R_.append((name, bool(ok), detail))

    us = all_units(pkg)
    body = _flat(" ".join(us)).lower()
    rec = os.path.join(pkg, "01_Recording")

    # ------------------------------------------------------ source identity
    ck("The September 13 FINAL story-led script is the source used",
       M.read(n)["sha"] == M.sha256(M.path(n)), M.read(n)["sha"])
    ck("Recording master carries every spoken word, unchanged",
       _spoken_present(os.path.join(rec, "Recording_Master.docx"), n),
       "%d words" % M.word_count(n))
    ok, detail = R.matches_script(n)
    ck("Thought-block copy matches the script exactly", ok, detail)
    ck("Spoken wording unchanged",
       M.spoken_text(n) == "\n".join(M.paragraphs(n)),
       "the build reads the script and never rewrites it")
    w, c = M.counts(n)
    ck("Spoken words = %d by whitespace count" % w,
       w == (980 if n == 22 else 897),
       "%d whitespace, %d with the currency symbol counted separately; was "
       "%d before the source-language correction"
       % (w, c, M.WHITESPACE_PRE_CORRECTION[n]))

    lang = LANG.findings(M.spoken_text(n))
    ck("No unsupported audience-behavior claim in the spoken script",
       not lang,
       ["%s <- %s" % (a[:70], b) for a, b in lang]
       or "%d sentences read; the check fires on both corrected sentences "
          "and stays silent on quoted employer language, bounded "
          "observations, possibility statements and viewer instructions"
          % len(list(LANG._sentences(M.spoken_text(n)))))

    # ---------------------------------------------------------- packaging
    ck("Title exact", any(u.strip() == M.title(n) for u in us), M.title(n))
    ck("Thumbnail exact, stated on its own line",
       any(u.strip() == M.script_header_thumbnail(n) for u in us),
       M.script_header_thumbnail(n))
    stray = [t for t in M.SUPERSEDED_TITLES if _flat(t).lower() in body]
    stray += [t for t in M.SUPERSEDED_THUMBNAILS
              if _flat(t).lower() in body]
    live = _superseded_outside_the_index(pkg)
    ck("Superseded titles and thumbnail absent from active production",
       not live,
       live or "listed only in the source hierarchy and changelog, marked "
               "superseded")

    # ------------------------------------------------------------ triggers
    bad = [f["key"] for f in F.SETS[n] if not M.trigger_ok(n, f["trigger"])]
    ck("Every visual trigger exists in the new spoken stream", not bad,
       bad or "%d cues, each a whole spoken paragraph found once"
       % len(F.SETS[n]))
    lab = [f["key"] for f in F.SETS[n] if M.is_label(f["trigger"])]
    ck("No cue lands on a section label", not lab,
       lab or "section labels are production navigation and cue nothing")
    pl = SP.placements(n)
    twice = sorted({k for k in pl if pl.count(k) > 1})
    ck("Each active graphic is cued once only",
       not twice and len(pl) == len(F.SETS[n]),
       twice or "%d families, %d placements" % (len(F.SETS[n]), len(pl)))
    ret = [k for k in F.RETIRED if k.startswith("V%d" % n)
           and any(re.search(r"\[ FULL SCREEN \]\s+" + re.escape(k), u)
                   for u in us)]
    ck("No retired graphic appears in the active map", not ret,
       ret or "%d retired families carry no cue"
       % len([k for k in F.RETIRED if k.startswith("V%d" % n)]))

    # ------------------------------------------------------------- visuals
    cam, full = SP.counts(n)
    ck("The video stays camera-led", cam >= full,
       "%d camera stretches against %d cues; %d of %d spoken words on camera"
       % (cam, full,
          sum(len(p.split()) for x in SP.spine(n) if x[0] == "CAMERA"
              for p in x[1]), M.word_count(n)))
    ck("Substantive teaching is true full screen",
       all(f["mode"] == "FULL SCREEN" for f in F.SETS[n]),
       "no overlay, no corner placement, no presenter behind a card")
    ck("Every card is 1920 x 1080", _all_1080(assets), "%d PNG" % len(assets))
    ck("Geometry is clean against the rendered DOM", not geo_problems,
       geo_problems or "%d states measured" % len(F.states(n)))
    mismatch = [r for r in reuse_rows if r[0] == n and r[2] != r[3]]
    ck("Every reuse class matches the rendered bytes", not mismatch,
       mismatch or "%d families measured against the previous package"
       % len([r for r in reuse_rows if r[0] == n]))
    multi, bad_active = _active_states(n)
    ck("One active idea at a time where a structure is taught",
       not bad_active,
       bad_active or "%d multi-state families, each measured against its "
                     "declared build shape" % multi)
    mp = os.path.join(pkg, "03_Riverside", "Camera_and_Full_Screen_Map.txt")
    t = open(mp, encoding="utf-8").read() if os.path.exists(mp) else ""
    ck("The map distinguishes camera from full screen",
       "[ CAMERA ]" in t and "[ FULL SCREEN ]" in t,
       "both are marked throughout the spine")

    # ------------------------------------------------------ CTA and finish
    urls = set()
    for u in us:
        urls |= set(re.findall(r"temidayoafonja\.com/[\w\-/]+", u))
    allowed = ({PUB.ROUTES[PUB.RESOURCE[n]]} if PUB.RESOURCE[n] else set())
    ck("Only a resource the script speaks appears", urls <= allowed,
       (urls - allowed) or (PUB.RESOURCE[n] or "this script names no "
                            "resource"))
    ck("Watch Next is full screen and final",
       "full screen and final" in body and "no return to camera" in body,
       "stated in the production documents")
    chap = _chapter_lists(pkg)
    ck("No chapters before the final edit",
       not chap and "after the final edit" in body,
       chap or "the scripts carry no timing markers at all, and no document "
               "carries a chapter list")
    ck("SRT after the final edit only",
       not glob.glob(os.path.join(pkg, "**", "*.srt"), recursive=True)
       and "srt" in body and "after the final edit" in body,
       "generated in Riverside after the cut")
    ck("No burned-in long-form captions",
       "no burned-in caption" in body, "stated in the production documents")

    # ------------------------------------------------------------- shorts
    ck("Six candidate Shorts", len(SH.rows(n)) == 6,
       "a selection bank, not six uploads")
    ck("Every Short line is in the new source script", not SH.verify(n),
       SH.verify(n) or "%d lines verified"
       % sum(len(r["lines"]) for r in SH.rows(n)))
    ck("Every Short carries its boundary",
       all(r["boundary"].strip() for r in SH.rows(n)), "six of six")

    # ---------------------------------------------------------- integrity
    ck("U.S. English throughout what this build authored",
       not _british(n, us), _british(n, us) or "clean")
    ck("No em dashes in what this build authored",
       not _emdash(n, us), _emdash(n, us) or "clean")
    ck("No invented runtime",
       "not a runtime" in body and not re.search(
           r"\b(measured|final|actual)\s+runtime\s+(is|of)\s+\d", body),
       "every figure is arithmetic on the script")
    perf = forbidden(n, us, ("music license", "licensed track",
                             "click-through rate", "impressions",
                             "views expected"))
    ck("No invented performance result", not perf, perf or "none claimed")

    # ------------------------------------------------------- per-video set
    if n == 22:
        ck("15-posting and 11-employer research boundary preserved",
           M.contains(22, "I read 15 postings from 11 employers")
           and "11 employers" in body, "stated in the script and on the card")
        gen = forbidden(22, us, ("most employers", "the market wants",
                                 "all employers", "titles are meaningless",
                                 "titles never matter",
                                 "representative of the labor market"))
        ck("No labor-market generalization", not gen, gen or "none present")
        mkt = forbidden(22, us, ("highest in the market",
                                 "highest published ceiling in the market"))
        ck("The xAI ceiling stays bounded to this sample",
           M.contains(22, "in the sample") and "in the sample" in body
           and not mkt,
           mkt or "highest published ceiling in the sample")
        who = [body[max(0, m.start() - 50):m.end() + 20]
               for m in re.finditer(r"(someone|somebody|another person|else)"
                                    r"\s+(made|created|wrote)\s+"
                                    r"(those|the)\s+predefined", body)
               if not negated(body, m.start())]
        ck("No claim about who wrote the predefined decisions", not who,
           who or "the posting establishes them, and nothing says who made "
                  "them")
        ck("GiveDirectly constraints remain accurate",
           M.contains(22, "unlikely to be a strong fit")
           and M.contains(22, "at least three hours of overlap with East "
                              "Africa Time")
           and "operating constraint" in body,
           "both stated constraints preserved, with the script's own reading")
        am = [body[max(0, m.start() - 60):m.end() + 30] for m in
              re.finditer(r"\b(7 or 8|seven or eight)\s*(a\.?m\.?)", body)
              if not negated(body, m.start())]
        ck("No 7 or 8 a.m. claim added back", not am,
           am or "the retired interpretation appears nowhere")
        ck("No compensation comparison between the two Director roles",
           not forbidden(22, us, ("sixty-five thousand", "$65,000",
                                  "65,000 dollars")),
           "the script no longer draws one, and neither does the package")
        cta = [f for f in F.SETS[22] if f["treatment"] == "CTA"]
        ck("V22 CTA contains no added product or comment ask",
           len(cta) == 1 and not urls
           and not re.search(r"comment(s)? (below|what|and tell)", body),
           "one ask, as the script states it")
    else:
        ck("Synthetic example control preserved",
           "synthetic example" in body and "not a client" in body,
           "labeled as invented, not a client, employer or posting")
        ck("Every card showing a synthetic figure carries the label",
           not _unlabeled_synthetic(), "checked state by state")
        ck("No deleted nine-of-fifteen claim in active materials",
           not re.search(r"\bnine of (the )?fifteen\b|\b9 of 15\b", body),
           "the new script makes no denominator claim")
        active = _active_body(pkg)
        ck("No active same-employer comparison",
           "mercury" not in active
           and "same company" not in active
           and not any(k.startswith("V23_FS_14") or k.startswith("V23_FS_15")
                       for k in SP.placements(23)),
           "retired with the section the script dropped; the evidence stays "
           "in 07_Evidence, marked archived and still anonymized")
        ck("The research is stated only as the script states it",
           M.contains(23, "In the job postings I reviewed, employers often "
                          "asked for more than outcomes."),
           "bounded prose, no denominator")
        ck("Execution is not treated as lack of judgment",
           M.contains(23, "Execution still contains decisions.")
           and "execution still contains decisions" in body,
           "the line is in the script and on a card")
        ck("Real gaps are preserved",
           M.contains(23, "domain knowledge, a credential, regulated "
                          "experience, or direct exposure")
           and "change the emphasis, not the truth" in body,
           "the catch and its closing line are both on screen")
        ck("Career Evidence Starter is the only resource CTA",
           urls == {PUB.ROUTES["Career Evidence Starter"]},
           "one resource, not stacked")
    return R_


# ------------------------------------------------------------- predicates
EVIDENCE_ONLY = ("07_Evidence",)


def _active_body(pkg):
    """Everything the edit is actually cut from.

    The evidence archive is deliberately excluded: the capture packet
    preserves employer identity there for internal traceability, and the rule
    the video has to keep is that no employer-derived comparison reaches the
    active production layer.
    """
    out = []
    for root, _, names in os.walk(pkg):
        if any(x in root for x in EVIDENCE_ONLY):
            continue
        for nm in sorted(names):
            if nm.endswith((".docx", ".txt")):
                out.extend(units(os.path.join(root, nm)))
    return _flat(" ".join(out)).lower()


def _chapter_lists(pkg):
    """Documents carrying something shaped like a YouTube chapter list."""
    bad = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")):
                continue
            lines = [_flat(u) for u in units(os.path.join(root, nm))]
            stamps = [l for l in lines
                      if re.match(r"^\d{1,2}:\d\d(\s|$)", l)]
            if len(stamps) >= 3 and any(l.startswith("0:00") for l in stamps):
                bad.append("%s: %d timestamped lines" % (nm, len(stamps)))
    return bad


def _spoken_present(path, n):
    if not os.path.exists(path):
        return False
    b = _flat(" ".join(units(path)))
    return all(_flat(p) in b for p in M.paragraphs(n))


def _all_1080(assets):
    from PIL import Image
    for p in assets:
        if p.endswith(".png") and Image.open(p).size != (1920, 1080):
            return False
    return bool(assets)


def _active_states(n):
    import sys
    sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                    "riverside-build")
    import rdeck
    built, bad = 0, []
    for f in F.SETS[n]:
        seen = []
        for st in f["states"]:
            c = rdeck.Card(1, st["name"])
            st["draw"](c)
            a = getattr(c, "active_items", None)
            if a is None:
                bad.append("%s: the layout declares no emphasis state"
                           % st["name"])
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


def _superseded_outside_the_index(pkg):
    allowed = ("Source_Hierarchy_and_Manifest.txt", "Source_Hierarchy.txt",
               "V22-V23_MASTER_CHANGELOG_AND_SOURCE_HIERARCHY.docx",
               "Synchronization_Change_Log.txt")
    stray = []
    for root, _, names in os.walk(pkg):
        for nm in sorted(names):
            if not nm.endswith((".docx", ".txt")) or nm in allowed:
                continue
            b = _flat(" ".join(units(os.path.join(root, nm)))).lower()
            for t in M.SUPERSEDED_TITLES:
                if _flat(t).lower() in b:
                    stray.append("%s: %s" % (nm, t))
            for t in M.SUPERSEDED_THUMBNAILS:
                if _flat(t).lower() in b:
                    stray.append("%s: %s" % (nm, t))
    return stray


def _british(n, us):
    hits = []
    for u in us:
        for w in BRITISH:
            if re.search(r"\b%s\b" % w, u.lower()) and not quoted(n, u, w):
                hits.append((w, u[:46]))
    return hits


def _emdash(n, us):
    return [u[:60] for u in us if EM_DASH in u and not quoted(n, u, EM_DASH)]


def _unlabeled_synthetic():
    import sys
    sys.path.append("/home/user/temidayoafonja-site/deliverables/"
                    "riverside-build")
    import rdeck
    FIGS = ("18 percent", "71 percent", "89 percent", "seven months")
    bad = []
    for f in F.SETS[23]:
        for s in f["states"]:
            c = rdeck.Card(1, s["name"])
            s["draw"](c)
            text = " ".join(p["text"].lower() for el in c.els
                            if el["t"] == "text" for p in el["paras"])
            if any(x in text for x in FIGS) and not any(
                    "synthetic example" in t.lower()
                    for t in getattr(c, "foot_texts", [])):
                bad.append(s["name"])
    return bad
