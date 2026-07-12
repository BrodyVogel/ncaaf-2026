#!/usr/bin/env python3
"""Square the raw PFF History exports (2021-2024) against the 2025 exports.

Checks, per year and table:
  1. schema vs the 2025 counterpart (column names, order-insensitive)
  2. team-name convention vs team_name_map.csv's pff_2025 column
  3. season-vintage fingerprint via FBS membership (JMU joined 2022, Jax St/Sam Houston
     2023, Kennesaw 2024) + row/team counts
Read-only: reports; never edits the raw files.
"""
import csv, sys, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P25 = os.path.join(REPO, "data/pff")
HIST = os.path.join(REPO, "data/pff_history")

PAIRS = {  # history basename (sans _year.csv) -> 2025 file
    "passing_summary": "PFF_passing_summary.csv",
    "rushing_summary": "PFF_rushing_summary.csv",
    "receiving_summary": "PFF_receiving_summary.csv",
    "offense_blocking": "PFF_offense_blocking.csv",
    "defense_summary": "PFF_defense_summary.csv",
    "special_teams_summary": "PFF_special_teams_summary.csv",
}

def cols(path):
    with open(path, newline="") as f:
        return next(csv.reader(f))

def team_col(path):
    c = cols(path)
    for cand in ("team_name", "team", "Team", "TEAM"):
        if cand in c:
            return cand
    return None

def teams_in(path):
    tc = team_col(path)
    with open(path, newline="") as f:
        return set(r[tc] for r in csv.DictReader(f) if r.get(tc))

def main():
    ok = True
    map_pff = set()
    with open(os.path.join(REPO, "data/anchors/team_name_map.csv"), newline="") as f:
        for r in csv.DictReader(f):
            map_pff.add(r["pff_2025"])

    for y in (2021, 2022, 2023, 2024):
        d = os.path.join(HIST, str(y))
        print(f"=== {y} ===")
        # team grades
        tg_hist = os.path.join(d, f"PFF_{y}_team_grades.csv")
        tg_25 = os.path.join(P25, "PFF_2025_team_grades.csv")
        c_h, c_25 = cols(tg_hist), cols(tg_25)
        if c_h != c_25:
            ok = False
            print(f"  team_grades SCHEMA MISMATCH:\n    only-{y}: {set(c_h)-set(c_25)}\n    only-2025: {set(c_25)-set(c_h)}")
        tset = teams_in(tg_hist)
        n25 = len(teams_in(tg_25))
        finger = {"James Madison": y >= 2022, "Jacksonville State": y >= 2023,
                  "Sam Houston State": y >= 2023, "Kennesaw State": y >= 2024}  # PFF spellings
        bad_finger = [t for t, expect in finger.items() if (t in tset) != expect]
        unmapped = tset - map_pff
        print(f"  team_grades: {len(tset)} teams (2025 file: {n25}); schema {'==' if c_h==c_25 else '!='} 2025")
        if bad_finger:
            ok = False
            print(f"  VINTAGE FINGERPRINT FAIL: {bad_finger}")
        if unmapped:
            print(f"  teams not in name map (expected for since-departed/renamed): {sorted(unmapped)}")
        # player tables
        for base, f25 in PAIRS.items():
            hp = os.path.join(d, f"{base}_{y}.csv")
            ch, c2 = cols(hp), cols(os.path.join(P25, f25))
            nrows = sum(1 for _ in open(hp)) - 1
            tag = "==" if ch == c2 else ("~= (same set, diff order)" if set(ch) == set(c2) else "!=")
            if tag == "!=":
                ok = False
                print(f"  {base}: SCHEMA MISMATCH  only-hist:{sorted(set(ch)-set(c2))[:6]} only-2025:{sorted(set(c2)-set(ch))[:6]}")
            else:
                print(f"  {base}: {nrows} rows, schema {tag} 2025")
    print("\nRESULT:", "CLEAN — history files line up with 2025 exports" if ok else "ISSUES FOUND (above)")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
