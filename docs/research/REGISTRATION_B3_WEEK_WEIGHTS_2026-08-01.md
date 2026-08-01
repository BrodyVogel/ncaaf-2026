# Registration — Build 3: week-indexed observation weights (2026-08-01)

Owner question: "Is there an optimal update based on time of season — weeks
1–4 more aggressive than late? Already baked in?" The DECLINE of update
aggressiveness over the season is endogenous to the v2 filter (prior weight
vs accumulated-evidence weight), and B2-N2 already made early season MORE
aggressive (looser prior, faster forgetting). What is NOT yet tested: whether
September GAMES per se carry different per-game information — week-1 rust /
vanilla schemes (noisier) vs raw talent gaps exposed (more informative).

Registered before running (no outcome computed). Baseline: frozen v2
(insession_v2_constants.json). Folds/loss/bars identical to B2 (2021–24
wk2+, pooled MAE; adopt iff ≥0.02 improvement AND ≥3/4 folds).

## Menu (one item, small grid)

Observation-noise multipliers by the GAME'S OWN week (applied to that game's
efficiency and margin rows in every subsequent solve):
- m1 (week 1) ∈ {0.8, 1.0, 1.25} — <1 = trust week-1 games MORE, >1 = less.
- m24 (weeks 2–4) ∈ {0.9, 1.0, 1.15}.
Weeks 5+ = 1.0 fixed. 8 non-baseline combos. Winner by pooled tune MAE at
the registered bar; else v2 stands and the endogenous schedule is declared
adequate at current power.

Report regardless: mean |weekly team rating change| by week (2023 example)
— the realized aggressiveness schedule, for the owner's intuition.
