# Pre-registration — Study 14: preseason consensus vs the early-season spread market (2026-07-31)

Owner-commissioned, opening the single-game workstream. This is the GATING test —
the F1 analog for sides: F1 (validated, totals) says consensus-vs-market
disagreement is exploitable on season win totals; S14 asks whether the same
mechanism pays on early-season POINT SPREADS, where the market is sharpest.
Owner's standing instruction: "this isn't worth it" is an acceptable verdict.

**Peek disclosure:** CFBD lines 2021–25 were pulled today and inspected for
COVERAGE ONLY (game counts, providers, spreadOpen availability, 2026 postings).
No ATS outcome, margin, or disagreement statistic has been computed. Prior
knowledge disclosed: early-season power-rating-vs-spread angles are a known
public genre (SP+ ATS results have been publicized in past seasons); bars are
set at claim-worthy levels accordingly, and LOYO stability is required.

## Data (frozen)

data/cfbd/lines/lines_{2021..2025}.json (regular season). FBS-vs-FBS only; both
teams present in data/backtest/sp_preseason/SP+_{y}_preseason.csv (norm join,
uconn alias); games with recorded scores only; |spread| > 60 discarded as feed
error. Market CLOSE = median provider `spread`; market OPEN = median `spreadOpen`
where present (~55–60% of rows; providers shift across years — median absorbs).
Neutral-site flag joined from games_{y}_regular.json by game id.

Consensus-implied home margin M = (SP_home − SP_away) + 2.3·site (rig HFA; site
= 0 neutral, else +2.3 home). Disagreement D = M + spread_close (market home
margin is −spread). D > 0 → consensus likes HOME against the number. ATS win =
consensus side covers vs the evaluated line; pushes excluded from denominators.

## Legs and bars

- **S14-A (PRIMARY, the gate):** weeks 0–3, |D| ≥ 3, vs CLOSING spread,
  2021–25 pooled. PASS iff pooled cover ≥ 55.0% AND per-year cover ≥ 52.4% in
  ≥ 4 of 5 seasons. (Break-even 52.38% at −110; expected n ≈ 400–600.)
- **S14-B (openers, the practical target):** same slice vs OPENING spread where
  posted. Secondary PASS at the same bars. Interpretation note registered now:
  B-pass-without-A-pass = we are picking off soft posts (still money, tracked by
  CLV); A-pass = the mechanism itself survives to the close.
- **S14-C (decay curve, report-only, feeds the in-season design):** by week
  0–14: (i) slope/R² of market home margin on M; (ii) RMSE(M vs market margin);
  (iii) competitive accuracy — MAE(actual margin | market) vs MAE(actual | M).
  Answers: when does preseason information die, and how big is the market's own
  early-season self-correction (owner's "5–10 pts early is not crazy" prior).
- **S14-D (shape, report-only):** cover% by |D| bucket (1–3, 3–5, 5–8, 8+) ×
  week bucket (0–1, 2–3, 4–8, 9+), pooled, vs close — does the top-decile
  threshold pattern from the totals work rhyme on sides?

## Decision rules (registered)

- A PASS → camp-1 doctrine licensed: consensus-vs-market disagreement ≥ the
  S14-D-supported threshold qualifies Week 0/1/GOTY sides; our roster residual
  (R_pre) enters as tie-breaker/booster only (its own game-level test is S8c in
  December). The 53 already-posted 2026 spreads get priced under this doctrine.
- A FAIL, B PASS → openers-only program, reduced sizing, mandatory CLV logging;
  no representation that the edge is fundamental.
- Both FAIL → sides at market prices are DROPPED from the 2026 program (totals
  remain the book); in-season work proceeds only as a ratings-maintenance and
  totals-repricing exercise unless S14-C shows exploitable anchor drift.

## Limitations (registered)

2021 preseason carries COVID inputs (LOYO guards). Provider mix shifts across
years; median-of-available is not a single book's executable number. spreadOpen
missing for ~40% of rows (B is the available-subset answer). No moneyline/juice
modeling — flat −110 assumed. SP+ preseason is the consensus proxy throughout
(same convention as S6–S13); our own 2026 ratings are untested at game level
until S8c/live tracking.
