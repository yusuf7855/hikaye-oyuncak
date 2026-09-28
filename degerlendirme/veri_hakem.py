"""Eğitim verisini hakemle.

ESKİ HAT (eski klasörler için kalır; HAKEM_VERI.md, DUZELTICI.md): yalnız 10/10 alan hikâyeler eğitime girer.
Kullanım: python degerlendirme/veri_hakem.py hazirla <klasör> [--onek tek_kus_2] [--parti-boyu 40] [--ad AD]
          python degerlendirme/veri_hakem.py ozet [<ad> ...]       # -> data/veri_haric.txt (10 almayanlar)
          python degerlendirme/veri_hakem.py duzelt <ad>           # 10 almayanlar -> veri_<ad>/duzelt.json (düzeltici)
          python degerlendirme/veri_hakem.py tekrar <ad>           # düzeltilenleri yeniden hakeme: parti_tN.json
Döngü: yaz -> kontrol.py -> hazirla -> hakem -> duzelt -> düzeltici ajan dosyayı düzeltir -> tekrar -> hakem ...
Bir hikâyenin son puanı, en son hakemlendiği partideki puandır (parti_tN, parti_N'yi geçersiz kılar).
<klasör>: data/ altındaki hikâye klasörü (oyuncak_v4, oyuncak_populer); kimlikler prepare_ft2.kimlik_ver ile aynı
("v4/tek_kus_2#5", "populer/elsa_1#3"). Çıktı: degerlendirme/veri_<ad>/parti_N.json, gorev.json.
ozet bütün veri_* klasörlerindeki puanları toplar; 10'dan düşük (ya da puanı eksik) hikâyelerin kimliklerini
data/veri_haric.txt'ye yazar: ince ayarda prepare_ft2 --haric data/veri_haric.txt.

ÜRÜN HATTI (docs/KUSURSUZ_VERI.md; Adım 0h). <ad> varsayılanı urun_v1; veri data/<ad>/, hakem işleri
degerlendirme/<ad>/ altında (--kok <dizin> ile ikisi de <dizin>/data/<ad> ve <dizin>/degerlendirme/<ad> olur).
  kart-kontrol [--kilitle]            kart şeması, kaynaklar, D denetimi, kural düzenli ifadeleri; onaylı kartın
                                      sha1'i data/<ad>/kart_kilidi.json'a kilitlenir (Adım 1)
  tohum --figur F --n 400 --tohum 2026 [--denetle]   data/<ad>/tohum/<figür>.jsonl (Adım 3, 'Sistem tarafı')
  yaz-istemi --figur F [--n 12]       yazar ajanının tam istemi: data/<ad>/istem/<figür>_<parti>.md (+ .json)
  kontrol <yazar dosyası>             yazarın öz-denetimi (Kural 10): kapılar + yama sayacı (en çok 1 yama)
  kapi --figur F | --hepsi            data/<ad>/aday/<figür>_*.txt -> data/<ad>/aday.jsonl (Adım 5)
  hazirla <ad> --lens M|D|K           hakem partileri (Adım 7): <= 10 hikâye, 0-2 kanarya, dolgu, karıştırma,
                                      ikinci hakem farklı bileşim ve ters sıra, madde sırası karışık
  oku [<ad>]                          puan JSON'larını doğrular, 'gecti'yi yeniden hesaplar, alıntıyı metinde
                                      arar, kanarya yakalamasını denetler (Adım 8) -> hakem/oylar.jsonl
  karar [<ad>]                        tek yönlü veto; kabul.jsonl, ret.jsonl, kuyruk.jsonl, izin.txt (Adım 8-9)
  altin sec|oku|kurul                 altın set seçimi, kör etiket şablonu, etiket okuma, kurul partileri (Adım 6)
  uyum [<ad>] [--pilot]               pozitif uyum, ikinci hakemin tek başına yakalaması, kanarya yakalama,
                                      altın sette kaçırma/yanlış ret/q̂ ve konum etkisi (Adım 6, Pilot ölçüleri)
Pilot-0 akışı: tohum -> yaz-istemi -> (yazar) kontrol -> kapi -> hazirla -> (hakem) -> oku -> karar.
"""
import argparse, collections, difflib, glob, hashlib, importlib.util, json, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def hikayeler(klasor, onek=""):
    d = os.path.join(ROOT, "data", klasor)
    spec = importlib.util.spec_from_file_location(f"kontrol_{klasor}", os.path.join(d, "kontrol.py"))
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    iyi, _ = k.oku()   # kimlik sırası dosyanın bütün geçerlilerine göre: önek filtresi sonradan
    kartlar = {}
    yol = os.path.join(d, "karakterler.json")
    if os.path.exists(yol):
        kartlar = {c["isim"]: c for c in json.load(open(yol, encoding="utf-8"))}
    sira, out = {}, []
    for h in iyi:
        n = sira.get(h["dosya"], 0)
        sira[h["dosya"]] = n + 1
        if not h["dosya"].startswith(onek):
            continue
        kayit = {"id": f"{klasor.split('_')[-1]}/{h['dosya'][:-4]}#{n}", "metin": h["metin"]}
        if h["turler"][0] in kartlar:
            kayit["kart"] = kartlar[h["turler"][0]]
        out.append(kayit)
    return out


