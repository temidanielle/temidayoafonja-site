# -*- coding: utf-8 -*-
"""Video 2 H.I.T. package QA. Offsets are found, not assumed."""
import zipfile, re, sys, os, json
from xml.etree import ElementTree as ET
sys.path.insert(0,'/tmp/v2hit')
from script_text import LINES, SPOKEN, MARKERS
NS='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R="/tmp/v2hit/Video_2_HIT_FINAL"
MK=re.compile(r'^SLIDE\s+—\s+(.+)$')

def paras(p):
    x=ET.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
    t=lambda q:''.join(e.text or '' for e in q.iter(NS+'t'))
    return [t(el).strip() for el in x.find(NS+'body') if el.tag==NS+'p' and t(el).strip()]

def from_first_spoken(seq):
    """Drop any leading document furniture by finding the real first line."""
    return seq[seq.index(SPOKEN[0]):]

def txt_paras(p):
    return [b.strip() for b in open(p).read().strip().split("\n\n") if b.strip()]

L=R+"/LONG_FORM/"
tel_d = from_first_spoken(paras(L+"Video2TeleprompterScriptwithslidemarkers_HIT_v2.0.docx"))
tel_t = from_first_spoken(txt_paras(L+"Video2TeleprompterScriptwithslidemarkers_HIT_v2.0.txt"))
rd_d  = from_first_spoken(paras(L+"Video2ReadingScriptnomarkers_HIT_v2.0.docx"))
rd_t  = from_first_spoken(txt_paras(L+"Video2ReadingScriptnomarkers_HIT_v2.0.txt"))
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
BAN=("EDITOR","On-screen hook","Visual:","B-roll","caption","zoom","punch-in",
     "stock footage","overlay","9:16","Do not illustrate")
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
    ("LONG_FORM/Video_2_EDITOR_ONLY_HIT_Brief_v2.0.docx",
     "SHORTS/Video_2_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
rep["9_exactly_four_short_recording_docs"] = len(shorts)==4
rep["spoken_paragraphs"]=len(SPOKEN)
rep["spoken_words"]=sum(len(p.split()) for p in SPOKEN)
# reading files must carry no marker or production text
body="\n".join(rd_d)
rep["reading_has_no_markers"] = "SLIDE" not in body and "[SLIDE" not in body
rep["reading_has_no_timestamps"] = not re.search(r'\d+:\d\d', body)
ok=all(v for k,v in rep.items() if isinstance(v,bool))
rep["ALL_PASS"]=ok
print(json.dumps(rep, indent=1, ensure_ascii=False))
