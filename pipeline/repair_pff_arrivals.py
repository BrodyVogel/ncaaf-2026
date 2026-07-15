#!/usr/bin/env python3
"""Repair pass for the 2026-07-15 arrival-row drop bug (approved retro fix).

Two builder defects silently dropped arrival PFF rows from snapshot evidence packs:
  1. lookup() gaps — six FBS aliases (GA TECH, VA TECH, CAL, LA TECH, GA STATE,
     LA MONROE) and all FCS/D2 names were unresolvable, so the name+origin match
     failed (fixed: ALIAS additions + data/anchors/pff_nonfbs_map.csv overlay).
  2. exact-string player matching — PFF "D.J. McKinney" != CFBD "DJ McKinney"
     (fixed: pff_common.player_norm on both sides).

This script regenerates ONLY pff/unit_*.csv for existing snapshots using the patched
matching, preserving hand-appended rows (provenance contains "(manual:"). Everything
else in the snapshot (research, roster, META, grades) is untouched. Prints a per-team
diff of added/removed rows so the repair is fully auditable.

Usage: python3 pipeline/repair_pff_arrivals.py [Team_Dir ...]   (default: all snapshots/*)
"""
import csv, glob, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pff_common import UNITS, build_team_lookup, load_unit_rows, player_norm


def repair(root):
    meta = json.load(open(f"{root}/META.json"))
    team = meta["team"]
    pin = f"{root}/pulls/portal_2026_in.json"
    if not os.path.exists(pin):
        print(f"{team}: no portal_in pull — skipped")
        return False
    _, lookup = build_team_lookup()
    arrivals = {player_norm(p.get("firstName", "") + " " + p.get("lastName", "")): p.get("origin")
                for p in json.load(open(pin))}
    changed = False
    for unit, (table, positions, vol_col, grade_col, _, _) in UNITS.items():
        rows_out = []
        for r in load_unit_rows(table, 2025, positions):
            mapped = lookup(r["team_name"])
            pn = player_norm(r["player"])
            if mapped == team:
                rows_out.append({**r, "_provenance": "2025_this_team"})
            elif arrivals.get(pn) and mapped == arrivals[pn]:
                rows_out.append({**r, "_provenance": f"arrival_2025_at_{r['team_name']}"})
        path = f"{root}/pff/unit_{unit}.csv"
        old_rows, manual = [], []
        if os.path.exists(path):
            old_rows = list(csv.DictReader(open(path)))
            manual = [r for r in old_rows if "(manual:" in r.get("_provenance", "")]
        auto_ids = {r["player_id"] for r in rows_out}
        rows_out += [m for m in manual if m["player_id"] not in auto_ids]
        old_key = {(r["player_id"], r["_provenance"]) for r in old_rows}
        new_key = {(r["player_id"], r["_provenance"]) for r in rows_out}
        if old_key == new_key:
            continue
        changed = True
        names_old = {r["player_id"]: r["player"] for r in old_rows}
        names_new = {r["player_id"]: r["player"] for r in rows_out}
        for pid, prov in sorted(new_key - old_key):
            print(f"  {team} {unit}: + {names_new[pid]} [{prov}]")
        for pid, prov in sorted(old_key - new_key):
            print(f"  {team} {unit}: - {names_old[pid]} [{prov}]")
        if rows_out:
            fieldnames = list(rows_out[0].keys())
            with open(path, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(rows_out)
        elif os.path.exists(path):
            os.remove(path)
            print(f"  {team} {unit}: file removed (no qualifying rows)")
    if not changed:
        print(f"{team}: no changes")
    return changed


if __name__ == "__main__":
    dirs = [f"snapshots/{d}" for d in sys.argv[1:]] or sorted(
        d for d in glob.glob("snapshots/*") if os.path.isdir(d))
    total = 0
    for d in dirs:
        if os.path.exists(f"{d}/META.json"):
            total += bool(repair(d))
    print(f"\nrepaired {total}/{len(dirs)} snapshots")
