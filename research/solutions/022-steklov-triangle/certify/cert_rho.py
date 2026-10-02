"""CERTIFIED STEP 1:  rho <= sigma_3(E)   (E = equilateral, circumradius 1).

Method (PROOF.md, Lemma 2):
  * Crouzeix-Raviart FEM on the uniform mesh of E with n^2 equilateral elements.
  * Exact integer inertia of  A = q*Kint - p*N3  (p/q = mu/(2n)) via the
    characteristic polynomial (FLINT, exact integers) and Descartes' rule of
    signs, which is exact for real-rooted polynomials (A is symmetric).
    #neg(A) = #{discrete eigenvalues < mu} counting the eigenvalue 0.
    If #neg(A) == 3 then lambda_{h,3} >= mu.
  * Guaranteed bound  sigma_3 >= lambda_{h,3}/(1 + C_h^2 lambda_{h,3})
                              >= mu/(1 + C_h^2 mu),
    C_h^2 = 2*(2/pi^2 + 2/pi) * h^2/H   (elements have <= 2 boundary edges),
    h^2/H = 2/n for equilateral elements of side h = sqrt(3)/n.
  * All real-number arithmetic in Arb ball arithmetic (outward rounding).
"""
import sys
import time
import flint
from flint import arb, fmpz_mat, fmpq
from cr_mesh import build

flint.ctx.prec = 256


def descartes_sign_changes(coeffs):
    s = [c for c in coeffs if c != 0]
    return sum(1 for a, b in zip(s, s[1:]) if (a > 0) != (b > 0))


def inertia_int_symmetric(A):
    """Exact inertia (n_neg, n_zero, n_pos) of an integer symmetric matrix."""
    n = A.nrows()
    for i in range(n):
        for j in range(i):
            assert A[i, j] == A[j, i], "matrix not symmetric"
    p = A.charpoly()
    c = [int(p.coeffs()[k]) for k in range(p.degree() + 1)]  # c[k] coefficient of x^k
    nzero = 0
    while c[nzero] == 0:
        nzero += 1
    cc = c[nzero:]
    npos = descartes_sign_changes(cc)
    nneg = descartes_sign_changes([cc[k] * (-1) ** k for k in range(len(cc))])
    assert npos + nneg + nzero == n, "real-rootedness/Descartes count inconsistent"
    return nneg, nzero, npos


def certify_rho(n=16, mu=fmpq(196, 100), log=print):
    t0 = time.time()
    ndof, Kint, N3, maxnb, ntri = build(n)
    log(f"mesh n={n}: {ntri} equilateral elements, {ndof} CR dofs, max boundary edges per element = {maxnb}")
    assert maxnb <= 2
    mup = mu / (2 * n)  # rational
    p, q = mup.p, mup.q
    A = fmpz_mat(ndof, ndof)
    for (i, j), v in Kint.items():
        A[i, j] += q * v
    for (i, j), v in N3.items():
        A[i, j] -= p * v
    nneg, nzero, npos = inertia_int_symmetric(A)
    log(f"mu = {mu} : inertia of q*Kint - p*N3 (p/q = {mup}) = (neg {nneg}, zero {nzero}, pos {npos})")
    assert nneg == 3, "expected exactly 3 discrete eigenvalues below mu (0, lam_h1, lam_h2)"
    log("=> discrete CR eigenvalues: lambda_{h,3} >= mu (certified, exact integer arithmetic)")
    pi = arb.pi()
    Cpw = 2 / pi**2 + 2 / pi                      # (2/pi^2 + 2/pi)
    Ch2 = 2 * Cpw * arb(2) / n                    # 2 * Cpw * h^2/H, h^2/H = 2/n
    muA = arb(mu.p) / mu.q
    rho = muA / (1 + Ch2 * muA)
    rho_lo = rho.lower()
    log(f"C_h^2 in {Ch2.str(20)} ; rho = mu/(1+C_h^2 mu) in {rho.str(20)}")
    # rational certificate rho_q <= rho_lo (checked in ball arithmetic)
    rho_q = fmpq(int((rho_lo * 10**6).floor().unique_fmpz()), 10**6)
    assert arb(rho_q.p) / rho_q.q <= rho_lo
    log(f"CERTIFIED: sigma_3(E) >= rho_lo = {rho_lo.str(25)} >= rho_q = {rho_q}")
    return rho_q


if __name__ == "__main__":
    rho = certify_rho()
    with open("rho.txt", "w") as f:
        f.write(f"{rho.p}/{rho.q}\n")
