#!/usr/bin/env python3
"""Build the FIXED calibration exemplar block (brief §3) from PFF 2025 data.

Scale: a unit's grade = its percentile among 2025 FBS units of the same group (as
played, snap-weighted PFF aggregates). Exemplars are named 2025 units pinned at chosen
percentiles; every grading call compares against the same anchors. 2025 facts are
blinding-safe.

v3.1 FINAL (2026-07-14): + team-grade corroboration filter for anchors (an anchor's
  adjusted percentile must sit within 25 of PFF's own team-grade percentile for that
  unit's side - the Northwestern-DL rule; unit percentile TABLES unchanged)
v3 (competition-adjusted scale):
  - unit aggregates adjusted by conference offsets (data/backtest/conf_offsets_2021_2025.json)
    BEFORE percentile ranking - raw PFF is not opponent-adjusted (the Gleason fix)
  - anchors show raw and adjusted aggregates; conference discount table appended
carried from v2:
  - 12 global anchors spanning ~3rd-97th percentile (was 8)
  - upper anchors (>=75) prefer legible P4 programs; >=3 G5 anchors kept at mid/low
  - each global anchor carries a data-driven qualitative sketch (compare on substance)
  - per-group tables widened to 7 percentiles (3/10/25/50/75/90/97)
  - band descriptors
Run ONCE, commit, NEVER regenerate (the generator remains for audit only).
"""
import csv, json, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pff_common import UNITS, build_team_lookup, team_unit_grades_asplayed, load_unit_year
from step4b_calibration_conf_adjusted import group_of, confs

OFFSETS = json.load(open("data/backtest/conf_offsets_2021_2025.json"))["offsets"]

POWER = {"SEC", "Big Ten", "Big 12", "ACC"}
D = "data/cfbd/2026-07-12"

# (unit, target percentile, class preference: "P4" | "G5" | None)
GLOBAL_PICKS = [
    ("QB", 97, "P4"), ("DL", 92, "P4"), ("OL", 85, "P4"), ("WRTE", 78, "P4"),
    ("DB", 70, "G5"), ("DL", 60, None), ("WRTE", 50, None), ("LB", 42, "G5"),
    ("RB", 33, None), ("OL", 25, "G5"), ("QB", 15, None), ("DB", 6, None),
]
VOL_LABEL = {"QB": "dropbacks", "RB": "att", "WRTE": "routes", "OL": "snaps",
             "DL": "snaps", "LB": "snaps", "DB": "snaps"}

