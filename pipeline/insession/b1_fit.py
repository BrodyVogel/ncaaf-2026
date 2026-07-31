#!/usr/bin/env python3
"""B1: in-season anchor fitting harness.
Per REGISTRATION_B1_INSEASON_ANCHOR_2026-08-01.md. Stage-wise greedy selection
on tune folds (2016-19 weeks>=5 flat-prior; 2021-24 full; 2020 excluded; 2025
reserved -- only touched when RUN_2025=1 after freeze).

Implementation notes (disclosed in findings): process noise implemented as
exponential age-forgetting rho on observation weights (maps the registered
sigma_proc knob); full re-solve each week IS the re-smoothing; robustness via
IRLS reweighting passes.
"""
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
TUNE_FULL = [2021, 2022, 2023, 2024]
OBS_YEARS = [2016, 2017, 2018, 2019]
ALL_YEARS = OBS_YEARS + TUNE_FULL + ([2025] if RUN_2025 else [])

# ---------- load panel ----------
panel = defaultdict(list)          # year -> rows
for r in csv.DictReader(open('data/research/insession_panel_2016_2025.csv')):
    y = int(r['year'])
    if y == 2020 or y not in ALL_YEARS:
        continue
    if r['fcs_opp'] == '1':
        continue
    panel[y].append(r)

# rolling-modal QB flag (registration: starter != modal of PRIOR games)
def qb_flags(rows):
    seen = defaultdict(list)
    flags = {}
    for r in sorted(rows, key=lambda x: int(x['week'])):
        t, st = r['team'], r['qb_starter']
        prior = seen[t]
        flags[(int(r['week']), t)] = int(bool(st) and bool(prior)
                                         and st != max(set(prior), key=prior.count))
        if st:
            seen[t].append(st)
    return flags

# ---------- PPA->points mapping (fit on 2016-19 only) ----------
X, Yp = [], []
for y in OBS_YEARS:
    for r in panel[y]:
        if r['off_ppa'] and r['points']:
            tp = float(r['off_ppa']) * float(r['off_plays'] or 0)
            X.append(tp); Yp.append(float(r['points']))
b_ppa = np.polyfit(X, Yp, 1)
print(f'PPA->points map (2016-19): points ~ {b_ppa[1]:.2f} + {b_ppa[0]:.3f}*totalPPA  (n={len(X)})')


def eff_pts(r):
    if not r['off_ppa'] or not r['off_plays']:
        return None
    return b_ppa[1] + b_ppa[0] * float(r['off_ppa']) * float(r['off_plays'])


# ---------- per-season game structures ----------
def season_games(y):
    """home-perspective game records with both sides' efficiency."""
    rows = {(r['game_id'], r['team']): r for r in panel[y]}
    fl = qb_flags(panel[y])
    out = []
    for (gid, t), r in rows.items():
        if r['home'] != '1' and r['neutral'] != '1':
            continue
        opp = rows.get((gid, r['opp']))
        if opp is None or (r['home'] != '1' and norm(opp['team']) < norm(t)):
            continue   # neutral: keep lexicographic-first side once
        w = int(r['week'])
        to = int(r['turnovers'] or 0) + int(opp['turnovers'] or 0)
        out.append(dict(
            w=w, i=t, j=r['opp'], gid=gid,
            site=0.0 if r['neutral'] == '1' else 1.0,
            margin=float(r['margin']), effi=eff_pts(r), effj=eff_pts(opp),
            to=to, blow=int(abs(float(r['margin'])) >= 28),
            qbi=fl.get((w, t), 0), qbj=fl.get((w, r['opp']), 0)))
    return sorted(out, key=lambda g: g['w'])


# ---------- priors ----------
def sp_prior(y):
    off, dfn = {}, {}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv')):
        k = AL.get(r['norm_key'], r['norm_key'])
        off[k], dfn[k] = float(r['sp_plus_off']), float(r['sp_plus_def'])
    mo, md = np.mean(list(off.values())), np.mean(list(dfn.values()))
    return {t: (off[t] - mo, md - dfn[t]) for t in off}


