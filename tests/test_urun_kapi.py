"""Kusursuz veri hattı Adım 0 birim testleri (KUSURSUZ_VERI.md 'Hazırlık', geçme şartları 1, 3, 4).

  (1) bozucu'nun biçimsel kusurlarını kod kapıları %100 yakalar (her kusur, beklenen kapı kodunda).
  (3) Sade sözlüğün sha256'sı tokenizer ile eşleşir.
  (4) Aynı kayıt her zaman aynı dizgiyi verir (süreçler arası ve PYTHONHASHSEED'den bağımsız; altın sha1).
Ek: normalizasyon, kesme eki, K5 zaman kuralının sıfat-fiil/askıda ek ayrımı, K7 kanat/kanama, K9, K11,
semantik kanaryaların koddan geçmesi. Test tabanları aşağıdaki 7 elle yazılmış hikâyedir (kartlar henüz onaysız:
taslak_kart=True).

Koşma: .venv/bin/python -m unittest tests.test_urun_kapi -v
       URUN_YANLIS_ALARM=1 ile tr-tinystories 200 hikâyelik K5/K7 ölçümü de koşar (~10 sn).
"""
import json
import os
import random
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "degerlendirme"))

import bozucu  # noqa: E402
import kapi  # noqa: E402
import sade_sozluk  # noqa: E402
import urun_kayit as uk  # noqa: E402

