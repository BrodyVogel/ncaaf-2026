# v2 rollout — full impact memo (2026-07-23)

The v2 grading arithmetic (validated w(n) shrinkage + class-jump terms + freshman
composite priors + missed-year look-through) is now the baseline for player grades, and
every unit on every FBS team has been adjudicated against it. This memo records what
changed, why, and what it does to the board and the 14 open bets.

## The adjudication, by the numbers

1,098 logged verdicts in `data/research/adjudication_v2.csv` — every (team, unit) on all
138 teams. Two full dossier re-opens (Illinois, Notre Dame), 12 bet-team reviews, a
9-team shortlist round, and a 1,041-verdict scripted field sweep with a manual pass over
every |dg|>20 case. Net: **302 unit grades changed across 122 teams** (118 up, 138 down
in the sweep round; mean move 5.0 grade points; hard cap ±8).

### Protocol (as executed; middle grounds allowed at every tier)

- Gap metric: v2 formula percentile − dossier grade, **demeaned within conference×unit**
  (raw gaps are swamped by the scale-convention artifact — graders deliberately weighted
  down the big conference offsets). Independents demean against class pools (ND→P4,
  UConn→G5), matching the final_pass pseudo-pools; Pac-12 pools with MWC.
- **Blend trigger |dg| > 8 ≈ 1 SD** of the demeaned gap (8.49 empirically). The plan doc
  originally said |dg|>4, but that would have "corrected" 61% of the field — i.e. noise.
  1 SD matches the de facto floor of the manual rounds (nothing below |dg|=8 was ever
  hand-blended). Deviation logged here and in the plan doc.
- Blend weights toward the formula: **DB 1/3** (S2: DB tape earns only w≈0.40 even at
  full volume — neither source deserves full trust), **LB 0.40**, all others **0.50**;
  move capped **±8**; grades clamped [1, 99].
- **Unit-info guard**: formula informativeness = matched volume-weight share of the
  two-deep. Info < 0.10 → hold, "formula uninformative" (37 cases — e.g. Iowa QB, where
  the "evidence" was 3 and 21 dropbacks of transfer tape); info < 0.20 → blend halved.
  Freshman composite priors credited at 0.25 (S2b: partial r 0.266 ≈ quarter-season).
- **Option-academy rule**: Army/Navy/Air Force blends halved — PFF individual grades of
  triple-option units are scheme-distorted (e.g. Army OL 84 → 79, not 76).
- Tier-3 accepts within the noise band are logged with their dg — nothing was rubber-stamped
  silently.

### The two re-opens

**Illinois** (flagged: 5 units moving against our U7.5): the formula won. Houser's
84.0/473-dropback ECU season is genuine full-volume tape and the dossier double-discounted
the G5→P4 step (the exact v1 failure mode the research program identified). QB 62→70,
RB 32→38, WRTE 48→52, OL 38→42, DL 41→45, LB 46→48.

**Notre Dame** (deferred until the Independents fix): the pro forma's craters (QB −34,
WRTE −31, OL −23) were 100% artifact — the polluted IND offset cells (Army-dominated:
OL −22.0 where the P4 pool mean is +6.0). The dossier had itself refused that cell and
graded ND P4-elite; recomputed with the P4-pool scale term, five of seven units confirm
within ±4. Three modest markdowns survive scrutiny: QB 86→84, RB 66→64, OL 78→74 (PFF
individual OL grades are lukewarm — only Knapp above 65 — recovering C, freshman LT).
Sum 602→594.

### Manual middle-ground overrides (|dg|>20 review)

- **Duke QB 50→46** (not 42): solo-matched unit — the FR QB2 is unmatched, so the
  aggregation percentile is an artifact; Eget's v2 *player* value is actually above v1
  (the spec's own worked example).
- **Michigan QB 60→56** (not 52): Underwood's actual freshman tape (69.3/399) is
  league-average QB play at the w-cap; the year-2-leap premium is partly narrative, but
  a 5-star who *played immediately* is not the dead-pedigree case.
- **Wisconsin QB 62→57** (not 54): Joseph's 78.9/334 is real full-volume G5 tape (the
  Houser lesson) and the validated step-up charge is only −3.5.
- **Louisiana Tech WRTE 44→50** (not 52): half the matched evidence is a 92-route 2024
  sample and the room lost its top four.
