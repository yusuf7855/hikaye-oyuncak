"""Ürün akışının kartın kendi koduyla (hikaye_oyuncak.ino, sahte ESP32 başlıklarıyla: tools/kart_pc) bilgisayarda
denemesi: stand (taslak NFC okuyucu, etiket kaydı), tanınmış figürler, selamlama, okuma ve halka, oyuncak çekilince
davranışları, sesli komutlar (taklit), gece figürü (ninni, uyku zamanlayıcısı, kapanma), ayar kartı (Wi-Fi, ayar
sayfası istekleri, form doğrulaması, oyuncak tanıt, hikâyeleri sil, kalıcılık).

Saat taklittir (KART_SAAT=sahte): okuma süresi harf başına 40 ms, üretim her saat okumasında 50 µs; aynı girdi her
seferinde aynı çıktıyı verir. Kuyruk K=2 aday, figür başına en çok 2 hikâye (hızlı).

  1. tanınma:   tanınmış figür yokken arka plan hiçbir şey üretmez; Elsa konunca halka dolar, selamlanır, canlı
                yazılır, okunur (halka ilerlemesi); tanınır (NVS) ve arka plan yalnız Elsa'yı hazırlar; yeniden
                başlatınca hazır hikâye üretmeden okunur.
  2. çekilince: aynı hikâye "cümle sonunda dur" / "hemen dur" / "hikâyeyi bitir" ayarlarıyla.
  3. sesli:     uyandırma (dinle), dur (kaldığı cümle), devam, bir daha, başka, sesi aç/kıs (okurken), oyuncak yokken,
                komutsuz uyandırma (anlaşılmadı), canlı üretim sırasında dur.
  4. etiket:    UID tablosuna düşme, bilinmeyen etiket, halka karesinin RMT bitlerinden çözümü (renk, tavan).
  5. gece:      Ay Dede: ninni selamı, yerleşik ninniler art arda, zamanlayıcı -> sönme -> kapanma (hafif uyku),
                başka oyuncakla uyanma; gece figürü için arka planda üretim yok.
  6. ayar:      ayar kartı: WPA2 erişim noktası + söylenen şifre, captive yönlendirme, /durum, /kaydet (geçerli ve
                geçersiz), oyuncak tanıt (etiket belleği dosyası), /sil, /bitir; kart çekilince kapanma, 10 dk, Wi-Fi
                hatası; ayarların kalıcılığı (selamda ad).

Kullanım: .venv/bin/python firmware/hikaye_oyuncak/tools/urun_akis_test.py [--dizin D]   (çıkış kodu: hata varsa 1)
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SKETCH = os.path.dirname(TOOLS)
ROOT = os.path.dirname(os.path.dirname(SKETCH))
MODEL = os.path.join(ROOT, "hf_c3ft_karma", "model.bin")
with open(os.path.join(ROOT, "data", "figur_donanim.json"), encoding="utf-8") as _f:
    DONANIM = json.load(_f)
TAVAN, PARLAK = 25, 60  # HALKA_PARLAKLIK_SINIR, varsayılan ayar

hatalar = []


def dene(kosul, mesaj):
    if not kosul:
        hatalar.append(mesaj)
        print("  HATA:", mesaj)
    return kosul


def derle(d):
    kart = os.path.join(d, "kart_pc")
    subprocess.run([os.environ.get("CXX", "g++"), "-O2", "-Wall", "-Wno-unused-function", "-DKUYRUK_K=2",
                    "-DKUYRUK_FIGUR_MAKS=2", "-I" + os.path.join(TOOLS, "kart_pc", "sahte"), "-o", kart,
                    os.path.join(TOOLS, "kart_pc", "kart_pc.cpp")], check=True)
    return kart


class Kart:
    def __init__(self, kart, d):
        self.kart, self.d = kart, d

    def kos(self, satirlar, ek_env=None):
        env = dict(os.environ, KART_MODEL=MODEL, KART_BOLUMLER=os.path.join(SKETCH, "partitions.csv"),
                   KART_KUYRUK=os.path.join(self.d, "kuyruk.bin"), KART_NVS=os.path.join(self.d, "nvs.txt"),
                   KART_SAAT="sahte")
        env.update(ek_env or {})
        r = subprocess.run([self.kart], input="".join(s + "\n" for s in satirlar), capture_output=True, text=True,
                           env=env, timeout=900)
        if r.returncode:
            print(r.stdout[-3000:], r.stderr[-3000:])
            raise SystemExit(f"kart_pc çıkış kodu {r.returncode}")
        return r.stdout, r.stderr.splitlines()

    def sifirla(self):
        for ad in ("kuyruk.bin", "nvs.txt"):
            p = os.path.join(self.d, ad)
            if os.path.exists(p):
                os.remove(p)

    def nvs(self, **kv):
        """NVS dosyasına sayı anahtarları ekler (ayar sayfası yerine)."""
        p = os.path.join(self.d, "nvs.txt")
        satir = [s for s in (open(p).read().splitlines() if os.path.exists(p) else [])
                 if not any(s.startswith(f"i {k} ") for k in kv)]
        satir += [f"i {k} {v}" for k, v in kv.items()]
        with open(p, "w") as f:
            f.write("\n".join(satir) + "\n")

    def sakla(self, ad):
        for f in ("kuyruk.bin", "nvs.txt"):
            if os.path.exists(os.path.join(self.d, f)):
                shutil.copy(os.path.join(self.d, f), os.path.join(self.d, f"{ad}_{f}"))

    def geri(self, ad):
        for f in ("kuyruk.bin", "nvs.txt"):
            if os.path.exists(os.path.join(self.d, f"{ad}_{f}")):
                shutil.copy(os.path.join(self.d, f"{ad}_{f}"), os.path.join(self.d, f))


def halka_d(err):
    return [s[8:] for s in err if s.startswith("HALKA_D ")]


def okumalar(out):
    """(okunan, toplam, durdu, cümle ortasında)"""
    return [(int(a), int(b), bool(c), bool(o)) for a, b, c, o in
            re.findall(r"\(okuma: (\d+)/(\d+) cümle(, durdu)?(, cümle ortasında)?\)", out)]


def durum(err):
    return [list(map(int, s.split()[1:])) for s in err if s.startswith("DURUM ")]


def isler(err):
    return [s.split() for s in err if s.startswith("KUYRUK ")]


def http(err):
    out = []
    for s in err:
        m = re.match(r"HTTP (\d+) (.*?)(?: -> (\S+))?$", s)
        if m:
            out.append((int(m.group(1)), m.group(2), m.group(3)))
    return out


def renk(d):
    h = DONANIM["figurler"][d]["renk"].lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def kisik(c):  # halka_ciz: tavan x ayar (yuvarlama)
    return [(x * TAVAN * PARLAK + 5000) // 10000 for x in c]


def crc16(b):
    c = 0xFFFF
    for x in b:
        c ^= x << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    return c


def tanima(k):
    print("1. tanınma, selamlama, okuma, arka plan yalnız tanınmış figürler için")
    k.sifirla()
    out, err = k.kos(["#durum", "#bosta", "#durum"])
    dene("BOSTA 0" in err and not isler(err) and not any(s.startswith("ADAY") for s in err),
         "tanınmış figür yokken arka plan üretti")
    out, err = k.kos(["#etiket koy 8", "#sonra 400 #halka", "#bekle 60000", "#etiket kaldir", "#bekle 4000", "#durum"])
    ii = isler(err)  # boşta (5 s sonra) arka plan başlar
    dene("[Merhaba, şimdi sana Elsa'nın hikâyesini okuyacağım.]" in out, "Elsa selamı yok")
    dene("(yeni oyuncak tanındı: Elsa" in out, "Elsa tanınmadı")
    ok = okumalar(out)
    dene(ok and ok[-1][0] == ok[-1][1] and not ok[-1][2], f"hikâye sonuna kadar okunmadı: {ok}")
    hd = halka_d(err)
    sira = ["dolma -", "okuma 0/35 -", "hazirlik -", "okuma 35/35 -", "oyuncak -", "bosta -"]
    i = 0
    for h in hd:
        if i < len(sira) and h == sira[i]:
            i += 1
    dene(i == len(sira), f"halka sırası {hd} (beklenen alt dizi {sira})")
    ilerleme = [int(h.split()[1].split("/")[0]) for h in hd if h.startswith("okuma ")]
    dene(ilerleme == sorted(ilerleme) and len(set(ilerleme)) > 5, f"ilerleme cümle cümle artmadı: {ilerleme}")
    kare = [s for s in err if s.startswith("HALKA dolma")]
    if dene(kare, "dolma karesi yok"):
        lr = [list(map(int, x.split(","))) for x in kare[0].split("|")[3].split()]
        yanan = [c for c in lr if any(c)]
        dene(0 < len(yanan) < 35 and all(c == kisik(renk(7)) for c in yanan), f"dolma: Elsa rengi değil {lr[:3]}")
        dene("0 hata" in kare[0], "RMT bit zamanlaması")
    dene(durum(err)[-1][5] == 1 << 7, f"sahip maskesi {durum(err)}")
    out, err = k.kos(["#bosta", "#durum"])
    ii += isler(err)
    dene(len(ii) == 2 and all(x[2] == "7" for x in ii), f"arka plan: {[(x[2], x[3]) for x in ii]} (yalnız Elsa, 2)")
    dene(durum(err)[-1][0] == 2, "hazır 2 değil")
    k.sakla("elsa2")
    out, err = k.kos(["#etiket koy 8", "#bekle 60000"])
    cal = [i for i, s in enumerate(err) if s.startswith("CALINDI 7")]
    aday = [i for i, s in enumerate(err) if s.startswith("ADAY")]
    dene(cal and (not aday or cal[0] < aday[0]), "yeniden başlatınca hazır hikâye okunmadı")
    dene("Senin için yeni bir hikâye" not in out, "hazır varken canlı yazıldı")
    dene(okumalar(out) and okumalar(out)[-1][0] == okumalar(out)[-1][1], "hazır hikâye okunmadı")
    print("  Elsa tanındı, okundu; arka plan yalnız Elsa için 2 hikâye; hazır hikâye beklemeden okundu")


def cekilince(k):
    print("2. oyuncak çekilince: cümle sonunda / hemen / bitir")
    sonuc = {}
    for ayar in (0, 1, 2):
        k.geri("elsa2")
        k.nvs(cekil=ayar)
        out, err = k.kos(["#etiket koy 8", "#sonra 9700 #etiket kaldir", "#bekle 60000"])
        ok = okumalar(out)
        sonuc[ayar] = ok[-1] if ok else None
        dene("(oyuncak kalktı" in out, f"ayar {ayar}: kalkış görülmedi")
        dene(halka_d(err)[-1] == "bosta -", f"ayar {ayar}: halka boşta değil {halka_d(err)[-3:]}")
    c, h, b = sonuc[0], sonuc[1], sonuc[2]
    dene(h and h[2] and h[3] and c and c[2] and not c[3] and c[0] == h[0] + 1,
         f"cümle sonunda {c} / hemen {h}: hemen cümle ortasında, cümle sonunda bir sonraki cümlenin başında")
    dene(b and not b[2] and b[0] == b[1], f"bitir: {b}")
    print(f"  aynı hikâye, aynı anda: hemen {h[0]}. cümlede, cümle sonunda {c[0]}. cümleden önce, bitir {b[0]}/{b[1]}")


def sesli(k):
    print("3. sesli komutlar")
    k.geri("elsa2")
    satir = ["#etiket koy 8", "#sonra 7000 #w uyandirma", "#sonra 7500 #w dur", "#bekle 9000", "#durum",
             "#w devam", "#bekle 60000", "#w bir_daha", "#sonra 4000 #w sesi_ac", "#sonra 5000 #w sesi_kis",
             "#bekle 60000", "#w baska", "#bekle 60000", "#etiket kaldir", "#bekle 3000", "#w baska", "#bekle 9000",
             "#w uyandirma", "#bekle 6000"]
    out, err = k.kos(satir)
    ok = okumalar(out)
    hd = halka_d(err)
    dene(any("dinle" in h for h in hd) and any("onay" in h for h in hd), "dinle/onay halkası")
    if dene(len(ok) >= 4, f"okumalar {ok}"):
        dur, devam, tekrar, baska = ok[0], ok[1], ok[2], ok[3]
        dene(dur[2] and dur[0] < dur[1], f"dur: {dur}")
        dene(f"(devam: {dur[0] + 1}. cümleden)" in out and devam[0] == devam[1], f"devam: {devam}")
        dene("(bir daha: baştan)" in out and tekrar[0] == tekrar[1] == dur[1], f"bir daha: {tekrar} ({dur[1]} cümle)")
        dene(not baska[2], f"başka: {baska}")
    cal = [s for s in err if s.startswith("CALINDI")]
    dene(len(cal) == 2 and cal[0] != cal[1], "başka: aynı oyuncağın ikinci hazır hikâyesi okunmadı")
    sv = re.findall(r"ses seviyesi (\d)/7 \(en çok \d; kazanç", out)
    dene(sv[:2] == ["6", "5"], f"sesi aç / kıs: {sv}")
    dene(any(h.endswith(" ses") for h in hd), "ses göstergesi halkada yok")
    dene(ok[2][0] == ok[2][1], "ses aç/kıs okumayı kesti")
    dene("[Önce bir oyuncağını standa koy.]" in out, "oyuncak yokken başka")
    dene(out.count("(sesli komut: anlaşılmadı)") == 1 and any("anlasilmadi" in h for h in hd), "komutsuz uyandırma")
    # canlı üretim sırasında dur: üretim durur, hikâye okunmaz
    k.sifirla()
    out, err = k.kos(["#etiket koy 6", "#sonra 5600 #w dur", "#bekle 20000"])
    dene("(durduruldu)" in out and not okumalar(out)[1:], f"canlı üretim durmadı {okumalar(out)}")
    print("  dur/devam/bir daha/başka, ses aç/kıs, oyuncaksız komut, anlaşılmadı, üretim sırasında dur tamam")


def etiket(k):
    print("4. etiket: UID tablosu, bilinmeyen etiket")
    k.sifirla()
    out, err = k.kos(["#etiket koy uid 04A1B2C3", "#bekle 300", "#etiket kaldir", "#bekle 2000",
                      "#etiket koy uid DEADBEEF", "#bekle 2000", "#etiket koy bos", "#bekle 2000"])
    dene("(stand: etiket 04A1B2C3, nfc_no 1 UID tablosundan)" in out and "[oyuncak: Niloya]" in out, "UID tablosu")
    dene(out.count("bilinmeyen etiket") == 2, "bilinmeyen etiketler")
    dene(sum("anlasilmadi" in h for h in halka_d(err)) >= 2, "bilinmeyen etikette turuncu yok")
    print("  UID tablosu, bilinmeyen etiket tamam")


def gece(k):
    print("5. gece figürü (Ay Dede): ninni, zamanlayıcı, sönme, kapanma, uyanma")
    k.sifirla()
    k.nvs(uyku_dk=10)
    out, err = k.kos(["#etiket koy 12", "#bekle 760000", "#durum", "#bosta", "#etiket kaldir", "#bekle 3000",
                      "#etiket koy 8", "#bekle 3000", "#durum"])
    dene("[İyi geceler, şimdi sana bir ninni söyleyeceğim.]" in out, "ninni selamı")
    ninni = re.findall(r"=== Ay Dede \| yerleşik metin (\d+)/(\d+) ===", out)
    dene(len(ninni) >= 5 and [int(a) for a, _ in ninni[:3]] == [1, 2, 3], f"ninniler art arda: {ninni[:5]}")
    dene("(uyku modu: ninniler 10 dk, müzik kutusu açık)" in out, "uyku modu")
    i_son, i_kap = out.find("zamanlayıcı doldu"), out.find("(uyku: kapandı")
    dene(0 < i_son < i_kap, "zamanlayıcı -> kapandı sırası")
    hd = halka_d(err)
    dene("gece -" in hd and "kapali -" in hd, f"halka gece/kapalı: {hd[:8]}")
    d = durum(err)
    dene(d and d[0][6] == 3 and d[0][5] & (1 << 11), f"uyku kapalı ve Ay Dede tanınmış: {d}")
    dene(any(s.startswith("UYKU ") for s in err), "kapalıyken hafif uyku yok")
    dene("BOSTA 0" in err, "Ay Dede (modelde yok) için arka plan üretti")
    dene("(uyku: uyandı)" in out and "[oyuncak: Elsa]" in out and d[-1][6] == 0, "başka oyuncakla uyanmadı")
    print(f"  {len(ninni)} ninni, zamanlayıcı -> 60 sn sönme -> kapalı (hafif uyku) -> Elsa ile uyandı")


def ayar(k):
    print("6. ayar kartı: Wi-Fi, ayar sayfası, oyuncak tanıt, sil, kalıcılık")
    k.sifirla()
    etiket_yol = os.path.join(k.d, "etiket.bin")
    if os.path.exists(etiket_yol):
        os.remove(etiket_yol)
    satir = ["sahip +8", "#bosta", "#etiket koy 200", "#bekle 10000", "#bosta 1", "#http GET /", "#http GET /generate_204",
             "#http GET /hotspot-detect.html", "#http GET /durum",
             "#http POST /kaydet ad=%C3%87a%C4%9Fr%C4%B1+Emre&ses_maks=4&uyku_dk=30&parlaklik=25&cekilince=1&nefes=0"
             "&arka_goster=1&muzik=0",
             "#http POST /kaydet ad=Emre123", "#http POST /kaydet ad=Abcdefghijklmnoprstuv", "#http POST /kaydet uyku_dk=15",
             "#http POST /tanit no=3", "#etiket kaldir", "#bekle 3000", f"#etiket dosya {etiket_yol}", "#bekle 4000",
             "#http GET /durum", "#http POST /sil onay=1&unut=0", "#http POST /bitir", "#bekle 2000", "#durum"]
    out, err = k.kos(satir)
    ap = [s for s in err if s.startswith("WIFI ap Masalci")]
    if dene(ap, "erişim noktası açılmadı"):
        _, _, ssid, sifre = ap[0].split()[:4]
        dene(re.fullmatch(r"Masalci-Ayar-[0-9A-F]{4}", ssid) and re.fullmatch(r"\d{8}", sifre), f"{ssid} {sifre}")
        sozcuk = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        dene(", ".join(sozcuk[int(c)] for c in sifre) in out, "şifre sesli söylenmedi")
    dene("HALKA_D ayar -" in err, "turkuaz halka")
    dene("BOSTA 0" in err and len(isler(err)) == 2, "ayar modunda arka plan üretti (ya da önce üretmedi)")
    h = http(err)
    dene(h[0][0] == 200 and h[0][1].startswith("<html"), f"sayfa {h[0]}")
    dene(h[1][0] == 302 and h[1][2] == "http://192.168.4.1/" and h[2][0] == 302, "captive yönlendirme")
    j = json.loads(h[3][1])
    dene(len(j["figurler"]) == 12 and j["kalan_sn"] > 500 and j["ayar"]["ses_maks"] == 7, f"durum {h[3][1][:120]}")
    dene(h[4][0] == 200 and '"tamam":true' in h[4][1], f"kaydet {h[4]}")
    dene(h[5][0] == 400 and "harf" in h[5][1], f"geçersiz ad {h[5]}")
    dene(h[6][0] == 400 and "20 harf" in h[6][1], f"uzun ad {h[6]}")
    dene(h[7][0] == 400 and "10, 20 ya da 30" in h[7][1], f"uyku {h[7]}")
    dene(h[8][0] == 200, f"tanıt {h[8]}")
    dene("[ayar] oyuncak tanıt: Tamam: bu etiket artık Pepee." in out, "tanıt yazılmadı")
    with open(etiket_yol, "rb") as f:
        b = f.read()
    kayit = b[8 + 16:8 + 24]
    dene(kayit[:4] == b"EKO\x01" and kayit[4] | kayit[5] << 8 == 3 and crc16(kayit[:6]) == kayit[6] | kayit[7] << 8,
         f"etiket belleği: {kayit.hex()}")
    j = json.loads(h[9][1])
    dene(j["tanit"]["durum"] == 2 and j["tanit"]["tamam"] == 1 and j["ayar"]["ad"] == "Çağrı Emre", f"durum {j['tanit']}")
    dene([f["sahip"] for f in j["figurler"]][2] == 1, "tanıtılan Pepee tanınmış sayılmadı")
    dene(h[10][0] == 200 and '"silinen":2' in h[10][1], f"sil {h[10]}")
    dene([f["hazir"] for f in j["figurler"]][7] == 2, "durum: Elsa'nın 2 hazır hikâyesi görünmedi")
    dene("[ayar modu kapandı: sayfadan bitirildi]" in out and "WIFI ap kapandi" in err, "bitir")
    dene(durum(err)[-1][7] == 0, "ayar modu kapanmadı")
    # kalıcılık: ad, ses en çok 4, Pepee etiketi dosyadan
    out, err = k.kos([f"#etiket dosya {etiket_yol}", "#bekle 60000"])
    dene("ayarlar: ad \"Çağrı Emre\", uyku 30 dk, parlaklık 25, çekilince hemen dur, müzik kutusu kapalı" in out,
         "ayarlar kalıcı değil")
    dene("ses seviyesi 4/7 (en çok 4)" in out, "ses seviyesi en yüksek sese inmedi")
    dene("[Merhaba Çağrı Emre, şimdi sana Pepee'nin hikâyesini okuyacağım.]" in out, "selamda ad yok")
    # kart çekilince kapanır; 10 dakika; Wi-Fi açılamazsa hata
    out, err = k.kos(["#etiket koy 200", "#bekle 9000", "#etiket kaldir", "#bekle 3000", "#durum"])
    dene("[ayar modu kapandı: ayar kartı kaldırıldı]" in out and durum(err)[-1][7] == 0, "kart çekilince kapanmadı")
    out, err = k.kos(["#etiket koy 200", "#bekle 610000", "#durum"])
    dene("[ayar modu kapandı: 10 dakika doldu]" in out, "10 dakikada kapanmadı")
    out, err = k.kos(["#etiket koy 200", "#bekle 5000", "#durum"], {"KART_WIFI_HATA": "1"})
    dene("HATA: Wi-Fi erişim noktası açılamadı" in out and "HALKA_D hata -" in err, "Wi-Fi hatası")
    print("  erişim noktası, şifre, captive, form, tanıt (etiket dosyası), sil, bitir, kalıcılık, kapanmalar tamam")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dizin")
    a = ap.parse_args()
    d = a.dizin or tempfile.mkdtemp(prefix="urun_akis_")
    os.makedirs(d, exist_ok=True)
    k = Kart(derle(d), d)
    tanima(k)
    cekilince(k)
    sesli(k)
    etiket(k)
    gece(k)
    ayar(k)
    print(f"\nurun_akis_test.py: {'HATA ' + str(len(hatalar)) if hatalar else 'hepsi geçti'} ({d})")
    if not a.dizin and not hatalar:
        shutil.rmtree(d, ignore_errors=True)
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
