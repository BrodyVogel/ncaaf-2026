#!/usr/bin/env python3
"""Generate the self-contained win-totals artifact (single HTML file).

Pipeline: win_totals_compute.build_payload()  ->  embed {payload, engine JS, UI JS, CSS}
into one HTML document. Re-run any time ratings / market / engine change; the output is fully
regenerable (owner's requirement: "not a one-off build").

    python3 pipeline/build_win_totals_artifact.py
    -> outputs/win_totals_2026.html
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from win_totals_compute import build_payload

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    payload = build_payload()
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
@media(max-width:640px){.units{grid-template-columns:repeat(4,1fr)}.col{min-width:100%}}
'''


UI_JS = r'''
(function(){
'use strict';
var P = window.PAYLOAD, WE = window.WinEngine, ENG = WE.makeEngine(P.meta);
var state = { sigma:P.meta.sigma_game, hfa:P.meta.hfa, bts:P.meta.band_to_sd,
              overrides:{}, team:null, expl:null, boardMode:'regular', boardSort:'ev' };

// ---------- helpers ----------
function fmtOdds(a){ a=Math.round(a); if(Math.abs(a)>100000) return '<span class="mut">—</span>'; return (a>0?'+':'')+a; }
function pct(p){ return (100*p).toFixed(1)+'%'; }
function sgn(x,d){ d=d==null?1:d; return (x>=0?'+':'')+x.toFixed(d); }
function curOpts(){ return {sigma_game:state.sigma, hfa:state.hfa, band_to_sd:state.bts}; }
function isFbs(ref){ return !!P.teams[ref]; }
function baseFinal(ref){ return isFbs(ref)?P.teams[ref].final:(P.fcs[ref]?P.fcs[ref].rating:-40); }
function baseAnchor(ref){ return isFbs(ref)?P.teams[ref].anchor:(P.fcs[ref]?P.fcs[ref].rating:-40); }
function baseBand(ref){ return isFbs(ref)?P.teams[ref].band:(P.fcs[ref]?P.fcs[ref].band:10); }
function ov(ref){ return state.overrides[ref]||null; }
function ourRating(ref){ var o=ov(ref); return o&&o.final!=null?o.final:baseFinal(ref); }
function ourBand(ref){ var o=ov(ref); return o&&o.band!=null?o.band:baseBand(ref); }
function anchorRating(ref){ return baseAnchor(ref); }   // anchor = fixed consensus reference
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
  var sc=P.schedules[nk]||[], out=[];
  for(var i=0;i<sc.length;i++){ var g=sc[i]; if(confOnly&&!g.is_conf) continue;
    var ref=g.opp_ref;
    out.push({mu_opp: kind==='our'?ourRating(ref):anchorRating(ref), site:g.site,
              band_opp: kind==='our'?ourBand(ref):baseBand(ref), g:g});
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
  var mu = kind==='our'?ourRating(nk):anchorRating(nk);
  var bd = kind==='our'?ourBand(nk):baseBand(nk);
  var r=ENG.winDistribution(mu,bd,gs.map(function(x){return{mu_opp:x.mu_opp,site:x.site,band_opp:x.band_opp};}),curOpts());
  return {dist:r.dist, ew:r.expected_wins, G:r.G, ladder:ladder(r.dist)};
}
function marketBlock(offers, distOur, distAnchor){
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
  var lines=books.map(function(b){return b.line;}).sort(function(a,b){return a-b;});
  var med=lines[Math.floor((lines.length-1)/2)];
  if(lines.length%2===0) med=(lines[lines.length/2-1]+lines[lines.length/2])/2;
  var at=books.filter(function(b){return Math.abs(b.line-med)<1e-9;});
  if(!at.length) at=books;
  var oos=at.map(function(b){return b.over_odds;}).sort(function(a,b){return a-b;});
  var oo=oos[Math.floor((oos.length-1)/2)];
  var pov=WE.americanToProb(oo), puv=WE.americanToProb(WE.underFromOver(oo)), mkt_po=pov/(pov+puv);
  function edge(d){ var op=pOverAt(d.dist,med); return {line:med,mkt_po:mkt_po,our_po:op,
      edge_over:op-mkt_po, edge_under:(1-op)-(1-mkt_po)}; }
  return {books:books, median_line:med, best:best, edge_our:edge(distOur), edge_anchor:edge(distAnchor)};
}
function computeTeam(nk){
  var t=P.teams[nk];
  var regOur=distBlock(nk,'our',false), regAnc=distBlock(nk,'anchor',false);
  var regMkt=marketBlock((P.market[nk]||{}).regular, regOur, regAnc);
  var out={t:t, reg:{our:regOur,anchor:regAnc,market:regMkt}};
  var hasConf=(P.schedules[nk]||[]).some(function(g){return g.is_conf;});
  if(hasConf){
    var cOur=distBlock(nk,'our',true), cAnc=distBlock(nk,'anchor',true);
    var cMkt=marketBlock((P.market[nk]||{}).conference, cOur, cAnc);
    out.conf={our:cOur,anchor:cAnc,market:cMkt};
  }
  return out;
}

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
      line:m.median_line, edgeOur:(b.side==='over'?m.edge_our.edge_over:m.edge_our.edge_under),
      edgeAnc:(b.side==='over'?m.edge_anchor.edge_over:m.edge_anchor.edge_under),
      side:b.side, bestline:b.line, odds:b.odds, ev:b.ev});
  });
  var key=state.boardSort;
  rows.sort(function(a,b){
    if(key==='ev') return b.ev-a.ev;
    if(key==='edge') return Math.abs(b.edgeOur)-Math.abs(a.edgeOur);
    if(key==='team') return a.name.localeCompare(b.name);
    if(key==='ew') return b.ew-a.ew;
    if(key==='line') return b.line-a.line;
    return 0; });
  var h='<div class="panel"><h2>Board — every mispricing our model sees</h2>'+
    '<p class="hint">Best bet = highest-EV side across all posted books (under priced at 30&cent; off the over). '+
    '“Edge” is our probability minus the de-vigged market probability on the best side. '+
    'Positive EV = our model likes it. Click a row to open the team. Reclassifying programs ('+P.meta.reclass.join(', ')+') carry extra uncertainty.</p>'+
    '<div class="kv"><label class="hint">View: </label>'+
    '<select id="boardmode"><option value="regular"'+(mode==='regular'?' selected':'')+'>Regular-season wins</option>'+
    '<option value="conference"'+(mode==='conference'?' selected':'')+'>Conference wins (P4)</option></select>'+
    '<select id="boardsort"><option value="ev">Sort: Best EV</option><option value="edge"'+(key==='edge'?' selected':'')+'>Sort: |Edge|</option>'+
    '<option value="ew"'+(key==='ew'?' selected':'')+'>Sort: Our E[wins]</option>'+
    '<option value="team"'+(key==='team'?' selected':'')+'>Sort: Team</option></select></div>';
  h+='<table><thead><tr><th>Team</th><th>Conf</th><th>Our E[w]</th><th>Mkt line</th>'+
     '<th>Best bet</th><th>Edge (ours)</th><th>Edge (anchor)</th><th>EV /$1</th></tr></thead><tbody>';
  rows.forEach(function(r){
    var evc=r.ev>0.02?'pos edge-strong':(r.ev>0?'pos':'mut');
    h+='<tr data-nk="'+r.nk+'" style="cursor:pointer"><td>'+r.name+(r.reclass?' <span class="chip reclass">FBS debut</span>':'')+'</td>'+
       '<td class="mut">'+r.conf+'</td><td>'+r.ew.toFixed(2)+'</td><td>'+r.line.toFixed(1)+'</td>'+
       '<td>'+(r.side==='over'?'Over':'Under')+' '+r.bestline.toFixed(1)+' <span class="mut">'+fmtOdds(r.odds)+'</span></td>'+
       '<td>'+edgeCell(r.edgeOur)+'</td><td>'+edgeCell(r.edgeAnc)+'</td>'+
       '<td class="'+evc+'">'+sgn(r.ev,3)+'</td></tr>';
  });
  h+='</tbody></table><p class="hint">'+rows.length+' teams with posted '+mode+' totals.</p></div>';
  v.innerHTML=h;
  document.getElementById('boardmode').onchange=function(){state.boardMode=this.value;renderBoard();};
  document.getElementById('boardsort').onchange=function(){state.boardSort=this.value;renderBoard();};
  Array.prototype.forEach.call(v.querySelectorAll('tr[data-nk]'),function(tr){
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
  var lo=blk.our.ladder, la=blk.anchor.ladder;
  var h='<table><thead><tr><th>Line</th><th>Over (ours)</th><th>Under (ours)</th><th>P over (ours)</th>'+
        '<th>Over (anchor)</th><th>Under (anchor)</th></tr></thead><tbody>';
  for(var i=0;i<lo.length;i++){
    h+='<tr><td>'+lo[i].line.toFixed(1)+'</td><td>'+fmtOdds(lo[i].fair_over)+'</td><td>'+fmtOdds(lo[i].fair_under)+'</td>'+
       '<td class="mut">'+pct(lo[i].p_over)+'</td><td class="mut">'+fmtOdds(la[i].fair_over)+'</td>'+
       '<td class="mut">'+fmtOdds(la[i].fair_under)+'</td></tr>';
  }
  return h+'</tbody></table>';
}
function marketPanel(mkt, blkName){
  if(!mkt) return '<p class="hint">No posted '+blkName+' total.</p>';
  var b=mkt.best;
  var h='<div class="best'+(b.side==='under'?' under':'')+'"><b>Best bet:</b> '+(b.side==='over'?'Over':'Under')+' '+b.line.toFixed(1)+
        ' @ '+fmtOdds(b.odds)+' <span class="mut">('+b.book+')</span> · our P '+pct(b.our_p)+
        ' · <b>EV '+sgn(b.ev,3)+'/$1</b></div>';
  h+='<div class="kv"><div class="k"><div class="l">Consensus line</div><div class="v">'+mkt.median_line.toFixed(1)+'</div></div>'+
     '<div class="k"><div class="l">Edge (ours)</div><div class="v">'+edgeCell(b.side==='over'?mkt.edge_our.edge_over:mkt.edge_our.edge_under)+'</div></div>'+
     '<div class="k"><div class="l">Edge (anchor)</div><div class="v">'+edgeCell(b.side==='over'?mkt.edge_anchor.edge_over:mkt.edge_anchor.edge_under)+'</div></div></div>';
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
    '<div class="k"><div class="l">Consensus anchor</div><div class="v">'+anchorRating(nk).toFixed(1)+'</div></div></div>'+
    (isOverridden(nk)?'<p class="hint">Base: power '+baseFinal(nk).toFixed(2)+', band '+baseBand(nk).toFixed(2)+'. <a href="#" id="revert" style="color:var(--warn)">revert this team</a></p>':'')+
    '</div></div>';
  h+='<div class="kv"><div class="k"><div class="l">Reg. E[wins] (ours)</div><div class="v">'+c.reg.our.ew.toFixed(2)+'</div></div>'+
     '<div class="k"><div class="l">Reg. E[wins] (anchor)</div><div class="v">'+c.reg.anchor.ew.toFixed(2)+'</div></div>'+
     (c.conf?'<div class="k"><div class="l">Conf. E[wins] (ours)</div><div class="v">'+c.conf.our.ew.toFixed(2)+'</div></div>':'')+
     '<div class="k"><div class="l">Conference</div><div class="v" style="font-size:14px">'+t.conf+'</div></div>'+
     (t.reclass?'<div class="k" style="border-color:var(--bad)"><div class="l">Note</div><div class="v" style="font-size:12px;color:var(--bad)">FBS debut ’26</div></div>':'')+'</div></div>';

  // schedule
  h+='<div class="panel"><h2>Schedule &amp; per-game win probability</h2>'+
     '<p class="hint">Verify the slate here. Opponent power ratings are editable too (edits ripple into this team\'s totals). '+
     '“P win” columns use our rating and the consensus anchor respectively.</p>'+
     '<table><thead><tr><th>Wk</th><th>Opponent</th><th>Site</th><th>Opp power (ours)</th><th>Opp (anchor)</th>'+
     '<th>P win (ours)</th><th>P win (anchor)</th></tr></thead><tbody>';
  (P.schedules[nk]||[]).forEach(function(g){
    var ref=g.opp_ref;
    var po=ENG.gameWinProb(ourRating(nk),ourRating(ref),g.site,ourBand(ref),curOpts());
    var pa=ENG.gameWinProb(anchorRating(nk),anchorRating(ref),g.site,baseBand(ref),curOpts());
    var tags=(g.opp_kind==='fcs'?' <span class="chip fcs">FCS</span>':'')+(g.is_conf?' <span class="chip conf">conf</span>':'')+
             (isFbs(ref)&&P.teams[ref].reclass?' <span class="chip reclass">FBS debut</span>':'');
    var editable='<input class="rate" data-ref="'+ref+'" data-f="final" type="number" step="0.5" value="'+ourRating(ref).toFixed(1)+'">';
    h+='<tr><td>'+g.week+'</td><td>'+g.opp_name+tags+'</td><td>'+siteTag(g.site)+'</td><td>'+editable+'</td>'+
       '<td class="mut">'+anchorRating(ref).toFixed(1)+'</td><td>'+pct(po)+'</td><td class="mut">'+pct(pa)+'</td></tr>';
  });
  h+='</tbody></table></div>';

  // regular win total
  h+='<div class="panel"><h2>Regular-season win total</h2><div class="row">'+
     '<div class="col"><h3>Win distribution &amp; fair odds (per exact win count)</h3>'+distTable(c.reg)+'</div>'+
     '<div class="col"><h3>Fair no-vig ladder (each line) — ours vs anchor</h3>'+ladderTable(c.reg)+'</div></div>'+
     '<h3>Market — best price &amp; edge</h3>'+marketPanel(c.reg.market,'regular')+'</div>';

  // conference win total
  if(c.conf){
    h+='<div class="panel"><h2>Conference win total</h2><div class="row">'+
       '<div class="col"><h3>Conf. win distribution &amp; fair odds</h3>'+distTable(c.conf)+'</div>'+
       '<div class="col"><h3>Conf. fair no-vig ladder — ours vs anchor</h3>'+ladderTable(c.conf)+'</div></div>'+
       '<h3>Conference market — best price &amp; edge</h3>'+marketPanel(c.conf.market,'conference')+'</div>';
  }
  v.innerHTML=h;

  document.getElementById('teamsel').onchange=function(){state.team=this.value;renderTeam();};
  var fin=document.getElementById('ov-final'), bnd=document.getElementById('ov-band');
  fin.onchange=function(){ setOverride(nk,'final',parseFloat(this.value)); renderTeam(); };
  bnd.onchange=function(){ setOverride(nk,'band',parseFloat(this.value)); renderTeam(); };
  var rev=document.getElementById('revert'); if(rev) rev.onclick=function(e){e.preventDefault();delete state.overrides[nk];refreshOvbar();renderTeam();};
  Array.prototype.forEach.call(v.querySelectorAll('input[data-ref]'),function(inp){
    inp.onchange=function(){ setOverride(inp.getAttribute('data-ref'),'final',parseFloat(this.value)); renderTeam(); };
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
       row2('League re-centering shift',sgn(d.recenter_shift,1),'Final power rating',sgn(d.final,1))+
       '</tbody></table>'+
       (d.capped?'<p class="hint"><span class="flag">Movement from anchor was capped this cycle.</span></p>':'')+
       '<p class="hint">Read it as: start at the <b>anchor blend '+sgn(d.anchor_blend,1)+'</b>; our grades imply a '+
       (d.residual>=0?'stronger':'weaker')+' team (residual '+sgn(d.residual,1)+'), which after clipping moves the number '+
       sgn(d.resid_adj,1)+'; special teams '+sgn(d.st_term,1)+' and re-centering '+sgn(d.recenter_shift,1)+
       ' give the <b>final '+sgn(d.final,1)+'</b>. The band ±'+t.band.toFixed(1)+' is our 1-SD uncertainty on that number.</p></div>';
  } else h+='<div class="panel"><p class="hint">No derivation on file.</p></div>';
  v.innerHTML=h;
  document.getElementById('explsel').onchange=function(){state.expl=this.value;renderExplainer();};
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
  '<p>The win distribution gives a fair no-vig price for every line (over k−0.5 = P(wins ≥ k)). Against the market we assume the owner&rsquo;s <b>30-cent line</b>: an over posted at −175 implies an under at +145. We de-vig the two sides to a market probability and call the difference from our probability the <b>edge</b>; EV is the expected profit per $1 at the posted price.</p>'+
  '<h3>Calibration (what we checked)</h3>'+
  '<p>Across all 129 teams with posted totals, our win probabilities are <b>unbiased against the market on average</b> (mean edge ≈ 0.0%). The disagreements are concentrated in specific teams — exactly what a mispricing finder should produce — rather than a systematic tilt. There is a small residual <i>compression</i> (we are a touch high on the weakest teams and a touch low on the strongest, ≈ ±5% at the extremes). We <b>left it in</b> rather than curve-fit the ratings to the market: &sigma;<sub>game</sub> = 13.5 is the theoretically correct single-game value, and the biggest edges (e.g. reclassifying North Dakota State, where the market prices a 9-time FCS champion&rsquo;s FBS debut far above our conservative grade) are real disagreements to adjudicate by hand, not artifacts to smooth away.</p>'+
  '<h3>Tune it yourself</h3>'+
  '<p>These are the live constants. Changing them recomputes the entire board and every team instantly — the same pro forma as editing a rating.</p>'+
  '<div class="kv"><div class="k"><div class="l">HFA (home-field pts)</div><input class="rate" id="m-hfa" type="number" step="0.1" value="'+state.hfa+'"></div>'+
  '<div class="k"><div class="l">&sigma;<sub>game</sub></div><input class="rate" id="m-sig" type="number" step="0.5" value="'+state.sigma+'"></div>'+
  '<div class="k"><div class="l">band → SD factor</div><input class="rate" id="m-bts" type="number" step="0.05" value="'+state.bts+'"></div>'+
  '<div class="k" style="align-self:center"><a href="#" id="m-reset" style="color:var(--warn)">reset constants</a></div></div>'+
  '<p class="hint">Anchor sanity check at the current &sigma;<sub>game</sub>: '+
  '3-pt favorite '+pct(ENG.phi(3/state.sigma))+', 7-pt '+pct(ENG.phi(7/state.sigma))+', 10-pt '+pct(ENG.phi(10/state.sigma))+', 14-pt '+pct(ENG.phi(14/state.sigma))+'.</p>'+
  '</div>';
  v.innerHTML=h;
  function bind(id,key,fn){ var el=document.getElementById(id); el.onchange=function(){ var x=parseFloat(this.value); if(!isNaN(x)){ state[key]=x; refreshOvbar(); renderMethod(); } }; }
  bind('m-hfa','hfa'); bind('m-sig','sigma'); bind('m-bts','bts');
  document.getElementById('m-reset').onclick=function(e){e.preventDefault();state.hfa=P.meta.hfa;state.sigma=P.meta.sigma_game;state.bts=P.meta.band_to_sd;refreshOvbar();renderMethod();};
}

// ---------- tab machinery ----------
var RENDER={board:renderBoard, team:renderTeam, explainer:renderExplainer, method:renderMethod};
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
