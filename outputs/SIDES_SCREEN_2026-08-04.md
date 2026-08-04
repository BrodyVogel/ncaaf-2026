# Single-Game Side Screen — posted-lines capture, 2026-08-04

**Question asked:** "Any lines showing a lot of value on our numbers?" — on the single-game
spreads in the 2026-08-03 20:33 ET capture (`data/market/spreads_wk01_goty_2026-08-03.csv`,
117 rows: Week 0, Week 1, and Game-of-the-Year boards).

**Answer: no bets. Zero recommendations.** Two independent reasons, either one sufficient.

1. **Preregistered.** S14 flushed "our board disagrees with the posted spread" as a betting
   signal. That decision is already binding and this capture is exactly the population it
   was tested on.
2. **The screen's own finding.** The largest disagreements here are not game-level
   mispricings. When decomposed, they are **team-level rating differences** — and the ones
   that are identifiable replicate cleanly in those teams' *other* capture games, which is
   the signature of our rating being off, not the line being off.

The screen's real product is diagnostic: a list of teams where the spread market
disagrees with our raw ratings, and a read-through onto the open win-total book.

Artifacts: `outputs/sides_screen_2026-08-04.csv` (58 sign-stable games),
`outputs/sides_book_read_2026-08-04.csv` (20 open positions).

---

## 1. The governing decision (S14, 2026-07-31)

From `docs/research/FINDINGS_S14_2026-07-31.md`:

> Sides at market prices are DROPPED from the 2026 program as consensus-disagreement
> plays — Week 0/1 and GOTY spreads do not qualify on "our board disagrees with the line,"
> because the board's dominant component (consensus) is now proven unprofitable against
> this market.

Panel: 3,568 FBS-FBS games, 2021–25. S14-A (weeks 0–3, |D| ≥ 3, vs close) **48.6%**
(n=395). S14-B (vs openers) **48.4%** (n=382). Per-year: 2021 60.5%, then 46.4 / 45.3 /
44.4 / 46.0 — the 2021 number is a COVID-dislocation artifact that has since been
arbitraged away.

S14-D tested whether a bigger disagreement redeems it. It does not: the 8+ point cells hit
64.3% on n=14 (early noise) and **49.2% on n=585** (late), with nothing monotone in
between. The loud-disagreement pattern that works on totals does **not** rhyme on sides.

`pipeline/price_game.py` carries this banner. The only door back in is S8c (December) →
a registered 2027 retry. Everything below is paper only.

## 2. Method and the controls applied

**Lens.** Compared on the `raw` lens. Raw is the unshrunk final rating and it is the
spread market's own scale (slope 1.02, corr 0.978 per `SPREAD_CALIBRATION_2026-08-03.md`).
Using `calibrated` here would manufacture edges out of shrinkage. A raw-lens delta maps to
the calibrated lens by ×0.75.

**Error identity.** For each game,

```
err(g) = model_home_spread(HFA) − posted_home_spread = d_home − d_away
d_t    = (market's rating of t) − (our raw rating of t)
```

So **err > 0 ⇒ the market rates the HOME team higher than we do ⇒ our value is on the AWAY
side.** (This sign was inverted in a first draft of the screen; the derivation is now in the
script docstring.)

**Control 1 — HFA.** Our house constant is 2.3; the market-implied constant is ~3.5. Every
game is computed at both, and only games whose error **sign** survives both are kept, at
the smaller magnitude. 11 of 69 flipped and were dropped. All 11 are small (|e| ≤ 1.2 in
both) — they are HFA artifacts, not lost edges:

| game | posted | e@2.3 | e@3.5 |
|---|---:|---:|---:|
| Clemson @ LSU | −9.5 | +0.07 | −1.13 |
| Western Kentucky @ Nevada | +3.0 | +0.16 | −1.04 |
| Northern Illinois @ Iowa | −30.5 | +0.19 | −1.01 |
| Missouri @ Kansas | +6.5 | +1.04 | −0.16 |
| SMU @ Florida State | +1.5 | +0.95 | −0.25 |
| USC @ Indiana | −10.0 | +0.94 | −0.26 |
| Oklahoma @ Michigan | −2.5 | +0.82 | −0.38 |
| Boston College @ Cincinnati | −7.5 | +0.40 | −0.80 |
| Colorado @ Georgia Tech | −7.5 | +0.77 | −0.43 |
| Sam Houston @ Troy | −16.0 | +0.46 | −0.74 |
| Virginia @ Virginia Tech | −2.5 | +0.51 | −0.69 |

