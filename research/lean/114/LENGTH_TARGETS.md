# Joint rational independence of the actual prescribed edge lengths

## Frozen source and scope

Mathematical source: Sidney Holden, *A non-Gaussian limit for nodal surplus*,
v0.3, 2026-10-02, Section 1, equation (1) and its following paragraph. The
submitted PDF SHA256 is
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6.
The canonical AIM problem 114 and its original mathematical target are
unchanged. This is a supporting metric-admissibility block, not the complete
spectral counterexample.

The source numbers the core edges module by module. It assigns the first
3m prime square roots to them and assigns m^6 times the next prime square
root to the pendant. Rational independence means every finite rational
linear relation among the actual lengths has all coefficients zero.
Individual irrationality and pairwise irrational ratios do not by themselves
establish this conclusion; the first target is full joint independence.

## Exact definitions and three statements

`AIM/P114/LengthDefinitions.lean` imports the existing graph and transfer
definitions unchanged. The actual graph edge type is
`CounterexampleEdge m = Option (Fin m × Fin 3)`. Its `none` edge is the
pendant; `some (i,j)` identifies each core edge separately, including the two
parallel edges. Define:

- `counterexampleMetricLength m none = pendantLength m`;
- `counterexampleMetricLength m (some (i,j)) = primeRootLength (3*i.val+j.val)`.

The imported definitions are exactly
`primeRootLength n = Real.sqrt (Nat.nth Nat.Prime n : ℝ)` and
`pendantLength m = (m : ℝ)^6 * primeRootLength (3*m)`.
There is no abstract length parameter or independence assumption.

The precise signatures in `LengthChallenge.lean` are:

1. `prime_root_lengths_linearIndependent`:
   `LinearIndependent ℚ primeRootLength`. The entire natural-number-indexed
   sequence is independent, and therefore every finite subfamily is too.
2. `counterexample_metric_lengths_positive`: for every natural m with m≥3,
   every actual graph edge has strictly positive length.
3. `counterexample_metric_lengths_linearIndependent`: for every natural m
   with m≥3, `LinearIndependent ℚ (counterexampleMetricLength m)`.

The m≥3 restriction matches the source family; it also makes the pendant's
rational multiplier m^6 nonzero. No target assumes joint independence,
independent sign-changing automorphisms, a multiquadratic degree formula,
or a spectral-frequency law. No finite numerical sampling substitutes for
the universal quantifiers.

## Proposed proof and inspected pinned-library dependencies

Pinned Mathlib commit: 0df444a360eaa60ab8c11dca51a86af692955474.
No direct theorem for the linear independence of distinct prime square roots
was found. The following existing general results provide a coherent route
without a new multiquadratic degree calculation:

- `FieldTheory/AlgebraicClosure.lean`: the relative algebraic closure
  `algebraicClosure ℚ ℂ` and its `IsAlgClosure` instance.
- `Analysis/Complex/Polynomial/Basic.lean`: the algebraic closedness of ℂ.
- `FieldTheory/IsAlgClosed/Basic.lean`: normality and separability of an
  algebraic closure in characteristic zero.
- `FieldTheory/Galois/Infinite.lean`:
  `InfiniteGalois.mem_range_algebraMap_iff_fixed`, identifying the rational
  elements as those fixed by every rational automorphism of this closure.
- `LinearAlgebra/LinearIndependent/Basic.lean`:
  `linearIndependent_monoidHom`, Dedekind's independence of characters,
  together with restriction of an independent family and nonzero rational
  rescaling via `LinearIndependent.units_smul`.
- `NumberTheory/Real/Irrational.lean`, `Data/Rat/Lemmas.lean`, and
  `Data/Nat/Squarefree.lean`: irrational square roots, the equivalence
  between rational and natural squarehood of natural numbers, and
  squarefreeness of products of coprime primes.
- `Data/Nat/Nth.lean` and `Data/Nat/Prime/Infinite.lean`: membership and
  injectivity of the sequence of successive primes.

Place the actual real root sqrt(p), viewed in ℂ, into the relative algebraic
closure using its equation x²=p. For each such nonzero root a, define the
character χ_a(σ)=σ(a)/a on the rational automorphism group. Its values are
±1 because σ preserves a²=p. Consequently these values are fixed by all
automorphisms, which proves that χ_a is multiplicative.

Characters belonging to distinct primes are distinct. Otherwise a/b would
be fixed by all automorphisms, hence rational. Then a*b=(a/b)*q would be
rational and its square would be p*q. But the product of two distinct primes
is squarefree and greater than one, so it is not a rational square. This
contradiction establishes character injectivity without assuming the
existence of an automorphism that flips one prescribed root alone.

Given an actual rational relation among the roots, apply every automorphism
to it. This gives a relation among these distinct characters with
coefficients c_a*a. Dedekind's theorem sets every coefficient to zero;
each root is nonzero, so every rational c_a is zero. Transport the resulting
independence from the algebraic closure back to the actual real roots.

Finally, core edge labels map injectively to indices 3*i+j below 3*m, and
the pendant maps to 3*m. Restrict the sequence to these distinct indices.
Multiply the pendant's entry by the nonzero rational m^6 and leave other
entries unchanged. This gives the exact graph edge family. Positivity
follows from positivity of primes, real square roots, and m^6.

## Implementation risks and remaining obligations

This route uses existing deep field-theoretic results; the main work is
constructing the sign characters, transporting actual roots through subtype
coercions, and moving rational relations between ℝ, ℂ and the relative
algebraic closure. Those are genuine proof obligations and have not been
implemented at boundary proposal time. The distinct-square-class step must
use arithmetic, not assume pairwise character distinction. The graph edge
index injectivity and exact rational pendant rescaling must also be proved.

The result establishes positive, jointly rationally independent lengths for
the actual finite multigraph. It does not define the Kirchhoff Laplacian,
enumerate eigenvalues, establish generic-index frequencies, identify the
spectral surplus law with the module model, prove the stable response law,
or prove the empirical-process/random-index limit. Those remain separate
parts of the end-to-end task.

Two independent statement reviews and successful boundary typechecking must
precede proof implementation. Typechecking placeholder declarations certifies
only well-formed signatures, not these results.
