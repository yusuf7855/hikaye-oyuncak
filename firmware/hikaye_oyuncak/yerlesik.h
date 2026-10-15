// Üretildi: tools/ninniler.py (ninniler.txt). Elle değiştirme; ninniler.txt'yi düzenleyip aracı çalıştır.
// Yerleşik metinler: kartta sabit duran, modelin yazmadığı içerik. Gece figürü (Ay Dede, mod "uyku") yalnız
// bu ninnileri okur (ürün sahibinin kararı, 15 Ekim 2026: 15 sabit, bilinen anonim halk ninnisi); sırayla döner, aynı
// ninni art arda gelmez. Ninni modunda yavaş, alçak, kısık okunur; her iki dize bir cümle (arada uzun durak).
#pragma once

static const char *const NINNILER[] = {
    // Dandini dandini dastana
    "Dandini dandini dastana, danalar girmiş bostana. Kov bostancı danayı, yemesin lahanayı, nenni. Eee, "
    "eee, eee. Biner atın iyisine, düşer yolun kıyısına. Haber verin dayısına, şeker alsın kuzusuna, "
    "nenni. Eee, eee, eee.",
    // Uyusun da büyüsün
    "Uyusun da büyüsün, ninni, tıpış tıpış yürüsün, ninni. Dandini dandini danalı bebek, elleri kolları "
    "kınalı bebek. Eee, eee, eee, uyu yavrum, ninni. Lahanayı yemez, kökünü yer, benim de kuzum lokum "
    "yer. Uyusun da büyüsün, ninni, tıpış tıpış yürüsün, ninni.",
    // Fış fış kayıkçı
    "Fış fış kayıkçı, kayıkçının küreği. Hop hop eder yüreği, akşama fincan böreği. Yavrum yesin büyüsün, "
    "tıpış tıpış yürüsün. Fış fış kayıkçı, kayıkçıya gidelim. Kayığına binelim, denizlerde gezelim. Akşam "
    "eve gidelim. Eee, eee, eee.",
    // E bebeğim
    "Minik minik kolları, düşmüş iki yanına. Başı düşmüş yastığa, uyuyor mışıl mışıl. E bebeğim, eee, "
    "eee, e bebeğim, eee, eee.",
    // Ninni ninni ninnice
    "Ninni ninni ninnice, akşam baban gelince. Hani yavrum deyince, seni önüne koyunca. Öpüp karnı "
    "doyunca. Ninni yavrum ninni, ninni ninni, hu ninni.",
    // Bol soğanlı börülce
    "Ninni de ninni ninnice, bol soğanlı börülce. Yesin benim yavrum doyunca, mini mini yavrum, ninni. "
    "Dandini dandini dan ister, bey babasından don ister. Basmadan beğenmez yavrum, kadifeden don ister.",
    // Atem tutam ben seni
    "Hop hopun olsun yavrum, gül topun olsun yavrum. Sıralı kavak dibinde, toyluğun olsun yavrum. Atem "
    "tutem men seni, şekere katem men seni. Akşam baban gelende, önüne atem men seni.",
    // Ninnilerin benim olsun
    "Ninnilerin benim olsun, uykuların senin olsun. Akan sular ömrün olsun, ninni yavrum, kuzum ninni.",
    // Gökte yıldız oynuyor
    "Gökte yıldız oynuyor, gözüm yavruma doymuyor. Ellerde yavru çok amma, benim yavrum uyumuyor. Ninni "
    "ninni, bebeğim ninni.",
    // Kavak gibi boylanasın
    "Kavak gibi boylanasın, ninni, söğüt gibi dallanasın, ninni. Uyusun da büyüsün, ninni, ninni benim "
    "yavrum, ninni.",
    // Hey develer develer
    "Hey develer develer, peynirlidir pideler. Yedi yedi dedeler, hani bize dediler. Yavruma uyku "
    "verdiler.",
    // Yağmur yağar sere serpe
    "Yağmur yağar sere serpe, kulağında elmas küpe. Uyuturum yavrumu koka öpe. Eee, eee, ninni, ninni "
    "benim nazlı yavrum, sana ninni.",
    // Ninnilerin merdanesi
    "Ninnilerin merdanesi, ninni, annesinin bir tanesi. Mini mini yavrum, ninni, benim güzel yavrum, "
    "ninni. Ninni desem nihal olur, ninni, açar güller bahar olur. Yavrum uyumazsa ne hal olur, adı güzel "
    "yavrum, ninni.",
    // E e esine
    "E, e, esine, yavrum gitti teyzesine. Teyzesi çok kibar hanım, altın koymuş çevresine. Uyusun da "
    "büyüsün, ninni, tıpış tıpış yürüsün, ninni.",
    // Salıncak
    "Asmaya kurdum salıncak, eline de verdim oyuncak. Yine de uyumadı gitti, şu küçücük yumurcak. Ninni "
    "yavrum, ninni, uyusun da büyüsün, ninni.",
};

typedef struct {
  const char *kimlik;              // DONANIM_KIMLIK
  const char *const *metin;
  int n;
} YerlesikListe;

static const YerlesikListe YERLESIK[] = {
    {"gece", NINNILER, (int)(sizeof NINNILER / sizeof NINNILER[0])},
};
