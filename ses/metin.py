"""Türkçe metin -> sembol dizisi (ses modelinin girdisi).

Türkçe yazım neredeyse sesletimle bire bir: model harflerden (grafem) öğrenir, ayrı bir sesbirim sözlüğü
gerekmez. Kartta da aynı kural C'de uygulanacak (ses/kart/metin.h), bu yüzden kurallar kasten basit:
- Türkçe küçük harf (I -> ı, İ -> i), şapkalı harfler korunur (â î û),
- noktalama bir sembol (duraklama ve tonlama için): , . ! ? ve tırnak açılış/kapanışı,
- rakamlar ve bilinmeyen karakterler atlanır, çoklu boşluk tek boşluk.
"""
import re

HARFLER = "abcçdefgğhıijklmnoöprsştuüvyzâîû"
NOKTALAMA = ",.!?\"-:;"
SEMBOLLER = ["_"] + [" "] + list(NOKTALAMA) + list(HARFLER)   # 0 = dolgu
SEMBOL_ID = {s: i for i, s in enumerate(SEMBOLLER)}
N_SEMBOL = len(SEMBOLLER)


def kucult(metin):
    return metin.replace("I", "ı").replace("İ", "i").lower()


def temizle(metin):
    m = kucult(metin)
    m = m.replace("“", '"').replace("”", '"').replace("’", "'").replace("…", ".").replace("—", "-")
    m = m.replace("'", "")  # Alev'e -> aleve (kesme sesletimi değiştirmez)
    m = "".join(c if (c in SEMBOL_ID or c.isspace()) else " " for c in m)
    return re.sub(r"\s+", " ", m).strip()


def kodla(metin):
    """Metin -> sembol kimlikleri (dolgu hariç)."""
    return [SEMBOL_ID[c] for c in temizle(metin)]


if __name__ == "__main__":
    import sys
    ornek = " ".join(sys.argv[1:]) or '"Yardım eder misin?" diye sordu karınca. İkisi Alev\'e teşekkür etti.'
    print(temizle(ornek))
    print(kodla(ornek), N_SEMBOL)
