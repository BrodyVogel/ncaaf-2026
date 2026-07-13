#!/usr/bin/env python3
"""Backtest v2 (approved 2026-07-12): real preseason-SP+ misses, portal era only.

miss(T,Y) = final SP+ − TRUE preseason SP+ (user-purchased files, validated), Y in 2021-2025.

Answers, in order:
 1. How wrong is the real anchor? (base sigma, by year)
 2. Does preseason SP+ already price churn? (directional regression of miss on
    returning / coach change / power / portal-quality features — if coefficients are
    significant, SP+ does NOT fully price them and a mechanical pre-adjustment is justified)
 3. Portal horse-race: CFBD blue-chip arrivals vs 247 transfer class rankings (user note:
    flag outsized 247 gains — possible lookahead in the rankings)
 4. Churn multipliers for the variance band, re-measured on real misses
 5. Epistemic split: sigma_epistemic = sqrt(sigma² − in-season noise²), noise 4.0/4.5/5.0
 6. Coach-change subtypes (exploratory, user brain-dump): prior FBS HC experience,
    up-class moves, first-FBS-job-at-G5 (FCS→G5 proxy)

Usage: python3 step2_backtest_v2.py <cfbd_dir> <sp_pre_dir> <portal_247_dir> <outdir>
"""
import csv, json, os, sys
import numpy as np

POWER = {"SEC", "Big Ten", "Big 12", "ACC", "Pac-12"}

def name_map():
    return {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}

def load_pre(sp_dir, y, n2c):
    out = {}
    for r in csv.DictReader(open(f"{sp_dir}/SP+_{y}_preseason.csv")):
        c = n2c[r["norm_key"]]
        out[c] = dict(overall=float(r["sp_plus_overall"]), off=float(r["sp_plus_off"]), dfn=float(r["sp_plus_def"]))
    return out

def load_final(d, y):
    out = {}
    for r in json.load(open(f"{d}/sp_{y}.json")):
        t = r.get("team")
        if isinstance(t, str) and t.lower() != "nationalaverages" and r.get("rating") is not None:
            out[t] = dict(overall=r["rating"],
                          off=(r.get("offense") or {}).get("rating"),
                          dfn=(r.get("defense") or {}).get("rating"))
    return out

def load_ret(d, y):
    return {r["team"]: r["percentPPA"] for r in json.load(open(f"{d}/returning_{y}.json"))
            if r.get("percentPPA") is not None}

def power_flag(d, y):
    out = {}
    for r in json.load(open(f"{d}/records_{y}.json")):
        if r.get("classification") == "fbs":
            out[r["team"]] = 1 if (r.get("conference") in POWER or r["team"] == "Notre Dame") else 0
    return out

def bluechip(d, y, fbs):
    out = {}
    for r in json.load(open(f"{d}/portal_{y}.json")):
        if (r.get("stars") or 0) >= 4 and r.get("destination") in fbs:
            out[r["destination"]] = out.get(r["destination"], 0) + 1
    return out

def r247(p247_dir, y, n2c):
    path = f"{p247_dir}/247_Transfer_{y}.csv"
    if not os.path.exists(path):
        return None
    out = {}
    for r in csv.DictReader(open(path)):
        pts = 0.0 if r["points"] in ("NA", "") else float(r["points"])
        out[n2c[r["norm_key"]]] = pts
    return out

def coach_meta(d, years):
    """Per (team, year): primary HC name; plus per-coach set of (year, school) HC jobs."""
    primary, jobs = {}, {}
    for y in years:
        best = {}
        for c in json.load(open(f"{d}/coaches_{y}.json")):
            nm = f"{c.get('firstName')} {c.get('lastName')}"
            for s in c.get("seasons", []):
                if s.get("year") == y and s.get("school"):
                    g = s.get("games") or 0
                    if s["school"] not in best or g > best[s["school"]][1]:
                        best[s["school"]] = (nm, g)
        for t, (nm, _) in best.items():
            primary[(t, y)] = nm
            jobs.setdefault(nm, set()).add((y, t))
    return primary, jobs

