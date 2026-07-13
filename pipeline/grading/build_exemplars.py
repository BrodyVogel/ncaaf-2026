#!/usr/bin/env python3
"""Build the FIXED calibration exemplar block (brief §3) from PFF 2025 data.

Scale definition: a unit's grade on our 0-100 scale = its percentile among 2025 FBS
units of the same group (as played, snap-weighted PFF grades). Exemplars are named 2025
units pinned at chosen percentiles so every future grading call compares against the
same reference points. Historical (2025) facts are blinding-safe per the brief.

Outputs pipeline/grading/exemplars.md:
  - global block: 8 named units spanning ~8th-95th percentile, >=2 G5
  - per-group reference table: team names + PFF grade at p10/p25/p50/p75/p90
Run ONCE, commit, never regenerate (the brief requires the block never vary).
"""
import csv, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pff_common import UNITS, build_team_lookup, team_unit_grades_asplayed, load_unit_year
import numpy as np

POWER = {"SEC", "Big Ten", "Big 12", "ACC"}
D = "data/cfbd/2026-07-12"

# Global-block picks: (unit, target percentile). Chosen to span the scale with a mix of
# offense/defense and legible programs; actual teams resolved from the data below.
GLOBAL_PICKS = [("QB", 95), ("OL", 85), ("DB", 70), ("DL", 60), ("WRTE", 50), ("LB", 35), ("RB", 20), ("DB", 8)]

def main():
    n2c, lookup = build_team_lookup()
    conf = {r["team"]: r.get("conference") for r in json.load(open(f"{D}/records_2025.json"))
            if r.get("classification") == "fbs"}
    ug = team_unit_grades_asplayed(2025, lookup)

    # per-unit sorted lists
    by_unit = {}
    for (team, unit), (grade, vol) in ug.items():
        by_unit.setdefault(unit, []).append((grade, team, vol))
    for u in by_unit:
        by_unit[u].sort()

    def n_qualifying(unit, team):
        table, positions, vol_col, grade_col, min_pv, _ = UNITS[unit]
        return sum(1 for pid, (tn, vol, g) in
                   load_unit_year(table, 2025, positions, vol_col, grade_col).items()
                   if lookup(tn) == team and vol >= min_pv)

    def robust(unit, team, vol):
        """Exemplar eligibility: comfortably-observed units only (user snap-size note)."""
        min_uv = UNITS[unit][5]
        need_players = 1 if unit == "QB" else 2
        return vol >= 2.5 * min_uv and n_qualifying(unit, team) >= need_players

    def pct_team(unit, pct, want_g5=None, exemplar=False):
        arr = by_unit[unit]
        idx = int(round(pct / 100 * (len(arr) - 1)))
        # nudge to nearest index satisfying class + (for exemplars) robustness
        order = sorted(range(len(arr)), key=lambda i: abs(i - idx))
        for i in order:
            g, t, v = arr[i]
            is_p = conf.get(t) in POWER or t == "Notre Dame"
            if want_g5 is True and is_p:
                continue
            if want_g5 is False and not is_p:
                continue
            if exemplar and not robust(unit, t, v):
                continue
            return round(100 * i / (len(arr) - 1)), g, t
        return round(100 * idx / (len(arr) - 1)), *arr[idx][:2]

    def key_players(unit, team):
        table, positions, vol_col, grade_col, min_pv, _ = UNITS[unit]
        rows = []
        for pid, (tn, vol, grade) in load_unit_year(table, 2025, positions, vol_col, grade_col).items():
            if lookup(tn) == team and vol >= min_pv:
                rows.append((vol, grade, pid))
        # volume leaders AND best-graded qualifiers (2026-07-13 amendment: volume-only
        # selection could showcase a good unit's dullest grades - e.g. Temple OL)
        by_vol = sorted(rows, reverse=True)[:2]
        by_grade = sorted(rows, key=lambda r: -r[1])[:2]
        picked, seen = [], set()
        for vol, grade, pid in by_vol + by_grade:
            if pid not in seen:
                seen.add(pid); picked.append((vol, grade, pid))
        # resolve names
        names = {}
        for r in csv.DictReader(open(f"data/pff/PFF_{table}.csv")):
            names[r["player_id"]] = r["player"]
        return [(names.get(pid, pid), int(vol), grade) for vol, grade, pid in picked[:4]]

    lines = ["# FIXED CALIBRATION EXEMPLAR BLOCK — built 2026-07-13 from PFF 2025 (as played)",
             "# Scale: grade = percentile among 2025 FBS units of the same group.",
             "# This block NEVER changes (brief §3). 2025 facts are blinding-safe.",
             "",
             "## Global anchors (compare every grade against these)"]
    g5_count = 0
    for i, (unit, pct) in enumerate(GLOBAL_PICKS):
        want_g5 = True if (g5_count < 2 and pct <= 70 and i >= 2) else None
        our, pff, team = pct_team(unit, pct, want_g5, exemplar=True)
        is_p = conf.get(team) in POWER or team == "Notre Dame"
        if not is_p:
            g5_count += 1
        kp = ", ".join(f"{n} (PFF {g:.1f}, {v} vol)" for n, v, g in key_players(unit, team))
        lines.append(f"- **{our}** — {team} {unit} 2025 ({'P4' if is_p else 'G5'}): "
                     f"unit PFF {pff:.1f}. Key: {kp}.")
    lines += ["", "## Per-group percentile references (2025, snap-weighted unit PFF grade)", ""]
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        refs = []
        for p in (10, 25, 50, 75, 90):
            our, pff, team = pct_team(u, p)
            refs.append(f"p{p} {team} ({pff:.1f})")
        lines.append(f"- **{u}**: " + " | ".join(refs))
    lines += ["", "## ST", "- ST grade = percentile of prior-season PFF team SPEC grade;",
              "  adjust only for known specialist departures/arrivals (evidence required).", ""]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exemplars.md")
    open(out, "w").write("\n".join(lines))
    print("\n".join(lines[:20]))
    print(f"...\nwrote {out}")

if __name__ == "__main__":
    main()
