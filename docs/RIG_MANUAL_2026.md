# The Rig, Explained — CFB 2026 Win-Total Model, Ground Up

*(2026-07-24. Written for a newcomer who wants to understand every part and be able to
modify it. Every formula and constant below is transcribed from source files, which are
named as you go. The one-screen version: we grade rosters unit-by-unit with a
formula+dossier double arm, convert grades to a power rating leashed to a public
consensus, run an exact win-distribution engine under two honesty lenses, and bet only
totals that clear +4% on both lenses. Discipline — pre-registration, provenance ledgers,
dual-lens conviction — is treated as part of the model, not paperwork.)*

Data flow at a glance:

```
PFF player history ─┐
CFBD (rosters, recruits, ├─► PLAYER projections (formula arm) ─┐
  schedules, lines)  │                                         ├─► UNIT grades (adjudicated)
magazines / media days / ├─► UNIT dossiers (qualitative arm) ──┘        │
  portal rankings    ─┘                                                 ▼
six public rating systems ──► CONSENSUS anchor ──► TEAM assembly (final_pass.py)
                                                        │  power rating + band
                                                        ▼
                                       lenses: calibrated (×0.75) / market-matched (×~1.15)
                                                        │
                              win engine (probit + shared shock, exact Poisson-binomial)
                                                        │
                        board of edges vs de-vigged lines ──► conviction (min-lens) ──► bets
```

---

## 1. Sources — what we lean on

- **PFF player grades + workload volumes, 2021–2025** (`data/pff`, `data/pff_history`).
  The backbone of the formula arm. One primary facet per position group (QB→passing,
  RB→rushing, WR/TE→receiving, OL→blocking, front-7/DB→defense); volume is the
  file-native workload (dropbacks/carries/routes/snaps). Compiled into
  `data/research/spine.csv` (player-season rows) and `pairs.csv` (year-over-year pairs)
  by `pipeline/research/build_spine.py`.
- **CFBD API** (key in `/root/.cfb_secrets/`, never committed): schedules, conference
  membership, recruiting player composites (`recruits_2026.json`), team talent, records,
  and posted game lines (`/lines`). Usage is far below quota; the tier allows 30k
  calls/month.
- **Six public rating systems** (`data/anchors/`): SP+ (double weight), FEI, Massey,
  FPI, TeamRankings, Pick Six — pulled 2026-07-12/14, z-normalized to SP+'s scale,
  winsorized, blended into the consensus anchor. `BLINDING_README.txt` documents that
  unit grading was done blind to these.
- **Preseason magazines and beat coverage** (`data/magazines`, `data/media_days`,
  `data/portal_rankings`): Athlon, Phil Steele, conference media-day triage notes,
  portal transfer rankings. These feed the dossier arm only.
- **Sportsbook win-total board** (`data/win_totals/win_totals_2026.csv`): manually
  maintained snapshots of FD/DK/CZR/BetRivers/Bet365 posted totals (regular +
  conference). Check the file's git date before trusting a price.
- **FCS opponent ratings** (`data/fcs_ratings_2026.csv`, method in
  `docs/FCS_RATINGS_METHOD.md`): 100 FCS opponents tiered from the Opta/consensus FCS
  Top 25 + program knowledge onto the FBS points scale (elite −18…−22 through low
  −44…−52), with deliberately wide bands (9–12).

## 2. Player grades — the formula arm, from the ground up

Everything here lives in the sweep/adjudication scripts
(`pipeline/research/field_sweep.py`, `reconcile_v2.py`, `accept_screen.py`) and is
specified in `docs/research/GRADING_V2_SPEC_2026-07-23.md`. For a rostered player on a
2026 two-deep (`snapshots/<Team>/roster_two_deep.csv`):

**Matched player (has 2025 PFF tape, or 2024 tape if absent in 2025):**

```
projected = posmean_u + w(vol) · (grade − posmean_u) + jump + dterm

posmean:  QB 69.7  RB 73.5  WRTE 62.6  OL 62.0  DL 64.9  LB 62.3  DB 65.2
w(vol) = min( vol / (vol + k_u), cap_u )          — reliability shrinkage
k:        QB 230  RB 110  WRTE 190  OL 595  DL 290  LB 630  DB 1180   (Study 2, LOYO CV 4–15%)
caps:     QB 0.55, LB 0.50 (reliability plateaus observed there in Study 2)
2024-only tape: volume × 0.5 (validated look-through, S2-D-A)
jump:     G5→P4 −3.54 (se .48) · P4→G5 +1.45 (se .32) · lateral 0   (Study 1)
dterm:    destination conference-cell offset from conf_offsets_2021_2025.json
          (fitted 2021–25: as-played unit grades vs same-year SP+, conference dummies;
          this is a SCALE term — centering values in the destination grade environment —
          NOT a performance forecast; Study 1's headline was that using these offsets as
          forecasts is worse than doing nothing)
Independents: ND uses the all-P4 pool mean scale term, UConn the all-G5 pool mean.
```

