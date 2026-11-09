"""degerlendirme/urun_uret.py seçici kuralları: kadro_cezalari ve takinti_cezasi.

Kurallar hakemlerin 740/1030 kıyasındaki en sık gerekçelerinden çıktı (degerlendirme/urun_kiyas_740_1030). Kabul
edilmiş (hakemlerden geçmiş) urun_v2 hikâyelerinde yanlış alarm oranı düşük kalmalı.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "degerlendirme"))
import urun_uret as u  # noqa: E402


def kabul_govdeleri(kimlik, veri="urun_v2"):
    yol = ROOT / "data" / veri / f"{kimlik}.txt"
    if not yol.exists():
        return []
    out = []
    for b in yol.read_text(encoding="utf-8").split("### ")[1:]:
        sat = b.strip().split("\n")
        out.append(" ".join(s for s in sat[1:] if not s.startswith("@")).strip())
    return out


class KadroKurallari(unittest.TestCase):
    def etiketler(self, metin, kimlik):
        return [e for _, e in u.kadro_cezalari(metin, kimlik)]

    def test_kendine_seslenme(self):
        m = 'Pepee topu buldu. "Teşekkürler, Pepee!" dedi Pepee. Sonra eve döndü.'
        self.assertTrue(any("kendine sesleniyor" in e for e in self.etiketler(m, "pepee")))

    def test_baskasina_seslenme_serbest(self):
        m = 'Pepee topu buldu. "Teşekkürler, Pepee!" dedi Şila. Sonra eve döndüler.'
        self.assertFalse(any("kendine sesleniyor" in e for e in self.etiketler(m, "pepee")))

    def test_ad_tekrari(self):
        self.assertTrue(any("'Elsa Elsa'" in e for e in self.etiketler("Elsa Elsa karlı dağa çıktı.", "elsa")))
        self.assertTrue(any("'Şakir Şakir'" in e for e in self.etiketler("Şakir ile Şakir parka gitti.", "sakir")))

    def test_kartta_olmayan_ad(self):
        e = self.etiketler("Niloya parkta Susie ile oynadı. Susie'nin topu vardı.", "niloya")
        self.assertTrue(any("kartta olmayan ad" in x and "Susie" in x for x in e))

    def test_kadro_ve_rol_adlari_serbest(self):
        e = self.etiketler("Niloya, Murat ve Babaannesi bahçedeydi. Babaanneciğim çok güzel dedi Niloya.", "niloya")
        self.assertFalse(any("kartta olmayan ad" in x for x in e))

    def test_takinti(self):
        m = " ".join(["Hayri havluyu aldı."] * 10)
        self.assertTrue(u.takinti_cezasi(m, "hayri"))
        self.assertFalse(u.takinti_cezasi("Hayri havluyu aldı ve kuruladı.", "hayri"))


class YanlisAlarm(unittest.TestCase):
    def olc(self, figurler, veri):
        n = alarm = 0
        for k in figurler:
            for g in kabul_govdeleri(k, veri):
                n += 1
                alarm += bool(u.kadro_cezalari(g, k) or u.takinti_cezasi(g, k))
        if n < 100:
            self.skipTest(f"{veri} verisi yok")
        self.assertLess(alarm / n, 0.06, f"{veri}: yanlış alarm {alarm}/{n}")

    def test_kabul_edilmis_hikayelerde_dusuk(self):
        """urun_v2 (hakemli 1030): eski lisanslı figürler ve Keloğlan (eğitim verisindeki figürler, ISIM_FIGURLER)."""
        self.olc(u.ISIM_FIGURLER, "urun_v2")

    def test_yeni_figurlerin_kabul_edilmis_hikayelerinde_dusuk(self):
        """urun_v5 (yeni 12 figürün kapıdan geçmiş hikâyeleri; 9 Kasım 2026'da ~12 bin hikâyede %2)."""
        self.olc(u.FIGURLER, "urun_v5")


if __name__ == "__main__":
    unittest.main()
