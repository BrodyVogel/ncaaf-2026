# CFB 2026 Power Ratings

Preseason power ratings for all 138 FBS teams (2026). Private: contains paid PFF exports and magazine-derived content.

**Read `PROJECT_INIT_PROMPT.md` first** — it is the governing brief (architecture, blinding rules, build order).

## Layout

```
data/cfbd/        league-wide CFBD pulls, date-stamped subdirs + pull manifests
data/pff/         27 PFF 2025 exports + data dictionary (research + flag-pass use)
data/pff_history/ PFF 2021-2024: team grades + 6 position summaries per year (conversion backtest)
data/anchors/     ⚠ COMPUTE PHASE ONLY (blinding, brief §4) — consensus captures + team_name_map.csv
data/win_totals/  ⚠ COMPUTE PHASE ONLY (blinding, brief §4) — 2025 preseason win totals
data/backtest/    backtest inputs/outputs
snapshots/{team}/ frozen per-team research (commit = freeze)
pipeline/         code: cfbd client, backtest, grading harness, blend, variance, flags
outputs/          ratings tables, run logs
```

## Session bootstrap

1. Clone (PAT in the connected folder's `secrets/github_token.txt`; CFBD key in `secrets/cfbd_api_key.txt` — never commit either; `secrets/` is gitignored).
2. Network egress must allow `api.collegefootballdata.com` (+ `apinext.`) and `github.com`.
3. Follow brief §0.

## Per-team pipeline (build steps 3-4, tooling in place)

1. `python3 pipeline/snapshot_build.py "<CFBD school>"` — deterministic evidence pack
2. Research pass per `pipeline/RESEARCH_PROCEDURE.md` (OurLads two-deep, magazines, news)
3. `python3 pipeline/blinding_check.py snapshots/<Team_Dir>` → commit = FREEZE
4. Grade 8 units in-session: `pipeline/grading/GRADING_PROMPT.md` + `exemplars.md` (FIXED
   scale anchors — never regenerate) → `grades.json` per `grading_schema.json`
5. League-wide fit/blend/variance when all teams graded (adopted params:
   `outputs/backtest_2026-07-12/PARAMETERS.json` — k=0.35, cap=±6, per-run class term,
   epistemic σ=6.0; grades on the conference-adjusted exemplars-v3 ruler)
6. Outputs: per-team BUILD SHEET (full derivation, per-source anchor values) +
   `outputs/overrides.csv` for logged user-directed overrides — never silent

## Blinding (brief §4 — HARD)

Nothing in `data/anchors/` or `data/win_totals/` may be read during research/snapshot/grading work. Reconciliation with consensus happens only in compute code.
