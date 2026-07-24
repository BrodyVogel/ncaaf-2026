#!/usr/bin/env python3
"""Study 4: retention calibration of w(n) shrinkage. Registered bars in
docs/research/PREREGISTRATION_S4_2026-07-24.md (committed before this ran).
LOYO over season_t 2021-2024, stayers, vol>=10."""
import csv, os
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
GRPS = list(POSMEAN)
FOLDS = [2021, 2022, 2023, 2024]

R = []
for r in csv.DictReader(open('data/research/pairs.csv')):
    if r['moved'] != '0' or r['grp'] not in POSMEAN: continue
    v = float(r['vol_t'])
    if v < 10: continue
    g = r['grp']
    R.append(dict(g=g, s=int(r['season_t']), v=v,
                  x=float(r['grade_t']) - POSMEAN[g],
                  y=float(r['grade_t1']) - POSMEAN[g]))
print(f"n={len(R)} stayer pairs | folds {FOLDS}")

def w_of(v, g, k=None, cap=None):
    k = K[g] if k is None else k
    c = (WCAP.get(g, 1.0) if cap is None else cap)
    return min(v / (v + k), c)

def alphas(rows):
    a = {}
    for g in GRPS:
        rr = [r for r in rows if r['g'] == g]
        a[g] = float(np.mean([r['y'] - w_of(r['v'], g) * r['x'] for r in rr])) if rr else 0.0
    return a

# ---------- S4-A: global residual slope, per fold ----------
print("\n== S4-A: residual slope beta (r = alpha_g + beta*x), per fold ==")
betas = []
for f in FOLDS:
    tr = [r for r in R if r['s'] == f]          # slope measured within each fold
    a = alphas(tr)
    xs = np.array([r['x'] for r in tr])
    rs = np.array([r['y'] - w_of(r['v'], r['g']) * r['x'] - a[r['g']] for r in tr])
    b = float(np.polyfit(xs, rs, 1)[0])
    betas.append(b)
    print(f"  fold {f}: beta {b:+.4f} (n={len(tr)})")
xa = np.array([r['x'] for r in R]); aP = alphas(R)
ra = np.array([r['y'] - w_of(r['v'], r['g']) * r['x'] - aP[r['g']] for r in R])
bP = float(np.polyfit(xa, ra, 1)[0])
s4a = all(b > 0 for b in betas) and bP >= 0.02
print(f"  pooled beta {bP:+.4f} | sign-stable {all(b>0 for b in betas)} | S4-A {'PASS' if s4a else 'FAIL'}")

# ---------- S4-B: piecewise beyond linear ----------
print("\n== S4-B: piecewise slopes (terciles of x within group, train-fold cuts) ==")
def fit_eval(train, test, model):
    a = alphas(train)
    if model == 'base':
        pred = lambda r: a[r['g']] + w_of(r['v'], r['g']) * r['x']
    elif model == 'lin':
        xs = np.array([r['x'] for r in train])
        rs = np.array([r['y'] - w_of(r['v'], r['g']) * r['x'] - a[r['g']] for r in train])
        b = float(np.polyfit(xs, rs, 1)[0])
        pred = lambda r: a[r['g']] + (w_of(r['v'], r['g']) + b) * r['x']
    elif model == 'pw':
        cuts = {g: np.percentile([r['x'] for r in train if r['g'] == g], [33.3, 66.7]) for g in GRPS}
        bs = {}
        for t_ in ('lo', 'mid', 'hi'):
            sel = [r for r in train if tier(r, cuts) == t_]
            xs = np.array([r['x'] for r in sel])
            rs = np.array([r['y'] - w_of(r['v'], r['g']) * r['x'] - a[r['g']] for r in sel])
            bs[t_] = float(np.polyfit(xs, rs, 1)[0]) if len(sel) > 50 and xs.std() > 1e-6 else 0.0
        pred = lambda r: a[r['g']] + (w_of(r['v'], r['g']) + bs[tier(r, cuts)]) * r['x']
        fit_eval.last_bs = bs
    return float(np.mean([abs(r['y'] - pred(r)) for r in test]))

def tier(r, cuts):
    lo, hi = cuts[r['g']]
    return 'lo' if r['x'] <= lo else ('hi' if r['x'] > hi else 'mid')

mae = {m: [] for m in ('base', 'lin', 'pw')}
pw_deltas = []
for f in FOLDS:
    tr = [r for r in R if r['s'] != f]; te = [r for r in R if r['s'] == f]
    for m in mae: mae[m].append(fit_eval(tr, te, m))
    bs = fit_eval.last_bs
    pw_deltas.append((bs['hi'] - bs['mid'], bs['lo'] - bs['mid']))
    print(f"  fold-out {f}: MAE base {mae['base'][-1]:.4f}  lin {mae['lin'][-1]:.4f}  pw {mae['pw'][-1]:.4f}"
          f" | b_hi-b_mid {bs['hi']-bs['mid']:+.4f} b_lo-b_mid {bs['lo']-bs['mid']:+.4f}")
