"""Run every exact certificate. Usage: python verify.py

The verification uses integers and rational arithmetic. NumPy is the only
external package. Floating-point conversions are used only for human-readable
printed approximations, never for acceptance of a certificate.
"""
import sys
from dstability import verify
from fourier import certify
from positivity import certify_positive

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Do not run this verifier with Python -O.')
    verify()
    certify(method='python' if '--slow-matmul' in sys.argv else 'int64')
    certify_positive()
    print('\nALL EXACT CERTIFICATES PASSED.',flush=True)
