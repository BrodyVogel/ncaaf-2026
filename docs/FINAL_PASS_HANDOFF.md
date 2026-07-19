# FINAL PASS — handoff & repeat procedure (for Opus / any successor)

Written 2026-07-18/19 by the Fable session that completed the 138-team field, ran the
first production final pass, and executed the owner's residual-mode decision. Owner:
Brody. Read this before touching any grade or board. The step-by-step execution plan
that remains is in docs/FINALIZATION_PLAN.md.

## 1. What the final pass is (and why it exists)

Every team's at-grading-time final (the `final` column in `outputs/grade_board.csv`) was
PROVISIONAL in two ways, both documented in pipeline/pilot_readout.py and
outputs/GRADING_BIAS_DIAG_2026-07-16.md:

1. **Proxy-fitted conversion.** The grade->points conversion (unit grades -> implied
   off/def points, whose gap vs the anchor is the "residual") was fitted on the 137-team
   SHADOW-PROXY field — known inflated at the bottom (diag Finding 2) — and applied to
   each real-graded team out-of-sample.
2. **Drifting recenter.** Each pilot final was recentered against whatever hybrid
   (proxy + real) field existed on its grading day.

`pipeline/final_pass.py` fixes both: it refits the conversion by OLS on **all 138 real
grades** against the frozen anchor off/def splits, recomputes every residual under that
one fit, reassembles every final under the frozen formula, and recenters the whole
field once. Deterministic (verified byte-identical across runs); hard-fails on a
partial or mis-joined field.

## 2. The formula (frozen constants; residual mode per the §6 decision)

```
final = anchor_blend                      (frozen anchor run, class0, 2026-07-14)
      + class_term                        (class_per_side = 0.0 in this run)
      + clip(0.35 * residual', ±6.0)      (K=0.35, CAP=6.0)
      + (ST_grade - 50)/50                (max ±1 pt)
      - field_mean                        (one recenter over all 138)

residual  = (implied_off - anchor_off) - (implied_def - anchor_def)
residual' = residual - pool_mean(residual)          <- OFFICIAL mode (see §6)
pool      = the team's conference; for the 2 FBS Independents (no conference):
            Notre Dame -> the all-P4 pool mean, UConn -> the all-G5 pool mean
            (pseudo-pools; anchor run's p4 flag decides class)
implied_off/def = OLS(all-138 real grades -> anchor off/def), intercept included
band = 6.0 x (1.13 if HC change) x (1.10 if anchor dispersion flag) x (1 + 0.03*min(L,5))
```

Off units: QB RB WRTE OL. Def units: DL LB DB. Coordinator changes do NOT trigger the
band — only head-coach changes. Anchor file:
`outputs/anchor_runs/anchor_run_2026-07-14_class0.json` (FROZEN input).
Do not change K, CAP, SIGMA, band multipliers, the class term, or the residual mode
without owner approval.

## 3. The repeat loop (Brody plans to edit grades — this is the whole procedure)

```
1. Edit snapshots/<Team_Dir>/grades.json      # change units.<U>.grade / confidence
2. Keep the paperwork consistent, or grades_check FAILS:
   - either update the dossier "PLANNED GRADES:" line in unit_dossiers.md to match, or
   - declare the change in grades.json _meta.planned_vs_final_deviations (name the unit)
3. python3 pipeline/grades_check.py <Team_Dir>     # per-team gate must return OK
4. python3 pipeline/final_pass.py                  # regenerates EVERYTHING (official mode)
5. Read outputs/final_pass/REFIT_DIAG.md           # sanity-check (see §5)
6. git add -A && git commit && git push
```

The refit re-estimates the conversion on the EDITED grade set; at n=138 a single-team
edit moves the weights only marginally. Grades are even integers by convention.

## 4. What lives where (authority map)

| file | status |
|---|---|
| `outputs/FINAL_BOARD_2026.csv` / `.md` | **AUTHORITATIVE** board — regenerated only by final_pass.py default (official) mode |
| `outputs/final_pass/ASSEMBLY.csv` | full per-team audit: anchor, implied O/D, resid, adj, ST, recenter, final, band |
| `outputs/final_pass/REFIT_DIAG.md` | weights, R², level slope, cap census, removed conference component, movers |
| `outputs/final_pass/*_frozen.*` | the pre-decision (full-residual) comparison variant, via `--frozen-resid` — never authoritative |
| `outputs/grade_board.csv` | pilot-era at-grading-time finals — HISTORICAL AUDIT ONLY; still the grading peer-rail |
| `snapshots/<Team>/grades.json` | the only file you edit to change a team's rating |

