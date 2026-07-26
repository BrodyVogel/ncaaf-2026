# Pre-registration — Study 5: opener margin calibration (2026-07-26)

Committed BEFORE any fitting. Purpose: the translation layer that lets the existing
power ratings price posted Week 0 / Week 1 / Game-of-the-Year spreads. Governance as
always: bars fixed now; failures reported and kept; the pricing product ships only on
PASS; owner signs off on the policy defaults before any bet.

## Peek disclosure

2026-07-23: our raw ratings' implied spreads were compared informally against the posted
2026 Week 1 board (51 games) and showed a systematic tail disagreement. That was a look
at 2026 POSTED LINES, not at this study's fit panel (2021–25 results). No 2021–25 margin
regressions have been run.

## Panel

FBS-vs-FBS regular-season games in each season's first two calendar weeks (the
Week 0 + Week 1 window), 2021–2025, from CFBD /games (scores, neutral-site flags).
Ratings: preseason SP+ vintages (`data/backtest/sp_preseason/`), the same proxy family
used by the ×0.75 season study. Closing spreads from CFBD /lines (report-only leg).
FCS-opponent games excluded (no preseason proxy; 2026 FCS games are flagged
v1-unpriceable in the product).

## Model

margin_home = b · (rat_home − rat_away) + h · site + ε      (site 1 unless neutral, then 0)

- b fitted pooled + LOYO by season (5 folds). Applied in production to the RAW power
  set — b IS the game-level shrink; the ×0.75 calibrated set plays no role here
  (using both would double-shrink).
- h fitted on non-neutral games only.
- ε kernel: empirical opener-window residuals, KDE-smoothed (Silverman), used for
  P(cover); normal-σ comparison reported. Kernel is descriptive — no bar.

## Bars and decision rules

- **S5-A (slope validity):** pooled b ∈ (0, 1) AND all five LOYO fold b's within ±0.15
  of pooled. Fail → no spread product; ratings stay totals-only.
- **S5-B (calibration helps):** LOYO margin MAE with fitted (b, h) beats the current
  engine assumption (b = 1, h = 2.3) by ≥ 0.10 points. Fail → no spread product.
- **S5-C (HFA decision rule, not a kill):** use fitted h iff |h − 2.3| ≤ 2.5 and its
  sign of deviation is fold-stable; else fall back to h = 2.3 with a note.
- **Report-only:** market-implied shrink b_mkt (regress closing spread on rating diff —
  the market's own preseason discount); linearity check (tercile slopes); residual SD
  vs the engine's 13.5.

## Production pricing rule (ships only on S5-A + S5-B pass; owner sign-off on defaults)

Fair spread = b·(our_final_diff) + h·site. Each posted spread priced under TWO lenses:
(i) fitted-b (honest) and (ii) b_mkt (our ratings wearing the market's preseason
discount — the mm analog). Cover probabilities from the kernel; de-vig from the real
two-way posted prices (no 30-cent inference needed). **Conviction = min-lens edge;
proposed bar ≥ +4% both lenses (✓✓), same as totals.** Proposed overlap policy: game
stakes count in full against the team's 1.1–1.2u season cap. Both defaults are
owner-approval items, flagged in the deliverable.

## Limitations (registered)

Proxy assumption: b is fitted on preseason SP+ and applied to our ratings on the same
anchor scale; if our ratings' game-level information content differs from SP+'s, b is
mis-scaled for us (direction unknowable pre-season; the paper-CLV log during September
is the check). Opener-window n ≈ 250–320 makes the kernel coarse near key numbers;
normal fallback reported alongside. August roster news arriving after our July grades
is handled procedurally (pre-bet freshness check), not statistically.
