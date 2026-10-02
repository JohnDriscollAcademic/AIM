"""Floating-point Steklov solver for convex polygons (NUMERICAL EVIDENCE ONLY).

Rayleigh-Ritz with harmonic polynomials Re/Im ((z-c)/s)^k, k<=K, on the
boundary of a polygon.  Every Ritz value is an upper bound for the
corresponding Steklov eigenvalue (in exact arithmetic).  Here floating point
is used, so the output is evidence, never proof.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss


def boundary_quadrature(verts, q):
    """Gauss-Legendre nodes on every edge.  Returns points (complex), weights,
    outward unit normals (complex), edge index."""
    verts = np.asarray(verts, dtype=complex)
    n = len(verts)
    # orientation: make counter-clockwise
    area2 = np.sum((verts.real * np.roll(verts.imag, -1)) - (np.roll(verts.real, -1) * verts.imag))
    if area2 < 0:
        verts = verts[::-1]
    x, w = leggauss(q)
    t = (x + 1) / 2
    w = w / 2
    P, W, N, E = [], [], [], []
    for k in range(n):
        a, b = verts[k], verts[(k + 1) % n]
        d = b - a
        L = abs(d)
        nrm = -1j * d / L  # outward normal for ccw orientation
        P.append(a + t * d)
        W.append(w * L)
        N.append(np.full(q, nrm))
        E.append(np.full(q, k))
    return np.concatenate(P), np.concatenate(W), np.concatenate(N), np.concatenate(E)


def harm_basis(z, nrm, c, s, K):
    """Values and normal derivatives of 1, Re w^k, Im w^k (w=(z-c)/s)."""
    w = (z - c) / s
    cols, dcols = [np.ones_like(z.real)], [np.zeros_like(z.real)]
    wp = np.ones_like(w)
    for k in range(1, K + 1):
        dwk = k * wp / s  # derivative of w^k wrt z
        wp = wp * w
        # f = w^k analytic: grad Re f = (Re f', -Im f'), grad Im f = (Im f', Re f')
        # normal derivative of Re f = Re(f' * nrm), of Im f = Im(f' * nrm)
        cols.append(wp.real)
        dcols.append((dwk * nrm).real)
        cols.append(wp.imag)
        dcols.append((dwk * nrm).imag)
    return np.array(cols).T, np.array(dcols).T


def steklov_eigs(verts, K=30, q=None, nev=6, return_vecs=False, tol=1e-13):
    verts = np.asarray(verts, dtype=complex)
    if q is None:
        q = K + 10
    z, w, nrm, eidx = boundary_quadrature(verts, q)
    c = np.mean(verts)
    s = np.max(np.abs(verts - c))
    H, Hn = harm_basis(z, nrm, c, s, K)
    sw = np.sqrt(w)[:, None]
    U, S, Vt = np.linalg.svd(sw * H, full_matrices=False)
    keep = S > tol * S[0]
    U, S, Vt = U[:, keep], S[keep], Vt[keep]
    T = Vt.T / S  # coefficients of orthonormal functions
    Phi = H @ T
    dPhi = Hn @ T
    A = (Phi * w[:, None]).T @ dPhi
    A = 0.5 * (A + A.T)
    ev, V = np.linalg.eigh(A)
    if return_vecs:
        return ev[:nev], (T @ V[:, :nev]), (c, s, K)
    return ev[:nev]


def perimeter(verts):
    v = np.asarray(verts, dtype=complex)
    return np.sum(np.abs(np.roll(v, -1) - v))


def sigma1_per(verts, K=30, **kw):
    ev = steklov_eigs(verts, K=K, **kw)
    return ev[1] * perimeter(verts)


if __name__ == "__main__":
    # validation 1: disk approximated? (harmonic polys exact for disk; use 400-gon)
    th = np.linspace(0, 2 * np.pi, 401)[:-1]
    disk = np.exp(1j * th)
    print("400-gon sigma1*Per (-> 2pi=6.283185...):", sigma1_per(disk, K=20, q=8))
    # validation 2: square [-1,1]^2 : sigma1 = t tanh t with tan t tanh t = 1
    from scipy.optimize import brentq
    t = brentq(lambda t: np.tan(t) * np.tanh(t) - 1, 0.5, 1.2)
    sq = [-1 - 1j, 1 - 1j, 1 + 1j, -1 + 1j]
    print("square exact sigma1 =", t * np.tanh(t), " sigma1*Per =", 8 * t * np.tanh(t))
    for K in [10, 20, 30, 40, 60]:
        ev = steklov_eigs(sq, K=K)
        print(K, ev[:5])
    # equilateral triangle
    E = [np.exp(1j * (np.pi / 2 + 2 * np.pi * k / 3)) for k in range(3)]
    for K in [10, 20, 30, 40, 60, 80, 100]:
        ev = steklov_eigs(E, K=K, nev=8)
        print("E", K, ev[:8] * perimeter(E))
