# VERDICT: BET — 0.10u (floor of the pilot lane), DEMOTED from #1 on the board. Corrected edge ≈ +6 (range +3 to +8), not the +10.3 pricer_v1 claims.

**Gunner Stockton (Georgia) — FanDuel Regular Season passing yards, UNDER 2650.5 (−113)**
Deep dive per `docs/DEEP_DIVE_PROCEDURE_QBPROPS_2026-08-04.md`. Dive 1 of 6.
Author: claude-fable-5, 2026-08-04. Nothing staked; returns to owner for approval.

**Headline finding, and it is slate-wide, not Stockton-specific:** pricer_v1 is
mis-specified. It prices off the ratio `r = line / (12 × prior pace)` and ignores
the *level* of prior pace. Prior pace is a strong, mechanically-explicable
moderator of the under rate, and Stockton sits on the wrong side of it. Section
1B carries this; §7 restates the corrected board for all six candidates.

---

## Step 0 — Rules gate

FanDuel house rules pulled live 2026-08-04 (`fanduel.com/fanduel-sportsbook-house-rules-nc`):

- *"For season long player prop bets, the nominated player must play at least
  one snap during the regular season for bets to have action."*
- *"For offensive player prop markets, the player must play at least one
  offensive snap for proposition bets to stand."*
- Dead heat: `Returns = (Stake × (Expected Winners / Actual Winners)) × Odds`.
- *"College Football Regular Season Wins: This market does not include
  Conference Championship Games, Bowl Games, or College Football Playoffs."*

**Two consequences, both material and both favourable:**

1. **The ≥1-snap rule makes this effectively all-action.** A Week-1
   season-ending injury *cashes* the under; it does not void. The availability
   thesis therefore survives in its strongest form — every game he misses after
   his first snap is pure profit to the under side.
2. **It also retroactively validates the panel.** `FINDINGS_S20_2026-08-03.md`
   logs a "survivor caveat" — the panel requires ≥1 attempt in year *t*, so
   total job-loss cases drop out, which the doc treats as a downward bias on the
   measured under rate. That is **wrong under this house text**: never-play cases
   *void* rather than lose, so the panel's entry filter is exactly the right
   filter for this market, not a conservative one. **Correction owed to the
   findings doc** (§Deviations & caveats).

