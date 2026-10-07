"""Negative checks and widget event tests for the Session 6 teaching tools."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PKIWalkthroughTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        helper = runpy.run_path(str(ROOT / 'src/crypto_workshop/day2.py'))
        cls.m = runpy.run_path(str(ROOT / 'src/crypto_workshop/pki_walkthrough.py'), init_globals=helper)

    def setUp(self):
        self.keys, self.certs = self.m['make_pki']()

    def test_failure_stage_and_no_later_acceptance(self):
        expected = {'unknown-root': 'Local trust anchor', 'missing-intermediate': 'Path available',
                    'expired': 'Validity time', 'wrong-purpose': 'Key use and EKU',
                    'wrong-identity': 'Expected identity', 'altered-signed-body': 'Issuer signatures',
                    'revoked': 'Leaf revocation', 'stale-crl': 'Leaf revocation',
                    'missing-crl': 'Leaf revocation', 'forged-crl': 'Leaf revocation',
                    'authorization-denied': 'Application permission'}
        for role in ('server', 'client'):
            rows, _ = self.m['validation_trace'](self.keys, self.certs, role, 'valid')
            self.assertTrue(all(r[1] == 'PASS' for r in rows))
            for scenario, stage in expected.items():
                with self.subTest(role=role, scenario=scenario):
                    rows, _ = self.m['validation_trace'](self.keys, self.certs, role, scenario)
                    failed = [i for i, row in enumerate(rows) if row[1] == 'FAIL']
                    self.assertEqual(len(failed), 1)
                    self.assertEqual(rows[failed[0]][0], stage)
                    self.assertTrue(all(row[1] == 'SKIP' for row in rows[failed[0] + 1:]))
        rows, _ = self.m['validation_trace'](self.keys, self.certs, 'client', 'missing-client')
        self.assertEqual(rows[0][1], 'FAIL')

    def test_crl_signature_time_and_issuer(self):
        for state in ('stale', 'future', 'bad-signature'):
            crl = self.m['make_teaching_crl'](self.keys, self.certs, state=state)
            self.assertFalse(self.m['crl_decision'](crl, self.certs['server'], self.certs['intermediate'])[0])
        crl = self.m['make_teaching_crl'](self.keys, self.certs)
        _, other = self.m['make_pki']()
        # Same issuer text but a different issuing key must not authenticate the CRL.
        self.assertFalse(self.m['crl_decision'](crl, self.certs['server'], other['intermediate'])[0])

    def test_revocation_is_serial_specific(self):
        crl = self.m['make_teaching_crl'](self.keys, self.certs, self.certs['client'].serial_number)
        self.assertFalse(self.m['crl_decision'](crl, self.certs['client'], self.certs['intermediate'])[0])
        self.assertTrue(self.m['crl_decision'](crl, self.certs['server'], self.certs['intermediate'])[0])

    def test_inspection_private_key_is_explicit(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.m['print_material'](self.keys, self.certs)
        self.assertIn('BEGIN CERTIFICATE', output.getvalue())
        self.assertNotIn('BEGIN PRIVATE KEY', output.getvalue())
        with contextlib.redirect_stdout(output):
            self.m['print_material'](self.keys, self.certs, 'client', True)
        self.assertIn('BEGIN PRIVATE KEY', output.getvalue())

    def test_widget_next_reset_and_role_events(self):
        with contextlib.redirect_stdout(io.StringIO()):
            controls = self.m['walkthrough_panel'](self.keys, self.certs)
            self.assertEqual(controls['state']['visible'], 0)
            controls['next'].click()
            self.assertEqual(controls['state']['visible'], 1)
            controls['scenario'].value = 'revoked'
            self.assertEqual(controls['state']['visible'], 0)
            controls['all'].click()
            self.assertEqual(controls['state']['visible'], 10)
            self.assertTrue(controls['next'].disabled)
            controls['role'].value = 'client'
            self.assertEqual(controls['state']['visible'], 0)
            self.assertIsNotNone(controls['state']['crl'].get_revoked_certificate_by_serial_number(self.certs['client'].serial_number))
            controls['crl_button'].click()
            controls['reset'].click()
            self.assertFalse(controls['next'].disabled)


if __name__ == '__main__':
    unittest.main()
