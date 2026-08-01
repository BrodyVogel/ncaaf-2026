#!/usr/bin/env python3
"""S16: continuous origin/destination strength in transfer grading.
Per PREREGISTRATION_S16_2026-08-01.md."""
import csv, os, re, unicodedata
import json
from collections import defaultdict
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}
POSGRP = {'QB': 'QB', 'HB': 'skill', 'FB': 'skill', 'WR': 'skill', 'TE': 'skill',
          'T': 'trench', 'G': 'trench', 'C': 'trench', 'ED': 'trench', 'DI': 'trench',
          'LB': 'back7', 'CB': 'back7', 'S': 'back7'}


def load_year(y):
    """Fixed file list (canonical unit file first; ties keep first-seen).
    Volume gate operationalized as player_game_count >= 6 (~150+ snaps),
    uniform across files — disclosed in findings."""
    if y < 2025:
        base = f'data/pff_history/{y}'
        files = [f'defense_summary_{y}.csv', f'offense_blocking_{y}.csv',
                 f'passing_summary_{y}.csv', f'receiving_summary_{y}.csv',
                 f'rushing_summary_{y}.csv']
    else:
        base = 'data/pff'
        files = ['PFF_defense_summary.csv', 'PFF_offense_blocking.csv',
                 'PFF_passing_summary.csv', 'PFF_receiving_summary.csv',
                 'PFF_rushing_summary.csv']
    out = {}
    for fn in files:
        p = os.path.join(base, fn)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p)):
            nm = norm(r.get('player') or '')
            g = r.get('grades_defense') if 'defense' in fn else r.get('grades_offense')
            gc = r.get('player_game_count') or 0
            try:
                g = float(g); gc = float(gc)
            except (TypeError, ValueError):
                continue
            tm = norm(r.get('team_name') or '')
            pos = (r.get('position') or '').upper()
            if nm and (nm not in out or gc > out[nm][2]):
                out[nm] = (tm, g, gc, pos)
    return out


# team maps: SP+ final (origin year) and preseason (dest year); class by year
def rdmap(path, col):
    return {AL.get(r['norm_key'], r['norm_key']): float(r[col]) for r in csv.DictReader(open(path))}


P4C = ('SEC', 'Big Ten', 'Big 12', 'ACC')
conf_by = {}
for y in range(2021, 2026):
    for r in json.load(open(f'data/cfbd/2026-07-12/records_{y}.json')):
        if r.get('classification') == 'fbs':
            conf_by[(y, norm(r['team']))] = r.get('conference')


def is_p4(y, t):
    return int(conf_by.get((y, t)) in P4C or t == 'notredame')


# team-name aliases between PFF team_name and SP+ norm keys
PFF_AL = {'olemiss': 'mississippi', 'ncstate': 'northcarolinastate', 'usc': 'southerncalifornia',
          'smu': 'southernmethodist', 'tcu': 'texaschristian', 'ucf': 'centralflorida',
          'utsa': 'texassanantonio', 'utep': 'texaselpaso', 'byu': 'brighamyoung',
          'lsu': 'louisianastate', 'unlv': 'nevadalasvegas', 'fiu': 'floridainternational',
          'fau': 'floridaatlantic', 'usf': 'southflorida', 'miamifl': 'miami',
          'miamioh': 'miamiohio', 'uab': 'alabamabirmingham', 'umass': 'massachusetts',
          'appstate': 'appalachianstate', 'ulmonroe': 'louisianamonroe', 'ull': 'louisiana',
          'hawaii': 'hawaii', 'sanjosest': 'sanjosestate', 'sandiegost': 'sandiegostate'}


def team_key(t):
    return PFF_AL.get(t, t)


rows = []
for y in (2021, 2022, 2023, 2024):
    fin = rdmap(f'data/backtest/sp_final/SP+_{y}_final.csv', 'final_overall')
    pre = rdmap(f'data/backtest/sp_preseason/SP+_{y+1}_preseason.csv', 'sp_plus_overall')
    a, b = load_year(y), load_year(y + 1)
    for nm, (tm, g, sn, pos) in a.items():
        if sn < 6 or nm not in b:
            continue
        tm2, g2, sn2, pos2 = b[nm]
        if sn2 < 6 or tm2 == tm:
            continue
        ko, kd = team_key(tm), team_key(tm2)
        if ko not in fin or kd not in pre:
            continue
        p4o, p4d = is_p4(y, ko), is_p4(y + 1, kd)
        rows.append(dict(y=y, nm=nm, gp=g, gn=g2, dsp=fin[ko] - pre[kd],
                         up=int(not p4o and p4d), down=int(p4o and not p4d),
                         same=int(p4o == p4d), p4o=p4o,
                         grp=POSGRP.get(pos, 'other'), wsn=min(sn, sn2)))
