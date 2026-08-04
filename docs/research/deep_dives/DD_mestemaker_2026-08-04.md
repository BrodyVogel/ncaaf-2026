# VERDICT: BET — 0.10u. Honest edge ≈ +10 (range +2 to +15), below v2's mechanical +18.7: the transfer hazard's job-loss mass does not apply to a $7M coach-brought QB, and full scheme continuity is a two-edged fact the mechanical price can't see.

**Drew Mestemaker (Oklahoma State, via North Texas) — FanDuel Regular Season passing yards, UNDER 3000.5 (−113)**
Deep dive per `docs/DEEP_DIVE_PROCEDURE_QBPROPS_2026-08-04.md` incl. its 2026-08-04
corrections block. Dive 2 of 6 (re-cut queue). Author: claude-fable-5, 2026-08-04.
Nothing staked; returns to owner.

**Benchmark prices (per corrected procedure, both quoted):** v1 p=0.619, edge +8.9
(r-clamped transfer ladder). **v2 p_raw=0.755 / p_v2=0.717, edge +18.7** (strict-12
+19.6, immaterial here — see Step 0). This dive's job is the judgment layer on top
of v2; it lands materially below it.

---

## Step 0 — Rules gate

Board-wide findings from DD 1 §0 stand (FD ≥1-snap action rule; dead-heat formula;
CCG text for this market still UNVERIFIED — owner gate). Two Mestemaker-specific
notes:

1. **The CCG question is immaterial for this leg.** OSU's conference win total is
   3.5 (−170/−160); Pick Six's 2025 arc is 1-11. P(B12 CCG) ≈ 0, so panel-basis vs
   strict-12 differ by nothing that matters (+18.7 vs +19.6).
2. **The ≥1-snap rule creates a favorable asymmetry unique to transfers:** if a
   camp shock costs him the job before he ever plays, the bet VOIDS (stake back)
   rather than losing. The under's only losing path is ~12 healthy games at a pace
   that beats 250.0/g. Job-security risk — the thing the transfer hazard mostly
   measures — cannot make this bet lose; it can only void or cash it.

Line U3000.5 −113 per the 2026-08-03 capture; no recheck possible from here
(flag for owner at fill time). Related observation for Step 5: FD's OSU *win
total* (6.5 +116) also sits off the 5.5 −166/−200 consensus at four other books —
FD's desk looks inattentive to OSU markets generally.

## Step 1 — Re-derivation (local data)

From `player_games_flat.csv`: **13 games** (wks 1,2,3,4,5,7,8,9,10,12,13,14,15 —
byes wks 6/11, zero games missed), **4,119 yds, 419 att**, all 13 games ≥10 att.
**pace₀ = 316.85** on the panel-consistent g10 basis ✓ (v1 JSON "317" is the
rounded version; within tolerance). Wk15 = AAC title game vs Tulane (L 21-34,
294 yds); ex-CCG 3,825/12 = 318.75. PFF cross-check: 14 games / 4,381 yds = +1
game (bowl), consistent with CFBD-regular exclusion. Name join clean.

**r = 3000.5 / (12 × 316.85) = 0.789** — FD marked him down 21%.
**v2 reproduced from scratch this session: p_raw = 0.7546 vs JSON 0.755** (<0.01,
no stop). Mechanism: fit μ̂ = 146.0 + 0.409×316.85 − 18.5 = **257.0 yd/g**;
transfer hazard P(12+) = 0.309; P(under | G): 13→0.295, 12→**0.445**, 11→0.622,
10→0.806, 9→0.934.

Read that conditional column once more: **at 12 games this line is a coin flip.**
The 21% markdown prices the pace correctly at the fit's own estimate (250.0
needed vs 257.0 predicted ≈ 0.445 under). The entire mechanical edge above
breakeven is the sub-12 branch. Same shape as Stockton: an availability bet.

## Step 1B — The cell, and what the mechanical price can't see

**High-pace transfers (pace₀ ≥ 270), t≥2022, n=16:** under at their own synthetic
line 14/16 (87.5%); **under at a 0.789-marked line 11/16 (68.8%)** — consistent
with the ADDENDUM-2 transfer ladder (67% at r=0.80). The five who beat the 0.789
discount: Shedeur Sanders (JSU→Colorado, **followed his HC**), Cam Ward
(system-familiar, elite), Dillon Gabriel (elite landing), Mendoza (→Indiana),
Aguilar (→Tennessee).

