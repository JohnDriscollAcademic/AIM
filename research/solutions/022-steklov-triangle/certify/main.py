"""Driver: runs every certified step of the triangle Steklov theorem in order.

Every step raises AssertionError (non-zero exit) if a check fails.  The final
line "ALL CERTIFIED CHECKS PASSED" is printed only if all steps succeeded.
"""
import sys
import platform
import flint
from flint import fmpq

from cert_rho import certify_rho
from cert_E import certify_E
from cert_local import certify_local
from cert_far import certify_far


def log(*a):
    print(*a)
    sys.stdout.flush()


def main():
    log(f"python {platform.python_version()}, python-flint {flint.__version__}, platform {platform.platform()}")
    log("=" * 78)
    log("STEP 1  rho <= sigma_3(E): Crouzeix-Raviart FEM + exact inertia (Lemma 2)")
    rho = certify_rho(n=16, mu=fmpq(196, 100), log=log)
    log("=" * 78)
    log("STEP 2  sigma_1(E) enclosure (Temple), eigenvector/moment enclosures (Lemmas 3-5)")
    E = certify_E(rho, log=log)
    log("=" * 78)
    log("STEP 3  local region 0 < |S| <= 3/5 (Lemma 6)")
    R_LOC = certify_local(E, R_LOC=fmpq(3, 5), log=log)
    log("=" * 78)
    log("STEP 4  far region |S| >= 11/20 (Lemma 7)")
    R_FAR = certify_far(E['sig_lo'], R_FAR=fmpq(11, 20), log=log)
    assert R_FAR <= R_LOC, "local and far regions must overlap"
    log("=" * 78)
    log(f"Coverage: (0, {R_LOC}] U [{R_FAR}, oo) = (0, oo) since {R_FAR} <= {R_LOC}.")
    log("THEOREM: for every non-equilateral triangle T, sigma_1(T)Per(T) < sigma_1(E)Per(E).")
    log("ALL CERTIFIED CHECKS PASSED")


if __name__ == "__main__":
    main()
