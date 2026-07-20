#!/usr/bin/env python3
"""Compute core for the win-totals artifact.

Builds the self-contained data payload the browser needs: every team's ratings, each team's
schedule (opponents referenced by key so a rating edit propagates to opponents' totals too),
FCS opponent ratings, and the market win-total lines (regular + P4 conference). The browser
JS re-derives all win distributions / fair odds / edges from this payload, so a manual rating
change recomputes the whole board live.

This module also computes the same distributions in Python (the reference) so we can (a) fill
the initial render and (b) assert Python<->JS parity in validation.
"""
import sys, os, json, csv, statistics as st, math
sys.path.insert(0, os.path.dirname(__file__))
from collections import defaultdict
from win_totals_data import load
import win_engine as E

# Reclassifying / first-year FBS programs: our grade has thin FBS-level data, so flag the
# rating (and any market edge) as elevated-uncertainty in the UI.
RECLASS_2026 = {'North Dakota State'}


def _derivations():
    """Per-team rating derivation for the primer page: unit grades (grade_board) + the
    assembly math that turns grades into the final power number (ASSEMBLY)."""
    import re as _re

    def _grade(v):
        """'91' -> (91,''); '42L' -> (42,'L'); '' -> (None,'')."""
        if not v:
            return (None, '')
        m = _re.match(r'\s*(\d+)\s*([LMH]?)', str(v))
        return (int(m.group(1)), m.group(2)) if m else (None, '')

    units = {}
    for r in csv.DictReader(open('outputs/grade_board.csv')):
        row = {}
        for u in ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB', 'ST']:
            score, conf = _grade(r.get(u, ''))
            row[u] = score
            row[u + '_conf'] = conf
        row['sum'] = _grade(r.get('sum', ''))[0]
        row['coach_change'] = r.get('coach_change', '') in ('True', 'true', '1')
        units[r['team']] = row
    # Teams whose final was manually set (grade unreliable): the ASSEMBLY 'final' column is the
    # override, but the component columns are the *discarded* grade math. Flag them so the primer
    # shows the override note instead of a grade-sum narrative that doesn't reconcile.
    ovr = {}
    if os.path.exists('data/manual_overrides_2026.csv'):
        for orow in csv.DictReader(open('data/manual_overrides_2026.csv')):
            ovr[orow['team']] = orow
    der = {}
    for r in csv.DictReader(open('outputs/final_pass/ASSEMBLY.csv')):
        t = r['team']
        cls = (r['class'] or '').replace('+', '')
        resid_adj = float(r['k_x_resid_clipped'].replace('+', '') or 0)
        st_term = float((r['st_term'] or '0').replace('+', ''))
        recenter = float((r['recenter_shift'] or '0').replace('+', ''))
        anchor_blend = float(r['anchor_blend'])
        # grade_final = what the power number would have been from grades alone (pre-override);
        # for non-override teams this equals the printed 'final' up to rounding.
        grade_final = anchor_blend + resid_adj + (float(cls) if cls else 0.0) + st_term + recenter
        o = ovr.get(t)
        d = {'anchor_blend': anchor_blend,
             'implied_off': float(r['implied_off']), 'anchor_off': float(r['anchor_off']),
             'implied_def': float(r['implied_def']), 'anchor_def': float(r['anchor_def']),
             'residual': float(r['residual']),
             'resid_adj': resid_adj,
             'class': cls,
             'st_term': st_term,
             'recenter_shift': recenter,
             'final': float(r['final']), 'band': float(r['band']),
             'grade_final': round(grade_final, 2),
             'overridden': o is not None,
             'override_note': (o['note'] if o else ''),
             'L_count': int(r['L_count']) if r['L_count'] else 0,
             'new_HC': (r.get('new_HC', '') or '').strip() not in ('', '0', 'False'),
             'capped': (r.get('capped', '') or '').strip() not in ('', '0', 'False'),
             'units': units.get(t, {})}
        der[t] = d
    return der


