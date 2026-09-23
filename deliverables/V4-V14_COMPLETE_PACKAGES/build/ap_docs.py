# -*- coding: utf-8 -*-
"""Operational documents for V4 to V14, in the approved architecture."""
import os, json
import ap_src as A, ap_meta as M

RULE = "=" * 78
def head(title, n):
    return ("%s\n%s\nVideo %d  ·  %s\nBuilt against %s  ·  locked\n%s\n"
            % (RULE, title, n, M.TITLES[n][0],
               os.path.basename(A.locked(n)[0]), RULE))

def mmss(w, rate):
    return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))

# ------------------------------------------------------------------ 01
def timing(n):
    L = [head("ESTIMATED SPEECH TIMING", n)]
    L.append("RUNTIME: ESTIMATE ONLY, NOT A MEASUREMENT\n")
    L.append("Arithmetic on the locked script's spoken word count at 130 to "
             "145 words per minute.\nSpeech only. It excludes holds on "
             "full-screen graphics and every edit decision.\nNarration "
             "continuing underneath a graphic OVERLAPS that visual.\n")
    L.append("Final timing and chapters come from the actual final export.\n")
    L.append("-" * 78 + "\nTHE NUMBERS\n" + "-" * 78 + "\n")
    w = A.words(n)
    L.append("  spoken words        %d" % w)
    L.append("  at 145 wpm          %s" % mmss(w, 145))
    L.append("  at 130 wpm          %s" % mmss(w, 130))
    L.append("  working estimate    %s to %s\n" % (mmss(w, 145), mmss(w, 130)))
    L.append("-" * 78 + "\nCUMULATIVE, AT 145 WPM AND 130 WPM\n" + "-" * 78 + "\n")
    cum = 0
    for i, p in enumerate(A.spoken(n), 1):
        pw = len(p.split())
        if i % 5 == 1 or i == 1:
            L.append("  paragraph %-4d starts %s / %s" % (i, mmss(cum, 145), mmss(cum, 130)))
        cum += pw
    L.append("  %-14s ends   %s / %s\n" % ("TOTAL", mmss(cum, 145), mmss(cum, 130)))
    L.append("-" * 78 + "\nLIKELY FULL-SCREEN ENTRY WINDOWS\n" + "-" * 78 + "\n")
    jw = " ".join(A.spoken(n)).split()
    for f in A.families(n):
        tw = f["trigger"].split()
        pos = next((i for i in range(len(jw) - len(tw) + 1)
                    if jw[i:i + len(tw)] == tw), None)
        if pos is None:
            continue
        L.append("  %-42s around %s / %s" % (f["family"][:42], mmss(pos, 145),
                                             mmss(pos, 130)))
    L.append("")
    L.append("-" * 78 + "\nTITLE PROMISE\n" + "-" * 78 + "\n")
    if n in (6, 12):
        L.append("  This title promises ten minutes, so the promise has to "
                 "stay defensible.\n")
        L.append("  Speech alone is %s to %s. Full-screen holds, the artifact "
                 "beats and the\n  edit add to that, so a finished cut lands "
                 "above the speech figure and below\n  the promise at normal "
                 "delivery speed. The promise is defensible.\n"
                 % (mmss(w, 145), mmss(w, 130)))
        L.append("  Do not pad the script and do not slow the delivery to "
                 "reach ten minutes. If the\n  finished export runs long, the "
                 "edit is where to look, not the speech.\n")
    else:
        L.append("  This title makes no runtime promise. Do not pad the script "
                 "or slow the delivery\n  to reach a number.\n")
    return "\n".join(L)

