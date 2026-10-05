import AIM.P114.LengthDefinitions
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.FieldTheory.AlgebraicClosure
import Mathlib.FieldTheory.Galois.Infinite
import Mathlib.Data.Nat.Squarefree
import Mathlib.NumberTheory.Real.Irrational

/-!
Joint rational independence of the actual prescribed lengths. The proof uses
Dedekind independence of characters on the automorphism group of the relative
algebraic closure of ℚ in ℂ. No independence or sign-flip action is assumed.
-/

noncomputable section

namespace AIM.P114

private lemma root_pos (j : ℕ) : 0 < primeRootLength j := by
  apply Real.sqrt_pos.2
  exact_mod_cast (Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime j).pos

private lemma root_sq (j : ℕ) :
    primeRootLength j ^ 2 = (Nat.nth Nat.Prime j : ℝ) :=
  Real.sq_sqrt (Nat.cast_nonneg _)

private abbrev RadicalField := algebraicClosure ℚ ℂ

private instance : IsAlgClosure ℚ RadicalField := algebraicClosure.isAlgClosure ℚ ℂ
private instance : IsGalois ℚ RadicalField := ⟨⟩

/-- The actual positive real root, viewed inside the relative algebraic closure. -/
private def radical (j : ℕ) : RadicalField :=
  ⟨(primeRootLength j : ℂ), mem_algebraicClosure_iff'.2 <|
    IsIntegral.of_pow (n := 2) (by norm_num) <| by
      have hs : (primeRootLength j : ℂ) ^ 2 = (Nat.nth Nat.Prime j : ℂ) := by
        exact_mod_cast root_sq j
      rw [hs]
      simpa using (isIntegral_algebraMap (R := ℚ) (A := ℂ)
        (x := (Nat.nth Nat.Prime j : ℚ)))⟩

private lemma radical_sq (j : ℕ) :
    radical j ^ 2 = (Nat.nth Nat.Prime j : RadicalField) := by
  apply Subtype.val_injective
  change (primeRootLength j : ℂ) ^ 2 = (Nat.nth Nat.Prime j : ℂ)
  exact_mod_cast root_sq j

private lemma radical_ne_zero (j : ℕ) : radical j ≠ 0 := by
  intro h
  have hv := congrArg (fun x : RadicalField => (x : ℂ)) h
  change (primeRootLength j : ℂ) = 0 at hv
  have hr : primeRootLength j = 0 := by exact_mod_cast hv
  exact (root_pos j).ne' hr

private lemma radical_aut_sign (j : ℕ) (σ : RadicalField ≃ₐ[ℚ] RadicalField) :
    σ (radical j) = radical j ∨ σ (radical j) = -radical j := by
  apply sq_eq_sq_iff_eq_or_eq_neg.1
  rw [← map_pow, radical_sq]
  simp

/-- A sign character is constructed from the actual root and its conjugates. -/
private def radicalCharacter (j : ℕ) :
    (RadicalField ≃ₐ[ℚ] RadicalField) →* RadicalField where
  toFun σ := σ (radical j) / radical j
  map_one' := by simp [radical_ne_zero]
  map_mul' σ τ := by
    change σ (τ (radical j)) / radical j =
      (σ (radical j) / radical j) * (τ (radical j) / radical j)
    rcases radical_aut_sign j τ with h | h <;>
      simp [h, radical_ne_zero, map_neg, neg_div]

private lemma distinct_primes_not_rat_square {p q : ℕ}
    (hp : Nat.Prime p) (hq : Nat.Prime q) (hpq : p ≠ q) (a : ℚ) :
    a ^ 2 ≠ ((p * q : ℕ) : ℚ) := by
  intro ha
  have hs : Squarefree (p * q) := (Nat.squarefree_mul
    ((Nat.coprime_primes hp hq).2 hpq)).2
    ⟨(Nat.prime_iff.1 hp).squarefree, (Nat.prime_iff.1 hq).squarefree⟩
  have hsq : IsSquare ((p * q : ℕ) : ℚ) := ⟨a, by simpa [pow_two] using ha.symm⟩
  obtain ⟨k, hk⟩ := Rat.isSquare_natCast_iff.1 hsq
  have hk1 : k = 1 := Nat.isUnit_iff.1 (hs k (by rw [hk]))
  rw [hk1] at hk
  nlinarith [hp.two_le, hq.two_le]

private lemma radical_ratio_not_rational {i j : ℕ} (hij : i ≠ j) (a : ℚ) :
    radical i / radical j ≠ (a : RadicalField) := by
  intro h
  have hm : radical i * radical j =
      (a : RadicalField) * (Nat.nth Nat.Prime j : RadicalField) := by
    calc
      radical i * radical j = (radical i / radical j) * radical j ^ 2 := by
        field_simp
      _ = _ := by rw [h, radical_sq]
  have hsq : ((a * (Nat.nth Nat.Prime j : ℚ) : ℚ) : RadicalField) ^ 2 =
      ((Nat.nth Nat.Prime i * Nat.nth Nat.Prime j : ℕ) : RadicalField) := by
    simp only [Rat.cast_mul, Rat.cast_natCast]
    rw [← hm, mul_pow, radical_sq, radical_sq, Nat.cast_mul]
  have hrat : (a * (Nat.nth Nat.Prime j : ℚ)) ^ 2 =
      ((Nat.nth Nat.Prime i * Nat.nth Nat.Prime j : ℕ) : ℚ) := by
    exact_mod_cast hsq
  exact distinct_primes_not_rat_square
    (Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime i)
    (Nat.nth_mem_of_infinite Nat.infinite_setOfPred_prime j)
    (fun he => hij (Nat.nth_injective Nat.infinite_setOfPred_prime he)) _ hrat

