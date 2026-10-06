"""Hikâye kuyruğunun ve ürün davranışının kartın kendi koduyla (hikaye_oyuncak.ino, sahte ESP32 başlıklarıyla:
tools/kart_pc) bilgisayarda denemesi. Kuyruk bölümü bir dosyada durur (KART_KUYRUK): kart_pc'yi yeniden çalıştırmak
kartı yeniden başlatmaktır.

  1. doldur:   bölüm eski model baytlarıyla (çöp) dolu; boşta arka plan üretimi her figüre KUYRUK_FIGUR_BASI hikâye
               yazar. Her işte K aday üretilir, yazılan = en yüksek puanlı aday (eşitlikte ilki), token token.
               --urun: ilk iki iş degerlendirme/urun_uret.py ile de üretilir; seçilen hikâye aynı olmalı.
  2. çal:      yeniden başlat; "8" Elsa'nın en eski hazır hikâyesini hiç üretmeden çalar, tüketir; "8 1" yer seçerek.
  3. kalıcı:   yeniden başlat; tüketilenler tüketilmiş kalır; boşta yalnız eksikler yeniden üretilir.
  4. bozulma:  dosyada bir hikâyenin bir baytı bozulur: o yuva açılışta yok sayılır ve yeniden üretilir.
  5. düğmeler: FİGÜR/YER/OYNAT kısa-uzun, OYNAT + FİGÜR/YER ses, FİGÜR + YER arka plan, NFC etiketi, hafif uyku,
               ayarların NVS'te kalması.
  6. kesme:    arka plan üretimi sürerken OYNAT'a basılır: aday bırakılır, hikâye okunur, iş kaldığı yerden sürer;
               canlı üretim OYNAT ile durur ve o basış yeni hikâye başlatmaz.

Kullanım: .venv/bin/python firmware/hikaye_oyuncak/tools/kuyruk_test.py [--K 3] [--basi 2] [--urun] [--ses ses.bin]
Çıkış kodu: hata varsa 1.
"""
import argparse
import os
import random
import re
import shutil
import struct
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SKETCH = os.path.dirname(TOOLS)
ROOT = os.path.dirname(os.path.dirname(SKETCH))
MODEL = os.path.join(ROOT, "hf_c3ft_karma")
KUYRUK_OFS, KUYRUK_BOYUT, SEKTOR = 0xB80000, 0x30000, 4096
N_FIGUR = 11
YER_N = [4, 3, 4, 4, 3, 4, 4, 4, 5, 3, 3]
PIN_FIGUR, PIN_YER, PIN_OYNAT = 7, 15, 16

hatalar = []


def dene(kosul, mesaj):
    if not kosul:
        hatalar.append(mesaj)
        print("  HATA:", mesaj)
    return kosul


def derle(d, K, basi):
    kart = os.path.join(d, "kart_pc")
    subprocess.run([os.environ.get("CXX", "g++"), "-O2", "-Wall", "-Wno-unused-function", f"-DKUYRUK_K={K}",
                    f"-DKUYRUK_FIGUR_BASI={basi}", "-I" + os.path.join(TOOLS, "kart_pc", "sahte"), "-o", kart,
                    os.path.join(TOOLS, "kart_pc", "kart_pc.cpp")], check=True)
    return kart


def kos(kart, d, satirlar, ses=None, ek_env=None):
    env = dict(os.environ, KART_MODEL=os.path.join(MODEL, "model.bin"),
               KART_BOLUMLER=os.path.join(SKETCH, "partitions.csv"),
               KART_KUYRUK=os.path.join(d, "kuyruk.bin"), KART_NVS=os.path.join(d, "nvs.txt"))
    if ses:
        env["KART_SES"] = ses
    env.update(ek_env or {})
    r = subprocess.run([kart], input="".join(s + "\n" for s in satirlar), capture_output=True, text=True, env=env)
    if r.returncode:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit(f"kart_pc çıkış kodu {r.returncode}")
    return r.stdout, r.stderr.splitlines()


