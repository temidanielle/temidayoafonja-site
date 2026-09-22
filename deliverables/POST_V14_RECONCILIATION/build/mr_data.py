# -*- coding: utf-8 -*-
"""Missing Rung x V15-V21 reconciliation. Architecture only."""

STAMP = "Tuesday, September 22, 2026"

INPUTS = [
 ("Missing_Rung_Series_Overview_and_Advisor_Handoff.docx",
  "dc7dd240158dea6a...", "39,316 bytes", "READ IN FULL",
  "Supplies the series purpose, the evidence boundary, the editorial rules, the playlist table "
  "with each episode's job, and the production direction."),
 ("Missing_Rung_Strategic_Update_and_Roadmap_Reconciliation.docx",
  "c6f0f7b24a68b9aa...", "41,223 bytes", "READ IN FULL",
  "Supplies the executive recommendation, the lock list, the per-episode strongest-and-development "
  "table, the V15 to V21 overlap table, the production standard and the anonymization correction. "
  "Three of the four uploaded files are byte-identical copies of this one document."),
 ("MR1 to MR8 recording masters",
  "not available", "n/a", "NOT SUPPLIED",
  "The eight first masters are not attached to this task and do not exist anywhere in the "
  "workspace or on the filesystem. Searched by filename and by content. What is reconciled below "
  "therefore rests on each episode's stated job in the overview table and its strongest-and-"
  "development row in the strategic update, not on the scripts themselves."),
 ("Second-Reader Audit and Market Discovery Report, September 22, 2026",
  "not available", "n/a", "NOT SUPPLIED",
  "Named as the primary source for the whole series. It is not in the workspace. Every structural "
  "claim in every Missing Rung episode traces to it, so it has to be in the workspace with a "
  "checksum before any of those claims can be verified."),
 ("V15 to V21 source scripts",
  "in workspace", "seven masters", "READ IN FULL",
  "old V17, V16, V21, V15 and V18 from the 14 to 21 production packages, plus old V25 and old V35 "
  "from the roadmap extension. Read in full for yesterday's pre-rewrite audit and re-used here."),
 ("Locked V4 to V14",
  "in workspace", "eleven masters", "READ ONLY",
  "Read to establish Watch Next promises, duplication boundaries and the anonymization conflict."),
]

LIMIT = ("The eight MR masters are not available. That limits four of the twelve determinations. "
         "Where a determination depends on wording rather than on editorial job, it is marked "
         "PROVISIONAL and the exact test to run once the masters arrive is stated. Everything "
         "marked FIRM rests on material that is in hand: the two supplied documents, the seven "
         "V15 to V21 sources read in full, and the locked V4 to V14 masters.")

EXEC = [
 "Lock the territory. The Missing Rung is a real franchise and it extends career portability "
 "rather than widening away from it. Nothing in the reconciliation argues against the concept.",

 "Do not append eight episodes. The eight-part journey survives as seven episodes once the "
 "duplication is resolved, and one of those seven is an existing V15 to V21 video rather than a "
 "new build. Four planned videos and three MR episodes collapse into three episodes.",

 "The manager and IC territory is where the real duplication sits. V21, MR2, MR6 and MR8 are four "
 "episodes answering two questions. Recommend two: one forward-looking management decision, one "
 "manager-to-IC episode that runs from identity to decision.",

 "MR5 and V20 are the same editorial job with different triggers, and their thumbnails would read "
 "as the same video in a sidebar. Recommend one merged episode on V20's stronger source, opening "
 "with MR5's more-people situation.",

 "Three locked videos name V15, V16 and V17 by title in their spoken Watch Next. That settles "
 "sequencing on its own: those three publish first, before any Missing Rung episode. It is not a "
 "preference, it is a promise already in published audio.",

 "V15 to V19 come through the reconciliation unchanged. The existing plan's first five slots are "
 "correct and the Missing Rung block starts at V20.",

 "One old roadmap episode is absorbed. Old V29, Career Ladders Don't Work Like They Used To, is "
 "MR3 and MR4's territory and shares MR4's title almost word for word. Mark it retired so nobody "
 "builds it later.",

 "The anonymization rule creates a direct conflict with the lock and I have not resolved it. The "
 "strategic update says the rule applies to V13 and V14. Those two name four employers on camera "
 "and they are locked. That is a decision, not a task.",
]

LOCKED = [
 ("The Missing Rung as a series and recurring franchise", "LOCK",
  "Nothing in the reconciliation weakens it."),
 ("The central question", "LOCK",
  "What happens when the next rung of your career no longer exists. It survives every merge below "
  "and none of the merged episodes needs a different premise."),
 ("The evidence boundary", "LOCK",
  "No claim that middle management is dead or universally disappearing. Forum language is not "
  "prevalence. Management contraction is not universal disappearance. No claim of verified "
  "YouTube search demand. The playlist is a content-market test."),
 ("The Capability Formation lens", "LOCK",
  "The permanent audit stays underneath and is not recited. No second framework is created by "
  "anything recommended here."),
 ("The human territory", "LOCK",
  "Losing a rung without assuming loss of value. Experienced and new at the same time. Status and "
  "identity after flattening. Choosing seniority without automatically choosing management."),
 ("Watch-Me-Read as internal behavior", "LOCK",
  "Never named publicly. Artifacts teach or they do not appear."),
 ("The eight-part decision journey", "LOCK AS A JOURNEY, NOT AS EIGHT SLOTS",
  "The logic survives. The count does not. Seven episodes carry it, and every retained episode "
  "keeps its position relative to the others."),
 ("Final public numbering", "DO NOT LOCK",
  "Recommended below and open to Temidayo."),
 ("The eight masters word for word", "DO NOT LOCK",
  "They are not available to read, and three of them are recommended for merges that change their "
  "shape."),
]
