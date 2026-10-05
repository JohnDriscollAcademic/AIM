import AIM.P114.VarianceDefinitions
import AIM.P114.MixtureProof
import Mathlib.MeasureTheory.Integral.Bochner.Set

/-! The actual Cauchy-triple variance function of the source manuscript.
Full support and atomlessness of its coordinate laws are proved from their
positive densities; no regularity or nonconstancy of the function is assumed. -/

noncomputable section

open MeasureTheory ProbabilityTheory Set Filter
open scoped Topology

namespace AIM.P114

private instance standardCauchy_noAtoms : NullSingletonClass (cauchyMeasure 0 1) := by
  rw [cauchyMeasure_of_scale_ne_zero 0 (by norm_num : (1 : NNReal) ≠ 0)]
  infer_instance

private instance standardCauchy_openPos : Measure.IsOpenPosMeasure (cauchyMeasure 0 1) := by
  have hac : (volume : Measure ℝ) ≪ cauchyMeasure 0 1 := by
    rw [cauchyMeasure_of_scale_ne_zero 0 (by norm_num : (1 : NNReal) ≠ 0)]
    apply withDensity_absolutelyContinuous' (by fun_prop)
    exact .of_forall fun x => (ne_of_gt (ENNReal.ofReal_pos.mpr
      (cauchyPDF_pos 0 (by norm_num : (1 : NNReal) ≠ 0) x)))
  exact hac.isOpenPosMeasure

private instance triple_probability : IsProbabilityMeasure cauchyTripleMeasure := by
  unfold cauchyTripleMeasure
  infer_instance

private instance triple_openPos : Measure.IsOpenPosMeasure cauchyTripleMeasure := by
  unfold cauchyTripleMeasure
  infer_instance

@[fun_prop] private lemma magnitude_continuous : Continuous cauchyMagnitude := by
  unfold cauchyMagnitude
  fun_prop

private lemma magnitude_sq (x : ℝ) : cauchyMagnitude x ^ 2 = 1 + x ^ 2 :=
  Real.sq_sqrt (by positivity)

private lemma magnitude_pos (x : ℝ) : 0 < cauchyMagnitude x := by
  unfold cauchyMagnitude
  positivity

private lemma abs_le_magnitude (x : ℝ) : |x| ≤ cauchyMagnitude x :=
  Real.abs_le_sqrt (by linarith)

private lemma triangle_open (r : ℝ) : IsOpen (varianceTriangleEvent r) := by
  unfold varianceTriangleEvent
  have h1 : IsOpen {p : (ℝ × ℝ) × ℝ |
      |cauchyMagnitude p.1.1 - cauchyMagnitude p.1.2| < |r| * cauchyMagnitude p.2} :=
    isOpen_lt (by fun_prop) (by fun_prop)
  have h2 : IsOpen {p : (ℝ × ℝ) × ℝ |
      |r| * cauchyMagnitude p.2 < cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2} :=
    isOpen_lt (by fun_prop) (by fun_prop)
  exact h1.inter h2

private lemma triangle_nonempty (r : ℝ) (hr : r ≠ 0) :
    (varianceTriangleEvent r).Nonempty := by
  refine ⟨((r, r), 0), ?_⟩
  simp only [varianceTriangleEvent, mem_ofPred_eq, sub_self, abs_zero,
    cauchyMagnitude, zero_pow (by decide : (2 : ℕ) ≠ 0), add_zero, Real.sqrt_one, mul_one]
  constructor
  · exact abs_pos.mpr hr
  · have h := abs_le_magnitude r
    have hp := magnitude_pos r
    dsimp [cauchyMagnitude] at h hp
    nlinarith