def main():
    n2c, lookup = build_team_lookup()
    conf = {r["team"]: r.get("conference") for r in json.load(open(f"{D}/records_2025.json"))
            if r.get("classification") == "fbs"}
    ug_raw = team_unit_grades_asplayed(2025, lookup)
    c25 = confs(2025)
    ug = {}   # competition-adjusted aggregates; raw kept alongside
    for (team, unit), (grade, vol) in ug_raw.items():
        adj = grade + OFFSETS[unit].get(group_of(team, c25), 0.0)
        ug[(team, unit)] = (adj, vol, grade)

    by_unit = {}
    for (team, unit), (adj, vol, raw) in ug.items():
        by_unit.setdefault(unit, []).append((adj, team, vol, raw))
    for u in by_unit:
        by_unit[u].sort()
    raw_pct = {}   # (team,unit) -> raw-scale percentile, for anchor coherence
    for u in by_unit:
        raws = sorted((raw, t) for adj, t, v, raw in by_unit[u])
        n = len(raws) - 1
        for i, (raw, t) in enumerate(raws):
            raw_pct[(t, u)] = 100 * i / n

    def qualifying(unit, team):
        table, positions, vol_col, grade_col, min_pv, _ = UNITS[unit]
        rows = [(vol, g, pid) for pid, (tn, vol, g) in
                load_unit_year(table, 2025, positions, vol_col, grade_col).items()
                if lookup(tn) == team and vol >= min_pv]
        return sorted(rows, reverse=True)

    # team-grade corroboration: PFF's own team-level column(s) for the unit's side
    TEAMCOLS = {"QB": ["PASS"], "RB": ["RUN"], "WRTE": ["RECV"], "OL": ["RBLK", "PBLK"],
                "DL": ["RDEF", "PRSH"], "LB": ["RDEF", "TACK"], "DB": ["COV"]}
    tg_rows = list(csv.DictReader(open("data/pff/PFF_2025_team_grades.csv")))
    p2c = {r["pff_2025"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    def teamcol_pct(unit, team):
        pcts = []
        for c in TEAMCOLS[unit]:
            vals = sorted(float(r[c]) for r in tg_rows)
            mine = [float(r[c]) for r in tg_rows if p2c.get(r["TEAM"]) == team]
            if mine:
                pcts.append(100 * sum(1 for x in vals if x < mine[0]) / (len(vals) - 1))
        return np.mean(pcts) if pcts else None

    def robust(unit, team, vol):
        min_uv = UNITS[unit][5]
        need = 1 if unit == "QB" else 2
        return vol >= 2.5 * min_uv and len(qualifying(unit, team)) >= need

    def is_p4(t):
        return conf.get(t) in POWER or t == "Notre Dame"

    def pct_team(unit, pct, want=None, exemplar=False):
        arr = by_unit[unit]
        idx = int(round(pct / 100 * (len(arr) - 1)))
        for i in sorted(range(len(arr)), key=lambda i: abs(i - idx)):
            g, t, v, raw = arr[i]
            if want == "P4" and not is_p4(t):
                continue
            if want == "G5" and is_p4(t):
                continue
            if exemplar and not robust(unit, t, v):
                continue
            adj_pct = 100 * i / (len(arr) - 1)
            if exemplar and abs(adj_pct - raw_pct[(t, unit)]) > 20:
                continue   # anchor coherence: guideposts where raw and adjusted agree
            if exemplar:
                tc = teamcol_pct(unit, t)
                if tc is not None and abs(adj_pct - tc) > 25:
                    continue   # corroboration: PFF's team-level view must agree (NW-DL rule)
            return round(adj_pct), g, t, raw
        return round(100 * idx / (len(arr) - 1)), arr[idx][0], arr[idx][1], arr[idx][3]

    def names_for(unit):
        table = UNITS[unit][0]
        return {r["player_id"]: r["player"] for r in csv.DictReader(open(f"data/pff/PFF_{table}.csv"))}

    def sketch(unit, team):
        """Data-driven qualitative sketch from 2025 facts."""
        q = qualifying(unit, team)
        names = names_for(unit)
        plus = sum(1 for _, g, _ in q if g >= 72)
        liab = sum(1 for _, g, _ in q if g < 58)
        vol, g, pid = q[0]
        best = max(q, key=lambda r: r[1])
        lead = f"volume leader {names.get(pid, pid)} ({g:.1f} on {int(vol)} {VOL_LABEL[unit]})"
        if best[2] != pid:
            lead += f", best grade {names.get(best[2], best[2])} ({best[1]:.1f} on {int(best[0])})"
        shape = f"{len(q)} qualifying — {plus} at 72+, {liab} below 58"
        return f"{shape}; {lead}"

    lines = [
        "# FIXED CALIBRATION EXEMPLAR BLOCK — v3 FINAL, frozen 2026-07-14 (PFF 2025, competition-adjusted)",
        "# Scale: grade = percentile among 2025 FBS units of the same group, AFTER conference",
        "# adjustment (raw PFF is not opponent-adjusted; see discount table below).",
        "# The anchors are the RULER; any evidence class may move a team along it (prompt v1.2).",
        "",
        "## Scale bands",
        "- 90+ ≈ top-10 unit nationally | 75 ≈ top-35 | 50 ≈ FBS average | 25 ≈ bottom-35 | 10 ≈ bottom-15",
        "",
        "## Global anchors (bracket every grade with these)",
    ]
    g5_n = 0
    for unit, pct, want in GLOBAL_PICKS:
        our, adj, team, raw = pct_team(unit, pct, want, exemplar=True)
        p4 = is_p4(team)
        g5_n += 0 if p4 else 1
        lines.append(f"- **{our}** — {team} {unit} 2025 ({'P4' if p4 else 'G5'}, raw PFF {raw:.1f} → adj {adj:.1f}): {sketch(unit, team)}.")
    lines += ["", "## Per-group percentile references (2025 unit aggregates, competition-ADJUSTED)", ""]
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        refs = []
        for p in (3, 10, 25, 50, 75, 90, 97):
            our, adj, team, raw = pct_team(u, p)
            refs.append(f"p{p} {team} ({adj:.1f})")
        lines.append(f"- **{u}**: " + " | ".join(refs))
    lines += ["", "## Conference discount table (grade points; ADD to a raw PFF grade by the",
              "## conference where it was earned — for weighing raw PFF evidence in dossiers)", ""]
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        lines.append(f"- **{u}**: " + " ".join(f"{g}:{v:+.0f}" for g, v in sorted(OFFSETS[u].items())))
    lines += ["", "(IND = non-ND independents: small, noisy cell — treat with judgment.)"]
    lines += ["", "## ST",
              "- ST grade = percentile of prior-season PFF team SPEC grade; adjust only for known",
              "  specialist departures/arrivals (evidence required).", ""]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exemplars.md")
    open(out, "w").write("\n".join(lines))
    print("\n".join(lines))
    print(f"\nG5 global anchors: {g5_n} (need >=3). wrote {out}")

if __name__ == "__main__":
    main()
