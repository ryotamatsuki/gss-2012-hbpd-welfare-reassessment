"""Clean-room exact reconstruction of the 2012 uniform-price game.

All prices are represented by net margins above marginal cost.  The direct
evaluator works from primitive switching thresholds and clipping; it does not
call the piecewise regime formula.  The separate piecewise function is only a
cross-check and a convenient statement of the proved demand correspondence.
"""

from __future__ import annotations

from fractions import Fraction as F


def Q(value: int | str | F) -> F:
    """Construct an exact rational from an integer, decimal string, or Fraction."""
    if isinstance(value, F):
        return value
    return F(value)


def clip(z: F, lo: F, hi: F) -> F:
    return min(max(z, lo), hi)


def thresholds(a: F, b: F, s: F) -> tuple[F, F]:
    """Primitive indifferent locations; tau is normalized to one."""
    d = b - a
    return (d + 1 + s) / 2, (d + 1 - s) / 2


def share_a_direct(a: F, b: F, x: F, s: F) -> F:
    """A's market share from the two history-specific primitive comparisons."""
    t_a, t_b = thresholds(a, b, s)
    return clip(t_a, F(0), x) + clip(t_b - x, F(0), 1 - x)


def share_a_piecewise(a: F, b: F, x: F, s: F) -> F:
    """The analytic five-regime demand correspondence for 0 < s < 1."""
    d = b - a
    left = -1 - s
    alpha = 2 * x - 1 - s
    beta = 2 * x - 1 + s
    right = 1 + s
    if d <= left:
        return F(0)
    if d < alpha:
        return (d + 1 + s) / 2
    if d <= beta:
        return x
    if d < right:
        return (d + 1 - s) / 2
    return F(1)


def profit_a(a: F, b: F, x: F, s: F) -> F:
    return a * share_a_direct(a, b, x, s)


def profit_b(a: F, b: F, x: F, s: F) -> F:
    return b * (1 - share_a_direct(a, b, x, s))


def x_h_condition(x: F, s: F) -> bool:
    """Exact comparison x >= 1/2-s/3+sqrt(3s(s+6))/6 for 0 <= s < 1."""
    if s == 0:
        return x >= F(1, 2)
    z = 6 * (x - F(1, 2) + s / 3)
    return z >= 0 and z * z >= 3 * s * (s + 6)


def source_uniform_prices(s: F) -> tuple[F, F]:
    return 1 + s / 3, 1 - s / 3


def hbp_weak_prices(x: F, s: F) -> tuple[F, F, F, F]:
    """Return (pA, qA, pB, qB), all as net margins, in tau=1 units."""
    return (
        (2 * x + 1 + s) / 3,
        (3 - 4 * x - s) / 3,
        (3 - 2 * x + s) / 3,
        (4 * x - 1 - s) / 3,
    )


def segment_share_a(a: F, b: F, k: F, length: F) -> F:
    """A's sales in a history-specific segment, from primitive clipping."""
    return clip((b - a + k) / 2, F(0), length)


def hbp_strong_unrestricted_family(
    x: F, s: F, u: F
) -> tuple[F, F]:
    """(q_A-c, p_B-c) on the extra below-cost HBP equilibria, tau=1.

    The family exists only when prices below marginal cost are allowed and
    x >= (3-s)/4.  Its source-paper member is u=0.
    """
    delta = 3 - s - 4 * x
    if not (x >= (3 - s) / 4 and delta <= u <= 0):
        raise ValueError("u must lie in [3-s-4x, 0] on the strong branch")
    return u, u + 2 * x - 1 + s


def hbp_strong_profile_unrestricted(x: F, s: F, u: F) -> tuple[F, F, F, F]:
    """Return (p_A-c,q_A-c,p_B-c,q_B-c) for the unrestricted family."""
    q_a, p_b = hbp_strong_unrestricted_family(x, s, u)
    return (
        (2 * x + 1 + s) / 3,
        q_a,
        p_b,
        (4 * x - 1 - s) / 3,
    )


def _integral_linear(base: F, slope: F, lo: F, hi: F) -> F:
    return base * (hi - lo) + slope * (hi * hi - lo * lo) / 2


