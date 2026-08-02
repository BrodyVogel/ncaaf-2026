#!/usr/bin/env python3
"""Portfolio screen 2026-08-02: committed rules + Amendments 1 (rp) + 2 (F5)
on the post-D1-D5/B4/FCS-rerate board. Lines = 07-19 capture (STALE — final
qualification needs owner's fresh prices). D4 raw-FCS convention."""
import csv, glob, json, math, os, re, sys, unicodedata
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
OVR = {norm(r['team']) for r in csv.DictReader(open('data/manual_overrides_2026.csv'))}
# current loud arm from ASSEMBLY (post D1-D5/B4)
resid = {}
name_of = {}
for r in csv.DictReader(open('outputs/final_pass/ASSEMBLY.csv')):
    resid[norm(r['team'])] = float(r['residual'])
    name_of[norm(r['team'])] = r['team']
loud_thr = np.quantile([abs(v) for v in resid.values()], 0.9)
# rp proxy + Q table
rp = {r['nk']: float(r['ret_share']) for r in csv.DictReader(open('data/research/s13_rp2026_proxy.csv'))}
rp_vals = sorted(rp.values())
Qtab = {r['team']: (float(r['Q']), int(r['N']), int(r['clust_max'])) for r in csv.DictReader(open('data/research/s18_fcs2026.csv'))}
Qs = sorted(q for q, _, _ in Qtab.values())
q_top = np.quantile(Qs, 0.75)
tm_map = {r['norm_key']: norm(r['cfbd_school']) for r in csv.DictReader(open('data/anchors/team_name_map.csv'))}
sp = {}
for r in csv.DictReader(open('data/anchors/SP+_2026preseason_2026-07-12.csv')):
    k = tm_map.get(r['norm_key'], r['norm_key'])
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
    return teams[ref][lens] if ref in teams else fcs[ref]['rating']   # D4: raw FCS


def p_over(nk, line, lens):
    gl = [{'mu_opp': oppR(g['opp_ref'], lens), 'site': g['site'],
           'band_opp': (teams[g['opp_ref']]['band'] if g['opp_ref'] in teams else fcs[g['opp_ref']]['band'])}
          for g in sched[nk]]
    d = E.win_distribution(teams[nk][lens], teams[nk]['band'], gl)['dist']
    return sum(d[math.floor(line) + 1:])


qbL = {}
for p in glob.glob('snapshots/*/grades.json'):
    g = json.load(open(p)); mt = json.load(open(p.replace('grades.json', 'META.json')))
    qbL[norm(mt['team'])] = g['units'].get('QB', {}).get('confidence') == 'L'

rows = []
for nk, t in teams.items():
    mk = M.get(nk, {}).get('regular', [])
    if not mk or t.get('reclass'):
        continue
    spx = sp.get(nk)
    ew = sp_exp(nk) if spx is not None else None
    for side in ('over', 'under'):
        best = None
        for line, o_odds, book in mk:
            odds = o_odds if side == 'over' else under_odds(o_odds)
            pc = p_over(nk, line, 'calibrated'); pm = p_over(nk, line, 'market_matched')
            if side == 'under':
                pc, pm = 1 - pc, 1 - pm
            em = min(pc, pm) - be(odds); ec = pc - be(odds)
            if best is None or em > best[0]:
                best = (em, ec, line, odds, book)
        if best is None:
            continue
        em, ec, line, odds, book = best
        gap = None if ew is None else (ew - line) * (1 if side == 'over' else -1)
        terc = None if spx is None else (0 if spx < q1 else (1 if spx < q2 else 2))
        rpv = rp.get(nk)
        rp_pct = (np.searchsorted(rp_vals, rpv) / len(rp_vals)) if rpv is not None else None
        Q, Nq, cl = Qtab.get(nk, (0.0, 0, 0))
        rd = resid.get(nk, 0.0)
        rows.append(dict(nk=nk, name=t['name'], side=side, line=line, odds=int(odds), book=book,
                         em=em, ec=ec, gap=gap, terc=terc, rp=rp_pct, Q=Q, Nq=Nq, cl=cl,
                         loud=(abs(rd) >= loud_thr), rdir=('over' if rd > 0 else 'under'),
                         rd=rd, qbL=qbL.get(nk, False),
                         held=HELD.get(nk, 0.0), hside=HELD_SIDE.get(nk), ovr=nk in OVR))


