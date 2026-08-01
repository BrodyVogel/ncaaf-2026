#!/usr/bin/env python3
"""B2: anchor v2 upgrade pass. Per REGISTRATION_B2_ANCHOR_V2_2026-08-01.md.
Portal-era tune folds (2021-24, wk2+). Greedy sequential items N1..N6.
RUN_2025=1 -> final re-run on (lightly reused) 2025 with adopted config."""
import csv, json, os, re, sys, unicodedata
from collections import defaultdict
from statistics import median
import numpy as np

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RUN_2025 = os.environ.get('RUN_2025') == '1'


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


AL = {'connecticut': 'uconn'}
TUNE = [2021, 2022, 2023, 2024]
YEARS = TUNE + ([2025] if RUN_2025 else [])

panel = defaultdict(list)
for r in csv.DictReader(open('data/research/insession_panel_2016_2025.csv')):
    y = int(r['year'])
    if y in YEARS and r['fcs_opp'] == '0':
        panel[y].append(r)
# mapping fits (N1/N5) use 2021-24 rows incl. from panel directly
MAP_OLD = (17.97, 0.950)


def fit_map(rows):
    X = [float(r['off_ppa']) * float(r['off_plays']) for r in rows if r['off_ppa'] and r['off_plays']]
    Y = [float(r['points']) for r in rows if r['off_ppa'] and r['off_plays']]
    b = np.polyfit(X, Y, 1)
    return (b[1], b[0])


MAP_ERA = fit_map([r for y in TUNE for r in panel[y]])
G5C = ('American Athletic', 'Conference USA', 'Mid-American', 'Mountain West', 'Sun Belt', 'AAC', 'CUSA', 'MAC', 'MWC', 'SBC')


def g5set(y):
    s = set()
    fn = f'data/cfbd/2026-07-12/records_{y}.json'
    if os.path.exists(fn):
        for r in json.load(open(fn)):
            if r.get('classification') == 'fbs' and any(c in (r.get('conference') or '') for c in G5C):
                s.add(AL.get(norm(r['team']), norm(r['team'])))
    return s


G5 = {y: g5set(y) for y in YEARS}
MAP_P4 = fit_map([r for y in TUNE for r in panel[y] if r['team'] not in G5[y]])
MAP_G5 = fit_map([r for y in TUNE for r in panel[y] if r['team'] in G5[y]])
print(f'mappings: era {MAP_ERA[0]:.2f}+{MAP_ERA[1]:.3f}x | P4 {MAP_P4[0]:.2f}+{MAP_P4[1]:.3f}x | G5 {MAP_G5[0]:.2f}+{MAP_G5[1]:.3f}x')


def qb_flags(rows):
    seen, flags = defaultdict(list), {}
    for r in sorted(rows, key=lambda x: int(x['week'])):
        t, st = r['team'], r['qb_starter']
        prior = seen[t]
        flags[(int(r['week']), t)] = int(bool(st) and bool(prior)
                                         and st != max(set(prior), key=prior.count))
        if st:
            seen[t].append(st)
    return flags


def season_games(y, mapping='old'):
    rows = {(r['game_id'], r['team']): r for r in panel[y]}

    def conv(r):
        if not r['off_ppa'] or not r['off_plays']:
            return None
        tp = float(r['off_ppa']) * float(r['off_plays'])
        if mapping == 'old':
            a, b = MAP_OLD
        elif mapping == 'era':
            a, b = MAP_ERA
        else:
            a, b = MAP_G5 if r['team'] in G5[y] else MAP_P4
        return a + b * tp
    out = []
    for (gid, t), r in rows.items():
        if r['home'] != '1' and r['neutral'] != '1':
            continue
        opp = rows.get((gid, r['opp']))
        if opp is None or (r['home'] != '1' and norm(opp['team']) < norm(t)):
            continue
        out.append(dict(w=int(r['week']), i=t, j=r['opp'], gid=gid,
                        site=0.0 if r['neutral'] == '1' else 1.0,
                        margin=float(r['margin']), effi=conv(r), effj=conv(opp)))
    return sorted(out, key=lambda g: g['w'])


