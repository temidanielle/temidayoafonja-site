# -*- coding: utf-8 -*-
"""Build the V4-V11 early-edit synchronization layer.

This layer synchronizes the edit against the September 16 scripts. It does
not rebuild visual assets: the handoff states it supplements existing
production assets and is not permission for a blanket rebuild, and the
ledger records exactly which assets that decision now leaves outstanding.
"""
import os, sys, re, shutil, zipfile, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DELIV = "/home/user/temidayoafonja-site/deliverables/"
sys.path.append(DELIV + "VIDEOS_22-23/build")
sys.path.append(DELIV + "riverside-build")

import src916 as S
import briefs as B
import ledger as LG
from docs23 import (base_doc, title_block, h, kv, para, callout, sub,
                    caption, table, bullets, footer_note, page_break, mono,
                    hr, head)

EYEBROW = "capability formation | v4 to v11 edit sync"
ZIP_DT = (2026, 9, 16, 0, 0, 0)
ARCHIVE = "YouTube_V4-V11_EARLY_EDIT_SYNC_2026-09-16.zip"


def stamp():
    return subprocess.check_output(
        ["env", "TZ=America/Chicago", "date",
         "+%A, %B %d, %Y | %-I:%M %p CT"]).decode().strip()


def sha256(p):
    h_ = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h_.update(b)
    return h_.hexdigest()


def _wrap(t, w=68):
    out, line = [], ""
    for word in str(t).split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out or [""]


def locate(n, trigger):
    """Resolve a trigger to section plus parent passage.

    The handoff asks for repeats to be resolved by section and parent
    passage rather than by first match, so every hit is reported and the
    editor is told which one the brief means.
    """
    return B.occurrences(n, trigger)


def accent_of(beat):
    m = re.search(r"\bS(\d)\b", beat["head"])
    return "S%s" % m.group(1) if m else None