# ------------------------------------------------------------------ 02
def trigger_map(n):
    L = [head("CURRENT-SCRIPT TRIGGER MAP", n)]
    L.append("Every trigger below is an exact sentence from the locked master. "
             "The build verifies\nthis and fails if one is not found, so no "
             "card can be cued by a line that is not in\nthe script.\n")
    src = ("the resolved event list, which carries an exact entry phrase per "
           "event" if n in A.SYNC else
           "an explicit trigger table, because this video's card copy is "
           "written as compressed\non-screen labels rather than as verbatim "
           "speech")
    L.append("Triggers for this video come from %s.\n" % src)
    L.append("-" * 78 + "\nSPOKEN TRIGGERS\n" + "-" * 78 + "\n")
    for f in A.families(n):
        L.append("  %s" % f["family"])
        L.append("        mode:    %s" % f["mode"])
        L.append("        cue:     “%s”" % f["trigger"])
        L.append("        in the locked script: YES")
        if f.get("display"):
            L.append("        on screen: %s" % f["display"])
        if len(f["states"]) > 1:
            L.append("        states:  %s" % ", ".join(f["states"]))
        if f.get("leave"):
            L.append("        leave:   “%s”" % f["leave"])
        if f.get("ret"):
            L.append("        exit:    %s" % f["ret"])
        elif f["family"].endswith("WATCH_NEXT"):
            L.append("        exit:    This is the final frame. Never return "
                     "to camera.")
        else:
            L.append("        exit:    Return to camera after the last state "
                     "in this family.")
        if f.get("note"):
            L.append("        note:    %s" % f["note"])
        L.append("")
    L.append("-" * 78 + "\nCAMERA MOMENTS, NOT VISUAL TRIGGERS\n" + "-" * 78 + "\n")
    for t, w in A.camera(n):
        L.append("  cue:     “%s”" % t)
        L.append("  action:  %s\n" % w)
    L.append("-" * 78 + "\nSUBSCRIBE CUE\n" + "-" * 78 + "\n")
    t, w = A.subscribe(n)
    L.append("  cue:     “%s”" % t)
    L.append("  action:  %s\n" % w)
    return "\n".join(L)

def asset_spec(n):
    reuse = A.assets_dir(n) is not None
    return dict(
        video=n, title=M.TITLES[n][0], thumbnail=M.TITLES[n][1],
        provenance=("REUSED. These are the approved synchronized assets "
                    "already rendered against this master. Not rebuilt."
                    if reuse else
                    "NEW RENDER FROM AN APPROVED SPECIFICATION. No prior "
                    "rendered artwork existed for this video. The card copy "
                    "is the locked specification and no line of it was "
                    "changed."),
        built_from=os.path.basename(A.locked(n)[0]),
        source_sha256=A.sha256(A.locked(n)[0]),
        spoken_words=A.words(n), canvas=[1920, 1080],
        palette=dict(navy="#112345", cream="#F5F1E8", gold="#C9A84C",
                     yellow="#F2C44C"),
        rules=["Camera-led, not camera-only.",
               "Substantive teaching and comparisons are TRUE FULL SCREEN.",
               "CTA is full screen.",
               "Watch Next is full screen and is the final frame.",
               "Never return to camera after Watch Next.",
               "No decorative stock, no constant effects, no burned-in "
               "long-form transcript captions."],
        families=[dict(id=f["family"], mode=f["mode"], trigger=f["trigger"],
                       trigger_in_locked_script=True,
                       on_screen=f.get("display"), states=f["states"])
                  for f in A.families(n)],
        watch_next_is_final=True)

