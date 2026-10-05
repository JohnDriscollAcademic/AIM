import Mathlib.Combinatorics.Graph.Simple
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Data.Set.Card
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Option
import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic

/-!
# The actual AIM 114 multigraph

Sidney Holden's v0.3 manuscript, Section 1, has vertices `u,v,w_i,t`,
two distinct edges from `u` to each `w_i`, one from `w_i` to `v`, and
one pendant from `u` to `t`. This module retains those distinct edge IDs.
It defines no metric lengths, differential operator, or spectral law.
-/

namespace AIM.P114

/-- Module vertices plus three distinguished vertices `u,v,t`, in that order. -/
abbrev CounterexampleVertex (m : ℕ) := Fin m ⊕ Fin 3

/-- Three separately identified edges per module, plus the pendant `none`.
Module labels `0,1` are the two parallel edges; label `2` reaches `v`. -/
abbrev CounterexampleEdge (m : ℕ) := Option (Fin m × Fin 3)

def graphU (m : ℕ) : CounterexampleVertex m := Sum.inr 0
def graphV (m : ℕ) : CounterexampleVertex m := Sum.inr 1
def graphT (m : ℕ) : CounterexampleVertex m := Sum.inr 2
def graphW {m : ℕ} (i : Fin m) : CounterexampleVertex m := Sum.inl i

/-- A chosen ordering of each edge's two endpoints; the graph forgets the
ordering, but does not identify distinct edges having the same endpoints. -/
def counterexampleEnds (m : ℕ) : CounterexampleEdge m →
    CounterexampleVertex m × CounterexampleVertex m
  | none => (graphU m, graphT m)
  | some (i, j) => if j = 2 then (graphW i, graphV m) else (graphU m, graphW i)

/-- The actual finite multigraph, with all elements of its ambient types
included as vertices and edges. Structural obligations only are proved here. -/
def counterexampleGraph (m : ℕ) : Graph (CounterexampleVertex m) (CounterexampleEdge m) where
  vertexSet := Set.univ
  edgeSet := Set.univ
  IsLink e x y :=
    (x = (counterexampleEnds m e).1 ∧ y = (counterexampleEnds m e).2) ∨
    (x = (counterexampleEnds m e).2 ∧ y = (counterexampleEnds m e).1)
  isLink_symm := by
    intro e _
    exact ⟨fun x y h => h.elim (fun h => Or.inr h.symm) (fun h => Or.inl h.symm)⟩
  eq_or_eq_of_isLink_of_isLink := by
    intro e x y v w h₁ h₂
    rcases h₁ with ⟨hx, hy⟩ | ⟨hx, hy⟩ <;>
      rcases h₂ with ⟨hv, hw⟩ | ⟨hv, hw⟩ <;> simp_all
  edge_mem_iff_exists_isLink := by
    intro e
    exact ⟨fun _ => ⟨(counterexampleEnds m e).1, (counterexampleEnds m e).2,
      Or.inl ⟨rfl, rfl⟩⟩, fun _ => Set.mem_univ _⟩
  left_mem_of_isLink := by intros; exact Set.mem_univ _

end AIM.P114
