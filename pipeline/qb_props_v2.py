#!/usr/bin/env python3
"""Pricer v2 — season QB passing-yards props.

Spec: docs/research/PRICER_V2_SPEC_2026-08-04.md (committed before this run).
Structure: v0 simulation skeleton (G hazard x fitted pace x noise) with
pace-level-aware persistence fit, transfer shift, empirical hazards, and a
fresh 2021-24 -> 2025 holdout Brier-optimal shrink clamped [0.50, 0.85].
"""
import json, csv, re, sys, collections
import numpy as np

ROOT = '/home/claude/cfb-2026-power-ratings'
SEED = 20260804
NSIM = 200_000
PER_GAME_SD = 75.0          # v0 constant, per spec
BREAKEVEN = 0.5305          # -113 both sides
KGRID = np.arange(0.30, 1.2001, 0.05)
KLO, KHI = 0.50, 0.85

def nk(s):
    """Normalize a player name; strip generational suffixes (Jr., III, ...)
    BEFORE compaction — the procedure's 'name variants (suffixes!)' warning."""
    s = re.sub(r'\s+(jr|sr|ii|iii|iv)\.?\s*$', '', s.strip(), flags=re.I)
    return re.sub(r'[^a-z]', '', s.lower())

# ---------- load panel ----------
panel = json.load(open(f'{ROOT}/data/cfbd/qb_props/panel_s20.json'))

def fit_pace(rows):
    """OLS pace1 = a + b*pace0 + c*transfer on g10_1>=6 rows.
    Adopt transfer x pace0 interaction only if F-test p < .05."""
    sub = [r for r in rows if r.get('pace1') is not None and r['g10_1'] >= 6]
    x0 = np.array([r['pace0'] for r in sub])
    tr = np.array([1.0 if r['transfer'] else 0.0 for r in sub])
    y  = np.array([r['pace1'] for r in sub])
    n = len(sub)
    X3 = np.column_stack([np.ones(n), x0, tr])            # base
    X4 = np.column_stack([np.ones(n), x0, tr, tr * x0])   # + interaction
    b3, res3, *_ = np.linalg.lstsq(X3, y, rcond=None)
    b4, res4, *_ = np.linalg.lstsq(X4, y, rcond=None)
    rss3 = float(((y - X3 @ b3) ** 2).sum())
    rss4 = float(((y - X4 @ b4) ** 2).sum())
    F = (rss3 - rss4) / (rss4 / (n - 4))
    # F(1, n-4) p-value via survival function of F distribution
    from scipy.stats import f as fdist
    pF = float(fdist.sf(F, 1, n - 4))
    use4 = pF < 0.05
    beta = b4 if use4 else b3
    rss = rss4 if use4 else rss3
    dof = n - (4 if use4 else 3)
    sigma = float(np.sqrt(rss / dof))
    # slope t-stat (base model) for the record
    XtXi = np.linalg.inv(X3.T @ X3)
    se_b = float(np.sqrt(rss3 / (n - 3) * XtXi[1, 1]))
    return {'beta': beta.tolist(), 'interaction': bool(use4), 'F': F, 'pF': pF,
            'sigma_season': sigma, 'n_fit': n, 'slope_t': float(b3[1] / se_b),
            'slope': float(b3[1])}

def predict_mu(fitres, pace0, transfer):
    b = fitres['beta']
    if fitres['interaction']:
        return b[0] + b[1] * pace0 + b[2] * transfer + b[3] * transfer * pace0
    return b[0] + b[1] * pace0 + b[2] * transfer

def hazard(rows, transfer):
    gs = [min(int(r['g10_1']), 13) for r in rows if bool(r['transfer']) == transfer]
    cnt = collections.Counter(gs)
    n = len(gs)
    pmf = np.array([cnt.get(g, 0) / n for g in range(14)])
    return pmf, n

def price(fitres, pmf, pace0, transfer, line, rng, cap12=False):
    mu = predict_mu(fitres, pace0, 1.0 if transfer else 0.0)
    G = rng.choice(14, size=NSIM, p=pmf)
    if cap12:
        G = np.minimum(G, 12)
    m = rng.normal(mu, fitres['sigma_season'], size=NSIM)
    tot = G * m + rng.normal(0.0, PER_GAME_SD, size=NSIM) * np.sqrt(G)
    return float((tot < line).mean()), mu

# ---------- holdout calibration: fit 2021-24, price 2025 synthetic lines ----------
fit_rows = [r for r in panel if r['t'] <= 2024]
hold_rows = [r for r in panel if r['t'] == 2025]
fit_h = fit_pace(fit_rows)
pmf_sec_h, n_sec_h = hazard(fit_rows, False)
pmf_tr_h,  n_tr_h  = hazard(fit_rows, True)

