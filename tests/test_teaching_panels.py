"""Exercise every scenario and interactive controls against real lesson fixtures."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest
import matplotlib
matplotlib.use('Agg')

ROOT = Path(__file__).resolve().parents[1]


class TeachingPanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ns={}
        for session in range(7,17):
            with contextlib.redirect_stdout(io.StringIO()):
                cls.ns[session]=runpy.run_path(str(ROOT / f'examples/session-{session:02d}/demo.py'))

    def test_all_scenarios_and_expected_rejections(self):
        reject={7:{'wrong-hostname','unknown-root','missing-client','wrong-client-purpose'},
                9:{'altered-kem-ciphertext','truncated-kem-ciphertext','wrong-recipient','changed-aad'},
                10:{'missing-contribution','downgrade','unauthenticated'},
                11:{'changed-message','changed-context','wrong-key','truncated-signature','old-version'},
                12:{'wrong-kek','changed-context'},13:{'wrong-tenant','operator-decrypt','revoked-grant'},
                15:{'legacy-write','unknown-profile','retire'},16:{'cycle'}}
        for session,ns in self.ns.items():
            for case in ns['TEACHING_CASES'][session]:
                with self.subTest(session=session,case=case):
                    rows=list(ns['teaching_steps'](session,ns,case))
                    self.assertGreaterEqual(len(rows),2)
                    self.assertEqual(any(r['status']=='REJECT' for r in rows),case in reject.get(session,set()))

    def test_inspection_is_explicit_and_dropdown_resets(self):
        ns=self.ns[9]
        with contextlib.redirect_stdout(io.StringIO()):
            panel=ns['teaching_panel'](9,ns)
            self.assertEqual(panel['state']['rows'],[])
            panel['next'].click()
            self.assertEqual(len(panel['state']['rows']),1)
        output=io.StringIO()
        with contextlib.redirect_stdout(output): panel['inspect'].click()
        secret=panel['state']['rows'][0]['artifacts']['sender secret'][0]
        self.assertNotIn(secret.hex(),output.getvalue())
        with contextlib.redirect_stdout(io.StringIO()): panel['secret'].value=True
        output=io.StringIO()
        with contextlib.redirect_stdout(output): panel['inspect'].click()
        self.assertIn(secret.hex(),output.getvalue())
        with contextlib.redirect_stdout(io.StringIO()):
            panel['case'].value='wrong-recipient'
            self.assertFalse(panel['secret'].value)
            self.assertEqual(panel['state']['rows'],[])
            panel['all'].click()
            self.assertEqual(panel['state']['rows'][-1]['status'],'REJECT')
            panel['reset'].click()
            self.assertFalse(panel['next'].disabled)

    def test_grant_restored_and_exposure_is_visible(self):
        ns=self.ns[13]; before=set(ns['grants'])
        list(ns['teaching_steps'](13,ns,'revoked-grant'))
        self.assertEqual(ns['grants'],before)
        rows=list(ns['teaching_steps'](13,ns,'compromised-reader'))
        self.assertEqual(rows[-1]['status'],'EXPOSED')
        ns=self.ns[12]
        rows=list(ns['teaching_steps'](12,ns,'stolen-old-backup'))
        self.assertEqual(rows[-1]['artifacts']['plaintext'][0],ns['plaintext'])

    def test_planning_sensitivity_and_retirement_gate(self):
        ns=self.ns[16]
        final=lambda case,p:list(ns['teaching_steps'](16,ns,case,p))[-1]['artifacts']['finish times'][0]['rollout']
        self.assertEqual(final('baseline',0),12)
        self.assertEqual(final('verifier-delay',3),15)
        self.assertEqual(final('transport-delay',1),12)
        self.assertEqual(final('transport-delay',10),18)
        ns=self.ns[15]
        self.assertEqual(list(ns['teaching_steps'](15,ns,'backup-not-ready'))[-1]['status'],'BLOCKED')
        ns=self.ns[14]
        self.assertEqual(list(ns['teaching_steps'](14,ns,'unknown-principal'))[-1]['status'],'UNKNOWN')


if __name__ == '__main__': unittest.main()
