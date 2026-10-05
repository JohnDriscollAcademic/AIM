import Mathlib.Probability.Distributions.Gaussian.Real
import Mathlib.MeasureTheory.Integral.Prod

/-! Actual Gaussian variance-mixture law for the concluding step of the
AIM 114 manuscript. This module does not identify the mixing variable with
the graph construction or establish convergence to the law. -/

noncomputable section

open MeasureTheory ProbabilityTheory

namespace AIM.P114

/-- The distribution of `Z * sqrt(V / E[V])`, with independent standard
Gaussian `Z`, constructed on the product probability space. The definition
is total; the theorem hypotheses ensure positive normalization. -/
def normalizedVarianceMixture {Ω : Type*} [MeasurableSpace Ω]
    (μ : Measure Ω) (V : Ω → ℝ) : Measure ℝ :=
  Measure.map (fun p : Ω × ℝ => p.2 * Real.sqrt (V p.1 / ∫ ω, V ω ∂μ))
    (μ.prod (gaussianReal 0 1))

end AIM.P114
