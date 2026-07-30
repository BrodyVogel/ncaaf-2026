import csv, json, math, re, unicodedata, os
from collections import defaultdict
import numpy as np
os.chdir('/home/claude/cfb-2026-power-ratings')
def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).encode('ascii','ignore').decode()
    return re.sub(r'[^a-z0-9]','',s.lower())
AL={'connecticut':'uconn'}
def rd(p,c): return {AL.get(r['norm_key'],r['norm_key']):float(r[c]) for r in csv.DictReader(open(p))}
rp={}; full={}
for y in range(2022,2026):
    for e in json.load(open(f'data/cfbd/2026-07-12/returning_{y}.json')):
        ks=[k for k in e if 'percent' in k.lower()]
        v=e.get('percentPPA', e.get(ks[0]) if ks else None)
        if v is not None: rp[(y,norm(e['team']))]=float(v)
        full[(y,norm(e['team']))]=e
pre={y:rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv','sp_plus_overall') for y in (2022,2023,2024)}
games={y:json.load(open(f'data/cfbd/2026-07-12/games_{y}_regular.json')) for y in (2022,2023,2024)}
def phi(x): return 0.5*(1+math.erf(x/math.sqrt(2)))
def sched_exp(tk,y,rat):
    ew=0.0
    for g in games[y]:
        h,a=norm(g['homeTeam']),norm(g['awayTeam'])
        if tk not in (h,a): continue
        opp=a if tk==h else h
        if opp not in rat: ew+=0.95; continue
        site=0.0 if g.get('neutralSite') else (1.0 if tk==h else -1.0)
        ew+=phi((rat[tk]-rat[opp]+2.3*site)/13.5)
    return ew
def wins(tk,y):
    w=0
    for g in games[y]:
        h,a=norm(g['homeTeam']),norm(g['awayTeam'])
        if tk not in (h,a) or g.get('homePoints') is None: continue
        mine=g['homePoints'] if tk==h else g['awayPoints']; their=g['awayPoints'] if tk==h else g['homePoints']
        w+=int(mine>their)
    return w
for lab in ('L1','L2'):
    res={'c':[],'k':[]}; zone={'c':[0,0],'k':[0,0]}
    for y in (2022,2023,2024):
        ymean=np.mean([rp[(y,t)] for t in pre[y] if (y,t) in rp])
        q1,q2=np.quantile(list(pre[y].values()),[1/3,2/3])
        adj={}
        for t in pre[y]:
            term=3.28*(rp.get((y,t),ymean)-ymean)
            use = True if lab=='L1' else (q1<=pre[y][t]<q2)
            adj[t]=pre[y][t]+(term if use else 0.0)
        for r in csv.DictReader(open(f'data/win_totals/sbd_historical/sbd_{y}.csv')):
            tk=AL.get(norm(r['team']),norm(r['team']))
            if tk not in pre[y]: continue
            line=float(r['line']); W=wins(tk,y)
            for key,rat in (('c',pre[y]),('k',adj)):
                e=sched_exp(tk,y,rat); res[key].append(abs(e-W))
                if abs(e-line)>=1.0 and W!=line:
                    zone[key][0]+=int((e>line)==(W>line)); zone[key][1]+=1
    mc,mk=np.mean(res['c']),np.mean(res['k'])
    zc=zone['c'][0]/zone['c'][1]; zk=zone['k'][0]/zone['k'][1] if zone['k'][1] else float('nan')
    ok = mk<mc and zk>=zc-0.05
    print(f'{lab}: MAE {mc:.3f}->{mk:.3f} | zone {100*zc:.1f}% (n={zone["c"][1]}) -> {100*zk:.1f}% (n={zone["k"][1]}) | {"PASS" if ok else "FAIL"}')
missP={}; sppP={}
for y in range(2022,2026):
    p=rd(f'data/backtest/sp_preseason/SP+_{y}_preseason.csv','sp_plus_overall')
    f_=rd(f'data/backtest/sp_final/SP+_{y}_final.csv','final_overall')
    for t in p:
        if t in f_: missP[(y,t)]=f_[t]-p[t]; sppP[(y,t)]=p[t]
sample=list(full.values())[0]
print('percent fields:', [k for k in sample if 'percent' in k.lower()])
rows=[]
for (y,t),m in missP.items():
    e=full.get((y,t))
    if not e: continue
    vals=[e.get(k) for k in ('percentPassingPPA','percentReceivingPPA','percentRushingPPA')]
    if any(v is None for v in vals): continue
    rows.append((m,sppP[(y,t)],*[float(v) for v in vals],y))
A=np.array(rows)
def ols(X,yv):
    M=np.column_stack([np.ones(len(yv))]+X); b,*_=np.linalg.lstsq(M,yv,rcond=None)
    r=yv-M@b; cov=(r@r/(len(yv)-M.shape[1]))*np.linalg.pinv(M.T@M)
    return b,b/np.sqrt(np.diag(cov))
if len(A):
    b,t=ols([A[:,1],A[:,2],A[:,3],A[:,4]],A[:,0])
    print(f'L3 n={len(A)}: pass {b[2]:+.2f} (t {t[2]:+.2f}) | recv {b[3]:+.2f} (t {t[3]:+.2f}) | rush {b[4]:+.2f} (t {t[4]:+.2f})')
    for y in (2022,2023,2024,2025):
        m=A[:,5]!=y
        bb,tt=ols([A[m,1],A[m,2],A[m,3],A[m,4]],A[m,0])
        print(f'  drop {int(y)}: pass {bb[2]:+.2f}({tt[2]:+.1f}) recv {bb[3]:+.2f}({tt[3]:+.1f}) rush {bb[4]:+.2f}({tt[4]:+.1f})')
else: print('L3 unavailable')
