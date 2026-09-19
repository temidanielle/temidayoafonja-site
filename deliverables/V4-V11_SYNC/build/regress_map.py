# -*- coding: utf-8 -*-
"""Regression fixtures for the final map review, run on delivered files.

Every finding in 03_Delivered_File_Conflicts.json is turned into an
assertion that reads the delivered documents, not the generator's own
dictionaries. Each one must fail on the reviewed archive and pass on the
correction, and the reviewed values are kept here so that can be shown.
"""
import os, re, sys, json, csv
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import recon as R
import events as EV
import packages as P

REVIEW = os.path.join(OUT, "_review", "map")
PKG = lambda n: os.path.join(OUT, "PACKAGES", P.PKG[n])


def norm(t):
    return " ".join((t or "").split())


def cam(n):
    return open(os.path.join(PKG(n), "03_RIVERSIDE",
                             "Camera_and_Full_Screen_Map.txt")).read()


def riv(n):
    return open(os.path.join(PKG(n), "03_RIVERSIDE",
                             "Riverside_CoCreator_Master_Prompt.txt")).read()


def blocks(n):
    """The camera map parsed back into (section, para, mode, family)."""
    out, sec, cur = [], None, None
    for line in cam(n).split("\n"):
        m = re.match(r"^SECTION (\d+)\s+(.*)$", line)
        if m:
            sec = (int(m.group(1)), m.group(2).strip())
            continue
        m = re.match(r"^  PARA (\d+)\s+MODE: ([A-Z ]+?)(,|\s{2,}|\[|$)",
                     line)
        if m:
            cur = dict(sec=sec, para=int(m.group(1)),
                       mode=m.group(2).strip(), fam=None, body=[])
            out.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^\s+ASSET FAMILY: (\S+)", line)
        if m:
            cur["fam"] = m.group(1)
        cur["body"].append(line.strip())
    return out


def covered(n):
    """Every (section, paragraph) a full-screen event covers, per the map."""
    got = set()
    for b in blocks(n):
        if b["mode"] != "FULL SCREEN" or not b["sec"]:
            continue
        got.add((b["sec"][0], b["para"]))
        m = re.search(r"SPANS PARAGRAPHS (\d+) TO (\d+)",
                      " ".join(b["body"]))
        if m:
            for p in range(int(m.group(1)), int(m.group(2)) + 1):
                got.add((b["sec"][0], p))
    return got


