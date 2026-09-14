# Visual manifest

Essay: **What Your Current Role Should Be Doing for Your Future**
Publication: The Capability Formation Brief, Wednesday, September 9, 2026
Source of truth: `Capability_Formation_Sep09_2026_What_Your_Current_Role_Should_Be_Doing_for_Your_Future_PRODUCTION_FINAL_v5.2.docx`

Three assets were produced. One is the cover and social preview. Two go inside the
essay body. No other in body image is part of this package.

---

## 1. Cover and social preview

| | |
| --- | --- |
| **Filename** | `01-current-role-cover-1600x900.png` |
| **Dimensions** | 1600 x 900 |
| **Placement** | Substack cover and social preview image only |
| **In body** | No. Do not insert this image inside the essay. |
| **Anchor** | Not applicable |
| **Alt text** | Cream editorial cover reading "What Your Current Role Should Be Doing for Your Future." |

Copy on the asset: the title over three lines, a gold rule, the supporting line
`BETTER DECISIONS · CLEAR PROOF · MORE OPTIONS`, and the footer
`CAPABILITY FORMATION · TEMIDAYO AFONJA`.

---

## 2. The 3 Ps of a role that builds your future

| | |
| --- | --- |
| **Filename** | `02-three-ps-role-builds-future.png` |
| **Dimensions** | 1600 x 1000 |
| **Placement** | In body |
| **Insert after** | "A role does not need to maximize all three every quarter. But over time, you should be able to see evidence of each one. That is what the 3 Ps help you see." |
| **Insert before** | "Practice: What are you becoming better able to handle?" |
| **In body** | Yes |
| **Alt text** | The 3 Ps of a role that builds your future: Practice, Proof and Portability. |

Both anchor sentences were checked against v5.2 and are unaltered. The article
document itself was not modified.

---

## 3. Career Evidence Starter

| | |
| --- | --- |
| **Filename** | `03-career-evidence-starter-artifact.png` |
| **Dimensions** | 1600 x 1000 |
| **Placement** | In body |
| **Insert after** | "That is exactly where the Starter begins." |
| **Insert before** | "Get the free 10-Minute Career Evidence Starter:" |
| **In body** | Yes |
| **Alt text** | Preview of the Career Evidence Starter worksheet. |

The asset composes two real product page renders already held in the repository:
`career-evidence-starter-cover.png` (the cover) and
`career-evidence-starter-inside.png` (the Portable Proof Line page). Both are
placed at their natural proportions, scaled down and never up, with no
recolouring, retyping or invented content. No device mockup, stock image or
generated workbook appears.

---

## Files in this folder

| File | What it is |
| --- | --- |
| `01-current-role-cover-1600x900.png` | Cover and social preview |
| `02-three-ps-role-builds-future.png` | In body visual 1 |
| `03-career-evidence-starter-artifact.png` | In body visual 2 |
| `contact-sheet.png` | All three together |
| `VISUAL_MANIFEST.md` | This file |
| `QA-REPORT.md` | What was verified and what could not be |
| `source/copy.json` | Editable copy for all three visuals |
| `source/visuals.html` | Editable layout, live DOM text, no outlined type |
| `source/build-visuals.mjs` | Renders the three PNGs and the contact sheet |
| `source/verify-visuals.mjs` | The quality gate |

To change a line and re-export:

```sh
node substack-sep09-current-role-final-visuals/source/build-visuals.mjs
node substack-sep09-current-role-final-visuals/source/verify-visuals.mjs <essay-extract.txt>
```

## Design system

Navy `#0F2347`, warm cream `#F5F0E8`, gold `#B8952E` on cream and `#C9A84C`
inside a navy panel, rust `#C1440E` for the short divider rules. The three
sheets follow the Capability Audit treatment: a cream field inside a thin gold
hairline frame, with the content carried on filled navy panels with rounded
corners, cream serif type on the navy and gold small capitals for labels.
Display type is Cormorant Garamond, labels and supporting copy are DM Sans.

Rust is used only for the divider rules, which is where the real Career
Evidence Starter uses it. It is deliberately not used as a card fill on the
3 Ps. In the Capability Audit grid the rust card marks the destination among
four states, and the essay is explicit that none of the three Ps outranks the
others. Both families are already self hosted in the
repository, and both are the families the Career Evidence Starter itself uses,
so the visuals and the real artifact read as one system.

No em dash or en dash characters appear anywhere in this package.
