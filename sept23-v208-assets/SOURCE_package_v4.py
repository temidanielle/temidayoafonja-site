# -*- coding: utf-8 -*-
"""Assemble and verify the September 23 revision-2 package.

Every sweep runs on the packaged bytes before the ZIP is written, so a defect
stops the package rather than shipping inside it.
"""
import hashlib, io, os, re, shutil, tokenize, zipfile
import docx, pymupdf
from pptx import Presentation

ROOT = "scratchpad/sept23/pkg/September_23_Stay_or_Leave_CANDIDATE_v4"
A = "sept23-v208-assets"
WB = "free-flagship-assets/60min-v2.0.1/Capability_Position_Read_Workbook_60MIN_v2.0.1_CANDIDATE.pdf"
WB_SHA = "2bd2912846a679837e8e6bfb4aadff2bb07ee5959d35502ca1c5b5c728efa3ee"
FACING = ("01_LIVE_DELIVERY", "02_FACILITATOR_OPERATIONS", "03_QA_AND_CHANGE_CONTROL")
LAYOUT = {
 "01_LIVE_DELIVERY": [
   f"{A}/PRESENTER_VERSION_Stay_or_Leave_Live_Career_Growth_Assessment_60MIN_v2.0.7_CANDIDATE.pptx", WB],
 "02_FACILITATOR_OPERATIONS": [
   f"{A}/Capability_Formation_Free_Flagship_SOP_Sept23_2026_60MIN_v2.0.10_CANDIDATE.docx"],
 "03_QA_AND_CHANGE_CONTROL": [
   f"{A}/Free_Flagship_60MIN_v2.0.11_Change_Log_and_QA_Report.docx",
   f"{A}/Manual_Maven_and_Website_Edit_Checklist_v1.3.docx",
   f"{A}/PREVIEW_Presentation_60MIN_v2.0.7_LibreOffice.pdf",
   f"{A}/PREVIEW_SOP_60MIN_v2.0.10_LibreOffice.pdf"],
 "04_BUILD_AND_REPRODUCIBILITY": [
   f"{A}/SOURCE_build_v207.py", f"{A}/SOURCE_build_sop_v2010.py",
   f"{A}/SOURCE_build_report_v2011.py", f"{A}/SOURCE_build_checklist_v13.py",
   f"{A}/SOURCE_qa_v208.py"],
}
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def units(p):
    """Text in the units a claim lives in. PDFs by paragraph, never by rendered
    line, so a sentence naming an old value beside its replacement is not split
    in half and misread."""
    if p.endswith(".pptx"):
        pr = Presentation(p); out = []
        for s in pr.slides:
            out += [sh.text_frame.text for sh in s.shapes if sh.has_text_frame]
            if s.has_notes_slide:
                out.append(s.notes_slide.notes_text_frame.text)
        return out
    if p.endswith(".docx"):
        d = docx.Document(p); out = [x.text for x in d.paragraphs]
        for t in d.tables:
            for r in t.rows:
                out += [c.text for c in r.cells]
        return out
    if p.endswith(".pdf"):
        return [re.sub(r"\s+", " ", b[4]).strip()
                for pg in pymupdf.open(p) for b in pg.get_text("blocks")]
    return [open(p, encoding="utf-8").read()]


# The word boundary matters: without it, "First private reading" matched.
PRIVATE = re.compile(r"Private (Capability )?(Position )?Read\b", re.I)
S16 = re.compile(r"(September 16|Sept ?16|2026-09-16)", re.I)
CST = re.compile(r"(?<![A-Za-z_])CST(?![A-Za-z_])")
# A mention is not a live offer when it retires it, records what an earlier
# version did, asserts its absence, or instructs its removal from the site.
RETIRED = re.compile(
  r"(RETIRED|retired|Withdrawn|does not return|replaces it|Replaced|removed|"
  r"removal|is gone|was route 3|until v2\.0\.4|not pitched|not offered|"
  r"no spoken continuation script|off the continuation|still live on the website|"
  r"REPOINTED|is not re-pitched|not operational|unavailable|stays off the slide)",
  re.I)