**The pattern in the beats is the problem: coach/scheme continuity.** Mestemaker
is not a normal transfer. Per the OSU dossier: Eric Morris brought **his OC (Sean
Brophy), his DC, and 18 North Texas players — including Mestemaker, RB1 Hawkins,
WR1 Young, two starting OL, and the long snapper.** This is a program transplant.
The v2 transfer intercept (−18.5) and the transfer hazard (P(12+)=0.309) are
averages over a population whose disruption he mostly won't experience. Two
precedents cut against us and one cuts for us:

- **Cam Ward followed Eric Morris up a level (IWU→WSU, 2022): 256.8 yd/g at 38.7
  att/g.** The single closest analog in the dataset lands ON the v2 fit (257.0)
  — and 12 × 256.8 = 3,082 **beats this line by 81 yards**.
- **Shedeur (the only in-cell continuity case): over his 0.789 line by ~600.**
- **Chandler Morris — the previous NT QB who LEFT the system (→Virginia 2025):
  314.5 → 233.5, UNDER.** (And Chandler Rogers →Cal: job lost, 1 game.) The
  system's alumni collapse when they leave it; Mestemaker isn't leaving it.

**The NT system baseline is the scariest number in this file:** UNT QB1 pace was
**307.5 (Rogers), 314.5 (C. Morris), 316.8 (Mestemaker)** in Morris's three years
— three different QBs, same output. Pick Six: Morris has produced "9 top-5
passing attacks" in 13 years; 2025 NT was **#1 nationally in scoring and total
offense.** The system, not the QB, sets the volume. If it transplants at full
strength, this bet is dead (see sensitivity).

Against full transplant: every one of those seasons came against G5 defenses.
Mestemaker's one 2025 start vs a power-classed opponent (Washington State) is his
second-lowest output, 211 yds. Our own dossier flags "**No P4 tape on the
offensive spine**" as OSU's #1 known gap; the OL is an all-transfer five (unit
grade 44, arrangement still disputed between PS and Athlon in May); and S17's
translation study — for grades, caveat join-limited — found destination strength
adds little *once quality is measured*, which supports the QB himself traveling
but says nothing about a G5 offense's *volume* surviving B12 defenses. Ward's
257 — the follow-Morris precedent — is itself the "system translates at ~80%"
data point.

## Step 2 — Availability audit (the thesis)

**Injury history: clean, unusually so.** Zero games missed at UNT (13/13 in
2025); no injury reports in his Wikipedia/beat coverage at any level; in high
school he wasn't even the starter (backup QB + safety + **punter**) — a
walk-on-trajectory player (Burlsworth Trophy winner) with almost no accumulated
hit load. No adverse camp health reports as of 2026-08-04; OSU players reported
**today** (Aug 4), first practice Aug 5.

**Style exposure: the lowest on the board.** 2025 PFF: sack% **3.8**,
pressure-to-sack **14.7**, avg time-to-throw **2.58s**, only **21 scrambles**
(vs Stockton's 53), 4 hit-as-threw, 0 penalties. Air-raid quick game +
"fast post-snap processing" (P6). He simply doesn't take hits — 19 sacks on 506
dropbacks *behind a UNT line*. Offset: the 2026 OL is nine transfers deep with
zero returning OSU starts (grade 44); B12 fronts (Oregon DL 88 in wk2, Texas
Tech 73 in wk11) are a different bar. Net: below-average injury exposure for the
position, above-average line risk.

**Job security: effectively absolute.** Two-year, **$7M** deal (reported at
signing, Jan 2026); the HC built the entire roster around him; QB2 is Grant
Jordan, a Yale→UMass journeyman (PFF 57.5, 5.2 ypa at UMass) — no bench threat,
and a QB2 that bad means any injury absence produces near-zero replacement yards
(pro-under). 2025 OSU QBs are gone (Flores → Iowa State, Hejny not on the May
two-deep). Per the procedure: an empty room lowers both pull risk and bench risk.

**Game-count distribution (mine vs the machinery):**

| | P(12+) | P(10–11) | P(≤9) |
|---|---|---|---|
| v2 transfer hazard (n=68) | 0.309 | 0.074 | 0.617 |
| v2 secure hazard (n=113) | 0.451 | 0.230 | 0.319 |
| **Mestemaker, my estimate** | **~0.42** | **~0.30** | **~0.28** |

The transfer hazard's sub-12 mass is dominated by job-loss cases (g10 ≤ 4 =
34% of the transfer panel!) — Rogers, Van Dyke, Edwards, Gonzales — that a
$7M coach-brought QB won't reproduce. I place him between the two hazards,
nearer secure, minus a small increment for the OL and the thin one-year hit
history. Procedure kill check: P(12) ≥ 0.65 would kill; I'm at 0.42, and even
0.60 leaves +7.1 (below). **The availability leg is robust here in a way
Stockton's wasn't.**

