#!/usr/bin/env python3
"""Win-total simulation engine (reference implementation).

MODEL (documented for owner evaluation)
=======================================
Ratings are neutral-field point margins vs an average FBS team (0). For a game between the
subject team S (rating mu_S) and opponent O (rating mu_O):

    expected_margin = mu_S - mu_O + HFA * site        site in {+1 home, -1 away, 0 neutral}
    P(S wins)       = Phi(expected_margin / sigma_eff)

This is a probit (normal-CDF) win model. Two variance sources, treated distinctly because
they correlate differently across a season:

1. GAME randomness (sigma_game): even with perfectly known ratings, a single game's margin
   scatters around its expectation. INDEPENDENT across games. Calibrated to CFB
   spread->win% conversion: sigma_game = 13.5 (a 7-pt favorite ~ Phi(7/13.5)=70%, a 3-pt
   favorite ~59%, a 14-pt favorite ~85% — matching how books price CFB moneylines).

2. OPPONENT rating uncertainty (opp band): we're unsure of each opponent's true rating.
   INDEPENDENT across the season's different opponents, so it adds to the per-game spread:
        sigma_eff_g = sqrt(sigma_game^2 + (band_O_g * BAND_TO_SD)^2)

3. OUR rating uncertainty (subject band): we're unsure of the SUBJECT team's true rating.
   This is a SHARED shock — if we're 2 pts too high, we're too high in EVERY game — so it
   is CORRELATED across all of the team's games. Modeled as a latent offset
        delta ~ Normal(0, tau_S^2),  tau_S = band_S * BAND_TO_SD
   applied to mu_S in every game, then integrated out. This shared shock is what fattens
   the win-total tails (extreme seasons become more likely than an independent-game model
   would say) — the single most important modeling choice here.

WIN DISTRIBUTION (exact, not Monte Carlo)
    Given delta, games are independent -> wins ~ Poisson-Binomial with probs p_g(delta),
    computed EXACTLY by DP (O(G^2)). Then mix over delta by Gauss-Hermite quadrature:
        P(wins=k) = sum_i w_i * PoissonBinomial(k | {p_g(delta_i)})
    with delta_i = sqrt(2)*tau_S*x_i and weights w_i/sqrt(pi) (x_i,w_i = Hermite nodes).
    21 nodes -> effectively exact for this smooth integrand; deterministic (no simulation
    noise). The same fixed nodes are shipped to the browser so the JS matches to 1e-9.

DEFAULTS (all adjustable, documented, exposed in the UI):
    HFA = 2.3, sigma_game = 13.5, BAND_TO_SD = 1.0 (band treated as ~1 SD of rating).
"""
import math

HFA = 2.3
SIGMA_GAME = 13.5
BAND_TO_SD = 1.0

# 21-point Gauss-Hermite nodes/weights (physicists', weight e^{-x^2}); hardcoded so the
# Python reference and the browser JS produce identical numbers. (numpy.hermgauss(21))
GH_NODES = [
 -5.550351873264678, -4.773992343411219, -4.121995547659471, -3.531972877137959,
 -2.979991207704598, -2.453552124512838, -1.944962949186254, -1.448934250650732,
 -0.961499634418369, -0.479450707079108, 0.0, 0.479450707079108, 0.961499634418369,
 1.448934250650732, 1.944962949186254, 2.453552124512838, 2.979991207704598,
 3.531972877137959, 4.121995547659471, 4.773992343411219, 5.550351873264678]
GH_WEIGHTS = [
 3.720365070136023e-14, 8.818611242049933e-11, 2.5712301800593154e-08, 2.17188489805667e-06,
 7.478398867310063e-05, 0.0012549820417264088, 0.011414065837434397, 0.0601796466589123,
 0.19212032406699775, 0.3816690736135022, 0.47902370312017756, 0.3816690736135022,
 0.19212032406699775, 0.0601796466589123, 0.011414065837434397, 0.0012549820417264088,
 7.478398867310063e-05, 2.17188489805667e-06, 2.5712301800593154e-08, 8.818611242049933e-11,
 3.720365070136023e-14]
_SQRT_PI = math.sqrt(math.pi)