# ---------- market-implied chain + per-game open/close (2021+) ----------
def market_data(y):
    neutral = {}
    gp = (f'data/cfbd/insession/games_{y}_regular.json'
          if os.path.exists(f'data/cfbd/insession/games_{y}_regular.json')
          else f'data/cfbd/2026-07-12/games_{y}_regular.json')
    for g in json.load(open(gp)):
        neutral[g['id']] = bool(g.get('neutralSite'))
    by_week, lines_by_gid = defaultdict(list), {}
    for g in json.load(open(f'data/cfbd/lines/lines_{y}.json')):
        if g.get('homeClassification') != 'fbs' or g.get('awayClassification') != 'fbs':
            continue
        h, a = AL.get(norm(g['homeTeam']), norm(g['homeTeam'])), AL.get(norm(g['awayTeam']), norm(g['awayTeam']))
        cl = [l['spread'] for l in g.get('lines') or [] if l.get('spread') is not None and abs(l['spread']) <= 60]
        op = [l['spreadOpen'] for l in g.get('lines') or [] if l.get('spreadOpen') is not None and abs(l['spreadOpen']) <= 60]
        if cl:
            lines_by_gid[g['id']] = (median(op) if op else None, median(cl))
            by_week[g['week']].append((h, a, median(cl), 0.0 if neutral.get(g['id']) else 1.0))
    return by_week, lines_by_gid


def market_chain(y, prior, hfa):
    """weekly market-implied OVERALL ratings; returns week -> {team: rating}."""
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


# ---------- the filter ----------
def run_season(games, prior, cfg, teams=None, mkt=None):
    """walk-forward; returns list of (week, pred_margin, actual, i, j, gid)."""
    if teams is None:
        teams = sorted({g['i'] for g in games} | {g['j'] for g in games})
    idx = {t: k for k, t in enumerate(teams)}
    N = len(teams)
    x0 = np.zeros(2 * N)
    for t in teams:
        if prior and t in prior:
            x0[idx[t]], x0[N + idx[t]] = prior[t]
    x = x0.copy()
    preds, hist = [], []
    for w in range(1, 16):
        wk = [g for g in games if g['w'] == w and g['i'] in idx and g['j'] in idx]
        for g in wk:   # predict BEFORE update
            m = (x[idx[g['i']]] + x[N + idx[g['i']]]) - (x[idx[g['j']]] + x[N + idx[g['j']]]) \
                + cfg['hfa'] * g['site']
            preds.append((w, m, g['margin'], g['i'], g['j'], g['gid']))
        hist.extend(wk)
        # build weighted system over all games to date
        rows, rhs, wts = [], [], []
        for g in hist:
            age = w - g['w']
            aw = cfg['rho'] ** age
            base = cfg['sig_eff'] ** 2
            pen = 1.0
            if cfg.get('to_pen') and g['to'] >= 4:
                pen *= 1.3 ** 2
            if cfg.get('blow_pen') and g['blow']:
                pen *= 1.3 ** 2
            ii, jj = idx[g['i']], idx[g['j']]
            if g['effi'] is not None:      # off_i - def_j = effi - mu
                r1 = np.zeros(2 * N); r1[ii], r1[N + jj] = 1, -1
                q = pen * (1 / cfg['wqb'] if g['qbi'] else 1)
                rows.append(r1); rhs.append(g['effi'] - cfg['mu']); wts.append(aw / (base * q))
            if g['effj'] is not None:
                r2 = np.zeros(2 * N); r2[jj], r2[N + ii] = 1, -1
                q = pen * (1 / cfg['wqb'] if g['qbj'] else 1)
                rows.append(r2); rhs.append(g['effj'] - cfg['mu']); wts.append(aw / (base * q))
            r3 = np.zeros(2 * N)
            r3[ii], r3[N + ii], r3[jj], r3[N + jj] = 1, 1, -1, -1
            q = pen * (1 / cfg['wqb'] if (g['qbi'] or g['qbj']) else 1)
            rows.append(r3); rhs.append(g['margin'] - cfg['hfa'] * g['site'])
            wts.append(aw / ((cfg['sig_m'] * cfg['sig_eff']) ** 2 * q))
        # market measurement (M4)
        if mkt is not None and w - 1 >= 1 and cfg.get('sig_mkt'):
            for t, rv in mkt.get(w - 1, {}).items():
                if t in idx:
                    r4 = np.zeros(2 * N); r4[idx[t]], r4[N + idx[t]] = 1, 1
                    rows.append(r4); rhs.append(rv); wts.append(1 / cfg['sig_mkt'] ** 2)
        # priors
        for t in teams:
            sp = cfg['sig_prior']
            if cfg.get('g5_mult') and prior and t in cfg.get('g5set', ()):
                sp *= cfg['g5_mult']
            for off_def in (0, N):
                rp = np.zeros(2 * N); rp[idx[t] + off_def] = 1
                rows.append(rp); rhs.append(x0[idx[t] + off_def]); wts.append(1 / sp ** 2)
        A = np.array(rows); b = np.array(rhs); W = np.array(wts)
        for it in range(cfg.get('irls', 1)):
            sw = np.sqrt(W)
            sol, *_ = np.linalg.lstsq(A * sw[:, None], b * sw, rcond=None)
            if cfg.get('robust') == 'none' or it == cfg.get('irls', 1) - 1:
                break
            res = (b - A @ sol) * np.sqrt(W)
            if cfg['robust'] == 'clip':
                W = W * np.minimum(1.0, cfg['clip_c'] / np.maximum(np.abs(res), 1e-9)) ** 2
            elif cfg['robust'] == 't':
                W = W * (cfg['nu'] + 1) / (cfg['nu'] + res ** 2)
        x = sol
        x[:N] -= x[:N].mean(); x[N:] -= x[N:].mean()
    return preds


