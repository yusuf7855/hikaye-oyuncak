"""secici.h (C) ile Python seçicisinin eşitlik testi: aday havuzlarının her adayı iki tarafta da puanlanır; puan
farkı, kural kural fark ve vaka başına seçim (argmax) karşılaştırılır.

--urun (kartın kullandığı yol): secici_urun_puanla = degerlendirme/urun_uret.puanla. Havuzlar urun_uret.py çıktıları
  (vaka başına bütün adaylar "adaylar" altında; varsayılan: c3ft_karma, 1030s2, 1030, 740 kıyaslarının 8'er adayı,
  ~5000 aday). Puan farkı toleransı 1e-9 (lp kartta da gen -l'nin 4 basamaklı değerlerinden hesaplanır).
  python firmware/hikaye_oyuncak/tools/secici_karsilastir.py --urun [--sentetik 5000]
Eski yol: secici_puanla (-DSECICI_ESKI=1) = degerlendirme/sec.py puanla, tolerans 1e-3.
Kullanım: python firmware/hikaye_oyuncak/tools/secici_karsilastir.py [havuz.json ...] [--guvenlik] [--ayrinti N]
  varsayılan havuzlar: hf_c2ft_plan/adaylar_c2ft_plan.json ve adaylar_c2ft_plan_dog.json
  --guvenlik: puanla(guvenlik=True) ile de (kartta açık olan yol) karşılaştır.
  --sentetik N: ayrıca havuz adaylarından N bozulmuş aday üret (kuralları tetikleyen parçalar, büyük İ/I, tırnak,
      satır sonu, kesme, yinelenen cümle, bozuk plan ...) ve onları da karşılaştır (seçim yok, yalnız puan).
  Her adayda kural kural karşılaştırma da yapılır (toplam aynı ama kurallar farklıysa da uyuşmazlık sayılır).
  tools/secici_test.c cc ile derlenir (derleyici: CC ortam değişkeni, varsayılan cc).
Çıkış kodu: uyuşmazlık varsa 1.
"""
import argparse
import json
import os
import random
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(TOOLS)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
from baslangic import KAR  # noqa: E402
import sec  # noqa: E402
import urun_uret as U  # noqa: E402

FIGUR = list(KAR)  # secici.h SC_ISIM sırası
YER = ["orman", "deniz", "ev", "park", "sato", "dag"]
# sec.cezalar mesajı -> secici.h kural adı (sıra önemli: ilk eşleşen)
MESAJ = [("kendine gönderme", "kendine"), ("hikâyede yeterince yok", "az_isim"), ("sonda yok", "sonda_yok"),
         ("sonradan beliren", "yeni_hayvan"), ("aynı konuşmacı", "konusmaci"), ("yanlış isim", "yanlis_isim"),
         ("tekrarlanan cümle", "tekrar_cumle"), ("yarım son", "yarim"), ("çok kısa", "kisa"),
         ("uydurma kelime", "uydurma_kelime"), ("tekrar eden ifade", "tekrar_ifade"),
         ("iki kez tanıtılıyor", "iki_tanitim"), ("kendi kendine", "kendi_kendine"), ("başkası kendini", "baskasi"),
         ("uydurma karakter adı", "uydurma_ad"), ("özellik karışması", "ozellik"), ("kekeme tekrar", "kekeme"),
         ("ders olaydan kopuk", "ders"), ("plan bozuk", "plan"), (" ve ", "isim_ve_isim")]


def py_kurallar(h, guvenlik):
    d = {}
    for p, msj in sec.cezalar(h["metin"], h["kim"], h["n"], bitti=h["bitti"], plan=h.get("plan")):
        ad = next(a for m, a in MESAJ if m in msj)
        d[ad] = d.get(ad, 0) + p
    if (y := sec.yer_cezasi(h["metin"], h["yer"])):
        d["yer"] = y
    if guvenlik and (g := sec.guvenlik_cezasi(h["metin"])):
        d["guvenlik"] = g[0]
    return d