def ayikla(err):
    """stderr satırları -> olay listesi: ("ADAY", j, puan, tok) | ("KUYRUK", y, f, j, K, puan, n_plan, tok) |
    ("CALINDI", f, j, tok) | ("DURUM", hazır, yuva, uyku, bekçi, silme) | ("UYKU", ms) | ("BOSTA", n)"""
    olay = []
    for s in err:
        p = s.split()
        if not p:
            continue
        if p[0] == "ADAY":
            olay.append(("ADAY", int(p[1]), float(p[7]), [int(x) for x in p[8:]], int(p[3]), p[5] == "1"))
        elif p[0] == "KUYRUK":
            olay.append(("KUYRUK", int(p[1]), int(p[2]), int(p[3]), int(p[4]), float(p[5]), int(p[7]),
                         [int(x) for x in p[8:]]))
        elif p[0] == "CALINDI":
            olay.append(("CALINDI", int(p[1]), int(p[2]), [int(x) for x in p[4:]]))
        elif p[0] == "DURUM":
            olay.append(("DURUM",) + tuple(int(x) for x in p[1:]))
        elif p[0] == "UYKU":
            olay.append(("UYKU", int(p[1]), "GPIO" in s))
        elif p[0] == "BOSTA":
            olay.append(("BOSTA", int(p[1])))
    return olay


def f32(x):
    return struct.unpack("<f", struct.pack("<f", x))[0]


def isler(olay, K):
    """ADAY ... KUYRUK gruplarını çıkarır ve her işte yazılanın en iyi aday olduğunu denetler."""
    out, aday = [], []
    for o in olay:
        if o[0] == "ADAY":
            aday.append(o)
        elif o[0] == "KUYRUK":
            _, y, f, j, k, puan, n_plan, tok = o
            dene(y >= 0, f"kuyruğa yazılamadı ({f} {j})")
            son = aday[-K:]
            dene([a[1] for a in son] == list(range(K)), f"iş ({f},{j}): aday sırası {[a[1] for a in son]}")
            en = max(range(len(son)), key=lambda i: (son[i][2], -i))
            dene(son[en][3] == tok and f32(son[en][2]) == puan and son[en][4] == n_plan,
                 f"iş ({f},{j}): yazılan en iyi aday değil")
            dene(k == K, f"iş ({f},{j}): K={k}")
            out.append({"y": y, "f": f, "j": j, "puan": puan, "tok": tok, "adaylar": son})
            aday = []
    return out


def durum(olay):
    d = [o for o in olay if o[0] == "DURUM"]
    return [x[1] for x in d]


def urun_karsilastir(d, isler_, tohum, K):
    """İlk işleri urun_uret ile üretir (gen.c -DLLM_INT8_ACT; tools/kart_pc_karsilastir.py ile aynı yol)."""
    gen_i8 = os.path.join(d, "gen_i8")
    subprocess.run([os.environ.get("CC", "cc"), "-O3", "-DLLM_INT8_ACT", "-o", gen_i8,
                    os.path.join(ROOT, "runtime", "host_verify", "gen.c"), "-lm"], check=True)
    os.environ["GEN"] = gen_i8
    sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
    import urun_uret as U
    from tokenizers import Tokenizer
    tok = Tokenizer.from_file(os.path.join(MODEL, "tokenizer.json"))
    os.makedirs(os.path.join(d, "suzgec"), exist_ok=True)
    for i in isler_:
        fig = U.FIGURLER[i["f"]]
        k = U.KARTLAR[fig]
        yer = k["yerler"][i["j"]]["etiket"]
        suz = U.suzgec_dosyasi(tok, U.kadro_disi(fig), os.path.join(d, "suzgec", fig + ".txt"))
        ids = U.istem(tok, k["ad"]["deger"], yer, None)
        py = []
        for jj in range(K):
            c = U.aday_uret(MODEL, tok, ids, tohum + jj, 0.5, suz)
            c["puan"], _ = U.puanla(c, fig, yer)
            py.append(c)
        en = max(range(K), key=lambda x: py[x]["puan"])
        t = i["tok"]
        n_plan = [a for a in i["adaylar"] if a[3] == t][0][4]
        plan = ("Sorun:" + tok.decode(t[:n_plan - 2])).strip()
        metin = tok.decode(t[n_plan:]).strip()
        ok = dene(plan == py[en]["plan"] and metin == py[en]["metin"] and abs(py[en]["puan"] - i["puan"]) < 1e-5,
                  f"urun_uret farkı: {fig} {yer}")
        print(f"  urun_uret: {fig} {yer} K={K}: seçilen aday {en}, puan {py[en]['puan']:.4f} -> "
              f"{'aynı' if ok else 'FARKLI'}")


