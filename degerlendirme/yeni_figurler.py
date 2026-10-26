"""Lisanssız yeni figürler (ürün sahibi, 26 Ekim 2026): kart taslakları ve ürün listesi girdileri.

    python degerlendirme/yeni_figurler.py yaz       # data/yeni_figurler.json (kartlar + ürün listesi girdileri + kaynaklar)
    python degerlendirme/yeni_figurler.py kontrol   # mevcut kartlarla birleştirip veri_hakem kart-kontrol'den geçirir
    python degerlendirme/yeni_figurler.py ozet      # docs/YENI_FIGURLER.md (ürün sahibinin okuyacağı özet)

Kartlar data/urun_kartlari.json şemasında (docs/KUSURSUZ_VERI.md). Masal karakterleri 'populer' (kaynak: Vikipedi),
bizim karakterlerimiz 'temel' (yanlar isimsiz hayvanlar). Onaylanınca urun_kartlari.json'a ve urun_figurleri.json'a
eklenir; o zamana kadar onayli: false.
"""
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KOK, "data", "yeni_figurler.json")
ERISIM = "2026-10-26"

KAYNAKLAR = {
    "kullanici_karari_yeni": {"tur": "kullanici", "baslik": "Ürün sahibinin lisanssız figür listesi (26 Ekim 2026)",
                              "dosya": "docs/YENI_FIGURLER.md", "erisim": ERISIM},
    "vikipedi_pamuk_prenses": {"tur": "vikipedi", "baslik": "Pamuk Prenses ve Yedi Cüceler (Grimm Kardeşler, 1812)",
                               "url": "https://tr.wikipedia.org/wiki/Pamuk_Prenses", "erisim": ERISIM},
    "vikipedi_pinokyo": {"tur": "vikipedi", "baslik": "Pinokyo (Carlo Collodi, Pinokyo'nun Serüvenleri, 1883)",
                         "url": "https://tr.wikipedia.org/wiki/Pinokyo", "erisim": ERISIM},
    "vikipedi_en_pinokyo": {"tur": "vikipedi", "baslik": "The Adventures of Pinocchio (Collodi, 1883)",
                            "url": "https://en.wikipedia.org/wiki/The_Adventures_of_Pinocchio", "erisim": ERISIM},
    "vikipedi_alaaddin": {"tur": "vikipedi", "baslik": "Alaaddin'in Sihirli Lambası (Binbir Gece Masalları)",
                          "url": "https://tr.wikipedia.org/wiki/Alaaddin%27in_Sihirli_Lambas%C4%B1", "erisim": ERISIM},
    "vikipedi_nasreddin": {"tur": "vikipedi", "baslik": "Nasreddin Hoca",
                           "url": "https://tr.wikipedia.org/wiki/Nasreddin_Hoca", "erisim": ERISIM},
}
UK, UT, KK = ["urun_karari"], ["urun_kurali"], ["kullanici_karari_yeni"]


def o(deger, kaynak, **ek):
    d = {"deger": deger, "kaynak": list(kaynak)}
    d.update(ek)
    return d


def oz(deger, kok, ifade, bicimler, kaynak):
    return {"deger": deger, "anahtar_kok": kok, "anahtar_ifade": ifade, "ornek_bicimler": bicimler, "kaynak": list(kaynak)}


def yer(etiket, tarif, kaynak, karsilik="urun_tanimi", not_=None):
    d = {"etiket": etiket, "tarif": tarif, "dizide_karsiligi": karsilik, "kaynak": list(kaynak)}
    if not_:
        d["not"] = not_
    return d


def yan(kimlik, kisa, tip, bicimler, iliski, tur, konusur, kaynak, yerler=None, resmi=None):
    d = {"yan_kimlik": "yan:" + kimlik, "kisa_ad": kisa, "tip": tip, "yuzey_bicimleri": bicimler,
         "iliski": o(iliski, kaynak), "tur": o(tur, kaynak), "konusur": o(konusur, kaynak)}
    if resmi:
        d["resmi_ad"] = resmi
    if yerler:
        d["yerler"] = o(yerler, UT, not_="Doğa hayvanı yalnız yaşadığı yerde bulunur (tohum dünyası kuralı).")
    return d


def hayvan(kimlik, ad, yerler=None, kaynak=UK):
    """İsimsiz, konuşan doğa hayvanı yanı (kullanıcı kararı 3). Masal kartında kaynak masal + kullanıcı kararı."""
    return yan(kimlik, ad, "isimsiz", [ad], "Figürün dünyasında yaşayan bir doğa hayvanı.", ad, True, kaynak, yerler)


def kural(metin, ifadeler, kaynak):
    return {"kural": metin, "yasak_duzenli_ifadeler": ifadeler, "kaynak": list(kaynak)}


KONUSMA = r"(?:dedi|sordu|söyledi|konuştu|anlattı|seslendi|fısıldadı|bağırdı|cevap\s+verdi)"


def konusmaz(adlar):
    a = "(?:" + "|".join(adlar) + ")"
    return [KONUSMA + r"\s+" + a + r"\b", a + r"\b\s+(?:[\w']+\s+){0,3}" + KONUSMA + r"\b"]


DOGA = ["teknoloji", "cagdas_arac", "arac", "cagdas", "ev_esyasi", "mutfak", "giysi", "okul", "hazir_yiyecek",
        "bostan", "calgi", "buyu"]
MASAL = ["teknoloji", "cagdas_arac", "arac", "cagdas"]


