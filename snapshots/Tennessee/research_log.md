# Tennessee — research log (process + exposure disclosures)

## Sources consulted
- Athlon 2026 SEC p15 (readable text layer via pdftotext -layout): full depth chart + prose.
- Phil Steele 2026 SEC p8 (rendered pdftoppm -r200 -png, read as image): position outlook, projected lineup, RET STARTERS box.
- Pick Six 2026 SEC p145-146 (Brett Ciancia; pdftotext -layout of p6_sec.txt lines ~657-773): facts-only 3rd source (R16).
- CFBD pulls: roster_2025 (110), portal in/out (21/29), PFF unit tables (8 units).
- Web (facts-only disposition verification, 2026-07-18): three targeted searches, see below.

## Blinding (v2)
- Assembler read no rating/market/anchor data. Magazines.md written facts-only.
- Pick Six consulted facts-only; its rankings/Game-Grader NOT recorded or used.

## DISCLOSED incidental ranking exposure (logged, NOT used in grading)
- Athlon page header "NATIONAL FORECAST: 21 | SEC PREDICTION: 8" - unavoidable on the team page; incidental.
- Pick Six SEC index/header "#7(TIE) [SEC], #15 [overall]" incidentally visible while grepping the
  Tennessee byline in p6_sec.txt (line 14 + the team header line). Tennessee is NOT one of the six
  SEC_PAGE_MAP flagged P6-exposure teams; logging this incidental exposure for completeness.
- PS overall/SEC ordering NOT read (page-image inspection limited to the personnel columns).
- Grading remains percentile-mapped off PFF + frozen exemplars; full anchor values unconsulted.

## Web verification (facts-only; disposition, not rankings)
Three grade-critical dispositions where the CFBD feed conflicted with the magazines were verified:
- Colton Hood (CB 79.2/774): feed showed RETURNS; Athlon 2-deep + P6 omitted him. Web CONFIRMED he
  declared early for the 2026 NFL Draft and was a 2nd-round pick (#37, NY Giants). -> nfl_declare_confirmed.
- Jermod McCoy (CB): '24 All-SEC corner, missed all of '25 (ACL). Web CONFIRMED he entered the draft
  (projected R1, TN pro day). No '25 tape; not a returning factor.
- Joshua Josephs (ED 87.1/365): highest returning DL grade but yr4. Web CONFIRMED drafted (#147, Commanders)
  -> EXPIRED(yr4) correct; validated the "D-line loses all 4 starters" magazine claim.
Rationale: these were the only cases where trusting the raw returning-production feed would have
materially mis-graded a unit (the secondary and DL). Only departure facts were taken; no rankings.

## Grade-critical facts double-checked
- OL continuity: 5 returning starters (Sanders/Moe/Pendleton/Perry/Umarov), only Heard (LT) departed - Athlon + P6 agree.
- DL exodus: all 4 starters + Josephs/Ross/Herring gone; only rotational Hobbs/Weathersby back - PS + P6 agree.
- LB: Arion Carter's return (forwent NFL) confirmed by P6 prose + Athlon bold; a genuine strength.
