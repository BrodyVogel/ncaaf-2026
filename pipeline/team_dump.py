#!/usr/bin/env python3
"""Per-team EVIDENCE DUMP (handoff package, 2026-07-17).

Prints the exact evidence sheet used for every graded build since the MAC
round — previously retyped inline each team, scripted here so every future
build (any operator/model) sees identical inputs in identical format:

  1. Portal feed (in/out) with origins/destinations
  2. Per-unit PFF tables: player, grade, volume(+key), provenance
     (>=30 vol shown for this-team rows; ALL arrival rows shown)
  3. Team as-played percentile line vs the n=136 FBS file
     (absent for FBS newcomers - SacSt/NDSU pattern)
  4. Shadow proxy grades (diagnostic only)
  5. yr4+ roster list (roster_2025 year in {4,5,6})
  6. Full conference-offset table (adjusted = raw + offset[unit][group];
     offsets keyed to WHERE THE TAPE WAS EARNED - ex-conf rule: NIU/UTEP
     returning tape uses MAC/CUSA cells; FCS/D2/NAIA/JC/Ivy = no cell)

Usage: python3 pipeline/team_dump.py <Team_Dir> [--all-rows]
"""
import csv, json, os, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

VOLK = ["passing_snaps", "snap_counts_offense", "snap_counts_defense",
        "attempts", "routes", "player_game_count"]
GRDK = ["grades_offense", "grades_defense", "grades_misc_st",
        "grades_kicking", "grades_punting"]
PCT_LAB = ["OVER", "OFF", "PASS", "PBLK", "RECV", "RUN", "RBLK",
           "DEF", "RDEF", "TACK", "PRSH", "COV", "SPEC"]
UNITS = ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s.upper() if c.isalpha())


def vol(r):
    for k in VOLK:
        v = r.get(k)
        if v not in (None, "", "0"):
            try:
                return int(float(v)), k
            except ValueError:
                pass
    return 0, "?"


def grade(r):
    for k in GRDK:
        v = r.get(k)
        if v not in (None, ""):
            try:
                return float(v)
            except ValueError:
                pass
    return None


def main(team_dir, all_rows=False):
    root = f"snapshots/{team_dir}"
    if not os.path.isdir(root):
        sys.exit(f"no snapshot dir: {root}")
    team_space = team_dir.replace("_", " ")

    # 1. portal feed
    for side in ("in", "out"):
        p = f"{root}/pulls/portal_2026_{side}.json"
        recs = json.load(open(p)) if os.path.exists(p) else []
        print(f"## PORTAL {side.upper()} ({len(recs)})")
        for r in recs:
            print(f"  {r.get('firstName','')} {r.get('lastName','')} | "
                  f"{r.get('position')} | {r.get('origin')} -> {r.get('destination')}")
        print()

    # 2. unit tables
    for u in UNITS:
        f = f"{root}/pff/unit_{u}.csv"
        print(f"## {u}")
        if not os.path.exists(f):
            print("  (no unit file)")
            continue
        rows2 = []
        for r in csv.DictReader(open(f)):
            v, vk = vol(r)
            rows2.append((v, vk, grade(r), r.get("player"), r.get("position"),
                          r.get("_provenance"), r.get("team_name")))
        rows2.sort(key=lambda x: -x[0])
        for v, vk, g, pl, pos, prov, tn in rows2:
            if all_rows or v >= 30 or prov != "2025_this_team":
                print(f"  {pl:28s} {pos or '':4s} g={g} v={v}({vk}) [{prov}|{tn}]")
        print()

    # 3. percentiles
    pf = "data/pff/PFF_2025_team_grades.csv"
    trows = list(csv.DictReader(open(pf)))
    tgt = _norm(team_space)
    hit = ([r for r in trows if _norm(r["TEAM"]) == tgt]
           or [r for r in trows if tgt in _norm(r["TEAM"]) or _norm(r["TEAM"]) in tgt])
    print("## TEAM PERCENTILES (n=%d)" % len(trows))
    if hit:
        t = hit[0]
        out = []
        for l in PCT_LAB:
            v = float(t[l])
            pct = 100.0 * sum(1 for r in trows if float(r[l]) < v) / (len(trows) - 1)
            out.append(f"{l} {v} p{pct:.0f}")
        print("  " + " | ".join(out))
        print(f"  RECORD {t['RECORD']}  PF {t['PF']}  PA {t['PA']}  (row: {t['TEAM']})")
    else:
        print(f"  NO ROW for '{team_space}' - FBS newcomer? (SacSt/NDSU pattern: "
              "no percentile line, evidence-only build)")
    print()

    # 4. proxy
    pr = json.load(open("data/backtest/shadow_proxy_2026.json"))["grades"]
    key = team_space if team_space in pr else next(
        (k for k in pr if _norm(k) == tgt), None)
    print("## SHADOW PROXY (diagnostic only)")
    print(f"  {pr.get(key) if key else 'NO ENTRY (newcomer all-void, artifact #43 pattern)'}")
    print()

    # 5. yr4 list
    rp = f"{root}/pulls/roster_2025.json"
    ros = json.load(open(rp)) if os.path.exists(rp) else []
    yr4 = sorted(f"{r.get('firstName')} {r.get('lastName')} ({r.get('position')})"
                 for r in ros if r.get("year") in (4, 5, 6))
    print(f"## YR4+ ROSTER LIST ({len(yr4)} of {len(ros)})")
    for x in yr4:
        print("  " + x)
    print()

    # 6. offsets table
    off = json.load(open("data/backtest/conf_offsets_2021_2025.json"))["offsets"]
    groups = sorted(next(iter(off.values())).keys())
    print("## CONFERENCE OFFSETS (adjusted = raw + cell; keyed to where tape was EARNED;")
    print("##  FCS/D2/D3/NAIA/JC/Ivy = NO CELL, evidence-only)")
    print("  unit  " + "".join(f"{g:>8s}" for g in groups))
    for u in UNITS:
        print(f"  {u:5s} " + "".join(f"{off[u][g]:8.2f}" for g in groups))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("usage: python3 pipeline/team_dump.py <Team_Dir> [--all-rows]")
    main(args[0], all_rows="--all-rows" in sys.argv)
