#!/usr/bin/env python3
"""Compile outputs/grade_board.csv — the calibration board (handoff item 5).

One row per graded team: 8 unit grades (L-suffixed when low-confidence),
sum, L-count, latest pilot final/rank/band, frozen rev, conference.
This externalizes the peer-rail memory: before grading any unit, look up
the comparable rooms here instead of recalling them.

Regenerate after EVERY graded team:  python3 pipeline/build_board.py
"""
import csv, glob, json, os

UNITS = ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB", "ST"]


def latest_pilot(team):
    hits = []
    for d in sorted(glob.glob("outputs/pilot_*")):
        p = f"{d}/{team}_pilot.json"
        if os.path.exists(p):
            hits.append(p)
    if not hits:
        return {}
    return json.load(open(hits[-1]))  # latest pilot dir wins


def main():
    rows = []
    for d in sorted(glob.glob("snapshots/*")):
        team = os.path.basename(d)
        gp = f"{d}/grades.json"
        if not os.path.exists(gp):
            continue
        g = json.load(open(gp))
        meta = json.load(open(f"{d}/META.json")) if os.path.exists(f"{d}/META.json") else {}
        pilot = latest_pilot(team)
        row = {"team": team.replace("_", " "),
               "conference": meta.get("conference", "")}
        L = 0
        for u in UNITS:
            e = g["units"].get(u, {})
            low = e.get("confidence") == "L"
            L += low
            row[u] = f"{e.get('grade','')}{'L' if low else ''}"
        row["sum"] = sum(g["units"][u]["grade"] for u in UNITS if u in g["units"])
        row["L_count"] = L
        row["final"] = pilot.get("final", "")
        row["rank"] = pilot.get("rank", "")
        row["band"] = pilot.get("band", "")
        row["coach_change"] = meta.get("coach_change", "")
        row["snapshot_rev"] = g.get("_meta", {}).get("snapshot_rev", "")
        row["corrections"] = len(g.get("_meta", {}).get("corrections", []))
        rows.append(row)
    rows.sort(key=lambda r: (r["final"] if isinstance(r["final"], (int, float)) else -99),
              reverse=True)
    cols = ["team", "conference"] + UNITS + ["sum", "L_count", "final", "rank",
                                             "band", "coach_change", "snapshot_rev", "corrections"]
    with open("outputs/grade_board.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"outputs/grade_board.csv: {len(rows)} teams")


if __name__ == "__main__":
    main()