**CCG treatment — UNVERIFIED, and the procedure's kill switch is mis-specified.**
The CCG-exclusion text above is confirmed only for the Regular Season *Wins*
market. Two searches failed to surface the equivalent text for season passing
yards. But the kill switch as written in the procedure ("if CCGs are INCLUDED …
flag and stop") has the logic backwards, because it assumes the historical panel
is a strict 12-game basis. It is not: the S20 panel was built on CFBD
`seasonType=regular`, which **includes** conference title games (max g=13
observed). Therefore:

| FD settlement basis | Relation to panel | Effect on this bet |
|---|---|---|
| CCG **included** | matches panel exactly | neutral — no recompute needed |
| CCG **excluded** | one fewer game than panel comparables | **bonus to the under** |

Neither branch is a kill. Georgia is a live SEC-title participant (market
conference-wins line 6.5/7.5), so if CCGs are excluded, ~1 game of Stockton's
exposure (his 2025 CCG was 156 yds) comes off the top. **Not priced in below —
treated as unmodelled upside.** Correction owed to the procedure doc.

**Line check:** U2650.5 −113 stands as of the 2026-08-03 capture. No movement,
so no "what did the market learn" question to answer.

---

## Step 1 — Re-derivation from local data

Source: `data/cfbd/qb_props/player_games_flat.csv`, filter `player=Gunner Stockton`.

- **13 games**, weeks 1,2,3,5,6,7,8,10,11,12,13,14,15 (weeks 4 and 9 = byes).
- **2,691 yards, 355 attempts** → **pace₀ = 207.00 yd/g**.
- Week 15 vs Alabama = **SEC Championship Game, 156 yds**. Ex-CCG: 12 games,
  2,535 yds, **211.25 yd/g**.
- Name-join check: single spelling, no suffix, no team ambiguity, no missing
  weeks against Georgia's own 13-game CFBD-regular slate. **He played every
  game Georgia played.** Clean.
- Cross-check vs `snapshots/Georgia/pff/unit_QB.csv`: PFF shows 14 g / 2,906 yds
  — the extra game and 215 yards are the CFP, correctly excluded by CFBD
  `seasonType=regular`. Consistent.

**Ratio:** `r = 2650.5 / (12 × 207.00) = 1.0670` (panel basis).
Ex-CCG basis: `2650.5 / (12 × 211.25) = 1.0455`.

**pricer_v1 reproduced exactly.** Secure ladder at r clamped to 1.05 → 0.690 raw;
shrink `0.5 + 0.70 × (0.690 − 0.5)` = **0.633**; edge `63.3 − 53.05` = **+10.25 ≈ +10.3**.
Matches `data/cfbd/qb_props/pricer_v1_2026-08-04.json` to <0.001. **No Step 1 stop.**

---

## Step 1B — UNSCHEDULED: the pricer is mis-specified (this is the report's core)

The procedure did not ask for this step. It exists because Step 1 surfaced a
contradiction the findings doc flags but never resolves: the H11 (grade ≥80) cell
decays −22.1 yd/g and goes under 77.8%, while the H12 analog cell (year-2 ∧
grade ≥75) decays **+0.6** and goes under 67.6%. Stockton's PFF pass grade of
**80.7** puts him in *both*. They disagree on direction, so the bet's sign was
genuinely undetermined.

**Cell replication first.** Every AMENDMENT 1 cell reproduces exactly from
`panel_s20.json` + `pff_history/` (n=163 at t≥2022; H10 n=75 70.7%; H11≥80 n=45
77.8%; H12 n=34 67.6% Δ+0.6). The panel is sound.

**Arbitration attempt — and it fails in an instructive way.** The uncomputed
sub-cell:

| Cell | n | UNDER | P(12+) | Δpace |
|---|---|---|---|---|
| year-2 ∧ grade ≥80 | 19 | 73.7% | 42% | −12.5 |
| …same-school only | 16 | 75.0% | 44% | −12.7 |
| year-2 ∧ 75 ≤ g < 80 | 15 | 60.0% | 47% | **+17.1** |

Read naively this resolves for the under: the H12 cell's flat Δpace is carried
entirely by the 75–80 band, and Stockton at 80.7 belongs to the decaying half.
**Do not read it naively.** The continuous test kills it: regressing Δpace on
grade *within* the year-2 subset gives slope **−0.45 yd/g per grade point,
t = −0.63, n=66** — indistinguishable from zero. The band table bounces (78–81:
+23.7 on n=7; 81–85: −13.6 on n=10) because the cells are tiny. **There is no
cliff at 80. The H11/H12 contradiction is a small-n binning artifact, and
neither cell's Δpace should be applied to Stockton.** Best estimate of his pace
change from grade alone: ≈ −4 yd/g, with an error bar that swamps it.

**What replaced it — the real moderator.** Sorting the panel by *prior pace
level* instead of grade produces a monotone, large, and mechanically obvious
gradient. Under rate at Stockton's own r = 1.067:

| pace₀ quartile | range | n | UNDER@1.067 | Δpace | P(12+) |
|---|---|---|---|---|---|
| Q1 lowest | <210 | 39 | 61.5% | **+14.3** | 41% |
| Q2 | 210–233 | 39 | 74.4% | +1.1 | 36% |
| Q3 | 233–270 | 39 | 76.9% | −11.5 | 44% |
| Q4 highest | ≥270 | 39 | 89.7% | **−55.0** | 49% |

Same-school only, the spread is wider still: Q1 **54.5%** (n=22, Δpace +22.7) vs
Q4 **91.3%** (n=23, Δpace −42.1).

**The mechanism is regression to the mean and it is not subtle.** Same-school
fit `pace_t = 119.8 + 0.500 × pace_{t−1}` (n=93, **t = 5.36**, resid sd 45.2,
panel mean pace 243.6). The line scales with pace₀; the reversion target does
not. A 300-yd/g QB is priced at ~315 and reverts toward ~270 — near-automatic
under. A 207-yd/g QB is priced at ~221 and reverts toward **223** — the fit
predicts him *over his own line*. This is the same regression structure that
makes the desk's ratio anchor exploitable in the first place; pricer_v1 captures
one half of it (the ratio) and discards the other (the level).

**Stockton's number, four ways, all at r = 1.067:**

| Estimator | n | raw | shrunk | edge |
|---|---|---|---|---|
| pricer_v1 (secure ladder, r-clamped) | 87 | 69.0% | 63.3% | **+10.3** |
| same-school, pace-matched ±30 | 47 | 66.0% | 61.2% | +8.1 |
| same-school, year-2, pace₀ 180–240 | 28 | 67.9% | 62.5% | +9.5 |
| logistic, pace₀ + log r + transfer | 156 | 64.9% | 60.4% | +7.4 |
| same-school, pace₀ <210 (his actual quartile) | 24 | 58.3% | 55.8% | **+2.8** |

Caveat on the logistic: it is fit across an r-grid with repeated rows, so its
standard errors are understated and its absolute levels drift low against the
published ladder (41.9% vs 55.2% at r=0.85). Use it for the **sign and size of
the pace₀ coefficient (+0.387 per 50 yd/g, z≈+4.8)**, not for levels. The
non-parametric pace-matched estimate is the one to lean on.

**The pace correction is post-hoc and was not preregistered.** It is reported as
exploratory. It is nonetheless mechanically derived rather than dredged, is
monotone across four quartiles, and rests on the single most significant
relationship in the panel (t=5.36) — so ignoring it would be motivated reasoning
in the direction of our own position, which is the exact failure mode
`AUDIT_2026-08-03_FULL_STACK.md` exists to police.

---

## Step 2 — Availability audit (the whole thesis)

**Injury history.** Spring 2026 knee: Smart called it *"a little offseason injury
in our workouts,"* Stockton limited two days, wore a right-knee sleeve,
practising and *"fine now"* as of **2026-03-31** (AJC; CBS Sports same day).
Non-structural, no surgery. **2025: started and played all 13 CFBD-regular games
plus the CFP** — a clean, complete season. No prior structural history surfaced.

**Playing style — genuine exposure, but the sack numbers are good.** From
`snapshots/Georgia/pff/unit_QB.csv` (2025, 14 g incl. CFP): sack_percent **3.9**,
pressure_to_sack_rate **15.0**, 18 sacks on 458 dropbacks against 120
defence-generated pressures — he gets rid of it (avg_time_to_throw 2.76, aDOT
7.3). Against that: **53 scrambles and 462 rush yards with 10 rushing TDs**, i.e.
designed and improvised carries in traffic, and Bulldawg Illustrated (2026-07-31)
notes he *"took more hits than Georgia would like for its starting quarterback."*
Net: below-average sack exposure, above-average rush exposure.

**Backup situation — pull risk real, bench risk near zero.** QB2 Ryan Puglisi
appeared in **6 of 13 games on 27 attempts** (161 yds, 6% of team QB yards) —
pure mop-up, which confirms Georgia *does* empty the pocket in blowouts but that
it costs Stockton little. Room behind: Ryan Montgomery, Hezekiah Millender,
Bryson Beaver (Oregon transfer). Smart praised depth (2026-03-31) but no name
threatens the job; every 2026 source has Stockton as the unquestioned starter
(*"Stockton isn't just getting ready to be the quarterback — he is the
quarterback now"*). Senior, no redshirt/draft-preservation angle.

**Game-count distribution — my honest estimate:**

| | P(12+) | P(10–11) | P(≤9) |
|---|---|---|---|
| Panel (all, t≥2022) | 40% | — | — |
| Comparable cell (same-school, pace₀ 180–240) | 41% | | |
| His pace quartile (same-school <210) | 50% | | |
| **Stockton, my estimate** | **~50%** | **~27%** | **~23%** |

Above the base rate — secure job, no competition, low sack rate, clean 2025,
resolved minor knee — but not dramatically, because the rush volume is real and
because a 41–50% base rate reflects seasons that also began with healthy secure
starters. **This is the number the bet lives or dies on**, and the procedure's
own kill threshold is P(12) ≥ 65%. I do not reach it, so the bet survives — but
see the sensitivity in §7, because it survives narrowly.

---

## Step 3 — Volume audit

**Scheme continuity: CONFIRMED, no volume shock.** `snapshots/Georgia/META.json`
coach_note has HC Kirby Smart Year 11, NO CHANGE, band ×1.00 — but names no OC,
the one genuine repo gap. Filled live: **Mike Bobo returns for his fourth season
as OC**, extended through 2029 at $2.2M for 2026 (AJC, July 2026), a 2025 Broyles
finalist. **No new-OC air-raid risk — the single biggest volume threat to an
under is off the table.**

**Directional read is run-heavy.** DawgNation (2026-01-22) quotes Bill Connelly:
*"I have quite a few questions about the Dawgs' offensive upside in 2026"*; the
plan leans on returning backs Nate Frazier and Chauncey Bowens, with *"a strong
running game would go a long way in easing the burden on Stockton."*

**Georgia's own QB volume history — the most useful number in this section**
(computed from `player_games_flat.csv`, all Georgia QBs, CFBD regular):

| year | g | team QB yd/g | att/g | QB1 share |
|---|---|---|---|---|
| 2022 | 13 | 284.9 | 33.1 | Bennett 92% |
| 2023 | 13 | 305.6 | 32.8 | Beck 94% |
| 2024 | 13 | 284.6 | 37.0 | Beck 94% |
| **2025** | 13 | **220.3** | **29.5** | **Stockton 94%** |

Georgia's passing offense fell **−64 yd/g** the year Stockton took over. The FD
line implies **2650.5 / 12 = 220.9 yd/g for Stockton alone** — i.e. essentially
*Georgia's entire 2025 team QB output*, asking for ~+6.7% growth on his own pace.

**Supporting cast.** Payload unit grades: **WRTE 54**, OL 60, QB 68, RB 70. All
three magazines corroborate a gutted receiver room — six of the top seven WRs
gone including Zachariah Branch (NFL); only London Humphreys returns of the top
five; replacements are GT transfer Isiah Canion (480 yds/14.6 in 2025, ankle-limited
in spring) plus freshmen Talyn Taylor, CJ Wiley, Landon Roldan and TE Kaiden Prothro.
OL lost 1st-round LT Monroe Freeling and G Micah Morris, returns three starters
(Bobo — 2nd-team All-SEC C, Greene, Glover); Pick Six notes the last two Georgia
lines ranked #65/#66 in Run Push.

**Discipline note — I am deliberately NOT crediting the WR argument.** H6
(supporting cast) came back **NULL** at team level (+5.7 yd/g per 100% returning
receiving share, t=+0.3, n=155). The gutted room is the most emotionally
persuasive fact in this file and the panel says it does not predict pace change.
It is logged as colour, not as an input.

**Pace estimate:** central **207–215 yd/g**, range 190–230. The OLS fit says 223;
the team-context and receiver evidence says flat-to-down; I weight them roughly
evenly and land just below his 2025 mark. Against a required 220.9, that is a
modest under lean on the yards leg alone — far weaker than v1 implies.

---

## Step 4 — Schedule walk (repo only)

From `outputs/win_totals_payload.json` via `pipeline/win_engine.py` (HFA 2.3,
σ_game 13.5, BAND_TO_SD 1.0). Georgia rating **26.80**, band 6.00.

| wk | site | opponent | oppR | margin | P(win) | P(blow W) | P(blow L) | opp DB/DL |
|---|---|---|---|---|---|---|---|---|
| 1 | home | Tennessee State (FCS) | −42.00 | +71.10 | 1.000 | 0.999 | 0.000 | — |
| 2 | home | Western Kentucky | −6.67 | +35.77 | 0.992 | 0.896 | 0.000 | 58/40 |
| 3 | away | Arkansas | 4.23 | +20.27 | 0.909 | 0.585 | 0.007 | 48/48 |
| 4 | home | Oklahoma | 18.91 | +10.19 | 0.755 | 0.322 | 0.033 | 60/62 |
| 5 | home | Vanderbilt | 10.36 | +18.74 | 0.897 | 0.547 | 0.008 | 58/48 |
| 6 | away | Alabama | 18.20 | +6.30 | 0.664 | 0.237 | 0.059 | **75**/46 |
| 7 | home | Auburn | 12.58 | +16.52 | 0.863 | 0.487 | 0.013 | 50/59 |
| 9 | neut | Florida | 13.29 | +13.51 | 0.811 | 0.410 | 0.023 | 54/56 |
| 10 | away | Ole Miss | 20.54 | +3.96 | 0.603 | 0.194 | 0.083 | 56/60 |
| 11 | home | Missouri | 13.62 | +15.48 | 0.853 | 0.459 | 0.014 | 47/53 |
| 12 | away | South Carolina | 11.46 | +13.04 | 0.810 | 0.395 | 0.022 | 52/56 |
| 13 | home | Georgia Tech | 5.70 | +23.40 | 0.941 | 0.665 | 0.004 | 48/40 |

**Expected wins 10.10** (FD win total 9.5 −172). Single bye at week 8, splitting
the Auburn and Florida games; no late-season open date and no cold-weather road
site (latest away trip is South Carolina, week 12).

- **E[blowout LOSSES] = 0.27.** This is the killer for the script leg. H9
  established that blowout *losses* are the only state that suppresses passing
  (−51 yd/g); Georgia will essentially never be in one. **No script help.**
- **E[blowout WINS] = 6.20** — very high, and Puglisi's 6-game/27-attempt 2025
  proves Georgia empties the bench. But **H9 found blowout wins NULL** (250 yd/g
  vs 247 competitive, n=605/1118) and the "Georgia leads and runs clock"
  justification was formally **RETRACTED**. Not credited. Also note this
  suppression, whatever its true size, is already inside his 2025 pace₀ of 207 —
  Georgia won plenty of blowouts last year too.
- Weakest pass defences faced: Missouri (DB 47), Georgia Tech (48), Arkansas (48).
  Toughest: **Alabama DB 75** (away, W6). Pick Six calls this *"the SEC's easiest
  schedule"* and picks Georgia to win the SEC.
- **Correlation with the open book:** none. No existing win-total position sits
  on a Georgia opponent. This leg is independent of the 18 open positions.

---

## Step 5 — Market context

**No competing market found.** Searched for season-long CFB passing-yards props
at DraftKings, BetMGM and via aggregators; DraftKings' "Passing Props – Pass
Yards" category is **game-level only**. FanDuel appears to be the sole book
posting this market.

That is a double-edged finding and I will not spin it:

- *For us:* no consensus to fade — we are not betting into a sharp market number,
  and a lone desk pricing 17 marquee names off a mechanical `12 × prior pace`
  anchor is precisely the soft-post condition S20 was built to exploit.
- *Against us:* no line shopping, no steam check, no second opinion, and **no way
  to detect that we are wrong before settlement**. The prereg's soft-market
  caveat is live: first-post limits are low, and season-long props on marquee
  names get profiled fast. Expect a small max bet; at 0.10u that is not binding.

No movement from the 2026-08-03 capture (−113/−113), so there is no "what did the
market learn" question outstanding.

---

## Step 6 — Adversarial pass: the OVER case

**The over is the statistically favoured side conditional on health, and anyone
betting the under should be clear-eyed that they are buying an injury.**

Start with the number that should worry us most: among same-school comparables in
Stockton's pace band who *played 12+ games*, only **32% went under** (6 of 19).
For his own quartile it is **25%** (3 of 12). The under is not winning on yards;
it is winning on absence. And the mechanism pushing the over is the best-supported
relationship in the entire panel — mean reversion, t=5.36. The fit puts Stockton
at **223.3 yd/g → 2,679 yards → over by 29** if he simply plays. His 2025 pace of
207 was not a big season being priced for a fall; it was a *low* season, and low
seasons revert **up** (+14.3 yd/g in Q1, +22.7 same-school). The desk asking for
+6.7% growth from a returning starter is not a shaded number — it is roughly what
the historical fit says will happen.

Layer the development story on top. This is the owner's own confirmed intuition
from H10: year-2 clearcut starters do **not** decay (Δpace −6.1 vs −18.5 for
veterans), because development cancels reversion. Stockton is now a *senior*
entering **year three in Mike Bobo's system**, with his first full offseason as
the unquestioned QB1 — no spring split, no competition, Manning Passing Academy
invite, and a coordinator just paid $2.2M and extended to 2029 on the strength of
a Broyles-finalist season. Athlon's read is that he *"must shrink the gap between
ceiling and floor"* — a QB whose problem is floor variance and who fixes it goes
*up* in yards, not down. His efficiency profile has obvious headroom: aDOT 7.3 is
conservative to the point of being suppressible, 69.7% completions with only 12
turnover-worthy plays, and a 3.3% big-time-throw rate that a defence-first team
deliberately capped. Any downfield uptick from the freshman speed (Taylor, Wiley,
Prothro) converts directly into yards on the same attempt volume.

And the schedule helps the over more than the under. Pick Six calls it the SEC's
easiest and picks Georgia to win the league; the payload has 10.10 expected wins
with **0.27** expected blowout losses — meaning the one script state that
historically suppresses passing is absent, while five games (Oklahoma, Alabama,
Florida, Ole Miss, South Carolina) project close enough to demand full
fourth-quarter passing. Georgia's 2025 attempt rate of 29.5/g was the program's
lowest in four years and sits well below its 2023–24 level of 33–37; regression
in *team* attempts alone gets most of the way to the line. Finally, the desk
knows Georgia better than we do — this is their marquee SEC name, the one where
a mispriced number costs them most, and they still hung 2650.5.

### Observable kill criteria (→ tracker note)

1. **Line moves to 2600.5 or below**, or the price on the under lengthens past
   −125. Either says the market found the same availability story and we no
   longer own it. *(Also the CLV checkpoint.)*
2. **Any August/September report of a designed-run-package expansion, tempo
   increase, or Stockton attempt-share above ~34/game through three weeks.** The
   line needs 220.9 yd/g; at 34 att/g and his 7.5 career YPA that is 255 — the
   under is dead on volume alone.
3. **Ryan Puglisi transfers out or the QB room otherwise empties.** Counter-
   intuitive but correct: it removes the mop-up pull that trims Stockton's
   blowout-win snaps and raises the chance he takes meaningful reps in games
   Georgia leads by 30 — the exact games our 6.20 expected blowout wins predict.
4. *(Soft)* **Structural knee news at any point in camp.** This one flips the bet
   *toward* us, not against — logged so it is not mistaken for a kill.

---

## Step 7 — Verdict and sizing

**BET — 0.10u, floor of the S20 pilot lane. Not the top leg on the board.**

**Final p(under) ≈ 0.59** (range 0.55–0.63). **Edge ≈ +6 points** vs the .5305
breakeven, range +3 to +8. Down from pricer_v1's 0.633 / +10.3.

Derivation of the headline number — the conditional decomposition, which is more
honest than any single cell because it separates what we know from what we are
guessing:

```
P(under) = P(12+ games) × P(under | 12+) + P(<12) × P(under | <12)
         = 0.50 × 0.32 + 0.50 × 0.93
         = 0.625 raw  →  0.5 + 0.70×(0.625−0.5) = 0.588 shrunk  →  edge +5.7
```
`P(under | 12+) = 0.32` and `P(under | <12) = 0.93` are empirical from the
comparable cell (same-school, pace₀ 180–240, n=46) at r=1.067. Only `P(12+)` is
my judgement, raised from the 41% base rate to 50% for job security and sack
profile.

**The three numbers that carry the conclusion:**

1. **P(under | he plays 12+ games) = 32%.** The under is an injury bet, nothing else.
2. **pace₀ = 207.0 puts him in the bottom quartile, where the same-school under
   rate is 54.5% (Δpace +22.7), not the 69.0% pricer_v1 applied.**
3. **P(12+) ≈ 50%** — the whole edge, and the softest input in the file.

**Sensitivity — this is why the size is 0.10u and not 0.15u:**

| P(12+) | p(under) raw | shrunk | edge |
|---|---|---|---|
| 0.41 (base rate) | 0.680 | 0.626 | +9.5 |
| 0.50 (my estimate) | 0.625 | 0.588 | **+5.7** |
| 0.55 | 0.595 | 0.567 | +3.6 |
| 0.60 | 0.564 | 0.545 | +1.5 |
| 0.65 | 0.534 | 0.524 | **−0.7 (dead)** |

A ten-point error on a quantity I cannot observe moves this from actionable to
dead. That is the correct reason to take the floor size, and the correct reason
not to add on a line move in our favour without new availability information.

**Unmodelled upside not in the number:** if FD's passing-yards market excludes
CCGs (unverified — §0), Georgia's SEC-title participation removes ~1 game of
exposure. Worth perhaps +3 to +5 points of edge on its own. **Verifying this text
is the single highest-value outstanding item on this leg** and should be done
before the stake, not after.

**Tracker-ready entry line:**

```
2026-08-04 | FanDuel | Gunner Stockton (UGA) Reg-Season Pass Yds | UNDER 2650.5 | -113 | 0.10u
note: S20 pilot leg 1/≤5. p=.588 (v1 said .633 — pace-level correction, see DD §1B).
      Pure availability bet: P(under|12+ g)=32%. KILL: line ≤2600.5 or price past -125;
      att/g >34 through wk3; Puglisi transfers out. CLV re-check wk0 + at close.
      OPEN: FD house text on CCG inclusion for pass-yds market UNVERIFIED (upside if excluded).
```

**CLV plan:** re-check the line at Week 0 and at season close; log both against
the −113 entry in the CLV ledger alongside the win-total book.

---

## Flags to the owner (no edits made from this process)

1. **`pricer_v1` is mis-specified slate-wide — this is the big one.** It ignores
   pace₀ level. Corrected edges, non-parametric pace-matched estimate (logistic
   in parentheses):

   | QB | pace₀ | r | v1 edge | corrected | Δ |
   |---|---|---|---|---|---|
   | Mestemaker | 316.85 | 0.789 | +8.9 | **+16.4** (n=9, unstable) / (+10.8) | ↑ |
   | Hoover | 289.33 | 0.807 | +9.2 | **+7.6** / (+9.4) | ≈ |
   | Stockton | 207.00 | 1.067 | **+10.3** | **+8.1** / (+7.4) | ↓ |
   | Bachmeier | 208.31 | 1.030 | +9.1 | **+7.6** / (+4.5) | ↓ |
   | Moore | 227.75 | 1.043 | +9.7 | **+6.4** / (+8.0) | ↓ |
   | **Iamaleava** | **175.27** | 1.034 | +9.3 | **−0.7** / (+0.5) | **↓↓ dead** |

   **Iamaleava's leg does not survive the correction** — at 175.3 yd/g he is the
   lowest-pace name on the board and mean reversion points hard against the under.
   His dive should be re-scoped as a likely PASS before it is written. The board's
   ordering inverts: the high-pace transfers (Mestemaker, Hoover) get *better*,
   the low-pace returners get worse.

2. **`FINDINGS_S20_2026-08-03.md` survivor caveat is wrong** and should be
   reframed — the ≥1-snap house rule makes the panel's entry filter correct for
   this market, not a downward bias (§0).

3. **The deep-dive procedure's Step 0 kill switch is mis-specified** — it assumes
   a strict-12 panel basis; CFBD `seasonType=regular` includes CCGs, so
   CCG-inclusion is neutral and CCG-exclusion is a bonus. Neither is a kill (§0).

4. **The H11/H12 grade contradiction is not real** — it is small-n binning noise;
   the continuous grade→Δpace relationship inside year-2 starters is flat
   (t=−0.63). The findings doc should stop presenting those two cells as
   competing evidence (§1B).

5. **Mestemaker's "scheme change" justification in the findings doc is factually
   wrong** — he followed HC Eric Morris from North Texas to Oklahoma State. That
   is scheme *continuity* and it weakens that leg's stated rationale, independent
   of the pace correction that strengthens its price.

---

## Sources

Repo: `data/cfbd/qb_props/{panel_s20.json, player_games_flat.csv, pricer_v1_2026-08-04.json}`,
`data/pff_history/{2021–2024}/passing_summary_*.csv`, `data/pff/PFF_passing_summary.csv`,
`outputs/win_totals_payload.json`, `pipeline/win_engine.py`,
`snapshots/Georgia/{META.json, news.md, magazines.md, pff/unit_QB.csv}`,
`docs/research/{FINDINGS_S20_2026-08-03.md, PREREGISTRATION_S20_2026-08-03.md}`.

External (all dated): FanDuel house rules (retrieved 2026-08-04); AJC, Georgia
coordinator contracts (July 2026); AJC + CBS Sports, Stockton knee (2026-03-31);
DawgNation, Bobo/2026 offensive upside (2026-01-22); Bulldawg Illustrated daily
thread (2026-07-31). The SI "What We Know About Georgia Entering Fall Camp" piece
returned by search is dated **July 2025** and was discarded as wrong-season.

---

## ADDENDUM — v2 reconciliation (2026-08-04, post-review, append-only)

The owner-directed review of this DD's §1B led to pricer v2 (spec registered
before computation; see PRICER_V2_SPEC_2026-08-04.md). Reconciliation:

- **v2 mechanical: p = 0.620, edge +9.0** (strict-12: +9.9). This DD's
  judgment-layer number: p = 0.588, edge +5.7. The gap decomposes exactly:
  v2 uses the base secure hazard P(12+)=0.451 where §7 used 0.50 (job
  security bump — REDUCES the under), and v2's holdout-derived shrink is
  k=0.85 where §7 reused v1's 0.70 (v2's spec beat v1's on holdout Brier,
  0.167 vs 0.229, so the lighter shrink is earned).
