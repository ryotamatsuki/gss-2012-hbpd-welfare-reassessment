"""Symbolic primitive reconstruction of the 2012 welfare formulas.

The script integrates utility and real resource costs directly. It is separate
from the exact-rational profile evaluator in uniform_game_cleanroom.py.
Requires SymPy 1.14 or a compatible current SymPy release.
"""

import sympy as sp


x, s, z = sp.symbols("x s z", real=True)
beta, c, tau = sp.symbols("beta c tau", real=True, positive=True)

# Normalize tau=1, c=beta=0 only after deriving primitive expressions.
# Price entries below are net margins in these normalized units.
a_u, b_u = 1 + s / 3, 1 - s / 3
x_u = sp.Rational(1, 2) + s / 6

p_a_w = (2 * x + 1 + s) / 3
q_a_w = (3 - 4 * x - s) / 3
p_b_w = (3 - 2 * x + s) / 3
q_b_w = (4 * x - 1 - s) / 3
x_a = (2 * x + 1 + s) / 6
x_b = (2 * x + 3 - s) / 6

cs_hbp_weak = (
    sp.integrate(-p_a_w - z, (z, 0, x_a))
    + sp.integrate(-q_b_w - 1 + z - s, (z, x_a, x))
    + sp.integrate(-q_a_w - z - s, (z, x, x_b))
    + sp.integrate(-p_b_w - 1 + z, (z, x_b, 1))
)
cs_uniform_switch = (
    sp.integrate(-a_u - z, (z, 0, x_u))
    + sp.integrate(-b_u - 1 + z - s, (z, x_u, x))
    + sp.integrate(-b_u - 1 + z, (z, x, 1))
)
cs_uniform_no_switch = (
    sp.integrate(-a_u - z, (z, 0, x))
    + sp.integrate(-b_u - 1 + z, (z, x, 1))
)

gap_weak_switch = sp.factor(cs_hbp_weak - cs_uniform_switch)
gap_weak_no_switch = sp.factor(cs_hbp_weak - cs_uniform_no_switch)
expected_weak_switch = (
    -52 * x**2 + 52 * x + 1 + 36 * s * x - 34 * s + s**2
) / 36
expected_weak_no_switch = (
    s**2 + 12 * s * x - 14 * s - 8 * x**2 + 8 * x + 5
) / 18
assert sp.factor(gap_weak_switch - expected_weak_switch) == 0
assert sp.factor(gap_weak_no_switch - expected_weak_no_switch) == 0
assert sp.factor(gap_weak_switch.subs(x, x_u) - gap_weak_no_switch.subs(x, x_u)) == 0

# Strong HBP candidate (q_A=c) against the two actual uniform allocation branches.
p_a_s, q_a_s = p_a_w, sp.Integer(0)
p_b_s, q_b_s = 2 * x - 1 + s, q_b_w
cs_hbp_strong = (
    sp.integrate(-p_a_s - z, (z, 0, x_a))
    + sp.integrate(-q_b_s - 1 + z - s, (z, x_a, x))
    + sp.integrate(-p_b_s - 1 + z, (z, x, 1))
)
gap_strong_switch = sp.factor(cs_hbp_strong - cs_uniform_switch)
gap_strong_no_switch = sp.factor(cs_hbp_strong - cs_uniform_no_switch)
expected_strong_switch = (1 - x) * (16 - 7 * x - 13 * s) / 9
expected_strong_no_switch = (
    s**2 + 40 * s * x - 46 * s + 64 * x**2 - 128 * x + 73
) / 36
assert sp.factor(gap_strong_switch - expected_strong_switch) == 0
assert sp.factor(gap_strong_no_switch - expected_strong_no_switch) == 0
assert sp.factor(gap_strong_switch.subs(x, x_u) - gap_strong_no_switch.subs(x, x_u)) == 0

