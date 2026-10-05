import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Data.Nat.Prime.Infinite
import Mathlib.Analysis.Real.Sqrt
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

/-!
# The prescribed lengths and contamination measure in AIM 114

Source: Sidney Holden, revised proof v0.3, Section 5. Prime indexing in Lean
starts at zero: `primeRootLength 0 = sqrt 2`. These definitions model the
actual length fraction and a convex combination of probability laws. They
do not identify that combination with a quantum-graph spectral law.
-/

noncomputable section

open MeasureTheory

namespace AIM.P114

/-- The `(j+1)`st prime's square root, matching the source's one-based indexing. -/
def primeRootLength (j : ℕ) : ℝ := Real.sqrt (Nat.nth Nat.Prime j : ℝ)

/-- Total length of the `3*m` core edges. -/
def coreLength (m : ℕ) : ℝ := ∑ j ∈ Finset.range (3 * m), primeRootLength j

/-- The prescribed dominant pendant length. -/
def pendantLength (m : ℕ) : ℝ := (m : ℝ) ^ 6 * primeRootLength (3 * m)

/-- Fraction of total length on the core, defined also at `m=0` by real division. -/
def coreWeight (m : ℕ) : ℝ := coreLength m / (coreLength m + pendantLength m)

/-- The actual measure `(1-w) μ + w ν`, with real nonnegative weights.
All theorems using it explicitly restrict `w` to `[0,1]`. -/
def contaminatedLaw {Ω : Type*} [MeasurableSpace Ω]
    (w : ℝ) (μ ν : Measure Ω) : Measure Ω :=
  ENNReal.ofReal (1 - w) • μ + ENNReal.ofReal w • ν

/-- Even moment integrand centered at `(2m-1)/2` and scaled by `sqrt m`.
`k=1` and `k=2` are the source's second and fourth moments respectively. -/
def surplusEvenMoment (m k : ℕ) (s : ℝ) : ℝ :=
  ((s - (2 * (m : ℝ) - 1) / 2) / Real.sqrt (m : ℝ)) ^ (2 * k)

end AIM.P114
