"""Response-function sanity checks; no numerical existence certificate.

Run with Python and mpmath from this directory. Writes numerical-checks.json.
The proof itself uses analytic estimates, not these finite samples.
"""

from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 60
M0 = mp.quad(
    lambda z: mp.exp(z*z/2) * mp.sqrt(mp.pi/2)
    * (1 + mp.erf(z/mp.sqrt(2))), [-1, 0]
)
N0 = 1/M0
P = lambda w: N0 * mp.exp(-w*w/2) * mp.quad(
    lambda z: mp.exp(z*z/2), [max(w, mp.mpf(-1)), 0]
)


def response(lam):
    """Exact K via the decaying parabolic-cylinder solution of the OU ODE."""
    denominator = mp.pcfd(-lam, 0)
    h_reset = mp.exp(mp.mpf(1)/4) * mp.pcfd(-lam, 1)/denominator
    hprime_reset = -h_reset + mp.exp(mp.mpf(1)/4) * mp.pcfd(1-lam, 1)/denominator
    hprime_zero = mp.sqrt(2) * mp.gamma((lam+1)/2)/mp.gamma(lam/2)
    return N0*(hprime_zero-hprime_reset)/((lam+1)*(1-h_reset))


mass = mp.quad(P, [-mp.inf, -1, 0])
assert abs(mass-1) < mp.mpf('1e-45')
mprime = mp.quad(
    lambda z: -1-z*mp.sqrt(mp.pi/2)*mp.exp(z*z/2)
    * (1+mp.erf(z/mp.sqrt(2))), [-1, 0]
)
k_zero = -mprime/M0**2
assert k_zero > 0
samples = []
for omega in [20, 50, 100, 200, 500]:
    k = response(1j*omega)
    b = -1/abs(k)
    delta = (mp.arg(k)+mp.pi) % (2*mp.pi)
    critical_residual = abs(b*mp.exp(-1j*delta)*k-1)
    assert critical_residual < mp.mpf('1e-50')
    step = mp.mpf('0.01')
    derivative = (response(1j*(omega+step))-response(1j*(omega-step)))/(2*step)
    phase_derivative = mp.im(derivative/k)
    assert phase_derivative < 0
    asymptotic = N0*(1j*omega)**mp.mpf('-0.5')*(1-5/(4*1j*omega))
    samples.append({
        'omega': omega,
        'response_real': float(mp.re(k)),
        'response_imag': float(mp.im(k)),
        'relative_asymptotic_error': float(abs(k-asymptotic)/abs(k)),
        'omega_squared_phase_derivative': float(omega**2*phase_derivative),
        'b0': float(b), 'delta': float(delta),
        'd0': float(delta/omega), 'period0': float(2*mp.pi/omega),
        'V_F': float(b*N0), 'V_R': float(b*N0-1),
        'critical_residual': float(critical_residual),
    })

omega = 100
ratios = {str(n): float(abs(response(1j*n*omega))/abs(response(1j*omega)))
          for n in range(2, 65)}
assert max(ratios.values()) < 1
result = {
    'scope': 'Nonrigorous numerical sanity checks, not an existence or branch certificate',
    'mpmath_version': mp.__version__, 'decimal_precision': mp.mp.dps,
    'mean_hitting_time': float(M0), 'stationary_firing_rate': float(N0),
    'stationary_mass_error': float(abs(mass-1)), 'K_zero': float(k_zero),
    'phase_difference_step': '0.01',
    'expected_phase_limit': '-5/4', 'samples': samples,
    'sampled_harmonic_ratios_at_omega_100': ratios,
    'all_checks_passed': True,
}
Path(__file__).with_name('numerical-checks.json').write_text(
    json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n'
)
print(json.dumps({k: result[k] for k in [
    'stationary_firing_rate', 'stationary_mass_error', 'K_zero', 'all_checks_passed'
]}))
