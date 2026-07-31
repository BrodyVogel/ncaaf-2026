# Registration — Build 1: in-season mechanical anchor (2026-08-01)

Engineering build under IN_SEASON_ANCHOR_DESIGN_2026-08-01.md, registered
BEFORE any fitting. "B" series = builds (pre-committed loss + selection
procedure + freeze rules), distinct from "S" hypothesis studies. No outcome
statistic has been computed from the P0 panel beyond the coverage census in
commit 798efbb.

## Data and folds

Panel: data/research/insession_panel_2016_2025.csv (15,342 team-games).
- **2016–2019:** observation-model fitting years. No preseason SP+ available →
  flat conference-mean prior; contribute to loss only weeks ≥5 (post-burn-in).
- **2020:** EXCLUDED from tuning and evaluation (COVID: opt-outs, empty
  stadiums, short season). Kept in panel for continuity only.
- **2021–2024:** full-system tune folds (preseason SP+ off/def priors from
  data/backtest CSVs; LOYO within these four).
- **2025:** RESERVED. Untouched during all tuning; single final run after
  freeze = the headline out-of-sample number.

Exclusions: FBS-vs-FCS games are excluded from observations AND loss (v1;
opponent unrated). Postseason excluded. QB-change flag recomputed as ROLLING
modal (starter ≠ modal of team's PRIOR games this season; week-1 exempt).

## Model structure (fixed) and menu (registered search space)

State per team: (off, def), points scale. Observations per game: (a) sided
efficiency: team totalPPA vs opponent ≈ μ + off_i − def_j; (b) mirrored for
opponent; (c) margin channel ≈ (off_i−def_j) − (off_j−def_i) + HFA·site.
Weekly ridge solve, walk-forward; S smoothing re-passes over the season to
date. Gauge: FBS mean preserved. HFA single fitted constant.

Stage-wise GREEDY selection (registered procedure; coarse grids, winner by
tune-fold pooled MAE):
- **M1 baseline:** σ_prior ∈ {4, 5.5, 7}, weekly σ_proc ∈ {0.5, 1.0, 1.5},
  channel σ_obs and HFA fit; smoothing passes S ∈ {1, 3}.
- **M2 per-game noise:** σ_obs multipliers from turnovers, plays, blowout
  indicator; QB-change down-weight w_qb ∈ {1.0, 0.5, 0.25}.
- **M3 robustness:** none vs hard clip (innovation cap ∈ {2, 3}σ) vs soft-t
  (IRLS, ν ∈ {4, 8}). Winner by MAE; clipped-residue diagnostic reported
  regardless (does discarded innovation predict next-3-week drift? |t|≥2 →
  flag for live-ops loosening).
- **M4 market-augmented arm (2021–24 only):** last-week market-implied
  ratings (chained ridge from lines, demo machinery) as an extra per-team
  measurement, weight fitted. Ship decision by MAE; the BLIND arm is
  computed and reported weekly in live operation regardless (attribution).
- **M5 conditioning:** variance multipliers — G5 σ_prior×{1.25, 1.5}, newHC
  σ_prior/early-σ_proc×{1.25, 1.5} (coaches data 2021+), rp low-continuity
  σ_prior scaling (2022+). KEEP a term iff pooled tune MAE improves ≥0.02
  AND ≥3/4 folds improve.

## Loss and bars

Loss: out-of-sample pre-game margin MAE, weeks ≥2 (2021–24) / ≥5 (2016–19),
FBS-vs-FBS, walk-forward (predictions use only prior information; smoothing
re-passes never see the predicted week).

- **B1-i (gate):** final config beats FROZEN-PRESEASON-ALL-SEASON on the
  weeks-3+ slice, pooled AND in ≥3/4 tune folds.
- **B1-ii (gate):** beats margin-only Elo (K fit on the same tune folds) pooled.
- **B1-iii (report):** clean-segment gap to closing spreads by week bucket
  (clean = no QB-change flag, |open−close| < 2.5, both posted). Aspiration
  from the design doc: RMSE ≤ ~3.5 by weeks 8+. Report-only in B1.
- **B1-iv (report):** implied gain schedule — effective preseason weight by
  week — vs the S14-C market drift curve; per-game rating-move distribution
  (the "5–10 pts early" sanity check).
- FAIL both gates after M3 → per design doc, the home-built anchor is not
  good enough to carry a qualitative layer; program stops before the paper
  year. Gates re-checked on the 2025 headline run (a headline reversal is
  reported, not silently absorbed).

## Freeze

Winning config + all constants → data/research/insession_v1_constants.json,
committed with FINDINGS_B1. Any post-freeze change requires a new B
registration. The 2025 run happens ONCE, after freeze, and is reported as-is.

## Limitations (registered)

Marginal-MAE differences between rating systems are small (market ≈ 12.0–12.5
all year); the build claims infrastructure quality, not betting edge — edge
claims remain with the paper year (T2) per SINGLE_GAME_PROGRAM. Composite
observation is PPA-only in v1 (SR/explosiveness enter σ, not the mean; ST
omitted). 2016–19 priors are flat (conference mean), so those years inform
observation noise more than prior/gain constants. Greedy stage-wise search
can miss interactions (accepted for v1 tractability).