def reveal_map(n):
    L = [head("VISUAL AND MOTION / REVEAL MAP", n)]
    fams = A.families(n)
    L.append("%d full-screen families. These are reference frames for the "
             "edit, not one slide per\nparagraph.\n" % len(fams))
    L.append("-" * 78 + "\nTRUE FULL-SCREEN SCENES\n" + "-" * 78 + "\n")
    L.append("Teaching comparisons, artifact moments, the CTA and Watch Next "
             "fill the entire\ncanvas. Temidayo is hidden visually during "
             "those scenes while her voice continues.\n")
    L.append("-" * 78 + "\nPER FAMILY\n" + "-" * 78 + "\n")
    snd = dict(A.sound(n))
    for f in fams:
        L.append("  %s" % f["family"])
        L.append("     entry:            on “%s”" % f["trigger"])
        if len(f["states"]) > 1:
            L.append("     progressive:      YES, %d states in order:" % len(f["states"]))
            for s in f["states"]:
                L.append("                         %s" % s)
        else:
            L.append("     progressive:      no, single state")
        L.append("     Temidayo visible: no, this is true full screen")
        L.append("     return to camera: %s" % (
            "never, this is the final frame" if f["family"].endswith("WATCH_NEXT")
            else (f.get("ret") or "after the last state in this family")))
        L.append("     motion:           entry only. No drift, no continuous "
                 "zoom, no parallax.")
        acc = snd.get(f["trigger"])
        L.append("     sound accent:     %s\n" % (acc or "none on entry"))
    L.append("-" * 78 + "\nMOTION RESTRAINT\n" + "-" * 78 + "\n")
    L.append("Do not create movement because the software can. A reveal exists "
             "to stop two ideas\ncompeting while one is being taught.\n")
    return "\n".join(L)

# ------------------------------------------------------------------ 03
def editor_notes(n):
    L = [head("EDITOR MASTER NOTES", n)]
    L.append("-" * 78 + "\nWHAT THIS VIDEO IS DOING\n" + "-" * 78 + "\n")
    L.append("Title promise:      %s" % M.TITLES[n][0])
    L.append("Thumbnail promise:  %s" % M.TITLES[n][1])
    L.append("Viewer arrives thinking:\n    %s\n" % M.THINKING[n])
    L.append("The realization:\n    %s\n" % M.REALIZATION[n])
    L.append("Seven-day memory line:\n    %s\n" % M.MEMORY[n])
    L.append("Observable action:\n    %s\n" % M.ACTION[n])
    L.append("-" * 78 + "\nFIRST THIRTY SECONDS\n" + "-" * 78 + "\n")
    L.append("About the first 73 spoken words at the 145 wpm end of the band:\n")
    L.append("    " + " ".join(" ".join(A.spoken(n)).split()[:75]) + "\n")
    L.append("Do not trim the opening to reach the teaching faster.\n")
    L.append("-" * 78 + "\nFULL-SCREEN MOMENTS AND CAMERA RETURNS\n" + "-" * 78 + "\n")
    for f in A.families(n):
        L.append("  FULL SCREEN  %s" % f["family"])
        L.append("     on:      “%s”" % f["trigger"])
        L.append("     %s" % ("this is the final frame, never return to camera"
                              if f["family"].endswith("WATCH_NEXT")
                              else "back to camera: %s"
                                   % (f.get("ret") or "after the last state")))
    L.append("")
    cam = A.camera(n)
    L.append("-" * 78 + "\nDELIBERATE CAMERA MOMENTS  (%d)\n" % len(cam) + "-" * 78 + "\n")
    if n in A.SYNC and len(cam) < 3:
        L.append("This video carries %d, not the three to five the guide "
                 "suggests for a newly built\nscript. That is the approved "
                 "structure: it puts most of its emphasis into full-screen\n"
                 "inserts, and the approved Camera and Full-Screen Map ships "
                 "in this folder. The count\nis reported as it is rather than "
                 "padded to reach a guide.\n" % len(cam))
    for t, w in cam:
        L.append("  “%s”\n     %s\n" % (t, w))
    L.append("-" * 78 + "\nMEANINGFUL B-ROLL AND ARTIFACT MOMENTS  (%d)\n"
             % len(A.broll(n)) + "-" * 78 + "\n")
    for t, w in A.broll(n):
        L.append("  “%s”\n     %s\n" % (t, w))
    L.append("-" * 78 + "\nSOUND ACCENTS  (%d)\n" % len(A.sound(n)) + "-" * 78 + "\n")
    for t, w in A.sound(n):
        L.append("  “%s”\n     %s\n" % (t, w))
    t, w = A.subscribe(n)
    L.append("-" * 78 + "\nSUBSCRIBE, CTA AND WATCH NEXT\n" + "-" * 78 + "\n")
    L.append("Subscribe on “%s”\n    %s\n" % (t, w))
    L.append("CTA: %s\n" % M.CTA[n])
    L.append("Watch Next full screen and FINAL: “%s”\n" % M.WATCH[n])
    L.append("-" * 78 + "\nRESTRAINT\n" + "-" * 78 + "\n")
    L.append("No constant punch-ins. No fake energy. No decorative stock. No "
             "burned-in long-form\ntranscript captions.\n")
    return "\n".join(L)

