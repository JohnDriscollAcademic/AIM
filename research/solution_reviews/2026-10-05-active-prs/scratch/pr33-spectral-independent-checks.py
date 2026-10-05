"""Reproduce the fresh PR33 spectral referee's independent Fraction checks.

This preserves the mathematical calculations from the two original inline tool
calls: the seeded core-graph regression and the effective-sign enumeration.
Only function boundaries and a portable JSON-output wrapper have been added.
It does not import or read the submission's check script, source, or snapshot.

Run with ordinary Python (not -O):
    python pr33-spectral-independent-checks.py
Optionally save the same JSON printed to stdout:
    python pr33-spectral-independent-checks.py --output checks.json

These finite regression checks do not prove the spectral or limiting theorems.
"""

import argparse
import json
import platform
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random


def graph_checks():
    rng = Random(11433)

    def sign(x):
        return (x > 0) - (x < 0)

    def edge(z):
        return ((1 - z*z)/(2*z), (1 + z*z)/(2*z))

    checked = 0
    excluded = 0
    for m in [3, 4, 7, 12]:
        for rep in range(250):
            triples = []
            for i in range(m):
                z = [F(rng.choice([j for j in range(-13, 14) if j]),
                       rng.randint(1, 11)) for k in range(3)]
                ec = [edge(t) for t in z]
                x = [e[0] for e in ec]
                c = [e[1] for e in ec]
                a = sum(x)
                p = c[0] + c[1]
                q = c[2]
                if a == 0:
                    break
                triples.append((x, c, a, p, q))
            if len(triples) != m:
                excluded += 1
                continue
            U = sum(p*q/a for x, c, a, p, q in triples)
            T = sum(-x[2] + q*q/a for x, c, a, p, q in triples)
            if U == 0 or T == 0:
                excluded += 1
                continue
            r = -U/T
            Lam = sum(-x[0] - x[1] + p*p/a for x, c, a, p, q in triples)
            g = Lam - U*U/T
            if g == 0 or any(p + r*q == 0 for x, c, a, p, q in triples):
                excluded += 1
                continue
            n = m + 1
            A = [[F(0) for j in range(n)] for i in range(n)]
            Q = F(0)
            hs = F(0)
            neg_a = 0
            for i, (x, c, a, p, q) in enumerate(triples):
                A[i][i] = -a
                A[i][m] = q
                A[m][i] = q
                A[m][m] -= x[2]
                fw = (p + r*q)/a
                assert -a*fw + p + q*r == 0
                Q += sum(sign(t) < 0 for t in [fw*c[0], fw*c[1], fw*r*q])
                h = F(sign(a), 2)*(1 - sign(p + r*q)*
                     (sign(c[0]) + sign(c[1]) + sign(r*q)))
                assert h in [-1, 0, 1]
                hs += h
                neg_a += a < 0
            assert sum(q*((p + r*q)/a) - x[2]*r
                       for x, c, a, p, q in triples) == 0
            assert sum(-x[0] - x[1] + p*((p + r*q)/a)
                       for x, c, a, p, q in triples) == g
            piv = []
            for k in range(n):
                pivot = A[k][k]
                assert pivot != 0
                piv.append(pivot)
                for i in range(k + 1, n):
                    for j in range(k + 1, n):
                        A[i][j] -= A[i][k]*A[k][j]/pivot
            assert piv == [-a for x, c, a, p, q in triples] + [T]
            core_inertia = sum(t > 0 for t in piv)
            surplus = Q - core_inertia
            assert Q - neg_a == m + hs
            assert surplus - F(2*m - 1, 2) == hs - F(sign(T), 2)
            assert surplus.denominator == 1 and 0 <= surplus <= 2*m - 1
            checked += 1
    return {
        "seed": 11433,
        "proposed_samples": 1000,
        "exact_samples_passed": checked,
        "samples_on_excluded_equations": excluded,
        "m_values": [3, 4, 7, 12],
        "checked": "core equations, exact LDL pivots, local sign formula, "
                   "total surplus identity and range",
    }


def sign_variance_checks():
    sgn = lambda x: (x > 0) - (x < 0)
    checked = 0
    for C1, C2, C3, rho in product(
            [F(3, 2), F(2), F(3), F(5)],
            [F(3, 2), F(2), F(3), F(5)],
            [F(3, 2), F(2), F(3), F(5)],
            [F(1, 4), F(1, 2), F(1), F(2), F(4)]):
        if rho*C3 in [abs(C1 - C2), C1 + C2]:
            continue
        total = 0
        for e1, e2, e3 in product([-1, 1], repeat=3):
            c1, c2, c3 = e1*C1, e2*C2, e3*C3
            g = F(1, 2)*(1 - sgn(c1 + c2 + rho*c3)*
                         (sgn(c1) + sgn(c2) + sgn(c3)))
            assert g in [-1, 0, 1]
            total += g*g
        expected = F(1, 4)*(1 + (rho*C3 > C1 + C2) +
                            (rho*C3 < abs(C1 - C2)))
        assert total/8 == expected
        checked += 1
    return {
        "independent_sign_variance_cases_passed": checked,
        "each_sign_patterns": 8,
    }


def main():
    if not __debug__:
        raise SystemExit("Run without -O: the preserved original checks use assert.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also save JSON to this file.")
    args = parser.parse_args()
    result = {
        "status": "passed",
        "execution_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "arithmetic": "fractions.Fraction; exact rational arithmetic",
        "graph": graph_checks(),
        "sign_variance": sign_variance_checks(),
    }
    assert result["graph"]["exact_samples_passed"] == 983
    assert result["graph"]["samples_on_excluded_equations"] == 17
    assert result["sign_variance"]["independent_sign_variance_cases_passed"] == 296
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
