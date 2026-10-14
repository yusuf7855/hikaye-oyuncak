"""Uyku modu (gece figürü Ay Dede) veri hattı testleri: kart, gece tohumu, kod kapılarının ninni / uyku masalı
kuralları (geçerli metin geçer, bozuk metin beklenen kapıda düşer), öteki figürlerin kurallarının değişmediği, yeni
turun (urun_v4) tohumlarının önceki turla çakışmadığı, yazar istemi, toplama (gece doğrulama ayrımı) ve ürün modeli
figür listesinin gece'yi içermediği (degerlendirme/KILAVUZ_GECE.md, degerlendirme/urun_hafif_topla.py).

Koşma: .venv/bin/python -m pytest -q tests/test_gece.py
"""
import contextlib
import copy
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "degerlendirme"))
sys.path.insert(0, str(ROOT))

import kapi  # noqa: E402
import urun_kayit as uk  # noqa: E402
import veri_hakem as vh  # noqa: E402

GERCEK_FIGUR = os.path.join(ROOT, "data", "urun_figurleri.json")

NINNI_TOHUM = {"id": "gece-9001", "figur": "Ay Dede", "tur": "ninni", "yer": "bahçe", "tema": "herkes_uyuyor",
               "yan": ["kuzu"], "uyuyan": "kuzu", "eslik": None, "duyu": "koku", "ozellik": "ışık", "isim": "çimen",
               "fiil": "salla-", "fiil_mastar": "sallamak", "sifat": "yumuşak", "diyalog": "yok", "acilis": "nakarat",
               "kapanis": "nakarat", "deneme": 1}
MASAL_TOHUM = {"id": "gece-9002", "figur": "Ay Dede", "tur": "uyku_masali", "yer": "orman", "tema": "uykusu_gelmeyen",
               "yan": ["sincap"], "uyuyan": "sincap", "eslik": None, "duyu": "işitme", "ozellik": "fısılda",
               "isim": "yaprak", "fiil": "say-", "fiil_mastar": "saymak", "sifat": "uykulu", "diyalog": "var",
               "acilis": "zaman", "kapanis": "iyi_geceler", "deneme": 1}
NINNI_BAS = "### Ay Dede | bahçe | kuzu\n@plan: ninni, minik kuzuyu uyutuyor | ay ışığıyla ve rüzgarın sesiyle\n" \
            "@tohum: gece-9001\n"


def ornekler():
    """KILAVUZ_GECE.md'deki iki örnek blok (yazara giden kılavuzla aynı metin)."""
    s = (ROOT / "degerlendirme" / "KILAVUZ_GECE.md").read_text(encoding="utf-8")
    return [b.strip() for b in re.findall(r"```\n(### .*?)```", s, re.S)]


def kodlar(sonuc):
    return {x["kod"] for x in sonuc["ihlaller"]}


