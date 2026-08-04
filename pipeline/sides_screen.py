#!/usr/bin/env python3
"""Single-game side screen + read-through onto the open win-total book.

Companion to outputs/SIDES_SCREEN_2026-08-04.md. DIAGNOSTIC ONLY — S14 flushed
consensus-disagreement sides from the 2026 program; this script does not produce bets.

err(g) = model_home_spread(HFA) - posted_home_spread = d_home - d_away,
where d_t = (market's rating of t) - (our raw rating of t).
So err > 0  =>  market rates the HOME team higher than we do  =>  our value is on the AWAY side.

Controls: HFA sign-stability (2.3 house vs 3.5 market-implied), FCS-at-FBS rows excluded,
localization + identifiability (an opponent with no other capture game leaves the pair
unidentifiable, so full attribution is an UPPER BOUND, not an estimate).
"""
import csv, json, sys
import numpy as np
sys.path.insert(0, 'pipeline')
import win_engine as E

P = json.load(open('outputs/win_totals_payload.json'))
teams = P['teams']; sched = P['schedules']; fcs = P['fcs']
N2K = {t['name']: nk for nk, t in teams.items()}
for a, b in [('Hawai’i', "Hawai'i"), ('Miami (FL)', 'Miami'),
             ('UMass', 'Massachusetts'), ('Appalachian State', 'App State')]:
    N2K[a] = N2K[b]

R = list(csv.DictReader(open('data/market/spreads_wk01_goty_2026-08-03.csv')))
G = []
for r in R:
    if r['raw'] in ('', 'None', None) or r['away'] not in N2K or r['home'] not in N2K: continue
    G.append(dict(away=N2K[r['away']], home=N2K[r['home']], site=int(float(r['site'])),
                  raw=float(r['raw']), posted=float(r['h_spread']),
                  nb=int(r['n_books']), bucket=r['bucket']))
NM = lambda nk: teams[nk]['name']

def err(g, h=3.5): return (g['raw'] - (h - 2.3) * g['site']) - g['posted']

n = {}
for g in G:
    n[g['home']] = n.get(g['home'], 0) + 1; n[g['away']] = n.get(g['away'], 0) + 1
T = sorted(n); ix = {t: i for i, t in enumerate(T)}

def ridge(lam):
    A = np.zeros((len(G), len(T))); y = np.zeros(len(G))
    for i, g in enumerate(G):
        y[i] = err(g); A[i, ix[g['home']]] += 1; A[i, ix[g['away']]] -= 1
    a = np.linalg.solve(A.T @ A + lam * np.eye(len(T)), A.T @ y)
    return {t: float(a[ix[t]]) for t in T}
R1, R3 = ridge(1.0), ridge(3.0)

def d_in(g, t): return err(g) if g['home'] == t else -err(g)   # delta implied for t by game g

def localized(t, g):
    """delta for t from game g, netting out the opponent's read from the opponent's OTHER games.
    Returns (delta, n_other_opp). n_other_opp = 0 means unidentifiable (50/50 split is all you get)."""
    opp = g['away'] if g['home'] == t else g['home']
    oth = [o for o in G if o is not g and opp in (o['home'], o['away'])]
    d_opp = np.mean([d_in(o, opp) for o in oth]) if oth else 0.0
    return d_in(g, t) + d_opp, len(oth)

# ---------------- 1. the screen ----------------
e23 = np.array([err(g, 2.3) for g in G]); e35 = np.array([err(g, 3.5) for g in G])
lines = []
W = lines.append
W(f"n(FBS-FBS, joined) {len(G)}   teams {len(T)}")
W(f"HFA 2.3  MAE {np.abs(e23).mean():.2f}  mean {e23.mean():+.2f}  sd {e23.std(ddof=1):.2f}")
W(f"HFA 3.5  MAE {np.abs(e35).mean():.2f}  mean {e35.mean():+.2f}  sd {e35.std(ddof=1):.2f}")

stable, flipped = [], []
for g in G:
    a, b = err(g, 2.3), err(g, 3.5)
    (flipped if a * b <= 0 else stable).append((g, a if abs(a) < abs(b) else b))