def uniform_cs_direct(
    p_a: F, p_b: F, x: F, s: F, tau: F = F(1), beta: F = F(0)
) -> F:
    """Integrate realized primitive utility under uniform prices and full coverage."""
    d = p_b - p_a
    t_a = (d + tau + s * tau) / (2 * tau)
    t_b = (d + tau - s * tau) / (2 * tau)
    k_a = clip(t_a, F(0), x)
    k_b = clip(t_b, x, F(1))
    return (
        _integral_linear(beta - p_a, -tau, F(0), k_a)
        + _integral_linear(beta - p_b - tau - s * tau, tau, k_a, x)
        + _integral_linear(beta - p_a - s * tau, -tau, x, k_b)
        + _integral_linear(beta - p_b - tau, tau, k_b, F(1))
    )


def hbp_cs_direct(
    p_a: F,
    q_a: F,
    p_b: F,
    q_b: F,
    x: F,
    s: F,
    tau: F = F(1),
    beta: F = F(0),
) -> F:
    """Integrate each history group's chosen primitive utility."""
    t_a = (q_b - p_a + tau + s * tau) / (2 * tau)
    t_b = (p_b - q_a + tau - s * tau) / (2 * tau)
    k_a = clip(t_a, F(0), x)
    k_b = clip(t_b, x, F(1))
    return (
        _integral_linear(beta - p_a, -tau, F(0), k_a)
        + _integral_linear(beta - q_b - tau - s * tau, tau, k_a, x)
        + _integral_linear(beta - q_a - s * tau, -tau, x, k_b)
        + _integral_linear(beta - p_b - tau, tau, k_b, F(1))
    )


def hbp_profits_direct(
    p_a: F, q_a: F, p_b: F, q_b: F, x: F, s: F, tau: F = F(1)
) -> tuple[F, F]:
    """Firm profits using clipped primitive demands; prices include c=0."""
    t_a = (q_b - p_a + tau + s * tau) / (2 * tau)
    t_b = (p_b - q_a + tau - s * tau) / (2 * tau)
    a_hist_a = clip(t_a, F(0), x)
    b_hist_a = x - a_hist_a
    b_hist_to_a = clip(t_b - x, F(0), 1 - x)
    b_hist_b = (1 - x) - b_hist_to_a
    return (
        p_a * a_hist_a + q_a * b_hist_to_a,
        p_b * b_hist_b + q_b * b_hist_a,
    )


def direct_best_response_candidates(
    firm: str, rival_margin: F, x: F, s: F
) -> tuple[F, tuple[F, ...]]:
    """Global best-response value/candidate set on margins m >= 0.

    Candidate breakpoints are obtained by making each primitive switching
    threshold hit an endpoint of its own history interval.  On every resulting
    interval the direct clipped demand is affine, so m*demand is quadratic.
    We evaluate each endpoint and every feasible interior vertex exactly.
    """
    if firm not in {"A", "B"}:
        raise ValueError("firm must be 'A' or 'B'")
    if not (F(0) < x < F(1) and F(0) <= s < F(1)):
        raise ValueError("expected 0 < x < 1 and 0 <= s < 1")

    if firm == "A":
        # Vary a with b fixed. These solve t_A=0,x and t_B=x,1.
        raw = (
            rival_margin + 1 + s,
            rival_margin + 1 + s - 2 * x,
            rival_margin + 1 - s - 2 * x,
            rival_margin - 1 - s,
        )

        def demand(m: F) -> F:
            return share_a_direct(m, rival_margin, x, s)

    else:
        # Vary b with a fixed. These solve t_A=0,x and t_B=x,1.
        raw = (
            rival_margin - 1 - s,
            rival_margin + 2 * x - 1 - s,
            rival_margin + 2 * x - 1 + s,
            rival_margin + 1 + s,
        )

        def demand(m: F) -> F:
            return 1 - share_a_direct(rival_margin, m, x, s)

    knots = sorted({F(0), *(z for z in raw if z > 0)})
    candidates = set(knots)
    for lo, hi in zip(knots, knots[1:]):
        if hi == lo:
            continue
        y_lo, y_hi = demand(lo), demand(hi)
        slope = (y_hi - y_lo) / (hi - lo)
        intercept = y_lo - slope * lo
        if slope < 0:
            vertex = -intercept / (2 * slope)
            if lo <= vertex <= hi:
                candidates.add(vertex)

    values = {
        m: m * demand(m)
        for m in candidates
    }
    best = max(values.values())
    maximizers = tuple(sorted(m for m, value in values.items() if value == best))
    # The unbounded tail has zero demand for the deviator and hence payoff 0.
    if best == 0:
        maximizers = maximizers + (F(max(knots) + 1),)
    return best, maximizers


