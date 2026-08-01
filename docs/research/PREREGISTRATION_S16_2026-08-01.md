# Pre-registration — Study 16: continuous origin/destination strength in transfer grading (2026-08-01)

Parking-lot item 6, corrected scope (owner: the GRADING machinery's
competition-level adjustments — "grouping Georgia with Purdue might not make
sense there"). Current v2 mechanism: binary class-jump terms (G5→P4 −3.5,
P4→G5 +1.45) + destination-conference scale cells; SAME-CLASS moves receive
zero adjustment.

**Peek disclosure:** feasibility count only (2026-08-01): ~1,072 transfer
pairs with ≥150 snaps both sides, ~597 matched to origin SP+ before alias
work. No outcome statistic computed. S10's position decomposition (down-
transfer QB −3.6) is prior context, disclosed.

## Panel

Player-pairs across consecutive seasons 2021→22 … 2024→25 (fold = origin
year): same player, different team, ≥150 snaps both sides, PFF season grade
(max-snap summary row) both sides. Origin strength = SP+ FINAL, year Y;
destination strength = SP+ PRESEASON, year Y+1 (pre-outcome, avoids the
destination's realized season contaminating the regressor). ΔSP = origin −
destination. Class = P4/G5 by year-appropriate conference (ND P4); pairs
with unmatched FBS ratings dropped (FCS-origin excluded, consistent with
the v2 formula's separate FCS bracket).

## Legs and bars

- **S16-L1 (granular vs binary):** grade_next ~ grade_prev + up + down
  (binary baseline) vs + ΔSP. PASS iff |t(ΔSP)| ≥ 2 AND ΔR² ≥ 0.01 over
  binary AND LOYO sign-stable ≥3/4. Robustness (report): min-snap weighted.
- **S16-L2 (the Georgia-vs-Purdue leg):** SAME-CLASS movers only —
  grade_next ~ grade_prev + ΔSP. The machinery currently applies ZERO here.
  PASS iff |t(ΔSP)| ≥ 2 AND LOYO ≥3/4. Report P4→P4 and G5→G5 separately.
- **S16-L3 (report-only):** ΔSP × position-group (QB / skill / trench /
  back-7) — does continuous conditioning absorb the S10 QB pathology?
- **S16-L4 (impact, runs ONLY on L1 or L2 pass; report-only):** apply the
  fitted continuous form to 2026 transfers (2025 tape, portal moves):
  count players with |implied adjustment − binary-implied| ≥ 2 grade pts,
  roll up to units/teams, flag held teams. 2026 ratings FROZEN regardless.

## Decision rules (registered)

L1 or L2 PASS → headline 2027 build candidate (continuous jump form,
design registered before 2027 fitting); owner may separately authorize a
targeted 2026 adjudication review of extreme same-class cases under his
accuracy waiver — not automatic. Both FAIL → item 6 closes for the grading
layer too ("binary + conference cells adequate at current power").

## Limitations

PFF season grades are context-blind performance measures (scheme/role
changes confound); grade_prev on different teammates; survivorship (must
earn 150 snaps at destination); 4 folds; SP+ final-vs-preseason asymmetry
registered above; max-snap row may mix position files for hybrid players.
