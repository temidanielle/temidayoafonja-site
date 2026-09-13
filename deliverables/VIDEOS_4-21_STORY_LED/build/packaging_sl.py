# -*- coding: utf-8 -*-
"""Packaging authority for the story-led batch.

The September 13 script layer is authoritative for current spoken wording and
recording delivery. Its header carries thumbnail metadata, and that metadata
is NOT packaging authority: the separately locked V4 to V21 roadmap is. For
two videos the two disagree, and the roadmap wins.

Nothing here reads or writes a source file. masters_sl keeps returning what
the script header actually says, so the divergence can be recorded rather
than hidden, and every derived production record asks this module instead.
"""
import masters_sl as M

# The locked roadmap wording, for the videos where the script header differs.
ROADMAP_THUMBNAIL = {
    4: "I'D NEVER HELD THE ROLE",
    5: "CHANGED TRACKS. NOT ZERO.",
}


def thumbnail(n):
    """The thumbnail of record. Packaging authority, not script metadata."""
    return ROADMAP_THUMBNAIL.get(n, M.thumbnail(n))


def script_header_thumbnail(n):
    """What the script document's header says, whatever that is."""
    return M.thumbnail(n)


def is_exception(n):
    return script_header_thumbnail(n) != thumbnail(n)


def exceptions():
    """[(video, script header metadata, thumbnail of record)] for the record."""
    return [(n, script_header_thumbnail(n), thumbnail(n))
            for n in M.VIDEOS if is_exception(n)]


EXCEPTION_NOTE = (
    "The September 13 script layer is authoritative for current spoken "
    "wording and recording delivery. The thumbnail text in its document "
    "header is non-spoken metadata and does not override the separately "
    "locked V4 to V21 roadmap and packaging decisions. Where the two "
    "differ, the roadmap is the thumbnail of record and the script header "
    "is carried here as a known metadata exception. No source document was "
    "edited, and every source hash is unchanged."
)


if __name__ == "__main__":
    for n in M.VIDEOS:
        mark = "  <- exception" if is_exception(n) else ""
        print("V%-3d record %-32r header %-32r%s"
              % (n, thumbnail(n), script_header_thumbnail(n), mark))