def tags(r):
    out = []
    if r['gap'] is not None and r['gap'] >= 1.0 and r['ec'] >= 0.04:
        out.append('F1')
    if r['side'] == 'over' and r['line'] <= 5.5 and (r['gap'] or 0) >= 0.75:
        out.append('F2o')
    if r['side'] == 'under' and r['line'] >= 8.0 and (r['gap'] or 0) >= 0.75:
        out.append('F2u')
    if r['rp'] is not None and ((r['side'] == 'over' and r['rp'] >= 0.67) or (r['side'] == 'under' and r['rp'] <= 0.33)):
        out.append('F3')
    if r['side'] == 'over' and r['Q'] >= q_top:
        out.append('F5' + ('*' if r['cl'] >= 3 else ''))
    if r['loud'] and r['rdir'] == r['side']:
        out.append('ARM')
    return out


def excluded(r):
    if r['ovr']:
        return 'override-priced'
    if r['side'] == 'over' and r['terc'] == 1 and (r['qbL'] or (r['rp'] is not None and r['rp'] < 0.33)):
        return 'mid-band disruption over'
    return None


def fmt(r):
    tg = ','.join(tags(r)) or '-'
    return (f"{r['name']:16s} {r['side'][0].upper()}{r['line']:4.1f} {r['odds']:+5d} {r['book']:5s} "
            f"minE {100*r['em']:+5.1f}% calE {100*r['ec']:+5.1f}% gap {(r['gap'] if r['gap'] is not None else 0):+.2f} "
            f"[{tg}]{' EXCL:' + excluded(r) if excluded(r) else ''}")


print('===== A. HELD BOOK (current state, factor tags) =====')
for r in sorted([x for x in rows if x['held'] and x['side'] == x['hside']], key=lambda x: -x['ec']):
    print(f"  {fmt(r)}  staked {r['held']:.2f}u")

print('\n===== B. ADDS on held (same side, min-lens >=4%, room to 1.1u) =====')
for r in sorted([x for x in rows if x['held'] and x['side'] == x['hside'] and x['em'] >= 0.04 and x['held'] < 1.05 and not excluded(x)], key=lambda x: -x['em']):
    print(f"  {fmt(r)}  room {1.1 - r['held']:.2f}u")

print('\n===== C. NEW F1 legs (gap>=1.0, calE>=4%, not held, not excluded) =====')
for r in sorted([x for x in rows if not x['held'] and x['gap'] is not None and x['gap'] >= 1.0 and x['ec'] >= 0.04 and not excluded(x)], key=lambda x: -x['gap']):
    print(f"  {fmt(r)}")

print('\n===== D. NEW MACRO sleeve (rules: O<=5.5 gap>=0.75 calE>=2.5%; U>=8.0 secondary) =====')
cands = [x for x in rows if not x['held'] and not excluded(x) and x['ec'] >= 0.025 and x['gap'] is not None and x['gap'] >= 0.75
         and ((x['side'] == 'over' and x['line'] <= 5.5) or (x['side'] == 'under' and x['line'] >= 8.0))]
for r in sorted(cands, key=lambda x: -(x['gap'] + (0.25 if 'F3' in tags(x) else 0) + (0.25 if 'F5' in ','.join(tags(x)) else 0))):
    pri = r['gap'] >= 1.0
    nudge = ('F3' in tags(r)) or ('F5' in ','.join(tags(r)))
    size = 0.25 if (pri and nudge) else (0.25 if pri else (0.20 if nudge else 0.15))
    print(f"  {fmt(r)}  -> {size:.2f}u{' PRIORITY' if pri else ''}")

print('\n===== E. EXCLUDED but notable (would qualify; rule blocks) =====')
for r in sorted([x for x in rows if not x['held'] and excluded(x) and x['ec'] >= 0.04 and (x['gap'] or 0) >= 0.75], key=lambda x: -x['ec'])[:8]:
    print(f"  {fmt(r)}")

print('\n===== F. WATCH (loud arm AGAINST a would-be leg, or near-miss gap 0.5-0.75) =====')
for r in sorted([x for x in rows if not x['held'] and not excluded(x) and x['ec'] >= 0.03 and x['gap'] is not None and 0.5 <= x['gap'] < 0.75], key=lambda x: -x['ec'])[:10]:
    print(f"  {fmt(r)}")
