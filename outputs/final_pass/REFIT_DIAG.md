# Final-pass refit diagnostic — 2026-08-02T18:18:54+00:00 @ f3f0908

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.147 |
| off | RB | +0.092 | +0.143 |
| off | WRTE | +0.037 | +0.046 |
| off | OL | +0.082 | +0.071 |
| def | DL | -0.083 | -0.157 |
| def | LB | -0.059 | -0.018 |
| def | DB | -0.096 | -0.146 |
| off | R² | 0.54 | 0.69 |
| def | R² | 0.61 | 0.51 |

intercepts: off +7.24, def +40.04

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **+0.004** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.171; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 1.84 / p90 5.78 / max 10.89

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Pac-12 | 8 | -1.37 | -6.4 | +5.2 |
| Mountain West | 10 | -1.02 | -9.0 | +4.7 |
| Conference USA | 10 | -0.54 | -5.1 | +4.2 |
| Mid-American | 13 | -0.13 | -9.6 | +5.8 |
| Sun Belt | 14 | -0.13 | -4.2 | +3.4 |
| American Athletic | 14 | -0.13 | -7.9 | +10.9 |
| ACC | 17 | -0.12 | -4.5 | +2.1 |
| Big 12 | 16 | -0.12 | -5.9 | +7.4 |
| Big Ten | 18 | -0.12 | -6.3 | +5.7 |
| SEC | 16 | -0.12 | -5.8 | +3.7 |
| FBS Independents | 2 | +8.30 | +7.2 | +9.4 |

## Movers vs the pilot-era board (mean |Δ| 2.33, max 10.67; rank Spearman vs pilot-era 0.985)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | Sam Houston | -5.55 |
| Oregon | +6.75 | | Middle Tennessee | -5.52 |
| Notre Dame | +6.47 | | Georgia State | -5.39 |
| Ohio State | +6.10 | | New Mexico State | -5.07 |
| Texas Tech | +5.75 | | UL Monroe | -4.89 |
| Miami | +5.72 | | Missouri State | -4.69 |
| Georgia | +5.60 | | Florida International | -4.50 |
| Texas | +5.33 | | Southern Miss | -3.97 |
| Ole Miss | +5.14 | | Liberty | -3.97 |
| LSU | +4.77 | | Charlotte | -3.92 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.01), UConn -> all-G5 mean (+0.01).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Conference USA | -0.14 | -0.05 |
| Mid-American | -0.14 | -0.05 |
| Sun Belt | -0.13 | -0.05 |
| Mountain West | -0.13 | -0.05 |
| American Athletic | -0.13 | -0.05 |
| Pac-12 | -0.13 | -0.05 |
| ACC | -0.13 | -0.04 |
| Big 12 | -0.13 | -0.04 |
| Big Ten | -0.12 | -0.04 |
| SEC | -0.12 | -0.04 |
| FBS Independents | +8.42 | +2.95 |
| (all-P4 pool / ND ref) | -0.01 | -0.00 |
| (all-G5 pool / UConn ref) | +0.01 | +0.01 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.223; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
