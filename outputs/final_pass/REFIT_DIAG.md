# Final-pass refit diagnostic — 2026-07-23T21:25:38+00:00 @ 36fcfed

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.132 |
| off | RB | +0.092 | +0.160 |
| off | WRTE | +0.037 | +0.021 |
| off | OL | +0.082 | +0.076 |
| def | DL | -0.083 | -0.144 |
| def | LB | -0.059 | -0.032 |
| def | DB | -0.096 | -0.132 |
| off | R² | 0.54 | 0.66 |
| def | R² | 0.61 | 0.47 |

intercepts: off +8.16, def +39.37

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.002** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.000; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 2.71 / p90 6.53 / max 13.98

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -2.11 | -7.7 | +2.9 |
| Mountain West | 10 | -1.94 | -10.7 | +4.6 |
| Mid-American | 13 | -1.51 | -14.0 | +6.9 |
| Pac-12 | 8 | -1.37 | -6.3 | +4.8 |
| Sun Belt | 14 | -1.08 | -6.7 | +5.5 |
| American Athletic | 14 | -0.66 | -10.0 | +11.4 |
| ACC | 17 | +0.76 | -4.3 | +6.5 |
| Big 12 | 16 | +0.88 | -4.8 | +6.6 |
| Big Ten | 18 | +1.32 | -4.8 | +7.3 |
| SEC | 16 | +1.69 | -5.8 | +7.1 |
| FBS Independents | 2 | +8.85 | +5.7 | +12.0 |

## Movers vs the pilot-era board (mean |Δ| 2.53, max 10.67; rank Spearman vs pilot-era 0.986)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | New Mexico State | -5.51 |
| Notre Dame | +6.32 | | Florida International | -5.38 |
| Ole Miss | +5.99 | | Sam Houston | -4.96 |
| Georgia | +5.76 | | Middle Tennessee | -4.90 |
| LSU | +5.48 | | Liberty | -4.65 |
| Texas Tech | +5.22 | | Missouri State | -4.59 |
| Oregon | +5.16 | | Georgia State | -4.24 |
| Texas | +5.09 | | UL Monroe | -3.93 |
| Oklahoma | +4.90 | | Arkansas State | -3.82 |
| Auburn | +4.86 | | Western Kentucky | -3.80 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.26), UConn -> all-G5 mean (+0.60).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -12.66 | -4.43 |
| Mid-American | -6.96 | -2.44 |
| Pac-12 | -5.42 | -1.90 |
| SEC | -5.04 | -1.76 |
| Big 12 | -0.49 | -0.17 |
| ACC | +0.04 | +0.01 |
| American Athletic | +0.60 | +0.21 |
| Big Ten | +3.76 | +1.31 |
| FBS Independents | +8.05 | +2.82 |
| Sun Belt | +10.10 | +3.53 |
| Conference USA | +14.08 | +4.93 |
| (all-P4 pool / ND ref) | -0.26 | -0.09 |
| (all-G5 pool / UConn ref) | +0.60 | +0.21 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
