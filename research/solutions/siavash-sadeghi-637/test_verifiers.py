"""Focused arithmetic and certificate-input regressions; standard library only.

These tests supplement the full certificate run, not the analytic proof.
"""
import copy
from fractions import Fraction as Q
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import verify_exact as exact
from verify_numeric import load_exact_certificate

ROOT = Path(__file__).resolve().parent


class VerifierTests(unittest.TestCase):
    def encloses(self, interval, value):
        self.assertLessEqual(Q(interval.lo, exact.D), value)
        self.assertGreaterEqual(Q(interval.hi, exact.D), value)

    def test_signed_rational_arithmetic(self):
        values = [Q(n, d) for n in (-17, -1, 0, 1, 19) for d in (1, 3, 10)]
        for a in values:
            ia = exact.I.q(a.numerator, a.denominator)
            self.encloses(ia, a)
            self.encloses(ia.sq(), a*a)
            for b in values:
                ib = exact.I.q(b.numerator, b.denominator)
                self.encloses(ia+ib, a+b)
                self.encloses(ia-ib, a-b)
                self.encloses(ia*ib, a*b)
                if b:
                    self.encloses(ia/ib, a/b)

    def test_interval_boundaries_and_domains(self):
        interval = exact.I(-2*exact.D, 3*exact.D)
        self.assertEqual(interval.sq(), exact.I(0, 9*exact.D))
        for divisor in (0, exact.I(-1, 1)):
            with self.assertRaises(ZeroDivisionError):
                exact.ONE/divisor
        with self.assertRaises(ValueError):
            exact.logi(exact.I.q(0))
        with self.assertRaises(ValueError):
            exact.I(1, 0)
        self.encloses(exact.expi(exact.I.q(0)), Q(1))
        self.encloses(exact.logi(exact.I.q(1)), Q(0))

    def test_certificate_parameters_match_exact_code(self):
        data = json.loads((ROOT/'certificate.json').read_text())
        self.assertEqual(exact.BITS, 192)
        self.assertEqual(exact.K, exact.I.q(9, 10))
        self.assertEqual(data['parameters'],
                         {'N': 2, 'rho': ['0', '0'], 'c': '1/2', 'K': '9/10', 'Kc': '9/20'})
        self.assertEqual(exact.COEFF, [exact.I.q(n, data['common_coefficient_denominator'])
                                      for n in data['coefficient_numerators']])
        self.assertEqual(data['drift_constant'], '7/10')
        self.assertEqual(data['grid'], {'first_index': 0, 'last_index': 5000,
                         'argument': 'j/1000', 'strict_upper_bound': '-9/10000'})

    def test_complete_record_accepted(self):
        self.assertEqual(load_exact_certificate(ROOT/'exact_results.json')['grid_checks'], 5001)

    def test_incomplete_or_malformed_records_rejected(self):
        record = json.loads((ROOT/'exact_results.json').read_text())
        cases = []
        for key, value in [('status', 'FAIL'), ('bits', 80), ('grid_checks', 1),
                           ('grid_start', 1), ('global_drift_inequality_certified', 1),
                           ('sample_residual_enclosures', {}), ('analytic_constant_checks', {})]:
            item = copy.deepcopy(record)
            item[key] = value
            cases.append(item)
        item = copy.deepcopy(record)
        item['sample_residual_enclosures']['0']['lower_numerator'] = '0'
        cases.append(item)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'invalid.json'
            for item in cases:
                path.write_text(json.dumps(item))
                with self.assertRaises(ValueError):
                    load_exact_certificate(path)

    def test_partial_cli_does_not_claim_global_proof(self):
        command = [sys.executable] + (['-O'] if sys.flags.optimize else [])
        command += [str(ROOT/'verify_exact.py'), '--start', '394', '--end', '394']
        data = json.loads(subprocess.check_output(command, text=True))
        self.assertFalse(data['global_drift_inequality_certified'])
        self.assertEqual(data['scope'], 'partial grid only')
        self.assertEqual(data['grid_checks'], 1)

    def test_invalid_cli_ranges_rejected(self):
        command = [sys.executable] + (['-O'] if sys.flags.optimize else [])
        for start, end in [('-1', '1'), ('2', '1'), ('0', '5001')]:
            result = subprocess.run(command+[str(ROOT/'verify_exact.py'), '--start', start,
                                     '--end', end], capture_output=True)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
