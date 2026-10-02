# Source provenance

The dependency pins, declaration checker, rejection controls, numerical smoke
certificate and separate Comparator challenge/solution pattern are adapted
from [OpenProblemsInNLA at commit
`e375a6fc0a12df52c4f5a38b53df78b837e1c390`](https://github.com/ajt60gaibb/OpenProblemsInNLA/tree/e375a6fc0a12df52c4f5a38b53df78b837e1c390/lean-statements).

Relevant upstream files are `lakefile.toml`, `lake-manifest.json`,
`lean-toolchain`, `NLA/Statements/Infrastructure.lean`,
`NLA/Statements/KernelSmoke.lean`, `StatementControls.lean`,
`IdentityChallenge.lean`, `IdentitySolution.lean` and `comparator.json`.

This adaptation changes the package name and namespace to AIM, retains only
the generic declaration controls and numerical smoke certificate, and includes
the certificate solution in the default build. It imports no NLA problem
statement, mathematical solution, computational model or review record.

The committed manifest preserves all upstream dependency revisions. Each
dependency retains its own license and attribution. The separately retained
Linux verification harness has its own [notice](../tools/lean/NOTICE.md).