def sp_prior(y):
    off, dfn = {}, {}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv')):
        k = AL.get(r['norm_key'], r['norm_key'])
        off[k], dfn[k] = float(r['sp_plus_off']), float(r['sp_plus_def'])
    mo, md = np.mean(list(off.values())), np.mean(list(dfn.values()))
    return {t: (off[t] - mo, md - dfn[t]) for t in off}


def market_data(y):
    gp = (f'data/cfbd/insession/games_{y}_regular.json'
          if os.path.exists(f'data/cfbd/insession/games_{y}_regular.json')
          else f'data/cfbd/2026-07-12/games_{y}_regular.json')
    neutral = {g['id']: bool(g.get('neutralSite')) for g in json.load(open(gp))}
    by_week, lines = defaultdict(list), {}
    for g in json.load(open(f'data/cfbd/lines/lines_{y}.json')):
        if g.get('homeClassification') != 'fbs' or g.get('awayClassification') != 'fbs':
            continue
        h, a = AL.get(norm(g['homeTeam']), norm(g['homeTeam'])), AL.get(norm(g['awayTeam']), norm(g['awayTeam']))
        cl = [l['spread'] for l in g.get('lines') or [] if l.get('spread') is not None and abs(l['spread']) <= 60]
        if cl:
            lines[g['id']] = median(cl)
            by_week[g['week']].append((h, a, median(cl), 0.0 if neutral.get(g['id']) else 1.0))
    return by_week, lines


def market_chain(y, prior, hfa):
    by_week, _ = market_data(y)
    teams = sorted(prior)
    idx = {t: i for i, t in enumerate(teams)}
    R = np.array([prior[t][0] + prior[t][1] for t in teams])
    out = {}
    for w in range(1, 16):
        gs = [g for g in by_week.get(w, []) if g[0] in idx and g[1] in idx]
        if gs:
            A = np.zeros((len(gs) + len(teams), len(teams)))
            b = np.zeros(len(gs) + len(teams))
            for k, (h, a, spr, site) in enumerate(gs):
                A[k, idx[h]], A[k, idx[a]] = 1, -1
                b[k] = -spr - hfa * site
            for i in range(len(teams)):
                A[len(gs) + i, i] = np.sqrt(0.5)
                b[len(gs) + i] = np.sqrt(0.5) * R[i]
            R, *_ = np.linalg.lstsq(A, b, rcond=None)
            R += -np.mean(R)
        out[w] = {t: R[idx[t]] for t in teams}
    return out


