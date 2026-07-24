# Pre-registration — Study 4: retention calibration of w(n) shrinkage (2026-07-24)

Committed BEFORE the study is run. Same governance as the 2026-07-23 program: bars may
not be revised after results; failures are reported and stay out of production; production
changes additionally require explicit owner sign-off; live 2026 grades change only via a
separately-approved targeted audit.

## Disclosure of prior peek (honesty clause)

On 2026-07-24, before this registration, a POOLED descriptive diagnostic was run (owner
Q&A): centered residuals of the shipped formula by within-group grade_t decile, all four
transitions pooled, no folds. It showed a monotone gradient (−0.9 worst decile → +1.1 best;
top decile on vol≥200: +1.9). This registration therefore does NOT treat the pooled effect
as evidence: every acceptance bar below is a FOLD-STABILITY or LOYO-MAE criterion the peek
did not examine. The owner's question motivating the study: is the miscalibration confined
to the tails, or does it standardize across the whole distribution ("any above-average unit
is weighted down by rule")?

## Data & null model

`data/research/pairs.csv`, stayers only (moved=0), vol_t ≥ 10, seven position groups.
x = grade_t − posmean_g, y = grade_t1 − posmean_g, w = min(vol/(vol+k_g), cap_g) as shipped
(k: QB 230, RB 110, WRTE 190, OL 595, DL 290, LB 630, DB 1180; caps QB 0.55, LB 0.50).
Null: ŷ = α_g + w·x with per-group intercept α_g fit on train folds (center drift is
absorbed in production by the field rescale, so intercepts are not at issue).
Validation: LOYO over season_t ∈ {2021, 2022, 2023, 2024}.

## Tests and acceptance bars

- **S4-A (global retention slope).** Fit r = y − w·x on α_g + β·x. PASS = β sign-stable
  in all 4 folds AND pooled β ≥ +0.02. Interpretation if passed: the formula
  under-retains tape across the whole distribution, not just the tails — the owner's
  "any above-average unit" framing is correct.
- **S4-B (nonlinearity beyond a linear fix).** Piecewise slopes by within-group train-fold
  terciles of x: r = α_g + β_lo·x + β_mid·x + β_hi·x (indicator-partitioned). PASS =
  (β_hi − β_mid) and (β_lo − β_mid) sign-stable in all 4 folds AND LOYO MAE of the
  piecewise model beats the S4-A linear-corrected model by ≥ 0.05 grade pts. If S4-A
  passes and S4-B fails, the artifact is LINEAR under-retention and the remedy is
  recalibrating w(n) — not a spline.
- **S4-C (mechanism: k and caps).** Per-group grid refit: k* ∈ k_shipped ×
  {0.25, 0.35, 0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0}; for QB/LB additionally cap* ∈
  {shipped, 0.65, 0.75, 1.0}. Objective: LOYO test MAE of α_g + w_{k*,cap*}(n)·x.
  PASS (production-recommendable) = per-group direction of k* vs shipped (smaller /
  equal / larger) consistent in all 4 folds AND pooled LOYO MAE improvement vs shipped
  ≥ 0.03 grade pts. Report w at a typical starter season, shipped vs refit.
- **S4-D (volume texture, report-only).** Residual slope β within volume terciles — no bar.

## Decision rules (registered)

1. S4-A pass + S4-B fail + S4-C pass → recommend **k/cap refit** (linear mechanism).
2. S4-A pass + S4-B pass → recommend **two-slope/spline retention**, k refit secondary.
3. S4-A fail → no production change; log the null; 2027 candidate stays as-is.
4. Any recommendation ships only after: (a) owner sign-off, (b) pro-forma 2026 board
   impact (formula-arm recompute → dg deltas → list of adjudications whose trigger
   status flips; NO grade rewrites inside this study), (c) a targeted re-adjudication
   pass limited to units whose sweep verdict the corrected formula overturns.

## Survivorship caveat (registered limitation)

Pairs condition on playing in t+1. The formula projects rostered players expected to
play, so the conditioning approximates the target population, but retention selection
(who returns) is not modeled; class/age interactions remain unfitted (Study 2 failure
stands). Results will be reported with this limitation attached.
