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

---

## Verification pass (Fable, same day — model switched back)

Re-ran every computation; one attribution corrected, everything else reproduces.

- **Finding 1 CORRECTED — "-0.541 is overfit" is the wrong mechanism.** In the
  proxy-fit regime (the regime the constant describes), the n=61 slope is
  **-0.41 with R2 0.73** (zero-intercept form -0.409) — the "~81% of resid
  variance" comment was approximately true FOR THAT REGIME, and the n=20 -> n=61
  drift (-0.541 -> -0.41) is moderate, not wild. Opus's -0.163 / 19% figures
  describe the REAL-REFIT regime — a different conversion. Correct statement:
  the steep level trend is largely a PROPERTY OF THE PROXY-FIT CONVERSION's
  scale mismatch with real grades; refit the conversion and the level trend
  mostly dissolves. This STRENGTHENS the overall diagnosis (shape was
  conversion-artifact-contaminated) while correcting the attribution. The
  LEVEL_SLOPE constant must be re-fit jointly with any conversion refit.
- Finding 0 reproduced (9/13 MAC positive raw resid; the wrap sentence was a
  shape-vs-resid conflation). Finding 2 reproduced exactly (R2 0.82/0.73; MAC
  -1.76, AAC +2.93; gradient dissolves). Finding 3 reproduced (Spearman 0.94).
  Finding 4 stands as the open concern (MAC def dummy -4.24 -> +4.58 margin).
- **Finding 5 STRENGTHENED.** Fixed the 75% match rate (502 -> 651 of ~656;
  only San José State's accent-norm edge case remains) and added within-year
  demeaning: G5 corr **+0.009** (n=276), G5 bottom-quartile churn mean
  **+1.70 ABOVE preseason** (43% below). The churn-markdown rationale is
  refuted at every reasonable specification.
- Final-impact computation reproduced (pipeline/diag_final_impact_61.py):
  proxy-fit vs real-refit-61 conversion, same field, same recentering — MAC
  mean final -14.94 -> -16.67 (**mean Δ -1.73**, range -1.05..-2.52, all 13
  down); all-61 mean |Δ| 0.97. Level/shape confirmed absent from the final
  path in code (adj = clip(K x resid) only). Caveats stand: refit-on-61 is a
  stand-in for the production refit-on-138 (G5-heavy field, 27/61), and
  production recenters over the full hybrid field — direction robust,
  magnitude provisional.

### Implemented on the back of this diagnostic (2026-07-16)
1. pilot_readout.py LEVEL_SLOPE comment corrected + printed decomposition
   relabeled "(proxy-fit regime)" — no numeric/behavior change.
2. MAC wrap: dated correction block appended (shape sentence withdrawn;
   Toledo/WMU market leans withdrawn; Toledo's anchor-side dispersion note
   retained).
3. Deferred to the refit checkpoint (owner approval obtained for the
   diagnostic, not for parameter changes): joint refit of conversion weights +
   level slope on real grades (production plan = at 138; consider an interim
   checkpoint at ~90-100 builds), and the Finding-4 defense-dummy
   investigation (is it my MAC defense grading or the anchors?).
