# Final-pass refit diagnostic — 2026-08-02T15:34:41+00:00 @ 1b70c61

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.141 |
| off | RB | +0.092 | +0.141 |
| off | WRTE | +0.037 | +0.052 |
| off | OL | +0.082 | +0.075 |
| def | DL | -0.083 | -0.161 |
| def | LB | -0.059 | -0.037 |
| def | DB | -0.096 | -0.123 |
| off | R² | 0.54 | 0.69 |
| def | R² | 0.61 | 0.50 |

intercepts: off +7.20, def +39.98

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **+0.004** (R² 0.00); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean -0.168; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 1.95 / p90 5.67 / max 10.22

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Pac-12 | 8 | -1.45 | -6.5 | +5.0 |
| Mountain West | 10 | -0.95 | -8.3 | +4.7 |
| Conference USA | 10 | -0.52 | -5.0 | +4.2 |
| Mid-American | 13 | -0.13 | -10.2 | +5.8 |
| Sun Belt | 14 | -0.13 | -4.5 | +3.4 |
| American Athletic | 14 | -0.13 | -7.6 | +10.1 |
| ACC | 17 | -0.13 | -5.1 | +2.6 |
| Big 12 | 16 | -0.13 | -5.6 | +6.8 |
| Big Ten | 18 | -0.12 | -6.8 | +5.9 |
| SEC | 16 | -0.12 | -6.4 | +3.8 |
| FBS Independents | 2 | +8.45 | +7.4 | +9.5 |

## Movers vs the pilot-era board (mean |Δ| 2.32, max 10.67; rank Spearman vs pilot-era 0.985)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| North Dakota State | +10.67 | | Sam Houston | -5.58 |
| Oregon | +6.81 | | Middle Tennessee | -5.47 |
| Notre Dame | +6.54 | | New Mexico State | -5.16 |
| Ohio State | +6.15 | | Georgia State | -5.04 |
| Texas Tech | +5.83 | | UL Monroe | -4.90 |
| Miami | +5.66 | | Missouri State | -4.62 |
| Georgia | +5.59 | | Florida International | -4.43 |
| Texas | +5.43 | | Southern Miss | -4.08 |
| Ole Miss | +5.19 | | Charlotte | -4.01 |
| Indiana | +4.88 | | Liberty | -3.93 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-0.01), UConn -> all-G5 mean (+0.01).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Conference USA | -0.14 | -0.05 |
| Mid-American | -0.14 | -0.05 |
| Sun Belt | -0.14 | -0.05 |
| Mountain West | -0.14 | -0.05 |
| American Athletic | -0.13 | -0.05 |
| Pac-12 | -0.13 | -0.05 |
| ACC | -0.13 | -0.04 |
| Big 12 | -0.13 | -0.04 |
| Big Ten | -0.13 | -0.04 |
| SEC | -0.12 | -0.04 |
| FBS Independents | +8.57 | +3.00 |
| (all-P4 pool / ND ref) | -0.01 | -0.00 |
| (all-G5 pool / UConn ref) | +0.01 | +0.00 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.223; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
