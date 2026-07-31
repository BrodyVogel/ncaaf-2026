# In-season mechanical anchor — design (2026-08-01)

Owner's key question: what is the best mechanical anchor for weekly rating
updates? Constraint set: qualitative layer does the edge work; the anchor must
be as good as our preseason anchors; injuries/availability must not bias model
fitting or evaluation. This doc fixes the architecture and the research plan
BEFORE any fitting (honesty regime: pre-committed loss, folds, and model menu).

## The structural fact the design starts from

Preseason, we stood on consensus's shoulders: SP+ IS the anchor and our work
is the residual. In-season there is no usable consensus at bet time (weekly
SP+ = scraping we've declined; market-implied = rejected as an INPUT for
attribution reasons). So the in-season anchor must be home-built: we are
replacing the in-season half of Connelly's machine with our own. That is why
this project is preseason-sized. The compensations: game data is free, deep
(10+ seasons), and the fitting loss needs no market data at all.

## Architecture: opponent-linked state-space filter (one model, not pieces)

State: per-team off and def strength on the SP+-scale split we already carry
(final_pass implied_off/implied_def = the week-0 state — the preseason rig's
output IS the prior; full continuity with existing machinery, conversion and
all lenses keep working). Optional v2: pass/rush sub-channels.

Observation, per game, per side: opponent-UNadjusted efficiency composite
(CFBD advanced box: PPA/play, success rate, explosiveness, turnover margin,
ST field-position value, plus scoring margin at low weight; garbage-time
filtered where flags allow). Composite weights fit on history (below).

Observation MODEL: y_game ≈ (off_i − def_j) + site + ε. Opponent adjustment
is therefore AUTOMATIC and recursive — each game is scored against the
opponent's CURRENT posterior, which embeds their full schedule to date. This
answers "how does the opponent/schedule factor in": it's not a pre-adjustment
of the metric; it's the linkage structure of the solve.

Weekly operation: not filter-forward-only — RE-SMOOTH the season to date each
Sunday (re-run the filter from week 1 with current estimates; ~5–14 cheap
ridge solves). This is the mechanical version of "that Week 1 win over X
looks better now": early games are re-valued all season as opponents clarify.

Gain schedule ("heavy early, light late — exact numbers"): NOT hand-set. The
gain falls out of three variance components — preseason prior width σ_prior,
weekly process noise σ_proc (teams genuinely change), observation noise σ_obs
(one game's information content) — all ESTIMATED on the historical panel.
Ballpark expectation (to be replaced by fits): σ_prior ≈ 5–6 (portal era),
σ_obs ≈ 10–12 on rating scale → per-game gain ≈ 0.2 early; effective weight
on preseason ≈ 40–50% by week 4, ~20% by week 8, floor >0 all year via
σ_proc (November games still move ratings 1–2 pts). Cross-check: the fitted
trajectory should resemble S14-C's market drift curve (RMSE 4→7 by wk 4–5).

Conditioning (owner's list) enters as VARIANCE multipliers, not mean terms:
- Competition level: G5 σ_prior larger (less preseason info); FCS opponents
  priced from the FCS table with inflated σ_obs; cross-level games flagged.
- New staff: σ_prior and early-week σ_proc multipliers (scheme install =
  true strength moving). NO mean term (S12: coach mean effects die).
- Roster continuity: rp modulates σ_prior (low-continuity = wider prior =
  faster early updates). Variance role, not the S13 mean role.
Each multiplier ships ONLY if it improves the pre-committed held-out loss by
a pre-set margin (bars in the build registration).

## The injury-contamination rule (owner's concern — two-sided fix)

Availability information contaminates BOTH directions: (i) evaluating vs the
market, games where books knew an absence are unfair market "wins"; (ii)
fitting, a backup-QB game contaminates the OBSERVATION (filter wrongly
downgrades the usual-team's θ). One mechanism fixes both:

- **QB-change flag, reconstructable historically:** the de facto starter is
  identifiable from per-game passing attempts; flag games where the starter
  differs from the team's season-modal QB. Flagged games are DOWN-WEIGHTED in
  fitting (their performance is less informative about usual-θ) and EXCLUDED
  from any model-vs-market diagnostic.
- **Late-move flag:** |open→close| ≥ 2.5 pts = the market learned something
  intraweek (injury proxy, feed-free). Excluded from model-vs-market
  diagnostics; reported both cuts.
- Non-QB absences are historically unreconstructable → accepted as
  irreducible σ_obs (inflates fitted obs noise slightly → conservative gains
  — benign direction). Live, the qualitative layer patches availability
  BEFORE the number ships, so the live product doesn't carry this handicap.
- **The fitting loss NEVER touches the market.** Model selection = pure
  forecasting: out-of-sample future-game margin/efficiency prediction, LOYO.
  Lines appear only in post-freeze diagnostics and the paper year. (This is
  also the answer to "unfair market wins" — the market isn't the judge of
  the mechanical arm at all; the future is.)

## Do unit/player grades matter?

v1: no player-level inputs — team off/def efficiency carries the mechanical
load; our preseason unit grades live in the PRIOR (they built it). The state
is STRUCTURED so unit channels can slot in later (pass/rush split v2; PFF
weekly snapshots = optional 2027 evaluation, owner's earlier call stands).
Player grades re-enter through the qualitative layer's availability deltas
(graded two-deeps → QB-out arithmetic, γ multiplier calibrated live).

## Build plan (phases, each gated)

- **P0 data:** extend games + advanced boxes back to ~2016 (~10 seasons,
  CFBD, free); QB-starter reconstruction; garbage-time convention; FCS table
  coverage check. One session.
- **P1 baseline (the registered build):** off/def filter, global variance
  components, composite weights. Pre-committed loss: LOYO out-of-sample
  next-game margin MAE (+ efficiency loss reported). Benchmarks it must beat:
  (a) frozen-preseason-all-year, (b) margin-only Elo at fitted K. Diagnostic
  (report-only, injury-flag-segmented): gap to closing spreads by week —
  expectation ~2.5–3.5 pts RMSE late-season if we've matched public in-season
  systems. Freeze v1 constants on pass. One–two sessions.
- **P2 conditioning:** level/newHC/rp variance multipliers, pass/rush
  channels, ST term — each vs pre-set improvement bars; drop what fails. One
  session.
- **P3 rehearsal:** walk-forward replay of 2025 as-if-live (Sunday by
  Sunday, no hindsight), producing the change-log/paper-card artifacts the
  live year will produce; final plumbing + adjudication interface. One session.
- **P4 live:** Sundays, in-season; paper card per SINGLE_GAME_PROGRAM T2.

S16's situational-term slot is SHELVED (owner: expository examples, not
expected edge); the S16 registration slot is reassigned to the P1 build
(loss, folds, benchmarks, freeze rules registered before fitting).

## What "as good as our preseason anchors" means, measurably

The preseason anchor's virtue is calibrated unbiasedness — it lets the
dossier spend attention only on real information. Acceptance for the weekly
anchor, same spirit: (i) beats frozen-preseason by week 3 and never loses to
it after; (ii) tracks within ~3 pts RMSE of closes by mid-season on the
clean (unflagged) segment; (iii) no systematic residual vs level/pace/style
in the P1 diagnostics. If P1 can't clear (i)–(ii), the honest conclusion is
that a home-built anchor isn't good enough to carry a qualitative layer, and
the program stops before the paper year burns a season — stated in advance.
