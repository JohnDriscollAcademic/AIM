import AIM.P114.TransferDefinitions

/-! The actual prescribed-length and moment-contamination step of the source.
This file does not import a Challenge or assume the spectral-law representation. -/

noncomputable section

open MeasureTheory Filter
open scoped Topology

namespace AIM.P114

private lemma primeRootLength_pos (j : ℕ) : 0 < primeRootLength j := by
  apply Real.sqrt_pos.2
  exact_mod_cast (Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime j).pos

private lemma coreLength_nonneg (m : ℕ) : 0 ≤ coreLength m := by
  exact Finset.sum_nonneg fun j _ => (primeRootLength_pos j).le

private lemma coreLength_le (m : ℕ) :
    coreLength m ≤ 3 * (m : ℝ) * primeRootLength (3 * m) := by
  calc
    coreLength m ≤ ∑ _j ∈ Finset.range (3 * m), primeRootLength (3 * m) := by
      apply Finset.sum_le_sum
      intro j hj
      apply Real.sqrt_le_sqrt
      exact_mod_cast (Nat.nth_strictMono Nat.infinite_setOfPred_prime).monotone
        (Finset.mem_range.1 hj).le
    _ = 3 * (m : ℝ) * primeRootLength (3 * m) := by simp

/-- The prescribed prime-root lengths give the source's explicit weight bound. -/
theorem core_weight_bound (m : ℕ) (hm : 1 ≤ m) :
    0 ≤ coreWeight m ∧ coreWeight m ≤ 3 / ((m : ℝ) ^ 5 + 3) := by
  have hmpos : 0 < (m : ℝ) := by exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one hm)
  have hp := primeRootLength_pos (3 * m)
  have hL := coreLength_nonneg m
  have hbound := coreLength_le m
  have hden : 0 < coreLength m + pendantLength m := by
    unfold pendantLength
    positivity
  constructor
  · exact div_nonneg hL hden.le
  · unfold coreWeight
    apply (div_le_div_iff₀ hden (by positivity)).2
    calc
      coreLength m * ((m : ℝ) ^ 5 + 3) =
          coreLength m * (m : ℝ) ^ 5 + 3 * coreLength m := by ring
      _ ≤ (3 * (m : ℝ) * primeRootLength (3 * m)) * (m : ℝ) ^ 5 +
          3 * coreLength m := by gcongr
      _ = 3 * (coreLength m + pendantLength m) := by unfold pendantLength; ring

