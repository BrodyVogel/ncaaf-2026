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

## Adjudication log started (2026-07-23) + one formula fix

**UConn adjudicated (worked example, adjudication_v2.csv).** Net: QB 46→44, LB 50→47,
DB 44→47, DL 46→47, rest hold. Team impact ≈ −0.1 pts — **the pro forma −19 dissolves
under adjudication**: it was (a) the v1-mech strawman at QB (dossier's L had already
hand-shrunk the tiny samples the offset arithmetic took at face value) and (b) an
**Independents artifact**: the IND destination-offset cells (RB −14.11, OL −21.97) are
fitted on an Army/UMass/UConn pool polluted by Army's option scheme.
**FIX (applies to ND + UConn in all v2 math): Independents use their class-pool mean
(ND → P4 pool, UConn → G5 pool) as the destination scale term, never the IND cell** —
same convention as final_pass demeaning. Notre Dame's −21 pro forma row must be re-read
the same way before any conclusion.
**Bet verdict: UConn O5.5 survives adjudication essentially intact (small QB trim).**
Remaining: 13 bet teams → shortlist → field, per the plan's tiering.

## Session 2 progress (bet teams adjudicated; method refinement)

**Method fix:** adjudication gaps are computed WITHIN-CONFERENCE (demeaned, mirroring
final_pass) — the raw v2-vs-dossier comparison was swamped by a scale-convention
artifact (graders "weighted DOWN" the big SEC offsets; the mechanical arm applies them
full-size onto compressed tape spreads → every SEC unit ranked 90s). Demeaned, the
field's disagreements are ~±10, DB-heavy (consistent with S2's DB-unreliability).
**13 bet teams adjudicated** (adjudication_v2.csv; pending grades — grades.json written
once at rebuild). **Illinois FLAGGED for full re-open** (formula up +10..+24 on five
units, against our U7.5). Kennesaw held (override-pinned).
**Next:** Illinois re-open; demeaned shortlist (Louisiana, Georgia State, South Alabama,
Tulane, Colorado State, Arizona, Notre Dame w/ IND fix, Rutgers, WKU, Michigan State);
then the field by conference; then rebuild + impact memo.