def mae(preds, wmin, wmax=15):
    e = [abs(p[1] - p[2]) for p in preds if wmin <= p[0] <= wmax]
    return (np.mean(e), len(e)) if e else (float('nan'), 0)


# ---------- evaluation drivers ----------
G5C = ('AAC', 'American Athletic', 'Conference USA', 'CUSA', 'MAC',
       'Mid-American', 'MWC', 'Mountain West', 'SBC', 'Sun Belt')


def g5set(y):
    s = set()
    for yy, fn in ((y, f'data/cfbd/2026-07-12/records_{y}.json'),):
        if os.path.exists(fn):
            for r in json.load(open(fn)):
                if r.get('classification') == 'fbs' and any(c in (r.get('conference') or '') for c in G5C):
                    s.add(AL.get(norm(r['team']), norm(r['team'])))
    return s


SEASONS = {}
for y in ALL_YEARS:
    SEASONS[y] = season_games(y)
PRIORS = {y: sp_prior(y) for y in TUNE_FULL + ([2025] if RUN_2025 else [])}


def evaluate(cfg, use_mkt=False, years_full=TUNE_FULL, quiet=True):
    per_fold = {}
    for y in OBS_YEARS:
        p = run_season(SEASONS[y], None, dict(cfg, sig_prior=12.0))
        per_fold[y] = mae(p, 5)
    for y in years_full:
        mk = market_chain(y, PRIORS[y], cfg['hfa']) if use_mkt else None
        c = dict(cfg)
        if cfg.get('g5_mult'):
            c['g5set'] = g5set(y)
        p = run_season(SEASONS[y], PRIORS[y], c,
                       teams=sorted(PRIORS[y]), mkt=mk)
        per_fold[y] = mae(p, 2)
        per_fold[(y, 'wk3')] = mae(p, 3)
        per_fold[(y, 'preds')] = p
    pooled = np.mean([per_fold[y][0] for y in OBS_YEARS + list(years_full)])
    return pooled, per_fold


if RUN_2025:
    # -------- headline fold: single run on reserved 2025 with FROZEN constants --------
    FINAL = json.load(open('data/research/insession_v1_constants.json'))
    USE_MKT = 'sig_mkt' in FINAL
    y = 2025
    mk = market_chain(y, PRIORS[y], FINAL['hfa']) if USE_MKT else None
    p = run_season(SEASONS[y], PRIORS[y], dict(FINAL), teams=sorted(PRIORS[y]), mkt=mk)
    m_all, n_all = mae(p, 2)
    m_w3, _ = mae(p, 3)
    frozen = dict(FINAL, rho=1.0, sig_eff=1e6, sig_m=1e6, robust='none', irls=1)
    frozen.pop('sig_mkt', None)
    pfz = run_season(SEASONS[y], PRIORS[y], frozen, teams=sorted(PRIORS[y]))
    fz_w3, _ = mae(pfz, 3)
    print(f'2025 HEADLINE: MAE wk2+ {m_all:.3f} (n={n_all}) | wk3+ {m_w3:.3f} vs frozen {fz_w3:.3f} '
          f'-> {"beats frozen" if m_w3 < fz_w3 else "DOES NOT beat frozen"}')
    _, lines_by_gid = market_data(y)
    fl = qb_flags(panel[y])
    rows = []
    for (w, m, act, i, j, gid) in p:
        ln = lines_by_gid.get(int(gid) if str(gid).isdigit() else gid)
        if not ln or ln[0] is None:
            continue
        if abs(ln[0] - ln[1]) >= 2.5 or fl.get((w, i)) or fl.get((w, j)):
            continue
        rows.append((w, m, -ln[1], act))
    for lo, hi in ((2, 4), (5, 8), (9, 15)):
        sub = [(m - mk_) for w, m, mk_, _ in rows if lo <= w <= hi]
        if sub:
            print(f'  wk{lo}-{hi}: RMSE vs close {np.sqrt(np.mean(np.square(sub))):.2f} (n={len(sub)})')
    mae_model = np.mean([abs(m - a) for _, m, _, a in rows])
    mae_mkt = np.mean([abs(mk_ - a) for _, _, mk_, a in rows])
    print(f'  clean-segment margin MAE: model {mae_model:.3f} vs market close {mae_mkt:.3f}')
    sys.exit(0)

