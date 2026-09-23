# -*- coding: utf-8 -*-
"""One interface over two very different approved cue sources.

V4 to V11  the resolved event list in V4-V11_SYNC/build/events.py. Every span,
           activation word, entry and exit phrase in it is already checked
           against the reconciled master and its own verify() is clean. It is
           reused, not re-derived.
V12 to V14 the production modules of the locked pack (V12) and the public
           employer anonymization patch (V13, V14), which the Source-of-Truth
           Manifest identifies as superseding the locked pack for those two.

Nothing editorial is decided here. Titles, thumbnails, sticky realizations,
observable actions, CTAs and Watch Next are carried from the manifest.
"""
import os, sys, hashlib, importlib
DELIV = "/home/user/temidayoafonja-site/deliverables/"
for p in ("V4-V11_SYNC/build", "V12-V14_LOCKED/build", "V13-V14_ANON/build",
          "V1-V14_FINAL_ARCHIVE/build", "V1-V3_COMPLETE_PACKAGES/build"):
    sys.path.append(DELIV + p)

import ar_sources as AR        # the locked master and blocks for every video
import ar_parity as AP
import events as EV            # V4 to V11
import p4_production as P4     # V12
import p5_production as P5     # V13 and V14
import p4_script12, p5_script13, p5_script14

VIDEOS = tuple(range(4, 15))
SYNC = tuple(range(4, 12))
BUILT = (12, 13, 14)

PKG = (DELIV + "V4-V11_SYNC/PACKAGES/NEW_V%02d_Synchronized_Production_Package")

def locked(n):
    return AR.SRC[n][0], AR.SRC[n][1]

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def shape(n):
    return AR.SRC[n][2]

def spoken(n):
    return AP.spoken(locked(n)[0], shape(n), "master")

def words(n):
    return len(" ".join(spoken(n)).split())

def runtime(n, rate):
    w = words(n)
    return "%d:%02d" % (int(w / rate), round((w / rate % 1) * 60))

import re
def sentences(p):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", p.strip()) if s.strip()]

def master_sentences(n):
    return [s for p in spoken(n) for s in sentences(p)]

def _mod(n):
    return P4 if n == 12 else P5

# ------------------------------------------------------------------ families
def families(n):
    """[(family_id, exact spoken trigger, mode, [state ids], on-card label)]"""
    out = []
    if n in SYNC:
        for e in EV.events(n):
            if e["mode"] != "FULL SCREEN" or not e.get("family"):
                continue
            sts = [s["name"] for s in (e.get("states") or [])] or [e["family"]]
            out.append(dict(family=e["family"], trigger=e["enter"],
                            leave=e.get("leave"), ret=e.get("ret"),
                            mode="TRUE FULL SCREEN", states=sts,
                            display=e.get("display"), note=e.get("note"),
                            eid=e["eid"], section=e.get("section")))
    else:
        # V12 to V14 card copy is written as compressed on-screen labels, not
        # as verbatim speech, so no inference from card text to spoken sentence
        # can work. The triggers are stated explicitly in ap_trig and verified.
        import ap_trig as TR
        M = _mod(n)
        for cid, headline, lines, label in M.FULLSCREEN[n]:
            out.append(dict(family=cid, trigger=TR.TRIGGER[n][cid],
                            leave=None, ret=None, mode="TRUE FULL SCREEN",
                            states=[cid], display=headline, note=None,
                            eid=cid, section=None, label=label, lines=lines))
    return out

def camera(n):
    """Deliberate camera moments.

    For V4 to V11 these are the CAMERA-mode events in the approved event list.
    There are two or three per video, not the three to five the guide suggests
    for a newly built script, because those videos deliberately put most of
    their emphasis into full-screen inserts and the camera map is an approved
    artifact. The count is reported as it is rather than padded to reach a
    guide, and the approved Camera and Full-Screen Map ships alongside it.
    """
    if n in SYNC:
        return [(e["enter"], e.get("note") or
                 "Camera. %s" % (e.get("display") or "Hold."))
                for e in EV.events(n) if e["mode"] == "CAMERA"]
    return list(_mod(n).CAMERA[n])

def broll(n):
    if n in SYNC:
        return [(e["enter"], e.get("note") or "Artifact moment.")
                for e in EV.events(n)
                if e["mode"] == "FULL SCREEN" and e["kind"] == "TEACHING"]
    return list(_mod(n).BROLL[n])

def sound(n):
    if n in SYNC:
        return [(e["enter"], e["sound"]) for e in EV.events(n) if e.get("sound")]
    return list(_mod(n).SOUND[n])

def subscribe(n):
    """One quiet cue, after value and clear of boundaries and the ending.

    Neither source carries a Subscribe cue, so one is placed here: the first
    sentence of the paragraph that sits closest to 60 per cent of the way
    through the spoken stream, which is after the teaching has paid off and
    well before the CTA. It is a placement decision, not new speech.
    """
    ps = spoken(n)
    wcum, total = 0, words(n)
    for p in ps:
        wcum += len(p.split())
        if wcum >= total * 0.6:
            return (sentences(p)[0],
                    "Small lower-third, four seconds, no sound and no "
                    "voiceover. It sits after the teaching has paid off and "
                    "well before the CTA, so it never lands on a boundary or "
                    "on the ending.")
    return (sentences(ps[-1])[0], "Small lower-third, four seconds, silent.")

def assets_dir(n):
    if n in SYNC:
        d = (PKG % n) + "/04_VISUAL_ASSETS"
        return d if os.path.isdir(d) else None
    return None

def existing(n, rel):
    """A file inside this video's approved synchronized package, or None."""
    if n not in SYNC:
        return None
    p = (PKG % n) + "/" + rel
    return p if os.path.exists(p) else None

def verify():
    bad = []
    for n in VIDEOS:
        joined = " ".join(master_sentences(n))
        for f in families(n):
            if not f["trigger"]:
                bad.append("V%d %s has no trigger" % (n, f["family"]))
            elif f["trigger"] not in joined:
                bad.append("V%d %s trigger not in the locked master: %s"
                           % (n, f["family"], f["trigger"][:50]))
        for label, group in (("camera", camera(n)), ("broll", broll(n)),
                             ("sound", sound(n))):
            for t, _w in group:
                if t not in joined:
                    bad.append("V%d %s cue not in the locked master: %s"
                               % (n, label, t[:50]))
        t, _w = subscribe(n)
        if t not in joined:
            bad.append("V%d subscribe cue not in the locked master" % n)
    return bad

if __name__ == "__main__":
    print("events.verify():", EV.verify() or "clean")
    for n in VIDEOS:
        print("V%-3d %4d words  %2d families  %d camera  %d broll  %d sound  "
              "assets: %s"
              % (n, words(n), len(families(n)), len(camera(n)), len(broll(n)),
                 len(sound(n)), "reuse" if assets_dir(n) else "none, must render"))
    bad = verify()
    print("\nunanchored or missing:", len(bad))
    for b in bad[:12]:
        print("   ", b)
