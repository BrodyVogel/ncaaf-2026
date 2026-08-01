# Pre-registration — Study 15: level-conditioning of win-total error structure (2026-08-01)

Parking-lot item 6, owner-commissioned ("finer than G5/P4"), scoped to the
win-total space per owner. Question: does the error structure that our
betting machinery rides on vary CONTINUOUSLY with consensus team strength, in
ways the binary G5/P4 split misses (the Georgia-vs-Purdue gulf)?

**Peek disclosure (seen, motivating, not re-claimed):** S9/S13 established
level-dependence for ONE factor (rp/disruption concentrates in the middle
preseason tercile; board-validated). S8b found the mechanical arm's signal
P4>G5 under the live-mirror. K3 established macro overs concentrate on low
totals (totals correlate with level — entanglement noted below). S15's new
questions are the two structures never conditioned on level: preseason
uncertainty itself, and the F1 consensus-vs-market zone edge.

## Data

Miss panel: SP+ preseason vs final, 2021–2025 (n≈650 team-seasons).
Board panel: SBD DK openers 2022–24 + settlements (S7/S12-E harness:
sched_exp probit, HFA 2.3, σ 13.5, wins from games files). Level = within-year
percentile of preseason SP+ overall among FBS (registered primary; raw points
scale as robustness). G5 = non-P4 conference (ND P4), as everywhere.

## Legs and bars

- **S15-L1 (uncertainty structure):** |miss| ~ G5 (binary baseline) vs
  G5 + pctl + pctl² (continuous). CLAIM "level-conditioning matters for
  uncertainty" iff a continuous term reaches |t| ≥ 2 AND ΔR² ≥ 0.01 over the
  binary model AND LOYO sign-stability 4/5 on the significant term. Report
  the fitted shape (where uncertainty peaks) and a within-P4-only slice
  (the direct Georgia-vs-Purdue read).
- **S15-L2 (the money leg — F1 by level):** S7-convention zone bets
  (|E_wins(consensus) − line| ≥ 1.0 → consensus side, pushes excluded):
  (i) side-rate by within-year level tercile of the board sample (report);
  (ii) logistic P(side wins) ~ level percentile. CLAIM "F1 is
  level-dependent" iff the logistic slope |t| ≥ 2 with LOYO sign 3/3.
  Expected n ≈ 200–230 zone bets — powered only for a strong gradient;
  an honest null is the likely outcome and is fine.
- **S15-L3 (report-only):** zone side-rate split overs vs unders × tercile —
  read alongside K3's low-total overs concentration; no claim (entangled
  with totals-level correlation, disclosed).

## Decision rules (registered)

- L1 PASS → the 2027 build registry item upgrades: bands/k-table/blend caps
  get a CONTINUOUS level form (design registered before any 2027 fitting);
  no 2026 rating or board change.
- L2 PASS → a level-based SIZING tie-breaker (Amendment-2 candidate for the
  completion screen, same license shape as the rp Amendment 1) is drafted
  for owner sign-off — qualification bars stay untouched.
- All-null → item 6 closes as "binary split adequate at current power";
  2027 candidate demoted.

## Limitations

Reused panels (S6–S13 lineage, disclosed); SBD boards P4-heavy (level
terciles within-board, so the G5 tail is thin); 5 seasons for L1, 3 for L2;
percentile conditioning coarse at the extreme top (n≈5–10 teams/yr above
95th pctl); multiplicity ≈ 4 looks.
