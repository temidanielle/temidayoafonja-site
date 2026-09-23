# -*- coding: utf-8 -*-
"""Recording Run of Show and Estimated Speech Timing.

The Run of Show is not another script. It tells Temidayo how to record the
locked one. Editor instructions stay out of the thought-block copy, which is
used exactly as locked.
"""
import os
import cp_src as C, cp_trig as T, cp_visuals as V

RULE = "=" * 78
def _head(title, n):
    return ("%s\n%s\nVideo %d  ·  %s\nBuilt against %s  ·  locked "
            "September 23, 2026\n%s\n"
            % (RULE, title, n, C.META[n]["title"],
               os.path.basename(C.LOCKED[n][0]), RULE))

def run_of_show(n):
    m = C.META[n]
    rows = V.trigger_rows(n)
    by_fam = {}
    for r in rows:
        by_fam.setdefault(r["family"], r)
    cam = {t: w for t, w in C.SPR.CAMERA[n]}
    L = [_head("RECORDING RUN OF SHOW", n)]
    L.append("This is not a script. It is how to record the locked one.\n")
    L.append("Thumbnail        %s" % m["thumb"])
    L.append("Spoken words     %d" % C.words(n))
    L.append("Speech estimate  %s at 145 wpm to %s at 130 wpm. ESTIMATE, not a "
             "measurement." % (C.runtime(n, 145), C.runtime(n, 130)))
    L.append("Resource         %s   %s" % (m["cta"], m["cta_url"]))
    L.append("Watch Next       %s" % m["watch"])
    L.append("Export           1920x1080 minimum, 16:9\n")
    L.append("-" * 78 + "\nBEFORE YOU PRESS RECORD\n" + "-" * 78 + "\n")
    for x in ["Horizontal. Confirm 16:9 before the first take.",
              "The opening is locked. Start on the exact first line and do not "
              "warm up into it.",
              "Say the first line once cold to set level, then start properly.",
              "One resource route in this video: %s. No second product mention "
              "and no extra\n     spoken CTA." % m["cta"],
              "Read from the thought-block copy. It carries the spoken words "
              "and nothing else.\n     Every editor instruction lives in this "
              "file, not in that one."]:
        L.append("  ·  %s" % x)
    L.append("")
    L.append("-" * 78 + "\nTHE RECORDING RHYTHM\n" + "-" * 78 + "\n")
    L.append("  read silently  →  lens  →  deliver  →  stop  "
             "→  reset  →  advance\n")
    L.append("  One block at a time. Stop fully between blocks. Reset posture "
             "and hands. The edit\n  needs the gap; it does not need you to "
             "carry momentum across blocks.\n")
    L.append("-" * 78 + "\nBEAT BY BEAT\n" + "-" * 78 + "\n")
    blocks = C.SP.blocks(n)
    idx = 0
    for sec, bs in blocks:
        L.append("  [%s]   %d block%s" % (sec, len(bs), "" if len(bs) == 1 else "s"))
        fam = None
        for f, r in by_fam.items():
            t = r["trigger"]
            if t and any(t == b or t in b or b in t for b in bs):
                fam = f
                break
        for b in bs:
            idx += 1
            marks = []
            for f, r in by_fam.items():
                t = r["trigger"]
                if t and (t == b or t in b or b in t):
                    marks.append("FULL SCREEN: %s enters here" % f)
            for t, w in cam.items():
                if t == b or t in b or b in t:
                    marks.append("CAMERA EMPHASIS: %s" % w)
            if C.SPR.SUBSCRIBE[n][0] in b:
                marks.append("SUBSCRIBE lower-third, silent, four seconds")
            if marks:
                L.append("     BLOCK %02d  %s" % (idx, b[:64] + ("..." if len(b) > 64 else "")))
                for mk in marks:
                    L.append("               → %s" % mk)
        if fam:
            L.append("     after this section, return to camera unless the "
                     "next trigger has arrived.")
        L.append("")
    L.append("-" * 78 + "\nTHE TWO TRANSITIONS THAT MATTER\n" + "-" * 78 + "\n")
    L.append("  CTA        on “%s”" % T.TRIGGER[n]["V%d_%s_CTA" % (n, {1:"10",2:"11",3:"12"}[n])])
    L.append("             Full screen. Deliver it as information, not as a "
             "sell. One ask.\n")
    L.append("  WATCH NEXT on “%s”" % T.TRIGGER[n][C.SPR.WATCH_CARD[n]])
    L.append("             Full screen and FINAL. Do not record anything after "
             "this line. Never\n             return to camera.\n")
    L.append("-" * 78 + "\nIF A TAKE GOES WRONG\n" + "-" * 78 + "\n")
    L.append("  Stop, reset, and take the whole block again. Do not patch "
             "mid-block. The block is\n  the unit because the edit cuts on "
             "block boundaries.\n")
    return "\n".join(L)

