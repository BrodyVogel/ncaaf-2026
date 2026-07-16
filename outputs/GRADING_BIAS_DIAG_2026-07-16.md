# Grading-bias diagnostic — is "cool on every MAC roster" a grader problem?

Prompted by owner challenge (2026-07-16): "if you're below consensus on every
single roster, the problem might be you." Two tests on the current 61 real-graded
teams + 2021-2025 history. Scripts: pipeline/diag_refit_61.py, diag_churn_backtest.py.

## Verdict
The owner is substantially right. The uniform coolness was **mostly a mechanism
artifact, not roster signal**, and the piece that survives a fair fit is NOT
supported by history. Relative ordering of teams is sound; absolute level was
inflated by two calibration bugs.

## Finding 0 — my "cooler on every roster" claim was overstated (lens artifact)
On the RAW grades-vs-anchor comparison (resid, no decomposition), the MAC is
near-balanced: proxy-fit mean +0.74, and 9 of 13 teams grade WARMER than anchor
(KSU +5.5, UMass +13.1, Akron +4.2...). The uniform negativity appears ONLY in
"shape," which subtracts an expected mean-reversion fade. The wrap sentence
conflated shape with raw resid. Withdrawn.

## Finding 1 (mechanism bug) — the level slope is overfit
`LEVEL_SLOPE = -0.541` was fit on n=20 pilot teams; the code comment claims level
explains "~81% of resid variance." Refit on all 61: slope **-0.163**, and level
explains only **19%** of resid variance. The steep slope manufactures uniform
negative shape for every bad team — and since the MAC is entirely bad teams, it
manufactures a conference-wide negative shape. Recomputing MAC mean shape with the
honest slope: **-10.0 -> -4.3**.

## Finding 2 (mechanism bug) — conversion is trained on the inflated-bottom proxy
The grade->points conversion is fit on shadow-proxy grades (documented inflated at
the bottom, artifacts #43-45), then real grades are pushed through OOS. A fair
real-grade refit fits BETTER (R2 off 0.82 / def 0.73 vs proxy 0.54 / 0.63) and
removes the monotonic "G5-floored" gradient:

| conf | proxy-fit "shape" (wrap) | real-refit mean resid |
|------|--------------------------|-----------------------|
| American Athletic | -2.4 | **+2.9** |
| Big Ten | +0.7 | +0.4 |
| Big 12 | -1.9 | -1.6 |
| Mid-American | -7.5 | **-1.8** |

The AAC (same G5 conventions, same grader) flips positive. No uniform G5 penalty.

## Finding 3 (robust signal) — relative ordering survives
Within-MAC worst->best ordering under proxy-fit vs real-refit: Spearman **0.94**.
Toledo/Ohio/WMU/Miami/SacSt/Buffalo stay the cool ones. My RELATIVE roster reads
are stable; only the absolute level was inflated.

## Finding 4 (open concern) — a defense-tilted MAC residual survives a fair fit
Conf-dummy fit (holding my unit grades fixed): MAC anchors expect **+4.58** more
margin than my grades imply, almost entirely on DEFENSE (off dummy +0.34, def
dummy **-4.24**). Confounded with all-bottom composition, but this is the one piece
that could be genuine bias: I may grade MAC defenses systematically low.

## Finding 5 (decisive) — the churn defense does NOT hold for G5
My wrap rationale for the negative shape was "roster churn the anchors haven't
priced." Backtest 2021-2025 (n=502 team-seasons), returning production (PPA) vs
(final SP+ - preseason SP+):

- overall corr **+0.099** (weak); slope +3.25 pts per unit RP
- **G5 only: corr +0.007, slope +0.19 — essentially ZERO**
- low-RP (high-churn) tail: all bottom-quartile mean -1.65 (mild, P4-driven);
  **G5 bottom-quartile mean +1.27 (finished ABOVE preseason), only 42% below**

Preseason systems already price G5 churn. Marking high-churn G5 rosters DOWN
further is not supported by history — those teams hit their number about as often
as anyone. Caveat: the backtest tests returning-PRODUCTION, not my grades (which
account for incoming transfers); it refutes the specific rationale I wrote and
shifts the burden onto me, but doesn't independently prove my grades wrong.

## Implications
- These are conversion/decomposition calibration objects, NOT frozen grades. No
  frozen artifact needs regrading on this basis.
- BUT: the Toledo/WMU "under" market leans rested on roster-cool-vs-anchor shape.
  With the churn backtest null for G5 and the level slope overfit, those leans are
  **withdrawn**, not merely downgraded. (Toledo's anchor-side dispersion story is
  independent and can stand.)
- Recommended fixes (propose->approve): (a) refit level slope + conversion at a
  checkpoint now, not at 138; (b) isolate the defense dummy — my grades vs the
  anchors; (c) treat low-confidence MAC defensive grades as candidates to drift
  toward anchor, and stop letting them drive market leans until validated.
