// Üretildi: tools/ninniler.py (ninniler.txt). Elle değiştirme; ninniler.txt'yi düzenleyip aracı çalıştır.
// Yerleşik metinler: kartta sabit duran, modelin yazmadığı içerik. Gece figürü (Ay Dede, mod "uyku") yalnız
// bu ninnileri okur (ürün sahibinin kararı, 15 Ekim 2026: ninniler sabit, 15 tane); liste sırayla döner, aynı
// ninni art arda gelmez. Ninni modunda yavaş, alçak, kısık okunur; her iki dize bir cümle (arada uzun durak).
#pragma once

static const char *const NINNILER[] = {
    // Dandini
    "Dandini dandini dastana, danalar girmiş bostana. Kov bostancı danayı, yemesin lahanayı. Dandini "
    "dandini dastana, Ay Dede gelmiş bostana. Yıldız doldurmuş sepete, getirmiş bizim bebeğe.",
    // Uyusun da büyüsün
    "Uyusun da büyüsün, tıpış tıpış yürüsün. Sabah olup kalkınca, güneş gibi gülüşsün. Ninni ninni, eee "
    "ninni, uyku gelsin gözüne. Ay Dede'nin ışığı, konsun tatlı yüzüne.",
    // Ninni ninni ninnisi
    "Ninni ninni ninnisi, kuzucuğun annesi. Ay Dede bekçi olmuş, uyusun gül goncası. Yıldızlar göz "
    "kırpıyor, rüzgâr ninni söylüyor. Uyu yavrum, uyu sen, gece seni sarıyor.",
    // Yumuk yumuk gözleri
    "Yumuk yumuk gözleri, tatlı tatlı sözleri. Ay Dede'den selam var, yıldız olsun düşleri. Pamuk gibi "
    "elleri, gül kokulu telleri. Uyusun da büyüsün, ninni söylesin yeller.",
    // Kuzu yatmış ağılda
    "Kuzu yatmış ağılda, kuşcağız da yuvada. Balık uyur suyunda, yavrum uyur kucakta. Baykuş öter "
    "dalında, kedi mırlar yanında. Uyusun da büyüsün, bu ninninin sonunda.",
    // Eee ninni
    "Eee ninni, eee ninni, gül dalında bülbül ninni. Bülbül uyur, gül uyur, yavrum da uyur ninni. Ay "
    "doğmuş tepelere, ışık sermiş her yere. Yavrum uyusun artık, ninni gelsin her gece.",
    // Kedicik
    "Mırnav mırnav kedicik, kıvrılmış da minicik. Kuyruğunu dolamış, uyumuş bir tanecik. Sen de uyu "
    "yavrucuk, yorganın da sıcacık. Uyusun da büyüsün, ninni ninni küçücük.",
    // Pamuk bulutlar
    "Pamuk pamuk bulutlar, gökyüzünde uyurlar. Yavrum gözün yumunca, rüyasına konarlar. Tıpır tıpır "
    "yağmur da, ninni söyler camlarda. Uyu yavrum, uyu sen, güneş doğar sabahta.",
    // Ay Dede
    "Ay Dede, Ay Dede, gökyüzünün dedesi. Yavrumu sen kolla, tatlı olsun gecesi. Yıldızlar, yıldızlar, Ay "
    "Dede'nin torunu. Göz kırpın yavruma, bulsun tatlı uykuyu.",
    // Uyu yavrum uyu da
    "Uyu yavrum, uyu da, kuşlar döndü yuvaya. Ay ışığı yorgandır, örter seni, uyu da. Uyu yavrum, uyu da, "
    "rüzgâr esti yavaşça. Ağaçlar da uyudu, uyu sen de rahatça.",
    // Yıldızları toplarım
    "Beşiğini sallarım, yıldızları toplarım. Uyusun da büyüsün, yastığına koyarım. Buluttandır yastığı, "
    "ay ışığı yorganı. Rüyasında görsün de, renk renk gökkuşağını.",
    // Tavşan yuvasına
    "Tavşan girmiş yuvasına, sincap ağaç kovuğuna. Ayıcık gitmiş inine, yavrum yatsın yatağına. Ninni "
    "ninni, eee ninni, ay doğdu usul usul. Yavrum yumdu gözünü, uyusun mışıl mışıl.",
    // Papatya
    "Papatya yumdu gözünü, lale de örttü yüzünü. Arılar döndü kovana, yavrum da yumsun gözünü. Kelebek "
    "kondu dala, kanatlarını yumdu. Yavrum uyusun ninni, gece masmavi oldu.",
    // Hu hu baykuş
    "Hu hu der baykuş dalda, ay ışığı yaprakta. Herkes uyur bu gece, yavrum tatlı uykuda. Hu hu ninni, hu "
    "ninni, yıldızlar parlar ninni. Uyusun da büyüsün, yavrum gülsün sabah ninni.",
    // Yorgan
    "Yorganı yumuşacık, yastığı da sıcacık. Ay Dede bakar ona, uyur yavrum tatlıcık. Ninni ninni, eee "
    "ninni, uyusun da büyüsün. Tıpış tıpış yarın da, sevinçle de yürüsün.",
};

typedef struct {
  const char *kimlik;              // DONANIM_KIMLIK
  const char *const *metin;
  int n;
} YerlesikListe;

static const YerlesikListe YERLESIK[] = {
    {"gece", NINNILER, (int)(sizeof NINNILER / sizeof NINNILER[0])},
};
