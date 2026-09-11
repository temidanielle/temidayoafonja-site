# -*- coding: utf-8 -*-
"""What each rendered asset actually is, measured rather than asserted.

Four earlier batches drew their cards with four different layout modules, so
byte identity alone cannot answer whether a card's words changed: the same
sentence drawn by lay813 and by lay421 produces two different PNGs. Two
measurements are therefore taken and the classification follows from them.

  REUSE                the newly rendered PNG is byte-identical to a prior
                       rendered file. Nothing changed, including the pixels.
  REUSE, RE-RENDERED   the words on the card are unchanged. This build drew
                       them, so the bytes differ and the file is new.
  COPY UPDATE          the card is recognizably the prior card with its
                       wording brought to the corrected master.
  REBUILD              a card in the same slot existed, but this one is a
                       different card.
  NEW                  no prior card resembles it.

The similarity floor separating COPY UPDATE from REBUILD is a judgment, and
it is stated here rather than buried: a card that still shares most of its
text with its predecessor is an update of it, and one that does not is a new
card in an old slot.
"""
import difflib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import priortext421 as PT
import masters421 as M
from frames421 import SETS

UPDATE_FLOOR = 0.60
NEW_CEILING = 0.25


def measure(identical_keys):
    """[(video, key, classification, evidence)] for all 180 assets."""
    prior = PT.prior_texts()
    out = []
    for n in M.VIDEOS:
        pool = [(t, PT.norm(t)) for t in prior.get(n, [])]
        for f in SETS[n]:
            new = PT._text(f["draw"])
            nn = PT.norm(new)
            if f["key"] in identical_keys:
                out.append((n, f["key"], "REUSE",
                            "byte-identical to the prior rendered file"))
                continue
            if any(nn == p for _, p in pool):
                out.append((n, f["key"], "REUSE, RE-RENDERED",
                            "the card's words are unchanged; this build drew "
                            "them, so the file differs"))
                continue
            if not pool:
                out.append((n, f["key"], "NEW",
                            "no prior rendered card exists for this video"))
                continue
            best, ratio = None, 0.0
            for raw, p in pool:
                r = difflib.SequenceMatcher(None, p, nn).ratio()
                if r > ratio:
                    best, ratio = raw, r
            if ratio >= UPDATE_FLOOR:
                cls = "COPY UPDATE"
                ev = ("%.0f%% of the text is shared with the prior card, "
                      "which read: %s" % (100 * ratio, _clip(best)))
            elif ratio >= NEW_CEILING:
                cls = "REBUILD"
                ev = ("only %.0f%% of the text is shared with the closest "
                      "prior card, which read: %s" % (100 * ratio,
                                                      _clip(best)))
            else:
                cls = "NEW"
                ev = ("nothing in the prior package resembles it; the "
                      "closest card shares %.0f%% of its text"
                      % (100 * ratio))
            out.append((n, f["key"], cls, ev))
    return out


def _clip(s, n=110):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n - 1] + "…"


def disagreements(identical_keys):
    """Where the declared status makes a claim the evidence contradicts.

    Only two claims are checkable this way, and only those two are checked.

      a REUSE label asserts that an earlier rendered asset was carried
      across. Byte identity, or identical card copy, is what makes that
      true. Nothing else does.

      any other label asserts that something changed. A byte-identical file
      means nothing changed, so the label is wrong.

    The choice between COPY UPDATE, REBUILD and NEW is editorial judgment
    about which prior card a new card descends from. That judgment is
    recorded in each asset's own note and is not second-guessed here, because
    a best-match text score does not know which slot a card belongs to.
    """
    declared = {f["key"]: f["status"] for n in M.VIDEOS for f in SETS[n]}
    carried = {"REUSE", "REUSE, RE-RENDERED"}
    out = []
    for n, key, cls, ev in measure(identical_keys):
        d = declared[key]
        if d.startswith("REMOVE"):
            continue          # a removal is an editorial act, not a measurement
        if d in carried and cls not in carried:
            out.append((n, key, d, cls, ev))
        elif d not in carried and cls in carried:
            out.append((n, key, d, cls, ev))
    return out
