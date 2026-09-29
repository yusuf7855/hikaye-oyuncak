"""Kusursuz veri hattı Adım 0h-i birim testleri (KUSURSUZ_VERI.md 'Hazırlık').

  (5) prepare_ft2 --yalniz koruma testleri: yasak bayrak birleşimi, izin dışı hikâye, eksik sha1, iki kez bulunan
      sha1, kanarya sha1'i ve bozuk izin satırı hata verir; eski yol (--yalniz'sız) bayt bayt aynı kalır.
  veri_hakem.py'nin her yeni alt komutu küçük sahte veriyle: kart-kontrol, tohum, yaz-istemi, kontrol (yama
  sayacı), kapi, hazirla --lens, oku (alıntı doğrulama, gecti yeniden hesabı, kanarya), karar (tek yönlü veto,
  kuyruk, izin), altin, uyum. Sahte veri: test_urun_kapi.TABANLAR (7 elle yazılmış hikâye) + 1 Tosbi çeşitlemesi.
  Bütün çıktılar geçici bir köke yazılır (--kok); depodaki data/ ve degerlendirme/ klasörlerine yazılmaz.

Koşma: .venv/bin/python -m unittest tests.test_veri_hakem -v
"""
import contextlib
import copy
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "degerlendirme"))
sys.path.insert(0, str(ROOT))

import urun_kayit as uk  # noqa: E402
import veri_hakem as vh  # noqa: E402
from research.tinystories import prepare_ft2  # noqa: E402
from tests.test_urun_kapi import TABANLAR, TOHUMLAR  # noqa: E402

# Tosbi'nin ikinci hikâyesi: aynı figür ve tohum alanları, başka metin (kanarya tabanı ve K partisi için; K9'a
# takılmaz). YAKIN_KOPYA ise ilk Tosbi hikâyesinin tek cümlesi değişmiş kopyasıdır (aynı turda K9).
TOSBI2 = """\
### Tosbi | orman | baykuş
@plan: balonun ipi bir çalıya dolandı | baykuştan yardım isteyip ipi çözdü
@tohum: tosbi-0002
Ormanda serin bir sabah vardı. Tosbi ağaçların arasında kırmızı bir balon buldu. Balonun ipi bir çalıya \
dolanmıştı. Tosbi ipi çekti ama ip çözülmedi. Tosbi sabırla düşündü ve biraz bekledi. O sırada baykuş yakındaki \
bir dala kondu. "Baykuş, bu ipi çözebilir misin?" diye sordu Tosbi. Baykuş aşağı uçtu ve gagasıyla düğümü yavaşça \
açtı. Tosbi ipin ucunu sıkıca tuttu. Balon çalıdan kurtuldu ve havada sallandı. "Teşekkür ederim," dedi Tosbi. \
Baykuş başını salladı ve dalına döndü. Tosbi kırmızı balonla ağaçların arasında yürüdü."""
TOHUM2 = {**TOHUMLAR[0], "id": "tosbi-0002"}
YAKIN_KOPYA = TABANLAR.split("\n\n")[0].replace("@tohum: tosbi-0001", "@tohum: tosbi-0003").replace(
    "Ormanda sakin bir sabah vardı.", "Ormanda serin bir sabah vardı.")
TOHUM3 = {**TOHUMLAR[0], "id": "tosbi-0003"}


def sessiz(f, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()) as out:
        r = f(*a, **k)
    return r, out.getvalue()


def kok_kur(kok):
    """<kok>/data/urun_v1/{tohum,aday,istem}: 8 hikâye, figür başına bir aday dosyası."""
    v = Path(kok) / "data" / "urun_v1"
    for d in ("tohum", "aday", "istem"):
        (v / d).mkdir(parents=True, exist_ok=True)
    bloklar = uk.ayristir(TABANLAR)
    dosyalar = {}
    for t, b in zip(TOHUMLAR, bloklar):
        fk = t["id"].split("-")[0]
        dosyalar.setdefault(fk, ([], []))
        dosyalar[fk][0].append(t)
        dosyalar[fk][1].append(b["ham"])
    dosyalar["tosbi"][0].append(TOHUM2)
    dosyalar["tosbi"][1].append(TOSBI2)
    for fk, (ts, hamlar) in dosyalar.items():
        (v / "tohum" / f"{fk}.jsonl").write_text("".join(json.dumps(t, ensure_ascii=False) + "\n" for t in ts))
        (v / "aday" / f"{fk}_1.txt").write_text("\n\n".join(hamlar) + "\n")
        (v / "istem" / f"{fk}_1.json").write_text(json.dumps(
            {"figur": ts[0]["figur"], "parti": 1, "dosya": f"aday/{fk}_1.txt",
             "tohumlar": [{"id": t["id"], "deneme": 1} for t in ts]}, ensure_ascii=False))
    return vh.Yollar("urun_v1", str(kok))


def hakemle(Y, karar_ver=None):
    """Sahte hakem: puanı olmayan her partiye yazar. karar_ver(mercek, parti, konum, hikaye, yer) ->
    None ('yok'), ('madde', alıntı) ya da ham kayıt (dict). Kanaryalar varsayılan olarak yakalanır."""
    for L in vh.MERCEKLER:
        g = vh.json_oku(Y.hakem(L, "gorev.json"))
        if not g:
            continue
        yer = vh.json_oku(Y.hakem(L, "yerlesim.json"))
        for i in g["isler"]:
            hedef = i["cikti"] if not os.path.exists(i["cikti"]) else (
                i["cikti_yeniden"] if not os.path.exists(i["cikti_yeniden"]) else None)
            if hedef is None:
                continue
            ilk = hedef == i["cikti"]
            p = vh.json_oku(i["parti_dosyasi"])
            out = []
            for k, h in enumerate(p["hikayeler"]):
                y = yer[str(i["parti"])]["konumlar"][k]
                m = {x: "yok" for x in vh.MADDELER[L]}
                ih = []
                oy = karar_ver(L, i["parti"], k, h, y, ilk) if karar_ver else None
                if isinstance(oy, dict):
                    out.append(oy)
                    continue
                if oy is None and y["rol"] == "kanarya":
                    cs = uk.cumleler(h["govde"])
                    no = min(y["degisen_cumle"][0], len(cs))
                    oy = (vh.MADDELER[L][0], cs[no - 1])
                if oy == "kacir":
                    oy = None
                if oy:
                    m[oy[0]] = "var"
                    ih.append({"madde": oy[0], "alinti": oy[1], "cumle_no": None, "aciklama": "kusur var."})
                out.append({"id": h["id"], "ihlaller": ih, "maddeler": m, "gecti": not ih})
            vh.json_yaz(hedef, out)


