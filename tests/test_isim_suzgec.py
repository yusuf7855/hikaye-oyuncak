"""runtime/isim_suzgec.h: C birim testini derleyip koşar; urun_uret'in ad listeleri için birkaç temel kontrol."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "degerlendirme"))


class IsimSuzgecC(unittest.TestCase):
    @unittest.skipUnless(shutil.which("cc"), "C derleyicisi yok")
    def test_c_birim(self):
        with tempfile.TemporaryDirectory() as d:
            exe = os.path.join(d, "isim_suzgec_test")
            subprocess.run(["cc", "-O2", "-Wall", "-Werror", "-o", exe,
                            str(ROOT / "runtime" / "host_verify" / "isim_suzgec_test.c")], check=True)
            r = subprocess.run([exe], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class KadroAdlari(unittest.TestCase):
    def setUp(self):
        import urun_uret
        self.u = urun_uret

    def test_kendi_kadrosu_yasak_degil(self):
        yasak = set(self.u.kadro_disi("elsa"))
        for ad in ("Elsa", "Anna", "Olaf", "Kristoff", "Sven"):
            self.assertNotIn(ad, yasak)
        for ad in ("Niloya", "Pepee", "Şila", "Chase"):
            self.assertIn(ad, yasak)

    def test_ortak_isimler_yasak_degil(self):
        for f in self.u.FIGURLER:
            yasak = set(self.u.kadro_disi(f))
            self.assertNotIn("Ayı", yasak)       # 'Koca Ayı'nın parçası ama cümle başında sıradan kelime
            self.assertNotIn("Örümcek", yasak)   # 'Örümcek Adam'ın parçası
            self.assertNotIn("Anne", yasak)      # rol yanları hiçbir figürde yasak değil

    def test_yanlis_isim_kivrik_kesme(self):
        self.assertEqual(self.u.yanlis_isimler("Elsa, Niloya’nın elini tuttu.", "elsa"), ["Niloya"])
        self.assertEqual(self.u.yanlis_isimler("Timsah suya girdi.", "elsa"), [])


if __name__ == "__main__":
    unittest.main()
