# -*- coding: utf-8 -*-
"""Video 5 H.I.T. package QA, including the canonical source comparison."""
import zipfile, re, sys, os, json, hashlib, subprocess, glob, unicodedata
from xml.etree import ElementTree as ET
sys.path.insert(0,'/tmp/v5hit')
from script_text import LINES, SPOKEN, MARKERS
NS='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R="/tmp/v5hit/Video_5_HIT_FINAL"
MK=re.compile(r'^SLIDE\s+—\s+(.+)$')
CANON_FILE=("/root/.claude/uploads/f121668d-e262-5eb8-9b22-0eaa1006a361/"
            "95568f64-Video_5_Code_Prompt_HIT_Final.txt")

def paras(p):
    x=ET.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
    t=lambda q:''.join(e.text or '' for e in q.iter(NS+'t'))
    return [t(el).strip() for el in x.find(NS+'body') if el.tag==NS+'p' and t(el).strip()]
def txt_blocks(p):
    return [b.strip() for b in open(p,encoding="utf-8").read().strip().split("\n\n") if b.strip()]

L=R+"/LONG_FORM/"
rep={}

# ---- canonical source comparison, run in this same build pass --------------
raw=open(CANON_FILE,encoding="utf-8").read()
body=raw.split("BEGIN APPROVED VIDEO 5 SCRIPT",1)[1].split("END APPROVED VIDEO 5 SCRIPT",1)[0]
CANON=[b.strip() for b in body.split("\n\n") if b.strip()]
CANON_SPOKEN=[b for b in CANON if not b.startswith("[SLIDE:")]
CANON_MARKERS=[(i,b) for i,b in enumerate(CANON) if b.startswith("[SLIDE:")]

tel=txt_blocks(L+"Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.txt")
rd =txt_blocks(L+"Video5ReadingScriptnomarkers_HIT_v2.0.txt")
tel=tel[tel.index(CANON_SPOKEN[0]):]
rd = rd[rd.index(CANON_SPOKEN[0]):]
tel_spoken=[b for b in tel if not b.startswith("SLIDE  —")]

def first_diff(got,want):
    for i,(a,b) in enumerate(zip(got,want)):
        if a!=b:
            for j,(ca,cb) in enumerate(zip(a,b)):
                if ca!=cb:
                    return {"paragraph":i+1,"source":b,"package":a,"char":j,
                            "source_char":"%r U+%04X %s"%(cb,ord(cb),unicodedata.name(cb,'?')),
                            "package_char":"%r U+%04X %s"%(ca,ord(ca),unicodedata.name(ca,'?'))}
            return {"paragraph":i+1,"source":b,"package":a,"note":"length differs"}
    return {"note":"one is a prefix of the other"}

s_="\n\n".join(CANON_SPOKEN); t_="\n\n".join(rd); u_="\n\n".join(tel_spoken)
sv={"canonical_file":os.path.basename(CANON_FILE).split("-",1)[1],
    "canonical_file_sha256":hashlib.sha256(open(CANON_FILE,'rb').read()).hexdigest(),
    "method":"Extracted between the BEGIN/END APPROVED VIDEO 5 SCRIPT fences and "
             "compared literally. No normalisation of any kind.",
    "source_blocks":len(CANON),"source_markers":len(CANON_MARKERS),
    "source_spoken_paragraphs":len(CANON_SPOKEN),
    "source_spoken_words":sum(len(b.split()) for b in CANON_SPOKEN),
    "teleprompter_minus_markers_equals_source":tel_spoken==CANON_SPOKEN,
    "reading_script_equals_source":rd==CANON_SPOKEN,
    "characters_source":len(s_),"characters_reading":len(t_),
    "characters_teleprompter_minus_markers":len(u_),
    "sha256_joined_spoken_text":hashlib.sha256(s_.encode()).hexdigest(),
    "sha256_identical_across_all_three":
      hashlib.sha256(s_.encode()).hexdigest()==hashlib.sha256(t_.encode()).hexdigest()
      ==hashlib.sha256(u_.encode()).hexdigest(),
    "per_character_class":{k:(s_.count(v),t_.count(v),u_.count(v))
      for k,v in {"apostrophe":"’","left_quote":"“","right_quote":"”",
                  "em_dash":"—","ellipsis":"…"}.items()},
    "capital_letters":(sum(c.isupper() for c in s_),sum(c.isupper() for c in t_),
                       sum(c.isupper() for c in u_)),
    "checked":["every word","punctuation","apostrophes","quotation marks",
               "em dashes","capitalization","paragraph order"]}