class Ortak(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bg = vh._kapi().Baglam()

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="veri_hakem_")
        self.Y = kok_kur(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def vh(self, *argv):
        return sessiz(vh.main, list(argv) + ["--kok", self.tmp])

    def kapi(self):
        r, _ = self.vh("kapi", "--hepsi", "--taslak-kart")
        self.assertEqual(r, 0)
        return vh.aday_kayitlari(self.Y)


# ---------------------------------------------------------------- prepare_ft2 --yalniz (geçme şartı 5)

class PrepareYalniz(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="yalniz_"))
        self.veri = self.tmp / "data" / "urun_v1"
        self.veri.mkdir(parents=True)
        self.bloklar = uk.ayristir(TABANLAR)
        self.kayitlar = [uk.kayit(b) for b in self.bloklar]
        self.sha = [uk.sha1(k) for k in self.kayitlar]
        for b in self.bloklar:
            fk = b["tohum"].split("-")[0]
            (self.veri / f"{fk}.txt").write_text(uk.blok_yaz(uk.kayit(b), b["tohum"]))
        self.izin = self.veri / "izin.txt"
        self.izin_yaz({s: ("dogrulama" if i == 0 else "egitim") for i, s in enumerate(self.sha)})

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def izin_yaz(self, d, ek=""):
        self.izin.write_text("# test\n" + "".join(f"{s} {b}\n" for s, b in d.items()) + ek)

    def test_gecerli_izin(self):
        eg, dog, bilgi = prepare_ft2.yalniz_oku(self.izin)
        self.assertEqual(len(eg), 6)
        self.assertEqual([h["sha1"] for h in dog], [self.sha[0]])
        self.assertEqual({h["sha1"] for h in eg + dog}, set(self.sha))
        self.assertEqual(len(bilgi["izin_sha256"]), 64)

    def test_yasak_bayrak_birlesimi(self):
        for bayrak in (["--plan", "p.jsonl"], ["--haric", "h.txt"], ["--bolme", "b.json"], ["--kaynak", "oyuncak_v2"],
                       ["--tema"]):
            with self.assertRaises(prepare_ft2.YalnizHata, msg=bayrak) as c:
                with contextlib.redirect_stdout(io.StringIO()):
                    prepare_ft2.main(["--yalniz", str(self.izin), "--genel-token", "0",
                                      "--out", str(self.tmp / "o")] + bayrak)
            self.assertIn(bayrak[0], str(c.exception))

    def test_yansiz_manifest_yalniz_disinda_hata(self):
        with self.assertRaises(SystemExit):
            prepare_ft2.main(["--yansiz", "--genel-token", "0", "--out", str(self.tmp / "o")])
        with self.assertRaises(SystemExit):
            prepare_ft2.main(["--taslak-kart-izin", "--genel-token", "0", "--out", str(self.tmp / "o")])

    def test_taslak_kart_reddedilir(self):
        """Onaysız kartla kabul edilmiş veri (izin notu ya da kabul.jsonl) --taslak-kart-izin olmadan eğitime girmez;
        ret çıktı yazılmadan olur."""
        d = {s: ("dogrulama" if i == 0 else "egitim") for i, s in enumerate(self.sha)}
        for hazirla in (lambda: self.izin_yaz(d, ek="# taslak_kart: evet\n"),
                        lambda: (self.izin_yaz(d), (self.veri / "kabul.jsonl").write_text(
                            json.dumps({"sha1": self.sha[1], "taslak_kart": True}) + "\n"))):
            hazirla()
            with self.assertRaisesRegex(prepare_ft2.YalnizHata, "taslak"):
                with contextlib.redirect_stdout(io.StringIO()):
                    prepare_ft2.main(["--yalniz", str(self.izin), "--genel-token", "0", "--out", str(self.tmp / "o")])
            self.assertFalse((self.tmp / "o").exists())
        (self.veri / "kabul.jsonl").unlink()
        self.izin_yaz(d)
        self.assertFalse(prepare_ft2.taslak_kart_mi(self.izin, prepare_ft2.izin_oku(self.izin)[1]))

    def test_izin_disi_hikaye(self):
        d = {s: "egitim" for s in self.sha[1:]}
        self.izin_yaz(d)
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "izin listesinde olmayan"):
            prepare_ft2.yalniz_oku(self.izin)

    def test_eksik_sha1(self):
        d = {s: "egitim" for s in self.sha}
        d["0" * 40] = "egitim"
        self.izin_yaz(d)
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "bulunamadı"):
            prepare_ft2.yalniz_oku(self.izin)

    def test_iki_kez_bulunan(self):
        (self.veri / "kopya.txt").write_text((self.veri / "tosbi.txt").read_text())
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "ikinci kez"):
            prepare_ft2.yalniz_oku(self.izin)

    def test_izinde_iki_kez_ve_bozuk_satir(self):
        self.izin_yaz({self.sha[0]: "egitim"}, ek=f"{self.sha[0]} egitim\n")
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "iki kez"):
            prepare_ft2.izin_oku(self.izin)
        self.izin.write_text(f"{self.sha[0]} test\n")
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "egitim"):
            prepare_ft2.izin_oku(self.izin)

    def test_bicim_hatali_blok(self):
        (self.veri / "bozuk.txt").write_text("### Tosbi | orman\n@tohum: x\nGövde.\n")
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "biçim hatası"):
            prepare_ft2.yalniz_oku(self.izin)

    def test_kanarya_izinde(self):
        with self.assertRaisesRegex(prepare_ft2.YalnizHata, "kanarya"):
            prepare_ft2.yalniz_oku(self.izin, kanaryalar={self.sha[3]})
        d = self.tmp / "degerlendirme" / "urun_v1" / "hakem" / "M"
        d.mkdir(parents=True)
        (d / "kanarya.jsonl").write_text(json.dumps({"sha1": self.sha[2]}) + "\n")
        self.assertIn(self.sha[2], prepare_ft2.kanarya_sha1leri(self.izin))

    @unittest.skipUnless((ROOT / "data" / "tr2_tinystories" / "vocab-16384" / "train.bin").exists(), "genel veri yok")
    def test_uctan_uca_ve_dizgi(self):
        out = self.tmp / "cikti"
        with contextlib.redirect_stdout(io.StringIO()):
            m = prepare_ft2.main(["--yalniz", str(self.izin), "--genel", "tr2_tinystories", "--genel-token", "500",
                                  "--tekrar", "4", "--out", str(out), "--manifest", str(self.tmp / "model" / "m.json")])
        v = out / "vocab-16384"
        self.assertTrue((v / "manifest_urun.json").exists() and (self.tmp / "model" / "m.json").exists())
        self.assertEqual((m["egitim"], m["dogrulama"], m["kopya"]), (6, 1, 24))
        import numpy as np
        from tokenizers import Tokenizer
        tok = Tokenizer.from_file(str(v / "tokenizer.json"))
        ids = np.fromfile(v / "train.bin", dtype=np.uint16)
        bas, son = np.load(v / "train_bas.npy"), np.load(v / "train_son.npy")
        metinler = [tok.decode(ids[b:s - 1].tolist()).strip() for b, s in zip(bas, son)]
        self.assertEqual(len(metinler), 24)
        beklenen = {uk.dizgi(k, p, True) for k in self.kayitlar[1:] for p in (True, False)}
        self.assertTrue(all(x in beklenen for x in metinler), metinler[0][:80])
        self.assertEqual(sum(x.count("\nSorun: ") for x in metinler), m["planli_kopya"])
        # aynı argümanlarla ikinci koşu bayt bayt aynı
        with contextlib.redirect_stdout(io.StringIO()):
            prepare_ft2.main(["--yalniz", str(self.izin), "--genel", "tr2_tinystories", "--genel-token", "500",
                              "--tekrar", "4", "--out", str(self.tmp / "c2")])
        self.assertEqual((v / "train.bin").read_bytes(), (self.tmp / "c2" / "vocab-16384" / "train.bin").read_bytes())

    @unittest.skipUnless((ROOT / "data" / "tr2_tinystories" / "vocab-16384" / "train.bin").exists() and
                         (ROOT / "data" / "oyuncak_v2").exists(), "eski veri yok")
    def test_eski_yol_bayt_bayt_ayni(self):
        """--yalniz'sız eski komut (varsayılan --kaynak dahil) HEAD'deki prepare_ft2 ile aynı çıktıyı verir."""
        try:
            eski = subprocess.run(["git", "show", "HEAD:research/tinystories/prepare_ft2.py"], cwd=ROOT,
                                  capture_output=True, text=True, check=True).stdout
        except Exception as e:
            self.skipTest(f"git yok: {e}")
        if "--yalniz" in eski:
            self.skipTest("HEAD'deki sürüm zaten --yalniz içeriyor; kıyas tabanı yok")
        eski_yol = ROOT / "research" / "tinystories" / "_prepare_ft2_eski_test.py"
        eski_yol.write_text(eski)
        try:
            for ad, arg in (("eski", "research.tinystories._prepare_ft2_eski_test"),
                            ("yeni", "research.tinystories.prepare_ft2")):
                subprocess.run([sys.executable, "-m", arg, "--genel", "tr2_tinystories", "--genel-token", "2000",
                                "--tekrar", "2", "--out", str(self.tmp / ad)], cwd=ROOT, check=True,
                               capture_output=True, env={**os.environ, "PYTHONPATH": "src"})
        finally:
            eski_yol.unlink()
        for f in ("train.bin", "val.bin", "train_bas.npy", "dogrulama.json"):
            self.assertEqual((self.tmp / "eski" / "vocab-16384" / f).read_bytes(),
                             (self.tmp / "yeni" / "vocab-16384" / f).read_bytes(), f)


