# Single-game program — design memo (2026-07-31)

Owner commissioned two camps: (1) Week 0/1/GOTY lines bettable now; (2) an
in-season rating-update capability. Standing rule: "isn't worth it" is an
acceptable output. Camp 1 was gated by S14 (registered first, then run).

## Camp 1 verdict: FLUSHED (S14 A+B FAIL)

Preseason-consensus disagreement with posted spreads has covered 46–48% every
season since 2021 (2021's 60% = COVID-prior dislocation, since arbitraged).
The F1 mechanism is a soft-market phenomenon (win totals: stale, low-limit,
annual settle) and does not transfer to the sharpest market in the sport. No
side qualifies on "our board vs the line"; no threshold rescues it (S14-D).
Our idiosyncratic residual on TOP of consensus remains untested at game level
— S8c (December) is the only door back in, via a 2027 registered retry.
Meanwhile: pipeline/price_game.py prices any 2026 matchup (cal/raw/anchor
lenses) for context and paper-tracking; 53 posted 2026 spreads captured
(data/cfbd/lines/lines_2026_probe_2026-07-31.json).

## Camp 2 architecture: three layers, mirroring the rig

**Layer 1 — weekly consensus anchor (formulaic, free).** Market-implied
ratings: solve least-squares team ratings from each week's closing spreads
(ridge-anchored to prior week; HFA fit or fixed 2.3). S14-C licenses this:
week-1 closes carry R² 0.94 to preseason consensus and beat consensus on
accuracy EVERY week thereafter — the market is the best free weekly ratings
service in existence, available from CFBD Sunday morning. This kills two owner
pain points: no weekly SP+ scraping, and no consensus-timing gap (bet-day
anchor = last night's closes, not week-old SP+).

**Layer 2 — performance update (formulaic).** Opponent/site-adjusted per-game
performance residual (CFBD PPA/success-rate based, garbage-time filtered) vs
the anchor's pregame expectation, applied with a declining gain K_w. S14-C
sets the speed prior: the market itself drifts RMSE ~4→7 pts off the preseason
anchor by weeks 4–5 — so early-season K must allow 5–10 pt cumulative moves
(owner's prior confirmed quantitatively). K form frozen by registration before
any backtest (S16 below); capped per-week and per-season like the K-shrink.

**Layer 3 — dossier adjudication (qualitative, mine).** Sunday card per
candidate action: QB/injury/news verification, motivational/spot notes.
Spots are MECHANICAL, not vibes: rest differential, consecutive road weeks,
travel distance, altitude, kick window — computable from schedule data;
whether the market misprices any of them is an empirical question (proposed
S15 audit on the 2021–25 lines panel BEFORE any spot term earns points).

## Where the money output points (CORRECTED 2026-08-01, owner)

**STRUCK: season-totals repricing.** Owner correction: in-season season-total
markets are very illiquid with punishing holds — not a tradeable channel. The
original memo leaned on it as the licensed money output; that pillar is gone,
and with it the main argument for Path-A ("our belief evolves") as the spine.
The in-season program is now STRICTLY single games, and the honest edge theses
are only:

- **T1 — situational/overreaction terms (owner's Path B; backtestable = S16).**
  The market's own numbers as the base; registered candidate situations where
  openers (or closes) systematically misprice. Pre-committed candidate list to
  cage multiplicity — see S16 scope below.
- **T2 — the full weekly rig, paper-traded (REDEFINED 2026-08-01, owner).**
  Owner's vision, now the program's center: replicate the sharp workflow —
  our own ratings for every team, updated every week (mechanical arm
  adjudicated against qualitative research, mirroring the preseason rig), with
  the edge claim being "we rate teams better than the openers on a rolling
  basis." Not backtestable (the qualitative arm has no history); the 2026
  paper year IS the test. Depth-grade knowledge at news time (graded backups
  vs the market's guess) is one component inside it, not the whole thesis.
  Paper bets frozen at Sunday post with REASON CODES (injury/depth, perf-vs-
  market divergence, spot, other) so December attribution shows WHICH arm won.
  Bars: ≥55% on n≥50 or demonstrable CLV → 2027 money test; else dead.
  Pre-stated edge-location prediction (falsifiable in December): if real, wins
  cluster in news-timing weeks, depth-chart disruptions, low-attention G5
  games, and weeks 1–5 — not spread uniformly.
- The weekly rating chain itself claims NO edge (S14: 48.4% even at openers).
  It survives as infrastructure: fair-number baseline that T2 deltas apply to,
  feature source for T1, and 2027 preseason-build inputs.

## Backtest plan (S16, to be registered before running)

Panel: 2021–25 lines (opener + close both present ~55–60% of rows). Candidate
situational terms, ALL registered with bars before any outcome is computed,
each scored vs OPENER (the bet point) and vs CLOSE (the alpha test), LOYO:
(i) preseason-prior retention mid-season (market overweights recent results?
— the S14-D wk4–8 report cells are DISCLOSED AS SEEN and non-monotone; bars
set fresh); (ii) shock-blowout response, TWO-SIDED (owner hypothesizes
UNDER-penalization of early-season favorites who get destroyed; my prior was
overreaction — sign not assumed, claim at |t|≥2 + LOYO sign stability);
(iii) post-upset-loss bounce; (iv) rest/travel/spot set (bye edge, consecutive
road, short week, altitude, body-clock); (v) opener→close drift structure (do
Sunday numbers systematically migrate in predictable directions?); (vi) OWNER
CANDIDATE: accumulative efficiency-vs-market divergence — cumulative
opponent-adjusted YPP/PPA margin outrunning the team's market-implied rating
change over a multi-week window (the "five straight weeks of a big YPP edge
against good opponents and the market hasn't moved" case) — does the gap
predict ATS forward? Sobriety anchor registered up front: S14-B showed openers
already price preseason consensus; the null is that books are fine and every
cell is ~50%.

Design decisions recorded (owner may veto): the weekly MECHANICAL arm is
MARKET-BLIND (preseason prior + performance data only) — the market-implied
chain runs in parallel as fair-number reference, S16 feature source, and
final shrink target (the weekly analog of the K-shrink/blinding philosophy in
the preseason rig; keeps edge attribution clean). Weekly qualitative layer is
TRIAGE-based, not exhaustive: full-field availability sweep + deep reads only
on trigger (mechanical move > threshold, news flag, paper-card candidate) —
exhaustive weekly dossiers for 136 teams are not a real labor option.

## Data plan

CFBD only for v1 (games, lines, PPA — Sunday-updated, $0 marginal). PFF weekly
snapshots: NOT required for v1; optional Sunday ritual starting week 1 if the
owner wants the 2027 evaluation enabled (cost = his sub + ~10 min/wk; decision
his, no urgency). Weekly SP+: not needed (Layer 1 substitute). Injury/news:
researcher layer (me), owner may contribute preferred sources.

## Worth-it criteria (December review; bar RAISED by the 08-01 correction)

In-season build survives to 2027 iff: ≥1 S16 situational term passes its
registered bars (esp. vs close), OR the T2 paper pilot clears ≥55%/n≥50 or
positive CLV. If both come back empty, camp 2 was ratings maintenance for the
2027 build and nothing else — the owner accepts that outcome in advance, and
the build effort is sized accordingly (lean v1, no speculative polish).
