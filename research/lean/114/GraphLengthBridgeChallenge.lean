import AIM.P114.LengthDefinitions

/-! Isolated candidate boundary connecting the actual graph's edge-length
sums to the already defined core length and weight. Placeholders prove nothing. -/

noncomputable section

namespace AIM.P114

/-- Sum over all separately identified core edges, including parallel edges. -/
theorem actual_graph_core_length_sum (m : ℕ) :
    (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) =
      coreLength m := by sorry

/-- Sum over all actual graph edges, including the single pendant. -/
theorem actual_graph_total_length_sum (m : ℕ) :
    (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) =
      coreLength m + pendantLength m := by sorry

/-- The manuscript's weight bound for the ratio of actual graph edge-length sums. -/
theorem actual_graph_core_length_ratio_bound (m : ℕ) (hm : 3 ≤ m) :
    0 ≤ (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) /
      (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) ∧
    (∑ e : Fin m × Fin 3, counterexampleMetricLength m (some e)) /
      (∑ e : CounterexampleEdge m, counterexampleMetricLength m e) ≤
        3 / ((m : ℝ) ^ 5 + 3) := by sorry

end AIM.P114