- **Tulane RB 58→54** (not 50): three P4 transfer RBs sit unmatched in a combined roster
  row — the formula is partially blind to the additions.

## Board impact: small by design

The K=0.35 residual blend, ±6 clip, and anchor structure did their job — 302 grade
changes produce **mean |Δfinal| = 0.30 pts**, only 4 teams beyond ±1:

| team | before | after | Δ | driver |
|---|---|---|---|---|
| Rutgers | +2.9 | +4.1 | +1.21 | DB 36→42 + sweep QB/DL up |
| Illinois | +6.3 | +7.5 | +1.18 | re-open (QB 62→70 et al.) |
| Arizona | +11.1 | +10.0 | −1.12 | WRTE 52→45, RB, DB mix |
| Oregon | +30.7 | +29.6 | −1.09 | DL 90→82 (sweep) |
| Michigan State | −0.1 | +0.9 | +1.00 | WRTE 38→45, DL up |

Diagnostics: OLS R² off 0.66 / def 0.47 (vs 0.67/0.49 pre-v2 — unchanged in substance);
board SD 13.13; market stretch auto-refit 1.1475 → **1.1591**; recenter +0.57; 0 caps hit.
Census asserts pass (MW {8:10}, ACC {8:5, 9:12}). Calibrated lens remains ×0.75 (not
refit, by design — it is an out-of-sample honesty constant, not a fit-to-taste dial).

## All 14 open bets, re-priced

P = calibrated-lens probability of our side; mm = market-matched lens. Edge = P − breakeven.

| bet | P before→after | mm before→after | cal edge | verdict |
|---|---|---|---|---|
| UConn O5.5 −105 | 67.7→68.6% | 68.4→69.8% | +17.3% | OK (improved) |
| Tulsa O5.5 +100 | 66.1→66.2% | 67.0→67.4% | +16.2% | OK |
| Oregon St O3.5 −150 | 75.4→74.8% | 71.6→70.8% | +14.8% | OK |
| Bowling Green O4.5 −160 | 77.2→75.9% | 77.8→76.0% | +14.4% | OK |
| Liberty U8.5 −145 | 71.0→71.1% | 67.0→67.2% | +11.9% | OK |
| Arizona St U6.5 +100 | 59.0→60.3% | 62.8→64.7% | +10.3% | OK (improved) |
| Kennesaw O6.5 +120 | 54.8→55.3% | 60.1→61.1% | +9.9% | OK |
| Illinois U7.5 −160 | 71.9→69.0% | 73.7→69.7% | +7.4% | OK — thinned ~3pp as forecast, stays +EV |
| West Virginia U5.5 +132 | 50.2→48.8% | 59.7→57.6% | +5.7% | OK (cal side now a coin-flip; mm carries it) |
| East Carolina O7.5 +100 | 59.4→58.3% | 72.8→71.5% | +8.3% | OK |
| Hawai'i U7.5 −120 | 64.8→64.9% | 62.3→62.7% | +10.3% | OK |
| Florida U4.5 conf −110 | 59.2→58.2% | 63.6→62.2% | +5.8% | OK |
| **UCF O3.5 conf −115** | 60.9→59.8% | 56.7→55.0% | +6.3% | **THIN — mm edge +1.5%, below the 4% ✓✓ bar. Hold ticket, no add.** |
| Pittsburgh U5.5 conf −136 | 64.5→65.0% | 61.6→62.4% | +7.4% | OK (improved) |

No bet flips negative on either lens. Five improved. The one watch item is UCF: the v2
sweep took QB 52→46 (formula skeptical of the SBC-POY qualitative case) and the
market-matched edge is now inside noise. The ticket was struck at +7.4% and there is no
sell mechanism; logged in the tracker note, and UCF goes on the fall-camp re-check list.

## What v1 remains

v1 grades are preserved per-unit as `v1_grade` in each changed `grades.json` (and fully
in git history + `ASSEMBLY_LOCKED_2026-07-20`). FCS/D2/JUCO entrants still grade under
the v1 qualitative brackets (out of v2's validated scope). Specialists (ST) were never
in scope. Everything else — unit→rating OLS, K=0.35, ±6 clip, demeaning pools, bands,
engine — is unchanged machinery rerun on the new grades.
