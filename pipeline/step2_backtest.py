#!/usr/bin/env python3
"""Step 2 / §7 — anchor backtest. ANCHOR ONLY (never the grading layer).

CFBD stores only FINAL-season SP+, so we approximate the "preseason anchor" with a
model built from information known before the season: prior-year final SP+ + returning
production + portal volume + coaching change. Its residual vs realized (final) SP+ is the
preseason miss.

Outputs:
  base_sigma            = residual SD of the full preseason-info model
  churn multipliers     = residual SD within returning-production / coaching buckets, ÷ base
  directional test      = signed coefficients + t-stats on the offseason features
Model progression prints what each offseason signal buys (motivates adding PFF unit grades
as the next signal, via the conversion backtest in step 3).

Usage: python3 step2_backtest.py <cfbd_dir> <outdir>
"""
import json, os, sys, datetime
import numpy as np

def load_sp(d, y):
    out = {}
    p = f"{d}/sp_{y}.json"
    if not os.path.exists(p): return out
    for r in json.load(open(p)):
        t, v = r.get("team"), r.get("rating")
        if isinstance(t, str) and t.lower() != "nationalaverages" and v is not None:
            out[t] = v
    return out

def load_returning(d, y):
    out = {}
    p = f"{d}/returning_{y}.json"
    if not os.path.exists(p): return out
    for r in json.load(open(p)):
        if r.get("team") is not None and r.get("percentPPA") is not None:
            out[r["team"]] = r["percentPPA"]
    return out

def load_portal_in(d, y, fbs):
    """Incoming transfer count per destination team (portal era only)."""
    out = {}
    p = f"{d}/portal_{y}.json"
    if not os.path.exists(p): return out
    for r in json.load(open(p)):
        dest = r.get("destination")
        if dest in fbs:
            out[dest] = out.get(dest, 0) + 1
    return out

def hc_by_team(d, y):
    """Primary head coach (max games that year) per team, from coaches_<y>.json."""
    out = {}
    p = f"{d}/coaches_{y}.json"
    if not os.path.exists(p): return out
    best = {}
    for c in json.load(open(p)):
        name = f"{c.get('firstName')} {c.get('lastName')}"
        for s in c.get("seasons", []):
            if s.get("year") == y and s.get("school"):
                g = s.get("games") or 0
                if s["school"] not in best or g > best[s["school"]][1]:
                    best[s["school"]] = (name, g)
    return {t: v[0] for t, v in best.items()}

def ols(X, y):
    """Return coeffs, residuals, and t-stats (X already has intercept col)."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n, k = X.shape
    sigma2 = (resid @ resid) / (n - k)
    cov = sigma2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    return beta, resid, beta / se

def main(cfbd_dir, outdir):
    fbs = set()
    for y in range(2014, 2026):
        fbs |= set(load_sp(cfbd_dir, y))

    rows = []  # (year, team, sp_y, sp_prev, ret, portal_in, coach_change)
    for y in range(2015, 2026):
        sp_y, sp_p = load_sp(cfbd_dir, y), load_sp(cfbd_dir, y - 1)
        ret = load_returning(cfbd_dir, y)
        pin = load_portal_in(cfbd_dir, y, fbs)
        hc_y, hc_p = hc_by_team(cfbd_dir, y), hc_by_team(cfbd_dir, y - 1)
        for t in sp_y:
            if t in sp_p and t in ret:
                cc = 1 if (t in hc_y and t in hc_p and hc_y[t] != hc_p[t]) else 0
                rows.append((y, t, sp_y[t], sp_p[t], ret[t], pin.get(t, 0), cc))

    yv = np.array([r[2] for r in rows])
    prev = np.array([r[3] for r in rows])
    ret = np.array([r[4] for r in rows])
    pin = np.array([r[5] for r in rows], float)
    cc = np.array([r[6] for r in rows], float)
    ones = np.ones(len(rows))
    n = len(rows)

    def fit(cols, names):
        X = np.column_stack([ones] + cols)
        beta, resid, t = ols(X, yv)
        return resid.std(ddof=X.shape[1]), beta, t, names

    print(f"panel: {n} team-seasons, {rows[0][0]}-{rows[-1][0]} (CFBD canonical joins)")
    print(f"portal-era rows (>=2021): {sum(1 for r in rows if r[0] >= 2021)}\n")
    print("model progression — residual SD (= preseason miss) as offseason signal is added:")
    naive = (yv - prev).std()
    print(f"  naive (last-yr SP+ as-is, no fit): {naive:5.2f}")
    for cols, names in [
        ([prev], ["prev"]),
        ([prev, ret], ["prev", "returning"]),
        ([prev, ret, cc], ["prev", "returning", "coach_change"]),
        ([prev, ret, cc, pin], ["prev", "returning", "coach_change", "portal_in"]),
    ]:
        sig, beta, t, nm = fit(cols, names)
        print(f"  {'+'.join(names):38s} sigma={sig:5.2f}")
    base_sigma = fit([prev, ret, cc, pin], ["prev", "returning", "coach_change", "portal_in"])[0]

    print("\ndirectional test — full model coefficients (t-stat):")
    _, beta, t, _ = fit([prev, ret, cc, pin], ["prev", "returning", "coach_change", "portal_in"])
    for nm, b, tt in zip(["intercept", "prev_SP+", "returning", "coach_change", "portal_in"], beta, t):
        print(f"  {nm:14s} {b:+7.3f}  (t={tt:+.1f})")

    # churn multipliers: residual SD within buckets ÷ base
    X = np.column_stack([ones, prev, ret, cc, pin])
    _, resid, _ = ols(X, yv)
    print("\nchurn multipliers (bucket residual SD ÷ base_sigma):")
    lo, hi = np.quantile(ret, [1/3, 2/3])
    buckets = {
        "returning: low tercile": ret <= lo,
        "returning: mid tercile": (ret > lo) & (ret <= hi),
        "returning: high tercile": ret > hi,
        "coach change = yes": cc == 1,
        "coach change = no": cc == 0,
    }
    base = resid.std()
    for name, mask in buckets.items():
        s = resid[mask].std()
        print(f"  {name:26s} n={mask.sum():4d}  SD={s:5.2f}  mult={s/base:4.2f}")

    os.makedirs(outdir, exist_ok=True)
    summary = {
        "generated_from_cfbd_dir": cfbd_dir, "n_team_seasons": n,
        "year_range": [rows[0][0], rows[-1][0]],
        "base_sigma_full_model": round(float(base_sigma), 3),
        "naive_sigma": round(float(naive), 3),
        "coeffs": {nm: round(float(b), 4) for nm, b in zip(
            ["intercept", "prev_SP+", "returning", "coach_change", "portal_in"], beta)},
        "tstats": {nm: round(float(tt), 2) for nm, tt in zip(
            ["intercept", "prev_SP+", "returning", "coach_change", "portal_in"], t)},
        "multipliers": {name: round(float(resid[mask].std() / base), 3) for name, mask in buckets.items()},
        "caveat": "base_sigma here is preseason-MISS vs FINAL SP+, which conflates epistemic "
                  "(true-strength) uncertainty with in-season randomness. Splitting those ties to "
                  "the open sim double-counting question; treat this as an upper bound on the "
                  "epistemic band until resolved. PFF unit grades are the next signal to add (step 3).",
    }
    with open(f"{outdir}/backtest_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nbase_sigma (full model) = {base_sigma:.2f}  -> {outdir}/backtest_summary.json")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