# ================= M1 =================
print('\n===== M1 baseline grid =====')
best, bestv = None, 1e9
for sig_prior in (4.0, 5.5, 7.0):
    for rho in (1.0, 0.95, 0.90):
        for sig_m in (1.0, 1.5, 2.0):
            cfg = dict(sig_prior=sig_prior, rho=rho, sig_eff=9.0, sig_m=sig_m,
                       mu=0.0, hfa=2.5, wqb=1.0, robust='none', irls=1)
            v, pf = evaluate(cfg)
            tag = f'sp={sig_prior} rho={rho} sigm={sig_m}: pooled {v:.3f}'
            if v < bestv:
                best, bestv = cfg, v; tag += '  <-- best'
            print(tag)
M1 = best
print(f'M1 winner: sig_prior={M1["sig_prior"]} rho={M1["rho"]} sig_m={M1["sig_m"]} ({bestv:.3f})')

print('\n----- HFA refine -----')
for hfa in (2.0, 2.5, 3.0):
    v, _ = evaluate(dict(M1, hfa=hfa))
    print(f'hfa={hfa}: {v:.3f}' + ('  <-- best' if v < bestv - 1e-9 else ''))
    if v < bestv:
        bestv = v; M1 = dict(M1, hfa=hfa)

# mu refine (efficiency channel intercept)
print('\n----- mu refine -----')
for mu in (-2.0, 0.0, 2.0):
    v, _ = evaluate(dict(M1, mu=mu))
    print(f'mu={mu}: {v:.3f}' + ('  <-- best' if v < bestv - 1e-9 else ''))
    if v < bestv:
        bestv = v; M1 = dict(M1, mu=mu)

# ================= M2 =================
print('\n===== M2 per-game noise =====')
M2 = M1
for name, delta in (('to_pen', dict(to_pen=1)), ('blow_pen', dict(blow_pen=1)),
                    ('wqb=0.5', dict(wqb=0.5)), ('wqb=0.25', dict(wqb=0.25))):
    v, _ = evaluate(dict(M2, **delta))
    keep = v < bestv - 1e-9
    print(f'{name}: {v:.3f}' + ('  KEEP' if keep else ''))
    if keep:
        bestv = v; M2 = dict(M2, **delta)

# ================= M3 =================
print('\n===== M3 robustness =====')
M3 = M2
for name, delta in (('clip2', dict(robust='clip', clip_c=2.0, irls=3)),
                    ('clip3', dict(robust='clip', clip_c=3.0, irls=3)),
                    ('t4', dict(robust='t', nu=4.0, irls=3)),
                    ('t8', dict(robust='t', nu=8.0, irls=3))):
    v, _ = evaluate(dict(M2, **delta))
    keep = v < bestv - 1e-9
    print(f'{name}: {v:.3f}' + ('  KEEP' if keep else ''))
    if keep:
        bestv = v; M3 = dict(M2, **delta)

# ================= M4 =================
print('\n===== M4 market-augmented arm =====')
M4, m4v = M3, bestv
for sig_mkt in (2.0, 3.0, 5.0):
    v, _ = evaluate(dict(M3, sig_mkt=sig_mkt), use_mkt=True)
    keep = v < m4v - 1e-9
    print(f'sig_mkt={sig_mkt}: {v:.3f}' + ('  KEEP' if keep else ''))
    if keep:
        m4v = v; M4 = dict(M3, sig_mkt=sig_mkt)
USE_MKT = 'sig_mkt' in M4
print(f'shipping arm: {"market-augmented" if USE_MKT else "blind"}')

# ================= M5 =================
print('\n===== M5 conditioning =====')
M5, m5v = M4, m4v
for name, delta in (('g5x1.25', dict(g5_mult=1.25)), ('g5x1.5', dict(g5_mult=1.5))):
    v, pf = evaluate(dict(M5, **delta), use_mkt=USE_MKT)
    folds_better = sum(1 for y in TUNE_FULL
                       if pf[y][0] < evaluate(M5, use_mkt=USE_MKT)[1][y][0])
    keep = v < m5v - 0.02 and folds_better >= 3
    print(f'{name}: {v:.3f} (folds better: {folds_better}/4)' + ('  KEEP' if keep else ''))
    if keep:
        m5v = v; M5 = dict(M5, **delta)

