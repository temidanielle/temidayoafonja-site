# -*- coding: utf-8 -*-
"""Write /tmp/v51/v<N>/notes.py from the canonical script + directions.py."""
import sys, os
sys.path.insert(0,"/tmp/v51")
from notesgen import build
n=int(sys.argv[1])
NOTES,FRAMES=build(n)
B="/tmp/v51/v%d"%n
with open(os.path.join(B,"notes.py"),"w",encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Video %d v5.1 speaker/editor notes. Notes parts only; no slide XML.\n'
            'Generated from the canonical v5.1 script and the hand-written per-slide\n'
            'directions. Timings are working estimates at 145 wpm."""\n'%n)
    f.write("NOTES=%r\n"%(NOTES,))
    f.write("FRAMES=%r\n"%(FRAMES,))
    f.write('''
def reveal_notes():
    out=[]
    for s,(k,note) in enumerate(zip(FRAMES,NOTES),1):
        for j in range(1,k+1):
            head=("Reveal frame %d of %d — main slide %d."%(j,k,s)
                  if k>1 else "Single-state frame — main slide %d."%s)
            out.append(head+"\\n\\n"+note)
    return out
''')
print("V%d main notes %d  reveal %d"%(n,len(NOTES),sum(FRAMES)))
