# -*- coding: utf-8 -*-
"""Visual operational layer: reference deck, asset spec, trigger map, reveal map.

The slide PNGs themselves are NOT rebuilt. They are the approved V1-V3 assets
already rendered against these exact masters, reused as the brief requires.
What is built here is the operational layer the old packages carried and the
current archive did not: a deck an editor can scrub, a machine-readable asset
specification, and the two maps that tell an editor exactly when each asset
appears and what it does.
"""
import os, json, re
from pptx import Presentation
from pptx.util import Emu
import cp_src as C

W_EMU, H_EMU = Emu(12192000), Emu(6858000)          # 16:9 at 1920x1080

def states(n):
    return [(fam, name, note) for fam, name, _d, note in C.SF.states(n)]

def png(n, name):
    return os.path.join(C.VIS % n, name + ".png")

def reference_deck(n, path):
    """One slide per state, full bleed, with the pacing note in the notes pane."""
    prs = Presentation()
    prs.slide_width, prs.slide_height = W_EMU, H_EMU
    blank = prs.slide_layouts[6]
    for fam, name, note in states(n):
        p = png(n, name)
        if not os.path.exists(p):
            continue
        s = prs.slides.add_slide(blank)
        s.shapes.add_picture(p, 0, 0, width=W_EMU, height=H_EMU)
        s.notes_slide.notes_text_frame.text = "%s\n\n%s" % (name, note)
    prs.save(path)
    return len(prs.slides.__iter__.__self__._sldIdLst)

def _mode(name):
    if name.endswith("_WATCH_NEXT"):
        return "TRUE FULL SCREEN, FINAL FRAME"
    if name.endswith("_CTA"):
        return "TRUE FULL SCREEN"
    return "TRUE FULL SCREEN"

def trigger_rows(n):
    """(asset, mode, exact spoken trigger, in the locked script, exit).

    The family's entry trigger comes from cp_trig, where every family is mapped
    to an exact sentence from this master and each mapping is verified. States
    after the first in a family are progressive reveals under the same
    narration, so they are marked as such rather than being given an invented
    trigger of their own.
    """
    import cp_trig as T
    joined = " ".join(C.SP.master_sentences(n))
    art = {t: w for t, w in C.SPR.BROLL[n]}
    out, seen = [], set()
    for fam, name, note in states(n):
        first = fam not in seen
        seen.add(fam)
        trig = T.TRIGGER[n][fam] if first else None
        direction = None
        if trig:
            for t, w in C.SPR.BROLL[n]:
                if t == trig or trig in t or t in trig:
                    direction = w
                    break
        out.append(dict(asset=name, family=fam, mode=_mode(name),
                        trigger=trig,
                        trigger_in_script=(trig in joined) if trig else None,
                        direction=direction, note=note,
                        reveal=(not first)))
    return out

def asset_spec(n):
    rows = trigger_rows(n)
    return dict(
        video=n,
        title=C.META[n]["title"],
        thumbnail=C.META[n]["thumb"],
        status="Approved assets rendered against this exact locked master and "
               "reused here. Not rebuilt for this package.",
        built_from=os.path.basename(C.LOCKED[n][0]),
        source_sha256=C.sha256(C.LOCKED[n][0]),
        spoken_words=C.words(n),
        canvas=[1920, 1080],
        palette=dict(navy="#112345", cream="#F5F1E8", gold="#C9A84C",
                     yellow="#F2C44C"),
        rules=["Camera-led, not camera-only.",
               "Substantive teaching and comparisons are TRUE FULL SCREEN.",
               "Meaningful artifact and B-roll moments are TRUE FULL SCREEN.",
               "CTA is full screen.",
               "Watch Next is full screen and is the final frame.",
               "Never return to camera after Watch Next.",
               "No decorative stock, no constant effects, no burned-in "
               "long-form transcript captions."],
        states=[dict(id=r["asset"], family=r["family"], mode=r["mode"],
                     trigger=r["trigger"],
                     trigger_in_locked_script=r["trigger_in_script"],
                     purpose=r["note"]) for r in rows],
        cta_card="V%d_%s_CTA" % (n, {1: "10", 2: "11", 3: "12"}[n]),
        watch_next_card=C.SPR.WATCH_CARD[n],
        constructed_examples=[c[1] for c in C.SV.CONSTRUCTED if c[0] == n],
        constructed_label="SYNTHETIC EXAMPLE",
    )

RULE = "=" * 78
def _head(title, n):
    return ("%s\n%s\nVideo %d  ·  %s\nBuilt against %s  ·  locked "
            "September 23, 2026\n%s\n"
            % (RULE, title, n, C.META[n]["title"],
               os.path.basename(C.LOCKED[n][0]), RULE))

