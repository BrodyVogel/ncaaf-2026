# v2 rollout plan — full-board regrade (owner-approved direction 2026-07-23)

Owner decision: adopt v2 as the player-grade baseline and apply to EVERY team (mixed
vintage would break cross-team comparability). Steps and technical answers:

1. **v2 baseline accepted.** Formula (validated components only): w(n)=n/(n+k) shrinkage
   (k: QB230/RB110/WRTE190/OL595/DL290/LB630/DB1180; caps QB .55 LB .50) + class-jump
   terms (G5→P4 −3.54, P4→G5 +1.45) + freshman composite priors (per-position
   baselines/slopes in GRADING_V2_SPEC) + single-year missed-season look-through
   (volume ×0.5) + destination-conference SCALE term (offsets keep the scale job).
   FCS/D2/JUCO entrants: v1 qualitative brackets unchanged. Portal stars banned.
1a. **Bridge, no refit:** projected player grades → national percentile within unit type
   (built in pipeline/research/proforma_v2.py) → 0–100 unit scale. The unit→O/D OLS in
   final_pass auto-refits every run; its un-shrink handles any distribution change.
2. **Adjudication (the work):** 940 units, tiered — |formula−dossier| ≤ ~4 → accept with
   note; medium → dossier read + logged decision; large + ALL 14 bet-held teams → full
   re-open (bet teams FIRST, starting with UConn QB/unit stack, pro forma −19).
   Output: adjudication CSV (team, unit, formula#, final, confidence, deviation reason).
   Pace: 30–50 teams/session ⇒ 3–5 sessions. New grades land as regenerated grades.json
   with _meta vintage="v2 2026-07"; v1 preserved in git + ASSEMBLY_LOCKED_2026-07-20.
3. **Refits:** final_pass OLS = automatic. Market-stretch s* = automatic at payload
   build. Bands from new confidence letters = automatic. Calibrated ×0.75 = DO NOT
   refit (property of July-rating quality, fitted on 2021–25 outcomes; revisit post-2026).
   Anchor frozen. Manual overrides re-examined per team during adjudication; demeaning
   exclusion machinery stays.
4. **Rebuild + impact:** final_pass → win_totals_compute (payload) → artifact →
   bet_tracker; full before/after memo incl. all open bets re-priced (expect movement;
   bets hold at their prices); persisted-artifact refresh; commit per conference batch
   with session trailers.

Order of adjudication: (1) bet-held teams (UConn, Tulsa, Oregon State, Bowling Green,
Liberty, Arizona State, Kennesaw State, Illinois, West Virginia, East Carolina, Hawai'i,
Florida, UCF, Pittsburgh) → (2) pro forma |Δteam| > 12 shortlist → (3) remaining field
by conference. Inputs ready on disk: outputs/proforma_v2_2026.csv (formula numbers per
unit), snapshots/*/roster_two_deep.csv, spine, recruiting pulls.

## Adjudication log started (2026-07-23) + one formula fix

**UConn adjudicated (worked example, adjudication_v2.csv).** Net: QB 46→44, LB 50→47,
DB 44→47, DL 46→47, rest hold. Team impact ≈ −0.1 pts — **the pro forma −19 dissolves
under adjudication**: it was (a) the v1-mech strawman at QB (dossier's L had already
hand-shrunk the tiny samples the offset arithmetic took at face value) and (b) an
**Independents artifact**: the IND destination-offset cells (RB −14.11, OL −21.97) are
fitted on an Army/UMass/UConn pool polluted by Army's option scheme.
**FIX (applies to ND + UConn in all v2 math): Independents use their class-pool mean
(ND → P4 pool, UConn → G5 pool) as the destination scale term, never the IND cell** —
same convention as final_pass demeaning. Notre Dame's −21 pro forma row must be re-read
the same way before any conclusion.
**Bet verdict: UConn O5.5 survives adjudication essentially intact (small QB trim).**
Remaining: 13 bet teams → shortlist → field, per the plan's tiering.

## Session 2 progress (bet teams adjudicated; method refinement)

**Method fix:** adjudication gaps are computed WITHIN-CONFERENCE (demeaned, mirroring
final_pass) — the raw v2-vs-dossier comparison was swamped by a scale-convention
artifact (graders "weighted DOWN" the big SEC offsets; the mechanical arm applies them
full-size onto compressed tape spreads → every SEC unit ranked 90s). Demeaned, the
field's disagreements are ~±10, DB-heavy (consistent with S2's DB-unreliability).
**13 bet teams adjudicated** (adjudication_v2.csv; pending grades — grades.json written
once at rebuild). **Illinois FLAGGED for full re-open** (formula up +10..+24 on five
units, against our U7.5). Kennesaw held (override-pinned).
**Next:** Illinois re-open; demeaned shortlist (Louisiana, Georgia State, South Alabama,
Tulane, Colorado State, Arizona, Notre Dame w/ IND fix, Rutgers, WKU, Michigan State);
then the field by conference; then rebuild + impact memo.

## Session 2 close: Illinois re-opened, shortlist adjudicated, Tier-3 blend rule adopted

**Owner amendment:** middle-ground blending allowed at EVERY tier (not binary
accept/reopen); Tier 3 additionally requires coverage + staleness screens before accept.
**Illinois (re-opened):** formula vindicated — Houser's 84.0/473db is real full-volume
tape the dossier double-discounted (the v1 failure mode). QB 62→70, RB 32→38, WRTE
48→52, DL 41→45, OL 38→42, LB 46→48. Net ≈ +1 rating pt at rebuild → U7.5 thins ~3-4pp
but stays +EV. **DB adjudication policy (S2-informed):** dossier DB grades over-confident
AND formula DB percentiles under-informative (w≤0.35) → blend 1/3 toward formula, cap ±8.
Shortlist done except **Notre Dame (deferred — IND pool n=2 makes demeaning meaningless;
Illinois-style re-open under the Independents fix, first item next session).**
**Remaining:** ND re-open → ~110-team Tier-3 field sweep (scripted: blend rule where
|dg|>4, coverage+staleness screens, every unit logged) → regenerate grades.json v2
vintage for all 138 → final_pass → payload → artifacts → tracker → full impact memo
(all bets re-priced). Start a fresh thread with: "Continue the v2 rollout per
docs/research/V2_ROLLOUT_PLAN.md — pick up at Notre Dame."

## Session update (cont.) — field sweep complete
- ND re-opened under the Independents fix (P4-pool scale term): QB 86→84, RB 66→64, OL 78→74,
  five units hold. The pro forma craters were 100% polluted IND cells (OL cell −22.0 vs P4 pool +6.0).
- Field sweep: trigger reset |dg|>4 → |dg|>8 (=1 SD of the demeaned gap, 8.49; matches the manual
  rounds' de facto floor — |dg|>4 would have blended 61% of the field, i.e. noise). Added: unit-info
  guard (matched volume-weight share; <0.10 hold "formula uninformative" [37 cases, e.g. Iowa QB w̄=0.03],
  <0.20 blend halved), option-academy halving (Army/Navy/AF — PFF option-scheme distortion),
  FR-prior info credit 0.25 (S2b). Blend weights: DB 1/3, LB 0.40, others 0.50, cap ±8.
- 1,041 sweep verdicts appended; 256 blends (118 up / 138 down, mean |move| 5.0); 5 manual
  middle-ground overrides after |dg|>20 review (Duke QB 46, Michigan QB 56, Wisconsin QB 57,
  LaTech WRTE 50, Tulane RB 54). Every unit on every team now has a logged verdict.

## ROLLOUT COMPLETE (2026-07-23)
All four steps done: (1) v2 baseline accepted; (1a) no conversion refit needed — OLS
auto-refit R² 0.66/0.47 ≈ unchanged; (2) every unit on every team adjudicated (1,098
verdicts, 302 changes/122 teams); (3) no model refits beyond the automatic ones (stretch
1.1475→1.1591 at payload build; calibrated ×0.75 untouched by design); (4) all rating
variants recomputed and populated into win_totals_2026.html + bet_tracker.html.
Impact memo: docs/V2_IMPACT_MEMO_2026-07-23.md. All 14 bets survive; UCF conf O3.5
flagged THIN (mm +1.5%) — hold, no add, fall-camp re-check.
Standing next items: ACC official poll re-sweep (Jul 28), fall-camp QB-battle re-sweeps
(UCF QB explicitly), Study 3 (continuity × prior-stability) still deferred.

## Reconciliation pass (2026-07-23, post-rollout)
Dual-aggregation robustness check over all 256 sweep blends (starter-only vs full
two-deep; move only by the agreed disagreement). 51 amended toward dossier (mean 1.6,
max 5 grade pts), 4 full reverts, 205 confirmed. Board effect 0.036 mean |dFinal|.
v2.1 is the production vintage. Log: 51 AMENDED rows appended to adjudication_v2.csv.

## v2.2 (2026-07-23): sensitivity bound + full per-case re-read
Sensitivity: bets invariant across blend-weight [0x, 2x] — soft constants decision-irrelevant.
Re-read: all 256 blends read case-by-case (dossier rationale + player math + disagreement
reason); 136 confirmed, 120 adjusted (mostly toward dossier; ceiling-squeeze, offset-axis,
formula-void, dual-threat and solo-aggregation corrections). 2027 candidates: rank-based dg,
QB rushing-value term. Production vintage = v2.2.

## v2.3 (2026-07-23): accept-layer completion — full field adjudicated
False-agreement screens over all 625 accepts (rank-view, starter-view, missing-star,
dual-QB) → 320 case reads (68 adjustments ±2-3, 252 confirms); deep band sample-validated
0/40 (pre-registered rule, no expansion); ST 138/138 single-source scanned. Board delta
0.049 mean. All 14 bets stable; UCF THIN unchanged. Production vintage = v2.3.

## 2027-build candidate register (consolidated, owner Q&A 2026-07-24)
- Rank-based dg for adjudication sweeps (kills ceiling-squeeze / offset-axis artifacts).
- QB rushing-value term (formula is passing-facet only; dual-threat blind spot).
- Career pooling with FITTED decay (S2-C: directionally right, under bar with decay fixed at 0.5).
- Class-year aging interaction, retried jointly with career pooling (Study 2: stayers improve
  +1.3–1.9 uniformly — cancels in field rescale; FR/SO differential flipped sign across seasons,
  failed stability bar; more seasons of pairs may stabilize it).
- NEW: program-x-unit development residuals ("Iowa OL" effect) — regress unit as-played grade on
  prior-year projection; test whether program-unit residuals persist across seasons (fold-stable,
  pre-registered bar before shipping). Currently covered only by the dossier arm case-by-case
  and by the team-level anchor blend.
- Retention calibration of w(n) — Study 4 (2026-07-24, pre-registered): global under-retention
  beta +0.059 fold-stable 4/4 (S4-A PASS); NOT a tail/spline effect (S4-B FAIL — supersedes the
  spline idea from the 07-24 decile peek, which was never registered here); per-group k regrid
  under bar (S4-C FAIL). Within-group texture: miss lives in lo/mid-volume tape (+0.037/+0.040),
  hi-volume slightly over-retained (-0.036) -> 2027 remedy = refit w(n) FUNCTIONAL FORM
  (volume-dependent), not a flat beta and not per-group k. See FINDINGS_S4_2026-07-24.md.
