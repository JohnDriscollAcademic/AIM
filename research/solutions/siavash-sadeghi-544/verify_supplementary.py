#!/usr/bin/env python3
"""Supplementary exact checks for the original AIM 544 solution package.

Checks the machine-readable witness, off-diagonal persistence bars, rational
matching against exhaustive bijections, and finite diameter-bar examples.
Reuses verify_boundary.py; this is not a third independent implementation.
Python standard library only. Run from any directory, optionally with:
    python verify_supplementary.py --output supplementary_results.json
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import permutations
import importlib.util
import json
from pathlib import Path
import platform
import random
import sys

sys.dont_write_bytecode = True

SOURCE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("aim544_boundary", SOURCE / "verify_boundary.py")
if spec is None or spec.loader is None:
    raise ImportError("cannot load the accompanying verify_boundary.py")
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)


def run() -> dict:
    checks = 0

    def equal(actual, expected, label):
        nonlocal checks
        if actual != expected:
            raise AssertionError(f"{label}: {actual!r} != {expected!r}")
        checks += 1

    def require(condition, label):
        equal(bool(condition), True, label)

    # The original two verifiers construct their witnesses internally.
    # Check the accompanying JSON witness directly against their construction.
    witness = json.loads((SOURCE / "counterexample.json").read_text(encoding="utf-8"))
    equal(witness["problem"], 544, "original problem identity")
    equal(witness["degree"], 1, "witness degree")
    equal(witness["vertex_labels"], [1, 2, 3, 4], "original labels")
    equal(witness["XY_common_set"], [1, 2, 3, 4, 5], "witness common set")
    equal(witness["target_commit"], "aa776a01d7d48a79f93251af11fde9454b0aea95", "original target commit")
    spaces = [tuple(map(tuple, witness[name])) for name in ("X", "Y", "Z")]
    equal(tuple(spaces), boundary.family(1), "JSON matrices equal family at degree one")
    px = boundary.pullback(spaces[0], [i - 1 for i in witness["XY_map_to_X"]])
    py = boundary.pullback(spaces[1], [i - 1 for i in witness["XY_map_to_Y"]])
    for p in (0, 2, 3, 5, 7):
        originals = []
        for name, space in zip(("X", "Y", "Z"), spaces):
            boundary.validate_metric(space)
            bars = boundary.verbose_barcode(space, 1, p)
            equal(bars, tuple(map(tuple, witness["native_barcodes"][name])), f"JSON {name}, field {p}")
            originals.append(bars)
        pullbacks = [boundary.verbose_barcode(space, 1, p) for space in (px, py)]
        for bars in pullbacks:
            equal(bars, tuple(map(tuple, witness["XY_pullback_barcodes"])), f"JSON pullback, field {p}")
        equal(boundary.bottleneck(*pullbacks), witness["distances"]["D_1(X,Y)"], "XY explicit upper bound")
        equal(boundary.bottleneck(originals[1], originals[2]), witness["distances"]["D_1(Y,Z)"], "YZ explicit upper bound")
        equal(boundary.bottleneck(originals[0], originals[2]), witness["distances"]["D_1(X,Z)"], "XZ explicit upper bound")

    # A metric square has a nonzero-length degree-one bar, extending coverage
    # beyond the ultrametric examples whose bars all have zero length.
    square = ((0, 1, 2, 1), (1, 0, 1, 2), (2, 1, 0, 1), (1, 2, 1, 0))
    for scale in (1, Fraction(2, 3)):
        scaled = tuple(tuple(scale * value for value in row) for row in square)
        boundary.validate_metric(scaled)
        for p in (0, 2, 3, 5, 7):
            for tie in (None, 544):
                equal(boundary.verbose_barcode(scaled, 1, p, tie),
                      ((scale, 2 * scale), (2 * scale, 2 * scale), (2 * scale, 2 * scale)),
                      f"off-diagonal square, scale={scale}, field={p}, tie={tie}")

    # Compare exact matching to exhaustive bijections on rational endpoints.
    rng = random.Random(544)
    for size in range(1, 7):
        for case in range(10):
            def sample():
                bars = []
                for _ in range(size):
                    birth = Fraction(rng.randrange(7), 3)
                    death = birth + Fraction(rng.randrange(7), 3)
                    bars.append((birth, death))
                return tuple(bars)
            a, b = sample(), sample()
            brute = min(max(max(abs(x[0] - y[0]), abs(x[1] - y[1]))
                                for x, y in zip(a, perm)) for perm in permutations(b))
            equal(boundary.bottleneck(a, b), brute, f"rational matching size={size}, case={case}")

    # Exercise the ancillary diameter-bar claim on deterministic finite
    # metrics and their pseudometric pullbacks. This remains a finite check.
    for size in range(3, 7):
        for case in range(5):
            d = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(i):
                    d[i][j] = d[j][i] = rng.randrange(1, 8)
            for t in range(size):
                for i in range(size):
                    for j in range(size):
                        d[i][j] = min(d[i][j], d[i][t] + d[t][j])
            d = tuple(map(tuple, d))
            boundary.validate_metric(d)
            degree = size - 2
            diameter = max(map(max, d))
            enlarged = boundary.expand(d, [2 if i < 2 else 1 for i in range(size)])
            for p in (0, 2, 3):
                equal(boundary.verbose_barcode(d, degree, p), ((diameter, diameter),),
                      f"one original diameter bar, n={size}, case={case}, field={p}")
                require((diameter, diameter) in boundary.verbose_barcode(enlarged, degree, p),
                        f"pullback diameter bar, n={size}, case={case}, field={p}")

    return {
        "status": "PASS",
        "checks_passed": checks,
        "fields": ["Q", "F_2", "F_3", "F_5", "F_7"],
        "rational_matching_pairs": 60,
        "diameter_example_metrics": 20,
        "python": sys.version,
        "platform": platform.platform(),
        "scope": "Supplementary finite checks using verify_boundary.py, not an independent persistence implementation or proof of the unrestricted claims.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write complete JSON results")
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {result['checks_passed']} supplementary checks")


if __name__ == "__main__":
    main()
