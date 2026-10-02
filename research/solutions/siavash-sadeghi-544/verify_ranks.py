#!/usr/bin/env python3
"""Separate exact rank-based audit of AIM 544 (does not import verify_boundary).

Builds unfiltered boundary matrices at thresholds 0, 1, 2. Ordinary Gaussian
elimination verifies ranks and vanishing positive homology. Rank increments
therefore count zero-length bars. Includes finite checks of the combinatorial
inequality used for all pullbacks. These checks are not a formal proof.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import platform
import sys
from typing import Sequence

class Audit:
    def __init__(self) -> None:
        self.checks = 0
        self.ranks = 0
    def equal(self, a, b, description: str) -> None:
        if a != b:
            raise AssertionError(f"{description}: {a!r} != {b!r}")
        self.checks += 1
    def require(self, condition: bool, description: str) -> None:
        if not condition:
            raise AssertionError(description)
        self.checks += 1


def binomial(n: int, r: int) -> int:
    return comb(n, r) if n >= r >= 0 else 0


def matrix_from_blocks(blocks: Sequence[Sequence[int]], n: int) -> list[list[int]]:
    labels: dict[int,int] = {}
    for b, members in enumerate(blocks):
        for i in members:
            if i in labels:
                raise ValueError("blocks must be disjoint")
            labels[i] = b
    if set(labels) != set(range(n)):
        raise ValueError("blocks must partition the point set")
    return [[0 if i == j else 1 if labels[i] == labels[j] else 2
             for j in range(n)] for i in range(n)]


def enlarge(d: Sequence[Sequence[int]], extra_vertex: int) -> list[list[int]]:
    labels = list(range(len(d))) + [extra_vertex]
    return [[d[i][j] for j in labels] for i in labels]


def faces_at(d: Sequence[Sequence[int]], size: int, t: int) -> list[tuple[int, ...]]:
    return [face for face in combinations(range(len(d)), size)
            if all(d[a][b] <= t for a,b in combinations(face, 2))]


def boundary(d: Sequence[Sequence[int]], degree: int, t: int) -> list[list[int]]:
    if degree < 1:
        raise ValueError("positive boundary degree required")
    rows = faces_at(d, degree, t)
    cols = faces_at(d, degree+1, t)
    row_index = {face: i for i,face in enumerate(rows)}
    m = [[0] * len(cols) for _ in rows]
    for j, face in enumerate(cols):
        for r in range(len(face)):
            m[row_index[face[:r] + face[r+1:]]][j] = 1 if r % 2 == 0 else -1
    return m


def gaussian_rank(matrix: Sequence[Sequence[int]], p: int) -> int:
    """Dense row elimination; p=0 for Q, otherwise uses prime 3 in this audit."""
    if p not in (0, 3):
        raise ValueError("this separate audit uses Q and F_3")
    if not matrix or not matrix[0]:
        return 0
    a = [[v % p if p else Fraction(v) for v in row] for row in matrix]
    width = len(a[0])
    if any(len(row) != width for row in a):
        raise ValueError("ragged matrix")
    rank = 0
    for column in range(width):
        pivot = next((r for r in range(rank, len(a)) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(int(a[rank][column]), -1, p) if p else 1 / a[rank][column]
        a[rank][column:] = [(value * inverse) % p if p else value * inverse
                            for value in a[rank][column:]]
        for r in range(rank+1, len(a)):
            if not a[r][column]:
                continue
            coefficient = a[r][column]
            for c in range(column, width):
                value = a[r][c] - coefficient * a[rank][c]
                a[r][c] = value % p if p else value
        rank += 1
        if rank == len(a):
            break
    return rank


def run() -> dict:
    audit = Audit()
    records = []
    for degree in range(1, 6):
        n = degree + 3
        x = matrix_from_blocks([list(range(n-1)), [n-1]], n)
        y = matrix_from_blocks([list(range(n-2)), [n-2,n-1]], n)
        z = matrix_from_blocks([[i] for i in range(n)], n)
        px, py = enlarge(x, n-1), enlarge(y, 0)
        for p in (0,3):
            for label, d in (("X",x),("Y",y),("Z",z),("pullback_X",px),("pullback_Y",py)):
                cumulative = []
                for t in (0,1,2):
                    low = gaussian_rank(boundary(d, degree, t), p)
                    high = gaussian_rank(boundary(d, degree+1, t), p)
                    audit.ranks += 2
                    homology = len(faces_at(d, degree+1,t)) - low - high
                    audit.equal(homology, 0, "positive homology at every threshold vanishes")
                    cumulative.append(high)
                increments = [cumulative[0], cumulative[1]-cumulative[0], cumulative[2]-cumulative[1]]
                if label == "X":
                    expected = [0,1,degree+1]
                elif label in ("Y","Z"):
                    expected = [0,0,degree+2]
                else:
                    expected = [0,1,binomial(degree+3,degree+1)-1]
                audit.equal(increments, expected, f"{label}, k={degree}, field={p}: rank increments")
                records.append({"degree": degree, "field": "Q" if p == 0 else "F_3",
                                "space":label, "cumulative_boundary_ranks":cumulative,
                                "diagonal_bar_multiplicities_at_0_1_2":increments})
    # Independently audit the simplex boundary-rank identity used in the proof.
    for n in range(2,9):
        d = [[0] * n for _ in range(n)]
        for degree in range(1,n):
            for p in (0,3):
                rank = gaussian_rank(boundary(d, degree, 0), p)
                audit.ranks += 1
                audit.equal(rank, binomial(n-1,degree), "simplex boundary-rank identity")
    # This is a finite test, not a proof of the all-multiplicity quantifier.
    inequality_instances = 0
    for k in range(1,6):
        for weights in product((1,2,3), repeat=k+2):
            value = binomial(sum(weights)-1,k+1) - sum(binomial(w-1,k+1) for w in weights)
            audit.require(value >= 1, "finite subset-count lower bound")
            if k == 1:
                a,b,c = weights
                audit.equal(value, a*b+a*c+b*c-2, "degree-one polynomial identity")
            inequality_instances += 1
    # Exact formula at the minimum multiplicities for many additional degrees.
    for k in range(1,101):
        weights = [1] * (k+2)
        audit.equal(binomial(sum(weights)-1,k+1)-sum(binomial(w-1,k+1) for w in weights),
                    1, "minimal multiplicities in general degree")
    return {"status":"PASS", "checks_passed":audit.checks,
            "exact_boundary_matrix_ranks":audit.ranks,
            "finite_inequality_instances":inequality_instances,
            "records":records,
            "scope":"Independent implementation of exact finite rank checks, not independent mathematical review or a proof-assistant certificate.",
            "python":sys.version, "platform":platform.platform()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"PASS: {result['checks_passed']} checks; {result['exact_boundary_matrix_ranks']} exact matrix ranks; "
          f"{result['finite_inequality_instances']} finite inequality instances")

if __name__ == "__main__":
    main()
