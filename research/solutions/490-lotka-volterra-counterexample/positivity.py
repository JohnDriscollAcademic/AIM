"""Integer interval verification of positivity of the Fourier anchor.
No trigonometric library calls are used in the proof.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import numpy as np
from fourier import complex_parts
S=2**80

def ceildiv(a,b):return -((-a)//b)
def point(x):
    x=F(x);return (x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    p=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return (min(p)//S,ceildiv(max(p),S))
def divide(x,n):
    assert n>0;return (x[0]//n,ceildiv(x[1],n))
def scale(x,n):return (x[0]*n,x[1]*n) if n>=0 else (x[1]*n,x[0]*n)

def arctan_interval(q,n=40):
    """Alternating rational series brackets atan(1/q)."""
    assert q>1
    s=sum(((-1)**k*F(1,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0))
    t=s+(-1)**n*F(1,(2*n+1)*q**(2*n+1))
    return min(s,t),max(s,t)
def pi_bounds():
    a,b=arctan_interval(5);c,d=arctan_interval(239)
    return 16*a-4*d,16*b-4*c

def sincos(x):
    """Taylor polynomials through degree 35, plus rigorous remainders."""
    assert max(abs(x[0]),abs(x[1]))<4*S
    xx=mul(x,x);ct=(S,S);st=x;co=ct;si=st
    for j in range(1,18):
        ct=neg(divide(mul(ct,xx),(2*j-1)*(2*j)))
        st=neg(divide(mul(st,xx),(2*j)*(2*j+1)))
        co=add(co,ct);si=add(si,st)
    ec=ceildiv(4**36*S,factorial(36));es=ceildiv(4**37*S,factorial(37))
    # Cos degree34 has zero degree35 coefficient; sin degree35 has zero
    # degree36 coefficient, so these are valid Lagrange remainder bounds.
    return (co[0]-ec,co[1]+ec),(si[0]-es,si[1]+es)

def certify_positive(path=Path(__file__).with_name('fourier_certificate.npz'),grid=4096):
    z=np.load(path,allow_pickle=False);M=int(z['M']);Q=2**int(z['den_exp']);ints=z['coeffints']
    cr,ci=complex_parts(ints,M)
    rc=[[point(F(int(a),Q)) for a in row] for row in cr]
    ic=[[point(F(int(a),Q)) for a in row] for row in ci]
    pl,pu=pi_bounds();p=(point(pl)[0],point(pu)[1])
    lows=[None]*4;highs=[None]*4
    for j in range(grid):
        jj=j if j<=grid//2 else j-grid
        theta=divide(scale(p,2*jj),grid);co,si=sincos(theta)
        pr,pi=(S,S),(0,0)
        val=[add((S,S),rc[i][0]) for i in range(4)]
        for k in range(1,M+1):
            pr,pi=sub(mul(pr,co),mul(pi,si)),add(mul(pr,si),mul(pi,co))
            for i in range(4):
                val[i]=add(val[i],scale(sub(mul(rc[i][k],pr),mul(ic[i][k],pi)),2))
        for i in range(4):
            lows[i]=val[i][0] if lows[i] is None else min(lows[i],val[i][0])
            highs[i]=val[i][1] if highs[i] is None else max(highs[i],val[i][1])
    deriv=[F(2*sum(k*(abs(int(cr[i,k]))+abs(int(ci[i,k]))) for k in range(1,M+1)),Q) for i in range(4)]
    r=F(1,10**7)
    lower=[F(lows[i],S)-deriv[i]*pu/grid-r for i in range(4)]
    upper=[F(highs[i],S)+deriv[i]*pu/grid+r for i in range(4)]
    assert min(lower)>F(1,8)
    assert max(upper)<4
    # In the chosen norm, an individual nonzero Fourier real coefficient
    # changes by at most r/2. This proves the resulting solution is nonconstant.
    assert F(int(cr[0,1]),Q)-r/2>F(3,5)
    omega=F(int(ints[0]),Q)
    assert omega>r
    Tlo=2*pl/(omega+r);Thi=2*pu/(omega-r)
    assert Tlo>F(786959,100000) and Thi<F(786961,100000)
    print('EXACT POSITIVITY CERTIFICATE VERIFIED',flush=True)
    print('coordinate lower bounds',*[float(t) for t in lower],flush=True)
    print('coordinate upper bounds',*[float(t) for t in upper],flush=True)
    print('period between',float(Tlo),float(Thi),flush=True)
    print('Re c_{1,1} > 3/5',flush=True)
    out={'grid':grid,'fixedpoint_scale':S,'lower':[str(t) for t in lower],'upper':[str(t) for t in upper],'Tlo':str(Tlo),'Thi':str(Thi)}
    Path(__file__).with_name('positivity_bounds.json').write_text(json.dumps(out,indent=2))
    return out
if __name__=='__main__':
    if not __debug__:raise RuntimeError('Do not run this verifier with Python -O.')
    certify_positive()
