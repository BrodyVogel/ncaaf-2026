#!/usr/bin/env python3
"""S9 situational-bias audit (diagnostic; no bars).

Part A (2026): do OUR deviations from consensus (applied roster adjustment) and our
HELD STAKES cluster on common situations? Flags: new HC, QB-battle (dossier QB conf L),
new QB1 (top prior-vol QB gone), high tape-turnover, thin tape, 2025 luck, G5.
Part B (2022-25): does CONSENSUS misprice those situations (miss ~ sp + flag), and is
the mechanical arm's signal situation-dependent (miss ~ sp + R + flag + R*flag)?
Luck at consensus level was S6-F1 (FAIL); RP was S6-F2 (+, t 2.34) — replicated here
with this panel's construction for completeness.
"""
import csv, json, math, os, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8_shadow_arm import (load_spine, norm, pnorm, R, conf_map, TapeIndex,
                           membership_roster, membership_portal)

YEARS = [2022, 2023, 2024, 2025]
SP_ALIAS = {'connecticut': 'uconn'}


def ols(X, y):
    A = np.column_stack([np.ones(len(y))] + X)
    b, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ b
    cov = (r @ r / (len(y) - A.shape[1])) * np.linalg.pinv(A.T @ A)
    return b, b / np.sqrt(np.diag(cov))


def luck(season):
    """team -> wins minus sum(postgame win expectancy), FBS games with the field."""
    w, e = defaultdict(float), defaultdict(float)
    for part in ('regular', 'postseason'):
        p = f'{R}/data/cfbd/2026-07-12/games_{season}_{part}.json'
        if not os.path.exists(p):
            continue
        for g in json.load(open(p)):
            hp = g.get('homePostgameWinProbability')
            if hp is None or g.get('homePoints') is None:
                continue
            h, a = norm(g['homeTeam']), norm(g['awayTeam'])
            hw = int(g['homePoints'] > g['awayPoints'])
            w[h] += hw; e[h] += hp
            w[a] += 1 - hw; e[a] += 1 - hp
    return {t: w[t] - e[t] for t in w}


def rp_pct(season):
    """team -> returning production percentPPA (CFBD)."""
    out = {}
    for r in json.load(open(f'{R}/data/cfbd/2026-07-12/returning_{season}.json')):
        keys = [k for k in r if 'percent' in k.lower()]
        val = r.get('percentPPA', r.get(keys[0]) if keys else None)
        if val is not None:
            out[norm(r['team'])] = float(val)
    return out


def tape_flags(year, spine, mode):
    """(team -> retention share of y-1 team volume, evidence vol, new_qb1 flag)."""
    confs = conf_map(year)
    members = membership_roster(year, confs) if mode == 'roster' else membership_portal(year, confs, spine)
    tape = TapeIndex(spine, year)
    prev_vol = defaultdict(float)
    top_qb = {}
    for r in spine.get(year - 1, []):
        prev_vol[r['team']] += r['vol']
        if r['grp'] == 'QB':
            if r['team'] not in top_qb or r['vol'] > top_qb[r['team']][1]:
                top_qb[r['team']] = (pnorm(r['name']), r['vol'])
    out = {}
    for tk, plist in members.items():
        names = {nm for nm, _ in plist}
        ret_vol = ev = 0.0
        for nm in names:
            row, evol, fy = tape.find(nm, tk)
            if row is None:
                continue
            ev += evol
            if row['team'] == tk and row['season'] == year - 1:
                ret_vol += row['vol']
            del fy
        share = ret_vol / prev_vol[tk] if prev_vol.get(tk) else float('nan')
        nq = int(tk in top_qb and top_qb[tk][0] not in names)
        out[tk] = (share, ev, nq)
    return out


spine = load_spine()

# ================= PART B: historical =================
panel = list(csv.DictReader(open(f'{R}/data/research/s8b_panel.csv')))
for r in panel:
    for k in ('sp_pre', 'miss', 'R_pre'):
        r[k] = float(r[k])
    r['year'] = int(r['year'])
hc_by = {}
for y in [2021] + YEARS:
    for c in json.load(open(f'{R}/data/cfbd/2026-07-12/coaches_{y}.json')):
        for s in c.get('seasons', []):
            if s.get('year') == y:
                hc_by[(y, norm(s['school']))] = c.get('firstName', '') + c.get('lastName', '')