print(f'panel n={len(rows)}  (up {sum(r["up"] for r in rows)}, down {sum(r["down"] for r in rows)}, same {sum(r["same"] for r in rows)})')


def ols(X, y, w=None):
    M = np.column_stack([np.ones(len(y))] + X)
    if w is None:
        w = np.ones(len(y))
    sw = np.sqrt(w)
    b, *_ = np.linalg.lstsq(M * sw[:, None], y * sw, rcond=None)
    r = (y - M @ b) * sw
    dof = len(y) - M.shape[1]
    cov = (r @ r / dof) * np.linalg.pinv((M * sw[:, None]).T @ (M * sw[:, None]))
    r2 = 1 - (r @ r) / (((y - np.average(y, weights=w)) * sw) @ ((y - np.average(y, weights=w)) * sw))
    return b, b / np.sqrt(np.diag(cov)), r2


GN = np.array([r['gn'] for r in rows]); GP = np.array([r['gp'] for r in rows])
UP = np.array([r['up'] for r in rows], float); DN = np.array([r['down'] for r in rows], float)
DS = np.array([r['dsp'] for r in rows]); YR = np.array([r['y'] for r in rows])
SM = np.array([r['same'] for r in rows], bool); WS = np.array([r['wsn'] for r in rows])

print('\n===== S16-L1: binary vs +continuous =====')
b0, t0, r20 = ols([GP, UP, DN], GN)
print(f'binary:  prev {b0[1]:+.3f} | up {b0[2]:+.2f} (t {t0[2]:+.2f}) | down {b0[3]:+.2f} (t {t0[3]:+.2f})  R2 {r20:.4f}')
b1, t1, r21 = ols([GP, UP, DN, DS], GN)
print(f'+DSP:    prev {b1[1]:+.3f} | up {b1[2]:+.2f} | down {b1[3]:+.2f} | DSP {b1[4]:+.4f} (t {t1[4]:+.2f})  R2 {r21:.4f}  dR2 {r21-r20:.4f}')
signs = []
for yy in (2021, 2022, 2023, 2024):
    m = YR != yy
    bb, tt, _ = ols([GP[m], UP[m], DN[m], DS[m]], GN[m])
    signs.append(np.sign(bb[4]) == np.sign(b1[4]))
    print(f'  LOYO drop {yy}: DSP {bb[4]:+.4f} (t {tt[4]:+.2f})')
passL1 = abs(t1[4]) >= 2 and (r21 - r20) >= 0.01 and sum(signs) >= 3
print(f'S16-L1: {"PASS" if passL1 else "FAIL"}')
bw, tw, _ = ols([GP, UP, DN, DS], GN, w=WS)
print(f'robustness snap-weighted: DSP {bw[4]:+.4f} (t {tw[4]:+.2f})')

print('\n===== S16-L2: SAME-CLASS movers (currently zero-adjusted) =====')
b2, t2, _ = ols([GP[SM], DS[SM]], GN[SM])
print(f'same-class (n={int(SM.sum())}): prev {b2[1]:+.3f} | DSP {b2[2]:+.4f} (t {t2[2]:+.2f})')
signs2 = []
for yy in (2021, 2022, 2023, 2024):
    m = SM & (YR != yy)
    bb, tt, _ = ols([GP[m], DS[m]], GN[m])
    signs2.append(np.sign(bb[2]) == np.sign(b2[2]))
    print(f'  LOYO drop {yy}: DSP {bb[2]:+.4f} (t {tt[2]:+.2f})')
passL2 = abs(t2[2]) >= 2 and sum(signs2) >= 3
print(f'S16-L2: {"PASS" if passL2 else "FAIL"}')
for lab, msk in (('P4->P4', SM & (np.array([r['p4o'] for r in rows]) == 1)),
                 ('G5->G5', SM & (np.array([r['p4o'] for r in rows]) == 0))):
    bb, tt, _ = ols([GP[msk], DS[msk]], GN[msk])
    print(f'  {lab} (n={int(msk.sum())}): DSP {bb[2]:+.4f} (t {tt[2]:+.2f})')

print('\n===== S16-L3: position groups (report) =====')
for grp in ('QB', 'skill', 'trench', 'back7'):
    msk = np.array([r['grp'] == grp for r in rows])
    if msk.sum() < 40:
        print(f'  {grp:6s} n={int(msk.sum())} (thin)')
        continue
    bb, tt, _ = ols([GP[msk], UP[msk], DN[msk], DS[msk]], GN[msk])
    print(f'  {grp:6s} (n={int(msk.sum())}): DSP {bb[4]:+.4f} (t {tt[4]:+.2f}) | up {bb[2]:+.2f} | down {bb[3]:+.2f}')
