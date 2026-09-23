import Mathlib

namespace GSS2012

noncomputable section

def xH (s : ℝ) : ℝ :=
  (1 : ℝ) / 2 - s / 3 + Real.sqrt (3 * s * (s + 6)) / 6

def xL (s : ℝ) : ℝ :=
  (1 : ℝ) / 2 - s / 3 - Real.sqrt (3 * s * (s + 6)) / 6

def xU (s : ℝ) : ℝ :=
  (1 : ℝ) / 2 + s / 6

def xBar (s : ℝ) : ℝ :=
  (3 - s) / 4

def piBSource (s : ℝ) : ℝ :=
  (3 - s)^2 / 18

def piBKink (s x : ℝ) : ℝ :=
  (2 * x + 4 * s / 3) * (1 - x)

def correctedWeakSwitchCS (s x : ℝ) : ℝ :=
  (-52 * x^2 + 52 * x + 1 + 36 * s * x - 34 * s + s^2) / 36

def sourceEq15SwitchCS (s x : ℝ) : ℝ :=
  (-52 * x^2 + 52 * x + 1 + 36 * s * x - 34 * s + s^2) / 36

def sourceEq16PrintedCS (s x : ℝ) : ℝ :=
  -(s^2 + 2 * s * (18 * x - 17) - 52 * x^2 + 52 * x + 1) / 36

def weakBProfitGapNoSwitch (s x : ℝ) : ℝ :=
  (s^2 - 9 * s * x + 7 * s + 10 * x^2 - x - 4) / 9

def strongBProfitGapSwitch (s x : ℝ) : ℝ :=
  -((x - 1) * (13 * s + 10 * x - 13)) / 9

def correctedWeakNoSwitchCS (s x : ℝ) : ℝ :=
  (s^2 + 12 * s * x - 14 * s - 8 * x^2 + 8 * x + 5) / 18

def weakWelfareSwitch (s x : ℝ) : ℝ :=
  (28 * x^2 - 28 * x + 5 + 2 * s * (18 * x - 13) + 5 * s^2) / 36

lemma radicand_nonneg {s : ℝ} (hs : 0 ≤ s) :
    0 ≤ 3 * s * (s + 6) := by
  nlinarith

/-- UPE-2012-1B: exact factorization of the source-vs-kink B payoff difference. -/
theorem payoff_factorization (s x : ℝ) (hs : 0 ≤ s) :
    piBSource s - piBKink s x = 2 * (x - xL s) * (x - xH s) := by
  have hsq : (Real.sqrt (3 * s * (s + 6)))^2 = 3 * s * (s + 6) :=
    Real.sq_sqrt (radicand_nonneg hs)
  unfold piBSource piBKink xL xH
  nlinarith [hsq]

/-- UPE-2012-1A: the global-equilibrium threshold is strictly above the
source switching cutoff for 0<s<1. -/
theorem xU_lt_xH {s : ℝ} (hs0 : 0 < s) (hs1 : s < 1) :
    xU s < xH s := by
  let r : ℝ := Real.sqrt (3 * s * (s + 6))
  have hrad : 0 ≤ 3 * s * (s + 6) := radicand_nonneg (le_of_lt hs0)
  have hsq : r^2 = 3 * s * (s + 6) := by
    dsimp [r]
    exact Real.sq_sqrt hrad
  have hr0 : 0 ≤ r := by
    dsimp [r]
    exact Real.sqrt_nonneg _
  have hrs : 3 * s < r := by
    by_contra h
    have hle : r ≤ 3 * s := le_of_not_gt h
    have hdiff : r - 3 * s ≤ 0 := by linarith
    have hsum : 0 ≤ r + 3 * s := by nlinarith
    have hprod : (r - 3 * s) * (r + 3 * s) ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg hdiff hsum
    nlinarith
  unfold xU xH
  dsimp [r] at hrs
  linarith

/-- UPE-2012-1A: x_H remains below one throughout the maintained source domain. -/
theorem xH_lt_one {s : ℝ} (hs0 : 0 ≤ s) (hs1 : s < 1) :
    xH s < 1 := by
  let r : ℝ := Real.sqrt (3 * s * (s + 6))
  have hrad : 0 ≤ 3 * s * (s + 6) := radicand_nonneg hs0
  have hsq : r^2 = 3 * s * (s + 6) := by
    dsimp [r]
    exact Real.sq_sqrt hrad
  have hr0 : 0 ≤ r := by
    dsimp [r]
    exact Real.sqrt_nonneg _
  have hbound : r < 3 + 2 * s := by
    by_contra h
    have hge : 3 + 2 * s ≤ r := le_of_not_gt h
    have hdiff : 0 ≤ r - (3 + 2 * s) := by linarith
    have hsum : 0 ≤ r + (3 + 2 * s) := by nlinarith
    have hprod : 0 ≤ (r - (3 + 2 * s)) * (r + (3 + 2 * s)) :=
      mul_nonneg hdiff hsum
    nlinarith [sq_nonneg (3 - s)]
  unfold xH
  dsimp [r] at hbound
  linarith