# ---------------------------------------------------------------- kart-kontrol

def kart_bul(veri, kimlik):
    return next(k for k in veri["kartlar"] if k["kimlik"] == kimlik)


class KartKontrol(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="kart_"))
        self.kart = json.loads((ROOT / "data" / "urun_kartlari.json").read_text())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def denetle(self, kart, kilit=None):
        yol = self.tmp / "kart.json"
        yol.write_text(json.dumps(kart, ensure_ascii=False))
        return vh.kart_kontrol(yol, ROOT / "data" / "urun_figurleri.json", kilit)

    def test_gercek_kartlar_temiz(self):
        h, u, s = self.denetle(self.kart)
        self.assertEqual(h, [])
        self.assertEqual((s["kart"], s["etkin"], s["regex"], s["ornek_yakalandi"]), (15, 11, 61, 61))

    def test_cikarilan_figurun_karti_etkin_sayilmaz(self):
        """Kullanıcı isteği: yalnız çizgi film karakterleri. Temel figürlerin kartları durur ama ürün listesinde
        'cikarilanlar'dadır: kart-kontrol onları denetler, etkin saymaz; çıkarılmamış fazla kart hatadır."""
        urun = json.loads((ROOT / "data" / "urun_figurleri.json").read_text())
        self.assertEqual([f["ad"] for f in urun["populer"]][-1], "Hello Kitty")
        self.assertEqual((len(urun["populer"]), urun["temel"]), (11, []))
        self.assertTrue({"Tosbi", "Tekir", "Pamuk", "Karabaş"} <= set(urun["cikarilanlar"]))
        urun["cikarilanlar"].remove("Tosbi")
        yol = self.tmp / "urun.json"
        yol.write_text(json.dumps(urun, ensure_ascii=False))
        h, _, _ = vh.kart_kontrol(ROOT / "data" / "urun_kartlari.json", yol)
        self.assertTrue(any("fazla ['Tosbi']" in x for x in h), h)

    def test_bozulmalar_yakalanir(self):
        bozuk = {
            "kaynak_yok": lambda k: k["kartlar"][0]["yanlar"][0]["iliski"].pop("kaynak"),
            "bilinmeyen_kaynak": lambda k: k["kartlar"][1]["tur"].__setitem__("kaynak", ["yok_boyle"]),
            "sapka": lambda k: k["kartlar"][2]["yerler"][0].__setitem__("tarif", "Kâğıt dolu bir oda."),
            "unlem": lambda k: k["kartlar"][8]["ozellikler"][0].__setitem__("deger", "Chase görevde!"),
            "yer_sirasi": lambda k: k["kartlar"][0]["yerler"].reverse(),
            "regex": lambda k: k["kartlar"][0]["dunya_kurallari"][0]["yasak_duzenli_ifadeler"].append("(("),
            "urun_dayanakli": lambda k: k["kartlar"][0]["yanlar"][0]["tur"].__setitem__("kaynak", ["urun_karari"]),
            "deyim": lambda k: k["kartlar"][3]["yerler"][0].__setitem__("tarif", "Herkesin içi rahat eder."),
            # yazarın kopyalayacağı metin kapılarla çatışmaz: K7 kalıbı ve kökü nadir kelime (Tosbi kartı)
            "k7_tarif": lambda k: kart_bul(k, "tosbi")["yerler"][2].__setitem__("tarif", "Kıyı; derin su var."),
            "nadir_tarif": lambda k: kart_bul(k, "tosbi")["yerler"][1].__setitem__("tarif", "Çiçekli bir dağ yamacı."),
            "yan_yeri": lambda k: kart_bul(k, "tosbi")["yanlar"][3]["yerler"].__setitem__("deger", ["çöl"]),
            "kategori": lambda k: kart_bul(k, "tosbi")["tohum_yasak_kategoriler"]["deger"].append("uzay"),
        }
        for ad, f in bozuk.items():
            k = copy.deepcopy(self.kart)
            f(k)
            h, _, _ = self.denetle(k)
            self.assertTrue(h, ad)

    def test_kilit(self):
        k = copy.deepcopy(self.kart)
        for x in k["kartlar"]:
            x["onayli"] = x["kimlik"] == "tosbi"
        h, u, s = self.denetle(k, {})
        self.assertEqual((h, s["onayli"]), ([], 1))
        self.assertTrue(any("kilitlenmemiş" in x for x in u))
        kilit = {"tosbi": {"sha1": vh.kart_sha1(kart_bul(k, "tosbi"))}}
        self.assertEqual(self.denetle(k, kilit)[0], [])
        kart_bul(k, "tosbi")["yerler"][0]["tarif"] = "Başka bir tarif."
        self.assertTrue(any("kilitten sonra değişti" in x for x in self.denetle(k, kilit)[0]))


# ---------------------------------------------------------------- tohum

class Tohum(Ortak):
    def test_paylar_kisitlar_ve_tekrarsizlik(self):
        for ad in ("Maşa", "Tosbi", "Chase", "Örümcek Adam"):
            fb = vh.FigurBilgi(vh._figur_bul(self.bg, ad), self.bg)
            t = vh.tohum_uret(fb, 400, 2026, self.bg)
            hatalar, pay = vh.tohum_denetle(t, fb, self.bg)
            self.assertEqual(hatalar, [], ad)
            self.assertEqual(len({x["id"] for x in t}), 400)
            for x in t:
                if x["kapanis"] == "replik":
                    self.assertEqual(x["diyalog"], "var")
                if x["diyalog"] == "var" or vh.TEMALAR[x["tema"]][1]:
                    self.assertTrue(x["yan"], x)
            self.assertLessEqual(max(p for p, _ in pay["tema"].values()), vh.TEMA_TAVAN)
            self.assertLessEqual(sum(p for k, (p, _) in pay["tema"].items() if k in vh.AHLAKI_TEMALAR),
                                 vh.AHLAKI_TAVAN, ad)
            self.assertLessEqual({x["kapanis"] for x in t}, {"duygu", "sonuc", "replik", "ders"})
        masa = vh.tohum_uret(vh.FigurBilgi(vh._figur_bul(self.bg, "Maşa"), self.bg), 200, 7, self.bg)
        self.assertTrue(any(len(x["yan"]) == 2 for x in masa))

    def test_belirlenimci_ve_bozuk_tohum_yakalanir(self):
        fb = vh.FigurBilgi(vh._figur_bul(self.bg, "Niloya"), self.bg)
        a, b = vh.tohum_uret(fb, 60, 5, self.bg), vh.tohum_uret(fb, 60, 5, self.bg)
        self.assertEqual(a, b)
        bozuk = copy.deepcopy(a)
        bozuk[0]["isim"] = "keçi"
        bozuk[1]["yan"] = ["Şuşu"]
        bozuk[2].update(kapanis="replik", diyalog="yok")
        bozuk[3]["id"] = bozuk[4]["id"]
        h, _ = vh.tohum_denetle(bozuk, fb, self.bg)
        for parca in ("keçi", "Şuşu", "replik", "kimliği tekrarlanıyor"):
            self.assertTrue(any(parca in x for x in h), parca)

    def test_kartin_dunyasi(self):
        """Tohum kartın dünyasına uyar: yan yalnız kartın izin verdiği yerde (Tosbi'nin ormanında balık yok), kelime
        yasak kategoriden gelmez (doğa dünyasında telefon, masal köyünde mikrofon yok) ve gerektirdiği canlı
        figürün ya da tohumdaki yanın türüdür (Tosbi'ye yansız 'havlamak' gelmez)."""
        kat, gerek = self.bg.tohum_kategori, self.bg.canli_gerektirir
        for ad in ("Tosbi", "Keloğlan", "Tekir", "Pamuk", "Doru", "Niloya"):
            fb = vh.FigurBilgi(vh._figur_bul(self.bg, ad), self.bg)
            t = vh.tohum_uret(fb, 400, 2026, self.bg)
            self.assertEqual(vh.tohum_denetle(t, fb, self.bg)[0], [], ad)
            yan_yer = {y["ad"]: y["yerler"] for y in fb.yanlar}
            for x in t:
                self.assertTrue(all(x["yer"] in yan_yer[y] for y in x["yan"]), x)
                for alan in ("isim", "fiil", "sifat"):
                    w = x[alan]
                    self.assertFalse(kat.get(w) in fb.yasak_kategoriler and w not in fb.kart_kelimeleri, (ad, w))
                    if w in gerek:
                        turler = fb.tur_lemmalari.union(*[y["turler"] for y in fb.yanlar if y["ad"] in x["yan"]])
                        self.assertTrue(turler & set(gerek[w]), (ad, w, x["yan"]))
            if ad == "Tosbi":
                self.assertFalse([x for x in t if "balık" in x["yan"] and x["yer"] != "deniz"])
                self.assertTrue([x for x in t if "balık" in x["yan"]])
                self.assertFalse({x["isim"] for x in t} & {"telefon", "mikrofon", "bilgisayar", "araba", "pizza"})
            if ad == "Keloğlan":
                self.assertFalse({x["isim"] for x in t} & {"telefon", "mikrofon", "televizyon", "tren", "pizza"})
        # bozuk tohum yakalanır: ormanda balık, doğa dünyasında telefon, köpeksiz havlamak
        fb = vh.FigurBilgi(vh._figur_bul(self.bg, "Tosbi"), self.bg)
        bozuk = copy.deepcopy(vh.tohum_uret(fb, 30, 1, self.bg))
        bozuk[0].update(yer="orman", yan=["balık"])
        bozuk[1]["isim"] = "telefon"
        bozuk[2].update(fiil="havla-", yan=[])
        h, _ = vh.tohum_denetle(bozuk, fb, self.bg)
        for parca in ("'balık' 'orman' yerinde bulunmaz", "'telefon' figürün dünyasına", "'havla-' figürün dünyasına"):
            self.assertTrue(any(parca in x for x in h), (parca, h))
        # kartın kendi metnindeki kelime yasak kategoride olsa da gelebilir (Niloya'nın parkında kaydırak)
        niloya = vh.FigurBilgi(vh._figur_bul(self.bg, "Niloya"), self.bg)
        self.assertEqual(kat.get("kaydırak"), "cagdas")
        self.assertTrue(niloya.kelime_uygun("kaydırak") and not niloya.kelime_uygun("pizza"))

    def test_komut(self):
        r, out = self.vh("tohum", "--figur", "Tekir", "--n", "100", "--tohum", "3")
        self.assertEqual(r, 0, out)
        self.assertEqual(len(vh.jsonl_oku(self.Y.tohum("tekir"))), 100)
        with self.assertRaises(SystemExit):   # var olan dosya üstüne yazılmaz
            self.vh("tohum", "--figur", "Tekir", "--n", "100")
        self.assertEqual(self.vh("tohum", "--figur", "Tekir", "--denetle")[0], 0)


