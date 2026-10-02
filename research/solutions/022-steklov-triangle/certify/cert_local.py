"""CERTIFIED STEP 3: local region 0 < |S| <= R_LOC.

For S = r*Shat(phi), Shat = [[cos phi, sin phi],[sin phi, -cos phi]], T_S = exp(S) E.
Trial space on T_S: span{ w_a o exp(-S) } minus boundary mean, with (w1,w2)
the exact orthonormal equivariant pair of first eigenfunctions of E.
With jbar = (j0+j1+j2)/3, j_k = |exp(S) tau_k|, P = Per(T_S) = 3*sqrt3*jbar:

  M'(S) = jbar*A(G) - sigma*B(j) + sigma*b(j) b(j)^T / P
        = (P/Per(E)) * [ A - (Per(E) sigma / P) (B - b b^T/P) ]

and lambda_min(M') < 0  ==>  sigma_1(T_S) Per(T_S) < sigma_1(E) Per(E)   (PROOF.md Lemma 6).

We certify, on a cover of (0, R_LOC] x [0, 2pi] by boxes, that the ball
enclosure of M'/r has  det < 0  or  trace < 0.
The removable singularity at r = 0 is handled by exact algebra:
  M'/r = sigma*jbar*((cosh2r-1)/r) I - jbar*(sinh2r/r)(cX+sY)
         - sigma*sum_k ((j_k-jbar)/r) (B_k - I/3)
         + sigma*r*(sum_k ((j_k-jbar)/r) b_k)(...)^T / P,
  (j_k - j_m)/r = (sinh2r/r) (t_k - t_m)/(j_k + j_m),  t_k = tau_k^T Shat tau_k.
For boxes with r_lo = 0 the monotone functions sinh(2r)/r and 2 sinh(r)^2/r
are enclosed by their values at the endpoints.
"""
import time
import flint
from flint import arb, fmpq

flint.ctx.prec = 128


def ball(lo, hi):
    lo, hi = arb(lo), arb(hi)
    return lo.union(hi)


class LocalData:
    def __init__(self, E):
        self.sig = E['sig_lo'].union(E['sig_hi'])
        self.X, self.Y, self.Bk, self.bk = E['X'], E['Y'], E['Bk'], E['bk']
        sq3 = arb(3).sqrt()
        # unit tangents of edges k: V_k -> V_{k+1}  (V0=(0,1), V1=(-sq3/2,-1/2), V2=(sq3/2,-1/2))
        V = [(arb(0), arb(1)), (-sq3 / 2, arb(-1) / 2), (sq3 / 2, arb(-1) / 2)]
        self.tau = []
        for k in range(3):
            dx = V[(k + 1) % 3][0] - V[k][0]
            dy = V[(k + 1) % 3][1] - V[k][1]
            L = (dx * dx + dy * dy).sqrt()
            self.tau.append((dx / L, dy / L))
        self.sq3 = sq3


def Mr_box(D, ra, rb, pa, pb):
    """ball enclosure of M'(r,phi)/r for r in [ra,rb] (ra>=0), phi in [pa,pb]."""
    r = ball(ra, rb)
    phi = ball(pa, pb)
    c, s = phi.cos(), phi.sin()
    sh2, ch2 = (2 * r).sinh(), (2 * r).cosh()
    if ra == 0:
        rbA = arb(rb)
        sh2r = ball(arb(2), ((2 * rbA).sinh() / rbA).upper())
        chm1r = ball(arb(0), (2 * rbA.sinh() ** 2 / rbA).upper())
    else:
        sh2r = sh2 / r
        chm1r = 2 * r.sinh() ** 2 / r
    t = [c * (tx * tx - ty * ty) + 2 * s * tx * ty for (tx, ty) in D.tau]
    j = [(ch2 + sh2 * tk).sqrt() for tk in t]
    jbar = (j[0] + j[1] + j[2]) / 3
    djr = []
    for k in range(3):
        acc = arb(0)
        for m in range(3):
            if m != k:
                acc += sh2r * (t[k] - t[m]) / (j[k] + j[m])
        djr.append(acc / 3)
    P = 3 * D.sq3 * jbar
    sig = D.sig
    M = [[arb(0), arb(0)], [arb(0), arb(0)]]
    bv = [sum(djr[k] * D.bk[k][a] for k in range(3)) for a in range(2)]
    for a in range(2):
        for b in range(2):
            v = -jbar * sh2r * (c * D.X[a][b] + s * D.Y[a][b])
            for k in range(3):
                Bk0 = D.Bk[k][a][b] - (arb(1) / 3 if a == b else arb(0))
                v -= sig * djr[k] * Bk0
            v += sig * r * bv[a] * bv[b] / P
            if a == b:
                v += sig * jbar * chm1r
            M[a][b] = v
    return M


def box_ok(D, ra, rb, pa, pb):
    M = Mr_box(D, ra, rb, pa, pb)
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    tr = M[0][0] + M[1][1]
    return (det < 0) or (tr < 0)


def certify_local(E, R_LOC=fmpq(3, 5), NR=60, NP=120, maxdepth=14, log=print):
    t0 = time.time()
    D = LocalData(E)
    twopi = 2 * arb.pi()
    # box = (ra, rb, num, den, depth): r in [ra,rb] (rationals), phi in [2pi*num/den, 2pi*(num+1)/den]
    work = []
    for i in range(NR):
        ra = fmpq(i, NR) * R_LOC
        rb = fmpq(i + 1, NR) * R_LOC
        for k in range(NP):
            work.append((ra, rb, k, NP, 0))
    nboxes = 0; maxd = 0; nsplit = 0
    while work:
        ra, rb, num, den, d = work.pop()
        lo = twopi * num / den
        hi = twopi * (num + 1) / den
        ra_a = 0 if ra == 0 else arb(ra.p) / ra.q
        rb_a = arb(rb.p) / rb.q
        if box_ok(D, ra_a, rb_a, lo.lower(), hi.upper()):
            nboxes += 1; maxd = max(maxd, d)
            continue
        if d >= maxdepth:
            raise AssertionError(f"local check failed at r in [{ra},{rb}], phi in 2pi*[{num}/{den},{num+1}/{den}]")
        nsplit += 1
        rm = (ra + rb) / 2
        for (r1, r2) in ((ra, rm), (rm, rb)):
            work.append((r1, r2, 2 * num, 2 * den, d + 1))
            work.append((r1, r2, 2 * num + 1, 2 * den, d + 1))
    log(f"local region 0<r<={R_LOC}: {nboxes} boxes verified (det(M'/r)<0 or tr(M'/r)<0), "
        f"{nsplit} splits, max depth {maxd}")
    log(f"CERTIFIED: sigma_1(T_S)Per(T_S) < sigma_1(E)Per(E) for all 0 < |S| <= {R_LOC}")
    return R_LOC


if __name__ == "__main__":
    from cert_E import certify_E
    rho = fmpq(*map(int, open("rho.txt").read().strip().split("/")))
    E = certify_E(rho, log=lambda *a: None)
    certify_local(E)
