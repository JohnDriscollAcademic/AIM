"""Crouzeix-Raviart discretisation of the Steklov problem on the equilateral
triangle E (circumradius 1, side sqrt(3)), uniform mesh of n^2 equilateral
elements of side h = sqrt(3)/n.  All matrices are returned as INTEGER matrices:

    K = (2/sqrt(3)) * Kint ,   N = (h/3) * N3 ,
so that  K x = lam N x  <=>  Kint x = (lam/(2n)) N3 x.

Local CR basis on an element: phi_i = 1 - 2*lambda_i (lambda_i barycentric),
DOF i sits at the midpoint of the edge opposite vertex i.
"""
import itertools


def build(n):
    # lattice points (i,j), i,j>=0, i+j<=n ; P = V0 + i/n (V1-V0) + j/n (V2-V0)
    tris = []
    for i in range(n):
        for j in range(n - i):
            tris.append(((i, j), (i + 1, j), (i, j + 1)))          # up
            if i + j + 2 <= n:
                tris.append(((i + 1, j), (i, j + 1), (i + 1, j + 1)))  # down
    edges = {}
    def eid(a, b):
        key = (a, b) if a <= b else (b, a)
        if key not in edges:
            edges[key] = len(edges)
        return edges[key]
    elem_dofs = []
    for (a, b, c) in tris:
        # dof opposite vertex a is edge (b,c), etc.
        elem_dofs.append((eid(b, c), eid(a, c), eid(a, b)))
    def on_boundary(a, b):
        # sides: j==0 (V0V1), i==0 (V0V2), i+j==n (V1V2)
        return (a[1] == 0 and b[1] == 0) or (a[0] == 0 and b[0] == 0) or \
               (sum(a) == n and sum(b) == n)
    ndof = len(edges)
    Kint = {}
    N3 = {}
    def add(D, i, j, v):
        if v != 0:
            D[(i, j)] = D.get((i, j), 0) + v
    nbd_edges_per_elem = []
    for (a, b, c), dofs in zip(tris, elem_dofs):
        loc = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
        for p in range(3):
            for q in range(3):
                add(Kint, dofs[p], dofs[q], loc[p][q])
        verts = (a, b, c)
        nb = 0
        for p in range(3):
            # edge opposite vertex p
            e = [verts[q] for q in range(3) if q != p]
            if on_boundary(e[0], e[1]):
                nb += 1
                own = dofs[p]
                others = [dofs[q] for q in range(3) if q != p]
                add(N3, own, own, 3)
                add(N3, others[0], others[0], 1)
                add(N3, others[1], others[1], 1)
                add(N3, others[0], others[1], -1)
                add(N3, others[1], others[0], -1)
        nbd_edges_per_elem.append(nb)
    return ndof, Kint, N3, max(nbd_edges_per_elem), len(tris)


if __name__ == "__main__":
    import numpy as np
    from scipy.linalg import eigh
    for n in [4, 8, 12, 16, 24, 32]:
        ndof, Kint, N3, maxnb, ntri = build(n)
        K = np.zeros((ndof, ndof)); N = np.zeros((ndof, ndof))
        for (i, j), v in Kint.items(): K[i, j] = v
        for (i, j), v in N3.items(): N[i, j] = v
        # generalized eigen: Kint x = mu N3 x on boundary-supported part: use K + N shift
        ev = eigh(K, K + N, eigvals_only=True)  # c = mu/(1+mu) style; c=K/(K+N)
        # eigenvalue c of (K, K+N) -> mu = c/(1-c)
        ev = np.sort(ev)
        mu = ev[ev < 1 - 1e-12] / (1 - ev[ev < 1 - 1e-12])
        lam = mu * 2 * n
        h = np.sqrt(3) / n
        Ch2 = 2 * (2 / np.pi**2 + 2 / np.pi) * h * 2 / np.sqrt(3)
        l3 = lam[3]
        print(f"n={n:3d} ndof={ndof:5d} ntri={ntri} max bd edges/elem={maxnb} "
              f"CR lam1..4={lam[1]:.6f} {lam[2]:.6f} {lam[3]:.6f} {lam[4]:.6f}  Ch2={Ch2:.4f}  "
              f"rho=lam3/(1+Ch2 lam3)={l3/(1+Ch2*l3):.4f}")