**Control 2 — FCS tier.** FCS-at-FBS rows carry mean error ≈ +9 in every lens: they measure
our FCS tier calibration, not the FBS host. Excluded. 117 rows → **69 FBS-FBS games**
(43 Week 1, 18 GOTY, 8 Week 0) covering **103 teams**.

**Control 3 — book depth.** `n_books` runs 1 to 14. Eight of the sign-stable rows are
single-book. Those are one shop's opinion, not consensus, and are flagged in the CSV.

**Aggregate fit after controls:**

| HFA | MAE | mean | sd |
|---|---:|---:|---:|
| 2.3 (house) | 2.45 | **+1.02** | 3.01 |
| 3.5 (market) | 2.34 | **−0.09** | 2.96 |

Slope of ours on posted 0.941, corr 0.979. The mean going from +1.02 to −0.09 is the HFA
gap in one number: at 2.3 we are systematically too kind to road teams.

**Control 4 — localization and identifiability.** This is what turns the screen from a bet
list into a diagnostic. A raw game-level gap cannot say *which* of the two teams is
mispriced. Two tools:

- *Localization.* `d_t from game g = d_in(g,t) + mean(d_in over the opponent's OTHER capture
  games)`. This nets the opponent's read out and moves the residual onto the team of interest.
- *Identifiability.* If the opponent appears in no other capture game, the pair is
  **unidentifiable** — there is no evidence which side of it is wrong, and a 50/50 split is
  all the data supports. Localized numbers in that case are **upper bounds, not estimates**.

Census of the 58 sign-stable games: **15 identified** (opponent has ≥2 other games),
**11 partial** (exactly 1), **32 unidentifiable**. Of the 15 games with edge ≥ 3.0 points,
only **4** are identified.

## 3. The screen output

Top 20 sign-stable disagreements. `edge` is the conservative-HFA magnitude.
`team read` is the localized delta on the value side (+ = market rates them higher than we
do); `ident` is whether that read is supported by the opponent's other games.

| game | bk | posted | ours | edge | value side | oppG | ident |
|---|---:|---:|---:|---:|---|---:|---|
| East Carolina @ Alabama | 8 | −28.5 | −19.3 | **9.19** | East Carolina +28.5 | 3 | yes |
| Ohio State @ Texas | 8 | −1.5 | +5.2 | **6.66** | Ohio State +1.5 | 2 | yes |
| North Texas @ Indiana | 8 | −40.5 | −34.8 | **5.66** | North Texas +40.5 | 2 | yes |
| Coastal Carolina @ West Virginia | 8 | −21.0 | −15.7 | 5.30 | Coastal Carolina +21.0 | 0 | no |
| Ohio @ Nebraska | 8 | −24.0 | −19.6 | 4.37 | Ohio +24.0 | 0 | no |
| Oklahoma State @ Tulsa | 8 | +13.5 | +8.1 | 4.22 | Tulsa +13.5 | 1 | partial |
| San José State @ USC | 8 | −38.5 | −34.4 | 4.15 | San José State +38.5 | 2 | yes |
| Liberty @ James Madison | 8 | −6.5 | −11.7 | 4.03 | James Madison −6.5 | 0 | no |
| Jacksonville State @ North Dakota State | 8 | −7.5 | −12.7 | 3.99 | North Dakota State −7.5 | 0 | no |
| Memphis @ UNLV | 8 | −5.5 | −1.5 | 3.97 | Memphis +5.5 | 1 | partial |
| Ball State @ Ohio State | 8 | −50.5 | −55.5 | 3.77 | Ohio State −50.5 | 0 | no |
| Arkansas @ Utah | **2** | −7.5 | −12.4 | 3.73 | Utah −7.5 | 0 | no |
| New Mexico State @ Florida State | 8 | −30.5 | −26.9 | 3.61 | New Mexico State +30.5 | 1 | partial |
| Missouri State @ Texas A&M | 8 | −39.0 | −35.7 | 3.27 | Missouri State +39.0 | 1 | partial |
| Arkansas State @ Memphis | 8 | −10.5 | −14.9 | 3.25 | Memphis −10.5 | 0 | no |
| Texas State @ Texas | 8 | −30.5 | −27.6 | 2.89 | Texas State +30.5 | 2 | yes |
| Texas @ Oklahoma | **1** | +6.5 | +3.8 | 2.71 | Oklahoma +6.5 | 2 | yes |
| BYU @ Utah | **1** | −3.0 | −0.4 | 2.63 | BYU +3.0 | 1 | partial |
| Wisconsin @ Notre Dame | 8 | −20.5 | −23.1 | 2.57 | Notre Dame −20.5 | 0 | no |
| Oregon @ Oklahoma State | 5 | +17.5 | +20.1 | 2.56 | Oregon −17.5 | 1 | partial |

