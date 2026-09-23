# Uniform-price game: primitive demand and provisional pure-equilibrium theorem

**Status:** Stage 4 working derivation; not yet certified at Stage 4A and not a frozen theorem.

## 1. Primitive choices and normalization

Let (x=x_0\in(1/2,1)), (s=\sigma/\tau\in[0,1)), and let

\[
a=(p_A-c)/\tau,\qquad b=(p_B-c)/\tau,\qquad d=b-a.
\]

For an A-history consumer at location (z\le x), the payoff difference between staying with A and switching to B is

\[
U_A(z)-U_B(z)=p_B-p_A+\tau(1-2z)+\sigma.
\]

For a B-history consumer at (z>x), the payoff difference between switching to A and staying with B is

\[
U_A(z)-U_B(z)=p_B-p_A+\tau(1-2z)-\sigma.
\]

Thus the two indifferent locations, before clipping, are

\[
t_A=\frac{d+1+s}{2},\qquad t_B=\frac{d+1-s}{2}.
\]

The primitive full-demand correspondence is

\[
q_A(d)=\operatorname{clip}(t_A,0,x)+\operatorname{clip}(t_B-x,0,1-x),\qquad q_B=1-q_A.
\]

The formulas use the measure-zero indifferent consumer only through a tie convention; market shares and profits are unaffected by that convention.

## 2. Complete demand regimes

For (0<s<1), define

\[
L=-1-s,\quad \alpha=2x-1-s,\quad \beta=2x-1+s,\quad U=1+s.
\]

Because (t_A-t_B=s>0), both directions of switching cannot occur simultaneously. The clipped primitive formula gives:

| Price-difference region | A-history allocation | B-history allocation | (q_A) |
|---|---|---|---|
| (d\le L) | A-history consumers switch to B | all stay with B | 0 |
| (L<d<\alpha) | A-history consumers below (t_A) stay A; those above switch to B | all stay B | ((d+1+s)/2) |
| (\alpha\le d\le\beta) | all A-history consumers stay A | all B-history consumers stay B | (x) |
| (\beta<d<U) | all A-history consumers stay A | B-history consumers below (t_B) switch to A | ((d+1-s)/2) |
| (d\ge U) | all A-history consumers stay A | all B-history consumers switch to A | 1 |

The first row means full capture by B: every consumer buys B. More simply, the table's aggregate statement is (q_A=0), (q_B=1). At exact boundaries the formulas agree. A more detailed branch description is:

* (d\le L): full capture by B.
* (L<d<\alpha): A-to-B switching only.
* (\alpha\le d\le\beta): no switching; the inherited shares remain (x) and (1-x).
* (\beta<d<U): B-to-A switching only.
* (d\ge U): full capture by A.

The (s=0) limit has coincident thresholds and no positive-length no-switch plateau; the demand reduces to the ordinary clipped Hotelling share.

## 3. Profits and source candidate

With net margins (a,b\ge0), normalized profits are

\[
\Pi_A(a,b)=a q_A(b-a),\qquad \Pi_B(a,b)=b[1-q_A(b-a)].
\]

For (0<s<1), the profile in the HECER 2010 version's Eq. (12) is

\[
a^*=1+s/3,\qquad b^*=1-s/3,\qquad d^*=-2s/3.
\]

The switching cutoff at that profile is (t_A^*=x_u=1/2+s/6). If (x<x_u), the actual allocation is the no-switch plateau (q_A=x); the source's displayed uniform-price CS integral instead orders the cutoff and (x_0) as if (x_u\le x_0). If (x>x_u), A-history consumers with (z\in(x_u,x)) switch to B and B-history consumers stay with B.

## 4. Candidate pure-strategy correspondence under a nonnegative-margin domain

This statement is provisional pending the independent Stage 4A proof. It is first derived on the explicit margin domain (a,b\in[0,\infty)); the next subsection shows why extending the price domain below cost does not add pure equilibria.

For (s=0), the candidate correspondence is the singleton ({(a,b)=(1,1)}).

For (0<s<1), define

\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}{6}.
\]

The candidate result is

\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&1/2<x<x_H(s).
\end{cases}
\]

The dimensional threshold is