PARCA = ["Pamuk'un", "Pamuk", "Tekir'e", "Karabaş", "Bal'ın", "Kızıl'dan", "Can", "Elif'le", "Dino'ya", "Alev",
         "Paytak", "Cikcik", "Tosbi'nin", "Tom", "Minnoş'un", "Zıpzıp", "İkisi", "IŞIK", "Işık", "\"Ben de Pamuk\" dedi kedi",
         "\"Merhaba\" dedi Pamuk.", "\"Evet\" diye sordu Pamuk.", "”Tamam” dedi Tekir", "adım Bal” diye bağırdı ayı",
         "Pamuk adında", "Pamuk ve Pamuk", "Bal, Bal'ın", "Pamuk Pamuk'u gördü", "Bir gün Pamuk ormanda Pamuk'a",
         "gaga", "gagasıyla", "kuş", "kaz", "kazan", "kuyruğunu salladı", "baloncuk", "burnunu soktu",
         "kabuğunu çıkardı", "koştu koştu", "yavaş yavaş", "çok çok çok", "top oynadı, top oynadı", "top ve top",
         "paylaşmanın güzel olduğunu anladı.", "dürüst olmayı öğrendi.", "sabırlı olmayı öğrenmişti.",
         "kan", "kanlar", "kanat", "yara", "yarası", "yaralandı", "gözyaşlarına boğuldu", "boğuldu", "dizi kanadı",
         "tehlikeli", "canı acıdı", "derin suya", "evde", "eve", "evimiz", "ev", "dağda", "dağın", "şatoda", "parkta",
         "denizde", "kumsalda", "kıyıya", "ormanda", "sincap", "uğur böceği", "tavşan", "kedi", "karınca",
         "zıplazıp", "qwx", "âlem", "Çok", "Öyle", "Şimdi", "Ürkek", "Ğ", ":", "“", "”", "'", "’", "\n", "\t", "  ",
         ".", "!", "?", ",", "diye", "dedi", "sordu", "123", "_x"]


def boz(h, rng):
    """Havuz adayından kuralları zorlayan bozulmuş bir kopya."""
    k = dict(h)
    w = k["metin"].split(" ")
    for _ in range(rng.randint(1, 8)):
        w.insert(rng.randint(0, len(w)), rng.choice(PARCA))
    if rng.random() < 0.3 and len(w) > 10:  # cümle tekrarı
        i = rng.randint(0, len(w) - 5)
        w[i:i] = w[i:i + 5] + ["."]
    if rng.random() < 0.2:
        w = w[:rng.randint(1, len(w))]
    k["metin"] = " ".join(w)
    if rng.random() < 0.2:
        k["metin"] = rng.choice(["", " ", "\n"]) + k["metin"] + rng.choice(["", " ", "\n", " .", "\"", "”"])
    k["bitti"] = rng.random() < 0.8
    k["yer"] = rng.choice(YER)
    if rng.random() < 0.3:
        k["kim"] = rng.sample(FIGUR, rng.choice([1, 2]))
    pl = k.get("plan") or "Sorun: x\nÇözüm: y"
    r = rng.random()
    if r < 0.1:
        pl = pl.replace("\nÇözüm:", "\n\nÇözüm:")
    elif r < 0.2:
        pl = pl.replace("Çözüm:", "Çözüm:  \t")
    elif r < 0.25:
        pl = pl + "\nbaşka satır"
    elif r < 0.3:
        pl = pl.split("\n")[0]
    elif r < 0.35:
        pl = "Sorun: \t\nÇözüm: y  \n "
    elif r < 0.4:
        pl = pl + " \n \n"
    k["plan"] = pl
    return k


# ---- ürün seçicisi (urun_uret.puanla) ----
URUN_HAVUZ = [os.path.join(ROOT, "degerlendirme", *y) for y in (
    ("urun_kiyas_karma", "mkarma.json"), ("urun_kiyas_karma", "m1030s2.json"),
    ("urun_kiyas_740_1030", "buyuk_164", "m1030.json"), ("urun_kiyas_740_1030", "buyuk_164", "m740.json"))]
