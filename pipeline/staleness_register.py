#!/usr/bin/env python3
"""Step 3 (FINALIZATION_PLAN): emit the staleness checklist from the frozen grades.

The L-confidence flags ARE the staleness checklist: an L unit is one the grader marked
low-confidence (open battle, thin/newcomer data, health-dependent). This script scans
every snapshots/<T>/grades.json for L-graded units and joins the board
(final/rank/band/coach_change) to produce outputs/STALENESS_REGISTER.csv — the durable,
regenerable checklist to re-verify as August camps resolve things.

The human-facing companion outputs/STALENESS_REGISTER.md carries the priority tiers, the
named battles/contingencies, and the re-check procedure (hand-authored; this CSV is its
backing data). Re-run after any grade edit:  python3 pipeline/staleness_register.py

Deterministic; reads only frozen inputs.
"""
import json, glob, os, csv

UNITS = ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB", "ST"]
BOARD = "outputs/FINAL_BOARD_2026.csv"   # AUTHORITATIVE refit board (not grade_board.csv)
OUT = "outputs/STALENESS_REGISTER.csv"


def load_board():
    b = {}
    for r in csv.DictReader(open(BOARD)):
        b[r["team"]] = r
    return b


def main():
    board = load_board()
    rows = []
    for gp in sorted(glob.glob("snapshots/*/grades.json")):
        d = json.load(open(gp))
        team = d["team"]
        u = d["units"]
        Ls = [x for x in UNITS if u.get(x, {}).get("confidence") == "L"]
        if not Ls:
            continue
        br = board.get(team, {})
        rows.append({
            "team": team,
            "conference": br.get("conference", "?"),
            "L_units": "|".join(Ls),
            "n_L": len(Ls),
            "qb_L": "Y" if "QB" in Ls else "",
            "final": br.get("power_rating", "?"),
            "rank": br.get("rank", "?"),
            "band": br.get("band_±", "?"),
            "new_HC": br.get("new_HC", "?"),
        })
    # sort: QB-L first, then by n_L desc, then rank
    rows.sort(key=lambda r: (r["qb_L"] != "Y", -r["n_L"],
                             int(r["rank"]) if str(r["rank"]).isdigit() else 999))
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["team", "conference", "L_units", "n_L",
                                          "qb_L", "final", "rank", "band", "new_HC"])
        w.writeheader()
        w.writerows(rows)
    nqb = sum(1 for r in rows if r["qb_L"] == "Y")
    n3 = sum(1 for r in rows if r["n_L"] >= 3)
    print(f"STALENESS REGISTER | {len(rows)} teams carry >=1 L unit | "
          f"{nqb} QB-L | {n3} with >=3 L units -> {OUT}")


if __name__ == "__main__":
    main()
