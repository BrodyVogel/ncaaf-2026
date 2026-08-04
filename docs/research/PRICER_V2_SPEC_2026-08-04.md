# PRICER V2 SPEC — registered before computation (2026-08-04)

Owner directive (2026-08-04): review DD 1's pricing critique, adjust, reprice
every posted line. This document fixes the v2 rules BEFORE the pricing script
is run. Committed first; the run follows in a separate commit.

## Honesty disclosure — this is not a blind registration

DD 1 (`deep_dives/DD_stockton_2026-08-04.md` §1B) already explored this panel
post-hoc: quartile under-rate tables, a ±30 pace-matched estimator, and a
grid-logistic have been seen. Full blindness is unrecoverable. Mitigations:
(a) every v2 component is chosen for its MECHANISM, not fitted shape — the
skeleton is pricer v0's, which predates DD 1 and was registered in the S20
prereg; (b) the calibration holdout (fit 2021–24 → price 2025) cannot have
been contaminated by DD 1, which never fit on split years; (c) the shrink rule
below is a formula, decided now, applied to whatever the holdout says; (d) no
candidate price is computed until this file is committed.

## Why v2 exists (the defect, restated once)

v1 prices off r = line/(12·pace₀) alone. The line scales with pace₀; mean
reversion pulls toward a fixed population mean (~244 yd/g same-school). So at
IDENTICAL r, a high-pace₀ QB faces a line far above his reverted expectation
(near-automatic under) while a low-pace₀ QB faces a line his reversion pulls
him THROUGH (weak under, sometimes over). v0's simulation handled this
automatically via its fitted pace model; v1's ratio-ladder "upgrade" discarded
it. v2 restores v0's structure with v1's calibration discipline. Evidence:
DD 1 §1B (same-school Q1 54.5% vs Q4 91.3% under at fixed r; OLS t=5.36).

## Model (all parameters fit by the script and recorded in the output JSON)

1. **Pace persistence.** OLS `pace₁ = a + b·pace₀ + c·transfer` fit on panel
   rows with `g10_1 ≥ 6` (pace₁ on <6 games is sampling noise, and DD 1's fit
   wrongly included 1-game seasons — e.g. a 421-yd single-game pace₁). A
   transfer×pace₀ slope interaction is adopted ONLY if its F-test p < .05;
   otherwise intercept shift only. Prediction uses OBSERVED pace₀ — no
   attenuation correction, deliberately: candidates are priced from observed
   pace₀ carrying the same measurement noise as the fit sample, so the
   attenuated slope is the correct predictive slope.
2. **Season spread.** σ_season = residual sd of that fit. Disclosed limitation:
   this partially double-counts per-game noise for small-G rows even at the
   ≥6 cut; the calibration shrink absorbs level bias, as in v0/v1.
3. **Per-game noise.** sd 75, v0's constant, unchanged.
4. **Availability.** G drawn from the EMPIRICAL distribution of `g10_1`
   (0–13), estimated separately for same-school vs transfer rows. No cap at
   12: the panel outcome basis (CFBD seasonType=regular) includes CCGs, and
   `pace₁ ≡ yds₁/g10_1`, so simulated total `G·μ + ε·√G·75` reproduces the
   measured outcome basis exactly.
5. **Simulation.** Per candidate: 200,000 draws, fixed seed 20260804.
   total = G·μ + N(0,75)·√G, μ ~ N(â + b̂·pace₀ + ĉ·T, σ_season).
   p_raw = P(total < line).
6. **Calibration.** Fit steps 1–4 on t=2021–2024 only; price every 2025 panel
   row's synthetic line L = 12·pace₀; shrink k* = argmin over
   k ∈ {0.30, 0.35, …, 1.20} of holdout Brier for p = 0.5 + k·(p_raw − 0.5);
   final k = clamp(k*, 0.50, 0.85) — the cap is conservative against n≈35
   holdout noise, the floor prevents overreacting to it. Report raw k*, Brier
   vs v1's holdout Brier (0.229), and calibration by predicted-probability
   bucket. Then REFIT steps 1–4 on all years 2021–2025 and price the 2026
   board with that k.
7. **Board.** All 17 posted names, inputs (line, pace₀, transfer flag) from
   `pricer_v1_2026-08-04.json`; pace₀ independently recomputed from
   `player_games_flat.csv` and any divergence > 0.01 yd/g flagged. Output:
   p_raw, p_v2, under-edge vs .5305 (negative ⇒ over side, reported vs the
   same breakeven), rank, and a strict-12 sensitivity (G capped at 12 — the
   FD-excludes-CCG branch, which remains unverified text). Note per team
   whether CCG likelihood is materially above panel base rate (asymmetry
   flagged in DD 1 review: for CCG-likely teams, the two settlement branches
   are NOT symmetric around the base price).

## What v2 does NOT do

No DD-layer judgments (job security, benching history, script, camp health) —
those stay in per-QB dives ON TOP of the mechanical price, as in DD 1 §7.
No grade/ratings changes. No staking: the board re-ranks the dive queue and
returns to the owner. v1 stays on disk untouched for the audit trail.

## Registered expectations (falsifiable, written before the run)

- k* lands above v1's 0.70 (the better-specified model should be less
  overconfident); if k* < 0.60 the spec is suspect — flag, don't ship.
- Holdout Brier ≤ 0.229 (beat v1's spec on its own test); if not, v2 does not
  replace v1 and the whole question returns to the owner.
- Ordering: high-pace₀ names (Mestemaker, Hoover) hold or improve; low-pace₀
  names (Stockton, Bachmeier, Iamaleava) fall; Iamaleava lands near/below
  breakeven. If the run contradicts these, that is INFORMATION, not an error
  to fix silently — report it.
