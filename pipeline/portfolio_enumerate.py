#!/usr/bin/env python3
"""Enumerate the full bettable universe with CALIBRATED (honest) edges, for portfolio building.

Candidates:
  - regular-season win total, best-EV side per team (over/under) at the best posted book
  - conference win total (P4), best-EV side per team
  - the 15 head-to-head props

For each: p under calibrated / market-matched / ours, de-vigged market prob, edge_cal, edge_mkt,
conviction = min(edge_cal, edge_mkt) (edge net of the dispersion factor), EV at the calibrated
prob (the honest sizing number). Best side chosen by CALIBRATED EV (not raw) so we never carry a
bet that only clears on the un-shrunk ratings. Writes /tmp/candidates.json.
"""
import sys, os, json, math, statistics as st
sys.path.insert(0, os.path.dirname(__file__))
import win_engine as E
from win_totals_data import load
from win_totals_compute import _market, consensus_line, compute_market_stretch

P = json.load(open('outputs/win_totals_payload.json'))
META = P['meta']
CAL = META['cal_shrink']; STR = META['market_stretch']; MEAN = META['rating_mean']
teams = P['teams']; sched = P['schedules']; fcs = P['fcs']
M = _market()


def rating(nk, kind):
    t = teams[nk]
    return {'our': t['final'], 'cal': t['calibrated'], 'mkt': t['market_matched'], 'anchor': t['anchor']}[kind]


def oppR(ref, kind):
    return rating(ref, kind) if ref in teams else fcs[ref]['rating']


def oppB(ref):
    return teams[ref]['band'] if ref in teams else fcs[ref]['band']


def dist(nk, kind, conf_only=False):
    gl = [{'mu_opp': oppR(g['opp_ref'], kind), 'site': g['site'], 'band_opp': oppB(g['opp_ref'])}
          for g in sched[nk] if (not conf_only or g['is_conf'])]
    return E.win_distribution(rating(nk, kind), teams[nk]['band'], gl)['dist']


def implied(a):
    return (-a) / ((-a) + 100.0) if a < 0 else 100.0 / (a + 100.0)


def dec(a):
    return 1.0 + (a / 100.0 if a > 0 else 100.0 / (-a))


def under_from_over(o, cents=30):
    return (-o - cents) if o < 0 else -(o + cents)


def p_over_at(d, line):
    need = math.floor(line) + 1
    return sum(d[need:])


def total_candidate(nk, market):
    offers = M.get(teams[nk]['name'], {}).get(market, [])
    if not offers:
        return None
    dc = {k: dist(nk, k, conf_only=(market == 'conference')) for k in ['our', 'cal', 'mkt']}
    med = consensus_line([l for (l, o, b) in offers])
    # de-vig market at the consensus line (over/under from the 30-cent convention on posted over)
    at = [o for (l, o, b) in offers if abs(l - med) < 1e-6]
    oo = st.median(at)
    pov_v = implied(oo); puv_v = implied(under_from_over(oo))
    mkt_po = pov_v / (pov_v + puv_v)
    # best side by CALIBRATED EV across all posted books
    best = None
    for (line, o, b) in offers:
        uo = under_from_over(o)
        po_cal = p_over_at(dc['cal'], line); pu_cal = 1 - po_cal
        for side, p, odds in [('over', po_cal, o), ('under', pu_cal, uo)]:
            ev = p * (dec(odds) - 1) - (1 - p)
            if best is None or ev > best['ev_cal']:
                best = {'side': side, 'line': line, 'odds': odds, 'ev_cal': ev, 'p_cal': p}
    s = best['side']

    def edge(kind):
        po = p_over_at(dc[kind], med)
        return (po - mkt_po) if s == 'over' else ((1 - po) - (1 - mkt_po))
    ec, em, eo = edge('cal'), edge('mkt'), edge('our')
    return {'kind': market, 'team': teams[nk]['name'], 'nk': nk, 'conf': teams[nk]['conf'],
            'teams_used': [nk], 'side': s, 'line': best['line'], 'odds': best['odds'],
            'label': f"{teams[nk]['name']} {s} {best['line']:g} ({'+' if best['odds']>0 else ''}{best['odds']})"
                     + (' [conf]' if market == 'conference' else ''),
            'p_cal': best['p_cal'], 'edge_cal': ec, 'edge_mkt': em, 'edge_our': eo,
            'conv': min(ec, em), 'ev_cal': best['ev_cal'],
            'direction': s}


