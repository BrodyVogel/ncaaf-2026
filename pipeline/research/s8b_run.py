#!/usr/bin/env python3
"""S8b: live-mirror shadow-arm re-test, per PREREGISTRATION_S8B_2026-07-27.md.

Chain per season: shadow unit VALUES (with per-team independent classing/offsets)
-> within-year OLS conversion onto preseason SP+ off/def splits -> match_spread
un-shrink -> resid -> conference demeaning (pseudo-pools; debut-excluded)
-> level-strip -> R_pre (primary) and R_adj = clip(0.35*R_pre, +/-6) + ST (companion).
Outputs: data/research/s8b_panel.csv + printed report.
"""
import csv, json, math, os, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8_shadow_arm import (build_shadow, load_spine, norm, GRPS, R, is_p4, conf_map)

YEARS = [2022, 2023, 2024, 2025]
OFFU, DEFU = ['QB', 'RB', 'WRTE', 'OL'], ['DL', 'LB', 'DB']
SP_ALIAS = {'connecticut': 'uconn'}
DEBUT = {(2022, 'jamesmadison'), (2023, 'jacksonvillestate'), (2023, 'samhouston'),
         (2024, 'kennesawstate'), (2025, 'delaware'), (2025, 'missouristate')}

# ---- per-team independent classing (registered) ----
OVR = {'p4': {}, 'offgrp': {}}
for s in range(2020, 2026):
    OVR['p4'][(s, 'notredame')] = True;  OVR['offgrp'][(s, 'notredame')] = 'ACC'
    OVR['p4'][(s, 'uconn')] = False;     OVR['offgrp'][(s, 'uconn')] = 'G5MEAN'
for s in range(2020, 2023):
    OVR['p4'][(s, 'byu')] = True;        OVR['offgrp'][(s, 'byu')] = 'B12'
    OVR['p4'][(s, 'liberty')] = False;   OVR['offgrp'][(s, 'liberty')] = 'G5MEAN'
    OVR['p4'][(s, 'newmexicostate')] = False; OVR['offgrp'][(s, 'newmexicostate')] = 'G5MEAN'
for s in range(2020, 2024):
    OVR['p4'][(s, 'army')] = False;      OVR['offgrp'][(s, 'army')] = 'G5MEAN'
for s in range(2020, 2025):
    OVR['p4'][(s, 'umass')] = False;     OVR['offgrp'][(s, 'umass')] = 'G5MEAN'


def read_sp(year):
    out = {}
    with open(f'{R}/data/backtest/sp_preseason/SP+_{year}_preseason.csv') as f:
        for r in csv.DictReader(f):
            k = SP_ALIAS.get(r['norm_key'], r['norm_key'])
            out[k] = (float(r['sp_plus_overall']), float(r['sp_plus_off']), float(r['sp_plus_def']))
    fin = {}
    with open(f'{R}/data/backtest/sp_final/SP+_{year}_final.csv') as f:
        for r in csv.DictReader(f):
            k = SP_ALIAS.get(r['norm_key'], r['norm_key'])
            fin[k] = float(r['final_overall'])
    return out, fin


def ols(X, y):
    A = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ b
    dof = len(y) - A.shape[1]
    cov = (resid @ resid / dof) * np.linalg.pinv(A.T @ A)
    return b, b / np.sqrt(np.diag(cov)), resid


def match_spread(x, target):
    mx, sx = float(x.mean()), float(x.std())
    return x.copy() if sx < 1e-9 else mx + (x - mx) * (float(np.std(target)) / sx)


def st_pcts(year):
    """team_nk -> y-1 PFF team SPEC percentile (0-100)."""
    prev = year - 1
    path = (f'{R}/data/pff_history/{prev}/PFF_{prev}_team_grades.csv' if prev < 2025
            else f'{R}/data/pff/PFF_2025_team_grades.csv')
    ALIAS = {'olemiss': 'olemiss', 'centralflorida': 'ucf', 'miamifl': 'miami',
             'southerncal': 'usc', 'louisianalafayette': 'louisiana', 'ulmonroe': 'louisianamonroe',
             'umass': 'massachusetts', 'uconn': 'uconn', 'pitt': 'pittsburgh',
             'appstate': 'appalachianstate', 'sanjosest': 'sanjosestate', 'hawaii': 'hawaii'}
    import re as _re
    vals = {}
    for r in csv.DictReader(open(path)):
        tk = norm(r['TEAM']); tk = _re.sub(r'st$', 'state', tk); tk = ALIAS.get(tk, tk)
        if tk == 'massachusetts': tk = 'umass'
        try:
            vals[tk] = float(r['SPEC'])
        except ValueError:
            pass
    sv = sorted(vals.values()); n = len(sv)
    return {tk: 100.0 * sum(1 for x in sv if x < v) / (n - 1) for tk, v in vals.items()}


