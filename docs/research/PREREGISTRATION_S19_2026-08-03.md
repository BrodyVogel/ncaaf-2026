# PREREGISTRATION S19 — Magazine information-type efficacy (2025 back-test)

Registered 2026-08-03, BEFORE any magazine content has been read, staged, or
extracted. As of this commit the 2025 magazine files exist only on the owner's
machine; the workspace holds their file inventory (names/sizes) and nothing else.
This ordering is the point: the taxonomy and bars below cannot have been shaped
by peeking at the content.

## Question

Which *types* of preseason-magazine information (Phil Steele, Athlon 2025
editions) carried incremental predictive value for 2025 market misses, over and
above the SP+ consensus we already anchor on? The 2026 editions are already
inside our dossier layer as sources; this study decides which information types
deserve that weight, and whether any deserve promotion to explicit factors.

## Data (all frozen before this registration)

- Magazines: 21 PDFs in owner folder "2025 Magazines" (Athlon ×11 incl. two
  team supplements; Steele ×10), 2025 preview editions.
- Market: `data/win_totals/Win Totals from 2025.csv` (DK column, owner capture).
- Consensus control: `data/backtest/sp_preseason/SP+_2025_preseason.csv`.
- Outcomes: `data/cfbd/2026-07-12/games_2025_regular.json` via the canonical
  `team_alias.to_nk()` joins (post-rejoin discipline; any unresolved name is
  counted and reported, never silently dropped).

## Unit of analysis

Team-season, 2025 FBS, n ≈ 133 (bounded by DK-line coverage). Primary outcome
`miss = actual 2025 regular-season wins − DK preseason line`. Secondary outcome
`miss_sp = actual wins − SP+-implied expected wins` (same probit engine as S7).

## Registered information-type taxonomy (extraction targets)

- **T1 Mechanical regression flags (Steele):** turnover-margin extremes,
  close-game (≤7 pt) records, "deserved/second-order wins" style notes.
  Coded as signed numeric where the magazine gives numbers.
- **T2 Experience/continuity counts:** returning starters (off/def), returning
  production %, two-deep seniority as printed.
- **T3 Subjective unit assessments:** per-unit verdicts mapped to a −2..+2
  scale by fixed phrase rules (e.g. "best in the league" = +2, "major concern"
  = −2), rules written down before coding the first team.
- **T4 Explicit projections:** Steele projected finish/wins, Athlon predicted
  record — converted to projected wins minus DK line (a second
  consensus-vs-market arm, F1-style but with magazine consensus).
- **T5 Narrative lists:** surprise teams, most-improved, hot-seat/coaching-fit
  claims. Binary membership dummies.
- **T6 Special-teams rankings (Steele).** Numeric rank.

## Registered tests

For each type k: OLS `miss ~ SP+_pre + signal_k` (and the same on `miss_sp`),
pooled 2025. Report coefficient per 1 SD of signal, t, and ΔR² over the
SP+-only baseline.

## Bars and discipline

- Single-season data ⇒ the whole study is **EXPLORATORY BY CONSTRUCTION.** No
  factor is adopted from S19 alone, whatever the t-stats.
- Reporting bar per type: |t| ≥ 2.0 AND effect ≥ 0.30 wins per 1 SD.
  Six families are being tested: the headline claim (if any) must clear
  |t| ≥ 2.5, per the multiplicity lesson of AUDIT_2026-08-03.
- A type that clears the bar earns exactly one of: (a) corroboration attempt on
  2021–24 if older editions can be obtained, or (b) a 2026 **paper-tracked
  holdout** registered before Week 1 — no staked deployment until one of those
  resolves.
- Extraction blinding: magazine coding happens in a pass that references no
  2025 lines or results; signals land in
  `data/research/s19_mag2025_signals.csv` before any outcome join is run.
  Phrase→score rules for T3 are frozen in the extraction script header.
- Owner-visible deviation log: any departure from this document is recorded in
  the findings file with a timestamp.

## Explicitly out of scope

2026 magazine content (already consumed by the dossier layer under its own
rules); betting decisions of any kind; in-season updates.
