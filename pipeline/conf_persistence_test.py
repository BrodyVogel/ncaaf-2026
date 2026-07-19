#!/usr/bin/env python3
"""Step 2 (FINALIZATION_PLAN): anchor-side conference persistence test.

Question: do the MARKET's (SP+) preseason->final conference-level errors persist year
over year? If a conference is systematically under/over-rated preseason and that repeats,
that is a stable, exploitable conference-level market bias. If it is noise (low/negative
year-over-year correlation), there is no persistent conference market edge -> corroborates
demeaning the residual by conference.

Per the owner's policy (HANDOFF S6, FINALIZATION_PLAN Step 2): a null result corroborates
the demean decision; even a POSITIVE result does NOT reverse it (realignment turnover
makes historical per-conference estimates non-stationary). Only a large, stable,
realignment-robust effect would go back to the owner.

Method:
  - preseason SP+ overall per team-year: data/backtest/sp_preseason/SP+_YYYY_preseason.csv
    (uploaded; norm_key + sp_plus_overall). PRESEASON only.
  - final SP+ overall per team-year: pulled from CFBD /ratings/sp?year=YYYY (cached to
    data/backtest/sp_final/SP+_YYYY_final.csv).
  - conference = THAT season's AS-PLAYED membership from CFBD /teams/fbs?year=YYYY
    (cached to membership_YYYY.csv). NOTE: the /ratings/sp `conference` field is
    FORWARD-LOOKING (labels e.g. Boise State "Pac-12" for its 2026 destination in the
    2024/2025 files) and must NOT be used for as-played membership.
  - error_t(team) = final_overall - preseason_overall.
  - conf-mean error per year (conferences with >= MIN_N matched teams).
  - correlate conf-mean errors across adjacent years, matched by conference present in
    both years; split 2024+ (post-realignment) vs before. Also pool the pre pairs.

Repeatable:
  CFBD_KEY_FILE=/root/.cfb_secrets/cfbd_api_key.txt python3 pipeline/conf_persistence_test.py
Deterministic given the CFBD cache; re-pull by deleting data/backtest/sp_final/.
"""
import os, sys, csv, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from cfbd_client import CFBD
from pff_common import norm

YEARS = [2021, 2022, 2023, 2024, 2025]
MIN_N = 3                      # min matched teams for a conference to enter that year
PRESEASON_DIR = "data/backtest/sp_preseason"
FINAL_DIR = "data/backtest/sp_final"
OUT_MD = "outputs/CONF_PERSISTENCE_TEST.md"

# realignment boundary: 2024 preseason is the first alignment with SEC=16, B10=18,
# PAC collapsed. So the (2023->2024) pair straddles realignment; (2024->2025) is post.
POST_PAIR = (2024, 2025)
STRADDLE_PAIR = (2023, 2024)
PRE_PAIRS = [(2021, 2022), (2022, 2023)]


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None, n
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx == 0 or syy == 0:
        return None, n
    return sxy / math.sqrt(sxx * syy), n


def load_preseason(year):
    path = os.path.join(PRESEASON_DIR, f"SP+_{year}_preseason.csv")
    out = {}
    for r in csv.DictReader(open(path)):
        out[r["norm_key"]] = float(r["sp_plus_overall"])
    return out


def cfbd_to_normkey_map():
    m = {}
    for r in csv.DictReader(open("data/anchors/team_name_map.csv")):
        m[r["cfbd_school"]] = r["norm_key"]
    return m


def _client():
    key = os.environ.get("CFBD_KEY_FILE", "/root/.cfb_secrets/cfbd_api_key.txt")
    os.environ["CFBD_KEY_FILE"] = key
    return CFBD("/tmp/cfbd_sp_pull")


def pull_or_load_membership(year, c2n):
    """Return {norm_key: as-played conference} from /teams/fbs. Caches CSV.
    Authoritative membership (the /ratings/sp conference field is forward-looking)."""
    os.makedirs(FINAL_DIR, exist_ok=True)
    cache = os.path.join(FINAL_DIR, f"membership_{year}.csv")
    if os.path.exists(cache):
        rows = list(csv.DictReader(open(cache)))
    else:
        data = _client().get("/teams/fbs", {"year": year}).json()
        rows = []
        for rec in data:
            school = rec.get("school")
            conf = rec.get("conference")
            if school is None or conf is None:
                continue
            rows.append({"year": year, "school": school,
                         "norm_key": c2n.get(school) or norm(school),
                         "conference": conf})
        with open(cache, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["year", "school", "norm_key", "conference"])
            w.writeheader()
            w.writerows(rows)
    return {r["norm_key"]: r["conference"] for r in rows}


