"""Independent AIM641 exact audit; no supplied verifier functions imported."""
from pathlib import Path
import hashlib, json, itertools, math, sys
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

ROOT = Path(__file__).resolve().parents[4] / "research" / "solutions" / "siavash-sadeghi-641"
def need(v, msg):
    if not v: raise ArithmeticError(msg)
def kernel(p):
    S,p2,p3,p4,p5,p6 = p
    return (54*p6 + 78*S*p5 + 29*S*S*p4 - QQ(391,2)*p2*p4
            -18*S**3*p3 -144*S*p2*p3 +50*p3*p3 +QQ(9,4)*S**4*p2
            +QQ(47,2)*S*S*p2*p2 +QQ(487,4)*p2**3)
def h_coords(coords):
    powers=[sum(x**j for x in coords) for j in range(1,7)]
    return powers[0]**6-kernel(powers)
def print_hashes():
    for name in ("aim641_report.tex","verify_cubic.py","check_printed_table.py",
                 "crosscheck_cubic.py","test_verifier.py","cubic_certificate.json"):
        raw=(ROOT/name).read_bytes()
        normalized=raw.replace(b"\r\n",b"\n")
        print("INPUT",name,"sha256",hashlib.sha256(raw).hexdigest(),
              "LF_sha256",hashlib.sha256(normalized).hexdigest())
print("Python",sys.version.split()[0],"SymPy",sp.__version__)
print_hashes()

# Cardinal values are recomputed from independently constructed nodes.
rt=sp.sqrt(5); t=(1+1/rt)/2
for n in (2,3,4):
    labels=[("v",i) for i in range(n)]
    labels += [("e",i,j) for i in range(n) for j in range(n) if i!=j]
    labels += [("f",*a) for a in itertools.combinations(range(n),3)]
    points=[]
    for lab in labels:
        q=[sp.Integer(0)]*n
        if lab[0]=="v": q[lab[1]]=1
        if lab[0]=="e": q[lab[1]],q[lab[2]]=t,1-t
        if lab[0]=="f":
            for i in lab[1:]: q[i]=sp.Rational(1,3)
        points.append(q)
    for col,q in enumerate(points):
        S=sum(q); p2=sum(x*x for x in q)
        vals=[q[i]*(12*q[i]**2-12*S*q[i]+3*S*S-p2)/2 for i in range(n)]
        vals += [5*q[i]*q[j]*((3+rt)*q[i]/2+(3-rt)*q[j]/2-S)
                 for i in range(n) for j in range(n) if i!=j]
        vals += [27*q[i]*q[j]*q[k] for i,j,k in itertools.combinations(range(n),3)]
        need(all(sp.expand(value)==int(row==col) for row,value in enumerate(vals)),
             "Cardinal failure")
    need(len(labels)==math.comb(n+2,3),"Cardinality")
    print("CARDINAL_MATRIX",n,len(labels),"identity")

# Expand the three contributions separately in abstract power sums.
S,p2,p3,p4,p5,p6=sp.symbols("S p2 p3 p4 p5 p6")
A=(3*S*S-p2)/2
vertex=36*p6-72*S*p5+(36*S*S+12*A)*p4-12*S*A*p3+A*A*p2
edge=25*(7*(p2*p4-p6)+2*(p3*p3-p6)-6*S*(p2*p3-p5)+S*S*(p2*p2-p4))
face=sp.Rational(243,2)*p2**3-sp.Rational(729,2)*p2*p4+243*p6
need(sp.expand(vertex+edge+face-kernel((S,p2,p3,p4,p5,p6)))==0,"Kernel grouping")
print("KERNEL_GROUPING exact vertex + unordered-edge-pair + face expansion")

# Direct polynomial low-dimensional bases and induction: no orbit recursion.
R,a,b,w=ring("a,b,w",QQ)
need(h_coords([a,b])==12*a*b*(a*a-3*a*b+b*b)**2,"H2")
E=(104*(a**3+b**3)*w*w+106*(a*a*b+a*b*b)*w*w-27*(a**4+b**4)*w
   +522*(a**3*b+a*b**3)*w+405*a*a*b*b*w+108*(a**5+b**5)
   -351*(a**4*b+a*b**4)+1062*(a**3*b*b+a*a*b**3))
