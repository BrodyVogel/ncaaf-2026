#!/usr/bin/env python3
"""Exploration (2026-07-12, session 2): test the user's proposed backtest-v2 features
before re-speccing step 2. Panel: portal-era targets with prior-year PFF available
(2022-2025). Candidate features on top of base (prev SP+, returning, coach change):

  A. portal quality (net star-sum, blue-chip incoming count from CFBD ratings/stars)
     vs raw transfer count
  B. power-conference binary (year-accurate from records_<y>.json; ND counted power)
  C. prior-year PFF team grades (OVER, or OFF+DEF) from data/pff_history + data/pff

Reports in-sample sigma and leave-one-year-out (LOYO) sigma per model. Exploration only —
step2_backtest.py stays the frozen v1 until the user signs off on a v2 spec.
"""
import csv, json, os
import numpy as np

D = "data/cfbd/2026-07-12"
POWER = {"SEC", "Big Ten", "Big 12", "ACC", "Pac-12"}  # Pac-12 power through 2023 realignment

def load_sp(y):
    out = {}
    for r in json.load(open(f"{D}/sp_{y}.json")):
        t, v = r.get("team"), r.get("rating")
        if isinstance(t, str) and t.lower() != "nationalaverages" and v is not None:
            out[t] = v
    return out

def load_ret(y):
    return {r["team"]: r["percentPPA"] for r in json.load(open(f"{D}/returning_{y}.json"))
            if r.get("percentPPA") is not None}

def hc(y):
    best = {}
    for c in json.load(open(f"{D}/coaches_{y}.json")):
        nm = f"{c.get('firstName')} {c.get('lastName')}"
        for s in c.get("seasons", []):
            if s.get("year") == y and s.get("school"):
                g = s.get("games") or 0
                if s["school"] not in best or g > best[s["school"]][1]:
                    best[s["school"]] = (nm, g)
    return {t: v[0] for t, v in best.items()}

def power_flag(y):
    out = {}
    for r in json.load(open(f"{D}/records_{y}.json")):
        if r.get("classification") == "fbs":
            out[r["team"]] = 1 if (r.get("conference") in POWER or r["team"] == "Notre Dame") else 0
    return out

def portal_features(y, fbs):
    """Per team: in_count, net_stars (nulls=0), bluechip_in (stars>=4)."""
    feats = {}
    for r in json.load(open(f"{D}/portal_{y}.json")):
        stars = r.get("stars") or 0
        for side, team in (("in", r.get("destination")), ("out", r.get("origin"))):
            if team in fbs:
                f = feats.setdefault(team, {"in_count": 0, "net_stars": 0.0, "bluechip_in": 0})
                if side == "in":
                    f["in_count"] += 1; f["net_stars"] += stars
                    if stars >= 4: f["bluechip_in"] += 1
                else:
                    f["net_stars"] -= stars
    return feats

def pff_team_grades(y):
    path = f"data/pff_history/{y}/PFF_{y}_team_grades.csv" if y < 2025 else "data/pff/PFF_2025_team_grades.csv"
    out = {}
    for r in csv.DictReader(open(path)):
        out[r["TEAM"]] = {k: float(r[k]) for k in ("OVER", "OFF", "DEF")}
    return out

def pff_to_cfbd():
    m = {}
    for r in csv.DictReader(open("data/anchors/team_name_map.csv")):
        m[r["pff_2025"]] = r["cfbd_school"]
    return m

def build_panel():
    fbs = set()
    for y in range(2020, 2026):
        fbs |= set(load_sp(y))
    p2c = pff_to_cfbd()
    rows = []
    for y in range(2022, 2026):
        spy, spp, ret = load_sp(y), load_sp(y - 1), load_ret(y)
        hy, hp = hc(y), hc(y - 1)
        pw = power_flag(y)
        pf = portal_features(y, fbs)
        pff_prev = {p2c.get(t): g for t, g in pff_team_grades(y - 1).items() if p2c.get(t)}
        for t in spy:
            if t in spp and t in ret and t in pff_prev:
                f = pf.get(t, {"in_count": 0, "net_stars": 0.0, "bluechip_in": 0})
                rows.append(dict(year=y, team=t, sp=spy[t], prev=spp[t], ret=ret[t],
                                 cc=1 if (t in hy and t in hp and hy[t] != hp[t]) else 0,
                                 power=pw.get(t, 0), in_count=f["in_count"],
                                 net_stars=f["net_stars"], bluechip=f["bluechip_in"],
                                 pff_over=pff_prev[t]["OVER"], pff_off=pff_prev[t]["OFF"],
                                 pff_def=pff_prev[t]["DEF"]))
    return rows

def sigma(rows, feats):
    X = np.column_stack([np.ones(len(rows))] + [[r[f] for r in rows] for f in feats])
    y = np.array([r["sp"] for r in rows])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    ins = (y - X @ b).std(ddof=len(feats) + 1)
    # LOYO
    oos = []
    for yy in sorted(set(r["year"] for r in rows)):
        tr = [r for r in rows if r["year"] != yy]; te = [r for r in rows if r["year"] == yy]
        Xt = np.column_stack([np.ones(len(tr))] + [[r[f] for r in tr] for f in feats])
        bt, *_ = np.linalg.lstsq(Xt, np.array([r["sp"] for r in tr]), rcond=None)
        Xe = np.column_stack([np.ones(len(te))] + [[r[f] for r in te] for f in feats])
        oos.append(np.array([r["sp"] for r in te]) - Xe @ bt)
    return ins, np.concatenate(oos).std(), (X, y, b)

def tstats(X, y, b):
    res = y - X @ b
    s2 = res @ res / (X.shape[0] - X.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return b / se

if __name__ == "__main__":
    rows = build_panel()
    print(f"panel: {len(rows)} team-seasons, targets 2022-2025 (needs prior PFF + returning)\n")
    BASE = ["prev", "ret", "cc"]
    models = [
        ("base (prev+ret+cc)", BASE),
        ("+ in_count (raw portal count)", BASE + ["in_count"]),
        ("+ net_stars (portal quality)", BASE + ["net_stars"]),
        ("+ bluechip_in", BASE + ["bluechip"]),
        ("+ power flag", BASE + ["power"]),
        ("+ pff_over (prior yr)", BASE + ["pff_over"]),
        ("+ pff_off + pff_def (prior yr)", BASE + ["pff_off", "pff_def"]),
        ("+ power + net_stars + pff_off/def", BASE + ["power", "net_stars", "pff_off", "pff_def"]),
        ("kitchen sink", BASE + ["power", "net_stars", "bluechip", "in_count", "pff_off", "pff_def"]),
    ]
    for name, feats in models:
        ins, oos, _ = sigma(rows, feats)
        print(f"  {name:42s} in={ins:5.2f}  LOYO={oos:5.2f}")
    print("\ncoefficients (t-stats), model = base + power + net_stars + pff_off/def:")
    feats = BASE + ["power", "net_stars", "pff_off", "pff_def"]
    _, _, (X, y, b) = sigma(rows, feats)
    for nm, bb, tt in zip(["intercept"] + feats, b, tstats(X, y, b)):
        print(f"  {nm:10s} {bb:+8.3f}  (t={tt:+.1f})")
