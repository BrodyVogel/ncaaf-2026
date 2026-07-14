#!/usr/bin/env python3
"""Deterministic per-team snapshot assembler (build step 3, brief §2/§5).

Stages the machine-readable evidence for ONE team into snapshots/{team}/ so the
research pass starts from facts, not searches. Research-phase additions (OurLads
two-deep, magazines, news, Sideline) are made by hand per RESEARCH_PROCEDURE.md;
commit = freeze.

BLINDING: this script never reads data/anchors/ or data/win_totals/ (asserted below).

Usage: python3 snapshot_build.py "Kansas State" [--out snapshots]
"""
import argparse, csv, json, os, subprocess, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pff_common import UNITS, build_team_lookup, load_unit_rows

D = "data/cfbd/2026-07-12"
FORBIDDEN = ("data/anchors", "data/win_totals")

def jload(name):
    path = f"{D}/{name}.json"
    assert not any(f in path for f in FORBIDDEN)
    return json.load(open(path)) if os.path.exists(path) else None

def jdump(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("team")
    ap.add_argument("--out", default="snapshots")
    args = ap.parse_args()
    team = args.team

    teams = jload("teams_fbs_2026")
    trow = next((t for t in teams if t["school"] == team), None)
    if trow is None:
        sys.exit(f"'{team}' is not a canonical CFBD 2026 FBS school name. Check anchors/team_name_map.csv.")

    n2c, lookup = build_team_lookup()
    # NOTE: team_name_map.csv lives in data/anchors/ but is a NAME MAP, not a rating.
    # It is the single blinding-safe file there (no numbers in it). Everything else in
    # data/anchors/ stays forbidden.
    c2p = {r["cfbd_school"]: r["pff_2025"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}

    root = os.path.join(args.out, team.replace(" ", "_"))
    if os.path.exists(os.path.join(root, "META.json")) and os.environ.get("REBUILD") != "1":
        # fail loud (2026-07-14): re-assembly overwrites research skeletons and resets META.
        # A frozen/in-progress snapshot must never be clobbered by a casual re-run.
        sys.exit(f"REFUSING to rebuild existing snapshot {root} (set REBUILD=1 to override)")
    for sub in ("pulls", "pff"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)

    # --- CFBD pulls, filtered to this team
    jdump(trow, f"{root}/pulls/team.json")
    roster25 = [p for p in jload("roster_2025") or [] if p.get("team") == team]
    jdump(roster25, f"{root}/pulls/roster_2025.json")
    roster26 = [p for p in jload("roster_2026") or [] if p.get("team") == team]
    jdump(roster26 or {"status": "CFBD 2026 roster not loaded as of pull date - re-run step1 in August"},
          f"{root}/pulls/roster_2026.json")
    portal = jload("portal_2026") or []
    jdump([p for p in portal if p.get("destination") == team], f"{root}/pulls/portal_2026_in.json")
    jdump([p for p in portal if p.get("origin") == team], f"{root}/pulls/portal_2026_out.json")
    games = [g for g in jload("games_2026_regular") or [] if team in (g.get("homeTeam"), g.get("awayTeam"))]
    jdump(games, f"{root}/pulls/schedule_2026.json")
    jdump([r for y in (2023, 2024, 2025) for r in (jload(f"talent_{y}") or []) if r.get("team") == team],
          f"{root}/pulls/talent_history.json")
    jdump([r for y in (2023, 2024, 2025, 2026) for r in (jload(f"recruiting_teams_{y}") or [])
           if r.get("team") == team], f"{root}/pulls/recruiting_ranks.json")
    jdump([r for y in (2024, 2025) for r in (jload(f"coaches_{y}") or [])
           if any(s.get("school") == team for s in r.get("seasons", []))], f"{root}/pulls/coaches_recent.json")
    ret = [r for r in jload("returning_2026") or [] if r.get("team") == team]
    jdump(ret or {"status": "CFBD 2026 returning production not loaded - re-run step1 in August"},
          f"{root}/pulls/returning_2026.json")

    # --- PFF evidence pack per unit: 2025 rows for this team + arrivals' 2025 rows at origin
    pff_names_25 = {}  # for provenance: which PFF team_name strings map to this team
    arrivals = {(p.get("firstName", "") + " " + p.get("lastName", "")).strip().lower(): p.get("origin")
                for p in portal if p.get("destination") == team}
    for unit, (table, positions, vol_col, grade_col, _, _) in UNITS.items():
        rows_out = []
        for r in load_unit_rows(table, 2025, positions):
            mapped = lookup(r["team_name"])
            if mapped == team:
                rows_out.append({**r, "_provenance": "2025_this_team"})
            elif (arrivals.get(r["player"].lower())
                  and lookup(r["team_name"]) == arrivals[r["player"].lower()]):
                # name AND origin-school must both match (fix 2026-07-14: name-only matching
                # pulled same-named strangers, e.g. Clemson WR "Tyler Brown" into Iowa's pack)
                rows_out.append({**r, "_provenance": f"arrival_2025_at_{r['team_name']}"})
        if rows_out:
            with open(f"{root}/pff/unit_{unit}.csv", "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
                w.writeheader(); w.writerows(rows_out)
    pff_team = c2p.get(team)
    tg = [r for r in csv.DictReader(open("data/pff/PFF_2025_team_grades.csv")) if r["TEAM"] == pff_team]
    if tg:
        with open(f"{root}/pff/team_grades_2025.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(tg[0].keys())); w.writeheader(); w.writerows(tg)

    # --- research-phase skeletons
    with open(f"{root}/roster_two_deep.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["unit", "slot", "player", "position", "class", "origin",
                    "source_1", "source_2", "confidence_HML", "notes"])
        for u in list(UNITS) + ["ST"]:
            w.writerow([u, 1, "", "", "", "", "", "", "", ""])
            w.writerow([u, 2, "", "", "", "", "", "", "", ""])
    open(f"{root}/magazines.md", "w").write(
        f"# {team} — magazine findings (Phil Steele + Athlon, 2026 editions)\n\n"
        "RULES: extract unit FACTS (personnel, injuries, battles, scheme, coach quotes).\n"
        "NEVER copy order-of-finish forecasts, unit rank lists, rating numbers, or season totals from books (brief §4).\n"
        "Verify load-bearing OCR'd numbers against the page image (brief §14).\n\n"
        "## Phil Steele\n- (dated entries)\n\n## Athlon\n- (dated entries)\n")
    open(f"{root}/news.md", "w").write(
        f"# {team} — dated news & beat findings\n\n"
        "Format: `- YYYY-MM-DD [source] fact`. Verified enrollment for arrivals,\n"
        "injuries, suspensions, position battles, staff changes. Facts only - no forecasts.\n\n- \n")

    git_rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                             text=True).stdout.strip()
    jdump({
        "team": team, "conference": trow.get("conference"),
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "assembler_git_rev": git_rev,
        "cfbd_pull_dir": D,
        "known_gaps": [
            "CFBD 2026 roster/returning-production/talent/ratings/coaches feeds not yet published (as of pull dir date)",
            "2026 recruiting team ranks not on CFBD - use 247 site at research time for class context",
            "two-deep, magazines.md, news.md, Sideline valuations = research phase (RESEARCH_PROCEDURE.md)",
        ],
        "blinding": "assembler reads no rating/market data; team_name_map.csv used for names only",
        "frozen": False,
    }, f"{root}/META.json")
    print(f"assembled {root}: pulls={len(os.listdir(root + '/pulls'))} files, "
          f"pff={len(os.listdir(root + '/pff'))} units, roster25={len(roster25)} players, "
          f"portal in/out={sum(1 for p in portal if p.get('destination') == team)}/"
          f"{sum(1 for p in portal if p.get('origin') == team)}, games={len(games)}")

if __name__ == "__main__":
    main()
