# Media-days integration — impact report (2026-07-21)

Steps 4–6 of the owner-approved plan, closing out the first batch (ACC, Big 12, Mountain
West, Sun Belt). Inputs to this rebuild: **2 unit regrades** (Hawai'i LB 12L→14M, NIU QB
18L→20L), **1 schedule fix** (NDSU–SJSU flagged non-conference), and the **devig fix**
applied at all three sites (`_market_block`, `compute_market_stretch`, artifact JS).
Everything else in the four digests was confirmation — see the four triage memos.

## Field impact: surgical

One rating mover: **NIU −17.01 → −16.90 (+0.11)**. One band mover: **Hawai'i ±6.72 →
±6.54** (L-count 4→3). Every other team's rating shifted ≤0.02 (OLS-refit noise from
re-estimating conversion weights on the edited field). Market-matched stretch factor:
1.1480 → **1.1475** (the devig fix barely moved the fit). Post-build asserts passed:
MW conference census {8: 10}, ACC {8: 5, 9: 12}, tracker regenerated all 14 bets.

## Your 14 open bets — before → after

| Bet | Model P | % edge | EV/$1 |
|---|---|---|---|
| UConn o5.5 | 67.8 → 67.8% | +19.8 → +19.9% | +0.323 → +0.324 |
| Tulsa o5.5 | 66.0 → 66.0% | +18.5 → +18.5% | +0.319 → +0.319 |
| Oregon State o3.5 | 75.8 → 75.8% | +18.9 → +18.9% | +0.264 → +0.264 |
| Bowling Green o4.5 | 77.2 → 77.2% | +18.1 → +18.1% | +0.254 → +0.254 |
| Liberty u8.5 | 70.8 → 70.8% | +16.5 → +16.5% | +0.196 → +0.196 |
| Arizona State u6.5 | 59.1 → 59.1% | +10.8 → +10.8% | +0.182 → +0.181 |
| Kennesaw State o6.5 | 54.6 → 54.6% | +8.5 → +8.5% | +0.201 → +0.201 |
| Illinois u7.5 | 71.9 → 71.9% | +13.3 → +13.3% | +0.168 → +0.168 |
| West Virginia u5.5 | 50.3 → 50.3% | +8.5 → +8.5% | +0.167 → +0.167 |
| East Carolina o7.5 | 59.6 → 59.5% | +11.5 → +11.5% | +0.191 → +0.191 |
| **Hawai'i u7.5** | **64.2 → 64.4%** | **+9.9 → +10.1%** | **+0.177 → +0.181** |
| Florida u4.5 (conf) | 59.3 → 59.2% | +9.0 → +8.9% | +0.131 → +0.130 |
| UCF o3.5 (conf) | 60.9 → 60.9% | +10.0 → +10.0% | +0.138 → +0.138 |
| Pittsburgh u5.5 (conf) | 64.5 → 64.5% | +8.5 → +8.5% | +0.120 → +0.119 |

## The honest correction: Hawai'i moved *toward* us, not against us

I warned three times that the Otis resolution would hurt the under. It didn't, and the
decomposition is worth recording:

1. **The rating channel dampened to zero.** A +2 on one defensive unit passes through the
   OLS unit weight (~0.06 pts/grade-pt), then K=0.35 residual weighting, then conference
   demeaning — net ≈ +0.04 rating points, invisible at 2 decimals. Hawai'i's rating is
   **unchanged (−6.76)**.
2. **The band channel helps the side we hold.** L→M tightened the band ±6.72→±6.54.
   A tighter distribution concentrates mass near the mean — and Hawai'i's mean (E[w]≈6.9)
   is *below* 7.5, so the under (the 64% side) gains. My warning implicitly assumed the
   rating would rise enough to dominate; it never moved.
3. **The NIU offset also helps**: NIU (+0.11) is on Hawai'i's schedule.

Net: **+0.2pp of win probability and +0.004 EV in our favor.** Lesson logged for future
integrations: single-unit grade deltas of ±2 are sub-rounding on ratings; the confidence/
band channel dominates, and its direction depends on which side of 50% you hold.

## Devig fix effects

The invalid median-of-American-odds construction (garbage when books straddle ±100) is
replaced at all three sites by per-book de-vig + averaged fair probabilities (30-cent
convention). The conference-market artifact class is **eliminated** — zero conference
blocks now show |edge| > 25% (the old UNC-class +36% headline edges are gone). Regular-
season markets are essentially unchanged (5 books, straddles rare, and per-book EV at
your actual price was never affected).

## Board / unplaced candidates

No changes. The conviction-sorted board's top tier (UMass, UConn, Tulsa, Bowling Green,
Oregon State, Illinois, Texas…) is identical before/after; no bet enters or leaves any
top-10 list on these deltas. **Considered and not changed:** all 57 team sections across
the four digests, per the triage memos (B12: 0 changes; ACC: 0; SBC: 0; MWC: 2 + fix).

## Caveats & queue

- Any NEW bet: our stored prices are the July-12 snapshot and media-day info is fully
  public — re-check live lines before acting.
- Queued: ACC official poll re-sweep (July 28); fall-camp QB resolutions (13 open rooms);
  Dickens eligibility confirmation; watch items W1–W5 (B12), MWC W1–W3, A1–A2 (ACC),
  S1–S4 (SBC).
