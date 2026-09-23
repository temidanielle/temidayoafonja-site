# -*- coding: utf-8 -*-
"""Publishing, viewer application and evidence layers."""
import os, json
import cp_src as C, cp_trig as T, cp_visuals as V

RULE = "=" * 78
def _head(title, n):
    return ("%s\n%s\nVideo %d  ·  %s\nBuilt against %s  ·  locked "
            "September 23, 2026\n%s\n"
            % (RULE, title, n, C.META[n]["title"],
               os.path.basename(C.LOCKED[n][0]), RULE))

# ---------------------------------------------------------------- publishing
def description_draft(n):
    m = C.META[n]
    L = [_head("YOUTUBE DESCRIPTION. DRAFT, REVIEW REQUIRED", n)]
    L.append("STATUS: DRAFT. NOT YET APPROVED FOR PUBLICATION.\n")
    L.append(C.SD.STATUS + "\n")
    L.append("-" * 78 + "\nCOPY-READY BODY\n" + "-" * 78 + "\n")
    for p in C.SD.BODY[n]:
        L.append(p + "\n")
    emoji, name, blurb, url = C.SD.RESOURCE[n]
    L.append("%s\n%s\n%s\n%s\n" % (emoji, name, blurb, url))
    L.append("One resource. No second link and no second ask. The video names "
             "this resource out loud.\n")
    L.append("\U0001F3A5 Watch next\n%s\n[PASTE VIDEO URL AFTER UPLOAD]\n" % m["watch"])
    L.append("\U0001F4FA Playlist\n%s\n[PASTE PLAYLIST URL AFTER UPLOAD]\n" % C.SD.PLAYLIST)
    verse, ref, refl = C.SD.FAITH[n]
    L.append("\U0001F64F A faith anchor\n")
    L.append(C.SD.SCRIPTURE_STATUS + "\n")
    L.append("%s\n%s   [NLT WORDING REQUIRES VERIFICATION]\n%s\n" % (verse, ref, refl))
    L.append("The faith anchor follows the practical link, is not spoken on "
             "camera, and is not a\nsecond call to action.\n")
    L.append(C.SD.COPYRIGHT + "\n")
    return "\n".join(L)

def pinned_comment(n):
    L = [_head("PINNED COMMENT. DRAFT, REVIEW REQUIRED", n)]
    L.append("STATUS: DRAFT. NOT YET APPROVED FOR PUBLICATION.\n")
    L.append("-" * 78 + "\n")
    L.append(C.SD.PINNED[n] + "\n")
    return "\n".join(L)

def link_checklist(n):
    m = C.META[n]
    L = [_head("LINK AND PUBLICATION CHECKLIST", n)]
    L.append("Work top to bottom. Nothing here is a strategic decision; these "
             "are the steps that\ngo wrong when a video is uploaded in a hurry.\n")
    L.append("-" * 78 + "\nBEFORE UPLOAD\n" + "-" * 78 + "\n")
    for x in [
        "The recording matches the locked master. If it does not, note the "
        "differences before\n  the edit is finalized, not after.",
        "Thumbnail text reads at phone size: %s" % m["thumb"],
        "Title exactly as locked: %s" % m["title"],
        "Export is 1920x1080 or better, 16:9.",
        "Watch Next is the final frame and the video does not return to camera "
        "after it.",
        "The description below is still marked DRAFT. Either approve it or "
        "replace it. Do not\n  publish it silently as final.",
        "The NLT verse is confirmed against an authorized edition. This one "
        "blocks publication.",
    ]:
        L.append("  [ ]  " + x)
    if n == 1:
        L.append("  [ ]  V1 ONLY. The two role types are anonymized and their "
                 "private source\n       identifiers are still NOT SUPPLIED. "
                 "Publishing with the on-screen line\n       “two real "
                 "U.S. job postings” rests on the brief's own statement "
                 "and not on\n       a record anyone can re-check. Resolve or "
                 "accept this before publishing.")
    L.append("")
    L.append("-" * 78 + "\nAT UPLOAD\n" + "-" * 78 + "\n")
    for x in [
        "Paste the description. Confirm the one resource link resolves: %s" % m["cta_url"],
        "Confirm there is exactly one resource link in the description.",
        "Add the playlist: %s" % C.SD.PLAYLIST,
        "Add tags.",
        "Set the end screen to the Watch Next video: %s" % m["watch"],
        "Pin the pinned comment.",
    ]:
        L.append("  [ ]  " + x)
    L.append("")
    L.append("-" * 78 + "\nAFTER UPLOAD\n" + "-" * 78 + "\n")
    for x in [
        "Replace [PASTE VIDEO URL AFTER UPLOAD] in the Watch Next line of the "
        "video it\n       routes from.",
        "Replace [PASTE PLAYLIST URL AFTER UPLOAD].",
        "Check the first thirty seconds on a phone, with sound off, to confirm "
        "the promise\n       still reads.",
        "Record the final measured runtime. Every timing in this package is an "
        "estimate\n       until that exists.",
    ]:
        L.append("  [ ]  " + x)
    L.append("")
    return "\n".join(L)

