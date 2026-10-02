import AIM.Statements.KernelSmoke

/-! This certificate exercises the shared checker and proves no AIM problem. -/
set_option leancert.trust "kernel"

namespace AIM.Statements.ComparatorControl

theorem log_two_upper : Real.log 2 < (7 / 10 : ℝ) :=
  AIM.Statements.KernelSmoke.log_two_upper

#assert_trust kernel log_two_upper
#print axioms log_two_upper

end AIM.Statements.ComparatorControl