def edit_map(n, path, st):
    b = B.read(n)
    lo = S.word_count(n) / 145.0 * 60
    hi = S.word_count(n) / 130.0 * 60
    L = head("NEW PUBLIC V%d  |  EARLY-EDIT SYNCHRONIZATION MAP" % n)
    L += [S.title(n),
          "Thumbnail: %s" % S.thumbnail(n),
          "Generated %s" % st, "",
          "Current source: %s" % S.read(n)["file"],
          "  sha256  %s" % S.read(n)["sha"],
          "%s spoken words. Arithmetic estimate %d:%02d to %d:%02d at 130 "
          "to 145" % (format(S.word_count(n), ","), lo // 60, lo % 60,
                      hi // 60, hi % 60),
          "words per minute. That is arithmetic on the script, not a",
          "runtime: nothing has been recorded, edited or exported.",
          "", "Thought-block parity: %s" % S.blocks_match(n)[1],
          "", hr(), "", "CAMERA-LED IS NOT CAMERA-ONLY", "",
          "  Begin on the first spoken line. No logo, no welcome sequence,",
          "  no dead-air title card. Editorial opening text and a useful",
          "  cutaway may arrive in the first few seconds; there is no",
          "  required window of talking head before the first cutaway.",
          "  Her voice continues under a full-screen image. No moving",
          "  talking head behind a substantive card.",
          "", hr(), "", "THE VIEWER'S REASON TO WATCH", ""]
    for k in ("OUTCOME", "CURIOSITY", "WHY THIS METHOD",
              "OBSERVABLE TAKEAWAY"):
        if k in b["outcome"]:
            L += ["  %s" % k]
            L += ["      %s" % x for x in _wrap(b["outcome"][k])]
            L.append("")
    L += [hr(), "", "OPENING TREATMENT  |  FIRST SPOKEN BEATS", ""]
    for x in [y for y in b["beats"] if y["phase"] == "opening"]:
        L += _beat(n, x)
    L += [hr(), "", "MAKE THE TEACHING USABLE", ""]
    for x in [y for y in b["beats"] if y["phase"] == "teaching"]:
        L += _beat(n, x)
    L += [hr(), "", "SOUND PLAN  |  FIVE ACCENTS", "",
          "  A stinger means sound. A visual accent and a cutaway are",
          "  separate choices and are not implied by an accent.",
          "  Audition every cue under the actual voice. No alarms, no loud",
          "  whooshes, no compulsory bed, no accent on every bullet, and no",
          "  second effect where one already carries the moment.", ""]
    seen = []
    for x in b["beats"]:
        a = accent_of(x)
        if a:
            seen.append(a)
            L += ["  %s  on: %s" % (a, _clip(x["trigger"], 58))]
    missing = [s for s in ("S1", "S2", "S3", "S4", "S5") if s not in seen]
    if missing:
        L += ["", "  Accents carried in the brief prose rather than on a",
              "  numbered beat: %s. Place them on the passage the brief"
              % ", ".join(missing),
              "  names; do not invent a new placement."]
    L += ["", hr(), "", "CAMERA EMPHASIS  |  FOUR BEATS", "",
          "  Gentle push-ins or a return to the base frame. Keep natural",
          "  pauses. Do not cut on every thought-block boundary and do not",
          "  remove sentences to manufacture pace.", ""]
    for c in b["camera"]:
        L += ["  %s" % x for x in _wrap(c, 66)]
        L.append("")
    if b["boundary"]:
        L += [hr(), "", "PUBLIC BOUNDARY TO PRESERVE", ""]
        L += ["  %s" % x for x in _wrap(b["boundary"], 66)]
        L.append("")
    L += [hr(), "", "WATCH NEXT  |  FULL SCREEN FROM THE START, AND FINAL",
          ""]
    if b["watch_next"]:
        L += ["  EXACT PASSAGE:"]
        L += ["      %s" % x for x in _wrap(b["watch_next"], 62)]
        hits = locate(n, b["watch_next"][:60])
        L += ["", "  Found in section %s." % (hits[0][1] if hits
                                              else "the closing passage")]
    L += ["",
          "  Switch to true full screen from the start of that passage.",
          "  The Watch Next graphic is the last frame. Never return to",
          "  camera after it.",
          "  Verify the destination is publicly live before upload. If it",
          "  is not, flag it. Do not invent or silently change a link.",
          "", hr(), "", "AFTER THE EDIT", "",
          "  SRT and chapters are generated from the finished export and",
          "  are deliberately absent here. No runtime, retention, audio mix",
          "  or footage QA is claimed by this document.", ""]
    return mono(path, L)


def _clip(s, n=58):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n].rstrip() + "..."


def _beat(n, x):
    L = ["  %d. %s" % (x["n"], x["head"])]
    if x["display"]:
        L += ["     DISPLAY COPY:"]
        L += ["         %s" % y for y in _wrap(x["display"], 60)]
    if x["trigger"]:
        L += ["     EXACT SPOKEN TRIGGER:"]
        L += ["         %s" % y for y in _wrap(x["trigger"], 60)]
        hits = locate(n, x["trigger"])
        if len(hits) == 1:
            li, lab, pi, p = hits[0]
            L += ["     FOUND: section %d, %s, spoken paragraph %d"
                  % (li + 1, lab, pi + 1)]
        elif len(hits) > 1:
            L += ["     FOUND IN %d PLACES. Resolve by section and parent "
                  "passage:" % len(hits)]
            for li, lab, pi, p in hits:
                L += ["         section %d, %s, paragraph %d: %s"
                      % (li + 1, lab, pi + 1, _clip(p, 46))]
        else:
            L += ["     NOT FOUND IN THE CURRENT SCRIPT. Do not cue this."]
    note = [y for y in x["note"] if y not in (x["trigger"], x["display"])]
    if note:
        L += ["     DIRECTION:"]
        for y in note:
            L += ["         %s" % z for z in _wrap(y, 60)]
    L.append("")
    return L