def zscore_by_year(rows, key):
    for y in set(r["year"] for r in rows):
        vals = np.array([r[key] for r in rows if r["year"] == y], float)
        mu, sd = vals.mean(), vals.std() or 1.0
        for r in rows:
            if r["year"] == y:
                r[key + "_z"] = (r[key] - mu) / sd

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ b
    s2 = res @ res / max(1, X.shape[0] - X.shape[1])
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return b, res, b / se

def design(rows, feats):
    return np.column_stack([np.ones(len(rows))] + [[r[f] for r in rows] for f in feats])

def loyo(rows, feats):
    out = []
    for y in sorted(set(r["year"] for r in rows)):
        tr = [r for r in rows if r["year"] != y]; te = [r for r in rows if r["year"] == y]
        b, _, _ = ols(design(tr, feats), np.array([r["miss"] for r in tr]))
        out.append(np.array([r["miss"] for r in te]) - design(te, feats) @ b)
    return np.concatenate(out).std()

def main(cfbd, sp_pre, p247, outdir):
    n2c = name_map()
    fbs_all = set()
    for y in range(2020, 2026):
        fbs_all |= set(load_final(cfbd, y))
    primary, jobs = coach_meta(cfbd, range(2014, 2026))
    pclass = {}  # (team,year)->power for coach-class lookups
    for y in range(2014, 2026):
        pclass.update({(t, y): p for t, p in power_flag(cfbd, y).items()})

    rows = []
    for y in range(2021, 2026):
        pre, fin, ret = load_pre(sp_pre, y, n2c), load_final(cfbd, y), load_ret(cfbd, y)
        pw, bc, r2 = power_flag(cfbd, y), bluechip(cfbd, y, fbs_all), r247(p247, y, n2c)
        for t in pre:
            if t not in fin or t not in ret:
                continue
            hc_now, hc_prev = primary.get((t, y)), primary.get((t, y - 1))
            cc = 1 if (hc_now and hc_prev and hc_now != hc_prev) else 0
            row = dict(year=y, team=t, miss=fin[t]["overall"] - pre[t]["overall"],
                       pre=pre[t]["overall"], ret=ret[t], cc=cc, power=pw.get(t, 0),
                       bluechip=bc.get(t, 0), p247=(r2 or {}).get(t, np.nan))
            # coach subtypes (only when cc=1)
            if cc:
                prior_hc_years = [(yy, tt) for (yy, tt) in jobs.get(hc_now, set()) if yy < y]
                row["new_hc_prior_fbs"] = 1 if prior_hc_years else 0
                row["new_hc_first_fbs_g5"] = 1 if (not prior_hc_years and pw.get(t, 0) == 0) else 0
                up = 0
                if prior_hc_years:
                    last_y, last_t = max(prior_hc_years)
                    if pclass.get((last_t, last_y), 0) == 0 and pw.get(t, 0) == 1:
                        up = 1
                row["new_hc_upclass"] = up
            else:
                row["new_hc_prior_fbs"] = row["new_hc_first_fbs_g5"] = row["new_hc_upclass"] = 0
            rows.append(row)

    print(f"panel: {len(rows)} team-seasons 2021-2025 (real preseason vs final SP+)")
    miss = np.array([r["miss"] for r in rows])
    print(f"\n1) RAW ANCHOR MISS: SD={miss.std():.2f}, mean={miss.mean():+.2f}")
    for y in range(2021, 2026):
        m = np.array([r["miss"] for r in rows if r["year"] == y])
        print(f"   {y}: SD={m.std():.2f} mean={m.mean():+.2f} n={len(m)}")

    # z-score portal features within year
    zscore_by_year(rows, "bluechip")
    sub47 = [r for r in rows if not np.isnan(r["p247"])]
    zscore_by_year(sub47, "p247")

    print("\n2) DOES SP+ ALREADY PRICE CHURN? miss ~ features (2021-2025):")
    feats = ["ret", "cc", "power", "bluechip_z"]
    b, res, t = ols(design(rows, feats), miss)
    for nm, bb, tt in zip(["intercept"] + feats, b, t):
        print(f"   {nm:12s} {bb:+7.3f} (t={tt:+.1f})")
    print(f"   residual SD after mechanical churn model: {res.std():.2f} (raw {miss.std():.2f}); LOYO={loyo(rows, feats):.2f}")

    print("\n3) PORTAL HORSE-RACE (2022-2025, both features available, n=%d):" % len(sub47))
    m47 = np.array([r["miss"] for r in sub47])
    base = ["ret", "cc", "power"]
    for nm, ff in [("base", base), ("+bluechip", base + ["bluechip_z"]), ("+247pts", base + ["p247_z"]),
                   ("+both", base + ["bluechip_z", "p247_z"])]:
        bb, rres, tt = ols(design(sub47, ff), m47)
        print(f"   {nm:11s} resid SD={rres.std():.2f}  LOYO={loyo(sub47, ff):.2f}" +
              ("" if nm == "base" else f"  (last coef t={tt[-1]:+.1f})"))

    print("\n4) MULTIPLIERS (|residual| dispersion by bucket / overall):")
    _, res_full, _ = ols(design(rows, feats), miss)
    base_sd = res_full.std()
    ret_v = np.array([r["ret"] for r in rows])
    lo, hi = np.quantile(ret_v, [1/3, 2/3])
    buckets = {"returning low": ret_v <= lo, "returning mid": (ret_v > lo) & (ret_v <= hi),
               "returning high": ret_v > hi,
               "coach change": np.array([r["cc"] == 1 for r in rows]),
               "no change": np.array([r["cc"] == 0 for r in rows]),
               "power": np.array([r["power"] == 1 for r in rows]),
               "G5": np.array([r["power"] == 0 for r in rows])}
    mults = {}
    for nm, mask in buckets.items():
        mults[nm] = round(float(res_full[mask].std() / base_sd), 3)
        print(f"   {nm:15s} n={mask.sum():4d} SD={res_full[mask].std():5.2f} mult={mults[nm]:.2f}")

    print("\n5) EPISTEMIC SPLIT (band = sqrt(sigma_resid^2 - noise^2)):")
    for noise in (4.0, 4.5, 5.0):
        print(f"   in-season noise {noise}: epistemic sigma = {np.sqrt(max(base_sd**2 - noise**2, 0)):.2f}")

    print("\n6) COACH-CHANGE SUBTYPES (exploratory; miss stats within cc=1 rows):")
    cc_rows = [r for r in rows if r["cc"] == 1]
    cc_miss = np.array([r["miss"] for r in cc_rows])
    print(f"   all changes: n={len(cc_rows)} mean={cc_miss.mean():+.2f} SD={cc_miss.std():.2f}")
    for key, label in [("new_hc_prior_fbs", "prior FBS HC exp"), ("new_hc_upclass", "up-class move (G5->P4)"),
                       ("new_hc_first_fbs_g5", "first FBS job, at G5 (FCS->G5 proxy)")]:
        m1 = np.array([r["miss"] for r in cc_rows if r[key] == 1])
        m0 = np.array([r["miss"] for r in cc_rows if r[key] == 0])
        if len(m1) >= 8:
            se = np.sqrt(m1.var()/len(m1) + m0.var()/len(m0))
            print(f"   {label:36s} n={len(m1):3d} mean={m1.mean():+5.2f} vs others {m0.mean():+5.2f} (diff t={(m1.mean()-m0.mean())/se:+.1f}) SD={m1.std():.2f}")
        else:
            print(f"   {label:36s} n={len(m1)} - too few to read")

    os.makedirs(outdir, exist_ok=True)
    out = dict(panel_n=len(rows), years=[2021, 2025], raw_miss_sd=round(float(miss.std()), 3),
               churn_model={nm: round(float(bb), 4) for nm, bb in zip(["intercept"] + feats, b)},
               churn_model_tstats={nm: round(float(tt), 2) for nm, tt in zip(["intercept"] + feats, t)},
               resid_sd=round(float(base_sd), 3), loyo_sd=round(float(loyo(rows, feats)), 3),
               multipliers=mults,
               epistemic_sigma={str(nz): round(float(np.sqrt(max(base_sd**2 - nz**2, 0))), 2) for nz in (4.0, 4.5, 5.0)},
               notes="miss = final - TRUE preseason SP+. 247 z within year, NA->0. "
                     "Coach subtypes exploratory. See run stdout in git log / report.")
    with open(f"{outdir}/backtest_v2_summary.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nsaved -> {outdir}/backtest_v2_summary.json")

if __name__ == "__main__":
    main(*sys.argv[1:5])
