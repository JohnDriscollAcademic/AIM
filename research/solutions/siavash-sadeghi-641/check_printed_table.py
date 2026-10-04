"""Compare every polynomial in the paper's printed table with the certificate."""
import argparse
import json
from pathlib import Path
import re
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def check(paper, certificate):
    records=json.loads(certificate.read_text(encoding='utf-8'))
    expected={(r['z_power'],tuple(r['partition'])):sp.sympify(r['coefficient']) for r in records}
    seen=set()
    M=sp.Symbol('M')
    for line in paper.read_text(encoding='utf-8').splitlines():
        match=re.fullmatch(r'(\d+) & \$(.*?)\$ & \$(.*?)\$ & \$\((.*?)\)\$\\\\',line)
        if not match:
            continue
        k,part,factor,values=match.groups()
        alpha=[]
        if part!=r'\varnothing':
            for token in part.strip('()').split(','):
                p=re.fullmatch(r'(\d+)(?:\^\{(\d+)\})?',token)
                if not p: raise ArithmeticError('Invalid partition in printed table.')
                alpha.extend([int(p[1])]*int(p[2] or 1))
        key=int(k),tuple(alpha)
        if key in seen or key not in expected: raise ArithmeticError('Repeated or unexpected table row.')
        seen.add(key)
        factor=factor.replace(r'\left','').replace(r'\right','')
        factor=re.sub(r'\^\{(\d+)\}',r'**\1',factor)
        factored=parse_expr(factor,local_dict={'M':M},transformations=standard_transformations+(implicit_multiplication_application,))
        coeffs=[int(a) for a in values.split(',')]
        if min(coeffs)<=0: raise ArithmeticError('Nonpositive printed coefficient.')
        actual=factored*sum(a*(M-8)**j for j,a in enumerate(coeffs))
        if sp.expand(actual-expected[key])!=0: raise ArithmeticError(f'Printed polynomial mismatch: {key}')
    if len(seen)!=45 or seen!=set(expected): raise ArithmeticError('Printed table is incomplete.')
    print('PASS: all 45 printed coefficient polynomials agree exactly with the certificate.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--paper',type=Path,default=Path(__file__).with_name('aim641_report.tex'))
    p.add_argument('--certificate',type=Path,default=Path(__file__).with_name('cubic_certificate.json'))
    a=p.parse_args()
    check(a.paper,a.certificate)
