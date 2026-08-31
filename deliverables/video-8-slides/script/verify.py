# -*- coding: utf-8 -*-
"""Video 8 script-identity and QA verification. Everything here is measured."""
import os, re, sys, json, zipfile
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
HDR = re.compile(r'^\d+:\d\d[–-]\d+:\d\d\s*\|')
MARK = re.compile(r'^SLIDE (\d+)\s+—')

PKG = os.path.join(ROOT,
    "YouTube_Video_8_Production_Package_New_Industry.docx")
TEL = os.path.join(HERE, "Video_8_Teleprompter_Script_with_Slide_Markers.docx")
TXT = os.path.join(HERE, "Video_8_Recording_Script_Clean.txt")


def paras(path):
    z = zipfile.ZipFile(path)
    x = ET.fromstring(z.read('word/document.xml'))
    t = lambda p: ''.join(e.text or '' for e in p.iter(NS + 't'))
    return [t(el) for el in x.find(NS + 'body') if el.tag == NS + 'p']


def all_text(path):
    """Paragraphs AND table cells. Several locked decisions live in tables."""
    z = zipfile.ZipFile(path)
    x = ET.fromstring(z.read('word/document.xml'))
    return "\n".join(''.join(e.text or '' for e in el.iter(NS + 't'))
                     for el in x.find(NS + 'body'))


def package_spoken():
    b = paras(PKG)
    i4 = next(i for i, s in enumerate(b) if s.strip() == '4. Full recording script')
    i5 = next(i for i, s in enumerate(b) if s.strip().startswith('5. Slide deck content'))
    return [s.strip() for s in b[i4 + 1:i5]
            if s.strip() and not HDR.match(s.strip())
            and not s.strip().startswith('Target')]


def teleprompter_spoken():
    out, marks = [], []
    for s in paras(TEL):
        t = s.strip()
        if not t:
            continue
        m = MARK.match(t)
        if m:
            marks.append(int(m.group(1))); continue
        if HDR.match(t) or t.startswith('Target'):
            continue
        out.append(t)
    # drop the three title/preamble lines
    return out[3:], marks


rep = {}
pk = package_spoken()
tel, marks = teleprompter_spoken()
clean = [s.strip() for s in open(TXT).read().strip().split("\n\n") if s.strip()]

rep["package_paragraphs"] = len(pk)
rep["teleprompter_paragraphs"] = len(tel)
rep["clean_paragraphs"] = len(clean)
rep["word_count"] = sum(len(s.split()) for s in pk)
rep["word_count_in_target_1450_1700"] = 1450 <= rep["word_count"] <= 1700
rep["clean_equals_package"] = clean == pk
rep["teleprompter_equals_package"] = tel == pk
rep["clean_equals_teleprompter"] = clean == tel
rep["slide_markers"] = marks
rep["markers_present_1_to_12"] = marks == list(range(1, 13))
body = "\n".join(clean)
rep["clean_has_no_timestamps"] = not re.search(r'\d+:\d\d', body)
rep["clean_has_no_markers"] = "SLIDE " not in body
rep["clean_has_no_directions"] = not any(
    k in body for k in ("Timing:", "Reveal ", "[", "TubeBuddy", "weighted score"))

# locked strings that must be consistent everywhere they apply
TITLE = "How to Move Into a New Industry Without Starting Over"
KEY = "how to move into a new industry"
URL = "temidayoafonja.com/fieldkit"
THUMB = "YOUR EXPERIENCE STILL COUNTS"
pkg_all = all_text(PKG)
tel_all = all_text(TEL)
rep["title_in_package"] = TITLE in pkg_all
rep["title_in_teleprompter"] = TITLE in tel_all
rep["keyword_in_package"] = KEY in pkg_all
rep["keyword_opens_description"] = "how to move into a new industry without\nstarting over" in pkg_all or "how to move into a new industry without starting over" in pkg_all.lower()
rep["cta_url_in_package"] = URL in pkg_all
rep["cta_url_in_clean_script"] = URL in body
rep["thumbnail_copy_in_package"] = THUMB in pkg_all
rep["cta_name_in_package"] = "Capability Formation Field Kit" in pkg_all

