# S8b live-mirror audit — every derivation, live rig vs S8 vs S8b spec (2026-07-27)

Owner-ordered pre-registration audit after S8's construction flaws surfaced. Source of
truth for the live chain: pipeline/final_pass.py (production, owner decisions 07-19/07-23
inline), anchor run 2026-07-14, proforma_v2.py (formula-arm object), adjudication log.
S8b runs ONLY after this table is owner-reviewed.

## Component-by-component mirror

| # | component | LIVE rig | S8 did | S8b spec | residual gap |
|---|---|---|---|---|---|
| 1 | team anchor | 6-system blend, winsorized, implied off/dfn splits | SP+ overall, z-diff | preseason SP+ overall + off/def splits, per-year | single-system proxy (SP+ is the dominant anchor input); attenuating |
| 2 | unit inputs | dossier grades (human), formula-adjudicated | formula-only, slot-weighted, PERCENTILE scale | formula-only, slot-weighted, VALUE scale | dossier layer unmirrorable (hindsight-contaminated); S8b tests the mechanical core, stated scope |
| 3 | player formula | v2 constants (posmean/k/caps/jumps/FR) | same | same | pooled-fit constants (fold-stable, disclosed) |
| 4 | cross-conf scale & class | per-team classing: ND=P4, UConn=G5 (proforma P4_26 + ND exception); adjudication IND-dest fixes | IND offset group raw; ALL independents classed P4 for jumps (spine flag bug) | per-team classing by season (ND→P4/ACC-offset; UConn/UMass/Army-independent-era→G5/G5-mean offset); jump uses same | none material |
| 5 | conversion weights | OLS **with intercept**, off: 4 units→anchor off; def: 3 units→anchor dfn (lower=better); REFIT on full 138 every board | fixed display weights (QB 1.2…) over percentile means — never in production | within-year OLS per side, shadow values → SP+ off/def splits | fitted-on-SP+ vs fitted-on-blend; minor |
| 6 | un-shrink | match_spread: fitted values rescaled to anchor spread per side | absent | mirrored | none |
| 7 | residual | (impl_off−off) − (impl_def−dfn) | z(score)−z(sp) | mirrored | none |
| 8 | demeaning | conference-pool mean removed (owner policy: within-pool shape only); ND→all-P4 mean, UConn→all-G5 mean; override teams excluded from pools | ABSENT — cross-conference level polluted D | mirrored per conference-season, pseudo-pools, debut teams excluded from pools | none |
| 9 | level-orthogonalization | decompress step 2: strip resid component linear in anchor level, BEFORE clip | partial only (sp_pre as covariate; wrong order) | mirrored pre-clip | none |
| 10 | shrink + cap | adj = clip(0.35·resid, ±6) | absent | mirrored (companion regressor; see spec) | none |
| 11 | ST term | (ST_grade−50)/50, ±1 pt | absent | y−1 team PFF SPEC percentile as ST grade (shadow_proxy recipe) | dossier ST richer; tiny |
| 12 | recenter | mean shift, full field | within-year z (equivalent) | within-year demean | none |
| 13 | unreliable-grade teams | manual overrides (NDSU-type no-data artifacts) replaced + excluded from pools | debut teams included (diagnosed ≈harmless) | FBS-debut seasons (no y−1 FBS tape) excluded from pools AND panel — mirrors override policy | none |
| 14 | dossier/adjudication/news layer | human case reads, media sweeps, bounded blends | absent | absent | UNMIRRORABLE — S8b's verdict scoped to the mechanical arm only |
| 15 | outcome | (not a rig component) | final − preseason SP+ | same | one-system proxy for "consensus movement" |

## S8b regressor and bars (to be registered verbatim on owner OK)

Chain per season y: shadow unit values → within-year OLS off/def conversion →
match_spread un-shrink → resid → conference demean (pseudo-pools, debut-excluded) →
level-strip → two regressors: **R_pre = resid** (pre-K, full variance, PRIMARY for
power) and **R_adj = clip(0.35·resid, ±6) + ST term** (the applied-adjustment object,
COMPANION for product-scale reading). Both in SP+ points; β = pts of drift per pt.

Power note (pre-stated): after demean+strip, SD(R_adj) ≈ 1–1.5 pts vs miss SD ≈ 7.5 →
SE(β) ≈ 0.25–0.30 on n≈510; ΔR² is mechanically tiny for a bounded regressor, so the
S8-style ΔR² ≥ 0.02 bar would be uninterpretable here. Materiality is therefore
expressed through β itself (realization rate), not ΔR².

Bars: **PASS = t(β_pre) ≥ 2 AND LOYO sign-stable 4/4** on the primary; λ* =
clip(β_pre, 0, 1) if PASS else 0; β_adj reported with CI as the product-scale check.
Registered secondary: G5-only slice, same bars (carried from S8-L6 per its own
discipline). Report-only: P4 slice, large-|resid| terciles, new-HC, per-year c's,
2023 forensics. S8's L2 (trench/coachability) and L3 (money leg) verdicts are NOT
re-run in S8b unless owner asks; they carry S8's construction caveat where D-based
(L2a yes, L2b no — L2b never used D or the weights).

## What S8b still cannot test (unchanged scope statement)

Dossier layer, adjudication blends, media/news integration, the six-system anchor's
non-SP+ information, and 2026-style exotic-roster curation. A full S8b pass validates
the mechanical core at measured λ*; a fail says the mechanical core's live-style
adjustments do not realize in consensus drift — with the dossier layer still riding on
the 2026 live season either way.
