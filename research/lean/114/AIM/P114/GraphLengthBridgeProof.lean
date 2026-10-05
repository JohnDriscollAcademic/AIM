import AIM.P114.LengthDefinitions
import AIM.P114.TransferProof

/-!
Exact sums of the actual graph edge lengths. The finite product indexing
counts all three edges in each module, including both parallel edges.
-/

noncomputable section

namespace AIM.P114

/-- Sum over all separately identified core edges, including parallel edges. -/
theorem actual_graph_core_length_sum (m : ℕ) :
    (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) =
      coreLength m := by
  calc
    (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) =
        ∑ j : Fin (m * 3), primeRootLength j.val := by
      apply Fintype.sum_equiv finProdFinEquiv
      intro e
      simp [counterexampleMetricLength, finProdFinEquiv, Nat.add_comm]
    _ = coreLength m := by
      rw [Fin.sum_univ_eq_sum_range]
      simp [coreLength, Nat.mul_comm]

/-- Sum over all actual graph edges, including the single pendant. -/
theorem actual_graph_total_length_sum (m : ℕ) :
    (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) =
      coreLength m + pendantLength m := by
  rw [Fintype.sum_option, actual_graph_core_length_sum]
  simp [counterexampleMetricLength, add_comm]

/-- The source weight bound, now expressed with actual graph edge-length sums. -/
theorem actual_graph_core_length_ratio_bound (m : ℕ) (hm : 3 ≤ m) :
    0 ≤ (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) /
      (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) ∧
    (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) /
      (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) ≤
        3 / ((m : ℝ) ^ 5 + 3) := by
  rw [actual_graph_core_length_sum, actual_graph_total_length_sum]
  exact core_weight_bound m (by omega)

end AIM.P114
