# Actual Gaussian variance-mixture proof

The three declarations in `AIM/P114/MixtureProof.lean` remove a probability-law
connection left open by the first submission. They construct the law of
`Z sqrt(V / EV)` on an actual product probability space and prove its
nonequality to the standard Gaussian from measurable, bounded, nonconstant V.
The source-specific identification `V = v(-A/B)` and convergence of the
nodal-surplus laws to this mixture remain unformalized.

`standard_gaussian_fourth_moment` proves `integral z^4 d(gaussianReal 0 1)=3`
from Mathlib's Gaussian moment-generating function. Four explicit derivative
certificates establish the successive polynomials multiplying `exp(t^2/2)`;
`iteratedDeriv_mgf_zero` identifies the fourth derivative with the integral.
Gaussian integrability is separately obtained from the existing finite-p
`MemLp` theorem.

`normalized_variance_mixture_moments` derives `EV >= 1/4` from the a.e. source
bounds, so the normalization is positive. The amplitude `sqrt(V/EV)` lies in
`[0,2]` a.e.; its powers are therefore integrable. Product integrability proves
integrability of every natural power of the mapped random variable, including
the advertised first, second, and fourth powers. Product-integral factorization
and a.e. square-root identities then prove mean zero, second moment one, and
fourth moment `3 E[V^2] / (EV)^2`. The pushforward has total mass one because
its defining map is measurable and the product measure is a probability.

`normalized_variance_mixture_not_gaussian` uses Mathlib's theorem that zero
variance forces a random variable to be a.e. equal to its expectation. Thus
the intrinsic nonconstancy hypothesis gives strictly positive variance. The
previous exact integral kurtosis theorem makes the constructed law's fourth
moment strictly larger than 3, contradicting its equality to the actual
standard Gaussian measure and its proved fourth moment.

The two statement reviews preceded implementation and bind the exact definition,
signature, and target-document bytes. No mixture moment, independence claim,
or non-Gaussian conclusion is assumed as a hypothesis. The product construction
supplies independence; measurability, a.e. bounds, and intrinsic nonconstancy of
the manuscript's eventual mixing variable are still separate input obligations.
