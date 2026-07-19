/* Win-total engine — JS port of pipeline/win_engine.py.
   Mirrors the Python reference exactly (same GH nodes/weights are injected from the payload).
   Normal CDF uses a Cephes ndtr port so phi() matches Python's math.erf to ~1e-14. */
(function (root) {
  'use strict';

  // ---- Cephes ndtr (normal CDF), double-precision ----
  function polevl(x, c) { var r = c[0]; for (var i = 1; i < c.length; i++) r = r * x + c[i]; return r; }
  function p1evl(x, c) { var r = x + c[0]; for (var i = 1; i < c.length; i++) r = r * x + c[i]; return r; }
  var T = [9.60497373987051638749e0, 9.00260197203842689217e1, 2.23200534594684319226e3,
           7.00332514112805075473e3, 5.55923013010394962768e4];
  var U = [3.35617141647503099647e1, 5.21357949780152679795e2, 4.59432382970980127987e3,
           2.26290000613890934246e4, 4.92673942608635921086e4];
  var P = [2.46196981473530512524e-10, 5.64189564831068821977e-1, 7.46321056442269912687e0,
           4.86371970985681366614e1, 1.96520832956077098242e2, 5.26445194995477358631e2,
           9.34528527171957607540e2, 1.02755188689515710272e3, 5.57535335369399327526e2];
  var Q = [1.32281951154744992508e1, 8.67072140885989742329e1, 3.54937778887819891062e2,
           9.75708501743205489753e2, 1.82390916687909736289e3, 2.24633760818710981792e3,
           1.65666309194161350182e3, 5.57535340817727675546e2];
  var R = [5.64189583547755073984e-1, 1.27536670759978104416e0, 5.01905042251180477414e0,
           6.16021097993053585195e0, 7.40974269950448939160e0, 2.97886665372100240670e0];
  var S = [2.26052863220117276590e0, 9.39603524938001434673e0, 1.20489539808096656605e1,
           1.70814450747565897222e1, 9.60896809063285878198e0, 3.36907645100081516050e0];
  var SQRTH = 7.07106781186547524401e-1, MAXLOG = 7.09782712893383996732e2;

  function erf(x) {
    if (Math.abs(x) > 1.0) return 1.0 - erfc(x);
    var z = x * x;
    return x * polevl(z, T) / p1evl(z, U);
  }
  function erfc(a) {
    var x = Math.abs(a);
    if (x < 1.0) return 1.0 - erf(a);
    var z = -a * a;
    if (z < -MAXLOG) return (a < 0) ? 2.0 : 0.0;
    z = Math.exp(z);
    var p, q;
    if (x < 8.0) { p = polevl(x, P); q = p1evl(x, Q); }
    else { p = polevl(x, R); q = p1evl(x, S); }
    var y = (z * p) / q;
    if (a < 0) y = 2.0 - y;
    if (y === 0.0) return (a < 0) ? 2.0 : 0.0;
    return y;
  }
  function ndtr(a) {  // normal CDF
    var x = a * SQRTH, z = Math.abs(x);
    if (z < SQRTH) return 0.5 + 0.5 * erf(x);
    var y = 0.5 * erfc(z);
    return (x > 0) ? (1.0 - y) : y;
  }

  function phi(z) { return ndtr(z); }

  // ---- engine (mirrors win_engine.py) ----
  function makeEngine(meta) {
    var HFA = meta.hfa, SIGMA_GAME = meta.sigma_game, BAND_TO_SD = meta.band_to_sd;
    var NODES = meta.gh_nodes, WEIGHTS = meta.gh_weights;
    var SQRT_PI = Math.sqrt(Math.PI), SQRT2 = Math.sqrt(2.0);

    function gameWinProb(muSelf, muOpp, site, bandOpp, opts) {
      opts = opts || {};
      var sg = opts.sigma_game != null ? opts.sigma_game : SIGMA_GAME;
      var hfa = opts.hfa != null ? opts.hfa : HFA;
      var bts = opts.band_to_sd != null ? opts.band_to_sd : BAND_TO_SD;
      var delta = opts.delta != null ? opts.delta : 0.0;
      var sigmaEff = Math.sqrt(sg * sg + Math.pow(bandOpp * bts, 2));
      return phi((muSelf + delta - muOpp + hfa * site) / sigmaEff);
    }

    function poissonBinomial(probs) {
      var dist = [1.0];
      for (var i = 0; i < probs.length; i++) {
        var p = Math.min(Math.max(probs[i], 0.0), 1.0);
        var nd = new Array(dist.length + 1).fill(0.0);
        for (var k = 0; k < dist.length; k++) {
          nd[k] += dist[k] * (1.0 - p);
          nd[k + 1] += dist[k] * p;
        }
        dist = nd;
      }
      return dist;
    }

    // games: [{mu_opp, site, band_opp}]
    function winDistribution(muSelf, bandSelf, games, opts) {
      opts = opts || {};
      var sg = opts.sigma_game != null ? opts.sigma_game : SIGMA_GAME;
      var hfa = opts.hfa != null ? opts.hfa : HFA;
      var bts = opts.band_to_sd != null ? opts.band_to_sd : BAND_TO_SD;
      var tau = bandSelf * bts, G = games.length;
      var mixed = new Array(G + 1).fill(0.0);
      for (var n = 0; n < NODES.length; n++) {
        var delta = SQRT2 * tau * NODES[n];
        var probs = games.map(function (g) {
          return gameWinProb(muSelf, g.mu_opp, g.site, g.band_opp,
            { sigma_game: sg, hfa: hfa, band_to_sd: bts, delta: delta });
        });
        var pb = poissonBinomial(probs);
        var wq = WEIGHTS[n] / SQRT_PI;
        for (var k = 0; k <= G; k++) mixed[k] += wq * pb[k];
      }
      var s = mixed.reduce(function (a, b) { return a + b; }, 0);
      mixed = mixed.map(function (m) { return m / s; });
      var ew = 0; for (var k2 = 0; k2 <= G; k2++) ew += k2 * mixed[k2];
      var baseP = games.map(function (g) {
        return gameWinProb(muSelf, g.mu_opp, g.site, g.band_opp,
          { sigma_game: sg, hfa: hfa, band_to_sd: bts, delta: 0.0 });
      });
      return { dist: mixed, expected_wins: ew, base_p: baseP, G: G };
    }

    return { gameWinProb: gameWinProb, poissonBinomial: poissonBinomial,
             winDistribution: winDistribution, phi: phi,
             HFA: HFA, SIGMA_GAME: SIGMA_GAME, BAND_TO_SD: BAND_TO_SD };
  }

  // ---- odds utilities (mirror win_engine.py) ----
  function probToAmerican(p) {
    p = Math.min(Math.max(p, 1e-12), 1 - 1e-12);
    return p >= 0.5 ? (-100.0 * p / (1.0 - p)) : (100.0 * (1.0 - p) / p);
  }
  function americanToProb(a) { return a < 0 ? (-a) / ((-a) + 100.0) : 100.0 / (a + 100.0); }
  function americanToDecimal(a) { return 1.0 + (a > 0 ? a / 100.0 : 100.0 / (-a)); }
  function underFromOver(over, cents) {
    cents = cents == null ? 30 : cents;
    return over < 0 ? (-over - cents) : -(over + cents);
  }

  var api = { makeEngine: makeEngine, phi: phi, erf: erf, erfc: erfc, ndtr: ndtr,
              probToAmerican: probToAmerican, americanToProb: americanToProb,
              americanToDecimal: americanToDecimal, underFromOver: underFromOver };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.WinEngine = api;
})(typeof self !== 'undefined' ? self : this);