def video_ledger(n, path, st, rows):
    d = base_doc()
    title_block(d, EYEBROW, S.title(n), "Asset ledger")
    kv(d, "New public number", "V%d" % n)
    kv(d, "Current script", S.read(n)["file"])
    kv(d, "Spoken words", format(S.word_count(n), ","))
    kv(d, "Generated", st)
    c = LG.counts(rows)
    kv(d, "Verdicts", "  ".join("%s %d" % (k, c[k]) for k in
                                (LG.REUSE, LG.REANCHOR, LG.COPY, LG.REBUILD)
                                if k in c))
    callout(d, "REUSE means the cue sentence and every word of the teaching "
               "copy still exist in the current script. RE-ANCHOR means the "
               "card is correct and its placement is not. COPY UPDATE and "
               "REBUILD both mean the card has to be redrawn, which this "
               "pass did not do: the handoff supplements existing assets "
               "and is not permission for a blanket rebuild.")
    table(d, ["Family", "Verdict", "Why"],
          [[r["key"], r["verdict"], r["reason"]] for r in rows],
          widths=[2.5, 1.1, 3.1], size=7.5)
    gone = [r for r in rows if r["missing"]]
    if gone:
        h(d, "Teaching lines that no longer appear in the current script")
        table(d, ["Family", "Line"],
              [[r["key"], m] for r in gone for m in r["missing"]],
              widths=[2.3, 4.4], size=7)
        caption(d, "Each of these is drawn on a card today and cannot be "
                   "traced to a sentence in the September 16 script. Under "
                   "the standing rule that every word on a card is the "
                   "script's own, each one has to be replaced from the "
                   "current script before that card can be used.")
    footer_note(d, "The editorial label tier, the small all-capitals "
                   "headings and column labels, is judged separately: it "
                   "was never required to be verbatim speech and the "
                   "September 16 brief supplies display copy of its own.")
    d.save(path)
    return path


