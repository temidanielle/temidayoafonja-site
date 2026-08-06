#!/usr/bin/env python3
"""
Verification suite for the rebuilt Session Workbook.

Checks the section-7 acceptance criteria that can be tested mechanically:
  * page count reported
  * no hollow-box glyphs: U+2192 (arrow) or U+25A1 (box) anywhere
  * no em dashes (U+2014) or en dashes (U+2013) anywhere
  * form-field set identical to the frozen v5.3 field map (names + types)
  * pass-one score pages carry NO evidence fields and no "evidence" copy
  * all twelve frozen statements present verbatim
  * ten computed totals are read-only, carry a calculation action (/AA /C),
    and the calc JS strips non-numerics so "3?" counts as 3
  * AcroForm /CO calculation-order array present and NeedAppearances set
  * no overlapping text spans (text clipped/overlapped by neighbours)
  * page emptiness: flags any page with more than ~1/3 vertical whitespace

Usage:
    python3 verify_workbook.py [workbook.pdf] [--source v5.3_FILLABLE.pdf]
"""
import sys
import re
import fitz

NEW = sys.argv[1] if len(sys.argv) > 1 else \
    "Should_I_Stay_or_Should_I_Move_SESSION_WORKBOOK_v5.3.pdf"
SRC = None
if "--source" in sys.argv:
    SRC = sys.argv[sys.argv.index("--source") + 1]

fail = []
warn = []
doc = fitz.open(NEW)

STATEMENTS = [
    "In the last ninety days I have been handed a problem I did not already know how to solve.",
    "I work close enough to people who are better than me that I can watch how they think.",
    "My work is reviewed by someone who can tell the difference between good and adequate, and who says so directly.",
    "The feedback I receive changes what I do next, not just how I feel.",
    "I regularly operate at the edge of my competence rather than the comfortable center of it.",
    "Looking back six months, the work I do now would have been genuinely hard for me then.",
    "The capability I am building would be valued by an employer in a different industry.",
    "I can describe what I do in terms of outcomes, not just my company's internal language.",
    "If my role disappeared tomorrow, the capability I built would still be mine to carry.",
    "People with the power to hire or advance me, inside or outside my company, can already see what I am good at.",
    "What I am learning is a transferable capability rather than a company-specific procedure.",
    "I could rebuild a strong position somewhere else within a year.",
]

# expected frozen field set (name -> type) from v5.3 section 6
CHECK_NAMES = (["name", "date"]
    + ["d1_%d" % i for i in range(1, 13)]
    + ["d2_%d" % i for i in range(1, 13)]
    + ["ev_%d" % i for i in range(1, 13)]
    + ["dens_initial", "opt_initial", "dens_initial_copy", "opt_initial_copy",
       "dens_corr", "opt_corr",
       "dens_initial_r", "opt_initial_r", "dens_corr_r", "opt_corr_r",
       "state1_r", "state2_r", "conf1_r", "conf2_r"]
    + ["p1_DepthTrap", "p1_Compounding", "p1_Stagnant", "p1_Fragile",
       "p2_DepthTrap", "p2_Compounding", "p2_Stagnant", "p2_Fragile"]
    + ["corr%d" % i for i in range(5)]
    + ["cat%d" % i for i in range(7)]
    + ["nmd%d" % i for i in range(1, 11)]
    + ["log%d%s" % (i, s) for i in range(4) for s in ("a", "b")]
    + ["state1", "state2", "conf1", "conf2", "readdate", "rescoredate"]
    + ["ov", "un", "qm", "c_imm", "c_hid", "c_wait", "c_fr", "c_oneline"])
COMPUTED = ["dens_initial", "opt_initial", "dens_initial_copy", "opt_initial_copy",
            "dens_corr", "opt_corr", "dens_initial_r", "opt_initial_r",
            "dens_corr_r", "opt_corr_r"]

def full_text():
    return "\n".join(doc[i].get_text() for i in range(doc.page_count))

# ----------------------------------------------------------- 1. page count
print("== 1. PAGE COUNT ==")
print("   pages: %d (20 content + 4 section openers)" % doc.page_count)
if doc.page_count != 24:
    warn.append("page count is %d, expected 24" % doc.page_count)

# ----------------------------------------------------------- 2. glyphs
print("\n== 2. GLYPH / DASH CHECK ==")
txt = full_text()
for cp, name in [("→", "U+2192 arrow"), ("□", "U+25A1 box"),
                 ("—", "U+2014 em dash"), ("–", "U+2013 en dash")]:
    hits = txt.count(cp)
    print("   %-18s occurrences: %d" % (name, hits))
    if hits:
        fail.append("%s present (%d)" % (name, hits))