## Step 3 — Volume audit

**Scheme continuity: total.** Not merely "same system" — same play-caller
lineage (Morris + Brophy, his NT pass-game coordinator), same WR1 (Young, 1,264
@ 18.1), same RB1 (Hawkins, FBS-leading 25 rush TD), two scheme-familiar OL.
There is no volume-*down* scheme risk; the risk runs entirely the other way.
Coach-note ×1.13 band multiplier already reflects operation-wide uncertainty.

**Volume shape:** his 2025 was 32.2 att/g10 — *moderate* attempts at an absurd
**9.4 ypa**. The line's 250/g at his ypa needs only ~27 att/g; at a
translated-down 7.5 ypa it needs ~33. Morris air raids historically run 38-42
att/g when behind (Ward's WSU year: 38.7; C. Morris's NT year: 42.4).
**OSU will be behind a lot** (DL 45 / DB 48; see Step 4) — and his one 2025
blowout loss (36-63 USF) he threw **48 times for 326**. H9's blowout-loss
suppression (−51 yd/g panel-wide) plainly does not describe trailing air raids;
I am crediting ZERO script help to this under despite OSU's 2.14 expected
blowout losses. (Registered honesty: this is the same H9-discipline applied to
Stockton, in the opposite direction.)

**Efficiency translation:** the down-leg. 9.4 ypa led the country against the
AAC (608 vs Charlotte, 469 vs Rice — his two biggest games came against the two
worst defenses he saw). Every published projection of his pace at OSU embeds
some haircut; the v2 fit says −60 (to 257), the Ward precedent says ~257, the
FD desk says 250. **Central estimate: μ ≈ 255–260, range 235–290.** Below 250
the bet prices like +12; at 270 it's ~+2; at 290 it's dead (grid in Step 7).

**Supporting cast:** WRTE 62 (Young + Bowick + Barnes is a real B12 room), RB 67
(Hawkins may pull red-zone/clock share — his 25 TDs came off the board's
biggest rushing role), OL 44 (the drag). PS: "most improved QB position in the
country" — treated as an over-side warning, not comfort.

## Step 4 — Schedule walk (repo only)

OSU rating **5.60**, band 7.46 (coach ×1.13). **EW 6.22** vs market 5.5/6.5.
E[blowout W] 2.57 (Murray St, Tulsa-ish), **E[blowout L] 2.14** (Oregon-home
0.666, TTech-home 0.462, @Houston 0.220, @KSU 0.235) — not credited as under
help per Step 3. Byes wks 5→(after wk4)... open dates fall after wk4 and wk10
(12 games, wks 1–13). No late-November cold-weather road trip worse than
@Kansas State (wk10).

| wk | site | opp | oppR | P(win) | opp DB/DL |
|---|---|---|---|---|---|
| 1 | away | Tulsa | −7.00 | 0.756 | 58/40 |
| 2 | home | **Oregon** | 31.23 | 0.057 | **73/88** |
| 3 | home | Murray State (FCS) | −41.00 | 0.998 | — |
| 4 | away | West Virginia | 0.51 | 0.575 | 40/42 |
| 6 | home | UCF | 2.85 | 0.634 | 58/50 |
| 7 | away | Houston | 8.88 | 0.353 | 60/53 |
| 8 | home | Colorado | 0.88 | 0.683 | 46/57 |
| 9 | away | Iowa State | −0.13 | 0.586 | 40/46 |
| 10 | away | Kansas State | 9.40 | 0.343 | 52/45 |
| 11 | home | **Texas Tech** | 23.50 | 0.145 | **70/73** |
| 12 | away | Arizona State | 4.93 | 0.456 | 48/51 |
| 13 | home | Kansas | 2.91 | 0.632 | 42/50 |

