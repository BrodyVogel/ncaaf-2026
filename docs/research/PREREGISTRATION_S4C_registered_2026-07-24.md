# Pre-registration — Study 4c: pooled retention correction (registered 2026-07-24,
# to be EXECUTED for the 2027 build when 2025→26 pairs exist)

Registered now, before any 2026 season outcomes exist, so the future test is clean.
This is the single next-and-final corrective form for the S4 phenomenon. If it fails,
the shipped v2 w(n) stands for 2027 as well and the S4 doctrine remains reading guidance.

## Form (fixed now; no alternatives may be substituted at run time)

w′(n) = min( n / (n + m·k_g), p ) with ONE pooled m and ONE pooled p across all seven
groups (k_g = shipped per-group k; QB/LB caps replaced by p). Grids: m ∈ {0.15…1.20}
(9 points as in 4b), p ∈ {0.350…0.700} step 0.025.

## Data

Study 4 panel plus the 2025→26 transition (five folds). Stayers, vol ≥ 10, same
construction as `build_spine.py`/pairs.

## Bars (all must pass; LOYO over five folds)

- C1: pooled LOYO MAE gain vs shipped ≥ +0.010.
- C2: residual slope collapse — pooled |β| ≤ 0.015 AND five fold βs not all same sign.
- C3: fold-fit stability — all five fold-fit p within ±0.05 of pooled; all five fold-fit
  m on the pooled side of 1.0 (or equal).
- C4 (new-data guard): on the held-out 2025→26 fold specifically, the fitted form's MAE
  must not be worse than shipped by more than 0.01 (protects against the correction
  being an artifact of the 2021–24 era's grading regime).

## Deployment on PASS

2027 build only (constants module + full regrade under 2027 process). No retroactive
2026 changes.
