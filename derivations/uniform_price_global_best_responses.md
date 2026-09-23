# Uniform-price pure equilibrium: global best-response proof

**Status:** Second analytic path for Stage 4A; still awaiting formalization and independent hostile review.

## Setup

Normalize τ to one and write (a=(p_A-c)/\tau), (b=(p_B-c)/\tau), (d=b-a), (s=\sigma/\tau). Assume (0<s<1), (1/2<x=x_0<1), and first restrict margins to (a,b\ge0). From primitive utilities, define

\[
L=-1-s,\quad \alpha=2x-1-s,\quad \beta=2x-1+s,\quad U=1+s.
\]

For a fixed rival price, firm A can choose any (d\le b) and receives margin (a=b-d). Firm B can choose any (d\ge-a) and receives margin (b=a+d). This converts each unilateral problem into a one-dimensional global maximization.

## Payoffs on every demand piece

| Region | (q_A(d)) | (Pi_A(d;b)) | (Pi_B(d;a)) |
|---|---:|---:|---:|
| (d\le L) | 0 | 0 | (a+d) |
| (L<d<\alpha) | ((d-L)/2) | ((b-d)(d-L)/2) | ((a+d)(1-s-d)/2) |
| (\alpha\le d\le\beta) | (x) | (x(b-d)) | ((1-x)(a+d)) |
| (\beta<d<U) | ((d+1-s)/2) | ((b-d)(d+1-s)/2) | ((a+d)(1+s-d)/2) |
| (d\ge U) | 1 | (b-d) | 0 |

Each nonconstant switching-branch payoff is a concave quadratic in (d); each plateau payoff is affine. Thus a global best response is attained at that branch's unique vertex, a feasible endpoint/kink, or the zero-margin endpoint. The unbounded tail gives zero demand to the deviator.

## Exclude capture and zero-margin cases

If (d\le L), A has zero demand. Since (b\ge0), it can choose (a'=(b+1+s)/2>0), giving (d'=(b-1-s)/2>L) and strictly positive demand and profit. Hence full capture by B is not a Nash profile. If (d\ge U), B has zero demand; since (a\ge0), it can choose (b'=(a+1+s)/2>0), producing (d'=(1+s-a)/2<U) and strictly positive demand and profit. Hence full capture by A is not a Nash profile.

If a firm has positive demand and a negative net margin, it earns a negative payoff and can instead set (p_i=c), obtaining zero. The capture cases just excluded also rule out zero-demand boundary profiles. Therefore any equilibrium lies in a positive-demand switching or plateau region and has nonnegative margins; all smooth-branch FOCs below are interior.

## Exclude the no-switch plateau and both kinks

On (\alpha\le d\le\beta), A's payoff (x(b-d)) decreases in (d). At any (d>\alpha), A raises its own price to move (d) down to (\alpha), keeping share (x) and increasing profit. At (d=\alpha), B raises its own price to reach (\beta), keeps share (1-x), and increases profit by ((\beta-\alpha)(1-x)=2s(1-x)>0). At (d=\beta), A raises its price to reach (\alpha), keeping share (x) and increasing profit by (x(\beta-\alpha)=2sx>0). Thus no plateau point or plateau kink is a Nash equilibrium.

## Intersections of smooth switching branches

### A-history consumers switch to B

For (L<d<\alpha), A's first-order condition is (a=d+1+s); B's is (b=1-s-d). Since (d=b-a), the unique intersection is

\[
d^*=-2s/3,\qquad a^*=1+s/3,\qquad b^*=1-s/3.
\]

The branch condition (d^*<\alpha) is equivalent to (x>x_u=1/2+s/6); (d^*>L) holds for (0<s<1).

### B-history consumers switch to A

For (\beta<d<U), the FOCs yield

\[
d=2s/3,\qquad a=1-s/3,\qquad b=1+s/3.
\]

Its branch condition would require (2s/3>\beta=2x-1+s), or (x<1/2-s/6<1/2). It is therefore impossible in the maintained dominance domain (x>1/2).

## Test the source intersection against all deviations

At ((a^*,b^*)), A's payoff on the first switching branch has the unique vertex (d^*). On the plateau, A's best payoff is at (d=\alpha). Direct subtraction gives

\[
\Pi_A(a^*,b^*)-x(b^*-\alpha)=2(x-x_u)^2>0
\quad\text{when }x>x_u.
\]

On the upper switching branch, A's quadratic vertex is (d=s/3), strictly below (\beta>s); A's payoff therefore decreases throughout (d\ge\beta). Its best value on that branch is bounded by the plateau endpoint payoff. The full-A-capture branch is infeasible against (b^*<U); full-B capture gives zero. Thus the source price is A's unique global best response to (b^*) for (x>x_u).

Against (a^*), B's payoff on the first switching branch has the unique vertex (d^*). The no-switch plateau is maximized at (d=\beta), i.e.

\[
b_k=a^*+\beta=2x+4s/3.
\]

B's upper-branch quadratic vertex is (d=s/3<\beta), so the payoff decreases for all (d\ge\beta); its maximum there is also the kink value. Full-A capture yields zero. (Full-B capture is infeasible because (d\ge-a^*>L).)

Set

\[
x_L=\frac12-\frac{s}{3}-\frac{\sqrt{3s(s+6)}}6,
\qquad
x_H=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

Exact factorization gives

\[
\Pi_B(a^*,b^*)-\Pi_B(a^*,b_k)=2(x-x_L)(x-x_H).
\]

Because (x_L<1/2<x), B's source price is a global best response iff (x\ge x_H). At equality B has both (b^*) and (b_k) in its best-response set. But the kink profile itself is not a Nash equilibrium: holding (b_k) fixed, A can move (d=\beta) to (d=\alpha), raise its net price by (2s), retain share (x), and gain (2sx>0).

If (x\le x_u), the source profile lies on or inside the no-switch plateau and is not an equilibrium: at (x<x_u), A can raise its price toward (d=\alpha); at equality B can raise its price toward (d=\beta). If (x_u<x<x_H), the source profile is the only possible smooth-branch intersection, but B strictly prefers the kink (b_k). Combined with the capture, plateau, kink, and infeasible upper-branch exclusions above, no other pure intersection remains.

## Theorem candidate

For (0<s<1), (x\in(1/2,1)), and nonnegative net margins, the pure-strategy Nash correspondence is

\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&x<x_H(s).
\end{cases}
\]

For (s=0), it is the singleton ({(1,1)}). The price-domain reduction in `uniform_price_game_full_demand.md` extends this correspondence to any price strategy space containing (p_i=c) and every (p_i>c).

This path maximizes the (d)-parameterized branch payoffs directly. The regression program `code/uniform_game_cleanroom.py` independently works from clipped primitive cutoffs and does not call the piecewise demand function while evaluating unilateral deviations. Stage 4A remains OPEN until formal and hostile-review checks are complete.
