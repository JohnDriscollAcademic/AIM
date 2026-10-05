import AIM.P114.MixtureDefinitions
import Mathlib.Probability.Distributions.Cauchy
import Mathlib.MeasureTheory.Measure.OpenPos

/-! The actual deterministic variance function in Sidney Holden's
AIM 114 manuscript v0.3, Eq. (3). Three fresh independent standard Cauchy
coordinates define the triangle probability. The eventual ratio law is
an input to the application theorems, not constructed in this module. -/

noncomputable section

open MeasureTheory ProbabilityTheory

namespace AIM.P114

/-- The magnitude of the cosecant expressed through a Cauchy coordinate. -/
def cauchyMagnitude (x : ℝ) : ℝ := Real.sqrt (1 + x ^ 2)

/-- Three independent standard Cauchy variables, grouped as `(X₁,X₂),X₃`. -/
def cauchyTripleMeasure : Measure ((ℝ × ℝ) × ℝ) :=
  ((cauchyMeasure 0 1).prod (cauchyMeasure 0 1)).prod (cauchyMeasure 0 1)

/-- The strict triangle event in manuscript Eq. (3). -/
def varianceTriangleEvent (r : ℝ) : Set ((ℝ × ℝ) × ℝ) :=
  {p | |cauchyMagnitude p.1.1 - cauchyMagnitude p.1.2| <
      |r| * cauchyMagnitude p.2 ∧
    |r| * cauchyMagnitude p.2 < cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2}

/-- The manuscript's actual `v(r)`, extended at zero by the same event formula.
`Measure.real` is the real-valued mass of the displayed actual probability law. -/
def actualNodalVariance (r : ℝ) : ℝ :=
  1 / 2 - cauchyTripleMeasure.real (varianceTriangleEvent r) / 4

end AIM.P114
