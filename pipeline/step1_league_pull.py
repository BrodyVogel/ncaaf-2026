#!/usr/bin/env python3
"""Build step 1: batched league-wide CFBD pull.

2026 current-season backbone + historical series for the backtest (§7).
Usage: CFBD_KEY_FILE=... python3 step1_league_pull.py <outdir>
Idempotent: skips pulls already in the manifest with >0 records; ZERO-record pulls are
re-attempted every run (as of 2026-07-12, CFBD had not yet loaded 2026 rosters, SP+,
returning production, talent, or coaches — re-run this script in August until they fill).
"""
import sys, os
from cfbd_client import CFBD

HIST_SP = range(2014, 2026)        # final-season SP+ per year (preseason vintage: see NOTE)
HIST_RETURNING = range(2014, 2026)
HIST_TALENT = range(2015, 2026)
HIST_PORTAL = range(2021, 2026)    # portal era
HIST_RECORDS = range(2014, 2026)   # realized wins for the win-totals backtest
HIST_COACHES = range(2014, 2027)   # coaching-change features

# NOTE (§7): CFBD /ratings/sp?year=Y serves ONE vintage per season. Pulled mid-July,
# year=2026 is necessarily the preseason projection (no 2026 games exist) — that pull
# doubles as the canonical SP+ anchor (manifest: swap ESPN capture for CFBD). Whether
# historical years serve preseason or final vintage is checked in step2; expect final.

def main(outdir: str) -> None:
    api = CFBD(outdir)
    done = {m["name"] for m in api.manifest if m["n_records"] > 0}

    def pull(name, endpoint, params=None):
        if name in done:
            print(f"skip {name} (already pulled)")
            return
        data = api.pull(name, endpoint, params)
        print(f"{name}: {len(data) if isinstance(data, list) else 1} records")

    # --- 2026 backbone
    pull("teams_fbs_2026", "/teams/fbs", {"year": 2026})
    pull("roster_2026", "/roster", {"year": 2026})
    pull("roster_2025", "/roster", {"year": 2025})  # baseline until CFBD loads 2026 rosters
    for y in (2022, 2023, 2024):                    # historical rosters: PFF returning-weighted units
        pull(f"roster_{y}", "/roster", {"year": y})
    pull("games_2025_regular", "/games", {"year": 2025, "seasonType": "regular"})  # market check
    pull("games_2025_postseason", "/games", {"year": 2025, "seasonType": "postseason"})
    for y in (2023, 2024, 2025, 2026):                 # recruiting team ranks: unproven-player priors
        pull(f"recruiting_teams_{y}", "/recruiting/teams", {"year": y})
    pull("sp_2026", "/ratings/sp", {"year": 2026})
    pull("returning_2026", "/player/returning", {"year": 2026})
    pull("talent_2026", "/talent", {"year": 2026})
    pull("portal_2026", "/player/portal", {"year": 2026})
    pull("games_2026_regular", "/games", {"year": 2026, "seasonType": "regular"})
    pull("coaches_2026", "/coaches", {"year": 2026})

    # --- historical (backtest)
    for y in HIST_SP:        pull(f"sp_{y}", "/ratings/sp", {"year": y})
    for y in HIST_RETURNING: pull(f"returning_{y}", "/player/returning", {"year": y})
    for y in HIST_TALENT:    pull(f"talent_{y}", "/talent", {"year": y})
    for y in HIST_PORTAL:    pull(f"portal_{y}", "/player/portal", {"year": y})
    for y in HIST_RECORDS:   pull(f"records_{y}", "/records", {"year": y})
    for y in HIST_COACHES:
        if y != 2026:        pull(f"coaches_{y}", "/coaches", {"year": y})

    print(f"manifest: {len(api.manifest)} pulls -> {api.manifest_path}")

if __name__ == "__main__":
    main(sys.argv[1])
