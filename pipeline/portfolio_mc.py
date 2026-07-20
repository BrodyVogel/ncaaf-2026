#!/usr/bin/env python3
"""Full-field season Monte Carlo -> empirical payoff-correlation matrix across candidate bets,
then greedy selection of 15 max-edge, low-correlation positions.

Season model per sim (vectorized over N):
  - global dispersion factor g ~ N(0,1): realized_rating_i = mean + (final_i-mean)*(1+KAPPA*g)
    (KAPPA=0.12 ~ the season-to-season slope wobble in the 2021-25 backtest). This is the
    systematic factor almost every over-disperse edge loads on; it makes dog-overs and
    favorite-unders co-move (they're the same market-wide bet).
  - one season shock per team (shared as subject AND as everyone's opponent -> shared-opponent
    correlation), plus independent per-game noise sigma_game.
Payoff per bet = decimal-odds profit if it covers, else -1. Correlations of these payoff vectors
are exactly the outcome correlations that drive portfolio variance.
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import win_engine as E

P = json.load(open('outputs/win_totals_payload.json'))
META = P['meta']; MEAN = META['rating_mean']
teams = P['teams']; sched = P['schedules']; fcs = P['fcs']
HFA = E.HFA; SG = E.SIGMA_GAME
KAPPA = 0.12
N = 40000
rng = np.random.default_rng(20260720)

cands = json.load(open('/tmp/candidates.json'))
# portfolio universe: liquid + vetted -> regular totals & props only (conference excluded)
cands = [c for c in cands if c['kind'] in ('regular', 'prop')]

nks = list(teams.keys())
# Simulate with CALIBRATED ratings as the "truth" (our honest forecast) so empirical payoffs
# match the calibrated EVs we size on; the dispersion factor wobbles the (already-shrunk) spread.
base = {nk: teams[nk]['calibrated'] for nk in nks}
band = {nk: teams[nk]['band'] for nk in nks}

g = rng.standard_normal(N)
shock = {nk: rng.normal(0, band[nk], N) for nk in nks}
real = {nk: MEAN + (base[nk] - MEAN) * (1 + KAPPA * g) + shock[nk] for nk in nks}
# FCS opponent season draws (shared per FCS team)
fcs_names = set()
for nk in nks:
    for gm in sched[nk]:
        if gm['opp_kind'] == 'fcs':
            fcs_names.add(gm['opp_ref'])
fcs_real = {nm: fcs[nm]['rating'] + rng.normal(0, fcs[nm]['band'], N) for nm in fcs_names}

# simulate every team's win vector (regular) and conference win vector
Wreg = {}
Wconf = {}
for nk in nks:
    w = np.zeros(N); wc = np.zeros(N)
    for gm in sched[nk]:
        if gm['opp_kind'] == 'fbs':
            oppr = real[gm['opp_ref']]
        else:
            oppr = fcs_real[gm['opp_ref']]
        margin = real[nk] - oppr + HFA * gm['site'] + rng.normal(0, SG, N)
        win = (margin > 0).astype(np.float64)
        w += win
        if gm['is_conf']:
            wc += win
    Wreg[nk] = w; Wconf[nk] = wc


def dec(a):
    return 1.0 + (a / 100.0 if a > 0 else 100.0 / (-a))


def payoff(c):
    d = dec(c['odds']); L = c['line']
    if c['kind'] == 'prop':
        pr = next(p for p in P['props'] if p['fav'] + '/' + p['dog'] == c['team'])
        cover = (Wreg[pr['fav_nk']] - Wreg[pr['dog_nk']]) >= pr['thresh']
    else:
        W = Wconf[c['nk']] if c['kind'] == 'conference' else Wreg[c['nk']]
        need = math.floor(L) + 1
        cover = (W >= need) if c['side'] == 'over' else (W < need)
    return np.where(cover, d - 1.0, -1.0)


pay = np.vstack([payoff(c) for c in cands])                 # (B, N)
# empirical edge check vs analytic, and g-loading
emp_ev = pay.mean(axis=1)
gload = np.array([np.corrcoef(pay[i], g)[0, 1] for i in range(len(cands))])
C = np.corrcoef(pay)                                        # (B,B) payoff correlation

for i, c in enumerate(cands):
    c['emp_ev'] = float(emp_ev[i]); c['gload'] = float(gload[i])
np.save('/tmp/corr.npy', C)
json.dump(cands, open('/tmp/candidates_mc.json', 'w'))

# ---- greedy selection: max EV_cal, low correlation, diversified ----
POOL = [i for i, c in enumerate(cands) if c['ev_cal'] > 0.05 and c['conv'] >= 0.02]
POOL.sort(key=lambda i: -cands[i]['ev_cal'])
CONF_CAP = 3
def select(corr_cap):
    chosen = []; used_teams = set(); conf_ct = {}
    for i in POOL:
        c = cands[i]
        if any(t in used_teams for t in c['teams_used']):
            continue
        if conf_ct.get(c['conf'], 0) >= CONF_CAP:
            continue
        if any(abs(C[i, j]) > corr_cap for j in chosen):
            continue
        chosen.append(i); used_teams.update(c['teams_used']); conf_ct[c['conf']] = conf_ct.get(c['conf'], 0) + 1
        if len(chosen) == 15:
            break
    return chosen

cap = 0.30
chosen = select(cap)
while len(chosen) < 15 and cap < 0.7:
    cap += 0.05
    chosen = select(cap)

# naive top-15 by EV (one per team only) for contrast
naive = []; ut = set()
for i in sorted(range(len(cands)), key=lambda i: -cands[i]['ev_cal']):
    c = cands[i]
    if c['ev_cal'] <= 0 or any(t in ut for t in c['teams_used']):
        continue
    naive.append(i); ut.update(c['teams_used'])
    if len(naive) == 15:
        break

def avg_abs_corr(idx):
    if len(idx) < 2:
        return 0.0
    v = [abs(C[a, b]) for k, a in enumerate(idx) for b in idx[k+1:]]
    return sum(v) / len(v)

def port_stats(idx, tag):
    w = np.ones(len(idx)) / len(idx)                        # equal weight
    pv = (w[:, None] * pay[idx]).sum(axis=0)                # portfolio payoff per sim
    ev = pv.mean(); sd = pv.std()
    net_g = np.corrcoef(pv, g)[0, 1]
    print(f"\n== {tag} == n={len(idx)} corr_cap={cap if tag.startswith('DIVERS') else 'n/a'}")
    print(f"  mean EV/$1 (equal-wt): {ev:+.3f}   SD: {sd:.3f}   EV/SD: {ev/sd:.3f}   avg|corr|: {avg_abs_corr(idx):.3f}   net g-load: {net_g:+.2f}")
    ov = sum(1 for i in idx if cands[i]['direction'] == 'over')
    un = sum(1 for i in idx if cands[i]['direction'] == 'under')
    pp = sum(1 for i in idx if cands[i]['direction'] == 'prop')
    from collections import Counter
    print(f"  direction: {ov} over / {un} under / {pp} prop    conferences: {dict(Counter(cands[i]['conf'] for i in idx))}")
    return ev, sd

print(f"\nsimulated {N} seasons, KAPPA={KAPPA}, {len(cands)} candidate bets, pool={len(POOL)}")
port_stats(naive, "NAIVE top-15 by EV (one/team)")
port_stats(chosen, "DIVERSIFIED (corr-capped, conf-capped)")

print("\n--- THE 15 (diversified) ---")
print(f"{'#':>2} {'bet':<46}{'EVcal':>7}{'conv':>7}{'gload':>7}  conf")
for r, i in enumerate(sorted(chosen, key=lambda i: -cands[i]['ev_cal']), 1):
    c = cands[i]
    print(f"{r:>2} {c['label']:<46}{c['ev_cal']:>+7.2f}{c['conv']:>+7.1%}{c['gload']:>+7.2f}  {c['conf']}")
json.dump([cands[i] for i in sorted(chosen, key=lambda i: -cands[i]['ev_cal'])], open('/tmp/portfolio15.json', 'w'))
