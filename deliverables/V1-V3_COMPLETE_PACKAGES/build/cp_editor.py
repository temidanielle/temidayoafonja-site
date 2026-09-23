# -*- coding: utf-8 -*-
"""Editor-facing operational layer, and the Riverside CoCreator prompt.

The old packages carried a Riverside prompt. This recreates that layer using
the old one as structural reference and the current production rules as the
authority, as the brief requires.
"""
import os, json
import cp_src as C, cp_trig as T, cp_visuals as V

RULE = "=" * 78

def _head(title, n):
    return ("%s\n%s\nVideo %d  ·  %s\nBuilt against %s  ·  locked "
            "September 23, 2026\n%s\n"
            % (RULE, title, n, C.META[n]["title"],
               os.path.basename(C.LOCKED[n][0]), RULE))

def riverside_prompt(n):
    m = C.META[n]
    rows = V.trigger_rows(n)
    L = [_head("RIVERSIDE CO-CREATOR MASTER PROMPT", n)]
    L.append("Self-contained. Paste the whole file. It assumes no previous "
             "conversation and no\nexisting graphics.\n")
    L.append("-" * 78 + "\nMASTER PROMPT\n" + "-" * 78 + "\n")
    L.append("I am giving you a NEW RECORDING. Create the visual and audio "
             "editing layer from\nthis recording and its transcript. Do not "
             "look for existing graphics to convert,\nand do not assume an "
             "earlier version of this video exists.\n")
    L.append("The locked Recording Master controls INTENDED MEANING. The "
             "recorded performance\ncontrols EDIT TIMING. If the recorded "
             "speech materially differs from the locked\nmaster, flag the "
             "mismatch and tell me which lines differ. Never manufacture "
             "missing\nspeech and never generate or synthesize audio I did not "
             "record.\n")
    L.append("CAMERA-LED FORMAT\n")
    L.append("Horizontal 16:9, exported at 1920 x 1080 or better. Clean false "
             "starts, unnecessary\nrepetitions and accidental waiting footage. "
             "Preserve useful pauses, natural rhythm,\ncomplete explanations "
             "and the full ending. Do not over-shorten the teaching.\n")
    L.append("Camera-led, not camera-only. Use camera emphasis selectively, at "
             "the beats listed\nbelow, and nowhere else. No constant punch-ins. "
             "No continuous zoom. No fake energy.\n")
    L.append("TRUE FULL-SCREEN SCENES\n")
    L.append("Teaching comparisons, artifact moments, the seven-day memory "
             "card, the CTA and Watch\nNext fill the entire canvas. Hide me "
             "visually during those scenes while my voice\ncontinues. Each one "
             "enters on the exact spoken trigger listed below.\n")
    for r in rows:
        if not r["trigger"]:
            continue
        L.append("  %-34s enters on “%s”" % (r["family"], r["trigger"]))
    L.append("")
    L.append("B-ROLL\n")
    L.append("Use B-roll only where it carries meaning. There are %d artifact "
             "moments in this\nvideo and they are listed in the B-roll "
             "guidance file. No decorative stock, no filler,\nno generic office "
             "footage.\n" % len(C.SPR.BROLL[n]))
    L.append("CAPTIONS\n")
    L.append("No burned-in long-form transcript captions. Short on-screen "
             "text only where the\nreveal map calls for it.\n")
    L.append("SOUND\n")
    L.append("Restrained. %d accents in the whole video, listed in the sound "
             "guidance file. Silence\nis a legitimate choice and is specified "
             "in several places.\n" % len(C.SPR.SOUND[n]))
    L.append("SUBSCRIBE\n")
    L.append("One quiet Subscribe cue, after value has been delivered, on "
             "“%s”\nIt is a small lower-third for about four "
             "seconds. No sound, no voiceover.\n"
             % C.SPR.SUBSCRIBE[n][0])
    L.append("ENDING\n")
    L.append("CTA is full screen: %s. Watch Next is full screen and is the "
             "FINAL FRAME:\n“%s”. Never return to camera after Watch "
             "Next.\n" % (m["cta"], m["watch"]))
    L.append("WHAT NOT TO DO\n")
    L.append("Do not add graphics I did not ask for. Do not summarize or "
             "re-order the teaching. Do\nnot cut the boundary paragraphs; they "
             "are the reason the video is honest. Do not add\nmusic under the "
             "sections marked silent.\n")
    return "\n".join(L)

