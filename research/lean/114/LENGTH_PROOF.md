# Proof of admissibility of the actual prime-root lengths

`AIM/P114/LengthProof.lean` proves the three exact statements reviewed in
`LengthChallenge.lean`. Definitions, statement signatures and `LENGTH_TARGETS.md`
remain unchanged from the two approved preproof reviews. The proof file does
not import any Challenge file or use a placeholder, custom axiom, or an
assumed family of sign-changing automorphisms.

The construction attaches lengths to the same distinct edge IDs used by
the actual multigraph. The first theorem proves the stronger fact that the
entire sequence of square roots of successive primes is linearly independent
over ℚ, meaning every finite rational relation is trivial. The final theorem
then specializes this to the actual graph edges, including the pendant's
prescribed factor m^6. Positivity is also established for every edge when m≥3.

## Actual roots and Galois characters

Each positive real root is first included in ℂ and then into
`algebraicClosure ℚ ℂ`. Membership is proved from its actual equation
x²=p and `IsIntegral.of_pow`. The code does not choose an unrelated
algebraic root or assume that the actual real root matches one. Mathlib's
fundamental theorem of algebra and the relative-closure instance provide
an algebraic closure of ℚ, which is normal and separable. These are the
inputs to the infinite Galois fixed-field theorem.

Every rational automorphism σ preserves x²=p, so σ(x)=x or σ(x)=-x.
Consequently χ_x(σ)=σ(x)/x is a multiplicative character. The proof constructs
this monoid homomorphism explicitly; multiplicativity is checked using the
two sign alternatives for the second automorphism. Positivity of the actual
root guarantees all divisions are by a nonzero element.

The characters are distinct for distinct prime indices. If χ_x=χ_y, direct
division algebra shows every automorphism fixes x/y. The fixed-field theorem
then supplies an actual rational a with x/y=a. It follows that x*y=a*q and
that the rational square (a*q)² equals p*q. The code separately proves that
the product of two distinct primes cannot be a rational square, using
natural-number squarefreeness and `Rat.isSquare_natCast_iff`. Distinctness of
the primes follows from injectivity of the nth-prime sequence.

Given any finite rational relation ∑ c_j*x_j=0, apply every automorphism to
it to obtain a relation among these characters, with coefficients c_j*x_j
in the algebraic closure. Mathlib's `linearIndependent_monoidHom` makes every
coefficient zero. Since each root is nonzero, every c_j is zero. An explicit
coercion of the original real relation transports the result back to the
actual real sequence `primeRootLength`.

## Binding the result to the multigraph

The proof defines a private prime-index map on actual edge IDs:
the pendant maps to 3*m, and a core edge `(i,j)` maps to 3*i+j. It proves
injectivity using the bounds i<m and j<3; hence no core edge can use the
pendant's prime, and distinct core edges have distinct prime indices.
Restricting the already independent prime-root sequence gives independence
on these edge IDs. The pendant entry is multiplied by the nonzero rational
unit m^6; every core entry is multiplied by one. `LinearIndependent.units_smul`
preserves independence, and the final simplification checks that this scaled
family is definitionally the displayed `counterexampleMetricLength` family.

## Verification and scope

Local evidence is retained in `verification/length-build.log`,
`verification/length-reelaboration.log`, and `verification/length-axioms.log`;
the axiom-audit source and source SHA256 JSON are retained beside them.
The final two independent proof reviews are a separate gate, as is the
repository's isolated Linux verification of the integrated package.

This block proves positive, jointly rationally independent metric lengths
for the actual graph. It does not define its Kirchhoff Laplacian or spectral
surplus law and does not identify the spectral distribution with the module
model. The stable-response and process-limit arguments are also separate.
