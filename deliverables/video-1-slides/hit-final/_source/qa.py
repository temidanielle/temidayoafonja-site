# -*- coding: utf-8 -*-
"""Video 1 H.I.T. package QA. Offsets are found, not assumed."""
import zipfile, re, sys, os, json, hashlib, subprocess
from xml.etree import ElementTree as ET
sys.path.insert(0,'/tmp/v1hit')
from script_text import LINES, SPOKEN, MARKERS
NS='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R="/tmp/v1hit/Video_1_HIT_FINAL"
MK=re.compile(r'^SLIDE\s+—\s+(.+)$')

def paras(p):
    x=ET.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
    t=lambda q:''.join(e.text or '' for e in q.iter(NS+'t'))
    return [t(el).strip() for el in x.find(NS+'body') if el.tag==NS+'p' and t(el).strip()]
def from_first_spoken(seq): return seq[seq.index(SPOKEN[0]):]
def txt_paras(p):
    return [b.strip() for b in open(p).read().strip().split("\n\n") if b.strip()]

L=R+"/LONG_FORM/"
tel_d=from_first_spoken(paras(L+"Video1TeleprompterScriptwithslidemarkers_HIT_v3.0.docx"))
tel_t=from_first_spoken(txt_paras(L+"Video1TeleprompterScriptwithslidemarkers_HIT_v3.0.txt"))
rd_d =from_first_spoken(paras(L+"Video1ReadingScriptnomarkers_HIT_v3.0.docx"))
rd_t =from_first_spoken(txt_paras(L+"Video1ReadingScriptnomarkers_HIT_v3.0.txt"))
strip=lambda s:[x for x in s if not MK.match(x)]

rep={}
rep["01_teleprompter_docx_equals_txt"]=tel_d==tel_t
rep["02_reading_docx_equals_txt"]=rd_d==rd_t
rep["03_teleprompter_minus_markers_equals_reading"]=strip(tel_d)==rd_d
rep["03b_both_equal_approved_script_verbatim"]=strip(tel_d)==SPOKEN and rd_d==SPOKEN
want=[m[len("[SLIDE:"):-1].strip() for m in MARKERS]
got=[MK.match(s).group(1) for s in tel_d if MK.match(s)]
rep["04_markers_present_ordered"]=got==want
rep["04b_marker_count_is_13"]=len(got)==13
rep["04c_marker_positions_match_source"]=(
 [i for i,l in enumerate(LINES) if l.startswith("[SLIDE:")]==
 [i for i,l in enumerate(tel_d) if MK.match(l)])
DECK=["Title","My Career Path","01: Look Underneath the Title","Move One",
 "02: Explain What the Work Changed","Move Two","One Result: 47 to 75",
 "03: Keep Evidence Before You Need It","Move Three",
 "Three Things I Learned to Do","Before Your Next Move",
 "Capability Formation Field Kit","Watch Next"]
rep["04d_markers_map_to_slides_1_to_13"]=len(got)==len(DECK)

TITLE="How to Change Jobs Without Starting Your Career Over"
DECK_TITLE="How I Changed Jobs Without Starting My Career Over"
brief=" ".join(paras(L+"Video_1_EDITOR_ONLY_HIT_Brief_v3.0.docx"))
pub=" ".join(paras(L+"Video_1_Publishing_Package_HIT_v3.0.docx"))
rep["05_titles_intentionally_different"]=(
 TITLE!=DECK_TITLE and TITLE in brief and DECK_TITLE in brief
 and "differ INTENTIONALLY" in brief and TITLE in pub and DECK_TITLE in pub)

BAN=("EDITOR","On-screen hook","Visual:","B-roll","caption","zoom","punch-in",
     "stock footage","overlay","9:16","Related Video","direct to camera",
     "Reveal the three questions progressively","full-screen")
shorts=[f for f in sorted(os.listdir(R+"/SHORTS")) if "EDITOR_ONLY" not in f]
bad={}
for f in shorts:
    t=" ".join(paras(R+"/SHORTS/"+f)).lower()
    hits=[b for b in BAN if b.lower() in t]
    if hits: bad[f]=hits