def _market():
    """team (board name) -> {'regular': [(line,over_odds,book)...], 'conference': [...]}.
    Market-file names are aliased to board names (MKT_ALIAS) so every team joins."""
    from win_totals_data import MKT_ALIAS
    m = defaultdict(lambda: {'regular': [], 'conference': []})
    for r in csv.DictReader(open('data/win_totals/win_totals_2026.csv')):
        team = MKT_ALIAS.get(r['team'], r['team'])
        m[team][r['market']].append((float(r['line']), int(r['over_odds']), r['book']))
    return m


def consensus_line(lines):
    """The posted line nearest the median of all posted lines (never a phantom midpoint).
    Tie on distance -> the line more books post; then the lower line."""
    med = st.median(lines)
    uniq = sorted(set(lines))
    return min(uniq, key=lambda L: (abs(L - med), -lines.count(L), L))


def _ladder(dist):
    """For each half-point line L in 0.5..G-0.5: P(over)=P(wins>=ceil(L)); fair no-vig odds."""
    G = len(dist) - 1
    out = []
    for k in range(1, G + 1):                       # line = k-0.5, over means wins>=k
        p_over = sum(dist[j] for j in range(k, G + 1))
        out.append({'line': k - 0.5,
                    'p_over': p_over,
                    'fair_over': E.prob_to_american(p_over),
                    'fair_under': E.prob_to_american(1 - p_over)})
    return out


def _dist_block(mu, band, games):
    """games -> engine dict + survival ladder + fair-odds ladder + per-win fair odds."""
    eg = [{'mu_opp': g['mu_opp'], 'site': g['site'], 'band_opp': g['band_opp']} for g in games]
    r = E.win_distribution(mu, band, eg)
    dist = r['dist']
    # fair no-vig odds for each exact win count k (owner: "fair odds for each number of wins")
    per_win = [{'k': k, 'p': dist[k], 'fair': E.prob_to_american(dist[k])} for k in range(len(dist))]
    return {'dist': dist, 'expected_wins': r['expected_wins'], 'G': r['G'],
            'per_win': per_win, 'ladder': _ladder(dist)}


def _market_block(offers, dist_our, dist_anchor):
    """offers: [(line,over_odds,book)]. Returns book list + best-price bet + edges vs our/anchor."""
    if not offers:
        return None
    books = []
    for line, oo, book in sorted(offers, key=lambda x: (x[0], -x[1])):
        uo = E.under_from_over(oo)
        books.append({'book': book, 'line': line, 'over_odds': oo, 'under_odds': uo})

    def p_over_at(dist, line):
        need = math.floor(line) + 1
        return sum(dist[k] for k in range(need, len(dist)))

    # Evaluate every posted side with our probability; the best bet = max EV across all offers.
    cand = []
    for b in books:
        po = p_over_at(dist_our['dist'], b['line'])
        pu = 1 - po
        ev_o = po * (E.american_to_decimal(b['over_odds']) - 1) - (1 - po)
        ev_u = pu * (E.american_to_decimal(b['under_odds']) - 1) - (1 - pu)
        cand.append({'side': 'over', 'book': b['book'], 'line': b['line'],
                     'odds': b['over_odds'], 'our_p': po, 'ev': ev_o})
        cand.append({'side': 'under', 'book': b['book'], 'line': b['line'],
                     'odds': b['under_odds'], 'our_p': pu, 'ev': ev_u})
    best = max(cand, key=lambda c: c['ev'])

    # Consensus line + de-vigged market prob there, for a clean edge headline.
    # Audit fix 2026-07-20: use the POSTED line nearest the median, never a phantom midpoint
    # (with books split 7.5/8.5 the plain median is 8.0 — a line nobody offers, and pooling
    # odds across different lines mislabels the headline edge). Tie -> the line more books post.
    med_line = consensus_line([b['line'] for b in books])
    at = [b['over_odds'] for b in books if abs(b['line'] - med_line) < 1e-6]
    oo = st.median(at)
    po_v = E.american_to_prob(oo); pu_v = E.american_to_prob(E.under_from_over(oo))
    mkt_po = po_v / (po_v + pu_v)

    def edge_block(dist):
        our_po = p_over_at(dist['dist'], med_line)
        return {'line': med_line, 'mkt_p_over': mkt_po, 'our_p_over': our_po,
                'edge_over': our_po - mkt_po, 'edge_under': (1 - our_po) - (1 - mkt_po)}

    return {'books': books, 'median_line': med_line,
            'best': best, 'edge_our': edge_block(dist_our),
            'edge_anchor': edge_block(dist_anchor)}