FINAL = M5
print(f'\nFINAL config: { {k: v for k, v in FINAL.items() if k != "g5set"} }')
print(f'FINAL pooled tune MAE: {m5v:.3f}')

# ================= gates + diagnostics on tune folds =================
print('\n===== GATES (tune folds) =====')
_, pf = evaluate(FINAL, use_mkt=USE_MKT)
frozen = dict(FINAL, rho=1.0, sig_eff=1e6, sig_m=1e6, robust='none', irls=1)
frozen.pop('sig_mkt', None)
_, pff = evaluate(frozen)
elo_best, elov = None, 1e9
for K in (0.05, 0.10, 0.20):
    tot = []
    for y in TUNE_FULL:
        R = {t: PRIORS[y][t][0] + PRIORS[y][t][1] for t in PRIORS[y]}
        errs = []
        for g in SEASONS[y]:
            if g['i'] not in R or g['j'] not in R:
                continue
            pred = R[g['i']] - R[g['j']] + FINAL['hfa'] * g['site']
            if g['w'] >= 2:
                errs.append(abs(pred - g['margin']))
            R[g['i']] += K * (g['margin'] - pred) / 2
            R[g['j']] -= K * (g['margin'] - pred) / 2
        tot.extend(errs)
    if np.mean(tot) < elov:
        elov, elo_best = np.mean(tot), K
print(f'{"fold":>6} {"B1":>7} {"frozen":>7} {"beats?":>7}')
wins = 0
for y in TUNE_FULL:
    b, f = pf[(y, 'wk3')][0], pff[(y, 'wk3')][0]
    wins += int(b < f)
    print(f'{y:>6} {b:>7.3f} {f:>7.3f} {"yes" if b < f else "NO":>7}')
pooled_b = np.mean([pf[(y, "wk3")][0] for y in TUNE_FULL])
pooled_f = np.mean([pff[(y, "wk3")][0] for y in TUNE_FULL])
print(f'B1-i (wk3+ vs frozen): pooled {pooled_b:.3f} vs {pooled_f:.3f}, folds {wins}/4 -> '
      f'{"PASS" if pooled_b < pooled_f and wins >= 3 else "FAIL"}')
pooled_all = np.mean([pf[y][0] for y in TUNE_FULL])
print(f'B1-ii (vs Elo K={elo_best}): {pooled_all:.3f} vs {elov:.3f} -> '
      f'{"PASS" if pooled_all < elov else "FAIL"}')

print('\n===== B1-iii gap to closes (clean segment, tune folds) =====')
for y in TUNE_FULL:
    _, lines_by_gid = market_data(y)
    fl = qb_flags(panel[y])
    rows = []
    for (w, m, act, i, j, gid) in pf[(y, 'preds')]:
        ln = lines_by_gid.get(int(gid) if str(gid).isdigit() else gid)
        if not ln or ln[0] is None:
            continue
        if abs(ln[0] - ln[1]) >= 2.5 or fl.get((w, i)) or fl.get((w, j)):
            continue
        rows.append((w, m, -ln[1]))
    for lo, hi in ((2, 4), (5, 8), (9, 15)):
        sub = [(m - mk) for w, m, mk in rows if lo <= w <= hi]
        if sub:
            print(f'  {y} wk{lo}-{hi}: RMSE vs close {np.sqrt(np.mean(np.square(sub))):.2f} (n={len(sub)})')

print('\n===== B1-iv effective preseason weight by week =====')
y = 2023
mk = market_chain(y, PRIORS[y], FINAL['hfa']) if USE_MKT else None
c = dict(FINAL)
if FINAL.get('g5_mult'):
    c['g5set'] = g5set(y)
p23 = run_season(SEASONS[y], PRIORS[y], c, teams=sorted(PRIORS[y]), mkt=mk)
pri23 = {t: PRIORS[y][t][0] + PRIORS[y][t][1] for t in PRIORS[y]}
by_w = defaultdict(list)
for (w, m, act, i, j, gid) in p23:
    pr = pri23[i] - pri23[j]
    by_w[w].append((m, pr))
for w in sorted(by_w):
    M_, P_ = np.array([a for a, _ in by_w[w]]), np.array([b for _, b in by_w[w]])
    if len(M_) > 10 and np.std(P_) > 0:
        print(f'  wk{w:2d}: corr(pred, preseason-implied) {np.corrcoef(M_, P_)[0,1]:.3f}')

json.dump({k: v for k, v in FINAL.items() if k != 'g5set'},
          open('data/research/insession_v1_constants.json', 'w'), indent=1)
print('\nconstants written (freeze pending findings commit)')
