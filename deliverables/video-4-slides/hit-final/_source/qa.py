# -*- coding: utf-8 -*-
"""Video 4 H.I.T. package QA. Offsets are found, not assumed."""
import zipfile, re, sys, os, json, hashlib, subprocess, glob
from xml.etree import ElementTree as ET
sys.path.insert(0,'/tmp/v4hit')
from script_text import LINES, SPOKEN, MARKERS
NS='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R="/tmp/v4hit/Video_4_HIT_FINAL"
MK=re.compile(r'^SLIDE\s+—\s+(.+)$')

def paras(p):
    x=ET.fromstring(zipfile.ZipFile(p).read('word/document.xml'))
    t=lambda q:''.join(e.text or '' for e in q.iter(NS+'t'))
    return [t(el).strip() for el in x.find(NS+'body') if el.tag==NS+'p' and t(el).strip()]
def from_first_spoken(s): return s[s.index(SPOKEN[0]):]
def txt_paras(p):
    return [b.strip() for b in open(p).read().strip().split("\n\n") if b.strip()]

L=R+"/LONG_FORM/"
tel_d=from_first_spoken(paras(L+"Video4TeleprompterScriptwithslidemarkers_HIT_v2.0.docx"))
tel_t=from_first_spoken(txt_paras(L+"Video4TeleprompterScriptwithslidemarkers_HIT_v2.0.txt"))
rd_d =from_first_spoken(paras(L+"Video4ReadingScriptnomarkers_HIT_v2.0.docx"))
rd_t =from_first_spoken(txt_paras(L+"Video4ReadingScriptnomarkers_HIT_v2.0.txt"))
strip=lambda s:[x for x in s if not MK.match(x)]
rep={}
rep["01_teleprompter_docx_equals_txt"]=tel_d==tel_t
rep["02_reading_docx_equals_txt"]=rd_d==rd_t
rep["03_teleprompter_minus_markers_equals_reading"]=strip(tel_d)==rd_d
rep["03b_both_equal_approved_script_verbatim"]=strip(tel_d)==SPOKEN and rd_d==SPOKEN

DECK=["Career Path","Chronology / Portability","1 — Name the Chapters Briefly",
 "2 — Find the Repeated Work","Look Beneath the Nouns",
 "3 — Explain the Direction","Three-Sentence Structure",
 "Do Not Invent a Perfect Plan","Explanation Test","Keep the Proof",
 "Watch Next"]
want=[m[len("[SLIDE:"):-1].strip() for m in MARKERS]
got=[MK.match(s).group(1) for s in tel_d if MK.match(s)]
rep["04_markers_ordered_and_mapped"]=got==want==DECK
rep["04b_marker_count_is_11"]=len(got)==11
rep["04c_marker_positions_match_source"]=(
 [i for i,l in enumerate(LINES) if l.startswith("[SLIDE:")]==
 [i for i,l in enumerate(tel_d) if MK.match(l)])

shorts=[f for f in sorted(os.listdir(R+"/SHORTS")) if "EDITOR_ONLY" not in f]
rep["05_exactly_four_short_recording_docs"]=len(shorts)==4
rep["05b_short_filenames"]=shorts
BAN=("EDITOR","On-screen hook","Visual:","B-roll","caption","zoom","punch-in",
     "stock footage","overlay","9:16","Related Video","direct to camera",
     "Reveal progressively","End on:","End visually on")
bad={}
for f in shorts:
    t=" ".join(paras(R+"/SHORTS/"+f)).lower()
    h=[b for b in BAN if b.lower() in t]
    if h: bad[f]=h
rep["06_shorts_free_of_editor_directions"]=not bad
rep["06b_offending"]=bad
rep["07_editor_docs_labelled"]=all(
 paras(R+"/"+f)[0]=="EDITOR ONLY" for f in
 ("LONG_FORM/Video_4_EDITOR_ONLY_HIT_Brief_v2.0.docx",
  "SHORTS/Video_4_Shorts_EDITOR_ONLY_HIT_Brief.docx"))