def summary(path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, "Early-edit synchronization summary",
                "What was done, what was found, what is outstanding")
    kv(d, "Generated", st)
    kv(d, "Intake archive", "intake.zip")
    kv(d, "Intake sha256", S.INTAKE_SHA)
    kv(d, "Scope", "NEW PUBLIC V4 to V11")
    callout(d, "This pass synchronized the EDIT against the September 16 "
               "scripts. It did not rebuild visual assets. The handoff "
               "states the briefs supplement existing production assets "
               "and are not permission for a rewrite or blanket rebuild, "
               "so the assets that no longer match are recorded in the "
               "ledger rather than redrawn.")

    h(d, "Source verification actually run")
    bullets(d, [
      "The intake archive hash was checked, and all 24 Word documents were "
      "checked against the hashes in SOURCE_MANIFEST.json. All 24 match.",
      "Every script's spoken word count was recounted from the document and "
      "compared with the manifest. All eight match.",
      "Every thought-block copy was compared paragraph by paragraph with "
      "its script. All eight are identical and in order.",
      "The three documented derivative repairs were confirmed present as "
      "spoken text in both the script and the thought-block copy.",
      "The V6 public employer substitution was confirmed, and all eight "
      "spoken scripts were searched for every employer name in the "
      "internal evidence layer. None appears in any spoken script.",
      "All 60 exact spoken triggers in the eight editing briefs were "
      "checked against their current script. All 60 were found.",
    ], size=10)

    h(d, "Script and recording-copy parity")
    table(d, ["", "Spoken words", "Manifest", "Paragraphs",
              "Thought-block parity"],
          [["V%d" % n, format(S.word_count(n), ","),
            format(S.manifest()["videos"][str(n)]["spoken_words"], ","),
            "%d" % len(S.paragraphs(n)),
            "identical and in order"] for n in S.VIDEOS],
          widths=[0.7, 1.1, 1.0, 1.0, 2.9], size=8)

    h(d, "The finding that governs everything else")
    para(d, "The September 16 scripts are a substantially different lineage "
            "from the one the existing production packages were built "
            "against, not a light revision. Measured across all 110 card "
            "families:", size=10.5)
    c = LG.counts(L)
    table(d, ["Verdict", "Families", "What it means"],
          [[LG.REUSE, "%d" % c.get(LG.REUSE, 0),
            "Cue sentence and every word of the teaching copy still exist "
            "in the current script. Usable as is."],
           [LG.REANCHOR, "%d" % c.get(LG.REANCHOR, 0),
            "The card is correct; its cue sentence is gone. An edit-map "
            "change, not a new asset."],
           [LG.COPY, "%d" % c.get(LG.COPY, 0),
            "The cue holds but teaching copy on the card no longer exists "
            "in the script. The card has to be redrawn."],
           [LG.REBUILD, "%d" % c.get(LG.REBUILD, 0),
            "Cue sentence gone and teaching copy gone. The card has to be "
            "redrawn and re-placed."]],
          widths=[1.1, 0.8, 4.8], size=8.5)
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    table(d, ["", "Families", LG.REUSE, LG.REANCHOR, LG.COPY, LG.REBUILD],
          [["V%d" % n, "%d" % len(per[n])]
           + ["%d" % LG.counts(per[n]).get(k, 0)
              for k in (LG.REUSE, LG.REANCHOR, LG.COPY, LG.REBUILD)]
           for n in sorted(per)], widths=[0.7, 1.0, 1.0, 1.1, 1.3, 1.1],
          size=8.5)
    callout(d, "73 of 110 families need their card redrawn, 60 of them in "
               "V4 to V9. Redrawing them is a rebuild of the visual layer "
               "for those six videos, which is the one thing this handoff "
               "says it is not authorizing. It is flagged here rather than "
               "done silently, and rather than shipping cards whose words "
               "contradict the script.")

    h(d, "What was delivered")
    bullets(d, [
      "Eight early-edit synchronization maps, one per video: viewer "
      "outcome, opening treatment, teaching moments, the five sound "
      "accents, the four camera-emphasis beats, the public boundary and "
      "the Watch Next passage.",
      "Every exact trigger resolved to its section and parent passage. "
      "Three triggers appear twice in their script and each is listed with "
      "both locations so the editor resolves it by section, not by first "
      "match.",
      "An asset ledger per video and a combined ledger, with a reason on "
      "every line.",
      "This summary.",
    ], size=10)

    h(d, "What was not done, and is not claimed")
    bullets(d, [
      "No visual asset was rebuilt, redrawn or re-rendered.",
      "No script, example, framework, section order, title, Watch Next or "
      "Shorts policy was altered. No sentence was invented for a Short.",
      "No historical archive was overwritten. The locked V4 to V21, V22 to "
      "V23, sprint V4 to V9 and V10 to V11 archives are untouched, and "
      "that was verified by hash.",
      "No recording, audio mix, footage QA, SRT, chapter timing, final "
      "runtime or retention result is claimed. None was performed.",
      "Existing factual and generalized claims in the scripts are "
      "preserved and were not independently reverified. The V4 opening, "
      "AI doing in 30 seconds what used to take three hours, is not "
      "treated as a measured benchmark anywhere in this layer and must "
      "not become a speed statistic graphic.",
      "V6's ten-minute promise is a claim about the finished edit. The "
      "1,096-word script gives 7.6 to 8.4 minutes of speech-only "
      "arithmetic, which is not a timed export. Check the actual cut "
      "before publishing under that title.",
    ], size=10)

    h(d, "Unresolved dependencies")
    table(d, ["", "What is outstanding"],
          [["Visual layer",
            "73 families need redrawing from the current script. That "
            "decision is yours: the handoff withholds blanket rebuild "
            "permission and the ledger names every affected family."],
           ["V10 thumbnail",
            "The current source carries the longer wording, DON'T SPEND "
            "YOUR FIRST 90 DAYS PROVING YOURSELF. The locked V10 package "
            "still carries the older shorter wording. The package metadata "
            "has not been changed in this pass because that package's "
            "script has also moved."],
           ["Watch Next availability",
            "Every destination still needs checking against what is "
            "publicly live at upload. Flag rather than substitute."],
           ["V4 opening claim",
            "Its evidence status is unresolved in this handoff and needs "
            "settling before public release."]],
          widths=[1.3, 5.4], size=8.5)
    footer_note(d, "Arithmetic estimates in these documents are arithmetic "
                   "on the script. Nothing here has been recorded, edited "
                   "or exported.")
    d.save(path)
    return path