spine = load_spine()
panel = []
for y in YEARS:
    units, diag = build_shadow(y, 'roster', spine, overrides=OVR)
    sp, fin = read_sp(y)
    confs = conf_map(y)
    stp = st_pcts(y)

    teams = sorted({tk for (tk, u) in units if tk in sp and tk in fin})
    umean = {u: float(np.mean([units[(t, u)]['value'] for t in teams if (t, u) in units]))
             for u in GRPS}
    V = {t: {u: units.get((t, u), {'value': umean[u]})['value'] for u in GRPS} for t in teams}
    complete = [t for t in teams if all((t, u) in units for u in GRPS)]
    fitset = [t for t in complete if (y, t) not in DEBUT]

    # conversion (within-year, mirroring final_pass)
    Xo_f = [np.array([V[t][u] for t in fitset]) for u in OFFU]
    Xd_f = [np.array([V[t][u] for t in fitset]) for u in DEFU]
    yo = np.array([sp[t][1] for t in fitset]); yd = np.array([sp[t][2] for t in fitset])
    bo, _, _ = ols(Xo_f, yo); bd, _, _ = ols(Xd_f, yd)
    io = {t: bo[0] + sum(b * V[t][u] for b, u in zip(bo[1:], OFFU)) for t in teams}
    idf = {t: bd[0] + sum(b * V[t][u] for b, u in zip(bd[1:], DEFU)) for t in teams}
    io_f = np.array([io[t] for t in fitset]); idf_f = np.array([idf[t] for t in fitset])
    so, sd_ = match_spread(io_f, yo), match_spread(idf_f, yd)
    # apply the same affine rescale to every team (fit-set anchored)
    ao = (np.std(yo) / np.std(io_f)) if np.std(io_f) > 1e-9 else 1.0
    ad = (np.std(yd) / np.std(idf_f)) if np.std(idf_f) > 1e-9 else 1.0
    mo, md = float(io_f.mean()), float(idf_f.mean())
    resid = {t: ((mo + ao * (io[t] - mo)) - sp[t][1]) - ((md + ad * (idf[t] - md)) - sp[t][2])
             for t in teams}

    # demeaning pools (pseudo-pools; Pac-12 2024+ -> MWC; debut excluded from pools)
    def poolkey(t):
        if (min(2025, y), t) in OVR['p4'] or (2020, t) in OVR['p4']:
            pass
        c = confs.get(t, '?')
        if c == 'FBS Independents':
            return 'IND_P4' if OVR['p4'].get((y, t), is_p4(c, y)) else 'IND_G5'
        if c == 'Pac-12' and y >= 2024:
            return 'Mountain West'
        return c
    p4c = {t: OVR['p4'].get((y, t), is_p4(confs.get(t, '?'), y)) for t in teams}
    pool_members = defaultdict(list)
    for t in teams:
        if (y, t) not in DEBUT:
            pool_members[poolkey(t)].append(resid[t])
    p4_mean = float(np.mean([resid[t] for t in teams if p4c[t] and (y, t) not in DEBUT]))
    g5_mean = float(np.mean([resid[t] for t in teams if not p4c[t] and (y, t) not in DEBUT]))
    pool_mean = {k: float(np.mean(v)) for k, v in pool_members.items()}
    pool_mean['IND_P4'], pool_mean['IND_G5'] = p4_mean, g5_mean
    resid = {t: resid[t] - pool_mean[poolkey(t)] for t in teams}

    # level-strip (before clip), fit on non-debut
    keep = [t for t in teams if (y, t) not in DEBUT]
    rv = np.array([resid[t] for t in keep]); lv = np.array([sp[t][0] for t in keep])
    cq, _, _ = ols([lv], rv)
    resid = {t: resid[t] - (cq[0] + cq[1] * sp[t][0]) for t in teams}

    for t in keep:
        r_pre = resid[t]
        st = (stp.get(t, 50.0) - 50.0) / 50.0
        panel.append(dict(year=y, team=t, sp_pre=sp[t][0], miss=fin[t] - sp[t][0],
                          R_pre=r_pre, R_adj=float(np.clip(0.35 * r_pre, -6, 6)) + st,
                          p4=int(p4c[t]), incomplete=int(t not in complete)))
    print(f'  {y}: {len(keep)} panel teams | conv weights off ' +
          ' '.join(f'{u}{b:+.3f}' for u, b in zip(OFFU, bo[1:])) + ' | def ' +
          ' '.join(f'{u}{b:+.3f}' for u, b in zip(DEFU, bd[1:])))

