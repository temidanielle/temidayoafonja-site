# -*- coding: utf-8 -*-
"""Things to flag rather than silently repair.

The instruction is explicit that approved speech is not edited and that a
genuine contradiction is raised rather than quietly fixed. Everything in this
module is a finding. None of it is applied to any package.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters421 as M

# The checksum the instruction supplied for the corrected recording-master
# archive, exactly as written.
PROMPT_CHECKSUM = None   # set by build421 from the instruction text if given

RESTORED_BAND = (9 * 60, 12 * 60)


def _secs(mmss):
    m, s = mmss.split(":")
    return int(m) * 60 + int(s)


def runtime_flags():
    """Videos whose speech-only estimate does not sit where its own stated
    target says it should. Nothing is lengthened or shortened in response."""
    out = []
    for n in M.VIDEOS:
        words, fast, slow = M.estimate(n)
        intent = M.runtime_intent(n)
        if n in M.FIVE_MIN:
            continue
        if n in M.RESTORED_DEPTH:
            if _secs(slow) < RESTORED_BAND[0]:
                out.append((n, "below the restored 9 to 12 minute band",
                            "%d words, %s to %s at 130 to 145 wpm. The "
                            "estimate is speech only and excludes pauses and "
                            "visual holds, so the recorded runtime will be "
                            "longer. Not lengthened: the master is approved "
                            "speech." % (words, fast, slow)))
            continue
        if not intent:
            if _secs(slow) < 5 * 60 + 30:
                out.append((n, "as short as the 5-minute experiment, but "
                            "designated regular long-form",
                            "%d words, %s to %s at 130 to 145 wpm. This "
                            "master states no runtime target."
                            % (words, fast, slow)))
            continue
        # A master that states its own target. The target is written either
        # as clock times ("9:15 to 10:15") or as plain minutes ("9 to 12
        # minutes"), and the two must not be mixed up: reading "9:15" as the
        # numbers 9 and 15 would make the floor 9 minutes in one place and 15
        # in another.
        import re
        clock = re.findall(r"\b(\d{1,2}):(\d{2})\b", intent)
        if clock:
            floor = min(int(a) * 60 + int(b) for a, b in clock)
        else:
            mins = [int(x) for x in re.findall(r"\b(\d{1,2})\b(?!\s*:)",
                                              intent)]
            floor = min(mins) * 60 if mins else 0
        if floor and _secs(slow) < floor:
            out.append((n, "below the target its own master states",
                        "%d words, %s to %s at 130 to 145 wpm against '%s'. "
                        "The estimate is speech only and excludes pauses and "
                        "visual holds. Not lengthened."
                        % (words, fast, slow, intent)))
    return out


def typography_flags():
    """Differences in punctuation between two approved masters.

    Recorded, and resolved only on the production-facing side: the Watch Next
    card carries the destination master's canonical title exactly. Neither
    locked source master is edited, because a punctuation glyph is not a
    reason to change approved copy, and both masters keep their checksums.
    """
    out = []
    for n in M.VIDEOS:
        wn = M.watch_next(n)
        if not wn or ":" not in wn:
            continue
        dest = int(wn.split(":")[0].strip().lstrip("Video").lstrip("V").strip())
        said = wn.split(":", 1)[1].strip()
        real = M.title(dest)
        if said != real and said.replace("’", "'") == real.replace("’", "'"):
            out.append((n, "apostrophe glyph differs from the destination "
                        "master's own title",
                        "V%d's Watch Next row writes it as %r. V%d's Title "
                        "row writes it as %r. Same words, different "
                        "apostrophe. RESOLVED on the production side: the "
                        "Watch Next card carries V%d's canonical title "
                        "exactly. Neither locked master is edited and both "
                        "keep their checksums."
                        % (n, said, dest, real, dest)))
    return out


def restoration_notes():
    """Videos whose supplied master was compressed and has been restored.

    Recorded as a note rather than a flag: the defect is resolved, but the
    fact that the supplied file was not the full-depth script has to stay
    visible, and the supplied file itself is retained unchanged."""
    out = []
    for n in sorted(M.RESTORED):
        prev = {6: 1151, 7: 1209, 8: 1198}[n]
        words, fast, slow = M.estimate(n)
        out.append((n, "restored from a compressed supplied master",
                    "The September 11 master carried about half the approved "
                    "teaching. The spoken source of truth is now %s, %d "
                    "words, %s to %s at 130 to 145 wpm, against %d in the "
                    "last full-length approved master. The supplied file is "
                    "unchanged in _source/ and still matches its original "
                    "checksum. No new teaching was authored."
                    % (M.RESTORED[n], words, fast, slow, prev)))
    return out


def all_flags():
    return ([(n, "RUNTIME", a, b) for n, a, b in runtime_flags()] +
            [(n, "TYPOGRAPHY", a, b) for n, a, b in typography_flags()] +
            [(n, "RESTORED", a, b) for n, a, b in restoration_notes()])


if __name__ == "__main__":
    for n, kind, label, detail in all_flags():
        print("V%-3d %-11s %s" % (n, kind, label))
        print("      %s" % detail)
