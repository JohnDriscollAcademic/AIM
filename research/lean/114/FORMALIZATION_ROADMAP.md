# AIM 114: independent dependency assessment and next formalization steps

Date: 2026-10-05. Assessor: Codex AI `spectral_review`, independent of implementation. This is a read-only library/source assessment: no mathematical proof implementation or execution claim is made here. The pinned Mathlib revision is `0df444a360eaa60ab8c11dca51a86af692955474` (Lean 4.33.1).

All source links below refer to that immutable Mathlib revision. Line numbers were checked in its local cached checkout. A failed text search is evidence about what was located, not a theorem that an API cannot exist under another name.

## Immediate substantive next blocks

1. **Actual Gaussian mixture and non-Gaussianity.** Define a product probability space with an actual standard Gaussian factor and a bounded positive nonconstant mixing variable; prove the law's mean/second/fourth moments and distinguish its law from standard Gaussian after normalization. This closes the gap between the existing scalar kurtosis inequality and an actual probability distribution. It still leaves construction of the particular `v(R)` and convergence from graph surplus open. Mathlib has [Gaussian distributions and characteristic functions](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/Distributions/Gaussian/Real.lean#L486), actual [Gaussian moments/integrability](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/Distributions/Gaussian/Real.lean#L540), product measures, and Bochner integration. Review the actual proposed boundary rather than assuming these facts are all packaged in the desired form.

