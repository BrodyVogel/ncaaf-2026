#!/usr/bin/env python3
"""Weekend board scan (2026-07-31): full-field pass under the committed
completion-screen rules + add-candidates on held teams. Lines = last-known
capture in the payload (STALE — final qualification needs owner's fresh prices).
Unders priced via the 30-cent inference unless a real two-way exists."""
import csv, json, math, os, re, sys, unicodedata
import numpy as np

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(R)
sys.path.insert(0, 'pipeline')
import win_engine as E


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


P = json.load(open('outputs/win_totals_payload.json'))
teams, sched, M, fcs = P['teams'], P['schedules'], P['market'], P['fcs']

HELD = {'uconn': 1.07, 'tulsa': 1.10, 'oregonstate': 0.65, 'bowlinggreen': 1.05,
        'liberty': 0.60, 'arizonastate': 0.95, 'kennesawstate': 0.55, 'illinois': 0.65,
        'westvirginia': 0.50, 'eastcarolina': 0.55, 'hawaii': 0.60, 'florida': 0.90,
        'ucf': 0.55, 'pittsburgh': 0.65, 'wisconsin': 0.60, 'buffalo': 0.75,
        'nevada': 0.75, 'wakeforest': 0.90, 'rutgers': 0.80}
HELD_SIDE = {'uconn': 'over', 'tulsa': 'over', 'oregonstate': 'over', 'bowlinggreen': 'over',
             'liberty': 'under', 'arizonastate': 'under', 'kennesawstate': 'over',
             'illinois': 'under', 'westvirginia': 'under', 'eastcarolina': 'over',
             'hawaii': 'under', 'florida': 'under', 'ucf': 'over', 'pittsburgh': 'under',
             'wisconsin': 'under', 'buffalo': 'over', 'nevada': 'over', 'wakeforest': 'over',
             'rutgers': 'over'}
LOUD = {'charlotte': 14.1, 'miamioh': -12.2, 'samhouston': 11.0, 'ulmonroe': 10.5,
        'ohio': -10.2, 'jamesmadison': -10.0, 'jacksonvillestate': -9.9, 'navy': -9.6,
        'northwestern': 9.4, 'liberty': -9.4, 'unlv': -9.3, 'rutgers': 9.2,
        'troy': -9.1, 'kennesawstate': -9.0}
OVR = {norm(r['team']) for r in csv.DictReader(open('data/manual_overrides_2026.csv'))}

tm = {r['norm_key']: norm(r['cfbd_school'])
      for r in csv.DictReader(open('data/anchors/team_name_map.csv'))}
sp = {}
for r in csv.DictReader(open('data/anchors/SP+_2026preseason_2026-07-12.csv')):
    k = tm.get(r['norm_key'], r['norm_key'])
    sp[{'connecticut': 'uconn'}.get(k, k)] = float(r['sp_plus_overall'])
q1, q2 = np.quantile(list(sp.values()), [1 / 3, 2 / 3])

games = json.load(open('data/cfbd/2026-07-12/games_2026_regular.json'))


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def sp_exp(tk):
    ew = 0.0
    for g in games:
        h, a = norm(g['homeTeam']), norm(g['awayTeam'])
        if tk not in (h, a):
            continue
        opp = a if tk == h else h
        if opp not in sp:
            ew += 0.95
            continue
        site = 0.0 if g.get('neutralSite') else (1.0 if tk == h else -1.0)
        ew += phi((sp[tk] - sp[opp] + 2.3 * site) / 13.5)
    return ew


def under_odds(o):
    if o <= -130:
        return abs(o) - 30
    if o < 0:
        return -(230 - abs(o))
    return -(o + 30)


def be(o):
    return (abs(o) / (abs(o) + 100)) if o < 0 else (100 / (o + 100))


def oppR(ref, lens):
    if ref in teams:
        return teams[ref][lens]
    return fcs[ref]['rating'] * 0.75


def p_over(nk, line, lens):
    gl = [{'mu_opp': oppR(g['opp_ref'], lens), 'site': g['site'],
           'band_opp': (teams[g['opp_ref']]['band'] if g['opp_ref'] in teams else fcs[g['opp_ref']]['band'])}
          for g in sched[nk]]
    d = E.win_distribution(teams[nk][lens], teams[nk]['band'], gl)['dist']
    return sum(d[math.floor(line) + 1:])


