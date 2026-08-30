# -*- coding: utf-8 -*-
"""Video 7 script-identity and QA verification. Everything here is measured."""
import os, re, sys, json, zipfile
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
HDR = re.compile(r'^\d+:\d\d[–-]\d+:\d\d\s*\|')
MARK = re.compile(r'^SLIDE (\d+)\s+—')

PKG = os.path.join(ROOT,
    "YouTube_Video_7_Production_Package_Impact_Without_Blueprint.docx")
TEL = os.path.join(HERE, "Video_7_Teleprompter_Script_with_Slide_Markers.docx")
TXT = os.path.join(HERE, "Video_7_Recording_Script_Clean.txt")


def paras(path):
    z = zipfile.ZipFile(path)
    x = ET.fromstring(z.read('word/document.xml'))
    t = lambda p: ''.join(e.text or '' for e in p.iter(NS + 't'))
    return [t(el) for el in x.find(NS + 'body') if el.tag == NS + 'p']


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
TITLE = "How to Show Your Impact at Work When You Built It From Scratch"
KEY = "how to show your impact at work"
URL = "temidayoafonja.com/keep-the-proof"
THUMB = "MAKE INVISIBLE WORK VISIBLE"
pkg_all = "\n".join(paras(PKG))
tel_all = "\n".join(paras(TEL))
rep["title_in_package"] = TITLE in pkg_all
rep["title_in_teleprompter"] = TITLE in tel_all
rep["keyword_in_package"] = KEY in pkg_all
rep["keyword_opens_description"] = "difficult to show your impact at work" in pkg_all
rep["cta_url_in_package"] = URL in pkg_all
rep["cta_url_in_clean_script"] = URL in body
rep["thumbnail_copy_in_package"] = THUMB in pkg_all
rep["cta_name_in_package"] = "Keep the Proof" in pkg_all

# excluded metrics must appear nowhere in the spoken script
lowered = body.lower()
rep["no_retention_metric_in_script"] = "30%" not in body and "30 per cent" not in lowered
rep["no_turnover_metric_in_script"] = ("$2" not in body and "2 million" not in lowered
                                       and "turnover" not in lowered)
rep["no_tubebuddy_in_script"] = "tubebuddy" not in lowered
rep["no_competing_offer_in_script"] = not any(
    x in lowered for x in ("field kit", "fieldkit", "career decision evidence check",
                           "career-decisions"))
rep["permitted_evidence_boundary_spoken"] = "employer-owned" in lowered
rep["no_promotion_promise"] = not re.search(
    r'(will|guarantee[sd]?) (get|earn|lead to) (you )?(a )?(promotion|promoted)',
    lowered)

ok = all(v for k, v in rep.items()
         if isinstance(v, bool))
rep["ALL_CHECKS_PASS"] = ok
print(json.dumps(rep, indent=2, ensure_ascii=False))
sys.exit(0 if ok else 1)