# ---------------------------------------------------------------- yaz-istemi, kontrol, kapi

class YazarVeKapi(Ortak):
    def test_yaz_istemi(self):
        (Path(self.Y.tohum("keloglan"))).write_text("")
        sessiz(vh.main, ["tohum", "--figur", "Keloğlan", "--n", "30", "--ustune-yaz", "--kok", self.tmp])
        bg_taslak = copy.copy(self.bg)             # onaysız kartla istem yazılmaz (depodaki kartlar onaylı)
        bg_taslak.kart_dosyasi = copy.deepcopy(self.bg.kart_dosyasi)
        for k in bg_taslak.kart_dosyasi["kartlar"]:
            k["onayli"] = False
        with self.assertRaises(SystemExit):
            sessiz(vh.yaz_istemi, self.Y, "Keloğlan", bg=bg_taslak)
        r, _ = self.vh("yaz-istemi", "--figur", "Keloğlan", "--n", "12")
        self.assertEqual(r, 0)
        md = Path(self.Y.v("istem", "keloglan_2.md")).read_text()
        ist = vh.json_oku(self.Y.v("istem", "keloglan_2.json"))
        self.assertEqual(len(ist["tohumlar"]), 12)
        self.assertFalse(ist["taslak_kart"])
        self.assertNotIn("KULLANICI ONAYLI", md)          # kılavuzdaki örnekler dolu, yer tutucu yok
        self.assertIn("aday/keloglan_2.txt", md)
        self.assertIn("veri_hakem.py kontrol", md)
        self.assertIn("**Kural bütçesi.**", md)          # kılavuz birebir
        self.assertIn("Bilgecan Dede", md)               # kart
        for t in ist["tohumlar"]:
            self.assertIn(f"@tohum: {t['id']}", md)
        # ikinci istem aynı tohumları yeniden vermez
        self.vh("yaz-istemi", "--figur", "Keloğlan", "--n", "12", "--taslak-kart")
        ist3 = vh.json_oku(self.Y.v("istem", "keloglan_3.json"))
        self.assertFalse({t["id"] for t in ist3["tohumlar"]} & {t["id"] for t in ist["tohumlar"]})

    def test_kontrol_yama_sayaci(self):
        dosya = self.Y.v("aday", "niloya_1.txt")
        r, out = self.vh("kontrol", dosya, "--taslak-kart")
        self.assertEqual(r, 0, out)
        ham = Path(dosya).read_text()
        Path(dosya).write_text(ham.replace("güzel bir resim", "büyük bir resim"))
        r, out = self.vh("kontrol", dosya, "--taslak-kart")
        self.assertEqual(r, 0, out)                   # 1 yama serbest
        Path(dosya).write_text(ham.replace("güzel bir resim", "yeni bir resim"))
        r, out = self.vh("kontrol", dosya, "--taslak-kart")
        self.assertEqual(r, 1)
        self.assertIn("K1.yama_siniri", out)
        aday = self.kapi()
        n = next(x for x in aday.values() if x["figur"] == "Niloya")
        self.assertTrue(n["yamali"])
        self.assertEqual(n["yama_sayisi"], 2)
        self.assertIn("-Niloya evde güzel bir resim", n["fark"])
        self.assertFalse(n["gecti"])

    def test_kapi(self):
        aday = self.kapi()
        self.assertEqual(len(aday), 8)
        self.assertTrue(all(r["gecti"] for r in aday.values()), [r["ihlaller"] for r in aday.values()])
        self.assertTrue(os.path.exists(self.Y.v("surum", f"{self.bg.surum_ozeti}.json")))
        # aynı tohum iki kez -> K1.tohum_tekrar; kapı yeniden koşunca eski kayıtlar değişir, çoğalmaz
        p = Path(self.Y.v("aday", "tosbi_1.txt"))
        p.write_text(p.read_text() + "\n" + TOSBI2.replace("serin bir sabah", "güzel bir sabah") + "\n")
        aday = self.kapi()
        self.assertEqual(len(aday), 9)
        self.assertTrue(any("K1.tohum_tekrar" in {x["kod"] for x in r["ihlaller"]} for r in aday.values()))

    def test_k9_ayni_turdaki_aday(self):
        """K9 havuzu aynı turdaki önceki adayları da içerir: kabul havuzu boşken yakın kopyanın ikincisi düşer,
        ilki geçer; aynı tohumun kendi kabulü havuza girmez."""
        t = Path(self.Y.tohum("tosbi"))
        t.write_text(t.read_text() + json.dumps(TOHUM3, ensure_ascii=False) + "\n")
        (Path(self.Y.v("aday")) / "tosbi_2.txt").write_text(YAKIN_KOPYA + "\n")
        aday = self.kapi()
        tosbi = {r["tohum"]: r for r in aday.values() if r["figur"] == "Tosbi"}
        self.assertTrue(tosbi["tosbi-0001"]["gecti"] and tosbi["tosbi-0002"]["gecti"])
        k9 = [x for x in tosbi["tosbi-0003"]["ihlaller"] if x["kapi"] == "K9"]
        self.assertTrue(k9 and tosbi["tosbi-0001"]["kimlik"] in k9[0]["aciklama"], tosbi["tosbi-0003"]["ihlaller"])
        # yazarın öz-denetimi de aynı dosyadaki önceki hikâyeyi havuzda görür
        (Path(self.Y.v("aday")) / "tosbi_3.txt").write_text(TABANLAR.split("\n\n")[0] + "\n\n" + YAKIN_KOPYA + "\n")
        r, out = self.vh("kontrol", self.Y.v("aday", "tosbi_3.txt"), "--taslak-kart")
        self.assertEqual(r, 1)
        self.assertIn("K9.", out)


