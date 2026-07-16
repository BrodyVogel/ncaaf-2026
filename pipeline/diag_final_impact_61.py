import json, glob, numpy as np, statistics as st
OFF, DEF = ["QB","RB","WRTE","OL"], ["DL","LB","DB"]
K, CAP = 0.35, 6.0
A = json.load(open('outputs/anchor_runs/anchor_run_2026-07-14_class0.json'))['teams']
proxy = json.load(open('data/backtest/shadow_proxy_2026.json'))['grades']

# 61 real-graded teams
teams=[]
for p in glob.glob('snapshots/*/grades.json'):
    tdir=p.split('/')[1]; g=json.load(open(p))['units']
    name=json.load(open(f'snapshots/{tdir}/META.json'))['team']
    if name not in A: continue
    conf=json.load(open(f'snapshots/{tdir}/META.json')).get('conference','?')
    teams.append(dict(name=name,conf=conf,g={u:g[u]['grade'] for u in g},
                      off=A[name]['off'],dfn=A[name]['dfn'],blend=A[name]['blend']))
def ols(X,y): b,*_=np.linalg.lstsq(X,y,rcond=None); return b

def conv_fit(grade_source):
    # grade_source: 'proxy' (fit on ALL proxy teams in A) or 'real' (fit on the 61)
    if grade_source=='proxy':
        src=[t for t in proxy if t in A]
        gg={t:{u:(proxy[t][u] if proxy[t][u] is not None else 50) for u in proxy[t]} for t in src}
    else:
        src=[t['name'] for t in teams]
        gg={t['name']:t['g'] for t in teams}
    ones=np.ones(len(src))
    Xo=np.column_stack([ones]+[[gg[t][u] for t in src] for u in OFF])
    Xd=np.column_stack([ones]+[[gg[t][u] for t in src] for u in DEF])
    yo=np.array([A[t]['off'] for t in src]); yd=np.array([A[t]['dfn'] for t in src])
    return ols(Xo,yo), ols(Xd,yd)

def finals(bo,bd):
    out={}
    for t in teams:
        io=np.array([1.0]+[t['g'][u] for u in OFF])@bo
        idf=np.array([1.0]+[t['g'][u] for u in DEF])@bd
        resid=(io-t['off'])-(idf-t['dfn'])
        adj=float(np.clip(K*resid,-CAP,CAP))
        stt=(t['g']['ST']-50)/50*1.0
        out[t['name']]=dict(resid=resid, raw=t['blend']+adj+stt)
    shift=st.mean(v['raw'] for v in out.values())
    for n in out: out[n]['final']=out[n]['raw']-shift
    return out

bo_p,bd_p=conv_fit('proxy'); bo_r,bd_r=conv_fit('real')
Fp=finals(bo_p,bd_p); Fr=finals(bo_r,bd_r)

print("MAC: final under proxy-fit conversion vs real-grade refit (same 61-team field)")
print(f"{'team':<18}{'blend':>7}{'resid_px':>9}{'resid_re':>9}{'final_px':>9}{'final_re':>9}{'Δfinal':>8}")
macd=[]
for t in sorted([x for x in teams if x['conf']=='Mid-American'],key=lambda x:Fr[x['name']]['final'],reverse=True):
    n=t['name']; d=Fr[n]['final']-Fp[n]['final']; macd.append(d)
    print(f"{n:<18}{t['blend']:>7.2f}{Fp[n]['resid']:>9.2f}{Fr[n]['resid']:>9.2f}{Fp[n]['final']:>9.2f}{Fr[n]['final']:>9.2f}{d:>+8.2f}")
print(f"\nMAC mean |Δfinal| = {st.mean(abs(x) for x in macd):.2f}   MAC mean Δfinal = {st.mean(macd):+.2f}   max |Δ| = {max(abs(x) for x in macd):.2f}")
alld=[Fr[t['name']]['final']-Fp[t['name']]['final'] for t in teams]
print(f"ALL 61 mean |Δfinal| = {st.mean(abs(x) for x in alld):.2f}   max |Δ| = {max(abs(x) for x in alld):.2f}")
# does MAC move RELATIVE to field? compare MAC mean final both ways
macfp=st.mean(Fp[t['name']]['final'] for t in teams if t['conf']=='Mid-American')
macfr=st.mean(Fr[t['name']]['final'] for t in teams if t['conf']=='Mid-American')
print(f"\nMAC mean FINAL: proxy-fit {macfp:+.2f}  ->  real-refit {macfr:+.2f}   (shift {macfr-macfp:+.2f})")