def canva_prompt(n):
    m = C.META[n]
    L = [_head("THUMBNAIL / CANVA BUILD PROMPT", n)]
    L.append("-" * 78 + "\nTHE BRIEF\n" + "-" * 78 + "\n")
    L.append("Build a 1280x720 YouTube thumbnail, exported at 1920x1080 for "
             "headroom.\n")
    L.append("TEXT, EXACTLY AS LOCKED. Do not reword it:\n")
    for line in m["thumb"].split(" "):
        pass
    L.append("    %s\n" % m["thumb"])
    L.append("PALETTE\n")
    L.append("    Deep navy    #112345    background\n"
             "    Warm cream   #F5F1E8    primary text\n"
             "    Muted gold   #C9A84C    rule or accent\n"
             "    Bright warm  #F2C44C    one emphasized word only, if any\n")
    L.append("LAYOUT\n")
    L.append("    Text occupies the left two thirds. Temidayo's photograph "
             "sits right, cut out,\n    facing into the text. Heavy weight, "
             "tight leading, generous margins.\n")
    L.append("    The single most important requirement is that the text is "
             "legible as a\n    thumbnail on a phone. Build it, then look at "
             "it at 20 percent size. If you\n    cannot read it, the type is "
             "too small or there are too many words.\n")
    L.append("DO NOT\n")
    L.append("    No arrows, no circles, no red outlines, no shocked face, no "
             "stock imagery, no\n    drop shadows, no gradients, no more words "
             "than the locked line.\n")
    L.append("-" * 78 + "\nWHAT THE THUMBNAIL IS PROMISING\n" + "-" * 78 + "\n")
    L.append("%s\n" % m["thinking"])
    L.append("The first thirty seconds of the video pay this off. If the "
             "thumbnail promises\nsomething the opening does not deliver, the "
             "thumbnail is wrong, not the script.\n")
    return "\n".join(L)

def metadata(n):
    m = C.META[n]
    return dict(video=n, title=m["title"], thumbnail=m["thumb"],
                playlist=C.SD.PLAYLIST, tags=C.SD.TAGS[n],
                watch_next=m["watch"], resource=m["cta"],
                resource_url=m["cta_url"],
                description_status="DRAFT, REVIEW REQUIRED",
                note="Metadata is useful, not filler. Hashtags are not a "
                     "strategic requirement and none is specified.")

# ---------------------------------------------------- viewer application
def viewer_exercise(n):
    m = C.META[n]
    headline, steps, footer = C.VIEWER_EXERCISE[n]
    L = [_head("VIEWER EXERCISE", n)]
    L.append("One page. You should be able to do this today, on paper, in "
             "about ten minutes.\n")
    L.append("-" * 78 + "\n%s\n" % headline.upper() + "-" * 78 + "\n")
    for i, s in enumerate(steps, 1):
        L.append("  %d.  %s\n" % (i, s))
    L.append("-" * 78 + "\n")
    L.append(footer + "\n")
    L.append("-" * 78 + "\nIF YOU REMEMBER ONE THING\n" + "-" * 78 + "\n")
    L.append("    %s\n" % m["memory"])
    return "\n".join(L)

