import AIM.P114.LengthDefinitions

/-! Isolated proposed boundary for joint rational independence of the
actual prescribed lengths. Deliberate placeholders prove nothing. -/

noncomputable section

namespace AIM.P114

/-- All square roots of successive primes are jointly independent over
the rationals. This asserts independence of every finite relation in the
entire sequence, not just individual irrationality or pairwise independence. -/
theorem prime_root_lengths_linearIndependent :
    LinearIndependent ℚ primeRootLength := by sorry

/-- Every actual graph edge has positive prescribed length in the source range. -/
theorem counterexample_metric_lengths_positive (m : ℕ) (hm : 3 ≤ m) :
    ∀ e : CounterexampleEdge m, 0 < counterexampleMetricLength m e := by sorry

/-- Joint rational independence of all `3*m+1` actual graph edge lengths,
including the prescribed rational scaling on the pendant edge. -/
theorem counterexample_metric_lengths_linearIndependent (m : ℕ) (hm : 3 ≤ m) :
    LinearIndependent ℚ (counterexampleMetricLength m) := by sorry

end AIM.P114
