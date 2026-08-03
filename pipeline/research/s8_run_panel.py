#!/usr/bin/env python3
"""S8 Phase 3: run all registered legs on the 2022-25 shadow-arm panel.
Everything per PREREGISTRATION_S8_2026-07-27.md. Prints the full report and writes
data/research/s8_panel.csv (team-season rows) for reproducibility.
"""
import csv, json, math, os, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8_shadow_arm import (build_shadow, percentiles, team_scores, load_spine,
                           norm, GRPS, UW, R, POSMEAN, K, WCAP, JUMP_G5P4,
                           JUMP_P4G5, FRB, is_p4, conf_map, TapeIndex,
                           membership_roster, recruits_for, NSLOT1, NSLOT2)

from team_alias import to_nk

YEARS = [2022, 2023, 2024, 2025]
# JOIN FIX 2026-08-03 (owner-approved): all cross-source names route through
# team_alias.to_nk(). The old bare-norm joins (a) dropped Miami-FL/App State/
# UL Monroe rows and (b) priced 61 real-FBS games at the 0.95 FCS constant
# inside exp_wins (see s7s8_rejoin_2026-08-03.py for the before/after).


def read_sp(path, valcol):
    out = {}
    with open(path) as f:
        for r in csv.DictReader(f):
            out[r['norm_key']] = float(r[valcol])
    return out


def nkify(d):
    """Re-key a shadow-space dict to canonical norm_key (identity for FCS/unknown)."""
    return {to_nk(k) or k: v for k, v in d.items()}


def ols(X, y):
    """X list of columns (without intercept). Returns b, t, r2, resid."""
    A = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ b
    dof = len(y) - A.shape[1]
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.pinv(A.T @ A)
    t = b / np.sqrt(np.diag(cov))
    r2 = 1 - (resid @ resid) / ((y - y.mean()) @ (y - y.mean()))
    return b, t, r2, resid


def zvec(d):
    v = np.array(list(d.values()), float)
    mu, sd = v.mean(), v.std()
    return {k: (x - mu) / sd for k, x in d.items()}, sd


# ---------------------------------------------------------------- panel build
spine = load_spine()
panel = []          # rows: year, team, sp_pre, sp_final, miss, D, D_t, D_r, D_pts, units...
proj_raw = {}       # (year, team, unit) -> raw-scale projection (Leg 2b, no offsets)
for y in YEARS:
    units, diag = build_shadow(y, 'roster', spine)
    pcts = percentiles(units)
    scores = team_scores(units, pcts)
    # trench / rest sub-scores
    sub = defaultdict(dict)
    for (tk, u) in units:
        sub[tk][u] = pcts[(tk, u)]
    tr, rs = {}, {}
    for tk, uu in sub.items():
        tw = [(UW[u], uu.get(u, 50.0)) for u in ('OL', 'DL')]
        rw = [(UW[u], uu.get(u, 50.0)) for u in ('QB', 'RB', 'WRTE', 'LB', 'DB')]
        tr[tk] = sum(w * v for w, v in tw) / sum(w for w, _ in tw)
        rs[tk] = sum(w * v for w, v in rw) / sum(w for w, _ in rw)
    scores, tr, rs = nkify(scores), nkify(tr), nkify(rs)
    sp_pre = read_sp(f'{R}/data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')
    sp_fin = read_sp(f'{R}/data/backtest/sp_final/SP+_{y}_final.csv', 'final_overall')
    common = [t for t in scores if t in sp_pre and t in sp_fin]
    spz, sp_sd = zvec({t: sp_pre[t] for t in common})
    scz, _ = zvec({t: scores[t]['score'] for t in common})
    trz, _ = zvec({t: tr[t] for t in common})
    rsz, _ = zvec({t: rs[t] for t in common})
    confs = conf_map(y)
    confs_nk = nkify(confs)          # canonical view for panel rows (proj_raw below
    for t in common:                 # stays in shadow space and keeps `confs`)
        D = scz[t] - spz[t]
        panel.append(dict(year=y, team=t, sp_pre=sp_pre[t], sp_final=sp_fin[t],
                          miss=sp_fin[t] - sp_pre[t], D=D, D_pts=D * sp_sd,
                          D_t=trz[t] - spz[t], D_r=rsz[t] - spz[t],
                          p4=int(is_p4(confs_nk.get(t, '?'), y)),
                          n_units=scores[t]['n_units']))
    # raw projections for Leg 2b (no offsets, no percentile — grade scale)
    tape = TapeIndex(spine, y)
    members = membership_roster(y, confs)
    recs = recruits_for(y)
    for tk, plist in members.items():
        pool = defaultdict(list)
        used = set()
        for nm, _cl in plist:
            if nm in used:
                continue
            row, ev, fy = tape.find(nm, tk)
            if row is None:
                continue
            used.add(nm)
            u = row['grp']; pm = POSMEAN[u]
            w = min(ev / (ev + K[u]), WCAP.get(u, 1.0))
            jump = 0.0
            if row['team'] != tk:
                pf, pt = bool(row['p4']), is_p4(confs.get(tk, '?'), y)
                jump = JUMP_G5P4 if (not pf and pt) else (JUMP_P4G5 if (pf and not pt) else 0.0)
            pool[u].append((ev, pm + w * (row['grade'] - pm) + jump))
        for u in GRPS:
            rows = sorted(pool.get(u, []), reverse=True)
            vals = [(v, 1.0 if i < NSLOT1[u] else 0.33)
                    for i, (ev, v) in enumerate(rows[:NSLOT1[u] + NSLOT2[u]])]
            nf = max(0, NSLOT1[u] + NSLOT2[u] - len(vals))
            for comp in recs.get((tk, u), [])[:nf]:
                b0, sl = FRB[u]
                vals.append((b0 + sl * (comp - 0.861), 0.33))
            if vals:
                proj_raw[(y, tk, u)] = sum(v * w for v, w in vals) / sum(w for _, w in vals)
    print(f'  built {y}: {len(common)} panel teams ({diag["matched"]} tape players)')