private lemma strict_complement_positive (r : ℝ) (hr : r ≠ 0) :
    0 < cauchyTripleMeasure.real (varianceTriangleEvent r)ᶜ := by
  let U : Set ((ℝ × ℝ) × ℝ) :=
    {p | cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2 < |r| * cauchyMagnitude p.2}
  have hUo : IsOpen U := by
    apply isOpen_lt <;> fun_prop (disch := exact magnitude_continuous)
  have hUn : U.Nonempty := by
    refine ⟨((0, 0), 3 / |r|), ?_⟩
    have hp : 0 < |r| := abs_pos.mpr hr
    have h := abs_le_magnitude (3 / |r|)
    rw [abs_of_nonneg (div_nonneg (by norm_num) hp.le)] at h
    have hh := mul_le_mul_of_nonneg_left h hp.le
    have he : |r| * (3 / |r|) = 3 := by field_simp
    rw [he] at hh
    change cauchyMagnitude 0 + cauchyMagnitude 0 < |r| * cauchyMagnitude (3 / |r|)
    norm_num [cauchyMagnitude] at *
    linarith
  have hUs : U ⊆ (varianceTriangleEvent r)ᶜ := by
    intro p hp hT
    exact (not_lt_of_gt hp) hT.2
  have hpU : 0 < cauchyTripleMeasure.real U :=
    ENNReal.toReal_pos (hUo.measure_ne_zero _ hUn) (measure_ne_top _ _)
  exact lt_of_lt_of_le hpU (measureReal_mono hUs)

/-- The same strict event formula gives `v(0)=1/2`. -/
theorem actual_nodal_variance_zero : actualNodalVariance 0 = 1 / 2 := by
  have he : varianceTriangleEvent 0 = ∅ := by
    ext p
    simp [varianceTriangleEvent, not_lt_of_ge (abs_nonneg _)]
  simp [actualNodalVariance, he]

/-- Strict source bounds for every finite nonzero real parameter. -/
theorem actual_nodal_variance_bounds (r : ℝ) (hr : r ≠ 0) :
    (1 / 4 : ℝ) < actualNodalVariance r ∧ actualNodalVariance r < (1 / 2 : ℝ) := by
  have hp : 0 < cauchyTripleMeasure.real (varianceTriangleEvent r) :=
    ENNReal.toReal_pos ((triangle_open r).measure_ne_zero _ (triangle_nonempty r hr))
      (measure_ne_top _ _)
  have hc := strict_complement_positive r hr
  have hsum := measureReal_add_measureReal_compl (μ := cauchyTripleMeasure)
    (triangle_open r).measurableSet
  rw [probReal_univ] at hsum
  unfold actualNodalVariance
  constructor <;> linarith

private lemma magnitude_ae_ne (c : ℝ) :
    ∀ᵐ x ∂cauchyMeasure 0 1, cauchyMagnitude x ≠ c := by
  by_cases hex : ∃ y : ℝ, cauchyMagnitude y = c
  · obtain ⟨y, hy⟩ := hex
    filter_upwards [(cauchyMeasure 0 1).ae_ne y, (cauchyMeasure 0 1).ae_ne (-y)] with x hxy hxny
    intro hx
    have he : cauchyMagnitude x = cauchyMagnitude y := hx.trans hy.symm
    have hs : x ^ 2 = y ^ 2 := by
      have he2 := congrArg (fun z : ℝ => z ^ 2) he
      rw [magnitude_sq, magnitude_sq] at he2
      linarith
    exact (sq_eq_sq_iff_eq_or_eq_neg.mp hs).elim hxy hxny
  · exact .of_forall fun x hx => hex ⟨x, hx⟩

private lemma magnitudes_ae_distinct :
    ∀ᵐ p ∂(cauchyMeasure 0 1).prod (cauchyMeasure 0 1),
      cauchyMagnitude p.1 ≠ cauchyMagnitude p.2 := by
  apply (Measure.ae_prod_iff_ae_ae ?_).mpr
  · exact .of_forall fun x => (magnitude_ae_ne (cauchyMagnitude x)).mono fun y hy => Ne.symm hy
  · exact (isClosed_eq (by fun_prop) (by fun_prop)).measurableSet.compl