flags_hist = {}
for y in YEARS:
    lk = luck(y - 1)
    rp = rp_pct(y)
    tf = tape_flags(y, spine, 'roster')
    for r in [x for x in panel if x['year'] == y]:
        t = r['team']
        share, ev, nq = tf.get(t, (float('nan'), 0.0, 0))
        flags_hist[(y, t)] = dict(
            newhc=int(hc_by.get((y - 1, t)) not in (None, hc_by.get((y, t)))),
            rp=rp.get(t, float('nan')),
            luck=lk.get(t, float('nan')),
            newqb=nq, ret_share=share, ev=ev)

Y = np.array([r['miss'] for r in panel])
SP = np.array([r['sp_pre'] for r in panel])
RP_ = np.array([r['R_pre'] for r in panel])
YR = np.array([r['year'] for r in panel])


def col(key):
    return np.array([flags_hist[(r['year'], r['team'])][key] for r in panel], float)


ev_all = col('ev')
ev_z = np.full(len(panel), np.nan)
for y in YEARS:  # thin-tape = within-year bottom quintile of evidence volume
    m = YR == y
    ev_z[m] = ev_all[m] < np.quantile(ev_all[m], 0.2)
FLAGS = {
    'new HC': col('newhc'),
    'new QB1 (top-vol QB gone)': col('newqb'),
    'high turnover (ret share, cont.)': col('ret_share'),
    'returning %PPA (cont.)': col('rp'),
    'lucky prior yr (wins-exp, cont.)': col('luck'),
    'thin tape (bottom-quintile ev)': ev_z,
}
print('===== PART B: does CONSENSUS misprice the situation? (miss ~ sp + flag) =====')
print(f'{"flag":34s} {"n":>4s} {"coef":>7s} {"t":>6s}')
for lab, F in FLAGS.items():
    m = ~np.isnan(F)
    b, t = ols([SP[m], F[m]], Y[m])
    print(f'{lab:34s} {int(m.sum()):4d} {b[2]:+7.3f} {t[2]:+6.2f}')

print('\n===== PART B2: is the ARM signal situation-dependent? (.. + R + flag + R*flag) =====')
print(f'{"flag":34s} {"c(R) base":>9s} {"R*flag":>8s} {"t":>6s}')
for lab, F in FLAGS.items():
    m = ~np.isnan(F)
    Fz = (F[m] - np.nanmean(F[m])) / (np.nanstd(F[m]) + 1e-12)
    b, t = ols([SP[m], RP_[m], Fz, RP_[m] * Fz], Y[m])
    print(f'{lab:34s} {b[2]:+9.3f} {b[4]:+8.3f} {t[4]:+6.2f}')

# ================= PART A: 2026 =================
print('\n===== PART A: 2026 board — do OUR deviations cluster on situations? =====')
asm = {norm(r['team']): r for r in csv.DictReader(open(f'{R}/outputs/final_pass/ASSEMBLY.csv'))}
adj = {t: float(r['k_x_resid_clipped']) + float(r['st_term']) for t, r in asm.items()}
qbconf = {}
import glob
for p in glob.glob(f'{R}/snapshots/*/grades.json'):
    g = json.load(open(p))
    mt = json.load(open(p.replace('grades.json', 'META.json')))
    qbconf[norm(mt['team'])] = (g['units'].get('QB', {}).get('confidence', '?'),
                                sum(1 for u in g['units'].values() if u.get('confidence') == 'L'))
