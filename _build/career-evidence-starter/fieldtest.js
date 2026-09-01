/* Field round trip: fill every field, save, reopen from disk, read back.
 * This is the closest thing available here to "type, save, reopen" in Reader:
 * it proves the fields exist, accept values, persist to the file, and survive a
 * reload. It cannot prove how Preview.app or a phone renders them. */
const { PDFDocument } = require('pdf-lib');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const SRC = path.join(DIR, 'Keep_the_Proof_Career_Evidence_Starter_v1.0_CANDIDATE.pdf');
const FILLED = path.join(DIR, 'filled-roundtrip.pdf');

(async () => {
  const pdf = await PDFDocument.load(fs.readFileSync(SRC));
  const form = pdf.getForm();
  const fields = form.getFields();

  const report = fields.map(f => ({
    name: f.getName(),
    type: f.constructor.name,
    multiline: typeof f.isMultiline === 'function' ? f.isMultiline() : null,
    readOnly: f.isReadOnly(),
  }));
  console.log('FIELD INVENTORY');
  report.forEach(r => console.log('  ', r.type.replace('PDF', '').padEnd(9),
    r.name.padEnd(20), 'multiline:', String(r.multiline).padEnd(5), 'readOnly:', r.readOnly));

  // every field must be writable
  const locked = report.filter(r => r.readOnly);
  if (locked.length) throw new Error('read-only fields: ' + locked.map(r => r.name).join(', '));

  // ── fill ──
  const SAMPLE = 'Sample text for the round trip. Line two of the same answer, long enough to wrap.';
  const written = {};
  for (const f of fields) {
    if (f.constructor.name === 'PDFTextField') {
      const v = f.getName() + ' :: ' + SAMPLE;
      f.setText(v); written[f.getName()] = v;
    } else if (f.constructor.name === 'PDFCheckBox') {
      f.check(); written[f.getName()] = true;
    }
  }
  fs.writeFileSync(FILLED, await pdf.save());

  // ── reopen from disk and read back ──
  const re = await PDFDocument.load(fs.readFileSync(FILLED));
  const reForm = re.getForm();
  let ok = 0, bad = [];
  for (const [name, expected] of Object.entries(written)) {
    if (expected === true) {
      const cb = reForm.getCheckBox(name);
      cb.isChecked() ? ok++ : bad.push(name + ' (unchecked)');
    } else {
      const tf = reForm.getTextField(name);
      tf.getText() === expected ? ok++ : bad.push(name + ' (text mismatch)');
    }
  }
  console.log('\nROUND TRIP');
  console.log('  fields written :', Object.keys(written).length);
  console.log('  read back OK   :', ok);
  console.log('  mismatches     :', bad.length ? bad : 'none');
  console.log('  filled bytes   :', fs.statSync(FILLED).size);

  // ── the blank file must stay blank ──
  const blank = await PDFDocument.load(fs.readFileSync(SRC));
  const blankVals = blank.getForm().getFields()
    .filter(f => f.constructor.name === 'PDFTextField')
    .map(f => f.getText())
    .filter(Boolean);
  console.log('  blank master still empty:', blankVals.length === 0);

  if (bad.length) process.exit(1);
})();