- §1B's three ad-hoc estimators (quartile cells, ±30 window, grid-logistic)
  are retired; they served to demonstrate the mis-specification, and v2 now
  supersedes them. The review also found §1B's OLS included <6-game pace₁
  seasons; the restricted refit (slope 0.409, t=5.01) reverts HARDER,
  strengthening rather than weakening the correction.
- **CCG asymmetry (review finding):** if FD's passing-yards market INCLUDES
  CCGs, Georgia's ~50% CCG probability vs the panel's 6% P(g=13) costs this
  leg roughly 5 points of edge (~+4); if it EXCLUDES them, +9.9. The §0
  framing ("neutral vs bonus") was right about the panel but wrong to treat
  the included branch as neutral FOR GEORGIA specifically. This widens the
  honest range to +4…+10 and RAISES the priority of verifying the FD text
  before staking.
- **Verdict unchanged: BET 0.10u, owner approval pending** — now 8th on the
  v2 board rather than 1st on v1's. The sizing logic in §7 (availability is
  the whole edge and the softest input) stands.

---

## RECHECK (2026-08-04, owner-requested; v2-consistent framework, append-only)

Full re-derivation under the machinery now standard across DDs 2-3 (v2
conditionals + judgment hazard + CCG-aware 13th-game mass + k=0.85):