/-- This is a probability law for all weights in the closed unit interval. -/
theorem contaminated_law_probability {Ω : Type*} [MeasurableSpace Ω]
    (μ ν : Measure Ω) [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (w : ℝ) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    IsProbabilityMeasure (contaminatedLaw w μ ν) := by
  constructor
  simp only [contaminatedLaw, Measure.add_apply, Measure.smul_apply,
    measure_univ, smul_eq_mul, mul_one]
  rw [← ENNReal.ofReal_add (sub_nonneg.mpr hw1) hw0]
  simp

/-- A nonnegative bounded observable loses at most `w*B` under contamination. -/
theorem contamination_integral_bound {Ω : Type*} [MeasurableSpace Ω]
    (μ ν : Measure Ω) [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (w B : ℝ) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (_hB : 0 ≤ B)
    (f : Ω → ℝ) (hf : Measurable f)
    (hμ : ∀ᵐ x ∂μ, 0 ≤ f x ∧ f x ≤ B)
    (hν : ∀ᵐ x ∂ν, 0 ≤ f x ∧ f x ≤ B) :
    |(∫ x, f x ∂contaminatedLaw w μ ν) - ∫ x, f x ∂μ| ≤ w * B := by
  have hfi : ∀ (η : Measure Ω) [IsProbabilityMeasure η],
      (∀ᵐ x ∂η, 0 ≤ f x ∧ f x ≤ B) → Integrable f η := by
    intro η _ hη
    apply (integrable_const B).mono' hf.aestronglyMeasurable
    filter_upwards [hη] with x hx
    simpa [Real.norm_of_nonneg hx.1] using hx.2
  have hfm := hfi μ hμ
  have hfn := hfi ν hν
  have ha0 : 0 ≤ ∫ x, f x ∂μ := integral_nonneg_of_ae (hμ.mono fun _ hx => hx.1)
  have hb0 : 0 ≤ ∫ x, f x ∂ν := integral_nonneg_of_ae (hν.mono fun _ hx => hx.1)
  have haB : (∫ x, f x ∂μ) ≤ B := by
    simpa using integral_mono_ae hfm (integrable_const B) (hμ.mono fun _ hx => hx.2)
  have hbB : (∫ x, f x ∂ν) ≤ B := by
    simpa using integral_mono_ae hfn (integrable_const B) (hν.mono fun _ hx => hx.2)
  have hd : |(∫ x, f x ∂ν) - ∫ x, f x ∂μ| ≤ B := by
    apply abs_le.2
    constructor <;> linarith only [ha0, hb0, haB, hbB]
  unfold contaminatedLaw
  rw [integral_add_measure (hfm.smul_measure ENNReal.ofReal_ne_top)
    (hfn.smul_measure ENNReal.ofReal_ne_top)]
  simp only [integral_smul_measure, ENNReal.toReal_ofReal (sub_nonneg.mpr hw1),
    ENNReal.toReal_ofReal hw0, smul_eq_mul]
  have heq : (1 - w) * (∫ x, f x ∂μ) + w * (∫ x, f x ∂ν) - (∫ x, f x ∂μ) =
      w * ((∫ x, f x ∂ν) - ∫ x, f x ∂μ) := by ring
  rw [heq, abs_mul, abs_of_nonneg hw0]
  exact mul_le_mul_of_nonneg_left hd hw0

private lemma surplusEvenMoment_bounds (m k : ℕ) (hm : 1 ≤ m) (s : ℝ)
    (hs : 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1) :
    0 ≤ surplusEvenMoment m k s ∧ surplusEvenMoment m k s ≤ (m : ℝ) ^ k := by
  have hmpos : 0 < (m : ℝ) := by exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one hm)
  have habs : |s - (2 * (m : ℝ) - 1) / 2| ≤ (m : ℝ) := by
    apply abs_le.2
    constructor <;> linarith [hs.1, hs.2]
  have hdiv : |(s - (2 * (m : ℝ) - 1) / 2) / Real.sqrt (m : ℝ)| ≤
      Real.sqrt (m : ℝ) := by
    rw [abs_div, abs_of_nonneg (Real.sqrt_nonneg _)]
    apply (div_le_iff₀ (Real.sqrt_pos.2 hmpos)).2
    simpa [Real.mul_self_sqrt hmpos.le] using habs
  have hsq : ((s - (2 * (m : ℝ) - 1) / 2) / Real.sqrt (m : ℝ)) ^ 2 ≤ (m : ℝ) := by
    calc
      _ = |(s - (2 * (m : ℝ) - 1) / 2) / Real.sqrt (m : ℝ)| ^ 2 := by simp
      _ ≤ (Real.sqrt (m : ℝ)) ^ 2 := pow_le_pow_left₀ (abs_nonneg _) hdiv 2
      _ = (m : ℝ) := Real.sq_sqrt hmpos.le
  unfold surplusEvenMoment
  rw [pow_mul]
  exact ⟨pow_nonneg (sq_nonneg _) _, pow_le_pow_left₀ (sq_nonneg _) hsq k⟩

/-- The actual second/fourth moment error for laws supported on the surplus interval. -/
theorem surplus_moment_contamination_bound (m k : ℕ) (hm : 1 ≤ m)
    (_hk : k = 1 ∨ k = 2) (μ ν : Measure ℝ)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (hμ : ∀ᵐ s ∂μ, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1)
    (hν : ∀ᵐ s ∂ν, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1) :
    |(∫ s, surplusEvenMoment m k s ∂contaminatedLaw (coreWeight m) μ ν) -
      ∫ s, surplusEvenMoment m k s ∂μ| ≤
        3 / ((m : ℝ) ^ 5 + 3) * (m : ℝ) ^ k := by
  have hw := core_weight_bound m hm
  have hw1 : coreWeight m ≤ 1 := by
    apply hw.2.trans
    apply (div_le_one₀ (by positivity : 0 < (m : ℝ) ^ 5 + 3)).2
    exact le_add_of_nonneg_left (by positivity)
  have hf : Measurable (surplusEvenMoment m k) := by
    unfold surplusEvenMoment
    fun_prop
  have bound := contamination_integral_bound μ ν (coreWeight m) ((m : ℝ) ^ k)
    hw.1 hw1 (by positivity) (surplusEvenMoment m k) hf
    (hμ.mono fun s hs => surplusEvenMoment_bounds m k hm s hs)
    (hν.mono fun s hs => surplusEvenMoment_bounds m k hm s hs)
  exact bound.trans (mul_le_mul_of_nonneg_right hw.2 (by positivity))

/-- Thus the prescribed lengths transfer both moments with error tending to zero. -/
theorem surplus_moment_contamination_tendsto (k : ℕ) (hk : k = 1 ∨ k = 2)
    (μ ν : ℕ → Measure ℝ)
    [∀ m, IsProbabilityMeasure (μ m)] [∀ m, IsProbabilityMeasure (ν m)]
    (hμ : ∀ m : ℕ, 1 ≤ m → ∀ᵐ s ∂μ m, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1)
    (hν : ∀ m : ℕ, 1 ≤ m → ∀ᵐ s ∂ν m, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1) :
    Tendsto (fun m => (∫ s, surplusEvenMoment m k s
      ∂contaminatedLaw (coreWeight m) (μ m) (ν m)) -
      ∫ s, surplusEvenMoment m k s ∂μ m) atTop (𝓝 0) := by
  apply squeeze_zero_norm' (a := fun m : ℕ => 3 / (m : ℝ))
  · filter_upwards [eventually_ge_atTop 1] with m hm
    have hmpos : 0 < (m : ℝ) := by exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one hm)
    have hmone : 1 ≤ (m : ℝ) := by exact_mod_cast hm
    have hexponent : k + 1 ≤ 5 := by rcases hk with rfl | rfl <;> omega
    have hpow := pow_le_pow_right₀ hmone hexponent
    have hrate : 3 / ((m : ℝ) ^ 5 + 3) * (m : ℝ) ^ k ≤ 3 / (m : ℝ) := by
      rw [div_mul_eq_mul_div]
      apply (div_le_div_iff₀ (by positivity) hmpos).2
      calc
        3 * (m : ℝ) ^ k * (m : ℝ) = 3 * (m : ℝ) ^ (k + 1) := by rw [pow_succ]; ring
        _ ≤ 3 * (m : ℝ) ^ 5 := by gcongr
        _ ≤ 3 * ((m : ℝ) ^ 5 + 3) := by linarith
    simpa [Real.norm_eq_abs] using
      (surplus_moment_contamination_bound m k hm hk (μ m) (ν m) (hμ m hm) (hν m hm)).trans hrate
  · exact tendsto_const_div_atTop_nhds_zero_nat 3

end AIM.P114
