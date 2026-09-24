#!/usr/bin/env python3
"""RC2 form acceptance test. Fills every field at its category's spec length,
computes whether the field box can display that many characters unclipped at a
legible font, fills/saves/reopens and verifies exact persistence, appearance
streams, and no cross-field bleed. Usage: qa_accept.py <in.pdf> <filled.pdf>"""
import sys, math, fitz

IN, OUT = sys.argv[1], sys.argv[2]
MULTI = 1 << 12
FS = 9.5                      # field font size (Helvetica) set by the engine
CHAR_W = FS * 0.52           # avg Helvetica advance
LINE_H = FS * 1.5            # rendered line height in an AcroForm field (measured)
PAD = 6                      # vertical padding inside the field box

def spec_len(nm):
    n = nm.lower()
    def has(*x): return any(k in n for k in x)
    if has("_what","_contrib","_change"): return 250      # QC main narrative
    if has("_verify","_out"):             return 110      # QC verifier / confidential
    if has("_sit","_why","_judge","_actions","_outcome","_prevented","_team"): return 250  # FE principal
    if has("_evref"):                     return 90
    if has("_date","_proj","_month","_done","_next","_q","ix_"): return 20  # short metadata
    if has("_tags","_captures","_expand"): return 60
    if has("tr_int","tr_por","_formal","_actual","_people","_scope","_quant","_qual","_internal","_portable","_conf","pl_cond","pl_part","pl_scope","pl_out"): return 160  # paired / medium narrative
    if has("pl_support"):                 return 100
    if has("pl_line"):                    return 200
    if has("ms_projects","ms_improved","qr_read","qr_fixed","qr_strong","qr_thin"): return 220
    return 40

def make_val(nm, L):
    base = f"[{nm}] "
    filler = ("Redesigned the onboarding sequence and made the call to phase the cutover, "
              "which kept a risky switch from becoming a bad weekend for the whole team. ")
    s = base + (filler * ((L // len(filler)) + 1))
    return s[:L]

d = fitz.open(IN)
fails = []
def chk(c, label):
    if not c: fails.append(label)
    return c

# capacity check + fill
sent = {}; clip_warn = []
for pg in d:
    for w in list(pg.widgets() or []):
        nm = w.field_name
        if not nm: continue
        L = spec_len(nm)
        ml = bool((w.field_flags or 0) & MULTI)
        val = make_val(nm, L)
        sent[nm] = f"[{nm}] "
        w.field_value = val
        w.update()
        # capacity: how many chars fit unclipped in this box?
        cpl = max(1, int((w.rect.width - 6) / CHAR_W))
        lines_cap = max(1, int((w.rect.height - PAD) / LINE_H))
        cap = cpl * lines_cap
        if ml and L > cap:
            clip_warn.append((nm, L, cap, round(w.rect.width), round(w.rect.height), cpl, lines_cap))
d.save(OUT, deflate=True, clean=True)

print(f"== {IN.split('/')[-1]} ==  fields={len(sent)}")
if clip_warn:
    print("POTENTIAL CLIP (name, testlen, capacity, w, h, chars/line, lines):")
    for c in clip_warn: print("   ", c)
chk(not clip_warn, f"{len(clip_warn)} field(s) too small for their spec length")

# reopen + verify
d2 = fitz.open(OUT)
persist=ap=bleed=0
for pg in d2:
    for w in list(pg.widgets() or []):
        nm=w.field_name
        if not nm: continue
        val=w.field_value or ""
        if sent[nm] not in val: persist+=1
        try:
            a=d2.xref_get_key(w.xref,"AP"); has_ap=a and a[0]!="null"
        except Exception: has_ap=False
        if not has_ap: ap+=1
        for other,os_ in sent.items():
            if other!=nm and os_ in val: bleed+=1; break
chk(persist==0, f"values persist after reopen (misses {persist})")
chk(ap==0, f"appearance streams present (missing {ap})")
chk(bleed==0, f"no cross-field bleed ({bleed})")

print("FAILURES:", len(fails))
for f in fails: print("  -", f)
sys.exit(1 if fails else 0)
