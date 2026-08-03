#!/usr/bin/env python3
"""S7 re-derivation under fixed name joins (2026-08-03, owner-approved).

WHY: the S7/S8 validation machinery joined SP+ vintages (canonical norm_key)
to CFBD game names and SBD board names by bare norm(). Three FBS teams never
matched in any season — Miami-FL ('miami'), App State ('appstate'),
UL Monroe ('ulmonroe') — so (a) every game against them was priced with the
0.95 FCS constant inside exp_wins (159 games, 2021-25), and (b) their own
board rows dropped. UConn was patched ad hoc (SP_ALIAS) and was fine.

This script recomputes S7's K1/K2 headline (FINDINGS_S7_2026-07-27.md:
consensus MAE 1.783 vs market 1.821; |d|>=1 n=44 side rate 77.3%; gradient
48/49/79%) under BOTH joins from the same inputs:
  OLD  = bare norm() + SP_ALIAS, byte-faithful to s8_run_panel.py Leg 3
  NEW  = team_alias.to_nk() everywhere, 0.95 only for true non-FBS opponents
Then a like-for-like decomposition of what moved. 2025 (owner capture,
peeked per S7 doc) reported alongside, excluded from bars, DK column.
"""
import csv, json, math, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from team_alias import to_nk

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP_ALIAS = {'connecticut': 'uconn'}


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


GAMES = {y: json.load(open(f'{R}/data/cfbd/2026-07-12/games_{y}_regular.json'))
         for y in range(2021, 2026)}


def read_sp(y, mode):
    out = {}
    for r in csv.DictReader(open(f'{R}/data/backtest/sp_preseason/SP+_{y}_preseason.csv')):
        k = r['norm_key']
        out[SP_ALIAS.get(k, k) if mode == 'old' else k] = float(r['sp_plus_overall'])
    return out


def game_keys(g, mode):
    if mode == 'old':
        return norm(g['homeTeam']), norm(g['awayTeam'])
    return (to_nk(g['homeTeam']) or 'FCS:' + norm(g['homeTeam']),
            to_nk(g['awayTeam']) or 'FCS:' + norm(g['awayTeam']))


def exp_wins(tk, y, ratings, mode, audit=None):
    ew = 0.0
    for g in GAMES[y]:
        h, a = game_keys(g, mode)
        if tk not in (h, a):
            continue
        opp = a if tk == h else h
        if opp not in ratings:
            ew += 0.95
            if audit is not None:
                cls = (g.get('awayClassification') if tk == h else g.get('homeClassification'))
                audit['n095'] += 1
                if cls == 'fbs':
                    audit['fbs_at_095'][opp] = audit['fbs_at_095'].get(opp, 0) + 1
            continue
        site = 0.0 if g.get('neutralSite') else (1.0 if tk == h else -1.0)
        ew += phi((ratings[tk] - ratings[opp] + 2.3 * site) / 13.5)
    return ew


def actual_wins(tk, y, mode):
    wn = 0
    for g in GAMES[y]:
        h, a = game_keys(g, mode)
        if tk not in (h, a) or g.get('homePoints') is None:
            continue
        mine = g['homePoints'] if tk == h else g['awayPoints']
        theirs = g['awayPoints'] if tk == h else g['homePoints']
        wn += int(mine > theirs)
    return wn


def board(y):
    """(team_raw, line) rows. 2021-24 SBD; 2025 owner capture DK column."""
    out = []
    if y <= 2024:
        for r in csv.DictReader(open(f'{R}/data/win_totals/sbd_historical/sbd_{y}.csv')):
            out.append((r['team'], float(r['line'])))
    else:
        for r in csv.DictReader(open(f'{R}/data/win_totals/Win Totals from 2025.csv')):
            v = (r.get('DraftKings Win Total') or '').strip()
            if v:
                out.append((r['TEAM'], float(v.split()[0])))
    return out


def run(mode, years):
    rows, dropped, audit = [], [], {'n095': 0, 'fbs_at_095': {}}
    for y in years:
        sp = read_sp(y, mode)
        for raw, line in board(y):
            tk = (SP_ALIAS.get(norm(raw), norm(raw)) if mode == 'old' else to_nk(raw))
            if tk is None or tk not in sp:
                dropped.append((y, raw))
                continue
            rows.append(dict(year=y, team=tk, raw=raw, line=line,
                             ew=exp_wins(tk, y, sp, mode, audit),
                             wins=actual_wins(tk, y, mode)))
    return rows, dropped, audit