private lemma triangle_boundaries_ae_ne (r : ℝ) :
    ∀ᵐ p ∂cauchyTripleMeasure,
      |cauchyMagnitude p.1.1 - cauchyMagnitude p.1.2| ≠ |r| * cauchyMagnitude p.2 ∧
      |r| * cauchyMagnitude p.2 ≠ cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2 := by
  by_cases hr : r = 0
  · subst r
    have hp : ∀ᵐ p ∂cauchyTripleMeasure, cauchyMagnitude p.1.1 ≠ cauchyMagnitude p.1.2 :=
      (Measure.quasiMeasurePreserving_fst (μ := (cauchyMeasure 0 1).prod (cauchyMeasure 0 1))
        (ν := cauchyMeasure 0 1)).ae magnitudes_ae_distinct
    filter_upwards [hp] with p hp
    simp only [abs_zero, zero_mul]
    exact ⟨abs_ne_zero.mpr (sub_ne_zero.mpr hp), ne_of_lt (add_pos (magnitude_pos _) (magnitude_pos _))⟩
  · change ∀ᵐ p ∂((cauchyMeasure 0 1).prod (cauchyMeasure 0 1)).prod (cauchyMeasure 0 1), _
    apply (Measure.ae_prod_iff_ae_ae ?_).mpr
    · apply Eventually.of_forall
      intro xy
      filter_upwards [magnitude_ae_ne (|cauchyMagnitude xy.1 - cauchyMagnitude xy.2| / |r|),
        magnitude_ae_ne ((cauchyMagnitude xy.1 + cauchyMagnitude xy.2) / |r|)] with z hl hu
      constructor
      · intro he
        apply hl
        exact (eq_div_iff (abs_ne_zero.mpr hr)).mpr (by nlinarith)
      · intro he
        apply hu
        exact (eq_div_iff (abs_ne_zero.mpr hr)).mpr (by nlinarith)
    · exact ((isClosed_eq (by fun_prop) (by fun_prop)).measurableSet.compl).inter
        ((isClosed_eq (by fun_prop) (by fun_prop)).measurableSet.compl)

private lemma continuousAt_triangle_indicator
    (r : ℝ) (p : (ℝ × ℝ) × ℝ)
    (hl : |cauchyMagnitude p.1.1 - cauchyMagnitude p.1.2| ≠ |r| * cauchyMagnitude p.2)
    (hu : |r| * cauchyMagnitude p.2 ≠ cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2) :
    ContinuousAt (fun s => (varianceTriangleEvent s).indicator (fun _ => (1 : ℝ)) p) r := by
  let l := |cauchyMagnitude p.1.1 - cauchyMagnitude p.1.2|
  let u := cauchyMagnitude p.1.1 + cauchyMagnitude p.1.2
  let f : ℝ → ℝ := fun s => |s| * cauchyMagnitude p.2
  have hfc : ContinuousAt f r := by dsimp [f]; fun_prop
  change l ≠ f r at hl
  change f r ≠ u at hu
  have hstable : ∀ᶠ s in 𝓝 r, (l < f s ∧ f s < u) ↔ (l < f r ∧ f r < u) := by
    rcases hl.lt_or_gt with hl | hl <;> rcases hu.lt_or_gt with hu | hu
    · filter_upwards [continuousAt_const.eventually_lt hfc hl,
        hfc.eventually_lt continuousAt_const hu] with s hs1 hs2
      exact iff_of_true ⟨hs1, hs2⟩ ⟨hl, hu⟩
    · filter_upwards [continuousAt_const.eventually_lt hfc hu] with s hs
      exact iff_of_false (fun h => (not_lt_of_gt hs) h.2) (fun h => (not_lt_of_gt hu) h.2)
    · filter_upwards [hfc.eventually_lt continuousAt_const hl] with s hs
      exact iff_of_false (fun h => (not_lt_of_gt hs) h.1) (fun h => (not_lt_of_gt hl) h.1)
    · filter_upwards [hfc.eventually_lt continuousAt_const hl] with s hs
      exact iff_of_false (fun h => (not_lt_of_gt hs) h.1) (fun h => (not_lt_of_gt hl) h.1)
  apply Filter.EventuallyEq.continuousAt (y := (varianceTriangleEvent r).indicator (fun _ => (1 : ℝ)) p)
  filter_upwards [hstable] with s hs
  have hmem : p ∈ varianceTriangleEvent s ↔ p ∈ varianceTriangleEvent r := hs
  by_cases hp : p ∈ varianceTriangleEvent r
  · exact (Set.indicator_of_mem (hmem.mpr hp) (fun _ => (1 : ℝ))).trans (Set.indicator_of_mem hp (fun _ => (1 : ℝ))).symm
  · have hsnot : p ∉ varianceTriangleEvent s := fun h => hp (hmem.mp h)
    exact (Set.indicator_of_notMem hsnot (fun _ => (1 : ℝ))).trans (Set.indicator_of_notMem hp (fun _ => (1 : ℝ))).symm

