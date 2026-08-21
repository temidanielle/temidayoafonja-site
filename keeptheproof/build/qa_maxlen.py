#!/usr/bin/env python3
"""Automated interactive-field-capacity QA (RC5).

Fails the build when any of these is true:

  * a field's /MaxLen is below its documented acceptance length
    (ktp.field_specs is the single source of truth);
  * a narrative/evidence/support field still carries ReportLab's default
    /MaxLen of 100 (the RC1-RC4 defect);
  * a field that must be multiline (anything expected to hold >= 140 chars) is
    not flagged multiline;
  * a stress value typed at the intended acceptance length is truncated after
    save and reopen;
  * field names, rectangles, multiline flags, or the field counts drift from the
    committed baseline (qa_field_baseline.json).

Usage:
  qa_maxlen.py <handbook.pdf> <ledger.pdf>          # both, against baseline
  qa_maxlen.py --doc handbook <one.pdf>             # single doc
Exit status is nonzero on any failure.
"""
import sys, os, json
import pymupdf
import ktp

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, "qa_field_baseline.json")
MULTILINE_MIN = 140          # any field expected to hold >= this must be multiline
DEFAULT_MAXLEN = 100         # ReportLab's default; a narrative field must never keep it

STRESS_BASE = ("During a cross-functional review I coordinated finance, risk and "
               "engineering to reconcile a persistent reporting gap and documented "
               "each control owner who signed off on the change. ")

def stress_text(n):
    return (STRESS_BASE * ((n // len(STRESS_BASE)) + 1))[:n]

def check_doc(path, doc, baseline, failures):
    d = pymupdf.open(path)
    base = baseline.get(doc) if baseline else None
    fields = []
    for pi in range(len(d)):
        for w in d[pi].widgets():
            xr = w.xref
            ml = d.xref_get_key(xr, "MaxLen")
            maxlen = int(ml[1]) if ml[0] != "null" else None
            intended, exp_max = ktp.field_specs(w.field_name)
            multi = bool(w.field_flags & 4096)
            fields.append(dict(page=pi + 1, name=w.field_name, maxlen=maxlen,
                               intended=intended, multiline=multi,
                               rect=[round(v, 1) for v in w.rect],
                               fontsize=round(w.text_fontsize, 1)))
            # 1. MaxLen >= intended
            if maxlen is None:
                failures.append(f"{doc}:{w.field_name} has NO /MaxLen")
            elif maxlen < intended:
                failures.append(f"{doc}:{w.field_name} /MaxLen {maxlen} < intended {intended}")
            # 2. narrative field must not keep the default 100
            if intended > DEFAULT_MAXLEN and maxlen == DEFAULT_MAXLEN:
                failures.append(f"{doc}:{w.field_name} still at ReportLab default /MaxLen 100 "
                                f"(needs >= {intended})")
            # 3. must-be-multiline
            if intended >= MULTILINE_MIN and not multi:
                failures.append(f"{doc}:{w.field_name} expected multiline (intended {intended}) "
                                f"but is single-line")

    # 4. baseline structural drift
    if base:
        if base["field_count"] != len(fields):
            failures.append(f"{doc}: field count {len(fields)} != baseline {base['field_count']}")
        if base["pages"] != len(d):
            failures.append(f"{doc}: page count {len(d)} != baseline {base['pages']}")
        got_ml = sum(1 for f in fields if f["multiline"])
        if base["multiline_count"] != got_ml:
            failures.append(f"{doc}: multiline count {got_ml} != baseline {base['multiline_count']}")
        b_by_name = {f["name"]: f for f in base["fields"]}
        for f in fields:
            bf = b_by_name.get(f["name"])
            if bf is None:
                failures.append(f"{doc}: unexpected field {f['name']} (not in baseline)")
                continue
            if bf["rect"] != f["rect"]:
                failures.append(f"{doc}:{f['name']} rect {f['rect']} != baseline {bf['rect']}")
            if bf["multiline"] != f["multiline"]:
                failures.append(f"{doc}:{f['name']} multiline {f['multiline']} != baseline {bf['multiline']}")
        got_names = {f["name"] for f in fields}
        for bf in base["fields"]:
            if bf["name"] not in got_names:
                failures.append(f"{doc}: missing baseline field {bf['name']}")

    # 5. stress fill -> save -> reopen -> no truncation
    d2 = pymupdf.open(path)
    expected = {}
    for pi in range(len(d2)):
        for w in d2[pi].widgets():
            intended, _ = ktp.field_specs(w.field_name)
            txt = stress_text(intended)
            expected[w.field_name] = txt
            w.field_value = txt
            w.update()
    tmp = path + ".qastress.pdf"
    d2.save(tmp)
    d3 = pymupdf.open(tmp)
    for pi in range(len(d3)):
        for w in d3[pi].widgets():
            got = w.field_value or ""
            exp = expected[w.field_name]
            if got != exp:
                failures.append(f"{doc}:{w.field_name} stress value truncated/altered "
                                f"(expected {len(exp)} chars, got {len(got)})")
    try:
        os.remove(tmp)
    except OSError:
        pass
    return fields

def main():
    args = sys.argv[1:]
    baseline = json.load(open(BASELINE)) if os.path.exists(BASELINE) else None
    if not baseline:
        print("WARNING: no baseline file; structural-drift checks skipped")
    failures = []
    if args[:1] == ["--doc"]:
        doc = args[1]; path = args[2]
        check_doc(path, doc, baseline, failures)
        targets = [(doc, path)]
    else:
        hb, lg = args[0], args[1]
        check_doc(hb, "handbook", baseline, failures)
        check_doc(lg, "ledger", baseline, failures)
        targets = [("handbook", hb), ("ledger", lg)]

    print("== interactive-field-capacity QA ==")
    for doc, path in targets:
        print(f"   {doc}: {os.path.basename(path)}")
    if failures:
        print(f"\nFAIL ({len(failures)} problem(s)):")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("\nPASS: every field's /MaxLen >= its documented acceptance length; no "
          "narrative field left at the default 100; required multiline fields are "
          "multiline; stress values survive save/reopen without truncation; names, "
          "rectangles, multiline flags and counts match the baseline.")
    sys.exit(0)

if __name__ == "__main__":
    main()