def report(rows, label):
    E = [r['ew'] for r in rows]; L = [r['line'] for r in rows]; W = [r['wins'] for r in rows]
    n = len(rows)
    mae_c = sum(abs(e - w) for e, w in zip(E, W)) / n
    mae_m = sum(abs(l - w) for l, w in zip(L, W)) / n
    print(f'--- {label}: n={n} | K1 consensus MAE {mae_c:.3f} vs market {mae_m:.3f} ---')
    for lo, hi, lab in ((0, 0.5, '<0.5   '), (0.5, 1.0, '0.5-1.0'), (1.0, 99, '>=1.0  ')):
        sel = [r for r in rows if lo <= abs(r['ew'] - r['line']) < hi and r['wins'] != r['line']]
        hit = sum(((r['ew'] > r['line']) == (r['wins'] > r['line'])) for r in sel)
        print(f'    |d| {lab}: n={len(sel):3d}  side {100 * hit / len(sel) if sel else float("nan"):5.1f}%')
    big = [r for r in rows if abs(r['ew'] - r['line']) >= 1.0 and r['wins'] != r['line']]
    for y in sorted({r['year'] for r in rows}):
        sel = [r for r in big if r['year'] == y]
        hit = sum(((r['ew'] > r['line']) == (r['wins'] > r['line'])) for r in sel)
        print(f'      {y}: {hit}/{len(sel)}')
    return {(r['year'], r['team']): r for r in rows}, big


BAR_YEARS = (2021, 2022, 2023, 2024)
print('================ S7 K1/K2 REJOIN — bar years 2021-24 ================')
old_rows, old_drop, old_aud = run('old', BAR_YEARS)
O, old_big = report(old_rows, 'OLD join (replication target: MAE 1.783/1.821, >=1.0 n=44 @ 77.3%)')
print(f'    dropped board rows: {len(old_drop)} {sorted(set(d[1] for d in old_drop))}')
print(f'    games priced 0.95: {old_aud["n095"]} of which vs REAL FBS opponents: '
      f'{sum(old_aud["fbs_at_095"].values())} {old_aud["fbs_at_095"]}')
new_rows, new_drop, new_aud = run('new', BAR_YEARS)
N, new_big = report(new_rows, 'NEW join (to_nk)')
print(f'    dropped board rows: {len(new_drop)} {sorted(set(d[1] for d in new_drop))}')
print(f'    games priced 0.95: {new_aud["n095"]} of which vs REAL FBS opponents: '
      f'{sum(new_aud["fbs_at_095"].values())} {new_aud["fbs_at_095"]}')

print('\n--- like-for-like decomposition ---')
common = set(O) & set(N)
d_ew = [abs(N[k]['ew'] - O[k]['ew']) for k in common]
moved = sorted((k for k in common if abs(N[k]['ew'] - O[k]['ew']) > 1e-9),
               key=lambda k: -abs(N[k]['ew'] - O[k]['ew']))
print(f'common rows {len(common)} | rows with changed EW: {len(moved)} | max |dEW| {max(d_ew):.3f}')
for k in moved[:12]:
    print(f'    {k[0]} {k[1]:20s} ew {O[k]["ew"]:5.2f} -> {N[k]["ew"]:5.2f}'
          f'  gap {O[k]["ew"] - O[k]["line"]:+5.2f} -> {N[k]["ew"] - N[k]["line"]:+5.2f}'
          f'  wins {O[k]["wins"]:2d}->{N[k]["wins"]:2d}')
ob = {k for k in common if abs(O[k]['ew'] - O[k]['line']) >= 1.0 and O[k]['wins'] != O[k]['line']}
nb = {k for k in common if abs(N[k]['ew'] - N[k]['line']) >= 1.0 and N[k]['wins'] != N[k]['line']}
print(f'left >=1.0 bucket: {sorted(ob - nb)}')
print(f'entered >=1.0 bucket: {sorted(nb - ob)}')
flip = [k for k in ob & nb if (O[k]['ew'] > O[k]['line']) != (N[k]['ew'] > N[k]['line'])]
print(f'side flips within bucket: {flip}')
rec = [k for k in N if k not in O]
print(f'recovered rows (never in old panel): {len(rec)}')
for k in sorted(rec):
    r = N[k]
    d = r['ew'] - r['line']
    res = 'push' if r['wins'] == r['line'] else ('HIT' if (d > 0) == (r['wins'] > r['line']) else 'MISS')
    print(f'    {k[0]} {k[1]:20s} line {r["line"]:4.1f} ew {r["ew"]:5.2f} gap {d:+5.2f} wins {r["wins"]:2d}'
          + (f'  [|d|>=1 {res}]' if abs(d) >= 1.0 and res != 'push' else ''))

print('\n================ 2025 (peeked, excluded from bars, DK owner capture) ================')
o25, _, _ = run('old', (2025,))
report(o25, 'OLD join 2025')
n25, d25, a25 = run('new', (2025,))
report(n25, 'NEW join 2025')
print(f'    new-join drops: {len(d25)} {sorted(set(x[1] for x in d25))[:6]}')

print('\n================ POOLED 2021-25 (>=1.0 bucket) ================')
for lab, rr in (('OLD', old_rows + o25), ('NEW', new_rows + n25)):
    sel = [r for r in rr if abs(r['ew'] - r['line']) >= 1.0 and r['wins'] != r['line']]
    hit = sum(((r['ew'] > r['line']) == (r['wins'] > r['line'])) for r in sel)
    print(f'  {lab}: {hit}/{len(sel)} = {100 * hit / len(sel):.1f}%')
