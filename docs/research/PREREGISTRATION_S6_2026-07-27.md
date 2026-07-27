# Pre-registration — Study 6: consensus-miss predictors (2026-07-27)

Committed BEFORE analysis. Target: miss_y = final SP+_y − preseason SP+_y (in-repo
vintages, 2022–2025 usable). Baseline model: miss ~ a + b·preseason_SP+ (mean-reversion
level control). Each factor is tested as an ADDITION to that baseline. LOYO by season
(4 folds). Owner-approved primary trio; hype/churn/off-def/G5-poach are later legs.

- **F1 prior-year luck:** prior-season (actual wins − Σ postgame win expectancy) from
  CFBD game data. Hypothesis: lucky_{y−1} → negative miss_y beyond level reversion.
- **F2 returning-production overweight:** CFBD returning production (%PPA), season y.
  Hypothesis: consensus overweights RP → high-RP teams under-deliver vs preseason
  number (negative coefficient), or the reverse; sign left free, stability required.
- **F3 trench concentration:** from the PFF spine, prior-season team OL+DL mean
  as-played grade minus skill (QB/RB/WRTE) mean, z-scored. Hypothesis (S4-derived):
  trench-tilted quality persists → positive miss.

**Bars per factor (all required to validate):** coefficient sign identical in all 4
LOYO train-folds; pooled |t| ≥ 2; ΔR² over the level-only baseline ≥ 0.02.
**Decision:** survivors → registered 2027 overlay candidates AND an immediate
descriptive audit of the current 24-ticket book (which side of the factor each position
sits on; no bet changes without owner sign-off). Failures reported and kept. Multiple-
testing note: three primaries, so expect ≥1 false survivor at ~10% if all are null;
treat single-bar-margin survivals with suspicion.