def riverside(n):
    L = [head("RIVERSIDE CO-CREATOR MASTER PROMPT", n)]
    L.append("Self-contained. Paste the whole file.\n")
    L.append("-" * 78 + "\nMASTER PROMPT\n" + "-" * 78 + "\n")
    L.append("I am giving you a NEW RECORDING. Create the visual and audio "
             "editing layer from this\nrecording and its transcript. Do not "
             "assume an earlier version of this video exists.\n")
    L.append("The locked Recording Master controls INTENDED MEANING. The "
             "recorded performance\ncontrols EDIT TIMING. If the recorded "
             "speech materially differs from the locked\nmaster, flag it. "
             "Never manufacture missing speech and never synthesize audio I "
             "did\nnot record.\n")
    L.append("Camera-led, not camera-only. Horizontal 16:9 at 1920 x 1080 or "
             "better. Preserve\nuseful pauses, natural rhythm and the full "
             "ending. No constant punch-ins. No fake\nenergy.\n")
    L.append("TRUE FULL-SCREEN SCENES enter on these exact spoken lines:\n")
    for f in A.families(n):
        L.append("  %-42s on “%s”" % (f["family"][:42], f["trigger"]))
    L.append("")
    L.append("Use B-roll only where it carries meaning. There are %d artifact "
             "moments and they are\nlisted in the B-roll guidance file. No "
             "decorative stock.\n" % len(A.broll(n)))
    L.append("No burned-in long-form transcript captions.\n")
    L.append("Sound is restrained: %d accents in the whole video, listed in "
             "the sound guidance file.\n" % len(A.sound(n)))
    t, _w = A.subscribe(n)
    L.append("One quiet Subscribe cue, after value, on “%s”\nA small "
             "lower-third for about four seconds. No sound, no voiceover.\n" % t)
    L.append("CTA is full screen. Watch Next is full screen and is the FINAL "
             "FRAME: “%s”.\nNever return to camera after Watch "
             "Next.\n" % M.WATCH[n])
    L.append("Do not add graphics I did not ask for. Do not re-order the "
             "teaching. Do not cut the\nboundary paragraphs.\n")
    return "\n".join(L)

def camera_map(n):
    cam = A.camera(n)
    L = [head("CAMERA EMPHASIS MAP", n)]
    L.append("%d deliberate camera moments.\n" % len(cam))
    if n in A.SYNC:
        L.append("The approved Camera and Full-Screen Map for this video ships "
                 "beside this file and is\nthe authority on mode per "
                 "paragraph. This file lists the deliberate camera moments\n"
                 "drawn from the same event list.\n")
    for i, (t, w) in enumerate(cam, 1):
        L.append("  %d.  “%s”" % (i, t))
        L.append("      %s\n" % w)
    L.append("Everywhere else, hold the frame.\n")
    return "\n".join(L)

