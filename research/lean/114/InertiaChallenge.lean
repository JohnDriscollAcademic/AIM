import AIM.P114.InertiaDefinitions

/-! Candidate boundary for the finite-dimensional core inertia step.
The two deliberate placeholders must never be imported by Solution.
No advertised proof implementation before two independent boundary approvals. -/

noncomputable section

namespace AIM.P114

/-- Completing the actual core form by the explicit invertible shear. -/
theorem core_completion_of_squares (m : ℕ) (a q x : Fin m → ℝ)
    (ha : ∀ i, a i ≠ 0) :
    coreQuadraticForm m a q x =
      (coreDiagonalForm m a q x).comp (coreDiagonalizingEquiv m a q).toLinearMap := by
  sorry

/-- The actual positive index of the core form, including the possible zero
residual pivot. Mathlib's `sigPos` counts the maximal dimension of a subspace
on which the real quadratic form is positive definite. -/
theorem core_positive_index (m : ℕ) (a q x : Fin m → ℝ)
    (ha : ∀ i, a i ≠ 0) :
    sigPos (coreQuadraticForm m a q x) =
      (Finset.univ.filter (fun i => a i < 0)).card +
        if 0 < coreSchurValue m a q x then 1 else 0 := by
  sorry

end AIM.P114
