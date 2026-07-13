#!/usr/bin/env python3
"""k/cap calibration (§3 mirror), approved 2026-07-12.

Idea: PFF returning-weighted unit grades stand in for our future LLM grades. For each
year Y in 2022-2025, fit the §3 cross-sectional regressions against the TRUE preseason
anchor; the residual (grade-implied minus anchor) is what the blend would have adjusted.
gamma = how much that residual actually predicted the anchor's realized miss = calibrated k.

Unit grade construction (per team T, year Y):
  membership: players who appear for T in PFF year-Y unit table (position-filtered)
  quality:    their YEAR Y-1 grades (any team - handles transfers), snap-weighted,
              subject to MIN-VOLUME thresholds (user note: never trust tiny-snap grades)
  LOOKAHEAD CAVEAT (flagged): membership comes from who actually played for T in Y;
  preseason you'd know rosters but not realized snap allocation. Mildly optimistic.
  ST: prior-year team SPEC grade (not returning-weighted; brief says handle ST simply).

Volume floors (player-level min to carry a grade / unit-level min to trust the unit):
  QB dropbacks 100/100, RB attempts 60/100, WR-TE routes 150/300, OL snaps 200/600,
  DL,LB,DB snaps 200/400. Sensitivity run at 0.5x and 2x thresholds.

Usage: python3 step4_conversion_calibration.py
"""
import csv, json, re, unicodedata
import numpy as np

D = "data/cfbd/2026-07-12"
UNITS = {  # unit: (table, positions, vol_col, grade_col, min_player_vol, min_unit_vol)
    "QB":   ("passing_summary",  {"QB"},        "dropbacks",            "grades_offense", 100, 100),
    "RB":   ("rushing_summary",  {"HB", "FB"},  "attempts",             "grades_offense",  60, 100),
    "WRTE": ("receiving_summary",{"WR", "TE"},  "routes",               "grades_offense", 150, 300),
    "OL":   ("offense_blocking", {"T", "G", "C"},"snap_counts_offense", "grades_offense", 200, 600),
    "DL":   ("defense_summary",  {"DI", "ED"},  "snap_counts_defense",  "grades_defense", 200, 400),
    "LB":   ("defense_summary",  {"LB"},        "snap_counts_defense",  "grades_defense", 200, 400),
    "DB":   ("defense_summary",  {"CB", "S"},   "snap_counts_defense",  "grades_defense", 200, 400),
}
OFF_UNITS, DEF_UNITS = ["QB", "RB", "WRTE", "OL"], ["DL", "LB", "DB"]

ALIAS = {  # player-file team_name -> norm_key (hand-verified); None = not an FBS panel team
    "ARK STATE": "arkansasstate", "BOSTON COL": "bostoncollege", "BOWL GREEN": "bowlinggreen",
    "C MICHIGAN": "centralmichigan", "COAST CAR": "coastalcarolina", "DOMINION": "olddominion",
    "E CAROLINA": "eastcarolina", "E MICHIGAN": "easternmichigan", "FAU": "floridaatlantic",
    "FIU": "floridainternational", "GA SOUTHRN": "georgiasouthern", "JAMES MAD": "jamesmadison",
    "JVILLE ST": "jacksonvillestate", "KENNESAW": "kennesawstate", "LA LAFAYET": "louisiana",
    "MIDDLE TN": "middletennessee", "MO STATE": "missouristate", "N CAROLINA": "northcarolina",
    "N ILLINOIS": "northernillinois", "N TEXAS": "northtexas", "NEW MEX ST": "newmexicostate",
    "NWESTERN": "northwestern", "S ALABAMA": "southalabama", "S CAROLINA": "southcarolina",
    "S DIEGO ST": "sandiegostate", "S JOSE ST": "sanjosestate", "SM HOUSTON": "samhouston",
    "SO MISS": "southernmiss", "UCONN": "connecticut", "UMASS": "massachusetts",
    "USF": "southflorida", "W KENTUCKY": "westernkentucky", "W MICHIGAN": "westernmichigan",
    "W VIRGINIA": "westvirginia", "WAKE": "wakeforest", "W GEORGIA": None,
}
EXP = {"st": "state", "okla": "oklahoma", "colo": "colorado", "app": "appalachian",
       "miss": "mississippi", "tenn": "tennessee", "wash": "washington", "mich": "michigan",
       "fla": "florida", "ill": "illinois", "wis": "wisconsin", "minn": "minnesota",
       "ariz": "arizona", "ore": "oregon", "neb": "nebraska", "tex": "texas", "wyo": "wyoming"}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)