def editor_notes(n):
    m = C.META[n]
    rows = V.trigger_rows(n)
    L = [_head("EDITOR MASTER NOTES", n)]
    L.append("-" * 78 + "\nWHAT THIS VIDEO IS DOING\n" + "-" * 78 + "\n")
    L.append("Title promise:      %s" % m["title"])
    L.append("Thumbnail promise:  %s" % m["thumb"])
    L.append("Viewer arrives thinking:\n    %s\n" % m["thinking"])
    L.append("The realization:\n    %s\n" % m["realization"])
    L.append("Seven-day memory line:\n    %s\n" % m["memory"])
    L.append("Observable action:\n    %s\n" % m["action"])
    L.append("-" * 78 + "\nFIRST THIRTY SECONDS\n" + "-" * 78 + "\n")
    ms = C.SP.master_sentences(n)
    L.append("About the first 73 spoken words at the 145 wpm end of the band. "
             "The title and\nthumbnail promise has to be met inside that, and "
             "it is:\n")
    L.append("    " + " ".join(" ".join(p for _s, p in C.SP.spoken(n)).split()[:75]))
    L.append("\nDo not trim the opening to get to the teaching faster. The "
             "recognition beat is what\nmakes the rest land.\n")
    L.append("-" * 78 + "\nSTORY SHAPE\n" + "-" * 78 + "\n")
    for sec, paras in C.SP.master(n)[1]:
        L.append("  %-34s %d paragraph%s" % (sec, len(paras),
                                             "" if len(paras) == 1 else "s"))
    L.append("")
    L.append("-" * 78 + "\nFULL-SCREEN MOMENTS AND CAMERA RETURNS\n" + "-" * 78 + "\n")
    for r in rows:
        if not r["trigger"]:
            continue
        L.append("  FULL SCREEN  %s" % r["family"])
        L.append("     on:      “%s”" % r["trigger"])
        L.append("     back to camera after the last state in this family."
                 if not r["family"].endswith("WATCH_NEXT")
                 else "     this is the final frame. Never return to camera.")
    L.append("")
    L.append("-" * 78 + "\nCAMERA-EMPHASIS BEATS  (%d, guide is 3 to 5)\n"
             % len(C.SPR.CAMERA[n]) + "-" * 78 + "\n")
    for t, w in C.SPR.CAMERA[n]:
        L.append("  “%s”\n     %s\n" % (t, w))
    L.append("-" * 78 + "\nMEANINGFUL B-ROLL AND ARTIFACT MOMENTS  (%d, guide "
             "is 2 to 4)\n" % len(C.SPR.BROLL[n]) + "-" * 78 + "\n")
    for t, w in C.SPR.BROLL[n]:
        L.append("  “%s”\n     %s\n" % (t, w))
    L.append("-" * 78 + "\nSOUND ACCENTS  (%d, guide is 4 to 7)\n"
             % len(C.SPR.SOUND[n]) + "-" * 78 + "\n")
    for t, w in C.SPR.SOUND[n]:
        L.append("  “%s”\n     %s\n" % (t, w))
    L.append("-" * 78 + "\nSUBSCRIBE, CTA AND WATCH NEXT\n" + "-" * 78 + "\n")
    L.append("Subscribe on “%s”\n    %s\n"
             % (C.SPR.SUBSCRIBE[n][0], C.SPR.SUBSCRIBE[n][1]))
    L.append("CTA full screen: %s\n    %s\n" % (m["cta"], m["cta_url"]))
    L.append("Watch Next full screen and FINAL: “%s”\n" % m["watch"])
    L.append("-" * 78 + "\nRESTRAINT\n" + "-" * 78 + "\n")
    L.append("No constant zooming. No fake energy. No unnecessary effects. No "
             "decorative stock.\nIf an effect does not help the viewer "
             "understand the teaching, it does not belong.\n")
    return "\n".join(L)

