# -*- coding: utf-8 -*-
"""Video 3 H.I.T. package QA. Offsets are found, not assumed."""
import zipfile, re, sys, os, json, subprocess, hashlib
from xml.etree import ElementTree as ET
sys.path.insert(0,'/tmp/v3hit')
from script_text import LINES, SPOKEN, MARKERS
NS='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R="/tmp/v3hit/Video_3_HIT_FINAL"
MK=re.compile(r'^SLIDE\s+—\s+(.+)$')

def paras(p):
    x=ET.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
    t=lambda q:''.join(e.text or '' for e in q.iter(NS+'t'))
    return [t(el).strip() for el in x.find(NS+'body') if el.tag==NS+'p' and t(el).strip()]

def from_first_spoken(seq):
    return seq[seq.index(SPOKEN[0]):]

def txt_paras(p):
    return [b.strip() for b in open(p).read().strip().split("\n\n") if b.strip()]

L=R+"/LONG_FORM/"
tel_d = from_first_spoken(paras(L+"Video3TeleprompterScriptwithslidemarkers_HIT_v2.0.docx"))
tel_t = from_first_spoken(txt_paras(L+"Video3TeleprompterScriptwithslidemarkers_HIT_v2.0.txt"))
rd_d  = from_first_spoken(paras(L+"Video3ReadingScriptnomarkers_HIT_v2.0.docx"))
rd_t  = from_first_spoken(txt_paras(L+"Video3ReadingScriptnomarkers_HIT_v2.0.txt"))
strip = lambda s: [x for x in s if not MK.match(x)]

rep={}
rep["1_teleprompter_docx_equals_txt"] = tel_d == tel_t
rep["2_reading_docx_equals_txt"] = rd_d == rd_t
rep["3_teleprompter_minus_markers_equals_reading"] = strip(tel_d) == rd_d
rep["3b_both_equal_approved_script_verbatim"] = strip(tel_d)==SPOKEN and rd_d==SPOKEN
want=[m[len("[SLIDE:"):-1].strip() for m in MARKERS]
got=[MK.match(s).group(1) for s in tel_d if MK.match(s)]
rep["4_markers_present_ordered_sequential"] = got==want
rep["4b_marker_count"] = len(got)
rep["4c_marker_positions_match_source"] = [
    i for i,l in enumerate(LINES) if l.startswith("[SLIDE:")] == [
    i for i,l in enumerate(tel_d) if MK.match(l)]

BAN=("EDITOR","On-screen hook","Visual:","B-roll","caption","zoom","punch-in",
     "stock footage","overlay","9:16","Do not illustrate","Related Video",
     "full-screen","direct to camera","reveal progressively")
bad={}
shorts=[f for f in sorted(os.listdir(R+"/SHORTS")) if "EDITOR_ONLY" not in f]
for f in shorts:
    txt=" ".join(paras(R+"/SHORTS/"+f)).lower()
    hits=[b for b in BAN if b.lower() in txt]
    if hits: bad[f]=hits
rep["5_shorts_free_of_editor_directions"] = not bad
rep["5b_offending"] = bad
rep["6_editor_docs_labelled"] = all(
    paras(R+"/"+f)[0]=="EDITOR ONLY" for f in
    ("LONG_FORM/Video_3_EDITOR_ONLY_HIT_Brief_v2.0.docx",
     "SHORTS/Video_3_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
rep["10_exactly_four_short_recording_docs"] = len(shorts)==4
rep["10b_short_filenames"] = shorts

# 11 — safety boundary verbatim in the long-form spoken script
SAFETY=["And if your health or safety is at risk, this is not a reason to wait.",
 "If your health or safety is at risk, or you are dealing with harassment, "
 "discrimination or another urgent threat, nothing in this video is a reason "
 "to delay leaving.",
 "Act on that first."]
rep["11_safety_boundary_verbatim"] = all(s in rd_d for s in SAFETY)
rep["11b_safety_boundary_in_short_4"] = any(
 "health or safety is at risk" in p for p in
 paras(R+"/SHORTS/Video_3_Short_4_Three_Questions_Before_You_Quit.docx"))

# 12 — no recording copy tells a viewer to retain material they may not keep
PERMISSION=["If you do not have the right to keep it, do not take it.",
 "Keep only what you are entitled to retain.",
 "Confidential information, customer or employee data, proprietary documents "
 "and employer-owned material stay with the employer."]
rep["12_permission_boundary_verbatim"] = all(s in rd_d for s in PERMISSION)
UNSAFE=("download","forward the","usb","screenshot","copy the file","export the",
        "take the file","save the file","back up the","email yourself")
recording=[R+"/LONG_FORM/Video3ReadingScriptnomarkers_HIT_v2.0.docx"]+\
          [R+"/SHORTS/"+f for f in shorts]
uns={}
for f in recording:
    txt=" ".join(paras(f)).lower()
    hits=[u for u in UNSAFE if u in txt]
    if hits: uns[os.path.basename(f)]=hits
rep["12b_no_unsafe_retention_instruction"] = not uns
rep["12c_offending"] = uns

body="\n".join(rd_d)
rep["reading_has_no_markers"] = "SLIDE" not in body and "[SLIDE" not in body
rep["reading_has_no_timestamps"] = not re.search(r'\d+:\d\d', body)
rep["spoken_paragraphs"]=len(SPOKEN)
rep["spoken_words"]=sum(len(p.split()) for p in SPOKEN)

# 17 — chapters are labelled as estimates
pub=" ".join(paras(L+"Video_3_Publishing_Package_HIT_v2.0.docx"))
rep["17_chapters_marked_working_estimates"] = (
 "WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT" in pub)
rep["17b_publication_gate_stated"] = "production-live" in pub

ok=all(v for k,v in rep.items() if isinstance(v,bool))
rep["ALL_BOOLEAN_CHECKS_PASS"]=ok
print(json.dumps(rep,indent=1,ensure_ascii=False))
