"""Hikâye Oyuncağı test yazılımının başlık dosyalarını üret: generated/vocab.h ve generated/istemler.h.

Kullanım: python firmware/hikaye_oyuncak/tools/basliklar.py [--tokenizer hf_c3ft_karma/tokenizer.json]
llm.h, ornekle.h, isim_suzgec.h: runtime/'dan kopya (Arduino IDE çizim dışındaki göreli yolları bulamaz).
vocab.h   : token id -> ham UTF-8 baytları (GPT-2 bayt düzeyi tablosundan; tek token'ın decode'u Türkçe harfin
            yarısını taşıyan token'da U+FFFD verirdi). Özel token'lar (<|endoftext|>) boş.
istemler.h: ürün kurulumu, degerlendirme/urun_uret.py ile birebir:
            - data/urun_kartlari.json'daki figürler (urun_uret.FIGURLER) ve kart yerleri; istem urun_uret.istem
              (EOT + "Karakter: F | Yer: Y\\nSorun:", plan modu, Yan alanı yok: ürün varsayılanı), yalnız tek figür
            - isim süzgeci (runtime/isim_suzgec.h, gen -Y): figür başına urun_uret.suzgec_dosyasi'nın ad satırları
              (kadro_disi, kelime başı olabilen adlar '$' ile) ve süzgecin token baytlarının vocab.h'den farklı
              olduğu token'lar (gen -Y dosyası özel token'ı da metniyle yazar: "<|endoftext|>")
            - seçici (secici.h secici_urun_puanla = urun_uret.puanla) tabloları: kadro, izinli adlar, bütün ürün
              adları, ISIM_KELIME, takıntı önekleri ve TAKINTI_HARIC
            Kartta seçim yalnız bu tablolardan okunur; tokenizer kartta çalışmaz.
"""
import argparse
import os
import shutil
import sys

from tokenizers import Tokenizer

SKETCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(SKETCH))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
from baslangic import KAR, YABANCI  # noqa: E402
import urun_uret as U  # noqa: E402

# secici.h sc_yer_say sırası (sec.YER_KELIME: orman, deniz, ev, park, sato, dag); kart etiketleri bunların
# Türkçe yazımı (urun_uret.YER_ANAHTAR)
YERLER = ["orman", "deniz", "ev", "park", "sato", "dag"]
YER_AD = ["orman", "deniz", "ev", "park", "şato", "dağ"]
YER_MAKS = 5


def bayt_tablosu():
    bs = list(range(33, 127)) + list(range(161, 173)) + list(range(174, 256))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return {chr(c): b for b, c in zip(bs, cs)}


def c_dizi(ad, degerler, tip="int16_t"):
    satirlar = [", ".join(map(str, degerler[i:i + 24])) for i in range(0, len(degerler), 24)]
    return f"static const {tip} {ad}[{len(degerler)}] = {{\n  " + ",\n  ".join(satirlar) + "\n};\n"


def c_dizge(s):
    """UTF-8 C dizgesi (s: str ya da bytes): ASCII dışı baytlar \\x.. ile; ardından onaltılık rakam gelirse dizge
    bölünür."""
    out, onceki_hex = [], False
    for b in (s if isinstance(s, bytes) else s.encode("utf-8")):
        c = chr(b)
        if b < 32 or b >= 127 or c in '"\\':
            out.append(f"\\x{b:02x}")
            onceki_hex = True
        else:
            if onceki_hex and c in "0123456789abcdefABCDEF":
                out.append('" "')
            out.append(c)
            onceki_hex = False
    return '"' + "".join(out) + '"'


def c_dizgeler(ad, liste):
    satirlar, satir = [], []
    for s in liste:
        satir.append(c_dizge(s))
        if sum(len(x) + 2 for x in satir) > 100:
            satirlar.append(", ".join(satir))
            satir = []
    if satir:
        satirlar.append(", ".join(satir))
    return f"static const char *const {ad}[{max(1, len(liste))}] = {{\n  " + ",\n  ".join(satirlar or ['""']) + "\n};\n"