URUN_YER = ["orman", "deniz", "ev", "park", "şato", "dağ"]  # generated/istemler.h YER_AD
# urun_uret.puanla mesajı -> secici.h kural adı (ilk eşleşen); "kendi kendine" figürün adıyla başlıyorsa olay kuralı,
# yoksa kadro_cezalari'nın yan kuralı; "'X X'" (içinde " ve " yok) kadro_cezalari, "'X ve X'" figürün kendi kuralı
URUN_MESAJ = [("hikâyede yeterince yok", "az_isim"), ("sonda yok", "sonda_yok"), ("yanlış isim", "yanlis_isim"),
              ("tekrarlanan cümle", "tekrar_cumle"), ("yarım son", "yarim"), ("çok kısa", "kisa"),
              ("uydurma kelime", "uydurma_kelime"), ("tekrar eden ifade", "tekrar_ifade"),
              ("iki kez tanıtılıyor", "iki_tanitim"), ("başkası kendini", "baskasi"),
              ("uydurma karakter adı", "uydurma_ad"), ("özellik karışması", "ozellik"), ("kekeme tekrar", "kekeme"),
              ("ders olaydan kopuk", "ders"), ("plan bozuk", "plan"), ("kendine sesleniyor", "kendine_seslenme"),
              ("kartta olmayan ad", "kartta_olmayan_ad"), ("takıntılı tekrar", "takinti"), ("yer tutmuyor", "yer"),
              ("çocuğa uygun olmayan", "guvenlik"), ("gövde yok", "govde_yok")]


def urun_kurallar(cez, ad):
    d = {}
    for p, msj in cez:
        if "kendi kendine" in msj:
            k = "kendi_kendine" if msj.startswith(ad + " kendi kendine") else "yan_kendi_kendine"
        elif msj.startswith("'") and msj.endswith("'"):
            k = "isim_ve_isim" if msj == f"'{ad} ve {ad}'" else "kadro_tekrar"
        else:
            k = next(a for m, a in URUN_MESAJ if m in msj)
        d[k] = d.get(k, 0) + p
    return d


URUN_PARCA = ["Niloya'nın", "Niloya", "Mete", "Murat", "Tospik'e", "Maşa", "Koca Ayı", "Daşa", "Pepee", "Şila'yla",
              "Bebee", "Keloğlan", "Bilgecan Dede", "Balkız", "Doru", "Kırat", "Alaca", "Hayri", "Basri Amca", "Yumak",
              "Şakir", "Fil Necati", "Kadriye", "Elsa", "Anna", "Olaf'ın", "Kristoff", "Sven", "Chase", "Ryder",
              "Skye", "Örümcek Adam", "Ghost-Spider", "Spin", "Hulk", "Hello Kitty", "Kitty", "Mimi", "Anne", "Dede",
              "Babaanneciğim", "Annesi", "Tim", "Timsah", "Bal", "Balık", "Can", "Canı", "Sara", "Sarayın", "Tom'un",
              "Susie'nin", "Kekiklerin", "Zort", "Zort'un", "Bobby-Lee", "Doru o evin", "İkisi", "IŞIK",
              "\"Teşekkürler, Şila!\" dedi Şila", "\"Merhaba Mete\" diye seslendi Mete", "“Gel Anna” dedi Anna Elsa",
              "\"Koca Ayı gel\" dedi Koca Ayı", "\"Tamam\" cevap verdi Mimi", "Mete Mete", "Mete ile Mete",
              "Anna, ve Anna", "Elsa ile Elsa", "Niloya ve Niloya", "Mete Mete'yi gördü", "Anna Anna'ya baktı",
              "Kitty Kitty'nin", "havlu", "havlusu", "havluyu", "kumdan", "kumdan kale", "sonra", "dedi", "Şimdi",
              "ormanda", "dağda", "şatoda", "denizde", "parkta", "evde", "kan", "yaralandı", "gaga", "baloncuk",
              "koştu koştu", "paylaşmanın güzel olduğunu anladı.", "\"", "“", "”", "'", "’", "\n", "  ", ".", "!",
              "?", ",", ":", "diye", "sordu", "-", "Ali-Veli"]


def urun_boz(h, rng):
    k = dict(h)
    w = k["metin"].split(" ")
    for _ in range(rng.randint(1, 10)):
        p = rng.choice(URUN_PARCA)
        w.insert(rng.randint(0, len(w)), " ".join([p] * (rng.randint(5, 12) if p.startswith("havlu") and rng.random() < 0.3 else 1)))
    if rng.random() < 0.3 and len(w) > 10:
        i = rng.randint(0, len(w) - 5)
        w[i:i] = w[i:i + 5] + ["."]
    if rng.random() < 0.2:
        w = w[:rng.randint(1, len(w))]
    k["metin"] = " ".join(w).strip()
    k["bitti"] = rng.random() < 0.8
    if rng.random() < 0.3:
        k["figur"] = rng.choice(list(U.FIGURLER))
        k["yer"] = rng.choice([y["etiket"] for y in U.KARTLAR[k["figur"]]["yerler"]])
    pl = k.get("plan") or "Sorun: x\nÇözüm: y"
    r = rng.random()
    if r < 0.1:
        pl = pl.replace("\nÇözüm:", "\n\nÇözüm:")
    elif r < 0.2:
        pl = pl.split("\n")[0]
    k["plan"] = pl
    k["plan_bozuk"] = rng.random() < 0.02
    return k


