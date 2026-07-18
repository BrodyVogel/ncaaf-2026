# Conference USA — round wrap (10/10 complete, 2026-07-18)

## Final board (best -> worst)
| Rank(CUSA) | Team | sum | anchor | final | band | coach chg |
|---|---|---|---|---|---|---|
| 1 | Western Kentucky | 366 | -6.47 | **-4.14** | 6.36 | - |
| 2 | Liberty | 342 | -8.79 | -6.49 | 6.54 | - |
| 3 | Jacksonville State | 374 | -9.83 | -6.52 | 6.00 | - |
| 4 | Kennesaw State | 340 | -12.24 | -8.97 | 6.36 | - |
| 5 | Delaware | 376 | -13.86 | -9.02 | 6.60 | - |
| 6 | Florida International | 352 | -15.51 | -10.72 | 6.00 | - |
| 7 | Missouri State | 340 | -16.15 | -11.55 | 7.19 | Woods (x1.13) |
| 8 | New Mexico State | 322 | -18.14 | -13.08 | 6.72 | - |
| 9 | Middle Tennessee | 324 | -14.89*... | -14.89 | 6.54 | - |
| 10 | Sam Houston | 316 | -23.69 | -17.40 | 6.36 | - |

(Middle Tennessee anchor -21.10.) Batch order: B1 Delaware/FIU/JAX State/Kennesaw; B2 Liberty/MTSU/
Missouri State; B3 New Mexico State/Sam Houston/WKU.

## Inflation check — PASSED (floor effect, not P4-inflation)
Every CUSA team's final sits ABOVE its anchor (gap >= 0, 10/10), and the gap grows MONOTONICALLY with
anchor bearishness: +2.30 (Liberty, anchor -8.79) -> +6.29 (Sam Houston, anchor -23.69, at the +-6 cap).
CUSA offset cells are heavily NEGATIVE (QB -5.61 ... LB -12.31), so there is no inflation mechanism - the
anchor-blind grades simply floor ABOVE brutal market anchors, and the residual pulls the final up (capped
+-6). Same finding as the SBC round. The two worst teams (MTSU +6.21, Sam Houston +6.29) hit the cap.

## Grade-vs-market: WKU is the exception that proves the rule
WKU (residual only +1.89) is the one CUSA team where the anchor-blind grade and the market AGREE (both say
CUSA's best). For every other team the grade is far more bullish than a bearish market anchor - the market
prices the churn/juco reality harder than an anchor-blind personnel read does.

## Data-integrity catches (verification discipline)
1. **Sam Houston / Univ of Houston ALIAS (critical).** team_dump.py's substring matcher ('houston' in
   'samhouston') grabbed the Univ of Houston percentile row (10-3, DEF p84, elite) instead of Sam Houston
   State (2-10, OVER p1/DEF p6). Caught via Athlon's 2-10 record; corrected from PFF_2025_team_grades.csv.
   Anchor run UNAFFECTED (canonical 'Sam Houston', blend -23.69). Logged to FORWARD_FLAGS. Without the catch
   Sam Houston would have been massively over-graded.
2. **New Mexico State / Tory Gethers (verification-changed disposition).** Athlon (print) lists LB Gethers
   returning; the current beat (Yahoo) says he is uncommitted-in-portal. Per verify-before-asserting, NOT
   credited - LB graded thin (Aupiu + no LB additions). His return = modest upside not in the number.
3. **Liberty name fixes.** Portal-feed cross-check caught a mis-tagged 'Jaylon Coleman' (real - a returning
   RS-Fr recruit) + a phantom 'Jamal Miles' (fixed to Quavo Marshall). Grade-neutral, documented.
4. **Name-form mismatches forced GONE via departure_confirmed_research:** NMSU 'Armhan Hale' (=Armahn Hale
   -> Bowling Green).
5. **OL scale correction (mid-round).** Placed bottom-tier lines against the board distribution rather than
   by feel: MTSU 30, Sam Houston 32, NMSU 34, Missouri State 36 (comparable bad G5 lines sit in the teens-30s,
   not the 40s). WKU's P4-transfer rebuild placed higher (42).

## Round-end recheck (blind)
- All 10 teams: grades_check OK, departure_check clean, blinding_check clean.
- Board: 136 teams total, 10 CUSA.
- Coach-change flags: Missouri State only (Casey Woods, x1.13) - correct.
- FBS-newcomer proxy artifact handled on Missouri State + (partially) Sam Houston: graded on personnel.

## Tooling flags logged (FORWARD_FLAGS.csv)
- UL_Monroe 'LA MONROE' PFF alias (from the SBC round).
- Sam_Houston team_dump 'houston' substring collision (this round).
