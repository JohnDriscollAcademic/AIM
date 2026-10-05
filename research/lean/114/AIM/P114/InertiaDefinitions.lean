import Mathlib.LinearAlgebra.QuadraticForm.Signature
import Mathlib.LinearAlgebra.Pi
import Mathlib.LinearAlgebra.Prod
import Mathlib.Data.Real.Basic

/-!
# The actual core quadratic form in AIM 114

Source: Sidney Holden, revised proof v0.3, Lemma 1. The scalar coordinate
is the value at `v`, and the `Fin m` coordinates are values at the module
vertices `w_i`, after removing vertex `u`. The pendant coordinate is omitted.
These are concrete quadratic forms and an explicit linear equivalence, not
an axiomatized inertia operation or a definition of a nodal-surplus law.
-/

noncomputable section

namespace AIM.P114

/-- The residual scalar pivot after eliminating the module coordinates.
In the manuscript `x i = cot(theta_(i,3))`, `q i = csc(theta_(i,3))`,
and `a i` is the sum of the three cotangents in module `i`. -/
def coreSchurValue (m : ℕ) (a q x : Fin m → ℝ) : ℝ :=
  ∑ i, (-x i + (q i) ^ 2 / a i)

/-- The actual form
`Q(r,z) = -sum_i a_i*z_i^2 + 2*r*sum_i q_i*z_i - (sum_i x_i)*r^2`.
It is assembled directly from linear coordinate maps and their products. -/
def coreQuadraticForm (m : ℕ) (a q x : Fin m → ℝ) :
    QuadraticForm ℝ (ℝ × (Fin m → ℝ)) :=
  let R : (ℝ × (Fin m → ℝ)) →ₗ[ℝ] ℝ := LinearMap.fst ℝ ℝ (Fin m → ℝ)
  let Z : (ℝ × (Fin m → ℝ)) →ₗ[ℝ] (Fin m → ℝ) :=
    LinearMap.snd ℝ ℝ (Fin m → ℝ)
  (-(QuadraticMap.weightedSumSquares ℝ a).comp Z) +
    (2 : ℝ) • QuadraticMap.linMulLin R ((∑ i, q i • LinearMap.proj i).comp Z) -
    (∑ i, x i) • QuadraticMap.linMulLin R R

/-- The candidate diagonal weights: `T` in the scalar coordinate and `-a_i`
in each module coordinate. A zero scalar pivot is permitted. -/
def coreDiagonalWeights (m : ℕ) (a q x : Fin m → ℝ) : Option (Fin m) → ℝ :=
  fun j => Option.elim j (coreSchurValue m a q x) (fun i => -a i)

/-- The concrete weighted sum of squares with the proposed diagonal pivots. -/
def coreDiagonalForm (m : ℕ) (a q x : Fin m → ℝ) :
    QuadraticForm ℝ (Option (Fin m) → ℝ) :=
  QuadraticMap.weightedSumSquares ℝ (coreDiagonalWeights m a q x)

/-- The explicit invertible change of coordinates
`(r,z) -> (none => r, some i => z_i - r*q_i/a_i)`.
It is a shear followed by a coordinate reindexing. Its inverse sends
`y` to `(y none, fun i => y (some i) + y none*q_i/a_i)`.
Invertibility itself does not require nonzero `a_i`; the completion theorem
does require it because real division is total. -/
def coreDiagonalizingEquiv (m : ℕ) (a q : Fin m → ℝ) :
    (ℝ × (Fin m → ℝ)) ≃ₗ[ℝ] (Option (Fin m) → ℝ) :=
  ((LinearEquiv.refl ℝ ℝ).skewProd (LinearEquiv.refl ℝ (Fin m → ℝ))
    (LinearMap.toSpanSingleton ℝ (Fin m → ℝ) (fun i => -(q i / a i)))).trans
    (LinearEquiv.piOptionEquivProd ℝ (ι := Fin m) (M := fun _ => ℝ)).symm

end AIM.P114
