#!/usr/bin/env python3
"""Band tail diagnostic (2026-07-15, user variance-clustering question):
does EXTREME roster churn predict larger preseason-anchor miss SD?
Panel: real preseason SP+ vs final SP+, 2021-2025 (n=656), same loaders as step2.
Cells: within-year returning-production deciles; 'Memphis cell' = coach change +
bottom-quartile RP; 'Army cell' = no change + top-quartile RP; bottom-5% RP tail.
Result (run 2026-07-15): SD flat across churn - bottom decile ratio 0.98;
Memphis-vs-Army cell 1.09 [0.89, 1.32]; bottom-5% 1.03 [0.81, 1.22].
1.5-2x churn multipliers are rejected by 5 years of data. Churn shows up as a
small MEAN effect (Memphis cell -2.13, t~-2.0), not a variance effect.
"""
import csv, importlib.util, sys
import numpy as np
sys.path.insert(0, "pipeline")
spec = importlib.util.spec_from_file_location("s2", "pipeline/step2_backtest_v2.py")
s2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s2)

def main():
    cfbd = "data/cfbd/2026-07-12"
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    primary, _ = s2.coach_meta(cfbd, range(2014, 2026))
    rows = []
    for y in range(2021, 2026):
        pre, fin, ret = s2.load_pre("data/backtest/sp_preseason", y, n2c), s2.load_final(cfbd, y), s2.load_ret(cfbd, y)
        for t in pre:
            if t not in fin or t not in ret: continue
            cc = 1 if (primary.get((t, y)) and primary.get((t, y-1)) and primary[(t, y)] != primary[(t, y-1)]) else 0
            rows.append(dict(year=y, miss=fin[t]["overall"] - pre[t]["overall"], ret=ret[t], cc=cc))
    miss = np.array([r["miss"] for r in rows]); ret = np.array([r["ret"] for r in rows])
    dec = np.zeros(len(rows), int)
    for y in range(2021, 2026):
        idx = [i for i, r in enumerate(rows) if r["year"] == y]
        qs = np.quantile(ret[idx], np.arange(.1, 1, .1))
        for i in idx: dec[i] = int(np.searchsorted(qs, ret[i]))
    def boot(a, b, B=4000, seed=7):
        rng = np.random.default_rng(seed)
        return np.percentile([rng.choice(a, len(a)).std() / rng.choice(b, len(b)).std() for _ in range(B)], [2.5, 50, 97.5])
    print(f"n={len(rows)} SD={miss.std():.2f}")
    for d in range(10): print(f"decile {d}: SD={miss[dec==d].std():.2f} mean={miss[dec==d].mean():+.2f} n={(dec==d).sum()}")
    print("bottom decile vs rest:", miss[dec==0].std()/miss[dec>0].std(), boot(miss[dec==0], miss[dec>0]))
    ymap = {y: i for i, y in enumerate(range(2021, 2026))}
    q25 = [np.quantile(ret[[i for i,r in enumerate(rows) if r['year']==y]], .25) for y in range(2021, 2026)]
    q75 = [np.quantile(ret[[i for i,r in enumerate(rows) if r['year']==y]], .75) for y in range(2021, 2026)]
    mem = miss[np.array([(r["cc"]==1) and (r["ret"]<=q25[ymap[r["year"]]]) for r in rows])]
    army = miss[np.array([(r["cc"]==0) and (r["ret"]>=q75[ymap[r["year"]]]) for r in rows])]
    print(f"Memphis cell SD={mem.std():.2f} mean={mem.mean():+.2f} n={len(mem)}; Army cell SD={army.std():.2f} n={len(army)}; ratio={mem.std()/army.std():.2f}", boot(mem, army))

if __name__ == "__main__":
    main()
