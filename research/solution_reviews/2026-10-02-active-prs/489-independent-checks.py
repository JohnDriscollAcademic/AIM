"""Additional exact checks of the pinned Lotka--Volterra certificate.

Usage: python -B 489-independent-checks.py PATH_TO_EXPORTED_PACKAGE
Reads the package without modifying it. The all-column derivative construction
below is separate from the supplied convolution-kernel implementation.
"""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

import numpy as np

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT))
from fourier import exact_jacobian
from dstability import polynomial

A = [[-224, -2551, -1969, 454], [6814, -682, -1358, -11601],
     [7845, -808, -1695, -16707], [328, 3248, 5200, -685]]
Q = 2**46
M, N = 48, 128
ZERO = (0, 0)


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def scaled(a, b):
    return a[0]*b, a[1]*b


def elimination_determinant(matrix):
    """Rational Gaussian elimination, independent of permutation sums."""
    work = [[Fraction(x) for x in row] for row in matrix]
    value = Fraction(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            work[pivot], work[k] = work[k], work[pivot]
            value = -value
        value *= work[k][k]
        for i in range(k+1, len(work)):
            factor = work[i][k] / work[k][k]
            for j in range(k+1, len(work)):
                work[i][j] -= factor * work[k][j]
    return value


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    hashes = json.loads(Path(__file__).with_name('489-input-hashes.json').read_text())
    for name, expected in hashes.items():
        content = (ROOT/name).read_bytes()
        # The verifier rewrites its two output JSON files in native text mode.
        # Normalize only their platform line endings when checking the pinned
        # mathematical output. Certificate and implementation inputs stay exact.
        if name in ('fourier_bounds.json', 'positivity_bounds.json'):
            content = content.replace(b'\r\n', b'\n')
        assert hashlib.sha256(content).hexdigest() == expected, name
    print(f'PASS: all {len(hashes)} pinned files match (two regenerated JSON outputs use LF-normalized hashes).', flush=True)

    minors, _ = polynomial()
    for size in range(1, 5):
        for indices in combinations(range(4), size):
            value = elimination_determinant([[-A[i][j] for j in indices] for i in indices]) / 1000**size
            assert value == minors[indices] and value > 0
    print('PASS: all 15 principal minors independently reproduced by rational elimination.', flush=True)

    atoms = json.loads((ROOT/'dstability_certificate.json').read_text())['atoms']
    rows = [line for line in (ROOT/'PROOF.md').read_text(encoding='utf-8').splitlines()
            if re.match(r'^\| [0-9]{4} \|', line)]
    assert len(rows) == len(atoms) == 21
    for line, atom in zip(rows, atoms):
        fields = [x.strip() for x in line.strip('|').split('|')]
        for key, field in zip(('u', 'v', 'w'), fields[:3]):
            assert list(map(int, field)) == atom[key]
        for key, field in zip(('a', 'b', 'c'), fields[3:]):
            assert Fraction(field) == Fraction(atom[key])
    print('PASS: all 21 printed AM--GM atoms equal the machine certificate.', flush=True)

    anchor = [dict() for _ in range(4)]
    with (ROOT/'anchor_coefficients.csv').open(newline='') as stream:
        for row in csv.DictReader(stream):
            i, k = int(row['species'])-1, int(row['mode'])
            assert int(row['denominator']) == Q
            real, imag = int(row['real_numerator']), int(row['imaginary_numerator'])
            anchor[i][k] = real, imag
            if k:
                anchor[i][-k] = real, -imag
            else:
                assert imag == 0
    linear = [{k: (sum(A[i][j]*anchor[j][k][0] for j in range(4)),
                    sum(A[i][j]*anchor[j][k][1] for j in range(4)))
               for k in range(-M, M+1)} for i in range(4)]
    with np.load(ROOT/'fourier_certificate.npz', allow_pickle=False) as data:
        assert np.array_equal(data['Aint'], np.array(A))
        integers = data['coeffints'].copy()
    omega = int(integers[0])
    jacobian, _, _ = exact_jacobian(np.array(A, dtype=np.int64), integers, Q, M, N, M)
    n = 1 + 4*(2*N+1)
    assert jacobian.shape == (n, n+8*M)

    # Differentiate the scalar quadratic equations one basis vector at a time,
    # using signed mode dictionaries and literal polynomial products.
    directions = [(0, None, 0, 0)]
    for species in range(4):
        offset = 1+species*(2*N+1)
        directions.append((offset, species, 0, 0))
        for k in range(1, N+M+1):
            col = (offset+2*k-1 if k <= N else n+2*species*M+2*(k-N)-2)
            directions.extend([(col, species, k, 0), (col+1, species, k, 1)])
    assert sorted(col for col, *_ in directions) == list(range(n+8*M))
    for col, species, ell, imaginary in directions:
        output = [0]*n
        if species is None:
            for i in range(4):
                offset = 1+i*(2*N+1)
                for k in range(1, N+1):
                    real, imag = anchor[i].get(k, ZERO)
                    output[offset+2*k-1] = -1000*k*imag
                    output[offset+2*k] = 1000*k*real
        else:
            direction = {ell: (0, 1) if imaginary else (1, 0)}
            if ell:
                direction[-ell] = (0, -1) if imaginary else (1, 0)
            if species == 0 and ell == 1 and imaginary:
                output[0] = 1000*Q
            for i in range(4):
                offset = 1+i*(2*N+1)
                for k in range(N+1):
                    val = scaled(direction.get(k, ZERO), -Q*A[i][species])
                    for mode, coefficient in direction.items():
                        val = plus(val, scaled(times(anchor[i].get(k-mode, ZERO), coefficient), -A[i][species]))
                        if i == species:
                            val = plus(val, scaled(times(coefficient, linear[i].get(k-mode, ZERO)), -1))
                    if i == species:
                        real, imag = direction.get(k, ZERO)
                        val = plus(val, (-1000*k*omega*imag, 1000*k*omega*real))
                    if k == 0:
                        assert val[1] == 0
                        output[offset] = val[0]
                    else:
                        output[offset+2*k-1], output[offset+2*k] = val
        assert np.array_equal(jacobian[:, col].astype(object), np.array(output, dtype=object)), col
    print(f'PASS: all {jacobian.size} Jacobian entries agree with a separate basis-vector reconstruction.', flush=True)
    print(f'PASS: storage bound max|J|={max(abs(int(v)) for v in jacobian.flat)} < 2**63.', flush=True)
    print('No new obstruction found; these finite checks supplement the separately audited infinite-tail proof.', flush=True)


if __name__ == '__main__':
    main()
