# SEC Round — magazine page map (2026)

Magazines: "Athlon 2026 - SEC.pdf", "Phil Steele 2026 - SEC (searchable).pdf",
"Pick Six 2026 - SEC.pdf" (all in /mnt/user-data/uploads/NCAAF Data 2026/).

## Athlon SEC (clean, alphabetical) — readable text layer
| Team | Athlon p |
|------|:--------:|
| Alabama | 3 |
| Arkansas | 4 |
| Auburn | 5 |
| Florida | 6 |
| Georgia | 7 |
| Kentucky | 8 |
| LSU | 9 |
| Mississippi State | 10 |
| Missouri | 11 |
| Oklahoma | 12 |
| Ole Miss | 13 |
| South Carolina | 14 |
| Tennessee | 15 |
| Texas | 16 |
| Texas A&M | 17 |
| Vanderbilt | 18 |

## Phil Steele SEC — non-sequential (team names in page margins; pin per-team)
Confirmed so far: Texas A&M p7, Vanderbilt p13, Missouri p14.
Method (per ACC): grep the PS SEC PDF for the team's coach name / unique QB to
locate its page, then render via pdftoppm -r 200 -png and Read the image.

## Batch plan (4 batches of 4, alphabetical; checkpoint between each)
- Batch 1: Alabama, Arkansas, Auburn, Florida
- Batch 2: Georgia, Kentucky, LSU, Mississippi State
- Batch 3: Missouri, Oklahoma, Ole Miss, South Carolina
- Batch 4: Tennessee, Texas, Texas A&M, Vanderbilt

## Pick Six protocol (R16 — REQUIRED third source for P4)
Pick Six SEC (34pp, ~2pp/team) is a full third source for every SEC build: extract
disposition FACTS ONLY (went-pro/declares, transfers, retentions, injuries) via
targeted keyword search of the team's pages; never absorb its rankings/ratings
(blinding v2 — they already enter via the anchor blend). DISCLOSURE: during the
2026-07-18 source inspection, a partial P6 SEC ordering was incidentally seen
(Georgia #1, Oklahoma/Texas #2t, Auburn #9, Missouri/S. Carolina #10t). Those six
teams' research logs must note this exposure at build time; grading remains
percentile-mapped off PFF + exemplars, and full anchor values remain unconsulted.

## SEC-specific methodology note
The SEC conference offsets are POSITIVE and LARGE (QB +7.72, RB +10.17, OL +13.45,
DL +7.87, LB +14.01, DB +5.44). For every OTHER conference's teams, SEC *arrivals*
were weighted DOWN (the offset over-credits limited-action transfers). For the SEC
teams themselves: their RETURNING players' tape was earned in the SEC, so the SEC
cell applies at face value on returning production; arrivals FROM other leagues use
their origin cells. Watch for heavy NFL early-declare attrition (the SEC sends the
most players to the draft) - verify via Phil Steele "#N DC [team]" draft notations.
