"""Regression tests: corrupted certificates and printed tables must fail, including -O."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent

class CertificateTests(unittest.TestCase):
    def test_corruptions_in_both_modes(self):
        original=json.loads((ROOT/'cubic_certificate.json').read_text(encoding='utf-8'))
        cases={}
        fractional=copy.deepcopy(original)
        fractional[0]['coefficient']='('+fractional[0]['coefficient']+')+1/2'
        cases['fractional']=fractional
        cases['missing']=original[:-1]
        cases['duplicate']=original[:-1]+original[:1]
        shifted=copy.deepcopy(original)
        shifted[0]['shifted_coefficients_ascending'][0]+=1
        cases['shifted']=shifted
        with tempfile.TemporaryDirectory() as td:
            for optimized in (False,True):
                for kind,records in cases.items():
                    path=Path(td)/f'{kind}.json'
                    path.write_text(json.dumps(records),encoding='utf-8')
                    scripts=['verify_cubic.py'] if kind=='shifted' else ['verify_cubic.py','crosscheck_cubic.py']
                    for script in scripts:
                        with self.subTest(optimized=optimized,kind=kind,script=script):
                            flag='--check-certificate' if script=='verify_cubic.py' else '--certificate'
                            args=[sys.executable]+(['-O'] if optimized else [])+[str(ROOT/script),flag,str(path)]
                            run=subprocess.run(args,capture_output=True,text=True)
                            self.assertNotEqual(run.returncode,0,run.stdout)
                            self.assertIn('ArithmeticError',run.stderr)

    def test_printed_table_damage(self):
        text=(ROOT/'aim641_report.tex').read_text(encoding='utf-8')
        damaged=text.replace('$(691,111)$','$(692,111)$')
        self.assertNotEqual(text,damaged)
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'damaged.tex'
            path.write_text(damaged,encoding='utf-8')
            run=subprocess.run([sys.executable,'-O',str(ROOT/'check_printed_table.py'),'--paper',str(path)],capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0)
            self.assertIn('Printed polynomial mismatch',run.stderr)

if __name__=='__main__': unittest.main(verbosity=2)
