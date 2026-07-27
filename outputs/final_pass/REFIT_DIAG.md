# Final-pass refit diagnostic — 2026-07-27T16:50:03+00:00 @ 83839f5

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.139 |
| off | RB | +0.092 | +0.162 |
| off | WRTE | +0.037 | +0.022 |
| off | OL | +0.082 | +0.069 |
| def | DL | -0.083 | -0.164 |
| def | LB | -0.059 | -0.025 |
| def | DB | -0.096 | -0.119 |
| off | R² | 0.54 | 0.67 |
| def | R² | 0.61 | 0.48 |

intercepts: off +7.88, def +39.46

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.002** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean +0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.61 / p90 6.58 / max 14.07

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -2.02 | -7.8 | +2.7 |
| Mountain West | 10 | -1.88 | -10.8 | +5.2 |
| Pac-12 | 8 | -1.42 | -6.6 | +4.8 |
| Mid-American | 13 | -1.41 | -14.1 | +6.7 |
| Sun Belt | 14 | -1.00 | -7.7 | +5.5 |
| American Athletic | 14 | -0.60 | -10.4 | +11.2 |
| ACC | 17 | +0.73 | -3.5 | +5.3 |
| Big 12 | 16 | +0.83 | -4.9 | +6.5 |
| Big Ten | 18 | +1.25 | -5.2 | +7.7 |
| SEC | 16 | +1.60 | -6.4 | +7.1 |
| FBS Independents | 2 | +8.58 | +5.5 | +11.7 |

## Movers vs the pilot-era board (mean |Δ| 2.52, max 10.67; rank Spearman vs pilot-era 0.986)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | New Mexico State | -5.21 |
| Notre Dame | +6.23 | | Middle Tennessee | -5.19 |
| Oregon | +5.99 | | Sam Houston | -4.93 |
| Ole Miss | +5.92 | | Florida International | -4.73 |
| Texas | +5.63 | | Missouri State | -4.71 |
| Georgia | +5.61 | | Liberty | -4.69 |
| LSU | +5.33 | | Georgia State | -4.25 |
| Texas Tech | +5.14 | | UL Monroe | -3.94 |
| Auburn | +4.95 | | Western Kentucky | -3.77 |
| Ohio State | +4.94 | | Delaware | -3.66 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.36), UConn -> all-G5 mean (+0.68).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -12.77 | -4.47 |
| Mid-American | -6.89 | -2.41 |
| SEC | -5.02 | -1.76 |
| Pac-12 | -3.84 | -1.34 |
| Big 12 | -0.58 | -0.20 |
| ACC | -0.24 | -0.08 |
| American Athletic | +0.39 | +0.14 |
| Big Ten | +3.69 | +1.29 |
| FBS Independents | +7.81 | +2.73 |
| Sun Belt | +10.04 | +3.51 |
| Conference USA | +14.01 | +4.90 |
| (all-P4 pool / ND ref) | -0.36 | -0.13 |
| (all-G5 pool / UConn ref) | +0.68 | +0.24 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