Key intuitions. A full starter season earns only w ≈ 0.52–0.65 — even proven tape is
half-shrunk toward the position mean, because that is what year-over-year reliability
measures. The transfer jumps are small on purpose: Study 1 showed the market-style
big-step-up discount double-counts (slope ≈ 0.40 of deviation transfers; the class jump
is the small residual on top). Known, quantified limitation (Study 4): w(n) under-retains
low/mid-volume tape by ~+0.04–0.07 of the deviation and slightly over-retains full-season
tape; three corrective forms failed registered validation, so the constants stand and the
knowledge ships as adjudication doctrine (§4).

**True freshman with a recruiting composite (no tape):**

```
projected = base_u + slope_u · (composite − 0.861) + dterm       (Study 2b fits)
base/slope: QB 58.1/92.4 · RB 73.0/12.0 · WRTE 61.0/32.5 · OL 56.5/76.6
            DL 60.5/50.3 · LB 58.8/31.1 · DB 62.7/46.8
```

Recruiting pedigree is steep for QBs, nearly flat for RBs — and it predicts NOTHING once
any FBS tape exists (the four-for-four null sweep: portal stars S1-C/D, composites past
year one, origin-roster brand S1-E: "a backup at Georgia was made a backup BY Georgia").

**Everyone else — JUCO, D2, FCS transfers, no-tape veterans:** the formula is silent. No
offset cell exists for their competition level, so they contribute nothing to the formula
aggregate; the dossier carries them entirely, and the unit's *info share* (volume-weighted
fraction of the room the formula actually saw; FR priors credited 0.25) throttles the
formula's authority in adjudication (<0.20 halves it, <0.10 holds the dossier).

## 3. Player grades — the dossier arm, and how the two become one

The dossier arm is a hand-built qualitative read per team unit
(`snapshots/<Team>/unit_dossiers.md`): returning production, portal arrivals/departures
with tape notes, magazine consensus (Athlon/Phil Steele), media-day and beat coverage,
depth, and an explicit bracketing against peer rooms on the calibration board
(`outputs/grade_board.csv` — regenerate with `pipeline/build_board.py` after any grade
change; its unit columns must track current grades or the artifact displays go stale).
Each unit gets a planned grade (1–99, roughly percentile-aligned within position) and a
confidence (H/M/L). L-confidence units widen the team band (§6).

**Adjudication (the v2 protocol, July 2026 — the current production grades).** The two
arms disagree constantly; the reconciliation is logged, append-only, in
`data/research/adjudication_v2.csv` (1,863 rows; last-write-wins per team×unit,
replayed by `pipeline/regen_grades_v2.py`). The machinery:

- Formula unit value = volume-weighted average of the room (starters 1.0, backups 0.33)
  → within-position rank percentile across all 138 teams → disagreement
  `dg = (formula pctile − dossier grade) − cell mean`, demeaned per conference×unit cell
  (Pac-12 pooled with MWC; Independents excluded from cells).
- Trigger: |dg| > 8 ≈ 1 SD of the dg distribution (a pre-registered |dg|>4 trigger was
  rejected — it would have "corrected" 61% of the field, i.e. noise).
- Blend on trigger: move the dossier toward the formula by weight 0.50 (DB ⅓, LB 0.40 —
  the lowest-reliability positions get the weakest formula vote), capped ±8, clamped
  [1,99]; info-share guard halves/kills thin-info pulls; service-academy units
  (Army/Navy/AF) get all formula authority halved — option/scheme outliers are a known
  formula failure mode.
- Every triggered blend was then CASE-READ (all 256), every accept passed
  false-agreement screens (rank-view, starter-view, missing-star, dual-QB) with 320
  further case reads, a dual-aggregation robustness check (starter-only vs full room,
  sign-preserving min), and a pre-registered 40-case audit of deep accepts (0/40
  expansions). Five units carry pinned manual overrides with written rationales.
- **S4 doctrine** (2026-07-24): in case reads, discount the formula's mean-ward pull on
  thin-tape rooms (its shrinkage is measurably too strong there); trust it on
  full-season tape.

