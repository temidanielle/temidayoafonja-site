#!/usr/bin/env python3
"""AcroForm QA + fill/reopen/persistence test for a Keep the Proof PDF.
Usage: python3 qa_acroform.py <in.pdf> <filled_out.pdf>"""
import sys, fitz

IN, OUT = sys.argv[1], sys.argv[2]
MULTI = 1 << 12  # multiline field flag

NARR = ("This is a realistic multiline test answer written to exercise the field. "
        "It describes a specific contribution, the judgment exercised, and the observable "
        "change that followed, in language an outsider could follow without any employer detail. "
        "It runs well past one line to confirm wrapping and persistence.")  # ~300 chars
SHORT = "Q3 2026 / promotion, review"

fails = []
def check(c, label):
    if not c: fails.append(label)
    print(("PASS" if c else "FAIL"), "-", label)

d = fitz.open(IN)
# 1-6: enumerate + structural checks
names = []
widget_count = 0
no_field = 0
oob = []
no_print = 0
multi_missing = []
per_field = []  # (page, name, rect, flags, multiline)
for pno in range(d.page_count):
    pg = d[pno]; pr = pg.rect
    for w in (pg.widgets() or []):
        widget_count += 1
        nm = w.field_name
        if not nm: no_field += 1; continue
        names.append(nm)
        fl = w.field_flags or 0
        ml = bool(fl & MULTI)
        per_field.append((pno, nm, w.rect, fl, ml))
        # bounds (allow 1pt tolerance)
        r = w.rect
        if r.x0 < pr.x0-1 or r.y0 < pr.y0-1 or r.x1 > pr.x1+1 or r.y1 > pr.y1+1:
            oob.append((nm, pno+1))
        # print flag: annotation flag bit 4 (PDF_ANNOT_IS_PRINT)
        try:
            aflags = w._annot.flags if hasattr(w, "_annot") else None
        except Exception:
            aflags = None
        if aflags is None:
            # fall back to reading /F from the xref
            try:
                fval = d.xref_get_key(w.xref, "F")
                aflags = int(fval[1]) if fval and fval[0] in ("int","xref") else None
            except Exception:
                aflags = None
        if aflags is not None and not (aflags & 4):
            no_print += 1

print(f"\n== {IN.split('/')[-1]} ==")
print("widgets:", widget_count, "| named:", len(names), "| unique:", len(set(names)))
check(no_field == 0, f"every widget belongs to a named field (orphans: {no_field})")
check(len(names) == len(set(names)), "every field name is unique")
check(len(oob) == 0, f"all widgets within page bounds (offenders: {oob[:6]})")
# narrative fields = those we built multiline; confirm flag actually set
ml_count = sum(1 for *_ , ml in per_field if ml)
print("multiline widgets:", ml_count)
check(ml_count > 0, "multiline fields present")
check(no_print == 0, f"print flag set on all widgets (missing: {no_print})")

# 8-9: fill every field with field-specific content (unique sentinel per field)
sent = {}
for pno in range(d.page_count):
    pg = d[pno]
    for w in (pg.widgets() or []):
        nm = w.field_name
        if not nm: continue
        fl = w.field_flags or 0
        ml = bool(fl & MULTI)
        s = f"[{nm}] "
        sent[nm] = s
        h = w.rect.height
        if ml and h >= 40:
            v = s + NARR                      # principal narrative field: ~300 chars
        elif ml and h >= 26:
            v = s + ("A concise but real two-line answer naming the "
                     "contribution and the change.")            # 2-line field ~85 chars
        else:
            v = (s + SHORT)[:56]              # short metadata
        w.field_value = v
        w.update()
d.save(OUT, deflate=True, clean=True)
print("saved filled ->", OUT.split('/')[-1])

# 11-13: reopen, verify persistence + appearance streams + no bleed
d2 = fitz.open(OUT)
persist_fail = 0; ap_fail = 0; bleed = 0
seen_values = {}
for pno in range(d2.page_count):
    pg = d2[pno]
    for w in (pg.widgets() or []):
        nm = w.field_name
        if not nm: continue
        val = w.field_value or ""
        if sent[nm] not in val:
            persist_fail += 1
        # appearance stream present
        try:
            ap = d2.xref_get_key(w.xref, "AP")
            has_ap = ap and ap[0] != "null"
        except Exception:
            has_ap = False
        if not has_ap: ap_fail += 1
        # cross-field bleed: this field must not contain another field's sentinel
        for other, os_ in sent.items():
            if other != nm and os_ in val:
                bleed += 1; break
check(persist_fail == 0, f"every value persists after reopen (misses: {persist_fail})")
check(ap_fail == 0, f"every filled field has an appearance stream (missing: {ap_fail})")
check(bleed == 0, f"no cross-field value bleed (offenders: {bleed})")

print("\nFAILURES:", len(fails))
for f in fails: print("  -", f)
sys.exit(1 if fails else 0)
