#!/usr/bin/env python3
"""Exact persistence-pairing checks for the proposed AIM 544 counterexample.

Python standard library only. Retains every zero-length persistence pair.
The finite computations support, but do not prove, the universal-over-tripods
lower bound; that bound is proved in aim544_counterexample.pdf.

Example:
    python3 verify_boundary.py --output boundary_results.json
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
import json
from math import comb, inf, isqrt
from pathlib import Path
import platform
import random
import sys
from typing import Any, Iterable, Sequence

Number = int | Fraction
Matrix = tuple[tuple[Number, ...], ...]
Barcode = tuple[tuple[Number, Number], ...]

class Checks:
    def __init__(self) -> None:
        self.count = 0
    def require(self, condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        self.count += 1
    def equal(self, actual: Any, expected: Any, label: str) -> None:
        self.require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def choose(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def validate_field(p: int) -> None:
    if p == 0:
        return
    if p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("field must be 0 (rationals) or a prime")


def validate_metric(d: Matrix, *, pseudo: bool = False) -> None:
    n = len(d)
    if n == 0 or any(len(row) != n for row in d):
        raise ValueError("nonempty square distance matrix required")
    for i in range(n):
        for j in range(n):
            x = d[i][j]
            if not isinstance(x, (int, Fraction)):
                raise TypeError("distances must be exact integers or Fractions")
            if x < 0 or d[i][j] != d[j][i] or (i == j and x != 0):
                raise ValueError("invalid distance matrix")
            if not pseudo and i != j and x == 0:
                raise ValueError("distinct original points must have positive distance")
            for t in range(n):
                if x > d[i][t] + d[t][j]:
                    raise ValueError("triangle inequality fails")


def ultrametric_from_partition(groups: Sequence[int]) -> Matrix:
    return tuple(tuple(0 if i == j else 1 if a == b else 2
                       for j, b in enumerate(groups))
                 for i, a in enumerate(groups))


def family(k: int) -> tuple[Matrix, Matrix, Matrix]:
    if k < 1:
        raise ValueError("positive degree required")
    n = k + 3
    x = ultrametric_from_partition([0] * (k + 2) + [1])
    y = ultrametric_from_partition([0] * (k + 1) + [1, 1])
    z = ultrametric_from_partition(list(range(n)))
    return x, y, z


def pullback(d: Matrix, labels: Sequence[int]) -> Matrix:
    if set(labels) != set(range(len(d))):
        raise ValueError("labels must specify a surjection")
    return tuple(tuple(d[i][j] for j in labels) for i in labels)


def expand(d: Matrix, sizes: Sequence[int]) -> Matrix:
    if len(sizes) != len(d) or any(v < 1 for v in sizes):
        raise ValueError("one positive multiplicity per original point is required")
    return pullback(d, [i for i, v in enumerate(sizes) for _ in range(v)])


def verbose_barcode(d: Matrix, k: int, p: int = 2, tie_seed: int | None = None) -> Barcode:
    """Standard oriented boundary-matrix reduction, including diagonal pairs."""
    validate_field(p)
    if k < 1:
        raise ValueError("this verifier is for positive homological degrees")
    n = len(d)
    simplices = [s for m in range(1, min(n, k + 2) + 1)
                 for s in combinations(range(n), m)]
    entry = {s: max((d[i][j] for i, j in combinations(s, 2)), default=0)
             for s in simplices}
    # Dimension first within each entry time guarantees faces precede cofaces.
    if tie_seed is None:
        simplices.sort(key=lambda s: (entry[s], len(s), s))
    else:
        shuffled = list(simplices)
        random.Random(tie_seed).shuffle(shuffled)
        tie = {s: i for i, s in enumerate(shuffled)}
        simplices.sort(key=lambda s: (entry[s], len(s), tie[s]))
    indices = {s: j for j, s in enumerate(simplices)}
    pivot_columns: dict[int, dict[int, Number]] = {}
    zero_column: list[bool] = []
    pairs: list[tuple[Number, Number]] = []
    for j, s in enumerate(simplices):
        col: dict[int, Number] = {}
        if len(s) > 1:
            for r in range(len(s)):
                face = s[:r] + s[r+1:]
                coefficient = (-1) ** r
                col[indices[face]] = coefficient % p if p else Fraction(coefficient)
        while col:
            low = max(col)
            if low not in pivot_columns:
                if low >= j or not zero_column[low]:
                    raise ArithmeticError("invalid persistence birth pivot")
                pivot_columns[low] = dict(col)
                if len(simplices[low]) == k + 1:
                    pairs.append((entry[simplices[low]], entry[s]))
                break
            previous = pivot_columns[low]
            factor = (int(col[low]) * pow(int(previous[low]), -1, p)) % p if p else col[low] / previous[low]
            for row, value in previous.items():
                result = col.get(row, 0) - factor * value
                if p:
                    result %= p
                if result:
                    col[row] = result
                else:
                    col.pop(row, None)
        zero_column.append(not col)
    return tuple(sorted(pairs))


def bottleneck(a: Barcode, b: Barcode) -> Number | float:
    """Exact matching, with no auxiliary diagonal points (augmenting paths)."""
    if len(a) != len(b):
        return inf
    if not a:
        return 0
    distances = [[max(abs(x[0]-y[0]), abs(x[1]-y[1])) for y in b] for x in a]
    thresholds = sorted({value for row in distances for value in row})
    def feasible(epsilon: Number) -> bool:
        owners = [-1] * len(b)
        def visit(i: int, seen: set[int]) -> bool:
            for j, value in enumerate(distances[i]):
                if value <= epsilon and j not in seen:
                    seen.add(j)
                    if owners[j] == -1 or visit(owners[j], seen):
                        owners[j] = i
                        return True
            return False
        return all(visit(i, set()) for i in range(len(a)))
    lo, hi = 0, len(thresholds) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(thresholds[mid]):
            hi = mid
        else:
            lo = mid + 1
    return thresholds[lo]


def diagonal_matching(a: Barcode, b: Barcode) -> Number:
    if len(a) != len(b) or any(x != y for x, y in a + b):
        raise ValueError("equal-size diagonal barcodes required")
    return max((abs(x[0] - y[0]) for x, y in zip(sorted(a), sorted(b))), default=0)


def positive_compositions(total: int, parts: int) -> Iterable[tuple[int, ...]]:
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in positive_compositions(total - first, parts - 1):
            yield (first,) + tail


def expected_pullback(sizes: Sequence[int], groups: Sequence[int], k: int) -> Barcode:
    at0 = sum(choose(n-1, k+1) for n in sizes)
    cluster_totals = Counter()
    for n, group in zip(sizes, groups):
        cluster_totals[group] += n
    through1 = sum(choose(n-1, k+1) for n in cluster_totals.values())
    total = choose(sum(sizes)-1, k+1)
    return tuple([(0, 0)] * at0 + [(1, 1)] * (through1-at0) + [(2, 2)] * (total-through1))


def describe(barcode: Barcode) -> list[dict[str, Any]]:
    return [{"birth": str(a), "death": str(b), "multiplicity": m}
            for (a, b), m in sorted(Counter(barcode).items())]


def run() -> dict[str, Any]:
    checks = Checks()
    reductions = 0
    fields = (0, 2, 3, 5, 7)
    cases = []
    for k in range(1, 7):
        x, y, z = family(k)
        n = len(x)
        for d in (x, y, z):
            validate_metric(d)
        x_labels = list(range(n)) + [n-1]
        y_labels = list(range(n)) + [0]
        checks.equal(len(set(zip(x_labels, y_labels))), n+1,
                     f"degree {k}: witnesses are also a correspondence")
        px, py = pullback(x, x_labels), pullback(y, y_labels)
        for p in fields:
            for tie in (None, 544 + k):
                bx, by, bz, bpx, bpy = [verbose_barcode(d, k, p, tie) for d in (x,y,z,px,py)]
                reductions += 5
                expected_x = tuple([(1,1)] + [(2,2)] * (k+1))
                expected_yz = tuple([(2,2)] * (k+2))
                expected_p = tuple([(1,1)] + [(2,2)] * (choose(k+3,k+1)-1))
                prefix = f"k={k}, field={p}, tie={tie}"
                checks.equal(bx, expected_x, prefix + " X")
                checks.equal(by, expected_yz, prefix + " Y")
                checks.equal(bz, expected_yz, prefix + " Z")
                checks.equal(bpx, expected_p, prefix + " pullback X")
                checks.equal(bpy, expected_p, prefix + " pullback Y")
                checks.equal(bottleneck(bpx,bpy), 0, prefix + " X-Y witness")
                checks.equal(bottleneck(by,bz), 0, prefix + " Y-Z witness")
                checks.equal(bottleneck(bx,bz), 1, prefix + " X-Z upper bound")
                checks.require(all(b for b in (bx,by,bz,bpx,bpy)), prefix + " nonempty")
            cases.append({"degree": k, "field": "Q" if p == 0 else f"F_{p}",
                          "original_vertices": n, "witness_vertices": n+1,
                          "original_X": describe(bx), "original_Y_and_Z": describe(by),
                          "XY_pullbacks": describe(bpx)})
    # All positive fiber-size vectors for 4 <= |S| <= 8, not just uniform copies.
    finite_comparisons = 0
    exhaustive_by_size = []
    x, _, z = family(1)
    for p in (0, 2, 5):
        for total in range(4, 9):
            vectors = list(positive_compositions(total, 4))
            x_bars, z_bars = [], []
            for sizes in vectors:
                bx = verbose_barcode(expand(x, sizes), 1, p)
                bz = verbose_barcode(expand(z, sizes), 1, p)
                reductions += 2
                checks.equal(bx, expected_pullback(sizes, [0,0,0,1], 1), "exhaustive X formula")
                checks.equal(bz, expected_pullback(sizes, [0,1,2,3], 1), "exhaustive Z formula")
                checks.require((1,1) in bx, "every tested X pullback retains a (1,1) bar")
                checks.require(all(a == b and a in (0,2) for a,b in bz), "Z endpoint restriction")
                x_bars.append(bx)
                z_bars.append(bz)
            minimum = inf
            for a in x_bars:
                for b in z_bars:
                    value = diagonal_matching(a,b)
                    checks.require(value >= 1, "finite pullback X-Z lower bound")
                    finite_comparisons += 1
                    minimum = min(minimum, value)
            checks.equal(minimum, 1, "minimum at every tested common size")
            # Check the sorted diagonal matcher against the general matcher.
            checks.equal(diagonal_matching(x_bars[-1], z_bars[0]), bottleneck(x_bars[-1], z_bars[0]),
                         "two matching implementations agree")
            exhaustive_by_size.append({"field": p, "vertices": total,
                                       "fiber_vectors": len(vectors), "minimum": int(minimum)})
    # General matching independently compared with exhaustive bijections.
    matching_samples = (
        (((1,1),(2,2),(2,2)), ((2,2),(2,2),(2,2))),
        (((0,0),(1,2),(2,2)), ((0,1),(1,1),(2,3))),
        (((1,1),), ((2,2),)),
        ((), ()),
    )
    for a,b in matching_samples:
        brute = min((max((max(abs(x[0]-y[0]), abs(x[1]-y[1]))
                              for x,y in zip(a, perm)), default=0)
                     for perm in permutations(b)), default=0)
        checks.equal(bottleneck(a,b), brute, "matcher versus all bijections")
    checks.equal(bottleneck(((1,1),), ((2,2),)), 1, "zero-length bars cannot be discarded")
    checks.equal(bottleneck((), ((0,0),)), inf, "different barcode sizes are not padded")
    for bad in (-1, 1, 4, 9):
        try:
            validate_field(bad)
        except ValueError:
            checks.require(True, "reject invalid field")
        else:
            checks.require(False, "invalid field accepted")
    try:
        pullback(x, [0,1,2])
    except ValueError:
        checks.require(True, "reject nonsurjective map")
    else:
        checks.require(False, "nonsurjective map accepted")
    return {
        "status": "PASS", "checks_passed": checks.count,
        "exact_persistence_reductions": reductions,
        "finite_pullback_pair_comparisons": finite_comparisons,
        "fields": ["Q", "F_2", "F_3", "F_5", "F_7"],
        "family_degrees_checked": [1,2,3,4,5,6],
        "cases": cases, "finite_exhaustive_checks": exhaustive_by_size,
        "scope": "Finite exact computations only. The proof handles all fields, all positive degrees, and all finite common pullbacks.",
        "python": sys.version, "platform": platform.platform()
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write complete JSON results")
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {result['checks_passed']} checks; {result['exact_persistence_reductions']} exact reductions; "
          f"{result['finite_pullback_pair_comparisons']} finite pullback-pair comparisons")

if __name__ == "__main__":
    main()
