"""Ürün akışının kartın kendi koduyla (hikaye_oyuncak.ino, sahte ESP32 başlıklarıyla: tools/kart_pc) bilgisayarda
denemesi: stand (taslak NFC okuyucu, etiket kaydı), tanınmış figürler, selamlama, okuma ve halka, oyuncak çekilince
davranışları, sesli komutlar (taklit), gece figürü (ninni, uyku zamanlayıcısı, kapanma), ayar kartı (Wi-Fi, ayar
sayfası istekleri, form doğrulaması, oyuncak tanıt, hikâyeleri sil, kalıcılık).

Saat taklittir (KART_SAAT=sahte): okuma süresi harf başına 40 ms, üretim her saat okumasında 50 µs; aynı girdi her
seferinde aynı çıktıyı verir. Kuyruk K=2 aday, figür başına en çok 2 hikâye (hızlı).

  1. tanınma:   oyuncak yokken de arka plan yazar; hazır yokken Pamuk Prenses (nfc_no 13) konunca halka dolar,
                selamlanır, canlı okunur (yazdıkça, halka ilerlemesi); tanınır (NVS); arka plan ilk açılıştan bütün
                figürlere yazar, tanınan Pamuk Prenses önce; yeniden başlatınca hazır hikâye üretmeden okunur.
  2. çekilince: aynı hikâye "cümle sonunda dur" / "hemen dur" / "hikâyeyi bitir" ayarlarıyla.
  3. sesli:     uyandırma (dinle), dur (kaldığı cümle), devam, bir daha, başka, sesi aç/kıs (okurken), oyuncak yokken,
                komutsuz uyandırma (anlaşılmadı), canlı okurken dur (sessiz tamamlama) / devam / başka.
  4. etiket:    UID tablosuna düşme, bilinmeyen etiket, halka karesinin RMT bitlerinden çözümü (renk, tavan).
  5. gece:      Ay Dede: ninni selamı, yerleşik ninniler art arda, zamanlayıcı -> sönme -> kapanma (hafif uyku),
                başka oyuncakla uyanma; gece figürü için arka planda üretim yok.
  6. ayar:      ayar kartı: WPA2 erişim noktası + söylenen şifre, captive yönlendirme, /durum, /kaydet (geçerli ve
                geçersiz), oyuncak tanıt (etiket belleği dosyası), /sil, /bitir; kart çekilince telefon bağlanmazsa
                3 dk'da kapanma, 10 dk, Wi-Fi hatası; ayarların kalıcılığı (selamda ad).
  7. dokunma:   ayar kartına Wi-Fi NDEF'i yazılır (bağımsız çözücüyle: ağ adı, şifre, MAC), kayıt sayfa 36'da; kart
                yeni düzeniyle yine ayar kartı tanınır, her oturumda yeni şifre; kart kaldırılınca açık kalır; telefon
                ayrılınca 2 dk'da kapanır; kilitli kartta eski yol (sesli şifre).
  8. zaman:     /saat, alarm/yatma/gece kilidi/okunuş/mesaj formu (geçerli ve geçersiz), gün doğumu ışığı, alarm
                (günaydın + ad okunuşu + mesajdaki rakamlar yazıyla), oyuncak koyunca susma ve hikâye, sürpriz mesaj
                bir kez, selam çeşitleri, yatma hatırlatması, gece kilidi (hikâye yok, Ay Dede serbest), alarm günü
                değilse çalmama.
  9. alarm sesi: ayar sayfasının kodlayıcısının paketi yüklenir (/alarm_ses), bozuk paket reddedilir ve silinir,
                dinle/dene, ad dinle; açılışta bölümden okunur, alarmda yüklenen ses çalar.

Kullanım: .venv/bin/python firmware/hikaye_oyuncak/tools/urun_akis_test.py [--dizin D]   (çıkış kodu: hata varsa 1)
Model: HIKAYE_MODEL (dizin; yoksa modeller/c3ft_urun13, o da yoksa modeller/c3ft_karma). Figürler: generated/istemler.h ve
data/figur_donanim.json'un üründe kalan figürleri (generated/figur_donanim.h sırası).
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
sys.path.insert(0, TOOLS)
from kuyruk_test import MODEL as _MODEL_DIZIN, istemler_tablosu  # noqa: E402

MODEL = os.path.join(_MODEL_DIZIN, "model.bin")
with open(os.path.join(ROOT, "data", "figur_donanim.json"), encoding="utf-8") as _f:
    DONANIM = json.load(_f)
DON = [f for f in DONANIM["figurler"] if not f.get("cikarildi")]  # generated/figur_donanim.h sırası (d)
N_FIGUR, _, FIGUR_AD = istemler_tablosu()


def don_d(kimlik):
    return next(i for i, f in enumerate(DON) if f["kimlik"] == kimlik)


# denemelerin figürleri: PP (Pamuk Prenses) hazır/canlı okuma ve sesli komutlar, PN (Pinokyo) canlı üretim ve tanıt
PP, PN, KEL = DON[don_d("pamuk_prenses")], DON[don_d("pinokyo")], DON[don_d("keloglan")]
PP_F = FIGUR_AD.index(PP["ad"])  # modeldeki figür numarası (istemler.h)
TAVAN, PARLAK = 25, 60  # HALKA_PARLAKLIK_SINIR, varsayılan ayar
N_LED = 16  # donanim.h HALKA_LED_SAYISI

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
                   KART_ALARM=os.path.join(self.d, "alarm.bin"),
                   KART_SAAT="sahte")
        env.update(ek_env or {})
        r = subprocess.run([self.kart], input="".join(s + "\n" for s in satirlar), capture_output=True, text=True,
                           env=env, timeout=900)
        if r.returncode:
            print(r.stdout[-3000:], r.stderr[-3000:])
            raise SystemExit(f"kart_pc çıkış kodu {r.returncode}")
        return r.stdout, r.stderr.splitlines()

    def sifirla(self):
        for ad in ("kuyruk.bin", "nvs.txt", "alarm.bin"):
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


def renk(f):
    h = f["renk"].lstrip("#")
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
    print("1. ilk açılış: canlı okuma (yazdıkça), tanınma, arka plan bütün figürler için (tanınmışlar önce)")
    k.sifirla()
    out, err = k.kos(["#durum", "#bosta 1", "#durum"])
    dene(len(isler(err)) == 1 and durum(err)[-1][0] == 1, "ilk açılışta (oyuncak yokken) arka plan üretmedi")
    k.sifirla()
    out, err = k.kos([f"#etiket koy {PP['nfc_no']}", "#sonra 400 #halka", "#bekle 60000", "#etiket kaldir", "#bekle 4000",
                      "#durum"])
    ii = isler(err)  # boşta (5 s sonra) arka plan başlar
    dene("[Merhaba, şimdi sana Pamuk Prenses'in hikâyesini okuyacağım.]" in out, "Pamuk Prenses selamı yok")
    dene("canlı okuma (yazdıkça)" in out and "biraz bekler" not in out, "hazır yokken canlı okuma olmadı")
    dene("(yeni oyuncak tanındı: Pamuk Prenses" in out, "Pamuk Prenses tanınmadı")
    ok = okumalar(out)
    dene(ok and ok[-1][0] == ok[-1][1] and not ok[-1][2], f"hikâye sonuna kadar okunmadı: {ok}")
    hd = halka_d(err)
    sira = ["dolma -", f"okuma 0/{N_LED} -", "hazirlik -", f"okuma 0/{N_LED} -", f"okuma {N_LED}/{N_LED} -", "oyuncak -",
            "bosta -"]
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
        dene(0 < len(yanan) < N_LED and all(c == kisik(renk(PP)) for c in yanan),
             f"dolma: Pamuk Prenses rengi değil {lr[:3]}")
        dene("0 hata" in kare[0], "RMT bit zamanlaması")
    dene(durum(err)[-1][5] == 1 << don_d("pamuk_prenses"), f"sahip maskesi {durum(err)}")
    out, err = k.kos(["#bosta", "#durum"])
    ii += isler(err)
    dene(len(ii) == 2 * N_FIGUR and [x[2] for x in ii[:2]] == [str(PP_F)] * 2,
         f"arka plan: {[(x[2], x[3]) for x in ii]} (önce Pamuk Prenses 2, sonra {N_FIGUR} figüre 2'şer)")
    dene(durum(err)[-1][0] == 2 * N_FIGUR, f"hazır {2 * N_FIGUR} değil")
    k.sakla("pp2")
    out, err = k.kos([f"#etiket koy {PP['nfc_no']}", "#bekle 60000"])
    cal = [i for i, s in enumerate(err) if s.startswith(f"CALINDI {PP_F} ")]
    aday = [i for i, s in enumerate(err) if s.startswith("ADAY")]
    dene(cal and (not aday or cal[0] < aday[0]), "yeniden başlatınca hazır hikâye okunmadı")
    dene("canlı okuma (yazdıkça)" not in out, "hazır varken canlı yazıldı")
    dene(okumalar(out) and okumalar(out)[-1][0] == okumalar(out)[-1][1], "hazır hikâye okunmadı")
    print("  oyuncak yokken de arka plan yazar; Pamuk Prenses canlı okundu (yazdıkça), tanındı; arka plan önce o, sonra"
          " hepsine 2'şer; hazır hikâye beklemeden okundu")


def cekilince(k):
    print("2. oyuncak çekilince: cümle sonunda / hemen / bitir")
    sonuc = {}
    for ayar in (0, 1, 2):
        k.geri("pp2")
        k.nvs(cekil=ayar)
        out, err = k.kos([f"#etiket koy {PP['nfc_no']}", "#sonra 9700 #etiket kaldir", "#bekle 60000"])
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
    k.geri("pp2")
    satir = [f"#etiket koy {PP['nfc_no']}", "#sonra 7000 #w uyandirma", "#sonra 7500 #w dur", "#bekle 9000", "#durum",
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
    # canlı okurken dur: anlatım susar, hikâye sessizce tamamlanır; devam kaldığı cümleden; başka: üretim bırakılır
    k.sifirla()
    out, err = k.kos([f"#etiket koy {PN['nfc_no']}", "#sonra 9000 #w dur", "#bekle 30000", "#w devam", "#bekle 60000"])
    ok = okumalar(out)
    dene("sustu; hikâye sessizce tamamlanıyor" in out and "(durduruldu)" not in out and len(ok) == 2 and ok[0][2]
         and f"(devam: {ok[0][0] + 1}. cümleden)" in out and ok[1][0] == ok[1][1] == ok[0][1],
         f"canlı okurken dur / devam {ok}")
    k.sifirla()
    out, err = k.kos([f"#etiket koy {PN['nfc_no']}", "#sonra 9000 #w baska", "#bekle 60000"])
    dene("(durduruldu)" in out and out.count("canlı okuma (yazdıkça)") == 2, "canlı okurken başka: yeni hikâye başlamadı")
    print("  dur/devam/bir daha/başka, ses aç/kıs, oyuncaksız komut, anlaşılmadı, üretim sırasında dur tamam")


def etiket(k):
    print("4. etiket: UID tablosu, bilinmeyen etiket")
    k.sifirla()
    out, err = k.kos(["#etiket koy uid 04A1B2C3", "#bekle 300", "#etiket kaldir", "#bekle 2000",
                      "#etiket koy uid DEADBEEF", "#bekle 2000", "#etiket koy bos", "#bekle 2000"])
    dene(f"(stand: etiket 04A1B2C3, nfc_no {KEL['nfc_no']} UID tablosundan)" in out and "[oyuncak: Keloğlan]" in out,
         "UID tablosu (nfc.h NFC_TABLO: Keloğlan)")
    dene(out.count("bilinmeyen etiket") == 2, "bilinmeyen etiketler")
    dene(sum("anlasilmadi" in h for h in halka_d(err)) >= 2, "bilinmeyen etikette turuncu yok")
    print("  UID tablosu, bilinmeyen etiket tamam")


def gece(k):
    print("5. gece figürü (Ay Dede): ninni, zamanlayıcı, sönme, kapanma, uyanma")
    k.sifirla()
    k.nvs(uyku_dk=10)
    out, err = k.kos(["#etiket koy 12", "#bekle 760000", "#durum", "#bosta", "#etiket kaldir", "#bekle 3000",
                      f"#etiket koy {PP['nfc_no']}", "#bekle 3000", "#durum"])
    dene("[İyi geceler, şimdi sana bir ninni söyleyeceğim.]" in out, "ninni selamı")
    ninni = re.findall(r"=== Ay Dede \| yerleşik metin (\d+)/(\d+) ===", out)
    dene(len(ninni) >= 5 and [int(a) for a, _ in ninni[:3]] == [1, 2, 3], f"ninniler art arda: {ninni[:5]}")
    dene("(uyku modu: ninniler 10 dk, müzik kutusu açık)" in out, "uyku modu")
    i_son, i_kap = out.find("zamanlayıcı doldu"), out.find("(uyku: kapandı")
    dene(0 < i_son < i_kap, "zamanlayıcı -> kapandı sırası")
    hd = halka_d(err)
    dene("gece -" in hd and "kapali -" in hd, f"halka gece/kapalı: {hd[:8]}")
    d = durum(err)
    dene(d and d[0][6] == 3 and d[0][5] & (1 << don_d("gece")), f"uyku kapalı ve Ay Dede tanınmış: {d}")
    dene(any(s.startswith("UYKU ") for s in err), "kapalıyken hafif uyku yok")
    dene("BOSTA 0" in err, "Ay Dede (modelde yok) için arka plan üretti")
    dene("(uyku: uyandı)" in out and "[oyuncak: Pamuk Prenses]" in out and d[-1][6] == 0, "başka oyuncakla uyanmadı")
    print(f"  {len(ninni)} ninni, zamanlayıcı -> 60 sn sönme -> kapalı (hafif uyku) -> Pamuk Prenses ile uyandı")


def ayar(k):
    print("6. ayar kartı: Wi-Fi, ayar sayfası, oyuncak tanıt, sil, kalıcılık")
    k.sifirla()
    etiket_yol = os.path.join(k.d, "etiket.bin")
    if os.path.exists(etiket_yol):
        os.remove(etiket_yol)
    satir = [f"sahip +{PP['nfc_no']}", "#bosta", "#etiket koy 200", "#bekle 10000", "#bosta 1", "#http GET /", "#http GET /generate_204",
             "#http GET /hotspot-detect.html", "#http GET /durum",
             "#http POST /kaydet ad=%C3%87a%C4%9Fr%C4%B1+Emre&ses_maks=4&uyku_dk=30&parlaklik=25&cekilince=1&nefes=0"
             "&arka_goster=1&muzik=0",
             "#http POST /kaydet ad=Emre123", "#http POST /kaydet ad=Abcdefghijklmnoprstuv", "#http POST /kaydet uyku_dk=15",
             f"#http POST /tanit no={PN['nfc_no']}", "#etiket kaldir", "#bekle 3000", f"#etiket dosya {etiket_yol}", "#bekle 4000",
             "#http GET /durum", "#http POST /sil onay=1&unut=0", "#http POST /bitir", "#bekle 2000", "#durum"]
    out, err = k.kos(satir)
    ap = [s for s in err if s.startswith("WIFI ap Masalci")]
    if dene(ap, "erişim noktası açılmadı"):
        _, _, ssid, sifre = ap[0].split()[:4]
        dene(re.fullmatch(r"Masalci-Ayar-[0-9A-F]{4}", ssid) and re.fullmatch(r"\d{8}", sifre), f"{ssid} {sifre}")
        sozcuk = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        dene(", ".join(sozcuk[int(c)] for c in sifre) in out, "şifre sesli söylenmedi")
    dene("HALKA_D ayar -" in err, "turkuaz halka")
    dene("BOSTA 0" in err and len(isler(err)) == 2 * N_FIGUR, "ayar modunda arka plan üretti (ya da önce üretmedi)")
    h = http(err)
    dene(h[0][0] == 200 and h[0][1].startswith("<html"), f"sayfa {h[0]}")
    dene(h[1][0] == 302 and h[1][2] == "http://192.168.4.1/" and h[2][0] == 302, "captive yönlendirme")
    j = json.loads(h[3][1])
    dene(len(j["figurler"]) == len(DON) and j["kalan_sn"] > 500 and j["ayar"]["ses_maks"] == 7, f"durum {h[3][1][:120]}")
    dene(h[4][0] == 200 and '"tamam":true' in h[4][1], f"kaydet {h[4]}")
    dene(h[5][0] == 400 and "harf" in h[5][1], f"geçersiz ad {h[5]}")
    dene(h[6][0] == 400 and "20 harf" in h[6][1], f"uzun ad {h[6]}")
    dene(h[7][0] == 400 and "10, 20 ya da 30" in h[7][1], f"uyku {h[7]}")
    dene(h[8][0] == 200, f"tanıt {h[8]}")
    dene("[ayar] oyuncak tanıt: Tamam: bu etiket artık Pinokyo." in out, "tanıt yazılmadı")
    with open(etiket_yol, "rb") as f:
        b = f.read()
    kayit = b[8 + 16:8 + 24]
    dene(kayit[:4] == b"EKO\x01" and kayit[4] | kayit[5] << 8 == PN["nfc_no"] and crc16(kayit[:6]) == kayit[6] | kayit[7] << 8,
         f"etiket belleği: {kayit.hex()}")
    j = json.loads(h[9][1])
    dene(j["tanit"]["durum"] == 2 and j["tanit"]["tamam"] == 1 and j["ayar"]["ad"] == "Çağrı Emre", f"durum {j['tanit']}")
    dene([f["sahip"] for f in j["figurler"]][don_d("pinokyo")] == 1, "tanıtılan Pinokyo tanınmış sayılmadı")
    dene(h[10][0] == 200 and '"silinen":2' in h[10][1], f"sil {h[10]}")
    dene([f["hazir"] for f in j["figurler"]][don_d("pamuk_prenses")] == 2, "durum: Pamuk Prenses'in 2 hazır hikâyesi görünmedi")
    dene("[ayar modu kapandı: sayfadan bitirildi]" in out and "WIFI ap kapandi" in err, "bitir")
    dene(durum(err)[-1][7] == 0, "ayar modu kapanmadı")
    # kalıcılık: ad, ses en çok 4, Pinokyo etiketi dosyadan
    out, err = k.kos([f"#etiket dosya {etiket_yol}", "#bekle 60000"])
    dene("ayarlar: ad \"Çağrı Emre\", uyku 30 dk, parlaklık 25, çekilince hemen dur, müzik kutusu kapalı" in out,
         "ayarlar kalıcı değil")
    dene("ses seviyesi 4/7 (en çok 4)" in out, "ses seviyesi en yüksek sese inmedi")
    dene("[Merhaba Çağrı Emre, şimdi sana Pinokyo'nun hikâyesini okuyacağım.]" in out, "selamda ad yok")
    # kart çekilince telefon bağlanmazsa 3 dakikada kapanır; 10 dakika; Wi-Fi açılamazsa hata
    out, err = k.kos(["#etiket koy 200", "#bekle 9000", "#etiket kaldir", "#bekle 3000", "#durum", "#bekle 180000", "#durum"])
    d = durum(err)
    dene("[ayar modu] ayar kartı kaldırıldı: telefon bağlanana kadar açık" in out and d[0][7] == 1, "kart çekilince hemen kapandı")
    dene("[ayar modu kapandı: ayar kartı kaldırıldı, telefon bağlanmadı]" in out and d[-1][7] == 0,
         "kart çekilip telefon bağlanmayınca 3 dakikada kapanmadı")
    out, err = k.kos(["#etiket koy 200", "#bekle 610000", "#durum"])
    dene("[ayar modu kapandı: 10 dakika doldu]" in out, "10 dakikada kapanmadı")
    out, err = k.kos(["#etiket koy 200", "#bekle 5000", "#durum"], {"KART_WIFI_HATA": "1"})
    dene("HATA: Wi-Fi erişim noktası açılamadı" in out and "HALKA_D hata -" in err, "Wi-Fi hatası")
    print("  erişim noktası, şifre, captive, form, tanıt (etiket dosyası), sil, bitir, kalıcılık, kapanmalar tamam")


# ---- 7. telefonla dokunma ----
sys.path.insert(0, TOOLS)
import ndef_test  # noqa: E402  (bağımsız NDEF / WSC çözücü)

NFC_SAYFA = 45


def ayar_karti_dosyasi(yol):
    """Ayar kartı (nfc_no 200) etiket belleği: kart_pc "#etiket dosya" biçimi (uid_n, uid[7], 45 sayfa)."""
    uid = bytes([0x04, 0xA7, 0x4E, 0x00, 0xC8, 0x5A, 0x81])
    b = bytearray(NFC_SAYFA * 4)
    b[0:7] = uid
    b[12:16] = bytes([0xE1, 0x10, 0x12, 0x00])
    kayit = b"EKO\x01" + (200).to_bytes(2, "little")
    kayit += crc16(kayit).to_bytes(2, "little")
    b[16:24] = kayit
    with open(yol, "wb") as f:
        f.write(bytes([7]) + uid + bytes(b))


def etiket_bellek(yol):
    with open(yol, "rb") as f:
        return f.read()[8:]


def ndef_denetle(bellek, ssid, sifre):
    mesaj, son, _ = ndef_test.tlv_coz(bellek[16:16 + 128])
    if not dene(mesaj is not None and son, "kartta NDEF yok"):
        return
    _, tur, yuk = ndef_test.ndef_coz(mesaj)
    kim = dict(ndef_test.wsc_coz(dict(ndef_test.wsc_coz(yuk))[0x100E]))
    dene(tur == b"application/vnd.wfa.wsc" and kim[0x1045] == ssid.encode() and kim[0x1027] == sifre.encode(),
         f"karttaki Wi-Fi kaydı oturumla uyuşmuyor: {kim.get(0x1045)} {kim.get(0x1027)}")
    kayit = bellek[36 * 4:36 * 4 + 8]
    dene(kayit[:4] == b"EKO\x01" and kayit[4] | kayit[5] << 8 == 200 and crc16(kayit[:6]) == kayit[6] | kayit[7] << 8,
         f"sayfa 36'da ayar kartı kaydı yok: {kayit.hex()}")


def dokunma(k):
    print("7. ayar kartı: telefonla dokunma (NDEF Wi-Fi), kart kaldırılınca açık kalma, kapanmalar")
    k.sifirla()
    yol = os.path.join(k.d, "ayar_karti.bin")
    ayar_karti_dosyasi(yol)
    sifreler = []
    for tur in range(2):  # 2. turda kart artık NDEF düzeninde: yine ayar kartı tanınmalı, şifre yenilenmeli
        out, err = k.kos([f"#etiket dosya {yol}", "#bekle 12000", "#http GET /durum", "#etiket kaldir", "#bekle 3000",
                          "#durum", "#bekle 125000", "#durum"])
        ap = [s.split() for s in err if s.startswith("WIFI ap Masalci")]
        if not dene(ap, f"{tur + 1}. tur: ayar modu açılmadı (kart tanınmadı)"):
            return
        ssid, sifre = ap[0][2], ap[0][3]
        sifreler.append(sifre)
        dene("[ayar modu] ayar kartına Wi-Fi bilgisi yazıldı: kartı telefona dokundurun" in out, f"{tur + 1}. tur: yazılmadı")
        dene("Ayar kartını telefonunun arkasına dokundur ya da telefonunla Masalcı Ayar ağına bağlan" in out,
             "dokunma yönergesi söylenmedi")
        ndef_denetle(etiket_bellek(yol), ssid, sifre)
        j = json.loads(http(err)[0][1])
        dene(j["kart_yazildi"] == 1, "durum: kart_yazildi değil")
        d = durum(err)
        dene(d[0][7] == 1, "kart kaldırılınca ayar modu kapandı")
        dene("[ayar modu kapandı: telefon ayrıldı]" in out and d[-1][7] == 0, "telefon ayrılınca 2 dakikada kapanmadı")
    # aynı açılışta iki oturum: şifre yenilenir (sahte esp_random her süreçte aynı diziyle başlar)
    out, err = k.kos(["#etiket koy 200", "#bekle 12000", "#http POST /bitir", "#bekle 3000", "#etiket kaldir", "#bekle 2000",
                      "#etiket koy 200", "#bekle 12000", "#http POST /bitir", "#bekle 3000"])
    ap = [s.split()[3] for s in err if s.startswith("WIFI ap Masalci")]
    dene(len(ap) == 2 and ap[0] != ap[1], f"her oturumda yeni şifre yazılmadı: {ap}")
    # telefon bağlıyken (istasyon sayısı) kart kaldırılsa da açık kalır
    out, err = k.kos(["#wifi istemci 1", "#etiket koy 200", "#bekle 12000", "#etiket kaldir", "#bekle 240000", "#durum",
                      "#wifi istemci 0", "#bekle 125000", "#durum"])
    d = durum(err)
    dene(d[0][7] == 1 and d[-1][7] == 0 and "[ayar modu kapandı: telefon ayrıldı]" in out,
         f"telefon bağlıyken açık kalma / ayrılınca kapanma: {d}")
    # kilitli kart: yazılamaz, eski yol (sesli şifre)
    out, err = k.kos(["#etiket koy 200", "#etiket kilitle", "#bekle 12000", "#http POST /bitir", "#bekle 2000"])
    dene("ayar kartına Wi-Fi bilgisi yazılamadı: yazılamadı (kilitli?)" in out and
         "Ayar modu açık. Telefonunla Masalcı Ayar ağına bağlan." in out, "kilitli kartta eski yol")
    print("  NDEF Wi-Fi kaydı (bağımsız çözücü), sayfa 36 kaydı, yeni düzenin tanınması, yeni şifre, açık kalma, "
          "kapanmalar, kilitli kart tamam")


# ---- 8. saat ve zamanlı işler ----
def epoch(yerel, tz_dk=180):
    import datetime as dt
    t = dt.datetime.strptime(yerel, "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone(dt.timedelta(minutes=tz_dk)))
    return int(t.timestamp())


def zaman(k):
    print("8. saat ve zamanlı işler: alarm, gün doğumu, sürpriz mesaj, selam çeşitleri, yatma vakti, gece kilidi")
    k.sifirla()
    from urllib.parse import quote
    form = ("ad=Emre&okunus=Emrecik&alarm_acik=1&alarm_saat=07:00&alarm_gunler=31&alarm_gunes=1&alarm_tur=0"
            f"&alarm_mesaj={quote('Bugün 2 kurabiye var, saat 8’de çıkıyoruz!')}&yatma_acik=1&yatma_saat=07:30"
            "&kilit=1&sabah_saat=08:00")
    out, err = k.kos([f"sahip +{PP['nfc_no']}", "#etiket koy 200", "#bekle 10000",
                      f"#http POST /saat t={epoch('2026-11-23 06:00:00')}&tz=180",  # pazartesi
                      f"#http POST /kaydet {form}", "#http GET /durum",
                      f"#http POST /surpriz mesaj={quote('Annen seni çok seviyor')}",
                      "#http POST /kaydet alarm_saat=25:00", "#http POST /kaydet alarm_mesaj=%3Cb%3E",
                      "#http POST /kaydet alarm_acik=1&alarm_gunler=0", "#http POST /kaydet kilit=1&sabah_saat=07:30",
                      "#http POST /saat t=12&tz=180", "#http POST /bitir", "#bekle 3000"])
    h = http(err)
    dene(h[0][0] == 200 and h[1][0] == 200, f"saat/kaydet {h[:2]}")
    j = json.loads(h[2][1])
    a = j["ayar"]
    dene(j["saat"]["gecerli"] == 1 and j["saat"]["simdi"] == "06:00" and j["saat"]["gun"] == 0, f"saat {j['saat']}")
    dene((a["alarm_acik"], a["alarm_saat"], a["alarm_gunler"], a["okunus"], a["kilit"], a["sabah_saat"]) ==
         (1, "07:00", 31, "Emrecik", 1, "08:00"), f"ayar {a}")
    dene(a["alarm_mesaj"] == "Bugün 2 kurabiye var, saat 8'de çıkıyoruz!", f"mesaj (kıvrık kesme düzleşmeli) {a['alarm_mesaj']!r}")
    dene(h[3][0] == 200, f"sürpriz {h[3]}")
    dene(h[4][0] == 400 and "SS:DD" in h[4][1], f"geçersiz saat {h[4]}")
    dene(h[5][0] == 400 and "yalnız harf" in h[5][1], f"geçersiz mesaj {h[5]}")
    dene(h[6][0] == 400 and "en az bir gün" in h[6][1], f"gün yok {h[6]}")
    dene(h[7][0] == 400 and "farklı" in h[7][1], f"kilit yatma = sabah {h[7]}")
    dene(h[8][0] == 400, f"geçersiz saat (epoch) {h[8]}")
    dene("[ayar] saat telefondan alındı: saat 06:00 |" in out and
         "[ayar] saat 06:00 | alarm açık 07:00 (Pzt,Sal,Çar,Per,Cum; gün doğumu 1 dk; Eko'nun sesi) | yatma vakti açık "
         "07:30 | gece kilidi açık (sabah 08:00)" in out, "saat özeti")
    # alarm: 06:59:30 (gün doğumu sürüyor) -> 07:00 çalar; oyuncak konunca susar, hikâye + sürpriz mesaj; ikinci selam
    out, err = k.kos([f"saat {epoch('2026-11-23 06:59:30')} 180", "#bekle 20000", "#halka",
                      f"#sonra 25000 #etiket koy {PP['nfc_no']}", "#bekle 90000", "#etiket kaldir", "#bekle 3000",
                      f"#etiket koy {PP['nfc_no']}", "#bekle 4000", "#etiket kaldir", "#bekle 2000",
                      f"#etiket koy {PP['nfc_no']}", "#bekle 4000"])
    dene("[gün doğumu: alarmdan 1 dk önce]" in out and "gunes -" in halka_d(err), "gün doğumu yok")
    gunes = [s for s in err if s.startswith("HALKA gunes")]
    if dene(gunes, "gün doğumu halka karesi yok"):
        r, g, b = map(int, gunes[0].split("|")[3].split()[0].split(","))
        dene(r > g > b and r > 0, f"gün doğumu rengi kırmızı-turuncu değil: {r},{g},{b}")
    dene("[alarm] çalıyor: Eko'nun sesi" in out and "alarm -" in halka_d(err), "alarm çalmadı")
    dene("[Günaydın Emrecik! Kalkma vakti geldi. Bugün iki kurabiye var, saat sekizde çıkıyoruz!]" in out,
         "alarm metni (okunuş, rakamlar yazıyla)")
    dene("[alarm] durdu: standa dokunuldu" in out, "oyuncak konunca alarm susmadı")
    dene("[Merhaba Emrecik, şimdi sana Pamuk Prenses'in hikâyesini okuyacağım. Emrecik, sana bir mesaj var: Annen seni "
         "çok seviyor]" in out and out.count("[sürpriz mesaj söyleniyor]") == 1, "sürpriz mesaj selamdan sonra bir kez")
    dene("[Emrecik, bak kim geldi: Pamuk Prenses! Dinlemeye hazır mısın?]" in out and
         "[Hoş geldin Emrecik! Pamuk Prenses yeni bir maceraya çıkıyor.]" in out, "selam çeşitleri sırayla")
    dene(out.count("[alarm] çalıyor") == 1, "alarm iki kez çaldı")
    # yatma vakti 07:30 hatırlatma; gece kilidi 07:30-08:00: Pinokyo yok, Ay Dede serbest; 08:00'de kilit biter
    out, err = k.kos([f"saat {epoch('2026-11-23 07:29:50')} 180", "#bekle 20000", f"#etiket koy {PN['nfc_no']}",
                      "#bekle 15000", "#etiket kaldir", "#bekle 2000", "#sonra 8000 #etiket kaldir", "#etiket koy 12",
                      "#bekle 12000", f"saat {epoch('2026-11-23 08:00:10')} 180", f"#etiket koy {PN['nfc_no']}", "#bekle 4000"])
    dene("[yatma vakti]" in out and "[Emrecik, uyku vakti geldi. Ay Dede'yi standa koyarsan sana ninni söylerim.]" in out,
         "yatma hatırlatması")
    dene("[gece kilidi: hikâye yerine ninni önerildi]" in out and "Emrecik, şimdi uyku vakti. Hikâyeler sabah devam edecek." in out,
         "gece kilidi")
    dene("[İyi geceler Emrecik, şimdi sana bir ninni söyleyeceğim.]" in out, "gece kilidinde Ay Dede serbest değil")
    son = out.split("[oyuncak: Pinokyo]")[-1].strip().split("\n")[0]
    dene(out.count("[gece kilidi") == 1 and "Pinokyo" in son and "uyku vakti" not in son,
         f"08:00'den sonra kilit kalkmadı: {son[:80]}")
    # cumartesi: alarm (hafta içi) çalmaz
    out, err = k.kos([f"saat {epoch('2026-11-28 06:59:50')} 180", "#bekle 30000"])
    dene("[alarm] çalıyor" not in out and "[gün doğumu" not in out, "cumartesi alarm çaldı")
    print("  saat, form, gün doğumu, alarm (okunuş, rakamlar), susma + hikâye, sürpriz mesaj, selam çeşitleri, yatma, "
          "gece kilidi, gün seçimi tamam")


# ---- 9. alarm sesi yükleme ----
def alarm_sesi(k):
    print("9. alarm sesi: yükleme, bozuk paket, dinle/dene, açılışta okuma, alarmda çalma")
    pak = os.path.join(k.d, "alarm.eko")
    subprocess.run([sys.executable, os.path.join(TOOLS, "alarm_ses_test.py"), "--paket", pak], check=True,
                   capture_output=True)
    bozuk = os.path.join(k.d, "bozuk.eko")
    with open(pak, "rb") as f:
        b = bytearray(f.read())
    b[1000] ^= 0x55
    with open(bozuk, "wb") as f:
        f.write(bytes(b))
    out, err = k.kos(["#etiket koy 200", "#bekle 10000", f"#http YUKLE /alarm_ses {bozuk}", "#http GET /durum",
                      f"#http YUKLE /alarm_ses {pak} 20000", "#http GET /durum",
                      f"#http YUKLE /alarm_ses {pak}", "#http GET /durum", "#http POST /kaydet alarm_tur=2",
                      "#http POST /alarm_ses_dinle", "#bekle 15000", "#http POST /dinle", "#bekle 5000",
                      "#http POST /alarm_dene", "#bekle 20000", "#http POST /bitir", "#bekle 2000"])
    h = http(err)
    dene(h[0][0] == 400 and "bozuk" in h[0][1] and json.loads(h[1][1])["alarm_ses"]["var"] == 0, f"bozuk paket {h[0]}")
    dene(h[2][0] == 0 and json.loads(h[3][1])["alarm_ses"]["var"] == 0 and "Yükleme yarıda kesildi" in out,
         f"yarım yükleme (bağlantı koptu: yanıt yok) {h[2]}")
    j = json.loads(h[5][1])["alarm_ses"]
    dene(h[4][0] == 200 and j["var"] == 1 and abs(j["sn"] - 10.0) < .05 and j["ad"].startswith("Deneme şarkısı"),
         f"yükleme {h[4]} {j}")
    dene("[alarm denemesi] çalıyor: yüklenen ses" in out and "[alarm denemesi] durdu: deneme bitti" in out, "sesi dinle")
    dene("[Merhaba Emrecik! Adını doğru söylüyor muyum?]" in out or "[Merhaba! Henüz bir ad yazılmadı.]" in out,
         "adı dinle")
    out, err = k.kos([f"saat {epoch('2026-11-24 06:59:58')} 180", f"#sonra 8000 #etiket koy {PP['nfc_no']}", "#bekle 12000"])
    dene("alarm sesi: Deneme şarkısı" in out, "açılışta alarm sesi okunmadı")
    dene("[alarm] çalıyor: yüklenen ses" in out and "[alarm] durdu: standa dokunuldu" in out, "alarmda yüklenen ses")
    print("  bozuk ve yarım paket reddi, yükleme (10 s), dinle, dene, açılışta okuma, alarmda yüklenen ses tamam")


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
    dokunma(k)
    zaman(k)
    alarm_sesi(k)
    print(f"\nurun_akis_test.py: {'HATA ' + str(len(hatalar)) if hatalar else 'hepsi geçti'} ({d})")
    if not a.dizin and not hatalar:
        shutil.rmtree(d, ignore_errors=True)
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
