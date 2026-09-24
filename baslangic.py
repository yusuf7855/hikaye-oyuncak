"""Figür okutulunca modele verilecek başlangıç ve yasaklı token listesi.

Oyuncak (ESP32) aynı mantığı uygular:
  1. başlık  : "Karakter: tavşan, tilki | Yer: orman\n\n"   (eğitimdeki biçim, katalog sırası)
  2. ilk cümle: "<açılış> Pamuk adında bembeyaz bir tavşan ile Kızıl adında turuncu bir tilki yaşardı."
     -> doğru isimler baştan bağlamda olur, model onları takip eder.
  3. yasak   : okutulmayan figürlerin isimleri + TinyStories'ten kalan yabancı isimler üretilemez.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
KATALOG = json.load(open(os.path.join(HERE, "data", "karakterler.json"), encoding="utf-8"))
KAR = {k["kimlik"]: k for k in KATALOG["karakterler"]}
YER = {y["kimlik"]: y for y in KATALOG["yerler"]}
SIRA = [k["kimlik"] for k in KATALOG["karakterler"]]
# Genel Türkçe veride sık geçen, oyuncak dünyasına ait olmayan isimler.
# Türkçede sıradan kelime olanlar bilerek yok: "Ben" (zamir), "Umut", "Ada", "Ege", "Nil", "Ela" yasaklanınca
# model "Ben de geleceğim" gibi cümleleri kuramıyordu.
YABANCI = ["Lily", "Tim", "Tom", "Sara", "Sue", "Max", "Lucy", "Anna", "Jack", "Mia", "Sam", "Timmy",
           "Bob", "Jane", "Spot", "Fluffy", "Amy", "Zeynep", "Ali", "Ayşe", "Mehmet", "Ahmet", "Boncuk",
           "Mert", "Defne", "Kerem", "Emir", "Zıpzıp"]


# Hikâye temaları (data/oyuncak_v3/KILAVUZ.md sırası). Başlığa "| Tema: <tema>" olarak girer (prepare_ft2 --tema).
TEMALAR = ["paylaşmak", "yeni arkadaş edinmek", "korkuyu yenmek", "kaybolan bir şeyi bulmak", "yardım etmek",
           "özür dilemek", "sabırlı olmak", "doğayı korumak", "sırasını beklemek", "dürüstlük", "merak ve keşif",
           "hasta bir arkadaşa bakmak", "farklılıklara saygı", "birlikte çalışmak", "hatadan öğrenmek",
           "doğum günü sürprizi", "kıskançlığı yenmek", "uyku vakti", "yağmur ya da kar günü", "teşekkür etmek"]


def baslangic(kimlikler, yer_kimlik, ilk_cumle=True, tema=None):
    kar = sorted((KAR[k] for k in kimlikler), key=lambda k: SIRA.index(k["kimlik"]))
    yer = YER[yer_kimlik]
    ek = f" | Tema: {tema}" if tema else ""
    metin = f"Karakter: {', '.join(k['tur'] for k in kar)} | Yer: {yer['ad']}{ek}\n\n"
    if ilk_cumle:
        tanit = " ile ".join(f"{k['isim']} adında {k['sifat']} bir {k['tur']}" for k in kar)
        metin += f"{yer['acilis']} {tanit} yaşardı."
    return metin


def prompt_idler(tok, kimlikler, yer_kimlik, tema=None, eot=False):
    """Başlığın token'ları, eğitimdeki gibi. Eğitimde başlığın ardından hikâye gelir ve "\n\n" iki ayrı
    token olur; başlık tek başına kodlanınca sondaki "\n\n" tek (eğitimde hiç görülmemiş) bir token'a
    dönüşüyordu. Bu yüzden başlık + örnek bir ilk kelime kodlanır ve yalnızca başlığa düşen token'lar alınır."""
    metin = baslangic(kimlikler, yer_kimlik, ilk_cumle=False, tema=tema)
    enc = tok.encode(metin + "Bir")
    ids = [i for i, (_, son) in zip(enc.ids, enc.offsets) if son <= len(metin)]
    # eot=True: eğitimde her hikâye bir önceki hikâyenin <|endoftext|>'inden sonra gelir
    return ([tok.token_to_id("<|endoftext|>")] if eot else []) + ids


def yasak_idler(tok, kimlikler):
    """Okutulmayan figür isimleri + yabancı isimler için yasaklanacak token id'leri."""
    secili = {KAR[k]["isim"] for k in kimlikler}
    isimler = [k["isim"] for k in KAR.values() if k["isim"] not in secili] + [n for n in YABANCI if n not in secili]
    idler = set()
    for n in isimler:
        for v in (" " + n, n):
            enc = tok.encode(v).ids
            if len(enc) == 1:
                idler.add(enc[0])
            elif tok.decode([enc[0]]).strip()[:1].isupper() and len(tok.decode([enc[0]]).strip()) >= 3:
                idler.add(enc[0])  # çok parçalı isim: büyük harfli ilk parçayı kes
    return sorted(idler)
