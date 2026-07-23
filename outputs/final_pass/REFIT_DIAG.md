# Final-pass refit diagnostic — 2026-07-23T23:00:36+00:00 @ 0924dad

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.139 |
| off | RB | +0.092 | +0.159 |
| off | WRTE | +0.037 | +0.024 |
| off | OL | +0.082 | +0.071 |
| def | DL | -0.083 | -0.162 |
| def | LB | -0.059 | -0.028 |
| def | DB | -0.096 | -0.119 |
| off | R² | 0.54 | 0.67 |
| def | R² | 0.61 | 0.48 |

intercepts: off +7.93, def +39.44

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.002** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.55 / p90 6.61 / max 14.07

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -2.00 | -7.8 | +2.7 |
| Mountain West | 10 | -1.87 | -10.7 | +5.0 |
| Pac-12 | 8 | -1.45 | -6.7 | +4.8 |
| Mid-American | 13 | -1.41 | -14.1 | +6.8 |
| Sun Belt | 14 | -1.00 | -7.7 | +5.5 |
| American Athletic | 14 | -0.60 | -10.3 | +11.1 |
| ACC | 17 | +0.73 | -4.1 | +5.5 |
| Big 12 | 16 | +0.83 | -4.9 | +7.0 |
| Big Ten | 18 | +1.25 | -5.2 | +7.4 |
| SEC | 16 | +1.60 | -6.3 | +6.6 |
| FBS Independents | 2 | +8.65 | +5.6 | +11.7 |

## Movers vs the pilot-era board (mean |Δ| 2.52, max 10.67; rank Spearman vs pilot-era 0.986)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | New Mexico State | -5.19 |
| Notre Dame | +6.26 | | Middle Tennessee | -5.17 |
| Ole Miss | +5.95 | | Florida International | -4.95 |
| Oregon | +5.94 | | Sam Houston | -4.93 |
| Georgia | +5.67 | | Missouri State | -4.69 |
| Texas | +5.64 | | Liberty | -4.68 |
| LSU | +5.43 | | Georgia State | -4.24 |
| Texas Tech | +5.12 | | UL Monroe | -3.92 |
| Ohio State | +4.93 | | Southern Miss | -3.66 |
| Texas A&M | +4.87 | | Western Kentucky | -3.65 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.37), UConn -> all-G5 mean (+0.68).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -12.83 | -4.49 |
| Mid-American | -6.89 | -2.41 |
| SEC | -5.09 | -1.78 |
| Pac-12 | -3.79 | -1.33 |
| Big 12 | -0.55 | -0.19 |
| ACC | -0.30 | -0.11 |
| American Athletic | +0.40 | +0.14 |
| Big Ten | +3.78 | +1.32 |
| FBS Independents | +7.88 | +2.76 |
| Sun Belt | +10.05 | +3.52 |
| Conference USA | +14.01 | +4.90 |
| (all-P4 pool / ND ref) | -0.37 | -0.13 |
| (all-G5 pool / UConn ref) | +0.68 | +0.24 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
