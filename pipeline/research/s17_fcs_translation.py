#!/usr/bin/env python3
"""S17: FCS->FBS grade translation. Per PREREGISTRATION_S17_2026-08-02.md."""
import csv, glob, json, os, re, unicodedata
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


def load_fcs(y):
    out = {}
    for fn in sorted(glob.glob(f'data/pff_history/fcs/*_{y}.csv')):
        if 'special_teams' in fn:
            continue
        for r in csv.DictReader(open(fn)):
            nm = norm(r.get('player') or '')
            g = r.get('grades_defense') if 'defense' in fn else r.get('grades_offense')
            try:
                g = float(g); gc = float(r.get('player_game_count') or 0)
            except (TypeError, ValueError):
                continue
            tm = norm(r.get('team_name') or '')
            pos = (r.get('position') or '').upper()
            if nm and (nm not in out or gc > out[nm][1]):
                out[nm] = (g, gc, pos, tm)
    return out


def load_fbs(y):
    if y < 2025:
        base = f'data/pff_history/{y}'
        files = [f'defense_summary_{y}.csv', f'offense_blocking_{y}.csv', f'passing_summary_{y}.csv',
                 f'receiving_summary_{y}.csv', f'rushing_summary_{y}.csv']
    else:
        base = 'data/pff'
        files = ['PFF_defense_summary.csv', 'PFF_offense_blocking.csv', 'PFF_passing_summary.csv',
                 'PFF_receiving_summary.csv', 'PFF_rushing_summary.csv']
    out = {}
    for fn in files:
        p = os.path.join(base, fn)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p)):
            nm = norm(r.get('player') or '')
            g = r.get('grades_defense') if 'defense' in fn else r.get('grades_offense')
            try:
                g = float(g); gc = float(r.get('player_game_count') or 0)
            except (TypeError, ValueError):
                continue
            tm = norm(r.get('team_name') or '')
            if nm and (nm not in out or gc > out[nm][1]):
                out[nm] = (g, gc, tm)
    return out


def team_means(fcs):
    """game-count-weighted mean grade per FCS team-year, min 20 graded players."""
    agg = defaultdict(lambda: [0.0, 0.0, 0])
    for nm, (g, gc, pos, tm) in fcs.items():
        a = agg[tm]
        a[0] += g * gc; a[1] += gc; a[2] += 1
    return {tm: v[0] / v[1] for tm, v in agg.items() if v[2] >= 20 and v[1] > 0}


