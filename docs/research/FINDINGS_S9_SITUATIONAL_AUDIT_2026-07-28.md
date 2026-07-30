# S9 situational-bias audit — findings (2026-07-28, diagnostic; no bars)

Owner question: are our "edges" really miscalibrated reads of common situations
(QB battles, turnover, new HC, luck, thin tape)? Script: pipeline/research/
s9_situations.py. Panel for history = s8b_panel (n=516, 2022–25); 2026 board from
final_pass ASSEMBLY + dossier confidences + spine/portal tape flags. Six flags ×
two families tested — expect ~0.3 false |t|≥2 by chance; three hit, two of which
replicate S6 independently. Flags are correlated (disruption cluster): likely ONE
underlying effect seen through several windows.

## B. Does CONSENSUS misprice the situation? (miss ~ sp_pre + flag)

| flag | coef (pts) | t | verdict |
|---|---|---|---|
| new HC | −1.54 | −1.98 | borderline REAL: consensus too optimistic on HC changes |
| returning %PPA | +3.20 | +2.28 | REAL (replicates S6-F2): continuity underweighted ⇒ turnover teams miss |
| thin tape (bottom-quintile evidence) | −1.94 | −2.13 | REAL-ish: unknown rosters miss |
| new QB1 (top-vol QB gone) | −0.45 | −0.68 | nothing |
| lucky prior year | −0.18 | −0.69 | nothing (replicates S6-F1) |
| high turnover (tape ret share) | +2.62 | +1.06 | same direction as %PPA, noisier window |

Reading: a coherent DISRUPTION effect ≈ −0.5 wins of settlement headwind for a
heavily disrupted roster vs its preseason SP+. Luck is clean (SP+ play-based).
Reconciliation with S7-K3 (low totals beat their LINES 4/4 years): both true —
disrupted teams mildly miss consensus while beating over-lowered market lines;
bets settle vs lines, so K3 is the controlling evidence for LOW-TOTAL overs and
already nets this headwind. The headwind bites un-covered spots: disruption OVERS
at mid/high totals.

## B2. Arm × situation (miss ~ sp + R + flag + R×flag)

Only %PPA interacts: +0.132, t +2.09 — the mechanical arm's signal is stronger on
HIGH-continuity rosters and weaker on turnover rosters (formula runs on returning
tape; where the roster is new it guesses). Consistent with Phase-1 curation gaps.

## A. 2026 board and book

Board-level: our applied adjustments are CAUTIOUS on the flagged categories —
corr(adj, flag): QB-battle −0.24 (mean adj −0.64 vs +0.13), thin-tape −0.18,
G5 −0.36, luck −0.10. The dossier's average instinct points the same direction as
the measured consensus biases. No aggregate miscalibration detected.

Book-level (14.17u gross): the HELD positions are concentrated overrides of that
caution — net-directional exposure: G5 +5.27u, QB-battle +3.47u, thin-tape +3.27u,
new-QB1 +3.12u, high-turnover +2.92u, new-HC +0.82u, lucky-2025 −1.65u (short).
The book is long exactly the categories where consensus errs optimistic and the
arm is weakest — BUT most of that tonnage is low-total overs where K3 coverage
applies (Buffalo, BGSU, Nevada, OSU, Wake, Rutgers, UConn, Tulsa).

## Watchlist implications (no forced action; sizing per owner)

- Headwind-adjusted consensus gaps (≈−0.5 w for heavy disruption): Buffalo +1.5→~+1.0,
  BGSU +1.4→~+0.95 (both stay in the S7 zone); Nevada/Tulsa +0.8→~+0.3 (macro-covered);
  **ECU O7.5 +0.47→~0.0 — disruption over at a HIGH total, no macro cover, QB battle:
  now the weakest ticket in the book alongside KSU** (loud arm against + disruption
  flags + lucky-2025). UConn unchanged (known dossier wager; macro-covered).
