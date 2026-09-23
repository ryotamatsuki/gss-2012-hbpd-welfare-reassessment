"""Exact symbolic identities for the Stage-7 downstream impact audit.

This file does not prove interval inequalities by numerical sampling. It records
the algebraic endpoint/factor identities used by the analytic sign proofs in
results/stage07_downstream_impact.md.
"""

import sympy as sp


def assert_zero(expr):
    """Version-stable symbolic equality check."""
    assert sp.factor(sp.together(expr)) == 0


x, s = sp.symbols("x s", real=True)
xu = sp.Rational(1, 2) + s / 6
xbar = (3 - s) / 4

# Weak-HBP versus the accepted-version uniform price profile.
cs_weak_switch_num = -52*x**2 + 52*x + 1 + 36*s*x - 34*s + s**2
cs_weak_noswitch_num = s**2 + 12*s*x - 14*s - 8*x**2 + 8*x + 5

assert_zero(
    cs_weak_switch_num.subs(x, xu)
    - 2 * (25*s**2 - 72*s + 63) / 9
)
assert_zero(
    cs_weak_switch_num.subs(x, xbar)
    + (s + 1) * (45*s - 43) / 4
)
assert_zero(
    cs_weak_noswitch_num.subs(x, sp.Rational(1, 2))
    - (s - 7) * (s - 1)
)
assert_zero(
    cs_weak_noswitch_num.subs(x, xu)
    - (25*s**2 - 72*s + 63) / 9
)
assert_zero(
    cs_weak_noswitch_num.subs(x, xbar)
    + (s - 1) * (5*s + 13) / 2
)

# Weak-HBP profit differences (HBP minus uniform), normalized by tau.
pi_a_weak_gap = (
    s**2 + 12*s*x - 10*s + 20*x**2 - 20*x + 1
) / 18
pi_b_weak_gap = (
    s**2 - 12*s*x + 14*s + 20*x**2 - 20*x + 1
) / 18
industry_weak_gap = (
    s**2 + 2*s + 20*x**2 - 20*x + 1
) / 9

# Endpoint identities used to show B's gap is strictly negative throughout
# the corrected weak-HBP / pure-uniform overlap.
assert_zero(
    (18*pi_b_weak_gap).subs(x, sp.Rational(1, 2))
    - (s**2 + 8*s - 4)
)
assert_zero(
    (18*pi_b_weak_gap).subs(x, xbar)
    - (s + 1) * (21*s - 11) / 4
)
assert_zero(sp.diff(18*pi_b_weak_gap, x, 2) - 40)

# Exact pure-overlap boundary: x_H(s)=xbar.
scrit = -3 + 6*sp.sqrt(33)/11
# Squared-equation polynomial after isolating the positive radical.
overlap_poly = 11*s**2 + 66*s - 9
assert_zero(overlap_poly.subs(s, scrit))

# Weak social-welfare gap (HBP minus uniform) on the only branch relevant
# to a pure-uniform equilibrium in weak dominance.
w_weak_switch = (
    28*x**2 - 28*x + 5 + 2*s*(18*x - 13) + 5*s**2
) / 36
assert_zero(
    w_weak_switch.subs(x, xbar)
    + (1+s)*(1+9*s)/144
)

# Strong-HBP selected source member (q_A=c): exact differences.
cs_strong_gap = (1-x)*(16-7*x-13*s)/9
pi_a_strong_gap = 2*(x-1)*(s+x+2)/9
pi_b_strong_gap = (1-x)*(13*s+10*x-13)/9
industry_strong_gap = (1-x)*(11*s+8*x-17)/9
w_strong_gap = -(1-x)*(1-x+2*s)/9

# Equality of social welfare across the below-cost strong-HBP zero-sales
# selection family is checked in uniform_game_cleanroom.py.

print("all Stage-7 symbolic impact identities passed")