# ---- props ----
def diff_ge(a, b, t):
    return sum(a[i] * b[j] for i in range(len(a)) for j in range(len(b)) if i - j >= t)


def plays(a, b):
    return any(g['opp_kind'] == 'fbs' and g['opp_ref'] == b for g in sched[a])


def dist_excl(nk, kind, excl):
    gl = [{'mu_opp': oppR(g['opp_ref'], kind), 'site': g['site'], 'band_opp': oppB(g['opp_ref'])}
          for g in sched[nk] if not (g['opp_kind'] == 'fbs' and g['opp_ref'] == excl)]
    return E.win_distribution(rating(nk, kind), teams[nk]['band'], gl)['dist']


def prop_prob(f, d, th, kind):
    if not plays(f, d):
        return diff_ge(dist(f, kind), dist(d, kind), th)
    site = next(g['site'] for g in sched[f] if g['opp_kind'] == 'fbs' and g['opp_ref'] == d)
    pf = E.game_win_prob(rating(f, kind), rating(d, kind), site, teams[d]['band'])
    xf, xd = dist_excl(f, kind, d), dist_excl(d, kind, f)
    return pf * diff_ge(xf, xd, th - 1) + (1 - pf) * diff_ge(xf, xd, th + 1)


def prop_candidate(pr):
    OVR = 2 * implied(-110)
    mktp = implied(pr['price']) / OVR
    pc = prop_prob(pr['fav_nk'], pr['dog_nk'], pr['thresh'], 'cal')
    pm = prop_prob(pr['fav_nk'], pr['dog_nk'], pr['thresh'], 'mkt')
    po = prop_prob(pr['fav_nk'], pr['dog_nk'], pr['thresh'], 'our')
    ev = pc * (dec(pr['price']) - 1) - (1 - pc)
    ec, em = pc - mktp, pm - mktp
    return {'kind': 'prop', 'team': pr['fav'] + '/' + pr['dog'], 'nk': pr['fav_nk'],
            'conf': teams[pr['fav_nk']]['conf'], 'teams_used': [pr['fav_nk'], pr['dog_nk']],
            'side': 'fav', 'line': pr['line'], 'odds': pr['price'],
            'label': f"{pr['fav']} -{pr['line']:g} ({'+' if pr['price']>0 else ''}{pr['price']}) vs {pr['dog']}",
            'p_cal': pc, 'edge_cal': ec, 'edge_mkt': em, 'edge_our': po - mktp,
            'conv': min(ec, em), 'ev_cal': ev, 'direction': 'prop'}


cands = []
for nk in teams:
    for market in ['regular', 'conference']:
        c = total_candidate(nk, market)
        if c:
            cands.append(c)
for pr in P['props']:
    cands.append(prop_candidate(pr))

json.dump(cands, open('/tmp/candidates.json', 'w'))
pos = [c for c in cands if c['ev_cal'] > 0]
conv = [c for c in cands if c['conv'] >= 0.04]
print(f"candidates: {len(cands)}  (+EV_cal: {len(pos)}, conviction>=4%: {len(conv)})")
print("\nTop 20 by conviction (edge net of dispersion factor):")
for c in sorted(cands, key=lambda x: -x['conv'])[:20]:
    print(f"  {c['label']:<44} conv {c['conv']:+.1%}  EVcal {c['ev_cal']:+.2f}  "
          f"eCal {c['edge_cal']:+.1%} eMkt {c['edge_mkt']:+.1%}  {c['conf']}")