brief=" ".join(paras(L+"Video_4_EDITOR_ONLY_HIT_Brief_v2.0.docx"))
pub=" ".join(paras(L+"Video_4_Publishing_Package_HIT_v2.0.docx"))
shbrief=" ".join(paras(R+"/SHORTS/Video_4_Shorts_EDITOR_ONLY_HIT_Brief.docx"))
sh1=" ".join(paras(R+"/SHORTS/Video_4_Short_1_Cat_With_Nine_Lives.docx"))
sh3=" ".join(paras(R+"/SHORTS/Video_4_Short_3_Not_A_Perfect_Plan.docx"))
longform="\n".join(rd_d)
ALLDOCS={os.path.basename(p):" ".join(paras(p)) for p in
         glob.glob(R+"/LONG_FORM/*.docx")+glob.glob(R+"/SHORTS/*.docx")}

# 08 / 09 — the "cat with nine lives" factual boundary
rep["08_established_description_present"]=(
 "A senior colleague once called me a cat with nine lives." in rd_d
 and "senior-manager friends at EY" in pub
 and "ESTABLISHED" in brief and "NOT ESTABLISHED" in brief)
INVENTED=("the meeting","in that meeting","she laughed","I laughed","we were sitting",
 "over coffee","in the hallway","the first time she said","she turned to me",
 "I remember the day","it was during a")
inv={n:[p for p in INVENTED if p.lower() in t.lower()] for n,t in ALLDOCS.items()}
rep["09_no_invented_original_conversation"]=not any(inv.values())
rep["09b_offending"]={k:v for k,v in inv.items() if v}

# 10 — cat imagery may appear only as an explicit prohibition.
# Evaluated per paragraph, carrying a "Do not use:" lead-in forward across the
# bullet paragraphs it governs, so a bullet is judged in its real context.
ALLDOC_PARAS={os.path.basename(p):paras(p) for p in
              glob.glob(R+"/LONG_FORM/*.docx")+glob.glob(R+"/SHORTS/*.docx")}
PROHIBIT=re.compile(r'do not|don’t|do NOT|no cat|avoid|never', re.I)
LEADIN=re.compile(r'^(do not use|do not add|avoid)\s*:?\s*$', re.I)
catmentions=[]
for name, ps in ALLDOC_PARAS.items():
    under_prohibition=False
    for para in ps:
        if LEADIN.match(para.strip()): under_prohibition=True; continue
        is_bullet=para.strip().startswith("—")
        if not is_bullet and not LEADIN.match(para.strip()): 
            if not para.strip().startswith("—"): under_prohibition = under_prohibition and is_bullet
        if re.search(r'\bcats?\b', para, re.I) and "nine lives" not in para.lower():
            ok_here = bool(PROHIBIT.search(para)) or under_prohibition
            catmentions.append({"doc":name,"text":para[:90],"prohibition":ok_here})
rep["10_cat_imagery_only_as_prohibition"]=all(m["prohibition"] for m in catmentions)
rep["10b_cat_mentions"]=catmentions
# and no recording document may mention a cat except in the approved hook line
recdocs=[R+"/SHORTS/"+f for f in shorts]+[L+"Video4ReadingScriptnomarkers_HIT_v2.0.docx"]
stray=[]
for f in recdocs:
    for para in paras(f):
        if re.search(r'\bcats?\b',para,re.I) and "cat with nine lives" not in para.lower():
            stray.append((os.path.basename(f),para[:70]))
rep["10c_recording_copy_cat_only_in_approved_hook"]=not stray
rep["10d_stray"]=stray

# 11 — 2008 context accurate
rep["11_2008_context_accurate"]=(
 "For me, the 2008 financial crisis is relevant context." in rd_d
 and "I graduated with an accounting degree in December 2008, during the "
     "financial crisis." in paras(R+"/SHORTS/Video_4_Short_3_Not_A_Perfect_Plan.docx"))

# 12 / 13 — planning and relearning boundaries
PLAN=["It does not say every move was planned.",
 "Coherence is not the same as claiming that every move was strategic.",
 "The goal is not to make your career look linear."]
rep["12_no_claim_every_move_planned"]=all(p in rd_d for p in PLAN)
RELEARN=["Some knowledge belonged to the context I was leaving, and every move "
 "required real learning.",
 "And it does not claim that everything I learned transferred automatically.",
 "A truthful career explanation can include interruption, redirection and "
 "relearning."]
rep["13_relearning_boundary_explicit"]=all(p in rd_d for p in RELEARN)

# 14 — no unsupported metric anywhere
METRIC=[r"\b\d{1,3}\s*%", r"\$\s*\d", r"\b\d+\s*million", r"\bNPS\b",
        r"\b47\b", r"\b75\b", r"\bROI\b"]