def camera_map(n):
    L = [_head("CAMERA EMPHASIS MAP", n)]
    L.append("%d beats. The guide is 3 to 5. Each one names the exact sentence "
             "it starts on.\n" % len(C.SPR.CAMERA[n]))
    for i, (t, w) in enumerate(C.SPR.CAMERA[n], 1):
        L.append("  %d.  “%s”" % (i, t))
        L.append("      %s\n" % w)
    L.append("Everywhere else, hold the frame. Emphasis that happens "
             "constantly stops being\nemphasis.\n")
    return "\n".join(L)

def broll_guidance(n):
    L = [_head("B-ROLL AND ARTIFACT GUIDANCE", n)]
    L.append("%d moments. The guide is 2 to 4. Every one carries meaning; none "
             "is decorative.\n" % len(C.SPR.BROLL[n]))
    for i, (t, w) in enumerate(C.SPR.BROLL[n], 1):
        L.append("  %d.  on “%s”" % (i, t))
        L.append("      %s\n" % w)
    con = [c for c in C.SV.CONSTRUCTED if c[0] == n]
    if con:
        L.append("-" * 78 + "\nCONSTRUCTED MATERIAL\n" + "-" * 78 + "\n")
        for _n, cid, what, why in con:
            L.append("  %s" % cid)
            L.append("      %s" % what)
            L.append("      on-card label: SYNTHETIC EXAMPLE, held for the "
                     "whole hold")
            L.append("      %s\n" % why)
    L.append("No generic office footage. No stock hands on keyboards. If there "
             "is nothing\nmeaningful to show, stay on camera.\n")
    return "\n".join(L)

def sound_guidance(n):
    L = [_head("SOUND ACCENT GUIDANCE", n)]
    L.append("%d accents. The guide is 4 to 7. A guide for the edit, not a "
             "quota.\n" % len(C.SPR.SOUND[n]))
    for i, (t, w) in enumerate(C.SPR.SOUND[n], 1):
        L.append("  %d.  on “%s”" % (i, t))
        L.append("      %s\n" % w)
    L.append("Silence is specified in several places above and is a decision, "
             "not an omission.\nDo not fill it.\n")
    return "\n".join(L)

def shorts_manifest(n):
    out = dict(video=n, title=C.META[n]["title"],
               built_from=os.path.basename(C.LOCKED[n][0]),
               source_sha256=C.sha256(C.LOCKED[n][0]),
               standard="Three candidate Shorts per long-form. A selection "
                        "bank, not three mandatory uploads. The old six-Short "
                        "requirement is retired and was not restored.",
               structure="STOP SCROLL, HOLD, ONE ASK",
               verbatim_rule="Every line is an unbroken run of the locked "
                             "master's own words, verified token by token at "
                             "build time.",
               shorts=[])
    for num in (1, 2, 3):
        k = (n, num)
        s = C.SS.SHORTS[k]
        out["shorts"].append(dict(
            n=num, title=s["label"], territory=s["territory"],
            payoff_card=s["card"],
            words=C.SS.words(k),
            estimated_seconds_at_165=round(C.SS.seconds(k, 165), 1),
            estimated_seconds_at_150=round(C.SS.seconds(k, 150), 1),
            duration_is_estimate_until_recorded=True,
            asks=C.SS.actions(k),
            standalone=True,
            opening=s["opening"], cut=s["cut"]))
    return out

if __name__ == "__main__":
    for n in (1, 2, 3):
        print("V%d  riverside %d lines  editor %d lines  shorts %d"
              % (n, riverside_prompt(n).count("\n"), editor_notes(n).count("\n"),
                 len(shorts_manifest(n)["shorts"])))