with open(f'{R}/data/research/s8_panel.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(panel[0].keys()))
    w.writeheader(); w.writerows(panel)
print(f'panel n = {len(panel)}')

Y = np.array([r['miss'] for r in panel])
SP = np.array([r['sp_pre'] for r in panel])
D = np.array([r['D'] for r in panel])
DP = np.array([r['D_pts'] for r in panel])
DT = np.array([r['D_t'] for r in panel])
DR = np.array([r['D_r'] for r in panel])
YR = np.array([r['year'] for r in panel])

# ---------------------------------------------------------------- Leg 1
print('\n===== LEG 1: main effect =====')
b0, t0, r20, _ = ols([SP], Y)
b1, t1, r21, _ = ols([SP, D], Y)
print(f'baseline:  miss ~ {b0[0]:+.2f} {b0[1]:+.3f}*sp   R2={r20:.4f}')
print(f'with arm:  miss ~ {b1[0]:+.2f} {b1[1]:+.3f}*sp {b1[2]:+.3f}*D   t(D)={t1[2]:+.2f}  R2={r21:.4f}')
dR2 = r21 - r20
print(f'L1-A c>0 & t>=2: c={b1[2]:+.3f}, t={t1[2]:+.2f} -> {"PASS" if b1[2] > 0 and t1[2] >= 2 else "FAIL"}')
folds = []
for y in YEARS:
    m = YR != y
    bb, tt, _, _ = ols([SP[m], D[m]], Y[m])
    folds.append((y, bb[2], tt[2]))
    print(f'  LOYO drop {y}: c={bb[2]:+.3f} t={tt[2]:+.2f}')
sign_ok = all((f[1] > 0) == (b1[2] > 0) for f in folds)
print(f'L1-B sign-stable 4/4: {"PASS" if sign_ok else "FAIL"}')
print(f'L1-C dR2={dR2:.4f} >= 0.02: {"PASS" if dR2 >= 0.02 else "FAIL"}')
L1 = b1[2] > 0 and t1[2] >= 2 and sign_ok and dR2 >= 0.02

# ---------------------------------------------------------------- Leg 2a
print('\n===== LEG 2a: trench premium =====')
b2, t2, r22, _ = ols([SP, DT, DR], Y)
print(f'c_t={b2[2]:+.3f} (t {t2[2]:+.2f})  c_r={b2[3]:+.3f} (t {t2[3]:+.2f})')
print(f'claim bar t(c_t)>=2 AND c_t>c_r: {"PASS" if t2[2] >= 2 and b2[2] > b2[3] else "FAIL"}')

# ---------------------------------------------------------------- Leg 2b
print('\n===== LEG 2b: coachability persistence =====')
realized = defaultdict(lambda: defaultdict(float))
volsum = defaultdict(lambda: defaultdict(float))
for y in YEARS:
    for r in spine.get(y, []):
        kk = (y, r['team'], r['grp'])
        realized[kk[0]][(kk[1], kk[2])] += r['grade'] * r['vol']
        volsum[kk[0]][(kk[1], kk[2])] += r['vol']
resid = {}
for (y, tk, u), pv in proj_raw.items():
    vv = volsum[y].get((tk, u), 0.0)
    if vv > 0:
        resid[(y, tk, u)] = realized[y][(tk, u)] / vv - pv
print('unit  n_pairs  persist_r     t   | mean|resid|')
per_unit = {}
for u in GRPS:
    a, b = [], []
    for y in YEARS[:-1]:
        for tk in {k[1] for k in resid if k[0] == y and k[2] == u}:
            if (y, tk, u) in resid and (y + 1, tk, u) in resid:
                a.append(resid[(y, tk, u)]); b.append(resid[(y + 1, tk, u)])
    a, b = np.array(a), np.array(b)
    rr = float(np.corrcoef(a, b)[0, 1])
    tt = rr * math.sqrt((len(a) - 2) / (1 - rr * rr))
    per_unit[u] = (len(a), rr, tt)
    print(f'{u:5s} {len(a):6d}   {rr:+.3f}  {tt:+6.2f} | {np.mean(np.abs(np.concatenate([a,b]))):.2f}')
ol_n, ol_r, ol_t = per_unit['OL']
print(f'focal OL bar r>=0.20 & t>=2: r={ol_r:+.3f} t={ol_t:+.2f} -> {"PASS" if ol_r >= 0.20 and ol_t >= 2 else "FAIL"}')

# ---------------------------------------------------------------- Leg 3
print('\n===== LEG 3: money leg (SBD 2022-24, soft bars) =====')
Dmap = {(r['year'], r['team']): r['D_pts'] for r in panel}
sp_pre_by = {}
for y in YEARS:
    sp_pre_by[y] = read_sp(f'{R}/data/backtest/sp_preseason/SP+_{y}_preseason.csv', 'sp_plus_overall')


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _gkeys(g):
    """Canonical keys for a game row; non-FBS names prefixed so they can never
    collide with a canonical norm_key."""
    return (to_nk(g['homeTeam']) or '~' + norm(g['homeTeam']),
            to_nk(g['awayTeam']) or '~' + norm(g['awayTeam']))


def exp_wins(team_nk, y, ratings, bump=0.0):
    ew = 0.0
    for g in json.load(open(f'{R}/data/cfbd/2026-07-12/games_{y}_regular.json')):
        h, a = _gkeys(g)
        if team_nk not in (h, a):
            continue
        opp = a if team_nk == h else h
        if opp not in ratings:
            ew += 0.95      # true non-FBS opponent (join fix: FBS always resolves)
            continue
        site = 0.0 if g.get('neutralSite') else (1.0 if team_nk == h else -1.0)
        mu = (ratings[team_nk] + bump) - ratings[opp] + 2.3 * site
        ew += phi(mu / 13.5)
    return ew


def actual_wins(team_nk, y):
    wn = 0
    for g in json.load(open(f'{R}/data/cfbd/2026-07-12/games_{y}_regular.json')):
        h, a = _gkeys(g)
        if team_nk not in (h, a) or g.get('homePoints') is None:
            continue
        mine = g['homePoints'] if team_nk == h else g['awayPoints']
        theirs = g['awayPoints'] if team_nk == h else g['homePoints']
        wn += int(mine > theirs)
    return wn


rows3 = []
for y in (2022, 2023, 2024):
    for r in csv.DictReader(open(f'{R}/data/win_totals/sbd_historical/sbd_{y}.csv')):
        tk = to_nk(r['team'])
        if tk is None:
            print(f'  [join guard] unresolved SBD team {y}: {r["team"]!r}')
            continue
        if (y, tk) not in Dmap or tk not in sp_pre_by[y]:
            continue
        line = float(r['line'])
        ew0 = exp_wins(tk, y, sp_pre_by[y])
        rows3.append(dict(year=y, team=tk, line=line, ew0=ew0,
                          ew_half=exp_wins(tk, y, sp_pre_by[y], 0.5 * Dmap[(y, tk)]),
                          ew_full=exp_wins(tk, y, sp_pre_by[y], 1.0 * Dmap[(y, tk)]),
                          wins=actual_wins(tk, y)))
W = np.array([r['wins'] for r in rows3], float)
L = np.array([r['line'] for r in rows3], float)
for lab, col in (('consensus      ', 'ew0'), ('arm lambda=0.5 ', 'ew_half'), ('arm lambda=1.0 ', 'ew_full')):
    E = np.array([r[col] for r in rows3])
    mae = np.mean(np.abs(E - W))
    big = np.abs(E - L) >= 1.0
    side = ((E > L) & (W > L)) | ((E < L) & (W < L))
    push = W == L
    nb = int(big.sum())
    wr = side[big & ~push].mean() if (big & ~push).any() else float('nan')
    print(f'{lab} MAE={mae:.3f} | |d|>=1: n={nb}, side wins {100*wr:.1f}%')
mae0 = np.mean(np.abs(np.array([r['ew0'] for r in rows3]) - W))
mae1 = np.mean(np.abs(np.array([r['ew_full'] for r in rows3]) - W))
print(f'soft bar (i) MAE improves at lambda=1: {"PASS" if mae1 < mae0 else "FAIL"} ({mae0:.3f} -> {mae1:.3f})')
flips = won = 0
for r in rows3:
    s0 = np.sign(r['ew0'] - r['line']); s1 = np.sign(r['ew_full'] - r['line'])
    if s0 != s1 and abs(r['ew_full'] - r['line']) >= 1.0 and r['wins'] != r['line']:
        flips += 1
        won += int((s1 > 0) == (r['wins'] > r['line']))
print(f'soft bar (ii) flipped sides at |d|>=1: {won}/{flips} = '
      f'{(100*won/flips if flips else float("nan")):.0f}% -> {"PASS" if flips and won/flips >= 0.5 else ("n/a" if not flips else "FAIL")}')

# ---------------------------------------------------------------- Leg 4
print('\n===== LEG 4: scale coefficient =====')
b4, t4, _, _ = ols([SP, DP], Y)
se = abs(b4[2] / t4[2])
print(f'beta = {b4[2]:+.3f} pts drift per pt of disagreement (t {t4[2]:+.2f}, 95% CI '
      f'[{b4[2]-1.96*se:+.3f}, {b4[2]+1.96*se:+.3f}])')
lam = min(max(b4[2], 0.0), 1.0) if L1 else 0.0
print(f'recommended 2027 arm multiplier lambda* = {lam:.2f} (L1 {"passed" if L1 else "failed"})')

# ---------------------------------------------------------------- Leg 6
print('\n===== LEG 6: heterogeneity (report-only) =====')
hc_by = {}          # (year, school_nk) -> coach name, from per-year files
for y in [min(YEARS) - 1] + YEARS:
    for c in json.load(open(f'{R}/data/cfbd/2026-07-12/coaches_{y}.json')):
        for s in c.get('seasons', []):
            if s.get('year') == y:
                hc_by[(y, to_nk(s['school']) or norm(s['school']))] = \
                    c.get('firstName', '') + c.get('lastName', '')
newhc = {(y, t) for (y, t) in hc_by if y in YEARS
         and hc_by.get((y - 1, t)) not in (None, hc_by[(y, t)])}
for lab, m in (('P4 ', np.array([r['p4'] == 1 for r in panel])),
               ('G5 ', np.array([r['p4'] == 0 for r in panel])),
               ('newHC', np.array([(r['year'], r['team']) in newhc for r in panel])),
               ('retHC', np.array([(r['year'], r['team']) not in newhc for r in panel]))):
    bb, tt, _, _ = ols([SP[m], D[m]], Y[m])
    print(f'  {lab:6s} n={int(m.sum()):3d} c={bb[2]:+.3f} t={tt[2]:+.2f}')
absD = np.abs(D)
for lab, lo, hi in (('small |D|', 0, np.quantile(absD, 1 / 3)),
                    ('mid   |D|', np.quantile(absD, 1 / 3), np.quantile(absD, 2 / 3)),
                    ('large |D|', np.quantile(absD, 2 / 3), 1e9)):
    m = (absD >= lo) & (absD < hi)
    bb, tt, _, _ = ols([SP[m], D[m]], Y[m])
    print(f'  {lab} n={int(m.sum()):3d} c={bb[2]:+.3f} t={tt[2]:+.2f}')
print('  per-year (single-year fits, diagnostic):')
for y in YEARS:
    m = YR == y
    bb, tt, _, _ = ols([SP[m], D[m]], Y[m])
    print(f'    {y}: n={int(m.sum())} c={bb[2]:+.3f} t={tt[2]:+.2f}')
print('  G5-only per-year:')
G5m = np.array([r['p4'] == 0 for r in panel])
for y in YEARS:
    m = (YR == y) & G5m
    bb, tt, _, _ = ols([SP[m], D[m]], Y[m])
    print(f'    {y}: n={int(m.sum())} c={bb[2]:+.3f} t={tt[2]:+.2f}')
infl = np.argsort(-absD)[:5]
mask = np.ones(len(panel), bool); mask[infl] = False
bb, tt, _, _ = ols([SP[mask], D[mask]], Y[mask])
print(f'  influence check (drop top-5 |D|): c={bb[2]:+.3f} t={tt[2]:+.2f} '
      f'(dropped: {", ".join(panel[i]["team"] + str(panel[i]["year"]) for i in infl)})')
