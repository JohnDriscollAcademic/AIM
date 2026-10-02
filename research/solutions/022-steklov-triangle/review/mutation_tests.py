"""Mutation tests (review only, not part of the proof): every certified check
must FAIL when fed a wrong input.  Run from the repository root:
    python3 review/mutation_tests.py
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "certify")); os.chdir(os.path.join(ROOT, "certify"))
from flint import fmpq, arb
from cert_rho import certify_rho
from cert_E import certify_E
from cert_local import certify_local
from cert_far import certify_far
q = lambda *a: None
ok = True
def expect_fail(name, f):
    global ok
    try:
        f(); print(f"MUTATION NOT DETECTED: {name}"); ok = False
    except AssertionError as e:
        print(f"detected: {name} -> {str(e)[:90]}")
E = certify_E(fmpq(1388851, 10**6), log=q)
expect_fail("mu = 1.98 > lambda_h3", lambda: certify_rho(n=16, mu=fmpq(198, 100), log=q))
expect_fail("rho = 0.7 < lambda~", lambda: certify_E(fmpq(7, 10), log=q))
expect_fail("R_LOC = 1", lambda: certify_local(E, R_LOC=fmpq(1), log=q))
expect_fail("R_FAR = 0.3", lambda: certify_far(E['sig_lo'], R_FAR=fmpq(3, 10), log=q))
expect_fail("target lowered", lambda: certify_far(E['sig_lo'] - arb('0.2'), R_FAR=fmpq(11, 20), log=q))
print("ALL MUTATIONS DETECTED" if ok else "SOME MUTATION NOT DETECTED")
