# Independent referee audit: AIM641 cubic claim, PR #32

**Repository evidence:** [proof](../../solutions/siavash-sadeghi-641/aim641_report.pdf), [source](../../solutions/siavash-sadeghi-641/aim641_report.tex), and [problem](../../../problems/641-bos-simplex-interpolation-nodes.md). Submitted in [PR #32](https://github.com/MColbrook/AIM/pull/32) at `5648871ddd78366312a70fec7284887072acc942`.

Reviewer: **independent_641_pr32 (OpenAI Codex AI)**. Date: **2026-10-04**.

Reviewed PR head: **5648871ddd78366312a70fec7284887072acc942**.
Snapshot root:
`C:\Users\MatthewColbrook\.codex\visualizations\2026\10\01\01a0f88a-46a6-73c1-ae0f-23d167c70a94\active-solution-pr-review-2026-10-04\pr32`.

**Verdict:** The cubic Fejér theorem passes this independent AI mathematical audit. I found no blocking mathematical or verifier defect in the reviewed argument. Its certificate establishes the assertion in every integer dimension $`d\ge1`$, rather than merely testing a bounded collection of dimensions. This is a partial resolution of the grouped AIM641 target: it does not establish any of the three remaining quartic assertions. No human audit, Lean verification, other formal proof verification, or manuscript compilation is claimed.

## Inputs and independence

I read the current repository's CONTRIBUTING.md and problems/641-bos-simplex-interpolation-nodes.md, then the snapshot's aim641_report.tex and all four Python source files before executing them. I did not use the submitter's REVIEW_REPORT.md, REPRODUCTION_RECORD.md, supplied PASS logs, or submitted PDF as evidence of mathematical correctness. I did not alter the supplied manuscript, certificate, or code, and made no repository, Git, or GitHub mutations.

The exact reviewed snapshot-byte SHA-256 of **aim641_report.tex** is
`9fd94d8f8a79e63048511d56f1dd868603f6a9299770c25992717ec4afd6d4ea`.
Normalizing CRLF to LF gives
`9a31cba0a79133cfda34a135405a99293a89e7932979f0ceea7aceb2fc30c03a`,
which matches its MANIFEST.sha256 entry. The coordinating reviewer separately checked that this LF hash is the exact Git blob hash at the cited head, and that all 23 manifest entries match the raw Git blobs. The snapshot byte/hash difference is line-ending conversion, not a content defect.

[The fresh independent log](641-independent-checks/independent-normal.log) records both byte and LF-normalized hashes of the manuscript, verify_cubic.py, check_printed_table.py, crosscheck_cubic.py, test_verifier.py, and cubic_certificate.json. The later optimized run records the same input hashes.

## Target and primary source

The node family and theorem agree exactly with assertion 1 of the repository statement. Bos's primary article defines this cubic family and proves the Fejér property for $`1\le d\le28`$, while conjecturing all dimensions. Its vertex, ordered-edge, and triangular-face cardinal polynomials agree with those in the manuscript after homogenization. Its proof uses the same centroid-to-facet induction and the finite elevations $`8,5,3,3`$ for dimensions $`3,4,5,6`$. These points were checked in [Bos, Section 3 and Proposition 3.1](https://arxiv.org/html/2205.06498v1#S3), with the [original PDF](https://arxiv.org/pdf/2205.06498) also opened. The publisher DOI was inaccessible through the browsing tool; the primary arXiv text was accessible.

The three quartic targets are distinct: the Fejér inequality in dimension three, the Fekete property in every dimension, and the fourth-power inequality in every dimension. They occur as Conjectures 4.2, 4.3, and 4.6 in [Bos, Section 4](https://arxiv.org/html/2205.06498v1#S4). The manuscript expressly excludes them. The cubic result therefore warrants changing the cubic known-case scope to every $`d\ge1`$, while retaining a partially resolved grouped entry and a nonempty remaining quartic target. This audit does not establish priority or an exhaustive absence of later publications.

## Independent mathematical derivation

Let $`M=d+1`$, $`S=\sum x_i`$, and $`p_j=\sum x_i^j`$.

**Cardinality and cardinality conditions.** There are
$`M+M(M-1)+\binom M3=\binom{M+2}3`$ nodes, the dimension of cubics on $`S=1`$. An independent derivation of the vertex polynomial is

```math
x_i(5x_i^2-5Sx_i+S^2)+x_i\sum_{\substack{j<k\\j,k\ne i}}x_jx_k
=\frac{x_i}{2}(12x_i^2-12Sx_i+3S^2-p_2).
```

At its own vertex this equals one. At either edge abscissa, $`t(1-t)=1/5`$ makes the first term zero; the second term vanishes. At a triangular-face centroid containing $`i`$, its two terms are $`-1/27`$ and $`1/27`$. Outside its support, the factor $`x_i`$ vanishes.

For an ordered edge, write $`A=(3+\sqrt5)/2`$, $`B=(3-\sqrt5)/2`$. The polynomial $`5x_ix_j(Ax_i+Bx_j-S)`$ is zero at all vertices and at every triangular-face centroid. At the intended edge node its bracket is one and $`5x_ix_j=1`$; at the reversed edge node its bracket is zero. At other edge nodes at least one product factor vanishes. The triangular-face polynomial $`27x_ix_jx_k`$ is one only at its own face centroid and zero at every other node. These arguments apply in every dimension and prove unisolvence as well as the claimed basis.

The fresh independent script additionally constructs all nodes and checks the full cardinal evaluation matrices for $`M=2,3,4`$, giving identities of sizes 4, 10, and 20.

**Squared-sum identity.** I independently grouped the vertex, unordered-edge-pair, and face sums. With $`a=(3S^2-p_2)/2`$, their expressions are

```math
V=36p_6-72Sp_5+(36S^2+12a)p_4-12Sap_3+a^2p_2,
```


```math
E=25\{7(p_2p_4-p_6)+2(p_3^2-p_6)-6S(p_2p_3-p_5)+S^2(p_2^2-p_4)\},
```


```math
F=\tfrac{243}{2}p_2^3-\tfrac{729}{2}p_2p_4+243p_6.
```

For the edge calculation, the sum of the two squares on an unordered pair is
$`25x_i^2x_j^2[7(x_i^2+x_j^2)+4x_ix_j-6S(x_i+x_j)+2S^2]`$;
the radical cancels exactly. Expanding $`V+E+F`$ gives precisely the manuscript's $`\mathcal K_M`$. This derivation holds for arbitrary $`M`$ and independently justifies the homogeneous, symmetric, zero-padding-stable deficit $`H_M=S^6-\mathcal K_M`$.

**Coverage and induction.** Choosing a smallest coordinate and setting $`z=Mx_M`$, $`\mu_i=x_i-x_M`$ maps every nonnegative point into the displayed substitution with $`\mu_i,z\ge0`$. The power-sum shift includes all $`M`$ constant terms, hence $`z^j/M^{j-1}`$; no factor of $`M-1`$ is lost. At $`z=0`$, the deficit restricts exactly to $`H_{M-1}`$.

The degree-eight polynomial $`Q_M`$ is divisible by $`z`$. Each remaining degree-eight monomial has at most seven $`\mu`$ variables in its support. Its positive-exponent partition and $`z`$-degree consequently belong to exactly 45 possible types. For $`M\ge8`$ they all fit. Positivity of their coefficients establishes $`Q_M\ge0`$ on the full orthant. Away from the origin the multiplier $`4M^5(\sum\mu_i+z)^2`$ is positive, so it may be cancelled. At the origin both deficits vanish. This yields the stated induction, including boundary cases and tied smallest coordinates.

**Bases and finite steps.** I checked directly that
$`H_2(u,v)=12uv(u^2-3uv+v^2)^2`$. For the $`M=3`$ decomposition, the factor $`u^2-uv+v^2=(u-v)^2+uv`$ is nonnegative and the elevated expression $`(u+v+w)^4E`$ has 49 nonzero monomials, all positive, with minimum coefficient 81. At the origin $`E=0`$; elsewhere the elevation factor is positive. Symmetry and the smallest-coordinate substitution cover the complete orthant.

I independently expanded the next four induction differences in multivariate rational polynomial rings:

| $`M`$ | elevation | nonzero monomials | coefficient types | minimum coefficient |
|---:|---:|---:|---:|---:|
| 4 | 8 | 560 | 123 | $`51/256`$ |
| 5 | 5 | 1001 | 94 | $`1146/3125`$ |
| 6 | 3 | 1287 | 60 | $`35/72`$ |
| 7 | 3 | 3003 | 64 | $`9606/16807`$ |

Every coefficient is positive and every monomial has positive $`z`$-degree. These independently establish the start $`H_7\ge0`$; applying the uniform step for $`M=8,9,\ldots`$ completes every $`d\ge1`$.

## Independent uniform expansion and fresh reproductions

[My fresh script](641-independent-checks/independent_checks.py) imports no supplied verifier functions and uses no power-sum coefficient recursion. It directly expands with seven explicit $`\mu`$ variables and symbolic $`M`$. Clearing denominators with $`y_i=M\mu_i+z`$ gives

```math
\widehat p_j=\sum_{i=1}^{7}(M\mu_i+z)^j+(M-7)z^j.
```

The second term accounts for every additional shifted coordinate whose $`\mu`$ is set to zero, including the distinguished final coordinate. It constructs

```math
Q_M=\frac4M(\sum\mu_i+z)^2
       [\,\widehat H_M-M^6H_7(\mu)\,]
```

by exact polynomial division by $`M`$. Restricting unused $`\mu`$'s to zero does not alter any coefficient supported on the explicit variables. Since every possible support has size at most seven, this is exhaustive for arbitrary $`M\ge8`$.

The expansion contains all 3,432 degree-eight $`\mu,z`$ monomials with positive $`z`$-degree. Their 45 symmetry types agree exactly with the supplied certificate **as polynomials in $`M`$**. A separate binomial transform computes the coefficients after $`M=u+8`$; all are strictly positive and agree with the stored shifted arrays. This challenges the dimension-uniform part independently of the submitter's recursion and finite $`M=8`$ crosscheck. [The independently derived symbolic certificate](641-independent-checks/independent-symbolic-certificate.json) is saved separately.

Runtime: bundled Python **3.12.14**, isolated SymPy **1.14.0**. The executable is
`C:\Users\MatthewColbrook\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`;
PYTHONPATH points to the existing cubic-review-deps directory. PYTHONDONTWRITEBYTECODE=1 and TEMP/TMP point inside independent-checks, so review-generated files stay under the snapshot.

[The fresh runner](641-independent-checks/review_runner.py) and [complete reproduction log](641-independent-checks/fresh-reproduction.log) record commands and results. Each supplied script was run in normal Python and with `-O`:

- verify_cubic.py: exit 0, full saved certificate agrees.
- check_printed_table.py: exit 0, all 45 printed polynomials agree exactly.
- crosscheck_cubic.py: exit 0, all 3,432 monomials and 45 types agree at $`M=8`$.
- test_verifier.py: exit 0, both unittest cases pass. Its certificate subtests reject fractional, missing, duplicate, and shifted-array damage in normal and optimized child modes.

My independent audit also passes both normally and with `-O`. I additionally damaged a printed integer in **both** modes; both runs fail with the expected printed-polynomial mismatch. Finally I added $`M-8`$ to a certificate polynomial, a corruption invisible to an $`M=8`$-only comparison. The full symbolic verifier rejects it in both modes with the expected saved-certificate mismatch. These are controlled failures, not proof failures.

Individual fresh logs and the machine-readable [result index](641-independent-checks/fresh-reproduction-results.json) are available under independent-checks. The code's operative checks use explicit exceptions, not optimization-removable assertions.

## Blockers and limits

**Blocking findings: none for the cubic theorem at this head.** The supplied code, printed table, homogeneous identity, base cases, coverage argument, and uniform symbolic induction agree with the independently derived checks.

The audit is a documented independent **AI** audit using exact computer algebra plus explicit mathematical reasoning. It is not a human referee report or a proof-assistant certificate. The three quartic assertions remain outside the proved scope. A full “Solved” claim for the current grouped AIM641 entry would therefore be unsupported by this submission alone.