To change a grade today: append a row to the adjudication log, then
`git checkout 36fcfed -- 'snapshots/*/grades.json'` (restore the v1 baseline — regen
compares against current grades, so replaying onto already-replayed grades corrupts
`v1_grade`), run `regen_grades_v2.py`, then the rebuild chain (§9).

## 4. Units → offense/defense/team: the assembly (`pipeline/final_pass.py`)

Eight unit grades per team (QB RB WRTE OL / DL LB DB / ST, 1–99). The conversion to
points is *fitted, not asserted*:

```
1. implied_off = OLS(QB, RB, WRTE, OL → anchor offensive points)    R² ≈ 0.67
   implied_def = OLS(DL, LB, DB    → anchor defensive points)       R² ≈ 0.49
   (refit on all 138 teams' real grades — the "full-138 refit," 2026-07-18)
2. un-shrink: rescale each implied side to the anchor side's SD (OLS fits compress
   toward the mean by ~√R²; without this the grade signal under-spreads)
3. resid = (implied_off − anchor_off) − (implied_def − anchor_def)
   then two owner-approved strips:
   a. CONFERENCE-DEMEANED — each league's mean residual removed (policy: no
      cross-conference level claims without direct evidence; the within-conference
      shape signal validated at Spearman ~0.94, the level component did not).
      Independents pseudo-pool: ND demeans vs the all-P4 mean, UConn vs all-G5.
      Manual-override teams are excluded from every demeaning pool (their junk
      residuals were polluting pool-mates).
   b. LEVEL-ORTHOGONALIZED — the component of the residual linear in anchor strength
      removed; it was measured to be grade compression (top teams read low, bottom
      high), not signal (docs/COMPRESSION_FIX.md).
4. adj = clip( 0.35 · resid, ±6 )        ← "our scouting gets a vote, not a veto"
5. final_raw = anchor_blend + adj + (ST−50)/50 + class_per_side (0.0 this run)
6. recenter once to field mean 0; then manual overrides for grade-unreliable
   reclass teams (data/manual_overrides_2026.csv, e.g. NDSU) applied post-recenter.
```

Special teams is deliberately shallow: a hand grade mapped to at most ±1 point. The
**band** (uncertainty, in points):

```
band = 6.0 · (×1.13 if new HC) · (×1.10 if anchor sources disagree top-decile)
           · (1 + 0.03·min(L, 5))          L = count of low-confidence units
```

## 5. The consensus anchor, and the exact role of the fade

The anchor (`pipeline/anchor_loader.py`, frozen run
`outputs/anchor_runs/anchor_run_2026-07-14_class0.json`) is a weighted z-blend of six
public systems on SP+'s scale — SP+ ×2, FEI/Massey/FPI/TeamRankings/PickSix ×1 — with
any source >5 pts from the others' median winsorized to that boundary. Off/def split
borrows SP+'s shape. Grading was done blind to it.

The philosophy of the leash: our grades are *independent* information (blind-built), so
their disagreement with consensus is allowed to move a team — but only the
within-conference, level-orthogonal component, at 35% weight, capped at ±6 points. Every
stripped component corresponds to a validated failure (level = compression; conference
means = unverifiable; P4/G5 class effect measured +0.15 pts, t=0.3 → class term 0.0).
The result ("Power/ours") spreads at SD ≈ 13.2, matching what true strength spreads to.
Competition-level terms inside player projections (the conference offsets, the ±3.5/±1.45
jumps) were all fitted on 2021–25 as-played data — provenance in §2.

## 6. Calibrated ratings (×0.75) — the honest probability lens

```
cal_T = field_mean + 0.75 · (ours_T − field_mean)
```

