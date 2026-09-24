/**
 * The voice rules, shared by the START HERE and Three Signs gates.
 *
 * Two rules:
 *
 *   1. The "not X, it is Y" construction. A negation followed by a copula
 *      clause that supplies the replacement: "It is not a skill gap, it is a
 *      translation gap." It is a tic, and once a reader notices it they see it
 *      everywhere.
 *
 *      This is deliberately narrow. "You are repeating, not stretching." is
 *      the opposite shape, the negation trailing rather than setting up a
 *      correction, and it stays.
 *
 *   2. The hedging adverbs: actually, honestly, genuinely. Each one concedes
 *      that the sentence around it might not have been believed.
 *
 * Run this file directly to prove the rules fire on what they claim to catch
 * and stay quiet on the approved copy:  node source/voice.mjs
 */
const NOT_X_IT_IS_Y =
  /\bnot\b[^.!?;]{2,70}[,;.]\s*(?:it|that|this|they|you|we)(?:'s|’s|\s+(?:is|are|was|were))\b/i;

const ADVERBS = ['actually', 'honestly', 'genuinely'];

export function voiceFaults(text) {
  const faults = [];
  const flat = text.replace(/\s+/g, ' ');
  const m = NOT_X_IT_IS_Y.exec(flat);
  if (m) faults.push(`"not X, it is Y" construction: "${m[0].trim()}"`);
  for (const a of ADVERBS)
    if (new RegExp(`\\b${a}\\b`, 'i').test(flat)) faults.push(`hedging adverb "${a}"`);
  return faults;
}

/* ── self test ────────────────────────────────────────────────────────── */
if (import.meta.url === `file://${process.argv[1]}`) {
  const MUST_FAIL = [
    'It is not a skill gap, it is a translation gap.',
    'This is not about confidence. It is about evidence.',
    'The problem is not the skill, it’s what the label fails to show.',
    'They are not slow, they are careful.',
    'What actually changed?',
    'Honestly, most records fail.',
    'Work that was genuinely hard for me then.',
  ];
  const MUST_PASS = [
    'You are repeating, not stretching.',
    'Adjacent experience still has to be read.',
    'Name the gap before someone else does.',
    'Learning them takes time, even when you are capable of it.',
    'A role can reward you long after it stops building you.',
    'Evidence tells you what to test next.',
    'The feedback I receive changes what I do next, not just how I feel.',
    'Keep your own account of the work. Leave employer-owned material where it belongs.',
  ];
  let bad = 0;
  for (const s of MUST_FAIL) if (!voiceFaults(s).length) { console.error(`  missed: ${s}`); bad++; }
  for (const s of MUST_PASS) {
    const f = voiceFaults(s);
    if (f.length) { console.error(`  false positive on: ${s}\n    ${f.join('; ')}`); bad++; }
  }
  console.log(`  voice rules: ${MUST_FAIL.length} constructions caught, ` +
              `${MUST_PASS.length} approved lines left alone`);
  if (bad) { console.error(`\n${bad} self test failures`); process.exit(1); }
  console.log('  self test passed');
}