rng = np.random.default_rng(SEED)
pred, real = [], []
for r in hold_rows:
    L = 12.0 * r['pace0']
    pmf = pmf_tr_h if r['transfer'] else pmf_sec_h
    p, _ = price(fit_h, pmf, r['pace0'], r['transfer'], L, rng)
    pred.append(p)
    real.append(1.0 if r['yds1'] < L else 0.0)
pred = np.array(pred); real = np.array(real)

briers = [(float(((0.5 + k * (pred - 0.5)) - real) ** 2 .mean() if False else (((0.5 + k * (pred - 0.5)) - real) ** 2).mean()), float(k)) for k in KGRID]
briers = [(float((((0.5 + k * (pred - 0.5)) - real) ** 2).mean()), float(k)) for k in KGRID]
brier_star, k_star = min(briers)
k_final = float(np.clip(k_star, KLO, KHI))
brier_at_final = float((((0.5 + k_final * (pred - 0.5)) - real) ** 2).mean())
brier_unshrunk = float(((pred - real) ** 2).mean())
brier_base = float(((real.mean() - real) ** 2).mean())

print('=== HOLDOUT (fit 2021-24 -> price 2025 synthetic lines) ===')
print(f'fit: pace1 = {fit_h["beta"][0]:.1f} + {fit_h["beta"][1]:.3f}*pace0 '
      f'+ {fit_h["beta"][2]:+.1f}*transfer  (interaction: {fit_h["interaction"]}, '
      f'F p={fit_h["pF"]:.3f}); slope t={fit_h["slope_t"]:.2f}; '
      f'sigma_season={fit_h["sigma_season"]:.1f}; n_fit={fit_h["n_fit"]}')
print(f'holdout n={len(hold_rows)}  predicted mean {pred.mean():.3f}  realized mean {real.mean():.3f}')
print(f'Brier: unshrunk {brier_unshrunk:.4f} | k*={k_star:.2f} -> {brier_star:.4f} | '
      f'k_final={k_final:.2f} -> {brier_at_final:.4f} | base-rate {brier_base:.4f} | v1 spec was 0.229')
for lo in (0.5, 0.6, 0.7, 0.8):
    m = (pred >= lo) & (pred < lo + 0.1)
    if m.sum():
        print(f'  bucket pred [{lo:.1f},{lo+0.1:.1f}): n={int(m.sum()):2d}  realized {real[m].mean():.3f}')

# gate from spec: ship only if holdout Brier (at k_final) beats v1's 0.229
SHIP = brier_at_final <= 0.229
print(f'SHIP GATE (Brier <= 0.229): {"PASS" if SHIP else "FAIL"}')
if k_star < 0.60:
    print('WARNING: k* < 0.60 — spec flags this as suspect.')

# ---------- final fit on all years, price the 2026 board ----------
fit_all = fit_pace(panel)
pmf_sec, n_sec = hazard(panel, False)
pmf_tr,  n_tr  = hazard(panel, True)
print(f'\n=== FINAL FIT (2021-2025) ===')
print(f'pace1 = {fit_all["beta"][0]:.1f} + {fit_all["beta"][1]:.3f}*pace0 '
      f'{fit_all["beta"][2]:+.1f}*transfer  (interaction: {fit_all["interaction"]}, '
      f'F p={fit_all["pF"]:.3f}); slope t={fit_all["slope_t"]:.2f}; '
      f'sigma_season={fit_all["sigma_season"]:.1f}; n_fit={fit_all["n_fit"]}')
print(f'hazard n: secure {n_sec}, transfer {n_tr}')
print('hazard P(12+): secure {:.3f}, transfer {:.3f}'.format(pmf_sec[12:].sum(), pmf_tr[12:].sum()))
print('hazard P(13):  secure {:.3f}, transfer {:.3f}'.format(pmf_sec[13], pmf_tr[13]))

# exact pace0 from flat file, PANEL-CONSISTENT BASIS: total yds / games with
# >=10 attempts. Audit result 2026-08-04: 181/181 panel rows match this basis,
# 0 match all-games-only (discriminating rows e.g. Van Dyke 270.30 = tot/g10).
att = collections.defaultdict(lambda: [0.0, 0, 0])   # [yds, g10, all_games]
for row in csv.DictReader(open(f'{ROOT}/data/cfbd/qb_props/player_games_flat.csv')):
    if int(row['year']) != 2025:
        continue
    k = nk(row['player'])
    att[k][0] += float(row['yds'] or 0)
    att[k][2] += 1
    if float(row['att'] or 0) >= 10:
        att[k][1] += 1

