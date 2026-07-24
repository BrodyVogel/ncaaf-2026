# Pre-registration — Study 4b: two-parameter retention curve (2026-07-24)

Committed BEFORE fitting. Governance as before. Owner directive 2026-07-24: if 4b passes,
ship the full chain now (corrected sweep → targeted flip audit → v2.4 rebuild → re-priced
book). **If any bar fails, nothing ships** and camp re-sweeps stay on the shipped v2 form.

## Peek disclosure

Motivated by the Study 4 volume-decile table (pooled, no folds): true reliability rises
~2× faster than n/(n+k) at low volume and plateaus ≈0.44–0.50 at d7–d9 while the
hyperbola climbs to 0.58. All bars below are LOYO / fold-stability criteria; the pooled
table is not the acceptance evidence.

## Candidate form

w'(n) = min( n / (n + k′_g), p_g ) — per group g: k′_g = k_shipped_g × m_g,
m_g ∈ {0.15, 0.20, 0.25, 0.35, 0.50, 0.70, 0.85, 1.00, 1.20}; plateau p_g ∈
{0.350, 0.375, …, 0.700} (step 0.025). Matched-tape arm only; FR priors, 2024
look-through ×0.5, jumps, and dterm scale terms unchanged. Objective: LOYO test MAE of
α_g(train) + w′(n)·x on the Study 4 panel (16,719 stayer pairs, vol ≥ 10).

## Acceptance bars (all must pass)

- **B1 (accuracy):** pooled LOYO MAE improvement vs shipped w ≥ **+0.015** grade pts
  (i.e., beats the flat-β patch's +0.0137, which is rejected on S4-D grounds).
- **B2 (calibration collapse):** under the fitted form, the S4-A residual slope β
  re-estimated per fold satisfies pooled |β| ≤ **0.02** AND the four fold βs are NOT
  all the same sign (no stable residual slope remains).
- **B3 (parameter stability):** refit on each fold's train set: all four fold-fit
  plateaus within **±0.05** of the pooled fit per group, and all four fold-fit m_g on
  the same side of 1.0 as the pooled fit (or equal) per group.

## Registered deployment (fires only on PASS)

1. Constants move to a single shared module (`pipeline/grading_w.py`); spec addendum.
2. Sweep dg recomputed under w′; **flip units** = trigger status (|dg|>8) differs from
   the logged v2 sweep. Audit policy: every flip unit gets an evidence case read.
   Newly-triggered → blend on dg_new with standard policy (DB ⅓, LB 0.40, else 0.50;
   info guard; academy halving; cap ±8) unless the read rejects it. De-triggered (v2
   blend now unsupported) → default KEEP the human-confirmed v2 verdict unless the
   corrected picture removes the original blend rationale; then revert partially/fully.
   Rows appended as `S4B-AUDIT` (last-write-wins).
3. Rebuild from the v1 grade baseline (git 36fcfed) replaying the full log → final_pass
   → payload/artifacts/tracker. Vintage **v2.4**.
4. Provenance ledger: every held bet and pending entry re-priced v2.3 vs v2.4, deltas
   reported regardless of direction.

## Limitation carried forward

Survivor-conditioned pairs; class/age and program×unit effects remain unmodeled
(registered 2027 candidates).