## 5. Sanity checks after every final_pass run (60 seconds)

Baselines from the adopted official run (2026-07-19 @ demean default):
- 138 teams joined, no assertion errors.
- R²: off **0.67**, def **0.49**. A collapse (<0.3) or a jump to ~1.0 = data problem.
- Level slope (diagnostic only, never enters finals): **-0.146** official mode
  (frozen-mode reference -0.363).
- Cap census: **0** teams capped in official mode (frozen-mode reference: 3).
- Recenter shift ~ **+0.55**; movers small and explainable; Spearman vs prior ~0.99+
  unless grades were edited.
- Post-demean conference mean residuals ≈ 0 (by construction) — shown in the diag.

## 6. DECISION RECORD — residual mode (owner: Brody, 2026-07-19)

**Adopted: conference-demeaned residual as the OFFICIAL mode** (default in
final_pass.py). Owner policy: "no conference biases unless quantitatively verified; a
P4/G5 bias conceivable with significant evidence; per-conference edges presumptively
distrusted given realignment turnover."

Basis, on the record:
- A direct backtest of the grades' conference-level signal is **impossible** — no
  historical grades exist from this two-week-old process.
- The indirect evidence points artifact: the churn rationale was backtest-refuted at
  n=651 (diag Finding 5); the conference-level component is unstable across fit regimes
  (AAC flipped -2.4 -> +2.9, Finding 2); the pattern is mechanically confounded with
  scale compression (level slope -0.363, conferences are level clusters).
- The class-level (P4/G5) effect the owner would entertain was already measured in the
  anchor run's class test (2026-07-15): **+0.15 pts, t=0.3 — nil.** Conference demeaning
  also removes any class component, so nothing evidenced is lost.
- Realignment makes historical per-conference estimates non-stationary (2026 CUSA
  contains two FBS newcomers), which caps how convincing any conference backtest could
  ever be — per the owner's own standard.
- Effect of adoption: SEC/MWC return ~+2.6/+3.1 toward their anchors, CUSA/SBC drop
  ~-3.5..-4.7 back to theirs; within-conference ordering (the validated signal,
  Spearman 0.94) is untouched; 0 teams cap.

Pseudo-pools: the 2 Independents demean against their class pool (ND -> all-P4 mean,
UConn -> all-G5 mean) — a conference-mean is meaningless for an n=2 "conference" of
unrelated teams. `--frozen-resid` reproduces the pre-decision board for comparison
only. Reversal of this decision = owner instruction + flip the default + update this
record.

## 7. Known open items a bettor (or successor) should keep in mind

1. **Diag Finding 4 (unresolved):** with grades held fixed, MAC defenses carry a -4.24
   def-dummy. Investigate before trusting MAC totals. (Note: conference demeaning now
   neutralizes its *level* effect on finals; the question of MAC defense grading
   accuracy remains open for within-MAC ordering.)
2. **Staleness:** snapshots frozen ~2026-07-18. 52 teams carry an L-graded QB (open or
   thin QB situations); 31 teams carry >=3 L units. The durable checklist is
   `outputs/STALENESS_REGISTER.md` (+ `.csv`, regenerated by
   `pipeline/staleness_register.py`); re-verify per its procedure + FINALIZATION_PLAN
   Step 3 before wagering. Open recommendation as of 2026-07-19: NMSU LB Tory Gethers
   appears to have returned (active on the current roster; the in-portal note was
   2026-01-21) — LB 38 L → ~44 M pending owner approval.
3. **Tooling flags** (outputs/FORWARD_FLAGS.csv, display-layer only): team_dump.py
   percentile matcher — 'LA MONroe' (UL Monroe), 'Houston' substring (Sam Houston),
   'Connecticut' (UConn). Fix before future re-grades.
4. **Notre Dame IND-cell judgment:** ND graded at elite/P4 level (IND cell NOT applied);
   a positive-P4-cell reading would add ~2-4 pts. UConn graded G5.
5. Ratings are neutral-field margins. Win totals require the schedule conversion
   (FINALIZATION_PLAN Step 4) — the board is the INPUT, not the edges.