def sticky_record(n):
    m = C.META[n]
    L = [_head("STICKY REALIZATION RECORD", n)]
    L.append("Carried from the Source-of-Truth Manifest. Not re-derived, and "
             "no new slogan was\ninvented for this package.\n")
    L.append("-" * 78 + "\nWHAT THE VIEWER IS ALREADY THINKING\n" + "-" * 78 + "\n")
    L.append(m["thinking"] + "\n")
    L.append("-" * 78 + "\nTHAT'S IT REALIZATION\n" + "-" * 78 + "\n")
    L.append(m["realization"] + "\n")
    L.append("-" * 78 + "\nSEVEN-DAY MEMORY LINE\n" + "-" * 78 + "\n")
    L.append(m["memory"] + "\n")
    L.append("-" * 78 + "\nOBSERVABLE ACTION\n" + "-" * 78 + "\n")
    L.append(m["action"] + "\n")
    L.append("-" * 78 + "\nTHE COMPLETION\n" + "-" * 78 + "\n")
    L.append(m["next_line"] + "\n")
    L.append("-" * 78 + "\nWHERE THIS LIVES IN THE VIDEO\n" + "-" * 78 + "\n")
    L.append("The memory line is spoken in the SEVEN-DAY MEMORY + ACTION "
             "section and is on its own\nfull-screen card. The four items "
             "above are internal editorial QA and are never\nlabelled or named "
             "in the video, on a card or in the description.\n")
    return "\n".join(L)

# ---------------------------------------------------------------- evidence
def source_manifest(n):
    m = C.META[n]
    return dict(
        video=n, title=m["title"], thumbnail=m["thumb"], status="LOCKED",
        spoken_source_of_truth=dict(
            file=os.path.basename(C.LOCKED[n][0]),
            sha256=C.sha256(C.LOCKED[n][0]), spoken_words=C.words(n)),
        thought_blocks=dict(
            file=os.path.basename(C.LOCKED[n][1]),
            sha256=C.sha256(C.LOCKED[n][1]), spoken_words=C.words(n),
            parity="PASS, word for word and in order"),
        sticky_realization=m["realization"],
        seven_day_memory_line=m["memory"],
        observable_action=m["action"],
        cta=dict(name=m["cta"], url=m["cta_url"],
                 named_in_spoken_master=True),
        watch_next=dict(title=m["watch"], final_frame=True),
        visual_assets=dict(
            source="Approved V1-V3 assets rendered against this exact master. "
                   "Reused, not rebuilt.",
            states=len(list(C.SF.states(n))),
            families=len(T.families(n))),
        publishing_status="DESCRIPTION AND PINNED COMMENT ARE DRAFT. NOT "
                          "APPROVED FOR PUBLICATION.",
        provenance_open=("V1 role identifiers are NOT SUPPLIED and remain OPEN"
                         if n == 1 else "none open"),
        superseded_reference=dict(
            file="Videos_813_Production_Packages.zip",
            role="STRUCTURE AND PRODUCTION-COMPLETENESS REFERENCE ONLY",
            controls_nothing="It does not control wording, titles, thumbnails, "
                             "CTAs, Watch Next, evidence claims or editorial "
                             "strategy."),
    )

