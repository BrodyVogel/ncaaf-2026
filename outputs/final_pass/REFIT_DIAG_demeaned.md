# Final-pass refit diagnostic — 2026-07-18T23:58:29+00:00 @ 7167d34

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
- resid ~ a + b*(anchor margin) at n=138: slope **-0.154** (R² 0.20); proxy-regime constant was -0.541 (diag predicted collapse; n=61 gave -0.163).

## Residual census (mean +0.000 — ~0 by construction)
- capped at ±6.0: **0** teams: (none)
- |resid| p50 3.15 / p90 7.13 / max 13.33

## Mean residual by conference (grades-vs-anchor, refit regime)
| conference | n | mean resid | min | max |
|---|--:|---:|---:|---:|
| SEC | 16 | -0.00 | -7.5 | +7.2 |
| Mid-American | 13 | -0.00 | -13.3 | +10.3 |
| Big 12 | 16 | +0.00 | -6.3 | +4.4 |
| American Athletic | 14 | +0.00 | -9.2 | +9.7 |
| Big Ten | 18 | +0.00 | -7.6 | +5.7 |
| FBS Independents | 2 | +0.00 | -8.2 | +8.2 |
| Sun Belt | 14 | +0.00 | -9.4 | +8.4 |
| Pac-12 | 8 | +0.00 | -6.8 | +5.9 |
| ACC | 17 | +0.00 | -7.1 | +6.0 |
| Mountain West | 10 | +0.00 | -7.9 | +5.9 |
| Conference USA | 10 | +0.00 | -6.0 | +6.6 |

## Movers vs the pilot-era board (mean |Δ| 2.11, max 4.77; rank Spearman vs pilot-era 0.990)
| biggest UP | Δ | | biggest DOWN | Δ |
|---|---:|---|---|---:|
| Ole Miss | +4.77 | | New Mexico State | -4.12 |
| Georgia | +4.49 | | Liberty | -4.06 |
| LSU | +4.43 | | Kennesaw State | -4.01 |
| Texas | +4.42 | | Missouri State | -4.01 |
| Oklahoma | +4.35 | | Middle Tennessee | -4.00 |
| Texas A&M | +4.15 | | Florida International | -3.82 |
| Auburn | +4.08 | | Jacksonville State | -3.79 |
| South Carolina | +4.03 | | Delaware | -3.67 |
| Missouri | +3.95 | | Sam Houston | -3.58 |
| Florida | +3.90 | | Western Kentucky | -3.51 |

## What-if: --demean-conf-resid (owner decision; NOT applied to the official board)
Under the frozen formula the k*clip(resid) term moves every team in a conference by
~k x (conference mean resid) on top of its within-conference shape. Demeaning drops that
shared component. Per-conference shift the variant would apply vs the official board:
| conference | mean resid | ~shift dropped (k x mean, pre-cap) |
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

## Provenance
- anchor run: outputs/anchor_runs/anchor_run_2026-07-14_class0.json (frozen); class_per_side 0.0; teams 138/138 joined
- constants: K=0.35 CAP=6.0 SIGMA=6.0; recenter shift +0.574; mode DEMEANED-VARIANT
- pilot-era finals (at-grading-time, proxy-fit OOS) remain in outputs/grade_board.csv as the audit trail.
