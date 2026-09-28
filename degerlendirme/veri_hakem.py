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


