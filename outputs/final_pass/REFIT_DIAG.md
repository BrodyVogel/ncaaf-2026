# Final-pass refit diagnostic — 2026-07-23T22:11:15+00:00 @ 1ece5e7

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.130 |
| off | RB | +0.092 | +0.156 |
| off | WRTE | +0.037 | +0.026 |
| off | OL | +0.082 | +0.077 |
| def | DL | -0.083 | -0.142 |
| def | LB | -0.059 | -0.037 |
| def | DB | -0.096 | -0.128 |
| off | R² | 0.54 | 0.66 |
| def | R² | 0.61 | 0.47 |

intercepts: off +8.18, def +39.38

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.002** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.69 / p90 6.53 / max 14.00

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -2.05 | -7.7 | +2.9 |
| Mountain West | 10 | -1.94 | -10.7 | +4.6 |
| Mid-American | 13 | -1.51 | -14.0 | +7.0 |
| Pac-12 | 8 | -1.41 | -6.4 | +4.8 |
| Sun Belt | 14 | -1.08 | -6.8 | +5.5 |
| American Athletic | 14 | -0.66 | -9.9 | +11.2 |
| ACC | 17 | +0.75 | -4.1 | +6.3 |
| Big 12 | 16 | +0.87 | -4.7 | +6.6 |
| Big Ten | 18 | +1.31 | -4.9 | +7.2 |
| SEC | 16 | +1.68 | -5.9 | +7.1 |
| FBS Independents | 2 | +8.90 | +5.8 | +12.0 |

## Movers vs the pilot-era board (mean |Δ| 2.52, max 10.67; rank Spearman vs pilot-era 0.987)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | Florida International | -5.39 |
| Notre Dame | +6.35 | | New Mexico State | -5.18 |
| Ole Miss | +5.97 | | Sam Houston | -5.00 |
| Georgia | +5.75 | | Middle Tennessee | -4.96 |
| LSU | +5.48 | | Missouri State | -4.73 |
| Oregon | +5.27 | | Liberty | -4.68 |
| Texas Tech | +5.22 | | Georgia State | -4.29 |
| Texas | +5.10 | | UL Monroe | -3.95 |
| Oklahoma | +4.93 | | Western Kentucky | -3.85 |
| Texas A&M | +4.82 | | Troy | -3.74 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.28), UConn -> all-G5 mean (+0.62).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -12.73 | -4.46 |
| Mid-American | -6.99 | -2.45 |
| Pac-12 | -5.35 | -1.87 |
| SEC | -5.06 | -1.77 |
| Big 12 | -0.51 | -0.18 |
| ACC | -0.03 | -0.01 |
| American Athletic | +0.57 | +0.20 |
| Big Ten | +3.76 | +1.32 |
| FBS Independents | +8.09 | +2.83 |
| Sun Belt | +10.20 | +3.57 |
| Conference USA | +14.15 | +4.95 |
| (all-P4 pool / ND ref) | -0.28 | -0.10 |
| (all-G5 pool / UConn ref) | +0.62 | +0.22 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