# QB-battle flag from grades
qbL = {}
import glob
for p in glob.glob('snapshots/*/grades.json'):
    g = json.load(open(p)); mt = json.load(open(p.replace('grades.json', 'META.json')))
    qbL[norm(mt['team'])] = g['units'].get('QB', {}).get('confidence') == 'L'

rows = []
for nk, t in teams.items():
    mk = M.get(nk, {}).get('regular', [])
    if not mk or t.get('reclass'):
        continue
    spx = sp.get(nk)
    tot_gap_base = sp_exp(nk) if spx is not None else None
    for side in ('over', 'under'):
        best = None
        for line, o_odds, book in mk:
            odds = o_odds if side == 'over' else under_odds(o_odds)
            pc = p_over(nk, line, 'calibrated')
            pm = p_over(nk, line, 'market_matched')
            if side == 'under':
                pc, pm = 1 - pc, 1 - pm
            edge_min = min(pc, pm) - be(odds)
            edge_cal = pc - be(odds)
            if best is None or edge_min > best[0]:
                best = (edge_min, edge_cal, line, odds, book, pc, pm)
        if best is None:
            continue
        edge_min, edge_cal, line, odds, book, pc, pm = best
        gap = None if tot_gap_base is None else (tot_gap_base - line) * (1 if side == 'over' else -1)
        terc = None if spx is None else (0 if spx < q1 else (1 if spx < q2 else 2))
        rows.append(dict(nk=nk, name=t['name'], side=side, line=line, odds=int(odds), book=book,
                         edge_min=edge_min, edge_cal=edge_cal, gap=gap, terc=terc,
                         loud=LOUD.get(nk, 0.0), qbL=qbL.get(nk, False),
                         held=HELD.get(nk, 0.0), held_side=HELD_SIDE.get(nk),
                         ovr=nk in OVR))


def fmt(r, extra=''):
    return (f"{r['name']:16s} {r['side'][0].upper()}{r['line']:4.1f} {r['odds']:+5d} {r['book']:4s} "
            f"minE {r['edge_min']*100:+5.1f}% calE {r['edge_cal']*100:+5.1f}% gap {r['gap']:+.2f} "
            f"terc {r['terc']} loud {r['loud']:+5.1f}{' QBL' if r['qbL'] else ''}{extra}")


print('===== A. ADDS on held teams (same side, min-lens >=4%, room under 1.1u cap) =====')
for r in sorted(rows, key=lambda x: -x['edge_min']):
    if r['held'] and r['side'] == r['held_side'] and r['edge_min'] >= 0.04 and r['held'] < 1.05:
        print(fmt(r, f"  held {r['held']:.2f}u room {1.1 - r['held']:.2f}"))

print('\n===== B. F1 pure-consensus (gap >= 1.0, min-lens >= 4%, not held, no overrides) =====')
for r in sorted(rows, key=lambda x: -(x['gap'] or -9)):
    if not r['held'] and not r['ovr'] and r['gap'] is not None and r['gap'] >= 1.0 and r['edge_min'] >= 0.04:
        print(fmt(r))

print('\n===== C. MACRO sleeve (O<=5.5 / U>=8.0, gap >= 0.75, cal-lens >= 2.5%, exclusions) =====')
for r in sorted(rows, key=lambda x: -(x['gap'] or -9)):
    if r['held'] or r['ovr'] or r['gap'] is None or r['gap'] < 0.75 or r['edge_cal'] < 0.025:
        continue
    if r['side'] == 'over' and r['line'] <= 5.5:
        if r['terc'] == 1 and r['qbL']:
            print(fmt(r, '  EXCLUDED mid-band disruption over'))
        else:
            print(fmt(r))
    elif r['side'] == 'under' and r['line'] >= 8.0:
        print(fmt(r))

print('\n===== D. Near-miss / watch (loud-arm side agreement but below a bar) =====')
for r in sorted(rows, key=lambda x: -abs(x['loud'])):
    agree = (r['loud'] > 8.9 and r['side'] == 'over') or (r['loud'] < -8.9 and r['side'] == 'under')
    if agree and not r['held'] and (r['edge_min'] < 0.04 or (r['gap'] or 0) < 1.0):
        print(fmt(r))
