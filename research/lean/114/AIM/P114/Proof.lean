import AIM.P114.Definitions

/-! Proofs of the three supporting results listed in NUMERICAL_TARGETS.md.
This module neither imports Challenge nor formalizes the full counterexample. -/

noncomputable section

open MeasureTheory

namespace AIM.P114

private lemma negativeIndicator_eq (x : ℝ) :
    negativeIndicator x = (1 - nonzeroSign x) / 2 := by
  unfold negativeIndicator nonzeroSign
  split_ifs <;> norm_num

private lemma nonzeroSign_mul (x y : ℝ) (hx : x ≠ 0) (hy : y ≠ 0) :
    nonzeroSign (x * y) = nonzeroSign x * nonzeroSign y := by
  rcases hx.lt_or_gt with hx | hx <;> rcases hy.lt_or_gt with hy | hy <;>
    unfold nonzeroSign <;> split_ifs <;> norm_num at * <;> nlinarith

private lemma nonzeroSign_div (x y : ℝ) (hx : x ≠ 0) (hy : y ≠ 0) :
    nonzeroSign (x / y) = nonzeroSign x * nonzeroSign y := by
  rw [div_eq_mul_inv, nonzeroSign_mul _ _ hx (inv_ne_zero hy)]
  simp only [nonzeroSign, inv_lt_zero]

/-- The local sign-count step in manuscript Lemma 1. -/
theorem module_count_identity (a x y z : ℝ)
    (ha : a ≠ 0) (hx : x ≠ 0) (hy : y ≠ 0) (hz : z ≠ 0)
    (hs : x + y + z ≠ 0) :
    moduleCount a x y z = 1 + centeredModule a x y z := by
  unfold moduleCount centeredModule signModule
  simp only [negativeIndicator_eq,
    nonzeroSign_mul x _ hx (div_ne_zero hs ha),
    nonzeroSign_mul y _ hy (div_ne_zero hs ha),
    nonzeroSign_mul z _ hz (div_ne_zero hs ha), nonzeroSign_div _ a hs ha]
  ring

/-- Exact finite sign average, excluding the two degenerate triangle boundaries. -/
theorem sign_second_moment (x y z : ℝ)
    (hx : 0 < x) (hy : 0 < y) (hz : 0 < z)
    (houter : z ≠ x + y) (hinner : z ≠ |x - y|) :
    signSecondMoment x y z = 1 / 2 - triangleIndicator x y z / 4 := by
  have hsum : ¬ x + y + z < 0 := by linarith
  unfold signSecondMoment signModule
  simp only [nonzeroSign, if_neg hx.not_gt, if_neg hy.not_gt, if_neg hz.not_gt,
    if_pos (neg_lt_zero.mpr hx), if_pos (neg_lt_zero.mpr hy), if_neg hsum]
  unfold triangleIndicator
  rcases le_total y x with hxy | hxy
  · rw [abs_of_nonneg (sub_nonneg.mpr hxy)] at *
    rcases houter.lt_or_gt with ho | ho <;> rcases hinner.lt_or_gt with hi | hi <;>
      split_ifs <;> norm_num at * <;> (first | linarith | (simp_all; linarith))
  · rw [abs_of_nonpos (sub_nonpos.mpr hxy)] at *
    rcases houter.lt_or_gt with ho | ho <;> rcases hinner.lt_or_gt with hi | hi <;>
      split_ifs <;> norm_num at * <;> (first | linarith | (simp_all; linarith))

/-- The strict normalized moment inequality, using actual Bochner integrals. -/
theorem variance_mixture_kurtosis {Ω : Type*} [MeasurableSpace Ω]
    (μ : Measure Ω) [IsProbabilityMeasure μ] (V : Ω → ℝ)
    (hV : Integrable V μ) (hV2 : Integrable (fun ω => V ω ^ 2) μ)
    (hmean : 0 < ∫ ω, V ω ∂μ)
    (hvar : 0 < ∫ ω, (V ω - ∫ ω', V ω' ∂μ) ^ 2 ∂μ) :
    3 < 3 * (∫ ω, V ω ^ 2 ∂μ) / (∫ ω, V ω ∂μ) ^ 2 := by
  let a := ∫ ω, V ω ∂μ
  have hsub : Integrable (fun ω => V ω ^ 2 - (2 * a) * V ω) μ :=
    hV2.sub (hV.const_mul (2 * a))
  have hexpand : (∫ ω, (V ω - a) ^ 2 ∂μ) = (∫ ω, V ω ^ 2 ∂μ) - a ^ 2 := by
    calc
      (∫ ω, (V ω - a) ^ 2 ∂μ) =
          ∫ ω, (V ω ^ 2 - (2 * a) * V ω) + a ^ 2 ∂μ := by
        congr 1
        funext ω
        ring
      _ = (∫ ω, V ω ^ 2 ∂μ) - (2 * a) * a + a ^ 2 := by
        rw [integral_add hsub (integrable_const (μ := μ) (a ^ 2)),
          integral_sub hV2 (hV.const_mul (2 * a)), integral_const_mul]
        simp [a]
      _ = (∫ ω, V ω ^ 2 ∂μ) - a ^ 2 := by ring
  change 0 < a at hmean
  change 0 < ∫ ω, (V ω - a) ^ 2 ∂μ at hvar
  rw [hexpand] at hvar
  change 3 < 3 * (∫ ω, V ω ^ 2 ∂μ) / a ^ 2
  apply (lt_div_iff₀ (sq_pos_of_pos hmean)).2
  linarith

end AIM.P114