def build_team_lookup():
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    def lookup(team_name):
        if team_name in ALIAS:
            k = ALIAS[team_name]
            return n2c.get(k) if k else None
        k = norm("".join(EXP.get(w, w) for w in team_name.lower().split()))
        return n2c.get(k) or n2c.get(norm(team_name))
    return n2c, lookup

def table_path(table, y):
    return f"data/pff_history/{y}/{table}_{y}.csv" if y < 2025 else f"data/pff/PFF_{table}.csv"

def load_unit_year(table, y, positions, vol_col, grade_col):
    """player_id -> (team_name, vol, grade) for the given unit-table-year."""
    out = {}
    for r in csv.DictReader(open(table_path(table, y))):
        if r["position"] not in positions:
            continue
        try:
            vol, grade = float(r[vol_col] or 0), float(r[grade_col])
        except ValueError:
            continue
        out[r["player_id"]] = (r["team_name"], vol, grade)
    return out

def team_spec(y, n2c):
    path = f"data/pff_history/{y}/PFF_{y}_team_grades.csv" if y < 2025 else "data/pff/PFF_2025_team_grades.csv"
    p2c = {r["pff_2025"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    return {p2c[r["TEAM"]]: float(r["SPEC"]) for r in csv.DictReader(open(path)) if r["TEAM"] in p2c}

def unit_grades_for_year(y, lookup, scale=1.0):
    """For season Y: returning-weighted unit grades from Y-1, membership from Y tables."""
    grades = {}   # (team, unit) -> (grade, coverage_vol)
    for unit, (table, positions, vol_col, grade_col, min_pv, min_uv) in UNITS.items():
        prior = load_unit_year(table, y - 1, positions, vol_col, grade_col)
        current = load_unit_year(table, y, positions, vol_col, grade_col)
        acc = {}
        for pid, (tn, _, _) in current.items():
            team = lookup(tn)
            if team is None or pid not in prior:
                continue
            _, pvol, pgrade = prior[pid]
            if pvol < min_pv * scale:
                continue
            a = acc.setdefault(team, [0.0, 0.0])
            a[0] += pgrade * pvol; a[1] += pvol
        for team, (num, den) in acc.items():
            if den >= min_uv * scale:
                grades[(team, unit)] = (num / den, den)
    return grades

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ b
    s2 = res @ res / max(1, len(y) - X.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return b, res, b / se

def main(scale=1.0, verbose=True):
    n2c, lookup = build_team_lookup()
    def pre(y):
        return {n2c[r["norm_key"]]: (float(r["sp_plus_off"]), float(r["sp_plus_def"]))
                for r in csv.DictReader(open(f"data/backtest/sp_preseason/SP+_{y}_preseason.csv"))}
    def fin(y):
        out = {}
        for r in json.load(open(f"{D}/sp_{y}.json")):
            t = r.get("team")
            if isinstance(t, str) and t.lower() != "nationalaverages":
                o, d = (r.get("offense") or {}).get("rating"), (r.get("defense") or {}).get("rating")
                if o is not None and d is not None:
                    out[t] = (o, d)
        return out

    panel = []
    imput = 0
    for y in (2022, 2023, 2024, 2025):
        ug = unit_grades_for_year(y, lookup, scale)
        spec = team_spec(y - 1, n2c)
        P, F = pre(y), fin(y)
        teams = [t for t in P if t in F]
        # impute unit means for missing (team, unit)
        umean = {u: np.mean([ug[(t, u)][0] for t in teams if (t, u) in ug]) for u in UNITS}
        rows = []
        for t in teams:
            g = {}
            for u in UNITS:
                if (t, u) in ug:
                    g[u] = ug[(t, u)][0]
                else:
                    g[u] = umean[u]; imput += 1
            rows.append((t, g))
        # SS3-mirror cross-sectional fits for THIS year
        Xo = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in OFF_UNITS])
        Xd = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in DEF_UNITS])
        yo = np.array([P[t][0] for t, _ in rows]); yd = np.array([P[t][1] for t, _ in rows])
        bo, ro, _ = ols(Xo, yo); bd, rd, _ = ols(Xd, yd)
        r2o = 1 - ro.var() / yo.var(); r2d = 1 - rd.var() / yd.var()
        for i, (t, g) in enumerate(rows):
            resid_off, resid_def = -ro[i], -rd[i]   # fitted - actual = grade-implied edge
            panel.append(dict(year=y, team=t,
                              resid_off=resid_off, resid_def=resid_def,
                              resid_total=resid_off - resid_def,
                              miss_off=F[t][0] - P[t][0], miss_def=F[t][1] - P[t][1],
                              miss=(F[t][0] - P[t][0]) - (F[t][1] - P[t][1])))
        if verbose:
            cov = sum(1 for t in teams for u in UNITS if (t, u) in ug) / (len(teams) * len(UNITS))
            print(f"  {y}: teams={len(rows)} unit-coverage={cov*100:.0f}% R2(off)={r2o:.2f} R2(def)={r2d:.2f}")

    def gamma(xk, yk):
        x = np.array([r[xk] for r in panel]); yv = np.array([r[yk] for r in panel])
        X = np.column_stack([np.ones(len(x)), x])
        b, res, t = ols(X, yv)
        return b[1], t[1], res.std()

    if verbose:
        print(f"\npanel={len(panel)} team-seasons; imputed unit grades: {imput}")
        print("gamma = realized-miss per point of grade-implied disagreement (this IS k):")
    g_off, t_off, _ = gamma("resid_off", "miss_off")
    g_def, t_def, _ = gamma("resid_def", "miss_def")
    g_tot, t_tot, sd_after = gamma("resid_total", "miss")
    if verbose:
        print(f"  offense: gamma={g_off:+.3f} (t={t_off:+.1f})")
        print(f"  defense: gamma={g_def:+.3f} (t={t_def:+.1f})")
        print(f"  overall: gamma={g_tot:+.3f} (t={t_tot:+.1f})")
        for y in (2022, 2023, 2024, 2025):
            sub = [r for r in panel if r["year"] == y]
            x = np.array([r["resid_total"] for r in sub]); yv = np.array([r["miss"] for r in sub])
            b, _, tt = ols(np.column_stack([np.ones(len(x)), x]), yv)
            print(f"    {y}: gamma={b[1]:+.3f} (t={tt[1]:+.1f})")
        # cap diagnostics: does the relationship survive in the tails?
        x = np.array([r["resid_total"] for r in panel]); yv = np.array([r["miss"] for r in panel])
        print("  |resid_total| percentiles 50/80/90/95:",
              np.round(np.percentile(np.abs(x), [50, 80, 90, 95]), 1))
        for lab, mask in [("inner |r|<=4", np.abs(x) <= 4), ("tail |r|>4", np.abs(x) > 4)]:
            if mask.sum() > 20:
                b, _, tt = ols(np.column_stack([np.ones(mask.sum()), x[mask]]), yv[mask])
                print(f"  {lab}: n={mask.sum()} gamma={b[1]:+.3f} (t={tt[1]:+.1f})")
    return g_tot

if __name__ == "__main__":
    print("=== thresholds x1.0 ===")
    g1 = main(1.0)
    print("\n=== sensitivity: thresholds x0.5 ===")
    g05 = main(0.5, verbose=False); print(f"  overall gamma={g05:+.3f}")
    print("=== sensitivity: thresholds x2.0 ===")
    g2 = main(2.0, verbose=False); print(f"  overall gamma={g2:+.3f}")