# ---------------------------------------------------------------- hazirla, oku, karar, altin, uyum

class Kurul(Ortak):
    def hazirla(self, L, **k):
        k.setdefault("taslak_kart", True)
        k.setdefault("taban_aday", True)
        return vh.hazirla_urun(self.Y, L, bg=self.bg, **k)

    def test_hazirla_parti_duzeni(self):
        self.kapi()
        ozet, isler = self.hazirla("M", parti_boyu=4, pilot=True, dagilim=(0, 1, 0))
        yer = vh.json_oku(self.Y.hakem("M", "yerlesim.json"))
        self.assertEqual({i["hakem"] for i in isler}, {1, 2})
        for i in isler:
            p = vh.json_oku(i["parti_dosyasi"])
            self.assertLessEqual(len(p["hikayeler"]), 4)
            self.assertEqual(sorted(p["madde_sirasi"]), sorted(vh.MADDELER["M"]))
            konum = yer[str(i["parti"])]["konumlar"]
            for k in konum:
                if k["rol"] == "kanarya":
                    self.assertNotIn(k["taban_sha1"], {x["sha1"] for x in konum})
            for h in p["hikayeler"]:
                self.assertEqual(set(h), {"id", "baslik", "plan", "govde", "ozellik"})
        self.assertGreaterEqual(ozet.get("kanarya", 0), 1)
        # her hedef her hakemden tam bir kez
        say = {}
        for i in isler:
            for k in yer[str(i["parti"])]["konumlar"]:
                if k["rol"] == "hedef":
                    say[(k["sha1"], i["hakem"])] = say.get((k["sha1"], i["hakem"]), 0) + 1
        self.assertEqual(set(say.values()), {1})
        self.assertEqual(len(say), 16)
        # bekleyen parti varken aynı hikâyeler yeniden partiye konmaz
        ozet2, isler2 = self.hazirla("M", parti_boyu=4, pilot=True)
        self.assertEqual(isler2, [])
        # K: tek figürlü parti ve kart; D: adlar ve K6 işaretleri
        _, isk = self.hazirla("K", parti_boyu=10, pilot=True, dagilim=(1, 0, 0))
        for i in isk:
            p = vh.json_oku(i["parti_dosyasi"])
            self.assertEqual(len({h["baslik"]["figur"] for h in p["hikayeler"]}), 1)
            self.assertEqual(vh._olgu(p["kart"]["ad"]), p["hikayeler"][0]["baslik"]["figur"])
            self.assertNotIn("acik_noktalar", p["kart"])
        _, isd = self.hazirla("D", parti_boyu=10, pilot=True, dagilim=(1, 0, 0))
        h = vh.json_oku(isd[0]["parti_dosyasi"])["hikayeler"][0]
        self.assertEqual(set(h), {"id", "plan", "govde", "adlar", "k6_isaretleri"})
        # ikinci hakem: farklı bileşim ya da ters sıra
        p1 = [vh.json_oku(i["parti_dosyasi"])["hikayeler"] for i in isd if i["hakem"] == 1]
        p2 = [vh.json_oku(i["parti_dosyasi"])["hikayeler"] for i in isd if i["hakem"] == 2]
        self.assertNotEqual([x["id"] for p in p1 for x in p], [x["id"] for p in p2 for x in p])

    def test_kisa_devre(self):
        self.kapi()
        ozet, isler = self.hazirla("D", parti_boyu=10)     # tam ölçek: M bitmeden D yok
        self.assertEqual((ozet["aday"], isler), (0, []))

    def test_alinti_dogrulama(self):
        h = {"plan": {"sorun": "kırmızı balon yüksek bir dala takıldı", "cozum": "baykuştan yardım isteyip indirdi"},
             "govde": "Tosbi yürüdü. Rüzgar esti ve balon yüksek bir dala takıldı. Baykuş uçtu."}
        d = lambda alinti, madde="M3", lens="M", cn=None: vh.alinti_dogrula(  # noqa: E731
            {"madde": madde, "alinti": alinti, "cumle_no": cn, "aciklama": "x"}, lens, h)
        self.assertEqual(d("balon yüksek bir dala")["bulunan_cumle"], 2)
        self.assertTrue(d("balon yüsek bir dalaa")["dogrulandi"])          # 2 düzenleme
        self.assertTrue(d("balon alçak bir dala")["uydurma"])               # 3+ düzenleme
        self.assertEqual(d("baykuştan yardım isteyip")["bulunan_cumle"], 0)  # plan
        self.assertTrue(d("“Tosbi yürüdü.”")["dogrulandi"])                 # normalizasyon
        self.assertTrue(d(None, "M5", cn=3)["eksiklik"])
        self.assertTrue(d(None, "M3", cn=3)["uydurma"])
        self.assertTrue(d(None, "D1", "D", cn=1)["uydurma"])
        self.assertTrue(d("Baykuş uçtu")["kisa"])

    def test_puan_dogrula(self):
        parti = {"hikayeler": [{"id": "a"}, {"id": "b"}]}
        tam = lambda i, **k: {"id": i, "ihlaller": [], "maddeler": {m: "yok" for m in vh.MADDELER["D"]},  # noqa
                              "gecti": True, **k}
        self.assertTrue(vh.puan_dogrula("D", parti, [tam("a"), tam("b")])[0])
        self.assertFalse(vh.puan_dogrula("D", parti, [tam("b"), tam("a")])[0])          # sıra
        self.assertFalse(vh.puan_dogrula("D", parti, [tam("a")])[0])                    # eksik
        self.assertFalse(vh.puan_dogrula("D", parti, [tam("a"), tam("b", gecti=False)])[0])
        k = tam("b")
        k["maddeler"]["D3"] = "var"
        self.assertFalse(vh.puan_dogrula("D", parti, [tam("a"), k])[0])                 # ihlalsiz var, gecti
        k["gecti"] = False
        k["ihlaller"] = [{"madde": "D3", "alinti": "x y z", "cumle_no": 1, "aciklama": "a"}]
        self.assertTrue(vh.puan_dogrula("D", parti, [tam("a"), k])[0])
        m = tam("a")
        del m["maddeler"]["D9"]
        self.assertFalse(vh.puan_dogrula("D", parti, [m, k])[0])

    def test_oku_karar_uctan_uca(self):
        aday = self.kapi()
        sha = {r["tohum"]: s for s, r in aday.items()}
        uyd, gerc, gecersiz_var = sha["chase-0001"], sha["niloya-0001"], sha["pamuk-0001"]
        for L in vh.MERCEKLER:
            self.hazirla(L, parti_boyu=4, pilot=True, dagilim=(0, 1, 0))
        gecersiz_parti = []

        def karar(L, n, k, h, y, ilk):
            if y["sha1"] == uyd and L == "M":
                return ("M3", "bu cümle hikâyede hiç geçmiyor")          # uydurma alıntı
            if y["sha1"] == gerc and L == "D":
                return ("D2", uk.cumleler(h["govde"])[1])                # doğrulanmış var
            if y["sha1"] == gecersiz_var and L == "K" and ilk:
                gecersiz_parti.append(n)
                return {"id": h["id"], "ihlaller": [{"madde": "C1", "alinti": uk.cumleler(h["govde"])[0],
                                                     "cumle_no": 1, "aciklama": "x"}],
                        "maddeler": {m: "yok" for m in vh.MADDELER["K"]}, "gecti": True}   # tutarsız: geçersiz
            return None
        hakemle(self.Y, karar)
        r, out = self.vh("oku")
        self.assertEqual(r, 2, out)                 # küçük örneklemde uydurma %33 > %3: M merceği durur
        self.assertIn("DUR: M", out)
        self.assertIn("GEÇERSİZ", out)
        hakemle(self.Y)            # geçersiz partinin yeniden koşusu (t2) temiz
        r, out = self.vh("karar", "--pilot", "--taslak-kart")
        self.assertEqual(r, 0, out)
        kabul = {k["sha1"] for k in vh.jsonl_oku(self.Y.v("kabul.jsonl"))}
        ret = vh.jsonl_oku(self.Y.v("ret.jsonl"))
        self.assertNotIn(uyd, kabul)
        self.assertNotIn(gerc, kabul)
        self.assertNotIn(gecersiz_var, kabul)      # tek yönlü veto: geçersiz partideki 'var' da düşürür
        self.assertTrue(any(x["sha1"] == uyd and x["uydurma"] for x in ret))
        self.assertEqual(len(kabul), 5)
        k0 = vh.jsonl_oku(self.Y.v("kabul.jsonl"))[0]
        self.assertIn("kapi.py", " ".join(k0["bilesenler"]["kod"]))
        self.assertEqual({o["mercek"] for o in k0["kararlar"] if o["oy"] == "yok" and o["gecerli"]}, set("MDK"))
        # kuyruk: düşen tohumlar deneme 2 ile
        kuyruk = {t["id"]: t["deneme"] for t in vh.jsonl_oku(self.Y.v("kuyruk.jsonl"))}
        self.assertEqual(kuyruk, {"chase-0001": 2, "niloya-0001": 2, "pamuk-0001": 2})
        # izin listesi prepare_ft2 ile birebir okunur (sha1'ler tam bir kez)
        eg, dog, _ = prepare_ft2.yalniz_oku(self.Y.v("izin.txt"), prepare_ft2.kanarya_sha1leri(self.Y.v("izin.txt")))
        self.assertEqual({h["sha1"] for h in eg + dog}, kabul)
        self.assertEqual(len(dog), 1)                # Tosbi x orman hücresinde 2 kabul -> 1 doğrulama
        # hakemden sonra metin değişirse kabul olmaz
        p = Path(self.Y.v("aday", "elsa_1.txt"))
        p.write_text(p.read_text().replace("güzel bir kış", "soğuk bir kış"))
        s = vh.karar_ver(self.Y, pilot=True, taslak_kart=True, bg=self.bg)
        self.assertEqual(len(s["kabul"]), 4)
        self.assertTrue(any("kaynak_degisti" in k for k in s["bekleyen"]))
        # onaysız kart --taslak-kart olmadan kabul edilmez (depodaki kartlar onaylı: onayı kaldırılmış kopya)
        bg_taslak = copy.copy(self.bg)
        bg_taslak.kartlar = {a: {**k, "onayli": False} for a, k in self.bg.kartlar.items()}
        self.assertEqual(len(vh.karar_ver(self.Y, pilot=True, bg=bg_taslak)["kabul"]), 0)
        # uyum
        u = vh.uyum_hesapla(self.Y)
        self.assertEqual(u["mercek"]["M"]["ikisi_var"], 1)            # iki hakem de uydurma alıntıyla 'var'
        self.assertEqual(u["mercek"]["D"]["ikisi_var"], 1)
        self.assertEqual(u["mercek"]["M"]["uydurma"], 2)
        self.assertEqual(u["kanarya"]["M"]["hepsi"]["oran"], 1.0)

    def test_kanarya_kacirilinca_parti_gecersiz(self):
        self.kapi()
        _, isler = self.hazirla("M", parti_boyu=4, pilot=True, dagilim=(0, 1, 0))
        hakemle(self.Y, lambda L, n, k, h, y, ilk: "kacir" if y["rol"] == "kanarya" else None)
        oylar, partiler = vh.oylari_topla(self.Y)
        kanaryali = {p["parti"] for p in partiler if p.get("kanarya")}
        self.assertTrue(kanaryali)
        self.assertTrue(all(p["durum"] == "gecersiz" for p in partiler if p["parti"] in kanaryali and p["deneme"] == 1))
        self.assertTrue(all(o["gecerli"] is False for o in oylar if o["parti"] in kanaryali))
        d = vh.dur_denetimi(partiler, oylar)
        self.assertTrue(d["M"]["dur"])
        # yeniden koşu bekleyen partinin hikâyeleri yeni partiye konmaz
        _, isler2 = self.hazirla("M", parti_boyu=4, pilot=True)
        bekleyen = {k["sha1"] for n in kanaryali for k in vh.json_oku(self.Y.hakem("M", "yerlesim.json"))[str(n)]["konumlar"]
                    if k["rol"] == "hedef"}
        yeni = {k["sha1"] for i in isler2 for k in vh.json_oku(self.Y.hakem("M", "yerlesim.json"))[str(i["parti"])]["konumlar"]}
        self.assertFalse(bekleyen & yeni)

    def test_kanarya_tabani_var(self):
        """Kanaryanın değiştirilmemiş kısmına verilen 'var' tabanı düşürür."""
        self.kapi()
        self.hazirla("M", parti_boyu=4, pilot=True, dagilim=(0, 1, 0))
        yer = vh.json_oku(self.Y.hakem("M", "yerlesim.json"))
        tabanlar = set()

        def karar(L, n, k, h, y, ilk):
            if y["rol"] != "kanarya":
                return None
            cs = uk.cumleler(h["govde"])
            degismeyen = [i for i in range(1, len(cs) + 1) if all(abs(i - d) > 1 for d in y["degisen_cumle"])]
            tabanlar.add(y["taban_sha1"])
            return ("M6", cs[degismeyen[-1] - 1])
        hakemle(self.Y, karar)
        oylar, partiler = vh.oylari_topla(self.Y)
        d = vh.oy_durumu(oylar, partiler)
        self.assertTrue(tabanlar)
        for s in tabanlar:
            self.assertTrue(any(x["kaynak"] == "kanarya_tabani" for x in d[s]["dusen"]))
        self.assertTrue(yer)

    def test_altin_ve_uyum(self):
        self.kapi()
        r, out = self.vh("altin", "sec", "--n", "8", "--okur-orani", "0.25", "--taslak-kart")
        self.assertEqual(r, 0, out)
        gizli = vh.json_oku(self.Y.d("pilot", "altin_gizli.json"))
        hedef = [o for o in gizli["ogeler"] if o["rol"] == "hedef"]
        okur = [o for o in gizli["ogeler"] if o["rol"] == "okur_kanarya"]
        self.assertEqual(len(hedef), 8)
        self.assertEqual(len(okur), 2)
        self.assertEqual({o["yari"] for o in hedef}, {"gelistirme", "olcum"})
        md = Path(self.Y.d("pilot", "insan.md")).read_text()
        self.assertNotIn("urun/", md)                          # kimlik ve rol gizli
        with self.assertRaises(SystemExit):                     # etiketlemeden kurul yok
            self.vh("altin", "kurul", "--taslak-kart", "--taban-aday")
        # etiketle: okur kanaryaları ve iki hedef kusurlu
        kusurlu = {o["sira"] for o in okur} | {hedef[0]["sira"], hedef[1]["sira"]}
        satirlar, sira = [], None
        for s in md.splitlines():
            if s.startswith("## "):
                sira = int(s[3:])
            if s.startswith("Etiket:"):
                s = "Etiket: kusurlu: 2 | anlamsız | M" if sira in kusurlu else "Etiket: kusursuz"
            satirlar.append(s)
        Path(self.Y.d("pilot", "insan.md")).write_text("\n".join(satirlar) + "\n")
        r, out = self.vh("altin", "oku")
        self.assertEqual(r, 0, out)
        et = vh.altin_etiketleri(self.Y)
        self.assertEqual(sum(e["etiket"] == "kusurlu" for e in et.values()), 2)
        self.assertEqual(vh.json_oku(self.Y.d("altin", "okur.json")), {"okur_kanarya": 2, "yakalanan": 2})
        r, out = self.vh("altin", "kurul", "--taslak-kart", "--taban-aday", "--parti-boyu", "4")
        self.assertEqual(r, 0, out)
        kus = {hedef[0]["sha1"], hedef[1]["sha1"]}
        hakemle(self.Y, lambda L, n, k, h, y, ilk: (("M2", uk.cumleler(h["govde"])[1])
                                                    if L == "M" and y["sha1"] in kus and y["rol"] == "hedef" else None))
        u = vh.uyum_hesapla(self.Y)
        k = u["altin"]["hepsi"]["kurul"]
        self.assertEqual((k["kusurlu"], k["yakalanan"], k["yanlis_ret"]), (2, 2, 0))
        self.assertEqual(k["q_hat"], 0.0)
        self.assertEqual(u["mercek"]["M"]["pozitif_uyum"], 1.0)
        r, out = self.vh("uyum", "--pilot")
        self.assertEqual(r, 0)
        self.assertTrue(os.path.exists(self.Y.d("uyum.json")))

    def test_clopper_pearson(self):
        self.assertAlmostEqual(vh.cp_alt(60, 60), 0.9513, places=3)
        self.assertGreaterEqual(vh.cp_alt(59, 60), 0.90)      # 60 kusurludan 1 kaçırma geçer
        self.assertLess(vh.cp_alt(58, 60), 0.90)              # 2 kaçırma geçmez
        self.assertAlmostEqual(vh.cp_ust(0, 308), 0.0097, places=4)