mets={n:[p for p in METRIC if re.search(p,t)] for n,t in ALLDOCS.items()}
rep["14_no_unsupported_metric"]=not any(mets.values())
rep["14b_offending"]={k:v for k,v in mets.items() if v}

# 15 — retention language stays inside permission
rep["15_permission_boundary_verbatim"]=(
 "Use only your own recollection and information you are permitted to retain." in rd_d
 and "Do not take confidential, proprietary, customer, employee or "
     "employer-owned material." in rd_d)
UNSAFE=("download","forward the","usb","screenshot","copy the file","export the",
        "take the file","save the file","email yourself")
uns={}
for f in [L+"Video4ReadingScriptnomarkers_HIT_v2.0.docx"]+[R+"/SHORTS/"+s for s in shorts]:
    t=" ".join(paras(f)).lower()
    h=[u for u in UNSAFE if u in t]
    if h: uns[os.path.basename(f)]=h
rep["15b_no_unsafe_retention_instruction"]=not uns

# 16 / 17 — single CTA, correct watch-next
OTHER=("Capability Formation Field Kit","Career Decision Evidence Check",
       "/fieldkit","/career-decisions","The Capability Audit","Maven")
leak={}
for n,t in ALLDOCS.items():
    h=[o for o in OTHER if o in t]
    # the editor brief names the other two only in order to forbid them
    if h and "EDITOR_ONLY_HIT_Brief_v2.0" not in n: leak[n]=h
rep["16_keep_the_proof_is_sole_cta"]=not leak
rep["16b_offending"]=leak
rep["16c_cta_url_present"]=all("temidayoafonja.com/keep-the-proof" in t
    for t in (longform,brief,pub))
rep["17_watch_next_is_video_5"]=(
 "Watch Should I Make an Internal Move? 3 Questions to Decide next." in rd_d
 and "Should I Make an Internal Move? 3 Questions to Decide" in brief
 and "Should I Make an Internal Move? 3 Questions to Decide" in pub)

# 18-21 — nothing outside this package changed
git=lambda *a: subprocess.run(["git","-C","/home/user/temidayoafonja-site"]+list(a),
                              capture_output=True,text=True).stdout
dirty=[l for l in git("status","--porcelain").splitlines()
       if "video-4-slides/hit-final" not in l and "SERIES_STATUS_TRACKER" not in l]
rep["18_21_nothing_else_modified"]=not dirty
rep["18_21b_unexpected_changes"]=dirty

body="\n".join(rd_d)
rep["reading_has_no_markers"]="SLIDE" not in body and "[SLIDE" not in body
rep["reading_has_no_timestamps"]=not re.search(r'\d+:\d\d',body)
rep["canonical_spoken_paragraphs"]=len(SPOKEN)
rep["canonical_spoken_words"]=sum(len(p.split()) for p in SPOKEN)

# 24-30 — packaging
ZIP="/tmp/v4hit/Video_4_HIT_FINAL_Recording_and_Shorts_Package.zip"
EXPECT=["Video_4_HIT_FINAL/"+m for m in [
 "LONG_FORM/Video4TeleprompterScriptwithslidemarkers_HIT_v2.0.docx",
 "LONG_FORM/Video4TeleprompterScriptwithslidemarkers_HIT_v2.0.txt",
 "LONG_FORM/Video4ReadingScriptnomarkers_HIT_v2.0.docx",
 "LONG_FORM/Video4ReadingScriptnomarkers_HIT_v2.0.txt",
 "LONG_FORM/Video_4_EDITOR_ONLY_HIT_Brief_v2.0.docx",
 "LONG_FORM/Video_4_Publishing_Package_HIT_v2.0.docx",
 "SHORTS/Video_4_Short_1_Cat_With_Nine_Lives.docx",
 "SHORTS/Video_4_Short_2_Chronology_Not_Explanation.docx",
 "SHORTS/Video_4_Short_3_Not_A_Perfect_Plan.docx",
 "SHORTS/Video_4_Short_4_Three_Sentences.docx",
 "SHORTS/Video_4_Shorts_EDITOR_ONLY_HIT_Brief.docx",
 "README_FINAL.txt","SHA256SUMS.txt"]]