def kart(kimlik, grup, ad, seri, kimlik_c, tur, lemmalar, ozellikler, guvenli, yerler, yanlar, kurallar, yasak_adlar,
         yasak_ogeler, izinli, eslesme, tohum_yasak, kararlar, kaynak, ornekler=None, k7=None):
    k = {"kimlik": kimlik, "grup": grup, "onayli": False, "ad": o(ad, UK + kaynak[-1:]), "okunus": o(ad.lower(), UT),
         "seri": o(seri, UK + kaynak[-1:]), "kimlik_cumlesi": o(kimlik_c, kaynak), "tur": o(tur, kaynak, lemmalar=lemmalar),
         "ozellikler": ozellikler, "guvenli_ozellik_kullanimi": o(guvenli, UT), "yerler": yerler, "yanlar": yanlar,
         "dunya_kurallari": kurallar, "yasaklar": {"adlar": yasak_adlar, "ogeler": yasak_ogeler},
         "izinli_dunya_kokleri": izinli, "urun_yan_eslesmesi": eslesme, "acik_noktalar": [],
         "tohum_yasak_kategoriler": o(tohum_yasak, UT + KK, not_="Tohum kelimesi dünyaya uyar."), "kararlar": kararlar}
    if ornekler:
        k["kural_ornekleri"] = ornekler
    if k7:
        k["k7_izinli"] = k7
    return k


def esle(yanlar):
    return [{"urun": y["kisa_ad"], "kart": [y["yan_kimlik"]]} for y in yanlar]


