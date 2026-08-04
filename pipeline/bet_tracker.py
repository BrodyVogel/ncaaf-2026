#!/usr/bin/env python3
"""CFB 2026 bet tracker. Bets are defined in SEED below (source of truth, git-tracked).
Re-run to regenerate outputs/bet_tracker.csv + outputs/bet_tracker.html.
To log a new bet: append a dict to SEED and re-run. To grade one: set result W/L/P.
To close one early (cash-out): result="C" + cashout_u=<realized P&L in units> (0.0
for an at-stake close). our_p is our calibrated model's probability of the bet side
(the edge at time of bet).

CATEGORIES. 'regular'/'conference' are win-total bets: our_p is computed live from
the calibrated ratings via win_engine, and pct_edge is measured against the market's
de-vigged fair probability. 'prop' rows (S20 QB season passing yards, from 2026-08-04)
are different in two ways and both are deliberate:
  1. our_p is SUPPLIED in the seed (key 'p'), not recomputed — it is the deep dive's
     final judgment-layer probability (pricer_v2 mechanical price + the DD's hazard/mu
     overlay). Provenance for every prop row is docs/research/deep_dives/DD_<name>_<date>.md.
  2. pct_edge for props = our_p - implied(price taken), i.e. edge vs BREAKEVEN, because
     the opposing side's price was never captured and no de-vigged fair exists. This is
     the same .5305-at-(-113) convention every S20 deep dive quotes."""
import json, math, os, sys, csv, html
sys.path.insert(0, os.path.dirname(__file__))
import win_engine as E
from win_totals_compute import _market, consensus_line