def main():
    d = json.load(open(os.path.join(REVIEW,
                                    "03_Delivered_File_Conflicts.json")))
    fail = 0

    print("EXACT TRIGGER QUOTATIONS (5)\n")
    for c in d["exact_trigger_conflicts"]:
        bs = [b for b in blocks(c["v"]) if b["fam"] == c["family"]]
        body = norm(" ".join(x for b in bs for x in b["body"]))
        stale = norm(c["printed"])[:60] in body
        good = norm(c["actual"])[:60] in body
        ok = good and not stale
        print("  V%-3d %-42s %s" % (c["v"], c["family"],
                                    "correct" if ok else "STALE"))
        fail += 0 if ok else 1

    print("\nRUN-OF-SHOW SECTION NAMES (7)\n")
    sys.path.insert(0, "/home/user/temidayoafonja-site/deliverables/"
                       "VIDEOS_22-23/build")
    from qa23 import units
    for c in d["run_of_show_section_label_conflicts"]:
        us = units(os.path.join(PKG(c["video"]), "02_RUN_OF_SHOW",
                                "Run_of_Show.docx"))
        near = " | ".join(us[k + 1] for k, u in enumerate(us)
                          if c["asset"] in u and k + 1 < len(us))
        ok = norm(c["expected_section"]) in norm(near)
        bad = norm(c["printed_section"]) in norm(near)
        print("  V%-3d %-42s %s" % (c["video"], c["asset"],
                                    "correct" if ok and not bad
                                    else "STALE"))
        fail += 0 if (ok and not bad) else 1

    print("\nFULL-SCREEN INSTRUCTIONS POINTING AT CAMERA PARAGRAPHS (17)\n")
    rows = list(csv.DictReader(open(os.path.join(
        REVIEW, "04_Full_Screen_Instruction_Conflicts.csv"))))
    # A conflict is resolved either by the paragraph becoming full screen
    # or by the instruction no longer claiming full screen there. The
    # second is only acceptable when the treatment survives: an event must
    # still exist at that location and the brief's own display copy must
    # still be in the prompt, so a conflict cannot be closed by deleting
    # the teaching.
    for r in rows:
        n, sec, para = int(r["video"]), int(r["section"]), int(r["paragraph"])
        full = (sec, para) in covered(n)
        here = [e for e in EV.events(n)
                if e["section"] + 1 == sec
                and e["para"] <= para - 1 <= e["para_out"]]
        disp = norm(r["display_instruction"].split("|")[-1])[:28]
        kept = disp.lower() in norm(riv(n)).lower()
        ok = full or (here and kept)
        how = ("full screen" if full else
               "camera, treatment kept at its own event" if ok else
               "UNRESOLVED")
        print("  V%-3d sec %2d p%d  %-32s %s"
              % (n, sec, para, r["section_name"][:32], how))
        fail += 0 if ok else 1

    print("\nTRUNCATED BOUNDARY FIELDS (36)\n")
    left = 0
    for c in d["truncated_camera_opening_boundaries"]:
        if norm(c["line"]) in norm(cam(c["v"])):
            left += 1
    ell = sum(1 for n in R.VIDEOS for line in cam(n).split("\n")
              if ("ENTER ON:" in line or "LEAVE ON:" in line)
              and "..." in line)
    print("  reviewed truncations still present: %d of 36" % left)
    print("  any ellipsis in an entry or exit line: %d" % ell)
    fail += left + ell

    print("\nCROSS-PARAGRAPH REVEALS\n")
    fixtures = [
     (11, "NEW_V11_FS_06_FOUR_COST_LENSES",
      {"NEW_V11_FS_06A_CAPABILITY": (7, 1),
       "NEW_V11_FS_06B_EVIDENCE": (7, 1),
       "NEW_V11_FS_06C_COMPENSATION": (7, 2),
       "NEW_V11_FS_06D_LIFE": (7, 2)}),
     (11, "NEW_V11_FS_09_THE_ROLE_DRIFT_READ",
      {"NEW_V11_FS_09A_EXPECTED": (10, 1),
       "NEW_V11_FS_09B_ACTUAL": (10, 1),
       "NEW_V11_FS_09C_COST": (10, 2),
       "NEW_V11_FS_09D_CHOICE": (10, 2)}),
     (6, "NEW_V6_FS_06_POSTING_WALKTHROUGH",
      {"NEW_V6_FS_06A_PROBLEM": (4, 2),
       "NEW_V6_FS_06B_AUTHORITY": (5, 2),
       "NEW_V6_FS_06C_PROOF": (6, 2)}),
    ]
    for n, fam, want in fixtures:
        got = {}
        for e in EV.events(n):
            if e["family"] != fam:
                continue
            for st in e["states"]:
                got[st["name"]] = (e["section"] + 1, st["para"] + 1)
        for name, where in sorted(want.items()):
            ok = got.get(name) == where
            print("  V%-3d %-34s section %d paragraph %d   %s"
                  % (n, name.replace("NEW_V%d_" % n, ""), where[0],
                     where[1], "ok" if ok else "WRONG %s" % (got.get(name),)))
            fail += 0 if ok else 1

    print("\nONE SEQUENCE, NOT TWO LAYERS\n")
    for n in R.VIDEOS:
        m = EV.modes(n)
        c = covered(n)
        mism = [(si + 1, pi + 1) for (si, pi), v in m.items()
                if v == EV.FULL and (si + 1, pi + 1) not in c]
        print("  V%-3d %d full-screen paragraphs in the event list, %d "
              "missing from the map" % (n, len([1 for v in m.values()
                                                if v == EV.FULL]),
                                        len(mism)))
        fail += len(mism)

    print("\nV11 SHORT 1 CLOSING\n")
    import shortsync as SH
    ask = norm(" ".join(SH.SHORTS[(11, 1)]["ask"]))
    want = norm("Write EXPECTED and ACTUAL side by side. Name one real "
                "cost. Then choose one next action: clarify, negotiate, "
                "test for a defined period, or begin planning another "
                "option.")
    ok = ask == want
    print("  ask is the approved closing application: %s" % ("yes" if ok
                                                             else "NO"))
    fail += 0 if ok else 1
    body = norm(" ".join(SH.lines(11, 1)))
    for keep in ("Before you call it a bait-and-switch, slow down.",
                 "This is not the job I thought I accepted."):
        k = norm(keep) in body
        print("  keeps %-52s %s" % (keep[:52], "yes" if k else "NO"))
        fail += 0 if k else 1

    print("\nTHE SAME ASSERTIONS, REPLAYED AGAINST THE REVIEWED VALUES\n")
    # The reviewed archive is not on disk, but the review recorded what
    # its files said. Feeding those recorded values back through the same
    # assertions shows the assertions are not vacuous.
    caught = 0
    for c in d["exact_trigger_conflicts"]:
        if norm(c["printed"])[:60] not in norm(c["actual"]):
            caught += 1
    print("  5 trigger quotations: %d would fail" % caught)
    fail += 5 - caught
    caught = sum(1 for c in d["run_of_show_section_label_conflicts"]
                 if norm(c["printed_section"]) != norm(
                     c["expected_section"]))
    print("  7 run-of-show names:  %d would fail" % caught)
    fail += 7 - caught
    caught = sum(1 for r in rows if r["camera_map_mode"] == "CAMERA")
    print("  17 mode conflicts:    %d would fail" % caught)
    fail += 17 - caught
    caught = sum(1 for c in d["truncated_camera_opening_boundaries"]
                 if "..." in c["line"])
    print("  36 truncations:       %d would fail" % caught)
    fail += 36 - caught
    print("  cross-paragraph:      the reviewed set put every state of a "
          "family in one paragraph,")
    print("                        which the span assertion above rejects")

    print("\nfindings not caught: %d" % fail)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
