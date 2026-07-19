# Win-total engine — model & calibration (2026)

This is the written companion to the interactive artifact (`outputs/win_totals_2026.html`,
Methodology tab). It documents the variance model — the step the owner flagged as the most
important — and the calibration work that justifies the shipped defaults.

## The win model (probit)

Every rating is a neutral-field point margin vs an average FBS team (0). For a game between
our team S and opponent O:

```
expected_margin = mu_S - mu_O + HFA * site      site ∈ {+1 home, -1 away, 0 neutral}
P(S wins)        = Φ( expected_margin / sigma_eff )
```

Φ is the normal CDF. Everything hinges on `sigma_eff`, which combines three uncertainty
sources that behave differently across a season:

1. **Game randomness — `sigma_game = 13.5`.** Even with perfectly known ratings, a single
   result scatters (turnovers, spot, weather). Independent game to game. Pinned to how CFB
   margins convert to win probability: a 7-pt favorite ≈ 70%, 3-pt ≈ 59%, 14-pt ≈ 85% — i.e.
   the SD of a result against its spread, ≈13.5.

2. **Opponent-rating uncertainty (their band).** We're unsure of each opponent's true
   strength. Different opponents → independent errors → adds to each game's spread:
   `sigma_eff = sqrt(sigma_game² + (band_opp · BAND_TO_SD)²)`, with `BAND_TO_SD = 1.0`.

3. **Our own rating uncertainty (the shared shock) — the important one.** If our number on
   *our* team is 2 pts high, it's high in *every* game; this error is **correlated across all
   games** and does not average out. Modeled as a single latent offset drawn once per season,
   `δ ~ Normal(0, τ²)`, `τ = band_self · BAND_TO_SD`, applied to mu_S in every game and
   integrated out. **This shared shock fattens the win-total tails** — great and disastrous
   seasons both get more likely than an "every-game-independent" model allows. Omitting it
   makes the model far too confident a team lands on its median. It is the single most
   consequential modeling choice.

## Win distribution (exact, deterministic)

Hold δ fixed → games independent → wins ~ **Poisson-Binomial**, computed **exactly** by DP
(O(G²)), not simulated. Average over δ with **21-point Gauss-Hermite quadrature**:

```
P(wins = k) = Σ_i w_i · PoissonBinomial( k | p_g(δ_i) ),   δ_i = √2·τ·x_i,  weight w_i/√π
```

Deterministic (no Monte-Carlo noise). The same fixed GH nodes ship to the browser; the JS
engine (Cephes ndtr port) reproduces the Python reference to **~1×10⁻¹⁴** (verified under
node and in-browser).

## Fair odds & edge

The distribution yields a fair no-vig price for every line (over k−0.5 = P(wins ≥ k)).
Against the market we use the owner's **30-cent line**: an over at −175 implies an under at
+145. De-vig both sides → market probability; edge = our prob − market prob; EV = expected
profit per $1 at the posted price. Best bet = the highest-EV side across all posted books.

## Calibration (why these defaults)

Across all 129 teams with posted regular-season totals:

- **Mean edge ≈ 0.0%** — our probabilities are unbiased against the market on average. The
  disagreements are concentrated in specific teams (SD ≈ 8.9% of edge), which is exactly what
  a mispricing finder should produce, not a systematic tilt.
- **Rating-scale compression — diagnosed and fixed (2026-07-19).** The original ratings
  carried a systematic tilt (back low-total dogs, fade high-total favorites; edge~line R² =
  0.32 overall, 0.43 in the P4) traced to the grade→points OLS fit shrinking the grade signal.
  It was de-compressed at the source (un-shrink the OLS fit + orthogonalize the grade residual
  to team strength), cutting edge~line R² to 0.14/0.16 and restoring the fair spread (SD ≈ 13),
  ordering unchanged. Full write-up in `docs/COMPRESSION_FIX.md`. Note `sigma_game = 13.5` was
  kept (the theoretically correct single-game value); the fix was in the ratings' scale, not
  the variance model.

- **Biggest edge is real, not a bug.** North Dakota State (−0.52 edge) is a **reclassifying
  program** — a 9-time FCS champion making its FBS debut in the reshaped Mountain West. The
  market prices ~9 wins; our grade, built on thin FBS-level data, has ~7.5. Flagged in the UI
  as elevated-uncertainty rather than treated as signal.

**Shipped defaults (all UI-tunable): HFA = 2.3, sigma_game = 13.5, BAND_TO_SD = 1.0.** No
ratings stretch. The artifact exposes all three constants plus per-team rating overrides so
the owner can explore the compression question and any rating hypothesis with a live pro
forma.

## Regenerating

The artifact is fully regenerable — not a one-off:

```
python3 pipeline/build_win_totals_artifact.py   # -> outputs/win_totals_2026.html
```

Pipeline: `win_engine.py` (reference engine) → `win_totals_data.py` (joins ratings/schedules/
market/FCS) → `win_totals_compute.py` (builds the lean embedded payload) →
`build_win_totals_artifact.py` (emits self-contained HTML with `win_engine.js` + UI). Update
any input (ratings in `outputs/final_pass/ASSEMBLY.csv`, market in
`data/win_totals/win_totals_2026.csv`, FCS in `data/fcs_ratings_2026.csv`) and re-run.
Parity/validation: `node` on `win_engine.js` vs the Python reference; Playwright browser
checks (138 board rows, engine parity, override pro forma).
```
