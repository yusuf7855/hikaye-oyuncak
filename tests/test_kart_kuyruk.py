"""Kartın ürün parçaları (firmware/hikaye_oyuncak): hikâye kuyruğu (kuyruk.h), düğmeler (dugmeler.h) ve ikisinin
çizimle birlikte davranışı.

- tools/kuyruk_test.c: bellekte NOR flash taklidiyle kuyruk.h (doldurma politikası, yeniden başlatma, tüketme, CRC,
  imza, güç kesilmesi, aşınma).
- tools/dugme_test.c: sekme süzgeci, kısa/uzun basış, ikili basışlar, millis taşması.
- tools/kuyruk_test.py: çizimin kendisi (tools/kart_pc, sahte ESP32) ve dosyadaki sahte kuyruk bölümüyle doldur /
  çal / yeniden başlat / bozulma / düğmeler / NFC / uyku / kesme (K=3, figür başına 2; ~1 dakika).
"""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "firmware" / "hikaye_oyuncak" / "tools"
MODEL = ROOT / "hf_c3ft_karma" / "model.bin"


@unittest.skipUnless(shutil.which("cc"), "C derleyicisi yok")
class KuyrukDugmeC(unittest.TestCase):
    def kos(self, ad):
        with tempfile.TemporaryDirectory() as d:
            exe = Path(d) / ad
            subprocess.run(["cc", "-O2", "-Wall", "-o", str(exe), str(TOOLS / f"{ad}.c")], check=True)
            r = subprocess.run([str(exe)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout[-3000:])
            self.assertIn("hepsi geçti", r.stdout)

    def test_kuyruk(self):
        self.kos("kuyruk_test")

    def test_dugme(self):
        self.kos("dugme_test")


@unittest.skipUnless(shutil.which("g++") and MODEL.exists(), "g++ ya da hf_c3ft_karma/model.bin yok")
class KuyrukKart(unittest.TestCase):
    def test_kart_pc(self):
        r = subprocess.run([sys.executable, str(TOOLS / "kuyruk_test.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-4000:] + r.stderr[-2000:])
        self.assertIn("hepsi geçti", r.stdout)


if __name__ == "__main__":
    unittest.main()
