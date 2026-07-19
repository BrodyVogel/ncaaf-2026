# Rating-scale compression — diagnosis & fix (2026-07-19)

## Symptom
The win-totals engine showed a systematic tilt: it backed the **over on low-total (weak)
teams** and the **under on high-total (strong) teams**, monotonically in the market line —
present even for top teams in top conferences that never play a bottom-feeder. ~⅓ of all
cross-team edge variance was explained by the market line alone (edge~line R² = 0.32 overall,
**0.43 within the Power 4**), the fingerprint of a compressed rating scale rather than real,
independent edges.

## Diagnosis
Compared our ratings to two independent fair references — KFord Final 2025 (SD 13.0, floor
−32.8) and the market-implied ratings backed out of the win totals (SD 13.3, floor −32.4).
Ours: SD 12.5, floor −26.7. Percentiles p5–p90 matched; the gap was the **extreme tails**,
worst at the bottom (our floor 6 pts too high). Conference and P4/G5 means were already fine.

Stage-by-stage decomposition of the assembly (`final = 0.65·anchor + 0.35·grade_implied`):

| stage | SD | floor |
|---|---|---|
| grade-implied | 10.1 | −23.2 |
| anchor blend | 12.94 | −30.2 |
| final (shipped) | 12.54 | −26.7 |

The **anchor was well-calibrated** (RMSE 1.97 vs the market). The **grade→points step was the
culprit**: it is an OLS fit, and OLS fitted values are shrunk toward the mean by √R² (off
R²≈0.67 → 82% of anchor spread; def R²≈0.49 → 70%). The resulting grade residual was
negatively correlated with team strength (corr −0.43), so blending 35% of it dragged every
extreme toward the middle — symmetrically (top down, bottom up). Confirmed at the top: fixing
a top team's rating to market-implied lifted its E[wins] toward the line, while halving the
variance did almost nothing — so the top-team under-lean was rating compression, not a
variance/ceiling effect.

## Fix (`pipeline/final_pass.py`, default on; `--no-decompress` reproduces the old formula)
Two market-agnostic operations that de-compress the **grade** signal without touching the
anchor or fitting to the betting market:

1. **Un-shrink the OLS fit** — rescale `implied_off`/`implied_def` back to their anchor
   counterparts' spread (`match_spread`), undoing the √R² shrinkage.
2. **Orthogonalize the residual** — remove the component of the grade residual that is linear
   in the anchor level (that correlation *is* the compression). What remains is
   level-orthogonal, team-specific grade signal that never pulls extremes inward.

## Result

| metric | before | after | fair ref |
|---|---|---|---|
| edge~line R² (all) | 0.322 | **0.143** | → 0 |
| edge~line R² (P4) | 0.432 | **0.164** | → 0 |
| rating SD | 12.5 | **13.2** | 13.0 / 13.3 |
| floor (min) | −26.7 | −28.2 | −32.8 / −32.4 |
| top-15 mean edge | −0.064 | **−0.032** | 0 |
| bottom-15 mean edge | +0.071 | **+0.055** | 0 |
| Spearman vs old order | — | **1.00** | — |

The systematic line-correlation is more than halved and the fair spread is restored, with the
board ordering intact (it was a scale fix, not a re-rank). Verified further with `--no-decompress`
reproducing the pre-fix numbers exactly.

## Residual (deliberately not "fixed")
The floor still stops near −28 vs the references' −32.5, and the bottom tail keeps a mild
over-lean. Two causes, both left as genuine per-team judgment rather than curve-fit away: (a)
the anchor's own floor is −30.2, and pushing past it would mean calibrating the extreme tail to
external references; (b) a few bad teams are graded near average (Sam Houston, UL Monroe imply
≈ −3 when they are −20+), a grading-quality issue for specific teams, not a scale artifact.
Reclassifying programs (North Dakota State) remain a separate anchor issue, untouched by this
fix. These are surfaced for manual adjudication in the artifact rather than smoothed over.
