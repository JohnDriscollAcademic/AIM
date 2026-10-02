import LeanCert.Tactic.LeanCert

/-! Infrastructure control only: this proves no AIM problem target. The exact
rational bound exercises LeanCert's kernel certificate route.

Adapted from OpenProblemsInNLA; see ../../NOTICE.md. -/
set_option autoImplicit false
set_option leancert.trust "kernel"

namespace AIM.Statements.KernelSmoke

theorem log_two_upper : Real.log 2 < (7 / 10 : ℝ) := by
  leancert (trust := kernel)

#assert_trust kernel log_two_upper
#print axioms log_two_upper

end AIM.Statements.KernelSmoke
