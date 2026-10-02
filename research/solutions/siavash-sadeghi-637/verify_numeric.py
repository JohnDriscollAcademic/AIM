"""Separate 80-digit numerical check of the Elo counterexample certificate.

Standard library only.  This script does not import verify_exact.py and uses
Decimal exp/ln, direct cosh/sinh formulas and analytic differentiation.
Its calculations are supplementary numerical checks, NOT interval proofs.
The global proof is in the PDF and verify_exact.py.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
import json
from pathlib import Path


def load_exact_certificate(exact_path: Path) -> dict:
    """Reject partial or malformed records before the expensive numerical run.

    This checks record completeness, not authenticity: rerun verify_exact.py
    to obtain a rigorous certificate from the supplied source.
    """
    exact = json.loads(exact_path.read_text(encoding='utf-8'))
    expected = {
        'status': 'PASS', 'scope': 'complete global certificate',
        'global_drift_inequality_certified': True, 'bits': 192,
        'grid_start': 0, 'grid_end': 5000, 'grid_checks': 5001,
        'pointwise_threshold': '-9/10000',
    }
    if not isinstance(exact, dict) or any(
        type(exact.get(key)) is not type(value) or exact[key] != value
        for key, value in expected.items()
    ):
        raise ValueError('require a complete 192-bit exact certificate')
    constants = exact.get('analytic_constant_checks', {})
    if not isinstance(constants, dict) or constants.get('checks') != 14:
        raise ValueError('require all 14 analytic constant checks')
    samples = exact.get('sample_residual_enclosures', {})
    indices = {'0', '1', '394', '500', '1000', '2000', '3000',
               '4000', '4999', '5000'}
    if not isinstance(samples, dict) or set(samples) != indices:
        raise ValueError('require all ten certified sample enclosures')
    for index, box in samples.items():
        if not isinstance(box, dict):
            raise ValueError(f'invalid sample enclosure: {index}')
        try:
            lo = int(box['lower_numerator'])
            hi = int(box['upper_numerator'])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f'invalid sample enclosure: {index}') from exc
        if lo > hi or hi * 10000 >= -9 * (1 << 192):
            raise ValueError(f'invalid sample enclosure: {index}')
    return exact


def run(exact_path: Path) -> dict:
    exact = load_exact_certificate(exact_path)
    with localcontext() as ctx:
        ctx.prec = 80
        D = Decimal
        k = D(9)/10
        beta = D(7)/10
        # Independently transcribed exact terminating decimals.
        a,b,c2,c4,c6,c8 = map(D, [
            '15.2316','-65.0393','23.7867','-5.4616','14.9840','-3.1596'])
        terms=[(2,c2),(4,c4),(6,c6),(8,c8)]
        def components(x: Decimal):
            ep, em = x.exp(), (-x).exp()
            ch, sh = (ep+em)/2, (ep-em)/2
            t, s2 = sh/ch, 1/(ch*ch)
            value = a*x*x+b*ch.ln()
            hp = 2*a*x+b*t
            hpp = 2*a+b*s2
            for m,c in terms:
                value += c*t**m
                hp += c*m*t**(m-1)*s2
                hpp += c*(m*(m-1)*(D(1) if m==2 else t**(m-2))*s2*s2-2*m*t**m*s2)
            d=1-k*s2
            dp=2*k*t*s2
            dpp=2*k*s2*(1-3*t*t)
            return value,hp,hpp,t,d,dp,dpp
        def residual_and_second(x: Decimal):
            value,hp,hpp,t,d,dp,dpp=components(x)
            center=x-k*t
            p=components(center+k)
            m=components(center-k)
            r=d.ln()+beta-value+(p[0]+m[0])/2
            rpp=dpp/d-(dp/d)**2-hpp+(p[2]+m[2])*d*d/2+(p[1]+m[1])*dp/2
            return r,rpp
        worst=None;where=None;max_second=D(0);checks=0
        values={}
        for j in range(10001):
            x=D(j)/2000
            r,rpp=residual_and_second(x)
            if r >= -D(9)/10000:
                raise ArithmeticError(f'numerical sign check failed at {x}')
            if abs(rpp)>=4000:
                raise ArithmeticError(f'curvature check failed at {x}')
            checks += 2
            max_second=max(max_second,abs(rpp))
            if worst is None or r>worst:
                worst,where=r,j
            if j%2==0:
                values[str(j//2)]=r
        denominator=D(2)**exact['bits']
        enclosure_checks=0
        for j,box in exact['sample_residual_enclosures'].items():
            lo=D(box['lower_numerator'])/denominator
            hi=D(box['upper_numerator'])/denominator
            if not lo<=values[j]<=hi:
                raise ArithmeticError(f'numerical value outside certified interval: {j}')
            enclosure_checks+=1
        # Check independently that the analytic formulas match differentiation
        # of the scalar residual at high precision (central second difference).
        eps=D('1e-18')
        diff_checks=0
        max_diff_error=D(0)
        for x in map(D,['0','0.394','0.9','1.8','3','5']):
            r,rpp=residual_and_second(x)
            rp,_=residual_and_second(x+eps)
            rm,_=residual_and_second(x-eps)
            fd=(rp-2*r+rm)/(eps*eps)
            err=abs(fd-rpp)
            if err>D('1e-29'):
                raise ArithmeticError(f'differentiation cross-check failed at {x}')
            max_diff_error=max(max_diff_error,err)
            diff_checks+=1
        # Supplementary tail samples; the PDF proves all tails analytically.
        tail_checks=0
        for x in map(D,['5','6','8','10','20','40']):
            r,_=residual_and_second(x)
            if r>=0:
                raise ArithmeticError(f'tail numerical check failed at {x}')
            tail_checks+=1
        return {
            'status':'PASS',
            'role':'supplementary numerical checks; not rigorous interval bounds',
            'decimal_precision':80,
            'grid_points_including_midpoints':10001,
            'grid_sign_checks':10001,
            'grid_curvature_checks':10001,
            'certified_enclosure_cross_checks':enclosure_checks,
            'finite_difference_cross_checks':diff_checks,
            'tail_sample_checks':tail_checks,
            'total_supporting_checks':checks+enclosure_checks+diff_checks+tail_checks,
            'largest_sampled_residual_at_x':str(D(where)/2000),
            'largest_sampled_residual':str(worst),
            'largest_sampled_absolute_second_derivative':str(max_second),
            'max_finite_difference_error':str(max_diff_error),
            'dimension_upper_bound_decimal':str(D(2).ln()/beta)
        }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact',type=Path,
                        default=Path(__file__).with_name('exact_results.json'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    data=run(args.exact)
    text=json.dumps(data,indent=2)+'\n'
    print(text,end='')
    if args.output:
        args.output.write_text(text,encoding='utf-8')

if __name__=='__main__':
    main()
