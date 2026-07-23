# Pre-registration — unit-forecast research program (2026-07-23)

Committed BEFORE any model was fit. Owner-approved program (this session). These criteria
may not be revised after seeing results; failed studies are reported as failures and stay
out of production. All validation is **leave-one-year-out (LOYO)** across the four
season-transitions (2021→22, 22→23, 23→24, 24→25). Everything gets reported, including
nulls. Production changes additionally require explicit owner sign-off, and nothing
touches live 2026 grades mid-season without a separately-approved targeted audit.

## Data

Player-season panel from `data/pff_history/{2021..2024}` + `data/pff` (2025), linked by
PFF `player_id`. Conference/class per (team, season) from `data/cfbd/.../records_*.json`.
Movers = team change between consecutive seasons; portal stars joined from
`portal_{2021..2026}.json` by normalized name + origin. P4(y) = SEC/B1G/B12/ACC (+ Pac-12
in 2021–23, + Notre Dame). Specialists excluded from v1. Primary facet grade per position
group (QB→passing, RB→rushing, WR/TE→receiving, OL→blocking, front-7/DB→defense);
volume = the file-native workload count (dropbacks/carries/routes/snaps).

## Study 1 — transfer translation

Model: grade_{t+1} ~ grade_t × volume_t with position effects; movement dummies
(within-class move, P4→G5, G5→P4) estimated against the **stayer baseline** (nets out
global aging/regression); usage-tercile × P4→G5 interaction (owner question); destination-
conference effects among movers (report-only, expect low power).

**Acceptance bars (production = replace flat conference offsets in grading):**
- S1-A: LOYO MAE on movers' grade_{t+1} beats naive carry-forward by **≥ 2%** AND beats
  (or ties within 0.5%) the current flat-offset rule emulated from
  `data/backtest/conf_offsets_2021_2025.json`.
- S1-B: class-jump coefficient signs stable in **all 4** LOYO folds.
- Report regardless: effect sizes with CIs, usage interactions, destination-conf table.

**Stars leg (report either way; no production gate needed to "confirm the owner's prior"):**
- S1-C: portal stars add partial R² **≥ 0.01** on movers' grade_{t+1} after controlling
  grade_t + volume_t + position → "ratings carry incremental signal." Below that =
  owner's skepticism confirmed.
- S1-D: for entrants with NO prior FBS row (FCS/JUCO/HS-recent): corr(stars,
  first-FBS grade) **≥ 0.15** to qualify stars as a usable prior component in Study 2.

## Study 2 — thin-sample reliability + priors

Stayers only (same team t and t+1, isolating measurement noise from context change):
regression slope of grade_{t+1} on grade_t within volume buckets, per position group =
reliability; fit shrinkage as w(n) = n/(n+k) per position (k = "phantom snaps of
league-average play").

**Acceptance bars (production = shrinkage table + prior formula in the grading manual):**
- S2-A: reliability weakly increasing in volume in ≥ 3 of 4 folds per position group
  (monotonicity sanity).
- S2-B: fitted k stable across folds (coefficient of variation **< 50%**) for the
  position groups we ship.
- Class-year aging curves (FR→SO→JR→SR mean deltas, rosters 2022+) are descriptive;
  ship only if sign-stable across years.

## Study 3 — continuity (deferred to next session)

Outcome: team facet grade t+1 residualized on talent-only forecast (needs S1+S2
machinery). Predictors: HC continuity, returning-QB, their interaction with prior unit
level AND 2-yr stability (owner's conditioning hypothesis). Bar: effect **≥ 1 grade
point** equivalent, sign-stable across folds. OC/DC table is a later hand-build.

## Known limitations (accepted going in)

- FBS-only panel: FCS→FBS movers have no prior-year grade; they enter via S1-D/S2 priors,
  not the translation model.
- Portal-name matching is fuzzy; match rate reported, unmatched movers keep team-change
  labels without stars.
- 4 transitions ≈ small for staff-level effects; individual-staff claims require a
  Bonferroni-adjusted p < 0.05 and are otherwise reported as anecdotes.
- PFF grades are themselves estimates; "reliability" here conflates measurement noise
  with true year-over-year change — acceptable because the production use (how much to
  trust n snaps when projecting next season) is exactly this composite quantity.

## Study 2b — HS recruiting composites as the small-sample prior (registered 2026-07-23, before any pull/fit)

Owner hypothesis: HS pedigree should inform the prior that w(n) shrinks toward (a 5-star
first-time player ≠ a 2-star). Data: CFBD `/recruiting/players` classes 2017–2025 (player
name, position, stars, composite rating, committedTo), matched by normalized name + school
to each panel player's **first meaningful-volume season** (volume ≥ the registered VOLMIN
floors). Outcome: that first-tape grade.

**Bars (same as S1-D for apples-to-apples with the failed transfer-stars test):**
- S2b-A: partial correlation of composite rating with first-tape grade, controlling
  position group, **≥ 0.15** → ships as the prior component in w(n): prior =
  position mean + c·(composite − composite mean).
- S2b-B: the effect must hold (sign-positive, ≥ half the pooled magnitude) in the
  **late-breakout slice** — players whose first meaningful volume comes in campus year
  ≥ 2 (the owner's motivating case) — else ship for true-freshman priors only.
- Report regardless: means by star tier, per-position partials, match rate, and the
  comparison to the transfer-stars null.

## S1-E — origin-program talent as a thin-tape mover prior (registered before fit)

Owner hypothesis (the "Georgia backup → UAB" case): a thin-tape mover from an elite
roster should project above one from a weak roster, beyond the class-jump term. Predictor:
CFBD team talent composite of the ORIGIN team in season t, z-scored within year. Sample:
movers with any tape (vol_t ≥ 10); "thin" = below the position-median mover volume.
Model: S1 base (grade_t, log vol, position FE, jump dummies) + talent_z (+ talent_z×thin).

**Bars:** ships as a thin-tape origin-talent term iff ΔR² ≥ 0.01 on the thin-mover
subsample AND talent_z sign-positive in all 4 LOYO folds. Report effect size per 1 SD of
origin talent either way.

## S2-C — career-pooled evidence vs last-season-only (registered before fit)

Owner's journeyman case: a 5th-year player's many prior seasons should pin him better
than one season can. Pooled evidence: volume- and recency-weighted career grade with
decay 0.5 per season back (FIXED a priori, not tuned); n_eff = Σ decayed volume.
Both arms use the full v2 formula (prior + w(n)·(evidence − prior) + jump term; w caps
QB 0.55 / LB 0.50). Eval: LOYO MAE on all pairs with vol_t ≥ 10.

**Bars:** pooled arm ships iff it beats single-season by ≥ 1% MAE overall AND ≥ 2% on
the multi-history slice (players with ≥ 2 prior seasons), with no slice degrading > 0.5%.