def run_season(games, prior, cfg, mkt=None):
    teams = sorted(prior)
    idx = {t: k for k, t in enumerate(teams)}
    N = len(teams)
    NH = N if cfg.get('sig_h') else 0          # per-team HFA states (N3)
    dim = 2 * N + NH
    x0 = np.zeros(dim)
    for t in teams:
        x0[idx[t]], x0[N + idx[t]] = prior[t]
    x = x0.copy()
    al, be = cfg.get('alpha', 1.0), cfg.get('beta', 1.0)
    preds, hist = [], []
    for w in range(1, 16):
        wk = [g for g in games if g['w'] == w and g['i'] in idx and g['j'] in idx]
        for g in wk:
            hloc = cfg['hfa'] + (x[2 * N + idx[g['i']]] if NH else 0.0)
            m = al * (x[idx[g['i']]] - x[idx[g['j']]]) + be * (x[N + idx[g['i']]] - x[N + idx[g['j']]]) \
                + hloc * g['site']
            preds.append((w, m, g['margin'], g['i'], g['j'], g['gid']))
        hist.extend(wk)
        rows, rhs, wts = [], [], []
        for g in hist:
            aw = cfg['rho'] ** (w - g['w'])
            ii, jj = idx[g['i']], idx[g['j']]
            if g['effi'] is not None:
                r1 = np.zeros(dim); r1[ii], r1[N + jj] = 1, -1
                rows.append(r1); rhs.append(g['effi']); wts.append(aw / cfg['sig_eff'] ** 2)
            if g['effj'] is not None:
                r2 = np.zeros(dim); r2[jj], r2[N + ii] = 1, -1
                rows.append(r2); rhs.append(g['effj']); wts.append(aw / cfg['sig_eff'] ** 2)
            r3 = np.zeros(dim)
            r3[ii], r3[N + ii], r3[jj], r3[N + jj] = 1, 1, -1, -1
            if NH:
                r3[2 * N + ii] = g['site']
            rows.append(r3); rhs.append(g['margin'] - cfg['hfa'] * g['site'])
            wts.append(aw / (cfg['sig_m'] * cfg['sig_eff']) ** 2)
        if mkt is not None and w - 1 >= 1:
            sm = cfg.get('sig_mkt_early', cfg['sig_mkt']) if w <= 5 else cfg['sig_mkt']
            for t, rv in mkt.get(w - 1, {}).items():
                if t in idx:
                    r4 = np.zeros(dim); r4[idx[t]], r4[N + idx[t]] = 1, 1
                    rows.append(r4); rhs.append(rv); wts.append(1 / sm ** 2)
        for t in teams:
            for od in (0, N):
                rp = np.zeros(dim); rp[idx[t] + od] = 1
                rows.append(rp); rhs.append(x0[idx[t] + od]); wts.append(1 / cfg['sig_prior'] ** 2)
            if NH:
                rh = np.zeros(dim); rh[2 * N + idx[t]] = 1
                rows.append(rh); rhs.append(0.0); wts.append(1 / cfg['sig_h'] ** 2)
        A = np.array(rows); b = np.array(rhs); sw = np.sqrt(np.array(wts))
        x, *_ = np.linalg.lstsq(A * sw[:, None], b * sw, rcond=None)
        x[:N] -= x[:N].mean(); x[N:2 * N] -= x[N:2 * N].mean()
    return preds


def mae(preds, wmin, wmax=15):
    e = [abs(p[1] - p[2]) for p in preds if wmin <= p[0] <= wmax]
    return (np.mean(e), len(e)) if e else (float('nan'), 0)


PRIORS = {y: sp_prior(y) for y in YEARS}
LINES = {y: market_data(y)[1] for y in YEARS}


def evaluate(cfg, years=TUNE):
    per, preds_by = {}, {}
    for y in years:
        gs = season_games(y, cfg.get('mapping', 'old'))
        mk = market_chain(y, PRIORS[y], cfg['hfa']) if cfg.get('sig_mkt') else None
        p = run_season(gs, PRIORS[y], cfg, mkt=mk)
        per[y] = mae(p, 2)[0]
        preds_by[y] = p
    return np.mean([per[y] for y in years]), per, preds_by


def profile(preds_by, years=TUNE):
    """model vs frozen vs market MAE by week bucket."""
    out = {}
    for lo, hi in ((2, 4), (5, 8), (9, 15)):
        me, mm = [], []
        for y in years:
            for (w, m, act, i, j, gid) in preds_by[y]:
                if not (lo <= w <= hi):
                    continue
                ln = LINES[y].get(int(gid) if str(gid).isdigit() else gid)
                if ln is None:
                    continue
                me.append(abs(m - act)); mm.append(abs(-ln - act))
        out[(lo, hi)] = (np.mean(me), np.mean(mm), len(me))
    return out


V1 = json.load(open('data/research/insession_v1_constants.json'))
V1.setdefault('mapping', 'old')

if RUN_2025:
    CFG = json.load(open('data/research/insession_v2_constants.json'))
    _, per, pb = evaluate(CFG, years=[2025])
    print(f'2025 v2 re-run (lightly reused holdout): MAE wk2+ {per[2025]:.3f}')
    pr = profile(pb, years=[2025])
    for k, (a, b, n) in pr.items():
        print(f'  wk{k[0]}-{k[1]}: model {a:.3f} vs market {b:.3f} (gap {a-b:+.3f}, n={n})')
    sys.exit(0)