def kartlar():
    out = []
    # ---------------------------------------------------------------- masal karakterleri (popüler)
    vp = ["vikipedi_pamuk_prenses"]
    yanlar = [yan("cuce", "en küçük cüce", "rol", ["en küçük cüce", "küçük cüce", "cüce"],
                  "Pamuk Prenses'le aynı evde yaşayan yedi cüceden en küçüğü; onun en yakın arkadaşı.", "cüce", True, vp),
              yan("cuceler", "cüceler", "rol", ["cüceler", "yedi cüce"],
                  "Ormandaki küçük evde yaşayan yedi cüce; gündüz çalışır, akşam eve döner.", "cüce", False, vp + KK),
              hayvan("tavsan", "tavşan", ["orman", "bahçe"], vp + KK), hayvan("kus", "kuş", None, vp + KK)]
    out.append(kart(
        "pamuk_prenses", "populer", "Pamuk Prenses", "Pamuk Prenses ve Yedi Cüceler (Grimm masalı)",
        "Pamuk Prenses, ormandaki küçük bir evde cücelerle yaşayan nazik bir prensestir.", "prenses",
        ["prenses", "kız"],
        [oz("Herkese karşı nazik ve yardımseverdir.", "nazik", r"\bnazik\w*", ["nazik", "nazikçe"], vp),
         oz("Şarkı söylemeyi çok sever.", "şarkı", r"\bşarkı\w*", ["şarkı", "şarkısını"], vp + KK),
         oz("Evi temiz ve düzenli tutmayı sever.", "düzen", r"\bdüzen\w*", ["düzenli", "düzenledi"], vp)],
        "Yardımseverliği tek başına uzak yerlere gitmek olarak gösterilmez; yardım ederken hep evin ve bahçenin yakınında kalır.",
        [yer("orman", "Evin çevresindeki yeşil orman; çiçekler ve küçük patikalar vardır.", vp, "dogrulandi"),
         yer("ev", "Cücelerin ormandaki küçük evi; yedi küçük yatağı ve küçük bir masası vardır.", vp, "dogrulandi"),
         yer("bahçe", "Küçük evin önündeki çiçekli bahçe.", UK + KK, "urun_tanimi"),
         yer("şato", "Pamuk Prenses'in eskiden yaşadığı taş saray; bahçesi ve yüksek kapıları vardır.", vp, "kismen",
             "Masalda saray kötü kraliçenindir; kraliçe hikayeye girmez, saray yalnız güzel bir yer olarak anlatılır.")],
        yanlar,
        [kural("Kötü kraliçe, sihirli ayna, avcı ve zehirli elma hikayeye girmez.",
               [r"\b[Kk]raliçe\w*", r"\b[Aa]yna\w*\s+(?:[\w']+\s+){0,2}(?:konuştu|dedi|cevap)", r"\b[Zz]ehir\w*",
                r"\b[Aa]vcı\w*"], vp + UT),
         kural("Cüceler topluca konuşmaz; konuşan yalnız en küçük cücedir.", konusmaz(["[Cc]üceler", "[Yy]edi\\s+cüce"]),
               UT),
         kural("Prens, düğün, evlilik ve uzun uyku hikayeye girmez.",
               [r"\b[Pp]rens(?!es)\w*", r"\b[Dd]üğün\w*", r"\b[Ee]vlen\w*"], vp + UT)],
        [{"ad": "Kraliçe", "kaynak": vp, "belirsiz": True}, {"ad": "Prens", "kaynak": vp, "belirsiz": True}],
        [o("Büyü, cadı, zehir ve korkutucu kılık değiştirme hikayeye girmez.", vp + UT)],
        ["cüce", "şarkı"], esle(yanlar), MASAL,
        ["Masalın kötü kısmı (kraliçe, zehirli elma, avcı) çıkarıldı; yalnız ormandaki evde cücelerle mutlu yaşam kaldı.",
         "Cüceler adsız: Disney'in cüce adları kullanılmaz."], vp,
        ornekler=(["Kraliçe saraydan çıktı.", "Zehirli bir elma getirdi.", "Prens atına bindi.",
                   '"Gel," dedi cüceler.'],
                  ["En küçük cüce güldü.", "Pamuk Prenses elmayı yıkadı.", "Cüceler eve döndü."])))
    vpi = ["vikipedi_pinokyo", "vikipedi_en_pinokyo"]
    yanlar = [yan("gepetto", "Gepetto Usta", "adli", ["Gepetto Usta", "Gepetto", "usta", "babası"],
                  "Pinokyo'yu tahtadan yapan yaşlı ve iyi kalpli marangoz; onun babasıdır.", "dede", True, vpi),
              yan("circir", "cırcır böceği", "rol", ["cırcır böceği", "böcek"],
                  "Pinokyo'ya doğruyu söyleyen ve ona yol gösteren konuşan cırcır böceği.", "böcek", True, vpi),
              hayvan("kus", "kuş", None, vpi + KK), hayvan("kopek", "köpek", ["ev", "park"], vpi + KK)]
    out.append(kart(
        "pinokyo", "populer", "Pinokyo", "Pinokyo'nun Serüvenleri (Collodi masalı)",
        "Pinokyo, yaşlı bir marangozun tahtadan yaptığı meraklı bir kukladır.", "kukla", ["kukla", "çocuk", "oğlan"],
        [oz("Tahtadan yapılmıştır.", "tahta", r"\btahta\w*", ["tahtadan", "tahta"], vpi),
         oz("Yalan söylediğinde burnu biraz uzar, doğruyu söyleyince eski haline döner.", "burn",
            r"\bburn\w*|\bburun\w*", ["burnu", "burun"], vpi),
         oz("Her şeyi merak eder ve yeni şeyler öğrenmek ister.", "merak", r"\bmerak\w*", ["meraklı", "merakla"], vpi)],
        "Burnunun uzaması yalnız komik ve küçük bir şey olarak gösterilir; ceza ya da korku değildir. Doğruyu söyleyince burnu hemen eski haline döner. Merakı tek başına uzağa gitmek olarak gösterilmez.",
        [yer("ev", "Yaşlı marangozun küçük atölyesi; tahta oyuncaklar ve aletler vardır.", vpi, "dogrulandi"),
         yer("park", "Kasabanın meydanı; çeşmesi ve ağaçları vardır.", UK + KK, "urun_tanimi"),
         yer("orman", "Kasabanın yanındaki orman.", vpi, "kismen", "Masalda ormanda kötü karakterler var; onlar girmez.")],
        yanlar,
        [kural("Tilki, kedi ve dev balık hikayeye girmez; kimse Pinokyo'yu kandırmaz ya da yutmaz.",
               [r"\b[Tt]ilki\w*", r"\b[Yy]ut(?:tu|ar|mak)\w*", r"\b[Dd]ev\s+balı\w*"], vpi + UT),
         kural("Pinokyo eşeğe dönüşmez ve kimse onu cezalandırmaz.", [r"\beşeğe\s+dönüş\w*", r"\b[Cc]eza\w*"], vpi + UT),
         kural("Gepetto Usta Pinokyo'nun babasıdır; annesi hikayede yoktur.", [r"Pinokyo'nun\s+anne"], vpi)],
        [{"ad": "Mavi Peri", "kaynak": vpi}, {"ad": "Jiminy", "kaynak": vpi}, {"ad": "Lambalı", "kaynak": vpi,
                                                                              "belirsiz": True}],
        [o("Kötü kukla tiyatrosu sahibi, hırsızlar ve büyü hikayeye girmez.", vpi + UT)],
        ["kukla", "tahta", "marangoz", "cırcır", "atölye"], esle(yanlar), MASAL,
        ["Burun uzaması komik bir işaret olarak kalır; ceza ve korku yok.",
         "Ürün sahibi kararı (26 Ekim 2026, seçenek 1): burun özelliği seçilen hikayede Pinokyo küçük bir yalan söyler, "
         "burnu biraz uzar, doğruyu söyleyince eski haline döner ve herkes güler. Bu figür için 'figürün kendi hatası "
         "yalnız özür temasında olur' kuralının istisnasıdır; yalan hep küçük ve zararsızdır, kimse üzülmez.",
         "Disney'deki adlar (Jiminy) kullanılmaz; Collodi'deki adsız konuşan cırcır böceği kullanılır."], vpi,
        ornekler=(["Tilki ona yaklaştı.", "Dev balık onu yuttu.", "Pinokyo'nun annesi geldi."],
                  ["Pinokyo'nun burnu biraz uzadı.", "Gepetto Usta güldü.", "Cırcır böceği ötüyordu."])))
    va = ["vikipedi_alaaddin"]
    yanlar = [yan("ana", "annesi", "rol", ["annesi", "anne", "anneciğim"],
                  "Alaaddin'in annesi; onunla küçük bir evde yaşar.", "anne", True, va),
              yan("cin", "lamba cini", "rol", ["lamba cini", "cin", "Lamba Cini"],
                  "Eski lambadan çıkan iyi kalpli ve şakacı cin; Alaaddin'in arkadaşıdır.", "cin", True, va + KK),
              hayvan("kedi", "kedi", ["ev", "bahçe", "park"], va + KK), hayvan("kus", "kuş", None, va + KK)]
    out.append(kart(
        "alaaddin", "populer", "Alaaddin", "Alaaddin'in Sihirli Lambası (Binbir Gece Masalları)",
        "Alaaddin, annesiyle küçük bir evde yaşayan cesur ve iyi kalpli bir çocuktur.", "oğlan", ["oğlan", "çocuk"],
        [oz("Eski bir lambası vardır; lambayı ovunca içinden bir cin çıkar.", "lamba", r"\blamba\w*", ["lamba", "lambayı"],
            va),
         oz("Arkadaşlarına yardım etmeyi sever.", "yardım", r"\byardım\w*", ["yardım", "yardımcı"], va + KK),
         oz("Yeni yerler görmeyi ve keşfetmeyi sever.", "keşf", r"\bkeşf\w*|\bkeşif\w*", ["keşfetti", "keşif"], KK + va)],
        "Cin yalnız küçük, iyi ve eğlenceli şeyler yapar; kimseyi korkutmaz. Keşif tek başına uzağa gitmek ya da karanlık bir yere girmek olarak gösterilmez.",
        [yer("ev", "Alaaddin'in annesiyle yaşadığı küçük ev.", va, "dogrulandi"),
         yer("park", "Kasabanın renkli çarşısı ve meydanı; çeşmesi vardır.", va, "kismen", "Masalda çarşı geçer; ayrıntı ürün kararı."),
         yer("bahçe", "Meyve ağaçları olan büyük bir bahçe.", va, "kismen", "Masaldaki mağara bahçesi; mağara girmez."),
         yer("şato", "Kasabanın büyük ve güzel sarayı; bahçesi ve yüksek kapıları vardır.", va, "dogrulandi")],
        yanlar,
        [kural("Kötü büyücü ve hırsızlar hikayeye girmez; kimse lambayı çalmaz.",
               [r"\b[Bb]üyücü\w*", r"\b[Hh]ırsız\w*", r"\bçal(?:dı|mak|ındı)\b"], va + UT),
         kural("Cin altın, zenginlik ya da güç vermez; küçük ve eğlenceli yardımlar yapar.",
               [r"\b[Aa]ltın\w*", r"\b[Zz]engin\w*"], UT + KK),
         kural("Mağara, yer altı ve karanlık yerler hikayeye girmez.", [r"\b[Mm]ağara\w*", r"\b[Yy]er\s*altı\w*"], va + UT)],
        [{"ad": "Cafer", "kaynak": va}, {"ad": "Yasemin", "kaynak": va}, {"ad": "Abu", "kaynak": va}],
        [o("Uçan halı ve Disney'e özgü karakterler hikayeye girmez.", va + UT)],
        ["lamba", "cin", "çarşı"], esle(yanlar), MASAL,
        ["Disney'e özgü adlar (Yasemin, Cafer, Abu) ve uçan halı kullanılmaz.",
         "Cin dilek dağıtıp zenginlik getirmez; küçük, eğlenceli yardımlar yapar (kullanıcı kararı)."], va,
        ornekler=(["Büyücü kapıyı çaldı.", "Cin ona altın verdi.", "Bir mağaraya girdiler."],
                  ["Lamba cini güldü.", "Alaaddin lambayı ovdu.", "Annesi çorba yaptı."])))
    vn = ["vikipedi_nasreddin"]
    yanlar = [yan("esek", "eşeği", "rol", ["eşek", "eşeği", "eşeğine"],
                  "Nasreddin Hoca'nın eşeği; Hoca bazen ona ters biner.", "eşek", False, vn + KK),
              yan("komsu", "komşusu", "rol", ["komşu", "komşusu", "komşular"],
                  "Hoca'nın iyi kalpli komşusu; birlikte gülerler.", "komşu", True, vn + KK),
              hayvan("kedi", "kedi", ["ev", "bahçe", "park"], vn + KK), hayvan("kus", "kuş", None, vn + KK)]
    out.append(kart(
        "nasreddin_hoca", "populer", "Nasreddin Hoca", "Nasreddin Hoca fıkraları",
        "Nasreddin Hoca, Akşehir'de yaşayan akıllı ve güler yüzlü bir dededir.", "dede", ["dede", "hoca"],
        [oz("Herkesi güldüren komik cevaplar verir.", "komik", r"\bkomik\w*", ["komik", "komikti"], vn),
         oz("Eşeğine bazen ters biner.", "ters", r"\bters\w*", ["ters", "tersine"], vn),
         oz("Akıllı fikirleriyle sorunları çözer.", "fikir", r"\bfikir\w*|\bfikr\w*", ["fikir", "fikri"], vn)],
        "Ters binmek yalnız yavaş yürüyen eşekte komik bir şey olarak gösterilir; kimse düşmez. Kimseyle alay etmez.",
        [yer("ev", "Hoca'nın Akşehir'deki küçük evi.", vn, "kismen", "Fıkralarda evi geçer; tarif ürün kararı."),
         yer("park", "Akşehir'in meydanı ve pazarı.", vn, "kismen", "Fıkralarda pazar geçer."),
         yer("bahçe", "Hoca'nın evinin önündeki bahçe; ceviz ağacı vardır.", vn, "kismen", "Ceviz ağacı fıkrası."),
         yer("dağ", "Akşehir'in yakınındaki tepe.", UK + KK, "dogrulanmadi", "Ürün kararı.")],
        yanlar,
        [kural("Hoca'nın eşeği konuşmaz; yük taşır, başını sallar, anırır.", konusmaz(["[Ee]şe[kğ]\\w*"]), vn),
         kural("Kimse kızmaz, kavga etmez; şakalar herkesi güldürür.", [r"\b[Kk]avga\w*", r"\b[Dd]öv\w*"], UT)],
        [{"ad": "Timur", "kaynak": vn}, {"ad": "Kadı", "kaynak": vn, "belirsiz": True}],
        [o("Kadı, hükümdar, savaş ve borç fıkraları hikayeye girmez.", vn + UT)],
        ["hoca", "ters", "Akşehir"], esle(yanlar), MASAL,
        ["Eşek konuşmaz (Karakaçan kararıyla aynı).", "Yetişkin konulu fıkralar (kadı, borç, hükümdar) girmez."], vn,
        ornekler=(['"Hadi," dedi eşek.', "Komşusuyla kavga etti."],
                  ["Hoca eşeğine ters bindi.", "Eşek anırdı.", "Komşusu güldü."])))
    # ---------------------------------------------------------------- bizim karakterlerimiz (temel)
    def temel(kimlik, ad, kimlik_c, tur, lem, ozl, guvenli, yerler, hayvanlar, kurallar, izinli, kararlar, ornekler):
        yl = [hayvan(*h) for h in hayvanlar]
        return kart(kimlik, "temel", ad, "temel figür", kimlik_c, tur, lem, ozl, guvenli, yerler, yl, kurallar, [], [],
                    izinli, esle(yl), DOGA, kararlar, KK, ornekler=ornekler)
    out.append(temel(
        "bulut", "Bulut", "Bulut, bembeyaz ve yumuşak tüylü, sevecen bir kedidir.", "kedi", ["kedi"],
        [oz("Tüyleri bembeyaz ve yumuşaktır.", "beyaz", r"\bbeyaz\w*|\bbembeyaz\w*", ["bembeyaz", "beyaz"], KK),
         oz("Sevinince mırlar.", "mırla", r"\bmırla\w*|\bmırıl\w*", ["mırladı", "mırlayarak"], KK),
         oz("Güneşte uyuklamayı sever.", "uyukla", r"\buyukla\w*", ["uyukladı", "uyuklamak"], KK)],
        "Uyuklamayı yalnız güneşli ve güvenli bir yerde yapar; yükseğe tırmanmaz, suya girmez.",
        [yer("ev", "Sıcak ve rahat bir ev; pencerenin önünde güneşli bir minder vardır.", KK),
         yer("bahçe", "Çiçekli bir bahçe; kelebekler uçar.", KK), yer("park", "Çimenleri ve ağaçları olan bir park.", KK)],
        [("kelebek", "kelebek", ["bahçe", "park"]), ("kus", "kuş"), ("fare", "fare", ["ev", "bahçe"])],
        [kural("Bulut hiçbir hayvanı kovalamaz, yakalamaz ya da yemez; fare ve kuş onun arkadaşıdır.",
               [r"\b(?:[Ff]are|[Kk]uş|[Kk]elebe[kğ])\w*\s+(?:[\w']+\s+){0,2}(?:kovaladı|yakaladı|yedi)\b"], UT)],
        ["mırla"], ["Pamuk adı Pamuk Prenses yüzünden kullanılmaz; beyaz kedinin adı Bulut (kullanıcı onayı)."],
        (["Fareyi hızla kovaladı."], ["Bulut topu yakaladı.", "Kuş ağaca kondu."])))
    out.append(temel(
        "zipzip", "Zıpzıp", "Zıpzıp, zıplamayı çok seven neşeli bir tavşandır.", "tavşan", ["tavşan"],
        [oz("Her yere zıplayarak gider.", "zıpla", r"\bzıpla\w*|\bzıpl\w*", ["zıpladı", "zıplayarak"], KK),
         oz("Uzun kulakları vardır.", "kulak", r"\bkula[kğ]\w*", ["kulakları", "kulağı"], KK),
         oz("Havucu çok sever.", "havuç", r"\bhavu[cç]\w*", ["havuç", "havucu"], KK)],
        "Zıplarken yükseğe çıkmaz, kimseye çarpmaz; zıplaması hep yumuşak ve kısadır.",
        [yer("bahçe", "Sebzeli ve çiçekli bir bahçe.", KK), yer("orman", "Büyük ağaçları olan yeşil bir orman.", KK),
         yer("park", "Çimenleri olan bir park.", KK)],
        [("kirpi", "kirpi", ["bahçe", "orman"]), ("sincap", "sincap", ["orman", "park"]), ("kus", "kuş")],
        [kural("Hayvanlar tek tek konuşabilir; arka plandaki hayvan toplulukları konuşmaz.", [], UT)],
        ["zıpla", "havuç"], ["Pamuk (tavşan kartı) yerine yeni kart: ad Zıpzıp (kullanıcı onayı)."], ([], ["Zıpzıp havucu yedi."])))
    out.append(temel(
        "tontis", "Tontiş", "Tontiş, kocaman ama çok yumuşak kalpli, sevimli bir dinozordur.", "dinozor", ["dinozor"],
        [oz("Kocamandır ama çok dikkatli yürür.", "dikkat", r"\bdikkat\w*", ["dikkatli", "dikkatle"], KK),
         oz("Yaprak ve meyve yemeyi sever.", "yaprak", r"\byaprak\w*", ["yaprak", "yaprakları"], KK),
         oz("Küçük ve tatlı bir sesle kükrer.", "kükre", r"\bkükre\w*|\bkükr\w*", ["kükredi", "kükreyerek"], KK)],
        "Büyüklüğü kimseyi korkutmaz ve hiçbir şeyi kırmaz; kükremesi küçük ve tatlıdır.",
        [yer("orman", "Kocaman ağaçları olan yeşil bir orman.", KK), yer("dağ", "Çiçekli ve taşlı bir tepe.", KK),
         yer("park", "Çimenleri ve ağaçları olan büyük bir park.", KK)],
        [("kus", "kuş"), ("kaplumbaga", "kaplumbağa", ["orman", "park"]), ("kelebek", "kelebek", ["orman", "dağ", "park"])],
        [kural("Tontiş et yemez, kimseyi kovalamaz ve korkutmaz.",
               [r"\b[Ee]t\s+ye\w*", r"\bkorkut\w*", r"\bkovala\w*"], UT)],
        ["dinozor", "kükre"], ["Dinozor otobur ve yumuşak kalpli; korku öğesi yok."],
        (["Tontiş kuşu kovaladı.", "Herkesi korkuttu."], ["Tontiş yaprakları yedi.", "Kuş güldü."])))
    out.append(temel(
        "bilge_baykus", "Bilge Baykuş", "Bilge Baykuş, çok şey bilen ve soru sormayı seven yaşlı bir baykuştur.", "baykuş",
        ["baykuş"],
        [oz("Çok şey bilir ve bildiklerini anlatmayı sever.", "bil", r"\bbili[ry]\w*|\bbilg\w*", ["bilir", "bilgi"], KK),
         oz("Kocaman, yuvarlak gözleri vardır.", "göz", r"\bgöz\w*", ["gözleri", "gözlerini"], KK),
         oz("Geceleri uyanıktır, gündüz biraz uykuludur.", "uyku", r"\buyku\w*", ["uykulu", "uykusu"], KK)],
        "Bilgisini yardım etmek için kullanır; kimseyi küçümsemez. Geceleri yalnız yıldızlara bakar, karanlıkta kimse yolunu kaybetmez.",
        [yer("orman", "Kocaman bir meşe ağacının olduğu orman; Bilge Baykuş'un yuvası bu ağaçtadır.", KK),
         yer("dağ", "Ağaçları olan bir tepe.", KK), yer("gökyüzü", "Yıldızlı ve sakin gece göğü.", KK)],
        [("sincap", "sincap", ["orman", "dağ"]), ("tavsan", "tavşan", ["orman", "dağ"]),
         ("kirpi", "kirpi", ["orman", "dağ"])],
        [kural("Bilge Baykuş hiçbir hayvanı avlamaz, yakalamaz ya da yemez.",
               [r"\b(?:[Ff]are|[Tt]avşan|[Ss]incap|[Ss]incab)\w*\s+(?:[\w']+\s+){0,2}(?:avladı|yakaladı|yedi)\b"], UT)],
        ["baykuş", "yuva"], ["Baykuş avcı değil; bilge bir öğretmen gibi."],
        (["Fareyi yakaladı."], ["Bilge Baykuş bir soru sordu.", "Sincap güldü."])))
    out.append(temel(
        "ejderha_yavrusu", "Ejderha Yavrusu", "Ejderha Yavrusu, ağzından baloncuk üfleyen küçük ve şirin bir ejderhadır.",
        "ejderha", ["ejderha"],
        [oz("Ağzından renkli baloncuklar üfler.", "baloncuk", r"\bbaloncu\w*", ["baloncuk", "baloncukları"], KK),
         oz("Küçük kanatlarıyla uçmayı öğreniyor.", "kanat", r"\bkanat\w*", ["kanatları", "kanatlarını"], KK),
         oz("Çok meraklı ve neşelidir.", "neşe", r"\bneşe\w*", ["neşeli", "neşeyle"], KK)],
        "Uçarken alçakta kalır ve hep dikkatlidir; baloncukları kimseye zarar vermez.",
        [yer("dağ", "Çiçekli, yeşil bir tepe; ejderhanın yuvası buradadır.", KK),
         yer("gökyüzü", "Bulutlu ve güneşli gökyüzü.", KK), yer("orman", "Yeşil bir orman.", KK),
         yer("şato", "Tepedeki eski ve boş taş saray; bahçesinde çiçekler vardır.", KK)],
        [("kus", "kuş"), ("kelebek", "kelebek", ["dağ", "orman"]), ("sincap", "sincap", ["orman", "dağ"])],
        [kural("Ejderha Yavrusu ateş üflemez, hiçbir şeyi yakmaz.", [r"\b[Aa]teş\w*", r"\b[Yy]ak(?:tı|mak|ar)\b"], UT),
         kural("Şövalye, savaş ve canavar hikayeye girmez.", [r"\b[Şş]övalye\w*", r"\b[Ss]avaş\w*", r"\b[Cc]anavar\w*"], UT)],
        ["ejderha", "baloncuk"], ["Ateş yok: baloncuk üfler (kullanıcıya önerildi, onaylandı)."],
        (["Ağzından ateş üfledi.", "Şövalye geldi."], ["Baloncuklar uçtu.", "Kuş güldü."])))
    out.append(temel(
        "tek_boynuzlu_at", "Tek Boynuzlu At", "Tek Boynuzlu At, alnında parlayan bir boynuzu olan nazik bir attır.", "at",
        ["at"],
        [oz("Alnındaki boynuzu karanlıkta parlar.", "boynuz", r"\bboynuz\w*", ["boynuzu", "boynuz"], KK),
         oz("Yelesi gökkuşağı renklerindedir.", "yele", r"\byele\w*", ["yelesi", "yelesini"], KK),
         oz("Çok naziktir ve herkese yardım eder.", "nazik", r"\bnazik\w*", ["nazik", "nazikçe"], KK)],
        "Boynuzuyla kimseyi itmez; boynuzu yalnız yolu aydınlatmak için parlar.",
        [yer("gökyüzü", "Bulutların üstü; gökkuşağı vardır.", KK), yer("orman", "Çiçekli bir orman.", KK),
         yer("bahçe", "Çiçeklerle dolu büyük bir bahçe.", KK), yer("dağ", "Yeşil bir tepe.", KK)],
        [("kelebek", "kelebek", ["orman", "bahçe", "dağ"]), ("kus", "kuş"), ("tavsan", "tavşan", ["orman", "bahçe"])],
        [kural("Hayvanlar tek tek konuşabilir; arka plandaki hayvan toplulukları konuşmaz.", [], UT)],
        ["boynuz", "yele", "gökkuşağı"], ["Ad Türkçe: Tek Boynuzlu At (unicorn)."], ([], ["Tek Boynuzlu At koştu."])))
    out.append(temel(
        "bip", "Bip", "Bip, bip bip diye konuşan, yardımsever küçük bir robottur.", "robot", ["robot"],
        [oz("Konuşurken bip bip diye ses çıkarır.", "bip", r"\bbip\b", ["bip"], KK),
         oz("Gözleri ışık gibi parlar.", "ışık", r"\bışı[kğ]\w*", ["ışık", "ışığı"], KK),
         oz("Saymayı ve düzenlemeyi çok sever.", "say", r"\bsay(?:dı|mak|ar|arak|ıyor)\w*", ["saydı", "saymak"], KK)],
        "Elektrik, kablo, priz ve pil hikayeye girmez; Bip kendi kendine çalışır. Hiçbir şeyi sökmez ya da kırmaz.",
        [yer("ev", "Rahat bir ev; oyuncaklarla dolu bir oda vardır.", KK), yer("park", "Çimenleri ve ağaçları olan bir park.", KK),
         yer("bahçe", "Çiçekli bir bahçe.", KK)],
        [("kedi", "kedi", ["ev", "bahçe", "park"]), ("kus", "kuş"), ("kelebek", "kelebek", ["bahçe", "park"])],
        [kural("Elektrik, priz, kablo ve pil hikayeye girmez.",
               [r"\b[Ee]lektri\w*", r"\b[Pp]riz\w*", r"\b[Kk]ablo\w*", r"\b[Pp]il(?:i|ler|leri)?\b"], UT),
         kural("Bip hiçbir şeyi sökmez ve kırmaz.", [r"\bsök(?:tü|mek)\b"], UT)],
        ["robot", "bip"], ["Elektrik güvenliği: priz/kablo/pil yok."],
        (["Bip prize koştu.", "Kabloyu çekti."], ["Bip bip dedi.", "Kuş güldü."])))
    out.append(temel(
        "fistik", "Fıstık", "Fıstık, hortumuyla su püskürtmeyi seven neşeli bir yavru fildir.", "fil", ["fil"],
        [oz("Hortumuyla su püskürtür.", "hortum", r"\bhortum\w*", ["hortumu", "hortumuyla"], KK),
         oz("Kocaman kulaklarını yelpaze gibi sallar.", "kulak", r"\bkula[kğ]\w*", ["kulakları", "kulağını"], KK),
         oz("Arkadaşlarıyla oyun oynamayı çok sever.", "oyun", r"\boyun\w*|\boyna\w*", ["oyun", "oynadı"], KK)],
        "Su püskürtmeyi yalnız oyun olarak yapar; kimseyi ıslatıp üzmez, kimse suya girmez.",
        [yer("orman", "Büyük ağaçları olan yeşil bir orman.", KK), yer("park", "Çimenleri ve ağaçları olan bir park.", KK),
         yer("bahçe", "Çiçekli bir bahçe; küçük bir su birikintisi vardır.", KK)],
        [("kus", "kuş"), ("kaplumbaga", "kaplumbağa", ["orman", "bahçe"]), ("maymun", "maymun", ["orman", "park"])],
        [kural("Avcı ve tehlikeli hayvanlar hikayeye girmez.", [r"\b[Aa]vcı\w*", r"\b[Aa]slan\w*", r"\b[Tt]imsah\w*"], UT)],
        ["hortum", "püskürt"], ["Yavru fil; annesi yok (temel figürün yanları isimsiz hayvanlar)."],
        (["Avcı geldi."], ["Fıstık su püskürttü.", "Maymun güldü."])))
    return out