TABANLAR = """\
### Tosbi | orman | baykuş
@plan: kırmızı balon yüksek bir dala takıldı | baykuştan yardım isteyip balonu indirdi
@tohum: tosbi-0001
Ormanda sakin bir sabah vardı. Tosbi yavaş yavaş yürürken kırmızı bir balon gördü. Rüzgar esti ve balon yüksek bir dala takıldı. Tosbi dala uzanamadı çünkü çok kısaydı. Önce sabırla bekledi ama balon inmedi. Sonra dalda oturan baykuşu gördü. "Baykuş, balonu bana verir misin?" diye sordu Tosbi. Baykuş kanatlarını açtı ve dala uçtu. Gagasıyla ipi tuttu ve balonu yavaşça aşağı indirdi. "Teşekkür ederim!" dedi Tosbi. Baykuş başını salladı. Tosbi ipi kabuğuna bağladı. Kırmızı balon Tosbi'nin kabuğunun üstünde sallandı.

### Niloya | ev | Murat
@plan: rüzgar resmi pencereden bahçeye uçurdu | ağabeyiyle bahçeyi arayıp resmi buldu
@tohum: niloya-0001
Niloya evde güzel bir resim çiziyordu. Resimde sarı bir güneş ve mavi bir çiçek vardı. Birden pencereden rüzgar esti. Kağıt uçtu ve bahçeye düştü. Niloya pencereye koştu ama resmi göremedi. "Murat, resmim kayboldu!" dedi Niloya. Murat hemen yanına geldi. "Merak etme, birlikte ararız," dedi. İkisi bahçeye çıktı. Niloya her yere baktı ve sorular sordu. "Çiçeklerin arasında mı? Çitin yanında mı?" Murat çitin yanında beyaz bir şey gördü. Resim oradaydı! Murat resmi Niloya'ya verdi. Niloya ağabeyine sarıldı.

### Chase | park | Skye
@plan: uçurtmanın ipi koptu ve uçurtma kayboldu | ipin kokusunu izleyip uçurtmayı çalının dibinde buldu
@tohum: chase-0001
Parkta rüzgarlı bir gün vardı. Chase ile Skye sarı bir uçurtma uçuruyordu. Birden ip koptu ve uçurtma çalıların arasına düştü. Skye her yere baktı ama uçurtmayı göremedi. "Uçurtmamız kayboldu," dedi Skye üzgün bir sesle. Chase burnunu yere yaklaştırdı. Uçurtmanın ipini kokladı ve kokuyu izledi. Çalıların arasında yavaşça yürüdü. Sonunda sarı uçurtmayı büyük bir çalının dibinde buldu. "Buldum!" dedi Chase. Skye sevinçle kuyruğunu salladı. İki arkadaş uçurtmayı yeniden uçurdu. Chase'in burnu yine işe yaramıştı.

### Örümcek Adam | park | Spin
@plan: rüzgar şapkayı yüksek bir dala taşıdı | ağ atıp şapkayı yavaşça aşağı çekti
@tohum: orumcek_adam-0001
Parkta güneşli bir gündü. Örümcek Adam ile Spin çiçek bahçesinin yanında yürüyordu. Birden rüzgar esti ve Spin'in şapkası uçtu. Şapka yüksek bir dala takıldı. "Şapkamı nasıl alacağız?" diye sordu Spin. Örümcek Adam elini kaldırdı ve ağ attı. Ağ şapkaya sıkıca yapıştı. Örümcek Adam ağı yavaşça çekti. Şapka dallardan kurtuldu ve aşağı indi. Spin şapkasını başına taktı. "Çok teşekkür ederim," dedi Spin. İki arkadaş bahçede yürümeye devam etti. Örümcek Adam'ın ağı bugün de işe yaramıştı.

### Pamuk | deniz | -
@plan: dalga geldi ve havuç sepeti devrildi | havuçları tek tek toplayıp sepete koydu
@tohum: pamuk-0001
Deniz kıyısında hava serin ve güneşliydi. Pamuk kumların üstünde zıplayarak oynuyordu. Yanında küçük bir sepet dolusu havuç vardı. Birden büyük bir dalga geldi ve sepet devrildi. Havuçlar kumun üstüne dağıldı. Pamuk üzüldü ama hemen işe başladı. Havuçları tek tek topladı. Bir havuç suyun kenarına kadar gitmişti. Pamuk dalganın geri çekilmesini bekledi. Sonra hızla koştu ve havucu aldı. Bütün havuçlar yeniden sepetteydi. Pamuk'un uzun kulakları sevinçle kalktı. Sepeti aldı ve kumların üstünde neşeyle zıpladı.

### Keloğlan | dağ | Balkız
@plan: bir taşa takıldı ve elmalar yuvarlandı | sepeti yokuşun altına koyup elmaları topladılar
@tohum: keloglan-0001
Keloğlan ile Balkız tepede yürüyordu. Keloğlan'ın elinde kırmızı elmalarla dolu bir sepet vardı. Keloğlan biraz sakardı. Bir taşa takıldı ve sepet elinden kaydı. Elmalar yokuş aşağı yuvarlandı. "Elmalar kaçıyor!" dedi Balkız. Keloğlan önce durdu ve düşündü. Sonra aklına bir fikir geldi. Yokuşun altına yürüdü ve sepeti yere koydu. Balkız elmaları yavaşça sepete doğru itti. Elmalar teker teker sepete girdi. Keloğlan son elmayı da aldı. İki arkadaş sepeti birlikte taşıdı ve güldü.

### Elsa | şato | Olaf
@plan: olafın havucu karın içinde kayboldu | buzdan kürek yapıp karı kenara itti
@tohum: elsa-0001
Şatonun bahçesinde güzel bir kış günüydü. Elsa ile Olaf kardan bir kule yapıyordu. Olaf'ın havucu birden yere düştü ve karın içinde kayboldu. "Burnum nerede?" diye sordu Olaf. Elsa karın içine dikkatle baktı. Havuç hiçbir yerde yoktu. Elsa ellerini kaldırdı ve buzdan küçük bir kürek yaptı. Kürekle karı yavaşça kenara itti. Sonunda turuncu havucu buldu. Elsa havucu Olaf'ın yüzüne taktı. "Teşekkürler Elsa!" dedi Olaf. İkisi birlikte kuleyi bitirdi. Elsa'nın buzdan küreği güneşte parladı.
"""
TOHUMLAR = [
    {"id": "tosbi-0001", "figur": "Tosbi", "yer": "orman", "yan": ["baykuş"], "ozellik": "sabır",
     "isim": "balon", "fiil": "bekle-", "sifat": "kırmızı"},
    {"id": "niloya-0001", "figur": "Niloya", "yer": "ev", "yan": ["Murat"], "ozellik": "soru",
     "isim": "resim", "fiil": "ara-", "sifat": "beyaz"},
    {"id": "chase-0001", "figur": "Chase", "yer": "park", "yan": ["Skye"], "ozellik": "koku",
     "isim": "uçurtma", "fiil": "kokla-", "sifat": "sarı"},
    {"id": "orumcek_adam-0001", "figur": "Örümcek Adam", "yer": "park", "yan": ["Spin"], "ozellik": "ağ",
     "isim": "şapka", "fiil": "çek-", "sifat": "yüksek"},
    {"id": "pamuk-0001", "figur": "Pamuk", "yer": "deniz", "yan": [], "ozellik": "havuç",
     "isim": "sepet", "fiil": "topla-", "sifat": "küçük"},
    {"id": "keloglan-0001", "figur": "Keloğlan", "yer": "dağ", "yan": ["Balkız"], "ozellik": "sakar",
     "isim": "elma", "fiil": "taşı-", "sifat": "kırmızı"},
    {"id": "elsa-0001", "figur": "Elsa", "yer": "şato", "yan": ["Olaf"], "ozellik": "buz",
     "isim": "havuç", "fiil": "bul-", "sifat": "turuncu"},
]
# Altın değerler: serileştirme ya da normalizasyon değişirse bu test düşer; o zaman urun_kayit.SURUM artırılır ve
# K1, K4 ve sha1 bütün veriye yeniden koşulur (KUSURSUZ_VERI.md Adım 2 geçme şartı).
ALTIN_SHA1 = {"tosbi-0001": "7dd4a4d9ce71e95bbe7215aa99af8e15d3795506",
              "pamuk-0001": "6d13e63143b48258b1647f42f33388f5ab038b2d"}