def bas_birak(pin, ms):
    return [f"#pin {pin} 0", f"#bekle {ms}", f"#pin {pin} 1", "#bekle 100"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=3, help="kuyruk aday sayısı (ürün 16; deneme hızlı olsun diye 3)")
    ap.add_argument("--basi", type=int, default=2, help="figür başına hazır hikâye (ürün 3)")
    ap.add_argument("--urun", action="store_true", help="ilk iki işi urun_uret.py ile karşılaştır")
    ap.add_argument("--ses", help="ses.bin (verilirse düğme denemesi konuşmayla)")
    ap.add_argument("--dizin")
    a = ap.parse_args()
    d = a.dizin or tempfile.mkdtemp(prefix="kuyruk_test_")
    os.makedirs(d, exist_ok=True)
    K, B = a.K, a.basi
    kart = derle(d, K, B)
    toplam = N_FIGUR * B

    print(f"1. doldur (K={K}, figür başına {B}; bölüm çöp dolu)")
    random.seed(3)
    with open(os.path.join(d, "kuyruk.bin"), "wb") as f:
        f.write(bytes(random.getrandbits(8) for _ in range(KUYRUK_BOYUT)))
    if os.path.exists(os.path.join(d, "nvs.txt")):
        os.remove(os.path.join(d, "nvs.txt"))
    out, err = kos(kart, d, ["#tohum 100", "#durum", "#bosta", "#durum", "k"])
    olay = ayikla(err)
    ii = isler(olay, K)
    dene(durum(olay) == [0, toplam], f"hazır sayısı {durum(olay)}, beklenen [0, {toplam}]")
    dene(len(ii) == toplam, f"{len(ii)} iş")
    for f in range(N_FIGUR):
        yerler = [i["j"] for i in ii if i["f"] == f]
        dene(len(yerler) == B and len(set(yerler)) == min(B, YER_N[f]), f"figür {f}: yerler {yerler}")
    dene(len({i["y"] for i in ii}) == toplam, "yuvalar tekrar etti")
    print(f"  {len(ii)} hikâye yazıldı, her biri {K} adayın en iyisi")
    if a.urun:
        urun_karsilastir(d, ii[:2], 100, K)

    print("2. yeniden başlat, çal")
    elsa = [i for i in ii if i["f"] == 7]  # yazılış sırası = sıra
    beklenen_8 = elsa[0]
    kalan = elsa[1:]
    yer0 = [i for i in kalan if i["j"] == 0]
    out, err = kos(kart, d, ["#durum", "8", "8 1", "#durum"])
    olay = ayikla(err)
    cal = [o for o in olay if o[0] == "CALINDI"]
    ilk_aday = next((k for k, o in enumerate(olay) if o[0] == "ADAY"), len(olay))
    ilk_cal = next((k for k, o in enumerate(olay) if o[0] == "CALINDI"), len(olay))
    dene(ilk_cal < ilk_aday, "\"8\" hazır hikâyeyi üretmeden önce çalmadı")
    dene(cal and cal[0][1] == 7 and cal[0][3] == beklenen_8["tok"], "\"8\": Elsa'nın en eski hikâyesi çalınmadı")
    dene("hazır hikâye" in out, "çıktıda 'hazır hikâye' yok")
    tuketilen = 1
    if yer0:
        dene(len(cal) == 2 and cal[1][2] == 0 and cal[1][3] == yer0[0]["tok"], "\"8 1\": Elsa dağ hazırı çalınmadı")
        tuketilen = 2
    else:
        dene(len(cal) == 1 and any(o[0] == "ADAY" for o in olay), "\"8 1\": hazır yokken canlı üretilmedi")
    dene(durum(olay) == [toplam, toplam - tuketilen], f"hazır sayısı {durum(olay)}")
    print(f"  {tuketilen} hazır hikâye çalındı (üretim beklemeden)")

    print("3. yeniden başlat: tüketilenler kalıcı, eksikler yeniden üretilir")
    out, err = kos(kart, d, ["#tohum 300", "#durum", "#bosta", "#durum"])
    olay = ayikla(err)
    yeni = isler(olay, K)
    dene(durum(olay) == [toplam - tuketilen, toplam], f"hazır sayısı {durum(olay)}")
    dene(len(yeni) == tuketilen and all(i["f"] == 7 for i in yeni), f"yeniden üretilen {[(i['f'], i['j']) for i in yeni]}")
    print(f"  {len(yeni)} hikâye yeniden üretildi (Elsa)")

    print("4. bozulma: bir hikâyenin bir baytı bozuldu")
    with open(os.path.join(d, "kuyruk.bin"), "r+b") as f:
        hedef = ii[3]
        f.seek(hedef["y"] * SEKTOR + 32 + 7)
        b = f.read(1)
        f.seek(hedef["y"] * SEKTOR + 32 + 7)
        f.write(bytes([b[0] ^ 0x10]))
    out, err = kos(kart, d, ["#tohum 400", "#durum", "#bosta", "#durum"])
    olay = ayikla(err)
    yeni = isler(olay, K)
    dene(durum(olay) == [toplam - 1, toplam], f"hazır sayısı {durum(olay)}")
    dene(len(yeni) == 1 and yeni[0]["f"] == hedef["f"], "bozulan yeniden üretilmedi")
    print(f"  bozuk yuva yok sayıldı ve yeniden üretildi (figür {hedef['f'] + 1})")

    print("5. düğmeler, NFC, ses seviyesi, uyku, ayarlar" + (" (konuşmalı)" if a.ses else ""))
    niloya = [i for i in ii if i["f"] == 0]
    sat = ["k-", "#durum"]
    sat += bas_birak(PIN_FIGUR, 100)                  # Maşa
    sat += bas_birak(PIN_FIGUR, 1000)                 # uzun: geri, Niloya
    sat += bas_birak(PIN_YER, 100)                    # Niloya'nın 1. yeri (orman)
    sat += bas_birak(PIN_OYNAT, 100)                  # Niloya orman: hazır
    sat += ["#pin 16 0", "#bekle 300"] + bas_birak(PIN_FIGUR, 80) + bas_birak(PIN_YER, 80) + bas_birak(PIN_YER, 80)
    sat += bas_birak(PIN_FIGUR, 80) + ["#pin 16 1", "#bekle 100"]  # ses 7, 6, 5, 6; OYNAT'ın kendi olayı yok
    sat += bas_birak(PIN_OYNAT, 1200)                 # uzun: son hikâye yeniden
    sat += ["n DEADBEEF", "#bekle 50", "n 04 A1 B2 C3", "#bekle 50"]  # bilinmeyen; Niloya (NFC_OYNAT: çalar)
    sat += ["#pin 7 0", "#bekle 200", "#pin 15 0", "#bekle 3600", "#pin 7 1", "#pin 15 1", "#bekle 100"]  # arka aç
    sat += ["k-", "#pin_sonra 15 0 35000", "#pin_sonra 15 1 35100", "#bekle 70000", "#durum"]  # uyku; YER uyandırır
    out, err = kos(kart, d, sat, ses=a.ses)
    olay = ayikla(err)
    dene("figür: 2 Maşa" in out, "FİGÜR kısa: Maşa")
    dene(out.count("figür: 1 Niloya") >= 2, "FİGÜR uzun ve NFC: Niloya")
    dene("yer: orman (Niloya)" in out, "YER kısa: orman")
    cal = [o for o in olay if o[0] == "CALINDI"]
    nil_or = [i for i in niloya if i["j"] == 0]
    dene(len(cal) >= 3 and cal[0][1:3] == (0, 0) and (not nil_or or cal[0][3] == nil_or[0]["tok"]),
         "OYNAT: Niloya orman hazırı çalınmadı")
    dene(len(cal) >= 2 and cal[1][3] == cal[0][3], "OYNAT uzun: son hikâye yeniden okunmadı")
    sv = re.findall(r"ses seviyesi (\d)/7 \(", out)
    dene(sv == ["7", "6", "5", "6"], f"OYNAT + FİGÜR / YER: ses seviyeleri {sv}")
    dene(out.count("(düğme: oynat)") == 1, f"OYNAT basışı {out.count('(düğme: oynat)')} kez (ikili basışta bastırılmadı?)")
    dene("bilinmeyen etiket: DEADBEEF" in out, "bilinmeyen NFC etiketi")
    dene(len(cal) >= 3 and cal[2][1] == 0, "NFC: Niloya hikâyesi başlamadı")
    dene("arka plan üretimi: açık" in out, "FİGÜR + YER: arka plan")
    uyku = [o for o in olay if o[0] == "UYKU"]
    dene(any(u[1] >= 10000 for u in uyku), "boşta hafif uyku yok")
    dene(any(u[2] for u in uyku) and out.count("yer: orman (Niloya)") == 2, "uykuda YER basışı uyandırmadı")
    dene(any(o[0] == "DURUM" and o[3] > 0 for o in olay), "uyku sayılmadı")
    dene(not any(o[0] == "ADAY" for o in olay), "düğme denemesinde üretim olmamalıydı (hazırlar yeterdi)")
    if a.ses:
        dene("[Niloya]" in out and "[ses:" in out, "konuşma yok")
    out, err = kos(kart, d, ["#durum"])
    dene("seçili: Niloya, orman" in out and "ses seviyesi 6/7 |" in out and "arka plan kapalı" in out,
         "ayarlar NVS'te kalmadı")
    print(f"  düğmeler, NFC, ses seviyesi, {len(uyku)} hafif uyku, ayarlar tamam")

    print("6. kesme: arka plan üretimi sırasında OYNAT; canlı üretim sırasında OYNAT")
    os.remove(os.path.join(d, "kuyruk.bin"))
    # ARKA_BEKLE_MS (5 s, sahte saat) sonra iş başlar; basış ondan ~1,2 s sonra (gerçek saat: aday ortası)
    out, err = kos(kart, d, ["k+", "#tohum 500", "#pin_sonra 16 0 6200", "#pin_sonra 16 1 6300", "#bosta 1", "#durum"])
    olay = ayikla(err)
    ii6 = isler(olay, K)
    dene("(düğme: oynat)" in out, "arka planda OYNAT görülmedi")
    dene("yarım kuyruk işinden" in out or "=== Niloya" in out, "OYNAT'tan sonra hikâye yok")
    dene(len(ii6) == 1, "iş sürüp bitmedi")
    print(f"  arka plan: {'yarım işin en iyisi çalındı' if 'yarım kuyruk işinden' in out else 'canlı'}; iş sonra tamamlandı")
    out, err = kos(kart, d, ["k-", "k sil", "#pin_sonra 16 0 300", "#pin_sonra 16 1 400", "6 1", "#bekle 300", "#durum"])
    olay = ayikla(err)
    dene("(durduruldu)" in out, "canlı üretim OYNAT ile durmadı")
    dene(out.count("=== Hayri") == 1, "durduran OYNAT yeni hikâye başlattı")
    print("  canlı üretim durdu, basış yutuldu")

    print(f"\nkuyruk_test.py: {'HATA ' + str(len(hatalar)) if hatalar else 'hepsi geçti'} ({d})")
    if not a.dizin and not hatalar:
        shutil.rmtree(d, ignore_errors=True)
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
