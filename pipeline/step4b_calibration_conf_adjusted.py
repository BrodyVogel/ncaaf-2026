#!/usr/bin/env python3
"""k/cap recalibration on COMPETITION-ADJUSTED unit grades (2026-07-14, user-prompted).

Question: was gamma=0.32 (raw-grade calibration, step4) an artifact of PFF's
competition inflation? Here every player's prior-year grade is adjusted by a
conference-level offset BEFORE unit aggregation, so the class axis moves out of the
residuals. If disagreement still predicts misses, the signal is real and k gets
re-based in the same grade-space production grades will use.

Rigor guards:
  - offsets fitted LEAVE-ONE-YEAR-OUT: year-Y grades use offsets fitted on all years
    except Y (no outcome of year Y touches its own adjustment)
  - offsets applied by the conference where the grade was EARNED (player's Y-1 team),
    matching the production rule for judging transfer evidence
  - offsets re-centered to FBS mean 0 per unit (level-neutral)
Everything else identical to step4 (thresholds, membership, imputation, SS3-mirror).

Usage: python3 step4b_calibration_conf_adjusted.py
"""
import csv, json
import numpy as np
from pff_common import (UNITS, OFF_UNITS, DEF_UNITS, build_team_lookup,
                        table_path, load_unit_year, team_unit_grades_asplayed)

D = "data/cfbd/2026-07-12"
GROUP_MAP = {"SEC": "SEC", "Big Ten": "B10", "Big 12": "B12", "ACC": "ACC",
             "Pac-12": "PAC", "Mountain West": "MWC", "American Athletic": "AAC",
             "Sun Belt": "SBC", "Conference USA": "CUSA", "Mid-American": "MAC",
             "FBS Independents": "IND"}

def confs(y):
    return {r["team"]: r.get("conference") for r in json.load(open(f"{D}/records_{y}.json"))
            if r.get("classification") == "fbs"}

def group_of(team, conf_map):
    if team == "Notre Dame":
        return "SEC"  # power-class treatment for ND (no IND-power cell sparsity)
    return GROUP_MAP.get(conf_map.get(team, ""), "IND")