ALTIN_PAMUK_PLANSIZ_BAS = "Karakter: Pamuk | Yer: deniz\n\nDeniz kıyısında hava serin ve güneşliydi."

_BG = None


def baglam():
    global _BG
    if _BG is None:
        _BG = kapi.Baglam()
    return _BG


def tabanlar():
    t = {x["id"]: x for x in TOHUMLAR}
    return [(b, uk.kayit(b), t[b["tohum"]]) for b in uk.ayristir(TABANLAR)]


def kodlar(sonuc):
    return {x["kod"] for x in sonuc["ihlaller"]}


class TabanlarGecer(unittest.TestCase):
    def test_tabanlar_butun_kapilardan_gecer(self):
        bg = baglam()
        for blok, _, tohum in tabanlar():
            s = kapi.denetle(blok, tohum, bg, taslak_kart=True)
            self.assertTrue(s["gecti"], f"{s['kimlik']}: {s['ihlaller']}")
            if bg.zemberek is None:                    # Zemberek yoksa çözümleme açıkça 'atlanan' olarak yazılır
                self.assertIn("K5.cozumleme", {x["kod"] for x in s["atlanan"]})


class Bicimsel(unittest.TestCase):
    """Geçme şartı (1): biçimsel kusurlar %100 yakalanır, hem de beklenen kapıda."""

    def test_bicimsel_kusurlarin_hepsi_beklenen_kapida(self):
        bg = baglam()
        rng = random.Random(2026)
        uygulanan, kacan, uygulanmayan = 0, [], []
        for _, kayit, tohum in tabanlar():
            for tur, beklenen in bozucu.BICIMSEL.items():
                r = bozucu.bicimsel(kayit, tohum, tur, bg, rng, taslak_kart=True)
                if r is None:
                    uygulanmayan.append((kayit["figur"], tur))
                    continue
                aday, aciklama, _, s = r
                self.assertNotEqual(aday["govde"], kayit["govde"])
                bek = {beklenen} if isinstance(beklenen, str) else set(beklenen)
                uygulanan += 1
                if not kodlar(s) & bek:
                    kacan.append((kayit["figur"], tur, aciklama, sorted(kodlar(s))))
        self.assertEqual(kacan, [])
        self.assertEqual(uygulanmayan, [])
        self.assertEqual(uygulanan, len(bozucu.BICIMSEL) * len(TOHUMLAR))

    def test_tasarimdaki_ornekler(self):
        """Tasarımın saydığı örnekler birebir: 'Tosbi'nın', 'koşdu', 'ertesi sabah', 'hastaydı', 'keçi'."""
        bg = baglam()
        blok, kayit, tohum = tabanlar()[0]
        ornekler = {
            "Kırmızı balon Tosbi'nin kabuğunun": ("Kırmızı balon Tosbi'nın kabuğunun", "K5.kesme_eki"),
            "Tosbi dala uzanamadı": ("Tosbi dala koşdu ve uzanamadı", "K5.sertlesme"),
            "Önce sabırla bekledi": ("Ertesi sabah sabırla bekledi", "K1.zaman"),
            "Baykuş başını salladı.": ("Baykuş biraz hastaydı.", "K7.saglik"),
            "Sonra dalda oturan baykuşu gördü.": ("Sonra dalda oturan keçiyi gördü.", "K4.canli_rol"),
            "Baykuş kanatlarını açtı ve dala uçtu.": ("Baykuş kanatlarını açıyor ve dala uçuyor.", "K5.zaman"),
            "Tosbi ipi kabuğuna bağladı.": ("Tosbi ipi kabuğuna bağlamış.", "K5.zaman"),
            "Önce sabırla bekledi ama": ("Önce hâlâ sabırla bekledi ama", "K3.sapka"),
        }
        for eski, (yeni, kod) in ornekler.items():
            k = dict(kayit, govde=kayit["govde"].replace(eski, yeni))
            self.assertNotEqual(k["govde"], kayit["govde"], eski)
            s = kapi.denetle(k, tohum, bg, taslak_kart=True)
            self.assertIn(kod, kodlar(s), f"{yeni}: {s['ihlaller']}")