def combined_ledger(path, st, L):
    d = base_doc()
    title_block(d, EYEBROW, "Asset ledger, V4 to V11",
                "Reuse, re-anchor, copy update, rebuild, with reasons")
    kv(d, "Generated", st)
    kv(d, "Families audited", "%d" % len(L))
    c = LG.counts(L)
    kv(d, "Verdicts", "  ".join("%s %d" % (k, c.get(k, 0)) for k in
                                (LG.REUSE, LG.REANCHOR, LG.COPY,
                                 LG.REBUILD)))
    callout(d, "Two independent questions were asked of every family and "
               "never conflated. ANCHOR: does its exact trigger sentence "
               "still exist in the current script? COPY: does every word "
               "of its teaching copy still exist there? A family can keep "
               "one and lose the other, and the remedy is different.")
    per = {}
    for r in L:
        per.setdefault(r["video"], []).append(r)
    for n in sorted(per):
        h(d, "NEW PUBLIC V%d  %s" % (n, S.title(n)))
        table(d, ["Family", "Anchor", "Verdict", "Why"],
              [[r["key"], r["anchor"] or "end card", r["verdict"],
                r["reason"]] for r in per[n]],
              widths=[2.2, 0.7, 1.0, 2.8], size=7.5)
    d.save(path)
    return path


def main():
    st = stamp()
    print("stamp:", st)
    got = sha256(os.path.join(OUT, "_source", "intake.zip"))
    print("  intake.zip  %s" % ("verified" if got == S.INTAKE_SHA
                                else "MISMATCH"))
    if got != S.INTAKE_SHA:
        raise SystemExit("intake mismatch")
    man = S.manifest()
    bad = 0
    for n in S.VIDEOS:
        for o in man["videos"][str(n)]["outputs"]:
            if sha256(os.path.join(S.SRC, o["file"])) != o["sha256"]:
                bad += 1
    if bad:
        raise SystemExit("%d documents do not match the manifest" % bad)
    print("  24 documents verified against SOURCE_MANIFEST.json")
    for n in S.VIDEOS:
        ok, det = S.blocks_match(n)
        if not ok:
            raise SystemExit("V%d thought-block mismatch: %s" % (n, det))
        w = man["videos"][str(n)]["spoken_words"]
        if S.word_count(n) != w:
            raise SystemExit("V%d word count %d, manifest %d"
                             % (n, S.word_count(n), w))
    print("  eight scripts and eight thought-block copies, all parity")
    tb = sum(len(B.verify(n)) for n in S.VIDEOS)
    if tb:
        raise SystemExit("%d brief triggers not found in their script" % tb)
    print("  60 brief triggers, all found in their current script")

    L = LG.ledger()
    out = os.path.join(OUT, "EDIT_SYNC")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    files = []
    for n in S.VIDEOS:
        files.append(edit_map(n, os.path.join(
            out, "V%02d_EARLY_EDIT_SYNC_MAP.txt" % n), st))
        files.append(video_ledger(n, os.path.join(
            out, "V%02d_ASSET_LEDGER.docx" % n), st,
            [r for r in L if r["video"] == n]))
    files.append(combined_ledger(os.path.join(
        out, "V4-V11_ASSET_LEDGER.docx"), st, L))
    files.append(summary(os.path.join(
        out, "V4-V11_EDIT_SYNC_SUMMARY.docx"), st, L))

    zpath = os.path.join(OUT, ARCHIVE)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as z:
        for p in sorted(files):
            zi = zipfile.ZipInfo(os.path.basename(p), date_time=ZIP_DT)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(p, "rb") as fh:
                z.writestr(zi, fh.read())
    digest = sha256(zpath)
    with open(zpath + ".sha256", "w") as f:
        f.write("%s  %s\n" % (digest, ARCHIVE))
    c = LG.counts(L)
    print("\n  %s" % ARCHIVE)
    print("  sha256 %s" % digest)
    print("  %d entries" % len(zipfile.ZipFile(zpath).namelist()))
    print("  ledger: %s" % "  ".join("%s %d" % (k, c.get(k, 0)) for k in
                                     (LG.REUSE, LG.REANCHOR, LG.COPY,
                                      LG.REBUILD)))


if __name__ == "__main__":
    main()
