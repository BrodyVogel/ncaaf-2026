#!/usr/bin/env python3
"""S8 Phase 1: fidelity of the mechanical (auto-roster) formula arm.

(1) 2026: auto arm (portal mode) vs the curated proforma_v2 arm -> rho per unit,
    team-score rho, and the GATE metric: rho of D = z(team score) - z(SP+ preseason).
(2) 2025 bridge: Mode A (portal recipe) vs Mode B (real CFBD roster) same metrics --
    how much of Mode A's loss is membership vs irreducible.
(3) Curation ROI: where the hand-curated arm and the machine disagree most.

Outputs: data/research/s8_phase1_fidelity.json + printed report. No outcome data
(SP+ finals / misses / wins) is touched in this phase.
"""
import csv, json, os, sys
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8_shadow_arm import (build_shadow, percentiles, team_scores, load_spine,
                           norm, GRPS, UW, R)

SP_ALIAS = {'connecticut': 'uconn', 'texasam': 'texasam', 'olemiss': 'olemiss',
            'hawaii': 'hawaii', 'sanjosestate': 'sanjosestate'}


def zmap(d):
    ks = list(d); vs = np.array([d[k] for k in ks], float)
    mu, sd = vs.mean(), vs.std()
    return {k: (d[k] - mu) / sd for k in ks}


def sp_preseason(year):
    """team norm-key -> preseason SP+ overall."""
    out = {}
    if year == 2026:
        # CFBD sp_2026 endpoint was empty at the July pull; use the anchor capture.
        tm = {r['norm_key']: norm(r['cfbd_school'])
              for r in csv.DictReader(open(f'{R}/data/anchors/team_name_map.csv'))}
        with open(f'{R}/data/anchors/SP+_2026preseason_2026-07-12.csv') as f:
            for r in csv.DictReader(f):
                k = tm.get(r['norm_key'], r['norm_key'])
                out[SP_ALIAS.get(k, k)] = float(r['sp_plus_overall'])
    else:
        with open(f'{R}/data/backtest/sp_preseason/SP+_{year}_preseason.csv') as f:
            for r in csv.DictReader(f):
                k = r['norm_key']
                out[SP_ALIAS.get(k, k)] = float(r['sp_plus_overall'])
    return out


def corr(a, b):
    return float(np.corrcoef(a, b)[0, 1])


def spearman(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    return corr(ra.astype(float), rb.astype(float))


def compare(unitsA, pctsA, scoresA, unitsB, pctsB, scoresB, sp, label):
    """A vs B fidelity + gate metric vs an SP+ vintage. Returns dict."""
    rep = {'label': label, 'units': {}, 'n_teams': 0}
    for u in GRPS:
        ks = [k for k in unitsA if k[1] == u and k in unitsB]
        a = np.array([pctsA[k] for k in ks]); b = np.array([pctsB[k] for k in ks])
        rep['units'][u] = dict(n=len(ks), pearson=corr(a, b), spearman=spearman(a, b),
                               mad=float(np.mean(np.abs(a - b))))
    common = [t for t in scoresA if t in scoresB and t in sp]
    rep['n_teams'] = len(common)
    sA = {t: scoresA[t]['score'] for t in common}
    sB = {t: scoresB[t]['score'] for t in common}
    spz = zmap({t: sp[t] for t in common})
    zA, zB = zmap(sA), zmap(sB)
    dA = np.array([zA[t] - spz[t] for t in common])
    dB = np.array([zB[t] - spz[t] for t in common])
    rep['team_score_rho'] = corr(np.array([sA[t] for t in common]),
                                 np.array([sB[t] for t in common]))
    rep['gate_rho_D'] = corr(dA, dB)
    rep['spearman_D'] = spearman(dA, dB)
    rep['_D'] = {t: (float(dA[i]), float(dB[i])) for i, t in enumerate(common)}
    return rep


def main():
    spine = load_spine()

    # ---- curated reference (proforma v2, as shipped) ----
    cur_units, cur_team_pct = {}, defaultdict(dict)
    for r in csv.DictReader(open(f'{R}/outputs/proforma_v2_2026.csv')):
        tk = norm(r['team'])
        cur_units[(tk, r['unit'])] = float(r['v2_pct'])
        cur_team_pct[tk][r['unit']] = float(r['v2_pct'])
    cur_scores = {}
    for tk, uu in cur_team_pct.items():
        num = den = 0.0
        for u in GRPS:
            num += UW[u] * uu.get(u, 50.0); den += UW[u]
        cur_scores[tk] = dict(score=num / den, n_units=len(uu))

    # ---- auto 2026 (Mode A) ----
    a26_units, diagA26 = build_shadow(2026, 'portal', spine)
    a26_pcts = percentiles(a26_units)
    a26_scores = team_scores(a26_units, a26_pcts)

    sp26 = sp_preseason(2026)
    # curated units dict needs same key-shape for compare(): fake units/pcts maps
    curU = {k: {'value': v} for k, v in cur_units.items()}
    rep1 = compare(a26_units, a26_pcts, a26_scores, curU, cur_units, cur_scores,
                   sp26, '2026 auto(ModeA) vs curated')

    # ---- 2025 bridge: Mode A vs Mode B ----
    b25_units, diagB25 = build_shadow(2025, 'roster', spine)
    a25_units, diagA25 = build_shadow(2025, 'portal', spine)
    b25_p, a25_p = percentiles(b25_units), percentiles(a25_units)
    b25_s, a25_s = team_scores(b25_units, b25_p), team_scores(a25_units, a25_p)
    rep2 = compare(a25_units, a25_p, a25_s, b25_units, b25_p, b25_s,
                   sp_preseason(2025), '2025 ModeA vs ModeB')

    # ---- curation ROI: biggest auto-vs-curated unit gaps ----
    gaps = []
    for k, cpct in cur_units.items():
        if k in a26_pcts:
            gaps.append((abs(a26_pcts[k] - cpct), k[0], k[1], a26_pcts[k], cpct))
    gaps.sort(reverse=True)

    out = dict(rep_2026=rep1, rep_2025_bridge=rep2,
               diag=dict(auto26=diagA26, a25=diagA25, b25=diagB25),
               top_gaps=[dict(team=t, unit=u, auto=round(a, 1), curated=round(c, 1))
                         for _, t, u, a, c in gaps[:25]])
    j = {k: v for k, v in out.items()}
    for rep in (j['rep_2026'], j['rep_2025_bridge']):
        rep.pop('_D', None)
    json.dump(j, open(f'{R}/data/research/s8_phase1_fidelity.json', 'w'), indent=1)

    for rep in (rep1, rep2):
        print(f"\n== {rep['label']} (n={rep['n_teams']} teams)")
        for u in GRPS:
            d = rep['units'][u]
            print(f"  {u:5s} n={d['n']:4d} r={d['pearson']:+.3f} rho_s={d['spearman']:+.3f} MAD={d['mad']:.1f} pct-pts")
        print(f"  team-score r = {rep['team_score_rho']:+.3f}")
        print(f"  GATE rho(D)  = {rep['gate_rho_D']:+.3f}  (spearman {rep['spearman_D']:+.3f})")
    print('\nTop curation gaps (auto vs curated pct):')
    for _, t, u, a, c in gaps[:12]:
        print(f'  {t:20s} {u:5s} auto {a:5.1f} vs curated {c:5.1f}')
    print('\ndiag:', out['diag'])


if __name__ == '__main__':
    main()