A July rating is an estimate; before it becomes a probability it must shrink toward the
mean. Game-level probit on 2021–25: preseason ratings carry slope **0.624** (a paper "93%
favorite" wins 81.5%); December ratings carry 0.983 ≈ 1 — the machinery is fine, July
information is the problem. Season-level, over 663 replayed team-seasons, the raw set is
overconfident (65% claims hit 60%) while ×0.75 is near-textbook (central-80% coverage
80.8%). The shrink is 0.75 rather than 0.62 because the band terms already absorb part
of the uncertainty. **All bet probabilities, EVs, and the tracker's Model P use this
lens. It is deliberately never refit toward the market** — it answers "what is true,"
not "what is priced."

## 7. Market-matched ratings (×s*) — the isolation device

```
mm_T = field_mean + s* · (ours_T − field_mean)      s* refit each build; currently 1.1545 (payload meta key: market_stretch)
```

`win_totals_compute.compute_market_stretch` bisects s* ∈ [0.8, 1.6] until the slope of
(our edge) on (market line) across all posted totals is exactly zero — the stretch at
which our edges stop correlating with how good the market thinks teams are. The market
prices totals as if strength spreads ~15% wider than our scale; this set adopts that
dispersion while keeping our ordering. It is **not** a belief — it is a screen: any edge
that survives on this set is team-specific, not the macro "market spreads too wide"
trade expressed 130 times. De-vig throughout is per-book fair probability averaging
(never medians of raw American odds across the ±100 boundary), with unposted under
prices inferred by the house 30-cent convention (`under_from_over`: over −132 ↔ under
+102).

## 8. Simulation — exact, not Monte Carlo (`pipeline/win_engine.py`)

```
P(S beats O) = Φ( (μ_S + δ − μ_O + 2.3·site) / σ_eff )
σ_eff  = sqrt(13.5² + band_O²)     game noise + opponent uncertainty (independent per game)
δ ~ N(0, band_S²)                  OUR error on S — ONE draw shared across the season
wins   = Poisson-Binomial over the schedule given δ (exact O(G²) DP),
         δ integrated out by 21-node Gauss-Hermite quadrature (deterministic)
```

Calibration of the constants: σ_game = 13.5 matches CFB spread→moneyline conversion (a
7-point favorite ≈ 70%, 14-point ≈ 85%); HFA = 2.3 points; band treated as 1 SD. The
shared shock δ is the engine's most consequential choice — being 2 points wrong on a team
means being wrong every week, which fattens season-win tails exactly the way real seasons
behave. FCS opponents enter at their tiered rating scaled to the active lens (×0.75
calibrated / ×s* market-matched) with their wide bands. The same hardcoded GH nodes ship
to the browser artifact so JS matches Python to 1e-9.

**Edges, EV, and what gets bet.** For each posted total: P(side) under each lens, minus
the de-vigged market probability (edge columns) and minus the breakeven at the actual
odds (the bettable edge). **Conviction = min(calibrated edge, market-matched edge)** at
the best posted price; ✓✓ requires ≥ +4% on both. Because edges are monotone in the
dispersion factor, clearing both endpoints certifies the edge under every dispersion
hypothesis in between — the board's defense against betting one macro opinion 50 times.
Sizing conventions: entries 0.50–0.70u scaled to conviction and juice; season cap
1.1–1.2u per team across regular + conference markets; adds require the bar at the
*current* price plus provenance review. Every bet lives in `pipeline/bet_tracker.py`'s
SEED list (source of truth), re-priced by the tracker against the current payload.

## 9. What we believe our edge is — and our assumptions

Stated plainly, in order of how much we lean on each:

1. **Attention asymmetry.** Books and the public price 20 marquee teams with real
   effort; the G5 and the bottom of the P4 get formula-plus-vibes. Our unit-level roster
   work is deepest exactly where the market's is shallowest. It is no accident the book
   is heavy on UConn/Tulsa/BGSU/Nevada-class positions.
2. **Portal-era information decay.** Rosters now turn over faster than public priors
   update. A system that regrades every two-deep from tape each July should beat
   numbers anchored to last season's brand. (This is also our biggest exposure: our
   transfer machinery being wrong would correlate across the whole G5-over cluster.)
3. **Dispersion mispricing, isolated but not bet.** The market prices totals as if
   strength spreads ~15% wider than reality. We do NOT bet that macro view naked — the
   min-lens rule means we only bet where the edge survives even under the market's own
   dispersion. The macro tilt is a tailwind we decline to count.
4. **Microstructure.** Five books disagree; lines go stale; unders are inferred off
   juiced overs; off-market lines (DK's Florida 6.5 vs the field's 7.5) appear. Price
   shopping against a 30-cent convention adds real percentage points.
5. **Discipline as meta-edge.** Pre-registered studies, blind grading against the
   anchor, provenance ledgers ("how much of this edge came from our own newest pen?"),
   the dual-lens bar, and known-failure-mode vetoes (service academies, new-HC
   uncertainty priced into bands). None of it predicts a game; all of it prevents the
   classic ways a model bettor donates.

Assumptions we knowingly make: PFF grades carry real, transferable signal (validated at
slope ~0.40 with heavy shrinkage — modest but real); the six-system consensus is
approximately fair-scaled (SD ~13); July estimates need ×0.75 before becoming
probabilities (validated on 663 team-seasons); posted totals are exhaustible via five
books; and the dossier arm's human judgment is roughly unbiased — **this last one is
untested** (Study 3 territory) and is candidly the most plausible large error source
left in the system.

## 10. Tested and NOT implemented (the graveyard — each with receipts)

- Flat conference offsets as transfer forecasts: worse than naive carry-forward
  (MAE 9.93 vs 8.92; fitted translation 7.15). Replaced by shrinkage + small jumps.