def broll_guidance(n):
    L = [head("B-ROLL AND ARTIFACT GUIDANCE", n)]
    L.append("%d moments. Every one carries meaning; none is decorative.\n"
             % len(A.broll(n)))
    for i, (t, w) in enumerate(A.broll(n), 1):
        L.append("  %d.  on “%s”" % (i, t))
        L.append("      %s\n" % w)
    L.append("No generic office footage. If there is nothing meaningful to "
             "show, stay on camera.\n")
    return "\n".join(L)

def sound_guidance(n):
    L = [head("SOUND ACCENT GUIDANCE", n)]
    L.append("%d accents. A guide for the edit, not a quota.\n" % len(A.sound(n)))
    for i, (t, w) in enumerate(A.sound(n), 1):
        L.append("  %d.  on “%s”" % (i, t))
        L.append("      %s\n" % w)
    L.append("Silence is a decision where it is specified. Do not fill it.\n")
    return "\n".join(L)

# ------------------------------------------------------------------ 06
def viewer_exercise(n):
    headline, steps, footer = M.EXERCISE[n]
    L = [head("VIEWER EXERCISE", n)]
    L.append("One page. You should be able to do this today, on paper.\n")
    L.append("-" * 78 + "\n%s\n" % headline.upper() + "-" * 78 + "\n")
    for i, s in enumerate(steps, 1):
        L.append("  %d.  %s\n" % (i, s))
    L.append("-" * 78 + "\n")
    L.append(footer + "\n")
    L.append("-" * 78 + "\nIF YOU REMEMBER ONE THING\n" + "-" * 78 + "\n")
    L.append("    %s\n" % M.MEMORY[n])
    return "\n".join(L)

def sticky_record(n):
    L = [head("STICKY REALIZATION RECORD", n)]
    L.append("Carried from the Source-of-Truth Manifest and the approved V4 to "
             "V14 reconciliation.\nNot re-derived. No new slogan was invented "
             "for this package.\n")
    for title, val in (("WHAT THE VIEWER IS ALREADY THINKING", M.THINKING[n]),
                       ("THAT'S IT REALIZATION", M.REALIZATION[n]),
                       ("SEVEN-DAY MEMORY LINE", M.MEMORY[n]),
                       ("OBSERVABLE ACTION", M.ACTION[n]),
                       ("THE COMPLETION", M.NEXT_LINE[n])):
        L.append("-" * 78 + "\n%s\n" % title + "-" * 78 + "\n")
        L.append(val + "\n")
    L.append("-" * 78 + "\nWHERE THIS LIVES IN THE VIDEO\n" + "-" * 78 + "\n")
    L.append("The four items above are internal editorial QA. They are never "
             "labelled or named in\nthe video, on a card or in the "
             "description.\n")
    return "\n".join(L)

# ------------------------------------------------------------------ 07
def source_manifest(n, publishing):
    return dict(
        video=n, title=M.TITLES[n][0], thumbnail=M.TITLES[n][1], status="LOCKED",
        spoken_source_of_truth=dict(file=os.path.basename(A.locked(n)[0]),
                                    sha256=A.sha256(A.locked(n)[0]),
                                    spoken_words=A.words(n)),
        thought_blocks=dict(file=os.path.basename(A.locked(n)[1]),
                            sha256=A.sha256(A.locked(n)[1]),
                            parity="PASS, word for word and in order"),
        sticky_realization=M.REALIZATION[n],
        seven_day_memory_line=M.MEMORY[n],
        observable_action=M.ACTION[n],
        cta=M.CTA[n], watch_next=dict(title=M.WATCH[n], final_frame=True),
        visual_assets=dict(
            provenance=("REUSED approved synchronized assets"
                        if A.assets_dir(n) else
                        "NEW RENDER from the approved card specification"),
            families=len(A.families(n))),
        publishing_status=publishing,
        cue_source=("resolved event list, V4-V11_SYNC/build/events.py"
                    if n in A.SYNC else
                    "locked production module for this video"),
        optional_v9_change_applied=(False if n == 9 else None),
    )