def self_check() -> None:
    # Uniform-demand regime table versus primitive direct clipping.
    for x in (F(51, 100), F(3, 5), F(7, 10), F(9, 10)):
        for s in (F(0), F(1, 10), F(1, 2), F(99, 100)):
            for d in (F(-2), F(-1) - s, 2 * x - 1 - s,
                      2 * x - 1 + s, F(1) + s, F(2)):
                a, b = F(3, 2), F(3, 2) + d
                assert share_a_direct(a, b, x, s) == share_a_piecewise(a, b, x, s)

    # Target both sides of every clipping boundary and disappearing history.
    eps = F(1, 10**8)
    for x in (F(1, 2), F(1, 2) + eps, F(1) - eps, F(1)):
        for s in (F(0), eps, F(1) - eps):
            cuts = (-1 - s, 2 * x - 1 - s, 2 * x - 1 + s, 1 + s)
            for cut in cuts:
                for d in (cut - eps, cut, cut + eps):
                    a, b = F(2), F(2) + d
                    assert share_a_direct(a, b, x, s) == \
                        share_a_piecewise(a, b, x, s)

    # Exact regime-crossing counterexample to the source uniform candidate.
    x, s = F(3, 5), F(1, 2)
    a, b = source_uniform_prices(s)
    b_dev = F(28, 15)
    assert share_a_direct(a, b, x, s) == F(7, 12)
    assert profit_b(a, b, x, s) == F(25, 72)
    assert profit_b(a, b_dev, x, s) == F(56, 75)
    assert profit_b(a, b_dev, x, s) - profit_b(a, b, x, s) == F(719, 1800)

    # Equality and both sides of the necessary-and-sufficient pure-NE boundary.
    # For each exact rational s, x_H is irrational; choose rationals on either side
    # and test the square-root-free equivalent comparison.
    assert x_h_condition(F(7, 10), F(1, 10))
    assert not x_h_condition(F(69, 100), F(1, 10))
    assert x_h_condition(F(9, 10), F(1, 2))
    assert not x_h_condition(F(4, 5), F(1, 2))
    assert x_h_condition(F(1, 2), F(0))

    # An exact equality-boundary point: the small firm is indifferent between
    # its interior response and the no-poaching kink, but only the interior
    # response intersects A's best response.
    s, x = F(6, 47), F(67, 94)
    assert x_h_condition(x, s)
    a, b = source_uniform_prices(s)
    br_a, br_a_m = direct_best_response_candidates("A", b, x, s)
    br_b, br_b_m = direct_best_response_candidates("B", a, x, s)
    assert br_a == profit_a(a, b, x, s) and a in br_a_m
    assert br_b == profit_b(a, b, x, s) and b in br_b_m
    kink_b = a + 2 * x - 1 + s
    assert kink_b in br_b_m and kink_b != b
    assert direct_best_response_candidates("A", kink_b, x, s)[0] > \
        profit_a(a, kink_b, x, s)

    # Below x_H, the direct best-response evaluator finds the kink deviation.
    x_below = F(66, 94)
    assert not x_h_condition(x_below, s)
    br_b, br_b_m = direct_best_response_candidates("B", a, x_below, s)
    kink_below = a + 2 * x_below - 1 + s
    assert br_b_m == (kink_below,)

    # Eq. (15): invalid regression point is no-switch, with direct sign positive.
    tau, s, x = F(1), F(99, 100), F(501, 1000)
    p_a, p_b = (1 + s / 3), (1 - s / 3)
    p_a_d, q_a_d, p_b_d, q_b_d = hbp_weak_prices(x, s)
    direct_gap = hbp_cs_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s, tau) - \
        uniform_cs_direct(p_a, p_b, x, s, tau)
    printed_eq15 = (-52 * x * x + 52 * x + 1 + 34 * s - 36 * s * x - s * s) / 36
    assert direct_gap == F(17993, 4500000)
    assert printed_eq15 == F(1801513, 2250000)

    # Eq. (15) is also wrong on a valid weak-HBP / pure-uniform-NE point.
    tau, s, x = F(1), F(1, 10), F(7, 10)
    assert x < (3 - s) / 4 and x_h_condition(x, s)
    p_a, p_b = source_uniform_prices(s)
    p_a_d, q_a_d, p_b_d, q_b_d = hbp_weak_prices(x, s)
    direct_gap = hbp_cs_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s, tau) - \
        uniform_cs_direct(p_a, p_b, x, s, tau)
    printed_eq15 = (-52 * x * x + 52 * x + 1 + 34 * s - 36 * s * x - s * s) / 36
    assert direct_gap == F(221, 720)
    assert printed_eq15 == F(1279, 3600)
    assert direct_gap > 0 and printed_eq15 > 0

    # Weak-welfare endpoint identity from Eq. (23), evaluated exactly.
    for s in (F(0), F(1, 10), F(1, 2), F(99, 100)):
        xbar = (3 - s) / 4
        eq23 = (28 * xbar * xbar - 28 * xbar + 5
                + 2 * s * (18 * xbar - 13) + 5 * s * s) / 36
        assert eq23 == -(1 + s) * (1 + 9 * s) / 144

    # Strong HBP: the candidate q_A=c is unique when margins must be nonnegative.
    # If below-cost poaching is allowed, a bounded no-demand equilibrium family
    # appears; sales stay zero on the segment, so price transfers cancel in W.
    x, s = F(4, 5), F(1, 2)
    delta = 3 - s - 4 * x
    u = F(-1, 2)
    q_a_m, p_b_m = hbp_strong_unrestricted_family(x, s, u)
    length = 1 - x
    k = 1 - s - 2 * x
    assert delta <= u <= 0
    assert segment_share_a(q_a_m, p_b_m, k, length) == 0
    b_kink = q_a_m - k
    assert p_b_m == b_kink and b_kink >= 2 * length
    # q_A below cost is weakly optimal only because its segment sales are zero;
    # every lower price creates positive sales at a negative margin.
    assert segment_share_a(u, p_b_m, k, length) == 0
    assert u * segment_share_a(u, p_b_m, k, length) == 0
    assert (u - F(1, 10)) * segment_share_a(u - F(1, 10), p_b_m, k, length) < 0

    # Positive markup at q_A is not an equilibrium: A can cut it in half,
    # attracting consumers at a positive margin for a positive payoff.
    lam = F(1, 5)
    p_b_m = lam + 2 * x - 1 + s
    gain_from_undercut = (lam / 2) * segment_share_a(lam / 2, p_b_m, k, length)
    assert gain_from_undercut == lam * lam / 8 > 0

    # Direct CS and industry-profit changes offset on the below-cost family.
    p_a0, q_a0, p_b0, q_b0 = hbp_strong_profile_unrestricted(x, s, F(0))
    p_au, q_au, p_bu, q_bu = hbp_strong_profile_unrestricted(x, s, u)
    cs0 = hbp_cs_direct(p_a0, q_a0, p_b0, q_b0, x, s)
    csu = hbp_cs_direct(p_au, q_au, p_bu, q_bu, x, s)
    assert csu - cs0 == -u * (1 - x)
    profit_a0, profit_b0 = hbp_profits_direct(p_a0, q_a0, p_b0, q_b0, x, s)
    profit_au, profit_bu = hbp_profits_direct(p_au, q_au, p_bu, q_bu, x, s)
    assert profit_au == profit_a0
    assert profit_bu - profit_b0 == u * (1 - x)
    assert (csu + profit_au + profit_bu) == (cs0 + profit_a0 + profit_b0)

    # Direct welfare identity in a strong region that also has a uniform pure NE.
    x, s = F(19, 20), F(1, 2)
    assert x_h_condition(x, s) and x > (3 - s) / 4
    p_a_d, q_a_d, p_b_d, q_b_d = hbp_strong_profile_unrestricted(x, s, F(0))
    p_a_u, p_b_u = source_uniform_prices(s)
    cs_d = hbp_cs_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s)
    cs_u = uniform_cs_direct(p_a_u, p_b_u, x, s)
    pi_a_d, pi_b_d = hbp_profits_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s)
    pi_a_u = p_a_u * share_a_direct(p_a_u, p_b_u, x, s)
    pi_b_u = p_b_u * (1 - share_a_direct(p_a_u, p_b_u, x, s))
    welfare_gap = cs_d + pi_a_d + pi_b_d - cs_u - pi_a_u - pi_b_u
    assert welfare_gap == -(1 - x) * ((1 - x) + 2 * s) / 9


if __name__ == "__main__":
    self_check()
    print("all exact clean-room checks passed")
