"""Fresh corroborating checks for the independent AIM505 mathematical audit.

This script is not a proof and does not integrate the stiff ODE. It checks
closed-form profile asymptotics and the actual reflected-grid identities.
It uses only Python's standard library and the bundled NumPy.
"""
from __future__ import annotations

import hashlib
import json
from math import acosh, cosh, log, tanh
from pathlib import Path
import platform

import numpy as np

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[3] / "research/solutions/siavash-sadeghi-505/aim505_report.tex"
SCRIPT = ROOT.parents[3] / "research/solutions/siavash-sadeghi-505/check_505.py"


def density_rhs(n, h, gamma):
    """Implement the complete target, using explicit reflected ghost values."""
    p = n ** gamma
    extended_n = np.r_[n[1], n, n[-2]]
    extended_p = extended_n ** gamma
    out = np.empty_like(n)
    for i in range(len(n)):
        right = max(extended_n[i+1], extended_n[i+2]) * (
            extended_p[i+2] - extended_p[i+1])
        left = max(extended_n[i], extended_n[i+1]) * (
            extended_p[i+1] - extended_p[i])
        out[i] = (right-left)/h**2 + n[i]*(1-p[i])
    return out


def pressure_identity_error(n, h, gamma):
    p = n ** gamma
    extended_p = np.r_[p[1], p, p[-2]]
    lhs = density_rhs(n, h, gamma) / n
    rhs = np.empty_like(n)
    for i in range(len(n)):
        pi = extended_p[i+1]
        neighbors = [extended_p[i], extended_p[i+2]]
        laplacian = (sum(neighbors)-2*pi)/h**2
        correction = sum((np.expm1(log(pj/pi)/gamma)*(pj-pi))
                         for pj in neighbors if pj > pi)/h**2
        rhs[i] = laplacian + 1-pi + correction
    return float(np.max(np.abs(lhs-rhs)))


def checks():
    c = tanh(0.5)
    profile_rows = []
    for M in [10, 20, 40, 80, 160, 320, 640, 1280]:
        h, K = 1/M, M//2
        eta = acosh(1+h*h/2)
        P = np.array([1-cosh(eta*i)/cosh(eta*(K+1))
                      for i in range(-K, K+1)])
        ext = np.r_[0.0, P, 0.0]
        residual = (ext[2:]-2*P+ext[:-2])/h**2 + 1-P
        A = (P[-2]-P[-1])*log(P[-2]/P[-1])/h**2
        t = -log(0.75) + log(1+0.5*h*h/(8*P[-1]))
        profile_rows.append({"M": M, "h": h,
            "P_K_over_h": float(P[-1]/h),
            "P_Kminus1_over_P_K": float(P[-2]/P[-1]),
            "edge_slope": float((P[-2]-P[-1])/h),
            "A_h": A, "h_A_h": h*A, "t_h": t,
            "t_h_A_h": t*A,
            "max_linear_profile_residual": float(np.max(np.abs(residual)))})

    rng = np.random.default_rng(50528)
    identity_rows = []
    weighted_rows = []
    symmetry_rows = []
    for M, gamma in [(4, 2), (10, 3), (20, 7), (40, 30)]:
        h = 1/M
        n = rng.uniform(0.2, 0.95, 2*M+1)
        rhs = density_rhs(n, h, gamma)
        reaction = n*(1-n**gamma)
        weights = np.ones_like(n)
        weights[[0, -1]] = 0.5
        weighted_rows.append({"M": M, "gamma": gamma,
            "weighted_diffusion_sum": float(weights @ (rhs-reaction)),
            "unweighted_diffusion_sum": float(np.sum(rhs-reaction))})
        identity_rows.append({"M": M, "gamma": gamma,
            "max_pressure_identity_error": pressure_identity_error(n,h,gamma)})
        half = rng.uniform(0.2,0.95,M+1)
        full = np.r_[half[:0:-1],half]
        p = half**gamma
        face = np.maximum(half[:-1],half[1:])*(p[1:]-p[:-1])/h
        half_rhs = np.r_[2*face[0],face[1:]-face[:-1],-2*face[-1]]/h
        half_rhs += half*(1-p)
        symmetry_rows.append({"M":M,"gamma":gamma,
            "max_halfgrid_fullgrid_error":float(np.max(np.abs(
                half_rhs-density_rhs(full,h,gamma)[M:])))})

    return {"reviewer":"independent_505_pr28 (OpenAI Codex AI)",
        "date":"2026-10-04", "python":platform.python_version(),
        "numpy":np.__version__,
        "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "submitted_script_sha256":hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
        "analytic_limits":{"P_K_over_h":c,"ratio":2.0,
                           "h_A_h":c*log(2)},
        "profile_checks":profile_rows,
        "reflected_weight_checks":weighted_rows,
        "pressure_identity_checks":identity_rows,
        "symmetric_halfgrid_checks":symmetry_rows,
        "limitation":"Floating-point corroboration only; not interval-certified, not ODE integration, not a proof."}


if __name__ == "__main__":
    result = checks()
    output = ROOT / "independent-checks.json"
    output.write_text(json.dumps(result, indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,allow_nan=False))
    print("Wrote",output)
