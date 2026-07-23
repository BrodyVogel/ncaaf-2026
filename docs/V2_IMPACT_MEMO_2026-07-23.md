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

---

## Addendum — reconciliation pass over the sweep blends (same day)

Owner asked whether the ~230 mid-band blends (scripted policy, no individual eyes)
deserved reconciliation. Answer: yes, done, via a uniform robustness check rather than
230 hand re-reads.

**Method.** Every blend's demeaned gap was recomputed under a second aggregation —
**starters only** (slot-1 rows) — alongside the full two-deep view. The five artifact
signatures the |dg|>20 review had surfaced (solo-matched units, FR-prior backup drag,
combined-name parse misses, unmatched-heavy rooms, stale-2024 evidence) are all
*composition* artifacts: they distort the unit aggregate while the starter-level evidence
is fine. Rule: the dossier only moves by the disagreement **both views agree on**
(sign-preserving minimum; zero when the views disagree in direction). Policy weights,
info/academy halvings, and the ±8 cap unchanged. The five pinned manual overrides kept.

**Result.** 51 of 256 blends amended — **all 51 toward the dossier** (mean 1.6 grade
points, max 5), the exact signature of artifact-stripping. Four fully reverted
(Coastal Carolina DB, New Mexico State DL, Florida LB, and the sign-disagreement cases).
Equally important: cases flagged by intuition but *confirmed* by the starter view
(Penn State QB, Western Michigan QB) kept their moves — the check cuts both ways.
205 blends unchanged: both views independently agree on them.

**Board effect: negligible.** v2.0 → v2.1 mean |Δfinal| = 0.036 pts; biggest mover New
Mexico State +0.33. Stretch 1.1587, SD 13.13, census asserts pass, R² unchanged. All 14
bets re-priced: no verdict changes; Florida conf U4.5 gives back ~0.3pp (its LB blend
reverted); UCF conf O3.5 still THIN (mm +1.7%) — hold, no add. Final grade-change count
vs v1: **299 units across 138 teams**, every one carrying either two-view formula
agreement, a logged blend with robustness confirmation, or a hand adjudication.

---

## Addendum 2 — sensitivity bound + per-case re-read (v2.2, same day)

**Sensitivity bound (the soft constants are decision-irrelevant).** The board was rebuilt
with every rule-set blend at 0× (reverted to dossier) and at 2× (double weight, cap ±16),
and all 14 bets re-priced at both extremes. No bet flips on the min-lens edge anywhere in
the bracket; 13 of 14 stay ≥ +4.5% at every point. UCF's thinness (+1.9…+2.2%) persists
even at 0× — it comes from the hand-adjudicated QB verdict and the market, not the blend
constants. The ⅓/0.4/0.5 weights and ±8 cap can therefore not change any decision we act
on, which retires their unvalidatability as a practical concern.

**Per-case re-read (all 256 blends, every verdict logged).** Each blended unit got a
read of its full dossier rationale, per-player formula math, and the *reason* for the
disagreement. 136 policy verdicts confirmed; **120 adjusted** (mean adjustment ~2.8
grade pts), overwhelmingly back toward the dossier. What the re-read found that no
script had:

- **Ceiling-squeeze bias**: cell-mean demeaning breaks near the grade tails — a
  dossier-90 unit mechanically cannot show its cell's typical +15 gap, producing
  spurious negative dg. Corrected by rank-agreement checks: Oregon DL 82→88, Iowa OL
  85→87, Ohio State RB→74/WRTE→82, BYU RB→80, Penn State QB 66→72, Georgia QB→68.
- **Offset-axis distortion for elite G5 skill units**: MWC/SBC RB-WRTE values compared
  on a P4-offset axis read spuriously low despite elite raw values — SDSU RB 44→50,
  Texas State WRTE 46→52 (the only FBS team returning two 1,000-yd receivers),
  Washington State RB/WRTE, Western Michigan QB 38→44 (Lowry, MAC OPOY, 80.1 value).
