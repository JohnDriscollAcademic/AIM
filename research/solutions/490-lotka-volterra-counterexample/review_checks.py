"""Supplementary exact checks written during the independent AI review.

Reconstruct the Fourier polynomial from the CSV, evaluate the ODE by direct
Python-integer sums, and check the supplied Jacobian using the exact central
difference identity for a quadratic polynomial. These finite cross-checks
support the analytic review; they do not replace the infinite-tail estimates.
"""

import csv
from pathlib import Path
import subprocess
import sys

import numpy as np

from fourier import AINT, exact_jacobian, exact_residual

ROOT = Path(__file__).resolve().parent


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    return (left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def scale(value, factor):
    return value[0] * factor, value[1] * factor


def complete_modes(positive):
    modes = []
    for species in positive:
        full = dict(species)
        for k, (real, imaginary) in species.items():
            if k:
                full[-k] = (real, -imaginary)
            else:
                assert imaginary == 0
        modes.append(full)
    return modes


def direct_equations(omega, modes, cutoff, denominator):
    """Return numerators of the phase and ODE equations over 1000*Q**2."""
    support = sorted(set().union(*(species.keys() for species in modes)))
    linear = [dict() for _ in range(4)]
    for i in range(4):
        for k in support:
            value = (0, 0)
            for j in range(4):
                value = add(value, scale(modes[j].get(k, (0, 0)), int(AINT[i, j])))
            linear[i][k] = value
    result = [modes[0][1][1] * 1000 * denominator]
    for i in range(4):
        for k in range(cutoff + 1):
            quadratic = (0, 0)
            for ell, coefficient in modes[i].items():
                quadratic = add(quadratic, multiply(
                    coefficient, linear[i].get(k - ell, (0, 0))))
            real, imaginary = modes[i].get(k, (0, 0))
            equation = scale((-imaginary, real), 1000 * k * omega)
            equation = add(equation, scale(linear[i].get(k, (0, 0)), -denominator))
            equation = add(equation, scale(quadratic, -1))
            result.append(equation[0])
            if k:
                result.append(equation[1])
            else:
                assert equation[1] == 0
    return np.array(result, dtype=object)


def main():
    if not __debug__:
        raise RuntimeError("Do not run exact review checks with Python -O.")
    with np.load(ROOT / "fourier_certificate.npz", allow_pickle=False) as data:
        degree, cutoff = int(data["M"]), int(data["N"])
        denominator = 2 ** int(data["den_exp"])
        integers = data["coeffints"].copy()
    assert degree == 48 and cutoff == 128 and denominator == 2**46
    anchor = [dict() for _ in range(4)]
    with (ROOT / "anchor_coefficients.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 4 * (degree + 1)
    for row in rows:
        species, k = int(row["species"]) - 1, int(row["mode"])
        assert 0 <= species < 4 and 0 <= k <= degree
        assert int(row["denominator"]) == denominator and k not in anchor[species]
        pair = int(row["real_numerator"]), int(row["imaginary_numerator"])
        offset = 1 + species * (2 * degree + 1)
        expected = ((int(integers[offset]), 0) if k == 0 else
                    (int(integers[offset + 2*k - 1]), int(integers[offset + 2*k])))
        assert pair == expected
        anchor[species][k] = pair
    print("PASS: all 196 CSV coefficient pairs agree exactly with the NPZ certificate.", flush=True)

    omega = int(integers[0])
    direct = direct_equations(omega, complete_modes(anchor), cutoff, denominator)
    reference = exact_residual(AINT, integers, denominator, degree, cutoff)
    assert np.array_equal(direct, reference)
    print("PASS: all 1029 residual coordinates agree with independent direct integer sums.", flush=True)

    jacobian, _, _ = exact_jacobian(AINT, integers, denominator, degree, cutoff, degree)
    high = cutoff + degree
    for trial in range(3):
        delta_omega = (3, -2, 0)[trial]
        direction = [dict() for _ in range(4)]
        finite, tail = [delta_omega], []
        for species in range(4):
            for k in range(high + 1):
                real = ((species + 2) * (k + 3) + trial) % 7 - 3
                imaginary = 0 if k == 0 else ((species + 3) * (k + 2) + trial) % 5 - 2
                if trial == 2 and k <= cutoff:
                    real = imaginary = 0
                direction[species][k] = (real, imaginary)
                output = finite if k <= cutoff else tail
                output.append(real)
                if k:
                    output.append(imaginary)
        vector = np.array(finite + tail, dtype=object)
        values = []
        for sign in (1, -1):
            shifted = [{k: add(anchor[i].get(k, (0, 0)), scale(direction[i][k], sign))
                        for k in range(high + 1)} for i in range(4)]
            values.append(direct_equations(
                omega + sign * delta_omega, complete_modes(shifted), cutoff, denominator))
        assert np.array_equal(values[0] - values[1], 2 * (jacobian.astype(object) @ vector))
    print("PASS: three exact quadratic central-difference identities, including tail-only input.", flush=True)

    rejected = subprocess.run([sys.executable, "-O", str(ROOT / "verify.py")],
                              capture_output=True, text=True)
    assert rejected.returncode != 0 and "Do not run this verifier with Python -O." in rejected.stderr
    print("PASS: the main verifier rejects disabled assertions (Python -O).", flush=True)


if __name__ == "__main__":
    main()
