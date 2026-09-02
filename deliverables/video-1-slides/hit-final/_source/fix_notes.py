# -*- coding: utf-8 -*-
"""Correct the stale Field Kit language in the Video 1 speaker/editor notes.

Only notesSlide parts are touched. Slide XML, media, rels and geometry are
copied through byte-identically, so nothing visual can move.

The notes wrap each line as its own paragraph with blank paragraphs between
blocks. The invitation block is rebuilt as one paragraph per sentence, keeping
the note's existing convention of showing the invitation inside quotes, and
the three sentences are the canonical v3.1 spoken CTA verbatim.
"""
import copy, shutil, zipfile
from lxml import etree

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
def q(t): return "{%s}%s" % (A, t)

# canonical v3.1 spoken CTA, verbatim
CTA = ["If you want to try this on one real accomplishment, I made a free Career Evidence Starter.",
       "It takes about 10 to 15 focused minutes and helps you turn one piece of work into a portable Proof Line.",
       "I’ve linked it below."]

NOTE1_OLD = ["Leave five to seven seconds after the third question before moving to the",
             "Field Kit invitation."]
NOTE1_NEW = ["Leave five to seven seconds after the third question before moving to the",
             "Career Evidence Starter invitation."]
NOTE2_OLD = ['"If these questions are showing you that you need a fuller reading of what',
             'your current work is building, the Capability Formation Field Kit will help',
             'you complete that assessment privately using evidence from the last 90',
             'days."']
NOTE2_NEW = ['"' + CTA[0], "", CTA[1], "", CTA[2] + '"']
NOTE3_OLD = ["Keep the delivery calm and brief. This is the only purchase invitation in",
             "the video."]
NOTE3_NEW = ["Keep the delivery calm and brief. This is the only resource invitation in",
             "the video."]

EDITS = [(NOTE1_OLD, NOTE1_NEW), (NOTE2_OLD, NOTE2_NEW), (NOTE3_OLD, NOTE3_NEW)]

TARGETS = {
 "Video-1-How-I-Changed-Jobs-Without-Starting-My-Career-Over_v2.4.pptx":
     ["ppt/notesSlides/notesSlide11.xml", "ppt/notesSlides/notesSlide12.xml"],
 "Video-1-Reveal-Builds_v2.4.pptx":
     ["ppt/notesSlides/notesSlide18.xml", "ppt/notesSlides/notesSlide19.xml",
      "ppt/notesSlides/notesSlide20.xml", "ppt/notesSlides/notesSlide21.xml"],
}

def para_text(p):
    return "".join(t.text or "" for t in p.iter(q("t")))

def set_para(p, text, template_run):
    """Replace a paragraph's runs with one run carrying `text`."""
    for child in list(p):
        if etree.QName(child).localname in ("r", "br"):
            p.remove(child)
    if text:
        r = copy.deepcopy(template_run)
        r.find(q("t")).text = text
        p.append(r)

total = 0
for path, parts in TARGETS.items():
    zin = zipfile.ZipFile(path)
    out = {}
    for part in parts:
        root = etree.fromstring(zin.read(part))
        # notesSlide carries several <p:txBody> elements (the slide-image
        # placeholder among them); pick the one holding the notes prose.
        body = None
        for tb in root.iter("{%s}txBody" % P):
            joined = [para_text(p) for p in tb.findall(q("p"))]
            if any(old[0] in joined for old, _ in EDITS):
                body = tb; break
        assert body is not None, "notes body not found in " + part
        paras = body.findall(q("p"))
        texts = [para_text(p) for p in paras]
        template = None
        for p in paras:
            r = p.find(q("r"))
            if r is not None:
                template = r; break
        assert template is not None, "no run to clone in " + part
        for old, new in EDITS:
            for i in range(len(texts) - len(old) + 1):
                if texts[i:i + len(old)] == old:
                    # rewrite in place, then add or drop paragraphs as needed
                    for k, line in enumerate(new[:len(old)]):
                        set_para(paras[i + k], line, template)
                    for extra in new[len(old):]:
                        np = copy.deepcopy(paras[i + len(old) - 1])
                        set_para(np, extra, template)
                        paras[i + len(old) - 1].addnext(np)
                        paras = body.findall(q("p"))
                    for drop in range(len(old) - len(new)):
                        body.remove(paras[i + len(new)])
                        paras = body.findall(q("p"))
                    texts = [para_text(p) for p in body.findall(q("p"))]
                    paras = body.findall(q("p"))
                    total += 1
                    print("  %-26s %s applied" % (part.split("/")[-1], old[0][:38]))
                    break
        out[part] = etree.tostring(root, xml_declaration=True,
                                   encoding="UTF-8", standalone=True)
    tmp = "/tmp/v1notes/_out.pptx"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            zout.writestr(item, out.get(item.filename, zin.read(item.filename)))
    zin.close()
    shutil.move(tmp, path)
print("edits applied:", total)