- **Formula-void cases**: Texas DL held at 62 — Colin Simmons (All-SEC, 12 sacks) was
  absent from the matched set entirely; Jacksonville State QB fixed a name-collision
  (CSU's DL Jack Moran had matched as the QB2); Oregon State WRTE held — the formula
  never saw the corrected Butler/Durant reload.
- **Dual-threat blind spot**: the QB formula is the passing facet only; run value is
  invisible. Blends halved for running QBs (Louisiana, A&M, Washington QBs).
- **Solo/positive aggregation inflation** (Duke-precedent, symmetric): Indiana QB
  77→74, Miami QB 74→72, KSU QB, SMU QB, UAB QB, UTSA RB and peers halved.
- Confirms where evidence was real: Nevada DL 34 (LaBarbera), Rutgers DL 61 (three
  all-league transfer tapes), Texas Tech DL 73, Oklahoma QB 54 (the S2-D-B validated
  hampered-tape read), Arkansas State OL 62, Clemson QB 40.

**Net effect v2.1 → v2.2**: mean |Δfinal| 0.114 (top movers Oregon +0.67, Texas +0.54);
stretch 1.1557; SD 13.12; census asserts pass; R² unchanged. All 14 bets re-verified —
no verdict changes; UCF conf O3.5 remains the lone THIN (mm +1.2%, hold/no add).
Adjudication log now carries **1,405 rows**; every blended unit has a human-written
verdict with reasoning, and every accept carries two-view formula agreement. Grade
changes vs v1: 290 units.

**Methodological note for 2027**: future sweeps should compute disagreement on
within-cell *ranks* (immune to ceiling squeeze and offset-axis artifacts) and add a
rushing-value term to the QB formula arm. Logged as build candidates.

---

## Addendum 3 — full-field completion: the accept layer (v2.3, same day)

The final layer: every unit that had been a Tier-3 *accept* (or hold) got the treatment
appropriate to its evidence structure, completing owner-directed adjudication of the
entire 1,104-unit field.

**Design.** Accepts differ from blends: two views already agree, so the failure mode is
*false agreement* (an artifact masking a real disagreement). All 625 remaining accepts
were screened four ways — within-cell rank disagreement (immune to ceiling/axis
artifacts), starter-only view, missing-star scan of unmatched roster rows, and a
dual-threat-QB flag. 101 flagged + 179 near-trigger (|dg| 4–8) got full case reads;
310 deep-clean accepts got a pre-registered 40-case random sample with an expansion
rule (≥2 real adjustments → read the whole band). The 138 ST units (no formula arm
exists) got a single-source scan: stored-vs-text grade reconciliation + unresolved-flag
search.

**Results.**
- 320 case reads → **68 adjustments, all ±2–3 grade points** (252 confirms). Typical
  moves: Louisville DL 62→65 (Lubin 91.4/597 + two 80+ tapes), Clemson DL 58→61,
  Virginia Tech DB 60→62 (White 87.4/879 + four 72+ at volume), Penn State DL 60→57
  (entire front + best per-snap tape gone), USC OL 54→52 (five returners, tape 53–57
  at volume), BYU LB 50→48 (aligning the stored grade with the dossier's own text).
- **Sample: 0 of 40 deep accepts needed adjustment** → no expansion; the 310-case band
  stands as screen-cleared and sample-validated.
- **ST scan: 138/138 clean** (one benign open-kicker-battle flag at Indiana, already
  priced by its confidence letter).
- Board effect v2.2 → v2.3: **mean |Δfinal| 0.049** (max Boston College −0.31); stretch
  1.1545; SD 13.12; census asserts pass. All 14 bets re-verified — no changes; UCF conf
  O3.5 remains the lone THIN hold (mm +1.6%).

**Where this leaves the ledger.** 1,104 units: ~80 hand-adjudicated in the manual
rounds, 256 blends re-read case-by-case, 280 flagged/near-trigger accepts read
case-by-case, 310 deep accepts screen-cleared + sample-validated (0/40), 138 ST
single-source scanned, and 37 info-holds (formula uninformative by construction)
reviewed wherever any screen flagged them. Grade changes vs v1: **358 units**. The
adjudication log stands at 1,863 rows. v2.3 is the production vintage.
