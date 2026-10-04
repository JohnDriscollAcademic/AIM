# Independent mathematical AI audit of PR 30 — AIM 553

**Repository evidence:** [proof](../../solutions/siavash-sadeghi-553/aim553_report.pdf), [source](../../solutions/siavash-sadeghi-553/aim553_report.tex), and [problem](../../../problems/553-continuous-adaptive-measurement-complexity.md). Submitted in [PR #30](https://github.com/MColbrook/AIM/pull/30) at `1efa5e29038e1fb338e04ee7aa3f5ac0a23cea4d`.

Date: 4 October 2026.

This is a fresh, independent AI referee audit. The reviewing agent had no role in preparing the submitted manuscript. Its mathematical conclusions below come from reading the proof and checking the imported results, not from accepting the package's preparation reports, catalogue checks, compile logs, or assertions of earlier review. This is neither independent human review nor formal proof verification. No repository/manuscript edits or GitHub actions were made in this audit.

## Exact scope and integrity

- Submitted PR: 30; exact reviewed head: `1efa5e29038e1fb338e04ee7aa3f5ac0a23cea4d`.
- Submitted package: `research/solutions/siavash-sadeghi-553`.
- Mathematical source: `aim553_report.tex`, 182 physical lines in the inspected snapshot.
- Current target: `problems/553-continuous-adaptive-measurement-complexity.md` at catalogue commit `c4b2a812bb5babdb1efdad8c3b8080e7301ee507`.
- Exact Git TeX blob: 10,057 bytes; SHA-256 `74c85ecffe3752c2837abda39922ad36c0ab455b73f35f27e484fab5f851567a`.
- Inspected snapshot TeX: 10,239 bytes; SHA-256 `516160feb6452b3c54070a7ea68c9837bd223beb2f6c56174bbc040d18ac6ae8`.

I independently recomputed both TeX hashes and compared the snapshot bytes with the exact Git blob. The snapshot has CRLF line endings and the Git blob has LF line endings; replacing CRLF by LF gives byte-for-byte identity. This audit is therefore of the mathematical text at the stated PR head, not a later worktree version. The root reviewer separately checked the package manifest; that packaging fact is not evidence for the proof.

I read the current target from the exact catalogue commit. I also read the target at the manuscript's cited commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441`; the mathematical statement and information model agree with the current target. This manuscript is specifically the sharp-asymptotic solution, not a claim that every exact value of N(m) is determined.

## Verdict and status recommendation

**Verdict: the submitted proof establishes its stated bound in the full target information model. No substantive mathematical defect was found.** It proves


```math
\lfloor\log_2 m\rfloor+1\leq N(m)\leq\lceil\log_2 m\rceil+1
```


for m >= 2, and hence N(m) ~ log_2 m. It also determines N(2^r) = r+1 for r >= 1. The lower-bound argument is stronger: whenever m >= 2^n, every deterministic procedure using at most n such measurements has infinite worst-case error on all of R^m.

**Recommendation: accept as solving the sharp-asymptotic alternative in entry 553, and permit a solved status explicitly qualified as “sharp asymptotic established; exact non-power-of-two values remain open.”** The current target explicitly asks to determine N(m) **or** its sharp asymptotic growth. The unresolved value N(3) does not prevent this submission from satisfying that alternative. A status description must not imply that N(3), or all exact N(m), is known.

The outcome is an independent AI mathematical assessment; any catalogue provenance should retain that distinction from human refereeing or a checked formal development.

## Independent proof audit

### 1. The genus is meaningful on the actual sets used

The definition is the least r for which a continuous odd map K -> R^r minus {0} exists, with genus(empty) = 0. All nonempty K under consideration are compact invariant subsets of a Euclidean sphere of positive radius. The inclusion into the ambient R^m is an odd nonvanishing map, so the genus is finite. Nonempty sets have genus at least one. Normalizing a nonvanishing map gives an odd map to S^(r-1), without changing the relevant existence assertion.

No manifold, local connectedness, triangulation, or finite-complex hypothesis is required. Compact subsets of the sphere are metrizable and normal, and compact subspaces are closed. Those are precisely the facts needed for the extension and compactness arguments below. In particular, the iteratively chosen sets can be quite irregular without invalidating the proof.

For S_R^(m-1), the inclusion gives genus <= m. An odd nonvanishing map into R^r with r < m, padded with zero coordinates to R^(m-1), contradicts Borsuk–Ulam: its antipodal equality would imply that its value is zero. Thus genus(S_R^(m-1)) = m. Rescaling R does not change this conclusion.

### 2. Odd extension and the zero-set loss

For a compact invariant A contained in K, extend each coordinate of an odd sphere-valued map on A to a continuous real-valued function on K by Tietze. These coordinate functions are bounded on A. If F_0 denotes the vector extension, then


```math
F(x)=\tfrac12(F_0(x)-F_0(-x))
```


is continuous, odd, and agrees with the original map on A. The agreement uses both the invariance of A and oddness of the original map. The set where F is nonzero is invariant and open and contains A; restricting and normalizing gives the required neighborhood map. Nonvanishing on all of K is not asserted or needed.

For odd h, Z = h^(-1)(0) is compact and invariant. If Z is empty, h itself witnesses genus(K) <= 1. If Z is nonempty and has genus r, the extension F is nonzero on Z. The odd vector map (F,h) is then nonzero everywhere on K: on Z the F coordinate works; off Z the h coordinate works. Therefore genus(K) <= r+1. This proves the claimed zero-set inequality without any unproved genus subadditivity theorem or regularity assumption on Z.

### 3. The even-fiber half-genus lemma and its gluing step

This is the main topological point, and I checked it directly rather than treating the claimed lemma as a standard imported result.

Suppose every fiber of the continuous even f:K -> R has genus <= r. For nonempty K one can take r >= 1; a map of a lower-dimensional target can be padded to R^r and normalized. Each fiber is compact and invariant and has an invariant open neighborhood U_y with an odd map to S^(r-1). Compactness of K guarantees an interval I_y about y with f^(-1)(I_y) contained in U_y. Otherwise a sequence in the closed compact complement K minus U_y would have f-values tending to y; a convergent subsequence would produce a point of the fiber outside U_y, a contradiction.

The two-color refinement used in the source is valid for an arbitrary compact subset B=f(K) of R, including disconnected sets and sets with isolated points. Here is an explicit version that checks the mesh and disjointness details. Give the finite original interval cover of B a relative Lebesgue number delta. Choose a grid spacing a > 0 with 3a/2 < delta and use intervals


```math
J_k=(ka-3a/4,ka+3a/4).
```


Their union covers R. Consecutive intervals overlap, while intervals whose indices have the same parity are pairwise disjoint. Each J_k intersected with B has diameter < delta and thus lies in some original I_y relative to B. Retain the finitely many J_k meeting B. Coloring by k modulo 2 gives exactly the refinement asserted in the manuscript, with each preimage f^(-1)(J_k) in a valid U_y.

For each color, the preimages are pairwise disjoint open subsets of K. Defining a map on each such preimage by its inherited odd sphere map therefore yields a continuous map on their union V_j: continuity is local, and each piece is open in that union. The pieces need not be connected; the source's phrase “component interval” refers to the disjoint intervals, not to an assumption on their preimages. Evenness of f makes V_j invariant.

The partition-of-unity step is also sound. For this two-set cover one may avoid any additional topological theorem: using the antipodally invariant Euclidean metric on K, let d_j(x)=dist(x,K minus V_j), treating d_j=1 when V_j=K. When a complement is nonempty it is closed and compact, so d_j is continuous and is positive exactly inside V_j. Since V_0 and V_1 cover K, their sum is everywhere positive. The functions alpha_j=d_j/(d_0+d_1) are continuous, even, sum to one, and vanish outside the respective V_j. Alternatively the averaging argument in the source preserves these properties because V_j is invariant.

Although v_j may fail to have a limit at a boundary point of V_j, alpha_j v_j does have zero limit there: its norm equals alpha_j, since v_j is sphere-valued. Its zero extension is therefore continuous. The concatenated map


```math
x\longmapsto(\alpha_0(x)v_0(x),\alpha_1(x)v_1(x))
```


is odd. It is nonzero because at least one alpha_j is positive and its corresponding v_j has norm one; the two blocks cannot cancel. Hence genus(K) <= 2r. Taking r = ceil(genus(K)/2)-1 proves the claimed existence of a fiber of genus >= ceil(genus(K)/2). The genus-one and empty-set cases are immediate. There is no missing passage to closed neighborhoods, no requirement of a continuous choice of the maps as y varies, and no infinite gluing issue.

### 4. One measurement loses at most half the genus

For arbitrary continuous lambda on K, the function h(x)=lambda(x)-lambda(-x) is continuous and odd. On its zero set Z, the restriction of lambda is even. The preceding lemmas therefore give a compact invariant fiber K' with


```math
\mathop{\mathrm{genus}}(K')\geq
\left\lceil\frac{\mathop{\mathrm{genus}}(K)-1}{2}\right\rceil
=\left\lfloor\frac{\mathop{\mathrm{genus}}(K)}2\right\rfloor.
```


Using an inequality for genus(Z) is legitimate because ceiling is monotone. The fiber is closed in the compact Z, and its invariance follows from the even restriction. For genus(K) >= 2 this guarantees that K' is nonempty. For genus <= 1 the statement allows K' to be empty; choosing any scalar y handles that vacuous boundary case. Thus the proof does not assume that a nonempty zero set exists when the lower bound is only zero.

### 5. The adaptive transcript and arbitrary history dependence

Fix one deterministic algorithm and one positive R. Beginning at K_0=S_R^(m-1), use the one-measurement lemma only after the preceding measurement history has been fixed. At stage j, all points of K_(j-1) have the same earlier history. They therefore select the same branch functional, which is continuous in x by the target assumption. Its restriction to K_(j-1) is continuous. The lemma gives one measurement value y_j and a compact invariant K_j on which this value is constant. Every point of K_j has the same entire history through stage j.

The integer recursion is correct: genus(K_j) >= floor(m/2^j), since floor(floor(a)/2)=floor(a/2) for this integer iteration. If m >= 2^n, the set reached after n-1 stages has genus >= 2. All sets needed along this induction are consequently nonempty. No dependence of the branch on y_1,...,y_(j-1) is assumed continuous, measurable, or computable.

At the last fixed branch, the continuous odd difference lambda_n(x)-lambda_n(-x) must vanish somewhere on K_(n-1). A nowhere-zero difference would witness genus <= 1, contradicting genus >= 2. This gives x and -x with the same final value and, by the induction, the same complete transcript. The argument for n=1 uses K_0 directly and is valid. Padding an algorithm that stops based on its measured history with zero measurements preserves the transcript equivalence and the permitted continuity. The n=0 case, if zero is included in the convention for n, follows separately from the fact that a measurement-free deterministic decoder returns one fixed vector.

### 6. Decoder obstruction on every radius and quantifiers

Determinism and the unrestricted decoder mean exactly that the same transcript yields the same vector z. No decoder continuity is used. Since ||x-(-x)||_2=2R, the triangle inequality forces at least one of ||x-z||_2 and ||-x-z||_2 to be >= R. The algorithm was fixed before R was chosen. Repeating this existence argument for every R > 0 proves that this fixed algorithm's worst-case error is infinite.

The transcript and obstructing pair are permitted to depend on R; a common transcript for all radii is unnecessary. In particular, this reasoning does not accidentally prove only a lower bound for an algorithm chosen after seeing R. It proves “for every algorithm, for every radius, there exists a bad indistinguishable pair,” which implies the asserted infinite supremum.

For n=floor(log_2 m), m >= 2^n and n >= 1 when m >= 2. Such an algorithm cannot achieve any finite uniform error. This rules out every epsilon-dependent algorithm using at most n measurements and establishes N(m) >= n+1 with the target's order of quantifiers. Equivalence of finite-dimensional norms also makes infinite error persist in any norm, as stated in the source. The imported upper bound supplies an algorithm for every epsilon > 0 in the same global R^m model, completing the main theorem.

## Primary-reference audit

1. **Krieg–Novak–Ullrich, arXiv:2412.06468v2 (22 September 2026).** I accessed the [version-specific primary author manuscript](https://arxiv.org/html/2412.06468v2), rather than relying on the submitted review report. Theorem 1 states the upper bound ceil(log_2 m)+1 for every positive tolerance on all of R^m. Its definition allows adaptive continuous branch functionals and arbitrary reconstruction, matching the target. Section 2 explains the improvement over the Lipschitz construction; Section 3 still states the lower-bound question. Thus the imported upper bound and its version/date attribution are correct. Lemma 9 concerns nonadaptive reconstruction and is not used by the submitted lower-bound proof. The extra bibliography mention of it and Banach unit balls creates no mathematical dependency here.

2. **Borsuk–Ulam.** I checked the [publisher's record for Borsuk's original 1933 paper](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/20/0/93008/drei-satze-uber-die-n-dimensionale-euklidische-sphare): *Fundamenta Mathematicae* 20, 177–190, DOI 10.4064/fm-20-1-177-190. The publisher's scan download returned HTTP 403, so I do not claim to have inspected that scan. I checked the precise theorem and proof in [Hatcher's author-hosted *Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Corollary 2B.7, printed page 176. Its antipodal-equality assertion is exactly the one needed for the sphere genus calculation.

3. **Tietze extension.** The original DOI 10.1515/crll.1915.145.9 and a Göttingen scan entry were inaccessible through the browsing tool. The needed bounded normal-space statement was checked in the [official Mizar Mathematical Library's TIETZE article](https://mizar.uwb.edu.pl/version/current/html/tietze.html), theorem TIETZE:23: a continuous [-1,1]-valued map on a closed subset of a normal space has a continuous extension to that space. Sphere-map coordinates satisfy the bound, and compact metric K satisfies normality. This is a primary formal-library theorem statement, not a claim that the present manuscript has been formalized or checked by Mizar.

The proof's fiber results are proved within the submission and were independently checked above. I did not use search snippets, tertiary summaries, or other submission packages as premises. The interval refinement and partition of unity were checked by direct constructions, so they do not depend on an unverified imported dimension theorem.

## Defects, limitations, and optional polish

There are **no blocking mathematical defects** and no missing assumption that narrows the result relative to the current target. The proof applies to deterministic algorithms with globally continuous branch functionals for each fixed history, unrestricted dependence on exact histories, unrestricted decoding, every epsilon, and every input in R^m.

Optional precision improvements would be to give explicit grid interval widths in the even-fiber proof; explicitly dispatch the empty/genus-one case of the one-measurement lemma; mention the trivial n=0 case if the stronger statement intends to include it; and add bibliographic references for the two named classical theorems. These details are fully justified above and are exposition improvements, not gaps requiring a new argument.

The paper deliberately leaves the one-integer gap at non-powers of two. In particular it only yields 2 <= N(3) <= 3. It should continue to say so. Novelty/priority beyond verifying the version-specific cited paper is not a comprehensive literature certification; it does not affect the internal validity or exact target coverage assessed here.

## Audit boundary

I reviewed the entire submitted mathematical argument, checked its target quantifiers, recomputed the TeX integrity comparison, and consulted primary theorem sources. I did not count successful compilation or package preparation logs as mathematical validation, and I did not conduct independent PDF layout or build verification. No package or repository content was modified. This audit is saved outside the submitted package as requested.
