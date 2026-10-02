"""Numerical exploration of the local bound near E (NUMERICAL EVIDENCE ONLY).

F_loc(S) = Per(T_S) * lambda_min( A(G), B(j) - beta beta^T / Per )
built from the (numerical) first eigenspace (w1,w2) of E pulled back by exp(S).
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from stek import steklov_eigs, perimeter
from moduli_map import tri_S, s1per, E0


def harm_vals_grads(z, c, s, K):
    w = (z - c) / s
    V, Gx, Gy = [np.ones_like(z.real)], [np.zeros_like(z.real)], [np.zeros_like(z.real)]
    wp = np.ones_like(w)
    for k in range(1, K + 1):
        d = k * wp / s
        wp = wp * w
        V += [wp.real, wp.imag]
        Gx += [d.real, d.imag]
        Gy += [-d.imag, d.real]
    return np.array(V).T, np.array(Gx).T, np.array(Gy).T


def tri_quad(verts, n):
    x, w = leggauss(n)
    s = (x + 1) / 2
    w = w / 2
    S, T = np.meshgrid(s, s, indexing="ij")
    WS, WT = np.meshgrid(w, w, indexing="ij")
    a = S
    b = T * (1 - S)
    jac = (1 - S)
    P0, P1, P2 = verts
    z = P0 + a * (P1 - P0) + b * (P2 - P0)
    area2 = abs(((P1 - P0).conjugate() * (P2 - P0)).imag)
    return z.ravel(), (WS * WT * jac).ravel() * area2


def moments(K=30):
    ev, C, (c, s, K) = steklov_eigs(E0, K=K, nev=3, return_vecs=True)
    sig = ev[1]
    # pick w1 odd under x->-x, then w2 from rotation formula
    W = C[:, 1:3]
    # odd/even split: evaluate at mirrored points
    zt = np.array([0.3 + 0.1j, 0.2 - 0.3j, -0.1 + 0.2j])
    Vt, _, _ = harm_vals_grads(zt, c, s, K)
    Vm, _, _ = harm_vals_grads(-zt.conjugate(), c, s, K)
    # find combination with f(-zbar) = -f(z)
    Mm = (Vt + Vm) @ W
    _, _, vt = np.linalg.svd(Mm)
    a1 = W @ vt[-1]
    # rotation: (rho f)(p) = f(R^{-1} p), w2 = (2/sqrt3)(rho w1 + w1/2)
    om = np.exp(-2j * np.pi / 3)
    def f1(z):
        V, gx, gy = harm_vals_grads(z, c, s, K)
        return V @ a1, gx @ a1, gy @ a1
    def f2(z):
        v1, gx1, gy1 = f1(z)
        v1r, gx1r, gy1r = f1(z * om)  # f1(R^{-1} z)
        # gradient of f1(R^{-1}z) = R grad f1 (R^{-1} z)
        c3, s3 = np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3)
        gxr = c3 * gx1r - s3 * gy1r
        gyr = s3 * gx1r + c3 * gy1r
        k = 2 / np.sqrt(3)
        return k * (v1r + v1 / 2), k * (gxr + gx1 / 2), k * (gyr + gy1 / 2)
    # boundary moments per edge k (edge from V_k to V_{k+1})
    x, wq = leggauss(K + 20)
    t = (x + 1) / 2; wq = wq / 2
    Bk = np.zeros((3, 2, 2)); bk = np.zeros((3, 2)); tau = []
    for k in range(3):
        a, b = E0[k], E0[(k + 1) % 3]
        z = a + t * (b - a); L = abs(b - a)
        tau.append((b - a) / L)
        F = np.array([f1(z)[0], f2(z)[0]])
        Bk[k] = (F * wq * L) @ F.T
        bk[k] = (F * wq * L).sum(axis=1)
    zq, wa = tri_quad(E0, K + 20)
    g1 = f1(zq); g2 = f2(zq)
    Gr = [np.array([g1[1], g1[2]]), np.array([g2[1], g2[2]])]  # each 2 x npts
    Aij = np.zeros((2, 2, 2, 2))  # [i,j,a,b] int d_i w_a d_j w_b
    for a_ in range(2):
        for b_ in range(2):
            Aij[:, :, a_, b_] = (Gr[a_] * wa) @ Gr[b_].T
    norm = np.trace(Bk.sum(axis=0)) / 2
    return sig, Aij / norm, Bk / norm, bk / np.sqrt(norm), np.array(tau)


def F_loc(r, p, sig, Aij, Bk, bk, tau):
    Sh = np.array([[np.cos(p), np.sin(p)], [np.sin(p), -np.cos(p)]])
    eS = np.cosh(r) * np.eye(2) + np.sinh(r) * Sh
    G = np.cosh(2 * r) * np.eye(2) - np.sinh(2 * r) * Sh
    A = np.einsum('ij,ijab->ab', G, Aij)
    j = np.array([np.linalg.norm(eS @ np.array([t.real, t.imag])) for t in tau])
    L = np.sqrt(3)
    P = L * j.sum()
    B = np.einsum('k,kab->ab', j, Bk)
    be = j @ bk
    D = B - np.outer(be, be) / P
    lam = np.min(np.real(np.linalg.eigvals(np.linalg.solve(D, A))))
    return P * lam


if __name__ == "__main__":
    sig, Aij, Bk, bk, tau = moments(30)
    np.set_printoptions(precision=10, suppress=True, linewidth=150)
    print("sigma1(E) =", sig, " sigma*Per =", sig * 3 * np.sqrt(3))
    print("sum_k Bk =\n", Bk.sum(0))
    print("sum_k bk =", bk.sum(0))
    print("A(I) =\n", Aij[0, 0] + Aij[1, 1], "  (should be sigma*I)")
    for k in range(3):
        print("edge", k, "Bk=\n", Bk[k], " bk=", bk[k])
    print("Aij[0,0]=\n", Aij[0, 0], "\nAij[1,1]=\n", Aij[1, 1], "\nAij[0,1]=\n", Aij[0, 1])
    target = sig * 3 * np.sqrt(3)
    for r in [1e-3, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0]:
        vals = [F_loc(r, p, sig, Aij, Bk, bk, tau) for p in np.linspace(0, 2 * np.pi, 73)]
        tru = [s1per(tri_S(r, p)) for p in np.linspace(0, 2 * np.pi, 13)]
        print(f"r={r:6.3f}  max F_loc={max(vals):.8f}  (F_loc-target)/r={(max(vals)-target)/r:+.5f}  true max={max(tru):.6f}")
