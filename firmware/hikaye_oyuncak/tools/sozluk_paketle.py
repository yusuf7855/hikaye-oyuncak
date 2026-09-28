"""Kart seçicisinin (secici.h) uydurma-kelime sözlüğü: degerlendirme/sozluk.pkl -> generated/sozluk.h.

Kullanım: python firmware/hikaye_oyuncak/tools/sozluk_paketle.py [--sozluk degerlendirme/sozluk.pkl]
Biçim: kelimeler 35 harflik alfabede (SOZLUK_ALFABE sırası, kod 1..35) kodlanır, kod dizisine göre sıralanır ve
16'lık bloklara bölünür. Blok başı tam yazılır; öteki kelimeler önek sıkıştırmalı: [önceki kelimeyle ortak önek
uzunluğu][sonek kodları; son kodun 0x80 biti açık]. SOZLUK_BLOK[b] b. bloğun SOZLUK_VERI içindeki başlangıcı.
Kartta arama: blok başlarında ikili arama + blok içinde sıralı çözme (secici.h secici_sozlukte).
Yalnız [a-zçğıöşüâîû]+ kelimeleri tutulur (sec.py yalnız bunları sorar). ~76 bin kelime ~290 KB flash.
"""
import argparse
import os
import pickle
import re

SKETCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(SKETCH))
ALFABE = "abcçdefgğhıijklmnoöprsştuüvyzqwxâîû"
BLOK = 16


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sozluk", default=os.path.join(ROOT, "degerlendirme", "sozluk.pkl"))
    a = ap.parse_args()
    assert len(ALFABE) == 35 and len(set(ALFABE)) == 35
    kod = {c: i + 1 for i, c in enumerate(ALFABE)}
    sozluk = pickle.load(open(a.sozluk, "rb"))
    kelimeler = sorted(tuple(kod[c] for c in w) for w in sozluk if re.fullmatch(r"[a-zçğıöşüâîû]+", w))
    veri, blok, onceki = bytearray(), [], ()
    for i, w in enumerate(kelimeler):
        if i % BLOK == 0:
            blok.append(len(veri))
            p = 0
        else:
            p = 0
            while p < min(len(w), len(onceki)) and w[p] == onceki[p]:
                p += 1
        assert p < len(w) and p < 128
        veri.append(p)
        veri.extend(w[p:-1])
        veri.append(w[-1] | 0x80)
        onceki = w
    uzun = max(map(len, kelimeler))
    out = os.path.join(SKETCH, "generated", "sozluk.h")
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Üretildi: tools/sozluk_paketle.py (degerlendirme/sozluk.pkl). secici.h uydurma-kelime kuralı.\n")
        f.write("#pragma once\n#include <stdint.h>\n")
        f.write(f"#define SOZLUK_N {len(kelimeler)}\n#define SOZLUK_N_BLOK {len(blok)}\n#define SOZLUK_BLOK_BOY {BLOK}\n")
        f.write(f"#define SOZLUK_UZUN {uzun}\n")
        f.write(f'static const char SOZLUK_ALFABE[] = "{ALFABE}";  // kod 1..35 (UTF-8)\n')
        f.write(f"static const uint32_t SOZLUK_BLOK[{len(blok)}] = {{\n")
        for i in range(0, len(blok), 16):
            f.write("  " + ", ".join(map(str, blok[i:i + 16])) + ",\n")
        f.write("};\n")
        f.write(f"static const uint8_t SOZLUK_VERI[{len(veri)}] = {{\n")
        for i in range(0, len(veri), 32):
            f.write("  " + ",".join(map(str, veri[i:i + 32])) + ",\n")
        f.write("};\n")
    print(f"sozluk.h: {len(kelimeler)} kelime, {len(blok)} blok, veri {len(veri)} B + blok {4 * len(blok)} B")


if __name__ == "__main__":
    main()
