import re, io

src = "_build/keep-the-proof-v2/stage2/01_MANUSCRIPT_KEEP_THE_PROOF_V2.md"
lines = open(src, encoding="utf-8").read().split("\n")

design_notes = []
out = []
current_section = "(front)"
for ln in lines:
    m = re.match(r'^#{1,3}\s+(.*)', ln)
    if m:
        current_section = m.group(1).strip()
    if ln.startswith("> VISUAL:"):
        design_notes.append((current_section, ln[len("> VISUAL:"):].strip()))
        continue
    if ln.startswith("> LEGAL REVIEW REQUIRED"):
        # drop internal legal-review markers
        continue
    out.append(ln)

open("/tmp/manuscript_stripped.md","w",encoding="utf-8").write("\n".join(out))

# design notes file
dn = ["# Keep the Proof V2 — Design notes (internal, not shipped)",
      "",
      "Extracted `> VISUAL:` guidance from the approved Stage 2 manuscript, grouped by section. These direct the handbook layout; they are not reader-facing text.",
      ""]
last = None
for sec, note in design_notes:
    if sec != last:
        dn.append(f"\n## {sec}\n")
        last = sec
    dn.append(f"- {note}")
open("_build/keep-the-proof-v2/production/DESIGN_NOTES.md","w",encoding="utf-8").write("\n".join(dn))

print("VISUAL notes extracted:", len(design_notes))
print("Lines out:", len(out), "of", len(lines))
