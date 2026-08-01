# Registration — Build 2: anchor v2 upgrade pass (2026-08-01)

Owner-commissioned refinements to the frozen B1 anchor, targeting his four
critiques + the week-profile question. Registered before any B2 fitting.
Baseline = frozen v1 (insession_v1_constants.json, commit 579553f).

## Peek disclosure

Seen before this registration: everything in FINDINGS_B1; plus one diagnostic
run post-freeze (2026-08-01, in-chat): the PPA→points mapping refit by era —
2016–19: 17.97+0.950·PPA; 2021–24: 16.81+0.898; 2023–25: 16.83+0.908. That
peek MOTIVATES item N1 (drift is real); its adoption still must clear the
registered bar. No other B2 quantity has been computed.

## Folds, loss, bars

Tune folds: PORTAL ERA ONLY — 2021–24, weeks 2+, FBS-vs-FBS (his era
concern applied to evaluation as well as coefficients). Loss: same
walk-forward pre-game margin MAE. Greedy sequential adoption; each item KEPT
iff pooled tune MAE improves ≥0.02 vs the running config AND ≥3/4 folds
improve. 2025: single re-run at the end IF any item adopts. DISCLOSED: 2025
was already opened once for the v1 headline, so the v2 2025 number is a
lightly-reused holdout (constants still never selected on it) — stated with
that caveat wherever reported.

## Registered items (order fixed)

- **N0 (report):** frozen v1 re-scored on portal-era folds + **week-profile
  table** — model vs frozen-preseason vs market-close MAE by week bucket
  (2–4 / 5–8 / 9–15), per fold and pooled. This answers the owner's
  better/worse/consistent question. Pre-stated interpretation rule: if the
  early-bucket (2–4) model-minus-market gap exceeds 2× the late-bucket gap,
  declare an "early-season anchor weakness" finding and treat N6 as its
  designated remedy candidate.
- **N1 era mapping:** replace the 2016–19 PPA→points conversion with the
  2021–24 fit (slope 0.898). Bar as above.
- **N2 portal-era selection robustness:** re-grid the M1 core (σ_prior ×
  ρ × σ_m) on 2021–24 folds only. If a different winner beats the running
  config by the bar → adopt; else report "v1 constants era-robust."
- **N3 per-team HFA (hierarchical):** add per-team home-advantage states
  h_i (margin rows get site-coefficient on h_i), prior 0, σ_h ∈ {0.5, 1.0}
  — per-team HFA shrunk toward the global 2.5. Bar as above.
- **N4 off/def asymmetric prediction:** margin-hat = α·Δoff + β·Δdef + HFA
  with (α,β) ∈ {(1.1,0.9), (1.2,0.8)} (owner: "good offense worth more").
  Prediction-side only; solve unchanged. Bar as above.
- **N5 level-specific conversion:** separate PPA→points mappings by offense
  class (P4 vs G5, 2021–24 fits). Bar as above.
- **N6 early-season market tether:** σ_mkt tightened to {2.0, 3.0} for
  weeks ≤5 only (baseline 5.0 thereafter) — lean harder on the market's
  numbers exactly when our own game data is thinnest. Attribution unaffected
  (blind arm computed regardless). Bar as above.

## Outputs

FINDINGS_B2 with per-item verdicts + the N0 week-profile table + final
week-profile of the adopted config; insession_v2_constants.json IF anything
adopts (else v1 stands); the P3 runner consumes whichever is current.
