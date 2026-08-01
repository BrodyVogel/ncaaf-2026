# B1 in-season anchor — as-built model spec (2026-08-01)

The frozen v1 model, stated precisely. Constants: insession_v1_constants.json.
Code: pipeline/insession/b1_fit.py (run_season). Companion docs:
IN_SEASON_ANCHOR_DESIGN (rationale), FINDINGS_B1 (evidence).

## State

Each FBS team i carries two numbers, in points, centered on the field:
- off_i — points above FBS-average its offense produces vs an average defense
- def_i — points below average an average offense manages vs its defense
  (higher = better defense)
Team overall = off_i + def_i. Gauge: after every solve, off and def are
re-centered to field mean 0 (only differences are identified; the level is a
convention).

## Priors (week 0)

Backtest 2021–25: centered preseason SP+ splits — off_i0 = sp_off_i − mean,
def_i0 = mean − sp_def_i (sign flip: SP+ def is lower-better).
Live 2026: OUR final calibrated board's implied_off / implied_dfn split (the
preseason rig's output is the prior; the anchor inherits the whole book).

## Observations (per game, i = home or lexicographic-first at neutral)

Three measurement rows per game:
1. eff_i:  pts_i^eff ≈ off_i − def_j        σ = 9.0
2. eff_j:  pts_j^eff ≈ off_j − def_i        σ = 9.0
3. margin: margin_ij − 2.5·site ≈ (off_i + def_i) − (off_j + def_j)
                                             σ = 1.5 × 9.0 = 13.5

pts^eff = 17.97 + 0.950 · totalPPA (offense, garbage-time-excluded; mapping
fit once on 2016–19 and frozen). site = 1 unless neutral. The margin channel
is deliberately trusted 1.5× less than the efficiency channels: the
scoreboard carries turnover/fluke variance that garbage-filtered PPA strips.
A constant intercept on the eff channel is gauge-inert (absorbed by
recentering) and therefore omitted. FBS-vs-FCS games are excluded entirely.

## The weekly solve (batch re-smoothing, not forward filtering)

After week W's games, ONE weighted least-squares problem over the whole
season to date:

  minimize  Σ_g  0.95^(W−w_g) · Σ_rows residual²/σ_row²        (all games so far)
          + Σ_i [ (off_i − off_i0)² + (def_i − def_i0)² ] / 4.0²   (preseason tether)
          + Σ_i (off_i + def_i − M_i^{W−1})² / 5.0²                (market tether)

- 0.95^age: games lose 5% weight per week of age (the process-noise stand-in;
  a September game still matters in November at ~70% weight).
- σ_prior = 4.0 (tight — the fit said preseason deserves more respect than
  looser priors give it; 5.5 and 7.0 tested worse).
- M^{W−1} = last week's market-implied OVERALL rating (chained ridge on
  closing spreads, λ=0.5, HFA 2.5). σ_mkt = 5.0 is a WEAK tether (worth
  −0.006 MAE pooled; the blind arm without it is computed and reported
  weekly; removing it changes little).
- Because everything re-solves every week, opponent adjustment is automatic
  AND retroactive: a week-1 win over a team that later proves good is
  revalued upward all season. There is no separate "SOS correction."

## Prediction

Pregame, week W+1:  margin-hat = (off_i + def_i) − (off_j + def_j) + 2.5·site.
Predictions are logged before those games ever enter a solve (walk-forward;
this is how all B1 numbers were scored).

## Deliberately absent (tested and REJECTED on held-out forecast MAE)

Turnover/blowout per-game noise penalties; QB-change down-weighting (changes
persist → those games are informative); innovation clipping and Student-t
robustness (monotone dose-response: any discounting of shocking games worsens
forecasts — outlier judgment belongs to the qualitative layer); G5 prior
multipliers. Never candidates in v1: special teams channel, pace/tempo
terms, success rate/explosiveness in the mean, postseason games.

## Measured behavior (2025 headline, frozen constants, untouched fold)

Margin MAE 12.10 (wk2+); beats frozen-preseason 12.19 vs 13.72 on wk3+;
RMSE vs closing spreads on the clean segment 3.5 / 2.9 / 3.8 (wk2–4 / 5–8 /
9–15); margin MAE 11.96 vs the closes' 11.70 (the market stays ~0.25
pts/game better — this model is a fair-number machine, not an edge). Speed:
prediction correlation with preseason decays 1.00 → ~0.92 (wk 6) → ~0.80
(mid-November). Single games move a team ~2–4 points; an Indiana-2024-sized
re-rating accumulates over ~4–5 weeks, mirroring the market's own pace.

## Known weaknesses (open eyes, v2 candidates)

Single flat HFA 2.5 (no team/altitude/travel variation); no pace model
(margin treated scale-invariant across styles); PPA→points mapping frozen on
2016–19 (era drift risk); FCS openers discarded → some teams' first real
update waits a week; availability-blind BY DESIGN (the qualitative layer
patches rosters before numbers ship); off/def split identification rides on
the PPA channels — any systematic PPA bias for a style (tempo, option)
leaks into the split; weekly gauge centering means levels are within-week
relative, not absolute across seasons.