def compute_market_stretch(teams, sch, M):
    """The MARKET-MATCHED set: our ratings linearly stretched (around the field mean) by the
    factor s* whose win-total edges have ZERO slope vs the market line — i.e. the version of our
    ratings that adopts the market's *dispersion*. On this set the systematic fade-favorites/
    back-dogs tilt is neutralized, so any surviving edge is team-specific. Returns (s*, mean)."""
    mean = st.mean(t['final'] for t in teams.values())

    def devig(line, offers):
        at = [o for (l, o, b) in offers if abs(l - line) < 1e-6]
        oo = st.median(at)
        po = E.american_to_prob(oo); pu = E.american_to_prob(E.under_from_over(oo))
        return po / (po + pu)

    def pov(dist, line):
        need = math.floor(line) + 1
        return sum(dist[k] for k in range(need, len(dist)))

    def slope(s):
        xs, ys = [], []
        for nk, t in teams.items():
            offers = M.get(t['name'], {}).get('regular')
            if nk not in sch or not offers:
                continue
            L = consensus_line([l for (l, o, b) in offers])
            games = []
            for g in sch[nk]:
                o = g['opp']
                om = mean + s * (o['mu_our'] - mean) if o['kind'] == 'fbs' else o['mu_our']
                games.append({'mu_opp': om, 'site': g['site'], 'band_opp': o['band']})
            d = E.win_distribution(mean + s * (t['final'] - mean), t['band'], games)['dist']
            xs.append(L); ys.append(pov(d, L) - devig(L, offers))
        mx = st.mean(xs); my = st.mean(ys)
        return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)

    lo, hi = 0.8, 1.6
    for _ in range(22):
        mid = (lo + hi) / 2
        if slope(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2, mean


def build_payload():
    """Lean, self-contained inputs the browser computes everything from. Small on purpose:
    no precomputed distributions (JS re-derives them, incl. after manual rating edits)."""
    D = load()
    teams, sch, fcs, n2 = D['teams'], D['schedules'], D['fcs'], D['name2nk']
    M = _market()
    DER = _derivations()
    from team_primers import build_primers
    PRIMERS = build_primers()
    mkt_stretch, rating_mean = compute_market_stretch(teams, sch, M)
    pteams, pfcs, psched, pmarket = {}, {}, {}, {}
    for name, nk in n2.items():
        if nk not in teams:
            continue
        t = teams[nk]
        mm = rating_mean + mkt_stretch * (t['final'] - rating_mean)
        pteams[nk] = {'nk': nk, 'name': name, 'conf': t['conf'],
                      'final': round(t['final'], 2), 'band': round(t['band'], 2),
                      'anchor': round(t['anchor'], 2),
                      'market_matched': round(mm, 2),
                      'reclass': name in RECLASS_2026,
                      'der': DER.get(name), 'primer': PRIMERS.get(name)}
    for name, fr in fcs.items():
        pfcs[name] = {'name': name, 'rating': fr['rating'], 'band': fr['band'],
                      'tier': fr.get('tier', ''), 'note': fr.get('note', '')}
    for nk, glist in sch.items():
        arr = []
        for g in glist:
            o = g['opp']
            e = {'week': g['week'], 'site': g['site'], 'is_conf': g['is_conf'],
                 'opp_kind': o['kind'],
                 'opp_ref': (o['nk'] if o['kind'] == 'fbs' else o['name']),
                 'opp_name': o['name']}
            if g.get('flex'):
                e['flex'] = True
            arr.append(e)
        psched[nk] = arr
        t = teams[nk]
        pmarket[nk] = {'regular': [[l, o, b] for (l, o, b) in M.get(t['name'], {}).get('regular', [])],
                       'conference': [[l, o, b] for (l, o, b) in M.get(t['name'], {}).get('conference', [])]}
    return {
        'meta': {'hfa': E.HFA, 'sigma_game': E.SIGMA_GAME, 'band_to_sd': E.BAND_TO_SD,
                 'gh_nodes': E.GH_NODES, 'gh_weights': E.GH_WEIGHTS,
                 'n_teams': len(pteams), 'reclass': sorted(RECLASS_2026),
                 'market_stretch': round(mkt_stretch, 4), 'rating_mean': round(rating_mean, 4)},
        'teams': pteams, 'fcs': pfcs, 'schedules': psched, 'market': pmarket,
    }


def build_reference():
    """Full Python-side precompute (distributions, ladders, edges) — the validation reference
    the browser JS must match. NOT embedded in the artifact."""
    D = load()
    teams, sch, fcs, n2 = D['teams'], D['schedules'], D['fcs'], D['name2nk']
    M = _market()
    pinitial = {}
    for nk, glist in sch.items():
        t = teams[nk]
        name = t['name']
        reg = glist
        conf = [g for g in glist if g['is_conf']]

        def games_for(gl, which):
            return [{'mu_opp': (g['opp']['mu_our'] if which == 'our' else g['opp']['mu_anchor']),
                     'site': g['site'], 'band_opp': g['opp']['band']} for g in gl]

        block = {'name': name, 'conf': t['conf'], 'final': t['final'], 'band': t['band'],
                 'anchor': t['anchor'], 'reclass': name in RECLASS_2026, 'reg': {}, 'conf_wins': {}}
        block['reg']['our'] = _dist_block(t['final'], t['band'], games_for(reg, 'our'))
        block['reg']['anchor'] = _dist_block(t['anchor'], t['band'], games_for(reg, 'anchor'))
        block['reg']['market'] = _market_block(M.get(name, {}).get('regular', []),
                                                block['reg']['our'], block['reg']['anchor'])
        # per-game win probs (our + anchor) for the schedule table
        pg = []
        for g in reg:
            o = g['opp']
            pg.append({'week': g['week'], 'opp': o['name'], 'kind': o['kind'], 'site': g['site'],
                       'is_conf': g['is_conf'], 'mu_our': o['mu_our'], 'mu_anchor': o['mu_anchor'],
                       'band': o['band'],
                       'p_our': E.game_win_prob(t['final'], o['mu_our'], g['site'], o['band']),
                       'p_anchor': E.game_win_prob(t['anchor'], o['mu_anchor'], g['site'], o['band'])})
        block['reg']['games'] = pg
        if conf:
            block['conf_wins']['our'] = _dist_block(t['final'], t['band'], games_for(conf, 'our'))
            block['conf_wins']['anchor'] = _dist_block(t['anchor'], t['band'], games_for(conf, 'anchor'))
            block['conf_wins']['market'] = _market_block(M.get(name, {}).get('conference', []),
                                                         block['conf_wins']['our'], block['conf_wins']['anchor'])
            block['conf_wins']['n_games'] = len(conf)
        pinitial[nk] = block
    return pinitial


if __name__ == '__main__':
    p = build_payload()
    os.makedirs('outputs', exist_ok=True)
    with open('outputs/win_totals_payload.json', 'w') as f:
        json.dump(p, f)
    sz = os.path.getsize('outputs/win_totals_payload.json') / 1024
    print(f"payload: {p['meta']['n_teams']} teams, {len(p['fcs'])} FCS, {sz:.0f} KB")
    ref = build_reference()
    for nm in ['Ohio State', 'North Dakota State', 'Massachusetts', 'Nevada']:
        nk = next(k for k, t in p['teams'].items() if t['name'] == nm)
        b = ref[nk]; r = b['reg']['our']; mk = b['reg']['market']
        best = mk['best'] if mk else None
        if best:
            print(f"{nm:<20} E[w]={r['expected_wins']:.2f} G={r['G']} mline={mk['median_line']} "
                  f"best={best['side']}{best['line']}@{best['odds']}(EV{best['ev']:+.3f})")
        else:
            print(f"{nm:<20} E[w]={r['expected_wins']:.2f} (no market)")
