# Grader bridge test — Fable 5 → Opus 4.8 (2026-07-16)

METHOD: 10 frozen teams (6 B12 + 4 AAC, stratified top→bottom), blind-regraded by fresh
Opus 4.8 subagents. Blinding: each subagent read the FROZEN grading prompt + exemplars +
the team's raw evidence (roster two-deep, magazines, news, META, PFF unit tape) + a
REDACTED dossier (Fable's grade verdicts masked as [GRADE REDACTED]; evidence synthesis
retained). Withheld: grades.json and the un-redacted dossier. This replicates the
go-forward condition (a clean Opus context grading from evidence) and models the workflow
where the grader is not handed a pre-committed grade.

SAMPLE: Texas_Tech BYU Utah Houston Kansas Iowa_State | Tulane Memphis East_Carolina Charlotte
(deliberately includes BOTH Kansas and East Carolina to test that specific gap.)

FINDINGS (80 unit grades):
- Rank-order agreement HIGH: r = 0.921 (r^2 = 0.847).
- Mean offset +1.65 grade pts (small), SD of per-unit diff 9.89.
- SYSTEMATIC LEVEL-SLOPE DIFFERENCE (the real signal): diff(Opus-Fable) = -18.36 + 0.416*Fable_grade,
  slope t = +6.1. Opus uses more of the scale — grades high units higher, low units lower.
  Crossover ~Fable 44. Team-mean shift is monotonic in strength: Texas Tech +16.0 ... Charlotte -7.0.
- NOT a conference bias: the "B12 +5.8 / AAC -4.6" split is confounded by B12 being higher-graded
  in-sample. Kansas (-0.2) and East Carolina (-1.8), both mid-scale, are ~dead-on.

RATING IMPACT:
- NAIVE swap (no correction): 4.87 pts of rating spread across the 10; directional (widens).
  Texas Tech-Charlotte gap 36.9 -> 41.7. Kansas-ECU gap 3.55 -> 3.65 (UNCHANGED — see below).
- BRIDGE (fable_equiv = 18.33 + 0.598*opus, fit n=80): rating spread drops to 1.33 pts
  (noise, unordered); Texas Tech-Charlotte gap 36.9 -> 36.7. Residual per-unit grader noise
  after bridge = 5.29 grade pts (down from 9.89) -> ~1.3 rating pts of team-level noise.

KANSAS-ECU: two independent frontier graders, blind, both land the gap at ~3.5-3.6. The
3.5 gap is a robust property of the evidence, not a Fable artifact.

PROPOSED (not yet ratified): adopt fable_equiv = a + b*opus as a standing transform on all
go-forward Opus grades, so the ratified conversion/k/level-slope (all Fable-calibrated) still
apply and the 31 completed teams stay unchanged. Recommend refitting a,b on a larger blind
sample (all 31 done teams, regraded by Opus subagents at ~zero Fable cost) before ratifying.
