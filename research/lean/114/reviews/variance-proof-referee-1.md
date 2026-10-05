# Independent final proof review 1: actual nodal variance

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of implementer `lean_feasibility`.
- Verdict: **APPROVE** the five advertised results at the hashes below.
- This is a mathematical/source audit and independent local Lean check; expanded isolated Linux verification remains a separate gate.

## Exact source and checks

The three statement-boundary hashes match my preproof approval without changes.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/VarianceDefinitions.lean` | `39448627e15c3dc5b6d0a9c825928abe8f79a6b92fed300cf40313bc9b5ef3aa` |
| `VarianceChallenge.lean` | `6b77c1f2e4debf3ac27f7264ab36ee8431a59c060e3e98ac99824160a21be0b5` |
| `VARIANCE_TARGETS.md` | `a215fb1019cd18812094ad0adac10aef5427e2346af39e9004db38e01cca14fb` |
| `AIM/P114/VarianceProof.lean` | `3a160951c60be915a49a2b9dedb1495e76e6f35007339ab7f30d03901e33e6c2` |

I read the complete proof, definitions, Challenge, and explanation. Independently, I ran `lake build AIM.P114.VarianceProof`, `lake env lean AIM/P114/VarianceProof.lean`, and a fresh import printing axioms for each of the five declarations. All exited zero. The [build](../verification/referee-1-variance-build.log), [re-elaboration](../verification/referee-1-variance-reelaboration.log), and [axiom audit](../verification/referee-1-variance-axioms.log) are separate from the implementer's logs. A successful quiet re-elaboration produces an empty log. Each theorem depends exactly on `propext`, `Classical.choice`, and `Quot.sound`. There is no custom axiom, `sorryAx`, native-execution axiom, or Challenge import in the proof closure.

## Proof assessment

The proof obtains atomlessness of the actual standard Cauchy distribution from its density. To obtain full support, it proves the correct direction of absolute continuity: Lebesgue measure is absolutely continuous with respect to the Cauchy measure, using strict positivity of the density. Thus every nonempty open set has positive Cauchy mass. Product instances apply these facts to the actual triple law.

The explicit triangle witness `((r,r),0)` works for every nonzero r, including arbitrarily small or large r. The strict-complement witness `((0,0),3/abs r)` proves positive complement mass; no event being proper is mistaken for positive complement measure. Finiteness and probability normalization make the real-valued masses legitimate. The resulting strict bounds are exactly those in the frozen statement. At zero the lower strict inequality is impossible, so the event is empty.

The null-boundary proof is substantive. Equal magnitudes imply equal squares, giving at most the two points y and -y. Cauchy atomlessness removes both, and the no-fiber case is handled separately. Product almost-everywhere statements include the required measurability. For nonzero r, each boundary conditioned on the first two coordinates fixes a third-coordinate magnitude. At zero, the proof instead conditions equal first/second magnitudes; the upper boundary is excluded by positive magnitudes. It does not divide by zero or apply the nonzero-r argument at the origin.

For each fixed parameter, off the null boundaries, the event indicator is locally constant as a function of the parameter. The proof handles all four order cases. It then uses dominated continuity with the constant-one integrable bound and identifies the actual indicator integral with event probability. This proves continuity of the original function on the whole real line, rather than a modified version or only a punctured domain.

For the general ratio law rho, no mass at zero gives the strict bounds almost everywhere. Full support and continuity turn almost-everywhere constancy into equality at every point; the values at zero and one contradict that equality. The final theorem applies the independently reviewed actual Gaussian-mixture theorem to precisely this fixed variance function. Its hypotheses concern only rho's intrinsic probability, support, and zero-atom properties. No moment formula, variance regularity, or non-Gaussianity is an input assumption.

## Scope retained

The proof establishes all five frozen statements and discharges the variance-function hypotheses of the mixture theorem. It does not construct the manuscript's stable ratio law, prove these intrinsic conditions for that law, or identify the Gaussian mixture as the spectral graph-surplus limit. Those remaining spectral and probabilistic links are explicitly documented. This approval cannot certify the complete AIM 114 counterexample or settle the universal variance assertion.
