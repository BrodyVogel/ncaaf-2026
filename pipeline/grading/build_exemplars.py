#!/usr/bin/env python3
"""Build the FIXED calibration exemplar block (brief §3) from PFF 2025 data.

Scale: a unit's grade = its percentile among 2025 FBS units of the same group (as
played, snap-weighted PFF aggregates). Exemplars are named 2025 units pinned at chosen
percentiles; every grading call compares against the same anchors. 2025 facts are
blinding-safe.

v2 FINAL (2026-07-14, user-approved last amendment before freeze):
  - 12 global anchors spanning ~3rd-97th percentile (was 8)
  - upper anchors (>=75) prefer legible P4 programs; >=3 G5 anchors kept at mid/low
  - each global anchor carries a data-driven qualitative sketch (compare on substance)
  - per-group tables widened to 7 percentiles (3/10/25/50/75/90/97)
  - band descriptors
Run ONCE, commit, NEVER regenerate (the generator remains for audit only).
"""
import csv, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pff_common import UNITS, build_team_lookup, team_unit_grades_asplayed, load_unit_year

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
    ug = team_unit_grades_asplayed(2025, lookup)

    by_unit = {}
    for (team, unit), (grade, vol) in ug.items():
        by_unit.setdefault(unit, []).append((grade, team, vol))
    for u in by_unit:
        by_unit[u].sort()

    def qualifying(unit, team):
        table, positions, vol_col, grade_col, min_pv, _ = UNITS[unit]
        rows = [(vol, g, pid) for pid, (tn, vol, g) in
                load_unit_year(table, 2025, positions, vol_col, grade_col).items()
                if lookup(tn) == team and vol >= min_pv]
        return sorted(rows, reverse=True)

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
            g, t, v = arr[i]
            if want == "P4" and not is_p4(t):
                continue
            if want == "G5" and is_p4(t):
                continue
            if exemplar and not robust(unit, t, v):
                continue
            return round(100 * i / (len(arr) - 1)), g, t
        return round(100 * idx / (len(arr) - 1)), *arr[idx][:2]

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
        "# FIXED CALIBRATION EXEMPLAR BLOCK — v2 FINAL, frozen 2026-07-14 (PFF 2025, as played)",
        "# Scale: grade = percentile among 2025 FBS units of the same group.",
        "# The anchors are the RULER; any evidence class may move a team along it (prompt v1.1).",
        "",
        "## Scale bands",
        "- 90+ ≈ top-10 unit nationally | 75 ≈ top-35 | 50 ≈ FBS average | 25 ≈ bottom-35 | 10 ≈ bottom-15",
        "",
        "## Global anchors (bracket every grade with these)",
    ]
    g5_n = 0
    for unit, pct, want in GLOBAL_PICKS:
        our, pff, team = pct_team(unit, pct, want, exemplar=True)
        p4 = is_p4(team)
        g5_n += 0 if p4 else 1
        lines.append(f"- **{our}** — {team} {unit} 2025 ({'P4' if p4 else 'G5'}, unit PFF {pff:.1f}): {sketch(unit, team)}.")
    lines += ["", "## Per-group percentile references (2025 unit aggregates)", ""]
    for u in ["QB", "RB", "WRTE", "OL", "DL", "LB", "DB"]:
        refs = []
        for p in (3, 10, 25, 50, 75, 90, 97):
            our, pff, team = pct_team(u, p)
            refs.append(f"p{p} {team} ({pff:.1f})")
        lines.append(f"- **{u}**: " + " | ".join(refs))
    lines += ["", "## ST",
              "- ST grade = percentile of prior-season PFF team SPEC grade; adjust only for known",
              "  specialist departures/arrivals (evidence required).", ""]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exemplars.md")
    open(out, "w").write("\n".join(lines))
    print("\n".join(lines))
    print(f"\nG5 global anchors: {g5_n} (need >=3). wrote {out}")

if __name__ == "__main__":
    main()