private lemma triangle_probability_continuous :
    Continuous (fun r => cauchyTripleMeasure.real (varianceTriangleEvent r)) := by
  have heq (r : ℝ) : cauchyTripleMeasure.real (varianceTriangleEvent r) =
      ∫ p, (varianceTriangleEvent r).indicator (fun _ => (1 : ℝ)) p ∂cauchyTripleMeasure :=
    (integral_indicator_one (triangle_open r).measurableSet).symm
  simp_rw [heq]
  apply continuous_iff_continuousAt.mpr
  intro r
  apply continuousAt_of_dominated (bound := fun _ => (1 : ℝ))
  · exact .of_forall fun s => (measurable_const.indicator (triangle_open s).measurableSet).aestronglyMeasurable
  · apply Eventually.of_forall
    intro s
    exact .of_forall fun p => by
      by_cases hp : p ∈ varianceTriangleEvent s <;> simp [hp]
  · exact integrable_const _
  · filter_upwards [triangle_boundaries_ae_ne r] with p hp
    exact continuousAt_triangle_indicator r p hp.1 hp.2

/-- The actual Cauchy triangle probability is continuous, including at zero. -/
theorem actual_nodal_variance_continuous : Continuous actualNodalVariance := by
  unfold actualNodalVariance
  exact continuous_const.sub (triangle_probability_continuous.div_const 4)

/-- The source's actual function satisfies all hypotheses needed by the
completed product-law mixture theorem. -/
theorem actual_nodal_variance_mixture_inputs
    (ρ : Measure ℝ) [IsProbabilityMeasure ρ] [Measure.IsOpenPosMeasure ρ]
    (hzero : ρ {0} = 0) :
    Measurable actualNodalVariance ∧
    (∀ᵐ r ∂ρ, (1 / 4 : ℝ) < actualNodalVariance r ∧
      actualNodalVariance r < (1 / 2 : ℝ)) ∧
    (¬ ∃ c : ℝ, actualNodalVariance =ᵐ[ρ] fun _ => c) := by
  refine ⟨actual_nodal_variance_continuous.measurable, ?_, ?_⟩
  · have hz : ∀ᵐ r ∂ρ, r ≠ 0 := by simpa only [ae_iff, not_not, ofPred_eq_eq_singleton] using hzero
    exact hz.mono fun r hr => actual_nodal_variance_bounds r hr
  · rintro ⟨c, hc⟩
    have he := Measure.eq_of_ae_eq hc actual_nodal_variance_continuous continuous_const
    have h0 := congrFun he 0
    have h1 := congrFun he 1
    have hb := (actual_nodal_variance_bounds 1 one_ne_zero).2
    rw [actual_nodal_variance_zero] at h0
    linarith

/-- The actual Cauchy-defined variance produces a non-Gaussian normalized
law for any full-support ratio law with no atom at zero. -/
theorem actual_nodal_variance_mixture_not_gaussian
    (ρ : Measure ℝ) [IsProbabilityMeasure ρ] [Measure.IsOpenPosMeasure ρ]
    (hzero : ρ {0} = 0) :
    normalizedVarianceMixture ρ actualNodalVariance ≠ gaussianReal 0 1 := by
  obtain ⟨hm, hb, hn⟩ := actual_nodal_variance_mixture_inputs ρ hzero
  exact normalized_variance_mixture_not_gaussian ρ actualNodalVariance hm hb hn

end AIM.P114
