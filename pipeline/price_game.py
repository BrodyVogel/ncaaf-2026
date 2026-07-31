#!/usr/bin/env python3
"""Single-game pricer (2026): our implied spread for any matchup.

Usage: price_game.py HOME AWAY [--neutral] [--market H_SPREAD]
  --market takes the HOME spread as books quote it (home -3.5 => -3.5).

Doctrine banner (S14, 2026-07-31): consensus-vs-market disagreement is NOT a
licensed qualifying signal for sides — both S14 legs failed. This tool is for
context, paper-tracking, and totals-related work, not side qualification.
"""
import argparse, csv, os, re, sys, unicodedata

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HFA = 2.3


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', s.lower())


def load():
    R = {}
    for r in csv.DictReader(open('outputs/final_pass/ASSEMBLY.csv')):
        anchor, final = float(r['anchor_blend']), float(r['final'])
        R[norm(r['team'])] = dict(team=r['team'], final=final, anchor=anchor,
                                  cal=anchor + 0.75 * (final - anchor), fcs=False)
    if os.path.exists('data/fcs_ratings_2026.csv'):
        for r in csv.DictReader(open('data/fcs_ratings_2026.csv')):
            k = norm(r.get('team') or r.get('team_name') or '')
            v = next((float(r[c]) for c in ('rating', 'sp_equiv', 'rating_sp_scale') if c in r and r[c]), None)
            if k and v is not None and k not in R:
                R[k] = dict(team=(r.get('team') or r.get('team_name')) + ' (FCS)',
                            final=v, anchor=v, cal=v, fcs=True)
    return R


def find(R, q):
    k = norm(q)
    if k in R:
        return R[k]
    hits = [v for kk, v in R.items() if k in kk or kk in k]
    if len(hits) == 1:
        return hits[0]
    sys.exit(f"team '{q}' not found" + (f" (ambiguous: {[h['team'] for h in hits][:6]})" if hits else ''))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('home'); ap.add_argument('away')
    ap.add_argument('--neutral', action='store_true')
    ap.add_argument('--market', type=float, default=None)
    a = ap.parse_args()
    R = load()
    h, w = find(R, a.home), find(R, a.away)
    site = 0.0 if a.neutral else HFA
    for lens in ('cal', 'final', 'anchor'):
        m = h[lens] - w[lens] + site
        lab = {'cal': 'calibrated (board lens)', 'final': 'raw final', 'anchor': 'consensus anchor'}[lens]
        line = f'{h["team"]} {-m:+.1f}' if m > 0 else f'{w["team"]} {m:+.1f}'
        extra = ''
        if a.market is not None and lens == 'cal':
            D = m + a.market
            extra = f'   | market {h["team"]} {a.market:+.1f} -> D={D:+.1f} ({"home" if D > 0 else "away"} side vs number)'
        print(f'{lab:24s}: {h["team"]} by {m:+.1f}  ({line}){extra}')
    print('\n[S14 doctrine: no side qualifies on model-vs-market disagreement; paper-track only.]')
