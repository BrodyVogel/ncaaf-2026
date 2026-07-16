import json, csv, glob, numpy as np, statistics as st, re

def norm(s):
    s=s.lower().strip()
    s=re.sub(r'\bst\.?\b','state',s); s=re.sub(r'[^a-z0-9]','',s)
    for a,b in [('stateate','state')]: s=s.replace(a,b)
    return s

P4={'SEC','Big Ten','Big 12','ACC','Pac-12'}
rows=[]
for yr in [2021,2022,2023,2024,2025]:
    pre={}
    for r in csv.DictReader(open(f'data/backtest/sp_preseason/SP+_{yr}_preseason.csv')):
        pre[norm(r['team_raw'])]=float(r['sp_plus_overall'])
    fin={}; conf={}
    for r in json.load(open(f'data/cfbd/2026-07-12/sp_{yr}.json')):
        if r.get('rating') is None: continue
        fin[norm(r['team'])]=r['rating']; conf[norm(r['team'])]=r.get('conference','')
    ret={}
    for r in json.load(open(f'data/cfbd/2026-07-12/returning_{yr}.json')):
        if r.get('percentPPA') is None: continue
        ret[norm(r['team'])]=r['percentPPA']
    keys=set(pre)&set(fin)&set(ret)
    for k in keys:
        rows.append(dict(yr=yr,team=k,pre=pre[k],fin=fin[k],rp=ret[k],
                         conf=conf.get(k,''),g5=conf.get(k,'') not in P4 and conf.get(k,'')!=''))
print(f"matched {len(rows)} team-seasons across 2021-2025")
delta=np.array([r['fin']-r['pre'] for r in rows])   # + = finished ABOVE preseason
rp=np.array([r['rp'] for r in rows])
print(f"overall corr(returning production, final-minus-preseason): {np.corrcoef(rp,delta)[0,1]:+.3f}")
# regression delta ~ rp
b=np.polyfit(rp,delta,1)
print(f"  slope: {b[0]:+.2f} SP+ pts per unit returning-production (rp in 0..1)")

# G5 subset
g5=[r for r in rows if r['g5']]
gd=np.array([r['fin']-r['pre'] for r in g5]); grp=np.array([r['rp'] for r in g5])
print(f"\nG5 only (n={len(g5)}): corr {np.corrcoef(grp,gd)[0,1]:+.3f}, slope {np.polyfit(grp,gd,1)[0]:+.2f}")

# THE key test: low-RP (churned) teams — do they finish below preseason?
def tail(rows,lab,thresh):
    lo=[r for r in rows if r['rp']<thresh]
    d=[r['fin']-r['pre'] for r in lo]
    print(f"  {lab}: n={len(d)}  mean(final-preseason)={st.mean(d):+.2f}  median={st.median(d):+.2f}  %below={100*sum(1 for x in d if x<0)/len(d):.0f}%")
print("\nLOW returning-production tail (did preseason SP+ over-rate them?):")
q10=np.percentile(rp,10); q25=np.percentile(rp,25)
tail(rows,f"all, rp<{q25:.2f} (bottom quartile)",q25)
tail(rows,f"all, rp<{q10:.2f} (bottom decile)",q10)
tail(g5, f"G5,  rp<{np.percentile(grp,25):.2f} (G5 bottom quartile)",np.percentile(grp,25))
print("\nHIGH returning-production tail (control):")
tail(rows,f"all, rp>{np.percentile(rp,75):.2f} (top quartile)",1e9) if False else None
hi=[r for r in rows if r['rp']>np.percentile(rp,75)]
d=[r['fin']-r['pre'] for r in hi]
print(f"  all, rp>{np.percentile(rp,75):.2f} (top quartile): n={len(d)} mean {st.mean(d):+.2f} %below {100*sum(1 for x in d if x<0)/len(d):.0f}%")