base=QQ(262,81)*(a*a-a*b+b*b)*w**4+12*a*b*(a*a-3*a*b+b*b)**2+QQ(2,27)*w*E
need(h_coords([a+w/3,b+w/3,w/3])==base,"H3 decomposition")
elevated=(a+b+w)**4*E
need(all(c>=0 for c in elevated.values()),"E positivity")
print("BASE_DIMENSIONS_1_2",len(elevated),"elevated E monomials",
      "minimum",min(elevated.values()))
for n,r in ((4,8),(5,5),(6,3),(7,3)):
    names=",".join("a"+str(i) for i in range(n-1))+",z"
    data=ring(names,QQ); ringN=data[0]; xs=data[1:-1]; z=data[-1]
    direct=(sum(xs)+z)**r*(h_coords([x+z/n for x in xs]+[z/n])-h_coords(xs))
    need(all(e[-1]>0 for e in direct),"Constant-in-z term")
    need(all(c>=0 for c in direct.values()),"Finite induction positivity")
    types=set((e[-1],tuple(sorted((i for i in e[:-1] if i),reverse=True))) for e in direct)
    print("FINITE_INDUCTION",n,"elevation",r,"nonzero_monomials",len(direct),
          "nonzero_types",len(types),"minimum",min(direct.values()))

# Symbolic dimension, in a direct rational polynomial ring:
# Seven explicit mu coordinates; the other M-7 shifted coordinates equal z.
# Using y=M*x avoids rational-function arithmetic. Degree six support ensures
# that seven mu variables see every degree-eight term with positive z degree.
data=ring(",".join("a"+str(i) for i in range(7))+",z,M",QQ)
RR=data[0]; xs=data[1:8]; z,M=data[8:]
shifted=[sum((M*x+z)**j for x in xs)+(M-7)*z**j for j in range(1,7)]
scaled_h=shifted[0]**6-kernel(shifted)
numerator=4*(sum(xs)+z)**2*(scaled_h-M**6*h_coords(xs))
need(all(e[-1]>=1 for e in numerator),"Cleared dimension denominator")
direct=RR.from_dict({e[:-1]+(e[-1]-1,):c for e,c in numerator.items()})
group={}
for e,c in direct.items():
    need(e[-2]>0,"Uniform constant-in-z term")
    mu_z=e[:-1]
    bucket=group.setdefault(mu_z,{})
    bucket[e[-1]]=bucket.get(e[-1],QQ.zero)+c
dimension=sp.Symbol("M")
records=json.loads((ROOT/"cubic_certificate.json").read_text())
saved={(r["z_power"],tuple(r["partition"])):r for r in records}
need(len(saved)==45,"Certificate keys")
types={}
for exps,terms in group.items():
    key=(exps[-1],tuple(sorted((v for v in exps[:-1] if v),reverse=True)))
    if key in types: need(types[key]==terms,"Symmetric coefficients")
    else: types[key]=terms
need(set(types)==set(saved),"Uniform type completeness")
independent_records=[]
for key,terms in sorted(types.items()):
    coeff=sum(sp.Rational(c.numerator,c.denominator)*dimension**j for j,c in terms.items())
    need(sp.expand(coeff-sp.sympify(saved[key]["coefficient"]))==0,"Symbolic certificate mismatch")
    # Independent binomial transform instead of calling coefficient recursion.
    shifted_coeffs=[sum(sp.Rational(c.numerator,c.denominator)*math.comb(j,k)*8**(j-k)
                        for j,c in terms.items() if j>=k) for k in range(6)]
    need(all(c>0 for c in shifted_coeffs),"Strict uniform positivity")
    need(shifted_coeffs==saved[key]["shifted_coefficients_ascending"],"Shifted certificate mismatch")
    independent_records.append({"z_power":key[0],"partition":list(key[1]),
                                "coefficient":str(sp.expand(coeff)),
                                "shifted_coefficients_ascending":[int(c) for c in shifted_coeffs]})
print("UNIFORM_DIRECT_SYMBOLIC_EXPANSION",len(group),"mu-z monomials",len(types),
      "coefficient types, each agrees as a polynomial in M; all shifted coefficients strictly positive")
Path(__file__).with_name("independent-symbolic-certificate.json").write_text(
    json.dumps(independent_records,indent=2)+"\n",encoding="utf-8")
print("ALL INDEPENDENT EXACT CHECKS PASSED")