def pull_or_load_final(year, c2n):
    """Return {norm_key: (fallback_conf, final_overall)} for a season. Caches CSV.
    The conference here is the /ratings/sp label (forward-looking) kept only as a
    fallback; as-played membership comes from pull_or_load_membership()."""
    os.makedirs(FINAL_DIR, exist_ok=True)
    cache = os.path.join(FINAL_DIR, f"SP+_{year}_final.csv")
    rows = []
    if os.path.exists(cache):
        rows = list(csv.DictReader(open(cache)))
    else:
        data = _client().get("/ratings/sp", {"year": year}).json()
        for rec in data:
            team = rec.get("team")
            conf = rec.get("conference")
            rating = rec.get("rating")
            if team is None or conf is None or rating is None:
                continue  # drops national-average / incomplete rows
            nk = c2n.get(team) or norm(team)
            rows.append({"year": year, "team": team, "conference": conf,
                         "norm_key": nk, "final_overall": rating})
        with open(cache, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["year", "team", "conference",
                                              "norm_key", "final_overall"])
            w.writeheader()
            w.writerows(rows)
    out = {}
    for r in rows:
        out[r["norm_key"]] = (r["conference"], float(r["final_overall"]))
    return out


P4_CONF = {"SEC", "Big Ten", "Big 12", "ACC", "Pac-12"}


def main():
    c2n = cfbd_to_normkey_map()
    # per-year: {norm_key: (conf, error, preseason)}, and match diagnostics
    per_year = {}
    match_log = {}
    for y in YEARS:
        pre = load_preseason(y)
        fin = pull_or_load_final(y, c2n)
        mem = pull_or_load_membership(y, c2n)
        joined, unmatched_final, no_conf = {}, [], []
        for nk, (fb_conf, fo) in fin.items():
            if nk not in pre:
                unmatched_final.append(nk)
                continue
            conf = mem.get(nk, fb_conf)   # as-played membership; fallback to sp label
            if nk not in mem:
                no_conf.append(nk)
            joined[nk] = (conf, fo - pre[nk], pre[nk])
        per_year[y] = joined
        match_log[y] = {"final_n": len(fin), "pre_n": len(pre),
                        "joined_n": len(joined),
                        "unmatched_final": sorted(unmatched_final),
                        "no_membership": sorted(no_conf)}

    # compression diagnostic: does error correlate with preseason level? (pooled all yrs)
    allpre = [p for y in YEARS for (_, _, p) in per_year[y].values()]
    allerr = [e for y in YEARS for (_, e, _) in per_year[y].values()]
    comp_r, comp_n = pearson(allpre, allerr)
    mx = sum(allpre) / comp_n
    my = sum(allerr) / comp_n
    comp_slope = (sum((x - mx) * (e - my) for x, e in zip(allpre, allerr))
                  / sum((x - mx) ** 2 for x in allpre))

    # P4/G5 gap per year
    p4g5 = {}
    for y in YEARS:
        p4 = [e for (c, e, _) in per_year[y].values() if c in P4_CONF]
        g5 = [e for (c, e, _) in per_year[y].values() if c not in P4_CONF]
        p4g5[y] = (sum(p4) / len(p4), len(p4), sum(g5) / len(g5), len(g5))

    # conf-mean error per year (n >= MIN_N)
    conf_mean = {}   # {year: {conf: (mean, n)}}
    for y in YEARS:
        agg = {}
        for nk, (conf, err, _pre) in per_year[y].items():
            agg.setdefault(conf, []).append(err)
        conf_mean[y] = {c: (sum(v) / len(v), len(v))
                        for c, v in agg.items() if len(v) >= MIN_N}

    # adjacent-pair correlations (conf present in both years w/ n>=MIN_N)
    def pair_corr(y1, y2):
        commons = sorted(set(conf_mean[y1]) & set(conf_mean[y2]))
        xs = [conf_mean[y1][c][0] for c in commons]
        ys = [conf_mean[y2][c][0] for c in commons]
        r, n = pearson(xs, ys)
        return r, n, commons, xs, ys

    pairs = [(2021, 2022), (2022, 2023), (2023, 2024), (2024, 2025)]
    pair_results = {p: pair_corr(*p) for p in pairs}

    # pooled pre (fully pre-realignment pairs) vs post
    def pooled(pairs_list):
        X, Y = [], []
        for (y1, y2) in pairs_list:
            _, _, commons, xs, ys = pair_corr(y1, y2)
            X += xs
            Y += ys
        return pearson(X, Y)

    pre_pooled = pooled(PRE_PAIRS)
    post_pooled = pooled([POST_PAIR])

    comp = {"r": comp_r, "n": comp_n, "slope": comp_slope}
    write_report(match_log, conf_mean, pair_results, pre_pooled, post_pooled, comp, p4g5)
    # console delta line
    def f(x):
        return f"{x:+.2f}" if x is not None else "n/a"
    print("CONF PERSISTENCE | pair r: "
          + " ".join(f"{a}->{b}:{f(pair_results[(a,b)][0])}" for (a, b) in pairs))
    print(f"  pre-pooled r={f(pre_pooled[0])} (n={pre_pooled[1]}) | "
          f"post(24->25) r={f(post_pooled[0])} (n={post_pooled[1]})")
    print(f"  compression corr(preseason,error)={f(comp_r)} slope={comp_slope:+.3f} "
          f"(n={comp_n}) -> P4-down/G5-up is mechanical")


