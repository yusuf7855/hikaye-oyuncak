// Üretildi: tools/ninniler.py (ninniler.txt). Elle değiştirme; ninniler.txt'yi düzenleyip aracı çalıştır.
// Yerleşik metinler: kartta sabit duran, modelin yazmadığı içerik. Gece figürü (Ay Dede, mod "uyku") yalnız
// bu ninnileri okur (ürün sahibinin kararı, 15 Ekim 2026: 100 sabit, bilinen anonim halk ninnisi); sırayla döner, aynı
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
    // Bebeğimin beşiği bakır
    "Bebeğimin beşiği bakır, yerinden kalkmıyor ağır. Ben sallarım takır takır, nenni nenni, nenni nenni. "
    "Nenni nenni, nenni bebek oy.",
    // Al babası
    "Al babası, al babası, yağlığımı sar babası. Yavrun mektebe hazırla, kitap al da sal babası.",
    // Göllerde biter kamış
    "Göllerde biter kamış, uzar gider vermez yemiş. Benim çocuğum dökme gümüş, kuyumcular dökememiş.",
    // Kovan kovan balın olsun
    "Kovan kovan balın olsun, bin çiçekli dalın olsun. Denizlerde salın olsun, uyu ninni, uyu ninni.",
    // Elmadan kırmızısın
    "A yavrum, kimin yavrususun, elmadan kırmızısın. Baban anan beslemiş, ne güzelce kuzusun.",
    // Ninni diyem yatasın
    "Ninni diyem yatasın, kızıl güle batasın. Kızıl gülün içinde, şirin yuhu tapasın.",
    // Bebeğin beşiği serin
    "Bebeğin beşiği serin, bebek uyur derin derin. Gözlerini yine yummaz, bebeği babasına verin. Uyu "
    "ninni, uyu ninni, uyu ninni, uyu ninni. Eee eee eee, eee eee eee.",
    // Karanfil oylum oylum
    "Karanfil oylum oylum, uyuyor benim yavrum. Eğer yavrum uyursa, şen olur benim gönlüm.",
    // Ninni derim beşiğine
    "Ninni derim beşiğine, hızır gelsin eşiğine. Ulu devletler başına, uyu yavrum, ninni.",
    // Kuzularla yürüyecek
    "Uyuyup da büyüyecek, ninni, kuzularla yürüyecek, ninni. Ninni yavrum, ninni, uyu yavrum, ninni.",
    // Ninni ninni nestane
    "Ninni ninni nestane, cepleri dolu kestane. Gelsin yavruma bir tane. Ninni ninni demişler, hak yoluna "
    "girmişler. Bir fırın ekmek yemişler, daha var mı demişler.",
    // Uyutayım seni
    "Nenni, nenni, uyutayım seni. Akşama baban gelince, uyutayım seni. Nenni kuzum nenni, nenni de "
    "bebeğim nenni.",
    // Nenniler diyem de uyusun
    "Nenniler diyem de uyusun, allah diyem de büyüsün. Küçücük topacığım, nenni, güzel boylum da, nenni, "
    "nenni. Nenniler senin olsun da, uykuların da senin olsun. Nenni kuzum nenni, nenni. Nenniler de "
    "tatlım benim, nenni, küçücük palazım da nenni, nenni. Nenni bebeğim de nenni, nenni. Uyusun da "
    "büyüsün, tıpış tıpış da yürüsün nenni. Nenni kuzum nen, nenni.",
    // İnce elekten eledim
    "İnce elekten eledim, ak tülbente beledim. Ben yavrumu tek Allahtan diledim, uyusun da büyüsün yavrum "
    "nenni.",
    // Benim çocuğum okucak
    "Hu hu hu, benim çocuğum okucak. Paşa olacak. Hu hu hu, benim çocuğum okucak. Öğretmen olacak. Hu hu "
    "hu, benim çocuğum okucak. Mühendis olacak.",
    // Akranları içinde
    "Akranları içinde, benim yavrum bir tane. Ninni kuzuma ninni, ninni yavruma ninni.",
    // Dağa gittim dağ uyur
    "Dağa gittim dağ uyur ninni, dağda tavşanlar uyur ninni. Göle gittim göl uyur ninni, eve geldim ev "
    "uyur ninni. Evde yavrum uyur ninni, uyu da büyü kuzum ninni. Uyu da büyü kuzum ninni.",
    // Dağda tavşanlar uyudu
    "Uyu bebeğim, benim nazlı meleğim. Dağda tavşanlar uyudu, evde koşanlar uyudu. Ninni bebeğim, ninni "
    "nazlı meleğim.",
    // Yuvada yavru kuş
    "Yuvada yavru kuş ninni, erkenden uyusun ninni. Yavrum sen de güzel uyu, güzel gözlü yavrum ninni. "
    "Gökte ay soldu ninni, yıldızlar kayboldu ninni. Uyusun da büyüsün ninni.",
    // Bahçede gül açar
    "Bahçede gül açar, dağda ceylan kaçar. Benim yavrum güler, yüzünde gül açar.",
    // Ninni ninni nesi var
    "Ninni ninni nesi var, naylondan bebesi var. Susun susun çocuklar, bebemin uykusu var. Uyu bebeğim "
    "uyu.",
    // Babası yoldan geliyor
    "Babası yoldan geliyor ninni, benim bebeğim uyur mu ola. Babası yoldan geliyor ninni, benim bebeğim "
    "büyür mü ola. Uyu bebeğim uyu ninni, uyu bebeğim uyu ninni.",
    // Uyur uykusu gelir
    "Uyur uykusu gelir, nenni yavrum nenni. Akşam babası gelir, nenni yavrum nenni.",
    // Bahçelerde hıyarım
    "Bahçelerde hıyarım, mor mendile koyarım. Sen orada ne yaparsan, ben burada duyarım. Ninni bebeğim "
    "ninni.",
    // Çayda kumlar kaynaşır
    "Çayda kumlar kaynaşır, suda balık oynaşır. Çocuk sesin duymazsam, elim kolum dolaşır.",
    // İnce gömlek biçemem
    "İnce gömlek biçemem, soğuk sular içemem. Dünyayı verseler de, ben yavrumdan geçemem.",
    // Aşağı bağın omçası
    "Aşağı bağın omçası, yukarı bağın yoncası. Sensin gönlümün eğlencesi, büyüsün içimin goncası ninni.",
    // Bir meleksin bakışın
    "Bir meleksin bakışın, babanı andırıyor. Cân oyalandırıyor, seni yavrum severim ninni.",
    // Gül dalı gülsüz olmaz
    "Gül dalı gülsüz olmaz, kuzum evler sensiz olmaz. Uyu kuzum ninni ninni. Ninni yavrum, ninni, uyusun "
    "da büyüsün, ninni.",
    // Yavrumun adı var
    "Yavrumun adı var, baldan tatlı tadı var. Benim yavrum güzel, melek tabiatı var. Nenni bebek nenni, "
    "nenni gülüm nenni.",
    // Yavrum yavrum gül yavrum
    "Yavrum yavrum gül yavrum, şeker yavrum bal yavrum. Güllü müsün, ballı mısın, yoksa portakallı mısın. "
    "Uyu yavrum ninni, uyu yavrum ninni.",
    // Yavrumun gözleri sürmeli
    "Yavrumun gözleri sürmeli, yumuk yumuk elleri. Tatlı mı tatlıdır dilleri, nenni kuzum nenni nenni. "
    "Nenni yavrum nenni nenni.",
    // Dudakları bahçe kirazı
    "Dudakları bahçe kirazı, kulakları kuş yuvası. Yanakları misket elması, ninni derim yavruma ninni.",
    // Tokası var saçında
    "Tokası var saçında, sürmesi var gözünde. Tatlılık var sözünde, nenni yavruma nenni. Nenni kuzuma "
    "nenni, nenni kuzuma nenni.",
    // Çiçek çiçek öpüşüm var
    "Bilirim ne çok düşün var, çiçek çiçek öpüşüm var. Bir gül gibi öpüşün var, uyu ninni, uyu ninni. Uyu "
    "ninni, uyu ninni, eee eee eee, eee eee eee.",
    // Gökte uçan martılar
    "Nenni yavrum nenni, nenni yavrum nenni. Gökte uçan martılar, denizde yüzen balıklar. Anneler çok "
    "emektar, yavrusunu sayıklar. Nenni yavrum nenni, nenni yavrum nenni.",
    // Yüce dağ başında
    "Yüce dağ başında turna yeleği, yel vurdukça kaldırıyor yeleği. Benim yavrum yedi dağın meleği, sakla "
    "dağlar koyma yavrumu ninni. Uyusun da büyüsün yavrucak, uyusun da büyüsün ninni. Tıpış tıpış yürüsün "
    "ninni, eee bebeğim eee eee eee.",
    // Dandini dandini dan kuşu
    "Dandini dandini dan kuşu, çalı diken yuvası. Atta gitmiş bey babası, mamalar pişirmiş hanım ninesi. "
    "Elinde şeker halkası. Yavrum yesin büyüsün, sokaklarda yürüsün. Hem yürüsün hem büyüsün, mini mini "
    "yavruma ninni. Küçücük yavruma hû ninni.",
    // Dandini dandini dan atmış
    "Dandini dandini dan atmış, allah neler yaratmış. Çenesi çukur yavrumun, kaşları keman yaratmış. "
    "Gözleri kudret halkası, burnu Kâbe hurması. Ağzı şeker hokkası, yanakları misk elması. Uyku getir "
    "yavruma babası, ninni güzel çocuğuma ninni.",
    // Altına pantol üstüne yelek
    "Dandini dandini danalı bebek, altına pantol üstüne yelek. Hiç yaya gezmez bu nazlı melek, ninni "
    "benim yavrum ninni.",
    // Dandini dandini danaylı
    "Dandini dandini danaylı, boynunda gümüş hamaylı. Hamaylısı boynunda, yavrum annesinin koynunda. "
    "Ninni yavrum ninni, uyusun da büyüsün ninni.",
    // Alaylı alaylı bebek
    "Alaylı alaylı alaylı bebek, maşrabası kalaylı bebek. Mama getir bey babası, yavrum uyuyup büyüyecek.",
    // Sepet sepet narım var
    "Sepet sepet narım var, benim güzel yavrum var. Babası şimdi gelir çarşıdan, heybesinde şeker var. "
    "Ninni yavrucağım ninni.",
    // Evlerinin önü kaya
    "Evlerinin önü kaya, kayadan bakarlar aya. Baban binmiş gelip gelir, kuyruğu kınalı doru taya.",
    // Ev yapalım dam yapalım
    "Ev yapalım, dam yapalım, çıkalım nardan bakalım. Baban gelmiş diyene de, sırmalı yağlık takalım.",
    // Benim kuzum aş istemiş
    "Benim kuzum aş istemiş, aşına kaşık istemiş. Salıngaçları beğenmemiş, konya'dan beşik istemiş.",
    // Bir baş soğan heybesine
    "Bir baş soğan heybesine, benim yavrum gidecek babaannesine. Babaannesi pideler pişirecek, benim "
    "yavrum tumbasını şişirecek. Hû, hû, hû, hû.",
    // Hop getir hop getir
    "Hop getir, hop getir, yavruma babsı top getir. Yavrum topunu oynasın, mini mini gönlünü eylesin, "
    "ninni.",
    // Hoppala yavrum hoppala
    "Hoppala yavrum hoppala, yavrum gider bakkala. Bakkal yolu taşlıdır, yavrum kara kaşlıdır.",
    // Ak kesenin yoğurdu
    "Ak kesenin yoğurdu, yavrumu kimler doğurdu. Nolaydı ikiz olaydı, bir evde sekiz olaydı. Dördü çalıp "
    "çağıraydı, dördü okuyup yazaydı. Anası vah vah diyeydi, babası kah kah güleydi. E, e, e, e hu ninni.",
    // Ala beşik allanıyor
    "Ala beşik allanıyor, yel değmeden sallanıyor. Şu gelinin kuzuları, yeni yeni dilleniyor.",
    // Amasya'nın oldu kirazı
    "Amasya'nın oldu kirazı, dibinde kalmış birazı. Anasının gül beyazı, ninni yavrum ninni.",
    // Bahçelerde biter kayısı
    "Bahçelerde biter kayısı, altına dökülür iyisi. Yavrumun hani koç dayısı, ninni yavrum ninni.",
    // Uyku gelsin gözlerine
    "Ninni derim özlerine, uyku gelsin gözlerine. Ninni yavrum ninni. Uyusun da büyüsün, ninni, tıpış "
    "tıpış yürüsün, ninni.",
    // Nenni nenni nen kuşu
    "Nenni nenni nen kuşu, çıkamadım yokuşu. Neredeyse gelsin, benim yavrumun uykusu. E, e, e, e.",
    // Ninni desem yaraşır
    "Ninni desem yaraşır, sokakları dolaşır. Benim yavruma uyku yaraşır, ninni yavruma ninni. Uyusun da "
    "büyüsün ninni.",
    // Dağda tavşan kovarım
    "Dağda tavşan kovarım, düştüm dizim ovarım. Ben yavrumu sallarım, uyu benim yavrum ninni.",
    // Fındık harmanını kollarım
    "Ninni derim sallarım, fındık harmanını kollarım. Yavrum uyusun da büyüsün, gider babasına yollarım "
    "ninni.",
    // Beşik olsun sana dizim
    "Ağlama, yat iki gözüm, beşik olsun sana dizim. Uyusana körpe kuzum, uyu yavrum ninni ninni.",
    // Ağlama yavru Fındıcak
    "Ağlama yavru Fındıcak, anası gelir şimdicek. Uyusun da büyüsün ninni, yaylalarda yürüsün ninni. "
    "Ninni o, o, o, üvele, ninni düt dürü düt düvele.",
    // Uyur idin uyandın
    "Uyur idin uyandın, rüya imiş inandın. Benim güzel yavrucuğum, uykudan mı uyandın.",
    // Bebek uyandı bakar
    "Bebek uyandı bakar, eli kundaktan çıkar. Ağzından şefil akar, yanaktan gülü kokar. Ninni yavrum "
    "ninni, ninni yavrum ninni.",
    // Ninni derim uyutayım
    "Ninni derim uyutayım, sallayım da büyütüyüm. Yaşına gelmeden yürütüyüm, ninni yavrum ninni.",
    // Eledim beledim sevdim
    "Eledim, beledim, sevdim, yavrum büyüsün dedim. Ak sütümden içirip helal eyledim, uyusun da büyüsün "
    "ninni. Tıpış tıpış yürüsün ninni, eee eee eee.",
    // Nenni nenni nelediğim
    "Nenni nenni nelediğim, al kundaklar doladığım. Uzun ömür dilediğim, nenni kuzum nenni.",
    // Evine varayım güzün
    "Evine varayım güzün, evinde bulayım üzüm. Uyku dolsun iki gözün, uykular tutmayan kuzum. Nenni kuzum "
    "nenni derim, körpe kuzum uyu derim.",
    // Uyu uyan kaldırayım
    "Uyu, uyan kaldırayım, sana neler aldırayım. Koynuna gül doldurayım, gül dolduğum kuzum nenni.",
    // Dağda gezer bağda gezer
    "Dağda gezer, bağda gezer, ailesine güller cizer. Benim kuzum nerde gezer, nerde gezen kuzum nenni.",
    // Nenni desem adın dilden
    "Nenni desem adın dilden, kurusun gömleğin yelden. Ben de seni sakınırım, esen yelden kötü dilden.",
    // Gül ağacını budamışlar
    "Gül ağacını budamışlar, gülü göya koksun deyi. Nar ağacını budamışlar, narı büyük olsun deyi. Allah "
    "da seni bize vermiş, dünya eğlencesi olsun deyi.",
    // Ninni ninni ne seslenir
    "Ninni ninni ne seslenir, keklik kafeste beslenir. Yavrum büyürse uslanır, ninni yavrum ninni.",
    // Hu bebeğime
    "Hu bebeğime hu hu hu, hu bebeğime hu hu hu. Adı güzel yavrum ninni, kendi güzel yavrum ninni.",
    // Gökte güneşi tutsun
    "Gökte güneşi tutsun yavrum, yerde çadırlar kursun yavrum. Uyusun da büyüsün yavrum, nenni yavrum "
    "nenni nenni. Nenni kuzum nenni nenni.",
    // Bebeğim ceylan bakışlı
    "Bebeğim ceylan bakışlı, teyzesi kalem kaşlı. Elinde kitap akıllı, nenni nenni bebeğim. Nenni nenni "
    "meleğim.",
    // Beşiğimin altı şişe
    "Beşiğimin altı şişe, içinde yatar paşa. Ninnilerle uyusun ninni, beşikten kalksın büyüsün ninni. "
    "Ninni yavrum ninni.",
    // Üç gün kaldı bayrama
    "Ninni bebek ninni, ninni melek ninni. Ağlama bebek ağlama, üç gün kaldı bayrama. Uyu yavrum nenni "
    "nenni, büyü yavrum nenni nenni. Yürü yavrum nenni nenni, ninni ninni oy oy oy.",
    // Bana mama getirsin
    "Hadi benim yavruma hû, hû, uyusun da büyüsün ninni. Sokaklarda yürüsün ninni, bana mama getirsin "
    "ninni.",
    // Koşa koşa yorulsun
    "Uyusun da büyüsün yavrum ninni, koşa koşa yorulsun ninni. Büyüsün de okusun ninni, benim yavrum "
    "annesine. Babasına baksın ninni.",
    // Uyu uykun tatlı olsun
    "Uyu uykun tatlı olsun, ninni yavruma ninni. İyi uykular seni bulsun, ninni kuzuma ninni. Koltukların "
    "kitapla dolsun, ninni yavruma ninni. Hafızlar bülbülü olsun, ninni yavruma ninni.",
    // Otuz iki kitap okur
    "İstanbul'un yolu çukur, çuhasına kaytan dokur. Yavrum büyür inşallah, otuz iki kitap okur.",
    // Çocukları okutsun
    "Benim yavrum uyusun ninni, uyusun da büyüsün ninni. Yavrum öğretmen olsun da, çocukları okutsun "
    "ninni.",
    // Derelerin çakıl taşları
    "Derelerin çakıl taşları, yavrumun kalem kaşları. Yavrum büyüyüp okuyacak, olacak Cumhurbaşkanı. Nen, "
    "nen, nen, nen.",
    // Doktor diye tanınacak
    "Benim yavrum uyuyacak, uyuyup da büyüyecek. Doktor diye tanınacak, ninni yavrum ninni.",
    // Armut dalda sallanır
    "Armut dalda sallanır, yemiş ağaçta ballanır. Küçük yavrum dallanır, okuyup memur olur. Ninni yavruma "
    "ninni.",
    // Yavrum benim yürüdü
    "Ninni yavruma ninni, yavrum benim yürüdü. Ak donunu sürüdü, haydi, büyü geç yavrum. Tarlayı diken "
    "bürüdü.",
};

typedef struct {
  const char *kimlik;              // DONANIM_KIMLIK
  const char *const *metin;
  int n;
} YerlesikListe;

static const YerlesikListe YERLESIK[] = {
    {"gece", NINNILER, (int)(sizeof NINNILER / sizeof NINNILER[0])},
};
