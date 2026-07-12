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

## Blinding (brief §4 — HARD)

Nothing in `data/anchors/` or `data/win_totals/` may be read during research/snapshot/grading work. Reconciliation with consensus happens only in compute code.
