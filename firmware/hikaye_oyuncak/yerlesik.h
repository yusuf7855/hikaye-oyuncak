// Yerleşik metinler: hikâye modelinin henüz bilmediği donanım figürleri için flash'ta duran kısa metinler.
//
// Kart bir donanım figürünün içeriğini şöyle seçer (hikaye_oyuncak.ino icerik_hazirla):
//   DONANIM_MODEL[d] >= 0  -> model figürü: kuyruk / arka plan üretimi / canlı üretim (her figürde olduğu gibi)
//   değilse                -> YERLESIK tablosunda kimliğin listesi sırayla döner
// Gece figürü ("gece", Ay Dede) bugün modelde yok: ninniler buradan okunur. Model "gece" figürüyle eğitilip
// tools/basliklar.py yeniden çalıştırılınca DONANIM_MODEL tablosu değişir ve aynı figür kendiliğinden kuyruk yoluna
// geçer; bu dosyaya ve koda dokunmak gerekmez.
// Metinler geleneksel ninni tarzında, bu proje için yazıldı (anonim halk ninnilerinin kalıp dizeleri: "uyusun da
// büyüsün", "dandini"); her biri ninni modunda yavaş, alçak ve kısık okunur.
#pragma once

static const char *const NINNILER[] = {
    "Uyusun da büyüsün, ninni. Tıpış tıpış yürüsün, ninni. Ay doğdu, yıldızlar uyandı, ninni. "
    "Gözlerin kapansın, tatlı rüyalar gelsin, ninni.",
    "Dandini dandini, uyu yavrum uyu. Kuzular ahırda, kuşlar yuvasında uyudu. Rüzgâr yavaşça esti, "
    "yapraklar ninni söyledi. Sen de uyu, yavrum, sen de uyu.",
    "Ay Dede gökyüzünden baktı. Bütün çocuklar yatağında mı, diye sordu. Yıldızlar göz kırptı, evet dediler. "
    "Ay Dede gülümsedi ve herkese iyi geceler dedi.",
    "Küçük bir kedi yumak gibi kıvrıldı. Kuyruğunu burnuna sardı. Yavaşça esnedi, gözleri kapandı. "
    "Mırr, mırr, dedi ve uykuya daldı.",
    "Ninni, ninni, ninni. Bulutlar pamuk gibi yumuşacık. Bir bulut gelip seni sarsın, ninni. "
    "Uyusun da büyüsün yavrum, ninni.",
    "Ormanda akşam oldu. Tavşan yuvasına girdi, sincap ağaç kovuğuna sokuldu. Baykuş yumuşak bir sesle "
    "huu huu dedi. Orman sessizleşti, herkes uyudu.",
    "Deniz kıyıda dalgalarını sallar, hış hış, hış hış. Küçük bir balık yosunların arasında uyur. "
    "Sen de dalgaları dinle, gözlerini yum, uyu.",
    "Yıldızlar birer birer yandı. Biri sana göz kırptı. Ay ışığı pencereden süzüldü, yorganına kondu. "
    "İyi geceler küçüğüm, tatlı rüyalar.",
};

typedef struct {
  const char *kimlik;              // DONANIM_KIMLIK
  const char *const *metin;
  int n;
} YerlesikListe;

static const YerlesikListe YERLESIK[] = {
    {"gece", NINNILER, (int)(sizeof NINNILER / sizeof NINNILER[0])},
};
