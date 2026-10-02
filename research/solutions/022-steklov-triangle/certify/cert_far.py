"""CERTIFIED STEP 4: far region |S| >= R_FAR.

Lemma 7 (PROOF.md): for every S with |S| = r,
   sigma_1(T_S) Per(T_S) <= Bfar(r) := 12 |E| ( e^{-2r}/W^2 + d e^{-4r}/W^3 ),
with |E| = 3 sqrt3/4, W = 3/2 (minimal width of E), d = sqrt3 (diameter of E).
Bfar is decreasing in r, so it suffices to check Bfar(R_FAR) < Per(E) * sigma_lo.
"""
import flint
from flint import arb, fmpq

flint.ctx.prec = 128


def Bfar(r):
    sq3 = arb(3).sqrt()
    areaE = 3 * sq3 / 4
    W = arb(3) / 2
    d = sq3
    return 12 * areaE * ((-2 * r).exp() / W**2 + d * (-4 * r).exp() / W**3)


def certify_far(sig_lo, R_FAR=fmpq(11, 20), log=print):
    r = arb(R_FAR.p) / R_FAR.q
    B = Bfar(r)
    target = 3 * arb(3).sqrt() * sig_lo
    log(f"Bfar({R_FAR}) in {B.str(15)} ; Per(E)*sigma_lo in {target.str(20)}")
    assert B < target, "far bound failed"
    log(f"CERTIFIED: sigma_1(T_S)Per(T_S) < sigma_1(E)Per(E) for all |S| >= {R_FAR}")
    return R_FAR


if __name__ == "__main__":
    from cert_E import certify_E
    rho = fmpq(*map(int, open("rho.txt").read().strip().split("/")))
    E = certify_E(rho, log=lambda *a: None)
    certify_far(E['sig_lo'])
