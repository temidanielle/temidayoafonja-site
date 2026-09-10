# -*- coding: utf-8 -*-
"""Things to flag rather than silently repair.

Nothing here is fixed in the package. Approved speech is not edited, and a
scheduling dependency is not resolved by redirecting a handoff.
"""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import masters1421 as M

DELIV = "/home/user/temidayoafonja-site/deliverables/"

# Titles of the videos this batch hands off to, taken from the packages that
# already exist rather than from any roadmap text.
def existing_titles():
    out = {}
    b813 = DELIV + "VIDEOS_8-13_LOCKED_MASTER_BUILD/build"
    if os.path.isdir(b813):
        sys.path.insert(0, b813)
        try:
            import masters813 as M813
            for n in M813.VIDEOS:
                out[n] = M813.title(n)
        except Exception:
            pass
    # V4 to V7 come from the September 9 synchronization tracker entry.
    out.update({
      4: "How to Explain a Career That Looks All Over the Place",
      5: "Why Nobody Can Tell What You’re Actually Good At",
      6: "Before You Take an Internal Role, Ask These 3 Questions",
      7: "Are You Growing, or Just Being Given More Work?",
    })
    for n in M.VIDEOS:
        out[n] = M.title(n)
    return out


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip().lower()


def watch_next_check():
    """Every Watch Next destination, its number, and whether the title the
    master uses matches the title that destination actually carries."""
    titles = existing_titles()
    rows = []
    for n in M.VIDEOS:
        wn = M.watch_next(n)
        m = re.match(r"(?:V|Video )(\d+)\s*:\s*(.+)", wn)
        if not m:
            rows.append((n, None, wn, None, "could not parse a destination"))
            continue
        dest, string = int(m.group(1)), m.group(2).strip()
        actual = titles.get(dest)
        if actual is None:
            note = "destination title not available in this workspace"
            ok = None
        else:
            ok = _norm(actual) == _norm(string)
            note = "matches" if ok else "DIFFERS from %r" % actual
        rows.append((n, dest, string, ok, note))
    return rows


def scheduling_dependencies():
    """A Watch Next that points at a video which is not yet published."""
    published = {1, 2, 3}
    out = []
    for n, dest, string, ok, note in watch_next_check():
        if dest is None:
            continue
        if dest in published:
            continue
        if dest in M.VIDEOS and dest > n:
            kind = ("FORWARD. The destination is later in this same batch and "
                    "must be live when this video publishes.")
        elif dest in M.VIDEOS:
            kind = ("Earlier in this same batch. Publish in numeric order and "
                    "the dependency is satisfied.")
        else:
            kind = ("Built but not yet published. The destination package "
                    "exists in this workspace; the video does not exist on "
                    "the channel yet.")
        spoken = M.contains(n, string)
        out.append((n, dest, string, kind, spoken))
    return out


def runtime_note():
    rows = []
    for n in M.VIDEOS:
        w, fast, slow = M.estimate(n)
        rows.append((n, w, fast, slow))
    return rows


NOTES = [
 ("V20 opens on a real personal account",
  "The master's hook is Temidayo's own maternity-leave return. It is not a "
  "constructed illustration and must never be labeled as one. The frame set "
  "keeps the opening camera-led. The constructed illustration later in the "
  "same video is separately labeled, and the two must not be confused."),
 ("V14 employers are described by type on every rendered frame",
  "The master's research notes permit Humana, Wells Fargo, Mass General "
  "Brigham and JPMorgan to be named on screen, but only with the preserved "
  "source wording and with the capture kept in the production archive. No "
  "frame in this batch names an employer. If the editor decides to name one, "
  "the source capture must travel with it, and several source postings were "
  "mirrored, older or closed, so not every source is a currently live "
  "employer posting."),
 ("Thumbnail artwork is not produced",
  "Only Canva briefs exist. The wording in each master is authoritative and "
  "is not restyled. No portrait is generated and no face is altered."),
 ("No resource route exists for Video 14",
  "The V14 master names no resource. None was added to the script, the "
  "description, the pinned comment or any card. Its CTA card carries the "
  "action instead of a URL."),
]


if __name__ == "__main__":
    print("WATCH NEXT")
    for n, dest, string, ok, note in watch_next_check():
        print("  V%-3d -> V%-3s %-58s %s" % (n, dest, string[:58], note))
    print("\nSCHEDULING DEPENDENCIES")
    for n, dest, string, kind, spoken in scheduling_dependencies():
        print("  V%d -> V%d  spoken in script: %s" % (n, dest, spoken))
        print("       %s" % kind)
    print("\nRUNTIME")
    for n, w, f, s in runtime_note():
        print("  V%-3d %4d words  %s to %s" % (n, w, f, s))