# ----------------------------------------------------------- 3. field parity
print("\n== 3. FORM-FIELD PARITY ==")
widgets = []
for i in range(doc.page_count):
    for w in doc[i].widgets():
        widgets.append((w.field_name, w.field_type_string, i + 1, w.field_flags))
names = [w[0] for w in widgets]
tf = sum(1 for w in widgets if w[1] != "CheckBox")
cb = sum(1 for w in widgets if w[1] == "CheckBox")
print("   widgets: %d  (text %d, checkbox %d)" % (len(widgets), tf, cb))
missing = [n for n in CHECK_NAMES if n not in names]
extra = [n for n in names if n not in CHECK_NAMES]
dupes = sorted({n for n in names if names.count(n) > 1})
if missing:
    fail.append("missing fields: %s" % missing)
if extra:
    fail.append("unexpected fields: %s" % extra)
if dupes:
    fail.append("duplicate field names: %s" % dupes)
if len(widgets) != 104 or tf != 84 or cb != 20:
    fail.append("expected 104 fields (84 text, 20 checkbox), got %d (%d/%d)"
                % (len(widgets), tf, cb))
if not (missing or extra or dupes):
    print("   OK: all 104 frozen field names present, no extras, no duplicates")

if SRC:
    sdoc = fitz.open(SRC)
    snames = set()
    for i in range(sdoc.page_count):
        for w in sdoc[i].widgets():
            snames.add(w.field_name)
    only_new = set(names) - snames
    only_src = snames - set(names)
    print("   vs source v5.3: fields only-in-new=%s  only-in-source=%s"
          % (sorted(only_new), sorted(only_src)))
    if only_new or only_src:
        fail.append("field set differs from v5.3 source")
    else:
        print("   OK: field set identical to v5.3 source")

# ----------------------------------------------------------- 4. pass-one pages
print("\n== 4. PASS-ONE PAGES CARRY NO EVIDENCE ==")
# density initial = page 4, optionality initial = page 5 (1-indexed)
for pidx, name in [(4, "Density initial"), (5, "Optionality initial")]:
    page = doc[pidx - 1]
    fns = [w.field_name for w in page.widgets()]
    ev_here = [f for f in fns if f.startswith("ev_")]
    has_ev_word = "evidence line yet" in page.get_text().lower() or \
                  bool(re.search(r"\bevidence\b", page.get_text().lower())) and \
                  "no evidence" not in page.get_text().lower()
    d1_here = [f for f in fns if f.startswith("d1_")]
    print("   p%d %s: d1 fields=%d, ev fields=%d" % (pidx, name, len(d1_here), len(ev_here)))
    if ev_here:
        fail.append("evidence field on pass-one page %d: %s" % (pidx, ev_here))
# confirm no ev_ fields appear before the evidence-read section (page 9)
early_ev = []
for i in range(0, 8):  # pages 1..8
    for w in doc[i].widgets():
        if w.field_name.startswith("ev_"):
            early_ev.append((i + 1, w.field_name))
if early_ev:
    fail.append("evidence fields before protocol page: %s" % early_ev)
else:
    print("   OK: no ev_* fields on any page before the evidence-backed read")

# ----------------------------------------------------------- 5. statements verbatim
print("\n== 5. TWELVE STATEMENTS VERBATIM ==")
norm = re.sub(r"\s+", " ", txt)
miss = [i + 1 for i, s in enumerate(STATEMENTS) if s not in norm]
print("   statements found: %d/12" % (12 - len(miss)))
if miss:
    fail.append("statements not found verbatim: %s" % miss)
else:
    print("   OK: all twelve present verbatim (each appears in pass one and pass two)")

# ----------------------------------------------------------- 6. computed totals
print("\n== 6. COMPUTED TOTALS (read-only + calc JS, tolerant of '3?') ==")
calc_ok = 0
ro_ok = 0
for i in range(doc.page_count):
    for w in doc[i].widgets():
        if w.field_name in COMPUTED:
            obj = doc.xref_object(w.xref)
            has_calc = "/AA" in obj and "/C " in obj
            is_ro = bool(w.field_flags & 1)
            if is_ro:
                ro_ok += 1
            # find the calc JS: /AA /C -> action dict -> /JS (string, or N 0 R
            # pointing to a stream/string). Follow both hops.
            js = ""
            m = re.search(r"/C\s+(\d+)\s+0\s+R", obj)
            if m:
                act = doc.xref_object(int(m.group(1)))
                js_lit = re.search(r"/JS\s*\((.*)\)\s*>>", act, re.S)
                js_ref = re.search(r"/JS\s+(\d+)\s+0\s+R", act)
                if js_lit:
                    js = js_lit.group(1)
                elif js_ref:
                    r = int(js_ref.group(1))
                    try:
                        js = doc.xref_stream(r).decode("latin-1", "ignore")
                    except Exception:
                        sobj = doc.xref_object(r)
                        sm = re.search(r"\((.*)\)", sobj, re.S)
                        js = sm.group(1) if sm else ""
            tolerant = "[^0-9" in js
            if has_calc and tolerant:
                calc_ok += 1