class Sizinti(Ortak):
    hazirla = Kurul.hazirla

    """Uçtan uca sınamada bulunan sızıntı yolları (kusurlu hikâyenin izin listesine girmesi)."""

    def test_bozuk_ciktidaki_isaret_kaybolmaz(self):
        """Geçersiz partideki 'VAR', maddesiz gecti=false ve kimliği yanlış kayıttaki 'var' tek yönlü veto
        sayılır: temiz yeniden koşu onları silmez."""
        aday = self.kapi()
        sha = {r["tohum"]: s for s, r in aday.items()}
        hedef = {sha["chase-0001"]: "buyuk", sha["niloya-0001"]: "gecti", sha["pamuk-0001"]: "kimlik"}
        self.hazirla("M", parti_boyu=4, pilot=True, dagilim=(1, 0, 0))

        def karar(L, n, k, h, y, ilk):
            tur = hedef.get(y["sha1"]) if ilk else None
            if tur is None:
                return None
            r = {"id": h["id"], "ihlaller": [], "maddeler": {m: "yok" for m in vh.MADDELER[L]}, "gecti": True}
            if tur == "buyuk":
                r["maddeler"]["M3"] = "VAR"
            elif tur == "gecti":
                r["gecti"] = False
            else:
                r["id"] += "x"
                r["maddeler"]["M3"] = "var"
                r["gecti"] = False
                r["ihlaller"] = [{"madde": "M3", "alinti": uk.cumleler(h["govde"])[0], "cumle_no": 1,
                                  "aciklama": "x"}]
            return r
        hakemle(self.Y, karar)
        hakemle(self.Y)                      # geçersiz partilerin temiz yeniden koşusu
        oylar, partiler = vh.oylari_topla(self.Y)
        d = vh.oy_durumu(oylar, partiler)
        for s in hedef:
            self.assertTrue(d[s]["dusen"], hedef[s])
        self.assertFalse(any(d[s]["dusen"] for s in aday if s not in hedef))

    def test_altin_kusurlu_ve_kapi_yeniden(self):
        """Okurun 'kusurlu' dediği altın hikâye kurul 'yok' dese de girmez; kapı yeniden koşulunca kabul edilmiş
        hikâye K9'da kendisinin kopyası sayılmaz."""
        aday = self.kapi()
        kus = sorted(aday)[0]
        vh.jsonl_yaz(self.Y.d("altin", "etiketler.jsonl"),
                     [{"sha1": kus, "etiket": "kusurlu", "cumle": 2, "neden": "anlamsız", "mercek": "M"}])
        for L in vh.MERCEKLER:
            self.hazirla(L, parti_boyu=4, pilot=True, dagilim=(1, 0, 0))
        hakemle(self.Y)
        r, out = self.vh("karar", "--pilot", "--taslak-kart")
        self.assertEqual(r, 0, out)
        kabul = {k["sha1"] for k in vh.jsonl_oku(self.Y.v("kabul.jsonl"))}
        self.assertNotIn(kus, kabul)
        self.assertEqual(kabul, set(aday) - {kus})
        self.assertTrue(any(x["sha1"] == kus and x["madde"] == "altin_kusurlu"
                            for x in vh.jsonl_oku(self.Y.v("ret.jsonl"))))
        aday2 = self.kapi()                  # ör. kapı sürümü değişti: kapı yeniden koşar
        for s in kabul:                      # hiçbir kabul kendisinin kopyası sayılmaz
            self.assertFalse([x for x in aday2[s]["ihlaller"] if aday2[s]["kimlik"] in x["aciklama"]])
        # iki Tosbi hikâyesi birbirinin yakın kopyası değil: kapı yeniden koşunca bütün kabuller yine geçer
        self.assertEqual([s[:8] for s in kabul if not aday2[s]["gecti"]], [])
        self.assertEqual({k["sha1"] for k in vh.karar_ver(self.Y, pilot=True, taslak_kart=True, bg=self.bg)["kabul"]},
                         kabul)


