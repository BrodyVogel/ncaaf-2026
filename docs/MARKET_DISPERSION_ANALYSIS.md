# Is the monotonic win-total gradient our error, or the market's? (2026-07-20)

After the grade de-compression fix, the win-total edge stayed monotonic in the line (back
low-total dogs, fade high-total favorites; slope ~−1.8%/win). The owner read this as residual
compression in our ratings. A stretch sweep showed the gradient flattens only if our ratings
are stretched to **effective SD ~15.8** — so *something* is at SD ~16. The question: is it our
ratings that are too narrow (compression, stretch them) or the market's totals that are too
wide (over-dispersion, leave ours alone)?

## Verdict: the market over-disperses; our scale is correct. Do NOT stretch.

Three independent lines of evidence, all pointing the same way.

### 1. Every real rating system sits at SD ~13, not ~16
- SP+ (elite public system), 2021–2025, preseason **and** final: SD 12.3–13.7 (mean ~13).
- KFord Final 2025: SD 13.0.
- Our fixed ratings: SD 13.2.
- Market win totals price an effective spread of **~15–16** — wider than any rating system.

### 2. Game-level calibration (4,332 games, 2021–2025): more spread predicts *worse*
Using SP+ preseason (our scale) + the win model on actual games:

| model P(win) | actual |
|---|---|
| 55.0% | 56.6% |
| 65.2% | 62.0% |
| 74.9% | 70.5% |
| 85.3% | 80.0% |
| 96.6% | 92.8% |

Favorites win **less** than we predict (all favorites: predicted 80.4%, actual 77.1%) — the
signature of a mildly **over-confident** model, the opposite of compression. If we were
compressed, favorites would beat our predictions. Re-fitting the rating-spread multiplier to
actual games, log-likelihood **monotonically worsens** with more spread: x0.8 −2312 › x1.0
(ours) −2384 › x1.2 (market) −2508 › x1.3 −2588. The market's wider spread is decisively a
worse description of reality. (The sub-1.0 optimum is the expected shrinkage of a noisy
*preseason* forecast, not a target for final ratings — the point is the direction: stretching
hurts.)

### 3. The one year with market data confirms it at the win-total level
2025 (136 teams), actual minus market total by tier: low totals (≤5) **+0.34 wins**, mid +0.06,
high (≥8) **−0.21 wins**. Dogs beat their numbers, favorites missed — the market over-priced
favorites and under-priced dogs. SP+-scale expected wins also beat the market outright:
MAE 1.91 vs 1.95, closer 64% of the time when they disagreed.

## Implication
The monotonic residual is **not** leftover compression — it is the edge. Win-total markets are
known to over-disperse (recreational money on favorites' overs / dogs' unders; books shade to
match). Our correctly-scaled ratings lean against it, and in-sample that lean has been right.
Flattening the gradient by stretching to SD ~16 would destroy the edge *and* make the ratings
worse at predicting games. The earlier fix (SD 12.5 → 13.2, correcting the OLS grade shrinkage
to match SP+) was the right and sufficient scale correction; no further stretch.

## Limits / follow-ups
- 5 years of *game* outcomes but only **1** year of *market* totals. Confirm with 2021–2024
  historical win-total lines and real backtested betting P&L before sizing bets.
- The mild game-level over-confidence hints at a touch *less* spread or slightly higher
  σ_game — again, opposite of stretching.

## Follow-up (2026-07-20): ratings locked + a third "market-matched" set

**Locked.** The de-compressed ratings (SD 13.2, floor −28.2) are frozen as the official set:
`outputs/final_pass/ASSEMBLY_LOCKED_2026-07-20.csv` (+ FINAL_BOARD_LOCKED_...). `final_pass.py`
still regenerates them identically; no further scale changes.

**Third set — MARKET-MATCHED.** Added alongside ours (roster) and consensus (anchor). It is our
ratings linearly stretched around the field mean by **s\* = 1.177** (SD 13.2 → 15.5) — the factor
whose win-total edge-vs-line slope is exactly zero, i.e. our ratings wearing the market's own
dispersion. Since the market over-disperses, most of our aggregate edge is the (market-wide)
fade-favorites/back-dogs tilt; the market-matched set neutralizes that tilt by construction, so an
edge that still shows up on it is **team-specific** — a disagreement about that team beyond the
spread play. In the artifact: three edge columns on the Board, a conviction score = the edge on the
*weaker* of ours and market-matched (default sort), and a ✓✓ flag when both clear +4%. ~60 of 138
clear it — the market really is that inefficient — so the score/sort matters more than the binary.
Owner's read: a total standing out on both lenses is the higher-confidence bet.

## AUDIT CORRECTION (2026-07-20, Fable)
The Pac-12 examples in this doc ("Boise/SDSU/Wazzu unders are real edges") were contaminated by a missing-game data bug: all 8 Pac-12 schedules lacked the Week-13 flex game, deflating E[wins] ~0.3-0.7 vs 12-game market totals. Post-fix, those teams lean modest OVER at posted lines. The dispersion conclusion itself SURVIVES (field-wide gradient nearly unchanged ex-Pac-12; game-level calibration confirms and strengthens it — see docs/AUDIT_2026-07-20_fable.md §3, which also quantifies the sub-1.0 shrink this doc footnoted: the calibrated optimum is ~0.75x, i.e. our own preseason probabilities are overconfident on extremes too).

## Addendum 2026-07-27 — disagreement-SIZE buckets (owner question)
Same 2025 panel (128 joined teams), consensus-implied wins vs market median line, bucketed
by |disagreement|: <0.5: side-win 49% (n=63) · 0.5–1.0: 49% (n=49) · **1.0–1.75: 80%
(n=15), MAE 1.67 vs 2.17**. The edge concentrated in the LARGE disagreements; the market
was not "catching something" where it strayed furthest from consensus — the opposite.
Contrast the S5 spread result (big rating-vs-CLOSER disagreements: 45–49%): against a
sharp number, a big disagreement means you're missing something; against a soft June
total, it means the market never did the work. Caveats: one season; n=15 in the money
bucket (SE ~10%); crude unshrunk expected-wins proxy.
