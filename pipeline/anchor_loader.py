#!/usr/bin/env python3
"""Anchor loader (compute phase): captures -> normalized -> robust blended anchor.

Per PARAMETERS.json (ratified): weights SP+ 2.0, FEI/Massey/FPI/TR 1.0, Pick Six 1.0
(P4-only, ordinal -> order-statistic conversion onto the partial-blend P4 slice);
z-normalization onto SP+ scale; winsorize any source > 5 pts from the median of the
OTHERS (logged); per-team dispersion + top-decile flag; per-run class term
per_side = (3.49 - blend_tilt)/2; O/D split via SP+ component shape.

Usage: python3 anchor_loader.py <out_json>
Writes full per-source detail per team (raw, normalized, winsorized) for build sheets.
"""
import csv, json, sys, os, datetime
import numpy as np

D = "data/cfbd/2026-07-12"
P4 = {"SEC", "Big Ten", "Big 12", "ACC"}
WEIGHTS = {"SP+": 2.0, "FEI": 1.0, "Massey": 1.0, "FPI": 1.0, "TR": 1.0, "PickSix": 1.0}

def main(out_json):
    n2c = {r["norm_key"]: r["cfbd_school"] for r in csv.DictReader(open("data/anchors/team_name_map.csv"))}
    conf = {t["school"]: t.get("conference") for t in json.load(open(f"{D}/teams_fbs_2026.json"))}
    is_p4 = lambda t: conf.get(t) in P4 or t == "Notre Dame"

    sp = {}
    for r in csv.DictReader(open("data/anchors/SP+_2026preseason_2026-07-12.csv")):
        sp[n2c[r["norm_key"]]] = dict(overall=float(r["sp_plus_overall"]),
                                      off=float(r["sp_plus_off"]), dfn=float(r["sp_plus_def"]))
    raw = {"SP+": {t: v["overall"] for t, v in sp.items()}}
    SRC_LABEL = {"FEI": "FEI", "Massey (own model)": "Massey", "ESPN FPI": "FPI",
                 "TeamRankings Predictive": "TR"}
    for r in csv.DictReader(open("data/anchors/anchors_overall_2026-07-12.csv")):
        lab = SRC_LABEL.get(r["source"])
        if lab:
            raw.setdefault(lab, {})[n2c[r["norm_key"]]] = float(r["overall_rating"])

    spv = np.array(list(raw["SP+"].values())); smu, ssd = spv.mean(), spv.std()
    norm = {}
    for s, d in raw.items():
        v = np.array(list(d.values()))
        norm[s] = {t: (x - v.mean()) / v.std() * ssd + smu for t, x in d.items()}

    # Pick Six: rank -> order statistic of the partial blend's P4 slice
    ps_rank = {r["cfbd_school"]: int(r["overall_rank"])
               for r in csv.DictReader(open("data/anchors/PickSix_2026preseason_2026-07-14.csv"))}
    partial = {t: np.average([norm[s][t] for s in ("SP+", "FEI", "Massey", "FPI", "TR")],
                             weights=[2, 1, 1, 1, 1]) for t in norm["SP+"]}
    p4_sorted = sorted((v for t, v in partial.items() if is_p4(t)), reverse=True)
    norm["PickSix"] = {t: p4_sorted[ps_rank[t] - 1] for t in ps_rank}

    # winsorize + blend + dispersion
    teams = sorted(norm["SP+"])
    out, winsor_log = {}, []
    disp_list = []
    for t in teams:
        vals = {s: norm[s][t] for s in norm if t in norm[s]}
        used = dict(vals)
        for s in vals:
            others = [v for s2, v in vals.items() if s2 != s]
            med = float(np.median(others))
            if abs(vals[s] - med) > 5.0:
                used[s] = med + 5.0 * np.sign(vals[s] - med)
                winsor_log.append(dict(team=t, source=s, raw=round(vals[s], 2),
                                       winsorized=round(used[s], 2), median_others=round(med, 2)))
        w = np.array([WEIGHTS[s] for s in used])
        v = np.array([used[s] for s in used])
        blend = float(np.average(v, weights=w))
        dispersion = float(max(vals.values()) - min(vals.values()))
        disp_list.append(dispersion)
        gap = blend - sp[t]["overall"]
        out[t] = dict(
            sources={s: dict(raw=round(raw[s].get(t, float("nan")), 2) if s != "PickSix" else ps_rank.get(t),
                             normalized=round(vals[s], 2), used=round(used[s], 2),
                             winsorized=bool(used[s] != vals[s])) for s in vals},
            blend=round(blend, 2), dispersion=round(dispersion, 2),
            off=round(sp[t]["off"] + gap / 2, 2), dfn=round(sp[t]["dfn"] - gap / 2, 2),
            p4=is_p4(t),
        )
    thresh = float(np.quantile(disp_list, 0.9))
    for t in teams:
        out[t]["dispersion_flag"] = bool(out[t]["dispersion"] >= thresh)

    # per-run class term: (3.49 - blend_tilt_vs_SP+)/2
    tilts = []
    for s in ("FEI", "Massey", "FPI", "TR"):
        dp = [norm[s][t] - norm["SP+"][t] for t in teams if is_p4(t)]
        dg = [norm[s][t] - norm["SP+"][t] for t in teams if not is_p4(t)]
        tilts.append((np.mean(dg) - np.mean(dp)) * WEIGHTS[s])
    blend_tilt = float(sum(tilts) / sum(WEIGHTS[s] for s in ("SP+", "FEI", "Massey", "FPI", "TR")))
    class_per_side = round((3.49 - blend_tilt) / 2, 2)

    run = dict(
        _meta=dict(run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   captures="anchors 2026-07-12 (SP+ human-verified) + PickSix 2026-07-14",
                   weights=WEIGHTS, class_per_side=class_per_side, blend_tilt=round(blend_tilt, 3),
                   dispersion_flag_threshold=round(thresh, 2), n_winsorized=len(winsor_log)),
        winsor_log=winsor_log, teams=out)
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    json.dump(run, open(out_json, "w"), indent=1)
    top = sorted(out.items(), key=lambda kv: -kv[1]["blend"])[:5]
    print(f"anchor run: {len(teams)} teams | class term ±{class_per_side} | "
          f"winsorized {len(winsor_log)} source-values | dispersion flags {sum(1 for t in teams if out[t]['dispersion_flag'])}")
    print("top 5 blend:", ", ".join(f"{t} {v['blend']}" for t, v in top))
    print("winsor log:", [(w['team'], w['source'], w['raw'], '->', w['winsorized']) for w in winsor_log[:6]])

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "outputs/anchor_runs/anchor_run_2026-07-14.json")