2. **Prescribed lengths and actual measure/moment transfer.** Formalize positive prime-root lengths, the core fraction bound, the convex mixture of two actual probability measures, and bounds for the actual standardized second/fourth integrals. This proves the manuscript's last transfer step conditional on the explicit spectral measure-mixture equality; it is materially stronger than a scalar inequality about unspecified errors. Sources: [Nat.nth_strictMono and nth_mem_of_infinite](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Data/Nat/Nth.lean#L144); [Euclid's theorem](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Data/Nat/Prime/Infinite.lean#L33); [Real.sqrt monotonicity](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/Real/Sqrt.lean#L209), [positivity](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/Real/Sqrt.lean#L286); [integral_add_measure](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean#L974), [integral_smul_measure](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean#L1014), and [integral_mono_ae](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean#L627). Do not claim rational independence from individual irrationality.

## Concrete graph and inertia blocks

### Graph family and admissibility

Mathlib has a genuine multigraph structure, [Graph alpha beta](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/Graph/Basic.lean#L92), expressly allowing loops and parallel edges. Its incidence relation and [incidenceSet](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/Graph/Basic.lean#L402) preserve the two distinct edges between `u` and each `w_i`. This avoids incorrectly representing the construction as a simple graph.

A practical definition uses vertex type `Fin m` plus three distinguished vertices and edge type `(Fin m × Fin 3)` plus one pendant edge. Define endpoints explicitly. Prove looplessness, finite cardinalities `m+3` and `3m+1`, and incidence cardinalities `2m+1,m,3,1`. These are elementary finite equivalence/counting proofs. For connectedness use [Graph.toSimpleGraph](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/Graph/Simple.lean#L100) only for connectivity, not degree or edge counts: every module vertex and the pendant endpoint connects to `u`; `v` connects through a fixed module vertex. For `m>=3`, every degree avoids two.

The number `E-V+1=2m-1` can immediately be proved as the Euler cycle-rank expression. An eventual claim identifying it with first homology rank needs that bridge or an explicit spanning-tree/cycle-basis proof; it must not be assumed through a name alone. The Graph directory currently has basic, simple, lattice, subgraph, maps, and deletion modules; I did not locate a packaged multigraph metric-Kirchhoff construction or cycle-space spectral theorem there.

### Finite inertia reduction

This is feasible using existing nontrivial linear algebra. Mathlib provides:

- [QuadraticForm.sigPos and sigNeg](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/QuadraticForm/Signature.lean#L59), defined by dimensions of definite subspaces.
- [Equivalent.sigPos_eq](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/QuadraticForm/Signature.lean#L121), and the corresponding negative-signature invariant.
- [sigPos_weightedSumSquares](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/QuadraticForm/Signature.lean#L189), which counts positive diagonal weights.
- [Matrix.fromBlocks_eq_of_invertible11](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Matrix/SchurComplement.lean#L48), the exact block LDU factorization, plus invertibility and determinant results.

The shortest route for this graph is an explicit congruence, without first developing a fully general inertia additivity theorem. For nonzero `a_i`, the actual core principal quadratic form is

    Q(r,z) = -sum a_i*z_i^2 + 2*r*sum q_i*z_i - (sum x_i3)*r^2.

Complete squares to obtain

    Q(r,z) = sum (-a_i)*(z_i-(q_i/a_i)*r)^2 + T*r^2,
    T = sum (-x_i3+q_i^2/a_i).

The triangular map `(r,z) -> (r,z-(q/a)r)` has an explicit inverse. Package it as a linear equivalence/isometry between actual quadratic forms, then derive `sigPos(Q)=count(a_i<0)+1{T>0}` from the weighted-square theorem. Add the pendant coordinate to get the remaining pivot. Combine this with the existing local sign-count theorem for the finite surplus-oracle identity.

A further finite step proves the full assembled matrix has a one-dimensional kernel when the principal minor is invertible and the supplied vector lies in its kernel; then proves the two pendant completions and their coincident finite surplus values. These are genuine matrix/trigonometric results. They still do not identify a spectral nodal count with the finite oracle: that is a separate analytical bridge.

## Rational independence of the prescribed radicals

The source's prime-root argument needs **joint** linear independence over the rationals. [Nat.Prime.irrational_sqrt](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/Real/Irrational.lean#L141) proves only single-root irrationality. Full-tree searches for `multiquadratic`, square-root linear-independence descriptions, and corresponding `LinearIndependent`/`sqrt` combinations did not locate the needed joint theorem.

There is infrastructure for adjoining roots and [AdjoinRoot power bases](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/RingTheory/AdjoinRoot.lean#L688), Galois/normal extensions, and prime factorization. A direct route is to prove that products of distinct primes represent independent square classes, construct the finite multiquadratic extension with degree `2^n`, and its individual sign automorphisms, then isolate coefficients. This is a separate algebra project, not a missing axiom to add to the final theorem.

For the full existential counterexample target, an explicitly documented alternative is to select rationally independent positive lengths in intervals with pendant dominance. [Countability of a rational span of a finite family](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Countable.lean#L25) and uncountability of nonempty real intervals permit induction avoiding the previous span. This would prove existence of a valid family with the same probabilistic argument, but would **not** certify the manuscript's explicit prime-root family. Such a changed construction needs an explicit new reviewed boundary and should not silently replace that family.

## Spectral-to-phase analytical dependencies

A full-tree source search for `Kirchhoff`, `quantum graph`, `metric graph`, `nodal surplus`, `secular`, and `Dirichlet-to-Neumann` found no matching packaged theory. The ordinary [SimpleGraph Laplacian](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/SimpleGraph/LapMatrix.lean) is a discrete operator and cannot stand in for the metric differential operator.

There is useful analytical infrastructure: [spectral theory for bounded self-adjoint operators, including compact operators](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/InnerProductSpace/Spectrum.lean#L17), ODE existence/uniqueness, derivatives and interval integration, and [Sobolev/Bessel potential spaces on normed vector spaces](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/Distribution/Sobolev.lean#L11). These do not directly supply finite-interval vertex traces, the Kirchhoff form domain, a compact graph resolvent, or the ordered eigenvalue counting formula.

An actionable analytical sequence is:

1. Define edgewise sine/cosine solutions and outgoing derivatives; prove interpolation, zero counts, and the vertex-matrix boundary equation at nonzero edge sines.
2. Define the compact metric-graph operator or its closed quadratic form; establish self-adjointness/compact resolvent and ordered spectrum.
3. Prove the form decomposition into Dirichlet edge functions and Helmholtz extensions, its index count, and the nodal-surplus oracle equality.
4. Formalize the secular torus, generic subset, and phase measure; prove the published length-mixture and uniform projection theorems, or an explicit equivalent proof specialized to these graphs.
5. Relate generic spectral frequencies for rationally independent lengths to this phase law. A citation is acceptable in the mathematical report but cannot discharge a Lean theorem hypothesis in the complete counterexample.

The finite steps above reduce the amount of new spectral material needed, but do not remove these bridges.

## Probability/process dependencies beyond the new mixture block

Mathlib already has [cauchyMeasure and its probability instance](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/Distributions/Cauchy.lean#L170), [the scalar i.i.d. CLT](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/CentralLimitTheorem.lean#L79), [characteristic-function Taylor tools](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/MeasureTheory/Measure/CharacteristicFunction/TaylorExpansion.lean), tightness/Prokhorov results, and [Levy convergence when the limiting probability law is supplied](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/MeasureTheory/Measure/LevyConvergence.lean#L200).

The Cauchy source file ends with the probability instance; it does not itself prove the tangent pushforward, Cauchy characteristic function, or fractional moment estimates needed here. The checked Levy API assumes a supplied limiting probability measure; existence of the stable vector from a continuous limiting characteristic function needs a further argument. Searches for Donsker, empirical process, Brownian bridge, and Skorokhod in Probability/MeasureTheory found no packaged functional empirical-process CLT.

Recommended next probability blocks: establish the uniform-phase Cauchy transformation and sign independence; prove the actual response representation and `E W^2=2`; develop characteristic-function asymptotics and the stable law; prove positivity/continuity/nonconstancy of the actual `v` and full support of the ratio; then join the module process and stable vector.

It may be more economical to prove the random evaluation limit directly using finite grids, joint finite-dimensional convergence, and uniform increment bounds than to formalize the full Skorokhod empirical-process theorem. That is a proposed proof strategy, not an already available library theorem. The finite-grid route still must prove stochastic equicontinuity, tightness/localization of the ratio, and uniform integrability. It cannot assume independence of the finite-sample response and surplus process.

## Recommended order and review boundaries

Proceed with the actual mixture and transfer packages now, retaining the original three proofs unchanged. Next do graph admissibility and the explicit quadratic-form congruence/inertia package; both have direct existing API support. Develop Cauchy/phase distribution lemmas and rational independence as separate substantial blocks. Formalize the spectral-frequency-to-phase theorem and random evaluation convergence only after their component infrastructure is explicit.

Each new package should freeze actual definitions and complete signatures, receive two independent boundary reviews, and type-check before implementation. Report exactly which bridges it closes. The known lack of a ready-made quantum-graph or Donsker module is a roadmap for new work, not an impossibility result or a reason to stop at the original three lemmas.