def main():
    if os.path.exists("scratchpad/sept23/pkg"):
        shutil.rmtree("scratchpad/sept23/pkg")
    rows = []
    for folder, files in LAYOUT.items():
        os.makedirs(f"{ROOT}/{folder}", exist_ok=True)
        for src in files:
            shutil.copyfile(src, f"{ROOT}/{folder}/{os.path.basename(src)}")
            rows.append((f"{folder}/{os.path.basename(src)}",
                         os.path.getsize(src), sha(src)))

    bad, hist, stale16, cst_hits = [], 0, [], []
    for folder in FACING:
        for src in LAYOUT[folder]:
            name = os.path.basename(src)
            for u in units(src):
                if PRIVATE.search(u):
                    if RETIRED.search(u):
                        hist += 1
                    else:
                        bad.append(f"{name}  {u.strip()[:110]}")
                if S16.search(u) and not re.search(r"(September 23|Sept23)", u) \
                   and "stale" not in u.lower():
                    stale16.append(f"{name}  {u.strip()[:90]}")
                if CST.search(u) and "Never write CST" not in u \
                   and "never CST" not in u:
                    cst_hits.append(f"{name}  {u.strip()[:80]}")
    assert not bad, "LIVE PRIVATE READ REFERENCE:\n" + "\n".join(bad)
    assert not stale16, "STALE SEPTEMBER 16:\n" + "\n".join(stale16)
    assert not cst_hits, "CST AS A LABEL:\n" + "\n".join(cst_hits)

    # Folder 04 is tooling whose job is to name the old values. Checked by
    # tokenising: every occurrence must sit in a string literal or a comment.
    tooling = 0
    for src in LAYOUT["04_BUILD_AND_REPRODUCIBILITY"]:
        source = open(src, encoding="utf-8").read()
        spans = [(t.start[0], t.end[0])
                 for t in tokenize.generate_tokens(io.StringIO(source).readline)
                 if t.type in (tokenize.STRING, tokenize.COMMENT)]
        for n, line in enumerate(source.split("\n"), 1):
            if PRIVATE.search(line) or S16.search(line) or CST.search(line):
                assert any(a <= n <= b for a, b in spans), \
                    f"{src}:{n} carries a retired name in executable code"
                tooling += 1

    assert sha(WB) == WB_SHA, "the workbook is not the approved v2.0.1 build"
    assert not any("FINAL" in r[0] for r in rows), "an asset was renamed to FINAL"

    man = open("scratchpad/sept23/manifest_head_v4.txt", encoding="utf-8").read()
    man = man.replace("{hist}", str(hist)).replace("{tooling}", str(tooling))
    w = max(len(r[0]) for r in rows)
    man += "".join(f"{p:<{w}}  {s:>7}  {h}\n" for p, s, h in rows)
    open(f"{ROOT}/MANIFEST.txt", "w", encoding="utf-8").write(man)

    Z = "September_23_Stay_or_Leave_CANDIDATE_Asset_Package_v4.zip"
    if os.path.exists(Z):
        os.remove(Z)
    with zipfile.ZipFile(Z, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(ROOT):
            for f in sorted(files):
                full = os.path.join(dirpath, f)
                z.write(full, os.path.relpath(full, "scratchpad/sept23/pkg"))
    print(f"01-03: 0 live Private Read ({hist} retired or historical), "
          f"0 stale September 16, 0 CST labels")
    print(f"04: {tooling} tooling occurrences, all inside strings or comments")
    print("built", Z, os.path.getsize(Z), "bytes")
    with zipfile.ZipFile(Z) as z:
        for n in sorted(z.namelist()):
            print("  ", n)
        print("  integrity:", z.testzip() or "OK")
    print("  sha256", sha(Z))


if __name__ == "__main__":
    main()
