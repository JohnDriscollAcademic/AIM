"""CERTIFIED STEP 2: enclosure of sigma_1(E) and of the moments of the first
eigenspace of E (circumradius 1, vertices i, e^{i 7pi/6}, e^{-i pi/6}).

Input: rho (rational) with rho <= sigma_3(E)   (from cert_rho.py).

Trial function: w~ = Re F(z), F(z) = sum_k c_k a_k z^k over k in the odd E-type
sector (k not divisible by 3; a_k = 1 for odd k, a_k = -i for even k), with
exact rational (dyadic) coefficients c_k read from trial_coeffs.json (generated once
by the non-rigorous helper make_trial_coeffs.py; their origin is irrelevant for
rigour).  All integrals are integrals of polynomials along the three edges,
computed exactly in Arb ball arithmetic.  No floating point is used here.

Outputs (PROOF.md, Lemmas 3-5):
  * sigma_1 in [sigma_lo, sigma_hi]  (Temple + Rayleigh)
  * delta0 >= ||g||_{L2(dE)},  delta1 >= ||grad G||_{L2(E)}  (eigenvector error)
  * enclosures of X, Y (2x2), B_k (2x2), b_k (2) for the exact orthonormal
    equivariant pair (w1, w2) of eigenfunctions.
"""
import json
import os
import flint
from flint import arb, acb, arb_poly, acb_poly, fmpq

flint.ctx.prec = 320

SQ3 = arb(3).sqrt()
I = acb(0, 1)
VERTS = [acb(0, 1), acb(-SQ3 / 2, arb(-1) / 2), acb(SQ3 / 2, arb(-1) / 2)]
OMEGA = acb(arb(-1) / 2, SQ3 / 2)          # e^{2 pi i/3}
OMEGA_BAR = acb(arb(-1) / 2, -SQ3 / 2)


def sector_degrees(K):
    return [k for k in range(1, K + 1) if k % 3 != 0]


def F_coeffs(ks, cq):
    """complex coefficient list of F (index = power of z)."""
    deg = max(ks)
    co = [acb(0)] * (deg + 1)
    for k, ck in zip(ks, cq):
        ak = acb(1) if k % 2 == 1 else acb(0, -1)
        co[k] = co[k] + ak * acb(arb(ck.p) / ck.q)
    return co


def rotate_coeffs(co, w):
    """coefficients of F(w z)"""
    out, wp = [], acb(1)
    for c in co:
        out.append(c * wp)
        wp = wp * w
    return out


def deriv(co):
    return [co[k] * k for k in range(1, len(co))] or [acb(0)]


def compose_edge(co, a, d):
    """acb_poly in t of sum co[k] (a + t d)^k (Horner)."""
    p = acb_poly([acb(0)])
    lin = acb_poly([a, d])
    for c in reversed(co):
        p = p * lin + acb_poly([c])
    return p


def re_poly(p):
    return arb_poly([c.real for c in p.coeffs()])


def int01(p):
    """exact integral over [0,1] of a real/complex polynomial in t"""
    s = 0
    for i, c in enumerate(p.coeffs()):
        s = s + c / (i + 1)
    return s


class Edge:
    def __init__(self, k):
        a, b = VERTS[k], VERTS[(k + 1) % 3]
        self.a, self.d = a, b - a
        self.L = abs(self.d)                     # = sqrt(3)
        self.nu = acb(0, -1) * self.d / self.L   # outward unit normal (ccw)


EDGES = [Edge(k) for k in range(3)]


class HarmPoly:
    """u = Re F, F given by coefficient list; precomputes edge polynomials."""
    def __init__(self, co):
        self.co = co
        dco = deriv(co)
        self.val, self.dn, self.Fp = [], [], []
        for e in EDGES:
            self.val.append(re_poly(compose_edge(co, e.a, e.d)))
            fp = compose_edge(dco, e.a, e.d)
            self.Fp.append(fp)
            self.dn.append(re_poly(fp * acb_poly([e.nu])))


def edge_int(pk, e):
    return e.L * int01(pk)


def moments_pair(u, v):
    """returns dict of exact (ball) moments for harmonic polynomials u, v."""
    out = {}
    out['B'] = [edge_int(u.val[k] * v.val[k], EDGES[k]) for k in range(3)]
    out['grad'] = sum(edge_int(u.val[k] * v.dn[k], EDGES[k]) for k in range(3))
    # Phi = int_E F_u' F_v' dA = (1/(2i)) oint conj(z) F_u' F_v' dz
    Phi = acb(0)
    for k, e in enumerate(EDGES):
        zbar = acb_poly([e.a.conjugate(), e.d.conjugate()])
        integrand = zbar * u.Fp[k] * v.Fp[k] * acb_poly([e.d])
        Phi = Phi + int01(integrand)
    Phi = Phi / acb(0, 2)
    out['X'] = Phi.real            # int (u_x v_x - u_y v_y)
    out['Y'] = -Phi.imag           # int (u_x v_y + u_y v_x)
    return out


COEFF_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trial_coeffs.json")


def load_trial_coeffs(path=COEFF_FILE):
    with open(path) as f:
        data = json.load(f)
    ks = [int(k) for k in data["degrees"]]
    cq = []
    for txt in data["coefficients"]:
        p, q = txt.split("/")
        cq.append(fmpq(int(p), int(q)))
    assert ks == sector_degrees(max(ks)), "degrees must be the odd E-type sector degrees"
    assert len(cq) == len(ks)
    return ks, cq