class Onarim(Ortak):
    """Onarım döngüsü: yalnız hakem gerekçesiyle düşen aday editöre alıntılı bulgularla döner; onarılmış hikâye
    yeni adaydır (deneme ebeveyn + 1, '@onarim'), K9'da kendi ebeveyninin kopyası sayılmaz, en çok deneme 3."""
    M6 = "Chase burnunu yere yaklaştırdı"
    D6 = "Chase'in burnu yine işe yaramıştı"
    hazirla = Kurul.hazirla

    def ilk_tur(self):
        aday = self.kapi()
        sha = {r["tohum"]: s for s, r in aday.items()}
        for L in vh.MERCEKLER:
            self.hazirla(L, parti_boyu=4, pilot=True, dagilim=(1, 0, 0))

        def karar(L, n, k, h, y, ilk):
            if y["sha1"] == sha["chase-0001"] and L in "MD":
                return ("M6", self.M6) if L == "M" else ("D6", self.D6)    # iki M hakemi aynı alıntı
            if y["sha1"] == sha["niloya-0001"] and L == "K":
                return ("K1", uk.cumleler(h["govde"])[0])                   # figür düzeyi: onarılmaz
            return None
        hakemle(self.Y, karar)
        r, out = self.vh("karar", "--pilot", "--taslak-kart")
        self.assertEqual(r, 0, out)
        return aday, sha

    def test_onar_istemi_ve_yeni_aday(self):
        aday, sha = self.ilk_tur()
        ebeveyn = sha["chase-0001"]
        kuyruk = {t["id"]: t for t in vh.jsonl_oku(self.Y.v("kuyruk.jsonl"))}
        self.assertTrue(kuyruk["chase-0001"]["onarilabilir"])
        self.assertEqual(kuyruk["chase-0001"]["ebeveyn"], ebeveyn)
        self.assertFalse(kuyruk["niloya-0001"]["onarilabilir"])
        # istem: kılavuz, kart, özgün blok ve tekrarsız, alıntılı bulgular
        r, out = self.vh("onar-istemi", "--figur", "Chase", "--taslak-kart")
        self.assertEqual(r, 0, out)
        md = Path(self.Y.v("onar", "chase_1.md")).read_text()
        js = vh.json_oku(self.Y.v("onar", "chase_1.json"))
        self.assertEqual(js["dosya"], "aday/chase_onar1.txt")
        self.assertEqual(js["tohumlar"], [{"id": "chase-0001", "deneme": 2, "onarim": ebeveyn,
                                           "ebeveyn_kimlik": aday[ebeveyn]["kimlik"], "yeniden_yaz": False,
                                           "bulgu": 2}])
        self.assertIn("**Kural bütçesi.**", md)                   # kılavuz birebir
        self.assertIn("## Kart: Chase", md)
        self.assertIn(uk.blok_yaz(aday[ebeveyn]["kayit"], "chase-0001").strip(), md)   # özgün blok
        self.assertIn(f'Alıntı: "{self.M6}"', md)
        self.assertIn(f'Alıntı: "{self.D6}"', md)
        self.assertEqual(md.count(f'Alıntı: "{self.M6}"'), 1)    # iki hakemin aynı bulgusu tek kez
        self.assertIn("Cümle 6: «Chase burnunu yere yaklaştırdı.»", md)
        self.assertIn("Her olay bir öncekinden çıkıyor", md)     # madde tanımı
        self.assertIn(f"@onarim: {ebeveyn}", md)
        self.assertIn("aday/chase_onar1.txt", md)
        self.assertIn("kontrol", md)
        # K1 (figür düzeyi) ile düşen onarılmaz; aynı tohum ikinci kez atanmaz; yeni yazım onu almaz
        self.assertEqual(vh.onar_istemi(self.Y, "Niloya", taslak_kart=True, bg=self.bg), [])
        self.assertEqual(vh.onar_istemi(self.Y, "Chase", taslak_kart=True, bg=self.bg), [])
        with self.assertRaises(SystemExit):
            sessiz(vh.yaz_istemi, self.Y, "Chase", taslak_kart=True, bg=self.bg)
        # editör: tek cümle değişir (ebeveynin yakın kopyası)
        eski = uk.blok_yaz(aday[ebeveyn]["kayit"], "chase-0001")
        onarilan = eski.replace(self.D6 + ".", "Chase çok sevindi.").replace(
            "@tohum: chase-0001", f"@tohum: chase-0001\n@onarim: {ebeveyn}")
        Path(self.Y.v("aday", "chase_onar1.txt")).write_text(onarilan)
        r, out = self.vh("kontrol", self.Y.v("aday", "chase_onar1.txt"), "--taslak-kart")
        self.assertEqual(r, 0, out)
        aday2 = self.kapi()
        cocuk = next(x for x in aday2.values() if x.get("onarim"))
        self.assertEqual((cocuk["tohum"], cocuk["deneme"], cocuk["onarim"]), ("chase-0001", 2, ebeveyn))
        self.assertTrue(cocuk["gecti"], cocuk["ihlaller"])
        self.assertFalse([x for x in cocuk["ihlaller"] if x["kapi"] == "K9"])
        self.assertEqual(aday2[ebeveyn]["deneme"], 1)
        # yeni hakemler: onarım bulguları parti dosyasına girmez
        for L in vh.MERCEKLER:
            self.hazirla(L, parti_boyu=4, pilot=True, dagilim=(1, 0, 0))
            for i in vh.json_oku(self.Y.hakem(L, "gorev.json"))["isler"]:
                metin = Path(i["parti_dosyasi"]).read_text()
                self.assertNotIn(ebeveyn, metin)
                self.assertNotIn("onarim", metin)
        hakemle(self.Y)
        r, out = self.vh("karar", "--pilot", "--taslak-kart")
        self.assertEqual(r, 0, out)
        self.assertIn("(1 onarım)", out)
        kabul = {k["sha1"]: k for k in vh.jsonl_oku(self.Y.v("kabul.jsonl"))}
        self.assertIn(cocuk["sha1"], kabul)
        self.assertNotIn(ebeveyn, kabul)
        self.assertEqual((kabul[cocuk["sha1"]]["deneme"], kabul[cocuk["sha1"]]["onarim"]), (2, ebeveyn))
        self.assertTrue(any(x["sha1"] == ebeveyn for x in vh.jsonl_oku(self.Y.v("ret.jsonl"))))
        self.assertNotIn("chase-0001", {t["id"] for t in vh.jsonl_oku(self.Y.v("kuyruk.jsonl"))})
        figur_dosyasi = Path(self.Y.v("chase.txt")).read_text()    # eğitime giden dosyada @onarim yok
        self.assertIn("Chase çok sevindi.", figur_dosyasi)
        self.assertNotIn("@onarim", figur_dosyasi)

    def test_k9_ebeveyn_haric(self):
        onceki = [("Chase", "chase-0001", "urun/chase#a", "gövde", True, "a" * 40),
                  ("Chase", "chase-0002", "urun/chase#b", "gövde", True, "b" * 40),
                  ("Chase", "chase-0003", "urun/chase#c", "gövde", True, "c" * 40)]
        havuz = vh._tur_havuzu(onceki, "Chase", "chase-0001", {"b" * 40})
        self.assertEqual([k for k, _ in havuz], ["urun/chase#c"])   # kendi ebeveyni ve reddedilen hariç

    def test_deneme_siniri(self):
        aday, sha = self.ilk_tur()
        ebeveyn = sha["chase-0001"]
        b = {"tohum": "chase-0001", "onarim": ebeveyn}
        red = {ebeveyn}
        self.assertEqual(vh._onarim_denetle(b, {ebeveyn: {"tohum": "chase-0001", "deneme": 2}}, red), (3, []))
        d, ih = vh._onarim_denetle(b, {ebeveyn: {"tohum": "chase-0001", "deneme": 3}}, red)
        self.assertEqual(d, 4)
        self.assertEqual([x["kod"] for x in ih], ["K1.deneme_siniri"])
        self.assertEqual([x["kod"] for x in vh._onarim_denetle(b, {ebeveyn: {"tohum": "x", "deneme": 1}}, set())[1]],
                         ["K1.onarim", "K1.onarim"])
        self.assertEqual(vh._onarim_denetle(b, {}, red)[1][0]["kod"], "K1.onarim")
        # ebeveyn 3. denemeyse: onarım istemi vermez, karar tohumu bırakır
        kayitlar = vh.jsonl_oku(self.Y.v("aday.jsonl"))
        for x in kayitlar:
            if x["sha1"] == ebeveyn:
                x["deneme"] = 3
        vh.jsonl_yaz(self.Y.v("aday.jsonl"), kayitlar)
        ist = vh.json_oku(self.Y.v("istem", "chase_1.json"))
        ist["tohumlar"][0]["deneme"] = 3
        vh.json_yaz(self.Y.v("istem", "chase_1.json"), ist)
        self.assertEqual(vh.onarim_adaylari(self.Y, "Chase", "chase"), [])
        s = vh.karar_ver(self.Y, pilot=True, taslak_kart=True, bg=self.bg)
        self.assertIn("chase-0001", {t["id"] for t in s["birakilan"]})
        self.assertNotIn("chase-0001", {t["id"] for t in s["kuyruk"]})
        # 2. denemede düşen: onarılabilirse 3. deneme (yalnız onarım) kuyrukta, K1 ile düşen bırakılır
        for x in kayitlar:
            if x["sha1"] in (ebeveyn, sha["niloya-0001"]):
                x["deneme"] = 2
        vh.jsonl_yaz(self.Y.v("aday.jsonl"), kayitlar)
        for fk in ("chase", "niloya"):
            ist = vh.json_oku(self.Y.v("istem", f"{fk}_1.json"))
            ist["tohumlar"][0]["deneme"] = 2
            vh.json_yaz(self.Y.v("istem", f"{fk}_1.json"), ist)
        s = vh.karar_ver(self.Y, pilot=True, taslak_kart=True, bg=self.bg)
        kuyruk = {t["id"]: t for t in s["kuyruk"]}
        self.assertEqual((kuyruk["chase-0001"]["deneme"], kuyruk["chase-0001"]["onarilabilir"]), (3, True))
        self.assertIn("niloya-0001", {t["id"] for t in s["birakilan"]})
        self.assertEqual(len(vh.onarim_adaylari(self.Y, "Chase", "chase")), 1)


class EskiKomutlar(unittest.TestCase):
    def test_eski_hazirla_yolu(self):
        """--lens'siz hazirla eski fonksiyona eski varsayılanla (parti 40) gider."""
        yakalanan = {}
        eski = vh.hazirla
        vh.hazirla = lambda a: yakalanan.update(vars(a))
        try:
            vh.main(["hazirla", "oyuncak_v4", "--onek", "tek_kus_2"])
        finally:
            vh.hazirla = eski
        self.assertEqual((yakalanan["klasor"], yakalanan["onek"], yakalanan["parti_boyu"]), ("oyuncak_v4", "tek_kus_2", 40))

    def test_parti_boyu_siniri(self):
        with self.assertRaises(SystemExit):
            vh.hazirla_urun(vh.Yollar("urun_v1", tempfile.gettempdir()), "M", parti_boyu=12, bg=object())


if __name__ == "__main__":
    unittest.main()
