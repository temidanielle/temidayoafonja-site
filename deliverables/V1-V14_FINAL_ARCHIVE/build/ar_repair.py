# -*- coding: utf-8 -*-
"""Authorized formatting-only repair of the two fused section labels.

V2 and V3 each carry a section label that runs into the first spoken sentence
with no paragraph break, in both the recording master and the thought-block
copy. Temidayo authorized separating them on September 23, 2026, as a
formatting correction only.

What this does: splits one paragraph into two. The label becomes its own
paragraph, formatted exactly like the other section labels in the same file,
and the spoken sentence keeps the paragraph it was in.

What this must not do, and what verify() proves it did not do: change a single
spoken word, or any punctuation inside a spoken sentence. The only characters
removed from the spoken stream are the label's own, and the only characters
added are the label's own in its new paragraph.
"""
import os, copy, hashlib, shutil
import docx
from docx.text.paragraph import Paragraph
import ar_sources as S

HERE = os.path.dirname(os.path.abspath(__file__))
REPAIRED = os.path.join(os.path.dirname(HERE), "_repaired")

# n: (label, spoken sentence it was fused to, label template in master,
#     label template in blocks)
FIX = {
2: ("READ THE LAST 90 DAYS",
    "Then look at the last 90 days of your actual work.",
    "OUTSIDE-CONTEXT EVIDENCE", "OUTSIDE-CONTEXT EVIDENCE [NOT SPOKEN]"),
3: ("KEEP THE PROOF, NOT THE PROPERTY",
    "So here is the rule: keep the proof, not the property.",
    "WHAT DISAPPEARS", "WHAT DISAPPEARS [NOT SPOKEN]"),
}

def _set_text(p, text):
    """Replace a single-run paragraph's text, keeping its run formatting."""
    assert len(p.runs) == 1, "expected one run, found %d" % len(p.runs)
    p.runs[0].text = text

def repair(src, dst, label, spoken, template, blocks):
    d = docx.Document(src)
    ps = d.paragraphs
    hits = [i for i, p in enumerate(ps) if p.text.strip().startswith(label)]
    assert len(hits) == 1, "expected one fused paragraph, found %d" % len(hits)
    i = hits[0]
    # The label and the sentence are separated by a line break inside one
    # paragraph, not glued with nothing between them. In Word the label already
    # looks like its own line; it simply is not its own paragraph, which is why
    # a paragraph-level reader sees them as one unit. Reading the document by
    # joining <w:t> elements drops the <w:br/>, which is what made the earlier
    # extract show "DAYSThen". A scan of all twenty-eight files found these
    # four paragraphs and no others carrying a line break, so no other word
    # count anywhere in the archive is affected by this.
    got = ps[i].text.strip().replace("\n", "").replace("\r", "")
    assert got == label + spoken, \
        "fused paragraph is not label + spoken: %r" % ps[i].text[:90]

    tm = [j for j, p in enumerate(ps) if p.text.strip() == template]
    assert tm, "no label template found for %r" % template
    tmpl = ps[tm[0]]

    # The label goes where the other labels go. In the thought-block copy that
    # is before the BLOCK marker, because a section label heads the block that
    # follows it, not the text inside one.
    anchor = ps[i - 1] if blocks else ps[i]
    if blocks:
        assert anchor.text.strip().startswith("BLOCK "), \
            "expected a BLOCK marker before the fused block, found %r" % anchor.text[:40]

    new_p = copy.deepcopy(tmpl._p)
    anchor._p.addprevious(new_p)
    np = Paragraph(new_p, anchor._parent)
    for r in np.runs[1:]:
        r._r.getparent().remove(r._r)
    _set_text(np, tmpl.text if blocks else label)
    if blocks:
        # the template carries its own name; replace it with this label
        _set_text(np, label + " [NOT SPOKEN]")
    _set_text(ps[i], spoken)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    d.save(dst)
    return dst

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def run():
    out = {}
    for n, (label, spoken, tm_m, tm_b) in sorted(FIX.items()):
        m_dst = os.path.join(REPAIRED, "V%d_FINAL_Sticky_Realization_Recording_Master.docx" % n)
        b_dst = os.path.join(REPAIRED, "V%d_FINAL_Sticky_Realization_Thought_Blocks.docx" % n)
        repair(S.SRC[n][0], m_dst, label, spoken, tm_m, blocks=False)
        repair(S.SRC[n][1], b_dst, label, spoken, tm_b, blocks=True)
        out[n] = (m_dst, b_dst)
    return out

if __name__ == "__main__":
    for n, (m, b) in sorted(run().items()):
        print("V%d repaired" % n)
        print("   master %s" % sha256(m))
        print("   blocks %s" % sha256(b))


def verify():
    """The repair must remove the label from the spoken stream and change
    nothing else. Compared token by token against the original, the only
    permitted difference is the label's own words."""
    import ar_parity as PA
    out = []
    for n, (label, spoken, _tm, _tb) in sorted(FIX.items()):
        lab_tokens = label.split()
        for kind, idx, fname in (
                ("master", 0, "V%d_FINAL_Sticky_Realization_Recording_Master.docx" % n),
                ("blocks", 1, "V%d_FINAL_Sticky_Realization_Thought_Blocks.docx" % n)):
            # Read the PRE-REPAIR original. ar_sources now points SRC at the
            # repaired files, so comparing against SRC would compare a file
            # with itself and report success without testing anything.
            before = PA.spoken(S.PRE_REPAIR[n][idx], "sticky", kind)
            after = PA.spoken(os.path.join(REPAIRED, fname), "sticky", kind)
            a = " ".join(before).split()
            b = " ".join(after).split()
            # rebuild what 'a' should look like once the label stops being
            # counted: the fused token splits back into label-tail + sentence
            fused = label.split()[-1] + spoken.split()[0]
            expect = []
            for tok in a:
                if tok == fused:
                    expect.append(spoken.split()[0])
                elif expect[-len(lab_tokens) + 1:] == lab_tokens[:-1] and tok in lab_tokens:
                    expect.append(tok)
                else:
                    expect.append(tok)
            # drop the label tokens that precede the fused position
            idx_f = a.index(fused)
            expect = a[:idx_f - (len(lab_tokens) - 1)] + [spoken.split()[0]] + a[idx_f + 1:]
            out.append(dict(video=n, kind=kind, before=len(a), after=len(b),
                            clean=(b == expect),
                            removed=len(a) - len(b)))
    return out