class Kanarya(unittest.TestCase):
    def test_kanaryalar_koddan_gecer_ve_tek_degisiklik(self):
        bg = baglam()
        rng = random.Random(7)
        uretilen = 0
        for lens in bozucu.TURLER:
            for _, kayit, tohum in tabanlar():
                atilan = []
                k = bozucu.kanarya(kayit, tohum, lens, bg, rng, taslak_kart=True, atilan=atilan)
                if k is None:
                    continue
                uretilen += 1
                self.assertEqual(k["ad_alani"], "kanarya")
                self.assertTrue(k["kimlik"].startswith("urun/"))       # hakeme gerçek hikâye biçiminde gider
                self.assertNotEqual(k["sha1"], k["taban_sha1"])
                self.assertIn(k["tur"], bozucu.TURLER[lens])
                s = kapi.denetle(k["kayit"], tohum, bg, taslak_kart=True)
                self.assertTrue(s["gecti"], s["ihlaller"])
                for t, kod in atilan:                                  # atılan adaylar gerçekten koda takılmıştı
                    self.assertTrue(kod, t)
        self.assertGreaterEqual(uretilen, 3 * len(TOHUMLAR) - 2)

    def test_bicimsel_turler_kanarya_olamaz(self):
        for lens, turler in bozucu.TURLER.items():
            self.assertFalse(set(turler) & set(bozucu.BICIMSEL), lens)


