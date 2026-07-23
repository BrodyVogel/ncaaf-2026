# v2 rollout plan — full-board regrade (owner-approved direction 2026-07-23)

Owner decision: adopt v2 as the player-grade baseline and apply to EVERY team (mixed
vintage would break cross-team comparability). Steps and technical answers:

1. **v2 baseline accepted.** Formula (validated components only): w(n)=n/(n+k) shrinkage
   (k: QB230/RB110/WRTE190/OL595/DL290/LB630/DB1180; caps QB .55 LB .50) + class-jump
   terms (G5→P4 −3.54, P4→G5 +1.45) + freshman composite priors (per-position
   baselines/slopes in GRADING_V2_SPEC) + single-year missed-season look-through
   (volume ×0.5) + destination-conference SCALE term (offsets keep the scale job).
   FCS/D2/JUCO entrants: v1 qualitative brackets unchanged. Portal stars banned.
1a. **Bridge, no refit:** projected player grades → national percentile within unit type
   (built in pipeline/research/proforma_v2.py) → 0–100 unit scale. The unit→O/D OLS in
   final_pass auto-refits every run; its un-shrink handles any distribution change.
2. **Adjudication (the work):** 940 units, tiered — |formula−dossier| ≤ ~4 → accept with
   note; medium → dossier read + logged decision; large + ALL 14 bet-held teams → full
   re-open (bet teams FIRST, starting with UConn QB/unit stack, pro forma −19).
   Output: adjudication CSV (team, unit, formula#, final, confidence, deviation reason).
   Pace: 30–50 teams/session ⇒ 3–5 sessions. New grades land as regenerated grades.json
   with _meta vintage="v2 2026-07"; v1 preserved in git + ASSEMBLY_LOCKED_2026-07-20.
3. **Refits:** final_pass OLS = automatic. Market-stretch s* = automatic at payload
   build. Bands from new confidence letters = automatic. Calibrated ×0.75 = DO NOT
   refit (property of July-rating quality, fitted on 2021–25 outcomes; revisit post-2026).
   Anchor frozen. Manual overrides re-examined per team during adjudication; demeaning
   exclusion machinery stays.
4. **Rebuild + impact:** final_pass → win_totals_compute (payload) → artifact →
   bet_tracker; full before/after memo incl. all open bets re-priced (expect movement;
   bets hold at their prices); persisted-artifact refresh; commit per conference batch
   with session trailers.

Order of adjudication: (1) bet-held teams (UConn, Tulsa, Oregon State, Bowling Green,
Liberty, Arizona State, Kennesaw State, Illinois, West Virginia, East Carolina, Hawai'i,
Florida, UCF, Pittsburgh) → (2) pro forma |Δteam| > 12 shortlist → (3) remaining field
by conference. Inputs ready on disk: outputs/proforma_v2_2026.csv (formula numbers per
unit), snapshots/*/roster_two_deep.csv, spine, recruiting pulls.