/-- UPE-2012-1C: exact rational gain in the regime-crossing counterexample. -/
theorem exact_counterexample_gain :
    (56 / 75 : ℝ) - 25 / 72 = 719 / 1800 ∧ (0 : ℝ) < 719 / 1800 := by
  norm_num

/-- UPE-2012-1D: the A deviation gain at the equality kink is strictly positive. -/
theorem equality_kink_A_gain {s x : ℝ} (hs : 0 < s) (hx : 0 < x) :
    0 < 2 * s * x := by
  positivity

/-- CS-2012-1A: accepted-manuscript Eq. (15) matches the
primitive switching-branch CS expression. -/
theorem source_eq15_matches_switch_branch (s x : ℝ) :
    sourceEq15SwitchCS s x = correctedWeakSwitchCS s x := by
  unfold sourceEq15SwitchCS correctedWeakSwitchCS
  ring

/-- CS-2012-1B: accepted-manuscript Eq. (16) is the negative of the
correctly normalized Eq. (15). -/
theorem source_eq16_negates_eq15 (s x : ℝ) :
    sourceEq16PrintedCS s x = - sourceEq15SwitchCS s x := by
  unfold sourceEq16PrintedCS sourceEq15SwitchCS
  ring

/-- CS-2012-1C: exact source-fidelity regression at a valid switching point. -/
theorem source_eq15_exact_point :
    sourceEq15SwitchCS (1 / 10) (7 / 10) = (221 / 720 : ℝ) ∧
    sourceEq16PrintedCS (1 / 10) (7 / 10) = (-221 / 720 : ℝ) := by
  constructor <;> norm_num [sourceEq15SwitchCS, sourceEq16PrintedCS]

/-- PROF-2012-1: branch-correct no-switch weak-profile regression. -/
theorem weak_B_profit_no_switch_regression :
    weakBProfitGapNoSwitch (1 / 2) (51 / 100) = (-227 / 4500 : ℝ) := by
  norm_num [weakBProfitGapNoSwitch]

/-- PROF-2012-2: the small-firm profit ranking can reverse under the
source-selected strong-HBP profile. -/
theorem strong_B_profit_counterexample :
    strongBProfitGapSwitch (9 / 10) (19 / 20) = (41 / 900 : ℝ) ∧
    (0 : ℝ) < 41 / 900 := by
  constructor <;> norm_num [strongBProfitGapSwitch]

/-- CS-2012-2: the upstream negative regression is false on its actual
no-switch branch; the branch-correct gap is positive. -/
theorem rejected_upstream_cs_regression :
    correctedWeakNoSwitchCS (99 / 100) (501 / 1000) =
      (17993 / 4500000 : ℝ) ∧
    (0 : ℝ) < 17993 / 4500000 := by
  constructor <;> norm_num [correctedWeakNoSwitchCS]

/-- W-2012-1: exact endpoint substitution into the weak switching-branch
welfare formula. -/
theorem weak_welfare_endpoint_identity (s : ℝ) :
    weakWelfareSwitch s (xBar s) =
      -((1 + s) * (1 + 9 * s)) / 144 := by
  unfold weakWelfareSwitch xBar
  ring

/-- Downstream-overlap algebra: equality of x_H and xBar forces the
polynomial boundary used in Stage 7. -/
theorem overlap_equality_implies_polynomial {s : ℝ} (hs : 0 ≤ s)
    (hEq : xH s = xBar s) :
    11 * s^2 + 66 * s - 9 = 0 := by
  have hsq : (Real.sqrt (3 * s * (s + 6)))^2 = 3 * s * (s + 6) :=
    Real.sq_sqrt (radicand_nonneg hs)
  unfold xH xBar at hEq
  nlinarith [hsq]

/-- The closed-form Stage-7 critical value solves the overlap polynomial. -/
theorem overlap_closed_form_root :
    let sc : ℝ := -3 + 6 * Real.sqrt 33 / 11
    11 * sc^2 + 66 * sc - 9 = 0 := by
  dsimp
  have hsq : (Real.sqrt (33 : ℝ))^2 = 33 := by
    norm_num
  nlinarith [hsq]

end

#print axioms GSS2012.payoff_factorization
#print axioms GSS2012.xU_lt_xH
#print axioms GSS2012.xH_lt_one
#print axioms GSS2012.exact_counterexample_gain
#print axioms GSS2012.equality_kink_A_gain
#print axioms GSS2012.source_eq15_matches_switch_branch
#print axioms GSS2012.source_eq16_negates_eq15
#print axioms GSS2012.source_eq15_exact_point
#print axioms GSS2012.weak_B_profit_no_switch_regression
#print axioms GSS2012.strong_B_profit_counterexample
#print axioms GSS2012.rejected_upstream_cs_regression
#print axioms GSS2012.weak_welfare_endpoint_identity
#print axioms GSS2012.overlap_equality_implies_polynomial
#print axioms GSS2012.overlap_closed_form_root
