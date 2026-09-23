# Stage 1 Reopened — Source Fidelity Recertification after Independent Astra Audit

**Status:** PASS / RECERTIFIED  
**Date:** 2026-09-23  
**Trigger:** independent post-Stage-14 audit identified a false transcription of accepted-manuscript Eq. (15).  
**Controlling source:** Hanken post-referee accepted manuscript, PDF pp. 16–20 of the article body (institutional PDF pp. 19–23).

## 1. Exact re-transcription of the weak-CS sequence

The accepted manuscript gives, on its one-way-switch uniform allocation:

Eq. (13): the uniform-CS integral with the interval from (x_1^u) to (x_0).

Eq. (14): the weak-HBP CS integral.

Eq. (15):
[
CS^d-CS^u
=
-\frac{
\tau^2(52x_0^2-52x_0-1)
+2sigma\tau(17-18x_0)
-sigma^2
}{36\tau}.
]

Expanding the outer minus gives
[
CS^d-CS^u
=
\frac{
-\tau^2(52x_0^2-52x_0-1)
+2sigma\tau(18x_0-17)
+sigma^2
}{36\tau},
]
which is exactly the independently reconstructed primitive switching-branch expression.

Therefore **Eq. (15) is not algebraically wrong on its valid switching branch**.

With (s=sigma/\tau), the correct normalization of Eq. (15) is
[
CS^d-CS^u
=
\frac{\tau}{36}
left[
-52x_0^2+52x_0+1+36sx_0-34s+s^2
\right].
]

The accepted manuscript's printed Eq. (16), however, places an additional minus sign in front of that same bracket:
[
CS^d-CS^u
=
-\frac{\tau}{36}
left[
s^2+2s(18x_0-17)-52x_0^2+52x_0+1
\right] >0.
]

The bracket is algebraically the same as the correct normalized Eq. (15) numerator. Hence the printed Eq. (16) is the **negative** of Eq. (15), not a valid substitution of (sigma=s\tau).

Condition (17), Figure 5, and Result 3 are downstream of that sign reversal.

## 2. Independent exact regression

At
[
s=1/10,qquad x_0=7/10,
]
the actual allocation is on the one-way-switch branch.

Direct primitive integration gives
[
CS^d-CS^u=221/720.
]

Accepted Eq. (15) also gives
[
221/720.
]

The previous project value (1279/3600), labelled as the accepted Eq. (15), came from an erroneous local transcription and is retired.

The accepted Eq. (16) evaluates to
[
-221/720,
]
confirming the sign inversion between Eqs. (15) and (16).

## 3. Independent branch issue

At
[
s=99/100,qquad x_0=501/1000,
]
the accepted uniform candidate has (x_0<x_u=1/2+s/6). The realized allocation is no-switch, so Eq. (13)'s one-way-switch integral is not an actual-allocation integral.

Direct primitive integration gives
[
CS^d-CS^u=17993/4500000>0.
]

Thus Result 3 fails for two distinct reasons that must not be conflated:

1. **source algebra:** Eq. (16) flips the sign of Eq. (15);
2. **allocation branch:** Eqs. (13)/(15) are not the realized profile CS expression when (x_0<x_u).

## 4. Weak profit source mapping

Accepted Eq. (18) substitutes Eq. (12) together with the one-way-switch allocation and therefore gives
[
pi_B^u=(3\tau-sigma)^2/(18\tau).
]

As a profile formula this is valid only when the accepted uniform price vector actually induces the switching branch, i.e. (x_0ge x_u).

If (x_0<x_u), the same price vector induces no switching and instead
[
\frac{pi_B^u}{\tau}
=
left(1-\frac{s}{3}\right)(1-x_0).
]

Consequently accepted Eq. (22) and Result 4 cannot be extrapolated through (x_0=x_u).

For weak HBP, direct primitive profits give
[
\frac{pi_B^d}{\tau}
=
\frac{s^2-6sx_0+4s+10x_0^2-10x_0+5}{9}.
]

Hence the actual source-profile difference is
[
\frac{pi_B^d-pi_B^u}{\tau}
=
\begin{cases}
dfrac{s^2-12sx_0+14s+20x_0^2-20x_0+1}{18},
&x_0ge x_u,\[0.9em]
dfrac{s^2-9sx_0+7s+10x_0^2-x_0-4}{9},
&x_0<x_u.
end{cases}
]

The two branches agree at (x_0=x_u).

Exact no-switch regression:
[
s=1/2,quad x_0=51/100:
qquad
pi_B^d-pi_B^u=-227/4500<0.
]

The invalid switching-branch extension at that point gives (4/375>0).

## 5. Strong endpoint (x_0=1)

At (x_0=1), the inherited B-history segment is empty. Therefore the prices directed only to that empty segment, (q_A) and (p_B), are payoff-irrelevant and are not uniquely pinned, even under nonnegative-margin restrictions.

The nondegenerate strong-HBP selection statement must therefore be written for
[
\bar x(s)le x_0<1.
]

At (x_0=1):

- the active allocation and active-segment outcomes remain well defined;
- the full four-price vector is not unique;
- the strong market-share difference is zero;
- the strong CS difference is zero;
- the strong welfare difference is zero.

## 6. Stage-1 corrected verdict

**PASS / RECERTIFIED.**

Retired claims:

- “accepted Eq. (15) is algebraically wrong”;
- “accepted Eq. (15) evaluates to (1279/3600) at (s=.1,x_0=.7)”.

Certified replacement:

- Eq. (15) is correct on its valid switching branch;
- Eq. (16) is the sign-reversed transformation;
- the no-switch branch requires a different realized-allocation formula;
- Result 3 remains invalid as stated;
- accepted Eq. (22)/Result 4 require branch qualification before any profile interpretation.