def urun_girdileri(ks):
    return [{"ad": k["ad"]["deger"], "grup": k["grup"], "seri": k["seri"]["deger"],
             "yerler": [y["etiket"] for y in k["yerler"]], "yan": [e["urun"] for e in k["urun_yan_eslesmesi"]],
             "veri": "yeni (lisanssız, 26 Ekim 2026)"} for k in ks]


def yaz():
    ks = kartlar()
    with open(CIKTI, "w", encoding="utf-8") as f:
        json.dump({"aciklama": "Lisanssız yeni figürlerin kart taslakları (onay bekliyor).", "kaynaklar": KAYNAKLAR,
                   "kartlar": ks, "urun": urun_girdileri(ks)}, f, ensure_ascii=False, indent=1)
    print(CIKTI, len(ks), "kart")


def kontrol():
    """Mevcut kart ve ürün dosyalarına yeni kartları ekleyip (geçici) kart-kontrol'den geçirir."""
    import tempfile
    sys.path.insert(0, os.path.join(KOK, "degerlendirme"))
    import veri_hakem as V
    ks = kartlar()
    kart = json.load(open(os.path.join(KOK, "data", "urun_kartlari.json"), encoding="utf-8"))
    urun = json.load(open(os.path.join(KOK, "data", "urun_figurleri.json"), encoding="utf-8"))
    kart["kaynaklar"].update(KAYNAKLAR)
    kart["kartlar"] += ks
    for g in urun_girdileri(ks):
        urun.setdefault(g["grup"], []).append({k: v for k, v in g.items() if k != "grup"})
    d = tempfile.mkdtemp()
    kp, up = os.path.join(d, "k.json"), os.path.join(d, "u.json")
    json.dump(kart, open(kp, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(urun, open(up, "w", encoding="utf-8"), ensure_ascii=False)
    hatalar, uyarilar, s = V.kart_kontrol(kp, up, None)
    yeni = {k["kimlik"] for k in ks} | {k["ad"]["deger"] for k in ks}
    for u in uyarilar:
        if any(n in u for n in yeni):
            print("UYARI:", u)
    hh = [h for h in hatalar if any(n in h for n in yeni)]
    for h in hh:
        print("HATA:", h)
    print(f"yeni kartlarda {len(hh)} hata (toplam {len(hatalar)})")
    return 1 if hh else 0



RENK = {"pamuk_prenses": ("#FF5A7A", "kırmızı-pembe"), "pinokyo": ("#E8A33D", "tahta sarısı"),
        "alaaddin": ("#8A4FFF", "mor"), "nasreddin_hoca": ("#2E9E5B", "yeşil"), "bulut": ("#FFFFFF", "beyaz"),
        "zipzip": ("#FF9EC7", "pembe"), "tontis": ("#7ED321", "açık yeşil"), "bilge_baykus": ("#B5793A", "kahverengi"),
        "ejderha_yavrusu": ("#1FB5B0", "turkuaz"), "tek_boynuzlu_at": ("#C77DFF", "lila"), "bip": ("#3B82F6", "mavi"),
        "fistik": ("#9CA3AF", "gri")}


def ozet():
    ks = kartlar()
    s = ["# Yeni figürler (lisanssız) — kart taslakları",
         "",
         "Ürün sahibinin onayladığı liste (26 Ekim 2026). Kartlar `data/yeni_figurler.json`'da, `veri_hakem.py kart-kontrol`",
         "denetiminden hatasız geçti; ürün sahibi onaylayınca `data/urun_kartlari.json`'a eklenir ve hikâye verisi üretilir.",
         "Keloğlan'ın kartı zaten var (değişmedi). NFC numaraları yeni: eski numaralar asla yeniden kullanılmaz.",
         "",
         "| NFC | Figür | Tür | Halka rengi | Yerler |", "|---|---|---|---|---|",
         "| 4 | Keloğlan | oğlan (masal) | yeşil (eski) | orman, dağ, ev, şato |"]
    for i, k in enumerate(ks):
        s.append(f"| {13 + i} | {k['ad']['deger']} | {k['tur']['deger']} ({'masal' if k['grup'] == 'populer' else 'bizim'}) | "
                 f"{RENK[k['kimlik']][1]} | {', '.join(y['etiket'] for y in k['yerler'])} |")
    s += ["", "Ay Dede (12, ninni modu) aynen kalır.", ""]
    for k in ks:
        s += [f"## {k['ad']['deger']}", "", f"**Kim:** {k['kimlik_cumlesi']['deger']}", "",
              "**Özellikleri:** " + " ".join(o_["deger"] for o_ in k["ozellikler"]), "",
              f"**Güvenlik:** {k['guvenli_ozellik_kullanimi']['deger']}", "",
              "**Yerler:** " + "; ".join(f"{y['etiket']} ({y['tarif']})" for y in k["yerler"]), "",
              "**Yanındakiler:** " + "; ".join(
                  f"{y['kisa_ad']} ({y['iliski']['deger'].rstrip('.') if y['tip'] != 'isimsiz' else 'doğa hayvanı'}"
                  f"{'' if y['konusur']['deger'] else ', konuşmaz'})" for y in k["yanlar"]), "",
              "**Hikâyeye girmeyenler:** " + " ".join(r["kural"] for r in k["dunya_kurallari"])
              + (" " + " ".join(o_["deger"] for o_ in k["yasaklar"]["ogeler"]) if k["yasaklar"]["ogeler"] else ""), ""]
        if k["kararlar"]:
            s += ["**Kararlar:** " + " ".join(k["kararlar"]), ""]
    yol = os.path.join(KOK, "docs", "YENI_FIGURLER.md")
    open(yol, "w", encoding="utf-8").write("\n".join(s) + "\n")
    print(yol)


if __name__ == "__main__":
    {"yaz": yaz, "kontrol": kontrol, "ozet": ozet}[sys.argv[1] if len(sys.argv) > 1 else "yaz"]()