class Ortak(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._eski = kapi.FIGUR
        kapi.FIGUR = GERCEK_FIGUR                   # test_urun_kapi süreçte kopya listeyi gösterebilir
        cls.bg = kapi.Baglam(zemberek=False)

    @classmethod
    def tearDownClass(cls):
        kapi.FIGUR = cls._eski

    def denetle(self, metin, tohum):
        b = uk.ayristir(metin)[0]
        return kapi.denetle(b, tohum, self.bg)


class GeceKart(Ortak):
    def test_kart_ve_figur_listesi(self):
        self.assertEqual(self.bg.mod_figurleri, ["Ay Dede"])
        self.assertNotIn("Ay Dede", self.bg.figurler)                  # hikâye figürü değil
        self.assertEqual(len(self.bg.figurler), 11)
        kart = self.bg.kartlar["Ay Dede"]
        self.assertEqual((kart["kimlik"], kart["grup"], kart["onayli"]), ("gece", "uyku", True))
        self.assertEqual(uk.figur_kimligi("Ay Dede"), "gece")             # donanım kimliğiyle aynı
        self.assertEqual(uk.figur_kimligi("Örümcek Adam"), "orumcek_adam")
        # 'ay' ve 'dede' öteki figürlerin planlarında özel ad sayılmaz ('dedesine sordu' K1.plan_ad olmaz)
        self.assertNotIn("dede", self.bg.urun_adlari())
        don = json.loads((ROOT / "data" / "figur_donanim.json").read_text(encoding="utf-8"))
        g = next(f for f in don["figurler"] if f["kimlik"] == "gece")
        self.assertEqual((g["ad"], g.get("mod")), ("Ay Dede", "uyku"))

    def test_kart_kontrol_temiz(self):
        h, _, s = vh.kart_kontrol(ROOT / "data" / "urun_kartlari.json", ROOT / "data" / "urun_figurleri.json")
        self.assertEqual(h, [])
        self.assertEqual(s["etkin"], 12)

    def test_urun_modeli_gece_icermez(self):
        """Ürün paketi (web, firmware istemler.h) urun_uret.FIGURLER'den gelir: gece kartı eklenince değişmez."""
        import urun_uret as u
        self.assertFalse(u.GECE_MODELDE)
        self.assertNotIn("gece", u.FIGURLER)
        self.assertEqual(len(u.FIGURLER), 11)
        self.assertEqual(u.FIGURLER[0], "niloya")
        from tokenizers import Tokenizer
        tok = Tokenizer.from_file(str(ROOT / "hf_c3ft_v6" / "tokenizer.json"))
        a = u.istem(tok, "Ay Dede", "bahçe", None)
        b = u.istem(tok, "Ay Dede", "bahçe", None, tur="ninni")
        self.assertEqual(tok.decode(b[1:]), "Karakter: Ay Dede | Yer: bahçe\nSorun: ninni,")
        self.assertEqual(b[:len(a)], a)


class GeceKapi(Ortak):
    def test_ornekler_gecer(self):
        for blok, tohum in zip(ornekler(), (NINNI_TOHUM, MASAL_TOHUM)):
            s = self.denetle(blok, tohum)
            self.assertTrue(s["gecti"], s["ihlaller"])
            self.assertEqual(s["rapor"]["gece_tur"], tohum["tur"])
            self.assertTrue(s["kimlik"].startswith("urun/gece#"))
        # tohum yoksa tür plandan okunur
        self.assertEqual(kapi.gece_turu(uk.kayit(uk.ayristir(ornekler()[1])[0]), None, self.bg), "uyku_masali")

    def bozuk(self, eski, yeni, tohum=NINNI_TOHUM, blok=0):
        metin = ornekler()[blok]
        self.assertIn(eski, metin)
        return kodlar(self.denetle(metin.replace(eski, yeni), tohum))

    def test_bozuk_ninniler_duser(self):
        nak = "Ninni ninni, yavrum ninni."
        vakalar = {
            # aynı dize 5 kez: nakarat tavanı ve çeşit
            "K8.ayni_cumle": ("Kuşlar yuvada uyuyor.", " ".join([nak] * 3)),
            "K7.gece": ("Kuşlar yuvada uyuyor.", "Karanlıkta öcü yok, korkma."),
            "K4.dunya_kurali": ("Kuşlar yuvada uyuyor.", "Uyumazsan rüzgar gelir."),
            "K8.kekeme": ("Ninni ninni, yavrum ninni. Ay Dede", "Ninni ninni ninni, yavrum. Ay Dede"),
            "K1.ninni_tirnak": ("Kuşlar yuvada uyuyor.", '"Uyu," dedi Ay Dede.'),
            "K4.baska_figur": ("Kuşlar yuvada uyuyor.", "Niloya da yatağında uyuyor."),
            "K4.canli_rol": ("Kuşlar yuvada uyuyor.", "Tavşan da yuvada uyuyor."),
        }
        for kod, (a, b) in vakalar.items():
            self.assertIn(kod, self.bozuk(a, b), kod)
        # üç dize üçer kez: hiçbir dize tavanı aşmaz ama dizelerin yarısından azı farklı
        az_cesit = NINNI_BAS + " ".join(
            [nak, "Ay Dede gökte gümüş ışığıyla parlıyor.", "Yumuşak çimende minik kuzu yatıyor."] * 3
            + ["Rüzgar dalları yavaşça sallıyor.", "Uyu kuzum, mışıl mışıl uyu.", nak])
        k = kodlar(self.denetle(az_cesit, {**NINNI_TOHUM, "kapanis": "nakarat"}))
        self.assertIn("K8.ninni_cesit", k)
        self.assertIn("K8.ayni_cumle", k)                      # nakarat 4. kez

    def test_son_tur_ve_uzunluk(self):
        m = ornekler()[0]
        # uyku olmadan biten ninni, kapanış türü tutmayan son
        son_uykusuz = m.replace("Uyu kuzum, mışıl mışıl uyu. Ninni ninni, yavrum ninni.",
                                "Ay Dede gökten bakıyor. Ninni ninni, yavrum ninni.")
        self.assertIn("K4.gece_uyku", kodlar(self.denetle(son_uykusuz, NINNI_TOHUM)))
        iyi = {**NINNI_TOHUM, "kapanis": "iyi_geceler"}
        self.assertIn("K4.gece_kapanis", kodlar(self.denetle(m, iyi)))
        # tohum ninni, plan masal
        self.assertIn("K1.gece_tur", kodlar(self.denetle(m.replace("@plan: ninni,", "@plan: masal,"), NINNI_TOHUM)))
        self.assertIn("K1.gece_tur", kodlar(self.denetle(m.replace("@plan: ninni,", "@plan:"), None)))
        # kısa ninni: 5 dize, 50 kelimeden az
        kisa = NINNI_BAS + "Ninni ninni, yavrum ninni. Ay Dede gökte parlıyor. Kuzu çimende yatıyor. " \
                           "Rüzgar yumuşak dalları sallıyor. Kuzu mışıl mışıl uyudu, ninni."
        k = kodlar(self.denetle(kisa, NINNI_TOHUM))
        self.assertTrue({"K2.ninni_dize", "K2.uzunluk"} <= k, k)
        # 'ninni' tek kez: nakarat yok
        tek = m.replace("Ninni ninni, yavrum ninni.", "Uyu yavrum, uyu.")
        self.assertIn("K8.ninni_nakarat", kodlar(self.denetle(tek, {**NINNI_TOHUM, "kapanis": "uyudu"})))

    def test_uyku_masali_kurallari(self):
        m = ornekler()[1]
        # uyku masalı -dı'lı anlatılır (ninni değil): şimdiki zaman K5'e takılır
        self.assertIn("K5.zaman", kodlar(self.denetle(m.replace("parlıyordu", "parlıyor"), MASAL_TOHUM)))
        # uyku masalında tekrar yok
        tekrar = m.replace("Sincap kuyruğuna sarıldı ve uyudu.",
                           "Sincap kuyruğuna sarıldı ve uyudu. Sincap kuyruğuna sarıldı ve uyudu.")
        self.assertIn("K8.ayni_cumle", kodlar(self.denetle(tekrar, MASAL_TOHUM)))
        # güvenlik: kaybolmak, ağlamak
        k = kodlar(self.denetle(m.replace("Sincabın hiç uykusu gelmiyordu.", "Sincap kaybolmuştu ve ağladı."),
                                MASAL_TOHUM))
        self.assertIn("K7.gece", k)

    def test_oteki_figurler_degismedi(self):
        """Gece kuralları yalnız Ay Dede'ye uygulanır: öteki figürde 'o gece' zaman atlaması, 70 kelime alt sınırı,
        aynı cümle tekrarı ve -dı kuralı aynen kalır."""
        from tests.test_urun_kapi import TABANLAR, TOHUMLAR
        t = {x["id"]: x for x in TOHUMLAR}
        b = uk.ayristir(TABANLAR)[1]                     # Niloya
        self.assertIsNone(kapi.gece_turu(uk.kayit(b), t[b["tohum"]], self.bg))
        g = b["govde"]

        def kod(govde):
            return kodlar(kapi.denetle({**b, "govde": govde}, t[b["tohum"]], self.bg, taslak_kart=True))
        self.assertEqual(kod(g), set())
        self.assertIn("K1.zaman", kod(g.replace("Niloya evde", "O gece Niloya evde")))
        self.assertIn("K2.uzunluk", kod(" ".join(g.split()[:60]).rstrip(",") + "."))
        self.assertIn("K8.ayni_cumle", kod(g + " Murat hemen yanına geldi."))
        self.assertIn("K5.zaman", kod(g.replace("Murat hemen yanına geldi.", "Murat hemen yanına geliyor.")))


class GeceTohum(Ortak):
    def gb(self):
        return vh.GeceBilgi(vh._figur_bul(self.bg, "Ay Dede"))

    def test_paylar_ve_kurallar(self):
        gb = self.gb()
        t = vh.gece_tohum_uret(gb, 1500, 4041)
        h, pay = vh.gece_tohum_denetle(t, gb)
        self.assertEqual(h, [])
        self.assertEqual(len({x["id"] for x in t}), 1500)
        self.assertEqual(sum(x["tur"] == "ninni" for x in t), 750)
        for x in t:
            self.assertTrue(set(x["yan"]) <= set(gb.yanlar))
            if x["tur"] == "ninni":
                self.assertEqual(x["diyalog"], "yok")
            else:
                self.assertNotEqual(x["kapanis"], "nakarat")
            if not x["yan"]:
                self.assertEqual(x["uyuyan"], "yavrum")
        self.assertEqual(t, vh.gece_tohum_uret(gb, 1500, 4041))           # belirlenimci
        self.assertNotEqual(t, vh.gece_tohum_uret(gb, 1500, 7))

    def test_bozuk_tohum_yakalanir(self):
        gb = self.gb()
        t = copy.deepcopy(vh.gece_tohum_uret(gb, 120, 1))
        n = next(i for i, x in enumerate(t) if x["tur"] == "ninni")
        t[n]["diyalog"] = "var"
        t[1].update(yer="deniz", yan=["sincap"], uyuyan="sincap")
        t[2]["id"] = t[3]["id"]
        t[4]["isim"] = "dalga" if t[4]["yer"] != "deniz" else "battaniye"
        h, _ = vh.gece_tohum_denetle(t, gb)
        for parca in ("ninnide diyalog", "'sincap' 'deniz' yerinde bulunmaz", "kimliği tekrarlanıyor", "yerine uymuyor"):
            self.assertTrue(any(parca in x for x in h), (parca, h[:5]))

    def test_yeni_tur_onceki_tohumlarla_cakismaz(self):
        fb = vh.FigurBilgi(vh._figur_bul(self.bg, "Niloya"), self.bg)
        eski = vh.tohum_uret(fb, 400, 3031, self.bg)
        haric = ({(x["isim"], x["fiil"], x["sifat"]) for x in eski}, {(x["yer"], x["tema"], x["isim"]) for x in eski},
                 {x["id"] for x in eski})
        yeni = vh.tohum_uret(fb, 300, 4041, self.bg, baslangic=2001, haric=haric)
        self.assertEqual(vh.tohum_denetle(yeni, fb, self.bg, haric)[0], [])
        self.assertEqual(yeni[0]["id"], "niloya-2001")
        self.assertFalse({(x["isim"], x["fiil"], x["sifat"]) for x in yeni} & haric[0])
        self.assertFalse({(x["yer"], x["tema"], x["isim"]) for x in yeni} & haric[1])
        # çakışan tohum yakalanır
        h, _ = vh.tohum_denetle(eski[:50], fb, self.bg, haric)
        self.assertTrue(any("önceki turda var" in x for x in h))


class GeceIstemVeToplama(Ortak):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="gece_"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_yaz_istemi_ve_kontrol(self):
        Y = vh.Yollar("urun_v4", str(self.tmp))
        gb = vh.GeceBilgi(vh._figur_bul(self.bg, "Ay Dede"))
        vh.jsonl_yaz(Y.tohum("gece"), vh.gece_tohum_uret(gb, 100, 4041) + [NINNI_TOHUM, MASAL_TOHUM])
        with contextlib.redirect_stdout(io.StringIO()):
            yol, sec = vh.yaz_istemi(Y, "Ay Dede", 24, bg=self.bg, tur_kota={"ninni": 18, "uyku_masali": 6})
        self.assertEqual(sum(t["tur"] == "ninni" for t in sec), 18)
        md = Path(yol).read_text(encoding="utf-8")
        self.assertIn("aday/gece_1.txt", md)
        self.assertIn("(18 ninni, 6 uyku masalı)", md)
        self.assertIn("Uyku modu yazım kılavuzu", md)              # gece kılavuzu, figür kılavuzu değil
        self.assertNotIn("**Kural bütçesi.**", md)
        self.assertIn("--ad urun_v4", md)
        self.assertIn("- uyuyan:", md)
        # kontrol: kılavuz örnekleri gece aday dosyasında geçer (tohumlar urun_v4'ten)
        aday = Path(Y.v("aday", "ornek.txt"))
        aday.parent.mkdir(parents=True, exist_ok=True)
        aday.write_text("\n\n".join(ornekler()) + "\n", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()) as out:
            r = vh.main(["kontrol", str(aday), "--ad", "urun_v4", "--kok", str(self.tmp)])
        self.assertEqual(r, 0, out.getvalue())

    def test_birlestir_gece_ayrimi(self):
        import urun_hafif_topla as h
        kok = self.tmp / "data"
        v2, v4 = kok / "urun_v2", kok / "urun_v4"
        v2.mkdir(parents=True)
        v4.mkdir(parents=True)
        from tests.test_urun_kapi import TABANLAR
        b2 = uk.ayristir(TABANLAR)[1]
        (v2 / "niloya.txt").write_text(b2["ham"] + "\n", encoding="utf-8")
        s2 = uk.sha1(uk.kayit(b2))
        (v2 / "izin.txt").write_text(f"# test\n{s2} dogrulama\n", encoding="utf-8")
        gece = ornekler()
        # ikinci ninni: ilk örneğin bir dizesi değişmiş kopyası
        gece.append(gece[0].replace("gece-9001", "gece-9003").replace("Kuşlar yuvada uyuyor.", "Kuşlar uyuyor."))
        (v4 / "gece.txt").write_text("\n\n".join(gece) + "\n", encoding="utf-8")
        shas = [uk.sha1(uk.kayit(uk.ayristir(g)[0])) for g in gece]
        (v4 / "gecen.txt").write_text("# test\n" + "".join(s + "\n" for s in shas), encoding="utf-8")
        eski = dict(h.GECE_DOGRULAMA)
        h.GECE_DOGRULAMA.clear()
        h.GECE_DOGRULAMA.update({"ninni": 1, "masal": 1})
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                say = h.birlestir("urun_karma2", ("urun_v4",), kok=str(kok))
        finally:
            h.GECE_DOGRULAMA.clear()
            h.GECE_DOGRULAMA.update(eski)
        self.assertEqual((say["gece"], say["gece_ayri"]), (1, 2))
        H = kok / "urun_karma2"
        liste = [x.split() for x in (H / "gece_ayri" / "liste.txt").read_text().splitlines() if not x.startswith("#")]
        self.assertEqual(sorted(t for _, t in liste), ["masal", "ninni"])
        izin = (H / "izin.txt").read_text()
        for s, _ in liste:
            self.assertNotIn(s, izin)                              # ayrılan gece metni eğitime girmez
        from research.tinystories import prepare_ft2
        eg, dog, _ = prepare_ft2.yalniz_oku(H / "izin.txt")
        self.assertEqual(([x["sha1"] for x in dog], len(eg)), ([s2], 1))   # doğrulama yalnız v2'den
        self.assertEqual(eg[0]["kayit"]["figur"], "Ay Dede")


if __name__ == "__main__":
    unittest.main()
