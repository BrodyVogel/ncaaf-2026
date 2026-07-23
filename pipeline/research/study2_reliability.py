#!/usr/bin/env python3
"""Study 2: thin-sample reliability w(n) + shrinkage constant k + class-year aging.
Stayers only (same team both seasons). Pre-registered bars: S2-A monotone-ish, S2-B k CV<50%."""
import csv, json, os, re, unicodedata
import numpy as np
from collections import defaultdict

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = [r for r in csv.DictReader(open('data/research/pairs.csv')) if r['moved'] == '0']
for r in P:
    for k in ('grade_t', 'vol_t', 'grade_t1'): r[k] = float(r[k])
    r['season_t'] = int(r['season_t'])
GRPS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB']

def slope(rows):
    x = np.array([r['grade_t'] for r in rows]); y = np.array([r['grade_t1'] for r in rows])
    return float(np.polyfit(x, y, 1)[0]) if len(rows) > 25 else None

# ---- reliability by volume bucket, per group; fit w(n)=n/(n+k) ----
print("reliability slope of grade_t1 on grade_t by volume quintile (stayers):")
ks = {}
for g in GRPS:
    rows = [r for r in P if r['grp'] == g]
    qs = np.percentile([r['vol_t'] for r in rows], [20, 40, 60, 80])
    buckets = []
    for lo, hi in zip([0] + list(qs), list(qs) + [1e9]):
        b = [r for r in rows if lo <= r['vol_t'] < hi]
        s = slope(b)
        if s is not None: buckets.append((float(np.median([r['vol_t'] for r in b])), s, len(b)))
    # fit k by least squares on w(n)=n/(n+k)
    ns = np.array([b[0] for b in buckets]); ws = np.clip(np.array([b[1] for b in buckets]), 0.01, 0.99)
    kgrid = np.arange(5, 2000, 5)
    k = float(kgrid[np.argmin([np.sum((ns/(ns+kk) - ws)**2) for kk in kgrid])])
    ks[g] = k
    mono = all(buckets[i][1] <= buckets[i+1][1] + 0.05 for i in range(len(buckets)-1))
    print(f"  {g:5s} slopes {[f'{b[1]:.2f}@n{int(b[0])}' for b in buckets]}  k={k:.0f}  {'monotone-ok' if mono else 'NON-MONOTONE'}")

# ---- S2-B: k stability across LOYO folds ----
print("\nS2-B k stability (LOYO folds, CV bar <50%):")
for g in GRPS:
    kf = []
    for hold in (2021, 2022, 2023, 2024):
        rows = [r for r in P if r['grp'] == g and r['season_t'] != hold]
        qs = np.percentile([r['vol_t'] for r in rows], [20, 40, 60, 80])
        bs = []
        for lo, hi in zip([0] + list(qs), list(qs) + [1e9]):
            b = [r for r in rows if lo <= r['vol_t'] < hi]; s = slope(b)
            if s is not None: bs.append((float(np.median([r['vol_t'] for r in b])), s))
        ns = np.array([b[0] for b in bs]); ws = np.clip(np.array([b[1] for b in bs]), 0.01, 0.99)
        kgrid = np.arange(5, 2000, 5)
        kf.append(float(kgrid[np.argmin([np.sum((ns/(ns+kk) - ws)**2) for kk in kgrid])]))
    cv = 100 * np.std(kf) / np.mean(kf)
    print(f"  {g:5s} k folds {[int(x) for x in kf]}  CV {cv:.0f}%  {'PASS' if cv < 50 else 'FAIL'}")

# ---- aging curves via CFBD roster class years (2022+) ----
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())
cls = {}
for y in range(2022, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/roster_{y}.json')):
        nm = norm((r.get('firstName') or '') + (r.get('lastName') or ''))
        if r.get('year'): cls[(nm, y)] = int(r['year'])
YR = {1: 'FR', 2: 'SO', 3: 'JR', 4: 'SR'}
ag = defaultdict(list)
for r in P:
    if r['season_t'] < 2022: continue
    c = cls.get((norm(r['name']), r['season_t']))
    if c in YR: ag[YR[c]].append(r['grade_t1'] - r['grade_t'])
print("\naging: mean grade change t->t+1 by class year in season t (stayers):")
for c in ('FR', 'SO', 'JR', 'SR'):
    v = ag[c]; print(f"  {c}: {np.mean(v):+.2f} (n={len(v)})")
# per-year sign stability for the FR jump
for c in ('FR', 'SO'):
    yr = defaultdict(list)
    for r in P:
        if r['season_t'] < 2022: continue
        cc = cls.get((norm(r['name']), r['season_t']))
        if cc in YR and YR[cc] == c: yr[r['season_t']].append(r['grade_t1'] - r['grade_t'])
    print(f"  {c} by year: " + str({y: f'{np.mean(v):+.1f}' for y, v in sorted(yr.items())}))