def phi(z):
    """Standard normal CDF."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def game_win_prob(mu_self, mu_opp, site, band_opp, sigma_game=SIGMA_GAME,
                  hfa=HFA, band_to_sd=BAND_TO_SD, delta=0.0):
    sigma_eff = math.sqrt(sigma_game * sigma_game + (band_opp * band_to_sd) ** 2)
    return phi((mu_self + delta - mu_opp + hfa * site) / sigma_eff)


def poisson_binomial(probs):
    """Exact distribution of the number of successes among independent Bernoulli(probs)."""
    dist = [1.0]
    for p in probs:
        p = min(max(p, 0.0), 1.0)
        nd = [0.0] * (len(dist) + 1)
        for k, dk in enumerate(dist):
            nd[k] += dk * (1.0 - p)
            nd[k + 1] += dk * p
        dist = nd
    return dist


def win_distribution(mu_self, band_self, games, sigma_game=SIGMA_GAME, hfa=HFA,
                     band_to_sd=BAND_TO_SD):
    """games: list of dicts {mu_opp, site, band_opp}. Returns dict with the mixed win
    distribution (list P(wins=k), k=0..G), expected wins, and the base p_g at delta=0."""
    tau = band_self * band_to_sd
    G = len(games)
    mixed = [0.0] * (G + 1)
    for x, w in zip(GH_NODES, GH_WEIGHTS):
        delta = math.sqrt(2.0) * tau * x
        probs = [game_win_prob(mu_self, g['mu_opp'], g['site'], g['band_opp'],
                               sigma_game, hfa, band_to_sd, delta) for g in games]
        pb = poisson_binomial(probs)
        wq = w / _SQRT_PI
        for k in range(G + 1):
            mixed[k] += wq * pb[k]
    s = sum(mixed)
    mixed = [m / s for m in mixed]                      # renormalize (guards tiny GH drift)
    exp_wins = sum(k * mixed[k] for k in range(G + 1))
    base_p = [game_win_prob(mu_self, g['mu_opp'], g['site'], g['band_opp'],
                            sigma_game, hfa, band_to_sd, 0.0) for g in games]
    return {'dist': mixed, 'expected_wins': exp_wins, 'base_p': base_p, 'G': G}


def ladder(dist):
    """P(wins >= k) for k=0..G+1 (survival ladder)."""
    G = len(dist) - 1
    out = {}
    for k in range(0, G + 2):
        out[k] = sum(dist[j] for j in range(k, G + 1))
    return out


# ---- American-odds utilities ----
def prob_to_american(p):
    p = min(max(p, 1e-12), 1 - 1e-12)
    return -100.0 * p / (1.0 - p) if p >= 0.5 else 100.0 * (1.0 - p) / p


def american_to_prob(a):
    return (-a) / ((-a) + 100.0) if a < 0 else 100.0 / (a + 100.0)


def american_to_decimal(a):
    return 1.0 + (a / 100.0 if a > 0 else 100.0 / (-a))


def under_from_over(over_american, cents=30):
    """Owner's convention: 30-cent line. over -175 <-> under +145."""
    return (-over_american - cents) if over_american < 0 else -(over_american + cents)


def market_edge(our_p_over, line, over_american, cents=30):
    """Returns dict of de-vigged market prob, our prob, edges, and EV per $1 each side."""
    under_american = under_from_over(over_american, cents)
    p_over_vig = american_to_prob(over_american)
    p_under_vig = american_to_prob(under_american)
    devig = p_over_vig + p_under_vig
    mkt_p_over = p_over_vig / devig
    our_p_under = 1.0 - our_p_over
    ev_over = our_p_over * (american_to_decimal(over_american) - 1) - (1 - our_p_over)
    ev_under = our_p_under * (american_to_decimal(under_american) - 1) - (1 - our_p_under)
    return {
        'line': line, 'over_odds': over_american, 'under_odds': under_american,
        'mkt_p_over': mkt_p_over, 'mkt_p_under': 1 - mkt_p_over, 'hold': devig - 1,
        'our_p_over': our_p_over, 'our_p_under': our_p_under,
        'edge_over': our_p_over - mkt_p_over, 'edge_under': our_p_under - (1 - mkt_p_over),
        'ev_over': ev_over, 'ev_under': ev_under,
    }
