#!/usr/bin/env python3
"""Study 1: transfer translation. Pre-registered bars: docs/research/PREREGISTRATION_2026-07-23.md.
LOYO across transitions 2021-24 -> t+1. Summary prints only."""
import csv, json, os
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = list(csv.DictReader(open('data/research/pairs.csv')))
for r in P:
    for k in ('grade_t', 'vol_t', 'grade_t1', 'p4_t', 'p4_t1'): r[k] = float(r[k])
    r['moved'] = int(r['moved']); r['season_t'] = int(r['season_t'])

VOLMIN = {'QB': 50, 'RB': 25, 'WRTE': 50, 'OL': 100, 'DL': 100, 'LB': 100, 'DB': 100}
P = [r for r in P if r['vol_t'] >= VOLMIN[r['grp']]]
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
JUMPS = ['within', 'P4>G5', 'G5>P4']

# CFBD conference -> offsets-file group key
C2G = {'SEC': 'SEC', 'American Athletic': 'AAC', 'ACC': 'ACC', 'Big Ten': 'B10', 'Big 12': 'B12',
       'Conference USA': 'CUSA', 'FBS Independents': 'IND', 'Mid-American': 'MAC',
       'Mountain West': 'MWC', 'Pac-12': 'PAC', 'Sun Belt': 'SBC'}
OFF = json.load(open('data/backtest/conf_offsets_2021_2025.json'))['offsets']
def flat_offset_pred(r):
    o = OFF[r['grp']]
    return r['grade_t'] + o.get(C2G.get(r['conf_t'], 'IND'), 0) - o.get(C2G.get(r['conf_t1'], 'IND'), 0)

def design(rows, coefs_only=False):
    X, y = [], []
    for r in rows:
        row = [1.0, r['grade_t'], np.log1p(r['vol_t'])]
        row += [1.0 if r['grp'] == g else 0.0 for g in GRPS[1:]]
        row += [1.0 if (r['moved'] and r['jump'] == j) else 0.0 for j in JUMPS]
        X.append(row); y.append(r['grade_t1'])
    return np.array(X), np.array(y)

COLS = ['const', 'grade_t', 'log_vol'] + GRPS[1:] + JUMPS

# ---- LOYO: fit on 3 transitions, evaluate MOVERS in the held-out one ----
seasons = [2021, 2022, 2023, 2024]
signs = {j: [] for j in JUMPS}; maes = {'model': [], 'carry': [], 'flat': []}
for hold in seasons:
    tr = [r for r in P if r['season_t'] != hold]
    te = [r for r in P if r['season_t'] == hold and r['moved']]
    X, y = design(tr); b, *_ = np.linalg.lstsq(X, y, rcond=None)
    for j in JUMPS: signs[j].append(np.sign(b[COLS.index(j)]))
    Xt, yt = design(te); pred = Xt @ b
    maes['model'].append(np.mean(np.abs(pred - yt)))
    maes['carry'].append(np.mean(np.abs(np.array([r['grade_t'] for r in te]) - yt)))
    maes['flat'].append(np.mean(np.abs(np.array([flat_offset_pred(r) for r in te]) - yt)))
m = {k: float(np.mean(v)) for k, v in maes.items()}
print(f"S1-A LOYO MAE (movers): model {m['model']:.3f} | carry-forward {m['carry']:.3f} | flat-offset {m['flat']:.3f}")
print(f"      vs carry: {100*(m['carry']-m['model'])/m['carry']:+.1f}% (bar >=2%) | vs flat: {100*(m['flat']-m['model'])/m['flat']:+.1f}% (bar: beat or tie within 0.5%)")
print(f"S1-B sign stability: " + str({j: ('STABLE' if len(set(signs[j])) == 1 else 'FLIPS ' + str(signs[j])) for j in JUMPS}))

# ---- full-sample coefficients (for effect sizes) ----
X, y = design(P); b, *_ = np.linalg.lstsq(X, y, rcond=None)
resid = y - X @ b; s2 = resid @ resid / (len(y) - len(b))
se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
print("\nfull-sample move effects vs stayers (grade pts):")
for j in JUMPS:
    i = COLS.index(j); print(f"  {j:7s} {b[i]:+.2f}  (se {se[i]:.2f})")
