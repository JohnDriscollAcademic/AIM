#!/usr/bin/env python3
"""Numerical corroboration of the counterexample to AIM catalogue entry 505.

This is NOT the proof. The proof, including the diagonal selection of gamma,
all initial-data bounds, and the reflected-boundary comparison argument, is
in aim505_report.pdf. In particular, the proof does not assert that the default
choice gamma=500*M works for every mesh.

Dependencies: NumPy and SciPy.
Example: python check_505.py --meshes 10 20 40 80 --output ab_experiments.json
"""
from __future__ import annotations
import argparse
import json
from math import acosh, cosh, log
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.sparse import csc_matrix, lil_matrix


def experiment(M: int, gamma: float) -> dict[str, int | float]:
    """Integrate on the symmetric half-grid, including reflected endpoints."""
    if M < 4 or M % 2:
        raise ValueError('M must be an even integer at least four.')
    if not np.isfinite(gamma) or gamma <= 1:
        raise ValueError('gamma must be finite and greater than one.')
    h, K = 1.0/M, M//2
    a, q = 0.75, 0.5
    t0 = -log(a)
    eta = acosh(1+h*h/2)
    P = np.array([1-cosh(eta*i)/cosh(eta*(K+1)) for i in range(K+1)])

    def stationary(p: np.ndarray) -> np.ndarray:
        # The high-gamma root lies close to P and has positive coordinates.
        # Clipping here only guards intermediate root-finder trial vectors.
        safe = np.maximum(p, np.finfo(float).tiny)
        neighbours = np.r_[safe[1], safe, 0.0]
        out = (neighbours[2:]-2*safe+neighbours[:-2])/h**2 + 1-safe
        for other in (neighbours[2:], neighbours[:-2]):
            higher = other > safe
            out[higher] += (
                np.expm1(np.log(other[higher]/safe[higher])/gamma)
                * (other[higher]-safe[higher])/h**2)
        return out

    stationary_result = root(stationary, P, tol=1e-11)
    pg = stationary_result.x
    residual = float(np.max(np.abs(stationary(pg))))
    if not np.all((pg > 0) & (pg < 1)) or residual > 1e-7:
        raise RuntimeError(f'Invalid stationary root: residual={residual:g}; '
                           f'{stationary_result.message}')
    tend = t0 + log(1+q*h*h/(8*P[-1]))
    initial = np.zeros(M+1)
    initial[:K+1] = a*np.exp(np.log(pg)/gamma)

    def powers(n: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        n = np.maximum(n, 0.0)
        # The exact solution lies in [0,1]. The upper exponent guard prevents
        # overflow on nonphysical intermediate Newton iterates of the solver.
        with np.errstate(over='ignore', under='ignore', invalid='ignore'):
            exponent = gamma*np.log(np.maximum(n, 1e-300))
            p = np.where(n > 0, np.exp(np.clip(exponent, -745, 100)), 0.0)
            dp_dn = np.where(n > 0, gamma*p/np.maximum(n, 1e-300), 0.0)
        return n, p, dp_dn

    def rhs(t: float, n: np.ndarray) -> np.ndarray:
        n, p, _ = powers(n)
        flux = np.maximum(n[:-1], n[1:])*(p[1:]-p[:-1])/h
        # Reflection at 0 is symmetry; reflection at M is the specified BC.
        diffusion = np.r_[2*flux[0], flux[1:]-flux[:-1], -2*flux[-1]]/h
        return diffusion+n*(1-p)

    def jacobian(t: float, n: np.ndarray) -> csc_matrix:
        n, p, dp_dn = powers(n)
        da = np.where(n[1:] >= n[:-1],
                      -n[1:]*dp_dn[:-1],
                      p[1:]-p[:-1]-n[:-1]*dp_dn[:-1])/h**2
        db = np.where(n[1:] >= n[:-1],
                      p[1:]-p[:-1]+n[1:]*dp_dn[1:],
                      n[:-1]*dp_dn[1:])/h**2
        matrix = lil_matrix((M+1, M+1))
        for i in range(M):
            left = 2 if i == 0 else 1
            right = 2 if i+1 == M else 1
            matrix[i, i] += left*da[i]
            matrix[i, i+1] += left*db[i]
            matrix[i+1, i] -= right*da[i]
            matrix[i+1, i+1] -= right*db[i]
        for i in range(M+1):
            matrix[i, i] += 1-(gamma+1)*p[i]
        return csc_matrix(matrix)

    start = time.perf_counter()
    sol = solve_ivp(rhs, (0,tend), initial, method='Radau', jac=jacobian,
                    rtol=2e-10, atol=2e-12, max_step=0.003)
    if not sol.success:
        raise RuntimeError(sol.message)
    if not np.all(np.isfinite(sol.y)) or np.min(sol.y) < -1e-9 or np.max(sol.y) > 1+1e-9:
        raise RuntimeError('Accepted trajectory violates the finite [0,1] density bounds.')
    n, p, dp_dn = powers(sol.y[:, -1])
    dp = dp_dn*rhs(tend, n)
    w = (p[K+1]-2*p[K]+p[K-1])/h**2+1-p[K]
    A = log(P[-2]/P[-1])*(P[-2]-P[-1])/h**2
    return {'M':M, 'h':h, 'gamma':gamma, 't':tend,
            'edge_pressure':float(p[K]), 'P':float(P[-1]),
            'n_out':float(n[K+1]), 'gamma_w':float(gamma*w),
            'expected_limit':-A, 'dp_over_p':float(dp[K]/p[K]),
            'gamma_t_minus_w':float(-gamma*tend*w),
            'stationary_residual':residual,
            'seconds':time.perf_counter()-start}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--meshes', nargs='+', type=int, default=[10,20,40,80])
    parser.add_argument('--gamma-multiplier', type=float, default=500.0)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('ab_experiments.json'))
    args = parser.parse_args()
    results = []
    print('  M     gamma          gamma*w             -A_h       -gamma*t*w')
    for M in args.meshes:
        result = experiment(M, args.gamma_multiplier*M)
        results.append(result)
        print(f"{M:3d} {result['gamma']:9.0f} {result['gamma_w']:16.8f} "
              f"{result['expected_limit']:16.8f} {result['gamma_t_minus_w']:16.8f}")
    args.output.write_text(json.dumps(results, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    print('Wrote', args.output)


if __name__ == '__main__':
    main()
