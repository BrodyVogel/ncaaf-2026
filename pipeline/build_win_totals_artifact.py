#!/usr/bin/env python3
"""Generate the self-contained win-totals artifact (single HTML file).

Pipeline: win_totals_compute.build_payload()  ->  embed {payload, engine JS, UI JS, CSS}
into one HTML document. Re-run any time ratings / market / engine change; the output is fully
regenerable (owner's requirement: "not a one-off build").

    python3 pipeline/build_win_totals_artifact.py
    -> outputs/win_totals_2026.html
"""
import os, sys, json, csv, re
sys.path.insert(0, os.path.dirname(__file__))
from win_totals_compute import build_payload

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Display-name -> canonical-name aliases needed to join the market captures. FBS side maps into
# payload['teams'] (by name, then to nk); FCS side maps into payload['fcs'] (keyed by name).
# Same four FBS aliases as pipeline/sides_screen.py. NEVER join on a display name without these.
FBS_ALIASES = [('Hawai’i', "Hawai'i"), ('Miami (FL)', 'Miami'),
               ('UMass', 'Massachusetts'), ('Appalachian State', 'App State')]
FCS_ALIASES = {'University at Albany': 'UAlbany', 'LIU': 'Long Island University',
               'Nicholls State': 'Nicholls', 'Southeastern Louisiana': 'SE Louisiana'}

SPREADS_CSV = os.path.join(ROOT, 'data', 'market', 'spreads_wk01_goty_2026-08-03.csv')
TRACKER_CSV = os.path.join(ROOT, 'outputs', 'bet_tracker.csv')
DD_DIR = os.path.join(ROOT, 'docs', 'research', 'deep_dives')

# The raw lens = the spread market's own scale (calibration study: slope 1.02, corr 0.978).
# In the 2026-08-03 capture, market_matched was built as 1.15x the raw lens, so raw_scale is
# pinned to market_stretch/1.15; check_spread_lenses() verifies that live recompute still
# reproduces the stored capture columns, and warns if the ratings have drifted underneath them.
MM_OVER_RAW = 1.15
# HFA the spread market implies (house constant is meta.hfa = 2.3). Edges must be sign-stable
# across both before they are even looked at -- see docs SIDES_SCREEN_2026-08-04.md.
HFA_MARKET = 3.5

# Player-prop rows in the tracker are labelled "Name (ABBR) market"; map ABBR -> payload nk so
# the page can deep-link into the Team tab.
PROP_TEAM_NK = {'OSU': 'ohiostate', 'OKST': 'oklahomastate', 'ORE': 'oregon',
                'UGA': 'georgia', 'TEX': 'texas'}
NOTE_MARKERS = ['KILL', 'REVERSE', 'CORR', 'CLV', 'Provenance']


def build_name_maps(payload):
    teams, fcs = payload['teams'], payload['fcs']
    n2k = {t['name']: nk for nk, t in teams.items()}
    for a, b in FBS_ALIASES:
        n2k[a] = n2k[b]
    return n2k, fcs


