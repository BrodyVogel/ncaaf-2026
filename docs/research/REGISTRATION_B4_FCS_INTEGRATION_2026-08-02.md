# Registration — Build 4: systematic FCS-curve grade integration (2026-08-02)

Owner decision: the S17 translation curve replaces dossier-and-vibes as the
grading basis for FCS→FBS entrants SYSTEMATICALLY (not targeted case reads),
with production push pre-authorized if the shadow is sane. Registered before
the shadow is computed.

## Mechanism (2026; no new constants)

For each of the 218 matched entrants: curve grade from
s17_projections_2026.csv (L1 model: grade+position only, per L2/L3 nulls).
Unit-level shadow delta ≈ w_share × (curve − dossier's recorded number for
that player), where w_share uses the standard k-table w(n) on the player's
actual 2025 FCS snap counts and the unit's dossier-listed contributor
volumes. Players whose dossier line records no number → flagged for manual
read (delta not computable mechanically).

INTEGRATION RULE (pre-registered): units with |delta| ≥ 2.0 grade pts get
an adjudication row (final = shipped + delta, capped at ±8, confidence
unchanged, reason cites the entrant/curve/share arithmetic) — the ±8 cap
and the adjudication-row mechanism are the EXISTING conventions. |delta| <
2.0 = below the adjudication noise floor (reconciliation-pass scale), no
row. Then regen → final_pass → full chain rebuild → before/after deltas
reported (board + all held positions vs bars).

SANITY GATE (the only stop condition, owner pre-authorized otherwise):
abort and report if the shadow reveals construction error — e.g. deltas
implying |unit moves| > 8 for >10% of affected units, or a degenerate
one-direction distribution inconsistent with S17's compressive curve
(which predicts BOTH directions: elite-FCS entrants marked down, weak-FCS
entrants marked up).

## Freeze and scoring

Pre-integration grades.json state preserved in git (this commit's parent).
DECEMBER SCORING (registered): (i) the 218 projections vs realized 2026
FBS grades (already registered in S17); (ii) integrated vs pre-integration
unit grades scored against realized unit performance for every changed
unit — the integrate-was-right arbiter; (iii) the untouched-bracket
players (no tape match) scored as the control group.

## Scope notes

D2/D3: pair-panel counted first; a thin curve ships ONLY if n ≥ 150 with
LOYO-stable slope, else brackets remain (owner expectation: won't move the
needle). JuCo/NAIA: brackets remain (no tape exists). Unmatched FCS names:
one aliasing pass (suffix/initial handling) before the shadow; residual
unmatched keep brackets and join the December control group.

2027: full formula-arm rewiring (curve grades enter proforma/percentile
machinery natively) — registered build candidate alongside S16 continuous
jumps; this B4 is the 2026 production expression via adjudication rows.

## AMENDMENT 1 (2026-08-02, pre-integration — registered before the full run)

Shadow finding: the registered delta mechanism assumed dossier lines carry
numeric grades for FCS entrants; they do for only 18 of 218 (the class was
graded in prose — the owner's "vibes" description was literal). The n=18
computable slice: mean +1.07, two-directional, two RB units at +8 (real
under-credits on elite-FCS workhorses, not construction error — the >=8
sanity clause's intent was pathology; distribution shape is consistent
with S17's compressive curve). REGISTERED REPLACEMENT MECHANISM for
no-number entrants: recompute the unit as the w(n)-weighted mean of the
dossier's LISTED tape players plus the entrant at (curve grade, 2025 FCS
snaps); delta = recomputed − shipped unit grade. Same |delta| >= 2 row
threshold, same ±8 cap, same conf-unchanged convention. Interpretation:
"if the entrant plays to curve at his volume, the unit computes to X; the
human shipped Y." Where a unit has NO listed tape players (total rebuild
units), fall back to delta = w_share × (curve − shipped) with w_share vs
the unit's k-mass at shipped grade. The 18 numeric cases keep the original
mechanism. Sanity gate re-stated for the full cohort: abort on >10% of
UNITS beyond ±8 pre-cap or a one-directional degenerate distribution.