def trigger_map(n):
    L = [_head("CURRENT-SCRIPT TRIGGER MAP", n)]
    L.append("Every trigger below is an exact sentence, or an exact "
             "consecutive run of sentences,\nfrom the locked master. The build "
             "verifies this and fails if one is not found, so no\ncard can be "
             "cued by a line that is not in the script.\n")
    L.append("SPOKEN TRIGGERS cue a visual. A state marked CONTINUES has no "
             "trigger of its own\nand builds on the state before it while the "
             "narration keeps running.\n")
    L.append("-" * 78 + "\nSPOKEN TRIGGERS\n" + "-" * 78 + "\n")
    for r in trigger_rows(n):
        L.append("  %s" % r["asset"])
        L.append("        mode:    %s" % r["mode"])
        if r["trigger"]:
            L.append("        cue:     “%s”" % r["trigger"])
            L.append("        in the locked script: %s"
                     % ("YES" if r["trigger_in_script"] else "NO"))
            L.append("        action:  %s" % r["direction"])
        else:
            L.append("        cue:     CONTINUES from the previous state.")
        L.append("        purpose: %s" % r["note"])
        L.append("        exit:    %s" % (
            "This is the final frame. Never return to camera."
            if r["asset"].endswith("_WATCH_NEXT")
            else "Hold while the narration runs, then return to camera when "
                 "the next family's trigger arrives."))
        L.append("")
    L.append("-" * 78 + "\nCAMERA-EMPHASIS BEATS, NOT VISUAL TRIGGERS\n" + "-" * 78 + "\n")
    for t, w in C.SPR.CAMERA[n]:
        L.append("  cue:     “%s”" % t)
        L.append("  action:  %s\n" % w)
    L.append("-" * 78 + "\nSUBSCRIBE CUE\n" + "-" * 78 + "\n")
    L.append("  cue:     “%s”" % C.SPR.SUBSCRIBE[n][0])
    L.append("  action:  %s\n" % C.SPR.SUBSCRIBE[n][1])
    return "\n".join(L)

def reveal_map(n):
    L = [_head("VISUAL AND MOTION / REVEAL MAP", n)]
    rows = trigger_rows(n)
    fams = []
    for r in rows:
        if r["family"] not in fams:
            fams.append(r["family"])
    L.append("%d full-screen states across %d families. These are reference "
             "frames for the\nedit, not one slide per paragraph.\n"
             % (len(rows), len(fams)))
    L.append("-" * 78 + "\nTRUE FULL-SCREEN SCENES\n" + "-" * 78 + "\n")
    L.append("Teaching comparisons, the artifact moments, the seven-day memory "
             "card, the CTA and\nWatch Next fill the entire canvas. Temidayo is "
             "hidden visually during those scenes\nwhile her voice continues.\n")
    L.append("-" * 78 + "\nPER FAMILY\n" + "-" * 78 + "\n")
    for fam in fams:
        group = [r for r in rows if r["family"] == fam]
        L.append("  %s   (%d state%s)" % (fam, len(group),
                                          "" if len(group) == 1 else "s"))
        first = group[0]
        L.append("     entry:            %s" % (
            "on “%s”" % first["trigger"] if first["trigger"]
            else "continues from the state before it"))
        if len(group) > 1:
            L.append("     progressive:      YES, %d states in order:" % len(group))
            for g in group:
                L.append("                         %s  |  %s" % (g["asset"], g["note"]))
        else:
            L.append("     progressive:      no, single state")
        L.append("     Temidayo visible: no, this is true full screen")
        L.append("     return to camera: %s" % (
            "never, this is the final frame"
            if fam.endswith("WATCH_NEXT") else
            "after the last state in this family"))
        L.append("     motion:           entry only. No drift, no continuous "
                 "zoom, no parallax.")
        acc = [w for t, w in C.SPR.SOUND[n]
               if first["trigger"] and (t in first["trigger"] or first["trigger"] in t)]
        L.append("     sound accent:     %s" % (acc[0] if acc else "none on entry"))
        L.append("")
    L.append("-" * 78 + "\nMOTION RESTRAINT\n" + "-" * 78 + "\n")
    L.append("Do not create movement because the software can. A reveal exists "
             "to stop two ideas\ncompeting while one is being taught. If a "
             "state does not do that, it should not move.\n")
    return "\n".join(L)

if __name__ == "__main__":
    for n in (1, 2, 3):
        rows = trigger_rows(n)
        cued = [r for r in rows if r["trigger"]]
        bad = [r["asset"] for r in cued if not r["trigger_in_script"]]
        print("V%d  %d states, %d families each cued by an exact spoken "
              "trigger, %d progressive reveals"
              % (n, len(rows), len(cued), len(rows) - len(cued)))
        print("    triggers not found in the locked script:", bad or "none")