- Portal star ratings as signal on movers with tape: ΔR² < 0.01 (S1-C/D). Dead.
- HS composites past year one: dead (S2b holds year one only).
- Origin-roster brand ("Georgia backup") for thin-tape movers: ΔR² 0.0001 (S1-E). Dead.
- Career pooling (recency-decayed multi-season evidence): right direction, +0.1–0.8%
  everywhere, under every registered bar (S2-C). 2027 retry with fitted decay.
- Class-year aging term (the "year-2 jump"): mean improvement is uniform (+1.3–1.9,
  cancels in the field rescale); the class-specific gradient flips sign across seasons
  (Study 2). Not shipped; lives qualitatively in dossiers.
- Hampered-season look-through (injured-year tape discount): tested worse than just
  using the small tape (S2-D-B).
- |dg|>4 adjudication trigger: would have "corrected" 61% of the field. Reset to 1 SD.
- Retention-curve fixes (Study 4 family): spline (S4-B fail), per-group k regrid (S4-C
  fail), per-group k′+plateau (4b: all three bars fail), flat +0.059 patch (never
  registered; known-wrong at high volume). Diagnosis validated, no cure validated;
  doctrine shipped instead; 4c pre-registered for 2027 (pooled form, fifth fold).
- Spread/game-line betting: CFBD lines flow works today, but our spreads show
  systematic tail bias vs posted numbers (the mm stretch was calibrated on totals, not
  spreads). Gated behind a pre-registered spread-calibration study. No spread bets.

## 11. Open areas that could merit research

- **Dossier-arm calibration (Study 3: continuity × prior-stability).** The formula arm's
  biases are now measured; the human arm's are not. Highest-value open question.
- **Study 4c** (registered, frozen form): pooled retention correction on five folds
  including 2025→26. Runs at the 2027 build.
- **Program×unit development residuals** ("Iowa OL"): does a program's unit as-played
  grade persistently beat its talent inputs? Registered 2027 candidate; feasible on the
  existing spine.
- **Rank-based dg** in adjudication (kills ceiling-squeeze/offset-axis artifacts
  structurally) and a **QB rushing-value term** (formula is passing-facet only;
  dual-threat QBs enter via dossier + DUALQB screen today).
- **Retention selection** (who returns is informative) and aging retried with the fifth
  fold of pairs.
- **Spread calibration study** → would unlock game lines, GOTY positions, and a daily
  CFBD puller (plumbing already proven).
- **In-season update policy**: when September results arrive, what updates (grades?
  anchor? band decay toward the 0.983 December slope?) and what stays frozen. Undesigned.
- **FCS bands/ratings** refinement if any FCS-adjacent total ever matters at the margin.

## 12. Modifying the rig safely — the loops, the freezes, the rules

**Rebuild chain after any grade change** (each step deterministic):

```
1. edit data/research/adjudication_v2.csv   (append; never rewrite history)
2. git checkout 36fcfed -- 'snapshots/*/grades.json'    # restore v1 baseline
3. python3 pipeline/regen_grades_v2.py                  # replay full log
4. python3 pipeline/grades_check.py <Team_Dir>          # per-team gate (if hand-editing)
5. python3 pipeline/build_board.py                      # calibration board (display source)
6. python3 pipeline/final_pass.py                       # refit conversion + boards
7. python3 pipeline/win_totals_compute.py               # payload (refits s* too)
8. python3 pipeline/build_win_totals_artifact.py        # the HTML
9. python3 pipeline/bet_tracker.py                      # re-price the book
```

**Frozen without owner sign-off:** K=0.35, CAP=±6, SIGMA=6.0, band multipliers, the
calibrated 0.75, the anchor run file, k/caps/posmeans/jumps/FR priors, HFA 2.3,
σ_game 13.5. **Auto-refit each build:** the OLS conversion weights, the recenter, s*.
**Governance:** anything touching fitted constants goes through a pre-registration in
docs/research/ (bars committed before results; failures reported and kept); production
changes need explicit owner sign-off; live grades change mid-season only via a
sign-offed targeted audit. Secrets (CFBD key, git credentials) live in
/root/.cfb_secrets/ and never in the repo. Every session ends pushed, with provenance
trailers on commits.

**Where the numbers you see in the UI come from:** `outputs/win_totals_payload.json`
(teams, schedules, FCS, market, per-team derivation blocks) → embedded in
`outputs/win_totals_2026.html`; the browser re-derives all distributions with the same
GH nodes, so hand-editing a rating in the UI reprices live and matches Python to 1e-9.