stable.sort(key=lambda x: -abs(x[1]))
W(f"sign-stable {len(stable)}  HFA-flipped(dropped) {len(flipped)}")

screen = []
for g, c in stable:
    vs = g['away'] if c > 0 else g['home']
    dl, no = localized(vs, g)
    screen.append(dict(away=NM(g['away']), home=NM(g['home']), bucket=g['bucket'], books=g['nb'],
                       posted=g['posted'], ours=round(g['raw'] - 1.2 * g['site'], 2),
                       edge=round(abs(c), 2), value_side=NM(vs),
                       value_number=round(g['posted'] if vs == g['home'] else -g['posted'], 1),
                       team_read=round(-dl, 2) if vs else None, opp_other_games=no,
                       identified=('yes' if no >= 2 else ('partial' if no == 1 else 'no'))))

# ---------------- 2. team-level reads that replicate ----------------
rep = []
for t in T:
    if n[t] < 2: continue
    ds = [d_in(g, t) for g in [x for x in G if t in (x['home'], x['away'])]]
    rep.append((t, np.mean(ds), np.std(ds, ddof=1) if len(ds) > 1 else None, len(ds),
                all(d > 0 for d in ds) or all(d < 0 for d in ds)))
rep.sort(key=lambda x: -abs(x[1]))

# ---------------- 3. read-through onto the open book ----------------
def oppR(r): return teams[r]['calibrated'] if r in teams else fcs[r]['rating']
def oppB(r): return teams[r]['band'] if r in teams else fcs[r]['band']
def glist(nk, conf): return [{'mu_opp': oppR(g['opp_ref']), 'site': g['site'], 'band_opp': oppB(g['opp_ref'])}
                             for g in sched[nk] if (g['is_conf'] or not conf)]
def wt_delta(nk, line, fair_over, conf):
    gl = glist(nk, conf); lo, hi = -18., 18.
    for _ in range(70):
        mid = (lo + hi) / 2
        d = E.win_distribution(teams[nk]['calibrated'] + 0.75 * mid, teams[nk]['band'], gl)['dist']
        if sum(d[int(line) + 1:]) > fair_over: hi = mid
        else: lo = mid
    return lo
def p_at(nk, line, side, conf, draw):
    d = E.win_distribution(teams[nk]['calibrated'] + 0.75 * draw, teams[nk]['band'], glist(nk, conf))['dist']
    po = sum(d[int(line) + 1:]); return po if side == 'over' else 1 - po

held = {}
for r in csv.DictReader(open('outputs/bet_tracker.csv')):
    if r['result'] != 'pending' or r['category'] == 'prop': continue
    k = (r['team'], r['category'], r['side'], float(r['line']))
    held.setdefault(k, [0.0, float(r['our_p']), float(r['pct_edge'].strip('%+')) / 100])
    held[k][0] += float(r['stake_u'])

book = []
for (tm, cat, side, line), (stk, p, edge) in sorted(held.items(), key=lambda x: -x[1][0]):
    nk = N2K[tm]; conf = (cat == 'conference')
    fair_over = (p - edge) if side == 'over' else 1 - (p - edge)
    wd = wt_delta(nk, line, fair_over, conf)
    gs = [g for g in G if nk in (g['home'], g['away'])]
    if gs:
        locs = [localized(nk, g) for g in gs]
        dloc = float(np.mean([l for l, _ in locs])); nopp = max(o for _, o in locs)
        # split attribution: when the opponent has no other game the pair is unidentifiable,
        # so the honest point estimate is half the gap, and dloc is only an upper bound.
        dsp = float(np.mean([(l if o else d_in(g2, nk) / 2.0) for (l, o), g2 in zip(locs, gs)]))
        pr = p_at(nk, line, side, conf, dloc); prs = p_at(nk, line, side, conf, dsp)
        hurt = (dsp < 0) if side == 'over' else (dsp > 0)
        ratio = dsp / wd if abs(wd) > 0.5 else None
    else:
        dloc = dsp = nopp = pr = prs = ratio = None; hurt = None
    book.append(dict(team=tm, cat=cat, side=side, line=line, stake=round(stk, 2), our_p=p,
                     wt_delta=round(wd, 2), n_games=len(gs), opp_other=nopp,
                     spread_delta=round(dloc, 2) if dloc is not None else None,
                     spread_delta_split=round(dsp, 2) if dloc is not None else None,
                     p_reprice_split=round(prs, 4) if dloc is not None else None,
                     move_split=round((prs - p) * 100, 1) if dloc is not None else None,
                     ridge_l1=round(R1[nk], 2) if nk in R1 else None,
                     p_reprice=round(pr, 4) if pr is not None else None,
                     move=round((pr - p) * 100, 1) if pr is not None else None,
                     confirm_ratio=round(ratio, 2) if ratio is not None else None,
                     direction=(None if hurt is None else ('against' if hurt else 'supports'))))

