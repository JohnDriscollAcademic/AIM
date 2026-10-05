import AIM.P114.MixtureDefinitions
import AIM.P114.Proof

/-! The actual standardized Gaussian variance-mixture inference.
The distribution, its integrability, and its moments are constructed here;
none is assumed as an input certificate. -/

noncomputable section

open MeasureTheory ProbabilityTheory

namespace AIM.P114

/-- The fourth moment is obtained from four derivatives of the existing
Gaussian MGF, rather than assumed as a moment specification. -/
theorem standard_gaussian_fourth_moment :
    (∫ z : ℝ, z ^ 4 ∂gaussianReal 0 1) = 3 := by
  let g : ℝ → ℝ := fun t => Real.exp (t ^ 2 / 2)
  have h0 (t : ℝ) : HasDerivAt g (t * g t) t := by
    convert! (((hasDerivAt_id t).pow 2).div_const 2).exp using 1; dsimp [g]; ring
  have h1 (t : ℝ) : HasDerivAt (fun s => s * g s) ((1 + t ^ 2) * g t) t := by
    convert! (hasDerivAt_id t).mul (h0 t) using 1; dsimp; ring
  have h2 (t : ℝ) : HasDerivAt (fun s => (1 + s ^ 2) * g s)
      ((3 * t + t ^ 3) * g t) t := by
    convert! ((hasDerivAt_const t (1 : ℝ)).add ((hasDerivAt_id t).pow 2)).mul
      (h0 t) using 1; dsimp; ring
  have h3 (t : ℝ) : HasDerivAt (fun s => (3 * s + s ^ 3) * g s)
      ((3 + 6 * t ^ 2 + t ^ 4) * g t) t := by
    convert! (((hasDerivAt_id t).const_mul 3).add ((hasDerivAt_id t).pow 3)).mul
      (h0 t) using 1; dsimp; ring
  have d0 : deriv g = fun t => t * g t := funext fun t => (h0 t).deriv
  have d1 : deriv (fun t => t * g t) = fun t => (1 + t ^ 2) * g t :=
    funext fun t => (h1 t).deriv
  have d2 : deriv (fun t => (1 + t ^ 2) * g t) = fun t => (3 * t + t ^ 3) * g t :=
    funext fun t => (h2 t).deriv
  have d3 : deriv (fun t => (3 * t + t ^ 3) * g t) =
      fun t => (3 + 6 * t ^ 2 + t ^ 4) * g t := funext fun t => (h3 t).deriv
  have hmgf : mgf (fun z : ℝ => z) (gaussianReal 0 1) = g := by
    rw [mgf_fun_id_gaussianReal]
    simp [g]
  have hm := iteratedDeriv_mgf_zero (X := fun z : ℝ => z)
    (μ := gaussianReal 0 1) (by simp) 4
  change iteratedDeriv 4 (mgf (fun z : ℝ => z) (gaussianReal 0 1)) 0 =
    (∫ z : ℝ, z ^ 4 ∂gaussianReal 0 1) at hm
  rw [← hm, hmgf]
  norm_num [iteratedDeriv_succ, iteratedDeriv_zero, d0, d1, d2, d3, g]

private lemma standard_gaussian_second_moment :
    (∫ z : ℝ, z ^ 2 ∂gaussianReal 0 1) = 1 := by
  have h := variance_fun_id_gaussianReal (μ := 0) (v := 1)
  rw [variance_eq_integral (by fun_prop)] at h
  simpa using h