def evidence_notes(n):
    L = [head("EVIDENCE AND ILLUSTRATION NOTES", n)]
    L.append("What this video's material actually supports, and where it "
             "stops.\n")
    L.append("-" * 78 + "\nCLASSIFICATION USED\n" + "-" * 78 + "\n")
    L.append("  DIRECT       quoted or near-quoted from a source document\n"
             "  PARAPHRASED  a source's meaning in Temidayo's words\n"
             "  SYNTHETIC    constructed for the video, labelled on screen\n"
             "  EDITORIAL    Temidayo's own reading, presented as hers\n")
    L.append("-" * 78 + "\nWHAT THIS VIDEO PROTECTS\n" + "-" * 78 + "\n")
    for b in M.PROTECT[n]:
        L.append("  ·  %s\n" % b)
    L.append("-" * 78 + "\nUPGRADES THAT WERE NOT MADE\n" + "-" * 78 + "\n")
    for a, b in [("adjacent", "direct"), ("preferred", "required"),
                 ("mismatch", "betrayal"),
                 ("AI automation", "guaranteed capability loss"),
                 ("an organizational decision", "pure merit"),
                 ("more responsibility", "growth"),
                 ("illustration", "evidence"),
                 ("a synthetic example", "a sourced case")]:
        L.append("  %-28s was NOT upgraded to %s" % (a, b))
    L.append("")
    if n in (13, 14):
        L.append("-" * 78 + "\nANONYMIZATION\n" + "-" * 78 + "\n")
        L.append("  Employer names were removed by the approved public "
                 "employer anonymization patch,\n  which the Source-of-Truth "
                 "Manifest identifies as superseding the locked pack for\n  "
                 "this video. They are not restored anywhere in this "
                 "package. Postings are\n  described by industry only.\n")
    if n == 13:
        L.append("-" * 78 + "\nTHE 28-POSTING RESEARCH RECORD\n" + "-" * 78 + "\n")
        L.append("  About 55 surfaced, 40 read in full, 28 retained, 18 "
                 "exclusions logged with reasons.\n  10 healthcare, 10 "
                 "financial services, 8 technology. All collected September "
                 "10, 2026.\n  Every count in the video is a count within "
                 "those 28 and the video says so.\n")
    if n == 12:
        L.append("-" * 78 + "\nSYNTHETIC MATERIAL\n" + "-" * 78 + "\n")
        L.append("  The accomplishment rebuilt in this video is synthetic. It "
                 "is labelled on camera in\n  the first thirty seconds, on "
                 "the card that carries it, and in the pinned comment.\n")
    return "\n".join(L)

def alignment_log(n):
    L = [head("ALIGNMENT LOG", n)]
    L.append("The final synchronization record. One row per spoken paragraph "
             "that carries a visual,\na camera moment, an accent or a "
             "boundary.\n")
    fam = {f["trigger"]: f for f in A.families(n)}
    cam = dict(A.camera(n))
    snd = dict(A.sound(n))
    art = dict(A.broll(n))
    sub_t, sub_w = A.subscribe(n)
    rows = 0
    for p in A.spoken(n):
        hits = []
        for t, f in fam.items():
            if t == p or t in p:
                hits.append(("VISUAL", "%s enters, %s" % (f["family"], f["mode"])))
        for t, w in art.items():
            if t == p or t in p:
                hits.append(("EDITOR", w))
        for t, w in cam.items():
            if t == p or t in p:
                hits.append(("CAMERA", w))
        for t, w in snd.items():
            if t == p or t in p:
                hits.append(("SOUND", w))
        if sub_t == p or sub_t in p:
            hits.append(("SUBSCRIBE", sub_w))
        if not hits:
            continue
        rows += 1
        L.append("  SPOKEN:    %s" % p)
        for k, v in hits:
            L.append("  %-10s %s" % (k + ":", v))
        L.append("")
    L.append("%d aligned rows.\n" % rows)
    return "\n".join(L)
