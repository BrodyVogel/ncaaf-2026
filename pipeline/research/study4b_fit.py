#!/usr/bin/env python3
"""Study 4b: fit w'(n) = min(n/(n+k'), plateau) per group. Registered bars in
PREREGISTRATION_S4B_2026-07-24.md (committed before this ran)."""
import csv, os, json
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
GRPS = list(POSMEAN)
FOLDS = [2021, 2022, 2023, 2024]
MGRID = [0.15, 0.20, 0.25, 0.35, 0.50, 0.70, 0.85, 1.00, 1.20]
PGRID = [round(0.350 + 0.025 * i, 3) for i in range(15)]   # 0.350..0.700

R = defaultdict(list)
for r in csv.DictReader(open('data/research/pairs.csv')):
    if r['moved'] != '0' or r['grp'] not in POSMEAN: continue
    v = float(r['vol_t'])
    if v < 10: continue
    g = r['grp']
    R[g].append((v, float(r['grade_t']) - POSMEAN[g], float(r['grade_t1']) - POSMEAN[g],
                 int(r['season_t'])))

def w_ship(v, g): return min(v / (v + K[g]), WCAP.get(g, 1.0))
def w_new(v, g, m, p): return min(v / (v + K[g] * m), p)

def fit_group(rows, train_seasons):
    """Grid-fit (m, p) minimizing LOYO-inner? No: fit on TRAIN by in-sample MAE (grid),
    per registered spec the selection metric is LOYO test MAE — so selection happens
    at the caller using per-fold train fits evaluated on the fold's test."""
    tr = [r for r in rows if r[3] in train_seasons]
    best, bm, bp = None, None, None
    for m in MGRID:
        for p in PGRID:
            a = np.mean([y - w_new(v, g_cur, m, p) * x for v, x, y, s in tr])
            mae = np.mean([abs(y - a - w_new(v, g_cur, m, p) * x) for v, x, y, s in tr])
            if best is None or mae < best:
                best, bm, bp = mae, m, p
    return bm, bp

pooled_fit, fold_fits, mae_ship_all, mae_new_all = {}, defaultdict(dict), [], []
detail = {}
for g in GRPS:
    g_cur = g
    rows = R[g]
    # pooled fit (all four transitions)
    pm, pp = fit_group(rows, set(FOLDS))
    pooled_fit[g] = (pm, pp)
    # per-fold train fits + LOYO evaluation of the *train-fit* params on held-out fold
    maes_ship, maes_new = [], []
    for f in FOLDS:
        trs = set(FOLDS) - {f}
        fm, fp = fit_group(rows, trs)
        fold_fits[g][f] = (fm, fp)
        tr = [r for r in rows if r[3] != f]; te = [r for r in rows if r[3] == f]
        a_s = np.mean([y - w_ship(v, g) * x for v, x, y, s in tr])
        a_n = np.mean([y - w_new(v, g, fm, fp) * x for v, x, y, s in tr])
        maes_ship.append(np.mean([abs(y - a_s - w_ship(v, g) * x) for v, x, y, s in te]))
        maes_new.append(np.mean([abs(y - a_n - w_new(v, g, fm, fp) * x) for v, x, y, s in te]))
    mae_ship_all.append(np.mean(maes_ship)); mae_new_all.append(np.mean(maes_new))
    detail[g] = dict(pooled=(pm, pp), folds=dict(fold_fits[g]),
                     mae_ship=float(np.mean(maes_ship)), mae_new=float(np.mean(maes_new)))
    sv = {'QB': 350, 'RB': 180, 'WRTE': 350, 'OL': 800, 'DL': 500, 'LB': 700, 'DB': 900}[g]
    lv = {'QB': 80, 'RB': 50, 'WRTE': 90, 'OL': 200, 'DL': 120, 'LB': 160, 'DB': 220}[g]
    print(f"{g:4s}: pooled k'={K[g]*pm:5.0f} ({pm:.2f}x) plateau {pp:.3f} | folds " +
          " ".join(f"{f}:({fold_fits[g][f][0]:.2f}x,{fold_fits[g][f][1]:.3f})" for f in FOLDS) +
          f" | LOYO MAE {np.mean(maes_ship):.4f}->{np.mean(maes_new):.4f}" +
          f" | w(thin {lv}) {w_ship(lv,g):.2f}->{w_new(lv,g,pm,pp):.2f}  w(starter {sv}) {w_ship(sv,g):.2f}->{w_new(sv,g,pm,pp):.2f}")

# ---- B1: pooled LOYO MAE gain ----
gain = float(np.mean(mae_ship_all) - np.mean(mae_new_all))
b1 = gain >= 0.015
print(f"\nB1 accuracy: pooled LOYO gain {gain:+.4f} (bar +0.015) -> {'PASS' if b1 else 'FAIL'}")

# ---- B2: residual slope collapse under pooled fit ----
betas = []
for f in FOLDS:
    xs, rs = [], []
    for g in GRPS:
        pm, pp = pooled_fit[g]
        rr = [r for r in R[g] if r[3] == f]
        a = np.mean([y - w_new(v, g, pm, pp) * x for v, x, y, s in rr])
        xs += [x for v, x, y, s in rr]
        rs += [y - a - w_new(v, g, pm, pp) * x for v, x, y, s in rr]
    betas.append(float(np.polyfit(np.array(xs), np.array(rs), 1)[0]))
xs, rs = [], []
for g in GRPS:
    pm, pp = pooled_fit[g]
    rr = R[g]
    a = np.mean([y - w_new(v, g, pm, pp) * x for v, x, y, s in rr])
    xs += [x for v, x, y, s in rr]
    rs += [y - a - w_new(v, g, pm, pp) * x for v, x, y, s in rr]
bp_ = float(np.polyfit(np.array(xs), np.array(rs), 1)[0])
same_sign = all(b > 0 for b in betas) or all(b < 0 for b in betas)
b2 = abs(bp_) <= 0.02 and not same_sign
print(f"B2 calibration: pooled beta {bp_:+.4f} | folds {[f'{b:+.3f}' for b in betas]} | "
      f"same-sign {same_sign} -> {'PASS' if b2 else 'FAIL'}")

# ---- B3: parameter stability ----
b3 = True
for g in GRPS:
    pm, pp = pooled_fit[g]
    for f in FOLDS:
        fm, fp = fold_fits[g][f]
        if abs(fp - pp) > 0.05: b3 = False; print(f"  B3 plateau drift {g} fold {f}: {fp} vs {pp}")
        side = lambda m: 'lt' if m < 1.0 else ('gt' if m > 1.0 else 'eq')
        if side(fm) != side(pm) and side(fm) != 'eq' and side(pm) != 'eq':
            b3 = False; print(f"  B3 m-side flip {g} fold {f}: {fm} vs {pm}")
print(f"B3 stability -> {'PASS' if b3 else 'FAIL'}")
print(f"\n=== Study 4b: {'ALL BARS PASS' if (b1 and b2 and b3) else 'FAIL — nothing ships'} ===")
json.dump({g: dict(m=pooled_fit[g][0], k=K[g] * pooled_fit[g][0], plateau=pooled_fit[g][1])
           for g in GRPS} | {'_meta': dict(b1=b1, b2=b2, b3=b3, gain=gain, beta=bp_)},
          open('/tmp/s4b_fit.json', 'w'), indent=1)
print("fit written to /tmp/s4b_fit.json")
