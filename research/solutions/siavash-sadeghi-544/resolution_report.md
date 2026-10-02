# Proposed resolution report: AIM 544

**Contributor and submitter:** Siavash Sadeghi.

**Target identity:** original AIM 544 at `aa776a01d7d48a79f93251af11fde9454b0aea95`,
now [AIM 534](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/534-verbose-persistence-pullback-triangle.md) at `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.
The statement changed only in its numbered heading. Package filenames retain
the original ID to preserve the supplied revision reference.

**Proof:** [PDF](aim544_counterexample.pdf), [editable source](aim544_counterexample.tex).

**Target:** Triangle inequality for the pullback distance of verbose
persistence barcodes.

**Pinned revision:** `aa776a01d7d48a79f93251af11fde9454b0aea95`.

**Proposed resolution:** the universal statement is false. Three four-point
ultrametrics X,Y,Z satisfy D_1(X,Y)=0, D_1(Y,Z)=0, D_1(X,Z)=1. The same pattern
occurs over every field and in every degree k>=1 on k+3 points per space.

**Evidence classification:** Solution claimed, pending independent mathematical
review. The supplied argument and programs are AI-generated. Codex and separate
AI reviewers examined the complete argument, programs, primary source, and
repository records during submission preparation. No human peer review or
formal proof-assistant verification is claimed. The scope and results are
documented in [verification_record.md](verification_record.md).

## Exact target comparison

| Target requirement | How the proof meets it |
|---|---|
| A specified field and positive degree | F_2 and k=1 suffice; the proof covers every field and k>=1. |
| Finite nonempty metric spaces | Three explicit genuine four-point ultrametrics with positive off-diagonal distances. |
| Diameter-entry Vietoris–Rips filtration | Every simplex enters at its diameter; thresholds are 0, 1, 2. |
| All zero-length persistence pairs retained | Every displayed barcode is verbose; diagonal pairs are never discarded. |
| Arbitrary finite common sets and surjections | Explicit common-set witnesses give both zero distances and the upper bound 1. |
| Infimum over every pullback, not selected witnesses | Every X pullback has at least one (1,1) bar, by an exact fiber-size formula. |
| Multiplicities and zero-distance vertices retained | Distinct duplicates remain separate vertices; simplex ranks count their pairs. |
| No free matching to added diagonals | Every matched point is an actual barcode entry. |
| Strict violation of the desired inequality | 1 > 0 + 0. |

## Uniform lower bound

For any common set S surjecting onto X, let a,b,c,d >=1 be the fiber sizes,
with a,b,c over its three-point close cluster. Its multiplicity of (1,1) is

`choose(a+b+c-1,2) - choose(a-1,2) - choose(b-1,2) - choose(c-1,2)`

`= a*b + a*c + b*c - 2 >= 1`.

Every pullback of the equilateral distance-2 space Z has only (0,0) and (2,2)
pairs in positive degree. Thus every admissible matching costs at least 1.
A matching between the original four-point barcodes attains 1.

This exact argument addresses the unbounded pullback-size quantifier; no
finite computation is used as a substitute for it.

## Prior work

The X,Y pair and its zero distance already occur in Mémoli–Zhou, Example 5.10.
No novelty is claimed for this pair. Adding the equilateral third space and
proving the uniform lower bound completes the proposed fixed-degree
counterexample. This is not the already-known all-degree pullback-
interleaving counterexample.
The distance-2 space Z used here differs from the distance-1 equilateral
space also called Z in that source example.

All degree-one barcodes in the comparison are nonempty, and all three
original spaces have equal cardinality and equal diameter. Thus no empty-
barcode or variable-original-cardinality convention is needed.

## Deliverables and checks

- `aim544_counterexample.pdf` and editable `.tex` source.
- `counterexample.json` with exact matrices, maps and certificate quantities.
- Two separate standard-library implementations and recorded JSON output.
- `target_audit.md` with the inspected status and prior-submission audit scope.
- `verification_record.md` and `SHA256SUMS` for reproduction and provenance.

This report accompanies a package-only pull request under
`research/solutions/siavash-sadeghi-544/`. It proposes no catalogue status change.
Independent mathematical acceptance remains outstanding; a maintainer should
apply the repository evidence rules before assigning a stronger status.
