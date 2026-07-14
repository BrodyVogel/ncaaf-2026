#!/usr/bin/env python3
"""AUDIT QA #1: mechanical shadow proxy grades for 2026 (k-transfer monitor).

Deterministic PFF-returning unit grades for every 2026 team, on the SAME 0-100
percentile ruler as the LLM grades, printed beside them on every build sheet.

Construction (membership mode "approx2026" until CFBD posts 2026 rosters):
  returning: 2025 PFF players at team T (team-scoped name match to 2025 CFBD roster;
             class year <= 3 or unknown presumed returning; SR presumed gone),
             minus portal_2026 departures
  arrivals:  portal_2026 destination=T, name-matched to their 2025 PFF rows anywhere
  quality:   2025 grades + conference offset by where EARNED, snap-weighted, same
             volume floors as the calibration
  scale:     unit aggregate -> percentile within the 2025 adjusted distribution
             (identical ruler to exemplars v3); ST = 2025 SPEC percentile
Known noise (documented): 5th-year seniors returning read as departed; unknown class
read as returning; walk-on name collisions dropped. This is a MONITOR, not the product.
Usage: python3 shadow_proxy_2026.py  -> data/backtest/shadow_proxy_2026.json
"""
import csv, json, re, sys, os, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pff_common import UNITS, build_team_lookup, load_unit_year, team_unit_grades_asplayed
from step4b_calibration_conf_adjusted import group_of, confs
import numpy as np

D = "data/cfbd/2026-07-12"
OFFSETS = json.load(open("data/backtest/conf_offsets_2021_2025.json"))["offsets"]

def nname(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", s)
    return re.sub(r"[^a-z]", "", s)

def main():
    n2c, lookup = build_team_lookup()
    c25 = confs(2025)
    teams26 = [t["school"] for t in json.load(open(f"{D}/teams_fbs_2026.json"))]

    # roster class map: (team, normname) -> class year
    roster = {}
    for p in json.load(open(f"{D}/roster_2025.json")):
        k = (p.get("team"), nname(f"{p.get('firstName','')} {p.get('lastName','')}"))
        y = p.get("year")
        roster[k] = y if isinstance(y, int) and 1 <= y <= 4 else None

    portal = json.load(open(f"{D}/portal_2026.json"))
    out_of = {}
    into = {}
    for p in portal:
        nm = nname(f"{p.get('firstName','')} {p.get('lastName','')}")
        if p.get("origin"):
            out_of.setdefault(p["origin"], set()).add(nm)
        if p.get("destination"):
            into.setdefault(p["destination"], set()).add(nm)

    # 2025 adjusted distributions per unit (the ruler) from as-played aggregates
    ug25 = team_unit_grades_asplayed(2025, lookup)
    dist = {}
    for (t, u), (g, v) in ug25.items():
        dist.setdefault(u, []).append(g + OFFSETS[u].get(group_of(t, c25), 0.0))
    for u in dist:
        dist[u].sort()

    def to_pct(u, val):
        arr = dist[u]
        return round(100 * sum(1 for x in arr if x < val) / (len(arr) - 1))

    # per-unit player pools from 2025 PFF, with adjusted grades + name keys
    pools = {}
    for u, (table, positions, vol_col, grade_col, min_pv, min_uv) in UNITS.items():
        rows = []
        for pid, (tn, vol, g) in load_unit_year(table, 2025, positions, vol_col, grade_col).items():
            team = lookup(tn)
            adj = g + OFFSETS[u].get(group_of(team, c25) if team else "IND", 0.0)
            rows.append((pid, team, tn, vol, adj))
        pools[u] = rows
    # name resolution for pff players (per unit table)
    pffnames = {}
    for u in UNITS:
        table = UNITS[u][0]
        pffnames[u] = {r["player_id"]: nname(r["player"])
                       for r in csv.DictReader(open(f"data/pff/PFF_{table}.csv"))}

    shadow, coverage = {}, {}
    for T in teams26:
        shadow[T] = {}
        for u, (table, positions, vol_col, grade_col, min_pv, min_uv) in UNITS.items():
            num = den = 0.0
            n_used = 0
            for pid, team, tn, vol, adj in pools[u]:
                if vol < min_pv:
                    continue
                nm = pffnames[u].get(pid, "")
                if team == T:
                    if nm in out_of.get(T, set()):
                        continue                       # transferred away
                    cls = roster.get((T, nm))
                    if cls == 4:
                        continue                       # senior, presumed gone
                elif nm in into.get(T, set()):
                    pass                               # verified arrival, grades from origin
                else:
                    continue
                num += adj * vol; den += vol; n_used += 1
            if den >= min_uv:
                shadow[T][u] = to_pct(u, num / den)
                coverage.setdefault(T, {})[u] = int(den)
            else:
                shadow[T][u] = None                    # compute imputes 50 + low confidence
                coverage.setdefault(T, {})[u] = int(den)
        # ST: 2025 team SPEC percentile (newcomers -> None)
        p2c = {r["pff_2025"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
        specs = {p2c[r["TEAM"]]: float(r["SPEC"]) for r in csv.DictReader(open("data/pff/PFF_2025_team_grades.csv")) if r["TEAM"] in p2c}
        sv = sorted(specs.values())
        shadow[T]["ST"] = (round(100 * sum(1 for x in sv if x < specs[T]) / (len(sv) - 1))
                           if T in specs else None)

    n_null = sum(1 for T in shadow for u in shadow[T] if shadow[T][u] is None)
    with open("data/backtest/shadow_proxy_2026.json", "w") as f:
        json.dump({"_meta": {"mode": "approx2026", "built": "2026-07-14",
                             "ruler": "percentile vs 2025 adjusted distribution (= exemplars v3)",
                             "null_units": n_null},
                   "grades": shadow, "coverage_vol": coverage}, f, indent=1)
    print(f"shadow proxy: {len(shadow)} teams, {n_null} null units (low coverage/newcomers)")
    for T in ("Iowa", "Memphis", "Ohio State", "North Dakota State"):
        print(f"  {T:20s} {shadow[T]}")

if __name__ == "__main__":
    main()
