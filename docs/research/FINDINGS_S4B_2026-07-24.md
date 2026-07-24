# Study 4b findings — two-parameter retention curve: FAIL, nothing ships (2026-07-24)

Pre-registration: `PREREGISTRATION_S4B_2026-07-24.md` (committed before fitting).
Owner directive was to ship the full chain on PASS. All three bars failed; per the
registered condition, **no production change of any kind ships**.

## Results

| Bar | Result | Verdict |
|---|---|---|
| B1 accuracy (pooled LOYO gain ≥ +0.015) | **+0.0027** — 4 of 7 groups got WORSE out-of-sample (RB −0.002, OL −0.023, DL −0.005, DB −0.004) | FAIL |
| B2 calibration collapse (pooled \|β\| ≤ 0.02, folds not same-sign) | β +0.0155 but folds +0.027/+0.002/+0.021/+0.020 — still same-sign | FAIL |
| B3 parameter stability (plateau ±0.05, m same side) | QB plateau 0.500–0.650 across folds; OL 0.450–0.650; DB 0.375–0.525 | FAIL |

## Interpretation

The phenomenon is real (S4-A stands: global +0.059, sign-stable 4/4 folds) but THIN —
~0.05 slope units against outcomes with ~7-point MAE. Pooled across 16,719 pairs it is
unmistakable; split per-group with two free parameters it is under-determined: the
(k′, plateau) objective surface is nearly flat, fold fits wander, and out-of-sample
gains evaporate. Three corrective forms have now failed under registration: spline
(S4-B), per-group k regrid (S4-C), per-group k′+plateau (4b: B1+B2+B3). Iterating
further forms against the same panel until one passes is the forking-paths anti-pattern
the governance exists to prevent. Stopped here by rule.

## What ships instead (knowledge, not constants)

1. **Adjudication doctrine (S4 doctrine), effective for the fall-camp re-sweeps:** where
   a unit's formula value rests on thin tape (low info share; volumes in the bottom
   third of the position's distribution), the formula's pull toward the mean is
   known-too-strong (+0.04–0.07 slope units, S4-A/S4-D); case reads should weight the
   dossier's tape-based view accordingly. Where the value rests on full-season tape,
   no discount — that end is calibrated to slightly over-retained. This is reading
   guidance in the same class as the Houser don't-double-discount lesson; it changes
   no constants.
2. **Study 4c pre-specified NOW for the 2027 build** (see
   `PREREGISTRATION_S4C_registered_2026-07-24.md`): the single next-and-final form —
   POOLED two parameters (one m, one p across all groups) — to be tested when the
   2025→26 transition adds a fifth fold. Pre-committing the form today, before 2026
   outcomes exist, keeps that future test clean.

## Board status

v2.3 stands untouched. Known-artifact exposure remains as bounded by the Study 4
pro-forma: ~1 rank point mean drift, team ratings ≲0.2 pts, no bet verdict affected.
Camp re-sweeps run on the shipped v2 form with the S4 doctrine in hand.