def hazirla(a):
    H = hikayeler(a.klasor, a.onek)
    ad = a.ad or (a.onek or a.klasor)
    d = os.path.join(HERE, f"veri_{ad}")
    os.makedirs(d, exist_ok=True)
    isler = []
    for i in range(0, len(H), a.parti_boyu):
        n = i // a.parti_boyu
        json.dump(H[i:i + a.parti_boyu], open(os.path.join(d, f"parti_{n}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        isler.append({"parti": os.path.join(d, f"parti_{n}.json"), "cikti": os.path.join(d, f"puan_{n}.json")})
    json.dump({"klasor": a.klasor}, open(os.path.join(d, "kaynak.json"), "w"))
    json.dump({"kural": os.path.join(HERE, "HAKEM_VERI.md"), "isler": isler}, open(os.path.join(d, "gorev.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"{len(H)} hikâye -> {d} ({len(isler)} parti)")


def son_puanlar(d):
    """{id: (puan, neden, kayıt)}: parti_N sonra parti_tN (tekrar) sırasıyla; sonraki öncekini ezer."""
    son = {}
    dosyalar = sorted(glob.glob(os.path.join(d, "parti_[0-9]*.json"))) + \
        sorted(glob.glob(os.path.join(d, "parti_t*.json")), key=lambda f: (len(f), f))
    for f in dosyalar:
        H = json.load(open(f, encoding="utf-8"))
        p = f.replace("parti_", "puan_")
        P = {r["id"]: r for r in json.load(open(p, encoding="utf-8"))} if os.path.exists(p) else {}
        for h in H:
            r = P.get(h["id"])
            son[h["id"]] = (r.get("puan") if r else None, (r or {}).get("neden", ""), h)
    return son


def duzelt(a):
    d = os.path.join(HERE, f"veri_{a.ad}")
    klasor = json.load(open(os.path.join(d, "kaynak.json")))["klasor"]
    liste = [{"id": i, "dosya": f"data/{klasor}/{i.split('/')[1].split('#')[0]}.txt",
              "ilk_cumle": h["metin"].split(". ")[0][:80], "neden": n, "metin": h["metin"],
              **({"kart": h["kart"]} if "kart" in h else {})}
             for i, (p, n, h) in son_puanlar(d).items() if p is not None and p < 10]
    json.dump(liste, open(os.path.join(d, "duzelt.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(liste)} hikâye düzeltilecek -> {d}/duzelt.json")


def tekrar(a):
    """Düzeltilen hikâyelerin güncel metinleriyle yeni bir hakem partisi (parti_tN.json)."""
    d = os.path.join(HERE, f"veri_{a.ad}")
    ids = {x["id"] for x in json.load(open(os.path.join(d, "duzelt.json"), encoding="utf-8"))}
    klasor = json.load(open(os.path.join(d, "kaynak.json")))["klasor"]
    guncel = [h for h in hikayeler(klasor) if h["id"] in ids]
    n = len(glob.glob(os.path.join(d, "parti_t*.json")))
    json.dump(guncel, open(os.path.join(d, f"parti_t{n}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(guncel)}/{len(ids)} hikâye yeniden hakeme -> {d}/parti_t{n}.json (eksikler kontrol.py'yi geçemedi)")


def ozet(a):
    klasorler = [os.path.join(HERE, f"veri_{x}") for x in a.adlar] if a.adlar else \
        sorted(p for p in glob.glob(os.path.join(HERE, "veri_*")) if os.path.exists(os.path.join(p, "kaynak.json")))
    haric, n, on = [], 0, 0
    for d in klasorler:
        for i, (p, _, _) in son_puanlar(d).items():
            n += 1
            if p == 10:
                on += 1
            else:
                haric.append(i)
    open(os.path.join(ROOT, "data", "veri_haric.txt"), "w").write("\n".join(haric) + "\n")
    print(f"{n} hikâye hakemlendi: {on} tam puan (%{100 * on / max(1, n):.0f}), {len(haric)} dışarıda -> data/veri_haric.txt")




# ================================================================ ÜRÜN HATTI (KUSURSUZ_VERI.md)
# Ağır modüller (kapi: sözlük + tokenizer; bozucu) yalnız ürün komutlarında yüklenir; eski komutlar etkilenmez.
if HERE not in sys.path:
    sys.path.insert(0, HERE)

MERCEKLER = "MDK"
MADDELER = {"M": [f"M{i}" for i in range(1, 11)], "D": [f"D{i}" for i in range(1, 10)],
            "K": [f"K{i}" for i in range(1, 9)] + [f"C{i}" for i in range(1, 7)]}
EKSIKLIK = {"M1", "M5", "M9"}                  # alıntı yerine cumle_no kabul edilen eksiklik maddeleri
HAKEM_SAYISI = {"M": 2, "D": 2, "K": 1}        # tam ölçek; pilotta K de 2 (--pilot)
KANARYA_DAGILIM = (0.2, 0.5, 0.3)              # partide 0 / 1 / 2 kanarya
ALINTI_MESAFE = 2                              # alıntı eşleşmesinde en çok düzenleme mesafesi (karakter)
DUR_PENCERE, DUR_KACIRMA, DUR_UYDURMA = 50, 0.10, 0.03


def _uk():
    import urun_kayit
    return urun_kayit


def _kapi():
    import kapi
    return kapi


class Yollar:
    """data/<ad> (veri: tohum, aday, kabul, izin) ve degerlendirme/<ad> (hakem partileri, oylar, altın, uyum)."""

    def __init__(self, ad="urun_v1", kok=None):
        self.ad = ad
        self.veri = os.path.join(kok, "data", ad) if kok else os.path.join(ROOT, "data", ad)
        self.deg = os.path.join(kok, "degerlendirme", ad) if kok else os.path.join(HERE, ad)

    def v(self, *p):
        return os.path.join(self.veri, *p)

    def d(self, *p):
        return os.path.join(self.deg, *p)

    def tohum(self, fk):
        return self.v("tohum", f"{fk}.jsonl")

    def hakem(self, lens, *p):
        return self.d("hakem", lens, *p)

    def goreli(self, yol):
        return os.path.relpath(yol, ROOT) if os.path.abspath(yol).startswith(ROOT + os.sep) else yol


def jsonl_oku(yol):
    if not os.path.exists(yol):
        return []
    with open(yol, encoding="utf-8") as f:
        return [json.loads(s) for s in f if s.strip()]


def _yaz(yol, metin):
    """Yarım dosya bırakmayan yazım (geçici dosya + rename)."""
    os.makedirs(os.path.dirname(os.path.abspath(yol)), exist_ok=True)
    gecici = f"{yol}.yaziliyor"
    with open(gecici, "w", encoding="utf-8") as f:
        f.write(metin)
    os.replace(gecici, yol)


def jsonl_yaz(yol, kayitlar):
    _yaz(yol, "".join(json.dumps(k, ensure_ascii=False) + "\n" for k in kayitlar))


def json_yaz(yol, veri):
    _yaz(yol, json.dumps(veri, ensure_ascii=False, indent=1) + "\n")


def json_oku(yol, varsayilan=None):
    if not os.path.exists(yol):
        return varsayilan
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def sha256_dosya(yol):
    h = hashlib.sha256()
    with open(yol, "rb") as f:
        for p in iter(lambda: f.read(1 << 20), b""):
            h.update(p)
    return h.hexdigest()


def _olgu(x):
    return x.get("deger") if isinstance(x, dict) else x


def _figur_kimligi(ad):
    return _uk().figur_kimligi(ad)


def _tr_kucuk(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


# ---------------------------------------------------------------- kart-kontrol (Adım 1 geçme şartı)

KAYNAK_TURLERI = {"yapimci", "trt", "vikipedi", "bolum", "urun", "kullanici", "diger"}
YER_KARSILIK = {"dogrulandi", "kismen", "dogrulanmadi", "yok", "urun_tanimi"}
YAN_TIP = {"adli", "rol", "isimsiz"}
KART_ALANLARI = ["kimlik", "grup", "onayli", "ad", "okunus", "seri", "kimlik_cumlesi", "tur", "ozellikler",
                 "guvenli_ozellik_kullanimi", "yerler", "yanlar", "dunya_kurallari", "yasaklar",
                 "izinli_dunya_kokleri", "urun_yan_eslesmesi", "acik_noktalar"]
# Kart metninde olmaması gereken deyim ve mecazlar (D6); genişletilebilir
KART_DEYIMLER = ["burnunu sok", "ateş topu", "başını derde", "gözü gibi", "kulak ver", "dert aç", "elinden geleni",
                 "içi rahat", "gözden kaç", "aklı evde", "kalbinde yer", "sırt sırta", "üstesinden gel",
                 "tatlı dert", "başının etini", "ağzı kulak", "yüreği ağz"]
# Anahtar ifadelerin yanlışlıkla yakalamaması gereken sık kelimeler
SAHTE_DOST = ["sorun", "sorunu", "sorunlar", "toprak", "topladı", "toplamak", "ağaç", "ağacın", "ağladı", "ağır",
              "ağız", "karar", "kardeş", "deniz", "derin", "kural", "kabul", "merdiven", "bilgi", "sabah", "kuyu",
              "hızır", "havuz", "kulübe"]
# Dünya kuralı düzenli ifadelerinin öz-sınaması: (yakalanmalı, yakalanmamalı). Kart bir gün kendi
# 'kural_ornekleri' alanını taşırsa o kullanılır.
KURAL_ORNEKLERI = {
    "niloya": (["Ağabeyi Mete koşarak geldi.", "Mete, Niloya'nın ağabeyiydi.", "abisi Mete güldü.",
                "Tospik hızla koştu.", "Tospik Niloya'nın yanına koştu.", "Niloya nehre girdi."],
               ["Ağabeyi Murat geldi.", "Mete, Murat'ın arkadaşıydı.", "Tospik yavaşça yürüdü.",
                "Niloya nehrin kıyısına oturdu.", "Mete ağaca baktı."]),
    "masa": (['"Gel," dedi Koca Ayı.', "Koca Ayı ona dönüp şöyle dedi.", "Kirpi yavaşça sordu.",
              '"Bak," diye seslendi sincap.', "Koca Ayı Maşa'ya dönüp dedi."],
             ["Koca Ayı başını salladı.", '"Gel," dedi Maşa.', "Kirpi elmayı Maşa'ya verdi.",
              "Maşa, Koca Ayı'ya seslendi.", "Maşa kirpiye seslendi.", '"Merhaba," dedi Daşa.']),
    "pepee": (["Kız kardeşi Şila geldi.", "Şila, Pepee'nin kardeşiydi.", "Ablası Bebee güldü.",
               "Şuşu bir soru sordu."],
              ["Kuzeni Şila geldi.", "Kız kardeşi Bebee güldü.", "Şila'nın elinde top vardı."]),
    "keloglan": (["Bilgecan Dede bir iksir yaptı.", '"Hadi," dedi eşek.', "Karakaçan ona dönüp sordu.",
                  "Keloğlan'ın babası geldi.", "Balkız'a aşık oldu."],
                 ["Karakaçan yükü taşıdı.", "Bilgecan Dede bir kitap okudu.", "Keloğlan eşeğine seslendi.",
                  "Keloğlan eşeği çağırdı."]),
    "doru": (["Babası Kırat geldi.", "Kırat, Doru'nun dedesiydi.", "Doru'nun babası koştu."],
             ["Kırat, sürünün en yaşlısıydı.", "Annesi Doru'ya baktı.", "Kırat başını salladı."]),
    "hayri": (["Hayri'nin kardeşi Akın geldi.", "Hayri'nin sevimli köpeği havladı.", '"Hav," dedi Yumak.',
               "Yumak ona bakıp sordu."],
              ["Basri Amca'nın köpeği Yumak havladı.", "Hayri Yumak'a seslendi.", "Hayri köpeğe baktı.",
               "Mert, Akın'ın ağabeyiydi."]),
    "sakir": (["Canan da bir aslandı.", "Remzi bir kediydi.", "Şakir'in amcası Necati geldi."],
              ["Canan kitabını okudu.", "Remzi ve Necati oyun oynadı.", "Şakir'in babası Remzi güldü."]),
    "elsa": (['"Merhaba," dedi Sven.', "Sven başını kaldırıp sordu.", "Elsa'nın ablası Anna geldi.",
              "Anna'nın küçük kız kardeşi Elsa güldü.", "Olaf güneşte yavaşça eridi."],
             ["Sven kızağı çekti.", "Elsa'nın küçük kız kardeşi Anna güldü.", "Kar yavaşça eridi.",
              "Kristoff Sven'e seslendi."]),
    "chase": (['"Chase görevde!" diye bağırdı.', "Ryder adlı köpek geldi.", "İtfaiyeci Chase koştu.",
               "Polis köpeği Marshall geldi."],
              ["Chase burnuyla kokladı.", "Ryder köpeklere seslendi.", "Pilot Skye uçtu.",
               "İtfaiyeci Marshall geldi.", "Polis köpeği Chase geldi."]),
    "orumcek_adam": (["Örümcek Adam tehlikeyi sezdi.", "Spin dolaba hızla tırmandı.", "Hulk yumruğunu kaldırdı.",
                      "Masaya tırmandı.", "Takım gizli üsse koştu.", "Spin gizli üste bekledi."],
                     ["Örümcek Adam duvara tırmandı.", "Örümcek hissi bir sorun olduğunu haber verdi.",
                      "Hulk ağacı dikti.", "Kutuyu rafın üstüne koydu.", "Takım gizli eve koştu."]),
    "tosbi": (["Tosbi hızla koştu.", "Tosbi ormana doğru koştu."], ["Tosbi yavaşça yürüdü.", "Tavşan hızla koştu."]),
    "tekir": (["Fareyi hızla kovaladı.", "Kuşu yakaladı."], ["Tekir topu yakaladı.", "Kuş ağaca kondu."]),
    "pamuk": ([], ["Pamuk havucu yedi."]),
    "karabas": (["Sincabı hızla kovaladı."], ["Karabaş topu yakaladı.", "Karabaş kuşa baktı."]),
}


def kart_sha1(kart):
    return hashlib.sha1(json.dumps(kart, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
                        ).hexdigest()


def kart_kontrol(kart_yolu, urun_yolu, kilit=None):
    """(hatalar, uyarilar, sayaç). kilit: {kimlik: {"sha1": ...}} ya da None. Şema, kaynak, ürün listesiyle yer ve
    yan eşleşmesi, kaynaklarla tutarlılık (dizi olguları ürün listesine değil kaynağa dayanır), kural düzenli
    ifadeleri ve öz-sınaması, kart metninin D denetimi (şapka, deyim, ünlem/slogan, kendine adıyla gönderme)."""
    hatalar, uyarilar = [], []
    sayac = collections.Counter()
    hata, uyari = hatalar.append, uyarilar.append
    with open(kart_yolu, encoding="utf-8") as f:
        veri = json.load(f)
    with open(urun_yolu, encoding="utf-8") as f:
        urun = json.load(f)
    kaynaklar = veri.get("kaynaklar", {})
    for a in ("surum", "kaynaklar", "kartlar"):
        if a not in veri:
            hata(f"üst düzey '{a}' yok")
    for kid, k in kaynaklar.items():
        if k.get("tur") not in KAYNAK_TURLERI:
            hata(f"kaynak {kid}: tür {k.get('tur')!r} geçersiz")
        if not k.get("baslik"):
            hata(f"kaynak {kid}: başlık yok")
        if not (k.get("url") or k.get("dosya")):
            hata(f"kaynak {kid}: url ya da dosya yok")
        if k.get("dosya") and not os.path.exists(os.path.join(ROOT, k["dosya"])):
            hata(f"kaynak {kid}: dosya yok: {k['dosya']}")
        if k.get("url") and not k["url"].startswith("https://"):
            hata(f"kaynak {kid}: url https değil")
        if not k.get("erisim"):
            hata(f"kaynak {kid}: erişim tarihi yok")
    kullanilan = set()

    def kaynak_denetle(yer, d, dizi_olgusu=False):
        ks = d.get("kaynak") if isinstance(d, dict) else None
        if not isinstance(ks, list) or not ks:
            hata(f"{yer}: kaynak yok")
            return
        for k in ks:
            if k not in kaynaklar:
                hata(f"{yer}: bilinmeyen kaynak {k!r}")
            kullanilan.add(k)
        sayac["olgu"] += 1
        if dizi_olgusu and all(kaynaklar.get(k, {}).get("tur") == "urun" for k in ks):
            hata(f"{yer}: dizi olgusu yalnız ürün listesine dayanıyor (kaynak gerekir)")
        if d.get("onay_bekliyor"):
            sayac["onay_bekliyor"] += 1
            if not (d.get("not") or d.get("not_")):
                hata(f"{yer}: onay_bekliyor ama not yok")

    def olgu(yer, d, tip=None, dizi_olgusu=False):
        if not isinstance(d, dict) or "deger" not in d:
            hata(f"{yer}: olgu değil ({d!r:.60})")
            return
        if tip and not isinstance(d["deger"], tip):
            hata(f"{yer}: değer türü {type(d['deger']).__name__}, beklenen {tip.__name__}")
        kaynak_denetle(yer, d, dizi_olgusu)

    def metinler(k):
        out = []

        def gez(x, yol):
            if isinstance(x, dict):
                for a, b in x.items():
                    if yol.endswith("urun_yan_eslesmesi[]") and a == "urun":
                        continue
                    gez(b, f"{yol}.{a}")
            elif isinstance(x, list):
                for b in x:
                    gez(b, f"{yol}[]")
            elif isinstance(x, str):
                out.append((yol, x))
        gez(k, k.get("kimlik", "?"))
        return out

    urun_fig = {f["ad"]: ("populer", f) for f in urun["populer"]}
    urun_fig.update({f["ad"]: ("temel", f) for f in urun["temel"]})
    kartlar = veri.get("kartlar", [])
    adlar = [_olgu(k.get("ad")) for k in kartlar]
    if set(adlar) != set(urun_fig) or len(adlar) != len(urun_fig):
        hata(f"figür kümesi ürün listesiyle aynı değil: eksik {sorted(set(urun_fig) - set(adlar))}, "
             f"fazla {sorted(set(adlar) - set(urun_fig))}")
    if len({k.get("kimlik") for k in kartlar}) != len(kartlar):
        hata("kart kimlikleri tekil değil")
    tum_yan_adlari = {}
    for k in kartlar:
        kim = k.get("kimlik", "?")
        for g in KART_ALANLARI:
            if g not in k:
                hata(f"{kim}: {g!r} alanı yok")
        if k.get("kimlik") != _figur_kimligi(_olgu(k.get("ad")) or ""):
            hata(f"{kim}: kimlik figür adından türetilen biçim değil ({_figur_kimligi(_olgu(k.get('ad')) or '')})")
        if not isinstance(k.get("onayli"), bool):
            hata(f"{kim}: onayli true/false olmalı")
        for alan in ("ad", "okunus", "seri", "guvenli_ozellik_kullanimi"):
            olgu(f"{kim}.{alan}", k.get(alan), str)
        olgu(f"{kim}.kimlik_cumlesi", k.get("kimlik_cumlesi"), str, dizi_olgusu=k.get("grup") == "populer")
        olgu(f"{kim}.tur", k.get("tur"), str, dizi_olgusu=k.get("grup") == "populer")
        if not (k.get("tur") or {}).get("lemmalar"):
            hata(f"{kim}.tur: lemmalar yok")
        ad = _olgu(k.get("ad"))
        grup, uf = urun_fig.get(ad, (None, None))
        if grup and k.get("grup") != grup:
            hata(f"{kim}: grup {k.get('grup')} (ürün listesinde {grup})")
        kc = _olgu(k.get("kimlik_cumlesi")) or ""
        if len(re.findall(r"[.!?]", kc)) != 1:
            hata(f"{kim}: kimlik cümlesi tek cümle değil")
        oz = k.get("ozellikler", [])
        if not 2 <= len(oz) <= 3:
            hata(f"{kim}: özellik sayısı {len(oz)} (2-3)")
        for i, o in enumerate(oz):
            olgu(f"{kim}.ozellikler[{i}]", o, str, dizi_olgusu=k.get("grup") == "populer")
            if not o.get("anahtar_kok"):
                hata(f"{kim}.ozellikler[{i}]: anahtar kök yok")
            try:
                rx = re.compile(o.get("anahtar_ifade", ""))
            except re.error as e:
                hata(f"{kim}.ozellikler[{i}]: anahtar_ifade derlenmiyor: {e}")
                continue
            if not o.get("anahtar_ifade"):
                hata(f"{kim}.ozellikler[{i}]: anahtar_ifade yok")
            if not o.get("ornek_bicimler"):
                hata(f"{kim}.ozellikler[{i}]: örnek biçim yok")
            for b in o.get("ornek_bicimler", []):
                if not rx.search(b):
                    hata(f"{kim}.ozellikler[{i}]: anahtar_ifade örneği yakalamıyor: {b}")
            for s in SAHTE_DOST:
                if s.startswith(o.get("anahtar_kok") or "\0") or s in o.get("ornek_bicimler", []):
                    continue
                if rx.search(" " + s + " "):
                    hata(f"{kim}.ozellikler[{i}]: anahtar_ifade sık kelimeyi yakalıyor: {s}")
        yerler = k.get("yerler", [])
        etiketler = [y.get("etiket") for y in yerler]
        if uf and etiketler != uf["yerler"]:
            hata(f"{kim}: yerler {etiketler} != ürün listesi {uf['yerler']} (firmware yer listesi)")
        for y in yerler:
            yy = f"{kim}.yerler[{y.get('etiket')}]"
            if not y.get("tarif"):
                hata(f"{yy}: tarif yok")
            if y.get("dizide_karsiligi") not in YER_KARSILIK:
                hata(f"{yy}: dizide_karsiligi {y.get('dizide_karsiligi')!r} geçersiz")
            if y.get("dizide_karsiligi") in ("kismen", "dogrulanmadi", "yok") and not y.get("not"):
                hata(f"{yy}: doğrulanmamış yerin notu yok")
            kaynak_denetle(yy, y)
            for kt in y.get("kosullu_tarifler", []):
                kaynak_denetle(f"{yy}.kosullu", kt)
        yanlar = k.get("yanlar", [])
        yan_kimlikleri = [y.get("yan_kimlik") for y in yanlar]
        if len(set(yan_kimlikleri)) != len(yan_kimlikleri):
            hata(f"{kim}: yan kimlikleri tekil değil")
        if len({y.get("kisa_ad") for y in yanlar}) != len(yanlar):
            hata(f"{kim}: yan kısa adları tekil değil")
        yan_buyuk = set()
        for y in yanlar:
            yy = f"{kim}.{y.get('yan_kimlik')}"
            if not str(y.get("yan_kimlik", "")).startswith("yan:"):
                hata(f"{yy}: yan_kimlik 'yan:' ile başlamıyor")
            if y.get("tip") not in YAN_TIP:
                hata(f"{yy}: tip {y.get('tip')!r} geçersiz")
            yb = y.get("yuzey_bicimleri", [])
            if not yb:
                hata(f"{yy}: yüzey biçimi yok")
            if y.get("kisa_ad") not in yb:
                hata(f"{yy}: kısa ad yüzey biçimlerinde yok")
            if y.get("resmi_ad") and y["resmi_ad"] not in yb:
                hata(f"{yy}: resmi ad yüzey biçimlerinde yok")
            if "," in (y.get("kisa_ad") or "") or "|" in (y.get("kisa_ad") or ""):
                hata(f"{yy}: kısa ad ',' ya da '|' içeremez (başlık biçimi)")
            dizi = k.get("grup") == "populer"
            olgu(f"{yy}.iliski", y.get("iliski"), str, dizi)
            olgu(f"{yy}.tur", y.get("tur"), str, dizi)
            olgu(f"{yy}.konusur", y.get("konusur"), bool, dizi)
            if "huy" in y:
                olgu(f"{yy}.huy", y["huy"], str, dizi)
            for b in yb:
                if b[:1].isupper():
                    yan_buyuk.add(b)
                    tum_yan_adlari.setdefault(b, set()).add(kim)
        tipler = [y.get("tip") for y in yanlar]
        if k.get("grup") == "temel" and any(t != "isimsiz" for t in tipler):
            hata(f"{kim}: temel figürün yanları isimsiz olmalı")
        if k.get("grup") == "populer" and not any(t in ("adli", "rol") for t in tipler):
            hata(f"{kim}: popüler figürde adlı yan yok")
        esl = k.get("urun_yan_eslesmesi", [])
        if uf and [e.get("urun") for e in esl] != uf["yan"]:
            hata(f"{kim}: ürün yan eşleşmesi ürün listesiyle aynı değil")
        kapsanan = set()
        for e in esl:
            for yk in e.get("kart", []):
                if yk not in yan_kimlikleri:
                    hata(f"{kim}: eşleşmedeki {yk} kartta yok")
                kapsanan.add(yk)
        for yk in yan_kimlikleri:
            if yk not in kapsanan:
                uyari(f"{kim}: {yk} ürün listesinde karşılığı olmayan yan")
        kurallar = k.get("dunya_kurallari", [])
        if len(kurallar) > 5:
            hata(f"{kim}: {len(kurallar)} dünya kuralı (en çok 5)")
        rxler = []
        for i, r in enumerate(kurallar):
            if not r.get("kural"):
                hata(f"{kim}.kural[{i}]: metin yok")
            kaynak_denetle(f"{kim}.kural[{i}]", r)
            for p in r.get("yasak_duzenli_ifadeler", []):
                try:
                    rxler.append(re.compile(p))
                    sayac["regex"] += 1
                except re.error as e:
                    hata(f"{kim}.kural[{i}]: düzenli ifade derlenmiyor: {p} ({e})")
        poz, neg = k.get("kural_ornekleri") or KURAL_ORNEKLERI.get(kim, ([], []))
        if rxler and not poz:
            uyari(f"{kim}: kural düzenli ifadeleri için örnek cümle yok")
        for c in poz:
            if any(r.search(c) for r in rxler):
                sayac["ornek_yakalandi"] += 1
            else:
                hata(f"{kim}: ihlal örneği yakalanmadı: {c}")
        for c in neg:
            es = [r.pattern for r in rxler if r.search(c)]
            if es:
                hata(f"{kim}: temiz cümle yanlışlıkla yakalandı: {c} <- {es[0]}")
            else:
                sayac["ornek_temiz"] += 1
        olumlu = [("kimlik_cumlesi", kc)] + [(f"ozellik{i}", o.get("deger", "")) for i, o in enumerate(oz)]
        for alan, metin in olumlu:
            for r in rxler:
                if r.search(metin):
                    hata(f"{kim}.{alan}: kartın kendi metni yasak ifadeye takılıyor: {r.pattern}")
            if ad and metin.count(ad) > 1:
                hata(f"{kim}.{alan}: figür adı cümlede iki kez (kendine gönderme)")
        ys = k.get("yasaklar", {})
        yasak_adlari = set()
        for i, a in enumerate(ys.get("adlar", [])):
            if not a.get("ad"):
                hata(f"{kim}.yasak_ad[{i}]: ad yok")
            kaynak_denetle(f"{kim}.yasak_ad[{a.get('ad')}]", a)
            yasak_adlari.add(a.get("ad"))
            if a.get("ad") == ad or a.get("ad") in yan_buyuk:
                hata(f"{kim}: yasak ad kendi figürü ya da yanı: {a.get('ad')}")
        for i, o in enumerate(ys.get("ogeler", [])):
            olgu(f"{kim}.yasak_oge[{i}]", o, str)
        for yol, metin in metinler(k):
            if ".kaynak" in yol or ".kural_ornekleri" in yol:
                continue
            if re.search("[âîûÂÎÛ]", metin):
                hata(f"{yol}: şapkalı harf: {metin[:60]}")
            dusuk = _tr_kucuk(metin)
            for dy in KART_DEYIMLER:
                if dy in dusuk:
                    hata(f"{yol}: deyim {dy!r}")
            if "!" in metin and ".yasak_duzenli_ifadeler" not in yol and ".anahtar_ifade" not in yol:
                hata(f"{yol}: ünlem (slogan şüphesi): {metin[:60]}")

        def ad_gecer(metin, a):
            return re.search(r"(?<![\w])" + re.escape(a) + r"(?![\w])", metin) is not None
        for yol, metin in ([(f"{kim}.yerler[{y.get('etiket')}].tarif", y.get("tarif", "")) for y in yerler]
                           + [(f"{kim}.ozellik{i}", o.get("deger", "")) for i, o in enumerate(oz)]
                           + [(f"{kim}.kimlik_cumlesi", kc),
                              (f"{kim}.guvenli", _olgu(k.get("guvenli_ozellik_kullanimi")) or "")]):
            for a in yan_buyuk:
                if ad_gecer(metin, a):
                    hata(f"{yol}: yan adı geçiyor ({a}); tohumda o yan yoksa metne sızar")
            for a in yasak_adlari:
                if ad_gecer(metin, a):
                    hata(f"{yol}: yasak ad geçiyor ({a})")
        # yazarın kopyalayacağı metin (yer tarifi, özellik, kimlik, yan ilişkisi) kod kapılarıyla çatışmaz (Adım 1):
        # K7 kalıbı yok (kartın k7_izinli beyaz listesi hariç), kökü ön eğitimde nadir (< 20) kelime yok
        kapi_ = _kapi()
        try:
            k7_izin = [re.compile(x) for x in k.get("k7_izinli", [])]
        except re.error as e:
            hata(f"{kim}.k7_izinli: düzenli ifade derlenmiyor: {e}")
            k7_izin = []
        adlar_k = {_tr_kucuk(w) for a in [ad or ""] + [b for y in yanlar for b in y.get("yuzey_bicimleri", [])]
                   + [a.get("ad", "") for a in ys.get("adlar", [])] + (k.get("tur") or {}).get("lemmalar", [])
                   + list(urun_fig) for w in re.findall(r"[\wçğıöşüÇĞİÖŞÜ]+", a)}
        izinli_k = {_tr_kucuk(x) for x in k.get("izinli_dunya_kokleri", [])}
        sozluk = kapi_.sade_sozluk.yukle()
        yazar_metni = ([(f"{kim}.yerler[{y.get('etiket')}].tarif", y.get("tarif", "")) for y in yerler]
                       + [(f"{kim}.yerler[{y.get('etiket')}].kosullu", kt.get("tarif", ""))
                          for y in yerler for kt in y.get("kosullu_tarifler", [])]
                       + [(f"{kim}.ozellik{i}", o.get("deger", "")) for i, o in enumerate(oz)]
                       + [(f"{kim}.kimlik_cumlesi", kc)]
                       + [(f"{kim}.{y.get('yan_kimlik')}.{a}", _olgu(y.get(a)) or "") for y in yanlar
                          for a in ("iliski", "huy")])
        for yol, metin in yazar_metni:
            for es in kapi_.guvenlik_eslesmeleri(metin):
                bas = _tr_kucuk(metin).find(es[2])
                if not any(m.start() <= bas < m.end() for r in k7_izin for m in r.finditer(_tr_kucuk(metin))):
                    hata(f"{yol}: K7 kalıbı ({es[1]}: {es[2]!r}); yazar kopyalarsa hikâye düşer")
            for w in kapi_.sade_sozluk.kelimeler(metin):
                kok = sozluk.kok(w)
                if w in adlar_k or any(w.startswith(i) or kok.rstrip("-") == i for i in izinli_k):
                    continue
                if sozluk.tf.get(w, 0) < sozluk.esik["nadir"] and sozluk.d["kok"].get(kok, 0) < sozluk.esik["nadir"]:
                    hata(f"{yol}: nadir kelime {w!r} (kök {kok!r}); sade kelimeyle yazılmalı ya da izinli dünya kökü olmalı")
        for y in yanlar:
            if "yerler" in y:
                olgu(f"{kim}.{y.get('yan_kimlik')}.yerler", y["yerler"], list)
                fazla = set(_olgu(y["yerler"]) or []) - set(etiketler)
                if fazla or not _olgu(y["yerler"]):
                    hata(f"{kim}.{y.get('yan_kimlik')}.yerler: kartta olmayan ya da boş yer listesi ({sorted(fazla)})")
        if "tohum_yasak_kategoriler" in k:
            olgu(f"{kim}.tohum_yasak_kategoriler", k["tohum_yasak_kategoriler"], list)
            bilinen = set(json_oku(kapi_.TOHUM_KELIME, {}).get("kategori", {}))
            bilinmeyen = set(_olgu(k["tohum_yasak_kategoriler"]) or []) - bilinen
            if bilinmeyen:
                hata(f"{kim}.tohum_yasak_kategoriler: bilinmeyen kategori {sorted(bilinmeyen)}")
        olumlu_metin = _tr_kucuk(" ".join(m for yol, m in metinler(k)
                                          if any(p in yol for p in (".deger", ".tarif", ".kural"))))
        yumusa = {"k": "ğ", "ç": "c", "p": "b", "t": "d"}
        for kok in k.get("izinli_dunya_kokleri", []):
            bic = {_tr_kucuk(kok)} | ({_tr_kucuk(kok)[:-1] + yumusa[kok[-1]]} if kok[-1:] in yumusa else set())
            if not any(b in olumlu_metin for b in bic):
                hata(f"{kim}: izinli dünya kökü kartın metninde yok: {kok}")
        # onay ve kilit
        s1 = kart_sha1(k)
        if k.get("onayli"):
            sayac["onayli"] += 1
            if kilit is not None:
                kl = kilit.get(kim)
                if kl is None:
                    uyari(f"{kim}: onaylı ama sha1'i kilitlenmemiş (kart-kontrol --kilitle)")
                elif kl.get("sha1") != s1:
                    hata(f"{kim}: onaylı kart kilitten sonra değişti ({kl.get('sha1', '')[:10]} -> {s1[:10]}); "
                         f"bu figürün bütün kabulleri K4 kapısından ve K merceğinden yeniden geçmeli")
        elif kilit and kim in kilit:
            hata(f"{kim}: kilitli kartın onayı kaldırılmış")
    for a, ks in tum_yan_adlari.items():
        if a in set(adlar):
            hata(f"yan adı bir ürün figürüyle aynı: {a} ({sorted(ks)})")
    kullanilmayan = set(kaynaklar) - kullanilan
    if kullanilmayan:
        uyari(f"kullanılmayan kaynaklar: {sorted(kullanilmayan)}")
    sayac["kart"], sayac["kaynak"] = len(kartlar), len(kaynaklar)
    return hatalar, uyarilar, sayac


def cmd_kart_kontrol(a):
    Y = Yollar(a.ad, a.kok)
    kapi = _kapi()
    kart_yolu = a.kart or kapi.KART
    kilit_yolu = Y.v("kart_kilidi.json")
    kilit = json_oku(kilit_yolu, {})
    hatalar, uyarilar, s = kart_kontrol(kart_yolu, a.urun or kapi.FIGUR, kilit)
    print(f"kart: {s['kart']}  kaynak: {s['kaynak']}  kaynaklı olgu: {s['olgu']}  onay bekleyen olgu: "
          f"{s['onay_bekliyor']}  onaylı kart: {s['onayli']}")
    print(f"kural düzenli ifadesi: {s['regex']}  ihlal örneği yakalandı: {s['ornek_yakalandi']}  "
          f"temiz örnek geçti: {s['ornek_temiz']}")
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    print(f"SONUÇ: {len(hatalar)} hata, {len(uyarilar)} uyarı")
    if a.kilitle:
        if hatalar:
            print("kilitlenmedi: önce hatalar giderilmeli")
            return 1
        with open(kart_yolu, encoding="utf-8") as f:
            kartlar = json.load(f)["kartlar"]
        yeni = dict(kilit)
        for k in kartlar:
            if k.get("onayli") and k["kimlik"] not in kilit:
                yeni[k["kimlik"]] = {"sha1": kart_sha1(k), "kart_dosyasi_sha256": sha256_dosya(kart_yolu)}
                print(f"kilitlendi: {k['kimlik']} {yeni[k['kimlik']]['sha1'][:10]}")
        json_yaz(kilit_yolu, yeni)
    return 1 if hatalar else 0


# ---------------------------------------------------------------- tohum (Adım 3; 'Sistem tarafı')

TOHUM_SURUM = "tohum/1"
# Tema kimliği -> (tanım, gerek). gerek: None | 'yan' (en az bir yan) | 'isimsiz' (isimsiz yan: yeni arkadaş,
# tanıdık aile üyesi 'yeni' olamaz) | 'hayvan' (türü canlı listesinde olan bir yan). Tanımlar KILAVUZ_URUN.md.
# Kullanıcı geri bildirimi: hikayeler hep 'hata -> özür -> düzeltme' mantığındaydı; ahlaki çatışma temaları
# (paylaşmak, yardım istemek, özür dilemek, sırayla oynamak) birlikte en çok %28'dir. Sorun çoğunlukla dışarıdan
# gelir (hava, takılan top, merak uyandıran bir ses); figürün kendi hatası yalnız özür temasında olur.
TEMALAR = {
    "merak_kesif": ("merak edip keşfetmek (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)", None),
    "oyun_eglence": ("eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik", None),
    "yardim_etmek": ("figür başkasına yardım eder (hasta ya da yaralı hayvan değil)", "yan"),
    "kutlama_hazirlik": ("aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak", "yan"),
    "doga_gozlem": ("doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef", None),
    "taklit_hayal": ("hayali oyun (kaptan, aşçı, kaşif olmak gibi) ve oyunda küçük bir hedef", None),
    "kaybolan_esya": ("kaybolan eşya", None),
    "yeni_sey_denemek": ("yeni bir şeyi denemek", None),
    "bir_sey_yapmak": ("bir şey yapmak", None),
    "yagmur_kar": ("yağmur ya da kar günü", None),
    "hayvana_yardim": ("sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)", "hayvan"),
    "yeni_arkadas": ("yeni arkadaş (ilk adımı figür atar)", "isimsiz"),
    "beklemek": ("ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)",
                 None),
    "paylasmak": ("paylaşmak", "yan"),
    "yardim_istemek": ("yardım istemek (çözüm, figürün yardım istemesidir)", "yan"),
    "ozur_dilemek": ("özür dilemek (figürün kendi hatası yalnız bu temada olur)", "yan"),
    "sirayla_oynamak": ("sırayla oynamak", "yan"),
}
# Tema ağırlığı (toplam 1); figürde kullanılamayan temanın payı kalanlara oranla dağılır.
TEMA_AGIRLIK = {"merak_kesif": 0.10, "oyun_eglence": 0.10, "yardim_etmek": 0.08, "kutlama_hazirlik": 0.07,
                "doga_gozlem": 0.07, "taklit_hayal": 0.07, "kaybolan_esya": 0.05, "yeni_sey_denemek": 0.05,
                "bir_sey_yapmak": 0.04, "yagmur_kar": 0.03, "hayvana_yardim": 0.03, "yeni_arkadas": 0.02,
                "beklemek": 0.01, "paylasmak": 0.07, "yardim_istemek": 0.07, "ozur_dilemek": 0.07,
                "sirayla_oynamak": 0.07}
AHLAKI_TEMALAR = ("paylasmak", "yardim_istemek", "ozur_dilemek", "sirayla_oynamak")
AHLAKI_TAVAN = 0.30
TEMA_TAVAN = 0.12
YER_AGIRLIK = {1: [1.0], 2: [0.6, 0.4], 3: [0.45, 0.35, 0.20], 4: [0.40, 0.30, 0.20, 0.10],
               5: [0.30, 0.25, 0.20, 0.15, 0.10]}
ACILIS = {"figur_adi": "figürün adıyla başlar ('Tosbi ...')",
          "zaman": "bir zaman ifadesiyle başlar ('Bir sabah ...')",
          "yer": "yerle başlar ('Ormanda ...')",
          "ses_hava": "bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')"}
# Her hikaye sorun çözülmüş ve sıcak bir kapanış cümlesiyle biter; çıplak bir eylem ya da durgun bir resimle
# bitmez (kullanıcı geri bildirimi: 'eylem' ve 'görüntü' kapanışları hikayeyi yarım bırakıyordu).
KAPANIS = {"duygu": (0.35, "figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir"),
           "sonuc": (0.30, "ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu "
                           "devam ettiler')"),
           "replik": (0.20, "son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok"),
           "ders": (0.15, "olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir")}
DIYALOG = {"var": 0.60, "yok": 0.40}
YAN_SAYISI = {0: 0.30, 1: 0.40, 2: 0.30}
PAY_TOLERANS = 0.05


class FigurBilgi:
    """Kart -> tohum üretiminin gördüğü dünya: yerler, özellikler, yanlar (kategori, hayvan mı, konuşur mu, hangi
    yerlerde bulunur) ve tohum kelimesinin dünyaya uyması (kartın 'tohum_yasak_kategoriler' alanı, kelimenin
    gerektirdiği canlılar: tohum kelimesi kartın izin vermediği bir canlı ya da çağ dışı bir eşya getirmez)."""

    def __init__(self, kart, bg):
        self.kart = kart
        self.ad = _olgu(kart["ad"])
        self.fk = kart["kimlik"]
        self.yerler = [y["etiket"] for y in kart["yerler"]]
        self.ozellikler = [o["anahtar_kok"] for o in kart["ozellikler"]]
        self.yanlar = []
        for y in kart["yanlar"]:
            tur = _tr_kucuk(_olgu(y.get("tur")) or "")
            kelimeler = re.findall(r"[a-zçğıöşü]+", tur)
            hayvan = any(w in bg.canli or bg.kok(w) in bg.canli for w in kelimeler)
            self.yanlar.append({"ad": y["kisa_ad"], "kat": "isimsiz" if y["tip"] == "isimsiz" else "adli",
                                "hayvan": hayvan, "konusur": bool(_olgu(y.get("konusur"))),
                                "yerler": _olgu(y.get("yerler")) or list(self.yerler),
                                "turler": set(kelimeler) | {bg.kok(w) for w in kelimeler}})
        self.tur_lemmalari = {_tr_kucuk(t) for t in (kart["tur"].get("lemmalar") or [_olgu(kart["tur"])])}
        self.yasak_kategoriler = set(_olgu(kart.get("tohum_yasak_kategoriler")) or [])
        self.kategori, self.gerektirir = bg.tohum_kategori, bg.canli_gerektirir
        # kartın kendi yazar metninde geçen kelimeler yasak kategoride olsa da gelebilir (Niloya'nın parkında kaydırak)
        metin = " ".join([y.get("tarif", "") for y in kart["yerler"]] + [o.get("deger", "") for o in kart["ozellikler"]]
                         + [_olgu(kart["kimlik_cumlesi"]) or ""] + list(kart.get("izinli_dunya_kokleri", [])))
        self.kart_kelimeleri = {bg.kok(w).rstrip("-") for w in _kapi().sade_sozluk.kelimeler(metin)}
        self.kategoriler = {y["kat"] for y in self.yanlar}
        self.temalar = [t for t, (_, g) in TEMALAR.items() if self._tema_mumkun(g)]
        if not self.yanlar:
            self.yan_hedef = {0: 1.0}
        elif len(self.kategoriler) == 2:
            self.yan_hedef = dict(YAN_SAYISI)
        else:   # '0-1 adlı + 0-1 isimsiz': tek kategorili kartta iki yan olamaz; iki yan payı tek yana geçer
            self.yan_hedef = {0: YAN_SAYISI[0], 1: YAN_SAYISI[1] + YAN_SAYISI[2]}
        self.yer_hedef = dict(zip(self.yerler, YER_AGIRLIK.get(len(self.yerler)) or
                                  [1 / len(self.yerler)] * len(self.yerler)))

    def _tema_mumkun(self, gerek):
        if gerek is None:
            return True
        if gerek == "yan":
            return bool(self.yanlar)
        if gerek == "isimsiz":
            return any(y["kat"] == "isimsiz" for y in self.yanlar)
        return any(y["hayvan"] for y in self.yanlar)

    def hedefler(self):
        return {"yer": self.yer_hedef, "tema": {t: TEMA_AGIRLIK[t] / sum(TEMA_AGIRLIK[x] for x in self.temalar)
                                              for t in self.temalar},
                "yan_sayisi": {str(k): v for k, v in self.yan_hedef.items()}, "diyalog": dict(DIYALOG),
                "acilis": {k: 1 / len(ACILIS) for k in ACILIS}, "kapanis": {k: v[0] for k, v in KAPANIS.items()},
                "ozellik": {o: 1 / len(self.ozellikler) for o in self.ozellikler}}

    def kelime_uygun(self, w, yanlar=()):
        """Tohum kelimesi figürün dünyasına uyuyor mu: yasak kategoride değil (kartın kendi kelimesi hariç) ve
        gerektirdiği canlı (tasma -> köpek) figürün türü ya da tohumdaki bir yanın türü."""
        if self.kategori.get(w) in self.yasak_kategoriler and w.rstrip("-") not in self.kart_kelimeleri:
            return False
        gerek = self.gerektirir.get(w)
        if gerek:
            turler = set(self.tur_lemmalari)
            for y in self.yanlar:
                if y["ad"] in yanlar:
                    turler |= y["turler"]
            return bool(turler & set(gerek))
        return True

    def yan_secenekleri(self, sayi, tema, diyalog, yer=None):
        ys = [y for y in self.yanlar if yer is None or yer in y["yerler"]]
        if sayi == 0:
            adaylar = [()]
        elif sayi == 1:
            adaylar = [(y,) for y in ys]
        else:
            adaylar = [(a, b) for a in ys if a["kat"] == "adli" for b in ys if b["kat"] == "isimsiz"]
        gerek = TEMALAR[tema][1]

        def uygun(c):
            if (gerek or diyalog == "var") and not c:
                return False      # diyalog varsa figür biriyle konuşur (kendi kendine konuşma yok)
            if gerek == "isimsiz" and not any(y["kat"] == "isimsiz" for y in c):
                return False
            if gerek == "hayvan" and not any(y["hayvan"] for y in c):
                return False
            return True
        return [c for c in adaylar if uygun(c)]


def kota(n, agirlik, rng):
    """Largest-remainder ile tam paylı liste (karışık): payı hedefin 1/n içinde tutar."""
    anahtarlar = list(agirlik)
    toplam = sum(agirlik.values())
    ham = [n * agirlik[k] / toplam for k in anahtarlar]
    sayi = [int(math.floor(x)) for x in ham]
    kalan = n - sum(sayi)
    for i in sorted(range(len(ham)), key=lambda i: (-(ham[i] - sayi[i]), i))[:kalan]:
        sayi[i] += 1
    out = [k for k, c in zip(anahtarlar, sayi) for _ in range(c)]
    rng.shuffle(out)
    return out


def _tohum_ihlali(s, fb):
    v = 0
    if s["kapanis"] == "replik" and s["diyalog"] == "yok":
        v += 1
    if not fb.yan_secenekleri(s["yan_sayisi"], s["tema"], s["diyalog"], s["yer"]):
        v += 1
    return v


def _kisitli_ata(slotlar, fb, rng, adim=200_000):
    """Payları koruyan takaslarla (yer, tema, yan sayısı, diyalog, kapanış) kısıtlarını sağlar: replik -> diyalog
    var; tema gereği, diyalog ve yer -> o yerde bulunan uygun yan seçeneği."""
    alanlar = ("yer", "tema", "yan_sayisi", "diyalog", "kapanis")
    ihl = [_tohum_ihlali(s, fb) for s in slotlar]
    n = len(slotlar)
    for _ in range(adim):
        kotu = [i for i, v in enumerate(ihl) if v]
        if not kotu:
            return True
        i = rng.choice(kotu)
        j = rng.randrange(n)
        f = rng.choice(alanlar)
        if i == j or slotlar[i][f] == slotlar[j][f]:
            continue
        once = ihl[i] + ihl[j]
        slotlar[i][f], slotlar[j][f] = slotlar[j][f], slotlar[i][f]
        yi, yj = _tohum_ihlali(slotlar[i], fb), _tohum_ihlali(slotlar[j], fb)
        if yi + yj <= once:
            ihl[i], ihl[j] = yi, yj
        else:
            slotlar[i][f], slotlar[j][f] = slotlar[j][f], slotlar[i][f]
    return not any(ihl)


class _Deste:
    """Kelime destesi: her kelime bir tur kullanılmadan ikinci kez çekilmez (çeşitlilik)."""

    def __init__(self, kelimeler, rng):
        self.k, self.rng, self.d = sorted(kelimeler), rng, []

    def cek(self, uygun=lambda w: True):
        for _ in range(3):
            if not self.d:
                self.d = self.k[:]
                self.rng.shuffle(self.d)
            for i in range(len(self.d) - 1, -1, -1):
                if uygun(self.d[i]):
                    return self.d.pop(i)
            self.d = []
        raise SystemExit("tohum: uygun kelime bulunamadı")


def tohum_kelimeleri(bg):
    """tohum_kelimeleri.json listeleri; canlı, rol ve belirsiz olanlar ile ürün adlarıyla aynı kelimeler (pamuk,
    yumak) yine de ayıklanır (Adım 0c)."""
    yasak = bg.canli | bg.rol | bg.belirsiz | bg.urun_adlari()
    return {t: sorted(w for w in bg.tohum_kelime[t] if w.rstrip("-") not in yasak) for t in ("isim", "fiil", "sifat")}


def tohum_uret(fb, n, tohum, bg, baslangic=1):
    rng = random.Random(f"tohum:{fb.fk}:{tohum}")
    h = fb.hedefler()
    slotlar = [dict(zip(("yer", "tema", "yan_sayisi", "diyalog", "acilis", "kapanis", "ozellik"), x)) for x in zip(
        kota(n, h["yer"], rng), kota(n, h["tema"], rng), kota(n, fb.yan_hedef, rng), kota(n, h["diyalog"], rng),
        kota(n, h["acilis"], rng), kota(n, h["kapanis"], rng), kota(n, h["ozellik"], rng))]
    if not _kisitli_ata(slotlar, fb, rng):
        raise SystemExit(f"tohum: {fb.ad} için kısıtlar paylar korunarak sağlanamadı")
    kullanim = collections.Counter()
    kel = tohum_kelimeleri(bg)
    deste = {t: _Deste(kel[t], rng) for t in kel}
    ucluler, hucreler = set(), set()
    mastar = json_oku(_kapi().TOHUM_KELIME, {}).get("fiil_mastar", {})
    out = []
    for i, s in enumerate(slotlar):
        secenek = fb.yan_secenekleri(s["yan_sayisi"], s["tema"], s["diyalog"], s["yer"])
        en_az = min(sum(kullanim[y["ad"]] for y in c) for c in secenek)
        c = rng.choice([c for c in secenek if sum(kullanim[y["ad"]] for y in c) == en_az])
        for y in c:
            kullanim[y["ad"]] += 1
        sira = [y["ad"] for y in fb.yanlar]
        yan = sorted((y["ad"] for y in c), key=sira.index)     # tohumdaki yan sırası = kart sırası
        uygun = lambda w: fb.kelime_uygun(w, yan)        # noqa: E731
        for _ in range(1000):
            isim = deste["isim"].cek(lambda w: (s["yer"], s["tema"], w) not in hucreler and uygun(w))
            fiil, sifat = deste["fiil"].cek(uygun), deste["sifat"].cek(uygun)
            if (isim, fiil, sifat) not in ucluler:
                break
        else:
            raise SystemExit("tohum: tekrarsız kelime üçlüsü bulunamadı")
        ucluler.add((isim, fiil, sifat))
        hucreler.add((s["yer"], s["tema"], isim))
        out.append({"id": f"{fb.fk}-{baslangic + i:04d}", "figur": fb.ad, "yer": s["yer"], "tema": s["tema"],
                    "yan": yan, "ozellik": s["ozellik"], "isim": isim, "fiil": fiil,
                    "fiil_mastar": mastar.get(fiil, fiil), "sifat": sifat, "diyalog": s["diyalog"],
                    "acilis": s["acilis"], "kapanis": s["kapanis"], "deneme": 1,
                    "uretim": {"tohum": tohum, "surum": TOHUM_SURUM}})
    return out


def tohum_denetle(tohumlar, fb, bg):
    """Adım 3 geçme şartı: paylar hedefin ±5 puanı içinde, tema <= %12, ahlaki çatışma temaları birlikte <= %30,
    (yer, tema, isim) ve kelime üçlüsü tekrarsız, kelimeler tohum_kelimeleri.json'da, yan ve özellik kaynaklı
    kartta, kısıtlar tutarlı."""
    hatalar = []
    n = len(tohumlar)
    if not n:
        return ["tohum yok"], {}
    h = fb.hedefler()
    pay = {}
    for alan, hedef in h.items():
        say = collections.Counter(str(len(t["yan"])) if alan == "yan_sayisi" else t[alan] for t in tohumlar)
        pay[alan] = {}
        for k in set(hedef) | set(say):
            p = say.get(k, 0) / n
            pay[alan][k] = (round(p, 3), round(hedef.get(k, 0.0), 3))
            if abs(p - hedef.get(k, 0.0)) > PAY_TOLERANS + 1e-9:
                hatalar.append(f"{alan}={k}: pay %{100 * p:.1f}, hedef %{100 * hedef.get(k, 0):.1f} (±5 puan)")
            if alan == "tema" and p > TEMA_TAVAN + 1e-9:
                hatalar.append(f"tema {k} %{100 * p:.1f} > %12")
    ahlaki = sum(t["tema"] in AHLAKI_TEMALAR for t in tohumlar) / n
    if ahlaki > AHLAKI_TAVAN + PAY_TOLERANS + 1e-9:
        hatalar.append(f"ahlaki çatışma temaları (paylaşmak, yardım istemek, özür, sırayla) %{100 * ahlaki:.1f} > "
                       f"%{100 * AHLAKI_TAVAN:.0f} (±5 puan)")
    kel = tohum_kelimeleri(bg)
    ucluler, hucreler, idler = collections.Counter(), collections.Counter(), collections.Counter()
    yan_adlari = {y["ad"]: y for y in fb.yanlar}
    for t in tohumlar:
        idler[t["id"]] += 1
        ucluler[(t["isim"], t["fiil"], t["sifat"])] += 1
        hucreler[(t["yer"], t["tema"], t["isim"])] += 1
        if t.get("figur") != fb.ad:
            hatalar.append(f"{t['id']}: figür {t.get('figur')!r}")
        for alan in ("isim", "fiil", "sifat"):
            if t[alan] not in kel[alan]:
                hatalar.append(f"{t['id']}: {alan} {t[alan]!r} tohum_kelimeleri.json listesinde değil")
            elif not fb.kelime_uygun(t[alan], t["yan"]):
                hatalar.append(f"{t['id']}: {alan} {t[alan]!r} figürün dünyasına uymuyor (kategori ya da gerektirdiği canlı)")
        yan_yer = {y["ad"]: y["yerler"] for y in fb.yanlar}
        for y in t["yan"]:
            if y in yan_yer and t["yer"] not in yan_yer[y]:
                hatalar.append(f"{t['id']}: yan {y!r} {t['yer']!r} yerinde bulunmaz ({', '.join(yan_yer[y])})")
        if t["yer"] not in fb.yerler:
            hatalar.append(f"{t['id']}: yer {t['yer']!r} kartta yok")
        if t["ozellik"] not in fb.ozellikler:
            hatalar.append(f"{t['id']}: özellik {t['ozellik']!r} kartta yok")
        if t["tema"] not in fb.temalar:
            hatalar.append(f"{t['id']}: tema {t['tema']!r} bu figürde kullanılamaz")
        for y in t["yan"]:
            if y not in yan_adlari:
                hatalar.append(f"{t['id']}: yan {y!r} kartta yok")
        kats = [yan_adlari[y]["kat"] for y in t["yan"] if y in yan_adlari]
        if len(kats) != len(set(kats)):
            hatalar.append(f"{t['id']}: en çok 1 adlı + 1 isimsiz yan ({t['yan']})")
        if t["kapanis"] == "replik" and t["diyalog"] == "yok":
            hatalar.append(f"{t['id']}: replik kapanışı diyalogsuz")
        if t["tema"] in TEMALAR and t["yan"] and t["tema"] in fb.temalar:
            c = {y for y in t["yan"] if y in yan_adlari}
            if c not in [{y["ad"] for y in x} for x in fb.yan_secenekleri(len(c), t["tema"], t["diyalog"], t["yer"])]:
                hatalar.append(f"{t['id']}: yanlar tema/diyalog gereğini karşılamıyor")
        elif not t["yan"] and (t["diyalog"] == "var" or TEMALAR.get(t["tema"], ("", None))[1]):
            hatalar.append(f"{t['id']}: yansız tohumda diyalog ya da yan isteyen tema")
    hatalar += [f"tohum kimliği tekrarlanıyor: {k}" for k, v in idler.items() if v > 1]
    hatalar += [f"kelime üçlüsü tekrarlanıyor: {k}" for k, v in ucluler.items() if v > 1]
    hatalar += [f"(yer, tema, isim) tekrarlanıyor: {k}" for k, v in hucreler.items() if v > 1]
    return hatalar, pay


def _bg(zemberek=True):
    return _kapi().Baglam(zemberek=zemberek)


def _figur_bul(bg, ad):
    for k in bg.kart_dosyasi["kartlar"]:
        if ad in (_olgu(k["ad"]), k["kimlik"]) or _figur_kimligi(ad) == k["kimlik"]:
            return k
    raise SystemExit(f"figür bulunamadı: {ad!r} (14 ürün figüründen biri)")


def cmd_tohum(a):
    Y = Yollar(a.ad, a.kok)
    bg = _bg(zemberek=False)
    figurler = [k for k in bg.kart_dosyasi["kartlar"]] if a.figur == "hepsi" else [_figur_bul(bg, a.figur)]
    kod = 0
    for kart in figurler:
        fb = FigurBilgi(kart, bg)
        yol = a.cikti if a.cikti and len(figurler) == 1 else Y.tohum(fb.fk)
        if a.denetle:
            tohumlar = jsonl_oku(yol)
        else:
            if os.path.exists(yol) and not a.ustune_yaz:
                raise SystemExit(f"{yol} var; üstüne yazmak için --ustune-yaz (tohum kimlikleri değişir)")
            tohumlar = tohum_uret(fb, a.n, a.tohum, bg)
            jsonl_yaz(yol, tohumlar)
        hatalar, pay = tohum_denetle(tohumlar, fb, bg)
        print(f"{fb.ad}: {len(tohumlar)} tohum -> {Y.goreli(yol)}; tema {len(fb.temalar)}/{len(TEMALAR)}, yan sayısı hedefi "
              f"{ {k: v for k, v in fb.yan_hedef.items()} }; {'GEÇTİ' if not hatalar else f'{len(hatalar)} HATA'}")
        if a.ayrinti:
            for alan, d in pay.items():
                print(f"   {alan}: " + ", ".join(f"{k} %{100 * p:.0f}/{100 * h:.0f}" for k, (p, h) in sorted(d.items())))
        for h in hatalar[:20]:
            print("   HATA:", h)
        kod |= bool(hatalar)
    return kod


# ---------------------------------------------------------------- kontrol ve kapi (Adım 4-5)

def tum_tohumlar(Y):
    """{tohum id: kayıt}: data/<ad>/tohum/*.jsonl."""
    t = {}
    for yol in sorted(glob.glob(Y.v("tohum", "*.jsonl"))):
        for k in jsonl_oku(yol):
            t[k["id"]] = k
    return t


def _kabul_havuzu(Y, figur, tohum=None):
    """K9 havuzu: aynı figürün kabulleri [(kimlik, gövde)]. Aynı tohumun kabulü hariç: kapı yeniden koşulunca
    (ör. yeni kapı sürümü) kabul edilmiş hikâye kendisinin 'kopyası' sayılıp düşmesin."""
    return [(k["kimlik"], k["kayit"]["govde"]) for k in jsonl_oku(Y.v("kabul.jsonl"))
            if k["figur"] == figur and (tohum is None or k.get("tohum") != tohum)]


def _tur_havuzu(onceki, figur, tohum):
    """K9 havuzunun tur parçası: aynı turda (bu kapı/kontrol koşusunda) daha önce denetlenip kod kapılarından geçmiş
    adaylar [(kimlik, gövde)]; aynı tohumun adayı hariç. Hakemden önce iki yakın kopyanın birlikte kabul edilmesini
    önler: turdaki ilk aday kalır, sonraki K9'a takılır. onceki: [(figür, tohum, kimlik, gövde, geçti)]."""
    return [(k, g) for f, t, k, g, gecti in onceki if gecti and f == figur and t != tohum]


def _kontrol_durumu_yolu(Y, dosya):
    return Y.v("kontrol", os.path.basename(dosya) + ".json")


def _ham_sha1(ham):
    return hashlib.sha1(ham.strip().encode("utf-8")).hexdigest()


def _istem_denemeleri(Y, dosya):
    """Yazar dosyasına atanmış tohumların deneme numaraları (yaz-istemi kaydı): {tohum id: deneme}."""
    ist = json_oku(Y.v("istem", os.path.basename(dosya)[:-4] + ".json"), {})
    return {t["id"]: t.get("deneme", 1) for t in ist.get("tohumlar", [])}


def _yama_bilgisi(surumler, ham):
    """(yama sayısı, fark): kontrol durumundaki sürümler + şimdiki metin. Her farklı metin bir yamadır."""
    hs = _ham_sha1(ham)
    zincir = [s["ham_sha1"] for s in surumler]
    if not zincir or zincir[-1] != hs:
        zincir.append(hs)
    yama = len(zincir) - 1
    fark = None
    if yama:
        ilk = surumler[0]["ham"] if surumler else ham
        fark = "".join(difflib.unified_diff(ilk.splitlines(True), (ham + "\n").splitlines(True),
                                            "once", "sonra", n=0))
    return yama, fark


def _sonuc_yaz(r, b, ek=""):
    print(f"{r['kimlik']}  {'GEÇTİ' if r['gecti'] else 'RET'}  (satır {b['satir']}, tohum {b['tohum']}){ek}")
    for x in r["ihlaller"]:
        print(f"   {x['kod']}: {x['aciklama']}")
    for x in r["notlar"]:
        print(f"   not {x['kod']} [{x['mercek']}]: {x['aciklama']}")


def _yama_ihlali(r, yama):
    if yama > 1:
        r["ihlaller"].append({"kod": "K1.yama_siniri", "kapi": "K1",
                              "aciklama": f"{yama} yama (en çok 1); hikâye boş bırakılmalı, tohum kuyruğa döner"})
        r["gecti"] = False


def cmd_kontrol(a):
    """Yazarın öz-denetimi. Her çağrıda hikâyenin metni kontrol durumuna yazılır; ilk kontrolden sonra değişen metin
    yamadır (en çok 1). Kapı kararı değişmez; kalıcı kayıt 'kapi' komutundadır."""
    Y = Yollar(a.ad, a.kok)
    kapi, uk = _kapi(), _uk()
    bg = kapi.Baglam()
    tohumlar = tum_tohumlar(Y)
    if a.tohum:
        tohumlar.update(kapi.tohum_oku(a.tohum))
    with open(a.dosya, encoding="utf-8") as f:
        bloklar = uk.ayristir(f.read())
    durum_yolu = _kontrol_durumu_yolu(Y, a.dosya)
    durum = json_oku(durum_yolu, {})
    gecen, gorulen = 0, collections.Counter(b["tohum"] for b in bloklar)
    onceki = []
    for b in bloklar:
        havuz = _kabul_havuzu(Y, b["figur"], b["tohum"]) + _tur_havuzu(onceki, b["figur"], b["tohum"])
        r = kapi.denetle(b, tohumlar.get(b["tohum"]), bg, havuz, a.taslak_kart)
        onceki.append((b["figur"], b["tohum"], r["kimlik"], uk.kayit(b)["govde"], r["gecti"]))
        anahtar = b["tohum"] or f"satir{b['satir']}"
        if gorulen[b["tohum"]] > 1:
            r["ihlaller"].append({"kod": "K1.tohum_tekrar", "kapi": "K1",
                                  "aciklama": f"@tohum {b['tohum']} dosyada {gorulen[b['tohum']]} kez"})
            r["gecti"] = False
        surumler = durum.setdefault(anahtar, [])
        yama, _ = _yama_bilgisi(surumler, b["ham"])
        _yama_ihlali(r, yama)
        if not surumler or surumler[-1]["ham_sha1"] != _ham_sha1(b["ham"]):
            surumler.append({"ham_sha1": _ham_sha1(b["ham"]), "sha1": r["sha1"], "gecti": r["gecti"],
                             "kodlar": sorted({x["kod"] for x in r["ihlaller"]}), "ham": b["ham"]})
        gecen += r["gecti"]
        if a.json:
            print(json.dumps({**r, "yama": yama}, ensure_ascii=False))
        else:
            hak = "yama hakkı kalmadı" if yama >= 1 else "1 yama hakkı var"
            _sonuc_yaz(r, b, "" if r["gecti"] else f"  [{hak}]")
    json_yaz(durum_yolu, durum)
    if not a.json:
        print(f"{gecen}/{len(bloklar)} geçti; sürüm {bg.surum_ozeti}")
    return 0 if gecen == len(bloklar) else 1


def cmd_kapi(a):
    """Resmî kapı (Adım 5): figürün bütün aday dosyaları -> data/<ad>/aday.jsonl (bileşen sürümleriyle)."""
    Y = Yollar(a.ad, a.kok)
    kapi, uk = _kapi(), _uk()
    bg = kapi.Baglam()
    tohumlar = tum_tohumlar(Y)
    if a.hepsi:
        dosyalar = sorted(glob.glob(Y.v("aday", "*.txt")))
    else:
        fk = _figur_kimligi(_olgu(_figur_bul(bg, a.figur)["ad"]))
        dosyalar = sorted(glob.glob(Y.v("aday", f"{fk}_*.txt")))
    if not dosyalar:
        raise SystemExit(f"aday dosyası yok: {Y.v('aday')}")
    goreli = {os.path.relpath(d, Y.veri) for d in dosyalar}
    eski = [r for r in jsonl_oku(Y.v("aday.jsonl")) if r["dosya"] not in goreli]
    gorulen_sha1 = {r["sha1"] for r in eski}
    gorulen_tohum = {(r["tohum"], r["deneme"]) for r in eski}
    yeni, bilinmeyen = [], set()
    kapi_say, kod_say, tohum_kaynakli = collections.Counter(), collections.Counter(), 0
    TOHUM_KODLARI = {"K1.tohum", "K1.yer", "K1.yan", "K4.ozellik", "K4.tohum_kelime", "K4.degisim"}
    onceki = []                                          # K9: turdaki önceki adaylar da havuzda
    for dosya in dosyalar:
        with open(dosya, encoding="utf-8") as f:
            bloklar = uk.ayristir(f.read())
        denemeler = _istem_denemeleri(Y, dosya)
        durum = json_oku(_kontrol_durumu_yolu(Y, dosya), {})
        for b in bloklar:
            havuz = _kabul_havuzu(Y, b["figur"], b["tohum"]) + _tur_havuzu(onceki, b["figur"], b["tohum"])
            r = kapi.denetle(b, tohumlar.get(b["tohum"]), bg, havuz, a.taslak_kart)
            deneme = denemeler.get(b["tohum"], 1)
            surumler = durum.get(b["tohum"] or f"satir{b['satir']}", [])
            yama, fark = _yama_bilgisi(surumler, b["ham"])
            _yama_ihlali(r, yama)
            if (b["tohum"], deneme) in gorulen_tohum:
                r["ihlaller"].append({"kod": "K1.tohum_tekrar", "kapi": "K1",
                                      "aciklama": f"tohum {b['tohum']} (deneme {deneme}) ikinci kez yazılmış"})
                r["gecti"] = False
            if r["sha1"] in gorulen_sha1:
                r["ihlaller"].append({"kod": "K11.sha1_tekrar", "kapi": "K11", "aciklama": "aynı kanonik kayıt"})
                r["gecti"] = False
            gorulen_tohum.add((b["tohum"], deneme))
            gorulen_sha1.add(r["sha1"])
            onceki.append((b["figur"], b["tohum"], r["kimlik"], uk.kayit(b)["govde"], r["gecti"]))
            kodlar = {x["kod"] for x in r["ihlaller"]}
            for k in kodlar:
                kod_say[k] += 1
            for k in {x["kapi"] for x in r["ihlaller"]}:
                kapi_say[k] += 1
            tohum_kaynakli += bool(kodlar) and kodlar <= TOHUM_KODLARI
            bilinmeyen |= set(r.get("bilinmeyen_kelimeler", []))
            yeni.append({"kimlik": r["kimlik"], "sha1": r["sha1"], "figur": uk.kayit(b)["figur"],
                         "tohum": b["tohum"], "deneme": deneme, "dosya": os.path.relpath(dosya, Y.veri),
                         "satir": b["satir"], "yamali": yama > 0, "yama_sayisi": yama, "fark": fark,
                         "kontrol_edildi": bool(surumler), "degisim": b["degisim"], "gecti": r["gecti"],
                         "ihlaller": r["ihlaller"], "notlar": r["notlar"], "atlanan": r["atlanan"],
                         "rapor": r["rapor"], "taslak_kart": r["taslak_kart"], "surum": r["surum"],
                         "serilestirme": r["serilestirme"], "kayit": uk.kayit(b)})
    jsonl_yaz(Y.v("aday.jsonl"), eski + yeni)
    surum_yolu = Y.v("surum", f"{bg.surum_ozeti}.json")
    if not os.path.exists(surum_yolu):
        json_yaz(surum_yolu, bg.surum)
    if bilinmeyen:
        yol = Y.d("bilinmeyen_kelimeler.txt")
        onceki = set()
        if os.path.exists(yol):
            with open(yol, encoding="utf-8") as f:
                onceki = set(f.read().split())
        _yaz(yol, "\n".join(sorted(onceki | bilinmeyen)) + "\n")
    n, g = len(yeni), sum(r["gecti"] for r in yeni)
    print(f"{len(dosyalar)} dosya, {n} hikâye: {g} geçti (%{100 * g / max(1, n):.0f}); tohum kaynaklı ret "
          f"{tohum_kaynakli}; yamalı {sum(r['yamali'] for r in yeni)}; sürüm {bg.surum_ozeti} -> {Y.goreli(Y.v('aday.jsonl'))}")
    print("kapı başına ret: " + (", ".join(f"{k} {v}" for k, v in sorted(kapi_say.items())) or "-"))
    print("kod başına ret: " + (", ".join(f"{k} {v}" for k, v in kod_say.most_common()) or "-"))
    atl = sorted({x["kod"] for r in yeni for x in r["atlanan"]})
    if atl:
        print(f"atlanan: {', '.join(atl)}")
    return 0


# ---------------------------------------------------------------- alıntı doğrulama (Adım 8 b)

def _alinti_norm(s):
    uk = _uk()
    s = uk.kucuk(uk.normallestir(s or ""))
    return re.sub(r"\s+", " ", s).strip()


def yakin_bul(q, t, k=ALINTI_MESAFE):
    """q'nun t içinde en çok k düzenlemeyle geçtiği yerin bitiş konumu (Sellers); yoksa -1."""
    if not q:
        return -1
    i = t.find(q)
    if i >= 0:
        return i + len(q)
    if len(q) > 400 or len(q) <= k:
        return -1
    n = len(t)
    onceki = [0] * (n + 1)
    for i in range(1, len(q) + 1):
        c = q[i - 1]
        simdi = [i] + [0] * n
        for j in range(1, n + 1):
            simdi[j] = min(onceki[j - 1] + (c != t[j - 1]), onceki[j] + 1, simdi[j - 1] + 1)
        onceki = simdi
    en = min(range(n + 1), key=lambda j: (onceki[j], j))
    return en if onceki[en] <= k else -1


def _cumle_sinirlari(govde):
    uk = _uk()
    sinir, bas = [], 0
    for c in uk.cumleler(govde):
        i = govde.find(c, bas)
        i = bas if i < 0 else i
        sinir.append((i, i + len(c)))
        bas = i + len(c)
    return sinir


def alinti_dogrula(ih, lens, hikaye):
    """Bir 'var' ihlalini metne karşı doğrular. hikaye: parti dosyasındaki kayıt (plan, govde)."""
    alinti, cn, madde = ih.get("alinti"), ih.get("cumle_no"), ih.get("madde")
    govde = hikaye["govde"]
    cs = _uk().cumleler(govde)
    v = {"madde": madde, "alinti": alinti, "cumle_no": cn, "aciklama": ih.get("aciklama"), "dogrulandi": False,
         "uydurma": False, "eksiklik": False, "kisa": False, "bulunan_cumle": None}
    if alinti is None or not str(alinti).strip():
        if madde in EKSIKLIK and lens == "M" and isinstance(cn, int) and 0 <= cn <= len(cs):
            v.update(dogrulandi=True, eksiklik=True, bulunan_cumle=cn)
        else:
            v["uydurma"] = True           # alıntısız 'var' yalnız M1, M5, M9'da kabul edilir
        return v
    q = _alinti_norm(str(alinti)).strip(" \"'.,;:!?…-")
    v["kisa"] = len(q.split()) < 3
    plan = hikaye.get("plan") or {}
    g = _alinti_norm(govde)
    son = yakin_bul(q, g)
    if son < 0:            # gövdede yoksa plan satırı (cümle 0)
        for p in (plan.get("sorun"), plan.get("cozum"), f"{plan.get('sorun')} | {plan.get('cozum')}"):
            if p and yakin_bul(q, _alinti_norm(p)) >= 0:
                v.update(dogrulandi=True, bulunan_cumle=0)
                return v
        v["uydurma"] = True
        return v
    orta = max(0, son - max(1, len(q) // 2))
    sinir = _cumle_sinirlari(govde)          # küçük harfe çevrilmiş metin cümlelere bölünemez (büyük harf ister)
    no = next((i + 1 for i, (a, b) in enumerate(sinir) if a <= orta < b + 1), len(sinir))
    v.update(dogrulandi=True, bulunan_cumle=no)
    return v


# ---------------------------------------------------------------- puan doğrulama ve oylar (Adım 8)

def puan_dogrula(lens, parti, veri):
    """(biçim geçerli mi, nedenler, {konum: kayıt}). 'gecti' maddelerden yeniden hesaplanır."""
    nedenler = []
    ids = [h["id"] for h in parti["hikayeler"]]
    if not isinstance(veri, list):
        return False, ["JSON bir liste değil"], {}
    if len(veri) != len(ids):
        nedenler.append(f"kayıt sayısı {len(veri)}, partide {len(ids)}")
    kayitlar = {}
    maddeler = set(MADDELER[lens])
    for i, r in enumerate(veri):
        if not isinstance(r, dict) or r.get("id") not in ids:
            nedenler.append(f"{i + 1}. kayıt partide olmayan id")
            continue
        konum = ids.index(r["id"])
        if konum != i:
            nedenler.append(f"{r['id']}: parti sırasında değil")
        if konum in kayitlar:
            nedenler.append(f"{r['id']}: iki kez")
        kayitlar[konum] = r
        m = r.get("maddeler")
        if not isinstance(m, dict) or set(m) != maddeler:
            nedenler.append(f"{r['id']}: maddeler eksik ya da fazla")
            m = m if isinstance(m, dict) else {}
        if any(x not in ("yok", "var") for x in m.values()):
            nedenler.append(f"{r['id']}: madde değeri yok/var dışında")
        ih = r.get("ihlaller")
        if not isinstance(ih, list):
            nedenler.append(f"{r['id']}: ihlaller liste değil")
            ih = []
        ih_madde = set()
        for x in ih:
            if not isinstance(x, dict) or x.get("madde") not in maddeler:
                nedenler.append(f"{r['id']}: geçersiz ihlal kaydı")
                continue
            ih_madde.add(x["madde"])
            if not isinstance(x.get("aciklama"), str) or not x["aciklama"].strip():
                nedenler.append(f"{r['id']}: {x['madde']} açıklamasız")
            if "cumle_no" in x and x["cumle_no"] is not None and not isinstance(x["cumle_no"], int):
                nedenler.append(f"{r['id']}: {x['madde']} cumle_no tamsayı değil")
        varlar = {k for k, x in m.items() if x == "var"}
        if varlar - ih_madde:
            nedenler.append(f"{r['id']}: ihlalsiz 'var' ({sorted(varlar - ih_madde)})")
        if ih_madde - varlar:
            nedenler.append(f"{r['id']}: 'yok' maddeye ihlal ({sorted(ih_madde - varlar)})")
        gecti = not varlar and set(m) == maddeler
        if r.get("gecti") is not gecti:
            nedenler.append(f"{r['id']}: gecti={r.get('gecti')!r}, maddelerden {gecti}")
    for k in range(len(ids)):
        if k not in kayitlar:
            nedenler.append(f"{ids[k]}: kayıt yok")
    return not nedenler, nedenler, kayitlar


def _konum_varlari(lens, r, hikaye):
    """Bir kayıttaki bütün 'var' işaretleri (tek yönlü veto: biçimi bozuk kayıttaki işaret de sayılır). 'var'
    işaretli ama ihlalsiz madde, 'yok' maddeye yazılmış ihlal, 'yok'/'var' dışı madde değeri ve maddesiz
    gecti=false da 'var' sayılır (alıntısızsa uydurma)."""
    if not isinstance(r, dict):
        return []
    m = r.get("maddeler") if isinstance(r.get("maddeler"), dict) else {}
    ih = [x for x in (r.get("ihlaller") if isinstance(r.get("ihlaller"), list) else []) if isinstance(x, dict)]
    out = [alinti_dogrula(x, lens, hikaye) for x in ih]
    yazili = {x.get("madde") for x in ih}
    for madde, deger in m.items():
        if deger != "yok" and madde not in yazili:      # 'VAR', 'evet', boş...: tek yönlü veto, işaret kaybolmaz
            out.append(alinti_dogrula({"madde": madde, "alinti": None, "cumle_no": None,
                                       "aciklama": f"(ihlal kaydı yok; değer {deger!r})"}, lens, hikaye))
    if not out and "gecti" in r and r["gecti"] is not True:
        out.append(alinti_dogrula({"madde": "gecti", "alinti": None, "cumle_no": None,
                                   "aciklama": f"(madde işaretsiz; gecti={r['gecti']!r})"}, lens, hikaye))
    return out


def _veto_kayitlari(veri, ids, kayitlar):
    """{konum: [kayıt, ...]}: 'var' aranacak bütün kayıtlar (tek yönlü veto). Biçimi bozuk çıktıda da işaret
    kaybolmaz: tek listeli sözlük sarmalayıcısı açılır; aynı kimliğin bütün kayıtları okunur; partide olmayan
    kimlikli kayıt listedeki sırasıyla eşlenir (o konumun kendi kaydı yoksa)."""
    out = collections.defaultdict(list)
    for k, r in kayitlar.items():
        out[k].append(r)
    if isinstance(veri, dict):
        listeler = [v for v in veri.values() if isinstance(v, list)]
        veri = listeler[0] if len(listeler) == 1 else None
    if not isinstance(veri, list):
        return out
    kimlikli = {ids.index(r["id"]) for r in veri if isinstance(r, dict) and r.get("id") in ids}
    for i, r in enumerate(veri):
        if not isinstance(r, dict):
            continue
        k = ids.index(r["id"]) if r.get("id") in ids else (i if i < len(ids) and i not in kimlikli else None)
        if k is not None and not any(r is x for x in out[k]):
            out[k].append(r)
    return out


def _degisen_kisimda(v, yer):
    """Kanarya varı değiştirilen cümlede mi (silmede komşu cümleler de sayılır)."""
    no = v.get("bulunan_cumle")
    if no is None or no == 0:
        return False
    pay = 1 if yer.get("kanarya_tur") == "cozum_sil" else 0
    return any(abs(no - d) <= pay for d in yer.get("degisen_cumle") or [])


def _gorevler(Y):
    out = {}
    for L in MERCEKLER:
        g = json_oku(Y.hakem(L, "gorev.json"))
        if g:
            out[L] = g
    return out


def oylari_topla(Y):
    """(oylar, parti denemeleri). Her parti için puan_<n>.json ve (yeniden koşu) puan_<n>_t2.json okunur."""
    oylar, partiler = [], []
    for L, gorev in _gorevler(Y).items():
        yerlesim = json_oku(Y.hakem(L, "yerlesim.json"), {})
        for is_ in gorev["isler"]:
            n = is_["parti"]
            parti = json_oku(os.path.join(ROOT, is_["parti_dosyasi"]) if not os.path.isabs(is_["parti_dosyasi"])
                             else is_["parti_dosyasi"])
            yer = yerlesim.get(str(n))
            if parti is None or yer is None:
                continue
            for deneme, cikti in enumerate([is_["cikti"], is_["cikti_yeniden"]], 1):
                yol = cikti if os.path.isabs(cikti) else os.path.join(ROOT, cikti)
                if not os.path.exists(yol):
                    partiler.append({"mercek": L, "parti": n, "deneme": deneme, "hakem": is_["hakem"],
                                     "tur": is_.get("tur"), "durum": "bekliyor"})
                    break
                try:
                    with open(yol, encoding="utf-8") as f:
                        veri = json.load(f)
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    veri, hata = None, f"JSON okunamadı: {e}"
                else:
                    hata = None
                if hata:
                    bicim, nedenler, kayitlar = False, [hata], {}
                else:
                    bicim, nedenler, kayitlar = puan_dogrula(L, parti, veri)
                    if not isinstance(veri, list):
                        kayitlar = {}
                    elif not kayitlar:
                        ids = [h["id"] for h in parti["hikayeler"]]
                        kayitlar = {ids.index(r["id"]): r for r in veri
                                    if isinstance(r, dict) and r.get("id") in ids}
                tum_kayitlar = _veto_kayitlari(veri if not hata else None, [h["id"] for h in parti["hikayeler"]],
                                               kayitlar)
                konum_oylari = []
                kanarya, yakalanan = 0, 0
                for k, h in enumerate(parti["hikayeler"]):
                    y = yer["konumlar"][k]
                    varlar = [v for r in tum_kayitlar.get(k, []) for v in _konum_varlari(L, r, h)]
                    kayit = {"mercek": L, "parti": n, "deneme": deneme, "hakem": is_["hakem"], "tur": is_.get("tur"),
                             "konum": k, "parti_boyu": len(parti["hikayeler"]),
                             "yari": "ilk" if k < len(parti["hikayeler"]) / 2 else "ikinci",
                             "id": y["id"], "sha1": y["sha1"], "rol": y["rol"], "figur": y["figur"],
                             "oy": "var" if varlar else ("eksik" if k not in kayitlar else "yok"), "varlar": varlar}
                    if y["rol"] == "kanarya":
                        kanarya += 1
                        kayit.update(taban_sha1=y["taban_sha1"], kanarya_tur=y["kanarya_tur"])
                        for v in varlar:
                            v["degisen_kisimda"] = _degisen_kisimda(v, y)
                        kayit["yakalandi"] = any(not v["uydurma"] for v in varlar)
                        kayit["taban_var"] = any(not v["uydurma"] and not v["degisen_kisimda"] for v in varlar)
                        yakalanan += kayit["yakalandi"]
                    konum_oylari.append(kayit)
                kacti = kanarya - yakalanan
                if kacti:
                    nedenler = nedenler + [f"{kacti}/{kanarya} kanarya kaçırıldı"]
                gecerli = bicim and not kacti
                for o in konum_oylari:
                    o["gecerli"] = gecerli
                oylar += konum_oylari
                vs = [v for o in konum_oylari for v in o["varlar"]]
                partiler.append({"mercek": L, "parti": n, "deneme": deneme, "hakem": is_["hakem"],
                                 "tur": is_.get("tur"), "durum": "gecerli" if gecerli else "gecersiz",
                                 "bicim": bicim, "nedenler": nedenler, "kanarya": kanarya, "yakalanan": yakalanan,
                                 "var": len(vs), "uydurma": sum(v["uydurma"] for v in vs)})
                if gecerli:
                    break
    return oylar, partiler


def oy_durumu(oylar, partiler):
    """{sha1: {"dusen": [...neden], "yok": {mercek: {hakem}}, "bekleyen": {(mercek, hakem)}}}."""
    d = collections.defaultdict(lambda: {"dusen": [], "yok": collections.defaultdict(set), "bekleyen": set()})
    for o in oylar:
        if o["rol"] in ("hedef", "dolgu"):
            if o["varlar"]:
                d[o["sha1"]]["dusen"].append({"mercek": o["mercek"], "parti": o["parti"], "deneme": o["deneme"],
                                              "kaynak": o["rol"], "varlar": o["varlar"]})
            elif o["oy"] == "yok" and o["gecerli"]:
                d[o["sha1"]]["yok"][o["mercek"]].add(o["hakem"])
        elif o["rol"] == "kanarya" and o.get("taban_var"):
            d[o["taban_sha1"]]["dusen"].append({"mercek": o["mercek"], "parti": o["parti"], "deneme": o["deneme"],
                                                "kaynak": "kanarya_tabani", "kanarya": o["sha1"],
                                                "varlar": [v for v in o["varlar"] if not v["degisen_kisimda"]]})
    return d


def _bekleyen_ciftler(Y, partiler):
    """Sonucu henüz belli olmayan (mercek, parti) -> sha1'ler: puanı yok ya da ilk denemesi geçersiz ve yeniden
    koşusu yok. Bu hikâyeler yeni partiye konmaz."""
    son = {}
    for p in partiler:
        son[(p["mercek"], p["parti"])] = p
    bekleyen = set()
    for (L, n), p in son.items():
        if p["durum"] == "bekliyor" or (p["durum"] == "gecersiz" and p["deneme"] == 1):
            yer = json_oku(Y.hakem(L, "yerlesim.json"), {}).get(str(n), {})
            for k in yer.get("konumlar", []):
                if k["rol"] in ("hedef", "dolgu"):
                    bekleyen.add((L, yer["hakem"], k["sha1"]))
    return bekleyen


# ---------------------------------------------------------------- hazirla --lens (Adım 7)

def aday_kayitlari(Y):
    """{sha1: aday kaydı} (dosyadaki son kayıt geçerli)."""
    return {r["sha1"]: r for r in jsonl_oku(Y.v("aday.jsonl"))}


def altin_ogeleri(Y):
    return (json_oku(Y.d("pilot", "altin_gizli.json"), {}) or {}).get("ogeler", [])


def altin_etiketleri(Y):
    return {r["sha1"]: r for r in jsonl_oku(Y.d("altin", "etiketler.jsonl"))}


def _ozellik_satiri(kart, oz):
    for o in kart["ozellikler"]:
        if o["anahtar_kok"] == oz:
            return {"anahtar_kok": oz, "deger": o["deger"]}
    return {"anahtar_kok": oz, "deger": None}


def gorunum(lens, rec, bg, tohumlar):
    """Hakemin gördüğü hikâye kaydı. Eğitime giren alanlar (başlık, plan, gövde) + merceğin yardımcı girdisi;
    tema, tohum kimliği, deneme ve yazar bilgisi yok."""
    k = rec["kayit"]
    kart = bg.kartlar[k["figur"]]
    t = tohumlar.get(rec.get("tohum")) or {}
    g = {"id": rec["kimlik"], "plan": {"sorun": k["sorun"], "cozum": k["cozum"]}, "govde": k["govde"]}
    if lens in "MK":
        g = {"id": rec["kimlik"], "baslik": {"figur": k["figur"], "yer": k["yer"], "yan": list(k["yan"])},
             **{a: g[a] for a in ("plan", "govde")}}
        oz = _ozellik_satiri(kart, t.get("ozellik"))
        g["ozellik"] = oz["deger"] if lens == "M" else oz
    if lens == "D":
        d = bg.dunya(k["figur"])
        adlar = [d.ad] + [b for y in k["yan"] if y in d.yanlar for b in d.yan_bicimleri(d.yanlar[y])]
        g["adlar"] = list(dict.fromkeys(adlar))
        g["k6_isaretleri"] = [n["aciklama"] for n in rec.get("notlar", []) if "D" in n.get("mercek", "")]
    if lens == "K":
        g["cogul_canli_notlari"] = [n["aciklama"] for n in rec.get("notlar", []) if n["kod"] == "K6.cogul_canli"]
        g["belirsiz_kelime_notlari"] = [n["aciklama"] for n in rec.get("notlar", []) if n["kod"] == "K6.belirsiz"]
    return g


def _hakem_sayilari(pilot, ozel=None):
    h = dict(HAKEM_SAYISI)
    if pilot:
        h["K"] = 2
    if ozel:
        for parca in ozel.split(","):
            L, s = parca.split("=")
            h[L.strip()] = int(s)
    return h


def _tamam(durum, L, H):
    return set(range(1, H[L] + 1)) <= durum["yok"].get(L, set())


def _kanarya_sayisi(rng, dagilim=KANARYA_DAGILIM):
    x, t = rng.random(), 0.0
    for i, p in enumerate(dagilim):
        t += p
        if x < t:
            return i
    return len(dagilim) - 1


def hazirla_urun(Y, lens, parti_boyu=10, tohum=2026, pilot=False, hakem=None, taslak_kart=False,
                 taban_aday=False, yalniz=None, kisa_devre=True, dagilim=KANARYA_DAGILIM, bg=None):
    """Partileri kurar. yalniz: yalnız bu sha1'ler (altın kurul). Dönüş: özet sözlüğü."""
    import bozucu
    if not 1 <= parti_boyu <= 10:
        raise SystemExit("parti boyu 1-10 olmalı (KUSURSUZ_VERI.md: parti <= 10)")
    bg = bg or _kapi().Baglam()
    tohumlar = tum_tohumlar(Y)
    aday = aday_kayitlari(Y)
    oylar, partiler = oylari_topla(Y)
    durum = oy_durumu(oylar, partiler)
    bekleyen = _bekleyen_ciftler(Y, partiler)
    H = _hakem_sayilari(pilot, hakem)
    gorev = json_oku(Y.hakem(lens, "gorev.json")) or {"mercek": lens, "istem": f"degerlendirme/HAKEM_{lens}.md",
                                                       "hakem_sayisi": H[lens], "isler": []}
    gorev["hakem_sayisi"] = max(gorev.get("hakem_sayisi", 0), H[lens])
    yerlesim = json_oku(Y.hakem(lens, "yerlesim.json"), {})
    tur = 1 + max([i.get("tur", 0) for i in gorev["isler"]] or [0])
    n_sonraki = 1 + max([i["parti"] for i in gorev["isler"]] or [0])
    onceki = MERCEKLER[:MERCEKLER.index(lens)]
    adaylar = []
    for s, r in aday.items():
        if not r["gecti"] or (s in durum and durum[s]["dusen"]):
            continue
        if yalniz is not None and s not in yalniz:
            continue
        if kisa_devre and not pilot and yalniz is None and not all(_tamam(durum[s], L, H) for L in onceki):
            continue
        adaylar.append(r)
    # dolgu: altın setteki kusursuz etiketli hikâyeler; kanarya tabanı: kabul + altın (kusursuz ya da etiketsiz)
    etiket = altin_etiketleri(Y)
    altin = [o for o in altin_ogeleri(Y) if o.get("rol") == "hedef" and o["sha1"] in aday]
    dolgu_havuzu = [aday[o["sha1"]] for o in altin if etiket.get(o["sha1"], {}).get("etiket") == "kusursuz"
                    and not durum[o["sha1"]]["dusen"]]
    taban_havuzu = {}
    for k in jsonl_oku(Y.v("kabul.jsonl")):
        taban_havuzu.setdefault(k["figur"], {})[k["sha1"]] = ({**aday.get(k["sha1"], {}), **k}, "kabul")
    for o in altin:
        if etiket.get(o["sha1"], {}).get("etiket", "kusursuz") == "kusursuz":
            r = aday[o["sha1"]]
            taban_havuzu.setdefault(r["figur"], {}).setdefault(r["sha1"], (r, "altin"))
    if taban_aday:     # Pilot-0 (duman testi): kabul ve altın yokken koddan geçmiş adaylar taban olur
        for r in aday.values():
            if r["gecti"]:
                taban_havuzu.setdefault(r["figur"], {}).setdefault(r["sha1"], (r, "aday"))
    kanarya_yolu = Y.hakem(lens, "kanarya.jsonl")
    yeni_kanarya, yeni_isler = [], []
    ozet = collections.Counter()
    for h in range(1, H[lens] + 1):
        rng = random.Random(f"hazirla:{tohum}:{lens}:{tur}:{h}")
        liste = [r for r in adaylar if h not in durum[r["sha1"]]["yok"].get(lens, set())
                 and (lens, h, r["sha1"]) not in bekleyen]
        liste.sort(key=lambda r: r["sha1"])
        rng.shuffle(liste)
        if lens == "K":        # K partileri tek figürlüdür (tek kart)
            gruplar = collections.defaultdict(list)
            for r in liste:
                gruplar[r["figur"]].append(r)
            kumeler = [gruplar[f] for f in sorted(gruplar)]
        else:
            kumeler = [liste]
        for kume in kumeler:
            i = 0
            while i < len(kume):
                c = min(_kanarya_sayisi(rng, dagilim), parti_boyu - 1)
                hedef = kume[i:i + max(1, parti_boyu - c)]
                i += len(hedef)
                icindeki = {r["sha1"] for r in hedef}
                dolgu = []
                bos = parti_boyu - c - len(hedef)
                if bos > 0:
                    uygun = [r for r in dolgu_havuzu if r["sha1"] not in icindeki
                             and (lens != "K" or r["figur"] == hedef[0]["figur"])]
                    dolgu = rng.sample(uygun, min(bos, len(uygun)))
                    ozet["dolgu_eksik"] += bos - len(dolgu)
                icindeki |= {r["sha1"] for r in dolgu}
                konumlar = [(r, "hedef", None) for r in hedef] + [(r, "dolgu", None) for r in dolgu]
                rng.shuffle(konumlar)
                figurler = sorted({r["figur"] for r, _, _ in konumlar})
                for _ in range(c):
                    k = None
                    for _deneme in range(6):
                        fig = rng.choice(figurler)
                        havuz = [x for s, x in sorted(taban_havuzu.get(fig, {}).items()) if s not in icindeki]
                        if not havuz:
                            continue
                        taban, kaynak = rng.choice(havuz)
                        k = bozucu.kanarya(taban["kayit"], tohumlar.get(taban.get("tohum")), lens, bg, rng,
                                           degisim=taban.get("degisim"), taslak_kart=taslak_kart)
                        if k:
                            k["taban_kaynagi"] = kaynak
                            icindeki.add(taban["sha1"])     # iki kanarya aynı tabandan gelmez
                            break
                    if not k:
                        ozet["kanarya_uretilemedi"] += 1
                        continue
                    konumlar.insert(rng.randrange(len(konumlar) + 1), (k, "kanarya", taban))
                if h == 2:
                    konumlar.reverse()          # ikinci hakem farklı bileşimi ters sırayla okur
                n = n_sonraki
                n_sonraki += 1
                parti_yolu = Y.hakem(lens, f"parti_{n}.json")
                cikti, cikti2 = Y.hakem(lens, f"puan_{n}.json"), Y.hakem(lens, f"puan_{n}_t2.json")
                sira = rng.sample(MADDELER[lens], len(MADDELER[lens]))
                hikayeler, yer = [], []
                for r, rol, taban in konumlar:
                    if rol == "kanarya":
                        rec = {"kimlik": r["kimlik"], "kayit": r["kayit"], "tohum": r["tohum"],
                               "notlar": r["kapi"]["notlar"]}
                        yeni_kanarya.append({**r, "mercek": lens, "parti": n})
                        yer.append({"konum": len(yer), "id": r["kimlik"], "sha1": r["sha1"], "rol": rol,
                                    "figur": r["kayit"]["figur"], "taban_sha1": r["taban_sha1"],
                                    "kanarya_tur": r["tur"], "degisen_cumle": r["degisen_cumle"],
                                    "taban_kaynagi": r["taban_kaynagi"]})
                    else:
                        rec = r
                        yer.append({"konum": len(yer), "id": r["kimlik"], "sha1": r["sha1"], "rol": rol,
                                    "figur": r["figur"]})
                    hikayeler.append(gorunum(lens, rec, bg, tohumlar))
                    ozet[rol] += 1
                parti = {"parti": n, "mercek": lens, "istem": f"degerlendirme/HAKEM_{lens}.md",
                         "cikti": Y.goreli(cikti), "madde_sirasi": sira,
                         "talimat": (f"Yalnız {lens} merceğinin istemini ve bu dosyayı oku. Maddelere bu sırayla bak: "
                                     f"{', '.join(sira)} (kimlikler değişmez). Çıktıyı {Y.goreli(cikti)} dosyasına "
                                     f"partideki sırayla yaz.")}
                if lens == "K":
                    kart = {a: b for a, b in bg.kartlar[figurler[0]].items() if a != "acik_noktalar"}
                    parti.update(hedef_yas="3-6", kart=kart)
                parti["hikayeler"] = hikayeler
                json_yaz(parti_yolu, parti)
                yerlesim[str(n)] = {"parti": n, "hakem": h, "tur": tur, "konumlar": yer}
                yeni_isler.append({"parti": n, "hakem": h, "tur": tur, "parti_dosyasi": Y.goreli(parti_yolu),
                                   "cikti": Y.goreli(cikti), "cikti_yeniden": Y.goreli(cikti2),
                                   "istem": f"degerlendirme/HAKEM_{lens}.md", "madde_sirasi": sira,
                                   "boy": len(hikayeler)})
                ozet["parti"] += 1
    gorev["isler"] += yeni_isler
    if yeni_isler:
        json_yaz(Y.hakem(lens, "gorev.json"), gorev)
        json_yaz(Y.hakem(lens, "yerlesim.json"), yerlesim)
        with open(kanarya_yolu, "a", encoding="utf-8") as f:
            for k in yeni_kanarya:
                f.write(json.dumps(k, ensure_ascii=False) + "\n")
    ozet["aday"] = len(adaylar)
    ozet["tur"] = tur
    return dict(ozet), yeni_isler


def cmd_hazirla_urun(a):
    Y = Yollar(a.klasor, a.kok)
    ozet, isler = hazirla_urun(Y, a.lens, a.parti_boyu_urun, a.tohum, a.pilot, a.hakem, a.taslak_kart,
                               a.taban_aday, kisa_devre=not a.kisa_devre_yok)
    print(f"{a.lens} tur {ozet['tur']}: {ozet.get('parti', 0)} parti; hedef {ozet.get('hedef', 0)}, kanarya "
          f"{ozet.get('kanarya', 0)}, dolgu {ozet.get('dolgu', 0)} (dolgu eksiği {ozet.get('dolgu_eksik', 0)}, "
          f"üretilemeyen kanarya {ozet.get('kanarya_uretilemedi', 0)}); aday havuzu {ozet['aday']}")
    if isler:
        print(f"görev: {Y.goreli(Y.hakem(a.lens, 'gorev.json'))} (her parti yeni bir ajana: yalnız istem + parti "
              f"dosyası; yerlesim.json ve kanarya.jsonl hakeme verilmez)")
    return 0


# ---------------------------------------------------------------- oku (Adım 8)

def dur_denetimi(partiler, oylar):
    """Mercek başına son 50 partide kanarya kaçırma > %10 ya da uydurma alıntı > %3 -> mercek durur."""
    out = {}
    for L in MERCEKLER:
        ps = sorted([p for p in partiler if p["mercek"] == L and p["durum"] != "bekliyor"],
                    key=lambda p: (p["parti"], p["deneme"]))[-DUR_PENCERE:]
        if not ps:
            continue
        kan = sum(p["kanarya"] for p in ps)
        kacti = sum(p["kanarya"] - p["yakalanan"] for p in ps)
        var = sum(p["var"] for p in ps)
        uyd = sum(p["uydurma"] for p in ps)
        k_oran = kacti / kan if kan else 0.0
        u_oran = uyd / var if var else 0.0
        out[L] = {"parti": len(ps), "kanarya": kan, "kacirilan": kacti, "kacirma_orani": round(k_oran, 3),
                  "var": var, "uydurma": uyd, "uydurma_orani": round(u_oran, 3),
                  "dur": k_oran > DUR_KACIRMA or u_oran > DUR_UYDURMA}
    return out


def cmd_oku(a):
    Y = Yollar(a.ad, a.kok)
    oylar, partiler = oylari_topla(Y)
    jsonl_yaz(Y.d("hakem", "oylar.jsonl"), oylar)
    dur = dur_denetimi(partiler, oylar)
    yeniden = [p for p in partiler if p["durum"] == "bekliyor" and p["deneme"] == 2]
    json_yaz(Y.d("hakem", "oku_ozet.json"), {"partiler": partiler, "dur": dur})
    for L in MERCEKLER:
        ps = [p for p in partiler if p["mercek"] == L]
        if not ps:
            continue
        say = collections.Counter(p["durum"] for p in ps)
        kan = sum(p.get("kanarya", 0) for p in ps)
        yak = sum(p.get("yakalanan", 0) for p in ps)
        var = sum(p.get("var", 0) for p in ps)
        uyd = sum(p.get("uydurma", 0) for p in ps)
        print(f"{L}: {say['gecerli']} geçerli, {say['gecersiz']} geçersiz, {say['bekliyor']} bekliyor | kanarya "
              f"{yak}/{kan} yakalandı | 'var' {var}, uydurma alıntı {uyd}")
        for p in ps:
            if p["durum"] == "gecersiz":
                print(f"   parti {p['parti']} deneme {p['deneme']} GEÇERSİZ: {'; '.join(p['nedenler'][:4])}")
        if dur.get(L, {}).get("dur"):
            d = dur[L]
            print(f"   DUR: {L} merceği durmalı (son {d['parti']} parti: kanarya kaçırma %{100 * d['kacirma_orani']:.0f}, "
                  f"uydurma %{100 * d['uydurma_orani']:.0f}); istem sorunu olarak kullanıcıya raporla")
    for p in yeniden:
        is_ = next(i for i in json_oku(Y.hakem(p["mercek"], "gorev.json"))["isler"] if i["parti"] == p["parti"])
        print(f"yeniden koşulacak (yeni ajan): {p['mercek']} parti {p['parti']} -> {is_['cikti_yeniden']}")
    print(f"{len(oylar)} oy -> {Y.goreli(Y.d('hakem', 'oylar.jsonl'))}")
    return 2 if any(d["dur"] for d in dur.values()) else 0


# ---------------------------------------------------------------- karar (Adım 8-9, 11'in izin listesi)

def kanarya_sha1leri(Y):
    return {k["sha1"] for L in MERCEKLER for k in jsonl_oku(Y.hakem(L, "kanarya.jsonl"))} | \
        {o["sha1"] for o in altin_ogeleri(Y) if o.get("rol") == "okur_kanarya"}


def _kaynak_sha1(Y, rec):
    """Aday kaydının kaynak dosyada (hakemden sonra değişmemiş) hâli: (sha1 ya da None, neden)."""
    uk = _uk()
    yol = Y.v(rec["dosya"])
    if not os.path.exists(yol):
        return None, "kaynak dosya yok"
    with open(yol, encoding="utf-8") as f:
        for b in uk.ayristir(f.read()):
            if b["tohum"] == rec["tohum"]:
                return uk.sha1(uk.kayit(b)), None
    return None, "kaynak dosyada tohum yok"


def karar_ver(Y, pilot=False, hakem=None, taslak_kart=False, bg=None):
    kapi, uk = _kapi(), _uk()
    bg = bg or kapi.Baglam()
    aday = aday_kayitlari(Y)
    oylar, partiler = oylari_topla(Y)
    durum = oy_durumu(oylar, partiler)
    H = _hakem_sayilari(pilot, hakem)
    for L, g in _gorevler(Y).items():
        H[L] = max(H[L], g.get("hakem_sayisi", 0))
    kanaryalar = kanarya_sha1leri(Y)
    insan = altin_etiketleri(Y)          # altın set: okurun 'kusurlu' dediği hikâye kurul ne derse desin girmez
    kilit = json_oku(Y.v("kart_kilidi.json"), {})
    tohumlar = tum_tohumlar(Y)
    kod_surumu = {os.path.basename(p): sha256_dosya(p) for p in
                  (os.path.abspath(__file__), os.path.join(HERE, "bozucu.py")) if os.path.exists(p)}
    kabul, ret, bekleyen = [], [], collections.Counter()
    for s, r in sorted(aday.items(), key=lambda x: (x[1]["figur"], x[1]["tohum"] or "", x[1]["deneme"])):
        if s in kanaryalar:
            ret.append({"sha1": s, "kimlik": r["kimlik"], "mercek": "kod", "madde": "kanarya", "alinti": None,
                        "aciklama": "kanarya ad alanındaki kayıt eğitim hattına giremez"})
            continue
        if not r["gecti"]:
            for x in r["ihlaller"]:
                ret.append({"sha1": s, "kimlik": r["kimlik"], "figur": r["figur"], "tohum": r["tohum"],
                            "deneme": r["deneme"], "yamali": r["yamali"], "mercek": "kod", "madde": x["kod"],
                            "alinti": None, "aciklama": x["aciklama"], "kaynak": "kapi"})
            continue
        e = insan.get(s, {})
        if e.get("etiket") == "kusurlu":
            ret.append({"sha1": s, "kimlik": r["kimlik"], "figur": r["figur"], "tohum": r["tohum"],
                        "deneme": r["deneme"], "yamali": r["yamali"], "mercek": e.get("mercek") or "insan",
                        "madde": "altin_kusurlu", "alinti": None, "cumle_no": e.get("cumle"),
                        "aciklama": e.get("neden") or e.get("ham"), "kaynak": "altin_etiket"})
            continue
        d = durum.get(s)
        if d and d["dusen"]:
            for dus in d["dusen"]:
                for v in dus["varlar"]:
                    ret.append({"sha1": s, "kimlik": r["kimlik"], "figur": r["figur"], "tohum": r["tohum"],
                                "deneme": r["deneme"], "yamali": r["yamali"], "mercek": dus["mercek"],
                                "madde": v["madde"], "alinti": v["alinti"], "uydurma": v["uydurma"],
                                "aciklama": v["aciklama"], "kaynak": dus["kaynak"], "parti": dus["parti"],
                                **({"kanarya": dus["kanarya"]} if "kanarya" in dus else {})})
            continue
        # kabul şartları
        eksik = [L for L in MERCEKLER if not (d and _tamam(d, L, H))]
        if eksik:
            bekleyen["hakem_eksik_" + "".join(eksik)] += 1
            continue
        if uk.sha1(r["kayit"]) != s:
            bekleyen["sha1_tutmuyor"] += 1
            continue
        kaynak, neden = _kaynak_sha1(Y, r)
        if kaynak != s:
            bekleyen[f"kaynak_degisti ({neden or 'metin hakemden sonra değişmiş'})"] += 1
            continue
        if r["surum"] != bg.surum_ozeti:
            bekleyen["kapi_surumu_eski (kapi yeniden koşulmalı)"] += 1
            continue
        kart = bg.kartlar[r["figur"]]
        if not kart.get("onayli") and not taslak_kart:
            bekleyen["kart_onaysiz"] += 1
            continue
        if kart.get("onayli") and kilit.get(kart["kimlik"], {}).get("sha1") not in (None, kart_sha1(kart)):
            bekleyen["kart_kilitten_sonra_degisti"] += 1
            continue
        kararlar = [{k: o[k] for k in ("mercek", "parti", "deneme", "hakem", "konum", "rol", "oy", "gecerli")}
                    for o in oylar if o["sha1"] == s]
        t = tohumlar.get(r["tohum"], {})
        kabul.append({"sha1": s, "kimlik": r["kimlik"], "figur": r["figur"], "yer": r["kayit"]["yer"],
                      "tohum": r["tohum"], "deneme": r["deneme"], "yamali": r["yamali"], "fark": r["fark"],
                      "degisim": r["degisim"], "tohum_ozellikleri": {k: t.get(k) for k in
                                                                    ("tema", "yan", "diyalog", "acilis", "kapanis",
                                                                     "ozellik")},
                      "kararlar": kararlar, "hakem_sayisi": {L: H[L] for L in MERCEKLER},
                      "taslak_kart": bool(r["taslak_kart"] or not kart.get("onayli")),
                      "kart_sha1": kart_sha1(kart), "serilestirme": r["serilestirme"], "surum_ozeti": r["surum"],
                      "bilesenler": {**bg.surum, "karar_kodu": kod_surumu}, "kayit": r["kayit"]})
    # kuyruk (Adım 9): son denemesi düşen (ya da boş bırakılan) tohum deneme+1 ile döner; iki kez düşen bırakılır
    ret_sha1 = {x["sha1"] for x in ret}
    yazilan = {(r["tohum"], r["deneme"]): r for r in aday.values()}
    kabul_tohum = {k["tohum"] for k in kabul}
    atanan = {}
    for p in sorted(glob.glob(Y.v("istem", "*.json"))):
        ist = json_oku(p)
        for t in ist.get("tohumlar", []):
            d = t.get("deneme", 1)
            if d >= atanan.get(t["id"], (0, None))[0]:
                atanan[t["id"]] = (d, ist.get("dosya"))
    kuyruk, birakilan = [], []
    for tid, (d_son, dosya) in sorted(atanan.items()):
        if tid in kabul_tohum:
            continue
        r = yazilan.get((tid, d_son))
        if r is not None:
            if r["sha1"] not in ret_sha1:
                continue            # sonucu bekleniyor
            neden = "ret"
        elif dosya and os.path.exists(Y.v(dosya)):
            neden = "boş"           # yazar dosyası var ama bu tohumun hikâyesi yok
        else:
            continue                # henüz yazılmadı
        t = tohumlar.get(tid)
        if t is None:
            continue
        if d_son >= 2:
            birakilan.append({**t, "deneme": d_son, "neden": neden,
                              "hucre": [t["yer"], t.get("tema"), t.get("kapanis")]})
        else:
            kuyruk.append({**t, "deneme": d_son + 1, "neden": neden})
    # izin listesi: figür x yer hücresi başına 1 doğrulama (hücrede >= 2 kabul varsa); önceki atama korunur
    onceki = {}
    if os.path.exists(Y.v("izin.txt")):
        with open(Y.v("izin.txt"), encoding="utf-8") as f:
            izin_satirlari = f.read().splitlines()
        for satir in izin_satirlari:
            p = satir.split()
            if len(p) >= 2 and not satir.startswith("#"):
                onceki[p[0]] = p[1]
    hucre = collections.defaultdict(list)
    for k in kabul:
        hucre[(k["figur"], k["yer"])].append(k["sha1"])
    bolme = {}
    for key, ss in hucre.items():
        eski = [x for x in ss if onceki.get(x) == "dogrulama"]
        sec = eski[0] if eski else (min(ss, key=lambda x: hashlib.sha256(f"dogrulama:{x}".encode()).hexdigest())
                                    if len(ss) >= 2 else None)
        for x in ss:
            bolme[x] = "dogrulama" if x == sec else "egitim"
    taslak = any(k["taslak_kart"] for k in kabul)
    satirlar = [f"# {Y.ad} izin listesi: <sha1> egitim|dogrulama. Yalnız prepare_ft2 --yalniz ile kullanılır.",
                f"# kabul {len(kabul)}; sürümler {sorted({k['surum_ozeti'] for k in kabul})}"]
    if taslak:
        satirlar.append("# taslak_kart: evet (onaysız kartla kabul; yalnız duman testi)")
    satirlar += [f"{k['sha1']} {bolme[k['sha1']]}" for k in kabul]
    for k in kabul:
        assert k["sha1"] not in kanaryalar
    return {"kabul": kabul, "ret": ret, "kuyruk": kuyruk, "birakilan": birakilan, "izin": satirlar,
            "bekleyen": bekleyen, "bolme": bolme}


def cmd_karar(a):
    Y = Yollar(a.ad, a.kok)
    uk = _uk()
    s = karar_ver(Y, a.pilot, a.hakem, a.taslak_kart)
    jsonl_yaz(Y.v("kabul.jsonl"), s["kabul"])
    jsonl_yaz(Y.v("ret.jsonl"), s["ret"])
    jsonl_yaz(Y.v("kuyruk.jsonl"), s["kuyruk"])
    jsonl_yaz(Y.v("birakilan.jsonl"), s["birakilan"])
    _yaz(Y.v("izin.txt"), "\n".join(s["izin"]) + "\n")
    # yalnız kabuller: data/<ad>/<figür>.txt (prepare_ft2 --yalniz bunları okur)
    figurler = collections.defaultdict(list)
    for k in s["kabul"]:
        figurler[k["figur"]].append(k)
    bilinen = {k["kimlik"] for k in json_oku(_kapi().KART)["kartlar"]}
    for eski in glob.glob(Y.v("*.txt")):       # yalnız figür dosyaları (izin.txt ve başkaları dokunulmaz)
        ad = os.path.basename(eski)[:-4]
        if ad in bilinen and ad not in {_figur_kimligi(f) for f in figurler}:
            os.remove(eski)
    for f, ks in figurler.items():
        _yaz(Y.v(f"{_figur_kimligi(f)}.txt"), "\n".join(uk.blok_yaz(k["kayit"], k["tohum"], k["degisim"])
                                                        for k in ks))
    n_ret = len({x["sha1"] for x in s["ret"]})
    print(f"kabul {len(s['kabul'])}, ret {n_ret} hikâye ({len(s['ret'])} gerekçe), bekleyen "
          f"{sum(s['bekleyen'].values())}; kuyruk {len(s['kuyruk'])}, bırakılan {len(s['birakilan'])}")
    for k, v in s["bekleyen"].most_common():
        print(f"   bekleyen: {k} {v}")
    uyd = sum(1 for x in s["ret"] if x.get("uydurma"))
    if uyd:
        print(f"   uydurma alıntıyla düşen gerekçe: {uyd}")
    dog = sum(v == "dogrulama" for v in s["bolme"].values())
    print(f"izin: {len(s['kabul'])} ({dog} doğrulama) -> {Y.goreli(Y.v('izin.txt'))}")
    return 0


# ---------------------------------------------------------------- altin (Adım 6: altın set ve kör etiket)

ETIKET_SATIRI = re.compile(r"^Etiket:\s*(.*)$")


def altin_sec(Y, n=150, tohum=2026, okur_orani=0.08, taslak_kart=False, bg=None):
    """Koddan geçmiş yeni yazımlardan figür x yer tabakalı n hikâye + ~%8 habersiz okur kanaryası."""
    import bozucu
    uk = _uk()
    bg = bg or _kapi().Baglam()
    rng = random.Random(f"altin:{tohum}")
    kanaryalar = kanarya_sha1leri(Y)
    aday = [r for r in aday_kayitlari(Y).values() if r["gecti"] and r["sha1"] not in kanaryalar]
    hucre = collections.defaultdict(list)
    for r in sorted(aday, key=lambda r: r["sha1"]):
        hucre[(r["figur"], r["kayit"]["yer"])].append(r)
    for v in hucre.values():
        rng.shuffle(v)
    anahtarlar = sorted(hucre)
    rng.shuffle(anahtarlar)
    secilen, tur = [], 0
    while len(secilen) < n and any(len(hucre[k]) > tur for k in anahtarlar):
        for k in anahtarlar:
            if len(secilen) < n and len(hucre[k]) > tur:
                secilen.append(hucre[k][tur])
        tur += 1
    # geliştirme / ölçüm yarıları hücre içinde dönüşümlü
    yari = {}
    say = collections.Counter()
    ilk = {k: rng.randrange(2) for k in anahtarlar}
    for r in secilen:
        k = (r["figur"], r["kayit"]["yer"])
        yari[r["sha1"]] = ("gelistirme", "olcum")[(say[k] + ilk[k]) % 2]
        say[k] += 1
    ogeler = [{"kimlik": r["kimlik"], "sha1": r["sha1"], "rol": "hedef", "yari": yari[r["sha1"]],
               "figur": r["figur"], "yer": r["kayit"]["yer"], "kayit": r["kayit"]} for r in secilen]
    rng.shuffle(ogeler)
    tohumlar = tum_tohumlar(Y)
    m = int(round(n * okur_orani))
    tabanlar = rng.sample(secilen, min(m * 3, len(secilen)))
    okur = []
    for t in tabanlar:
        if len(okur) >= m:
            break
        k = bozucu.kanarya(t["kayit"], tohumlar.get(t["tohum"]), rng.choice(MERCEKLER), bg, rng,
                           degisim=t.get("degisim"), taslak_kart=taslak_kart)
        if k:
            okur.append({"kimlik": k["kimlik"], "sha1": k["sha1"], "rol": "okur_kanarya", "yari": None,
                         "figur": k["kayit"]["figur"], "yer": k["kayit"]["yer"], "kayit": k["kayit"],
                         "kanarya": {x: k[x] for x in ("lens", "tur", "aciklama", "degisen_cumle", "taban",
                                                       "taban_sha1")}})
    for k in okur:       # tabanından en az 10 sıra uzağa (mümkünse)
        taban_i = next((i for i, o in enumerate(ogeler) if o["sha1"] == k["kanarya"]["taban_sha1"]), None)
        yerler = [i for i in range(len(ogeler) + 1) if taban_i is None or abs(i - taban_i) >= 10] or \
            list(range(len(ogeler) + 1))
        ogeler.insert(rng.choice(yerler), k)
    for i, o in enumerate(ogeler, 1):
        o["sira"] = i
    satir = ["# Altın set: kör etiketleme", "",
             "Her hikâyeyi oku ve 'Etiket:' satırına yaz: `kusursuz` ya da `kusurlu: <cümle no> | <neden> | <M/D/K>`.",
             "Cümle no: gövde cümleleri 1'den, plan satırı 0. Mercek: M mantık, D dil, K dünya-kart ve çocuk "
             "güvenliği. Başka dosya (hakem puanları, altin_gizli.json) açma; kurulu görmeden etiketle.", ""]
    for o in ogeler:
        k = o["kayit"]
        satir += [f"## {o['sira']}", f"Başlık: {k['figur']} | {k['yer']} | {', '.join(k['yan']) or '-'}",
                  f"Plan: {k['sorun']} | {k['cozum']}", "",
                  " ".join(f"({i}) {c}" for i, c in enumerate(uk.cumleler(k["govde"]), 1)), "", "Etiket: ", ""]
    return ogeler, "\n".join(satir) + "\n"


def etiket_ayristir(metin):
    """insan.md -> {sıra: (etiket, cümle, neden, mercek, ham)}; etiket: kusursuz | kusurlu | None."""
    out, sira = {}, None
    for s in metin.splitlines():
        m = re.match(r"^##\s+(\d+)\s*$", s)
        if m:
            sira = int(m.group(1))
            continue
        m = ETIKET_SATIRI.match(s)
        if m and sira is not None:
            ham = m.group(1).strip()
            dus = _tr_kucuk(ham)
            if not ham:
                out[sira] = (None, None, None, None, ham)
            elif dus.startswith("kusursuz"):
                out[sira] = ("kusursuz", None, None, None, ham)
            elif dus.startswith("kusurlu"):
                parca = [p.strip() for p in ham.split(":", 1)[1].split("|")] if ":" in ham else []
                cumle = next((int(x) for x in re.findall(r"\d+", parca[0])), None) if parca else None
                mercek = next((p.upper() for p in reversed(parca) if p.upper() in ("M", "D", "K")), None)
                neden = parca[1] if len(parca) > 1 else (parca[0] if parca else None)
                out[sira] = ("kusurlu", cumle, neden, mercek, ham)
            else:
                out[sira] = ("anlasilmadi", None, None, None, ham)
            sira = None
    return out


def cmd_altin(a):
    Y = Yollar(a.ad, a.kok)
    gizli_yolu, insan_yolu = Y.d("pilot", "altin_gizli.json"), Y.d("pilot", "insan.md")
    if a.eylem == "sec":
        if os.path.exists(gizli_yolu) and not a.ustune_yaz:
            raise SystemExit(f"{gizli_yolu} var (etiketler ona bağlı); yeniden seçmek için --ustune-yaz")
        ogeler, md = altin_sec(Y, a.n, a.tohum, a.okur_orani, a.taslak_kart)
        json_yaz(gizli_yolu, {"n": a.n, "tohum": a.tohum, "okur_orani": a.okur_orani, "ogeler": ogeler})
        _yaz(insan_yolu, md)
        hedef = [o for o in ogeler if o["rol"] == "hedef"]
        print(f"altın set: {len(hedef)} hikâye ({len({(o['figur'], o['yer']) for o in hedef})} figür x yer hücresi; "
              f"geliştirme {sum(o['yari'] == 'gelistirme' for o in hedef)}, ölçüm "
              f"{sum(o['yari'] == 'olcum' for o in hedef)}) + {len(ogeler) - len(hedef)} okur kanaryası")
        print(f"etiket şablonu: {Y.goreli(insan_yolu)} (okura yalnız bu dosya verilir)")
        if len(hedef) < a.n:
            print(f"UYARI: koddan geçmiş aday {len(hedef)} < {a.n}; 14'lük ek partiler yazılmalı")
        return 0
    gizli = json_oku(gizli_yolu)
    if gizli is None:
        raise SystemExit("önce: altin sec")
    if a.eylem == "oku":
        with open(insan_yolu, encoding="utf-8") as f:
            et = etiket_ayristir(f.read())
        kayit, okur, eksik, anlasilmadi = [], [], 0, []
        for o in gizli["ogeler"]:
            e = et.get(o["sira"], (None,) * 5)
            if e[0] is None:
                eksik += 1
            elif e[0] == "anlasilmadi":
                anlasilmadi.append(o["sira"])
            if o["rol"] == "okur_kanarya":
                okur.append(e[0] == "kusurlu")
                continue
            kayit.append({"sira": o["sira"], "kimlik": o["kimlik"], "sha1": o["sha1"], "figur": o["figur"],
                          "yer": o["yer"], "yari": o["yari"], "etiket": e[0] if e[0] != "anlasilmadi" else None,
                          "cumle": e[1], "neden": e[2], "mercek": e[3], "ham": e[4]})
        jsonl_yaz(Y.d("altin", "etiketler.jsonl"), kayit)
        json_yaz(Y.d("altin", "okur.json"), {"okur_kanarya": len(okur), "yakalanan": sum(okur)})
        say = collections.Counter(k["etiket"] for k in kayit)
        print(f"etiket: {len(kayit) - say[None]}/{len(kayit)} ({say['kusurlu']} kusurlu, {say['kusursuz']} kusursuz); "
              f"okur kanaryası {sum(okur)}/{len(okur)} yakalandı; boş {eksik}, anlaşılmayan {anlasilmadi[:10]}")
        for ad, v in (("kusurlu", say["kusurlu"]), ("kusursuz", say["kusursuz"])):
            if v < 60:
                print(f"UYARI: {ad} {v} < 60: 14'lük ek partiler yazılıp etiketlenmeli")
        if okur and sum(okur) / len(okur) < 0.9:
            print("UYARI: okurun kanarya yakalaması < %90: okuma yöntemi değişmeli (kısa oturum ya da ikinci okur)")
        return 0 if not eksik and not anlasilmadi else 1
    # kurul: etiketleme bittikten sonra, pilot düzeni (her mercekte 2 hakem, kısa devre yok)
    et = altin_etiketleri(Y)
    hedef = [o for o in gizli["ogeler"] if o["rol"] == "hedef"]
    eksik = [o["sira"] for o in hedef if not et.get(o["sha1"], {}).get("etiket")]
    if eksik:
        raise SystemExit(f"kurul etiketlemeden SONRA koşar: {len(eksik)} hikâye etiketsiz (ör. {eksik[:5]})")
    bg = _kapi().Baglam()
    for L in MERCEKLER:
        ozet, _ = hazirla_urun(Y, L, a.parti_boyu, a.tohum, pilot=True, hakem=a.hakem, taslak_kart=a.taslak_kart,
                               taban_aday=a.taban_aday, yalniz={o["sha1"] for o in hedef}, kisa_devre=False, bg=bg)
        print(f"{L}: {ozet.get('parti', 0)} parti, hedef {ozet.get('hedef', 0)}, kanarya {ozet.get('kanarya', 0)}, "
              f"dolgu {ozet.get('dolgu', 0)}")
    return 0


# ---------------------------------------------------------------- uyum (Adım 6, Pilot ölçüleri)

def _binom_kuyruk_ust(x, n, p):
    """P(X >= x)."""
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(x, n + 1))


def cp_alt(x, n, alfa=0.05):
    """Clopper-Pearson tek yönlü alt sınır."""
    if n == 0 or x == 0:
        return 0.0
    lo, hi = 0.0, x / n
    for _ in range(60):
        mid = (lo + hi) / 2
        if _binom_kuyruk_ust(x, n, mid) < alfa:
            lo = mid
        else:
            hi = mid
    return lo


def cp_ust(x, n, alfa=0.05):
    """Clopper-Pearson tek yönlü üst sınır."""
    if n == 0:
        return 1.0
    if x == n:
        return 1.0
    lo, hi = x / n, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if 1 - _binom_kuyruk_ust(x + 1, n, mid) < alfa:
            hi = mid
        else:
            lo = mid
    return hi


def _oran(a, b):
    return round(a / b, 4) if b else None


def uyum_hesapla(Y):
    oylar, partiler = oylari_topla(Y)
    et = altin_etiketleri(Y)
    out = {"mercek": {}, "altin": {}, "kanarya": {}, "konum": {}}
    # (mercek, sha1, hakem) -> var / yok kararı (var: herhangi bir denemede; yok: geçerli partide)
    karar = {}
    for o in oylar:
        if o["rol"] not in ("hedef", "dolgu"):
            continue
        k = (o["mercek"], o["sha1"], o["hakem"])
        if o["varlar"]:
            karar[k] = "var"
        elif o["oy"] == "yok" and o["gecerli"] and karar.get(k) != "var":
            karar[k] = "yok"
    for L in MERCEKLER:
        shalar = {s for (m, s, h) in karar if m == L}
        a = b = c = d = 0
        tek2_dogru = 0
        for s in shalar:
            h1, h2 = karar.get((L, s, 1)), karar.get((L, s, 2))
            if h1 is None or h2 is None:
                continue
            a += h1 == h2 == "var"
            b += h1 == "var" and h2 == "yok"
            c += h1 == "yok" and h2 == "var"
            d += h1 == h2 == "yok"
            tek2_dogru += h1 == "yok" and h2 == "var" and et.get(s, {}).get("etiket") == "kusurlu"
        ps = [p for p in partiler if p["mercek"] == L and p["durum"] != "bekliyor"]
        vs = [v for o in oylar if o["mercek"] == L for v in o["varlar"]]
        n = a + b + c + d
        out["mercek"][L] = {"cift": n, "ikisi_var": a, "yalniz_1": b, "yalniz_2": c, "ikisi_yok": d,
                            "pozitif_uyum": _oran(2 * a, 2 * a + b + c), "ikinci_tek_basina": _oran(c, n),
                            "ikinci_tek_basina_dogrulanan": _oran(tek2_dogru, n) if et else None,
                            "parti": len(ps), "gecersiz_parti": sum(p["durum"] == "gecersiz" for p in ps),
                            "gecersiz_orani": _oran(sum(p["durum"] == "gecersiz" for p in ps), len(ps)),
                            "var": len(vs), "uydurma": sum(v["uydurma"] for v in vs),
                            "uydurma_orani": _oran(sum(v["uydurma"] for v in vs), len(vs))}
        # kanarya: tür x konum yarısı (yapay; doğal kanarya henüz yok)
        kan = [o for o in oylar if o["mercek"] == L and o["rol"] == "kanarya"]
        tablo = collections.defaultdict(lambda: [0, 0])
        for o in kan:
            for anahtar in (("hepsi",), (o["kanarya_tur"],), (o["kanarya_tur"], o["yari"]), ("yari", o["yari"])):
                tablo[":".join(anahtar)][0] += o["yakalandi"]
                tablo[":".join(anahtar)][1] += 1
        out["kanarya"][L] = {k: {"yakalanan": v[0], "toplam": v[1], "oran": _oran(v[0], v[1]), "kaynak": "yapay"}
                             for k, v in sorted(tablo.items())}
        # konum etkisi: ilk / ikinci yarıda ret oranı; iki okuma sırası (hakem 1 / 2) arasındaki fark
        hed = [o for o in oylar if o["mercek"] == L and o["rol"] in ("hedef", "dolgu") and o["oy"] != "eksik"]
        yari = {y: [o for o in hed if o["yari"] == y] for y in ("ilk", "ikinci")}
        r = {y: _oran(sum(bool(o["varlar"]) for o in v), len(v)) for y, v in yari.items()}
        hk = {h: [o for o in hed if o["hakem"] == h] for h in (1, 2)}
        rh = {h: _oran(sum(bool(o["varlar"]) for o in v), len(v)) for h, v in hk.items()}
        fark = abs(r["ilk"] - r["ikinci"]) if None not in r.values() else None
        out["konum"][L] = {"ret_ilk_yari": r["ilk"], "ret_ikinci_yari": r["ikinci"],
                           "fark_puan": round(100 * fark, 1) if fark is not None else None,
                           "ret_hakem1": rh[1], "ret_hakem2": rh[2],
                           "parti_5e_insin": fark is not None and fark > 0.05}
    # altın set: kaçırma m, yanlış ret f, q̂ (ölçüm yarısı ve bütün set)
    if et:
        for kapsam in ("olcum", "hepsi"):
            ets = {s: e for s, e in et.items() if e.get("etiket") and (kapsam == "hepsi" or e["yari"] == "olcum")}
            kus = {s for s, e in ets.items() if e["etiket"] == "kusurlu"}
            tem = {s for s, e in ets.items() if e["etiket"] == "kusursuz"}
            sonuc = {}
            yargiclar = [(f"{L}{h}", lambda s, L=L, h=h: karar.get((L, s, h)) == "var")
                         for L in MERCEKLER for h in (1, 2) if any(k[0] == L and k[2] == h for k in karar)]
            yargiclar += [(L, lambda s, L=L: any(karar.get((L, s, h)) == "var" for h in (1, 2))) for L in MERCEKLER]
            yargiclar += [("kurul", lambda s: any(karar.get((L, s, h)) == "var" for L in MERCEKLER for h in (1, 2)))]
            for ad, isaret in yargiclar:
                hedef_kus = {s for s in kus if ad == "kurul" or ets[s].get("mercek") in (None, ad[0])}
                yak = sum(isaret(s) for s in hedef_kus)
                yr = sum(isaret(s) for s in tem)
                m = 1 - yak / len(hedef_kus) if hedef_kus else None
                f = yr / len(tem) if tem else None
                sonuc[ad] = {"kusurlu": len(hedef_kus), "yakalanan": yak, "kacirma_m": _oran(len(hedef_kus) - yak,
                                                                                            len(hedef_kus)),
                             "yakalama_alt95": round(cp_alt(yak, len(hedef_kus)), 4) if hedef_kus else None,
                             "temiz": len(tem), "yanlis_ret": yr, "yanlis_ret_f": _oran(yr, len(tem))}
                if ad == "kurul" and m is not None and f is not None and (kus or tem):
                    p = len(kus) / (len(kus) + len(tem))
                    pay = p * m + (1 - p) * (1 - f)
                    sonuc[ad]["p"] = round(p, 4)
                    sonuc[ad]["q_hat"] = round(p * m / pay, 4) if pay else None
                    sonuc[ad]["gecer"] = {"yakalama_alt95>=0.90": sonuc[ad]["yakalama_alt95"] >= 0.90,
                                          "q_hat<=0.01": (sonuc[ad]["q_hat"] or 0) <= 0.01,
                                          "yanlis_ret<=0.25": f <= 0.25}
            out["altin"][kapsam] = sonuc
        out["okur"] = json_oku(Y.d("altin", "okur.json"))
    return out


def cmd_uyum(a):
    Y = Yollar(a.ad, a.kok)
    u = uyum_hesapla(Y)
    u["pilot"] = bool(a.pilot)
    json_yaz(Y.d("uyum.json"), u)
    for L, m in u["mercek"].items():
        print(f"{L}: pozitif uyum {m['pozitif_uyum']} ({m['cift']} çift; 1:{m['yalniz_1']} 2:{m['yalniz_2']} "
              f"ikisi:{m['ikisi_var']}); ikinci hakem tek başına {m['ikinci_tek_basina']}"
              + (f" (kullanıcı doğruladı {m['ikinci_tek_basina_dogrulanan']})" if m["ikinci_tek_basina_dogrulanan"]
                 is not None else "")
              + f"; geçersiz parti {m['gecersiz_orani']}; uydurma {m['uydurma_orani']}")
        k = u["kanarya"].get(L, {}).get("hepsi")
        if k:
            print(f"   kanarya {k['yakalanan']}/{k['toplam']} ({k['oran']}); "
                  + ", ".join(f"{t} {v['yakalanan']}/{v['toplam']}" for t, v in u["kanarya"][L].items()
                              if ":" not in t and t != "hepsi"))
        ko = u["konum"][L]
        print(f"   konum: ret ilk yarı {ko['ret_ilk_yari']}, ikinci yarı {ko['ret_ikinci_yari']} (fark "
              f"{ko['fark_puan']} puan{'; PARTİ 5E İNMELİ' if ko['parti_5e_insin'] else ''}); hakem1 "
              f"{ko['ret_hakem1']}, hakem2 {ko['ret_hakem2']}")
    for kapsam, s in u["altin"].items():
        if "kurul" in s:
            k = s["kurul"]
            print(f"altın ({kapsam}): kurul yakalama {k['yakalanan']}/{k['kusurlu']} (alt %95 {k['yakalama_alt95']}), "
                  f"yanlış ret {k['yanlis_ret']}/{k['temiz']}, p {k.get('p')}, q̂ {k.get('q_hat')}; {k.get('gecer')}")
    print(f"-> {Y.goreli(Y.d('uyum.json'))}")
    return 0


# ---------------------------------------------------------------- yaz-istemi (Adım 4)

def _kart_metni(kart):
    """Kartın yazara gösterilen hâli (kaynak kimlikleri ve açık noktalar olmadan)."""
    o = _olgu
    s = [f"- Ad: {o(kart['ad'])} (okunuş: {o(kart['okunus'])}; kesme eki okunuşa uyar)",
         f"- Kimlik: {o(kart['kimlik_cumlesi'])}", f"- Tür: {o(kart['tur'])}",
         f"- Güvenli özellik kullanımı: {o(kart['guvenli_ozellik_kullanimi'])}", "- Özellikler:"]
    s += [f"  - {x['anahtar_kok']}: {x['deger']} (örnek biçimler: {', '.join(x.get('ornek_bicimler', []))})"
          for x in kart["ozellikler"]]
    s.append("- Yerler:")
    for y in kart["yerler"]:
        s.append(f"  - {y['etiket']}: {y['tarif']}")
        adlar = {x["yan_kimlik"]: x["kisa_ad"] for x in kart["yanlar"]}
        for kt in y.get("kosullu_tarifler", []):
            s.append(f"    - yan {adlar.get(kt.get('yan'), kt.get('yan'))} ise: {kt.get('tarif')}")
    s.append("- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):")
    for y in kart["yanlar"]:
        huy = f"; huy: {o(y['huy'])}" if y.get("huy") else ""
        s.append(f"  - {y['kisa_ad']}: {o(y['iliski'])} Tür: {o(y['tur'])}; "
                 f"{'konuşur' if o(y['konusur']) else 'KONUŞMAZ'}{huy}. Yüzey biçimleri: "
                 f"{', '.join(y.get('yuzey_bicimleri', []))}")
    s.append("- Dünya kuralları:")
    s += [f"  - {k['kural']}" for k in kart.get("dunya_kurallari", [])]
    ys = kart.get("yasaklar", {})
    s.append(f"- Yasak adlar: {', '.join(a['ad'] for a in ys.get('adlar', [])) or '-'}")
    s += [f"- Yasak: {o(x)}" for x in ys.get("ogeler", [])]
    s.append(f"- İzinli dünya kelimeleri: {', '.join(kart.get('izinli_dunya_kokleri', [])) or '-'}")
    return "\n".join(s)


def _tohum_metni(t, kart):
    oz = _ozellik_satiri(kart, t["ozellik"])
    yan = ", ".join(t["yan"]) or "-"
    yer = next((y for y in kart["yerler"] if y["etiket"] == t["yer"]), {})
    kimlik = {x["kisa_ad"]: x["yan_kimlik"] for x in kart["yanlar"]}
    tarif = [yer.get("tarif", "")] + [kt["tarif"] for kt in yer.get("kosullu_tarifler", [])
                                      if kt.get("yan") in {kimlik.get(y) for y in t["yan"]}]
    return "\n".join([
        f"### {t['figur']} | {t['yer']} | {yan}", f"@tohum: {t['id']}",
        f"- yer: {t['yer']} ({' '.join(x for x in tarif if x)})",
        f"- tema: {TEMALAR.get(t.get('tema'), (t.get('tema'), None))[0]}",
        f"- yan: {yan}", f"- özellik: {t['ozellik']} ({oz['deger']})",
        f"- kelimeler: isim '{t['isim']}', fiil '{t.get('fiil_mastar') or t['fiil']}', sıfat '{t['sifat']}'",
        f"- diyalog: {t.get('diyalog')}" + (" (hikâyede replik yok)" if t.get("diyalog") == "yok" else ""),
        f"- açılış: {ACILIS.get(t.get('acilis'), t.get('acilis'))}",
        f"- kapanış: {t.get('kapanis')} ({KAPANIS.get(t.get('kapanis'), (0, ''))[1]})"])


def yaz_istemi(Y, figur, n=12, taslak_kart=False, bg=None):
    bg = bg or _bg(zemberek=False)
    kart = _figur_bul(bg, figur)
    ad, fk = _olgu(kart["ad"]), kart["kimlik"]
    if not kart.get("onayli") and not taslak_kart:
        raise SystemExit(f"{ad} kartı onaylı değil; onaysız kartla hikâye yazılmaz (duman testi için --taslak-kart)")
    atanan = collections.defaultdict(set)
    partiler = [0]
    for p in glob.glob(Y.v("istem", f"{fk}_*.json")):
        ist = json_oku(p)
        partiler.append(ist.get("parti", 0))
        for t in ist.get("tohumlar", []):
            atanan[t["id"]].add(t.get("deneme", 1))
    secilen = [t for t in jsonl_oku(Y.v("kuyruk.jsonl")) if t["figur"] == ad and t["deneme"] not in atanan[t["id"]]]
    secilen = secilen[:n]
    for t in jsonl_oku(Y.tohum(fk)):
        if len(secilen) >= n:
            break
        if t["id"] not in atanan:
            secilen.append({**t, "deneme": 1})
    if not secilen:
        raise SystemExit(f"{ad}: yazılacak tohum yok ({Y.goreli(Y.tohum(fk))} ve kuyruk)")
    parti = max(partiler) + 1
    dosya_rel = f"aday/{fk}_{parti}.txt"
    istem_yolu = Y.v("istem", f"{fk}_{parti}.md")
    kilavuz_yolu = os.path.join(HERE, "KILAVUZ_URUN.md")
    with open(kilavuz_yolu, encoding="utf-8") as f:
        kilavuz = f.read().strip()
    yer_tutucu = re.compile(r"^\[KULLANICI ONAYLI[^\]]*\]\s*$", re.M)
    if yer_tutucu.search(kilavuz):      # onaylı iyi örnekler henüz yok: yer tutucu yazara gitmez
        print("UYARI: KILAVUZ_URUN.md'de kullanıcı onaylı örnek yok; istem örneksiz yazıldı")
        kilavuz = yer_tutucu.sub("", re.sub(r"^\*\*İyi örnekler\*\*.*$", "", kilavuz, flags=re.M))
        kilavuz = re.sub(r"\n{3,}", "\n\n", kilavuz).strip()
    kontrol = (f".venv/bin/python degerlendirme/veri_hakem.py kontrol {Y.goreli(Y.v(dosya_rel))}"
               + (f" --kok {os.path.dirname(os.path.dirname(Y.veri))}" if not Y.veri.startswith(ROOT + os.sep) else "")
               + (" --taslak-kart" if taslak_kart else ""))
    metin = f"""# Yazar görevi: {ad}, parti {parti}

Sen bir çocuk hikâyesi yazarısın. Aşağıdaki {len(secilen)} tohumun her birinden BİR hikâye yaz. Hikâyeler 3-6 yaş
çocuklara okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `{Y.goreli(Y.v(dosya_rel))}`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, hakem puanlarını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf). Başlık ve @tohum satırını
  aşağıdaki tohumdan birebir kopyala; hikâyeler arasında bir boş satır bırak:

```
### {ad} | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `{kontrol}`
  İşaretlenen hikâyede EN ÇOK 1 yerel düzeltme yap ve kontrolü bir kez daha koş. Yine geçmeyen hikâyenin bütün
  bloğunu (başlık dahil) dosyadan sil; zorlama. Geçen hikâyeye dokunma (her değişiklik bir yama sayılır).

## Yazım kılavuzu

{kilavuz}

## Kart: {ad} (kaynaklı, kapalı dünya)

{_kart_metni(kart)}

## Tohumlar

""" + "\n\n".join(_tohum_metni(t, kart) for t in secilen) + "\n"
    _yaz(istem_yolu, metin)
    json_yaz(Y.v("istem", f"{fk}_{parti}.json"), {
        "figur": ad, "parti": parti, "dosya": dosya_rel, "istem": os.path.relpath(istem_yolu, Y.veri),
        "tohumlar": [{"id": t["id"], "deneme": t["deneme"]} for t in secilen],
        "istem_sha256": hashlib.sha256(metin.encode()).hexdigest(), "kilavuz_sha256": sha256_dosya(kilavuz_yolu),
        "kart_sha1": kart_sha1(kart), "taslak_kart": not kart.get("onayli")})
    return istem_yolu, secilen


def cmd_yaz_istemi(a):
    Y = Yollar(a.ad, a.kok)
    yol, secilen = yaz_istemi(Y, a.figur, a.n, a.taslak_kart)
    d2 = sum(t["deneme"] > 1 for t in secilen)
    print(f"{len(secilen)} tohum ({d2} ikinci deneme) -> {Y.goreli(yol)}")
    return 0


# ---------------------------------------------------------------- komut satırı

def main(argv=None):
    ap = argparse.ArgumentParser(description="Eğitim verisi hakem hattı (eski ve ürün)")
    alt = ap.add_subparsers(dest="komut", required=True)

    def urun(p, ad=True):
        if ad:
            p.add_argument("ad", nargs="?", default="urun_v1", help="data/<ad> ve degerlendirme/<ad>")
        p.add_argument("--kok", default=None, help="deneme kökü: <kok>/data/<ad>, <kok>/degerlendirme/<ad>")
        return p

    h = alt.add_parser("hazirla", help="eski: hazirla <klasör>; ürün: hazirla urun_v1 --lens M|D|K")
    h.add_argument("klasor")
    h.add_argument("--onek", default="")
    h.add_argument("--parti-boyu", type=int, default=None, help="eski 40, ürün 10 (<= 10)")
    h.add_argument("--ad", default=None)
    h.add_argument("--lens", choices=list(MERCEKLER), default=None, help="ürün hattı merceği")
    h.add_argument("--tohum", type=int, default=2026)
    h.add_argument("--pilot", action="store_true", help="kısa devre yok, K de 2 hakem")
    h.add_argument("--hakem", default=None, help="hakem sayısı: 'M=2,D=2,K=1'")
    h.add_argument("--taslak-kart", action="store_true")
    h.add_argument("--taban-aday", action="store_true", help="Pilot-0: kanarya tabanı koddan geçmiş aday olabilir")
    h.add_argument("--kisa-devre-yok", action="store_true")
    h.add_argument("--kok", default=None)
    o = alt.add_parser("ozet")
    o.add_argument("adlar", nargs="*")
    for k in ("duzelt", "tekrar"):
        alt.add_parser(k).add_argument("ad")

    k = urun(alt.add_parser("kart-kontrol"))
    k.add_argument("--kart", default=None)
    k.add_argument("--urun", default=None)
    k.add_argument("--kilitle", action="store_true", help="onaylı kartların sha1'ini kilitle")
    t = urun(alt.add_parser("tohum"))
    t.add_argument("--figur", required=True, help="figür adı ya da 'hepsi'")
    t.add_argument("--n", type=int, default=400)
    t.add_argument("--tohum", type=int, default=2026)
    t.add_argument("--cikti", default=None)
    t.add_argument("--ustune-yaz", action="store_true")
    t.add_argument("--denetle", action="store_true", help="üretmeden var olan dosyayı denetle")
    t.add_argument("--ayrinti", action="store_true")
    y = urun(alt.add_parser("yaz-istemi"))
    y.add_argument("--figur", required=True)
    y.add_argument("--n", type=int, default=12)
    y.add_argument("--taslak-kart", action="store_true")
    kn = urun(alt.add_parser("kontrol"), ad=False)
    kn.add_argument("dosya")
    kn.add_argument("--ad", default="urun_v1")
    kn.add_argument("--tohum", default=None, help="ek tohum JSONL")
    kn.add_argument("--taslak-kart", action="store_true")
    kn.add_argument("--json", action="store_true")
    kp = urun(alt.add_parser("kapi"))
    g = kp.add_mutually_exclusive_group(required=True)
    g.add_argument("--figur")
    g.add_argument("--hepsi", action="store_true")
    kp.add_argument("--taslak-kart", action="store_true")
    urun(alt.add_parser("oku"))
    kr = urun(alt.add_parser("karar"))
    kr.add_argument("--pilot", action="store_true")
    kr.add_argument("--hakem", default=None)
    kr.add_argument("--taslak-kart", action="store_true", help="onaysız kartla kabul (yalnız duman testi)")
    al = alt.add_parser("altin")
    al.add_argument("eylem", choices=["sec", "oku", "kurul"])
    urun(al)
    al.add_argument("--n", type=int, default=150)
    al.add_argument("--tohum", type=int, default=2026)
    al.add_argument("--okur-orani", type=float, default=0.08)
    al.add_argument("--parti-boyu", type=int, default=10)
    al.add_argument("--hakem", default=None)
    al.add_argument("--taslak-kart", action="store_true")
    al.add_argument("--taban-aday", action="store_true")
    al.add_argument("--ustune-yaz", action="store_true")
    u = urun(alt.add_parser("uyum"))
    u.add_argument("--pilot", action="store_true")
    a = ap.parse_args(argv)
    if a.komut == "hazirla":
        if a.lens:
            a.parti_boyu_urun = a.parti_boyu or 10
            return cmd_hazirla_urun(a)
        a.parti_boyu = a.parti_boyu or 40
        return hazirla(a)
    return {"ozet": ozet, "duzelt": duzelt, "tekrar": tekrar, "kart-kontrol": cmd_kart_kontrol, "tohum": cmd_tohum,
            "yaz-istemi": cmd_yaz_istemi, "kontrol": cmd_kontrol, "kapi": cmd_kapi, "oku": cmd_oku,
            "karar": cmd_karar, "altin": cmd_altin, "uyum": cmd_uyum}[a.komut](a)


if __name__ == "__main__":
    sys.exit(main() or 0)