Outside Oregon/TTech, the B12 secondaries he faces grade 40–58 — soft. The wk2
Oregon game is the season's translation diagnostic (kill criterion 3).

**Correlations with the open book (4 real overlaps + 1 prospective):**
- **Tulsa OVER 5.5 (1.10u total, wk1 opponent): POSITIVE** — OSU-bad worlds help
  both. This is the book's largest single-team stake and it points the same way.
- UCF conf OVER 3.5 (0.55u, wk6): positive, small.
- WVU UNDER 5.5 (0.50u, wk4) and ASU UNDER reg+conf (0.95u, wk12): mildly
  NEGATIVE (they cash when OSU beats those teams).
- Prospective Moore leg (DD 5): Oregon @ OSU wk2 links the two unders weakly
  positively. Net book effect: small and two-sided; acceptable at 0.10u.

## Step 5 — Market context

FanDuel remains the only book with this market (DK's CFB passing props are
game-level). No consensus to check, no steam visible from here; the 2026-08-03
capture is the only price. FD's simultaneous off-market OSU win total (6.5 +116
vs 5.5 −166 consensus) suggests the OSU page is not getting desk attention —
supports the soft-line thesis, but also means the number could be stale in
either direction. Low first-post limits assumed per prereg; 0.10u is not
binding. **Owner should re-confirm line/juice at fill time.**

## Step 6 — Adversarial pass: the OVER case

Take the over seriously, because three of the five historical beats of this
discount looked exactly like him. Mestemaker is the reigning national passing
champion (4,379), PFF 86.1, the No. 3 transfer QB of the cycle, on a $7M deal —
programs do not pay that to hand off. The offense around him is not a rebuild;
it is his own offense, airlifted: his coordinator, his 1,264-yard WR1, his
25-TD running back, his center, in a scheme whose author has produced nine
top-5 passing attacks in thirteen years at four different schools. The system's
volume is proven portable — Morris's attacks hit top-5 at Incarnate Word, at
Washington State with a followed QB (Ward, 256.8/g as a first-year P5 QB — over
this line), and at North Texas with three different QBs above 307. The line
needs only 250. OSU's defense (DL 45/DB 48) guarantees trailing scripts, and
his own tape shows what he does trailing: 48 attempts, 326 yards in a 27-point
loss. Nine of his twelve B12 opponents field secondaries graded below 60. The
desk that posted 3000.5 also posted an OSU win total a full point off
consensus — this may be a stale page, not a sharp one, and stale can be stale
in our faces. If the transplant holds at even 85% strength (≈270/g), the under
is roughly breakeven; at 90% it is dead.

**Kill criteria (tracker note):**
1. **Line ≤ 2900.5 or under juice past −125** — market has found it; no chase.
2. **Volume: ≥40 att/g or >270 pass yd/g through wk 3** (Tulsa/Oregon/FCS) —
   the transplant is holding; dead.
3. **Wk2 vs Oregon ≥ 300 yds** — the one elite-defense diagnostic on the
   schedule; combined with (2), kill; alone, watch.
4. *(Not a kill — a scratch:)* loses the job pre-snap-1 → bet VOIDS.

## Step 7 — Verdict + sizing

**BET — 0.10u** (pilot floor). **Final p(under) ≈ 0.62** (v2-machinery overlay
at my hazard), **edge ≈ +9 to +11** vs .5305 — a large haircut from the
mechanical +18.7, for the same reason Stockton got one: the population hazard
is not this QB's hazard.

Two-axis sensitivity (v2 machinery, k=0.85; edge in pts):

| | μ=245 | μ=257 | μ=270 | μ=290 |
|---|---|---|---|---|
| P(12+)=0.31 (transfer base) | +20 | **+18.7** | +15 | +9 |
| **P(12+)=0.42 (mine)** | +12 | **+11.0** | ~+2 | dead |
| P(12+)=0.55 | +10 | +9.0 | ~0 | dead |
| P(12+)=0.60 | +8 | +7.1 | −1 | dead |