print(f"  grade_t slope {b[1]:.3f} (regression-to-mean applies to everyone)")

# ---- usage-tercile interaction for P4->G5 (owner question) ----
p4g5 = [r for r in P if r['jump'] == 'P4>G5']
terc = np.percentile([r['vol_t'] for r in p4g5], [33, 67])
print("\nP4->G5 by prior-usage tercile (mean grade change t->t+1, n):")
for lo, hi, lab in [(0, terc[0], 'low'), (terc[0], terc[1], 'mid'), (terc[1], 1e9, 'high')]:
    g = [r['grade_t1'] - r['grade_t'] for r in p4g5 if lo <= r['vol_t'] < hi]
    print(f"  {lab:4s} usage: {np.mean(g):+.2f} (n={len(g)})")
sty = [r['grade_t1'] - r['grade_t'] for r in P if not r['moved']]
print(f"  stayers baseline: {np.mean(sty):+.2f} (n={len(sty)})")

# ---- S1-C: stars incremental value on movers ----
mv = [r for r in P if r['moved'] and r['stars']]
Xb = np.array([[1, r['grade_t'], np.log1p(r['vol_t'])] + [1.0 if r['grp'] == g else 0 for g in GRPS[1:]] for r in mv])
ys = np.array([r['grade_t1'] for r in mv])
Xs = np.column_stack([Xb, [float(r['stars']) for r in mv]])
def r2(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); e = y - X @ b
    return 1 - e @ e / ((y - y.mean()) @ (y - y.mean()))
print(f"\nS1-C stars on movers (n={len(mv)}): R2 base {r2(Xb,ys):.4f} -> +stars {r2(Xs,ys):.4f} "
      f"(delta {r2(Xs,ys)-r2(Xb,ys):.4f}, bar >=0.01)")

# ---- S1-D: no-prior-tape entrants (stars vs first FBS grade) ----
S = list(csv.DictReader(open('data/research/spine.csv')))
seen = {}
for r in S: seen.setdefault(r['player_id'], []).append(int(r['season']))
first = {pid: min(ys_) for pid, ys_ in seen.items()}
byname = {}
for r in S:
    if int(r['season']) == first[r['player_id']]:
        byname.setdefault((r['name'].lower(), int(r['season'])), r)
import re, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())
pairs_sd = []
for yy in range(2022, 2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/portal_{yy}.json')):
        if not e.get('stars'): continue
        nm = ((e.get('firstName') or '') + ' ' + (e.get('lastName') or '')).lower()
        row = byname.get((nm, yy))
        if row and float(row['vol']) >= VOLMIN[row['grp']]:
            pairs_sd.append((float(e['stars']), float(row['grade'])))
if len(pairs_sd) > 30:
    a = np.array(pairs_sd)
    print(f"S1-D no-prior-tape entrants (n={len(a)}): corr(stars, first-FBS grade) = {np.corrcoef(a[:,0],a[:,1])[0,1]:.3f} (bar >=0.15)")

# ---- destination-conference effects among movers (report-only) ----
mv2 = [r for r in P if r['moved']]
Xb2 = np.array([[1, r['grade_t'], np.log1p(r['vol_t'])] + [1.0 if r['grp'] == g else 0 for g in GRPS[1:]] for r in mv2])
y2 = np.array([r['grade_t1'] for r in mv2])
b2, *_ = np.linalg.lstsq(Xb2, y2, rcond=None)
res2 = y2 - Xb2 @ b2
from collections import defaultdict
dc = defaultdict(list)
for r, e in zip(mv2, res2): dc[r['conf_t1']].append(e)
tab = sorted(((np.mean(v), len(v), c) for c, v in dc.items() if len(v) >= 40), reverse=True)
print("\ndest-conference residuals (movers, n>=40, +=overperform):")
for m_, n_, c in tab[:3] + tab[-3:]: print(f"  {c:20s} {m_:+.2f} (n={n_})")
