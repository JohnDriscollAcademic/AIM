"""Exact rational verification of D-stability, using a 21-term certificate.
Uses only the Python standard library. All decimals in the proof are exact.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import json
AINT=[[-224,-2551,-1969,454],[6814,-682,-1358,-11601],[7845,-808,-1695,-16707],[328,3248,5200,-685]]

def determinant(m):
    n=len(m);s=0
    for p in permutations(range(n)):
        v=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n):v*=m[i][p[i]]
        s+=v
    return s

def add(*polys):
    p={}
    for q in polys:
        for e,c in q.items():p[e]=p.get(e,F(0))+c
    return {e:c for e,c in p.items() if c}

def multiply(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            e=tuple(x+y for x,y in zip(a,b));r[e]=r.get(e,F(0))+c*d
    return {e:c for e,c in r.items() if c}

def scale(p,s):return {e:s*c for e,c in p.items()}

def polynomial():
    C=[None];minors={}
    for k in range(1,5):
        p={}
        for I in combinations(range(4),k):
            v=F(determinant([[-AINT[i][j] for j in I] for i in I]),1000**k)
            minors[I]=v;p[tuple(int(i in I) for i in range(4))]=v
        C.append(p)
    P=add(multiply(multiply(C[1],C[2]),C[3]),scale(multiply(C[3],C[3]),-1),scale(multiply(multiply(C[1],C[1]),C[4]),-1))
    return minors,P

def verify(path=Path(__file__).with_name('dstability_certificate.json')):
    z=json.loads(Path(path).read_text());assert z['Aint']==AINT and z['scale']==1000
    minors,P=polynomial();assert len(minors)==15 and min(minors.values())>0
    assert len(P)==38 and len(z['atoms'])==21
    rem=P.copy()
    for atom in z['atoms']:
        u,v,w=map(tuple,(atom['u'],atom['v'],atom['w']))
        a,b,c=F(atom['a']),F(atom['b']),F(atom['c'])
        assert len(u)==len(v)==len(w)==4
        assert all(isinstance(t,int) and t>=0 for t in (*u,*v,*w))
        assert sum(u)==sum(v)==sum(w)==6
        assert all(x+y==2*z for x,y,z in zip(u,v,w))
        assert a>0 and b>0 and c>0 and c*c<=4*a*b
        for e,t in [(u,a),(v,b),(w,-c)]:rem[e]=rem.get(e,F(0))-t
    assert set(rem)==set(P)
    assert all(rem[e]>=F(7,100)*abs(P[e]) for e in P)
    print('EXACT D-STABILITY CERTIFICATE VERIFIED',flush=True)
    print('All 15 principal minors of -A are positive.',flush=True)
    print('All 21 AM--GM inequalities and all 38 coefficient inequalities pass.',flush=True)
    print('Coefficientwise remainder >= (7/100)*absolute original coefficient.',flush=True)
    return True

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Do not run this verifier with Python -O.')
    verify()