- Florida under benefits: new-HC headwind is on our side there. Short-luck tilt
  (ASU/Hawai'i/Illinois unders): neutral per F1 — no help, no harm.
- Completion-round design note: prefer candidates WITHOUT disruption flags for overs,
  and note disruption UNDERS at mid totals get the headwind as a tailwind.
- 2027 candidate: a small disruption prior (−0.3..−0.5 w) on heavily-disrupted teams
  at the consensus-lens stage — register properly before use.

## ADDENDUM (2026-07-28, owner question): is the RP effect level-dependent?

Horse race (owner's collinearity read): miss ~ sp + rp + newHC + thin → rp +2.53
(t 1.77), newHC −1.14 (t 1.44), thin −1.50 (t 1.62). No variable survives alone —
ONE disruption factor, RP the best single window; owner's read supported.

Level dependence: rp × level interaction +1.42 (t 0.97). Terciles by preseason SP+
(within year): bottom +1.18 (t 0.46), **middle +5.88 (t 2.49)**, top +1.71 (t 0.71).
Owner's exposure zone: G5-only +1.13 (t 0.59); sp≤−4 +0.65 (t 0.28); G5∩sp≤−4
+0.91 (t 0.37). The effect concentrates in MID-EXPECTATION teams and is ~nil at the
bottom (and top). Mechanism (plausible, unproven): bad teams return bad production
(continuity uninformative); elite programs reload via recruiting; the middle is where
roster capital is both scarce and valuable. Caveats: within-slice SE ≈ 2.4 (bottom/top
"nil" = undetectable, not proven zero); one of three slices at t 2.49 is only
moderately beyond chance; report-only.

Book re-read: the disruption headwind on the G5 bottom-tercile overs (UConn, Buffalo,
Nevada, BGSU, KSU) measured in THEIR zone is ~−0.1 wins, not the pooled −0.5 —
S9's caution on those legs largely dissolves. Mid-band positions now cut BOTH ways:
turnover helps the Wisconsin/ASU/Florida UNDERS (~−0.3..−0.4 w tailwind at their
turnover levels); **ECU O7.5 is the one leg sitting mid-band on the wrong side** —
flag stands (third independent knock). KSU softens on this axis (bottom tercile);
its loud-arm caution remains. Completion-round rule refined: avoid MID-expectation
disruption overs; bottom-tercile disruption overs are K3-covered and RP-clean.

## ADDENDUM 2 (2026-07-31, owner hypothesis): coach track-record persistence

Owner asked (a-priori, motivated by ASU/Dillingham): do coaches with a history of
beating their preseason rating keep doing it? Test: miss_y ~ sp_pre + coach's mean
PRIOR miss (2021+ window, any school), panel 2022-25, n=411 (first-year-ever HCs
excluded by construction; fired coaches exit — selection noted).

**coef +0.164, t +2.82, LOYO positive 4/4** — the strongest situational predictor
found to date. Survives the horse race: prior_miss +0.155 (t 2.62) WITH rp +3.30
(t 2.04) both alive; newHC dies (+0.28). Scale: a career +10 coach (Cignetti-tier)
projects ≈ +1.6 pts ≈ +0.5 wins of drift; ±5 coach ≈ ±0.25 wins. Confound: coach ≈
program over short windows (skill vs ascending-program momentum not separable).
Ported-history slice (new team, n=27): +0.24, t 0.96 — right sign, underpowered.

Ledger face-validity: top = Cignetti +19.5 (min +14 in all 3), Kinne +12.6,
Odom +11.6, Wommack +10.8, Mora +10.8; bottom = Dabo −8.5, Tom Allen −8.3,
Tucker −7.8, Gundy −7.5, Mack Brown −7.2.

**Book reads (report-only overlay, no bars, no grade changes):**
- **ASU U6.5: hesitation RELIEVED — Dillingham career mean −1.43** (2023 −10.3,
  2024 +13.4, 2025 −7.4). The market premium (line 6.5 vs SP+ 5.96) rests on his
  one outlier year; 2025 already paid the fade.
- Wisconsin U6.5 tailwind: Fickell −5.74, five years trending down (2025 −13.3).
- Wake O5.5 nod: Dickert +6.6 (Wake yr-1 +10.4). UConn O mild nod: Candle +3.0
  (4/5 positive). Nevada (Choate +2.5), Tulsa (Lamb +6.8, n=1) mild nods.
- Mild cautions, consistent with existing no-add stance: Hawai'i U (Chang +2.7,
  2025 +13.3), Illinois U (Bielema +4.4 volatile), WVU U (Rich Rod +5.8 but WVU
  yr-1 −8.8). Neutral: Schiano −0.2, Narduzzi −1.0, Lembo +0.3.
- Single-season, no claim: Harrell (ECU) +15.1, Mack (KSU) +14.7 — noteworthy as
  the source of those teams' market/consensus warmth.

Status: report-only diagnostic on an owner a-priori hypothesis; **S12 (coach prior)
added to the 2027 registry** for proper registration before any rating/sizing use.
