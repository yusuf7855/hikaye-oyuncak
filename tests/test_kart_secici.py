"""Kart seçicisi (firmware/hikaye_oyuncak/secici.h secici_urun_puanla, C) = degerlendirme/urun_uret.puanla (Python).

tools/secici_karsilastir.py --urun'u koşar: gerçek model adayları (tests/atolye_secici_vakalar.json; varsa
urun_kiyas_karma'nın c3ft_karma adayları) ve bozulmuş sentetik adaylar iki tarafta puanlanır; puan (1e-9), kural kural
ceza ve vaka başına seçim aynı olmalı. Tablolar generated/istemler.h'den (tools/basliklar.py).
"""
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARAC = ROOT / "firmware" / "hikaye_oyuncak" / "tools" / "secici_karsilastir.py"
VAKALAR = Path(__file__).with_name("atolye_secici_vakalar.json")
KARMA = ROOT / "degerlendirme" / "urun_kiyas_karma" / "mkarma.json"


@unittest.skipUnless(shutil.which("cc") and (ROOT / "degerlendirme" / "sozluk.pkl").exists() and VAKALAR.exists(),
                     "C derleyicisi, sözlük ya da vakalar yok")
class KartSeciciAyni(unittest.TestCase):
    def test_c_python_ayni(self):
        havuz = [str(VAKALAR)] + ([str(KARMA)] if KARMA.exists() else [])
        r = subprocess.run([sys.executable, str(ARAC), "--urun", "--sentetik", "1000", *havuz],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-3000:] + r.stderr[-2000:])
        self.assertIn("uyuşmazlık 0", r.stdout)


if __name__ == "__main__":
    unittest.main()
