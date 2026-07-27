# Pre-registration — Study 8: shadow-arm backtest (2026-07-27)

Committed BEFORE any outcome regression is run. Purpose: the first movement-validation
test of the roster arm — does the FORMULA component's disagreement with preseason SP+
predict the preseason→final SP+ miss? Governance as always: bars fixed now; failures
reported and kept; owner-facing claims follow the interpretation matrix below.

## What is and is not under test

Under test: the mechanical formula arm ONLY (spine tape × k-retention × jumps ×
FR priors × conference offsets — the shipped v2 constants, unchanged). NOT under test
(unbacktestable): the dossier/qualitative layer and adjudication blends — any modern
source about historical fall camps is hindsight-contaminated. 2026 remains their first
live test. A full S8 pass licenses the sentence "the mechanical component is
movement-validated," not "the rig is validated."

## Peek disclosures

1. Phase 1 (fidelity, NO outcome data) ran before this registration by design:
   2026 auto-arm vs curated proforma_v2 gate ρ(D) = **0.958** (per-unit r 0.934–0.985);
   2025 Mode-A vs Mode-B bridge ρ(D) = **0.972**. Fidelity gate (bar ≥ 0.70) is MET —
   attenuation from mechanical rosters is ≤ ~8% on any true coefficient.
2. The outcome panel (miss = final − preseason SP+, 2022–25, reversion baseline
   −0.194·level) is the S6 panel and its baseline behavior is known. The S8 candidate
   (shadow-arm D) has never been computed against outcomes. S6-F3's crude trench proxy
   (no roster continuity) failed; that motivates Leg 2a, it does not prejudge it.
3. Study 7 (consensus vs market, same SBD boards used in Leg 3) is known: |d|≥1.0
   consensus side 77.3%. Leg 3 asks a NEW question of those boards (does the arm help
   consensus), not a rerun.

## Construction (fixed)

- Shadow arm per season y ∈ {2022,2023,2024,2025}: membership = CFBD season roster
  (Mode B; 97.5% contributor coverage, verified not participation-derived); tape =
  spine y−1 (full) else y−2 (vol×0.5); name match preference same-team → unique →
  drop; formula = shipped v2 constants (POSMEAN/K/WCAP/jumps/FRB/conf offsets);
  depth = top-N by evidence volume at 1.0 (QB 1, RB 2, WRTE 5, OL 5, DL 5, LB 3,
  DB 5), next 2 at 0.33 (QB 1); FR priors fill remaining slots from recruiting
  composites; unmatched newcomers silent. Engine: pipeline/research/s8_shadow_arm.py.
- Team score = UW-weighted mean of within-year unit percentiles (UW: QB 1.2, RB/WRTE/
  LB 0.8, OL/DL/DB 1.0). Missing unit → 50 imputed.
- Disagreement D = z_y(team score) − z_y(preseason SP+), z within year. D_pts =
  D × SD_y(preseason SP+).
- Outcome: miss = final SP+ − preseason SP+ (points), sp_final/sp_preseason vintages.
- Primary regression: miss ~ a + b·sp_pre + c·D, pooled 2022–25, OLS, plain t
  (S6 convention). LOYO = leave-one-year-out, 4 folds.

## Bars

- **Gate (met above):** 2026 fidelity ρ(D) ≥ 0.70. Had it failed, S8 would be declared
  underpowered and no outcome regression run.
- **L1-A (main effect):** c > 0 and t(c) ≥ 2.
- **L1-B (stability):** c's sign stable in 4/4 LOYO folds.
- **L1-C (materiality):** ΔR² ≥ 0.02 over the reversion baseline.
  L1 passes only if A, B, C all pass. L1 is the ONLY primary.
- **L2a (trench premium, secondary):** split score into trench (OL+DL) and rest
  (5 units), D_t and D_r as with D. miss ~ a + b·sp_pre + c_t·D_t + c_r·D_r.
  Claim "trench disagreements realize more" iff t(c_t) ≥ 2 AND c_t > c_r.
- **L2b (coachability, focal test + descriptive table):** unit residual = realized
  as-played unit grade (year y, volume-weighted from spine) − shadow-projected unit
  value (same scale, no offsets on both sides — offsets cancel; implemented as raw-
  grade projection). Persistence = Pearson r of consecutive-year residuals per program,
  pooled year-pairs 2022→23→24→25. Claim "OL is coachable" iff OL r ≥ 0.20 with
  t ≥ 2. All-unit ranking reported descriptively.
- **L3 (money leg, soft bars — no kill power):** SBD DK openers 2022–24 (~219 rows).
  Expected wins via probit engine (σ=13.5, HFA 2.3, FCS game = 0.95 win), rating
  vectors: consensus = preseason SP+; consensus+arm = SP+ + λ·D_pts for the rated
  team, λ ∈ {0.5, 1.0}, primary λ=1. Soft bars: (i) MAE vs actual regular-season wins
  improves; (ii) where arm-adjustment flips the side of the market at |d| ≥ 1.0,
  flipped sides win ≥ 50%. Wins definition identical to S7 (CFBD regular-season file).
- **L4 (scale, measurement not test):** β from miss ~ a + b·sp_pre + β·D_pts.
  If L1 passes: recommended 2027 arm multiplier λ* = clip(β, 0, 1) with CI. If L1
  fails: λ* = 0.
- **L6 (heterogeneity, report-only):** c by P4/G5, |D| terciles (threshold check),
  new-HC vs continuity (coaches file), and driving-unit attribution. Generates 2027
  hypotheses only; no claims from this leg.

## Interpretation matrix (registered)

- L1 pass → formula arm is movement-validated; measured effect is a LOWER bound
  (roster noise attenuates, ≤ ~8%). Book's arm-dependent positions upgrade from
  "component-validated" to "movement-validated (mechanical core)."
- L1 fail → the arm does not predict consensus drift at detectable size; the
  arm-dependent positions rest on the dossier layer + 2026 live results alone; the
  2027 build re-scopes the formula arm's role. (Gate already passed, so a fail is a
  REAL fail, not "rosters too noisy.")
- L2/L3/L4/L6 modify sizing and 2027 design only; they cannot rescue or overturn L1.

## Limitations (registered)

Retention/jump/FR/offset constants are pooled 2021–25 fits (S1/S2/S4 showed
fold-stability, bounding the leak; a real-time 2022 fit would have been noisier but
similar). CFBD rosters are season-vintage captures — residual mid-season-removal
channel unmeasurable but judged small (rosters retain ~42% never-played players, so
they are not attrition-trimmed lists). The shadow arm diverges from the curated arm
precisely on exotic-roster teams (JUCO/FCS/D2 influxes — UConn-type); S8 validates the
matched-tape core, and says nothing about unmatched-newcomer curation. SP+ miss is a
one-system proxy for "consensus movement." SBD money-leg boards are P4-heavy while the
2026 book's arm-dependent positions skew G5 — sample-mismatch caveat carries to L3's
reading. QB depth in the shadow arm is volume-ranked, not camp-informed; Phase 1 puts
that cost inside the measured 0.958.
