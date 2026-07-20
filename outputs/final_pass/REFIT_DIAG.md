# Final-pass refit diagnostic — 2026-07-20T00:37:02+00:00 @ e4b9663

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

intercepts: off +8.07, def +39.50

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.001** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.57 / p90 6.31 / max 14.68

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Mid-American | 13 | -1.58 | -14.7 | +5.9 |
| Conference USA | 10 | -1.50 | -7.1 | +3.5 |
| Sun Belt | 14 | -1.18 | -9.0 | +5.4 |
| Mountain West | 10 | -1.01 | -8.9 | +4.5 |
| American Athletic | 14 | -0.79 | -10.0 | +11.0 |
| Pac-12 | 8 | -0.45 | -6.1 | +5.9 |
| ACC | 17 | +0.51 | -3.4 | +4.9 |
| Big 12 | 16 | +0.62 | -3.8 | +7.8 |
| Big Ten | 18 | +1.03 | -8.3 | +5.4 |
| SEC | 16 | +1.37 | -5.6 | +6.5 |
| FBS Independents | 2 | +8.93 | +6.6 | +11.3 |

## Movers vs the pilot-era board (mean |Δ| 2.49, max 6.61; rank Spearman vs pilot-era 0.990)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| Notre Dame | +6.61 | | Middle Tennessee | -4.98 |
| Oregon | +6.28 | | New Mexico State | -4.93 |
| Georgia | +6.04 | | Missouri State | -4.69 |
| Ole Miss | +5.85 | | Sam Houston | -4.66 |
| Texas | +5.55 | | Kennesaw State | -4.51 |
| Ohio State | +5.52 | | Liberty | -4.44 |
| LSU | +5.44 | | Florida International | -4.29 |
| Oklahoma | +5.29 | | UL Monroe | -3.95 |
| Texas A&M | +4.89 | | Jacksonville State | -3.94 |
| BYU | +4.77 | | Delaware | -3.91 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.51), UConn -> all-G5 mean (+0.49).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -14.71 | -5.15 |
| Mid-American | -6.24 | -2.18 |
| SEC | -5.19 | -1.82 |
| Pac-12 | -3.57 | -1.25 |
| Big 12 | -0.66 | -0.23 |
| ACC | -0.45 | -0.16 |
| American Athletic | +0.57 | +0.20 |
| Big Ten | +3.50 | +1.23 |
| FBS Independents | +8.21 | +2.87 |
| Sun Belt | +9.98 | +3.49 |
| Conference USA | +13.09 | +4.58 |
| (all-P4 pool / ND ref) | -0.51 | -0.18 |
| (all-G5 pool / UConn ref) | +0.49 | +0.17 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
