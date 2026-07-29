#!/usr/bin/env python3
"""Wire the rating circles to the score boxes and totals via AcroForm calculation
scripts. Clicking a circle (radio rate_sN) fills box dN / oN and the /30 totals
recompute live. Degrades gracefully: viewers without JS still show the native
circle selection; the boxes just aren't auto-filled there.
"""
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DictionaryObject, ArrayObject, NameObject, TextStringObject,
)

SRC = "The_Capability_Formation_Diagnostic.pdf"   # radio-only version (fallback)
OUT = "The_Capability_Formation_Diagnostic_interactive.pdf"

reader = PdfReader(SRC)
writer = PdfWriter()
writer.append(reader)
acro = writer._root_object["/AcroForm"].get_object()

# map field name -> indirect ref
ref_by_name = {}
for fref in acro["/Fields"]:
    fo = fref.get_object()
    ref_by_name[str(fo.get("/T"))] = fref

def set_calc(field_name, js):
    ref = ref_by_name[field_name]
    fo = ref.get_object()
    action = DictionaryObject()
    action[NameObject("/S")] = NameObject("/JavaScript")
    action[NameObject("/JS")] = TextStringObject(js)
    aa = DictionaryObject()
    aa[NameObject("/C")] = action
    fo[NameObject("/AA")] = aa
    return ref

# set the box from its circle when one is chosen; otherwise leave manual entry
box_js = ('var v=this.getField("rate_s%d").valueAsString;'
          'if(v!="Off"&&v!=""){event.value=v;}')
def total_js(prefix, lo, hi):
    return ('var s=0,any=false;for(var i=%d;i<=%d;i++){'
            'var v=this.getField("%s"+i).valueAsString;'
            'if(v!=""){s+=parseInt(v,10);any=true;}}'
            'event.value=any?s:"";') % (lo, hi, prefix)

order = []
# Density statements 1-6 -> boxes d1..d6, then density_total
for n in range(1, 7):
    order.append(set_calc("d%d" % n, box_js % n))
order.append(set_calc("density_total", total_js("d", 1, 6)))
# Optionality statements 7-12 -> boxes o7..o12, then optionality_total
for n in range(7, 13):
    order.append(set_calc("o%d" % n, box_js % n))
order.append(set_calc("optionality_total", total_js("o", 7, 12)))

# calculation order (boxes must recompute before their totals)
acro[NameObject("/CO")] = ArrayObject(order)

with open(OUT, "wb") as f:
    writer.write(f)
print("wrote", OUT, "with calculation scripts + /CO order")
