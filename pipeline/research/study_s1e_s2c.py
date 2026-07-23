#!/usr/bin/env python3
"""S1-E (origin talent for thin-tape movers) + S2-C (career pooling). Registered bars apply."""
import csv, json, os
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']
POSMEAN = {'QB': 69.7, 'RB': 73.5, 'WRTE': 62.6, 'OL': 62.0, 'DL': 64.9, 'LB': 62.3, 'DB': 65.2}
K = {'QB': 230, 'RB': 110, 'WRTE': 190, 'OL': 595, 'DL': 290, 'LB': 630, 'DB': 1180}
WCAP = {'QB': 0.55, 'LB': 0.50}
JUMP = {'P4>G5': 1.45, 'G5>P4': -3.54, 'within': 0.0, 'stay': 0.0}

S = list(csv.DictReader(open('data/research/spine.csv')))
for r in S:
    r['season'] = int(r['season']); r['grade'] = float(r['grade']); r['vol'] = float(r['vol'])
hist = defaultdict(list)
for r in sorted(S, key=lambda x: x['season']): hist[r['player_id']].append(r)

P = list(csv.DictReader(open('data/research/pairs.csv')))
for r in P:
    for k in ('grade_t', 'vol_t', 'grade_t1'): r[k] = float(r[k])
    r['season_t'] = int(r['season_t']); r['moved'] = int(r['moved'])
P = [r for r in P if r['vol_t'] >= 10]

# ---- talent z-scores by (team, year) ----
tal = {}
for y in range(2021, 2026):
    ent = json.load(open(f'data/cfbd/2026-07-12/talent_{y}.json'))
    import re, unicodedata
    def norm(s):
        s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
        return re.sub(r'[^a-z0-9]', '', s.lower())
    vals = [(norm(e.get('school') or e.get('team', '')), float(e['talent'])) for e in ent if e.get('talent') is not None]
    m = np.mean([v for _, v in vals]); sd = np.std([v for _, v in vals])
    for t, v in vals: tal[(t, y)] = (v - m) / sd

# ================= S1-E =================
mv = [r for r in P if r['moved'] and (r['team_t'], r['season_t']) in tal]
for r in mv: r['tz'] = tal[(r['team_t'], r['season_t'])]
med = {g: np.median([r['vol_t'] for r in mv if r['grp'] == g]) for g in GRPS}
thin = [r for r in mv if r['vol_t'] < med[r['grp']]]

def base_X(rows):
    return np.array([[1, r['grade_t'], np.log1p(r['vol_t'])] + [1.0 if r['grp'] == g else 0 for g in GRPS[1:]]
                     + [1.0 if r['jump'] == j else 0 for j in ('P4>G5', 'G5>P4')] for r in rows])
def r2(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); e = y - X @ b
    return 1 - e @ e / ((y - y.mean()) @ (y - y.mean())), b
for lab, sample in (('all movers', mv), ('THIN movers', thin)):
    X0 = base_X(sample); y = np.array([r['grade_t1'] for r in sample])
    X1 = np.column_stack([X0, [r['tz'] for r in sample]])
    a, _ = r2(X0, y); b_, bb = r2(X1, y)
    print(f"S1-E {lab}: n={len(sample)}  dR2={b_-a:.4f}  talent coef {bb[-1]:+.2f}/SD")
signs = []
for hold in (2021, 2022, 2023, 2024):
    tr = [r for r in thin if r['season_t'] != hold]
    X1 = np.column_stack([base_X(tr), [r['tz'] for r in tr]])
    _, bb = r2(X1, np.array([r['grade_t1'] for r in tr]))
    signs.append(np.sign(bb[-1]))
print(f"S1-E thin-mover LOYO talent-coef signs: {signs} ({'STABLE' if len(set(signs))==1 else 'FLIPS'})")

# ================= S2-C =================
DECAY = 0.5
def pooled(pid, t):
    num = den = 0.0
    for r in hist[pid]:
        if r['season'] > t: break
        w = r['vol'] * (DECAY ** (t - r['season']))
        num += w * r['grade']; den += w
    return (num / den if den else None), den
def w_of(n, g):
    w = n / (n + K[g])
    return min(w, WCAP.get(g, 1.0))
def v2pred(r, evid, n):
    pm = POSMEAN[r['grp']]
    return pm + w_of(n, r['grp']) * (evid - pm) + JUMP[r['jump']]
def mae(rows, arm):
    errs = []
    for r in rows:
        if arm == 'single':
            p = v2pred(r, r['grade_t'], r['vol_t'])
        else:
            pg, ne = pooled(r['player_id'], r['season_t'])
            p = v2pred(r, pg, ne)
        errs.append(abs(p - r['grade_t1']))
    return float(np.mean(errs))
nprior = {}
for r in P:
    nprior[id(r)] = sum(1 for h in hist[r['player_id']] if h['season'] < r['season_t'])
multi = [r for r in P if nprior[id(r)] >= 2]
mvs = [r for r in P if r['moved']]
res = {}
for lab, rows in (('overall', P), ('multi-history(>=2 prior yrs)', multi), ('movers', mvs)):
    s = np.mean([mae([r], 'single') for r in []]) if False else mae(rows, 'single')
    p_ = mae(rows, 'pooled')
    res[lab] = (s, p_)
    print(f"S2-C {lab:30s} n={len(rows):5d}  single MAE {s:.3f}  pooled {p_:.3f}  ({100*(s-p_)/s:+.1f}%)")
# LOYO check overall
loyo = []
for hold in (2021, 2022, 2023, 2024):
    te = [r for r in P if r['season_t'] == hold]
    loyo.append((mae(te, 'single'), mae(te, 'pooled')))
print("S2-C LOYO per-fold (single, pooled):", [(f"{a:.2f}", f"{b:.2f}") for a, b in loyo])
# the Brody case: journeymen = >=2 prior seasons AND thin current tape
jm = [r for r in multi if r['vol_t'] < med.get(r['grp'], 1e9)]
print(f"S2-C journeyman slice (multi-history + thin current): n={len(jm)}  single {mae(jm,'single'):.3f}  pooled {mae(jm,'pooled'):.3f}  ({100*(mae(jm,'single')-mae(jm,'pooled'))/mae(jm,'single'):+.1f}%)")
