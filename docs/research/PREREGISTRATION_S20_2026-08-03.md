# PREREGISTRATION S20 — Season QB passing-yards props (P4 returning starters)

Registered 2026-08-03, before any backtest computation has been run. Live
market: FanDuel "Regular Season passing yards," 17 P4 QBs, −113/−113
(breakeven 53.05% per side). Owner-confirmed settlement basis: REGULAR SEASON
ONLY (CCG/CFP excluded, per FD market naming; owner re-verifies exact house
text before any stake). Reverse-engineered desk anchor (documented in chat
2026-08-03, before this registration): posted line ≈ 12 × prior-year
per-game passing yards, ratios 0.97–1.06 for same-school returners, manual
markdowns for transfers/scheme-movers.

## Panel

QB-seasons t ∈ 2021–2025. Entry: ≥250 pass attempts in season t−1 (mimics
"put up numbers last year" — the posted 17 range 296–503), playing year t at
a power-conference program (ACC/B10/B12/SEC + Notre Dame; plus Pac-12 through
2023 and WSU/OSU after — power-by-year from membership files). Transfers
INCLUDED with a flag (the live market includes them). **All accuracy metrics
P4-only — no G5 QBs (owner instruction).** Outcome: year-t REGULAR-SEASON
passing yards (CFBD, seasonType=regular), matching settlement.

## Registered hypotheses / components

- **H1 — class bias of the desk formula.** Synthetic line L_t = 12 ×
  reg-season pace_{t−1}. Prediction: realized UNDER rate > 55%, availability-
  driven. Bar: pooled exact-binomial p < .05 AND same direction ≥4/5 years.
  This is the go/no-go for treating the class skew as real.
- **H2 — availability hazard.** Distribution of reg-season games with
  meaningful passing work (≥10 att) in year t. Report overall; splits by
  rush-share tercile (runners absorb hits) and by t−1 missed games. This
  object feeds the pricer's game-count simulation.
- **H3 — outlier-game mean reversion (owner).** Trimmed pace (drop each QB's
  top-2/bottom-2 games in t−1) vs raw pace as predictor of year-t pace.
  Prediction: trimmed MAE < raw MAE (paired).
- **H4 — level of competition (owner).** Opponent-adjusted t−1 pace using
  SP+ vintage opponent strength; "fattening share" = fraction of t−1 yards
  vs bottom-quartile opponents. Prediction: high fattening share ⇒ larger
  year-t pace decline, esp. when year-t schedule hardens.
- **H5 — PFF grade predictiveness (owner ask).** Grade–production gap:
  does t−1 PFF passing grade predict year-t pace GROWTH conditional on t−1
  pace (grade above production ⇒ rise; below ⇒ fall)? This is the props-market
  version of our grade-layer thesis and gets its own report line either way.
- **H6 — supporting cast (owner).** Returning pass-catcher share (PFF
  receiving yards returning into year t) and team offense context as
  predictors of pace change.
- **H7 — staff/scheme change (owner).** HC-change flag (coaches files) and
  transfer flag as pace-disruption predictors — variance first, direction
  second. (OC changes: no historical ledger in repo — registered DATA GAP;
  2026 OC tags applied manually in the pricer, backtest limited to HC/transfer.)
- **H8 — production vs team quality (owner's Mestemaker point).** Pace
  residualized on team SP+; prediction: high-pace/low-quality "volume" QBs
  revert hardest (their volume was partly game-state induced).
- **H9 — game state (owner).** From per-game data: pace suppression in
  games decided by ≥17 vs competitive games; year-t expected script from
  team strength. Feeds the pricer via our 2026 win distributions.

## Pricer spec (v0)

Simulate: G ~ H2 hazard (QB-adjusted); per-game yards ~ Normal(pace_adj ×
opp_factor × script_factor, σ from panel); price P(over L) at −113
(breakeven .5305). Fit on 2021–24, **calibration holdout on 2025** (price
synthetic 2025 lines, report hit rate/Brier). 2026 manual layers (OC tags,
supporting-cast reads from our unit grades) documented per QB.

## Discipline

Nine components ⇒ multiplicity: headline claims need p < .01 (t ≥ 2.5);
p < .05 items are supporting color. Any live bet: pilot lane only, 0.10–0.15u
cap per prop, max 5 props until the first season settles, owner approves each.
Soft-market caveat logged: FD first-post limits are low and the 17 names are
the shaded marquee subset. Deviations from this doc get timestamped notes in
the findings file.