lk25 = luck(2025)
tf26 = tape_flags(2026, spine, 'portal')
teams26 = [t for t in adj if t in qbconf]
A = np.array([adj[t] for t in teams26])
F26 = {
    'new HC': np.array([1.0 if asm[t]['new_HC'] == 'Y' else 0.0 for t in teams26]),
    'QB conf L (battle proxy)': np.array([1.0 if qbconf[t][0] == 'L' else 0.0 for t in teams26]),
    'new QB1': np.array([float(tf26.get(t, (0, 0, 0))[2]) for t in teams26]),
    'ret share (cont.)': np.array([tf26.get(t, (np.nan, 0, 0))[0] for t in teams26]),
    'lucky 2025 (cont.)': np.array([lk25.get(t, np.nan) for t in teams26]),
    'thin tape (L_count>=2)': np.array([1.0 if qbconf[t][1] >= 2 else 0.0 for t in teams26]),
    'G5': np.array([0.0 if asm[t]['conference'] in ('SEC', 'Big Ten', 'Big 12', 'ACC')
                    or t == 'notredame' else 1.0 for t in teams26]),
}
print(f'{"flag":26s} {"corr(adj,flag)":>14s}   flagged-mean adj | rest')
for lab, F in F26.items():
    m = ~np.isnan(F)
    c = float(np.corrcoef(A[m], F[m])[0, 1])
    if set(np.unique(F[m])) <= {0.0, 1.0}:
        fm = A[m][F[m] == 1].mean() if (F[m] == 1).any() else float('nan')
        rm = A[m][F[m] == 0].mean()
        print(f'{lab:26s} {c:+14.3f}   {fm:+.2f} ({int((F[m]==1).sum())}) | {rm:+.2f}')
    else:
        print(f'{lab:26s} {c:+14.3f}   (continuous)')

# held-book exposure
BOOK = [('uconn', 'over', 1.07), ('tulsa', 'over', 1.10), ('oregonstate', 'over', 0.65),
        ('bowlinggreen', 'over', 1.05), ('liberty', 'under', 0.60), ('arizonastate', 'under', 0.95),
        ('kennesawstate', 'over', 0.55), ('illinois', 'under', 0.65), ('westvirginia', 'under', 0.50),
        ('eastcarolina', 'over', 0.55), ('hawaii', 'under', 0.60), ('florida', 'under', 0.90),
        ('ucf', 'over', 0.55), ('pittsburgh', 'under', 0.65), ('wisconsin', 'under', 0.60),
        ('buffalo', 'over', 0.75), ('nevada', 'over', 0.75), ('wakeforest', 'over', 0.90),
        ('rutgers', 'over', 0.80)]
gross = sum(s for _, _, s in BOOK)
print(f'\n===== held-book situational exposure (gross {gross:.2f}u) =====')
print(f'{"flag":26s} {"gross u":>8s} {"net-directional u":>18s}')
for lab, F in F26.items():
    if not set(np.unique(F[~np.isnan(F)])) <= {0.0, 1.0}:
        continue
    fl = {t: F26[lab][i] for i, t in enumerate(teams26)}
    gr = sum(s for t, sd, s in BOOK if fl.get(t) == 1.0)
    net = sum(s * (1 if sd == 'over' else -1) for t, sd, s in BOOK if fl.get(t) == 1.0)
    print(f'{lab:26s} {gr:8.2f} {net:+18.2f}')
lowret = {t for i, t in enumerate(teams26)
          if not np.isnan(F26['ret share (cont.)'][i]) and F26['ret share (cont.)'][i] <
          np.nanquantile(F26['ret share (cont.)'], 1 / 3)}
gr = sum(s for t, sd, s in BOOK if t in lowret)
net = sum(s * (1 if sd == 'over' else -1) for t, sd, s in BOOK if t in lowret)
print(f'{"high turnover (bottom-1/3 ret)":26s} {gr:8.2f} {net:+18.2f}')
lucky = {t for i, t in enumerate(teams26)
         if not np.isnan(F26['lucky 2025 (cont.)'][i]) and F26['lucky 2025 (cont.)'][i] > 1.0}
gr = sum(s for t, sd, s in BOOK if t in lucky)
net = sum(s * (1 if sd == 'over' else -1) for t, sd, s in BOOK if t in lucky)
print(f'{"lucky 2025 (>+1 win)":26s} {gr:8.2f} {net:+18.2f}')
print('\nper-position flags:')
for t, sd, s in BOOK:
    i = teams26.index(t)
    tags = [lab for lab, F in F26.items()
            if set(np.unique(F[~np.isnan(F)])) <= {0.0, 1.0} and F[i] == 1.0]
    rs = F26['ret share (cont.)'][i]
    lk = F26['lucky 2025 (cont.)'][i]
    if not np.isnan(rs) and t in lowret:
        tags.append(f'high-turnover({rs:.0%})')
    if not np.isnan(lk) and lk > 1.0:
        tags.append(f'lucky25({lk:+.1f})')
    print(f'  {t:15s} {sd:5s} {s:.2f}u  adj={adj[t]:+.2f}  {", ".join(tags) if tags else "-"}')
