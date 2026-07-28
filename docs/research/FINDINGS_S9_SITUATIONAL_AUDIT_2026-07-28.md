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