print('\n===== N0: frozen v1 on portal folds + week profile =====')
v0, per0, pb0 = evaluate(V1)
print(f'v1 pooled (2021-24, wk2+): {v0:.3f} | folds: ' + ' '.join(f'{y}:{per0[y]:.3f}' for y in TUNE))
prof = profile(pb0)
for k, (a, b, n) in prof.items():
    print(f'  wk{k[0]}-{k[1]}: model {a:.3f} vs market {b:.3f} (gap {a-b:+.3f}, n={n})')
gap_early = prof[(2, 4)][0] - prof[(2, 4)][1]
gap_late = prof[(9, 15)][0] - prof[(9, 15)][1]
print(f'early gap {gap_early:+.3f} vs late gap {gap_late:+.3f} -> '
      f'{"EARLY-SEASON WEAKNESS flag" if gap_early > 2 * max(gap_late, 0.0) else "no early-weakness flag"}')

CUR, curv = dict(V1), v0


def try_item(name, deltas):
    global CUR, curv
    best_d, best_v, best_per = None, curv, None
    for d in deltas:
        v, per, _ = evaluate(dict(CUR, **d))
        folds = sum(1 for y in TUNE if per[y] < per0[y] - 1e-9) if CUR == V1 else None
        # folds-better computed vs the RUNNING config:
        _, cper, _ = evaluate(CUR) if False else (None, None, None)
        print(f'  {name} {d}: {v:.3f}')
        if v < best_v:
            best_d, best_v = d, v
    if best_d is not None and curv - best_v >= 0.02:
        _, per_new, _ = evaluate(dict(CUR, **best_d))
        _, per_cur, _ = evaluate(CUR)
        fb = sum(1 for y in TUNE if per_new[y] < per_cur[y])
        if fb >= 3:
            CUR = dict(CUR, **best_d); curv = best_v
            print(f'  -> ADOPT {best_d} (pooled {best_v:.3f}, folds {fb}/4)')
            return
        print(f'  -> improvement {curv - best_v:.3f} but folds {fb}/4 — NOT adopted')
    else:
        print(f'  -> no adoption (best {best_v:.3f} vs {curv:.3f})')


print('\n===== N1 era mapping =====')
try_item('N1', [dict(mapping='era')])
print('\n===== N2 portal-era core selection =====')
try_item('N2', [dict(sig_prior=sp, rho=r, sig_m=sm)
                for sp in (3.0, 4.0, 5.5) for r in (1.0, 0.95, 0.90) for sm in (1.0, 1.5, 2.0)
                if not (sp == CUR['sig_prior'] and r == CUR['rho'] and sm == CUR['sig_m'])][:26])
print('\n===== N3 per-team HFA =====')
try_item('N3', [dict(sig_h=0.5), dict(sig_h=1.0)])
print('\n===== N4 off/def asymmetric prediction =====')
try_item('N4', [dict(alpha=1.1, beta=0.9), dict(alpha=1.2, beta=0.8)])
print('\n===== N5 level-specific mapping =====')
try_item('N5', [dict(mapping='level')])
print('\n===== N6 early-season market tether =====')
try_item('N6', [dict(sig_mkt_early=2.0), dict(sig_mkt_early=3.0)])

print(f'\nFINAL: {CUR} | pooled {curv:.3f} (v1 was {v0:.3f})')
_, perF, pbF = evaluate(CUR)
profF = profile(pbF)
print('final week profile:')
for k, (a, b, n) in profF.items():
    print(f'  wk{k[0]}-{k[1]}: model {a:.3f} vs market {b:.3f} (gap {a-b:+.3f}, n={n})')
if CUR != V1:
    json.dump(CUR, open('data/research/insession_v2_constants.json', 'w'), indent=1)
    print('v2 constants written')
else:
    print('v1 stands; no v2 constants file')