def urun_karsilastir(a, ikili, adlar):
    havuzlar = a.havuz or [y for y in URUN_HAVUZ if os.path.exists(y)]
    kumeler = []
    for y in havuzlar:
        adaylar = []
        for vi, v in enumerate(json.load(open(y, encoding="utf-8"))):
            for j, c in enumerate(v.get("adaylar") or [v]):
                adaylar.append({**c, "figur": v["figur"], "yer": v["yer"], "vaka": vi, "j": j})
        kumeler.append((os.path.relpath(y, ROOT), adaylar, True))
    if a.sentetik:
        rng = random.Random(a.tohum)
        kaynak = [h for _, v, _ in kumeler for h in v if h["metin"]]
        kumeler.append((f"sentetik_{a.sentetik}", [urun_boz(rng.choice(kaynak), rng) for _ in range(a.sentetik)], False))
    fig = list(U.FIGURLER)
    toplam_hata, toplam_aday = 0, 0
    for yol, adaylar, secimli in kumeler:
        girdi = bytearray()
        for h in adaylar:
            m = b"" if h["plan_bozuk"] else h["metin"].encode()
            p = h.get("plan")
            p = p.encode() if p is not None else None
            girdi += (f"{fig.index(h['figur'])} {URUN_YER.index(h['yer'])} {int(bool(h['bitti']))} {h['lp']!r} "
                      f"{len(m)} {len(p) if p is not None else -1}\n").encode()
            girdi += m + (p or b"")
        cikti = subprocess.run([ikili, "-u"], input=bytes(girdi), capture_output=True, check=True).stdout.decode()
        satirlar = [list(map(float, s.split())) for s in cikti.strip().split("\n")]
        assert len(satirlar) == len(adaylar), (len(satirlar), len(adaylar))
        fark, kural_fark, vakalar, gosterilen, tetik = 0, 0, {}, 0, {}
        for h, s in zip(adaylar, satirlar):
            py, cez = U.puanla(h, h["figur"], h["yer"])
            vakalar.setdefault(h.get("vaka", id(h)), []).append((h.get("j", 0), py, s[0]))
            pk = urun_kurallar(cez, U.KARTLAR[h["figur"]]["ad"]["deger"])
            ck = {ad: v for ad, v in zip(adlar, s[1:]) if v}
            for ad in pk:
                tetik[ad] = tetik.get(ad, 0) + 1
            ayri = {k: (pk.get(k, 0), ck.get(k, 0)) for k in set(pk) | set(ck)
                    if abs(pk.get(k, 0) - ck.get(k, 0)) > 1e-9}
            kural_fark += bool(ayri)
            if abs(py - s[0]) > 1e-9 or ayri:
                fark += abs(py - s[0]) > 1e-9
                if gosterilen < a.ayrinti:
                    gosterilen += 1
                    print(f"  {h['figur']} {h['yer']}: python {py:.6f} C {s[0]:.6f}  (python, C): {ayri}")
                    print("   ", repr(h["metin"][:400]), repr(h.get("plan")))
        secim = 0
        for v in (vakalar.values() if secimli else []):
            v.sort()
            py_en = max(range(len(v)), key=lambda i: v[i][1])
            c_en = max(range(len(v)), key=lambda i: v[i][2])
            secim += py_en != c_en
        print(f"{yol}: {len(adaylar)} aday, puan uyuşmazlığı {fark}, kural uyuşmazlığı {kural_fark}"
              + (f", {len(vakalar)} vakada seçim farkı {secim}" if secimli else ""))
        print("   python'da tetiklenen kurallar (aday):", dict(sorted(tetik.items())))
        toplam_hata += fark + kural_fark + secim
        toplam_aday += len(adaylar)
    print(f"toplam: {toplam_aday} aday, uyuşmazlık {toplam_hata}")
    return toplam_hata


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("havuz", nargs="*")
    ap.add_argument("--urun", action="store_true", help="ürün seçicisi (urun_uret.puanla = secici_urun_puanla)")
    ap.add_argument("--guvenlik", action="store_true")
    ap.add_argument("--sentetik", type=int, default=0)
    ap.add_argument("--tohum", type=int, default=1)
    ap.add_argument("--ayrinti", type=int, default=5, help="en çok bu kadar uyuşmazlığı ayrıntılı yaz")
    a = ap.parse_args()
    ikili = os.path.join(tempfile.gettempdir(), "secici_test")
    subprocess.run([os.environ.get("CC", "cc"), "-O2", "-Wall", "-Wno-unused-function", "-DSECICI_ESKI=1", "-o", ikili,
                    os.path.join(TOOLS, "secici_test.c")], check=True)
    adlar = subprocess.run([ikili, "-a"], capture_output=True, text=True, check=True).stdout.split()
    if a.urun:
        sys.exit(1 if urun_karsilastir(a, ikili, adlar) else 0)
    a.havuz = a.havuz or [os.path.join(ROOT, "hf_c2ft_plan", "adaylar_c2ft_plan.json"),
                          os.path.join(ROOT, "hf_c2ft_plan", "adaylar_c2ft_plan_dog.json")]
    toplam_hata = 0
    for guv in ([False, True] if a.guvenlik else [False]):
        kumeler = [(os.path.basename(y), json.load(open(y, encoding="utf-8")), True) for y in a.havuz]
        if a.sentetik:
            rng = random.Random(a.tohum)
            kaynak = [h for _, v, _ in kumeler for h in v if h["metin"]]
            kumeler.append((f"sentetik_{a.sentetik}", [boz(rng.choice(kaynak), rng) for _ in range(a.sentetik)], False))
        for yol, adaylar, secimli in kumeler:
            girdi = bytearray()
            for h in adaylar:
                m, p = h["metin"].encode(), h.get("plan")
                p = p.encode() if p is not None else None
                fig = [FIGUR.index(k) for k in h["kim"]]
                girdi += (f"{len(fig)} {' '.join(map(str, fig))} {YER.index(h['yer'])} {int(bool(h['bitti']))} "
                          f"{h['lp']!r} {int(guv)} {len(m)} {len(p) if p is not None else -1}\n").encode()
                girdi += m + (p or b"")
            cikti = subprocess.run([ikili], input=bytes(girdi), capture_output=True, check=True).stdout.decode()
            satirlar = [list(map(float, s.split())) for s in cikti.strip().split("\n")]
            assert len(satirlar) == len(adaylar), (len(satirlar), len(adaylar))
            fark, kural_fark, vakalar, gosterilen, tetik = 0, 0, {}, 0, {}
            for h, s in zip(adaylar, satirlar):
                py = sec.puanla(h["metin"], h["kim"], h["lp"], h["n"], h["yer"], h["bitti"], guvenlik=guv,
                                plan=h.get("plan"))
                vakalar.setdefault(h["vaka"], []).append((h["j"], py, s[0]))
                pk = py_kurallar(h, guv)
                ck = {ad: v for ad, v in zip(adlar, s[1:]) if v}
                for ad in pk:
                    tetik[ad] = tetik.get(ad, 0) + 1
                ayri = {k: (pk.get(k, 0), ck.get(k, 0)) for k in set(pk) | set(ck)
                        if abs(pk.get(k, 0) - ck.get(k, 0)) > 1e-9}
                kural_fark += bool(ayri)
                if abs(py - s[0]) > 1e-3 or ayri:
                    fark += abs(py - s[0]) > 1e-3
                    if gosterilen < a.ayrinti:
                        gosterilen += 1
                        print(f"  vaka {h['vaka']} j {h['j']}: python {py:.4f} C {s[0]:.4f}  (python, C): {ayri}")
                        print("   ", repr(h["metin"][:400]), repr(h.get("plan")))
            secim = 0
            for v in (vakalar.values() if secimli else []):
                v.sort()
                py_en = max(range(len(v)), key=lambda i: v[i][1])
                c_en = max(range(len(v)), key=lambda i: v[i][2])
                secim += py_en != c_en
            print(f"{yol} guvenlik={guv}: {len(adaylar)} aday, puan uyuşmazlığı {fark}, kural uyuşmazlığı "
                  f"{kural_fark}" + (f", {len(vakalar)} vakada seçim farkı {secim}" if secimli else ""))
            print("   python'da tetiklenen kurallar (aday):", dict(sorted(tetik.items())))
            toplam_hata += fark + kural_fark + secim
    sys.exit(1 if toplam_hata else 0)


if __name__ == "__main__":
    main()
