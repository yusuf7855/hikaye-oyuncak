"""Hikâye Oyuncağı test yazılımının başlık dosyalarını üret: generated/vocab.h ve generated/istemler.h.

Kullanım: python firmware/hikaye_oyuncak/tools/basliklar.py [--tokenizer modeller/c2_tokenizer.json]
llm.h, ornekle.h: runtime/'dan kopya (Arduino IDE çizim dışındaki göreli yolları bulamaz).
vocab.h   : token id -> ham UTF-8 baytları (GPT-2 bayt düzeyi tablosundan; tek token'ın decode'u Türkçe harfin
            yarısını taşıyan token'da U+FFFD verirdi). Özel token'lar (<|endoftext|>) boş.
istemler.h: 12 tek figür + 66 ikili, her biri 6 yerde istem id'leri (baslangic.prompt_idler: EOT + başlık +
            "\\nSorun:", plan modu) ve seçime göre yasaklı isim id'leri (yasak_idler). Kartta seçim yalnız bu
            tablolardan okunur; tokenizer kartta çalışmaz. C2 ve C3 aynı tokenizer'ı kullanır.
"""
import argparse
import shutil
import itertools
import json
import os
import sys

from tokenizers import Tokenizer

SKETCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(SKETCH))
sys.path.insert(0, ROOT)
from baslangic import KAR, prompt_idler, yasak_idler  # noqa: E402

YERLER = ["orman", "deniz", "ev", "park", "sato", "dag"]
YER_AD = ["orman", "deniz", "ev", "park", "şato", "dağ"]


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokenizer", default=os.path.join(ROOT, "modeller", "c2_tokenizer.json"))
    a = ap.parse_args()
    tok = Tokenizer.from_file(a.tokenizer)
    V = tok.get_vocab_size()
    ozel = {tok.token_to_id(s) for s in ["<|endoftext|>"] if tok.token_to_id(s) is not None}
    tb = bayt_tablosu()
    blob, offs = bytearray(), [0]
    for i in range(V):
        if i not in ozel:
            blob.extend(bytes(tb[ch] for ch in tok.id_to_token(i)))
        offs.append(len(blob))
    out = os.path.join(SKETCH, "generated")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "vocab.h"), "w") as f:
        f.write("// Üretildi: tools/basliklar.py. token id -> ham UTF-8 baytları.\n#pragma once\n#include <stdint.h>\n")
        f.write(f"#define VOCAB_N {V}\n")
        f.write(c_dizi("VOCAB_OFF", offs, "uint32_t"))
        f.write(c_dizi("VOCAB_BLOB", list(blob), "unsigned char"))

    figurler = list(KAR)  # kimlik sırası: tavsan, kedi, ...
    secimler = [(k,) for k in figurler] + list(itertools.combinations(figurler, 2))
    ist, ist_off, yas, yas_off = [], [0], [], [0]
    for kim in secimler:
        y = yasak_idler(tok, list(kim))
        yas += y
        yas_off.append(len(yas))
        for yer in YERLER:
            ist += prompt_idler(tok, list(kim), yer, eot=True, plan=True)
            ist_off.append(len(ist))
    nl = tok.encode("\n\n").ids
    govde_yasak = [199, 9491]
    assert tok.id_to_token(199) == "Ċ", tok.id_to_token(199)
    with open(os.path.join(out, "istemler.h"), "w", encoding="utf-8") as f:
        f.write("// Üretildi: tools/basliklar.py. Seçim s (0..77) = 12 tek figür + 66 ikili (baslangic.KAR sırası);\n"
                "// istem = ISTEM_ID[ISTEM_OFF[s*6+yer] .. ISTEM_OFF[s*6+yer+1]), yasak = YASAK_ID[YASAK_OFF[s]..].\n")
        f.write("#pragma once\n#include <stdint.h>\n")
        f.write(f"#define N_FIGUR {len(figurler)}\n#define N_SECIM {len(secimler)}\n#define N_YER 6\n")
        f.write(f"#define EOT_ID {tok.token_to_id('<|endoftext|>')}\n#define NL_ID 199\n")
        f.write(c_dizi("GOVDE_YASAK", govde_yasak))
        f.write("static const char *FIGUR_AD[N_FIGUR] = {" + ", ".join(
            f'"{KAR[k]["isim"]} ({KAR[k]["tur"]})"' for k in figurler) + "};\n")
        f.write("static const char *YER_AD[N_YER] = {" + ", ".join(f'"{y}"' for y in YER_AD) + "};\n")
        isim_id = []
        for k in figurler:
            ids = tok.encode(" " + KAR[k]["isim"]).ids
            assert len(ids) == 1, (KAR[k]["isim"], ids)
            isim_id.append(ids[0])
        f.write(c_dizi("ISIM_ID", isim_id))  # " Pamuk" gibi tek token: kartta isim sayımı (seçici)
        f.write(c_dizi("SECIM_A", [figurler.index(s[0]) for s in secimler], "int8_t"))
        f.write(c_dizi("SECIM_B", [figurler.index(s[1]) if len(s) > 1 else -1 for s in secimler], "int8_t"))
        f.write(c_dizi("ISTEM_ID", ist))
        f.write(c_dizi("ISTEM_OFF", ist_off, "uint16_t"))
        f.write(c_dizi("YASAK_ID", yas))
        f.write(c_dizi("YASAK_OFF", yas_off, "uint16_t"))
    # Motor başlıkları çizimin içine kopyalanır: Arduino IDE derlerken çizimi geçici bir klasöre taşır ve
    # "../../runtime/..." gibi dışarıdaki göreli yollar bulunamaz. Kaynak her zaman runtime/ (tek doğru kaynak).
    for ad in ("llm.h", "ornekle.h"):
        shutil.copyfile(os.path.join(ROOT, "runtime", ad), os.path.join(out, ad))
    print(f"vocab.h: {V} token, {len(blob)} B | istemler.h: {len(secimler)} seçim x 6 yer, {len(ist)} istem id, "
          f"{len(yas)} yasak id")


if __name__ == "__main__":
    main()