# Social welfare from primitive transport and switching costs.
cost_weak = (
    sp.integrate(z, (z, 0, x_a))
    + sp.integrate(1 - z, (z, x_a, x))
    + sp.integrate(z, (z, x, x_b))
    + sp.integrate(1 - z, (z, x_b, 1))
    + s * ((x - x_a) + (x_b - x))
)
cost_strong = (
    sp.integrate(z, (z, 0, x_a))
    + sp.integrate(1 - z, (z, x_a, x))
    + sp.integrate(1 - z, (z, x, 1))
    + s * (x - x_a)
)
cost_uniform_switch = (
    sp.integrate(z, (z, 0, x_u))
    + sp.integrate(1 - z, (z, x_u, x))
    + sp.integrate(1 - z, (z, x, 1))
    + s * (x - x_u)
)
cost_uniform_no_switch = (
    sp.integrate(z, (z, 0, x))
    + sp.integrate(1 - z, (z, x, 1))
)

gap_welfare_weak_switch = sp.factor(cost_uniform_switch - cost_weak)
gap_welfare_weak_no_switch = sp.factor(cost_uniform_no_switch - cost_weak)
expected_welfare_weak_switch = (
    28 * x**2 - 28 * x + 5 + 2 * s * (18 * x - 13) + 5 * s**2
) / 36
expected_welfare_weak_no_switch = (
    5 * s**2 - 4 * s + 32 * x**2 - 32 * x + 7
) / 18
assert sp.factor(gap_welfare_weak_switch - expected_welfare_weak_switch) == 0
assert sp.factor(gap_welfare_weak_no_switch - expected_welfare_weak_no_switch) == 0
assert sp.factor(
    gap_welfare_weak_switch.subs(x, x_u)
    - gap_welfare_weak_no_switch.subs(x, x_u)
) == 0

gap_welfare_strong_switch = sp.factor(cost_uniform_switch - cost_strong)
gap_welfare_strong_no_switch = sp.factor(cost_uniform_no_switch - cost_strong)
expected_welfare_strong_switch = -(1 - x) * ((1 - x) + 2 * s) / 9
expected_welfare_strong_no_switch = -(
    (5 * (1 + s) - 8 * x) * (4 * x - 1 - s)
) / 36
assert sp.factor(gap_welfare_strong_switch - expected_welfare_strong_switch) == 0
assert sp.factor(gap_welfare_strong_no_switch - expected_welfare_strong_no_switch) == 0
assert sp.factor(
    gap_welfare_strong_switch.subs(x, x_u)
    - gap_welfare_strong_no_switch.subs(x, x_u)
) == 0

# Result 1's weak-branch share gap and the best-response kink factorization.
share_uniform_switch = x_u
share_hbp_weak = (2 - x) / 3
share_hbp_strong = x_a
assert sp.factor(share_uniform_switch - share_hbp_weak - (2 * x + s - 1) / 6) == 0
assert sp.factor(share_uniform_switch - share_hbp_strong - (1 - x) / 3) == 0

x_l = sp.Rational(1, 2) - s / 3 - sp.sqrt(3 * s * (s + 6)) / 6
x_h = sp.Rational(1, 2) - s / 3 + sp.sqrt(3 * s * (s + 6)) / 6
pi_b_source = (3 - s) ** 2 / 18
pi_b_kink = (2 * x + 4 * s / 3) * (1 - x)
assert sp.simplify(pi_b_source - pi_b_kink - 2 * (x - x_l) * (x - x_h)) == 0

# Correct endpoint identities and branch domains.
x_bar = (3 - s) / 4
assert sp.factor(gap_welfare_weak_switch.subs(x, x_bar) + (1 + s) * (1 + 9 * s) / 144) == 0
assert sp.factor(gap_welfare_weak_no_switch.subs(x, x_bar) - (s - 1) * (7 * s - 1) / 18) == 0
assert sp.factor(gap_welfare_strong_no_switch.subs(x, x_bar) - (s - 1) * (7 * s - 1) / 18) == 0

print("all symbolic primitive welfare identities passed")
