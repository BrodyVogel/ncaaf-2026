# Final-pass refit diagnostic — 2026-07-23T15:59:53+00:00 @ a78c71f

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.149 |
| off | RB | +0.092 | +0.147 |
| off | WRTE | +0.037 | +0.028 |
| off | OL | +0.082 | +0.064 |
| def | DL | -0.083 | -0.154 |
| def | LB | -0.059 | -0.022 |
| def | DB | -0.096 | -0.134 |
| off | R² | 0.54 | 0.67 |
| def | R² | 0.61 | 0.49 |

intercepts: off +8.06, def +39.51

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.001** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.61 / p90 6.52 / max 14.43

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -1.86 | -7.5 | +3.2 |
| Pac-12 | 8 | -1.75 | -7.4 | +4.7 |
| Mountain West | 10 | -1.66 | -9.7 | +3.9 |
| Mid-American | 13 | -1.22 | -14.4 | +6.4 |
| Sun Belt | 14 | -0.86 | -8.8 | +5.9 |
| American Athletic | 14 | -0.51 | -9.7 | +11.3 |
| ACC | 17 | +0.66 | -3.3 | +5.1 |
| Big 12 | 16 | +0.75 | -3.6 | +7.9 |
| Big Ten | 18 | +1.12 | -8.2 | +5.6 |
| SEC | 16 | +1.43 | -5.6 | +6.7 |
| FBS Independents | 2 | +8.90 | +6.5 | +11.3 |

## Movers vs the pilot-era board (mean |Δ| 2.51, max 10.67; rank Spearman vs pilot-era 0.986)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | Middle Tennessee | -5.08 |
| Notre Dame | +6.59 | | New Mexico State | -5.04 |
| Oregon | +6.25 | | Missouri State | -4.81 |
| Georgia | +6.03 | | Sam Houston | -4.76 |
| Ole Miss | +5.86 | | Liberty | -4.58 |
| Texas | +5.54 | | Florida International | -4.42 |
| Ohio State | +5.49 | | Delaware | -4.04 |
| LSU | +5.45 | | UL Monroe | -3.80 |
| Oklahoma | +5.29 | | Western Kentucky | -3.64 |
| Texas A&M | +4.89 | | Georgia State | -3.62 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.51), UConn -> all-G5 mean (+0.83).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -13.73 | -4.81 |
| Mid-American | -6.26 | -2.19 |
| SEC | -5.18 | -1.81 |
| Pac-12 | -2.03 | -0.71 |
| Big 12 | -0.66 | -0.23 |
| ACC | -0.45 | -0.16 |
| American Athletic | +0.56 | +0.20 |
| Big Ten | +3.51 | +1.23 |
| FBS Independents | +8.22 | +2.88 |
| Sun Belt | +9.97 | +3.49 |
| Conference USA | +13.80 | +4.83 |
| (all-P4 pool / ND ref) | -0.51 | -0.18 |
| (all-G5 pool / UConn ref) | +0.83 | +0.29 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
