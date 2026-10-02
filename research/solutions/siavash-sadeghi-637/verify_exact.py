"""Certify the global Elo drift inequality for the AIM 637 counterexample.

Python 3.10+; standard library only.  All proof decisions use integers or
fractions.  No floating-point or platform transcendental routine is used.
See aim637_counterexample.pdf for the analytic implication from the finite
certificate to singularity of the invariant measure.  This is not a proof
assistant, a simulation of the chain, or an independent mathematical review.

Default run: python3 verify_exact.py --output exact_results.json
A --start/--end subrange certifies only the indicated portion of the grid.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import factorial
import argparse, json
from fractions import Fraction
from pathlib import Path
BITS=192
D=1<<BITS

def ceildiv(a:int,b:int)->int:
    if b<=0: raise ValueError('positive denominator required')
    return -((-a)//b)

@dataclass(frozen=True, slots=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError('invalid interval')
    @classmethod
    def q(cls,n:int,d:int=1)->'I':
        if d<=0: raise ValueError('positive denominator required')
        return cls(n*D//d,ceildiv(n*D,d))
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-asI(o)
    def __rsub__(self,o): return asI(o)+-self
    def __mul__(self,o):
        o=asI(o); p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(p)//D,ceildiv(max(p),D))
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,int):
            if o==0: raise ZeroDivisionError
            if o<0:return -self/(-o)
            return I(self.lo//o,ceildiv(self.hi,o))
        o=asI(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError('interval contains zero')
        if o.hi<0: return -self/(-o)
        inv=I(D*D//o.hi,ceildiv(D*D,o.lo))
        return self*inv
    def __rtruediv__(self,o): return asI(o)/self
    def sq(self):
        if self.lo>=0:return I(self.lo*self.lo//D,ceildiv(self.hi*self.hi,D))
        if self.hi<=0:return (-self).sq()
        return I(0,ceildiv(max(self.lo*self.lo,self.hi*self.hi),D))
    def dec(self,digits=25):
        def fmt(n,up):
            q=ceildiv(n*10**digits,D) if up else n*10**digits//D
            sign='-' if q<0 else ''; s=str(abs(q)).zfill(digits+1)
            return sign+s[:-digits]+'.'+s[-digits:]
        return [fmt(self.lo,False),fmt(self.hi,True)]

def asI(x):
    if isinstance(x,I):return x
    if isinstance(x,int):return I.q(x)
    raise TypeError('only exact integer/rational input allowed')

ONE=I.q(1)

def exp_nonnegative_endpoint(n:int)->I:
    if n<0:raise ValueError
    shift=0
    while ceildiv(n,1<<shift)>D//8: shift+=1
    z=I(n//(1<<shift),ceildiv(n,1<<shift))
    term=ONE; total=ONE
    for j in range(1,41):
        term=term*z/j
        total=total+term
    # Taylor tail: <= 2*(1/8)^41/41! < 1/D.
    if not (2*D < 8**41*factorial(41)):raise ArithmeticError('tail condition')
    total=I(total.lo,total.hi+1)
    for _ in range(shift):total=total.sq()
    return total

def exp_endpoint(n:int)->I:
    if n>=0:return exp_nonnegative_endpoint(n)
    return ONE/exp_nonnegative_endpoint(-n)

def expi(x:I)->I:
    a=exp_endpoint(x.lo)
    if x.lo==x.hi:return a
    b=exp_endpoint(x.hi)
    return I(a.lo,b.hi)

def atanh_series_twice(t:I)->I:
    if t.lo<0 or 5*t.hi>2*D:raise ArithmeticError('log series range')
    t2=t.sq(); term=t; total=t
    for j in range(1,100):
        term=term*t2
        total=total+term/(2*j+1)
    # 2*sum_{j>=100} t^(2j+1)/(2j+1) <=4*(2/5)^201 < 1/D.
    if not 4*2**201*D<5**201:raise ArithmeticError('log tail')
    total=2*total
    return I(total.lo,total.hi+1)

LN2=atanh_series_twice(I.q(1,3))

def log_endpoint(n:int)->I:
    if n<=0:raise ValueError('log domain')
    e=n.bit_length()-1-BITS
    if e>=0:y=I(n//(1<<e),ceildiv(n,1<<e))
    else:y=I(n<<(-e),n<<(-e))
    t=(y-1)/(y+1)
    return atanh_series_twice(t)+e*LN2

def logi(x:I)->I:
    a=log_endpoint(x.lo)
    if x.lo==x.hi:return a
    b=log_endpoint(x.hi)
    return I(a.lo,b.hi)

COEFF=[I.q(n,10000) for n in [152316,-650393,237867,-54616,149840,-31596]]
K=I.q(9,10)

def h_and_t(x:I):
    e=expi(2*x)
    t=(e-1)/(e+1)
    lc=logi(e+1)-x-LN2
    t2=t.sq()
    power=t2
    value=COEFF[0]*x.sq()+COEFF[1]*lc
    for j in range(2,6):
        value=value+COEFF[j]*power
        power=power*t2
    return value,t

def residual(x:I)->I:
    v,t=h_and_t(x)
    f=x-K*t
    vp,_=h_and_t(f+K); vm,_=h_and_t(f-K)
    g=logi(I.q(1,10)+K*t.sq())
    return g+I.q(7,10)-v+(vp+vm)/2

def verify_analytic_constants():
    """Check the rational constants used in the continuum and tail proofs."""
    checks = []
    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        checks.append(name)
    q = Fraction
    coefficients = [q(n,10000) for n in
                    [152316,-650393,237867,-54616,149840,-31596]]
    bounds = [16,66,24,6,15,4]
    check('all six coefficient bounds',
          all(abs(a)<b for a,b in zip(coefficients,bounds)))
    hp = 2*16*7+66+sum(b*m for b,m in zip(bounds[2:],[2,4,6,8]))
    hpp = 2*16+66+sum(b*m*(m+1) for b,m in zip(bounds[2:],[2,4,6,8]))
    check('h first derivative bound', hp == 484)
    check('h second derivative bound', hpp == 1280)
    d1, d2, dmin = q(9,5), q(18,5), q(1,10)
    gpp = d2/dmin+(d1/dmin)**2
    check('log derivative second derivative bound', gpp == 360)
    rpp = gpp+2*hpp+d1*hp
    check('residual curvature bound', rpp == q(18956,5) and rpp<4000)
    check('compact interpolation margin',
          -q(9,10000)+q(4000,8*1000**2) == -q(1,2500))
    check('tanh(5) lower bound via exponential Taylor sum',
          1+10+q(10**2,2)+q(10**3,6)>199)
    lower_quadratic = 2*q(9,10)*5*q(99,100)-2*q(9,10)**2
    tail = (coefficients[0]*lower_quadratic
            -abs(coefficients[1])*q(9,10)
            -sum(abs(a) for a in coefficients[2:]))
    check('global tail margin', tail == q(2555547,500000) and tail>q(7,10))
    check('tanh(2) lower bound', 1+4+q(4**2,2)+q(4**3,6)>19)
    check('exponential moment bound: exp(1.71)>4',
          1+q(171,100)+q(171,100)**2/2>4)
    check('exponential moment contraction',
          (q(100,91)+q(1,4))/2 == q(491,728) < q(3,4))
    check('exp Taylor remainder below one dyadic unit',
          2*D < 8**41*factorial(41))
    check('log Taylor remainder below one dyadic unit',
          4*2**201*D < 5**201)
    check('strict dimension gap: log(2)<7/10', LN2.hi*10 < 7*D)
    return {'checks':len(checks), 'passed':checks,
            'residual_curvature_bound':str(rpp),
            'compact_residual_upper_bound':'-1/2500',
            'tail_lower_bound_on_h_minus_Ph':str(tail)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start',type=int,default=0)
    parser.add_argument('--end',type=int,default=5000)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if not 0<=args.start<=args.end<=5000:
        parser.error('require 0 <= start <= end <= 5000')
    constants=verify_analytic_constants()
    worst=None
    where=None
    samples={}
    indices={0,1,394,500,1000,2000,3000,4000,4999,5000}
    for j in range(args.start,args.end+1):
        r=residual(I.q(j,1000))
        if r.hi*10000>=-9*D:
            raise ArithmeticError(f'grid certificate failed at {j}: {r.dec()}')
        if worst is None or r.hi>worst.hi:
            worst=r
            where=j
        if j in indices:
            samples[str(j)]={'lower_numerator':str(r.lo),
                             'upper_numerator':str(r.hi)}
    if worst is None:
        raise ArithmeticError('no grid points checked')
    full=(args.start==0 and args.end==5000)
    data={'status':'PASS',
          'scope':'complete global certificate' if full else 'partial grid only',
          'global_drift_inequality_certified':full,
          'bits':BITS,'grid_start':args.start,'grid_end':args.end,
          'grid_checks':args.end-args.start+1,
          'analytic_constant_checks':constants,
          'pointwise_threshold':'-9/10000',
          'largest_upper_endpoint_at_grid_index':where,
          'enclosure_at_that_index':worst.dec(),
          'ln2_enclosure':LN2.dec(),
          'sample_residual_enclosures':samples}
    encoded=json.dumps(data,indent=2)+'\n'
    print(encoded,end='')
    if args.output:
        args.output.write_text(encoded,encoding='utf-8')

if __name__=='__main__':
    main()
