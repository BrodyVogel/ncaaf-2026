# Grading v2 — player-projection spec (proposed 2026-07-23, awaiting owner sign-off)

What changes and what doesn't, side by side. Everything downstream of the player layer —
unit percentile mapping, depth/integration adjustments, exemplar bracketing, confidence
letters, magazine cross-checks, final_pass constants (K=0.35, ±6 cap, demeaning, bands) —
is **unchanged**. This spec replaces only the arithmetic that turns a player's history
into a projected grade before the grader maps players → unit percentile.

## Before → after, step by step

**1. A returning player with tape (same team).**
- *v1:* use last season's facet grade at face value, with ad-hoc language for small
  samples ("tiny sample — weighted DOWN HARD") and no fixed rule for how hard.
- *v2:* `projected = prior + w(n) · (grade − prior)`, with `w(n) = n/(n+k)`:
  k = QB **230** dropbacks · RB **110** carries · WR/TE **190** routes · OL **595** ·
  DL **290** · LB **630** · DB **1180** snaps. Cap w at ~0.55 (QB) and ~0.50 (LB), where
  their empirical curves plateau. Prior = position mean (QB 69.7, RB 73.5, WRTE 62.6,
  OL 62.0, DL 64.9, LB 62.3, DB 65.2 — PFF scale). The grader still adjusts
  qualitatively (injury, role, scheme) but writes the formula number first and records
  the deviation.

**2. An FBS→FBS transfer.**
- *v1:* flat conference offset applied to the raw grade
  ("67.5/441 → MWC −7.35 → 60.2 adj"), same charge regardless of sample size; offsets
  run ±5 to ±16 per side depending on unit.
- *v2:* shrink first (step 1), then one small jump term: **−3.5** stepping G5→P4,
  **+1.5** dropping P4→G5, **0** lateral (any P4↔P4 or G5↔G5). The old offsets are
  retired from player projection entirely. Validated: this beats the offset arithmetic
  by 28% out-of-sample; the offsets were scale-translation misused as forecasting.

**3. A true freshman projected to play (no college tape).**
- *v1:* position mean plus qualitative pedigree language ("ex-4-star, pure pedigree").
- *v2:* `prior = FR baseline(pos) + slope(pos) · (composite − 0.861)` — baselines/slopes:
  QB 58.1 (+9.2 per 0.10), RB 73.0 (+1.2), WRTE 61.0 (+3.3), OL 56.5 (+7.7),
  DL 60.5 (+5.0), LB 58.8 (+3.1), DB 62.7 (+4.7). (Thin cells — QB n=87 — may fall back
  to the pooled +4.7 slope.) Note freshmen anchor BELOW the all-player position means:
  a 5★ QB freshman projects ~71, not 75+. As real snaps arrive, w(n) blends tape in.

**4. A year-2+ player finally getting his first real role.**
- *v1:* pedigree still cited ("former top-100").
- *v2:* prior = position mean, **pedigree gets zero formal weight** — the composite's
  signal for late first-timers measured 0.05. Being kept off the field for two years is
  itself the evaluation. Qualitative camp/news reads still allowed, logged as deviations.

**5. Transfer-portal star ratings.**
- *v1:* occasionally cited as supporting color.
- *v2:* **banned as an input** (ΔR² 0.009 with tape known; 0.07 correlation when no tape
  exists). Cite them only when describing market/public perception.

**6. FCS/D2/JUCO entrants (no FBS tape).**
- *v1 and v2 identical:* existing qualitative brackets and level heuristics. The panel
  is FBS-only, so nothing here was validated either way — explicitly out of scope until
  a future study.

## Worked examples (real board cases)

- **Eget** (QB, 67.5 on 441 db, SJSU→Duke). v1: 67.5 − 7.35 = **60.2**.
  v2: w = 441/671 = 0.66 → 69.7 + 0.66·(67.5−69.7) = 68.3 → G5→P4 −3.5 = **64.8**.
  Directionally: our board under-rates him ~4.5 grade points.
- **Mendoza** (QB, 85.5 on 25 db, Indiana→GT, lateral). v1: "+B10 0.55 → ~86, weighted
  DOWN HARD" (unquantified). v2: w = 25/255 = 0.10 → 69.7 + 0.10·(15.8) = **71.2**.
  The down-weighting is now a number, not an adjective.
- **A 0.98-composite 5★ QB starting as a true freshman.** v1: position mean + vibes.
  v2: 58.1 + 92.4·(0.98−0.861) ≈ **69.1** — roughly average-starter level, which is
  exactly what history says elite freshman QBs deliver as first-year tape.

## Why the team-level effect is bounded (and that's fine)

Player projections feed unit percentiles → OLS conversion → a residual blended at
K=0.35 and clipped ±6. A 4-point player-grade correction on one starter moves a unit a
few percentile points and the team rating by ~0.1–0.3 — by design. The value shows up
in aggregate across every transfer-heavy roster, and in the discipline of run-to-run
consistency (the same inputs now always produce the same number).

## Rollout options (owner decision)

- **A (minimum):** adopt v2 prospectively — fall-camp adjustments, week-to-week updates,
  and the 2027 build use the new arithmetic. Zero disturbance to the frozen 2026 board.
- **B (recommended):** A + a **targeted audit** of 2026 grades where v1 and v2 disagree
  most: units leaning on G5→P4 imports (we over-charged; likely under-graded) and G5
  units built on P4 drop-downs (we over-credited; likely over-graded). Audit produces a
  diff list for owner review before any grade changes; changes then flow through the
  standard addendum/deviation machinery and a full rebuild.
- **C (maximum):** B + regrade every unit whose dossier arithmetic materially used the
  retired offsets. Not recommended mid-season — high churn, most moves would be <2
  grade points, and the anchor blend dampens them further.