class Serilestirme(unittest.TestCase):
    """Geçme şartı (4): aynı kayıt her zaman aynı dizgiyi verir."""

    def test_ayni_kayit_ayni_dizgi(self):
        a = [uk.kayit(b) for b in uk.ayristir(TABANLAR)]
        b = [uk.kayit(b) for b in uk.ayristir(TABANLAR)]
        for x, y in zip(a, b):
            self.assertEqual(uk.dizgiler(x), uk.dizgiler(y))
            self.assertEqual(uk.sha1(x), uk.sha1(y))

    def test_altin_sha1_ve_dizgi(self):
        for blok, kayit, _ in tabanlar():
            if blok["tohum"] in ALTIN_SHA1:
                self.assertEqual(uk.sha1(kayit), ALTIN_SHA1[blok["tohum"]])
        pamuk = [k for b, k, _ in tabanlar() if b["tohum"] == "pamuk-0001"][0]
        self.assertTrue(uk.dizgi(pamuk, plan=False).startswith(ALTIN_PAMUK_PLANSIZ_BAS))
        self.assertEqual(uk.dizgi(pamuk, True, True), uk.dizgi(pamuk, True, False))   # yansız: Yan alanı yok

    def test_dort_bicim_ayni_kaydin_alt_kumesi(self):
        _, kayit, _ = tabanlar()[0]
        d = uk.dizgiler(kayit)
        self.assertEqual(d[(True, True)],
                         "Karakter: Tosbi | Yer: orman | Yan: baykuş\nSorun: " + kayit["sorun"] + "\nÇözüm: "
                         + kayit["cozum"] + "\n\n" + kayit["govde"])
        self.assertEqual(d[(True, False)], d[(True, True)].replace(" | Yan: baykuş", ""))
        self.assertEqual(d[(False, True)], "Karakter: Tosbi | Yer: orman | Yan: baykuş\n\n" + kayit["govde"])
        self.assertEqual(d[(False, False)], "Karakter: Tosbi | Yer: orman\n\n" + kayit["govde"])

    def test_prepare_ft2_baslik_ile_ayni_iskelet(self):
        sys.path.insert(0, str(ROOT))
        try:
            from research.tinystories import prepare_ft2
        except Exception as e:    # pragma: no cover
            self.skipTest(f"prepare_ft2 yüklenemedi: {e}")
        elsa = [k for b, k, _ in tabanlar() if b["tohum"] == "elsa-0001"][0]
        if "Elsa" not in prepare_ft2.SIRA:
            self.skipTest("prepare_ft2.SIRA'da Elsa yok")
        h = {"turler": ["Elsa"], "yer": elsa["yer"], "metin": elsa["govde"]}
        self.assertEqual(prepare_ft2.baslik(h, plan=(elsa["sorun"], elsa["cozum"])),
                         uk.dizgi(elsa, plan=True, yan_alani=False))
        self.assertEqual(prepare_ft2.baslik(h), uk.dizgi(elsa, plan=False, yan_alani=False))

    def test_surecler_arasi_ve_hash_tohumundan_bagimsiz(self):
        kod = ("import sys, json; sys.path.insert(0, 'degerlendirme'); import urun_kayit as uk; "
               "from tests.test_urun_kapi import TABANLAR; "
               "print(json.dumps([[uk.sha1(k), uk.dizgi(k, p, y)] for k in map(uk.kayit, uk.ayristir(TABANLAR)) "
               "for p in (0, 1) for y in (0, 1)], ensure_ascii=False))")
        ciktilar = set()
        for tohum in ("0", "1", "12345"):
            env = dict(os.environ, PYTHONHASHSEED=tohum)
            r = subprocess.run([sys.executable, "-c", kod], cwd=ROOT, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            ciktilar.add(r.stdout)
        self.assertEqual(len(ciktilar), 1)

    def test_yazar_dosyasi_gidis_donus(self):
        for blok, kayit, _ in tabanlar():
            geri = uk.ayristir(uk.blok_yaz(kayit, blok["tohum"]))[0]
            self.assertEqual(uk.kayit(geri), kayit)
            self.assertEqual(geri["bicim_hatalari"], [])
        b = uk.ayristir("### Tosbi | orman | -\n@tohum: x\n@plan: a b c | d e f\nGövde.")[0]
        self.assertTrue(b["bicim_hatalari"])                                   # sıra yanlış

    def test_planli_mi_deterministik_ve_oran(self):
        _, kayit, _ = tabanlar()[0]
        s = uk.sha1(kayit)
        self.assertEqual([uk.planli_mi(s, i) for i in range(50)], [uk.planli_mi(s, i) for i in range(50)])
        n = sum(uk.planli_mi(f"{i:040x}", k) for i in range(2000) for k in range(5))
        self.assertAlmostEqual(n / 10000, 0.7, delta=0.02)

    def test_kimlik(self):
        _, kayit, _ = tabanlar()[3]
        self.assertTrue(uk.kimlik(kayit).startswith("urun/orumcek_adam#"))
        self.assertEqual(len(uk.kimlik(kayit).split("#")[1]), 10)
        with self.assertRaises(ValueError):
            uk.kanonik_json(dict(kayit, tema="paylaşmak"))


class Normalizasyon(unittest.TestCase):
    def test_sapka_tirnak_bosluk(self):
        self.assertEqual(uk.normallestir("Rüzgâr  esti,  “Kâğıdım!”  dedi."), 'Rüzgar esti, "Kağıdım!" dedi.')
        self.assertEqual(uk.normallestir("Tosbi hâlâ bekliyordu."), "Tosbi hâlâ bekliyordu.")   # eşsesli: kalır
        self.assertEqual(uk.normallestir("Tosbi’nin"), "Tosbi'nin")
        self.assertEqual(uk.normallestir("Kâr"), "Kâr")                                      # NFC, kalır

    def test_hala_k3_ret(self):
        bg = baglam()
        blok, kayit, tohum = tabanlar()[0]
        k = dict(kayit, govde=kayit["govde"].replace("Önce sabırla", "Önce hâlâ sabırla"))
        self.assertIn("K3.sapka", kodlar(kapi.denetle(k, tohum, bg, taslak_kart=True)))


class K5K7(unittest.TestCase):
    def test_kesme_eki(self):
        self.assertIsNone(kapi.kesme_eki_hatasi("çeys", "ten"))
        self.assertIsNotNone(kapi.kesme_eki_hatasi("çeys", "den"))
        self.assertIsNone(kapi.kesme_eki_hatasi("tosbi", "nin"))
        self.assertIsNotNone(kapi.kesme_eki_hatasi("tosbi", "nın"))
        self.assertIsNotNone(kapi.kesme_eki_hatasi("tosbi", "in"))
        self.assertIsNone(kapi.kesme_eki_hatasi("örümcek adam", "ın"))
        self.assertIsNone(kapi.kesme_eki_hatasi("tosbi", "ninki"))
        self.assertIsNone(kapi.kesme_eki_hatasi("murat", "tan"))
        self.assertIsNotNone(kapi.kesme_eki_hatasi("murat", "dan"))

    def test_zaman_kurali_sifat_fiil_ve_askida_ek(self):
        bg = baglam()
        gecer = ["Tosbi kırılmış oyuncağı aldı.", "Tosbi yiyecek buldu.", "Kuşlar koşuyor, zıplıyor ve gülüyordu.",
                 'Tosbi "Geliyorum!" dedi.', '"Yoruldum," diyor gibi baktı.', "Tosbi biliyordu ki yardım vardır.",
                 "Hayvanlar yüzüyor, eğleniyorlardı.", "Kutuyu açacak ve hediyeleri verecekti."]
        takilir = ["Tosbi çok yorulmuş.", "Tosbi eve gidiyor.", "Tosbi her gün koşar.", "Tosbi yarın gelecek.",
                   '"Gel," diyor Tosbi.', "Tosbi koşuyor ve sonra durdu.", "Masada ekmek var."]
        for c in gecer:
            self.assertEqual(kapi.zaman_ihlalleri(c, bg), [], c)
        for c in takilir:
            self.assertTrue(kapi.zaman_ihlalleri(c, bg), c)

    def test_k7_kanat_kanama(self):
        self.assertEqual(kapi.guvenlik_eslesmeleri("Kuğunun kanadı çok beyazdı. Kanadını açtı."), [])
        self.assertTrue(kapi.guvenlik_eslesmeleri("Tosbi düştü ve dizi kanadı."))
        self.assertTrue(kapi.guvenlik_eslesmeleri("Yağmurda ıslanıp üşümüştü."))
        self.assertEqual(kapi.guvenlik_eslesmeleri("Gözyaşlarına boğuldu."), [])


class K9K11(unittest.TestCase):
    def test_yakin_kopya(self):
        _, kayit, _ = tabanlar()[0]
        g = kayit["govde"]
        self.assertEqual(kapi.yakin_kopya(g, [("a", g)])[0][0], "K9.kopya")
        yakin = g.replace("kırmızı", "mavi").replace("Kırmızı", "Mavi")
        self.assertTrue(kapi.yakin_kopya(yakin, [("a", g)]))
        _, baska, _ = tabanlar()[1]
        self.assertEqual(kapi.yakin_kopya(g, [("b", baska["govde"])]), [])

    def test_onaysiz_kart_ret(self):
        bg = baglam()
        blok, _, tohum = tabanlar()[0]
        s = kapi.denetle(blok, tohum, bg)
        self.assertIn("K11.kart_onay", kodlar(s))
        self.assertFalse(s["taslak_kart"])


class SozlukTokenizer(unittest.TestCase):
    """Geçme şartı (3): sözlük sha256'sı tokenizer ile eşleşir."""

    def test_dogrula(self):
        self.assertEqual(sade_sozluk.dogrula(), [])
        self.assertEqual(baglam().surum["tokenizer"]["k2"], baglam().surum["tokenizer"]["sozluk"])


@unittest.skipUnless(os.environ.get("URUN_YANLIS_ALARM"), "URUN_YANLIS_ALARM=1 ile koşar")
class YanlisAlarm(unittest.TestCase):
    """Geçme şartı (2)'nin K5 zaman ve K7 kısmı (rapor; eşik yok). Zemberek kısmı Zemberek kurulunca."""

    def test_olcum(self):
        o = kapi.yanlis_alarm(200, 2026)
        print(json.dumps(o, ensure_ascii=False))
        self.assertEqual(o["n_hikaye"], 200)


if __name__ == "__main__":
    unittest.main()
