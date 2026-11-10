"""Kart seçicisi (firmware/hikaye_oyuncak/secici.h secici_urun_puanla, C) = degerlendirme/urun_uret.puanla (Python).

tools/secici_karsilastir.py --urun'u koşar: gerçek model adayları (ara model c3ft_v5a'nın ürün figürlerindeki adayları,
degerlendirme/urun_secici_v5a/m_v5a.json; tests/atolye_secici_vakalar.json ve varsa urun_kiyas_karma'nın c3ft_karma
adayları: bunlarda yalnız ürün figürlerininkiler, kart tabloları üründen çıkan figürleri taşımaz) ve bozulmuş sentetik
adaylar iki tarafta puanlanır; puan (1e-9), kural kural ceza ve vaka başına seçim aynı olmalı. Tablolar
generated/istemler.h'den (tools/basliklar.py).
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
YENI = ROOT / "degerlendirme" / "urun_secici_v5a" / "m_v5a.json"


@unittest.skipUnless(shutil.which("cc") and (ROOT / "degerlendirme" / "sozluk.pkl").exists() and VAKALAR.exists(),
                     "C derleyicisi, sözlük ya da vakalar yok")
class KartSeciciAyni(unittest.TestCase):
    def test_c_python_ayni(self):
        havuz = [str(y) for y in (YENI, VAKALAR, KARMA) if y.exists()]
        r = subprocess.run([sys.executable, str(ARAC), "--urun", "--sentetik", "1000", *havuz],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-3000:] + r.stderr[-2000:])
        self.assertIn("uyuşmazlık 0", r.stdout)


if __name__ == "__main__":
    unittest.main()