def load_games(payload):
    """Posted single-game lines -> payload['games'].

    Carries MARKET data only (posted spread, total, book, book count, site). The model side of
    every row is recomputed live in the browser off the current rating state, so editing a
    rating or HFA moves every disagreement instantly. All 117 captured rows are carried; rows
    with an FCS participant are tagged and excluded from the aggregates (FCS-at-FBS error is
    ~+9 pts in every lens -- it measures our FCS tier, not the FBS host)."""
    n2k, fcs = build_name_maps(payload)

    def resolve(nm):
        if nm in n2k:
            return n2k[nm], 'fbs'
        alt = FCS_ALIASES.get(nm, nm)
        if alt in fcs:
            return alt, 'fcs'
        return None, 'none'

    def num(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    rows = []
    for r in csv.DictReader(open(SPREADS_CSV)):
        aref, akind = resolve(r['away'])
        href, hkind = resolve(r['home'])
        tier = 'fbs' if akind == 'fbs' and hkind == 'fbs' else ('none' if 'none' in (akind, hkind) else 'fcs')
        rows.append(dict(bucket=r['bucket'], away=r['away'], home=r['home'],
                         aref=aref, href=href, akind=akind, hkind=hkind, tier=tier,
                         site=int(float(r['site'])), assumed=(r['site_src'] == 'assumed-home'),
                         posted=num(r['h_spread']), total=num(r['total']),
                         book=r['sp_book'], nb=int(r['n_books']),
                         cap_raw=num(r['raw'])))
    return rows


def check_spread_lenses(payload, games):
    """Build-time guard: recompute the capture's `raw` column from the CURRENT payload ratings
    and report the worst deviation. Large numbers mean the ratings have moved since the
    2026-08-03 capture -- the page is still right (it recomputes live) but the stored column,
    and anything quoting it, is stale."""
    teams, fcs = payload['teams'], payload['fcs']
    m, scale = payload['meta']['rating_mean'], payload['meta']['raw_scale']

    def rate(ref, kind):
        if kind == 'fbs':
            return m + scale * (teams[ref]['final'] - m)
        return fcs[ref]['rating'] if kind == 'fcs' else None

    worst, n, stale = 0.0, 0, 0
    for g in games:
        if g['cap_raw'] is None or g['tier'] == 'none':
            continue
        a, h = rate(g['aref'], g['akind']), rate(g['href'], g['hkind'])
        d = abs((a - h - payload['meta']['hfa'] * g['site']) - g['cap_raw'])
        worst = max(worst, d)
        n += 1
        if d > 0.25:
            stale += 1
    return n, worst, stale


def split_note(note):
    """Tracker note -> ordered [(label, text)] blocks on the logged markers."""
    pat = re.compile(r'\b(' + '|'.join(NOTE_MARKERS) + r'):\s*')
    hits = list(pat.finditer(note))
    out = []
    head = note[:hits[0].start()].strip() if hits else note.strip()
    if head:
        out.append(('Derivation', head))
    for i, mt in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(note)
        out.append((mt.group(1), note[mt.end():end].strip().rstrip(';').strip()))
    return out


def load_qbprops(payload):
    """Player props -> payload['qbprops']. Priced by the QB pass-yards model (v2 pricer), NOT
    by the win engine, so these rows are static: the board's rating controls do not move them.
    Edge is measured against the breakeven of the price actually taken, because the opposing
    quote was never captured (see the tracker footnote)."""
    n2k, _ = build_name_maps(payload)
    out = []
    for r in csv.DictReader(open(TRACKER_CSV)):
        if r['category'] != 'prop' or not r['team'].endswith('pass yds'):
            continue
        mt = re.match(r'^(.*?)\s*\(([A-Z]+)\)\s*(.*)$', r['team'])
        player, abbr, market = (mt.group(1), mt.group(2), mt.group(3)) if mt else (r['team'], '', '')
        nk = PROP_TEAM_NK.get(abbr)
        blocks = split_note(r['note'])
        prov = next((t for k, t in blocks if k == 'Provenance'), '')
        verdict = ''
        if prov:
            path = os.path.join(DD_DIR, prov)
            if os.path.exists(path):
                first = open(path).readline().strip()
                verdict = re.sub(r'^#\s*VERDICT:\s*', '', first)
        odds = int(r['odds'])
        dec = (100 + odds) / 100.0 if odds > 0 else (100 - odds) / abs(odds)
        p = float(r['our_p'])
        out.append(dict(player=player, abbr=abbr, nk=(nk if nk in payload['teams'] else None),
                        market=market, side=r['side'], line=float(r['line']), odds=odds,
                        book=r['book'], stake=float(r['stake_u']), p=p,
                        breakeven=abs(odds) / (abs(odds) + 100.0) if odds < 0 else 100.0 / (odds + 100.0),
                        ev=p * (dec - 1) - (1 - p), edge=float(r['pct_edge'].strip('%+')) / 100.0,
                        result=r['result'], date=r['date'], verdict=verdict, blocks=blocks))
    out.sort(key=lambda x: -x['ev'])
    return out


def main():
    payload = build_payload()
    payload['meta']['raw_scale'] = payload['meta']['market_stretch'] / MM_OVER_RAW
    payload['meta']['hfa_market'] = HFA_MARKET
    payload['games'] = load_games(payload)
    payload['qbprops'] = load_qbprops(payload)
    n, worst, stale = check_spread_lenses(payload, payload['games'])
    print(f"  games        {len(payload['games'])} rows "
          f"({sum(1 for g in payload['games'] if g['tier'] == 'fbs')} FBS-FBS, "
          f"{sum(1 for g in payload['games'] if g['tier'] == 'fcs')} FCS, "
          f"{sum(1 for g in payload['games'] if g['tier'] == 'none')} unjoined)")
    print(f"  lens check   n={n}  max|live-capture| {worst:.3f} pts  rows>0.25: {stale}"
          + ('   <-- ratings have drifted since capture' if stale else ''))
    print(f"  qbprops      {len(payload['qbprops'])} legs")
    engine_js = open(os.path.join(ROOT, 'pipeline', 'win_engine.js')).read()
    ui_js = UI_JS
    css = CSS
    html = (HTML_TEMPLATE
            .replace('/*__CSS__*/', css)
            .replace('//__ENGINE__//', engine_js)
            .replace('//__UI__//', ui_js)
            .replace('/*__PAYLOAD__*/', json.dumps(payload, separators=(',', ':'))))
    out = os.path.join(ROOT, 'outputs', 'win_totals_2026.html')
    with open(out, 'w') as f:
        f.write(html)
    kb = os.path.getsize(out) / 1024
    print(f"wrote {out}  ({kb:.0f} KB, {payload['meta']['n_teams']} teams)")


HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CFB 2026 — Win Totals Engine</title>
<style>/*__CSS__*/</style>
</head><body>
<header>
  <div class="wrap">
    <div class="brand"><h1>CFB 2026 · Win-Totals Engine</h1>
      <span class="sub">Power ratings &amp; variance model vs the market — finding mispriced totals</span></div>
    <nav id="tabs">
      <button data-tab="board" class="on">Board</button>
      <button data-tab="props">H2H Props</button>
      <button data-tab="qbprops">Player Props</button>
      <button data-tab="games">Single Games</button>
      <button data-tab="team">Team</button>
      <button data-tab="explainer">Rating Explainer</button>
      <button data-tab="method">Methodology</button>
    </nav>
  </div>
</header>
<div id="ovbar" class="ovbar wrap">
  <span id="ovstat">No manual rating changes.</span>
  <span class="engc">HFA <b id="c-hfa"></b> · &sigma;<sub>game</sub> <b id="c-sig"></b> · band→SD <b id="c-bts"></b></span>
  <button id="resetbtn" class="ghost" disabled>Reset all changes</button>
</div>
<main class="wrap">
  <section id="view-board" class="view on"></section>
  <section id="view-props" class="view"></section>
  <section id="view-qbprops" class="view"></section>
  <section id="view-games" class="view"></section>
  <section id="view-team" class="view"></section>
  <section id="view-explainer" class="view"></section>
  <section id="view-method" class="view"></section>
</main>
<footer class="wrap">Deterministic (exact Poisson-Binomial + Gauss-Hermite). Under prices assume a 30-cent line off the posted over. Not betting advice.</footer>
<script>window.PAYLOAD=/*__PAYLOAD__*/;</script>
<script>//__ENGINE__//</script>
<script>//__UI__//</script>
</body></html>'''


CSS = r'''
:root{--bg:#0e1116;--panel:#171b22;--panel2:#1e242e;--line:#2a3240;--ink:#e6e9ef;--dim:#9aa4b2;
--acc:#4f9dff;--good:#37c98b;--bad:#ff6b6b;--warn:#ffb454;--chip:#232b36;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 18px}
header{background:linear-gradient(180deg,#141a22,#0e1116);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 18px;flex-wrap:wrap}
.brand h1{font-size:17px;margin:0;letter-spacing:.2px}
.brand .sub{color:var(--dim);font-size:12px}
nav#tabs{display:flex;gap:6px;flex-wrap:wrap}
nav#tabs button{background:var(--chip);color:var(--dim);border:1px solid var(--line);padding:7px 13px;border-radius:8px;cursor:pointer;font-weight:600;font-size:13px}
nav#tabs button.on{background:var(--acc);color:#04101f;border-color:var(--acc)}
.ovbar{display:flex;align-items:center;gap:14px;padding:8px 18px;font-size:12px;color:var(--dim);flex-wrap:wrap}
.ovbar .engc{margin-left:auto}
.ovbar b{color:var(--ink)}
button.ghost{background:transparent;border:1px solid var(--line);color:var(--dim);padding:5px 10px;border-radius:7px;cursor:pointer}
button.ghost:not([disabled]){color:var(--warn);border-color:var(--warn)}
button.ghost[disabled]{opacity:.5;cursor:default}
main{padding:8px 0 40px}
.view{display:none}.view.on{display:block}
footer{color:var(--dim);font-size:11px;padding:20px 18px 40px;border-top:1px solid var(--line);margin-top:20px}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px;margin:14px 0}
.panel h2{margin:0 0 4px;font-size:15px}
.panel h3{margin:16px 0 6px;font-size:13px;color:var(--dim);text-transform:uppercase;letter-spacing:.6px}
.row{display:flex;gap:16px;flex-wrap:wrap}
.col{flex:1;min-width:300px}
select,input[type=number]{background:var(--panel2);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:8px 10px;font:inherit}
select{min-width:230px}
input.rate{width:76px;padding:4px 6px;text-align:right}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{color:var(--dim);font-weight:600;cursor:default;position:sticky;top:0;background:var(--panel)}
th.sort{cursor:pointer}th.sort:hover{color:var(--ink)}
tbody tr:hover{background:var(--panel2)}
.chip{display:inline-block;background:var(--chip);border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:11px;color:var(--dim)}
.chip.fcs{color:var(--warn)}.chip.conf{color:var(--acc)}.chip.reclass{color:var(--bad);border-color:var(--bad)}
.pos{color:var(--good)}.neg{color:var(--bad)}.mut{color:var(--dim)}
.conv{color:var(--good);letter-spacing:-1px}
.big{font-size:26px;font-weight:700}
.kv{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0}
.kv .k{background:var(--panel2);border:1px solid var(--line);border-radius:9px;padding:8px 12px;min-width:96px}
.kv .k .l{color:var(--dim);font-size:11px}.kv .k .v{font-size:17px;font-weight:700}
.bar{height:16px;background:var(--panel2);border-radius:4px;overflow:hidden;display:inline-block;vertical-align:middle}
.bar>span{display:block;height:100%;background:var(--acc)}
.dist td{padding:2px 8px;border:0}
.best{background:rgba(55,201,139,.12);border:1px solid var(--good);border-radius:9px;padding:10px 12px}
.best.under{background:rgba(79,157,255,.10);border-color:var(--acc)}
.hint{color:var(--dim);font-size:12px;margin:4px 0}
.edge-strong{font-weight:700}
.tag{font-size:10px;padding:1px 5px;border-radius:5px;margin-left:5px}
.tag.H{background:rgba(255,107,107,.15);color:var(--bad)}
.method p{max-width:760px;color:#cfd6e0}
.method code{background:var(--panel2);padding:1px 5px;border-radius:4px;color:var(--warn)}
.method .eq{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:8px 0;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:var(--ink);max-width:760px}
.units{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin:8px 0}
.unit{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:7px 4px;text-align:center}
.unit .u{color:var(--dim);font-size:10px}.unit .g{font-size:16px;font-weight:700}
.unit.L{border-color:var(--warn)}
.flag{display:inline-block;margin:2px 6px 2px 0;font-size:11px;color:var(--warn)}
.banner{background:rgba(255,180,84,.10);border:1px solid var(--warn);border-radius:10px;padding:11px 14px;margin:10px 0;font-size:12.5px;color:#e8dcc6}
.banner b{color:var(--warn)}
.leg{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:10px 0}
.leg .hd{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.leg .hd .nm{font-size:15px;font-weight:700}
.leg .hd .ln{color:var(--acc);font-weight:600}
.leg .vd{color:#cfd6e0;font-size:12.5px;margin:7px 0 2px;max-width:900px}
.blk{margin:7px 0;font-size:12px;color:var(--dim);max-width:900px}
.blk .lab{display:inline-block;min-width:78px;font-weight:700;font-size:10.5px;letter-spacing:.5px;color:var(--dim);vertical-align:top}
.blk.KILL .lab,.blk.REVERSE .lab{color:var(--bad)}
.blk.CORR .lab{color:var(--warn)}
.blk.CLV .lab{color:var(--acc)}
.blk .tx{display:inline-block;max-width:820px;vertical-align:top}
td.wide,th.wide{white-space:normal}
@media(max-width:640px){.units{grid-template-columns:repeat(4,1fr)}.col{min-width:100%}}
'''


UI_JS = r'''
(function(){
'use strict';
var P = window.PAYLOAD, WE = window.WinEngine, ENG = WE.makeEngine(P.meta);
var state = { sigma:P.meta.sigma_game, hfa:P.meta.hfa, bts:P.meta.band_to_sd,
              cal:(P.meta.cal_shrink||0.75),
              overrides:{}, team:null, expl:null, boardMode:'regular', boardSort:'conv', boardConv:false,
              gamesSort:'edge', gamesBucket:'all', gamesFcs:false };

// ---------- helpers ----------
function fmtOdds(a){ a=Math.round(a); if(Math.abs(a)>100000) return '<span class="mut">—</span>'; return (a>0?'+':'')+a; }
function pct(p){ return (100*p).toFixed(1)+'%'; }
function esc(s){ return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function sgn(x,d){ d=d==null?1:d; return (x>=0?'+':'')+x.toFixed(d); }
function curOpts(){ return {sigma_game:state.sigma, hfa:state.hfa, band_to_sd:state.bts}; }
// A control that re-renders the container it lives in has to do it OUT of the blur/change tick,
// or the browser throws "node to be removed is no longer a child of this node" when the input
// loses focus into a subtree we just replaced. Every in-panel control goes through this.
function redraw(fn){ setTimeout(fn,0); }
function isFbs(ref){ return !!P.teams[ref]; }
function baseFinal(ref){ return isFbs(ref)?P.teams[ref].final:(P.fcs[ref]?P.fcs[ref].rating:-40); }
function baseAnchor(ref){ return isFbs(ref)?P.teams[ref].anchor:(P.fcs[ref]?P.fcs[ref].rating:-40); }
function baseBand(ref){ return isFbs(ref)?P.teams[ref].band:(P.fcs[ref]?P.fcs[ref].band:10); }
function ov(ref){ return state.overrides[ref]||null; }
function ourRating(ref){ var o=ov(ref); return o&&o.final!=null?o.final:baseFinal(ref); }
function ourBand(ref){ var o=ov(ref); return o&&o.band!=null?o.band:baseBand(ref); }
function anchorRating(ref){ return baseAnchor(ref); }   // anchor = fixed consensus reference
// market-matched = our ratings stretched to the market's dispersion (propagates overrides;
// FCS opponents unchanged). On this set the fade-favorites/back-dogs tilt is neutralized.
function marketMatchedRating(ref){
  if(!isFbs(ref)) return P.fcs[ref]?P.fcs[ref].rating:-40;
  var m=P.meta.rating_mean, s=P.meta.market_stretch; return m+s*(ourRating(ref)-m);
}
// calibrated = our ratings pulled toward the field mean by the shrink that made preseason
// ratings actually predict 2021-25 games (probit slope ~1 at s~0.75). Same engine otherwise;
// this is the honest-probability lens for sizing (propagates overrides; FCS unchanged).
function calibratedRating(ref){
  if(!isFbs(ref)) return P.fcs[ref]?P.fcs[ref].rating:-40;
  var m=P.meta.rating_mean; return m+state.cal*(ourRating(ref)-m);
}
// raw = the SPREAD market's own scale (calibration study: slope 1.02, corr 0.978 against posted
// spreads). This is the lens to compare against a posted number; a raw-lens delta converts to the
// calibrated/sizing lens by x cal_shrink. FCS ratings pass through unchanged (D4 raw-FCS).
function rawRating(ref){
  if(!isFbs(ref)) return P.fcs[ref]?P.fcs[ref].rating:-40;
  var m=P.meta.rating_mean; return m+P.meta.raw_scale*(ourRating(ref)-m);
}
function ratingFn(kind){ return kind==='our'?ourRating:kind==='mkt'?marketMatchedRating:kind==='cal'?calibratedRating:kind==='raw'?rawRating:anchorRating; }
function nameOf(ref){ return isFbs(ref)?P.teams[ref].name:ref; }
function isOverridden(ref){ var o=ov(ref); return !!(o&&(o.final!=null||o.band!=null)); }
function nOverrides(){ return Object.keys(state.overrides).filter(isOverridden).length; }

function setOverride(ref, field, val){
  if(!state.overrides[ref]) state.overrides[ref]={};
  var base = field==='final'?baseFinal(ref):baseBand(ref);
  if(val===''||val==null||isNaN(val)||Math.abs(val-base)<1e-9){ delete state.overrides[ref][field];
    if(Object.keys(state.overrides[ref]).length===0) delete state.overrides[ref]; }
  else state.overrides[ref][field]=val;
  refreshOvbar();
}
function refreshOvbar(){
  var n=nOverrides();
  document.getElementById('ovstat').innerHTML = n? ('<b>'+n+'</b> team'+(n>1?'s':'')+' with manual rating changes — pro forma active.') : 'No manual rating changes.';
  document.getElementById('resetbtn').disabled = n===0;
  document.getElementById('c-hfa').textContent = state.hfa.toFixed(1);
  document.getElementById('c-sig').textContent = state.sigma.toFixed(1);
  document.getElementById('c-bts').textContent = state.bts.toFixed(2);
}

// ---------- core compute (mirrors win_totals_compute.py) ----------
function gamesFor(nk, kind, confOnly){
  var sc=P.schedules[nk]||[], out=[], rf=ratingFn(kind), ourB=(kind!=='anchor');
  for(var i=0;i<sc.length;i++){ var g=sc[i]; if(confOnly&&!g.is_conf) continue;
    var ref=g.opp_ref;
    out.push({mu_opp: rf(ref), site:g.site,
              band_opp: ourB?ourBand(ref):baseBand(ref), g:g});
  }
  return out;
}
function ladder(dist){
  var G=dist.length-1, out=[];
  for(var k=1;k<=G;k++){ var po=0; for(var j=k;j<=G;j++) po+=dist[j];
    out.push({line:k-0.5, p_over:po, fair_over:WE.probToAmerican(po), fair_under:WE.probToAmerican(1-po)}); }
  return out;
}
function pOverAt(dist,line){ var need=Math.floor(line)+1,s=0; for(var k=need;k<dist.length;k++) s+=dist[k]; return s; }
function distBlock(nk, kind, confOnly){
  var gs=gamesFor(nk,kind,confOnly);
  var mu = ratingFn(kind)(nk);
  var bd = kind==='anchor'?baseBand(nk):ourBand(nk);
  var r=ENG.winDistribution(mu,bd,gs.map(function(x){return{mu_opp:x.mu_opp,site:x.site,band_opp:x.band_opp};}),curOpts());
  return {dist:r.dist, ew:r.expected_wins, G:r.G, ladder:ladder(r.dist)};
}
function marketBlock(offers, distOur, distAnchor, distMkt, distCal){
  if(!offers||!offers.length) return null;
  var books=offers.map(function(o){return {line:o[0],over_odds:o[1],book:o[2],under_odds:WE.underFromOver(o[1])};})
                  .sort(function(a,b){return a.line-b.line||b.over_odds-a.over_odds;});
  var cand=[];
  books.forEach(function(b){
    var po=pOverAt(distOur.dist,b.line), pu=1-po;
    cand.push({side:'over',book:b.book,line:b.line,odds:b.over_odds,our_p:po,
               ev:po*(WE.americanToDecimal(b.over_odds)-1)-(1-po)});
    cand.push({side:'under',book:b.book,line:b.line,odds:b.under_odds,our_p:pu,
               ev:pu*(WE.americanToDecimal(b.under_odds)-1)-(1-pu)});
  });
  var best=cand.reduce(function(a,b){return b.ev>a.ev?b:a;});
  // consensus line = POSTED line nearest the median (never a phantom midpoint; tie -> more books, then lower)
  var lines=books.map(function(b){return b.line;}).sort(function(a,b){return a-b;});
  var m0=lines[Math.floor((lines.length-1)/2)];
  if(lines.length%2===0) m0=(lines[lines.length/2-1]+lines[lines.length/2])/2;
  var uniq=lines.filter(function(l,i){return lines.indexOf(l)===i;});
  var cnt=function(L){return lines.filter(function(l){return l===L;}).length;};
  var med=uniq.reduce(function(a,b){
    var da=Math.abs(a-m0), db=Math.abs(b-m0);
    if(db<da-1e-12) return b;
    if(da<db-1e-12) return a;
    if(cnt(b)!==cnt(a)) return cnt(b)>cnt(a)?b:a;
    return Math.min(a,b);
  });
  var at=books.filter(function(b){return Math.abs(b.line-med)<1e-9;});
  // Devig fix (2026-07-21): de-vig EACH book's two-way (30-cent unposted side) and average
  // the fair probabilities — never take a median/middle of raw American odds (invalid
  // across the +/-100 boundary and biased toward one book).
  var fps=at.map(function(b){var po=WE.americanToProb(b.over_odds),pu=WE.americanToProb(WE.underFromOver(b.over_odds));return po/(po+pu);});
  var mkt_po=fps.reduce(function(a,b){return a+b;},0)/fps.length;
  function edge(d){ var op=pOverAt(d.dist,med); return {line:med,mkt_po:mkt_po,our_po:op,
      edge_over:op-mkt_po, edge_under:(1-op)-(1-mkt_po)}; }
  // calibrated EV of the chosen best bet (the conservative sizing number)
  var pcal=pOverAt(distCal.dist,best.line);
  var pc=best.side==='over'?pcal:1-pcal;
  best.p_cal=pc;
  best.ev_cal=pc*(WE.americanToDecimal(best.odds)-1)-(1-pc);
  return {books:books, median_line:med, best:best,
          edge_our:edge(distOur), edge_anchor:edge(distAnchor), edge_mkt:edge(distMkt),
          edge_cal:edge(distCal)};
}
function computeTeam(nk){
  var t=P.teams[nk];
  var regOur=distBlock(nk,'our',false), regAnc=distBlock(nk,'anchor',false),
      regMm=distBlock(nk,'mkt',false), regCal=distBlock(nk,'cal',false);
  var regMkt=marketBlock((P.market[nk]||{}).regular, regOur, regAnc, regMm, regCal);
  var out={t:t, reg:{our:regOur,anchor:regAnc,mkt:regMm,cal:regCal,market:regMkt}};
  var hasConf=(P.schedules[nk]||[]).some(function(g){return g.is_conf;});
  if(hasConf){
    var cOur=distBlock(nk,'our',true), cAnc=distBlock(nk,'anchor',true),
        cMm=distBlock(nk,'mkt',true), cCal=distBlock(nk,'cal',true);
    var cMkt=marketBlock((P.market[nk]||{}).conference, cOur, cAnc, cMm, cCal);
    out.conf={our:cOur,anchor:cAnc,mkt:cMm,cal:cCal,market:cMkt};
  }
  return out;
}
// signed edge on a given side, for a set's edge block
function sideEdge(eb, side){ return side==='over'?eb.edge_over:eb.edge_under; }
// conviction = the edge on the WEAKER endpoint of the dispersion bracket: the CALIBRATED set
// (x0.75, what 2021-25 game outcomes support) and the MARKET-MATCHED set (x~1.15, the market's
// own spread). Edges move monotonically in the dispersion factor, so clearing both endpoints
// means the bet is +EV under EVERY dispersion hypothesis in between — team-specific, not a
// fade-the-spread play. (Our raw set sits inside the bracket and is shown for reference.)
function convScore(m){ var s=m.best.side; return Math.min(sideEdge(m.edge_cal,s), sideEdge(m.edge_mkt,s)); }
function convicted(m){ return convScore(m) >= 0.04; }

// ---------- rendering ----------
function teamOptions(sel, cur){
  var arr=Object.keys(P.teams).map(function(k){return P.teams[k];})
    .sort(function(a,b){return a.name.localeCompare(b.name);});
  return '<select id="'+sel+'">'+arr.map(function(t){
    return '<option value="'+t.nk+'"'+(t.nk===cur?' selected':'')+'>'+t.name+' ('+t.conf+')</option>';}).join('')+'</select>';
}
function siteTag(s){ return s>0?'<span class="chip">home</span>':s<0?'<span class="chip">away</span>':'<span class="chip">neutral</span>'; }

function edgeCell(e){
  var cls=Math.abs(e)>=0.05?(e>0?'pos edge-strong':'neg edge-strong'):(e>0?'pos':'neg');
  return '<span class="'+cls+'">'+sgn(100*e,1)+'%</span>';
}

// ----- Board -----
function renderBoard(){
  var v=document.getElementById('view-board');
  var mode=state.boardMode;
  var rows=[];
  Object.keys(P.teams).forEach(function(nk){
    var c=computeTeam(nk); var blk=mode==='regular'?c.reg:c.conf; if(!blk||!blk.market) return;
    var m=blk.market, b=m.best;
    rows.push({nk:nk, name:c.t.name, conf:c.t.conf, reclass:c.t.reclass, ew:blk.our.ew,
      line:m.median_line, edgeOur:sideEdge(m.edge_our,b.side),
      edgeAnc:sideEdge(m.edge_anchor,b.side), edgeMm:sideEdge(m.edge_mkt,b.side),
      edgeCal:sideEdge(m.edge_cal,b.side), evCal:b.ev_cal,
      conv:convicted(m), cscore:convScore(m), side:b.side, bestline:b.line, odds:b.odds, ev:b.ev});
  });
  if(state.boardConv) rows=rows.filter(function(r){return r.conv;});
  var key=state.boardSort;
  rows.sort(function(a,b){
    if(key==='conv') return b.cscore-a.cscore;
    if(key==='ev') return b.ev-a.ev;
    if(key==='edge') return Math.abs(b.edgeOur)-Math.abs(a.edgeOur);
    if(key==='team') return a.name.localeCompare(b.name);
    if(key==='ew') return b.ew-a.ew;
    if(key==='line') return b.line-a.line;
    return 0; });
  var h='<div class="panel"><h2>Board — every mispricing our model sees</h2>'+
    '<p class="hint">Best bet = highest-EV side across all posted books (under priced at 30&cent; off the over). '+
    'Four edge columns: <b>calibrated</b> (ours shrunk &times;'+state.cal.toFixed(2)+' to the dispersion that actually predicted 2021&ndash;25 — the honest probability &amp; the EV to size with), '+
    '<b>ours</b> (roster ratings, true-strength scale), <b>consensus</b> (analytics anchor), and <b>mkt-match</b> '+
    '(ours stretched to the market&rsquo;s dispersion, s='+P.meta.market_stretch.toFixed(2)+'). '+
    'Default sort ranks by <b>conviction</b> = the edge on the <i>weaker</i> of the two bracket endpoints (calibrated &amp; mkt-match); '+
    'a <b class="conv">✓✓</b> marks totals clearing +4% on both — bets that survive <i>every</i> dispersion assumption, team-specific by construction. Click a row to open the team.</p>'+
    '<div class="kv"><label class="hint">View: </label>'+
    '<select id="boardmode"><option value="regular"'+(mode==='regular'?' selected':'')+'>Regular-season wins</option>'+
    '<option value="conference"'+(mode==='conference'?' selected':'')+'>Conference wins (P4)</option></select>'+
    '<select id="boardsort"><option value="conv"'+(key==='conv'?' selected':'')+'>Sort: Conviction (dispersion bracket)</option>'+
    '<option value="ev"'+(key==='ev'?' selected':'')+'>Sort: Best EV</option><option value="edge"'+(key==='edge'?' selected':'')+'>Sort: |Edge|</option>'+
    '<option value="ew"'+(key==='ew'?' selected':'')+'>Sort: Our E[wins]</option>'+
    '<option value="team"'+(key==='team'?' selected':'')+'>Sort: Team</option></select>'+
    '<label class="hint" style="cursor:pointer"><input type="checkbox" id="convonly"'+(state.boardConv?' checked':'')+'> ✓✓ only (both ≥4%)</label></div>';
  h+='<table><thead><tr><th>Team</th><th>Conf</th><th></th><th>Our E[w]</th><th>Line</th>'+
     '<th>Best bet</th><th>Edge (calibr.)</th><th>Edge (ours)</th><th>Edge (consensus)</th><th>Edge (mkt-match)</th><th>EV /$1</th><th>EV cal</th></tr></thead><tbody>';
  rows.forEach(function(r){
    var evc=r.ev>0.02?'pos edge-strong':(r.ev>0?'pos':'mut');
    var evcc=r.evCal>0.02?'pos edge-strong':(r.evCal>0?'pos':'mut');
    h+='<tr data-nk="'+r.nk+'" style="cursor:pointer"><td>'+r.name+(r.reclass?' <span class="chip reclass">FBS debut</span>':'')+'</td>'+
       '<td class="mut">'+r.conf+'</td><td>'+(r.conv?'<b class="conv">✓✓</b>':'')+'</td><td>'+r.ew.toFixed(2)+'</td><td>'+r.line.toFixed(1)+'</td>'+
       '<td>'+(r.side==='over'?'Over':'Under')+' '+r.bestline.toFixed(1)+' <span class="mut">'+fmtOdds(r.odds)+'</span></td>'+
       '<td>'+edgeCell(r.edgeCal)+'</td><td>'+edgeCell(r.edgeOur)+'</td><td>'+edgeCell(r.edgeAnc)+'</td><td>'+edgeCell(r.edgeMm)+'</td>'+
       '<td class="'+evc+'">'+sgn(r.ev,3)+'</td><td class="'+evcc+'">'+sgn(r.evCal,3)+'</td></tr>';
  });
  var nconv=rows.filter(function(r){return r.conv;}).length;
  h+='</tbody></table><p class="hint">'+rows.length+' teams with posted '+mode+' totals'+(state.boardConv?'':' · '+nconv+' double-confirmed (✓✓)')+'.</p></div>';
  v.innerHTML=h;
  document.getElementById('boardmode').onchange=function(){state.boardMode=this.value;redraw(renderBoard);};
  document.getElementById('boardsort').onchange=function(){state.boardSort=this.value;redraw(renderBoard);};
  document.getElementById('convonly').onchange=function(){state.boardConv=this.checked;redraw(renderBoard);};
  Array.prototype.forEach.call(v.querySelectorAll('tr[data-nk]'),function(tr){
    tr.onclick=function(){ state.team=tr.getAttribute('data-nk'); setTab('team'); };
  });
}

// ----- Head-to-head props -----
// win distribution for a team under a rating set, optionally excluding one opponent (nk)
function propDist(nk, kind, exclNk){
  var sc=P.schedules[nk]||[], gs=[], rf=ratingFn(kind), ourB=(kind!=='anchor');
  for(var i=0;i<sc.length;i++){ var g=sc[i];
    if(exclNk && g.opp_kind==='fbs' && g.opp_ref===exclNk) continue;
    gs.push({mu_opp:rf(g.opp_ref), site:g.site, band_opp: ourB?ourBand(g.opp_ref):baseBand(g.opp_ref)});
  }
  var bd = kind==='anchor'?baseBand(nk):ourBand(nk);
  return ENG.winDistribution(rf(nk), bd, gs, curOpts()).dist;
}
// P(Wfav - Wdog >= t) for independent win distributions
function diffGe(dfav, ddog, t){
  var s=0; for(var i=0;i<dfav.length;i++){ for(var j=0;j<ddog.length;j++){ if(i-j>=t) s+=dfav[i]*ddog[j]; } }
  return s;
}
function playsEachOther(a,b){ return (P.schedules[a]||[]).some(function(g){return g.opp_kind==='fbs'&&g.opp_ref===b;}); }
// P(favorite finishes with >= thresh more wins than dog), under rating set `kind`.
// Exact head-to-head handling when the two teams actually play: condition on that game.
function propProb(favNk, dogNk, thresh, kind){
  if(!playsEachOther(favNk,dogNk)) return diffGe(propDist(favNk,kind), propDist(dogNk,kind), thresh);
  // find the H2H game on fav's schedule for its site, then split on the result
  var site=0; var sc=P.schedules[favNk]||[];
  for(var i=0;i<sc.length;i++){ if(sc[i].opp_kind==='fbs'&&sc[i].opp_ref===dogNk){ site=sc[i].site; break; } }
  var pf=ENG.gameWinProb(ratingFn(kind)(favNk), ratingFn(kind)(dogNk), site,
                         (kind!=='anchor'?ourBand(dogNk):baseBand(dogNk)), curOpts());
  var xf=propDist(favNk,kind,dogNk), xd=propDist(dogNk,kind,favNk);
  return pf*diffGe(xf,xd,thresh-1) + (1-pf)*diffGe(xf,xd,thresh+1);
}
var PROP_OVR = 2*WE.americanToProb(-110);   // standard-juice two-way overround (owner spec)
function computeProp(pr){
  var mktp = WE.americanToProb(pr.price)/PROP_OVR;    // de-vig at standard juice
  var pOur=propProb(pr.fav_nk,pr.dog_nk,pr.thresh,'our');
  var pCal=propProb(pr.fav_nk,pr.dog_nk,pr.thresh,'cal');
  var pMkt=propProb(pr.fav_nk,pr.dog_nk,pr.thresh,'mkt');
  var pAnc=propProb(pr.fav_nk,pr.dog_nk,pr.thresh,'anchor');
  var dec=WE.americanToDecimal(pr.price);
  function ev(p){ return p*(dec-1)-(1-p); }
  var conv=Math.min(pCal-mktp, pMkt-mktp);
  return {pr:pr, mktp:mktp, our:pOur, cal:pCal, mkt:pMkt, anc:pAnc,
          edgeOur:pOur-mktp, edgeCal:pCal-mktp, edgeMkt:pMkt-mktp,
          evOur:ev(pOur), evCal:ev(pCal), conv:conv, h2h:playsEachOther(pr.fav_nk,pr.dog_nk)};
}
function renderProps(){
  var v=document.getElementById('view-props');
  if(!P.props||!P.props.length){ v.innerHTML='<div class="panel"><p class="hint">No props loaded.</p></div>'; return; }
  var rows=P.props.map(computeProp);
  var key=state.propSort||'conv';
  rows.sort(function(a,b){ return key==='ev'?(b.evCal-a.evCal):key==='edge'?(b.edgeCal-a.edgeCal):(b.conv-a.conv); });
  var h='<div class="panel"><h2>Head-to-head win-total props</h2>'+
    '<p class="hint">Each bet: the <b>favorite</b> to finish the regular season with at least <b>⌈line⌉</b> more wins than the underdog, at the posted price. '+
    'We model it as the <b>difference of the two teams&rsquo; season win distributions</b> (same engine as the board); when the two teams actually play (tagged <span class="chip conf">H2H</span>) that game is handled exactly by conditioning on its result. '+
    'Market prob de-vigged assuming <b>standard −110 juice</b> on the unposted side. Probabilities shown under <b>calibrated</b> (×'+state.cal.toFixed(2)+', the honest/​sizing lens), <b>ours</b>, and <b>mkt-match</b>; '+
    '<b>EV</b> is per $1 at the posted price. <b class="conv">✓✓</b> = edge ≥ +4% on <i>both</i> bracket endpoints (calibrated &amp; mkt-match) — robust to the dispersion question. <b>Size with EV (cal).</b></p>'+
    '<div class="kv"><label class="hint">Sort: </label><select id="propsort">'+
    '<option value="conv"'+(key==='conv'?' selected':'')+'>Conviction (bracket)</option>'+
    '<option value="ev"'+(key==='ev'?' selected':'')+'>EV (calibrated)</option>'+
    '<option value="edge"'+(key==='edge'?' selected':'')+'>Edge (calibrated)</option></select></div>';
  h+='<table><thead><tr><th>Bet</th><th>Matchup</th><th></th><th>Mkt P</th><th>P (cal)</th><th>P (ours)</th><th>P (mkt-m)</th>'+
     '<th>Edge (cal)</th><th>EV (ours)</th><th>EV (cal)</th></tr></thead><tbody>';
  rows.forEach(function(r){
    var pr=r.pr, sign=pr.price>0?'+':'';
    var evc=function(e){return e>0.02?'pos edge-strong':(e>0?'pos':'mut');};
    h+='<tr data-fav="'+pr.fav_nk+'"><td>'+esc(pr.fav)+' −'+(pr.line)+' <span class="mut">'+sign+pr.price+'</span></td>'+
       '<td class="mut">'+esc(pr.t1)+' / '+esc(pr.t2)+(r.h2h?' <span class="chip conf">H2H</span>':'')+'</td>'+
       '<td>'+(r.conv>=0.04?'<b class="conv">✓✓</b>':'')+'</td>'+
       '<td class="mut">'+pct(r.mktp)+'</td><td>'+pct(r.cal)+'</td><td class="mut">'+pct(r.our)+'</td><td class="mut">'+pct(r.mkt)+'</td>'+
       '<td>'+edgeCell(r.edgeCal)+'</td><td class="'+evc(r.evOur)+'">'+sgn(r.evOur,3)+'</td><td class="'+evc(r.evCal)+'">'+sgn(r.evCal,3)+'</td></tr>';
  });
  var n=rows.filter(function(r){return r.conv>=0.04;}).length;
  h+='</tbody></table><p class="hint">'+rows.length+' props · '+n+' clear the ✓✓ bracket. Difference-of-distributions treats the two seasons as independent apart from any direct H2H game; residual common-opponent correlation (same-conference pairs) is unmodeled and would modestly narrow large-gap probabilities.</p></div>';
  v.innerHTML=h;
  document.getElementById('propsort').onchange=function(){state.propSort=this.value;redraw(renderProps);};
  Array.prototype.forEach.call(v.querySelectorAll('tr[data-fav]'),function(tr){
    tr.style.cursor='pointer';
    tr.onclick=function(){ state.team=tr.getAttribute('data-fav'); setTab('team'); };
  });
}

// ----- Player props (QB regular-season passing yards) -----
// These are priced by the pass-yards model, NOT the win engine: the rating/HFA controls above
// do not move them. Edge is measured against the BREAKEVEN OF THE PRICE TAKEN, not a de-vigged
// fair number, because the opposing quote was never captured.
function renderQbProps(){
  var v=document.getElementById('view-qbprops');
  var L=P.qbprops||[];
  if(!L.length){ v.innerHTML='<div class="panel"><p class="hint">No player props loaded.</p></div>'; return; }
  var stake=L.reduce(function(a,b){return a+b.stake;},0);
  var ev=L.reduce(function(a,b){return a+b.stake*b.ev;},0);
  var h='<div class="panel"><h2>Player props — QB regular-season passing yards</h2>'+
    '<p class="hint">Five FanDuel unders taken '+esc(L[0].date)+', all at −113. Priced by the QB pass-yards model '+
    '(availability hazard × per-game μ × games played), <b>not</b> by the win engine — the rating and HFA controls on this board do not move these numbers. '+
    'Settlement is <b>strict-12</b>: FanDuel&rsquo;s regular-season market excludes conference championship games, and its ≥1-snap action rule means a season never played <b>voids</b> rather than loses.</p>'+
    '<div class="kv">'+
    '<div class="k"><div class="l">legs</div><div class="v">'+L.length+'</div></div>'+
    '<div class="k"><div class="l">staked</div><div class="v">'+stake.toFixed(2)+'u</div></div>'+
    '<div class="k"><div class="l">model EV</div><div class="v pos">'+sgn(ev,3)+'u</div></div>'+
    '<div class="k"><div class="l">breakeven @ −113</div><div class="v">'+pct(L[0].breakeven)+'</div></div>'+
    '<div class="k"><div class="l">status</div><div class="v">'+esc(L[0].result)+'</div></div></div>';
  h+='<table><thead><tr><th>Leg</th><th>Bet</th><th>Price</th><th>P (ours)</th><th>Breakeven</th><th>Edge</th><th>EV /$1</th><th>Stake</th></tr></thead><tbody>';
  L.forEach(function(r){
    h+='<tr'+(r.nk?' data-nk="'+r.nk+'"':'')+'><td>'+esc(r.player)+' <span class="chip">'+esc(r.abbr)+'</span></td>'+
       '<td class="mut">'+esc(r.side)+' '+r.line.toFixed(1)+' '+esc(r.market)+'</td>'+
       '<td class="mut">'+(r.odds>0?'+':'')+r.odds+' <span class="chip">'+esc(r.book)+'</span></td>'+
       '<td>'+pct(r.p)+'</td><td class="mut">'+pct(r.breakeven)+'</td>'+
       '<td>'+edgeCell(r.p-r.breakeven)+'</td>'+
       '<td class="pos edge-strong">'+sgn(r.ev,3)+'</td><td>'+r.stake.toFixed(2)+'u</td></tr>';
  });
  h+='</tbody></table>'+
     '<p class="hint">Edge = our probability − the breakeven of the price taken ('+pct(L[0].breakeven)+' at −113). It is <b>not</b> measured against a de-vigged fair line: '+
     'FanDuel&rsquo;s opposing (over) quote was never captured, so no two-way de-vig is possible and this is the honest, conservative basis. '+
     'Row click opens that team on the Team tab.</p></div>';
  h+='<div class="panel"><h2>Dive detail</h2><p class="hint">The logged thesis, kill triggers, cross-leg correlation and CLV checkpoints for each leg, as recorded at the time of the bet. '+
     '<b class="conv">Verdict</b> lines are the one-sentence headline from each deep dive; the honest edge stated there is the number to trust, not the mechanical pricer output.</p>';
  L.forEach(function(r){
    h+='<div class="leg"><div class="hd"><span class="nm">'+esc(r.player)+'</span>'+
       '<span class="ln">'+esc(r.side)+' '+r.line.toFixed(1)+' @ '+(r.odds>0?'+':'')+r.odds+'</span>'+
       '<span class="chip">'+r.stake.toFixed(2)+'u</span><span class="chip">EV '+sgn(r.ev,3)+'</span></div>';
    if(r.verdict) h+='<div class="vd"><b class="conv">Verdict</b> '+esc(r.verdict)+'</div>';
    r.blocks.forEach(function(b){
      var lab=b[0]==='Derivation'?'DERIVATION':b[0]==='Provenance'?'SOURCE':b[0].toUpperCase();
      h+='<div class="blk '+esc(b[0])+'"><span class="lab">'+lab+'</span><span class="tx">'+esc(b[1])+'</span></div>';
    });
    h+='</div>';
  });
  h+='<p class="hint">A leg that trips a <b class="neg">KILL</b> trigger comes off at the next available price; <b class="neg">REVERSE</b> notes name the conditions under which the obvious read is backwards. '+
     '<b style="color:var(--warn)">CORR</b> flags legs whose seasons intersect directly — those are not independent and are floor-sized for that reason. '+
     '<b style="color:var(--acc)">CLV</b> gives the re-check points (Week 0 and close) that grade whether the number was right regardless of how the props settle.</p></div>';
  v.innerHTML=h;
  Array.prototype.forEach.call(v.querySelectorAll('tr[data-nk]'),function(tr){
    tr.style.cursor='pointer';
    tr.onclick=function(){ state.team=tr.getAttribute('data-nk'); setTab('team'); };
  });
}

// ----- Single games (posted spreads vs the board, recomputed live) -----
// err(g,h) = model_home_spread(h) - posted_home_spread = d_home - d_away,  d_t = market's rating
// of t minus ours. So err > 0 => the market rates the HOME team higher than we do => our
// (nominal) value is on the AWAY side. Spread sign convention: negative = home favored.
function gSpread(g, hfa){
  if(g.tier==='none'||g.posted==null) return null;
  return rawRating(g.aref) - rawRating(g.href) - hfa*g.site;
}
function gErr(g, hfa){ var s=gSpread(g,hfa); return s==null?null:s-g.posted; }
function fbsGames(){ return (P.games||[]).filter(function(g){return g.tier==='fbs'&&g.posted!=null;}); }
function dIn(g, ref, hfa){ var e=gErr(g,hfa); return g.href===ref?e:-e; }
// delta for `ref` from game g, netting out the opponent's read from the opponent's OTHER capture
// games. nOther === 0 means the pair is UNIDENTIFIABLE: full attribution is an upper bound, not
// an estimate, and a 50/50 split is all the data supports.
function localized(ref, g, hfa){
  var opp=(g.href===ref)?g.aref:g.href, oth=fbsGames().filter(function(o){
    return o!==g && (o.href===opp||o.aref===opp); });
  var d=0; oth.forEach(function(o){ d+=dIn(o,opp,hfa); });
  return {d: dIn(g,ref,hfa) + (oth.length?d/oth.length:0), n: oth.length};
}
function renderGames(){
  var v=document.getElementById('view-games');
  var all=P.games||[];
  if(!all.length){ v.innerHTML='<div class="panel"><p class="hint">No posted lines loaded.</p></div>'; return; }
  var hA=state.hfa, hB=P.meta.hfa_market, same=Math.abs(hA-hB)<1e-9;
  var showFcs=!!state.gamesFcs, key=state.gamesSort||'edge', bucket=state.gamesBucket||'all';
  var fbs=fbsGames();
  // aggregates: FBS-FBS only. FCS-at-FBS rows carry a ~+9 pt error in every lens -- they measure
  // our FCS tier, not the FBS host -- so they never enter a mean.
  function stats(hfa){
    var e=fbs.map(function(g){return gErr(g,hfa);});
    var n=e.length, mu=e.reduce(function(a,b){return a+b;},0)/n;
    var sd=Math.sqrt(e.reduce(function(a,b){return a+(b-mu)*(b-mu);},0)/(n-1));
    return {n:n, mae:e.reduce(function(a,b){return a+Math.abs(b);},0)/n, mean:mu, sd:sd};
  }
  var sA=stats(hA), sB=stats(hB);
  var rows=all.filter(function(g){ return (showFcs||g.tier==='fbs') && (bucket==='all'||g.bucket===bucket); })
    .map(function(g){
      var eA=gErr(g,hA), eB=gErr(g,hB);
      var stable=(eA==null)?false:(same?true:(eA*eB>0));
      var cons=(eA==null)?null:(same?eA:(Math.abs(eA)<Math.abs(eB)?eA:eB));   // conservative endpoint
      var side=null, num=null, loc=null;
      if(cons!=null && g.tier==='fbs' && stable){
        var vref=cons>0?g.aref:g.href;
        side=nameOf(vref); num=(vref===g.href)?g.posted:-g.posted;
        // Team read is ALWAYS taken at the market-implied HFA, never at the live one: it is only
        // interpretable where the aggregate mean error is ~0. At the house 2.3 every read inherits
        // the +1 pt systematic home bias and the attribution just re-reports the HFA gap.
        loc=localized(vref,g,hB);
      }
      return {g:g, eA:eA, eB:eB, stable:stable, cons:cons, side:side, num:num, loc:loc};
    });
  rows.sort(function(a,b){
    if(key==='books') return b.g.nb-a.g.nb;
    if(key==='posted') return (a.g.posted||0)-(b.g.posted||0);
    var x=a.cons==null?-1:(a.stable?Math.abs(a.cons):-1), y=b.cons==null?-1:(b.stable?Math.abs(b.cons):-1);
    return y-x;
  });
  var nStable=fbs.filter(function(g){var a=gErr(g,hA),b=gErr(g,hB);return same?true:a*b>0;}).length;

  var h='<div class="panel"><h2>Posted single-game lines vs the board</h2>'+
    '<p class="hint">The 2026-08-03 capture: Week 0, Week 1 and the Game-of-the-Year board, '+all.length+' lines. '+
    'The model side is <b>recomputed live from the current rating state</b> — edit a rating or move HFA and every row below moves with it. '+
    'Spreads are quoted <b>home-side</b> (negative = home favored) under the <b>raw lens</b> (×'+P.meta.raw_scale.toFixed(3)+'), which is the spread market&rsquo;s own scale — the correct one for comparing to a posted number. '+
    'A raw-lens gap converts to the calibrated/sizing lens by ×'+state.cal.toFixed(2)+'.</p>'+
    '<div class="banner"><b>These are not bets.</b> Preseason-consensus disagreement with posted spreads was preregistered as S14, tested, and <b>flushed</b>: 48.6% on n=395 and 48.4% on n=382, with no threshold redemption (8+ pt cells hit 49.2% on n=585 once the early-sample noise is excluded). '+
    'Decision text: <i>&ldquo;Sides at market prices are DROPPED from the 2026 program as consensus-disagreement plays.&rdquo;</i> This page is a <b>diagnostic</b> — it measures where the market disagrees with our team ratings, which is a read on <i>our numbers</i>, not a menu. '+
    'The screen&rsquo;s own finding reinforces that: the largest gaps localize to <b>team-level rating differences</b>, not game-level mispricings.</div>'+
    '<div class="kv">'+
    '<div class="k"><div class="l">FBS-FBS rows</div><div class="v">'+sA.n+'</div></div>'+
    '<div class="k"><div class="l">MAE @ HFA '+hA.toFixed(1)+'</div><div class="v">'+sA.mae.toFixed(2)+'</div></div>'+
    '<div class="k"><div class="l">mean @ '+hA.toFixed(1)+'</div><div class="v '+(Math.abs(sA.mean)>0.5?'neg':'')+'">'+sgn(sA.mean,2)+'</div></div>'+
    '<div class="k"><div class="l">MAE @ HFA '+hB.toFixed(1)+'</div><div class="v">'+sB.mae.toFixed(2)+'</div></div>'+
    '<div class="k"><div class="l">mean @ '+hB.toFixed(1)+'</div><div class="v '+(Math.abs(sB.mean)>0.5?'neg':'')+'">'+sgn(sB.mean,2)+'</div></div>'+
    '<div class="k"><div class="l">sign-stable</div><div class="v">'+nStable+'/'+sA.n+'</div></div></div>'+
    '<p class="hint">A non-zero <b>mean</b> is a systematic HFA statement, not a set of edges: at the house constant 2.3 the FBS-FBS mean error runs about +1 pt (we give the home team too little), and near 3.5 it vanishes. '+
    'That is why nothing is looked at unless its sign survives <b>both</b> constants'+(same?' — and with HFA set to '+hA.toFixed(1)+' the two endpoints coincide, so the stability test is currently vacuous.':'.')+' '+
    'FCS-at-FBS rows are excluded from every aggregate: their error is ≈ +9 pts in all lenses, which measures our FCS tier rather than the FBS host.</p>'+
    '<div class="kv"><label class="hint">Sort: </label><select id="gsort">'+
      '<option value="edge"'+(key==='edge'?' selected':'')+'>Disagreement (conservative)</option>'+
      '<option value="books"'+(key==='books'?' selected':'')+'>Book count</option>'+
      '<option value="posted"'+(key==='posted'?' selected':'')+'>Posted spread</option></select>'+
    '<label class="hint">Slate: </label><select id="gbucket">'+
      ['all','Week 0','Week 1','Game of the Year'].map(function(b){
        return '<option value="'+b+'"'+(bucket===b?' selected':'')+'>'+(b==='all'?'All':b)+'</option>';}).join('')+
    '</select><label class="hint"><input type="checkbox" id="gfcs"'+(showFcs?' checked':'')+'> show FCS / unjoined rows</label></div>';
  h+='<table><thead><tr><th>Game</th><th>Slate</th><th>Bk</th><th>Posted</th><th>Ours ('+hA.toFixed(1)+')</th>'+
     '<th>Err ('+hA.toFixed(1)+')</th><th>Err ('+hB.toFixed(1)+')</th><th></th><th>Nominal side</th><th>Team read @'+hB.toFixed(1)+'</th><th>Ident</th></tr></thead><tbody>';
  rows.forEach(function(r){
    var g=r.g, tag=g.tier==='fbs'?'':(g.tier==='fcs'?' <span class="chip fcs">FCS</span>':' <span class="chip reclass">unjoined</span>');
    var sp=gSpread(g,hA);
    h+='<tr'+(g.tier==='fbs'?' data-nk="'+g.href+'"':'')+'><td>'+esc(g.away)+' @ '+esc(g.home)+tag+
       (g.assumed?' <span class="chip">site assumed</span>':'')+'</td>'+
       '<td class="mut">'+esc(g.bucket)+'</td><td class="mut">'+g.nb+'</td>'+
       '<td>'+(g.posted==null?'—':sgn(g.posted,1))+'</td>'+
       '<td class="mut">'+(sp==null?'—':sgn(sp,1))+'</td>'+
       // the sign here is DIRECTION (which side the nominal value sits on), not quality. Deliberately
       // NOT coloured pos/neg -- everywhere else on the board green/red means +EV/-EV, and a big
       // negative err is exactly as interesting as a big positive one.
       '<td>'+(r.eA==null?'—':'<span class="'+(Math.abs(r.eA)>=3?'edge-strong':'mut')+'">'+sgn(r.eA,2)+'</span>')+'</td>'+
       '<td class="mut">'+(r.eB==null?'—':sgn(r.eB,2))+'</td>'+
       '<td>'+(r.cons==null?'':(r.stable?'':'<span class="chip fcs">flips</span>'))+'</td>'+
       '<td class="mut">'+(r.side?esc(r.side)+' '+sgn(r.num,1):'—')+'</td>'+
       '<td class="mut">'+(r.loc?sgn(-r.loc.d,2):'—')+'</td>'+
       '<td class="mut">'+(r.loc?(r.loc.n>=2?'yes':(r.loc.n===1?'partial':'<span class="chip fcs">no</span>')):'—')+'</td></tr>';
  });
  h+='</tbody></table>'+
     '<p class="hint">'+rows.length+' rows shown. <b>Err</b> = our home spread − the posted home spread; positive means the market rates the <b>home</b> team higher than we do, so the nominal value sits on the away side. '+
     '<b>Ours</b> is the raw-lens model spread at the live HFA. <b>Team read</b> attributes the gap to the named side after netting out the opponent&rsquo;s read from that opponent&rsquo;s <i>other</i> capture games '+
     '(<b>positive = our rating sits above the market-implied one</b> for that team, i.e. the disagreement really does belong to the named side). A <i>negative</i> read on the nominal side is a warning: '+
     'the localized attribution puts the gap on the <b>opponent</b> instead — we are not rating the named team above the market, we are rating its opponent below it. '+
     'It is fixed at HFA '+hB.toFixed(1)+' on purpose and does <b>not</b> follow the live control: an attributed team number is only interpretable where the aggregate mean error is ~0, '+
     'otherwise it just re-reports the HFA gap. <b>Ident</b> is how many other capture games the opponent has: <i>yes</i> ≥2, <i>partial</i> 1, '+
     '<i>no</i> = 0, meaning the pair is <b>unidentifiable</b> — the attribution is then an upper bound, not an estimate, and a 50/50 split is all the data supports. '+
     'Thin books (1–2) are the noisiest rows and routinely give the same team contradictory signs. Row click opens the home team on the Team tab.</p></div>';
  v.innerHTML=h;
  document.getElementById('gsort').onchange=function(){state.gamesSort=this.value;redraw(renderGames);};
  document.getElementById('gbucket').onchange=function(){state.gamesBucket=this.value;redraw(renderGames);};
  document.getElementById('gfcs').onchange=function(){state.gamesFcs=this.checked;redraw(renderGames);};
  Array.prototype.forEach.call(v.querySelectorAll('tr[data-nk]'),function(tr){
    tr.style.cursor='pointer';
    tr.onclick=function(){ state.team=tr.getAttribute('data-nk'); setTab('team'); };
  });
}

// ----- Team deep dive -----
function distTable(blk, marketLine){
  var d=blk.our.dist, da=blk.anchor.dist, G=blk.our.G, mx=Math.max.apply(null,d);
  var h='<table class="dist"><thead><tr><th>Wins</th><th>P (ours)</th><th></th><th>Fair (ours)</th><th>P (anchor)</th><th>Fair (anchor)</th></tr></thead><tbody>';
  for(var k=G;k>=0;k--){
    var w=Math.round(100*d[k]/mx);
    h+='<tr><td>'+k+'</td><td>'+pct(d[k])+'</td><td><span class="bar" style="width:90px"><span style="width:'+w+'%"></span></span></td>'+
       '<td class="mut">'+fmtOdds(WE.probToAmerican(d[k]))+'</td><td class="mut">'+pct(da[k])+'</td>'+
       '<td class="mut">'+fmtOdds(WE.probToAmerican(da[k]))+'</td></tr>';
  }
  return h+'</tbody></table>';
}
function ladderTable(blk){
  var lo=blk.our.ladder, la=blk.anchor.ladder, lm=blk.mkt.ladder, lc=blk.cal.ladder;
  var h='<table><thead><tr><th>Line</th><th>Over (cal)</th><th>Under (cal)</th><th>Over (ours)</th><th>Under (ours)</th>'+
        '<th>Over (cons)</th><th>Under (cons)</th><th>Over (mkt)</th><th>Under (mkt)</th></tr></thead><tbody>';
  for(var i=0;i<lo.length;i++){
    h+='<tr><td>'+lo[i].line.toFixed(1)+'</td><td>'+fmtOdds(lc[i].fair_over)+'</td><td>'+fmtOdds(lc[i].fair_under)+'</td>'+
       '<td>'+fmtOdds(lo[i].fair_over)+'</td><td>'+fmtOdds(lo[i].fair_under)+'</td>'+
       '<td class="mut">'+fmtOdds(la[i].fair_over)+'</td><td class="mut">'+fmtOdds(la[i].fair_under)+'</td>'+
       '<td class="mut">'+fmtOdds(lm[i].fair_over)+'</td><td class="mut">'+fmtOdds(lm[i].fair_under)+'</td></tr>';
  }
  return h+'</tbody></table>';
}
function marketPanel(mkt, blkName){
  if(!mkt) return '<p class="hint">No posted '+blkName+' total.</p>';
  var b=mkt.best;
  var conv=convicted(mkt);
  var h='<div class="best'+(b.side==='under'?' under':'')+'"><b>Best bet:</b> '+(b.side==='over'?'Over':'Under')+' '+b.line.toFixed(1)+
        ' @ '+fmtOdds(b.odds)+' <span class="mut">('+b.book+')</span> · our P '+pct(b.our_p)+
        ' · <b>EV '+sgn(b.ev,3)+'/$1</b> · <span title="EV under the calibrated set — the conservative number to size with">EV<sub>cal</sub> '+sgn(b.ev_cal,3)+'</span>'+
        (conv?' &nbsp;<b class="conv">✓✓ survives calibrated + market-matched</b>':'')+'</div>';
  h+='<div class="kv"><div class="k"><div class="l">Consensus line</div><div class="v">'+mkt.median_line.toFixed(1)+'</div></div>'+
     '<div class="k"><div class="l">Edge (calibrated)</div><div class="v">'+edgeCell(sideEdge(mkt.edge_cal,b.side))+'</div></div>'+
     '<div class="k"><div class="l">Edge (ours)</div><div class="v">'+edgeCell(sideEdge(mkt.edge_our,b.side))+'</div></div>'+
     '<div class="k"><div class="l">Edge (consensus)</div><div class="v">'+edgeCell(sideEdge(mkt.edge_anchor,b.side))+'</div></div>'+
     '<div class="k"><div class="l">Edge (mkt-match)</div><div class="v">'+edgeCell(sideEdge(mkt.edge_mkt,b.side))+'</div></div></div>';
  h+='<h3>Posted lines</h3><table><thead><tr><th>Book</th><th>Line</th><th>Over</th><th>Under (30&cent;)</th>'+
     '<th>P over (ours)</th><th>EV over</th><th>EV under</th></tr></thead><tbody>';
  mkt.books.forEach(function(bk){
    var evo=bk.__evo, evu=bk.__evu, po=bk.__po;
    h+='<tr><td>'+bk.book+'</td><td>'+bk.line.toFixed(1)+'</td><td>'+fmtOdds(bk.over_odds)+'</td><td>'+fmtOdds(bk.under_odds)+'</td>'+
       '<td class="mut">'+pct(po)+'</td><td class="'+(evo>0?'pos':'mut')+'">'+sgn(evo,3)+'</td>'+
       '<td class="'+(evu>0?'pos':'mut')+'">'+sgn(evu,3)+'</td></tr>';
  });
  return h+'</tbody></table>';
}

function renderTeam(){
  var v=document.getElementById('view-team');
  if(!state.team) state.team=Object.keys(P.teams).sort(function(a,b){return P.teams[a].name.localeCompare(P.teams[b].name);})[0];
  var nk=state.team, c=computeTeam(nk), t=c.t;
  // annotate books with our EV for the table
  ['reg','conf'].forEach(function(seg){ var blk=c[seg]; if(!blk||!blk.market) return;
    blk.market.books.forEach(function(bk){ var po=pOverAt(blk.our.dist,bk.line);
      bk.__po=po; bk.__evo=po*(WE.americanToDecimal(bk.over_odds)-1)-(1-po);
      bk.__evu=(1-po)*(WE.americanToDecimal(bk.under_odds)-1)-po; }); });
  var ovf=ov(nk)||{};
  var h='<div class="panel"><div class="row"><div class="col">'+
    '<h3>Choose team</h3>'+teamOptions('teamsel',nk)+
    '</div><div class="col"><h3>Our rating (editable — see the pro forma)</h3>'+
    '<div class="kv"><div class="k"><div class="l">Power (ours)</div>'+
       '<input class="rate" id="ov-final" type="number" step="0.5" value="'+ourRating(nk).toFixed(2)+'"></div>'+
    '<div class="k"><div class="l">Band (±, variance)</div><input class="rate" id="ov-band" type="number" step="0.5" value="'+ourBand(nk).toFixed(2)+'"></div>'+
    '<div class="k"><div class="l">Consensus anchor</div><div class="v">'+anchorRating(nk).toFixed(1)+'</div></div>'+
    '<div class="k"><div class="l">Market-matched</div><div class="v">'+marketMatchedRating(nk).toFixed(1)+'</div></div>'+
    '<div class="k"><div class="l">Calibrated (&times;'+state.cal.toFixed(2)+')</div><div class="v">'+calibratedRating(nk).toFixed(1)+'</div></div></div>'+
    (isOverridden(nk)?'<p class="hint">Base: power '+baseFinal(nk).toFixed(2)+', band '+baseBand(nk).toFixed(2)+'. <a href="#" id="revert" style="color:var(--warn)">revert this team</a></p>':'')+
    '</div></div>';
  h+='<div class="kv"><div class="k"><div class="l">Reg. E[wins] (ours)</div><div class="v">'+c.reg.our.ew.toFixed(2)+'</div></div>'+
     '<div class="k"><div class="l">E[wins] (consensus)</div><div class="v">'+c.reg.anchor.ew.toFixed(2)+'</div></div>'+
     '<div class="k"><div class="l">E[wins] (mkt-match)</div><div class="v">'+c.reg.mkt.ew.toFixed(2)+'</div></div>'+
     '<div class="k"><div class="l">E[wins] (calibrated)</div><div class="v">'+c.reg.cal.ew.toFixed(2)+'</div></div>'+
     (c.conf?'<div class="k"><div class="l">Conf. E[wins] (ours)</div><div class="v">'+c.conf.our.ew.toFixed(2)+'</div></div>':'')+
     '<div class="k"><div class="l">Conference</div><div class="v" style="font-size:14px">'+t.conf+'</div></div>'+
     (t.reclass?'<div class="k" style="border-color:var(--bad)"><div class="l">Note</div><div class="v" style="font-size:12px;color:var(--bad)">FBS debut ’26</div></div>':'')+'</div></div>';

  // schedule
  h+='<div class="panel"><h2>Schedule &amp; per-game win probability</h2>'+
     '<p class="hint">Verify the slate here. Opponent power ratings are editable too (edits ripple into this team\'s totals). '+
     '“P win” columns use our rating, the consensus anchor, and the market-matched set.</p>'+
     '<table><thead><tr><th>Wk</th><th>Opponent</th><th>Site</th><th>Opp (ours)</th><th>Opp (cons)</th><th>Opp (mkt)</th>'+
     '<th>P win (cal)</th><th>P win (ours)</th><th>P win (cons)</th><th>P win (mkt)</th></tr></thead><tbody>';
  (P.schedules[nk]||[]).forEach(function(g){
    var ref=g.opp_ref;
    var po=ENG.gameWinProb(ourRating(nk),ourRating(ref),g.site,ourBand(ref),curOpts());
    var pa=ENG.gameWinProb(anchorRating(nk),anchorRating(ref),g.site,baseBand(ref),curOpts());
    var pm=ENG.gameWinProb(marketMatchedRating(nk),marketMatchedRating(ref),g.site,ourBand(ref),curOpts());
    var pc=ENG.gameWinProb(calibratedRating(nk),calibratedRating(ref),g.site,ourBand(ref),curOpts());
    var tags=(g.opp_kind==='fcs'?' <span class="chip fcs">FCS</span>':'')+(g.is_conf?' <span class="chip conf">conf</span>':'')+
             (g.flex?' <span class="chip reclass" title="Pac-12 Week-13 flex game — pairing is the projected one (conference finalizes Nov 22); counts toward the regular-season total but NOT conference standings">flex (proj.)</span>':'')+
             (isFbs(ref)&&P.teams[ref].reclass?' <span class="chip reclass">FBS debut</span>':'');
    var editable='<input class="rate" data-ref="'+ref+'" data-f="final" type="number" step="0.5" value="'+ourRating(ref).toFixed(1)+'">';
    h+='<tr><td>'+g.week+'</td><td>'+g.opp_name+tags+'</td><td>'+siteTag(g.site)+'</td><td>'+editable+'</td>'+
       '<td class="mut">'+anchorRating(ref).toFixed(1)+'</td><td class="mut">'+marketMatchedRating(ref).toFixed(1)+'</td>'+
       '<td>'+pct(pc)+'</td><td>'+pct(po)+'</td><td class="mut">'+pct(pa)+'</td><td class="mut">'+pct(pm)+'</td></tr>';
  });
  h+='</tbody></table>';
  var hasFlex=(P.schedules[nk]||[]).some(function(g){return g.flex;});
  if(hasFlex) h+='<p class="hint">⚑ Wk-13 <b>flex game</b>: the Pac-12 assigns the final pairing no later than Nov 22; the one shown is the projected pairing from the Feb 2026 release. It counts in the regular-season win total but not the conference total.</p>';
  h+='</div>';

  // regular win total
  h+='<div class="panel"><h2>Regular-season win total</h2><div class="row">'+
     '<div class="col"><h3>Win distribution &amp; fair odds (per exact win count)</h3>'+distTable(c.reg)+'</div>'+
     '<div class="col"><h3>Fair no-vig ladder (each line) — calibrated · ours · consensus · mkt-match</h3>'+ladderTable(c.reg)+'</div></div>'+
     '<h3>Market — best price &amp; edge</h3>'+marketPanel(c.reg.market,'regular')+'</div>';

  // conference win total
  if(c.conf){
    h+='<div class="panel"><h2>Conference win total</h2><div class="row">'+
       '<div class="col"><h3>Conf. win distribution &amp; fair odds</h3>'+distTable(c.conf)+'</div>'+
       '<div class="col"><h3>Conf. fair no-vig ladder — calibrated · ours · consensus · mkt-match</h3>'+ladderTable(c.conf)+'</div></div>'+
       '<h3>Conference market — best price &amp; edge</h3>'+marketPanel(c.conf.market,'conference')+'</div>';
  }
  v.innerHTML=h;

  document.getElementById('teamsel').onchange=function(){state.team=this.value;redraw(renderTeam);};
  var fin=document.getElementById('ov-final'), bnd=document.getElementById('ov-band');
  fin.onchange=function(){ setOverride(nk,'final',parseFloat(this.value)); redraw(renderTeam); };
  bnd.onchange=function(){ setOverride(nk,'band',parseFloat(this.value)); redraw(renderTeam); };
  var rev=document.getElementById('revert'); if(rev) rev.onclick=function(e){e.preventDefault();delete state.overrides[nk];refreshOvbar();redraw(renderTeam);};
  Array.prototype.forEach.call(v.querySelectorAll('input[data-ref]'),function(inp){
    inp.onchange=function(){ setOverride(inp.getAttribute('data-ref'),'final',parseFloat(this.value)); redraw(renderTeam); };
  });
}

// ----- Rating explainer -----
function renderExplainer(){
  var v=document.getElementById('view-explainer');
  if(!state.expl) state.expl=state.team||Object.keys(P.teams).sort(function(a,b){return P.teams[a].name.localeCompare(P.teams[b].name);})[0];
  var nk=state.expl, t=P.teams[nk], d=t.der;
  var h='<div class="panel"><div class="row"><div class="col"><h3>Choose team</h3>'+teamOptions('explsel',nk)+'</div>'+
    '<div class="col"><div class="kv"><div class="k"><div class="l">Power rating</div><div class="v">'+sgn(t.final,1)+'</div></div>'+
    '<div class="k"><div class="l">Band (±)</div><div class="v">'+t.band.toFixed(1)+'</div></div>'+
    '<div class="k"><div class="l">Consensus anchor</div><div class="v">'+sgn(t.anchor,1)+'</div></div></div></div></div></div>';
  var pr=t.primer;
  if(pr){
    h+='<div class="panel"><h2>Why this rating — the scouting read</h2>';
    if(pr.override) h+='<div class="best under" style="border-color:var(--warn);background:rgba(255,180,84,.10)"><b>⚠ Manual override.</b> '+esc(pr.override)+'</div>';
    if(pr.summary) h+='<p style="max-width:820px;line-height:1.65;font-size:13.5px">'+esc(pr.summary)+'</p>';
    if(pr.units && Object.keys(pr.units).length){
      h+='<h3>Unit-by-unit read</h3><table><tbody>';
      ['QB','RB','WRTE','OL','DL','LB','DB','ST'].forEach(function(u){
        if(pr.units[u]) h+='<tr><td style="width:46px;font-weight:600;vertical-align:top">'+u+'</td>'+
          '<td style="text-align:left;color:#c7cdd6;white-space:normal;line-height:1.5">'+esc(pr.units[u])+'</td></tr>';
      });
      h+='</tbody></table>';
    }
    h+='<p class="hint">Extracted from the 2026 grading dossier. Grades below quantify this read.</p></div>';
  }
  if(d){
    h+='<div class="panel"><h2>Unit grades (0–100 scale)</h2><p class="hint">These eight returning-production/talent grades are the engine of the rating. An “L” tag = low-confidence (unsettled battle or thin data). Sum drives the offense/defense split below.</p><div class="units">';
    ['QB','RB','WRTE','OL','DL','LB','DB','ST'].forEach(function(u){
      var g=d.units[u], cf=d.units[u+'_conf']||'';
      h+='<div class="unit'+(cf==='L'?' L':'')+'"><div class="u">'+u+'</div><div class="g">'+(g==null?'–':g)+(cf?'<span class="tag '+cf+'">'+cf+'</span>':'')+'</div></div>';
    });
    h+='</div><p class="hint">Grade sum: <b>'+(d.units.sum!=null?d.units.sum:'–')+'</b>'+
       (d.L_count?' · <span class="flag">'+d.L_count+' low-confidence unit'+(d.L_count>1?'s':'')+'</span>':'')+
       (d.units.coach_change||d.new_HC?' · <span class="flag">new head coach (band widened ×1.13)</span>':'')+
       (t.reclass?' · <span class="flag">reclassifying to FBS in 2026 — rating is lower-confidence</span>':'')+'</p></div>';

    h+='<div class="panel"><h2>From grades to the power number</h2>'+
       '<p class="hint">Our grade-implied rating is blended with a market/analytics anchor, then nudged by the residual between the two, special teams, and a league re-centering. All units are points on a neutral field vs an average FBS team.</p>'+
       '<table><tbody>'+
       row2('Offense — grade-implied',sgn(d.implied_off,1),'Offense — anchor',sgn(d.anchor_off,1))+
       row2('Defense — grade-implied',sgn(d.implied_def,1),'Defense — anchor',sgn(d.anchor_def,1))+
       row2('Anchor blend (starting point)',sgn(d.anchor_blend,1),'Residual (grades − anchor)',sgn(d.residual,1))+
       row2('Residual adjustment (clipped)',sgn(d.resid_adj,1),'Special-teams term',sgn(d.st_term,1))+
       row2('League re-centering shift',sgn(d.recenter_shift,1),(d.overridden?'Grade-derived value (discarded)':'Final power rating'),sgn(d.overridden?d.grade_final:d.final,1))+
       '</tbody></table>'+
       (d.capped?'<p class="hint"><span class="flag">Movement from anchor was capped this cycle.</span></p>':'');
    if(d.overridden){
      h+='<div class="best under" style="border-color:var(--warn);background:rgba(255,180,84,.10)"><b>⚠ Final power rating set manually to '+sgn(d.final,1)+'.</b> The grade-derived value '+sgn(d.grade_final,1)+' above was <b>discarded</b>: this roster has no reliable FBS-level grade (reclassifying / heavy realignment), so the grade math is a no-data artifact rather than a real read. The final was set from targeted research and the analytics anchor — see the override rationale in the scouting read above.</div>';
    } else {
      h+='<p class="hint">Read it as: start at the <b>anchor blend '+sgn(d.anchor_blend,1)+'</b>; our grades imply a '+
         (d.residual>=0?'stronger':'weaker')+' team (residual '+sgn(d.residual,1)+'), which after clipping moves the number '+
         sgn(d.resid_adj,1)+'; special teams '+sgn(d.st_term,1)+' and re-centering '+sgn(d.recenter_shift,1)+
         ' give the <b>final '+sgn(d.final,1)+'</b>.</p>';
    }
    h+='<p class="hint">The band ±'+t.band.toFixed(1)+' is our 1-SD uncertainty on the final number.</p></div>';
  } else h+='<div class="panel"><p class="hint">No derivation on file.</p></div>';
  v.innerHTML=h;
  document.getElementById('explsel').onchange=function(){state.expl=this.value;redraw(renderExplainer);};
}
function row2(l1,v1,l2,v2){ return '<tr><td>'+l1+'</td><td>'+v1+'</td><td style="color:var(--dim)">'+l2+'</td><td>'+v2+'</td></tr>'; }

// ----- Methodology -----
function renderMethod(){
  var v=document.getElementById('view-method');
  var m=P.meta;
  var h='<div class="panel method"><h2>How the simulation works</h2>'+
  '<p>Every rating is a <b>neutral-field point margin</b> versus an average FBS team (0). For one game between our team S (rating &mu;<sub>S</sub>) and opponent O (rating &mu;<sub>O</sub>):</p>'+
  '<div class="eq">expected margin = &mu;<sub>S</sub> − &mu;<sub>O</sub> + HFA · site &nbsp;&nbsp;(site = +1 home, −1 away, 0 neutral)<br>P(S wins) = &Phi;( expected margin / &sigma;<sub>eff</sub> )</div>'+
  '<p>&Phi; is the normal CDF — a <b>probit</b> win model. The whole exercise lives or dies on &sigma;<sub>eff</sub>, so here is exactly what goes into it. There are three distinct sources of uncertainty, and they matter because they behave differently across a 12-game season.</p>'+
  '<h3>1 · Game randomness (&sigma;<sub>game</sub> = '+m.sigma_game+')</h3>'+
  '<p>Even with perfectly known ratings, a single result scatters around its expectation — turnovers, a bad spot, weather. This is <b>independent</b> game to game. It is pinned to how college margins actually convert to win probability: a 7-point favorite wins ~70%, a 3-pt favorite ~59%, a 14-pt favorite ~85%. That empirical curve <i>is</i> &sigma;<sub>game</sub>&nbsp;&asymp;&nbsp;13.5 (the standard deviation of a game result against its spread).</p>'+
  '<h3>2 · Opponent-rating uncertainty (their band)</h3>'+
  '<p>We are not certain of each opponent&rsquo;s true strength either. Because a season&rsquo;s opponents are all different teams, these errors are <b>independent</b>, so they add to each game&rsquo;s spread:</p>'+
  '<div class="eq">&sigma;<sub>eff</sub> = &radic;( &sigma;<sub>game</sub>&sup2; + (band<sub>opp</sub> · '+m.band_to_sd+')&sup2; )</div>'+
  '<h3>3 · Our own rating uncertainty (the shared shock) — the important one</h3>'+
  '<p>If our number on <i>our</i> team is 2 points too high, it is too high in <b>every</b> game. That error does not average out over the season — it is <b>correlated across all games</b>. We model it as a single latent offset drawn once per simulated season,</p>'+
  '<div class="eq">&delta; ~ Normal(0, &tau;&sup2;), &nbsp; &tau; = band<sub>self</sub> · '+m.band_to_sd+'</div>'+
  '<p>applied to &mu;<sub>S</sub> in every game and then integrated out. This shared shock is what <b>fattens the tails</b> of the win total: genuinely great and genuinely disastrous seasons both become more likely than an &ldquo;every game independent&rdquo; model would allow. Ignoring it would make us far too confident that a team lands on its median win total. This is the single most consequential modeling choice in the engine.</p>'+
  '<h3>Turning per-game probabilities into a win total (exactly, no Monte Carlo)</h3>'+
  '<p>Hold the shared shock &delta; fixed and the games are independent, so the number of wins follows a <b>Poisson-Binomial</b> distribution — computed <b>exactly</b> by dynamic programming, not simulated. We then average those exact distributions over &delta; using <b>21-point Gauss-Hermite quadrature</b> (the right tool for integrating against a normal weight). The result is deterministic: no simulation noise, and the browser reproduces the reference numbers to ~1&times;10<sup>−14</sup>.</p>'+
  '<div class="eq">P(wins = k) = &Sigma;<sub>i</sub> w<sub>i</sub> · PoissonBinomial( k | p<sub>g</sub>(&delta;<sub>i</sub>) )</div>'+
  '<h3>Fair odds &amp; edge</h3>'+
  '<p>The win distribution gives a fair no-vig price for every line (over k−0.5 = P(wins ≥ k)). Against the market we assume the owner&rsquo;s <b>30-cent line</b>: an over posted at −175 implies an under at +145. We de-vig the two sides to a market probability and call the difference from our probability the <b>edge</b>; EV is the expected profit per $1 at the posted price. The headline &ldquo;consensus&rdquo; line is the <b>posted</b> line nearest the books&rsquo; median (when books split 7.5/8.5 we use the more-posted real line, never a phantom 8.0), with each book at that line de-vigged separately and the fair probabilities averaged. Best bet is still evaluated at every posted price.</p>'+
  '<p><b>Pac-12 flex games:</b> all 8 Pac-12 teams play a 12th game in Week 13 (Nov 28) against a conference-assigned opponent (finalized Nov 22). Schedule feeds omitted it; we include the projected pairings (Boise@USU, OSU@WSU, SDSU@Fresno, TxSt@CSU), tagged &ldquo;flex (proj.)&rdquo; on team pages. These count in regular-season totals but not conference totals.</p>'+
  '<h3>Calibration (what we checked)</h3>'+
  '<p>Across all teams with posted totals, our win probabilities are <b>unbiased against the market on average</b> (mean edge ≈ 0.0%). We also checked whether the disagreements are <i>independent</i> per team (real signal) or a systematic function of the line (a scale artifact). The original ratings failed that test: our grade→points step was an OLS fit, and OLS fitted values are shrunk toward the mean by ~&radic;R², so the grades came out compressed — dragging every extreme toward the middle when blended in, so we systematically backed low-total underdogs&rsquo; overs and faded high-total favorites (~⅓ of edge variance was explained by the line alone). We <b>de-compressed the grade signal</b> (un-shrink the OLS fit + remove the level-correlated component of the grade residual — both market-agnostic), which cut that line-correlation by more than half and restored the fair rating spread (SD ≈ 13, matching KFord and the market), with the team ordering unchanged (Spearman ≈ 1.00). The residual is now concentrated in the extreme tails and traces to specific teams (e.g. reclassifying North Dakota State, where the market prices a 9-time FCS champion&rsquo;s FBS debut far above our grade) — genuine per-team disagreements to adjudicate by hand, not a mechanical tilt.</p>'+
  '<h3>Four rating sets &amp; the ✓✓ dispersion bracket</h3>'+
  '<p>Every total is priced under four sets that differ only in how spread-out team strength is assumed to be. <b>Calibrated</b> (×'+state.cal.toFixed(2)+') is our ratings pulled toward the field mean by the shrink that made preseason ratings actually predict 2021&ndash;25 game outcomes (≈3,700 FBS games: preseason favorites of every size win <i>less</i> than face-value ratings imply — probit slope 0.62 raw, ≈1.0 after this shrink — because July doesn&rsquo;t know about November&rsquo;s injuries, breakouts and busts; hindsight ratings at the same SD-13 scale calibrate perfectly, so this is a forecast-uncertainty effect, not a rating-scale error). <b>Ours</b> is the roster-graded power rating on the true-strength scale (SD ≈ 13, matching every real rating system). <b>Consensus</b> is the analytics anchor (SP+/Pick Six). <b>Market-matched</b> (×'+P.meta.market_stretch.toFixed(2)+') is our ratings stretched until their win-total edges have zero slope vs the line — the market&rsquo;s own dispersion.</p>'+
  '<p>Calibrated and market-matched are the <b>endpoints of the dispersion bracket</b> — the least and most spread the evidence and the market respectively support — and edges move monotonically between them. So an edge that clears both endpoints is +EV under <i>every</i> dispersion hypothesis in between: those are flagged <b class="conv">✓✓</b> and ranked by <b>conviction</b> (the weaker endpoint&rsquo;s edge). By construction a pure fade-the-favorites play can&rsquo;t earn ✓✓ (market-matched kills it), and a pure trust-the-chalk play can&rsquo;t either (calibrated kills it) — only team-specific mispricings survive. Size bets with the <b>calibrated EV</b>, the conservative number.</p>'+
  '<h3>Tune it yourself</h3>'+
  '<p>These are the live constants. Changing them recomputes the entire board and every team instantly — the same pro forma as editing a rating.</p>'+
  '<div class="kv"><div class="k"><div class="l">HFA (home-field pts)</div><input class="rate" id="m-hfa" type="number" step="0.1" value="'+state.hfa+'"></div>'+
  '<div class="k"><div class="l">&sigma;<sub>game</sub></div><input class="rate" id="m-sig" type="number" step="0.5" value="'+state.sigma+'"></div>'+
  '<div class="k"><div class="l">band → SD factor</div><input class="rate" id="m-bts" type="number" step="0.05" value="'+state.bts+'"></div>'+
  '<div class="k"><div class="l">calibration shrink</div><input class="rate" id="m-cal" type="number" step="0.05" value="'+state.cal+'"></div>'+
  '<div class="k" style="align-self:center"><a href="#" id="m-reset" style="color:var(--warn)">reset constants</a></div></div>'+
  '<p class="hint">Anchor sanity check at the current &sigma;<sub>game</sub>: '+
  '3-pt favorite '+pct(ENG.phi(3/state.sigma))+', 7-pt '+pct(ENG.phi(7/state.sigma))+', 10-pt '+pct(ENG.phi(10/state.sigma))+', 14-pt '+pct(ENG.phi(14/state.sigma))+'.</p>'+
  '</div>';
  v.innerHTML=h;
  function bind(id,key,fn){ var el=document.getElementById(id); el.onchange=function(){ var x=parseFloat(this.value); if(!isNaN(x)){ state[key]=x; refreshOvbar(); redraw(renderMethod); } }; }
  bind('m-hfa','hfa'); bind('m-sig','sigma'); bind('m-bts','bts'); bind('m-cal','cal');
  document.getElementById('m-reset').onclick=function(e){e.preventDefault();state.hfa=P.meta.hfa;state.sigma=P.meta.sigma_game;state.bts=P.meta.band_to_sd;state.cal=(P.meta.cal_shrink||0.75);refreshOvbar();redraw(renderMethod);};
}

// ---------- tab machinery ----------
var RENDER={board:renderBoard, props:renderProps, qbprops:renderQbProps, games:renderGames,
            team:renderTeam, explainer:renderExplainer, method:renderMethod};
function setTab(name){
  Array.prototype.forEach.call(document.querySelectorAll('#tabs button'),function(b){b.classList.toggle('on',b.getAttribute('data-tab')===name);});
  Array.prototype.forEach.call(document.querySelectorAll('.view'),function(v){v.classList.remove('on');});
  document.getElementById('view-'+name).classList.add('on');
  RENDER[name]();
}
Array.prototype.forEach.call(document.querySelectorAll('#tabs button'),function(b){
  b.onclick=function(){ setTab(b.getAttribute('data-tab')); };
});
document.getElementById('resetbtn').onclick=function(){ state.overrides={}; refreshOvbar();
  var cur=document.querySelector('#tabs button.on').getAttribute('data-tab'); RENDER[cur](); };
refreshOvbar(); setTab('board');
})();
'''


if __name__ == '__main__':
    main()