json.dump(dict(screen=screen, book=book,
               replicating=[dict(team=NM(t), mean=round(m, 2), sd=(round(s, 2) if s else None),
                                 n=k, consistent=c) for t, m, s, k, c in rep]),
          open('/tmp/final.json', 'w'), indent=1)

print('\n'.join(lines))
print("\n== TOP SIGN-STABLE DISAGREEMENTS ==")
print(f"{'game':40s}{'bk':>3s}{'posted':>8s}{'ours':>7s}{'edge':>6s}  {'value side':26s}{'oppG':>5s} ident")
for s in screen[:20]:
    print(f"{s['away']+' @ '+s['home']:40s}{s['books']:3d}{s['posted']:+8.1f}{s['ours']:+7.1f}{s['edge']:6.2f}  "
          f"{s['value_side']+' '+format(s['value_number'],'+.1f'):26s}{s['opp_other_games']:5d} {s['identified']}")

print("\n== TEAM READS THAT REPLICATE ACROSS >1 CAPTURE GAME (+ = market rates HIGHER than us) ==")
for t, m, s, k, c in rep[:16]:
    print(f"  {NM(t):22s} mean {m:+5.2f}  sd {('%.2f'%s):>5s}  n={k}  sign-consistent={c}")

print("\n== READ-THROUGH ONTO THE OPEN BOOK ==")
print(f"{'position':30s}{'stk':>5s}{'WTd':>7s}{'SPD_up':>7s}{'SPD_sp':>7s}{'oppG':>5s}{'p_now':>7s}{'p_split':>8s}{'move':>6s}{'r':>6s}  dir")
for b in book:
    f = lambda v, w=7, p=2: (f"{v:+{w}.{p}f}" if v is not None else ' ' * (w - 2) + '--')
    ps = format(b['p_reprice_split'] * 100, '7.1f') + '%' if b['p_reprice_split'] else '      --'
    lbl = b['team'] + ' ' + b['side'] + ' ' + str(b['line']) + ('c' if b['cat'] == 'conference' else '')
    print(f"{lbl:30s}"
          f"{b['stake']:5.2f}{f(b['wt_delta'])}{f(b['spread_delta'])}{f(b['spread_delta_split'])}"
          f"{(b['opp_other'] if b['opp_other'] is not None else 0):5d}"
          f"{b['our_p']*100:6.1f}%{ps}"
          f"{f(b['move_split'],6,1)}{f(b['confirm_ratio'],6)}  {b['direction'] or '--'}")

import csv as _c
with open('outputs/sides_screen_2026-08-04.csv','w',newline='') as fh:
    w=_c.DictWriter(fh, fieldnames=list(screen[0].keys())); w.writeheader(); w.writerows(screen)
with open('outputs/sides_book_read_2026-08-04.csv','w',newline='') as fh:
    w=_c.DictWriter(fh, fieldnames=list(book[0].keys())); w.writeheader(); w.writerows(book)
print('\nwrote outputs/sides_screen_2026-08-04.csv (%d rows), outputs/sides_book_read_2026-08-04.csv (%d rows)'%(len(screen),len(book)))
