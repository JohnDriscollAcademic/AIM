import AIM.P114.InertiaDefinitions
import Mathlib.Tactic

/-! Exact finite core diagonalization and positive index in Sidney Holden's
v0.3 manuscript, Lemma 1. The spectral interpretation remains separate. -/

noncomputable section

namespace AIM.P114

/-- Completing the actual core form by the explicit invertible shear. -/
theorem core_completion_of_squares (m : ℕ) (a q x : Fin m → ℝ)
    (ha : ∀ i, a i ≠ 0) :
    coreQuadraticForm m a q x =
      (coreDiagonalForm m a q x).comp (coreDiagonalizingEquiv m a q).toLinearMap := by
  ext w
  rcases w with ⟨r, z⟩
  simp [coreQuadraticForm, coreDiagonalForm, coreDiagonalWeights,
    coreDiagonalizingEquiv, LinearEquiv.piOptionEquivProd, Equiv.piOptionEquivProd,
    Fintype.sum_option]
  simp only [coreSchurValue, Finset.sum_mul, Finset.mul_sum,
    ← Finset.sum_neg_distrib, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  field_simp [ha i]
  ring

/-- The actual positive index of the core form, including a zero residual pivot. -/
theorem core_positive_index (m : ℕ) (a q x : Fin m → ℝ)
    (ha : ∀ i, a i ≠ 0) :
    sigPos (coreQuadraticForm m a q x) =
      (Finset.univ.filter (fun i => a i < 0)).card +
        if 0 < coreSchurValue m a q x then 1 else 0 := by
  have hequiv : QuadraticMap.Equivalent (coreQuadraticForm m a q x)
      (coreDiagonalForm m a q x) := by
    refine ⟨{ coreDiagonalizingEquiv m a q with map_app' := ?_ }⟩
    intro w
    exact (congrArg (fun Q : QuadraticForm ℝ (ℝ × (Fin m → ℝ)) => Q w)
      (core_completion_of_squares m a q x ha)).symm
  rw [QuadraticForm.sigPos_of_equiv_weightedSumSquares hequiv]
  rw [Set.ncard_eq_toFinset_card', Set.toFinset_ofPred]
  simp_rw [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Fintype.sum_option]
  simp [coreDiagonalWeights, add_comm]
  rfl

end AIM.P114