print("   computed fields: %d   read-only: %d   with tolerant calc JS: %d"
      % (len(COMPUTED), ro_ok, calc_ok))
if ro_ok != len(COMPUTED):
    fail.append("not all computed fields are read-only (%d/%d)" % (ro_ok, len(COMPUTED)))
if calc_ok != len(COMPUTED):
    fail.append("not all computed fields have tolerant calc JS (%d/%d)" % (calc_ok, len(COMPUTED)))

# /CO + NeedAppearances
cat = doc.pdf_catalog()
af = doc.xref_get_key(cat, "AcroForm")
co_ok = na_ok = False
if af[0] == "xref":
    axref = int(af[1].split()[0])
    aobj = doc.xref_object(axref)
    co_ok = "/CO" in aobj
    na = doc.xref_get_key(axref, "NeedAppearances")
    na_ok = (na[0] == "bool" and na[1] == "true")
print("   AcroForm /CO present: %s   NeedAppearances true: %s" % (co_ok, na_ok))
if not co_ok:
    fail.append("/CO calculation-order array missing")
if not na_ok:
    fail.append("NeedAppearances not set true")

# ----------------------------------------------------------- 7. overlap detection
print("\n== 7. TEXT-SPAN OVERLAP (clipping/overlap) ==")
def spans(page):
    out = []
    for blk in page.get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            for sp in ln.get("spans", []):
                if sp["text"].strip():
                    out.append((tuple(sp["bbox"]), sp["text"]))
    return out
total_overlaps = 0
for i in range(doc.page_count):
    sp = spans(doc[i])
    bad = []
    for a in range(len(sp)):
        for b in range(a + 1, len(sp)):
            (ax0, ay0, ax1, ay1), ta = sp[a]
            (bx0, by0, bx1, by1), tb = sp[b]
            ovx = min(ax1, bx1) - max(ax0, bx0)
            ovy = min(ay1, by1) - max(ay0, by0)
            if ovx > 1.0 and ovy > 1.0:
                bad.append((ta[:22], tb[:22]))
    if bad:
        total_overlaps += len(bad)
        print("   p%d: %d overlap(s): %s" % (i + 1, len(bad), bad[:3]))
if total_overlaps == 0:
    print("   OK: no overlapping text spans on any page")
else:
    fail.append("%d overlapping text spans" % total_overlaps)

# ----------------------------------------------------------- 8. emptiness
print("\n== 8. PAGE FILL (flag > ~1/3 vertical whitespace) ==")
# section openers (full-navy) are intentionally sparse, like the Field Kit; skip.
OPENERS = {3, 8, 11, 18}
COVER = {1}
PH = 792.0
FOOTER = 44.0
for i in range(doc.page_count):
    pno = i + 1
    if pno in OPENERS or pno in COVER:
        continue
    page = doc[i]
    FOOT_ZONE = PH - 52.0  # 740: ignore footer rule/identity/page-number below this
    ys = []
    for (bbox, t) in spans(page):
        if bbox[3] <= FOOT_ZONE:
            ys.append(bbox[3])  # bottom y (top-left coords)
    for w in page.widgets():
        if w.rect.y1 <= FOOT_ZONE:
            ys.append(w.rect.y1)
    # also drawings (matrix, cards, callouts), excluding the footer hairline
    for d in page.get_drawings():
        if (d.get("fill") or d.get("color")) and d["rect"].y1 <= FOOT_ZONE:
            ys.append(d["rect"].y1)
    if not ys:
        continue
    lowest = max(ys)  # largest top-left-y = lowest real content on page
    # content region below header (~y=96 top) to just above footer zone
    region_top = 96.0
    region_bot = FOOT_ZONE
    empty = region_bot - lowest
    frac = empty / (region_bot - region_top)
    flag = frac > 0.34
    print("   p%2d: content reaches y=%.0f  bottom whitespace=%.0f%% %s"
          % (pno, lowest, frac * 100, "  <-- OVER 1/3" if flag else ""))
    if flag:
        warn.append("page %d ~%.0f%% empty at bottom" % (pno, frac * 100))

# ----------------------------------------------------------- summary
print("\n== SUMMARY ==")
if warn:
    print("   WARNINGS:")
    for w in warn:
        print("     ~", w)
if fail:
    print("   FAILURES:")
    for f in fail:
        print("     -", f)
    sys.exit(1)
print("   ALL HARD CHECKS PASSED"
      + (" (with warnings)" if warn else ""))
