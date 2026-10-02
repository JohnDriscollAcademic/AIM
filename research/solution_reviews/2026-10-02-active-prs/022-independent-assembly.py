"""Independent coordinate/quadrature check of the submitted integer CR matrices.

Usage: python -B 022-independent-assembly.py PATH_TO_022_STEKLOV_TRIANGLE
This floating-point cross-check supports, but does not replace, the exact audit.
"""
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

package = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("submitted_mesh", package / "certify/cr_mesh.py")
submitted = importlib.util.module_from_spec(spec)
spec.loader.exec_module(submitted)
n = 16
ndof, integer_k, integer_n, max_boundary, count = submitted.build(n)
vertices = np.array([[0.0, 1.0], [-np.sqrt(3)/2, -0.5], [np.sqrt(3)/2, -0.5]])

def point(v):
    i, j = v
    return vertices[0] + (i*(vertices[1]-vertices[0])+j*(vertices[2]-vertices[0]))/n

cells = []
for i in range(n):
    for j in range(n-i):
        cells.append(((i,j),(i+1,j),(i,j+1)))
        if i+j < n-1:
            cells.append(((i+1,j),(i,j+1),(i+1,j+1)))
edge_ids = {}
cell_ids = []
for cell in cells:
    ids = []
    for opposite in range(3):
        edge = tuple(sorted(cell[k] for k in range(3) if k != opposite))
        if edge not in edge_ids:
            edge_ids[edge] = len(edge_ids)
        ids.append(edge_ids[edge])
    cell_ids.append(ids)
K = np.zeros((ndof, ndof))
B = np.zeros_like(K)
total_area = 0.0
total_boundary = 0.0
nodes, weights = np.polynomial.legendre.leggauss(3)
for cell, ids in zip(cells, cell_ids):
    coords = np.array([point(v) for v in cell])
    interpolator = np.linalg.inv(np.column_stack((np.ones(3), coords)))
    delta = coords[1:]-coords[0]
    area = abs(np.linalg.det(delta))/2
    total_area += area
    gradients = -2*interpolator[1:, :]
    K[np.ix_(ids, ids)] += area*gradients.T@gradients
    for p in range(3):
        others = [q for q in range(3) if q != p]
        ends = [cell[q] for q in others]
        boundary = any(all(v[axis] == 0 for v in ends) for axis in [0,1]) or all(sum(v) == n for v in ends)
        if not boundary:
            continue
        a, b = coords[others]
        length = np.linalg.norm(b-a)
        total_boundary += length
        xy = a[None,:]+((nodes+1)/2)[:,None]*(b-a)[None,:]
        bary = np.column_stack((np.ones(3), xy))@interpolator
        values = 1-2*bary
        B[np.ix_(ids, ids)] += values.T@((length*weights/2)[:,None]*values)
expected_k = np.zeros_like(K)
expected_b = np.zeros_like(B)
for (i,j), value in integer_k.items():
    expected_k[i,j] = 2/np.sqrt(3)*value
for (i,j), value in integer_n.items():
    expected_b[i,j] = np.sqrt(3)/(3*n)*value
k_error = float(np.max(abs(K-expected_k)))
b_error = float(np.max(abs(B-expected_b)))
assert k_error < 1e-10 and b_error < 1e-12
assert abs(total_area-3*np.sqrt(3)/4) < 1e-12
assert abs(total_boundary-3*np.sqrt(3)) < 1e-12
assert len(cells) == count == 256 and len(edge_ids) == ndof == 408
eigenvalues = np.linalg.eigvalsh(K-1.96*B)
assert sum(eigenvalues < -1e-10) == 3 and sum(abs(eigenvalues) <= 1e-10) == 0
print(json.dumps(dict(elements=count, degrees_of_freedom=ndof,
    stiffness_max_error=k_error, boundary_mass_max_error=b_error,
    area_error=float(total_area-3*np.sqrt(3)/4),
    perimeter_error=float(total_boundary-3*np.sqrt(3)),
    numerical_inertia=[3,0,405],
    smallest_positive_shifted_eigenvalue=float(eigenvalues[3]),
    status="PASS: coordinate and boundary-quadrature assembly agrees with the integer matrices"),indent=2))
