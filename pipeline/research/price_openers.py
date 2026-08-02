#!/usr/bin/env python3
"""Price posted Week 0/1/GOTY spreads under the S5-validated identity translation.
fair = final_diff + 2.3*site; cover probs sigma=16.09 with push handling; two lenses:
honest (b=1, h=2.3) and market-discount (b=0.895, h=3.16); conviction = min-lens,
proposed bar +4%. |fair|>35 flagged EXTRAP (outside fitted support). Fresh CFBD pulls
expected in /tmp: lines2026.json + g2026w{1,2}.json. See FINDINGS_S5_2026-07-27.md.
Betting gated on owner sign-off (identity-ship, bar, caps, real juice, freshness)."""
import json, math, re, unicodedata, statistics as st

def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())

P = json.load(open('outputs/win_totals_payload.json'))
name2 = {}
for nk, t in P['teams'].items():
    name2[norm(t['name'])] = t; name2[nk] = t

def team(nm):
    k = norm(nm)
    if k in name2: return name2[k]
    for nk in P['teams']:
        if k in nk or nk in k: return P['teams'][nk]
    return None

neutral = {}
for f in ('/tmp/g2026w1.json', '/tmp/g2026w2.json'):
    for g in json.load(open(f)):
        neutral[(norm(g['homeTeam']), norm(g['awayTeam']))] = bool(g['neutralSite'])

SIG = 16.09            # S5 opener residual SD (not the engine's 13.5)
B_MKT, H_MKT = 0.895, 3.16   # market-discount lens (S5 report leg)
SUPPORT = 35.0
BOOK = {'UConn', 'Tulsa', 'Oregon State', 'Bowling Green', 'Liberty', 'Arizona State',
        'Kennesaw State', 'Illinois', 'West Virginia', 'East Carolina', "Hawai'i",
        'Florida', 'UCF', 'Pittsburgh', 'Nevada', 'Wake Forest', 'Buffalo', 'Rutgers',
        'Wisconsin'}

def phi(z): return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def cover(fair, s, side):
    """P(win | no push) for a side at home-spread s (negative = home favored)."""
    x = -s - fair
    if abs(s - round(s)) > 1e-9:
        pw = 1 - phi(x / SIG); pp = 0.0
    else:
        pw = 1 - phi((x + 0.5) / SIG)
        pp = phi((x + 0.5) / SIG) - phi((x - 0.5) / SIG)
    ph = pw / (1 - pp) if pp < 1 else 0.5
    return ph if side == 'home' else 1 - ph

rows = []
for g in json.load(open('data/cfbd/lines/lines_2026_probe_2026-07-31.json')):
    if not g['lines']: continue
    th, ta = team(g['homeTeam']), team(g['awayTeam'])
    if th is None or ta is None: continue
    nflag = neutral.get((norm(g['homeTeam']), norm(g['awayTeam'])), False)
    site = 0.0 if nflag else 1.0
    diff = th['final'] - ta['final']
    fair1 = diff + 2.3 * site
    fair2 = B_MKT * diff + H_MKT * site
    spreads = [l['spread'] for l in g['lines'] if l.get('spread') is not None]
    if not spreads: continue
    cons = st.median(spreads)
    best = {'home': max(spreads), 'away': min(spreads)}
    brk = 110 / 210    # assumed -110 both sides until real juice supplied
    out = {}
    for side in ('home', 'away'):
        s = best[side]
        out[side] = (s, cover(fair1, s, side) - brk, cover(fair2, s, side) - brk)
    side = max(out, key=lambda k: min(out[k][1], out[k][2]))
    s, e1, e2 = out[side]
    own = s if side == 'home' else -s
    nm = (th if side == 'home' else ta)['name']
    opp = (ta if side == 'home' else th)['name']
    rows.append(dict(wk=g['week'],
                     label=f"{nm} {'+' if own > 0 else ''}{own:g} {'v' if side == 'home' else '@'} {opp}{' (N)' if nflag else ''}",
                     fair=fair1, cons=cons, e1=e1, e2=e2, mn=min(e1, e2),
                     extrap=abs(fair1) > SUPPORT,
                     port=(th['name'] in BOOK) or (ta['name'] in BOOK)))

rows.sort(key=lambda r: -r['mn'])
print(f"{'side @ best number (own spread)':44s} {'fair(hm)':>8s} {'cons':>6s} {'honest':>7s} {'mkt':>6s} {'MIN':>6s}")
for r in rows:
    if r['mn'] < 0.02: continue
    tag = ' ✓✓' if r['mn'] >= 0.04 else '  ~'
    ex = ' [EXTRAP]' if r['extrap'] else ''
    pt = ' [BOOK]' if r['port'] else ''
    print(f"wk{r['wk']} {r['label']:42s} {r['fair']:+7.1f} {r['cons']:+6.1f} "
          f"{100 * r['e1']:+6.1f} {100 * r['e2']:+5.1f} {100 * r['mn']:+6.1f}{tag}{ex}{pt}")
print(f"\n{sum(1 for r in rows if r['mn'] >= 0.04 and not r['extrap'])} inside-support ✓✓ | "
      f"{sum(1 for r in rows if r['extrap'] and r['mn'] >= 0.04)} extrapolation-zone ✓✓ (info only)")
