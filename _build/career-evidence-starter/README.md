# Career Evidence Starter: PDF generator

Source and build scripts for the free PDF. **Nothing here is a public page.**
The PDF itself is not committed: no PDFs are stored in this repository, and
where the file is hosted is still an open decision (see the QA report).

## Files

- `starter-source.html` — the six pages, in HTML, using the site's own woff2
  faces through `/fonts.css`. Field positions are the `.fld` placeholders.
- `build.js` — prints the source to a US Letter PDF with Chromium, then adds
  AcroForm fields with pdf-lib at coordinates measured from those placeholders.
  Asserts the px to pt factor is exactly 0.75 before placing anything.
- `qa.js` — overflow check on the source, then renders the produced PDF through
  pdf.js and screenshots every page. Poppler and LibreOffice are unavailable in
  the build container, so this is how the PDF gets looked at.
- `fieldtest.js` — fills every field, saves, reopens from disk, reads back.

## Images the build depends on

Two raster assets are placed into the PDF, and `build.js` **throws rather than
printing** if either fails to load, because a 404 renders as a silent empty box:

- `/images/temidayo-gold-ivory.png`, the author portrait beside the WHY I MADE
  THIS note on page 2. **Not yet in the repository.** Until it is committed,
  the build cannot run. Do not substitute another portrait.
- `/keep-the-proof-cover.png`, the paid product cover on page 6. Already in
  the repository.

## Running it

Needs `playwright`, `pdf-lib` and `pdfjs-dist`, and the repository served at
`http://127.0.0.1:8899` so `/fonts.css` and both images resolve.

```
node build.js      # writes Keep_the_Proof_Career_Evidence_Starter_v1.0_CANDIDATE.pdf
node qa.js         # overflow check + page renders
node fieldtest.js  # field round trip
```