def certify_E(rho, log=print, coeff_file=COEFF_FILE):
    ks, cq = load_trial_coeffs(coeff_file)
    log(f"trial function: {len(ks)} exact rational coefficients (degrees <= {max(ks)}, odd E-type sector) from trial_coeffs.json")
    co1 = F_coeffs(ks, cq)
    u1 = HarmPoly(co1)
    # second member of the equivariant pair: F2(z) = (2/sqrt3)(F(omega_bar z) + F(z)/2)
    rot = rotate_coeffs(co1, OMEGA_BAR)
    co2 = [(r + c1 / 2) * (2 / SQ3) for r, c1 in zip(rot, co1)]
    u2 = HarmPoly(co2)
    # --- Temple in the sector
    n0 = sum(edge_int(u1.val[k] * u1.val[k], EDGES[k]) for k in range(3))
    n1 = sum(edge_int(u1.val[k] * u1.dn[k], EDGES[k]) for k in range(3))
    n2 = sum(edge_int(u1.dn[k] * u1.dn[k], EDGES[k]) for k in range(3))
    mean1 = sum(edge_int(u1.val[k], EDGES[k]) for k in range(3))
    log(f"boundary mean of w~1 = {mean1.str(5)} (must be 0 by oddness)")
    lam = n1 / n0
    eps2 = n2 / n0 - lam * lam
    rhoA = arb(rho.p) / rho.q
    assert lam < rhoA, "Temple hypothesis violated: Rayleigh quotient must lie below rho"
    sig_lo = (lam - eps2 / (rhoA - lam)).lower()
    sig_hi = lam.upper()
    log(f"Rayleigh quotient lambda~ = {lam.str(30)}")
    log(f"residual eps^2 = ||Lf-lam f||^2/||f||^2 = {eps2.str(10)}")
    log(f"CERTIFIED: sigma_1(E) in [{sig_lo.str(30)}, {sig_hi.str(30)}]")
    # --- eigenvector error (unnormalised: ||r|| = sqrt(eps2 * n0))
    rnorm = (eps2 * n0).sqrt()
    gap = rhoA - lam
    delta0 = (rnorm / gap).upper()
    delta1 = (rhoA.sqrt() * rnorm / gap).upper()
    log(f"delta0 >= ||g||_dE = {delta0.str(5)} ; delta1 >= ||grad G||_E = {delta1.str(5)}")
    # --- moments of approximate pair
    m11, m12, m22 = moments_pair(u1, u1), moments_pair(u1, u2), moments_pair(u2, u2)
    lin1 = [edge_int(u1.val[k], EDGES[k]) for k in range(3)]
    lin2 = [edge_int(u2.val[k], EDGES[k]) for k in range(3)]
    ebn = [[(edge_int(u.val[k] * u.val[k], EDGES[k])).sqrt() for k in range(3)] for u in (u1, u2)]
    gn = [m11['grad'].sqrt(), m22['grad'].sqrt()]
    log(f"check ||w~2||^2_dE = {sum(m22['B']).str(15)} vs ||w~1||^2 = {n0.str(15)}; <w~1,w~2> = {sum(m12['B']).str(5)}")
    # normalisation N^2 = ||f1||^2 in [n0 - delta0^2, n0]
    d0, d1 = arb(delta0), arb(delta1)
    N2 = (n0 - d0 * d0).union(n0)
    N = N2.sqrt()
    def widen(x, r):
        return x + arb(0, r.upper())
    pairs = {(0, 0): m11, (0, 1): m12, (1, 1): m22}
    X = [[None, None], [None, None]]; Y = [[None, None], [None, None]]
    Bk = [[[None, None], [None, None]] for _ in range(3)]
    for (a, b), m in pairs.items():
        eg = d1 * (gn[a] + gn[b]) + d1 * d1
        xv = widen(m['X'], eg) / N2
        yv = widen(m['Y'], eg) / N2
        X[a][b] = X[b][a] = xv
        Y[a][b] = Y[b][a] = yv
        for k in range(3):
            eb = d0 * (ebn[a][k] + ebn[b][k]) + d0 * d0
            Bk[k][a][b] = Bk[k][b][a] = widen(m['B'][k], eb) / N2
    bk = [[widen(lin1[k], EDGES[k].L.sqrt() * d0) / N, widen(lin2[k], EDGES[k].L.sqrt() * d0) / N]
          for k in range(3)]
    log("Enclosures for the exact orthonormal pair (w1,w2):")
    for name, M in (("X", X), ("Y", Y)):
        log(f"  {name} = [[{M[0][0].str(12)}, {M[0][1].str(12)}], [{M[1][0].str(12)}, {M[1][1].str(12)}]]")
    for k in range(3):
        log(f"  B_{k} = [[{Bk[k][0][0].str(12)}, {Bk[k][0][1].str(12)}], [.., {Bk[k][1][1].str(12)}]]  b_{k} = ({bk[k][0].str(12)}, {bk[k][1].str(12)})")
    return dict(sig_lo=sig_lo, sig_hi=sig_hi, X=X, Y=Y, Bk=Bk, bk=bk)


if __name__ == "__main__":
    rho = fmpq(*map(int, open("rho.txt").read().strip().split("/")))
    certify_E(rho)