if not sv["teleprompter_minus_markers_equals_source"]:
    sv["teleprompter_first_difference"]=first_diff(tel_spoken,CANON_SPOKEN)
if not sv["reading_script_equals_source"]:
    sv["reading_first_difference"]=first_diff(rd,CANON_SPOKEN)
tel_markers=[(i,b) for i,b in enumerate(tel) if b.startswith("SLIDE  —")]
sv["marker_names_match"]=([c[1][len("[SLIDE:"):-1].strip() for c in CANON_MARKERS]==
                          [m[1][len("SLIDE  —"):].strip() for m in tel_markers])
sv["marker_positions_match"]=[c[0] for c in CANON_MARKERS]==[m[0] for m in tel_markers]
sv["status"]="PASSED" if all([sv["teleprompter_minus_markers_equals_source"],
   sv["reading_script_equals_source"],sv["marker_names_match"],
   sv["marker_positions_match"],sv["sha256_identical_across_all_three"]]) else "FAILED"
rep["SOURCE_VERIFICATION"]=sv
rep["00_canonical_source_verification_passed"]=sv["status"]=="PASSED"

# ---- the 32 checks ----------------------------------------------------------
def from_first(s): return s[s.index(SPOKEN[0]):]
tel_d=from_first(paras(L+"Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.docx"))
rd_d =from_first(paras(L+"Video5ReadingScriptnomarkers_HIT_v2.0.docx"))
strip=lambda s:[x for x in s if not MK.match(x)]
rep["01_teleprompter_docx_equals_txt"]=tel_d==tel
rep["02_reading_docx_equals_txt"]=rd_d==rd
rep["03_teleprompter_minus_markers_equals_reading"]=strip(tel_d)==rd_d
rep["03b_both_equal_approved_script_verbatim"]=strip(tel_d)==SPOKEN and rd_d==SPOKEN

DECK=["Core Distinction","The Three Questions","1 — Will the Work Change?",
 "Access Test","2 — Will Your Judgment Expand?","More Tasks / More Judgment",
 "3 — Will the Evidence Travel?","Result / Judgment / Range","Decision Read",
 "Conversation Prompts","Career Decision Evidence Check","Watch Next"]
got=[MK.match(s).group(1) for s in tel_d if MK.match(s)]
rep["04_markers_ordered_and_mapped"]=got==DECK
rep["04b_marker_count_is_12"]=len(got)==12

shorts=[f for f in sorted(os.listdir(R+"/SHORTS")) if "EDITOR_ONLY" not in f]
rep["05_exactly_four_short_recording_docs"]=len(shorts)==4
rep["05b_short_filenames"]=shorts
BAN=("EDITOR","On-screen hook","Visual:","B-roll","caption","zoom","punch-in",
     "stock footage","overlay","9:16","Related Video","direct to camera",
     "Reveal progressively","End on:","two-column","FACTUAL BOUNDARY")
bad={f:[b for b in BAN if b.lower() in " ".join(paras(R+"/SHORTS/"+f)).lower()]
     for f in shorts}
bad={k:v for k,v in bad.items() if v}
rep["06_shorts_free_of_editor_directions"]=not bad
rep["06b_offending"]=bad
rep["07_editor_docs_labelled"]=all(paras(R+"/"+f)[0]=="EDITOR ONLY" for f in
 ("LONG_FORM/Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx",
  "SHORTS/Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx"))

