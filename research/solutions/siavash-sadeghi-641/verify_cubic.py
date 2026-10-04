#!/usr/bin/env python3
"""Exact verification of the all-dimensional cubic Fejer certificate.

Requirements: Python 3.10+, SymPy.  All checks use exact arithmetic and remain active under python -O.
This program independently checks the cardinal-polynomial identity in six
variables, checks the two-dimensional base decomposition, checks the four
finite induction steps, and proves the remaining induction uniformly by
nonnegative coefficients in the symbolic dimension M-8.
"""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import argparse
import sympy as s

def require(condition, message):
    if not condition:
        raise ArithmeticError(message)

p = s.symbols('p0:7')
z, M, u = s.symbols('z M u')

def kernel(q):
    """Sum of squares of homogeneous cubic cardinal polynomials."""
    S, q2, q3, q4, q5, q6 = q[1:7]
    return (54*q6 + 78*S*q5 + 29*S*S*q4 - s.Rational(391,2)*q2*q4
            -18*S**3*q3 -144*S*q2*q3 +50*q3*q3
            +s.Rational(9,4)*S**4*q2 +s.Rational(47,2)*S*S*q2*q2
            +s.Rational(487,4)*q2**3)

def deficit(xs):
    ps = [len(xs)] + [sum(x**j for x in xs) for j in range(1,7)]
    return ps[1]**6-kernel(ps)

@lru_cache(None)
def partitions(n, largest=None):
    if n == 0:
        return ((),)
    largest = min(n, n if largest is None else largest)
    return tuple((j,)+a for j in range(largest,0,-1)
                 for a in partitions(n-j, min(j,n-j)))

@lru_cache(None)
def power_coefficient(parts, alpha):
    """Coefficient of x**alpha in product_j sum_i x_i**parts[j]."""
    if not parts:
        return int(all(a == 0 for a in alpha))
    j = parts[0]
    total = 0
    for i, a in enumerate(alpha):
        if a >= j:
            beta = list(alpha)
            beta[i] -= j
            total += power_coefficient(parts[1:], tuple(beta))
    return total

def orbit_coefficients(poly, degree, max_length=None):
    buckets = {}
    for exps, coeff in poly.terms():
        parts = tuple(j for j,e in enumerate(exps[1:],1) for _ in range(e))
        buckets.setdefault(exps[0], []).append((parts,coeff))
    for k in range(1, degree+1):
        for alpha in partitions(degree-k):
            if max_length is not None and len(alpha) > max_length:
                continue
            c = sum(coeff*power_coefficient(parts,alpha)
                    for parts,coeff in buckets.get(k,[]))
            yield k, alpha, s.factor(c)

def checks():
    # Independent, direct expansion of the three cardinal-polynomial types.
    x = s.symbols('x0:6')
    S = sum(x)
    p2 = sum(t*t for t in x)
    rt5 = s.sqrt(5)
    card = [t*(12*t*t-12*S*t+3*S*S-p2)/2 for t in x]
    card += [5*x[i]*x[j]*((3+rt5)*x[i]/2+(3-rt5)*x[j]/2-S)
             for i in range(6) for j in range(6) if i != j]
    from itertools import combinations
    card += [27*x[i]*x[j]*x[k] for i,j,k in combinations(range(6),3)]
    require(s.expand(sum(t*t for t in card)-kernel([6]+[sum(t**j for t in x) for j in range(1,7)])) == 0, "Exact identity or positivity check at source line 78")
    print('PASS: direct cardinal sum-of-squares identity (six variables).')

    v,w = s.symbols('v w')
    require(s.expand(deficit([u,v])-12*u*v*(u*u-3*u*v+v*v)**2) == 0, "Exact identity or positivity check at source line 82")
    E = (104*(u**3+v**3)*w*w+106*(u*u*v+u*v*v)*w*w
         -27*(u**4+v**4)*w+522*(u**3*v+u*v**3)*w+405*u*u*v*v*w
         +108*(u**5+v**5)-351*(u**4*v+u*v**4)
         +1062*(u**3*v*v+u*u*v**3))
    base = (s.Rational(262,81)*(u*u-u*v+v*v)*w**4
            +12*u*v*(u*u-3*u*v+v*v)**2+s.Rational(2,27)*w*E)
    require(s.expand(deficit([u+w/3,v+w/3,w/3])-base) == 0, "Exact identity or positivity check at source line 89")
    require(all(c >= 0 for c in s.Poly(s.expand((u+v+w)**4*E),u,v,w).coeffs()), "Exact identity or positivity check at source line 90")
    print('PASS: base cases, dimensions one and two.')

    shifted = [M]+[
        sum(comb(j,i)*p[i]*(z/M)**(j-i) for i in range(1,j+1))
        + z**j/M**(j-1) for j in range(1,7)]
    D = (p[1]+z)**6-kernel(shifted)-p[1]**6+kernel(p)
    for m,r in [(4,8),(5,5),(6,3),(7,3)]:
        q = s.Poly(s.expand((p[1]+z)**r*D.subs(M,m)),z,*p[1:])
        coeffs = list(orbit_coefficients(q,6+r,m-1))
        require(all(c >= 0 for _,_,c in coeffs), "Exact identity or positivity check at source line 100")
        # At z=0 the difference vanishes identically.
        require(q.as_expr().subs(z,0) == 0, "Exact identity or positivity check at source line 102")
        print(f'PASS: dimension {m-1}, elevation {r}, {len(coeffs)} coefficient types.')

    q = s.Poly(s.expand(4*M**5*(p[1]+z)**2*D),z,*p[1:])
    require(q.as_expr().subs(z,0) == 0, "Exact identity or positivity check at source line 106")
    records = []
    for k,alpha,c in orbit_coefficients(q,8):
        shifted_c = s.Poly(s.expand(c.subs(M,u+8)),u)
        require(all(b >= 0 for b in shifted_c.all_coeffs()), "Exact identity or positivity check at source line 110")
        require(all(b.is_Integer for b in shifted_c.all_coeffs()), "Exact identity or positivity check at source line 111")
        records.append({'z_power':k,'partition':list(alpha),
                        'coefficient':str(c),
                        'shifted_coefficients_ascending':[int(shifted_c.nth(j)) for j in range(6)]})
    require(len(records) == 45, "Exact identity or positivity check at source line 115")
    print('PASS: all 45 symbolic coefficient types are nonnegative for M >= 8.')
    return records

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Write the derived certificate to this path.')
    parser.add_argument('--check-certificate', type=Path, default=Path(__file__).with_name('cubic_certificate.json'), help='Compare the entire saved certificate against the exact derivation.')
    args = parser.parse_args()
    records = checks()
    saved = json.loads(args.check_certificate.read_text(encoding='utf-8'))
    require(saved == records, 'Saved certificate differs from the exact symbolic derivation.')
    if args.output:
        args.output.write_text(json.dumps(records, indent=2)+'\n', encoding='utf-8')
    print('ALL EXACT CHECKS PASSED. Saved certificate agrees in full.')

if __name__ == '__main__':
    main()
