"""Self-review checks for Lemma 6 / cert_local.py (not part of the proof).

(1) The factored expression M'/r used in cert_local equals (jbar*A - sigma*D)/r computed directly,
    for arbitrary (non-eigen) moment data satisfying the three exact identities.
(2) The moment-based Rayleigh-Ritz matrices equal direct quadrature of the pulled-back trial
    functions on the actual triangle T_S (validates G = exp(-2S), j_k, P, mean subtraction).
(3) Direct (unfactored) Arb check of lambda_min(A - (Per(E) sigma/P) D) < 0 on boxes with r >= 0.05.
"""
import sys, os
import numpy as np
import mpmath as mp
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + "/certify"); sys.path.insert(0, ROOT + "/numerics")
os.chdir(ROOT + "/certify")
import flint
from flint import arb, fmpq
from cert_local import LocalData, Mr_box

mp.mp.dps = 40
sq3 = mp.sqrt(3)
V = [(mp.mpf(0), mp.mpf(1)), (-sq3 / 2, mp.mpf(-1) / 2), (sq3 / 2, mp.mpf(-1) / 2)]
tau = []
for k in range(3):
    dx = V[(k + 1) % 3][0] - V[k][0]; dy = V[(k + 1) % 3][1] - V[k][1]; L = mp.sqrt(dx**2 + dy**2)
    tau.append((dx / L, dy / L))


def direct_M(r, phi, sig, X, Y, Bk, bk):
    c, s = mp.cos(phi), mp.sin(phi)
    Sh = mp.matrix([[c, s], [s, -c]])
    t = [tx * tx * c + 2 * tx * ty * s - ty * ty * c for tx, ty in tau]
    j = [mp.sqrt(mp.cosh(2 * r) + mp.sinh(2 * r) * tk) for tk in t]
    jbar = sum(j) / 3; P = 3 * sq3 * jbar
    A = sig * mp.cosh(2 * r) * mp.eye(2) - mp.sinh(2 * r) * (c * X + s * Y)
    B = sum((j[k] * Bk[k] for k in range(3)), mp.zeros(2, 2))
    b = sum((j[k] * bk[k] for k in range(3)), mp.zeros(2, 1))
    D = B - b * b.T / P
    return jbar * A - sig * D


def rand_sym(rng):
    a, b, c = rng.normal(size=3)
    return mp.matrix([[a, b], [b, c]])


# ---- (1) factored formula vs direct, random data with exact identities imposed
rng = np.random.default_rng(1)
D = LocalData.__new__(LocalData)
D.sq3 = arb(3).sqrt()
D.tau = [(arb(str(tx)), arb(str(ty))) for tx, ty in tau]
maxdiff = 0
for trial in range(20):
    sig = mp.mpf(rng.uniform(0.3, 1.5))
    X, Y = rand_sym(rng), rand_sym(rng)
    B0, B1 = rand_sym(rng), rand_sym(rng); B2 = mp.eye(2) - B0 - B1
    b0 = mp.matrix(rng.normal(size=2)); b1 = mp.matrix(rng.normal(size=2)); b2 = -b0 - b1
    Bk = [B0, B1, B2]; bk = [b0, b1, b2]
    D.sig = arb(str(sig))
    D.X = [[arb(str(X[a, b])) for b in range(2)] for a in range(2)]
    D.Y = [[arb(str(Y[a, b])) for b in range(2)] for a in range(2)]
    D.Bk = [[[arb(str(Bk[k][a, b])) for b in range(2)] for a in range(2)] for k in range(3)]
    D.bk = [[arb(str(bk[k][a])) for a in range(2)] for k in range(3)]
    r = mp.mpf(rng.uniform(0.001, 0.8)); phi = mp.mpf(rng.uniform(0, 2 * mp.pi))
    Md = direct_M(r, phi, sig, X, Y, Bk, bk) / r
    Mf = Mr_box(D, arb(str(r)), arb(str(r)), arb(str(phi)), arb(str(phi)))
    for a in range(2):
        for b in range(2):
            maxdiff = max(maxdiff, abs(Md[a, b] - mp.mpf(Mf[a][b].mid().str(30, radius=False))))
print("(1) max |factored M'/r - direct M'/r| over 20 random cases:", mp.nstr(maxdiff, 5))

# ---- (2) moment formula vs direct quadrature on T_S with float eigenfunctions
from local_num import moments, harm_vals_grads, tri_quad
from stek import steklov_eigs
from moduli_map import E0
from numpy.polynomial.legendre import leggauss
sigf, Aij, Bkf, bkf, tauf = moments(30)
ev, C, (c0, s0, K) = steklov_eigs(E0, K=30, nev=3, return_vecs=True)
W = C[:, 1:3]
# orthonormalise the float pair on the boundary
x, wq = leggauss(60); tq = (x + 1) / 2; wq = wq / 2
def bvals(z):
    Vv, _, _ = harm_vals_grads(z, c0, s0, K); return Vv @ W
