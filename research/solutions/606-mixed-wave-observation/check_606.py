#!/usr/bin/env python3
"""Numerical diagnostics for AIM 606. These checks are not a proof.

Run with Python 3, numpy and scipy:
    python check_606.py --output results.json
The test includes finite meshwise random potential arrays: these exercise the
algebraic estimates, and are not asserted to be samples of one fixed function.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.special import gammaln


def matrices(values):
    values = np.asarray(values)
    n = len(values)
    h = 1.0 / (n + 1)
    eye = np.eye(n)
    off = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    mass = h * (2 * eye + off) / 4
    stiffness = (2 * eye - off) / h
    full = stiffness + h * np.diag(values)
    squared, phi = eigh(full, mass)
    return h, mass, stiffness, full, np.sqrt(squared), phi


def potential(name, n):
    x = np.arange(1, n + 1) / (n + 1)
    if name == "zero":
        return np.zeros(n), 0.0
    if name == "constant_9":
        return np.full(n, 9.0), 9.0
    if name == "smooth":
        return 4 + 3 * np.sin(5 * np.pi * x) ** 2, 7.0
    if name == "step":
        return 25.0 * (x < 0.37), 25.0
    if name == "oscillatory":
        return 12.0 * (np.sin(1 / (x + 1e-5)) > 0), 12.0
    if name == "meshwise_random":
        return np.random.default_rng(60600 + n).uniform(0, 40, n), 40.0
    raise ValueError(name)


def integral_kernel(nu, time):
    differences = nu[None, :] - nu[:, None]
    # Integral_0^T exp(i delta t) dt, including its removable singularity.
    return time * np.sinc(differences * time / (2 * np.pi)) * np.exp(
        0.5j * differences * time
    )


def observation_gram(h, freq, phi, time):
    # Unit-energy coordinates: U=sum b_j phi_j/(sqrt(2)*lambda_j)
    # exp(+-i lambda_j t). Then E=sum |b_j|^2, exactly.
    q = phi[0, :] / (h * freq)
    r = phi[0, :] / 2
    nu = np.concatenate((-freq[::-1], freq))
    q_signed = np.concatenate((q[::-1], q))
    r_signed = np.concatenate((-r[::-1], r))
    gram = 0.5 * (
        np.outer(q_signed, q_signed) + np.outer(r_signed, r_signed)
    ) * integral_kernel(nu, time)
    return gram, nu, q_signed, r_signed


def spectral_checks():
    rows = []
    for name in ["zero", "constant_9", "smooth", "step", "oscillatory", "meshwise_random"]:
        for n in [1, 3, 7, 15, 31, 63, 127, 255]:
            values, bound = potential(name, n)
            h, mass, stiff, full, lam, phi = matrices(values)
            j = np.arange(1, n + 1)
            omega = 2 / h * np.tan(np.pi * j * h / 2)
            upper = np.sqrt((1 + bound * h * h / 4) * omega**2 + bound)
            q = phi[0] / (h * lam)
            r = phi[0] / 2
            scale = max(1, float(lam[-1]))
            lower_error = float(np.min(lam - omega))
            upper_error = float(np.min(upper - lam))
            tol = 2e-8 * scale
            assert lower_error >= -tol, (name, n, "lower sandwich", lower_error)
            assert upper_error >= -tol, (name, n, "upper sandwich", upper_error)
            identity_error = float(np.max(np.abs(h * np.eye(n) - mass - h*h*stiff/4)))
            ortho_error = float(np.max(np.abs(phi.T @ mass @ phi - np.eye(n))))
            assert ortho_error < 5e-9, (name, n, ortho_error)
            row = {
                "potential": name, "N": n, "A": bound,
                "mass_stiffness_identity_max_error": identity_error,
                "M_orthonormality_max_error": ortho_error,
                "sandwich_lower_min_margin": lower_error,
                "sandwich_upper_min_margin": upper_error,
                "q2_plus_r2_min": float(np.min(q*q+r*r)),
                "q2_plus_r2_max": float(np.max(q*q+r*r)),
            }
            if n > 1:
                tail_lower = np.pi - bound / (2*np.pi*j[:-1]) - bound**2*h*h/(64*np.pi)
                margin = float(np.min(np.diff(lam)-tail_lower))
                assert margin >= -tol, (name, n, "gap", margin)
                row["derived_gap_bound_min_margin"] = margin
                row["actual_positive_frequency_min_gap"] = float(np.min(np.diff(lam)))
            rows.append(row)
    return rows


def gram_checks():
    rows = []
    for name in ["zero", "smooth", "step", "oscillatory"]:
        for n in [7, 15, 31, 63, 127]:
            values, _ = potential(name, n)
            h, _, _, _, lam, phi = matrices(values)
            for time in [1.0, 1.5, 1.9, 2.1, 2.5, 3.0]:
                gram, _, _, _ = observation_gram(h, lam, phi, time)
                smallest = float(eigh(gram, subset_by_index=[0, 0], eigvals_only=True)[0])
                rows.append({"potential": name, "N": n, "T": time,
                             "minimum_O_over_E": smallest,
                             "interpretation": "Negative values near machine epsilon are roundoff."})
    return rows


def normalization_check():
    n, time = 7, 1.7
    vals, _ = potential("smooth", n)
    h, mass, _, full, lam, phi = matrices(vals)
    gram, nu, q, r = observation_gram(h, lam, phi, time)
    rng = np.random.default_rng(606)
    b = rng.normal(size=2*n) + 1j*rng.normal(size=2*n)
    basis = np.concatenate((phi[:, ::-1] / lam[::-1], phi / lam), axis=1) / np.sqrt(2)
    u0, v0 = basis @ b, basis @ (1j*nu*b)
    energy_direct = float(np.real(np.vdot(u0, full @ u0) + np.vdot(v0, mass @ v0)))
    energy_coeff = float(np.vdot(b, b).real)
    obs_gram = float(np.vdot(b, gram @ b).real)
    t = np.linspace(0, time, 200001)
    exp = np.exp(1j*np.outer(t, nu))
    # Compute the actual boundary values from the physical modal basis.
    boundary = exp @ (basis[0]*b/h)
    boundary_dot = exp @ (basis[0]*1j*nu*b/2)
    obs_quadrature = float(np.trapezoid(abs(boundary)**2 + abs(boundary_dot)**2, t))
    assert abs(energy_direct-energy_coeff) < 1e-9 * energy_coeff
    assert abs(obs_gram-obs_quadrature) < 1e-7 * obs_gram
    return {"N": n, "T": time, "energy_direct": energy_direct,
            "energy_coefficients": energy_coeff, "observation_analytic_gram": obs_gram,
            "observation_dense_trapezoid": obs_quadrature,
            "relative_observation_discrepancy": abs(obs_gram-obs_quadrature)/obs_gram}


def wave_packet_checks():
    # Moderate computational samples: the proof uses J=m^2, N=m^6 instead.
    # Finite checks use J=m^2 and N=max(511, 20*(J+m)) to keep dense eigh modest.
    rows = []
    for name in ["zero", "step"]:
        for m in [2, 3, 4, 5, 6]:
            start = m*m
            n = max(511, 20*(start+m))
            time = 1.0
            t0 = (time+2)/2
            ell = np.arange(m+1)
            logchoose = gammaln(m+1)-gammaln(ell+1)-gammaln(m-ell+1)
            lognorm = 0.5*(gammaln(2*m+1)-2*gammaln(m+1))
            coeff = np.exp(logchoose-lognorm-1j*np.pi*t0*ell)
            vals, bound = potential(name, n)
            h, _, _, _, lam_all, phi = matrices(vals)
            index = start-1+ell
            lam = lam_all[index]
            q = phi[0, index]/(h*lam)
            first = integral_kernel(lam, time)
            second = h*h/4 * np.outer(lam, lam) * first
            observed = float(np.real(np.vdot(coeff, (first+second) @ coeff)))
            energy = float(2*np.sum(abs(coeff)**2 / q**2))
            ideal = float(np.real(np.vdot(coeff, integral_kernel(np.pi*ell, time) @ coeff)))
            rows.append({"potential": name, "m": m, "J": start, "N": n,
                         "T": time, "coefficient_l2_squared": float(np.vdot(coeff, coeff).real),
                         "max_frequency_defect": float(np.max(abs(lam-np.pi*(start+ell)))),
                         "ideal_packet_observation": ideal,
                         "actual_O": observed, "actual_E": energy,
                         "O_over_E": observed/energy})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    report = {
        "purpose": "Finite numerical diagnostics only; no certification of the all-mesh theorem.",
        "numpy": np.__version__, "scipy": scipy.__version__,
        "spectral_checks": spectral_checks(),
        "normalization_check": normalization_check(),
        "gram_diagnostics": gram_checks(),
        "wave_packet_diagnostics": wave_packet_checks(),
    }
    Path(args.output).write_text(json.dumps(report, indent=2)+"\n")
    print(f"PASS: {len(report['spectral_checks'])} spectral cases; modal/Gram normalization checked.")
    print(f"Computed {len(report['gram_diagnostics'])} full-observation Gram minima and "
          f"{len(report['wave_packet_diagnostics'])} packet diagnostics.")
    print(f"Results: {args.output}")


if __name__ == "__main__":
    main()