board = json.load(open(f'{ROOT}/data/cfbd/qb_props/pricer_v1_2026-08-04.json'))
out = []
rng = np.random.default_rng(SEED + 1)
for e in board:
    key = nk(e['qb'])
    if key in att and att[key][1] > 0:
        pace0 = att[key][0] / att[key][1]          # g10 basis, matches panel
        src = 'flat-g10'
        if abs(pace0 - e['pace0']) > 0.6:
            print(f'  NOTE {e["qb"]}: g10 pace0 {pace0:.2f} vs v1 JSON {e["pace0"]} '
                  f'(v1 input was rounded/hand-entered; g10 basis governs)')
    else:
        pace0 = float(e['pace0'])
        src = 'json-fallback'
        print(f'  WARN {e["qb"]}: no flat-file match, using JSON pace0={pace0}')
    pmf = pmf_tr if e['transfer'] else pmf_sec
    p_raw, mu = price(fit_all, pmf, pace0, e['transfer'], e['line'], rng)
    p_raw12, _ = price(fit_all, pmf, pace0, e['transfer'], e['line'], rng, cap12=True)
    p_v2 = 0.5 + k_final * (p_raw - 0.5)
    p_v2_12 = 0.5 + k_final * (p_raw12 - 0.5)
    edge_under = 100 * (p_v2 - BREAKEVEN)
    edge_over = 100 * ((1 - p_v2) - BREAKEVEN)
    out.append({'qb': e['qb'], 'line': e['line'], 'pace0': round(pace0, 2),
                'pace0_src': src, 'transfer': e['transfer'],
                'ratio': round(e['line'] / (12 * pace0), 4),
                'mu_pace_pred': round(mu, 1),
                'p_raw': round(p_raw, 4), 'p_v2': round(p_v2, 4),
                'edge_under': round(edge_under, 1), 'edge_over': round(edge_over, 1),
                'p_v2_strict12': round(p_v2_12, 4),
                'edge_under_strict12': round(100 * (p_v2_12 - BREAKEVEN), 1),
                'p_under_v1': e['p_under_v1'],
                'edge_v1': round(100 * (e['p_under_v1'] - BREAKEVEN), 1)})

out.sort(key=lambda d: -d['edge_under'])
print(f'\n=== BOARD v2 (k={k_final:.2f}) — sorted by under edge ===')
print(f'{"QB":18s} {"line":>7} {"pace0":>7} {"tr":>3} {"r":>6} {"mu_hat":>7} '
      f'{"p_raw":>6} {"p_v2":>6} {"edgeU":>6} {"v1":>6} {"delta":>6} {"strict12":>8}')
for d in out:
    print(f'{d["qb"]:18s} {d["line"]:7.1f} {d["pace0"]:7.2f} '
          f'{"T" if d["transfer"] else "-":>3} {d["ratio"]:6.3f} {d["mu_pace_pred"]:7.1f} '
          f'{d["p_raw"]:6.3f} {d["p_v2"]:6.3f} {d["edge_under"]:+6.1f} '
          f'{d["edge_v1"]:+6.1f} {d["edge_under"]-d["edge_v1"]:+6.1f} '
          f'{d["edge_under_strict12"]:+8.1f}')

meta = {'spec': 'docs/research/PRICER_V2_SPEC_2026-08-04.md', 'seed': SEED,
        'nsim': NSIM, 'per_game_sd': PER_GAME_SD,
        'holdout': {'n': len(hold_rows), 'pred_mean': round(float(pred.mean()), 4),
                    'real_mean': round(float(real.mean()), 4),
                    'brier_unshrunk': round(brier_unshrunk, 4),
                    'k_star': round(k_star, 2), 'brier_at_kstar': round(brier_star, 4),
                    'k_final': round(k_final, 2), 'brier_at_kfinal': round(brier_at_final, 4),
                    'brier_base_rate': round(brier_base, 4), 'ship_gate_pass': bool(SHIP)},
        'fit_holdout_years': fit_h, 'fit_all_years': fit_all,
        'hazard_secure_pmf': [round(float(x), 4) for x in pmf_sec],
        'hazard_transfer_pmf': [round(float(x), 4) for x in pmf_tr]}
json.dump({'meta': meta, 'board': out},
          open(f'{ROOT}/data/cfbd/qb_props/pricer_v2_2026-08-04.json', 'w'), indent=1)
print('\nwrote data/cfbd/qb_props/pricer_v2_2026-08-04.json')