private lemma standard_gaussian_integrable_power (n : ℕ) :
    Integrable (fun z : ℝ => z ^ n) (gaussianReal 0 1) := by
  have hMem : MemLp (fun z : ℝ => z) (n : ENNReal) (gaussianReal 0 1) := by
    convert! (memLp_id_gaussianReal' (μ := 0) (v := 1) (n : ENNReal) (by simp)) using 1
  apply (integrable_norm_iff (by fun_prop)).mp
  simpa only [norm_pow] using hMem.integrable_norm_pow'

private lemma mixing_memLp_two
    {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : Measurable V)
    (hbound : ∀ᵐ ω ∂μ, (1 / 4 : ℝ) < V ω ∧ V ω < (1 / 2 : ℝ)) :
    MemLp V 2 μ := by
  apply memLp_of_bounded (a := 1 / 4) (b := 1 / 2) _ hV.aestronglyMeasurable 2
  filter_upwards [hbound] with ω hω using ⟨hω.1.le, hω.2.le⟩

private lemma mixing_mean_lower
    {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : Measurable V)
    (hbound : ∀ᵐ ω ∂μ, (1 / 4 : ℝ) < V ω ∧ V ω < (1 / 2 : ℝ)) :
    (1 / 4 : ℝ) ≤ ∫ ω, V ω ∂μ := by
  have hi := (mixing_memLp_two μ V hV hbound).integrable (by norm_num)
  have h := integral_mono_ae (integrable_const (μ := μ) (1 / 4 : ℝ)) hi
    (hbound.mono fun _ h => h.1.le)
  simpa using h

/-- Integrability and moment identities for the actual pushforward law. -/
theorem normalized_variance_mixture_moments
    {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : Measurable V)
    (hbound : ∀ᵐ ω ∂μ, (1 / 4 : ℝ) < V ω ∧ V ω < (1 / 2 : ℝ)) :
    IsProbabilityMeasure (normalizedVarianceMixture μ V) ∧
    Integrable (fun z : ℝ => z) (normalizedVarianceMixture μ V) ∧
    Integrable (fun z : ℝ => z ^ 2) (normalizedVarianceMixture μ V) ∧
    Integrable (fun z : ℝ => z ^ 4) (normalizedVarianceMixture μ V) ∧
    (∫ z : ℝ, z ∂normalizedVarianceMixture μ V) = 0 ∧
    (∫ z : ℝ, z ^ 2 ∂normalizedVarianceMixture μ V) = 1 ∧
    (∫ z : ℝ, z ^ 4 ∂normalizedVarianceMixture μ V) =
      3 * (∫ ω, V ω ^ 2 ∂μ) / (∫ ω, V ω ∂μ) ^ 2 := by
  let a := ∫ ω, V ω ∂μ
  let H : Ω → ℝ := fun ω => Real.sqrt (V ω / a)
  let F : Ω × ℝ → ℝ := fun p => p.2 * H p.1
  let γ := gaussianReal 0 1
  have haLower : (1 / 4 : ℝ) ≤ a := mixing_mean_lower μ V hV hbound
  have ha : 0 < a := lt_of_lt_of_le (by norm_num) haLower
  have hHm : Measurable H := by dsimp [H]; fun_prop
  have hFm : Measurable F := by dsimp [F]; fun_prop
  have hHb : ∀ᵐ ω ∂μ, H ω ∈ Set.Icc (0 : ℝ) 2 := by
    filter_upwards [hbound] with ω hω
    have hv : 0 ≤ V ω / a := div_nonneg (by linarith [hω.1]) ha.le
    have hv2 : V ω / a ≤ 2 := (div_le_iff₀ ha).2 (by linarith [hω.2])
    have hs := Real.sq_sqrt hv
    have hp := Real.sqrt_nonneg (V ω / a)
    dsimp [H]
    exact ⟨hp, by nlinarith⟩
  have hHi (n : ℕ) : Integrable (fun ω => H ω ^ n) μ := by
    have hM : MemLp H (n : ENNReal) μ :=
      memLp_of_bounded hHb hHm.aestronglyMeasurable n
    have hn : Integrable (fun ω => ‖H ω‖ ^ n) μ := hM.integrable_norm_pow'
    simpa only [H, Real.norm_eq_abs, abs_of_nonneg (Real.sqrt_nonneg _)] using hn
  have hFi (n : ℕ) : Integrable (fun p => F p ^ n) (μ.prod γ) := by
    have hprod := (hHi n).mul_prod (standard_gaussian_integrable_power n)
    simpa [F, γ, mul_pow, mul_comm] using hprod
  have hmapInt (n : ℕ) : Integrable (fun z : ℝ => z ^ n) (normalizedVarianceMixture μ V) := by
    change Integrable (fun z : ℝ => z ^ n) (Measure.map F (μ.prod γ))
    exact (integrable_map_measure (by fun_prop) hFm.aemeasurable).2 (hFi n)
  have hm (n : ℕ) :
      (∫ z : ℝ, z ^ n ∂normalizedVarianceMixture μ V) =
        (∫ ω, H ω ^ n ∂μ) * (∫ z : ℝ, z ^ n ∂γ) := by
    change (∫ z : ℝ, z ^ n ∂Measure.map F (μ.prod γ)) = _
    rw [integral_map hFm.aemeasurable (by fun_prop)]
    simpa [F, mul_pow, mul_comm] using
      (integral_prod_mul (μ := μ) (ν := γ) (fun ω => H ω ^ n) (fun z : ℝ => z ^ n))
  have hH2 : (fun ω => H ω ^ 2) =ᵐ[μ] fun ω => V ω / a := by
    filter_upwards [hbound] with ω hω
    exact Real.sq_sqrt (div_nonneg (by linarith [hω.1]) ha.le)
  have hH4 : (fun ω => H ω ^ 4) =ᵐ[μ] fun ω => V ω ^ 2 / a ^ 2 := by
    filter_upwards [hH2] with ω hω
    calc
      H ω ^ 4 = (H ω ^ 2) ^ 2 := by ring
      _ = (V ω / a) ^ 2 := by rw [hω]
      _ = V ω ^ 2 / a ^ 2 := div_pow _ _ _
  have hI2 : (∫ ω, H ω ^ 2 ∂μ) = 1 := by
    rw [integral_congr_ae hH2]
    simp only [div_eq_mul_inv, integral_mul_const]
    exact mul_inv_cancel₀ ha.ne'
  have hI4 : (∫ ω, H ω ^ 4 ∂μ) = (∫ ω, V ω ^ 2 ∂μ) / a ^ 2 := by
    rw [integral_congr_ae hH4]
    simp only [div_eq_mul_inv, integral_mul_const]
  refine ⟨?_, ?_, hmapInt 2, hmapInt 4, ?_, ?_, ?_⟩
  · change IsProbabilityMeasure (Measure.map F (μ.prod γ))
    exact Measure.isProbabilityMeasure_map hFm.aemeasurable
  · simpa using hmapInt 1
  · simpa [γ] using hm 1
  · rw [hm 2, hI2]
    simpa [γ] using standard_gaussian_second_moment
  · rw [hm 4, hI4]
    simp only [γ, standard_gaussian_fourth_moment]
    dsimp [a]
    ring

/-- Actual law nonequality follows from the proved fourth moments and the
strict variance inequality, with nonconstancy checked on the mixing variable. -/
theorem normalized_variance_mixture_not_gaussian
    {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) [IsProbabilityMeasure μ]
    (V : Ω → ℝ) (hV : Measurable V)
    (hbound : ∀ᵐ ω ∂μ, (1 / 4 : ℝ) < V ω ∧ V ω < (1 / 2 : ℝ))
    (hnonconstant : ¬ ∃ c : ℝ, V =ᵐ[μ] fun _ => c) :
    normalizedVarianceMixture μ V ≠ gaussianReal 0 1 := by
  have hM := mixing_memLp_two μ V hV hbound
  have hvpos : 0 < variance V μ := by
    refine lt_of_le_of_ne (variance_nonneg V μ) ?_
    intro hv
    exact hnonconstant ⟨∫ ω, V ω ∂μ, ae_eq_integral_of_variance_eq_zero hM hv.symm⟩
  have hmean : 0 < ∫ ω, V ω ∂μ :=
    lt_of_lt_of_le (by norm_num) (mixing_mean_lower μ V hV hbound)
  have hk := variance_mixture_kurtosis μ V (hM.integrable (by norm_num)) hM.integrable_sq
    hmean (by simpa only [variance_eq_integral hV.aemeasurable] using hvpos)
  have hm := (normalized_variance_mixture_moments μ V hV hbound).2.2.2.2.2.2
  intro heq
  rw [heq, standard_gaussian_fourth_moment] at hm
  linarith

end AIM.P114