def timing(n):
    m = C.META[n]
    L = [_head("ESTIMATED SPEECH TIMING", n)]
    L.append("RUNTIME: ESTIMATE ONLY, NOT A MEASUREMENT\n")
    L.append("Arithmetic on the locked script's spoken word count at 130 to "
             "145 words per minute,\nthe established band. Spoken words are "
             "counted separately from section labels and\nproduction "
             "scaffolding.\n")
    L.append("It is speech only. It excludes holds on full-screen graphics and "
             "every edit decision.\nNarration continuing underneath a graphic "
             "OVERLAPS that visual; do not add a visual's\nduration to speech "
             "time.\n")
    L.append("Final timing and YouTube chapters come from the actual final "
             "export.\n")
    L.append("-" * 78 + "\nTHE NUMBERS\n" + "-" * 78 + "\n")
    L.append("  spoken words          %d" % C.words(n))
    L.append("  at 145 wpm            %s" % C.runtime(n, 145))
    L.append("  at 130 wpm            %s" % C.runtime(n, 130))
    L.append("  working estimate      %s to %s\n" % (C.runtime(n, 145), C.runtime(n, 130)))
    L.append("-" * 78 + "\nCUMULATIVE BY SECTION, AT 145 WPM AND 130 WPM\n"
             + "-" * 78 + "\n")
    cum = 0
    def mmss(w, rate):
        return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))
    for sec, paras in C.SP.master(n)[1]:
        w = sum(len(p.split()) for p in paras)
        L.append("  %-34s %4d w    starts %s / %s"
                 % (sec, w, mmss(cum, 145), mmss(cum, 130)))
        cum += w
    L.append("  %-34s %4d w    ends   %s / %s\n"
             % ("TOTAL", cum, mmss(cum, 145), mmss(cum, 130)))
    L.append("-" * 78 + "\nLIKELY SLIDE-ENTRY WINDOWS\n" + "-" * 78 + "\n")
    L.append("Each window is where that family's spoken trigger falls in the "
             "cumulative count.\nA window, not a timecode.\n")
    ms = C.SP.master_sentences(n)
    running = 0
    pos = {}
    for s in ms:
        pos[s] = running
        running += len(s.split())
    for fam in T.families(n):
        t = T.TRIGGER[n][fam]
        w = None
        for s, p in pos.items():
            if s == t or t.startswith(s) or s in t:
                w = p
                break
        if w is None:
            joined_words = " ".join(ms).split()
            tw = t.split()
            for i in range(len(joined_words) - len(tw) + 1):
                if joined_words[i:i + len(tw)] == tw:
                    w = i
                    break
        L.append("  %-34s around %s / %s" % (fam, mmss(w or 0, 145), mmss(w or 0, 130)))
    L.append("")
    L.append("-" * 78 + "\nCTA AND WATCH NEXT WINDOWS\n" + "-" * 78 + "\n")
    cta_fam = "V%d_%s_CTA" % (n, {1: "10", 2: "11", 3: "12"}[n])
    for label, fam in (("CTA", cta_fam), ("WATCH NEXT", C.SPR.WATCH_CARD[n])):
        t = T.TRIGGER[n][fam]
        jw = " ".join(ms).split()
        tw = t.split()
        w = next((i for i in range(len(jw) - len(tw) + 1)
                  if jw[i:i + len(tw)] == tw), 0)
        L.append("  %-12s around %s / %s" % (label, mmss(w, 145), mmss(w, 130)))
    L.append("")
    L.append("-" * 78 + "\nTITLE PROMISE\n" + "-" * 78 + "\n")
    if "10 Minutes" in m["title"] or "10 minutes" in m["title"]:
        L.append("  This title promises a runtime. Preserve it. The estimate "
                 "above sits inside it.\n")
    else:
        L.append("  This title makes no runtime promise, so no runtime has to "
                 "be hit. Do not pad the\n  script or slow the delivery to "
                 "reach a number.\n")
    return "\n".join(L)

if __name__ == "__main__":
    for n in (1, 2, 3):
        print("V%d  run of show %d lines  timing %d lines  %s to %s"
              % (n, run_of_show(n).count("\n"), timing(n).count("\n"),
                 C.runtime(n, 145), C.runtime(n, 130)))