ASOF = "2026-07-20"
# category: 'regular' or 'conference'. result: 'pending'|'W'|'L'|'P'|'C' (closed early).
SEED = [
 dict(date="2026-07-20", cat="regular", team="UConn",          side="over",  line=5.5, odds=-105, book="DK",    stake=0.57, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Tulsa",          side="over",  line=5.5, odds=+100, book="CZR",   stake=0.55, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Oregon State",   side="over",  line=3.5, odds=-150, book="Bet365",stake=0.65, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Bowling Green",  side="over",  line=4.5, odds=-160, book="Bet365",stake=0.70, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Liberty",        side="under", line=8.5, odds=-145, book="Bet365",stake=0.60, result="pending", note="took -145"),
 dict(date="2026-07-20", cat="regular", team="Arizona State",  side="under", line=6.5, odds=+100, book="CZR",   stake=0.55, result="pending", note="took +100; juiced out at BetRivers"),
 dict(date="2026-07-20", cat="regular", team="Kennesaw State", side="over",  line=6.5, odds=+120, book="Bet365",stake=0.55, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Illinois",       side="under", line=7.5, odds=-160, book="CZR",   stake=0.65, result="pending", note="took -160"),
 dict(date="2026-07-20", cat="regular", team="West Virginia",  side="under", line=5.5, odds=+132, book="FD",    stake=0.50, result="pending", note="FD +132"),
 dict(date="2026-07-20", cat="regular", team="East Carolina",  side="over",  line=7.5, odds=+100, book="CZR",   stake=0.55, result="pending", note=""),
 dict(date="2026-07-20", cat="regular", team="Hawai'i",        side="under", line=7.5, odds=-120, book="CZR",   stake=0.60, result="pending", note="took -120 at CZR"),
 dict(date="2026-07-20", cat="conference", team="Florida",     side="under", line=4.5, odds=-110, book="CZR",   stake=0.50, result="pending", note="book confirmed CZR 2026-07-26"),
 dict(date="2026-07-20", cat="conference", team="UCF",         side="over",  line=3.5, odds=-115, book="DK",    stake=0.55, result="pending", note="DK -115; v2 re-price 2026-07-23: mm edge +1.5% (below the 4% double-check bar) — hold ticket, no add"),
 dict(date="2026-07-20", cat="conference", team="Pittsburgh",  side="under", line=5.5, odds=-136, book="DK",    stake=0.65, result="pending", note="DK -136"),
 # 2026-07-26 placement round (plan: session of 07-24; BR unavailable — B365-heavy fills)
 dict(date="2026-07-26", cat="regular",    team="Wisconsin",      side="under", line=6.5, odds=+100, book="CZR",  stake=0.60, result="pending", note="rec 0.60 @ +100; exact fill"),
 dict(date="2026-07-26", cat="regular",    team="Florida",        side="under", line=6.5, odds=+144, book="DK",   stake=0.40, result="pending", note="off-market 6.5 (field 7.5); rec 0.60, sized 0.40; team total 0.90 w/ conf leg"),
 dict(date="2026-07-26", cat="regular",    team="Bowling Green",  side="over",  line=4.5, odds=-160, book="DK",   stake=0.35, result="pending", note="ADD; team total 1.05"),
 dict(date="2026-07-26", cat="conference", team="Arizona State",  side="under", line=4.5, odds=+115, book="DK",   stake=0.40, result="pending", note="beat +106 inference; reg-add leg skipped; team total 0.95"),
 dict(date="2026-07-26", cat="regular",    team="Buffalo",        side="over",  line=5.5, odds=-144, book="FD",   stake=0.75, result="pending", note="rec 0.45 — owner sized up; MAC cluster w/ BGSU (wk8 h2h)"),
 dict(date="2026-07-26", cat="regular",    team="UConn",          side="over",  line=5.5, odds=-106, book="FD",   stake=0.50, result="pending", note="ADD; team total 1.07"),
 dict(date="2026-07-26", cat="regular",    team="Tulsa",          side="over",  line=5.5, odds=-105, book="B365", stake=0.55, result="pending", note="ADD at backup book (CZR +100 gone); team total 1.10 = cap"),
 dict(date="2026-07-26", cat="regular",    team="Nevada",         side="over",  line=4.5, odds=+145, book="B365", stake=0.75, result="C", cashout_u=0.0, note="CLOSED 2026-08-03 free B365 cash-out (P&L 0.00u) after rejoin fix killed F2o, its only tag (gap +0.76->+0.46 was a flat-0.95 FCS artifact). Odds corrected +120->+145 per owner statement 2026-08-03 (original log said +120). MSU@NEV wk2 opener = re-entry trigger. Was: rec 0.65 — owner sized up; top conviction"),
 dict(date="2026-07-26", cat="regular",    team="Wake Forest",    side="over",  line=5.5, odds=-130, book="B365", stake=0.90, result="pending", note="rec 0.60 — owner sized up; backup price"),
 dict(date="2026-07-26", cat="regular",    team="Rutgers",        side="over",  line=4.5, odds=-140, book="B365", stake=0.80, result="pending", note="rec 0.60 — owner sized up; provenance note: ~60% of edge from v2 re-adjudication"),
 # ---------------------------------------------------------------------------
 # 2026-08-04 — S20 QB season passing-yards props (FanDuel, all -113 UNDER).
 # First money staked in the props program. Settlement basis STRICT-12 (owner
 # verified FD excludes CCGs). 'p' = the deep dive's final judgment-layer number
 # on that basis, NOT pricer_v2's mechanical price (both are in each DD header).
 # Owner sized up from the recommended 0.55u slate to 0.90u; recommendations kept
 # in each note. Carr (U2875.5, honest ~+5) was the recommended cut and was cut.
 # ---------------------------------------------------------------------------
 dict(date="2026-08-04", cat="prop", team="Julian Sayin (OSU) pass yds", side="under", line=3000.5, odds=-113, book="FD", stake=0.25, p=0.661, result="pending",
      note="S20 prop 1/5. rec 0.15u — owner sized up. p=.661 strict-12 (v2 mech .668 / .680 s12); "
           "Arthur Smith run-first OC = the board's only pro-under SCHEME signal, mu shaded 250.5->245; "
           "P(under|G=12)=.496 at the unshaded fit (desk anchored r=0.978 and shaded nothing). "
           "KILL: line <=2900.5 or juice past -125; att/g >=32 thru wk4; RB-room injury (watch). "
           "CORR: wk2 @Texas = direct vs Manning leg; wk10 hosts Oregon = direct vs Moore leg. "
           "CLV: wk0 + close. Provenance: DD_sayin_2026-08-04.md"),
 dict(date="2026-08-04", cat="prop", team="Drew Mestemaker (OKST) pass yds", side="under", line=3000.5, odds=-113, book="FD", stake=0.20, p=0.620, result="pending",
      note="S20 prop 2/5. rec 0.10u — owner sized up. p=.620 (range .62-.64, edge +9 to +11); v2 mech "
           ".717 — big haircut because the transfer hazard's job-loss mass (34% at g10<=4) does not apply "
           "to a $7M coach-brought QB: P(12+) .309 base -> .42 mine. P(under|G=12)=.445. mu 257 (fit + Ward "
           "256.8 precedent); leg dies above mu ~275 = the NT-offense-transplants scenario. "
           "KILL: line <=2900.5 or juice past -125; >=40 att/g or >270 yd/g thru wk3; wk2 vs Oregon >=300. "
           "Job loss pre-Week-1 = VOID not loss (FD >=1-snap rule). "
           "CORR: wk2 HOSTS Oregon = direct vs Moore leg; book overlap Tulsa O (+), WVU U / ASU U (-). "
           "CLV: wk0 + close. Provenance: DD_mestemaker_2026-08-04.md"),
 dict(date="2026-08-04", cat="prop", team="Dante Moore (ORE) pass yds", side="under", line=2850.5, odds=-113, book="FD", stake=0.15, p=0.612, result="pending",
      note="S20 prop 3/5. rec 0.10u — owner sized up. p=.612 strict-12 (+8.2; CCG-incl basis was .600/+6.1); "
           "v2 mech .660. Crux is program-vs-player pace: fit prices Moore's own 227.8, Oregon QB1s ran "
           "274-319 — but those were 5th/6th-yr veterans; central mu 245. P(under|G=12)=.487, P(12+)=.52. "
           "KILL: line <=2750.5 or juice past -125; att/g >=31 thru wk4; wk4 @USC >=320 (with volume = kill). "
           "Raiola (QB2) exit = downgrade. CORR: wk2 @Oklahoma State (Mestemaker) AND wk10 @Ohio State "
           "(Sayin) — the only leg with two direct cross-leg games; floor-sized for that reason. "
           "CLV: wk0 + close. Provenance: DD_moore_2026-08-04.md"),
 dict(date="2026-08-04", cat="prop", team="Gunner Stockton (UGA) pass yds", side="under", line=2650.5, odds=-113, book="FD", stake=0.15, p=0.604, result="pending",
      note="S20 prop 4/5. rec 0.10u — owner sized up. p=.604 strict-12 (+7.4; CCG-incl was +4.9 — the widest "
           "CCG sensitivity on the slate, resolved in our favor). v1 said .633 before the pace-level "
           "correction that this dive found. Pure availability bet: P(under|G=12+)=.32. Recheck 2026-08-04 "
           "reaffirmed; added datum = played through a mid-season oblique in '25 (plus resolved spring knee). "
           "KILL: line <=2600.5 or price past -125; att/g >34 thru wk3; Puglisi transfers out. "
           "CORR: none (no direct game vs another leg). CLV: wk0 + close. Provenance: DD_stockton_2026-08-04.md"),
 dict(date="2026-08-04", cat="prop", team="Arch Manning (TEX) pass yds", side="under", line=2850.5, odds=-113, book="FD", stake=0.15, p=0.600, result="pending",
      note="S20 prop 5/5. rec 0.10u — owner sized up. p=.600 strict-12 (+7.0); v2 mech .628/.636. Hazard "
           "shaded DOWN to P(12+)=.44 on the web find the frozen dossier missed: Jan-2026 foot surgery "
           "(cleared 5/16) + a 2025 in-season concussion, on 399 rush yds, with E[blowout wins] 4.32 = the "
           "LOWEST mop-up slate on the board. P(under|G=12)=.432. H1/H2 split 207.0 vs 298.6 = widest mu "
           "band on the slate; season-raw pace governs (H3). "
           "KILL: line <=2750.5 or juice past -125; att/g >=34 thru wk4; two straight 320+ games. "
           "REVERSE: any foot/concussion recurrence is a HOLD-or-ADD, not a kill (>=1-snap rule means a "
           "mid-season miss cashes; only a pre-Week-1 season rule-out voids). "
           "CORR: wk2 HOSTS Ohio State = direct vs Sayin leg; book overlap Florida U reg+conf (+). "
           "CLV: wk0 + close. Provenance: DD_manning_2026-08-04.md"),
]

P = json.load(open('outputs/win_totals_payload.json'))
teams=P['teams']; sched=P['schedules']; fcs=P['fcs']
NAME2NK={t['name']:nk for nk,t in teams.items()}
def cal(nk):return teams[nk]['calibrated']
def oppR(r):return teams[r]['calibrated'] if r in teams else fcs[r]['rating']  # AUDIT D4 (2026-08-02): FCS raw — the 0.75 shrink was calibrated under the raw-FCS convention; all lenses now unified on raw
def oppB(r):return teams[r]['band'] if r in teams else fcs[r]['band']
def model_prob(team, cat, side, line):
    nk=NAME2NK[team]; conf=(cat=='conference')
    gl=[{'mu_opp':oppR(g['opp_ref']),'site':g['site'],'band_opp':oppB(g['opp_ref'])}
        for g in sched[nk] if (g['is_conf'] or not conf)]
    d=E.win_distribution(cal(nk),teams[nk]['band'],gl)['dist']
    p_over=sum(d[math.floor(line)+1:])
    return p_over if side=='over' else 1-p_over
def dec(a):return 1.0+(a/100.0 if a>0 else 100.0/(-a))
def profit_mult(a):return dec(a)-1.0
def implied(a):return (-a)/((-a)+100.0) if a<0 else 100.0/(a+100.0)
def ufo(o,c=30):  # AUDIT FIX 2026-08-02: correct +/-100 ladder crossing
    return (-o-c) if o<=-(100+c) else (-((200+c)-abs(o)) if o<0 else -(o+c))
M=_market()
def market_fair(team, cat, line, side):
    """Market's de-vigged fair probability of the bet side at the line (avg-prob de-vig
    across books, 30-cent convention for the unposted side). None if no market."""
    offers=M.get(team,{}).get('regular' if cat=='regular' else 'conference',[])
    if not offers: return None
    at=[o for (l,o,b) in offers if abs(l-line)<1e-6]
    if not at:
        cl=consensus_line([l for (l,o,b) in offers]); at=[o for (l,o,b) in offers if abs(l-cl)<1e-6]
    fps=[implied(o)/(implied(o)+implied(ufo(o))) for o in at]
    fo=sum(fps)/len(fps)
    return fo if side=='over' else 1-fo

rows=[]
for b in SEED:
    if b['cat']=='prop':
        # props: p is supplied by the deep dive; edge is vs the breakeven of the price
        # taken (no opposing quote captured, so no de-vigged fair is available).
        p=b['p']; edge=p-implied(b['odds'])
    else:
        p=model_prob(b['team'],b['cat'],b['side'],b['line'])
        mf=market_fair(b['team'],b['cat'],b['line'],b['side'])
        edge=(p-mf) if mf is not None else None
    ev=p*profit_mult(b['odds'])-(1-p)
    if b['result']=='W':   pnl=b['stake']*profit_mult(b['odds'])
    elif b['result']=='L': pnl=-b['stake']
    elif b['result']=='C': pnl=b.get('cashout_u', 0.0)
    else:                  pnl=0.0
    rows.append({**b,'our_p':round(p,4),'ev':round(ev,4),'edge':(round(edge,4) if edge is not None else None),'pnl':round(pnl,4)})

# CSV
os.makedirs('outputs',exist_ok=True)
with open('outputs/bet_tracker.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['date','category','team','side','line','odds','book','stake_u','our_p','pct_edge','model_ev','result','pnl_u','note'])
    for r in rows:
        w.writerow([r['date'],r['cat'],r['team'],r['side'],r['line'],
                    ('+%d'%r['odds'] if r['odds']>0 else r['odds']),r['book'],r['stake'],
                    '%.3f'%r['our_p'],('%+.1f%%'%(100*r['edge']) if r['edge'] is not None else 'n/a'),
                    '%+.3f'%r['ev'],r['result'],'%+.3f'%r['pnl'],r['note']])

# summary
n=len(rows); staked=sum(r['stake'] for r in rows)
graded=[r for r in rows if r['result'] in ('W','L','P','C')]
wins=sum(r['result']=='W' for r in rows); losses=sum(r['result']=='L' for r in rows)
pnl=sum(r['pnl'] for r in rows); risked_g=sum(r['stake'] for r in graded)
roi=(pnl/risked_g*100) if risked_g else None
avg_p=sum(r['our_p'] for r in rows)/n; avg_ev=sum(r['ev'] for r in rows)/n
_ed=[r['edge'] for r in rows if r['edge'] is not None]; avg_edge=(sum(_ed)/len(_ed)) if _ed else None

def odds_str(a):return ('+%d'%a) if a>0 else str(a)
def esc(s):return html.escape(str(s))
CARD=lambda label,val,sub='': f'<div class="kpi"><div class="l">{label}</div><div class="v">{val}</div><div class="s">{sub}</div></div>'
kpis=(CARD("Bets",n,f"{len(graded)} graded")+CARD("Staked",f"{staked:.2f}u")+
      CARD("Record",f"{wins}–{losses}", "pending" if not graded else "")+
      CARD("Net P&amp;L",f"{pnl:+.2f}u", ("—" if roi is None else f"ROI {roi:+.1f}%"))+
      CARD("Avg % edge",("—" if avg_edge is None else f"{avg_edge*100:+.1f}%"),"vs market fair")+
      CARD("Avg model EV",f"{avg_ev:+.2f}/$1"))
trs=""
for r in sorted(rows,key=lambda x:(x['cat'],-x['ev'])):
    cls={'W':'win','L':'loss','P':'push','C':'push'}.get(r['result'],'pend')
    res={'W':'WON','L':'LOST','P':'PUSH','C':'CLOSED','pending':'pending'}[r['result']]
    trs+=(f'<tr class="{cls}"><td>{esc(r["date"])}</td><td><span class="chip {r["cat"][:4]}">{r["cat"][:4]}</span></td>'
          f'<td class="bet">{esc(r["team"])} <b>{r["side"]} {r["line"]:g}</b></td>'
          f'<td>{odds_str(r["odds"])}</td><td class="mut">{esc(r["book"]) or "—"}</td><td>{r["stake"]:.2f}u</td>'
          f'<td>{r["our_p"]*100:.0f}%</td>'
          f'<td class="{"pos" if (r["edge"] or 0)>0 else "neg"}">{("%+.1f%%"%(100*r["edge"])) if r["edge"] is not None else "—"}</td>'
          f'<td class="{"pos" if r["ev"]>0 else "neg"}">{r["ev"]:+.2f}</td>'
          f'<td class="res">{res}</td><td>{r["pnl"]:+.2f}u</td><td class="mut">{esc(r["note"])}</td></tr>')

HTML=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CFB 2026 · Bet Tracker</title><style>
:root{{--bg:#0e1116;--panel:#171b22;--pan2:#1e242e;--line:#2a3240;--ink:#e6e9ef;--dim:#9aa4b2;--acc:#4f9dff;--good:#37c98b;--bad:#ff6b6b;--warn:#ffb454;--chip:#232b36}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding:20px 18px 48px}}
h1{{font-size:19px;margin:0 0 2px}} .sub{{color:var(--dim);font-size:12.5px;margin-bottom:16px}}
.kpis{{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin:12px 0 18px}}
.kpi{{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:11px 13px}}
.kpi .l{{color:var(--dim);font-size:11px}} .kpi .v{{font-size:20px;font-weight:700;margin-top:2px}} .kpi .s{{color:var(--dim);font-size:11px}}
table{{border-collapse:collapse;width:100%;font-size:12.5px;background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}}
th{{color:var(--dim);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.4px;background:var(--pan2)}}
td.bet{{white-space:normal}} .mut{{color:var(--dim)}} .pos{{color:var(--good)}} .neg{{color:var(--bad)}}
tr.win{{background:rgba(55,201,139,.07)}} tr.loss{{background:rgba(255,107,107,.07)}}
tr.win .res{{color:var(--good);font-weight:700}} tr.loss .res{{color:var(--bad);font-weight:700}} tr.pend .res{{color:var(--dim)}}
.chip{{display:inline-block;background:var(--chip);border:1px solid var(--line);border-radius:5px;padding:1px 6px;font-size:10px;color:var(--dim)}}
.chip.conf{{color:var(--acc)}} .chip.prop{{color:var(--warn)}} .foot{{color:var(--dim);font-size:11.5px;margin-top:14px}}
</style></head><body><div class="wrap">
<h1>CFB 2026 · Bet Tracker</h1><div class="sub">Season win totals, conference win totals &amp; QB season passing-yard props · ratings as of {ASOF} · all bets settle after the regular season</div>
<div class="kpis">{kpis}</div>
<table><thead><tr><th>Logged</th><th></th><th>Bet</th><th>Odds</th><th>Book</th><th>Stake</th><th>Model P</th><th>% edge</th><th>EV/$1</th><th>Result</th><th>P&amp;L</th><th>Note</th></tr></thead>
<tbody>{trs}</tbody></table>
<div class="foot"><b>Win totals</b> (reg/conf): Model P = our <b>calibrated</b> ratings&rsquo; win probability for the side (the honest &times;0.75 set); <b>% edge</b> = model P &minus; the market&rsquo;s de-vigged fair probability (how much sharper our number is).<br>
<b>Props</b>: Model P is the deep dive&rsquo;s final judgment-layer probability (pricer&nbsp;v2 mechanical price plus that dive&rsquo;s hazard/&mu; overlay), and <b>% edge</b> is measured against the <b>breakeven of the price taken</b> (.5305 at &minus;113), not a de-vigged fair &mdash; the opposing quote was never captured. Provenance for each prop row is the DD file named in its note. Settlement is strict-12 (FD excludes conference championship games), and FD&rsquo;s &ge;1-snap action rule means a never-played season <b>voids</b> rather than loses.<br>
<b>EV/$1</b> = expected profit per $1 at the price you took. P&amp;L updates as bets grade. Maintained by Claude &mdash; tell me when you log or settle a bet.</div>
</div></body></html>'''
open('outputs/bet_tracker.html','w').write(HTML)
print(f"tracker: {n} bets, {staked:.2f}u staked, avg model P {avg_p*100:.0f}%, avg EV {avg_ev:+.2f}, record {wins}-{losses}, P&L {pnl:+.2f}u")
print("wrote outputs/bet_tracker.csv + outputs/bet_tracker.html")