def figur_listesi(ad, listeler, f):
    """Figür başına dizge listeleri: AD[] düz liste + AD_OFF[N_FIGUR+1]."""
    duz, off = [], [0]
    for L in listeler:
        duz += L
        off.append(len(duz))
    f.write(c_dizgeler(ad, duz))
    f.write(c_dizi(ad + "_OFF", off, "uint16_t"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokenizer", default=os.path.join(ROOT, "hf_c3ft_karma", "tokenizer.json"))
    a = ap.parse_args()
    tok = Tokenizer.from_file(a.tokenizer)
    V = tok.get_vocab_size()
    ozel = {tok.token_to_id(s) for s in ["<|endoftext|>"] if tok.token_to_id(s) is not None}
    tb = bayt_tablosu()
    blob, offs, kayit = bytearray(), [0], []
    for i in range(V):
        b = b"" if i in ozel else bytes(tb[ch] for ch in tok.id_to_token(i))
        kayit.append(b)
        blob.extend(b)
        offs.append(len(blob))
    out = os.path.join(SKETCH, "generated")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "vocab.h"), "w") as f:
        f.write("// Üretildi: tools/basliklar.py. token id -> ham UTF-8 baytları.\n#pragma once\n#include <stdint.h>\n")
        f.write(f"#define VOCAB_N {V}\n")
        f.write(c_dizi("VOCAB_OFF", offs, "uint32_t"))
        f.write(c_dizi("VOCAB_BLOB", list(blob), "unsigned char"))

    # süzgecin token baytları (urun_uret.suzgec_dosyasi) vocab.h'den yalnız birkaç özel token'da ayrılır
    harita = U._bayt_haritasi()
    suz_ozel = []
    for i in range(V):
        s = tok.id_to_token(i) or ""
        b = bytes(harita[c] for c in s if c in harita)
        if b != kayit[i]:
            suz_ozel.append((i, b))
    assert len(suz_ozel) <= 8, suz_ozel

    figurler = list(U.FIGURLER)
    EOT = tok.token_to_id("<|endoftext|>")
    assert EOT == U.EOT and tok.id_to_token(U.NL) == "Ċ" and U.SATIR_YASAK == [199, 9491], (EOT, U.NL, U.SATIR_YASAK)
    ist, ist_off, fy_n, fy = [], [0], [], []
    for kim in figurler:
        k = U.KARTLAR[kim]
        yerler = [y["etiket"] for y in k["yerler"]]
        assert len(yerler) <= YER_MAKS, (kim, yerler)
        fy_n.append(len(yerler))
        fy += [YER_AD.index(y) for y in yerler] + [-1] * (YER_MAKS - len(yerler))
        for j in range(YER_MAKS):
            if j < len(yerler):
                ids = U.istem(tok, k["ad"]["deger"], yerler[j], None)
                assert tok.decode(ids[1:]) == f"Karakter: {k['ad']['deger']} | Yer: {yerler[j]}\nSorun:"
                ist += ids
            ist_off.append(len(ist))
    suz = [[a + ("$" if U.kelime_basi_mi(a) else "") for a in U.kadro_disi(k)] for k in figurler]
    kadro = [sorted(U.figur_adlari(k)) for k in figurler]
    izinli, takinti_ad = [], []
    for kim in figurler:
        k = U.KARTLAR[kim]
        kd = U.figur_adlari(kim)
        rol = {s for y in k["yanlar"] for s in y["yuzey_bicimleri"] if s[:1].isupper()}
        izinli.append(sorted(kd | rol | {w for x in kd | rol for w in x.split()}))  # urun_uret.kadro_cezalari
        takinti_ad.append(sorted({U.sec.kucuk(w)[:5] for x in kd for w in x.split()}))  # urun_uret.takinti_cezasi
    tum_isim = sorted(set().union(*(U.figur_adlari(k) for k in figurler)))  # puanla: sec.TUM_ISIM
    tum_ad = sorted(set(tum_isim) | set(YABANCI) | {x["isim"] for x in KAR.values()})  # kadro_cezalari: tum_urun
    for L in kadro + izinli + [tum_isim, tum_ad]:
        for s in L:
            assert "\n" not in s
    with open(os.path.join(out, "istemler.h"), "w", encoding="utf-8") as f:
        f.write("// Üretildi: tools/basliklar.py (degerlendirme/urun_uret.py ile birebir). Figür f (0..N_FIGUR-1,\n"
                "// urun_uret.FIGURLER sırası), kart yeri j (0..FIGUR_YER_N[f]-1): genel yer FIGUR_YER[f][j] (YER_AD),\n"
                "// istem = ISTEM_ID[ISTEM_OFF[f*YER_MAKS+j] .. ISTEM_OFF[f*YER_MAKS+j+1]) (urun_uret.istem, Yan yok),\n"
                "// süzgeç adları = SUZGEC_AD[SUZGEC_AD_OFF[f] .. SUZGEC_AD_OFF[f+1]) (urun_uret.kadro_disi, '$' =\n"
                "// KELIME_BASI). URUN_* tabloları secici.h secici_urun_puanla içindir (urun_uret.puanla).\n")
        f.write("#pragma once\n#include <stdint.h>\n")
        f.write(f"#define N_FIGUR {len(figurler)}\n#define N_YER {len(YER_AD)}\n#define YER_MAKS {YER_MAKS}\n")
        f.write(f"#define EOT_ID {EOT}\n#define NL_ID {U.NL}\n")
        f.write(c_dizi("GOVDE_YASAK", U.SATIR_YASAK))
        f.write(c_dizgeler("FIGUR_AD", [U.KARTLAR[k]["ad"]["deger"] for k in figurler]))
        f.write(c_dizgeler("FIGUR_KIMLIK", figurler))
        f.write(c_dizgeler("YER_AD", YER_AD))
        f.write(c_dizi("FIGUR_YER_N", fy_n, "int8_t"))
        f.write(c_dizi("FIGUR_YER", fy, "int8_t").replace(f"FIGUR_YER[{len(fy)}]", f"FIGUR_YER[N_FIGUR * YER_MAKS]"))
        f.write(c_dizi("ISTEM_ID", ist))
        f.write(c_dizi("ISTEM_OFF", ist_off, "uint16_t"))
        f.write("// isim süzgeci (runtime/isim_suzgec.h): figür başına yasaklı adlar ve bayt uzunlukları\n")
        duz = [s for L in suz for s in L]
        figur_listesi("SUZGEC_AD", suz, f)
        f.write(c_dizi("SUZGEC_AD_UZUN", [len(s.encode("utf-8")) for s in duz], "int"))
        f.write("// süzgeç token baytları vocab.h'den farklı olan token'lar (gen -Y dosyasındaki gibi)\n")
        f.write(f"#define SUZGEC_OZEL_N {len(suz_ozel)}\n")
        f.write(c_dizi("SUZGEC_OZEL_ID", [i for i, _ in suz_ozel] or [0], "int16_t"))
        f.write(c_dizgeler("SUZGEC_OZEL_BAYT", [b for _, b in suz_ozel]))
        f.write("// seçici (urun_uret.puanla): figur_adlari, kadro_cezalari'nın izinli kümesi, takıntı önekleri\n")
        figur_listesi("URUN_KADRO", kadro, f)
        figur_listesi("URUN_IZINLI", izinli, f)
        figur_listesi("URUN_TAKINTI_AD", takinti_ad, f)
        f.write(f"#define URUN_TUM_ISIM_N {len(tum_isim)}\n" + c_dizgeler("URUN_TUM_ISIM", tum_isim))
        f.write(f"#define URUN_TUM_AD_N {len(tum_ad)}\n" + c_dizgeler("URUN_TUM_AD", tum_ad))
        ik = sorted(U.ISIM_KELIME)
        f.write(f"#define URUN_ISIM_KELIME_N {len(ik)}\n" + c_dizgeler("URUN_ISIM_KELIME", ik))
        th = sorted(U.TAKINTI_HARIC)
        f.write(f"#define URUN_TAKINTI_HARIC_N {len(th)}\n" + c_dizgeler("URUN_TAKINTI_HARIC", th))
    # Motor başlıkları çizimin içine kopyalanır: Arduino IDE derlerken çizimi geçici bir klasöre taşır ve
    # "../../runtime/..." gibi dışarıdaki göreli yollar bulunamaz. Kaynak her zaman runtime/ (tek doğru kaynak).
    for ad in ("llm.h", "ornekle.h", "isim_suzgec.h"):
        shutil.copyfile(os.path.join(ROOT, "runtime", ad), os.path.join(out, ad))
    print(f"vocab.h: {V} token, {len(blob)} B | istemler.h: {len(figurler)} figür, {sum(fy_n)} figür x yer, "
          f"{len(ist)} istem id, {len(duz)} süzgeç adı, {len(suz_ozel)} özel süzgeç token'ı")


if __name__ == "__main__":
    main()
