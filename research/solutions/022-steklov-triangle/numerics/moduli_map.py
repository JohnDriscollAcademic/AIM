"""Map sigma1*Per over the moduli space of triangles (NUMERICAL EVIDENCE ONLY).

Moduli coordinates: every triangle is similar to T_S = exp(S) E, where E is the
equilateral triangle with circumradius 1 (vertices at angles 90,210,330 deg)
and S = r [[cos p, sin p],[sin p, -cos p]] is symmetric traceless.
"""
import numpy as np
import sys
from stek import steklov_eigs, perimeter

E0 = np.array([np.exp(1j * (np.pi / 2 + 2 * np.pi * k / 3)) for k in range(3)])


def tri_S(r, p):
    Sh = np.array([[np.cos(p), np.sin(p)], [np.sin(p), -np.cos(p)]])
    A = np.cosh(r) * np.eye(2) + np.sinh(r) * Sh
    X = np.array([E0.real, E0.imag])
    Y = A @ X
    return Y[0] + 1j * Y[1]


def s1per(verts, K=30):
    ev = steklov_eigs(verts, K=K, nev=3)
    return ev[1] * perimeter(verts)


if __name__ == "__main__":
    out = []
    rs = [0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
    ps = np.linspace(0, 2 * np.pi, 25)[:-1]
    for r in rs:
        row = []
        for p in ps:
            v = tri_S(r, p)
            a = s1per(v, K=30)
            b = s1per(v, K=45)
            row.append((a, b))
        vals = np.array([b for a, b in row])
        err = max(abs(a - b) for a, b in row)
        print(f"r={r:5.2f}  min={vals.min():.8f}  max={vals.max():.8f}  conv(K30 vs45)={err:.1e}  argmax p={ps[vals.argmax()]:.3f}")
        sys.stdout.flush()