def fin(y):
    out = {}
    for r in json.load(open(f"{D}/sp_{y}.json")):
        t = r.get("team")
        if isinstance(t, str) and t.lower() != "nationalaverages":
            o, d = (r.get("offense") or {}).get("rating"), (r.get("defense") or {}).get("rating")
            if o is not None and d is not None:
                out[t] = (o, d)
    return out

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ b
    s2 = res @ res / max(1, len(y) - X.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return b, res, b / se

_lookup_cache = {}
def fit_offsets(exclude_year, lookup):
    """(unit, group) -> grade-point adjustment (FBS-mean-centered), fitted on
    as-played unit grades vs same-year final SP+ across 2021-2025 minus exclude_year."""
    key = exclude_year
    if key in _lookup_cache:
        return _lookup_cache[key]
    groups = sorted(set(GROUP_MAP.values()))
    out = {}
    for u in UNITS:
        G, Y, Gr, W = [], [], [], []
        for y in range(2021, 2026):
            if y == exclude_year:
                continue
            ug = team_unit_grades_asplayed(y, lookup)
            F, C = fin(y), confs(y)
            for (t, uu), (g, v) in ug.items():
                if uu == u and t in F and t in C:
                    G.append(g)
                    Y.append(F[t][0] if u in OFF_UNITS else F[t][1])
                    Gr.append(group_of(t, C))
                    W.append(v)
        base = "SEC"
        dums = [np.array([1.0 if gr == g else 0.0 for gr in Gr]) for g in groups if g != base]
        X = np.column_stack([np.ones(len(Y)), np.array(G)] + dums)
        b, _, _ = ols(X, np.array(Y))
        slope = b[1]
        adj = {base: 0.0}
        for i, g in enumerate([g for g in groups if g != base]):
            adj[g] = float(b[2 + i] / slope)
        # re-center to observation-weighted mean 0
        m = np.mean([adj[gr] for gr in Gr])
        out[u] = {g: a - m for g, a in adj.items()}
    _lookup_cache[key] = out
    return out

def unit_grades_adjusted(y, lookup, offsets, scale=1.0):
    """Returning-weighted unit grades with each player's Y-1 grade adjusted by the
    conference (of the Y-1 team) offset."""
    conf_prev = confs(y - 1)
    grades = {}
    for unit, (table, positions, vol_col, grade_col, min_pv, min_uv) in UNITS.items():
        prior = load_unit_year(table, y - 1, positions, vol_col, grade_col)
        current = load_unit_year(table, y, positions, vol_col, grade_col)
        acc = {}
        for pid, (tn, _, _) in current.items():
            team = lookup(tn)
            if team is None or pid not in prior:
                continue
            prev_tn, pvol, pgrade = prior[pid]
            prev_team = lookup(prev_tn)
            if pvol < min_pv * scale:
                continue
            gr = group_of(prev_team, conf_prev) if prev_team else "IND"
            adj_grade = pgrade + offsets[unit].get(gr, 0.0)
            a = acc.setdefault(team, [0.0, 0.0])
            a[0] += adj_grade * pvol; a[1] += pvol
        for team, (num, den) in acc.items():
            if den >= min_uv * scale:
                grades[(team, unit)] = (num / den, den)
    return grades

def main(scale=1.0, verbose=True):
    n2c, lookup = build_team_lookup()
    def pre(y):
        return {n2c[r["norm_key"]]: (float(r["sp_plus_off"]), float(r["sp_plus_def"]))
                for r in csv.DictReader(open(f"data/backtest/sp_preseason/SP+_{y}_preseason.csv"))}
    POWER5 = {"SEC", "Big Ten", "Big 12", "ACC", "Pac-12"}

    panel, imput = [], 0
    for y in (2022, 2023, 2024, 2025):
        offsets = fit_offsets(exclude_year=y, lookup=lookup)   # LOYO: year y never sees itself
        ug = unit_grades_adjusted(y, lookup, offsets, scale)
        P, F, C = pre(y), fin(y), confs(y)
        teams = [t for t in P if t in F]
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
        Xo = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in OFF_UNITS])
        Xd = np.column_stack([np.ones(len(rows))] + [[g[u] for _, g in rows] for u in DEF_UNITS])
        yo = np.array([P[t][0] for t, _ in rows]); yd = np.array([P[t][1] for t, _ in rows])
        bo, ro, _ = ols(Xo, yo); bd, rd, _ = ols(Xd, yd)
        for i, (t, g) in enumerate(rows):
            pw = 1 if (C.get(t) in POWER5 or t == "Notre Dame") else 0
            panel.append(dict(year=y, team=t, power=pw,
                              resid_total=(-ro[i]) - (-rd[i]),
                              miss=(F[t][0] - P[t][0]) - (F[t][1] - P[t][1])))
        if verbose:
            print(f"  {y}: teams={len(rows)} R2(off)={1-ro.var()/yo.var():.2f} R2(def)={1-rd.var()/yd.var():.2f}")

    x = np.array([r["resid_total"] for r in panel]); m = np.array([r["miss"] for r in panel])
    w = np.array([r["power"] for r in panel], float)
    b, res, t = ols(np.column_stack([np.ones(len(x)), x]), m)
    if verbose:
        print(f"\npanel={len(panel)}; imputed={imput}")
        print(f"ADJUSTED-GRADE gamma: {b[1]:+.3f} (t={t[1]:+.1f})")
        print(f"resid-vs-class corr now: {np.corrcoef(x, w)[0,1]:+.3f} (raw-grade version was -0.70)")
        for y in (2022, 2023, 2024, 2025):
            s = [r for r in panel if r["year"] == y]
            xs = np.array([r["resid_total"] for r in s]); ms = np.array([r["miss"] for r in s])
            bb, _, tt = ols(np.column_stack([np.ones(len(xs)), xs]), ms)
            print(f"    {y}: gamma={bb[1]:+.3f} (t={tt[1]:+.1f})")
        bj, _, tj = ols(np.column_stack([np.ones(len(x)), x, w]), m)
        print(f"joint with power: gamma={bj[1]:+.3f} (t={tj[1]:+.1f}), power={bj[2]:+.2f} (t={tj[2]:+.1f})")
        print("|resid| percentiles 50/80/90/95:", np.round(np.percentile(np.abs(x), [50, 80, 90, 95]), 1))
        for lab, mask in [("inner |r|<=4", np.abs(x) <= 4), ("tail |r|>4", np.abs(x) > 4)]:
            if mask.sum() > 20:
                bb, _, tt = ols(np.column_stack([np.ones(mask.sum()), x[mask]]), m[mask])
                print(f"  {lab}: n={mask.sum()} gamma={bb[1]:+.3f} (t={tt[1]:+.1f})")
        for lab, mask in [("P4 only", w == 1), ("G5 only", w == 0)]:
            bb, _, tt = ols(np.column_stack([np.ones(mask.sum()), x[mask]]), m[mask])
            print(f"  {lab}: gamma={bb[1]:+.3f} (t={tt[1]:+.1f}, n={mask.sum()})")
    return b[1]

if __name__ == "__main__":
    print("=== conference-adjusted calibration (LOYO offsets), thresholds x1.0 ===")
    g = main(1.0)
    print("\n=== sensitivity x0.5 ==="); print(f"  gamma={main(0.5, verbose=False):+.3f}")
    print("=== sensitivity x2.0 ==="); print(f"  gamma={main(2.0, verbose=False):+.3f}")
