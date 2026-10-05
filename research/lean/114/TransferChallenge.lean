import AIM.P114.TransferDefinitions

/-! Candidate frozen boundary for the length and moment-transfer extension.
Placeholders are deliberate and must never be imported into Solution. -/

noncomputable section

open MeasureTheory Filter
open scoped Topology

namespace AIM.P114

/-- The prescribed prime-root lengths give the source's explicit weight bound. -/
theorem core_weight_bound (m : ℕ) (hm : 1 ≤ m) :
    0 ≤ coreWeight m ∧ coreWeight m ≤ 3 / ((m : ℝ) ^ 5 + 3) := by sorry

/-- This is a probability law for all weights in the closed unit interval. -/
theorem contaminated_law_probability {Ω : Type*} [MeasurableSpace Ω]
    (μ ν : Measure Ω) [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (w : ℝ) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    IsProbabilityMeasure (contaminatedLaw w μ ν) := by sorry

/-- A nonnegative bounded observable loses at most `w*B` under contamination. -/
theorem contamination_integral_bound {Ω : Type*} [MeasurableSpace Ω]
    (μ ν : Measure Ω) [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (w B : ℝ) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (hB : 0 ≤ B)
    (f : Ω → ℝ) (hf : Measurable f)
    (hμ : ∀ᵐ x ∂μ, 0 ≤ f x ∧ f x ≤ B)
    (hν : ∀ᵐ x ∂ν, 0 ≤ f x ∧ f x ≤ B) :
    |(∫ x, f x ∂contaminatedLaw w μ ν) - ∫ x, f x ∂μ| ≤ w * B := by sorry

/-- The actual second/fourth moment error for laws supported on the surplus interval. -/
theorem surplus_moment_contamination_bound (m k : ℕ) (hm : 1 ≤ m)
    (hk : k = 1 ∨ k = 2) (μ ν : Measure ℝ)
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (hμ : ∀ᵐ s ∂μ, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1)
    (hν : ∀ᵐ s ∂ν, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1) :
    |(∫ s, surplusEvenMoment m k s ∂contaminatedLaw (coreWeight m) μ ν) -
      ∫ s, surplusEvenMoment m k s ∂μ| ≤
        3 / ((m : ℝ) ^ 5 + 3) * (m : ℝ) ^ k := by sorry

/-- Thus the prescribed lengths transfer both moments with error tending to zero. -/
theorem surplus_moment_contamination_tendsto (k : ℕ) (hk : k = 1 ∨ k = 2)
    (μ ν : ℕ → Measure ℝ)
    [∀ m, IsProbabilityMeasure (μ m)] [∀ m, IsProbabilityMeasure (ν m)]
    (hμ : ∀ m : ℕ, 1 ≤ m → ∀ᵐ s ∂μ m, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1)
    (hν : ∀ m : ℕ, 1 ≤ m → ∀ᵐ s ∂ν m, 0 ≤ s ∧ s ≤ 2 * (m : ℝ) - 1) :
    Tendsto (fun m => (∫ s, surplusEvenMoment m k s
      ∂contaminatedLaw (coreWeight m) (μ m) (ν m)) -
      ∫ s, surplusEvenMoment m k s ∂μ m) atTop (𝓝 0) := by sorry

end AIM.P114
