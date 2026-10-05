import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.Tactic

/-!
# Algebraic support for AIM problem 114

Mathematical source: Sidney Holden, A non-Gaussian limit for nodal surplus,
revised proof v0.3 (2026-10-02). Formalization: Codex for Sidney Holden.
These definitions do not model metric graphs, spectral surplus, Cauchy laws,
or the empirical-process limit. See NUMERICAL_TARGETS.md for the exact scope.
-/

noncomputable section

namespace AIM.P114

/-- Sign of a nonzero real, extended by `+1` at zero.
Every mathematical use of this extension below excludes the zero case. -/
def nonzeroSign (x : ℝ) : ℝ := if x < 0 then -1 else 1

/-- Real-valued indicator of strict negativity. -/
def negativeIndicator (x : ℝ) : ℝ := if x < 0 then 1 else 0

/-- The function `g` in manuscript §3, with the effective third input `r*c₃`. -/
def signModule (x y z : ℝ) : ℝ :=
  (1 - nonzeroSign (x + y + z) *
    (nonzeroSign x + nonzeroSign y + nonzeroSign z)) / 2

/-- The manuscript's centered module contribution, Eq. (8). -/
def centeredModule (a x y z : ℝ) : ℝ := nonzeroSign a * signModule x y z

/-- Three edge sign counts minus the pivot contribution `1{a < 0}`.
The common vertex value is `(x+y+z)/a`; `z` denotes `r*c₃`. -/
def moduleCount (a x y z : ℝ) : ℝ :=
  negativeIndicator (x * ((x + y + z) / a)) +
  negativeIndicator (y * ((x + y + z) / a)) +
  negativeIndicator (z * ((x + y + z) / a)) - negativeIndicator a

/-- Average squared module value over the four first/second sign choices,
with the effective third sign fixed positive. -/
def signSecondMoment (x y z : ℝ) : ℝ :=
  (signModule x y z ^ 2 + signModule (-x) y z ^ 2 +
    signModule x (-y) z ^ 2 + signModule (-x) (-y) z ^ 2) / 4

/-- Strict triangle event used in the deterministic variance function `v`. -/
def triangleIndicator (x y z : ℝ) : ℝ :=
  if |x - y| < z ∧ z < x + y then 1 else 0

end AIM.P114