\[
x_H(\sigma/\tau)=\frac12-\frac{\sigma}{3\tau}
+\frac{\sqrt{3(\sigma/\tau)(\sigma/\tau+6)}}{6}.
\]

There is no multiplicity of Nash profiles on (x=x_H(s)): B has two best-response prices against (a^*) (the source price and the no-poaching kink), but the kink profile is not an intersection of both firms' best responses. The equilibrium set itself remains the singleton source profile.

### Proof map to be independently certified

1. Capture regions with (q_A=0) or (q_A=1) are eliminated by a small positive-margin deviation by the excluded firm.
2. In the A-to-B switching branch, the two interior FOCs give the source profile. The branch condition is (x>x_u).
3. In the B-to-A switching branch, the two interior FOCs give (a=1-s/3, b=1+s/3,d=2s/3), which violates (d>\beta) for every (x>1/2).
4. On the no-switch plateau, A wants to raise its margin up to (d=\alpha), while B wants to raise its margin up to (d=\beta). Since (\alpha<\beta), no plateau profile is a mutual best response. The same directional deviations eliminate the plateau endpoints.
5. Against (b^*), A's source-branch optimum is the source price. Its best plateau boundary payoff is lower by

   \[
   (a^*q_A^*)-x(b^*-\alpha)=2(x-x_u)^2.
   \]

   The upper switching branch cannot improve on its plateau boundary for (x>1/2).
6. Against (a^*), B's source-branch optimum is the source price. The best plateau/no-poaching kink is (b_k=a^*+\beta=2x+4s/3). Its payoff comparison is

   \[
   \Pi_B(a^*,b^*)-\Pi_B(a^*,b_k)=2(x-x_L)(x-x_H),
   \quad x_L=\frac12-\frac{s}{3}-\frac{\sqrt{3s(s+6)}}6<\frac12.
   \]

   Therefore the source candidate passes this global comparison iff (x\ge x_H(s)). Beyond the kink, B's payoff falls. If (x<x_H(s)), either the candidate is on the plateau ((x\le x_u)) and A is not best responding, or it is on the A-to-B branch but B prefers the kink. The branch and corner enumeration above is intended to exclude all other pure intersections.

The final sentence is the most delicate completeness step and remains open to hostile independent review. No mixed-strategy result is claimed.

## 5. Price-domain reduction

The author-version model text explicitly states full market coverage and the utility function, but the accessible pages do not impose (p_i\ge c) as a formal strategy restriction. The pure-equilibrium correspondence can nevertheless be reduced to nonnegative margins if the strategy space contains (p_i=c) and all higher prices.

* If a firm has positive demand and a negative net margin, its profit is negative; it can set (p_i=c) and secure a nonnegative profit.
* In a full-capture profile, the captured firm cannot have a negative net margin at equilibrium for the same reason. If its net margin is nonnegative, the excluded firm can choose a strictly positive net margin just below the corresponding capture threshold and earn a positive profit.

Thus no pure equilibrium uses negative net margins. This establishes that the candidate pure correspondence is the same on the unrestricted real-price domain and on (p_i\ge c). The exact Eq. (12) profitable-deviation counterexample below is itself strictly above cost and does not depend on this reduction.

The zero-margin boundary is also excluded. The clipped share (q_A(d)) is continuous. If (a=0) and (q_A(d)>0), raising A's margin to a sufficiently small (\epsilon>0) changes (d) continuously and preserves positive A demand, yielding positive profit instead of zero. If (q_A=0), the profile is full capture by B, already excluded. Symmetrically, if (b=0) and (q_B>0), a small positive increase in B's margin preserves positive B demand and yields positive profit; if (q_B=0), the profile is full capture by A, already excluded. Hence all equilibrium candidates have (a,b>0).

## 6. Exact source-candidate deviation

For ((\tau,\sigma,x,c)=(1,1/2,3/5,0)), the source candidate is ((p_A,p_B)=(7/6,5/6)), with B profit (25/72). The deviation (p'_B=28/15) makes (d=\beta), so the allocation is at the no-switch kink and B's profit is (56/75). The exact gain is

\[
\frac{56}{75}-\frac{25}{72}=\frac{719}{1800}>0.
\]

This point is inside the author-version weak-dominance domain because (1/2<3/5<5/8). It is a pure-price counterexample; it makes no claim about mixed equilibrium.