Note the composition problem immediately: the biggest numbers sit on FBS-vs-low-major
blowout lines (−28.5, −40.5, −38.5, −50.5, −39.0, −30.5). Those are lines where a rating
disagreement mechanically produces a large point gap without implying anything is
mispriced — and they are the least liquid, most number-shaded lines on the board.

## 4. Why the top three are not bets

**East Carolina @ Alabama (gap 9.19).** Alabama's three other capture games price at
**+1.9 (Georgia), +1.2 (LSU), +1.8 (Auburn)** — tight, consistent, and small. So roughly
1.6 of the 9.19 is Alabama and **~7.6 is East Carolina.** Well identified. This is not a
line to bet; it is the spread market telling us our East Carolina rating is ~7.5 points too
high. See §6 — we hold ECU over 7.5.

**Ohio State @ Texas (gap 6.66).** Texas reads **+2.9** (Texas State) and **+2.7**
(Oklahoma) in its other games — very tight. Ohio State reads **−5.0** (Ball State),
**−0.6** (Indiana), **−3.1** (Michigan) — scattered but uniformly negative. Two team-level
reads that replicate out of sample account for essentially the entire gap. There is nothing
left over that is specific to this game.

**North Texas @ Indiana (gap 5.66).** Indiana reads **+0.6** and **−0.3** in its other two
games — dead on our number. So the whole gap localizes onto **North Texas ≈ −5.5**. Again:
one team's rating, not one game's price.

**The unidentifiable class.** Coastal @ WVU (5.30), Ohio @ Nebraska (4.37), Liberty @ JMU
(4.03), JaxState @ NDSU (3.99) — both teams appear once. A 50/50 split is the honest read
and there is no evidence for anything sharper.

**The thin-book class.** Arkansas @ Utah (2 books) and BYU @ Utah (1 book) give Utah
*contradictory* signs, **−4.9** and **+2.6**. Single- and double-book rows are not consensus
and should not be treated as such.

## 5. Team reads that replicate across more than one capture game

(+ = the market rates them **higher** than our board does. Raw lens, HFA 3.5.)

| team | mean | sd | n | sign-consistent |
|---|---:|---:|---:|---|
| Memphis | **−4.21** | 0.34 | 2 | yes |
| Texas | **+4.09** | 2.23 | 3 | yes |
| Oklahoma State | +3.99 | 2.02 | 2 | yes |
| Ohio State | **−3.82** | 2.61 | 4 | yes |
| Alabama | +3.54 | 3.78 | 4 | yes |
| Miami | +3.14 | 0.62 | 2 | yes |
| Stanford | −3.04 | 0.76 | 2 | yes |
| Oregon | −2.84 | 0.39 | 2 | yes |
| San José State | −2.80 | 1.90 | 2 | yes |
| Notre Dame | −2.63 | 0.09 | 2 | yes |
| Iowa | −2.15 | 1.61 | 2 | yes |
| Indiana | +2.00 | 3.20 | 3 | **no** |
| USC | +1.83 | 2.05 | 3 | yes |
| Hawai'i | +1.77 | 1.03 | 2 | yes |

Memphis is the cleanest signal on the board: n=2, sd 0.34, both signs the same — our board
rates Memphis about 4.2 points above the market and does so consistently. Alabama's +3.54
is inflated by the disputed ECU game; **ex-ECU it is +1.63**, which is the number to carry.

These are ratings-maintenance inputs, not bets. They go on the watch list in §7.

## 6. Read-through onto the open win-total book