private lemma radicalCharacter_injective : Function.Injective radicalCharacter := by
  intro i j hij
  by_contra hne
  have hfixed (σ : RadicalField ≃ₐ[ℚ] RadicalField) :
      σ (radical i / radical j) = radical i / radical j := by
    have hc := congrArg (fun χ : (RadicalField ≃ₐ[ℚ] RadicalField) →* RadicalField =>
      χ σ) hij
    change σ (radical i) / radical i = σ (radical j) / radical j at hc
    rw [map_div₀]
    apply (div_eq_div_iff (by simpa using σ.injective.ne (radical_ne_zero j))
      (radical_ne_zero j)).2
    simpa [mul_comm] using (div_eq_div_iff (radical_ne_zero i) (radical_ne_zero j)).1 hc
  obtain ⟨a, ha⟩ :=
    (InfiniteGalois.mem_range_algebraMap_iff_fixed (radical i / radical j)).2 hfixed
  exact radical_ratio_not_rational hne a (by simpa using ha.symm)

private lemma radical_linearIndependent : LinearIndependent ℚ radical := by
  have hchars := (linearIndependent_monoidHom
    (RadicalField ≃ₐ[ℚ] RadicalField) RadicalField).comp
    radicalCharacter radicalCharacter_injective
  rw [linearIndependent_iff']
  intro s g h i hi
  have hfun : ∑ j ∈ s, ((g j : RadicalField) * radical j) •
      (radicalCharacter j : (RadicalField ≃ₐ[ℚ] RadicalField) → RadicalField) = 0 := by
    apply funext
    intro σ
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Pi.zero_apply]
    change ∑ j ∈ s, (g j : RadicalField) * radical j *
      (σ (radical j) / radical j) = 0
    have heq := congrArg (fun x : RadicalField => σ x) h
    simp only [map_sum, map_zero, Algebra.smul_def, map_mul, AlgEquiv.commutes] at heq
    convert heq using 1
    apply Finset.sum_congr rfl
    intro j hj
    change (g j : RadicalField) * radical j * (σ (radical j) / radical j) =
      (g j : RadicalField) * σ (radical j)
    field_simp [radical_ne_zero]
  have hz := (linearIndependent_iff'.1 hchars) s
    (fun j => (g j : RadicalField) * radical j) hfun i hi
  have hc := (mul_eq_zero.1 hz).resolve_right (radical_ne_zero i)
  exact_mod_cast hc

/-- All actual successive prime square roots are jointly rationally independent. -/
theorem prime_root_lengths_linearIndependent :
    LinearIndependent ℚ primeRootLength := by
  rw [linearIndependent_iff']
  intro s g h i hi
  have hk : ∑ j ∈ s, g j • radical j = 0 := by
    apply Subtype.val_injective
    have hc := congrArg Complex.ofReal h
    simpa [radical, Algebra.smul_def] using hc
  exact (linearIndependent_iff'.1 radical_linearIndependent) s g hk i hi

/-- Every actual edge has positive prescribed length in the source range. -/
theorem counterexample_metric_lengths_positive (m : ℕ) (hm : 3 ≤ m) :
    ∀ e : CounterexampleEdge m, 0 < counterexampleMetricLength m e := by
  intro e
  cases e with
  | none =>
      have hmpos : 0 < (m : ℝ) := by exact_mod_cast (show 0 < m by omega)
      exact mul_pos (pow_pos hmpos 6) (root_pos (3 * m))
  | some e => exact root_pos (3 * e.1.val + e.2.val)

private def edgePrimeIndex (m : ℕ) : CounterexampleEdge m → ℕ
  | none => 3 * m
  | some (i, j) => 3 * i.val + j.val

private lemma edgePrimeIndex_injective (m : ℕ) : Function.Injective (edgePrimeIndex m) := by
  intro e f h
  cases e with
  | none =>
      cases f with
      | none => rfl
      | some f =>
          have hi := f.1.isLt
          have hj := f.2.isLt
          simp only [edgePrimeIndex] at h
          omega
  | some e =>
      cases f with
      | none =>
          have hi := e.1.isLt
          have hj := e.2.isLt
          simp only [edgePrimeIndex] at h
          omega
      | some f =>
          have hj := e.2.isLt
          have hl := f.2.isLt
          simp only [edgePrimeIndex] at h
          congr 1
          apply Prod.ext <;> apply Fin.ext <;> omega

/-- The graph's exact length family, including the scaled pendant, is independent. -/
theorem counterexample_metric_lengths_linearIndependent (m : ℕ) (hm : 3 ≤ m) :
    LinearIndependent ℚ (counterexampleMetricLength m) := by
  have hm0 : (m : ℚ) ≠ 0 := by exact_mod_cast (show m ≠ 0 by omega)
  let w : CounterexampleEdge m → ℚˣ
    | none => Units.mk0 ((m : ℚ) ^ 6) (pow_ne_zero _ hm0)
    | some _ => 1
  have h := (prime_root_lengths_linearIndependent.comp (edgePrimeIndex m)
    (edgePrimeIndex_injective m)).units_smul w
  convert h using 1
  funext e
  cases e with
  | none => simp [w, counterexampleMetricLength, pendantLength, edgePrimeIndex,
      Function.comp_def, Units.smul_def, Algebra.smul_def]
  | some e => simp [w, counterexampleMetricLength, edgePrimeIndex,
      Function.comp_def]

end AIM.P114