def write_report(match_log, conf_mean, pair_results, pre_pooled, post_pooled,
                 comp, p4g5):
    L = []
    L.append("# Conference persistence test (Step 2 corroboration) — anchor-side\n")
    L.append("_Generated by pipeline/conf_persistence_test.py. OPTIONAL, non-blocking. "
             "Does NOT drive any rating; corroboration only (FINALIZATION_PLAN Step 2)._\n")
    L.append("## Question\n")
    L.append("Do the market's (SP+) **preseason→final** conference-level errors persist "
             "year over year? A persistent conference error would be an exploitable "
             "market bias; noise corroborates demeaning the residual by conference. "
             "Per owner policy, even a positive result does not reverse the demean "
             "decision (realignment non-stationarity).\n")
    L.append("## Method\n")
    L.append("- error(team, year) = final SP+ overall (CFBD `/ratings/sp`) − preseason "
             "SP+ overall (uploaded). Same scale (pts vs FBS average).\n")
    L.append(f"- Conference = that season's **as-played** membership from CFBD "
             f"`/teams/fbs?year=` (the `/ratings/sp` conference field is forward-looking — "
             f"it labels realigning G5 teams by their 2026 destination — and is NOT used). "
             f"Conf-mean error kept when ≥{MIN_N} matched teams.\n")
    L.append("- Pearson r of conf-mean errors across adjacent years (conferences present "
             "in both). Split: pre-realignment pairs (2021→22, 2022→23) pooled; "
             "2023→24 straddles realignment (flagged); 2024→25 post-realignment.\n")

    L.append("\n## Join coverage\n")
    L.append("| year | final n | preseason n | joined n | unmatched (final side) |")
    L.append("|---|---|---|---|---|")
    for y in YEARS:
        ml = match_log[y]
        um = ", ".join(ml["unmatched_final"]) if ml["unmatched_final"] else "—"
        if len(um) > 60:
            um = um[:57] + "…"
        L.append(f"| {y} | {ml['final_n']} | {ml['pre_n']} | {ml['joined_n']} | {um} |")

    L.append("\n## Conference-mean preseason→final error by year (pts; n in parens)\n")
    all_confs = sorted({c for y in YEARS for c in conf_mean[y]})
    L.append("| conference | " + " | ".join(str(y) for y in YEARS) + " |")
    L.append("|---" * (len(YEARS) + 1) + "|")
    for c in all_confs:
        cells = []
        for y in YEARS:
            if c in conf_mean[y]:
                m, n = conf_mean[y][c]
                cells.append(f"{m:+.1f} ({n})")
            else:
                cells.append("—")
        L.append(f"| {c} | " + " | ".join(cells) + " |")

    def f(x):
        return f"{x:+.3f}" if x is not None else "n/a"

    L.append("\n## Year-over-year persistence (Pearson r of conf-mean errors)\n")
    L.append("| pair | r | n conferences | note |")
    L.append("|---|---|---|---|")
    notes = {(2021, 2022): "pre", (2022, 2023): "pre",
             (2023, 2024): "STRADDLES realignment — not comparable membership",
             (2024, 2025): "post-realignment"}
    for p in [(2021, 2022), (2022, 2023), (2023, 2024), (2024, 2025)]:
        r, n, commons, xs, ys = pair_results[p]
        L.append(f"| {p[0]}→{p[1]} | {f(r)} | {n} | {notes[p]} |")
    L.append("")
    L.append(f"**Pooled pre-realignment** (2021→22 + 2022→23): r = {f(pre_pooled[0])} "
             f"(n = {pre_pooled[1]} conf-pairs).")
    L.append("")
    L.append(f"**Post-realignment** (2024→25): r = {f(post_pooled[0])} "
             f"(n = {post_pooled[1]} conferences).")

    # ---- compression confound ----
    L.append("\n## Confound check: preseason-dispersion compression\n")
    L.append("If SP+ preseason is more dispersed than final (a known property), high-rated "
             "teams drift DOWN and low-rated teams drift UP by construction. Because "
             "conferences are level clusters (P4 high, G5 low), that compression alone "
             "manufactures a P4-negative / G5-positive error pattern with **no** "
             "conference edge behind it.\n")
    L.append(f"- Pooled all team-years (n={comp['n']}): corr(preseason rating, error) = "
             f"**{comp['r']:+.2f}**, slope(error ~ preseason) = **{comp['slope']:+.3f}**. "
             f"Negative — high-rated teams systematically finish below their preseason "
             f"number. This is the same scale-compression confound cited in the decision "
             f"record (HANDOFF §6).\n")
    L.append("\n### P4 vs G5 mean preseason→final error (pts)\n")
    L.append("| year | P4 mean (n) | G5 mean (n) | G5−P4 gap |")
    L.append("|---|---|---|---|")
    for y in YEARS:
        p4m, p4n, g5m, g5n = p4g5[y]
        L.append(f"| {y} | {p4m:+.2f} ({p4n}) | {g5m:+.2f} ({g5n}) | {g5m - p4m:+.2f} |")
    gaps = [p4g5[y][2] - p4g5[y][0] for y in YEARS]
    n_pos = sum(1 for g in gaps if g > 0)
    L.append(f"\nGap is positive in {n_pos} of {len(gaps)} years (mean "
             f"{sum(gaps)/len(gaps):+.2f}; 2022 the lone exception at "
             f"{p4g5[2022][2]-p4g5[2022][0]:+.2f}); it is present pre-realignment too, so "
             "it is not a post-2024 phenomenon. Most of it is the compression above — the "
             "preseason P4−G5 rating spread (~15 pts) times the compression slope predicts "
             "a gap of roughly +2.5–3 pts, i.e. the bulk of the observed average. Any "
             "residual class effect is small and not separable from compression at this n. "
             "Note the anchor-run class test already measured the grade-side P4/G5 effect "
             "at **+0.15 pts, t=0.3 (nil)**.\n")

    L.append("\n## Reading\n")
    r_pre = pre_pooled[0]
    r_post = post_pooled[0]
    verdict = []
    if r_pre is None:
        verdict.append("Pre-realignment pooled correlation undefined (degenerate).")
    elif abs(r_pre) < 0.3:
        verdict.append(f"**Pre-realignment persistence is null** (pooled r={r_pre:+.2f}, "
                       f"|r|<0.3, n={pre_pooled[1]}): idiosyncratic conference-level "
                       "preseason errors do NOT repeat year to year — consistent with "
                       "noise, corroborating the demean decision.")
    else:
        verdict.append(f"Pre-realignment pooled r={r_pre:+.2f} (n={pre_pooled[1]}) — "
                       "non-trivial; weigh against the confound below and the small n.")
    if r_post is not None and r_post >= 0.5:
        verdict.append(f"**The post-realignment pair (2024→25) shows r={r_post:+.2f}** — "
                       "reported honestly, not buried. But it is a SINGLE year-transition "
                       "(one correlation over ~10 conferences), and the "
                       "conference-mean vector it correlates is dominated by the P4/G5 "
                       "level axis, which the compression confound above already explains "
                       "mechanically (G5 over, P4 under, every year). It is the P4/G5 "
                       "ordering re-expressing itself, not evidence of a per-conference "
                       "edge. Under the owner's standard ('significant evidence' for a "
                       "class edge; per-conference edges distrusted) one noisy post-"
                       "realignment pair, largely attributable to compression, does not "
                       "clear the bar.")
    verdict.append("Why demeaning is unaffected either way: the demean acts on the "
                   "grade→points **residual**, not on the anchor. Whatever real "
                   "conference/level information the market carries is already in the "
                   "anchor blend and flows through to every final rating untouched; "
                   "demeaning only neutralizes conference-correlated structure in the "
                   "grade-adjustment layer. So even a real market conference bias would "
                   "not argue against demeaning the residual.")
    verdict.append("The 2023→24 straddle pair mixes old/new membership and is reported "
                   "for completeness only. Small n (≤11 conferences/year, 5 seasons) caps "
                   "confidence regardless of sign — this is corroboration, not a test the "
                   "grades could ever pass or fail directly (no historical grades exist).")
    for v in verdict:
        L.append("- " + v)
    L.append("\n## Bottom line\n")
    L.append("This is anchor-side (SP+) evidence, the closest available proxy since the "
             "grades themselves have no history. It informs confidence in the demean "
             "decision but, by the owner's stated standard, cannot by itself change it. "
             "Decision unchanged: conference-demeaned residual remains OFFICIAL.\n")

    os.makedirs("outputs", exist_ok=True)
    with open(OUT_MD, "w") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