Method: for each open position, solve by bisection for the raw-lens delta the **win-total
market** implies (`WTd`, from the de-vigged fair probability we priced against), then compare
it to the delta the **spread market** implies (`SPD`) via localization. Three independent
numbers on the same team. `r = SPD_split / WTd` is the ratio: r ≈ 0 means the spread market
backs our number; r ≥ 1 means it has gone past the win-total market, away from us.

`SPD_up` is the full-attribution upper bound; `SPD_sp` is the honest split estimate where
the opponent is unidentified. Reprice uses `SPD_sp` mapped ×0.75 onto the calibrated lens.

| position | stk | WTd | SPD_up | SPD_sp | oppG | p now | p split | move | r | dir |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| East Carolina over 7.5 | 0.55 | −3.74 | −7.54 | **−7.54** | 3 | 61.2% | **35.8%** | **−25.4** | **2.02** | against |
| Arizona State under 6.5 | 0.55 | +3.61 | +5.04 | +5.04 | 1 | 60.9% | 43.0% | −17.9 | 1.40 | against |
| Arizona State under 4.5c | 0.40 | +3.93 | +5.04 | +5.04 | 1 | 61.3% | 44.1% | −17.2 | 1.28 | against |
| Tulsa over 5.5 | 1.10 | −5.26 | −2.86 | −2.86 | 1 | 66.0% | 56.4% | −9.6 | 0.54 | against |
| West Virginia under 5.5 | 0.50 | +2.74 | +5.30 | +2.65 | 0 | 51.5% | 42.1% | −9.4 | 0.97 | against |
| Liberty under 8.5 | 0.60 | +5.00 | +5.23 | +2.62 | 0 | 70.1% | 62.0% | −8.1 | 0.52 | against |
| Hawai'i under 7.5 | 0.60 | +2.27 | +1.97 | +1.97 | 1 | 61.8% | 55.1% | −6.7 | 0.87 | against |
| Illinois under 7.5 | 0.65 | +2.84 | +2.49 | +1.25 | 0 | 67.9% | 63.9% | −4.0 | 0.44 | against |
| Wake Forest over 5.5 | 0.90 | −3.12 | −2.38 | −1.19 | 0 | 63.4% | 59.5% | −3.9 | 0.38 | against |
| Rutgers over 4.5 | 0.80 | −4.80 | −1.45 | −0.72 | 0 | 70.8% | 68.6% | −2.2 | 0.15 | against |
| Pittsburgh under 5.5c | 0.65 | +2.90 | +0.62 | +0.31 | 0 | 65.3% | 64.4% | −0.9 | 0.11 | against |
| Florida under 4.5c | 0.50 | +2.65 | +0.58 | +0.29 | 0 | 58.3% | 57.4% | −0.9 | 0.11 | against |
| Florida under 6.5 | 0.40 | +3.36 | +0.58 | +0.29 | 0 | 49.7% | 48.8% | −0.9 | 0.09 | against |
| Oregon State over 3.5 | 0.65 | −5.33 | −0.71 | −0.36 | 0 | 72.6% | 71.7% | −0.9 | 0.07 | against |
| Wisconsin under 6.5 | 0.60 | +2.22 | −0.13 | −0.13 | 1 | 56.8% | 57.2% | +0.4 | −0.06 | **supports** |
| UConn over 5.5 | 1.07 | −5.51 | — | — | — | 65.7% | — | — | — | no game |
| Bowling Green over 4.5 | 1.05 | −4.33 | — | — | — | 72.8% | — | — | — | no game |
| Buffalo over 5.5 | 0.75 | −3.40 | — | — | — | 69.5% | — | — | — | no game |
| Kennesaw State over 6.5 | 0.55 | −2.56 | — | — | — | 55.0% | — | — | — | no game |
| UCF over 3.5c | 0.55 | −2.44 | — | — | — | 59.5% | — | — | — | no game |

### 6a. The selection-effect caveat — read this before reacting to the table

**12 of the 13 positions with a measurable spread read point against us.** A naive sign test
puts that at p ≈ 0.003. **That number is wrong and should not be quoted.**

Every position on this book was chosen *because* our board disagrees most with the win-total
market. Any independent measurement of our rating error, evaluated on that selected set,
will read adverse on average — that is what selecting on disagreement does. The correct
reading is directional, not inferential: it tells us where to look, not how much to update.

What survives the caveat is **magnitude and identifiability**, not the count. Most of the
column is small: eight of the thirteen move under 5 points of probability, and the four
largest `r` values carry the whole story.

