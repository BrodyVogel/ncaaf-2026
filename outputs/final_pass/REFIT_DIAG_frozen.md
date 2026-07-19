# Final-pass refit diagnostic — 2026-07-19T00:13:56+00:00 @ 9b80c41

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.149 |
| off | RB | +0.092 | +0.147 |
| off | WRTE | +0.037 | +0.028 |
| off | OL | +0.082 | +0.064 |
| def | DL | -0.083 | -0.151 |
| def | LB | -0.059 | -0.027 |
| def | DB | -0.096 | -0.133 |
| off | R² | 0.54 | 0.67 |
| def | R² | 0.61 | 0.49 |

intercepts: off +8.09, def +39.54

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.363** (R² 0.38); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean +0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **3** teams: Middle Tennessee, Sam Houston, UL Monroe
- |resid| p50 4.75 / p90 12.37 / max 19.81

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Mountain West | 10 | -9.03 | -17.0 | -3.1 |
| SEC | 16 | -7.58 | -15.1 | -0.4 |
| Big 12 | 16 | -2.25 | -8.5 | +2.1 |
| Pac-12 | 8 | -2.08 | -8.9 | +3.9 |
| ACC | 17 | -1.84 | -9.0 | +4.2 |
| Mid-American | 13 | -1.27 | -14.6 | +9.0 |
| Big Ten | 18 | -0.21 | -7.8 | +5.5 |
| American Athletic | 14 | +2.42 | -6.8 | +12.1 |
| FBS Independents | 2 | +4.26 | -4.0 | +12.5 |
| Sun Belt | 14 | +10.08 | +0.6 | +18.5 |
| Conference USA | 10 | +13.23 | +7.2 | +19.8 |

## Movers vs the pilot-era board (mean |Δ| 1.06, max 3.75; rank Spearman vs pilot-era 0.999)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| Oregon | +3.75 | | Ball State | -1.28 |
| Ohio State | +3.17 | | Massachusetts | -1.28 |
| Notre Dame | +2.93 | | UTEP | -1.25 |
| USC | +2.88 | | Northern Illinois | -1.21 |
| Michigan | +2.64 | | North Dakota State | -1.18 |
| BYU | +2.46 | | Sacramento State | -1.17 |
| Miami | +2.29 | | San José State | -1.00 |
| Indiana | +2.27 | | Wyoming | -0.98 |
| Penn State | +2.27 | | Ohio | -0.96 |
| Ole Miss | +2.13 | | Nevada | -0.83 |

## Conference-level component would be removed (frozen comparison run) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-2.89), UConn -> all-G5 mean (+2.81).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -9.03 | -3.16 |
| SEC | -7.58 | -2.65 |
| Big 12 | -2.25 | -0.79 |
| Pac-12 | -2.08 | -0.73 |
| ACC | -1.84 | -0.65 |
| Mid-American | -1.27 | -0.44 |
| Big Ten | -0.21 | -0.07 |
| American Athletic | +2.42 | +0.85 |
| FBS Independents | +4.26 | +1.49 |
| Sun Belt | +10.08 | +3.53 |
| Conference USA | +13.23 | +4.63 |
| (all-P4 pool / ND ref) | -2.89 | -1.01 |
| (all-G5 pool / UConn ref) | +2.81 | +0.98 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.588; mode FROZEN-RESID comparison variant
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
