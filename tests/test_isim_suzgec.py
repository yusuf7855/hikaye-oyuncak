"""runtime/isim_suzgec.h: C birim testini derleyip koşar; urun_uret'in ad listeleri için birkaç temel kontrol."""
import os
import re
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


# Ürün sahibi (26 Ekim 2026): lisanslı figürler üründen çıktı; model onların adlarıyla eğitildi
LISANSLI = ["niloya", "masa", "pepee", "doru", "hayri", "sakir", "elsa", "chase", "orumcek_adam", "hello_kitty"]


class LisansliAdlarYasak(unittest.TestCase):
    """Seçilebilir figürler ürün listesi; çıkarılan lisanslı figürlerin adları ve adlı yanları isim süzgecinde ve
    seçicide yasak kalır (yeni figürün hikâyesinde "Niloya" çıkmasın), kart başlıkları da aynı listeyle kurulur."""

    def setUp(self):
        import urun_uret
        self.u = urun_uret

    def test_figur_listeleri(self):
        u = self.u
        self.assertEqual(u.FIGURLER, ["keloglan", "pamuk_prenses", "pinokyo", "alaaddin", "nasreddin_hoca", "bulut",
                                      "zipzip", "tontis", "bilge_baykus", "ejderha_yavrusu", "tek_boynuzlu_at", "bip",
                                      "fistik"])
        self.assertEqual(u.ESKI_FIGURLER, LISANSLI)
        self.assertEqual(u.ISIM_FIGURLER, u.FIGURLER + LISANSLI)
        for k in LISANSLI:
            self.assertNotIn(k, u.FIGURLER)

    def test_lisansli_adlar_her_urun_figurunde_yasak(self):
        u = self.u
        lisansli_adlar = set().union(*(u.figur_adlari(k) for k in LISANSLI))
        for ad in ("Niloya", "Maşa", "Pepee", "Doru", "Hayri", "Şakir", "Elsa", "Chase", "Örümcek Adam", "Hello Kitty",
                   "Kitty", "Murat", "Şila", "Anna", "Olaf", "Ryder", "Basri"):
            self.assertIn(ad, lisansli_adlar)
        for f in u.FIGURLER:
            yasak = set(u.kadro_disi(f))
            self.assertEqual(lisansli_adlar - yasak, set(), f)               # süzgeç (gen -Y, isim_suzgec.h)
            metin = f"{u.KARTLAR[f]['ad']['deger']} parka gitti. Niloya ve Elsa onu bekliyordu. Chase havladı."
            self.assertEqual(u.yanlis_isimler(metin, f), ["Chase", "Elsa", "Niloya"])
            puan, c = u.puanla({"metin": metin, "plan": None, "plan_bozuk": False, "bitti": True, "lp": 0.0}, f, "park")
            self.assertTrue(any("yanlış isim" in e for _, e in c), (f, c))   # seçici
        self.assertLessEqual(lisansli_adlar, u.TUM_ISIM)                     # sec.TUM_ISIM (uydurma ad sayılmaz)
        self.assertLessEqual(lisansli_adlar, u.TUM_AD)                       # kadro_cezalari ('kartta olmayan ad' değil)

    def test_eski_figur_hala_uretilebilir(self):
        """Eski modelle kıyas: --figur elsa (kartı durur); kendi kadrosu serbest, yeni figür adları yasak."""
        u = self.u
        yasak = set(u.kadro_disi("elsa"))
        self.assertTrue({"Anna", "Olaf"}.isdisjoint(yasak))
        self.assertTrue({"Niloya", "Keloğlan", "Pinokyo", "Pamuk Prenses", "Tek Boynuzlu At"} <= yasak)
        self.assertEqual(len(u.vakalar(["elsa"])), len(u.KARTLAR["elsa"]["yerler"]))

    def test_yeni_figur_adlari(self):
        """Yeni figürlerin adları öteki figürlerde yasak; çok kelimeli adların sıradan kelime parçaları (Tek, Prenses,
        Hoca, Baykuş ...) tek başına yasak değil; 'Bulut' ve 'Fıstık' kelime başı olabilir ('$': Bulutlar serbest)."""
        u = self.u
        yasak = set(u.kadro_disi("pinokyo"))
        for ad in ("Keloğlan", "Pamuk Prenses", "Alaaddin", "Nasreddin Hoca", "Nasreddin", "Bulut", "Zıpzıp", "Tontiş",
                   "Bilge Baykuş", "Ejderha Yavrusu", "Tek Boynuzlu At", "Bip", "Fıstık", "Balkız"):
            self.assertIn(ad, yasak)
        for ad in ("Pinokyo", "Gepetto", "Gepetto Usta"):
            self.assertNotIn(ad, yasak)
        for f in u.FIGURLER:
            for parca in ("Tek", "Prenses", "Hoca", "Baykuş", "Ejderha", "Yavrusu", "Usta", "Bilge", "Boynuzlu", "At"):
                self.assertNotIn(parca, u.kadro_disi(f), f)
        self.assertTrue(u.kelime_basi_mi("Bulut") and u.kelime_basi_mi("Fıstık"))
        self.assertEqual(u.yanlis_isimler("Bulutlar dağıldı. Tek başına yürüdü.", "pinokyo"), [])
        self.assertEqual(u.yanlis_isimler("Bulut'un tüyleri beyazdı.", "pinokyo"), ["Bulut"])
        self.assertEqual(u.yanlis_isimler("Bulut'un tüyleri beyazdı.", "bulut"), [])

    def test_kart_basliklari_ayni_liste(self):
        """generated/istemler.h (tools/basliklar.py) urun_uret'le aynı: figürler, süzgeç adları, ad kümeleri;
        çıkarılan figürler başlıklarda yok (figur_donanim.h dahil)."""
        u = self.u
        gen = ROOT / "firmware" / "hikaye_oyuncak" / "generated"
        h = (gen / "istemler.h").read_text(encoding="utf-8")

        def dizgeler(ad):
            govde = re.search(rf"\b{ad}\[[^\]]*\] = \{{(.*?)\}};", h, re.S).group(1).replace('" "', "")
            return [x.encode("latin-1").decode("unicode_escape").encode("latin-1").decode("utf-8")
                    for x in re.findall(r'"((?:[^"\\]|\\.)*)"', govde)]

        def sayilar(ad):
            govde = re.search(rf"\b{ad}\[[^\]]*\] = \{{(.*?)\}};", h, re.S).group(1)
            return [int(x) for x in govde.replace(",", " ").split()]
        self.assertEqual(dizgeler("FIGUR_KIMLIK"), u.FIGURLER)
        ad, off = dizgeler("SUZGEC_AD"), sayilar("SUZGEC_AD_OFF")
        for i, f in enumerate(u.FIGURLER):
            self.assertEqual(ad[off[i]:off[i + 1]], [a + ("$" if u.kelime_basi_mi(a) else "") for a in u.kadro_disi(f)])
            self.assertIn("Niloya", ad[off[i]:off[i + 1]])
        self.assertEqual(dizgeler("URUN_TUM_ISIM"), sorted(u.TUM_ISIM))
        self.assertEqual(dizgeler("URUN_TUM_AD"), sorted(u.TUM_AD))
        self.assertEqual(dizgeler("URUN_ISIM_KELIME"), sorted(u.ISIM_KELIME))
        d = (gen / "figur_donanim.h").read_text(encoding="utf-8")
        for k in LISANSLI:   # FIGUR_KIMLIK yukarıda; URUN_ISIM_KELIME'de küçük harfli adlar ("niloya") bilerek var
            self.assertNotIn(f'"{k}"', d)


if __name__ == "__main__":
    unittest.main()
