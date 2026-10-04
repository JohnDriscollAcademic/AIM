"""Independent exact multivariate expansion at M=8, without power-sum recursion."""
import json
import argparse
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sympy as sp
from pathlib import Path
def require(condition, message):
 if not condition: raise ArithmeticError(message)

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('cubic_certificate.json'))
args=parser.parse_args()
R,*v=ring('x0,x1,x2,x3,x4,x5,x6,z',QQ)
mu,z=v[:-1],v[-1]
M=8
q=[M]+[sum((x+z/M)**j for x in mu)+(z/M)**j for j in range(1,7)]
r=[M-1]+[sum(x**j for x in mu) for j in range(1,7)]
def deficit(p):
 S,p2,p3,p4,p5,p6=p[1:]
 return S**6-(54*p6+78*S*p5+29*S**2*p4-QQ(391,2)*p2*p4-18*S**3*p3-144*S*p2*p3+50*p3**2+QQ(9,4)*S**4*p2+QQ(47,2)*S**2*p2**2+QQ(487,4)*p2**3)
Q=4*M**5*(sum(mu)+z)**2*(deficit(q)-deficit(r))
table={}
symM=sp.Symbol('M')
records=json.loads(args.certificate.read_text(encoding='utf-8'))
require(len(records)==45, 'Expected 45 certificate records.')
for d in records:
 key=d['z_power'],tuple(d['partition'])
 require(key not in table, 'Repeated certificate key.')
 value=sp.sympify(d['coefficient'],locals={'M':symM}).subs(symM,M)
 require(value.is_Rational is True, 'Non-rational coefficient.')
 table[key]=QQ(int(value.p),int(value.q))
for e,c in Q.items():
 require(e[-1]>0, "Independent coefficient mismatch at source line 34")
 key=(e[-1],tuple(sorted((i for i in e[:-1] if i),reverse=True)))
 require(c==table[key], "Independent coefficient mismatch at source line 36")
 require(c>0, "Independent coefficient mismatch at source line 37")
require(set((e[-1],tuple(sorted((i for i in e[:-1] if i),reverse=True))) for e in Q)==set(table), "Independent coefficient mismatch at source line 38")
print(f'Independent polynomial-ring expansion: all {len(Q)} nonzero monomials and all 45 types agree exactly at M=8.')
