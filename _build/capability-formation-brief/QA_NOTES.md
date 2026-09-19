# QA Notes

The Capability Formation Brief: paid system and two pilot tools.

Version 1.0 draft. These notes record the checks run before this set was handed back for review. Nothing here is marked final. Final status waits on approval of the actual PDFs and the architecture.

---

## 1. The single QA question, applied to each tool

The test: "Does this help the reader make a clearer decision, or did we merely give them more career content?"

Evidence Gap or Capability Gap?
Verdict: clearer decision. The reader arrives with an undifferentiated "not ready" and leaves with a named read (A, B, C, or D) and four specific lists. The tool spends almost no space re-teaching the concept and moves straight to sorting the reader's own case. It refuses to auto-validate, so the output is a real diagnosis rather than reassurance. Pass.

The 3P Role Read.
Verdict: clearer decision. The reader arrives asking "is this role still worth it" and leaves with a three-line read, a named trade, one capability to strengthen, and one concrete 30 to 90 day test. The output is a next action inside the role, not a feeling about it. Pass.

Neither tool is more content. Both end in something the reader can act on.

---

## 2. Source integrity

- Method statements were checked against the approved Keep the Proof source (the master manuscript and build engine). The evidence, contribution, and portability logic in these tools is consistent with that method. Nothing contradicts the approved teaching.
- No approved Keep the Proof file was modified, regenerated, or weakened. The tools were built as new source under _build/capability-formation-brief/. The Keep the Proof and Field Kit files were read for consistency only.
- Named language is reused, not invented. 3P is Practice, Proof, Portability. 4R is Responsibility, Range, Recognition, Recovery. MOVE is referenced as the approved decision check; its canonical step names are deliberately left to be pulled from approved source when that tool is built, rather than fabricated here.
- No new proprietary framework was manufactured. Eight of the ten bank tools are plain reads, sorts, tests, and checks, by design.
- No research, prevalence, or validation language is used. The words "most people," "most common," "proven," and "validated" do not appear in the tools. Claims are kept to the reader's own case.
- No testimonials and no invented outcomes.
- No outcome is promised. The tools sharpen a decision. They do not guarantee a promotion, an offer, or a move. The closing lines say so directly.

---

## 3. Design and house rules

- Visual system matches the brief: deep navy #112345, warm cream #F5F1E8, muted gold #C9A84C, with the bright accent #F2C44C used only for the short title rule and one card marker. Confirmed against the rendered pages.
- No em dashes. Checked across every deliverable file. Ranges are written with "to" and hyphens.
- Length: each tool is two pages. Both fit inside the page with margin to the footer, verified in the rendered PDF.
- Printable: high contrast on cream, writing areas are ruled boxes and lines that work in print and by hand. Backgrounds are set to print with color-adjust exact, and the layout also reads in grayscale.
- Time to complete is stated on each tool: about 10 to 15 minutes for Evidence Gap or Capability Gap, about 10 to 20 minutes for the 3P Role Read.
- Each tool ends in a concrete output, not reflection prompts. Confirmed.

---

## 4. Tool-specific integrity checks

Evidence Gap or Capability Gap?
- A genuine capability gap (read A) is preserved as a legitimate, non-inferior result. The copy states this twice, in the intro and the closing, and the read logic sends "not yet on capability" to A regardless of the other answers. The tool cannot be completed in a way that hides a real capability gap.
- The four reads are genuinely distinct and map cleanly from the three questions. Access (C) is kept separate from evidence (B), so a reader who was never given a chance is not told to go produce evidence they had no way to produce.

The 3P Role Read.
- A weak read is explicitly not converted into a resignation recommendation. The howto text, the page-two framing, and the closing all route a weak read to a test inside the role first. The only path to a leave decision runs through a test that the role fails.
- The 3P are used as the approved Practice, Proof, Portability, each tied to its approved core question.

---

## 5. Rendering and files

- Both tools and the tool index were rendered to PDF from the HTML sources with Chromium print, at US Letter with CSS page sizing.
- Every page was rendered to PNG and visually inspected. No clipping, no field overlapping instructional text, no content colliding with the footer.
- Fonts embed through the print step. Headings are Cormorant Garamond, body and labels are DM Sans, matching the wider brand while the deeper navy and tighter grid keep the paid tools visually their own tier.

---

## 6. Open items for review

- MOVE Decision Check: pull the canonical MOVE step names from approved source before building that tool. Not needed for the two pilots.
- Fillable fields: the pilots are print-and-write worksheets. If interactive AcroForm fields are wanted for on-screen completion, that is a straightforward addition on top of the same layout and can follow approval of the design.
- Distribution: these are paid artifacts, stored under _build/ and blocked from the public site. How they are delivered to subscribers (paywalled download, email, member area) is a commercial decision, not set here.
