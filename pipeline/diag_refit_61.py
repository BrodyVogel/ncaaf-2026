import json, glob, numpy as np, statistics as st

OFF, DEF = ["QB","RB","WRTE","OL"], ["DL","LB","DB"]
A = json.load(open('outputs/anchor_runs/anchor_run_2026-07-14_class0.json'))['teams']

# Assemble the 61 real-graded teams
teams=[]
for p in glob.glob('snapshots/*/grades.json'):
    tdir=p.split('/')[1]
    g=json.load(open(p))['units']
    meta=json.load(open(f'snapshots/{tdir}/META.json'))
    # map dir -> anchor-run key (space form)
    name=meta['team']
    if name not in A: 
        print('MISS', name); continue
    teams.append(dict(dir=tdir, name=name, conf=meta.get('conference','?'),
                      g={u:g[u]['grade'] for u in g},
                      off=A[name]['off'], dfn=A[name]['dfn'], blend=A[name]['blend'], p4=A[name]['p4']))
print(f'assembled {len(teams)} real-graded teams')

def ols(X,y):
    b,*_=np.linalg.lstsq(X,y,rcond=None); return b, y-X@b

def fit(rows, conf_dummy=False):
    n=len(rows); ones=np.ones(n)
    confs=sorted(set(r['conf'] for r in rows))
    def design(units):
        cols=[ones]+[np.array([r['g'][u] for r in rows]) for u in units]
        if conf_dummy:
            # drop first conf as baseline
            for c in confs[1:]:
                cols.append(np.array([1.0 if r['conf']==c else 0.0 for r in rows]))
        return np.column_stack(cols)
    Xo,Xd=design(OFF),design(DEF)
    yo=np.array([r['off'] for r in rows]); yd=np.array([r['dfn'] for r in rows])
    bo,ro=ols(Xo,yo); bd,rd=ols(Xd,yd)
    r2o=1-ro.var()/yo.var(); r2d=1-rd.var()/yd.var()
    io=Xo@bo; idf=Xd@bd
    resid=(io-yo)-(idf-yd)
    return dict(bo=bo,bd=bd,r2o=r2o,r2d=r2d,resid=resid,confs=confs,rows=rows)

# --- FIT A: real-grade refit, no conf dummy ---
fa=fit(teams,conf_dummy=False)
print(f"\n=== FIT A (real-grade, no conf dummy): R2 off {fa['r2o']:.2f} def {fa['r2d']:.2f} ===")
byc={}
for r,res in zip(teams,fa['resid']): byc.setdefault(r['conf'],[]).append(res)
for c in sorted(byc, key=lambda c:st.mean(byc[c])):
    print(f"  {c:<18} n={len(byc[c]):>2}  mean resid {st.mean(byc[c]):+6.2f}  (min {min(byc[c]):+.1f} max {max(byc[c]):+.1f})")
print(f"  GLOBAL mean resid {st.mean(fa['resid']):+.3f} (≈0 by construction)")

# --- FIT B: with conference dummies ---
fb=fit(teams,conf_dummy=True)
print(f"\n=== FIT B (real-grade + conf dummies): R2 off {fb['r2o']:.2f} def {fb['r2d']:.2f} ===")
confs=fb['confs']
# conf dummy coefficients: after intercept + unit slopes. off design: 1 + 4 units + (k-1) confs
noff=1+len(OFF); ndef=1+len(DEF)
print("  conf effect on ANCHOR margin held-grades-fixed (baseline =",confs[0],"):")
for i,c in enumerate(confs[1:]):
    # margin effect = off_dummy - def_dummy (def is points-allowed; margin=off-dfn)
    coff=fb['bo'][noff+i]; cdef=fb['bd'][ndef+i]
    print(f"    {c:<18} off {coff:+6.2f}  def {cdef:+6.2f}  -> anchor-margin effect {coff-cdef:+6.2f}")

print("\n"+"="*70)
print("LEVEL SLOPE refit (the object driving 'shape')")
# current: level = -0.541 * anchor_margin ; shape = resid - level
# refit slope on 61 real teams: regress resid on anchor_margin (with intercept)
margin=np.array([r['off']-r['dfn'] for r in teams])
resid=fa['resid']
Xl=np.column_stack([np.ones(len(teams)), margin])
bl,_=ols(Xl,resid)
print(f"  refit-61: resid = {bl[0]:+.2f} + {bl[1]:+.3f} * anchor_margin   (current fixed slope -0.541, intercept 0)")
# R2 of the level model
pred=Xl@bl; ss=1-((resid-pred).var()/resid.var())
print(f"  level-model R2 on 61: {ss:.2f}  (share of resid variance explained by anchor level)")

print("\n  MAC 'shape' under CURRENT (-0.541,0) vs REFIT-61 slope:")
print(f"  {'team':<18} {'anchor_marg':>11} {'raw_resid':>9} {'shape_cur':>9} {'shape_refit':>11}")
macrows=[(r,res) for r,res in zip(teams,fa['resid']) if r['conf']=='Mid-American']
cur_sh=[]; ref_sh=[]
for r,res in sorted(macrows,key=lambda x:x[0]['off']-x[0]['dfn']):
    m=r['off']-r['dfn']
    sh_cur=res-(-0.541*m)
    sh_ref=res-(bl[0]+bl[1]*m)
    cur_sh.append(sh_cur); ref_sh.append(sh_ref)
    print(f"  {r['name']:<18} {m:>11.2f} {res:>9.2f} {sh_cur:>9.2f} {sh_ref:>11.2f}")
print(f"  MAC mean shape: current {st.mean(cur_sh):+.2f}  ->  refit-61 {st.mean(ref_sh):+.2f}")

print("\n"+"="*70)
print("ORDERING preservation (within-MAC), proxy-fit vs real-refit resid")
proxy_resid={'Toledo':-12.13,'Ohio':-5.48,'Western Michigan':-4.55,'Miami (OH)':-3.55,
 'Central Michigan':1.39,'Sacramento State':1.42,'Buffalo':0.48,'Eastern Michigan':3.07,
 'Bowling Green':3.79,'Akron':4.23,'Kent State':5.50,'Ball State':2.41,'Massachusetts':13.06}
realr={r['name']:res for r,res in zip(teams,fa['resid']) if r['conf']=='Mid-American'}
import numpy as _np
pr=[proxy_resid[n] for n in realr]; rr=[realr[n] for n in realr]
names=list(realr)
order_p=sorted(names,key=lambda n:proxy_resid[n])
order_r=sorted(names,key=lambda n:realr[n])
print("  proxy-fit worst->best:", ' '.join(n[:4] for n in order_p))
print("  real-fit  worst->best:", ' '.join(n[:4] for n in order_r))
print(f"  Spearman rank corr: {_np.corrcoef(_np.argsort(_np.argsort(pr)),_np.argsort(_np.argsort(rr)))[0,1]:.2f}")