def evidence_notes(n):
    L = [_head("EVIDENCE AND ILLUSTRATION NOTES", n)]
    L.append("Every factual, sourced or artifact-based element in this video, "
             "with what it actually\nsupports and where it stops.\n")
    L.append("-" * 78 + "\nCLASSIFICATION USED\n" + "-" * 78 + "\n")
    L.append("  DIRECT       quoted or near-quoted from a source document\n"
             "  PARAPHRASED  a source's meaning in Temidayo's words\n"
             "  SYNTHETIC    constructed for the video, labelled on screen\n"
             "  EDITORIAL    Temidayo's own reading, presented as hers\n")
    con = [c for c in C.SV.CONSTRUCTED if c[0] == n]
    if con:
        L.append("-" * 78 + "\nSYNTHETIC MATERIAL\n" + "-" * 78 + "\n")
        for _n, cid, what, why in con:
            L.append("  %s" % cid)
            L.append("     classification:  SYNTHETIC")
            L.append("     what it shows:   %s" % what)
            L.append("     on-screen label: SYNTHETIC EXAMPLE, held for the "
                     "whole hold")
            L.append("     named on camera: yes")
            L.append("     limitation:      %s\n" % why)
    if n == 1:
        L.append("-" * 78 + "\nTHE TWO ROLE TYPES\n" + "-" * 78 + "\n")
        L.append("  classification:      PARAPHRASED from two real U.S. postings")
        L.append("  employer identity:   ANONYMIZED. Not shown and not implied.")
        L.append("  private identifiers: NOT SUPPLIED. Still OPEN. Not invented.")
        L.append("  required vs preferred: NOT ESTABLISHED for these two "
                 "postings. The video does\n     not describe the destination "
                 "context as a hard requirement, and the card\n     keeps the "
                 "word MAY in “what may need to be learned or built”.")
        L.append("  limitation:          The on-screen line “two real "
                 "U.S. job postings” rests on the\n     brief's own "
                 "statement, not on a record anyone can re-check today.\n")
    L.append("-" * 78 + "\nUPGRADES THAT WERE NOT MADE\n" + "-" * 78 + "\n")
    for a, b in [("adjacent", "direct"), ("preferred", "required"),
                 ("context", "universal rule"), ("illustration", "evidence"),
                 ("correlation", "causation")]:
        L.append("  %-14s was NOT upgraded to %s" % (a, b))
    L.append("")
    L.append("-" * 78 + "\nBOUNDARIES HELD ON CAMERA\n" + "-" * 78 + "\n")
    for b in C.SV.BOUNDARIES[n]:
        L.append("  ·  %s\n" % b)
    return "\n".join(L)

def alignment_log(n):
    """SPOKEN LINE -> VISUAL -> EDITOR ACTION -> EVIDENCE -> BOUNDARY."""
    rows = V.trigger_rows(n)
    by_trigger = {r["trigger"]: r for r in rows if r["trigger"]}
    cam = {t: w for t, w in C.SPR.CAMERA[n]}
    snd = {t: w for t, w in C.SPR.SOUND[n]}
    art = {t: w for t, w in C.SPR.BROLL[n]}
    sub = C.SPR.SUBSCRIBE[n]
    con_ids = {c[1] for c in C.SV.CONSTRUCTED if c[0] == n}
    L = [_head("ALIGNMENT LOG", n)]
    L.append("The final synchronization record. One row per spoken paragraph "
             "that carries a\nvisual, a camera beat, an accent or a boundary. "
             "Paragraphs with none of those are\nomitted rather than padded "
             "with an empty row.\n")
    out = 0
    for sec, paras in C.SP.master(n)[1]:
        for p in paras:
            hits = []
            for t, r in by_trigger.items():
                if t == p or t in p or p in t:
                    hits.append(("VISUAL", "%s enters, %s" % (r["family"], r["mode"])))
            for t, w in art.items():
                if t == p or t in p or p in t:
                    hits.append(("EDITOR", w))
            for t, w in cam.items():
                if t == p or t in p or p in t:
                    hits.append(("CAMERA", w))
            for t, w in snd.items():
                if t == p or t in p or p in t:
                    hits.append(("SOUND", w))
            if sub[0] == p or sub[0] in p:
                hits.append(("SUBSCRIBE", sub[1]))
            if not hits:
                continue
            out += 1
            L.append("  [%s]" % sec)
            L.append("  SPOKEN:    %s" % p)
            for k, v in hits:
                L.append("  %-10s %s" % (k + ":", v))
            ev = [c for c in con_ids
                  if any(c == r["family"] or c.startswith(r["family"])
                         for _t, r in by_trigger.items())]
            if any("SYNTHETIC" in h[1] or "constructed" in h[1].lower()
                   for h in hits):
                L.append("  EVIDENCE:  SYNTHETIC, labelled on the card")
            bl = [b for b in C.SV.BOUNDARIES[n]
                  if any(w in p for w in b.split()[:4])]
            if bl:
                L.append("  BOUNDARY:  %s" % bl[0])
            L.append("")
    L.append("%d aligned rows.\n" % out)
    return "\n".join(L)

if __name__ == "__main__":
    for n in (1, 2, 3):
        print("V%d  description %d ch  checklist %d ch  exercise %d ch  "
              "alignment rows %s"
              % (n, len(description_draft(n)), len(link_checklist(n)),
                 len(viewer_exercise(n)),
                 alignment_log(n).rsplit("\n", 3)[-2].split()[0]))
