#!/usr/bin/env python3
"""§0 step 4: fill the CFBD column of anchors/team_name_map.csv from the live CFBD team list.

Usage: python3 step0_fill_name_map.py <teams_fbs_2026.json> <team_name_map.csv>
Writes the map in place (renames cfbd_school_FILL_AT_STEP0 -> cfbd_school), validates 138/138.
Matching: norm(CFBD school) == norm_key, then norm(alternateNames/abbreviation),
then explicit OVERRIDES. Fails loud on any unmatched row or unused CFBD team.
"""
import csv, json, re, sys, unicodedata

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()  # é -> e (San José State)
    return re.sub(r"[^a-z0-9]", "", s.lower())

# norm_key -> CFBD school, for names no mechanical rule catches.
# Keep this list tiny and explicit; every entry was hand-verified.
OVERRIDES: dict[str, str] = {
    "louisianamonroe": "UL Monroe",  # map's key spells it out; CFBD school is "UL Monroe"
}

def main(teams_path: str, map_path: str) -> int:
    teams = json.load(open(teams_path))
    assert all(t["classification"] == "fbs" for t in teams)
    by_norm: dict[str, str] = {}
    for t in teams:
        by_norm.setdefault(norm(t["school"]), t["school"])
    alt_by_norm: dict[str, str] = {}
    for t in teams:
        for alt in (t.get("alternateNames") or []) + [t.get("abbreviation") or ""]:
            if alt:
                alt_by_norm.setdefault(norm(alt), t["school"])

    rows = list(csv.DictReader(open(map_path)))
    fill_col = "cfbd_school_FILL_AT_STEP0" if "cfbd_school_FILL_AT_STEP0" in rows[0] else "cfbd_school"
    unmatched, used = [], {}
    for r in rows:
        k = r["norm_key"]
        school = by_norm.get(k) or alt_by_norm.get(k) or OVERRIDES.get(k)
        if not school:
            unmatched.append(k)
            continue
        r[fill_col] = school
        used.setdefault(school, []).append(k)

    dupes = {s: ks for s, ks in used.items() if len(ks) > 1}
    unused = sorted(set(t["school"] for t in teams) - set(used))
    if unmatched or dupes or unused or len(rows) != len(teams):
        print(f"FAIL: rows={len(rows)} teams={len(teams)}")
        if unmatched: print("unmatched norm_keys:", unmatched)
        if dupes: print("CFBD school matched twice:", dupes)
        if unused: print("CFBD teams unused:", unused)
        return 1

    fieldnames = [("cfbd_school" if f == fill_col else f) for f in rows[0]]
    out = [{("cfbd_school" if k == fill_col else k): v for k, v in r.items()} for r in rows]
    with open(map_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(out)
    print(f"OK: {len(rows)}/{len(teams)} filled and validated; column renamed to cfbd_school")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
