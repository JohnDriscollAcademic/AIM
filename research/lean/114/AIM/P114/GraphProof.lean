import AIM.P114.GraphDefinitions

/-! The finite multigraph conditions in Sidney Holden's v0.3 manuscript,
Section 1. Edge counts and incident-edge degrees retain parallel edges. -/

namespace AIM.P114

/-- The actual construction has no loops at any index. -/
theorem counterexample_loopless (m : ℕ) : (counterexampleGraph m).Loopless := by
  constructor
  intro e v
  cases e with
  | none =>
    simp [Graph.IsLoopAt, counterexampleGraph, counterexampleEnds, graphU, graphT]
    aesop
  | some e =>
    rcases e with ⟨i, j⟩
    fin_cases j <;>
      simp [Graph.IsLoopAt, counterexampleGraph, counterexampleEnds, graphU, graphV, graphW]
        <;> aesop

private def actualVertex (m : ℕ) (v : CounterexampleVertex m) :
    (counterexampleGraph m).vertexSet := ⟨v, Set.mem_univ _⟩

private lemma simple_adj_of_link (m : ℕ) (e : CounterexampleEdge m)
    (u v : CounterexampleVertex m) (h : (counterexampleGraph m).IsLink e u v) :
    (counterexampleGraph m).toSimpleGraph.Adj (actualVertex m u) (actualVertex m v) := by
  let := counterexample_loopless m
  exact (Graph.toSimpleGraph_adj_iff _ _).2 ⟨e, h⟩

/-- For positive module count the actual graph is connected. -/
theorem counterexample_connected (m : ℕ) (hm : 1 ≤ m) :
    (counterexampleGraph m).toSimpleGraph.Connected := by
  apply (SimpleGraph.connected_iff_exists_forall_reachable _).2
  refine ⟨actualVertex m (graphU m), ?_⟩
  have huw (i : Fin m) : (counterexampleGraph m).toSimpleGraph.Reachable
      (actualVertex m (graphU m)) (actualVertex m (graphW i)) := by
    apply SimpleGraph.Adj.reachable
    apply simple_adj_of_link m (some (i, 0))
    simp [counterexampleGraph, counterexampleEnds]
  have hwv (i : Fin m) : (counterexampleGraph m).toSimpleGraph.Reachable
      (actualVertex m (graphW i)) (actualVertex m (graphV m)) := by
    apply SimpleGraph.Adj.reachable
    apply simple_adj_of_link m (some (i, 2))
    simp [counterexampleGraph, counterexampleEnds]
  rintro ⟨v, hv⟩
  cases v with
  | inl i => exact huw i
  | inr j =>
    fin_cases j
    · exact SimpleGraph.Reachable.rfl
    · exact (huw ⟨0, by omega⟩).trans (hwv ⟨0, by omega⟩)
    · apply SimpleGraph.Adj.reachable
      apply simple_adj_of_link m none
      simp [counterexampleGraph, counterexampleEnds, graphT]

/-- Cardinalities of the actual multigraph's vertex and edge sets. -/
theorem counterexample_cardinalities (m : ℕ) :
    (counterexampleGraph m).vertexSet.ncard = m + 3 ∧
    (counterexampleGraph m).edgeSet.ncard = 3 * m + 1 := by
  simp [counterexampleGraph, CounterexampleVertex, CounterexampleEdge,
    Nat.card_eq_fintype_card, Nat.mul_comm]

/-- The two parallel edges in every module remain distinct actual links. -/
theorem counterexample_parallel_edges (m : ℕ) (i : Fin m) :
    (some (i, (0 : Fin 3)) : CounterexampleEdge m) ≠ some (i, (1 : Fin 3)) ∧
    (counterexampleGraph m).IsLink (some (i, 0)) (graphU m) (graphW i) ∧
    (counterexampleGraph m).IsLink (some (i, 1)) (graphU m) (graphW i) := by
  simp [counterexampleGraph, counterexampleEnds]

private lemma incident_count_sum (m : ℕ) (v : CounterexampleVertex m) :
    ((counterexampleGraph m).incidenceSet v).ncard =
      ∑ e : CounterexampleEdge m,
        if v = (counterexampleEnds m e).1 ∨ v = (counterexampleEnds m e).2 then 1 else 0 := by
  classical
  have hset : (counterexampleGraph m).incidenceSet v =
      {e | v = (counterexampleEnds m e).1 ∨ v = (counterexampleEnds m e).2} := by
    ext e
    simp [Graph.incidenceSet, Graph.Inc, counterexampleGraph, exists_or]
  rw [hset, Set.ncard_eq_toFinset_card', Set.toFinset_ofPred,
    Finset.card_eq_sum_ones, Finset.sum_filter]

/-- Exact incident-edge counts, hence multigraph degrees for this loopless graph. -/
theorem counterexample_degrees (m : ℕ) :
    ((counterexampleGraph m).incidenceSet (graphU m)).ncard = 2 * m + 1 ∧
    ((counterexampleGraph m).incidenceSet (graphV m)).ncard = m ∧
    ((counterexampleGraph m).incidenceSet (graphT m)).ncard = 1 ∧
    ∀ i : Fin m, ((counterexampleGraph m).incidenceSet (graphW i)).ncard = 3 := by
  classical
  simp only [incident_count_sum, Fintype.sum_option, Fintype.sum_prod_type]
  norm_num [counterexampleEnds, graphU, graphV, graphT, graphW, Fin.sum_univ_three]
  simp [Nat.mul_comm, Nat.add_comm, Finset.sum_add_distrib]

/-- In the manuscript's graph range no vertex has degree two. -/
theorem counterexample_no_degree_two (m : ℕ) (hm : 3 ≤ m) :
    ∀ v : CounterexampleVertex m,
      ((counterexampleGraph m).incidenceSet v).ncard ≠ 2 := by
  intro v
  obtain ⟨hu, hv, ht, hw⟩ := counterexample_degrees m
  cases v with
  | inl i =>
    change ((counterexampleGraph m).incidenceSet (graphW i)).ncard ≠ 2
    rw [hw]
    decide
  | inr j =>
    fin_cases j
    · change ((counterexampleGraph m).incidenceSet (graphU m)).ncard ≠ 2
      rw [hu]
      omega
    · change ((counterexampleGraph m).incidenceSet (graphV m)).ncard ≠ 2
      rw [hv]
      omega
    · change ((counterexampleGraph m).incidenceSet (graphT m)).ncard ≠ 2
      rw [ht]
      decide

/-- The integer Euler expression for the actual multigraph. -/
theorem counterexample_euler_count (m : ℕ) :
    ((counterexampleGraph m).edgeSet.ncard : ℤ) -
      ((counterexampleGraph m).vertexSet.ncard : ℤ) + 1 = 2 * (m : ℤ) - 1 := by
  obtain ⟨hV, hE⟩ := counterexample_cardinalities m
  rw [hV, hE]
  push_cast
  ring

end AIM.P114