brief=" ".join(paras(L+"Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx"))
pub=" ".join(paras(L+"Video_5_Publishing_Package_HIT_v2.0.docx"))
shbrief=" ".join(paras(R+"/SHORTS/Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
ALL={os.path.basename(p):" ".join(paras(p)) for p in
     glob.glob(R+"/LONG_FORM/*.docx")+glob.glob(R+"/SHORTS/*.docx")}

# 08 — the scope-expansion proof stays bounded
rep["08_proof_boundary_stated_in_briefs"]=(
 "scope expanded after roughly six months" in brief
 and "beyond the original box" in brief
 and "FACTUAL BOUNDARY" in brief and "FACTUAL BOUNDARY" in shbrief)
INVENT=("EY","Deloitte","my employer at the time","the company I worked for",
        "as a director","as a manager at","promoted to","my boss said",
        "revenue","headcount","budget of")
inv={n:[x for x in INVENT if re.search(r'\b%s\b'%re.escape(x),t,re.I)]
     for n,t in ALL.items()}
inv={k:v for k,v in inv.items() if v}
rep["08b_no_invented_employer_role_or_metric"]=not inv
rep["08c_offending"]=inv
METRIC=[r"\b\d{1,3}\s*%", r"\$\s*\d", r"\b\d+\s*million", r"\bNPS\b", r"\bROI\b"]
mets={n:[p for p in METRIC if re.search(p,t)] for n,t in ALL.items()}
mets={k:v for k,v in mets.items() if v}
rep["08d_no_unsupported_metric"]=not mets
rep["08e_offending"]=mets

rep["09_old_1_35_exception_superseded"]=("1:35" in brief and "SUPERSEDED" in brief)
Q=["Will the work change?","Will your judgment expand?",
   "And will the evidence travel?"]
rep["10_three_question_architecture_intact"]=all(q in rd_d for q in Q)
VOL=["But movement is not automatically growth.",
 "That can make you busier without making the work more developmental.",
 "Do not call every useful move growth."]
rep["11_volume_not_treated_as_growth"]=all(v in rd_d for v in VOL)
TRADE=["That does not make the role automatically right. You still need to "
 "evaluate the manager, compensation, workload, stability and the rest of "
 "your life.",
 "A better manager, more flexibility, higher pay, stronger benefits or "
 "stability can legitimately make it the right decision.",
 "Pay, benefits, caregiving, location, immigration status, energy and timing "
 "can all legitimately change the answer."]
rep["12_decision_read_preserves_tradeoffs"]=all(t in rd_d for t in TRADE)
rep["13_safety_boundary_verbatim"]=(
 "If your health or safety is at risk, or you are dealing with harassment or "
 "discrimination, you do not need to optimize an internal-mobility strategy "
 "before protecting yourself and getting appropriate support." in rd_d)

OTHER=("Capability Formation Field Kit","Keep the Proof","/fieldkit",
       "/keep-the-proof")
leak={n:[o for o in OTHER if o in t] for n,t in ALL.items()}
leak={k:v for k,v in leak.items() if v and "EDITOR_ONLY_HIT_Brief_v2.0" not in k}
rep["14_cdec_is_sole_cta"]=not leak
rep["14b_offending"]=leak
rep["15_production_gate_recorded_satisfied"]=(
 "SATISFIED" in brief and "SATISFIED" in pub
 and "SATISFIED" in open(R+"/README_FINAL.txt",encoding="utf-8").read())
rep["16_watch_next_is_video_6"]=(
 "Watch Are You Growing—or Just Being Given More Work?" in rd_d
 and "Are You Growing—or Just Being Given More Work?" in brief
 and "Are You Growing—or Just Being Given More Work?" in pub)

git=lambda *a: subprocess.run(["git","-C","/home/user/temidayoafonja-site"]+list(a),
                              capture_output=True,text=True).stdout
dirty=[l for l in git("status","--porcelain").splitlines()
       if "video-5-slides/hit-final" not in l and "SERIES_STATUS_TRACKER" not in l
       and "CAPABILITY_FORMATION_YOUTUBE_STANDARDS" not in l]
rep["17_20_nothing_else_modified"]=not dirty
rep["17_20b_unexpected"]=dirty

# 21 — the approved restrained emoji treatment
pubp=paras(L+"Video_5_Publishing_Package_HIT_v2.0.docx")
bi=pubp.index("— END OF THE COPY-READY DESCRIPTION —")
desc=pubp[:bi]
EMOJI=["✨ Will the work change?","✨ Will your judgment expand?",
       "✨ Will the evidence travel?","🧭 CAREER DECISION EVIDENCE CHECK",
       "⏱️ CHAPTERS","▶️ WATCH NEXT","🔗 CONNECT AND EXPLORE"]
rep["21_restrained_emoji_treatment_retained"]=all(e in desc for e in EMOJI)
rep["21b_emoji_count_in_description"]=sum(
 sum(p.count(ch) for p in desc) for ch in "✨🧭⏱▶🔗")

# 22 — chapters inline, no placeholder
CH=["00:00 You May Not Need to Leave",
 "01:15 The 3 Questions for an Internal Move","01:35 Will the Work Change?",
 "03:20 Will Your Judgment Expand?","04:55 Will the Evidence Travel?",
 "06:15 Read the Pattern","07:15 What to Ask Before You Move",
 "08:50 Career Decision Evidence Check",
 "09:15 Are You Growing—or Just Being Given More Work?"]
ci=pubp.index("⏱️ CHAPTERS")
rep["22_all_chapters_inside_description"]=pubp[ci+1:ci+10]==CH
rep["22b_no_placeholder_in_description"]=not any("[INSERT" in p.upper() for p in desc)
rep["22c_warning_outside_description"]=(
 not any("WORKING ESTIMATES" in p for p in desc)
 and any("WORKING ESTIMATES" in p for p in pubp[bi:]))
rs=pubp.index("Working chapters — reference copy")
rep["22d_reference_matches_description"]=pubp[rs+2:rs+11]==CH

# 25-31 packaging
ZIP="/tmp/v5hit/Video_5_HIT_FINAL_Recording_and_Shorts_Package.zip"
EXPECT=["Video_5_HIT_FINAL/"+m for m in [
 "LONG_FORM/Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.docx",
 "LONG_FORM/Video5TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
 "LONG_FORM/Video5ReadingScriptnomarkers_HIT_v2.0.docx",
 "LONG_FORM/Video5ReadingScriptnomarkers_HIT_v2.0.txt",
 "LONG_FORM/Video_5_EDITOR_ONLY_HIT_Brief_v2.0.docx",
 "LONG_FORM/Video_5_Publishing_Package_HIT_v2.0.docx",
 "SHORTS/Video_5_Short_1_You_May_Not_Need_To_Leave.docx",
 "SHORTS/Video_5_Short_2_More_Tasks_Not_More_Judgment.docx",
 "SHORTS/Video_5_Short_3_More_Scope_Not_Automatic_Growth.docx",
 "SHORTS/Video_5_Short_4_Three_Questions_Before_You_Move.docx",
 "SHORTS/Video_5_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "README_FINAL.txt","SHA256SUMS.txt"]]
zf=zipfile.ZipFile(ZIP); names=zf.namelist()
rep["26_zip_file_count"]=len(names)
rep["26b_zip_count_is_13"]=len(names)==13
rep["25_zip_contents_exactly_as_specified"]=sorted(names)==sorted(EXPECT)
rep["27_no_source_folder"]=not any("_source" in n for n in names)
rep["27b_no_python_files"]=not any(n.endswith((".py",".pyc")) for n in names)
rep["27c_no_images_temp_hidden"]=not any(
 n.endswith((".png",".jpg",".pdf",".tmp","~")) or
 os.path.basename(n).startswith(".") for n in names)
rep["27d_zip_integrity"]=zf.testzip() is None
sums=zf.read("Video_5_HIT_FINAL/SHA256SUMS.txt").decode()
entries=[l for l in sums.splitlines() if l.strip() and not l.startswith("#")]
rep["29_sums_entry_count"]=len(entries)
rep["29b_sums_has_12_entries"]=len(entries)==12
rep["29c_sums_no_self_or_zip_entry"]=not any(
 "SHA256SUMS.txt" in e or ".zip" in e or ".py" in e for e in entries)
badh=[e.split("  ",1)[1] for e in entries
      if hashlib.sha256(zf.read("Video_5_HIT_FINAL/"+e.split("  ",1)[1])).hexdigest()
         != e.split("  ",1)[0]]
rep["30_every_listed_hash_matches"]=not badh
rep["30b_sums_identical_inside_and_outside"]=(
 zf.read("Video_5_HIT_FINAL/SHA256SUMS.txt")==open(R+"/SHA256SUMS.txt","rb").read())
readme=zf.read("Video_5_HIT_FINAL/README_FINAL.txt").decode()
listed=[l.strip() for l in readme.split("ALL FILES IN THIS PACKAGE")[1].splitlines()
        if l.strip().endswith((".docx",".txt"))]
rep["28_readme_lists_13_files"]=len(listed)==13
rep["28b_readme_matches_archive"]=sorted(x.split("/")[-1] for x in listed)==sorted(
 n.split("/")[-1] for n in EXPECT)
zh=hashlib.sha256(open(ZIP,"rb").read()).hexdigest()
rep["31_sibling_checksum_matches"]=(os.path.isfile(ZIP+".sha256")
 and open(ZIP+".sha256").read().split()[0]==zh)
rep["31b_zip_sha256"]=zh
rep["32_chapters_marked_working_estimates"]=(
 "WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT" in pub)

pages={}
for f in sorted(glob.glob("/tmp/render/V5_*-p01.png")):
    stem=f[:-8]; pages[os.path.basename(stem)[3:]]=len(glob.glob(stem+"-p*.png"))
rep["23_24_rendered_page_counts"]=pages
rep["canonical_spoken_paragraphs"]=len(SPOKEN)
rep["canonical_spoken_words"]=sum(len(p.split()) for p in SPOKEN)

ok=all(v for k,v in rep.items() if isinstance(v,bool))
rep["ALL_BOOLEAN_CHECKS_PASS"]=ok
print(json.dumps(rep,indent=1,ensure_ascii=False))