zf=zipfile.ZipFile(ZIP); names=zf.namelist()
rep["25_zip_file_count"]=len(names)
rep["25b_zip_count_is_13"]=len(names)==13
rep["24_zip_contents_exactly_as_specified"]=sorted(names)==sorted(EXPECT)
rep["26_no_source_folder"]=not any("_source" in n for n in names)
rep["26b_no_python_files"]=not any(n.endswith((".py",".pyc")) for n in names)
rep["26c_no_images_temp_or_hidden"]=not any(
 n.endswith((".png",".jpg",".pdf",".tmp","~")) or
 os.path.basename(n).startswith(".") for n in names)
rep["26d_zip_integrity"]=zf.testzip() is None
sums=zf.read("Video_4_HIT_FINAL/SHA256SUMS.txt").decode()
entries=[l for l in sums.splitlines() if l.strip() and not l.startswith("#")]
rep["28_sums_entry_count"]=len(entries)
rep["28b_sums_has_12_entries"]=len(entries)==12
rep["28c_sums_does_not_hash_itself"]=not any("SHA256SUMS.txt" in e for e in entries)
rep["28d_sums_has_no_zip_entry"]=not any(".zip" in e or ".py" in e for e in entries)
badh=[e.split("  ",1)[1] for e in entries
      if hashlib.sha256(zf.read("Video_4_HIT_FINAL/"+e.split("  ",1)[1])).hexdigest()
         != e.split("  ",1)[0]]
rep["29_every_listed_hash_matches"]=not badh
rep["29b_sums_identical_inside_and_outside_zip"]=(
 zf.read("Video_4_HIT_FINAL/SHA256SUMS.txt")==open(R+"/SHA256SUMS.txt","rb").read())
readme=zf.read("Video_4_HIT_FINAL/README_FINAL.txt").decode()
listed=[l.strip() for l in readme.split("ALL FILES IN THIS PACKAGE")[1].splitlines()
        if l.strip().endswith((".docx",".txt"))]
rep["27_readme_lists_13_files"]=len(listed)==13
rep["27b_readme_matches_archive"]=sorted(x.split("/")[-1] for x in listed)==sorted(
 n.split("/")[-1] for n in EXPECT)
sib=ZIP+".sha256"
zh=hashlib.sha256(open(ZIP,"rb").read()).hexdigest()
rep["30_sibling_checksum_matches"]=os.path.isfile(sib) and open(sib).read().split()[0]==zh
rep["30b_zip_sha256"]=zh
rep["31_chapters_marked_working_estimates"]=(
 "WORKING ESTIMATES — EDITOR MUST REPLACE FROM FINAL CUT" in pub)

# description is copy-ready, as established for Video 1
pubp=paras(L+"Video_4_Publishing_Package_HIT_v2.0.docx")
CH=["00:00 When a Career Looks Disconnected","01:10 Chronology vs. Portability",
 "01:55 Name the Chapters Briefly","02:55 Find the Repeated Work",
 "03:20 Look Beneath the Job Titles","04:30 Explain Why the Direction Follows",
 "04:50 The Three-Sentence Career Explanation",
 "05:45 Do Not Invent a Perfect Plan","06:30 Test Your Career Explanation",
 "07:55 Keep the Proof Behind Your Story",
 "08:35 Should You Make an Internal Move?"]
ci=pubp.index("CHAPTERS"); bi=pubp.index("— END OF THE COPY-READY DESCRIPTION —")
rep["D1_all_eleven_chapter_lines_in_description"]=pubp[ci+1:ci+12]==CH
rep["D2_no_placeholder_in_description"]=not any("[INSERT" in p.upper() for p in pubp[:bi])
rep["D3_warning_outside_description"]=(
 not any("WORKING ESTIMATES" in p for p in pubp[:bi])
 and any("WORKING ESTIMATES" in p for p in pubp[bi:]))
rs=pubp.index("Working chapters — reference copy")
rep["D4_reference_matches_description"]=pubp[rs+2:rs+13]==CH

# rendered page counts, filled in after rendering
pages={}
for f in sorted(glob.glob("/tmp/render/V4_*-p01.png")):
    stem=f[:-8]
    pages[os.path.basename(stem)[3:]]=len(glob.glob(stem+"-p*.png"))
rep["22_23_rendered_page_counts"]=pages

ok=all(v for k,v in rep.items() if isinstance(v,bool))
rep["ALL_BOOLEAN_CHECKS_PASS"]=ok
print(json.dumps(rep,indent=1,ensure_ascii=False))
