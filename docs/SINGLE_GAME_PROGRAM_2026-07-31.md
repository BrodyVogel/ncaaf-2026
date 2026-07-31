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

## Where the money output points (licensed vs pilot)

- **LICENSED: season-totals repricing.** The validated soft market. Weekly
  rating set → refreshed win distributions → (i) manage/hedge the held book,
  (ii) qualify mid-season totals adds under the committed screen rules, (iii)
  the rp receiving term's legitimate live home (owner-waived for in-season).
- **PILOT (paper only): Sunday openers on sides.** Updater + dossier card
  produces a logged, frozen-at-post paper bet each Sunday it finds one.
  Scored in December: ≥55% on n≥50 (or demonstrable CLV vs close) → register
  a 2027 money test; else sides stay dead. No dollars in 2026.

## Backtest plan (S16, to be registered before running)

Historical replay on the pulled 2021–25 lines: build weekly market-implied
ratings, apply the frozen K_w performance rule, test (a) next-week spread
prediction vs anchor-alone (does the update layer add accuracy the market
hasn't?), (b) simulated totals repricing value on SBD boards. LOYO; owner's
in-sample concern stands — mitigations: rule frozen at registration, gain form
chosen from S14-C (already published), leave-2025-out headline. Verdict rules
registered then, same honesty regime as S1–S14.

## Data plan

CFBD only for v1 (games, lines, PPA — Sunday-updated, $0 marginal). PFF weekly
snapshots: NOT required for v1; optional Sunday ritual starting week 1 if the
owner wants the 2027 evaluation enabled (cost = his sub + ~10 min/wk; decision
his, no urgency). Weekly SP+: not needed (Layer 1 substitute). Injury/news:
researcher layer (me), owner may contribute preferred sources.

## Worth-it criteria (December review)

In-season build survives to 2027 iff: totals repricing produced ≥3 qualified
adds or one materially-improved exit, OR the paper side pilot clears its bar,
OR S16 shows the update layer beats anchor-alone out-of-fold. Otherwise camp 2
reduces to ratings maintenance for the 2027 preseason build — also a win.
