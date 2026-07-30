#!/usr/bin/env python3
"""S10: jump-term refinements per PREREGISTRATION_S10_S11_2026-07-28.md.
S10-A position-bucket jump; S10-B graded (offset-distance) jump. S1 harness."""
import csv, json, os
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = list(csv.DictReader(open('data/research/pairs.csv')))
for r in P:
    for k in ('grade_t', 'vol_t', 'grade_t1'):
        r[k] = float(r[k])
    r['moved'] = int(r['moved']); r['season_t'] = int(r['season_t'])
VOLMIN = {'QB': 50, 'RB': 25, 'WRTE': 50, 'OL': 100, 'DL': 100, 'LB': 100, 'DB': 100}
P = [r for r in P if r['vol_t'] >= VOLMIN[r['grp']]]
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
JUMPS = ['within', 'P4>G5', 'G5>P4']
BUCKET = {'QB': 'QB', 'OL': 'TR', 'DL': 'TR', 'RB': 'OT', 'WRTE': 'OT', 'LB': 'OT', 'DB': 'OT'}
BKS = ['QB', 'TR', 'OT']
C2G = {'SEC': 'SEC', 'American Athletic': 'AAC', 'ACC': 'ACC', 'Big Ten': 'B10', 'Big 12': 'B12',
       'Conference USA': 'CUSA', 'FBS Independents': 'IND', 'Mid-American': 'MAC',
       'Mountain West': 'MWC', 'Pac-12': 'PAC', 'Sun Belt': 'SBC'}
OFF = json.load(open('data/backtest/conf_offsets_2021_2025.json'))['offsets']
for r in P:
    o = OFF[r['grp']]
    gap = o.get(C2G.get(r['conf_t1'], 'IND'), 0) - o.get(C2G.get(r['conf_t'], 'IND'), 0)
    r['upgap'] = max(0.0, gap) if r['moved'] else 0.0
    r['dngap'] = max(0.0, -gap) if r['moved'] else 0.0


def base_cols(r):
    return [1.0, r['grade_t'], np.log1p(r['vol_t'])] + [1.0 if r['grp'] == g else 0.0 for g in GRPS[1:]]


def design(rows, mode):
    X, y = [], []
    for r in rows:
        row = base_cols(r)
        if mode == 'pooled':
            row += [1.0 if (r['moved'] and r['jump'] == j) else 0.0 for j in JUMPS]
        elif mode == 'bucket':
            row += [1.0 if (r['moved'] and r['jump'] == j and BUCKET[r['grp']] == b) else 0.0
                    for j in JUMPS for b in BKS]
        elif mode == 'graded':
            row += [1.0 if (r['moved'] and r['jump'] == 'within') else 0.0, r['upgap'], r['dngap']]
        X.append(row); y.append(r['grade_t1'])
    return np.array(X), np.array(y)


NJ = {'pooled': 3, 'bucket': 9, 'graded': 3}
seasons = [2021, 2022, 2023, 2024]
maes = {m: [] for m in NJ}
coef_folds = {m: [] for m in NJ}
for hold in seasons:
    tr = [r for r in P if r['season_t'] != hold]
    te = [r for r in P if r['season_t'] == hold and r['moved']]
    for m in NJ:
        X, y = design(tr, m); b, *_ = np.linalg.lstsq(X, y, rcond=None)
        Xt, yt = design(te, m)
        maes[m].append(float(np.mean(np.abs(Xt @ b - yt))))
        coef_folds[m].append(b[-NJ[m]:])
mm = {m: float(np.mean(v)) for m, v in maes.items()}
print(f"LOYO mover MAE: pooled {mm['pooled']:.4f} | bucket {mm['bucket']:.4f} | graded {mm['graded']:.4f}")
impA = 100 * (mm['pooled'] - mm['bucket']) / mm['pooled']
impB = 100 * (mm['pooled'] - mm['graded']) / mm['pooled']
print(f"S10-A MAE gain {impA:+.2f}% (bar >=0.5%) | S10-B gain {impB:+.2f}% (bar >=0.5%)")

# F-test for bucket split (full sample)
Xp, y = design(P, 'pooled'); Xb, _ = design(P, 'bucket')
bp, *_ = np.linalg.lstsq(Xp, y, rcond=None); bb, *_ = np.linalg.lstsq(Xb, y, rcond=None)
rss_p = float(np.sum((y - Xp @ bp) ** 2)); rss_b = float(np.sum((y - Xb @ bb) ** 2))
df_extra, df_res = 6, len(y) - Xb.shape[1]
F = ((rss_p - rss_b) / df_extra) / (rss_b / df_res)
from scipy import stats as st
pF = 1 - st.f.cdf(F, df_extra, df_res)
print(f"S10-A F-test: F={F:.2f}, p={pF:.4f} (bar <0.05)")

# sign stability
labels_b = [f'{j}|{b}' for j in JUMPS for b in BKS]
print("bucket coefs (full sample) + LOYO sign-stable?:")
for i, lab in enumerate(labels_b):
    vals = [f[i] for f in coef_folds['bucket']]
    n = sum(1 for r in P if r['moved'] and r['jump'] == lab.split('|')[0] and BUCKET[r['grp']] == lab.split('|')[1])
    stable = len({np.sign(v) for v in vals}) == 1
    print(f"  {lab:12s} {bb[-9 + i]:+.2f}  n={n:4d}  {'stable' if stable else 'FLIPS'}")
labels_g = ['within', 'upgap', 'dngap']
bg, *_ = np.linalg.lstsq(design(P, 'graded')[0], y, rcond=None)
print("graded coefs + stability:")
for i, lab in enumerate(labels_g):
    vals = [f[i] for f in coef_folds['graded']]
    stable = len({np.sign(v) for v in vals}) == 1
    print(f"  {lab:6s} {bg[-3 + i]:+.3f}  {'stable' if stable else 'FLIPS'}")
