# Prescribed-length moment-transfer proof

The five declarations in `AIM/P114/TransferProof.lean` close the final
prescribed-length error calculation in Sidney Holden's v0.3 manuscript.
They use actual indexed prime-root lengths and actual integrals under a
convex combination of two probability measures. The published identification
of that combination with the spectral surplus law is still unformalized.

The length estimate uses the monotonicity of the prime sequence and square
root to bound every one of the `3m` core lengths by the pendant root. Positivity
of the denominator allows exact cross-multiplication, yielding the source's
`3/(m^5+3)` bound. Joint rational independence of the roots is a separate
remaining obligation.

For a measurable function with values in `[0,B]` almost everywhere under both
input laws, boundedness first proves integrability. The two expectations lie
in the same interval, so their difference has absolute value at most `B`.
Linearity in the measure then gives the error bound `w*B`, including weights
zero and one.

For the actual centered and scaled even moments, support in `[0,2m-1]` gives
a squared normalized value at most `m`; the second and fourth integrands are
therefore at most `m` and `m^2`. Applying the measure bound gives the advertised
finite estimate. Comparing it with `3/m` for `m>=1` proves that the actual
difference of moment integrals tends to zero. The theorem does not assert
that either input sequence itself has a limiting moment.

Both independent statement approvals and the successful frozen-boundary
typecheck preceded implementation. Both independent proof referees separately
rebuilt, re-elaborated, and inspected all five transitive axiom sets. The
combined project still needs its own current Linux verification record;
acceptance of the earlier three declarations does not certify these proofs.