def sp_pre(y):
    return {AL.get(r['norm_key'], r['norm_key']): float(r['sp_plus_overall'])
            for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv'))}


rows = []
for y in (2021, 2022, 2023, 2024):
    fcs = load_fcs(y)
    tmeans = team_means(fcs)
    ymean = float(np.mean(list(tmeans.values())))
    fbs_next, fbs_this = load_fbs(y + 1), load_fbs(y)
    pre = sp_pre(y + 1)
    for nm, (g, gc, pos, tm) in fcs.items():
        if gc < 6 or nm in fbs_this or nm not in fbs_next:
            continue
        g2, gc2, tm2 = fbs_next[nm]
        if gc2 < 6 or tm not in tmeans:
            continue
        dsp = pre.get(tm2)
        rows.append(dict(y=y, nm=nm, gp=g, gn=g2, grp=POSGRP.get(pos, 'other'),
                         orig=tmeans[tm] - ymean, dest=(dsp if dsp is not None else np.nan),
                         w=min(gc, gc2)))
print(f'S17 panel n={len(rows)}  by year: ' + str({y: sum(1 for r in rows if r["y"] == y) for y in (2021, 2022, 2023, 2024)}))


def ols(X, y):
    M = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(M, y, rcond=None)
    r = y - M @ b
    cov = (r @ r / (len(y) - M.shape[1])) * np.linalg.pinv(M.T @ M)
    r2 = 1 - (r @ r) / ((y - y.mean()) @ (y - y.mean()))
    return b, b / np.sqrt(np.diag(cov)), r2


GN = np.array([r['gn'] for r in rows]); GP = np.array([r['gp'] for r in rows])
OR = np.array([r['orig'] for r in rows]); YR = np.array([r['y'] for r in rows])
DE = np.array([r['dest'] for r in rows])
GD = {g: np.array([float(r['grp'] == g) for r in rows]) for g in ('skill', 'trench', 'back7')}
dums = [GD['skill'], GD['trench'], GD['back7']]

print('\n===== S17-L1 baseline: grade_FBS ~ grade_FCS + posgroup =====')
b1, t1, r21 = ols([GP] + dums, GN)
print(f'slope {b1[1]:+.3f} (t {t1[1]:+.2f}) | intercept {b1[0]:+.1f} | R2 {r21:.4f}')
print(f'level drop at FCS grade 70: {70 - (b1[0] + b1[1]*70):+.1f} pts (QB/other ref group)')
print(f'L1 claim (slope>0, t>=2): {"PASS" if b1[1] > 0 and t1[1] >= 2 else "FAIL"}')

print('\n===== S17-L2 CO-PRIMARY: + origin team tape-mean =====')
b2, t2, r22 = ols([GP] + dums + [OR], GN)
print(f'origin {b2[5]:+.3f} (t {t2[5]:+.2f}) | dR2 {r22-r21:.4f} | FCS slope now {b2[1]:+.3f}')
signs = []
for yy in (2021, 2022, 2023, 2024):
    m = YR != yy
    bb, tt, _ = ols([GP[m]] + [d[m] for d in dums] + [OR[m]], GN[m])
    signs.append(np.sign(bb[5]) == np.sign(b2[5]))
    print(f'  LOYO drop {yy}: origin {bb[5]:+.3f} (t {tt[5]:+.2f})')
passL2 = abs(t2[5]) >= 2 and (r22 - r21) >= 0.01 and sum(signs) >= 3
print(f'S17-L2: {"PASS" if passL2 else "FAIL"}')
p90, p10 = np.percentile(OR, 90), np.percentile(OR, 10)
print(f'NDSU-vs-MVSU spread: same FCS grade at 90th vs 10th pctl program -> {b2[5]*(p90-p10):+.1f} FBS grade pts')

print('\n===== S17-L3: + destination SP+ =====')
m3 = ~np.isnan(DE)
b3, t3, r23 = ols([GP[m3]] + [d[m3] for d in dums] + [OR[m3], DE[m3]], GN[m3])
print(f'(n={int(m3.sum())}) origin {b3[5]:+.3f} (t {t3[5]:+.2f}) | dest {b3[6]:+.4f} (t {t3[6]:+.2f})')
signs3 = []
for yy in (2021, 2022, 2023, 2024):
    m = m3 & (YR != yy)
    bb, tt, _ = ols([GP[m]] + [d[m] for d in dums] + [OR[m], DE[m]], GN[m])
    signs3.append(np.sign(bb[6]) == np.sign(b3[6]))
print(f'S17-L3 dest claim: {"PASS" if abs(t3[6]) >= 2 and sum(signs3) >= 3 else "FAIL"} (LOYO {sum(signs3)}/4)')

print('\n===== S17-L4 position groups (report) =====')
for g in ('QB', 'skill', 'trench', 'back7'):
    msk = np.array([r['grp'] == g for r in rows])
    if msk.sum() < 40:
        print(f'  {g:6s} n={int(msk.sum())} (thin)')
        continue
    bb, tt, _ = ols([GP[msk], OR[msk]], GN[msk])
    print(f'  {g:6s} (n={int(msk.sum())}): FCS slope {bb[1]:+.3f} (t {tt[1]:+.2f}) | origin {bb[2]:+.3f} (t {tt[2]:+.2f})')

# ===== S17-L5: 2026 projections for matched entrants =====
if b1[1] > 0 and t1[1] >= 2:
    print('\n===== S17-L5: 2026 projections (Phase B case-read queue) =====')
    fcs25 = load_fcs(2025)
    tm25 = team_means(fcs25)
    ym25 = float(np.mean(list(tm25.values())))
    fold_betas = []
    for yy in (2021, 2022, 2023, 2024):
        m = YR != yy
        bb, _, _ = ols([GP[m]] + [d[m] for d in dums] + [OR[m]], GN[m])
        fold_betas.append(bb)
    PAT = re.compile(r'FCS', re.I)
    out = []
    for p in sorted(glob.glob('snapshots/*/roster_two_deep.csv')):
        t = p.split('/')[1]
        for r in csv.DictReader(open(p)):
            blob = ' '.join(str(r.get(k) or '') for k in ('origin', 'note', 'notes', 'source_1'))
            if not r.get('player') or not PAT.search(blob):
                continue
            nk = norm(r['player'])
            if nk not in fcs25 or fcs25[nk][1] < 4:
                continue
            g, gc, pos, tm = fcs25[nk]
            orig = (tm25.get(tm, ym25) - ym25)
            grp = POSGRP.get(pos, 'other')
            dvec = [float(grp == 'skill'), float(grp == 'trench'), float(grp == 'back7')]
            preds = [bb[0] + bb[1] * g + bb[2] * dvec[0] + bb[3] * dvec[1] + bb[4] * dvec[2] + bb[5] * orig
                     for bb in fold_betas]
            slot = str(r.get('slot') or r.get('depth') or '').strip()
            out.append((t, r['player'], pos, slot, g, int(gc), round(orig, 1),
                        round(float(np.mean(preds)), 1), round(float(np.std(preds)), 1)))
    out.sort(key=lambda x: -x[7])
    with open('data/research/s17_projections_2026.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['team', 'player', 'pos', 'slot', 'fcs_grade', 'fcs_games', 'origin_ctr', 'proj_fbs', 'proj_sd'])
        w.writerows(out)
    print(f'wrote data/research/s17_projections_2026.csv ({len(out)} players)')
    HELD = {'UConn','Tulsa','Oregon_State','Bowling_Green','Liberty','Arizona_State','Kennesaw_State','Illinois','West_Virginia','East_Carolina',"Hawai'i",'Florida','UCF','Pittsburgh','Wisconsin','Buffalo','Nevada','Wake_Forest','Rutgers'}
    print('\ntop-10 projected (starters *):')
    for t, pl, pos, slot, g, gc, orig, proj, sd in out[:10]:
        star = '*' if slot == '1' else ' '
        held = 'HELD' if t in HELD else '    '
        print(f'  {held} {t:16s} {pl:24s} {pos:3s}{star} FCS {g:.1f} (orig {orig:+.1f}) -> {proj:.1f} ±{sd}')
    print('\nbottom-5 projected STARTERS (bracket over-credit risk):')
    st = [o for o in out if o[3] == '1']
    for t, pl, pos, slot, g, gc, orig, proj, sd in st[-5:]:
        held = 'HELD' if t in HELD else '    '
        print(f'  {held} {t:16s} {pl:24s} {pos:3s} FCS {g:.1f} (orig {orig:+.1f}) -> {proj:.1f} ±{sd}')