mb, ml, mp = (float(np.mean(mae[m])) for m in ('base', 'lin', 'pw'))
hi_stab = all(d[0] > 0 for d in pw_deltas) or all(d[0] < 0 for d in pw_deltas)
lo_stab = all(d[1] > 0 for d in pw_deltas) or all(d[1] < 0 for d in pw_deltas)
s4b = hi_stab and lo_stab and (ml - mp) >= 0.05
print(f"  LOYO MAE: base {mb:.4f} | +linear {ml:.4f} | +piecewise {mp:.4f}"
      f" | hi-stab {hi_stab} lo-stab {lo_stab} | S4-B {'PASS' if s4b else 'FAIL'}")

# ---------- S4-C: k / cap refit per group ----------
print("\n== S4-C: per-group k* (and QB/LB cap*) by LOYO MAE grid ==")
KGRID = [0.25, 0.35, 0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0]
CAPG = {g: ([WCAP[g], 0.65, 0.75, 1.0] if g in WCAP else [1.0]) for g in GRPS}
best = {}
for g in GRPS:
    rows = [r for r in R if r['g'] == g]
    res = {}
    for km in KGRID:
        for cap in CAPG[g]:
            k = K[g] * km
            maes, dirs = [], []
            for f in FOLDS:
                tr = [r for r in rows if r['s'] != f]; te = [r for r in rows if r['s'] == f]
                a = float(np.mean([r['y'] - w_of(r['v'], g, k, cap) * r['x'] for r in tr]))
                maes.append(float(np.mean([abs(r['y'] - a - w_of(r['v'], g, k, cap) * r['x']) for r in te])))
            res[(km, cap)] = float(np.mean(maes))
    (km, cap), m = min(res.items(), key=lambda kv: kv[1])
    ship = res[(1.0, WCAP.get(g, 1.0))]
    # fold-direction consistency: within each fold, does the best km sit on the same side of 1.0?
    sides = []
    for f in FOLDS:
        tr = [r for r in rows if r['s'] != f]; te = [r for r in rows if r['s'] == f]
        fres = {}
        for km2 in KGRID:
            for cap2 in CAPG[g]:
                k2 = K[g] * km2
                a = float(np.mean([r['y'] - w_of(r['v'], g, k2, cap2) * r['x'] for r in tr]))
                fres[(km2, cap2)] = float(np.mean([abs(r['y'] - a - w_of(r['v'], g, k2, cap2) * r['x']) for r in te]))
        (bkm, bcap), _ = min(fres.items(), key=lambda kv: kv[1])
        sides.append('lt' if bkm < 1.0 else ('gt' if bkm > 1.0 else 'eq'))
    stable = len(set(sides)) == 1
    best[g] = dict(km=km, cap=cap, mae=m, ship=ship, gain=ship - m, sides=sides, stable=stable)
    sv = {'QB': 350, 'RB': 180, 'WRTE': 350, 'OL': 800, 'DL': 500, 'LB': 700, 'DB': 900}[g]
    print(f"  {g:4s}: k* = {km:.2f}x ({K[g]*km:.0f}) cap* {cap:.2f} | LOYO MAE {m:.4f} vs shipped {ship:.4f}"
          f" (gain {ship-m:+.4f}) | fold sides {sides} {'STABLE' if stable else 'UNSTABLE'}"
          f" | w(starter {sv}) {w_of(sv,g):.2f} -> {w_of(sv,g,K[g]*km,cap):.2f}")
pool_gain = float(np.mean([best[g]['ship'] for g in GRPS]) - np.mean([best[g]['mae'] for g in GRPS]))
n_stable = sum(1 for g in GRPS if best[g]['stable'] and best[g]['km'] != 1.0)
s4c = pool_gain >= 0.03 and n_stable >= 1 and all(best[g]['stable'] or best[g]['km'] == 1.0 for g in GRPS)
print(f"  pooled LOYO gain {pool_gain:+.4f} | S4-C {'PASS' if s4c else 'FAIL'} "
      f"(stable-and-moved groups: {[g for g in GRPS if best[g]['stable'] and best[g]['km'] != 1.0]})")

# ---------- S4-D: report-only volume texture ----------
print("\n== S4-D (report-only): residual slope by volume tercile ==")
vq = np.percentile([r['v'] for r in R], [33.3, 66.7])
for lbl, sel in (('lo-vol', lambda r: r['v'] <= vq[0]), ('mid-vol', lambda r: vq[0] < r['v'] <= vq[1]),
                 ('hi-vol', lambda r: r['v'] > vq[1])):
    rr = [r for r in R if sel(r)]
    xs = np.array([r['x'] for r in rr])
    rs = np.array([r['y'] - w_of(r['v'], r['g']) * r['x'] - aP[r['g']] for r in rr])
    print(f"  {lbl}: beta {float(np.polyfit(xs, rs, 1)[0]):+.4f} (n={len(rr)})")

print(f"\n=== registered decision: S4-A {'PASS' if s4a else 'FAIL'} | S4-B {'PASS' if s4b else 'FAIL'}"
      f" | S4-C {'PASS' if s4c else 'FAIL'} ===")