### 6b. East Carolina — the one position worth flagging

ECU is the only held position where the spread market's disagreement is **both large and
identified**. Three independent numbers:

| source | implied raw delta | E[wins] | P(over 7.5) |
|---|---:|---:|---:|
| our board | 0 (by construction) | 7.96 | 61.2% |
| win-total market | −3.74 | 7.32 | (fair, de-vigged) |
| spread market (Alabama-pinned) | **−7.56** | 6.65 | **35.7%** |

Both markets point the same direction against the over, and the sharp market is roughly
twice as harsh as the soft one (r = 2.02). Alabama's other three games price to
+1.9 / +1.2 / +1.8, so the attribution onto ECU is not an artifact of one loose opponent.

This does not automatically mean sell — it is one game's read, at a −28.5 number where a
few points of rating error is worth very little to the bettor on either side, and our
position was taken on the win-total market's price, not Alabama's. But it is the single
strongest external disagreement on the book and it warrants a manual re-read of the ECU
case before Week 0.

Arizona State (r 1.28–1.40) is the second flag, but on a 3-book line with a partially
identified opponent (Texas A&M reads +3.3 in its one other game) — much weaker evidence.

Wisconsin is the only position the spread market **supports**.

## 7. Decision and what goes on the watch list

**Bets recommended: none.** Nothing is staked. This is consistent with S14 and reinforced
independently by §4.

**These do not qualify as T2 paper-track candidates either.** Per
`docs/SINGLE_GAME_PROGRAM_2026-07-31.md`, T2 requires a **reason code** — injury/depth,
performance-vs-market divergence, spot, or other. Every item on this screen has the reason
code "our board disagrees," which *is* the flushed lane. Manufacturing T2 entries out of
S14 residue would be laundering a dead signal through a live process. Declined.

**What is registered instead — a zero-stake CLV observation set.** Preregistered here, to be
graded at Week 1 close, no money either way:

- **Prediction:** if these gaps were market error, the lines should drift toward our numbers
  by close. If they are our rating error, they should not — or should drift away.
- **Set:** the 15 identified sign-stable games in `outputs/sides_screen_2026-08-04.csv`,
  plus the four unidentifiable 4+ point games as a control arm.
- **Grading:** signed movement of the posted number toward our raw number, in points, at
  Week 1 close vs this 2026-08-03 capture. Reported, not acted on.

**Ratings watch list (maintenance, not betting):** Memphis (−4.21, sd 0.34, our board's most
consistent overrate on this capture), East Carolina (−7.5, identified), North Texas (−5.5,
identified), Ohio State (−3.8, n=4), Texas (+4.1, n=3), Oklahoma State (+4.0), Alabama
(+1.6 ex-ECU), Miami (+3.1), Stanford (−3.0), Oregon (−2.8), Notre Dame (−2.6).

**Standing item confirmed:** the BGSU F1 tag stays live — Tarleton @ BGSU posted −2.5 is an
FCS row and excluded from this screen, so it is untouched by anything above.

## 8. Queue additions from this run

1. **Push the name aliases into the repo join layer.** Four FBS display-name mismatches
   (`Hawai’i` curly apostrophe → `Hawai'i`, `Miami (FL)` → `Miami`, `UMass` →
   `Massachusetts`, `Appalachian State` → `App State`) silently dropped 7 FBS-FBS games
   from an earlier pass (62 → 69, including both Hawai'i games). Currently patched in
   scratch scripts only. This is a real data-integrity bug and it will recur on the next
   capture.
2. **HFA study on the 2021–25 archive before touching the 2.3 constant.** The +1.02 → −0.09
   mean shift is now the third independent measurement pointing at ~3.5. Do not change the
   constant off a 69-game preseason capture.
3. **§5 of `SPREAD_CALIBRATION_2026-08-03.md` is superseded** for the per-team reads. Those
   were full-game attributions; the localized numbers here correct them (ECU −10.4 → −7.5;
   WVU +6.5 → +2.65 split and unidentified; Liberty +4.0 → +2.62 split).

---

*Generated by `pipeline/sides_screen.py`. Capture: `data/market/spreads_wk01_goty_2026-08-03.csv`,
117 rows, 2026-08-03 20:33 ET. Model constants: HFA 2.3 house / 3.5 market, σ_game 13.5.*
