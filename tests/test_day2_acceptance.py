"""Check that supplied lab acceptance checks reject insecure learner implementations."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Day2AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules = {}
        for slug in ('04-mini-pki', '05-pqc-channel', '06-pqc-signatures'):
            with contextlib.redirect_stdout(io.StringIO()):
                cls.modules[slug] = runpy.run_path(str(ROOT / 'labs' / ('lab-' + slug) / 'starter.py'))

    def test_tls_bypass_rejected(self):
        def bypass(hostname, required, present):
            return {'version': 'TLSv1.3', 'client_authenticated': required}
        with self.assertRaises(AssertionError):
            self.modules['04-mini-pki']['check_connection'](bypass)

    def test_constant_kdf_rejected(self):
        with self.assertRaises(AssertionError):
            self.modules['05-pqc-channel']['check_key'](lambda *args: bytes(32))

    def test_always_accept_signature_rejected(self):
        with self.assertRaises(AssertionError):
            self.modules['06-pqc-signatures']['check_verifier'](lambda *args: True)


if __name__ == '__main__':
    unittest.main()