Gb = np.zeros((2, 2))
for k in range(3):
    a, b = E0[k], E0[(k + 1) % 3]; z = a + tq * (b - a)
    F = bvals(z); Gb += (F * (wq * abs(b - a))[:, None]).T @ F
L = np.linalg.cholesky(Gb); Wn = W @ np.linalg.inv(L).T
def F_moment(r, p):
    Sh = np.array([[np.cos(p), np.sin(p)], [np.sin(p), -np.cos(p)]])
    eS = np.cosh(r) * np.eye(2) + np.sinh(r) * Sh
    Ainv = np.linalg.inv(eS)
    # direct: trial u = v o A^{-1} on T_S; compute energy and boundary matrices by quadrature on T_S
    TS = eS @ np.array([E0.real, E0.imag]); TSz = TS[0] + 1j * TS[1]
    zq, wa = tri_quad(TSz, 40)
    y = np.array([zq.real, zq.imag]); xx = Ainv @ y; zE = xx[0] + 1j * xx[1]
    _, gx, gy = harm_vals_grads(zE, c0, s0, K)
    GE = np.stack([gx @ Wn, gy @ Wn])           # grad_x v, shape (2, npts, 2fun)
    GT = np.einsum('ji,jnf->inf', Ainv, GE)      # grad_y u = A^{-T} grad_x v
    Amat = np.einsum('inf,ing,n->fg', GT, GT, wa)
    Bm = np.zeros((2, 2)); bv = np.zeros(2); P = 0
    for k in range(3):
        a, b = TSz[k], TSz[(k + 1) % 3]; zt = a + tq * (b - a); Lk = abs(b - a); P += Lk
        yy = np.array([zt.real, zt.imag]); xe = Ainv @ yy; ze = xe[0] + 1j * xe[1]
        Fv = bvals(ze) @ np.linalg.inv(L).T
        Bm += (Fv * (wq * Lk)[:, None]).T @ Fv; bv += (Fv * (wq * Lk)[:, None]).sum(0)
    Dm = Bm - np.outer(bv, bv) / P
    lam = np.min(np.linalg.eigvals(np.linalg.solve(Dm, Amat)).real)
    return P * lam
from local_num import F_loc
md = 0
for r, p in [(0.01, 0.2), (0.2, 1.3), (0.45, 2.9), (0.6, 4.4), (0.8, 5.9)]:
    a1 = F_moment(r, p); a2 = F_loc(r, p, sigf, Aij, Bkf, bkf, tauf)
    md = max(md, abs(a1 - a2))
    print(f"   r={r} phi={p}: direct quadrature on T_S {a1:.12f}  moment formula {a2:.12f}")
print("(2) max difference:", md)

# ---- (3) direct unfactored Arb check on boxes r in [0.05, 0.6]
from cert_E import certify_E
rho = fmpq(*map(int, open("rho.txt").read().strip().split("/")))
Ecert = certify_E(rho, log=lambda *a: None)
Dc = LocalData(Ecert)
def direct_ok(ra, rb, pa, pb):
    r = arb(ra).union(arb(rb)); ph = arb(pa).union(arb(pb)); c, s = ph.cos(), ph.sin()
    sh2, ch2 = (2 * r).sinh(), (2 * r).cosh()
    t = [c * (tx * tx - ty * ty) + 2 * s * tx * ty for (tx, ty) in Dc.tau]
    j = [(ch2 + sh2 * tk).sqrt() for tk in t]; P = Dc.sq3 * (j[0] + j[1] + j[2])
    sig = Dc.sig
    A = [[(sig * ch2 if a == b else arb(0)) - sh2 * (c * Dc.X[a][b] + s * Dc.Y[a][b]) for b in range(2)] for a in range(2)]
    bvec = [sum(j[k] * Dc.bk[k][a] for k in range(3)) for a in range(2)]
    Dm = [[sum(j[k] * Dc.Bk[k][a][b] for k in range(3)) - bvec[a] * bvec[b] / P for b in range(2)] for a in range(2)]
    lamt = 3 * Dc.sq3 * sig / P
    M = [[A[a][b] - lamt * Dm[a][b] for b in range(2)] for a in range(2)]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]; tr = M[0][0] + M[1][1]
    return (det < 0) or (tr < 0)
nb = 0; fails = 0
NR, NP = 110, 240
for i in range(NR):
    ra = 0.05 + (0.6 - 0.05) * i / NR; rb = 0.05 + (0.6 - 0.05) * (i + 1) / NR
    for k in range(NP):
        pa = 2 * np.pi * k / NP; pb = 2 * np.pi * (k + 1) / NP
        nb += 1
        if not direct_ok(ra, rb, pa, pb):
            fails += 1
print(f"(3) direct unfactored Arb check on r in [0.05,0.6]: {nb} boxes, {fails} not verified (float box endpoints; cross-check only)")