| estimator | p | edge |
|---|---|---|
| v2 mechanical (base secure hazard, panel P(13)=.062) | 0.614 | +8.4 |
| **recheck overlay: P(12+)=.50, CCG-INCLUDED (P13=.23)** | **0.579** | **+4.9** |
| recheck overlay: P(12+)=.50, strict-12 | 0.604 | +7.4 |
| DD 1 original judgment layer (for reference) | 0.588 | +5.7 |

Conditionals at μ̂=230.6: P(under|G=13/12/11/10/9) = .29/.42/.58/.75/.89.

**Reconciliation of the three prior numbers.** DD 1's empirical cell inputs
(P(u|12+)=.32, P(u|<12)=.93) vs the sim's (.42, ~.75-.80 weighted): the .32 is
inside its own CI [13,54] of the sim value; the .93 is validated by the cell's
sub-12 games distribution, which clusters LOW (median 8 games — the missing
seasons are big misses, not 11-game near-misses). The two biases roughly
cancel; DD 1's +5.7 lands almost exactly on the consistent framework's central
value. **The v2-addendum's +9.0 was the outlier** (base hazard, no CCG mass) —
the DD 1 arithmetic was closer to right than its own reconciliation implied.

**New availability datum:** Stockton played through a mid-season **oblique**
injury in 2025 (his own account, DawgNation newsletter, July 2026) in addition
to the resolved spring knee. Both minor and resolved; both consistent with the
"real rush exposure" note in §2. No camp red flags through 2026-08-03
(Bulldawg daily threads running quiet; camp opened on schedule).

**Kill-criteria status:** none triggered. No line information since the
2026-08-03 capture (re-confirm at fill); no Puglisi movement; no tempo
reports.

**RECHECK VERDICT: BET 0.10u REAFFIRMED — central edge ≈ +6 (range +4.9
CCG-included to +7.4 excluded).** Ranking note for the cull: this is now the
THINNEST of the four live legs (Sayin ~+10, Mestemaker ~+10, Moore ~+6,
Stockton ~+6 with the widest CCG sensitivity). If the FD text confirms CCGs
are INCLUDED and the ≤5 cap binds after Carr's dive, this is the natural cut.
