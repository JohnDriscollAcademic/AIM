import AIM.P114.GraphDefinitions
import AIM.P114.TransferDefinitions
import Mathlib.LinearAlgebra.LinearIndependent.Basic

/-!
# Actual prescribed metric lengths for AIM 114

Sidney Holden's v0.3 manuscript, Section 1, equation (1), numbers the
three edges of each module consecutively and gives the pendant length
`m^6 * sqrt(p_(3m+1))`. The existing prime-root definition is zero indexed.
These lengths are attached to the actual multigraph's distinct edge IDs.
-/

noncomputable section

namespace AIM.P114

/-- Actual edge lengths, with `some (i,j)` the `(3*i+j)`th core edge and
`none` the pendant. Prime indexing starts at zero, so the first length is
`sqrt 2` and the pendant uses the next prime after all `3*m` core primes. -/
def counterexampleMetricLength (m : ℕ) : CounterexampleEdge m → ℝ
  | none => pendantLength m
  | some (i, j) => primeRootLength (3 * i.val + j.val)

end AIM.P114
