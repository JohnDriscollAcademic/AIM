import AIM.P114.GraphDefinitions

/-! Candidate boundary for actual multigraph admissibility. The deliberate
placeholders are not certificates and must not be imported into Solution.
No advertised proof implementation before two independent approvals. -/

namespace AIM.P114

/-- The actual construction has no loops at any index. -/
theorem counterexample_loopless (m : ℕ) : (counterexampleGraph m).Loopless := by
  sorry

/-- For positive module count the actual graph is connected. Only adjacency
and connectivity use the underlying simple graph; all edge counts retain IDs. -/
theorem counterexample_connected (m : ℕ) (hm : 1 ≤ m) :
    (counterexampleGraph m).toSimpleGraph.Connected := by
  sorry

/-- Cardinalities of the actual multigraph's vertex and edge sets. -/
theorem counterexample_cardinalities (m : ℕ) :
    (counterexampleGraph m).vertexSet.ncard = m + 3 ∧
    (counterexampleGraph m).edgeSet.ncard = 3 * m + 1 := by
  sorry

/-- The two parallel edges in every module remain distinct actual links. -/
theorem counterexample_parallel_edges (m : ℕ) (i : Fin m) :
    (some (i, (0 : Fin 3)) : CounterexampleEdge m) ≠ some (i, (1 : Fin 3)) ∧
    (counterexampleGraph m).IsLink (some (i, 0)) (graphU m) (graphW i) ∧
    (counterexampleGraph m).IsLink (some (i, 1)) (graphU m) (graphW i) := by
  sorry

/-- Exact incident-edge counts, hence multigraph degrees once looplessness
is established. Parallel edges are counted separately. -/
theorem counterexample_degrees (m : ℕ) :
    ((counterexampleGraph m).incidenceSet (graphU m)).ncard = 2 * m + 1 ∧
    ((counterexampleGraph m).incidenceSet (graphV m)).ncard = m ∧
    ((counterexampleGraph m).incidenceSet (graphT m)).ncard = 1 ∧
    ∀ i : Fin m, ((counterexampleGraph m).incidenceSet (graphW i)).ncard = 3 := by
  sorry

/-- In the manuscript's graph range no vertex has degree two. -/
theorem counterexample_no_degree_two (m : ℕ) (hm : 3 ≤ m) :
    ∀ v : CounterexampleVertex m,
      ((counterexampleGraph m).incidenceSet v).ncard ≠ 2 := by
  sorry

/-- The integer Euler expression for the actual multigraph. This theorem
does not identify it with a homology or cycle-space dimension. -/
theorem counterexample_euler_count (m : ℕ) :
    ((counterexampleGraph m).edgeSet.ncard : ℤ) -
      ((counterexampleGraph m).vertexSet.ncard : ℤ) + 1 = 2 * (m : ℤ) - 1 := by
  sorry

end AIM.P114
