# Final-pass refit diagnostic — 2026-07-19T00:59:00+00:00 @ e81ee07

## Conversion weights (proxy-fit regime -> full-138 real-grade refit)
| side | unit | proxy-fit | refit-138 |
|---|---|---:|---:|
| off | QB | +0.072 | +0.149 |
| off | RB | +0.092 | +0.147 |
| off | WRTE | +0.037 | +0.028 |
| off | OL | +0.082 | +0.064 |
| def | DL | -0.083 | -0.153 |
| def | LB | -0.059 | -0.022 |
| def | DB | -0.096 | -0.135 |
| off | R² | 0.54 | 0.67 |
| def | R² | 0.61 | 0.49 |

intercepts: off +8.09, def +39.50

## Level slope (diagnostic only; NEVER enters the final)
- resid ~ a + b*(anchor margin) at n=138: slope **-0.146** (R² 0.18); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census — post-mode residual (mean +0.062; in official mode each conference mean is ≈0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 3.06 / p90 7.00 / max 13.32

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| Conference USA | 10 | -0.00 | -6.0 | +6.6 |
| SEC | 16 | -0.00 | -7.5 | +7.2 |
| Mid-American | 13 | -0.00 | -13.3 | +10.2 |
| Big Ten | 18 | -0.00 | -7.6 | +5.7 |
| American Athletic | 14 | +0.00 | -9.3 | +9.7 |
| Pac-12 | 8 | +0.00 | -6.8 | +5.9 |
| ACC | 17 | +0.00 | -7.1 | +6.0 |
| Big 12 | 16 | +0.00 | -6.3 | +4.4 |
| Sun Belt | 14 | +0.00 | -9.4 | +8.4 |
| Mountain West | 10 | +0.00 | -7.9 | +5.9 |
| FBS Independents | 2 | +4.27 | -1.1 | +9.7 |

## Movers vs the pilot-era board (mean |Δ| 2.12, max 4.74; rank Spearman vs pilot-era 0.990)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| Ole Miss | +4.74 | | New Mexico State | -4.10 |
| Georgia | +4.46 | | Liberty | -4.09 |
| LSU | +4.42 | | Kennesaw State | -4.04 |
| Texas | +4.40 | | Missouri State | -4.04 |
| Oklahoma | +4.33 | | Middle Tennessee | -4.04 |
| Texas A&M | +4.13 | | Florida International | -3.85 |
| Auburn | +4.05 | | Jacksonville State | -3.83 |
| South Carolina | +4.02 | | Delaware | -3.70 |
| Missouri | +3.91 | | Sam Houston | -3.59 |
| Notre Dame | +3.90 | | Western Kentucky | -3.52 |

## Conference-level component REMOVED (official mode) — owner decision 2026-07-19
The k*clip(resid) term otherwise moves every team in a conference by ~k x (conference
mean resid) on top of its within-conference shape. Demeaning drops that shared component.
Independents pseudo-pooled: ND -> all-P4 mean (-2.90), UConn -> all-G5 mean (+2.81).
| pool | mean resid (pre-demean) | ~shift dropped (k x mean, pre-cap) |
|---|---:|---:|
| Mountain West | -9.02 | -3.16 |
| SEC | -7.59 | -2.66 |
| Big 12 | -2.26 | -0.79 |
| Pac-12 | -2.07 | -0.72 |
| ACC | -1.84 | -0.65 |
| Mid-American | -1.25 | -0.44 |
| Big Ten | -0.22 | -0.08 |
| American Athletic | +2.43 | +0.85 |
| FBS Independents | +4.23 | +1.48 |
| Sun Belt | +10.07 | +3.52 |
| Conference USA | +13.24 | +4.63 |
| (all-P4 pool / ND ref) | -2.90 | -1.01 |
| (all-G5 pool / UConn ref) | +2.81 | +0.98 |

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.552; mode OFFICIAL (conference-demeaned; IND pseudo-pooled)
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
