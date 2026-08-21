# Deferred changes — Free Flagship 60-minute family

Approved wording and corrections that are **not** being applied yet, because the
artifact they touch is frozen and the change alone does not justify breaking the
freeze. Apply each one the next time that artifact is opened for a substantive
revision, then delete the entry.

Do not open an artifact solely to apply something from this file.

---

## 1. Workbook page 1 — Live / Replay block

**Artifact:** `Capability_Position_Read_Workbook_60MIN_v2.0.1_CANDIDATE.pdf`
**Generator:** `scratchpad/flagship/v2/build_workbook_v20.py`
**Status:** approved, deferred
**Recorded:** Friday, August 21, 2026, Central Time

Use the **shorter headings** — `LIVE SESSION` and `REPLAY`, not the current
`IN THE LIVE SESSION` / `ON THE REPLAY`.

**LIVE SESSION**

> Work through each phase with me. Use the timing cue at the top of each page to
> follow along.

**REPLAY**

> Pause whenever you need to and complete each phase at your own pace.

For reference, the wording this replaces:

| | Current in v2.0.1 |
|---|---|
| IN THE LIVE SESSION | Follow the presenter's pace. Every page shows the minutes it belongs to. |
| ON THE REPLAY | Pause and work at your own pace. Nothing here depends on keeping up. |

### When this is applied

The workbook filename changes, so it stops being v2.0.1. Everything below has to
move with it in the same pass:

- the SOP's three workbook references (link-ready line, asset list, source line);
- the QA report's workbook section and its "unchanged at v2.0.1" statements;
- QA check "Workbook is unchanged and still referenced at v2.0.1" in
  `v2/qa_v201.py`, and the SHA-256 pin in the group K workbook check;
- the Adobe Acrobat Reader behaviour test, which has to be re-run against the
  regenerated form.

---

## Gate status — current package

The v2.0.1 workbook is frozen byte-for-byte at SHA-256
`2bd2912846a679837e8e6bfb4aadff2bb07ee5959d35502ca1c5b5c728efa3ee`.

Three gates stand between CANDIDATE and FINAL. All three are required, in any
order.

| Gate | Status |
|---|---|
| Rehearsal 1 — timed content | **OUTSTANDING** |
| Rehearsal 2 — production | **OUTSTANDING** |
| Workbook behaviour test, Adobe Acrobat Reader | **PASSED** — reported Friday, August 21, 2026 CT |

The Acrobat test was run against the frozen v2.0.1 workbook and reported as
passing on all seven criteria: a bare `?` refused; `3?` accepted; `2?` and `5?`
accepted; `6?` and `1??` refused; all four totals calculating; question marks
excluded from the numeric total; every total still manually typeable.

That result belongs to THIS build of the workbook. If the workbook is ever
regenerated — including to apply the deferred change above — the test has to be
re-run against the new file, because the form and its JavaScript are rebuilt
with it.

The package therefore stays CANDIDATE until both rehearsals pass.