with open(f'{R}/data/research/s8b_panel.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(panel[0].keys())); w.writeheader(); w.writerows(panel)

Y = np.array([r['miss'] for r in panel]); SP = np.array([r['sp_pre'] for r in panel])
RP = np.array([r['R_pre'] for r in panel]); RA = np.array([r['R_adj'] for r in panel])
YR = np.array([r['year'] for r in panel]); P4 = np.array([r['p4'] for r in panel], bool)
print(f'\npanel n={len(panel)} | SD(R_pre)={RP.std():.2f} SD(R_adj)={RA.std():.2f} pts')

print('\n===== PRIMARY: miss ~ sp_pre + R_pre =====')
b, t, _ = ols([SP, RP], Y)
print(f'c = {b[2]:+.3f} pts drift per pt (t {t[2]:+.2f})')
folds = []
for y in YEARS:
    m = YR != y
    bb, tt, _ = ols([SP[m], RP[m]], Y[m])
    folds.append(bb[2]); print(f'  LOYO drop {y}: c={bb[2]:+.3f} t={tt[2]:+.2f}')
sign_ok = all((f > 0) == (b[2] > 0) for f in folds)
PASS = t[2] >= 2 and sign_ok
lam = min(max(b[2], 0.0), 1.0) if PASS else 0.0
print(f'bars: t>=2 {"PASS" if t[2]>=2 else "FAIL"} | LOYO 4/4 {"PASS" if sign_ok else "FAIL"} '
      f'| PRIMARY {"PASS" if PASS else "FAIL"} | lambda* = {lam:.2f}')

print('\n===== SECONDARY (registered): G5-only =====')
bg, tg, _ = ols([SP[~P4], RP[~P4]], Y[~P4])
fg = []
for y in YEARS:
    m = (YR != y) & ~P4
    bb, tt, _ = ols([SP[m], RP[m]], Y[m]); fg.append(bb[2])
g_sign = all((f > 0) == (bg[2] > 0) for f in fg)
GPASS = tg[2] >= 2 and g_sign
lg = min(max(bg[2], 0.0), 1.0) if GPASS else 0.0
print(f'n={int((~P4).sum())} c={bg[2]:+.3f} (t {tg[2]:+.2f}) LOYO {"4/4" if g_sign else "unstable"} '
      f'-> {"PASS" if GPASS else "FAIL"} | lambda*_G5 = {lg:.2f}')

print('\n===== COMPANION: beta on R_adj (measurement) =====')
ba, ta, _ = ols([SP, RA], Y)
se = abs(ba[2] / ta[2])
print(f'beta_adj = {ba[2]:+.3f} (t {ta[2]:+.2f}, 95% CI [{ba[2]-1.96*se:+.3f}, {ba[2]+1.96*se:+.3f}])')

print('\n===== REPORT-ONLY =====')
bp, tp, _ = ols([SP[P4], RP[P4]], Y[P4])
print(f'P4: n={int(P4.sum())} c={bp[2]:+.3f} t={tp[2]:+.2f}')
aR = np.abs(RP)
for lab, lo, hi in (('small', 0, np.quantile(aR, 1/3)), ('mid', np.quantile(aR, 1/3), np.quantile(aR, 2/3)),
                    ('large', np.quantile(aR, 2/3), 1e9)):
    m = (aR >= lo) & (aR < hi)
    bb, tt, _ = ols([SP[m], RP[m]], Y[m])
    print(f'|R| {lab}: n={int(m.sum())} c={bb[2]:+.3f} t={tt[2]:+.2f}')
hc_by = {}
for y in [2021] + YEARS:
    for c in json.load(open(f'{R}/data/cfbd/2026-07-12/coaches_{y}.json')):
        for s in c.get('seasons', []):
            if s.get('year') == y:
                hc_by[(y, norm(s['school']))] = c.get('firstName', '') + c.get('lastName', '')
NH = np.array([hc_by.get((r['year'] - 1, r['team'])) not in (None, hc_by.get((r['year'], r['team'])))
               for r in panel])
for lab, m in (('newHC', NH), ('retHC', ~NH)):
    bb, tt, _ = ols([SP[m], RP[m]], Y[m])
    print(f'{lab}: n={int(m.sum())} c={bb[2]:+.3f} t={tt[2]:+.2f}')
print('per-year:')
for y in YEARS:
    m = YR == y
    bb, tt, _ = ols([SP[m], RP[m]], Y[m])
    print(f'  {y}: c={bb[2]:+.3f} t={tt[2]:+.2f}')
infl = np.argsort(-aR)[:5]
mask = np.ones(len(panel), bool); mask[infl] = False
bb, tt, _ = ols([SP[mask], RP[mask]], Y[mask])
print(f'jackknife top-5 |R_pre| ({", ".join(panel[i]["team"]+str(panel[i]["year"]) for i in infl)}): '
      f'c={bb[2]:+.3f} t={tt[2]:+.2f}')
print('2023 forensics — top |R_pre| with misses:')
sub = sorted([r for r in panel if r['year'] == 2023], key=lambda r: -abs(r['R_pre']))[:8]
for r in sub:
    print(f"  {r['team']:20s} R_pre={r['R_pre']:+.1f} miss={r['miss']:+.1f}")
