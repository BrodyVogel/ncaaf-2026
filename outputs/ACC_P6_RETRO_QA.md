# ACC Round — Pick Six Retro-QA (2026-07-18)

## What happened
Pick Six Previews (P4 + Notre Dame only; no G5 edition) was a STANDING third source
in the B10 and B12 rounds (e.g. Ohio State magazines.md "Sources: Athlon; Pick Six
book pp. 64-65"; Kansas State "## Pick Six 2026 (B12 pp. 13-14; verbatim)"; Iowa's
two-deep cites P6 in source notes). The G5 rounds correctly documented it as N/A
("P4-only publication"). The ACC round used it for exactly ONE of 17 builds
(Virginia Tech, Batch 1: "Pick Six p.11") and then silently dropped it for the
other 16 — a process regression, most likely lost across a session-compaction
boundary. Its RANKINGS were always present in every team's anchor blend (one of
six anchor sources); what was skipped was its roster/disposition editorial.

## Method
Extracted Pick Six ACC (34pp) to text. Swept EVERY name in every ACC META override
array (portal_withdrawal, yr4_return, nfl_declare, departure_research,
portal_departure — ~45 names) plus all grade-critical QB/star calls against the P6
text, then read the full passages for every flagged team.

## Corroborated (the highest-risk calls all held)
- FSU ×5 withdrawals: "they were able to pull back the other two starters from the
  portal – corner Ja'Bril Rawls and safety Ashlynd Barker"; "retain the Desir twins";
  "just two return in Blake Nichelson and Omar Graham." Triple-verified.
- Louisville: "Both Brown's are back" (Isaac + Keyjuan); Lubin/AJ Green duo; Watts,
  Hurry, Lance Robinson returns; Kurisky→Duke confirmed on Duke's page ("signed
  veteran Nate Kurisky (Louisville)").
- NFL declares: Bain + Mesidor "two first-round draft picks off the edges"; Mauigoa
  "drafted in the first round"; Kyle Louis "heads to the pros"; Hibner "all three
  tight ends depart"; Clemson's Parker/Woods/Capehart "all depart," Terrell
  "graduated"; Duke's Brian Parker "left as an All-[ACC]."
- Research-GONE feed-misses, mechanism now explained (GRADUATIONS, invisible to the
  portal feed): NC State's Harsh ("graduated," with Cleveland/Price), Pitt's Raphael
  Williams ("graduated," with Spann), SMU's Harden + Brinson ("graduating").
- BC's Bam Crouch → "Daveon Crouch went to Kansas." GT's Melvin Jordan IV returns
  ("returns with EJ Lightsey and Melvin Jordan"). Miami's Toure "granted an eighth
  college season." Cal's Sidney/Burrell, Virginia's Marcellus/Courtney, VT's
  Hawkins/Cunningham, Wake's Lohavichan, Stanford's Rose/Tafiti/Cooper/Rowell,
  BC's Cam Martinez — all corroborated as returns.

## Contradicted → CORRECTED (7 roster spots, 2 teams, 3 unit grades)
| Team | Player | Was | Actually | Evidence |
|---|---|---|---|---|
| Pitt | Rashad Battle (CB) | yr4_return override, DB3 | GONE | P6 "loses four starters... Battle... departing" |
| Pitt | Javon McIntyre (S) | yr4_return override, DB6 | GONE | same P6 sentence |
| Pitt | Blaine Spires (ED) | yr4_return override, DL5 | GONE | no print naming anywhere; PS "lose 4 DL" |
| UNC | Marcus Allen (CB) | yr4_return override, DB1 | GONE | Athlon chart omits; P6 "four starters gone" |
| UNC | Gavin Gibson (S) | yr4_return override, DB2 | GONE | same |
| UNC | Thaddeus Dixon (CB) | yr4_return override, DB6 | GONE | P6 projects Cost/Patterson/Smith/Bryson/Willie |
| UNC | Smith Vilbert (DE) | yr4_return override, DL2 | GONE | P6 "end Smith Vilbert graduated" |

Also corrected: UNC's Hoilette (chart DE starter — had been mis-noted as OL) and
Willie (chart CB — had been noted at LB) added to the proper units; Pitt's Harrison
(returning rotational CB) added as depth.

Grade + rating impact:
- Pittsburgh: DB 52→50 (sum 412→410). Rating +5.90 → **+5.83** (rank 41 unchanged).
- North Carolina: DL 54→52, DB 54→48 (sum 384→376). Rating +1.84 → **+1.58** (rank 58→59).

## Root cause + rule change
All 7 bad calls were ONE failure mode: yr4 gate conflicts resolved as "veteran
returner" on tape volume, without a printed listing — 6 of 7 on the round's last
two builds. New R15 (DISPOSITION_RULES.md): a yr4 conflict may be resolved as a
return ONLY on a named magazine listing; otherwise the yr4 default stands and the
player comes out of the two-deep. New R16: Pick Six is a REQUIRED facts-only third
source for all P4 builds (rankings stay out of research; they already enter via
the anchor blend).

## Residual state
All 17 ACC teams re-verified: gates clean, board rebuilt (96 teams). Every
grade-critical ACC call is now either triple-corroborated or two-source-verified
with P6 silent. B10/B12 need no retro pass (P6 was used at build). SEC round
proceeds with P6 as the third source from team 1.