# excluded metrics must appear nowhere in the spoken script
lowered = body.lower()
rep["no_retention_metric_in_script"] = "30%" not in body and "30 per cent" not in lowered
rep["no_turnover_metric_in_script"] = ("$2" not in body and "2 million" not in lowered
                                       and "turnover" not in lowered)
rep["no_tradeoff_free_promise"] = not any(
    x in lowered for x in ("without any tradeoff", "avoid every tradeoff",
                           "guaranteed", "you will get the job"))
rep["opening_distinction_present"] = (
    "Changing industries does not make you entry-level at everything. It makes "
    "you new to a context.") in body
rep["cism_stated_within_ceiling"] = (
    "prepared for the CISM exam and did not pass the first time" in body
    and not any(x in lowered for x in ("cism score", "failed because", "second attempt",
                                       "passed on the second")))
rep["career_span_uses_ledger_wording"] = ("nearly two decades" in lowered
                                          and "18 years" not in body
                                          and "eighteen years" not in lowered)
rep["no_promotion_in_every_industry_claim"] = not any(
    x in lowered for x in ("promoted in every", "promotion in every"))
rep["no_seamless_claim"] = "seamless" not in lowered
rep["no_automatic_transfer_claim"] = "transfer automatically" not in lowered
rep["translation_sentence_present"] = "I am new to this industry, but I am not new to" in body
rep["three_columns_named"] = all(
    x in body for x in ("What travels:", "What changes:", "What I must earn:"))
rep["no_tubebuddy_in_script"] = "tubebuddy" not in lowered
rep["no_competing_offer_in_script"] = not any(
    x in lowered for x in ("keep the proof", "keep-the-proof",
                           "career decision evidence check", "career-decisions",
                           "maven", "my book"))
rep["confidentiality_boundary_spoken"] = "non-confidential" in lowered
rep["no_fabrication_permitted"] = "inventing experience" in lowered
# --- corrections applied in the targeted revision pass ---------------------
SOFTENED = [
    ("It is an information gap, and it can close when you are deliberate about "
     "learning it.",
     "closes faster than most people expect"),
    ("very little to evaluate, and experienced interviewers have heard them "
     "many times.",
     "nothing to evaluate, and experienced people stop hearing them entirely"),
    ("A clear first-ninety-days learning plan can also reduce the credibility "
     "gap.",
     "counts for more than most people expect"),
    ("You may find the first column is longer than you feared and the third is "
     "shorter than you assumed.",
     "Most people find the first column is longer than they feared"),
]
rep["softened_wording_present"] = all(new in body for new, _ in SOFTENED)
rep["superseded_wording_absent"] = all(old not in body for _, old in SOFTENED)
rep["watch_next_is_playlist_safe"] = (
    "When you are ready for the next step, continue with the Career "
    "Portability playlist." in body)
rep["script_names_no_unpublished_video"] = not any(
    x in lowered for x in ("layoff", "video 9", "what to do before"))
rep["viewer_definition_broadened"] = (
    "Experienced professionals" in pkg_all
    and "senior corporate woman" not in pkg_all)
rep["word_count_method_documented"] = "str.split() on whitespace" in pkg_all
rep["punctuation_identical_after_marker_strip"] = (
    "".join(clean) == "".join(pk) == "".join(tel))
rep["no_promotion_promise"] = not re.search(
    r'(will|guarantee[sd]?) (get|earn|lead to) (you )?(a )?(promotion|promoted)',
    lowered)

ok = all(v for k, v in rep.items()
         if isinstance(v, bool))
rep["ALL_CHECKS_PASS"] = ok
print(json.dumps(rep, indent=2, ensure_ascii=False))
sys.exit(0 if ok else 1)