rep["06_shorts_free_of_editor_directions"]=not bad
rep["06b_offending"]=bad
rep["07_editor_docs_labelled"]=all(
 paras(R+"/"+f)[0]=="EDITOR ONLY" for f in
 ("LONG_FORM/Video_1_EDITOR_ONLY_HIT_Brief_v3.0.docx",
  "SHORTS/Video_1_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
rep["08_exactly_four_short_recording_docs"]=len(shorts)==4
rep["08b_short_filenames"]=shorts

# 09 — the 47-to-75 boundary must appear in all five places
sh3=" ".join(paras(R+"/SHORTS/Video_1_Short_3_Result_Needs_Context.docx"))
shbrief=" ".join(paras(R+"/SHORTS/Video_1_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
longform="\n".join(rd_d)
def bounded(t):
    t=t.lower()
    return ("47" in t and "75" in t
            and "one measure" in t
            and ("with my team" in t or "team-based" in t or "with her team" in t))
places={"long_form":longform,"long_form_editor_brief":brief,"short_3":sh3,
        "shorts_editor_brief":shbrief,"publishing_package":pub}
rep["09_evidence_boundary_present"]={k:bounded(v) for k,v in places.items()}
rep["09b_evidence_boundary_all_five"]=all(rep["09_evidence_boundary_present"].values())

# 10 — no forbidden metric attached anywhere in the package
FORB=[r"30\s*%", r"30 percent", r"\$2", r"2 million", r"two million",
      r"avoided turnover", r"turnover cost"]
attached={}
for name,path in [(f,R+"/LONG_FORM/"+f) for f in sorted(os.listdir(L))
                  if f.endswith(".docx")]+[(f,R+"/SHORTS/"+f)
                  for f in sorted(os.listdir(R+"/SHORTS"))]:
    t=" ".join(paras(path))
    hits=[p for p in FORB if re.search(p,t,re.I)]
    # the editor briefs legitimately name these figures in order to FORBID them
    if hits and "EDITOR_ONLY" not in name: attached[name]=hits
rep["10_no_forbidden_metric_in_recording_or_publishing_copy"]=not attached
rep["10b_offending"]=attached
rep["10c_editor_briefs_explicitly_forbid_them"]=(
 "Do not attach" in brief and "Do not add the 30% retention" in shbrief)

# 11 — portability / relearning boundary explicit in the spoken script
BOUND=["Not everything transfers.",
 "Some knowledge belongs to the company, industry, regulation or relationships around the work. A move can require real relearning.",
 "But being new to a context is not the same as being new to every underlying problem."]
rep["11_portability_boundary_verbatim"]=all(b in rd_d for b in BOUND)

# 12 — no recording copy tells a viewer to retain what they may not keep
PERM=["Nothing confidential.","Nothing employer-owned.",
      "So create a permitted, high-level record in your own words.",
      "Your record does not need the employer’s files."]
rep["12_permission_boundary_verbatim"]=all(p in rd_d for p in PERM)
UNSAFE=("download","forward the","usb","screenshot","copy the file",
        "export the","take the file","save the file","email yourself")
uns={}
for f in [L+"Video1ReadingScriptnomarkers_HIT_v3.0.docx"]+[R+"/SHORTS/"+s for s in shorts]:
    t=" ".join(paras(f)).lower()
    h=[u for u in UNSAFE if u in t]
    if h: uns[os.path.basename(f)]=h
rep["12b_no_unsafe_retention_instruction"]=not uns
rep["12c_offending"]=uns

# 13-17 — nothing outside this package changed
git=lambda *a: subprocess.run(["git","-C","/home/user/temidayoafonja-site"]+list(a),
                              capture_output=True,text=True).stdout
dirty=[l for l in git("status","--porcelain").splitlines()
       if "video-1-slides/hit-final" not in l and "SERIES_STATUS_TRACKER" not in l]
rep["13_17_nothing_else_modified"]=not dirty
rep["13_17b_unexpected_changes"]=dirty

body="\n".join(rd_d)
rep["reading_has_no_markers"]="SLIDE" not in body and "[SLIDE" not in body
rep["reading_has_no_timestamps"]=not re.search(r'\d+:\d\d',body)
rep["canonical_spoken_paragraphs"]=len(SPOKEN)
rep["canonical_spoken_words"]=sum(len(p.split()) for p in SPOKEN)

# 20-26 — packaging
ZIP="/tmp/v1hit/Video_1_HIT_FINAL_Recording_and_Shorts_Package.zip"
EXPECT=["Video_1_HIT_FINAL/"+m for m in [
 "LONG_FORM/Video1TeleprompterScriptwithslidemarkers_HIT_v3.0.docx",
 "LONG_FORM/Video1TeleprompterScriptwithslidemarkers_HIT_v3.0.txt",
 "LONG_FORM/Video1ReadingScriptnomarkers_HIT_v3.0.docx",
 "LONG_FORM/Video1ReadingScriptnomarkers_HIT_v3.0.txt",
 "LONG_FORM/Video_1_EDITOR_ONLY_HIT_Brief_v3.0.docx",
 "LONG_FORM/Video_1_Publishing_Package_HIT_v3.0.docx",
 "SHORTS/Video_1_Short_1_New_Context_Not_Zero.docx",
 "SHORTS/Video_1_Short_2_Experience_Needs_Evidence.docx",
 "SHORTS/Video_1_Short_3_Result_Needs_Context.docx",
 "SHORTS/Video_1_Short_4_Look_Under_The_Title.docx",
 "SHORTS/Video_1_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "README_FINAL.txt","SHA256SUMS.txt"]]
zf=zipfile.ZipFile(ZIP); names=zf.namelist()
rep["21_zip_file_count"]=len(names)
rep["21b_zip_count_is_13"]=len(names)==13
rep["20_zip_contents_exactly_as_specified"]=sorted(names)==sorted(EXPECT)
rep["22_no_source_folder"]=not any("_source" in n for n in names)
rep["22b_no_python_files"]=not any(n.endswith((".py",".pyc")) for n in names)
rep["22c_no_images_temp_or_hidden"]=not any(
 n.endswith((".png",".jpg",".jpeg",".gif",".pdf",".tmp","~")) or
 os.path.basename(n).startswith(".") for n in names)
rep["22d_zip_integrity"]=zf.testzip() is None
sums=zf.read("Video_1_HIT_FINAL/SHA256SUMS.txt").decode()
entries=[l for l in sums.splitlines() if l.strip() and not l.startswith("#")]
rep["24_sums_entry_count"]=len(entries)
rep["24b_sums_has_12_entries"]=len(entries)==12
rep["24c_sums_does_not_hash_itself"]=not any("SHA256SUMS.txt" in e for e in entries)
rep["24d_sums_has_no_zip_or_python_entry"]=not any(
 ".zip" in e or ".py" in e or "_source" in e for e in entries)
badh=[]
for e in entries:
    h,rel_=e.split("  ",1)
    if hashlib.sha256(zf.read("Video_1_HIT_FINAL/"+rel_)).hexdigest()!=h: badh.append(rel_)
rep["25_every_listed_hash_matches"]=not badh
rep["25b_mismatched"]=badh
rep["25c_sums_identical_inside_and_outside_zip"]=(
 zf.read("Video_1_HIT_FINAL/SHA256SUMS.txt")==open(R+"/SHA256SUMS.txt","rb").read())
readme=zf.read("Video_1_HIT_FINAL/README_FINAL.txt").decode()
listed=[l.strip() for l in readme.split("ALL FILES IN THIS PACKAGE")[1].splitlines()
        if l.strip().endswith((".docx",".txt"))]
rep["23_readme_lists_13_files"]=len(listed)==13
rep["23b_readme_matches_archive"]=sorted(x.split("/")[-1] for x in listed)==sorted(
 n.split("/")[-1] for n in EXPECT)
sib=ZIP+".sha256"
zh=hashlib.sha256(open(ZIP,"rb").read()).hexdigest()
rep["26_sibling_checksum_matches"]=os.path.isfile(sib) and open(sib).read().split()[0]==zh
rep["26b_zip_sha256"]=zh
rep["27_chapters_marked_working_estimates"]=(
 "WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT" in pub)

ok=all(v for k,v in rep.items() if isinstance(v,bool))
rep["ALL_BOOLEAN_CHECKS_PASS"]=ok
print(json.dumps(rep,indent=1,ensure_ascii=False))