**The three numbers that carry the conclusion:**
1. **P(under | G=12) = 0.445** — at full health this is a coin flip; the edge
   is the sub-12 branch plus the desk's markdown being merely fair, not sharp.
2. **P(12+) ≈ 0.42** — above the 0.309 transfer base ($7M, coach-built roster,
   no bench threat) but below secure (all-transfer OL, one-year hit history).
3. **μ ≈ 257** — the fit and the lone follow-Morris precedent (Ward 256.8)
   agree; the bet survives anything below ~268 and dies above ~275.

Why 0.10u and not 0.15u: the μ axis. The one input with no historical anchor is
whether a #1-in-the-nation G5 offense transplants to a P4 at ≥85% strength —
our own dossier calls this exact unknown OSU's top known gap, and the bet is
dead if the answer is yes. Floor size, kill criteria armed.

**Tracker-ready entry:**
```
2026-08-04 | FanDuel | Drew Mestemaker (OKST) Reg-Season Pass Yds | UNDER 3000.5 | -113 | 0.10u
note: S20 pilot leg 2/≤5. p=.62 (v2 mech .717 — hazard overlay, see DD §2). Availability
      bet w/ pace coin-flip at G=12. KILL: line ≤2900.5/juice -125; ≥40 att/g or >270 yd/g
      thru wk3; wk2 @ Oregon ≥300. Job-loss pre-W1 = VOID (≥1-snap rule). Correlated:
      Tulsa O (+), UCF conf O (+), WVU U/ASU U (−), Moore leg via wk2. CLV: wk0 + close.
```

## Flags to the owner

1. **v2's transfer hazard needs a job-security split before the next transfer
   leg (Hoover, DD 3).** 34% of the transfer panel's mass sits at g10 ≤ 4 —
   overwhelmingly job-loss, not injury. A coach-brought/paid-QB flag would
   move transfer prices a lot. Candidate spec: split transfer hazard by
   "arrived with returning HC/OC" — needs a hand-built flag, ~68 rows.
2. **Same-school continuity precedents beat the 0.789-type discounts (Shedeur,
   Ward)** — n=2, but both in the exact structural situation Mestemaker is in.
   Logged as the honest anti-thesis; it is why the size is the floor.
3. FD's OSU page (win total 6.5 +116 vs consensus 5.5) is off-market — worth a
   look as a standalone OSU-under-6.5-at-plus-money... except our own EW is
   6.22, so no: it's roughly fair by our number. Noted only as desk-attention
   evidence.
4. S17-L3's destination-null (grades translate on quality, not destination
   level) is join-limited (505/1,035) — task #313 remains open; do not lean on
   it for pace conclusions in later dives.

## Sources

Repo: `player_games_flat.csv`, `panel_s20.json`, `pricer_v1/v2_2026-08-04.json`,
`outputs/win_totals_payload.json` + `pipeline/win_engine.py`, `outputs/bet_tracker.csv`,
`snapshots/Oklahoma_State/{META.json,news.md,magazines.md,pff/unit_QB.csv}`,
`data/pff/PFF_passing_summary.csv`, `data/pff_history/2024/…`,
`docs/research/{FINDINGS_S20…, FINDINGS_S16…, FINDINGS_S17…, PRICER_V2_SPEC…}`.

External (dated): Wikipedia "Drew Mestemaker" (retr. 2026-08-04: HS backup/punter,
walk-on trajectory, Burlsworth, $7M/2yr deal, clean injury record); SI/Oklahoma
State fall-camp schedule (2026-07-30: report Aug 4, first practice Aug 5, no QB
battle listed); ESPN + CBS Sports transfer stories (Jan 2026: commit, follows
Morris); stwnewspress camp preview (fetch blocked, 429 — not used). Magazine
claims via the frozen snapshot layer (P6 pp.116-117, Athlon B12 p98, PS B12 —
including P6's "national passing champ… #3 transfer QB," PS's "most improved QB
position in the country," and the Athlon anonymous B12 assistant: "Mestemaker is
special… he's a quick processor.").
