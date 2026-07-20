# Independent audit of the post-grading pipeline (2026-07-20, Fable)

Owner request: check everything since team-by-team grading finished — the simulation engine,
the artifact, the final assembly/de-meaning, the bias fixes, and the "market is inefficient"
conclusion. Everything below was **re-derived independently** (own implementations, own joins),
not re-read from Opus's docs.

## Verdict at a glance

| Area | Verdict |
|---|---|
| Engine math (probit, Poisson-Binomial DP, Gauss-Hermite, odds) | **Correct.** DP exact vs brute force (9e-17); GH matches adaptive quadrature (2e-10); phi matches scipy to machine eps; odds round-trip; all 785 market lines are half-points (no push handling needed). |
| JS port / artifact parity | **Correct.** All 138 teams, max P(k) deviation 1.4e-16; Cephes ndtr max err 1.1e-16 on [-12,12]. |
| final_pass assembly (OLS, un-shrink, orthogonalization, recenter, overrides) | **Correct.** Reimplemented from source; all 138 ASSEMBLY rows match; recenter mean exactly 0 pre-override; class term 0; 0 teams capped; locked snapshot == live. |
| Compression fix | **Correct and as claimed.** SD 12.54→13.19, Spearman 0.999, extremes moved outward linearly; edge~line R² 0.322→0.136 reproduces exactly. |
| Schedule data | **BUG (material), fixed.** All 8 Pac-12 teams were missing their Week-13 flex game (11 games vs the market's 12). See §1. |
| Consensus-line methodology | **Bug (minor), fixed.** 11 team-markets headlined a phantom median line no book posts. See §2. |
| "Market over-disperses" conclusion | **Confirmed — and understated.** But the same backtest shows our own engine is preseason-overconfident too. See §3. |
| Market-matched third set | Sound construction, correctly implemented (slope exactly 0 at s*; overrides propagate). s* recomputed 1.177→**1.148** after the fixes. |
| Manual overrides | Reasonable calls, correctly applied post-recenter; derivation pages now disclose them. NDSU's fair-priced +2.0 keeps it off the top of the board — right instinct. |

## §1. The material find: the Pac-12's missing 12th game

CFBD's 2026 schedule pull contains no entry for the Pac-12's new **Week-13 flex game**
(the conference assigns the pairing as late as Nov 22, so feeds carried nothing). Result:
every Pac-12 team was simulated over **11 games against market totals that price 12**.
That deflated each team's E[wins] by P(win the flex game) — +0.30 to +0.70 wins — and
manufactured phantom Under edges across the whole conference:

| team | old edge (11g, median line) | corrected (12g, posted line) |
|---|---|---|
| Boise State | −21.6% (under) | **+8.3% over** @ 7.5 |
| Washington State | −18.4% (under) | +2.5% over @ 4.5 |
| Texas State | −19.0% (under) | +7.1% over @ 5.5 |
| San Diego State | −29.5% (under) | +5.2% over @ 6.5 |
| Utah State / Fresno / Oregon State | small unders | flip to overs (+2.9% / +8.4% / +16.5%) |
| Colorado State | +8.2% over | +13.9% over @ 3.5 |

The earlier conclusion "the market over-hypes the rebuilt Pac-12; Boise/SDSU/Wazzu unders
are real edges" was **substantially this artifact**. (Conference totals used only the 7
conference games and were always correct. The team *ratings* are untouched — this was purely
a schedule/totals issue.) Also verified while here: San José State's 13 games are legit
(week-0 opener + at-Hawai'i exemption); Hawai'i's official 2026 slate is 12; every other team
is at 12; home/away reciprocity is perfect across all 138 schedules; every FCS opponent
carries a real rating from the FCS file (the nine at −40.0 are mid-tier by construction, not
join failures); every board team joins a market line.

**Fix shipped:** `data/pac12_flex_2026.csv` (projected pairings from the Feb 2026 release:
Boise@USU, OSU@WSU, SDSU@Fresno, TxSt@CSU) appended by the loader as non-conference Week-13
games, tagged **flex (proj.)** in the UI with a footnote, documented in Methodology. When the
conference finalizes pairings (by Nov 22) the CSV takes 30 seconds to update.

## §2. Phantom consensus lines (minor, fixed)

Where books split a full game (7.5 vs 8.5), the "median line" landed on 8.0 — a line nobody
posts — and de-vig odds were pooled across *different* lines. 11 team-markets were affected
(5 of them Pac-12, compounding §1 in the same direction). The headline consensus edge now uses
the **posted line nearest the median** (tie → the line more books post), with odds pooled only
at that line. Per-book best-bet EVs were always computed at real lines and are unchanged.

## §3. The dispersion question — who's right, us or the market?

Re-ran the game-level calibration from scratch: SP+ preseason ratings, 2021–2025, FBS-vs-FBS
regular season, n=3,730 games (own joins). Fit P(home win)=Φ(a + b·diff/13.5 + h·site/13.5):

- **Preseason ratings: b = 0.624** (95% CI 0.575–0.673; per-season 0.52–0.75, all « 1).
  A preseason "93% favorite" wins **81.5%**. Favorites at |pred margin| 17–25: predicted
  93.2%, actual 81.5%.
- **Final (retrospective) ratings: b = 0.983 ≈ 1**, margin residual SD **13.58 ≈ σ_game 13.5**.
  This validates the pipeline, the probit structure, and the σ_game=13.5 constant *for true
  ratings* — and isolates the attenuation as purely a preseason-information effect.
- Decomposition: margin slope 0.80 (preseason point estimates mean-revert ×0.80) with residual
  SD 16.9 (≈ σ 13.5 + our band 6–7 uncertainty). Staleness deepens it through the season
  (weeks 1–4 b=0.71 → weeks 9+ b=0.57) — and win totals settle on the *whole* season.

**So: (a) Opus's market conclusion is right, and stronger than he stated.** The market prices
totals at ~1.15× our dispersion; game outcomes calibrate at ~0.75× — the market runs ~1.5× the
calibrated preseason spread. The monotonic fade-favorites/back-dogs gradient is real edge, not
model error. The 2025 totals themselves agree directionally (totals ≤5 went over 65.5% of the
time, +1.16 wins vs the line; totals ≥8 went over 48%). The doc's exact 2025 tier numbers
(+0.34/−0.21) did not reproduce under my join, but the direction holds.

**(b) But our own engine is also preseason-overconfident.** The doc noticed the sub-1.0
optimum ("×0.8 beats ×1.0") and dismissed it as a footnote. It isn't: under the engine's own
structure the optimum is **shrink ≈ 0.75 with band 6, σ 13.5** (log-loss 0.5768 vs 0.5868
as-is). Practical meaning: our displayed probabilities and EVs on extreme totals are
overstated in absolute terms, even though the *direction* of the edges (and their ranking)
is right. The shrink is roughly uniform across mismatch sizes, so team ordering is untouched.

**Recommendation** (owner decision — this changes product semantics): add a fourth,
**calibrated** lens = our ratings shrunk ×0.75 around the field mean, same engine otherwise.
Since edges are monotone in the dispersion factor, conviction = min(edge) across the
calibrated (×0.75) and market-matched (×1.148) endpoints certifies an edge under *every*
dispersion hypothesis in between — the cleanest possible robustness filter. Sizing should
key on calibrated EVs, not the raw ones.

## §4. Opinion on the market-matched set + conviction (owner asked)

The construction is sound and the implementation verified (slope exactly 0 at s*; manual
rating edits propagate into the stretched set; conviction = min of the two lenses on the best
side; ✓✓ at both ≥4%). The owner's intuition — "standing out on both raw and market-shaped
ratings is strong evidence" — is exactly the right instinct; §3's calibrated lens is the same
idea extended to the *other* end of the dispersion bracket, where the evidence says reality
lives. One caveat inherited from §3: on the current pair of lenses, ✓✓ still certifies against
dispersion stories ≥1.0 only; the calibrated end is the stricter test.

## Residual caveats (unchanged from before, still true)

- One year of totals-level outcomes; no historical totals P&L backtest yet. The game-level
  evidence is strong but indirect for totals prices.
- Flex pairings are projected until Nov 22 (edge sensitivity to pairing swap is small —
  opponents are all mid-tier Pac-12 — but nonzero).
- HFA fits at 2.7–3.2 on 2021–25 games vs our 2.3 (minor, well within noise year to year).
- Our grades' incremental accuracy over SP+ preseason is unproven; the 0.75 shrink estimate
  borrows SP+'s error profile as the best available proxy.

---

# Part II — Intellectual audit of the engine (owner request, round 2)

The question: is this the *right way* to simulate a win total, not merely a correct
implementation of a chosen way? Verdict first: **the architecture is right — probit margin
model, three-source variance with the shared own-team shock, exact Poisson-Binomial +
Gauss-Hermite is the correct structure for this object, and better than the Monte-Carlo
independent-games models most bettors build (those understate tails; the shared shock is the
single most important choice here and Opus made it correctly). The one first-order thing the
architecture was missing is the forecast-calibration layer — now added as the Calibrated set.**

## The decisive test: season-level calibration (2021–25, 663 team-seasons)

A win-total engine's output is a season-win *distribution*, so I validated at that level: ran
the full engine (bands 6, σ 13.5, shared shock, PB+GH) on five seasons of SP+ preseason
ratings and real schedules, and compared predicted distributions to actual win counts.

| metric | RAW engine (shrink 1.0) | CALIBRATED (×0.75) | target |
|---|---|---|---|
| bias (actual − E[W]) | −0.02 wins | −0.03 wins | 0 |
| dispersion ratio | 1.18 (too narrow) | 1.07 | 1.00 |
| central-50% coverage | 49.0% | 51.6% | 50% |
| central-80% coverage | 75.6% | 80.8% | 80% |
| P(over) reliability, worst bucket | −6.2 pts | −3.9 pts | 0 |
| P(over) tails (≥0.90 bucket) | −2.1 pts | −0.3 pts | 0 |

The raw engine was well-centered but overconfident exactly as the game-level backtest
predicted (65% claims hit 60%, 10%-or-less claims hit at nearly double the stated rate).
The calibrated engine is near-textbook. This is the empirical answer to "is the method
right": **yes, once the shrink layer is in.**

## Design choices reviewed, one by one

- **Probit (normal-margin) win curve** — right family; margins around true ratings are
  ~N(0, 13.6) empirically (final-ratings residual SD 13.58 vs σ_game 13.5). Residual
  non-normality (fat tails / key numbers) matters for spreads, much less for win
  probabilities; after the shrink, tail buckets calibrate to −0.3 pts. No change needed.
- **Three-source variance & the shared shock** — conceptually correct and the reason the
  tails behave. One refinement available: the season-constant δ treats all rating error as
  fully season-correlated, while part of the real error is *drift* (b decays 0.71 → 0.57
  across the season), which correlates games less than a constant offset. Effect: current
  tails are very slightly fat given a calibrated center — visible as the calibrated
  dispersion ratio 1.07 sitting a touch above 1 while coverage is on target. Second-order;
  not worth the complexity.
- **Bands ±6, uniform-ish** — consistent with the preseason-error decomposition (margin
  residual 16.9² − 13.5² ⇒ per-team τ ≈ 7). Asymmetric team risk (QB-dependency skew) is
  unmodeled; teams collapse harder than they surge, which the symmetric shock misses. Minor.
- **HFA 2.3 constant** — 2021–25 fits say 2.7 (margin space); site-specific effects
  (altitude, Hawai'i travel) unmodeled. Worth ~±0.05 wins; it's a live-tunable in the UI.
- **FCS opponents at fixed tiers** — error budget trivial (favorites ≥97% either way).
- **What's genuinely unmodeled at the totals level** — (1) the bowl-eligibility push:
  teams finish on exactly 6 wins 14.3% vs the model's 13.3% — real, small, argues a
  half-point of extra respect for overs at 5.5 and unders at 6.5; (2) motivation/tanking
  and coach-firing dynamics in lost seasons (part of why the left tail is heavy);
  (3) schedule *order* (irrelevant under a constant δ, mildly relevant under drift).
- **Portfolio caveat (matters for betting, not simulation)** — fade-the-extremes edges are
  correlated across teams through the dispersion thesis: in a chalk-holds season they lose
  together. The ✓✓ bracket bets are the defense — team-specific by construction — and
  sizing on calibrated EV already prices the per-bet honesty. Do not size the aggregate
  as if the 51 ✓✓ bets were independent.

## Where the shrink's limits are

×0.75 is borrowed from SP+ preseason's five-year error profile (the best available proxy;
our blend has no history). If the roster grades genuinely add information beyond SP+, the
true factor is a bit milder (~0.8). It is a global constant — per-team shrink (shrink less
for stable veteran rosters, more for high-churn ones) is the natural next refinement, and
the band machinery (L-counts, coach-change flags) already contains the raw material. The
shrink is live-tunable in the Methodology tab (default 0.75; setting 1.0 reproduces the
raw engine exactly).

---

# Part III — Grading-cohort audit: did quality drop at the Opus handoff? (owner request, round 3)

## Where the handoff happened

Hard evidence from commit trailers (`Co-Authored-By`), not memory: the switch is commit
`f6fd648` — **"Handoff hardening + retro-audit corrections," 2026-07-17 02:58** — which also
retro-audited all 71 pre-handoff builds (5 re-grades) and hardened the gates (team_dump
evidence script, grades_check, hard-fail departure check) before handing over.

- **Pre-handoff (Fable 5): 71 teams** — Iowa pilot, AAC, Big 12, Big Ten, MAC, Mountain West.
  Graded 07-14 22:38 → 07-17 01:41.
- **Post-handoff (Opus 4.8): 67 teams** — Pac-12, ACC, SEC, Sun Belt, CUSA, Independents.
  Graded 07-17 14:38 → 07-18 22:45.

Fairness note the owner should see: the infamous NDSU −27 grade artifact was **pre-handoff
(Fable) work** — last team of an overnight session. Of the 5 manual-override teams, 1 is
Fable-era (NDSU), 4 are Opus-era (Boise, CSU, Kennesaw, Jax State) — but all 4 of those are
realignment/no-FBS-data teams, the class where grades break regardless of grader.

## Cohort fingerprints (all 137 mapped teams)

| metric | Fable (70) | Opus (67) |
|---|---|---|
| dossier length (median words) | 1,474 | 1,443 |
| distinct named players (median) | 44 | **60** |
| evidence pulls per team (median) | 10 | 10 |
| L-flags per team | 1.34 | 1.30 |
| grade-vs-anchor residual, mean abs | 3.54 | 2.98 |
| residual max abs | 14.7 | 11.3 |

Same depth, same evidence discipline, same uncertainty-flag usage; Opus names *more* players.
The one structural difference: Opus's grades sit ~16% closer to the analytics anchor. That
could have meant timidity (less independent signal) — but the deep audit below shows his
*boldest* calls (UConn +11.3 above anchor, JMU −9.0 below) were the best-verified dossiers
in the sample, so it reads as fewer wild misses, not anchor-hugging.

## Deep audit: 10 Opus teams + 4 Fable controls, graders blinded

Protocol: for each team, an independent auditor read the dossier/grades/META, extracted the
5–7 most load-bearing factual claims (QB rooms, transfers, returnees, coaching, injuries),
and verified each against July-2026 web sources (official rosters, ESPN/247/On3, beat
outlets). Sample was leverage-weighted: the biggest grade-vs-anchor deviations (UConn +11.3,
JMU −9.0, Liberty −7.1, Miss St +6.5) and top board-conviction teams (Texas, Miami,
Vanderbilt, Wake, Oregon State) plus the reclass risk class (Missouri State).

| team (cohort) | accuracy | specificity | coherence | grade-moving errors |
|---|---|---|---|---|
| UConn (O) | 9 | 9 | 9 | none — the +11 optimism fully verified |
| James Madison (O) | 9 | 9 | 9 | none — the −9 pessimism fully verified |
| Liberty (O) | 8 | 9 | 9 | none (2 misdescriptions, sub-threshold) |
| Mississippi St (O) | 8 | 9 | 8 | none (framing inflation only) |
| Texas (O) | 9 | 9 | 9 | none (Burke UDFA-vs-drafted cosmetic) |
| Vanderbilt (O) | 8.5 | 9 | 9 | none (QB race framing stale) |
| Miami (O) | 9.5 | 10 | 9.5 | none |
| Wake Forest (O) | 9.5 | 9 | 9 | none |
| Oregon State (O) | 9 | 9 | 8 | none (TE Olsen omitted, +2-4 WRTE at most) |
| Missouri State (O) | 9 | 9 | 10 | none; no-data class handled honestly |
| **Opus mean** | **8.9** | **9.1** | **9.0** | **0 of 10 teams** |
| Tulsa (F) | 9 | 9 | 8 | none (Tease listed departed but returns, +2-3 WRTE) |
| UTSA (F) | 9 | 9 | 7 | none (Kamar Missouri "returns" likely wrong, −2-3 OL; stale md grades) |
| New Mexico (F) | 9 | 9 | 9 | none (co-DPOY nit, INT arithmetic slip) |
| Kent State (F) | 9 | 9 | 9 | none (ST honors undersold) |
| **Fable mean** | **9.0** | **9.0** | **8.25** | **0 of 4 teams** |

~85 load-bearing claims verified across 14 teams: ~74 CONFIRMED (many to the exact digit),
~9 PARTLY, ~2 WRONG-but-cosmetic. **Zero errors in either cohort clear the materiality bar**
(≥6 unit points or ≥1 rating point).

## Verdict

**The fear is not supported. Opus's grading is statistically indistinguishable from the
pre-handoff work on every dimension measured, and his error profile is the same kind
(attribution/framing slips, stale details) rather than a worse kind (wrong rosters, invented
facts).** If anything the audit's two most concrete factual errors — Tulsa's Tease listed as
departed (he's on the 2026 roster) and UTSA's Kamar Missouri booked as returning (he's
almost certainly gone) — are both in the *Fable* cohort, whose post-correction file hygiene
(dossier headers out of sync with corrected grades.json) is also slightly worse.

## Sub-threshold corrections available (owner's call — none move a rating > ~0.2)

| team | unit | direction | basis |
|---|---|---|---|
| Tulsa (F) | WRTE +2-3 | up | Micah Tease returns (official roster) — listed as departed |
| UTSA (F) | OL −2-3 | down | Kamar Missouri likely departed (degree May '25; not on '26 roster) |
| Liberty (O) | QB +2-4 | up | Purdie is a junior w/ 8 FBS starts, not a thin-tape RS-Fr |
| Oregon State (O) | WRTE +2-4 | up | TE Eric Olsen (Utah Tech, Athlon 3rd-Tm All-Pac-12) omitted |
| Kent State (F) | ST +2-4 | up | Clark's MAC STPOY + preseason AA honors undersold |

At K=0.35 with the ±6 clip, each is worth ≤0.2 rating points — noise relative to bands of
±6. Recommendation: log them, change nothing; or batch them as a "micro-errata" pass if
purity is preferred. For what it's worth, the two board-relevant ones (Tulsa over, UTSA
under) both lean *toward* our current positions.
