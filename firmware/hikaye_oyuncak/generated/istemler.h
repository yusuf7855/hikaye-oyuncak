// Üretildi: tools/basliklar.py (degerlendirme/urun_uret.py ile birebir). Figür f (0..N_FIGUR-1,
// urun_uret.FIGURLER sırası), kart yeri j (0..FIGUR_YER_N[f]-1): genel yer FIGUR_YER[f][j] (YER_AD),
// istem = ISTEM_ID[ISTEM_OFF[f*YER_MAKS+j] .. ISTEM_OFF[f*YER_MAKS+j+1]) (urun_uret.istem, Yan yok),
// süzgeç adları = SUZGEC_AD[SUZGEC_AD_OFF[f] .. SUZGEC_AD_OFF[f+1]) (urun_uret.kadro_disi, '$' =
// KELIME_BASI). URUN_* tabloları secici.h secici_urun_puanla içindir (urun_uret.puanla).
#pragma once
#include <stdint.h>
#define N_FIGUR 13
#define N_YER 8
#define YER_MAKS 5
#define EOT_ID 0
#define NL_ID 199
static const int16_t GOVDE_YASAK[2] = {
  199, 9491
};
static const char *const FIGUR_AD[13] = {
  "Kelo\xc4\x9flan", "Pamuk Prenses", "Pinokyo", "Alaaddin", "Nasreddin Hoca", "Bulut", "Z\xc4\xb1pz\xc4\xb1p",
  "Tonti\xc5\x9f", "Bilge Bayku\xc5\x9f", "Ejderha Yavrusu", "Tek Boynuzlu At", "Bip", "F\xc4\xb1st\xc4\xb1k"
};
static const char *const FIGUR_KIMLIK[13] = {
  "keloglan", "pamuk_prenses", "pinokyo", "alaaddin", "nasreddin_hoca", "bulut", "zipzip", "tontis", "bilge_baykus",
  "ejderha_yavrusu", "tek_boynuzlu_at", "bip", "fistik"
};
static const char *const YER_AD[8] = {
  "orman", "deniz", "ev", "park", "\xc5\x9f" "ato", "da\xc4\x9f", "bah\xc3\xa7" "e", "g\xc3\xb6ky\xc3\xbcz\xc3\xbc"
};
static const int8_t FIGUR_YER_N[13] = {
  4, 4, 3, 4, 4, 3, 3, 3, 3, 4, 4, 3, 3
};
static const int8_t FIGUR_YER[N_FIGUR * YER_MAKS] = {
  0, 5, 2, 4, -1, 0, 2, 6, 4, -1, 2, 3, 0, -1, -1, 2, 3, 6, 4, -1, 2, 3, 6, 5,
  -1, 2, 6, 3, -1, -1, 6, 0, 3, -1, -1, 0, 5, 3, -1, -1, 0, 5, 7, -1, -1, 5, 7, 0,
  4, -1, 7, 0, 6, 5, -1, 2, 3, 6, -1, -1, 0, 3, 6, -1, -1
};
static const int16_t ISTEM_ID[732] = {
  0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 11057, 1217, 488,
  221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 532, 199, 3953, 26,
  0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 2687, 199, 3953, 26, 0, 43, 962, 2846, 26, 660, 5407, 221,
  92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 660, 5407, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43,
  962, 2846, 26, 660, 5407, 221, 92, 3032, 26, 2863, 199, 3953, 26, 0, 43, 962, 2846, 26, 660, 5407, 221, 92, 3032, 26,
  2687, 199, 3953, 26, 0, 43, 962, 2846, 26, 15551, 288, 2144, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846,
  26, 15551, 288, 2144, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 15551, 288, 2144, 221, 92, 3032, 26,
  1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 292, 290, 4911, 260, 78, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43,
  962, 2846, 26, 292, 290, 4911, 260, 78, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 292, 290, 4911,
  260, 78, 221, 92, 3032, 26, 2863, 199, 3953, 26, 0, 43, 962, 2846, 26, 292, 290, 4911, 260, 78, 221, 92, 3032, 26,
  2687, 199, 3953, 26, 0, 43, 962, 2846, 26, 1511, 383, 82, 1616, 260, 78, 391, 558, 65, 221, 92, 3032, 26, 532, 199,
  3953, 26, 0, 43, 962, 2846, 26, 1511, 383, 82, 1616, 260, 78, 391, 558, 65, 221, 92, 3032, 26, 531, 199, 3953, 26,
  0, 43, 962, 2846, 26, 1511, 383, 82, 1616, 260, 78, 391, 558, 65, 221, 92, 3032, 26, 2863, 199, 3953, 26, 0, 43,
  962, 2846, 26, 1511, 383, 82, 1616, 260, 78, 391, 558, 65, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846,
  26, 4398, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846, 26, 4398, 221, 92, 3032, 26, 2863, 199, 3953, 26,
  0, 43, 962, 2846, 26, 4398, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 4999, 221, 92, 3032, 26,
  2863, 199, 3953, 26, 0, 43, 962, 2846, 26, 4999, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 4999,
  221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 8817, 315, 261, 221, 92, 3032, 26, 1238, 199, 3953, 26,
  0, 43, 962, 2846, 26, 8817, 315, 261, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 8817, 315, 261,
  221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 6640, 2394, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0,
  43, 962, 2846, 26, 6640, 2394, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 6640, 2394, 221, 92, 3032,
  26, 2781, 199, 3953, 26, 0, 43, 962, 2846, 26, 4194, 4638, 1245, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962,
  2846, 26, 4194, 4638, 1245, 221, 92, 3032, 26, 2781, 199, 3953, 26, 0, 43, 962, 2846, 26, 4194, 4638, 1245, 221, 92, 3032,
  26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 4194, 4638, 1245, 221, 92, 3032, 26, 2687, 199, 3953, 26, 0, 43, 962,
  2846, 26, 893, 11115, 880, 348, 6115, 221, 92, 3032, 26, 2781, 199, 3953, 26, 0, 43, 962, 2846, 26, 893, 11115, 880, 348,
  6115, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 893, 11115, 880, 348, 6115, 221, 92, 3032, 26, 2863,
  199, 3953, 26, 0, 43, 962, 2846, 26, 893, 11115, 880, 348, 6115, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962,
  2846, 26, 309, 1068, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846, 26, 309, 1068, 221, 92, 3032, 26, 531,
  199, 3953, 26, 0, 43, 962, 2846, 26, 309, 1068, 221, 92, 3032, 26, 2863, 199, 3953, 26, 0, 43, 962, 2846, 26, 6291,
  221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 6291, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43,
  962, 2846, 26, 6291, 221, 92, 3032, 26, 2863, 199, 3953, 26
};
static const uint16_t ISTEM_OFF[66] = {
  0, 16, 32, 48, 64, 64, 79, 94, 109, 124, 124, 140, 156, 172, 172, 172, 190, 208, 226, 244, 244, 266, 288, 310,
  332, 332, 346, 360, 374, 374, 374, 388, 402, 416, 416, 416, 432, 448, 464, 464, 464, 479, 494, 509, 509, 509, 525, 541,
  557, 573, 573, 591, 609, 627, 645, 645, 660, 675, 690, 690, 690, 704, 718, 732, 732, 732
};
// isim süzgeci (runtime/isim_suzgec.h): figür başına yasaklı adlar ve bayt uzunlukları
static const char *const SUZGEC_AD[1358] = {
  "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$",
  "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif",
  "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost",
  "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily",
  "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin",
  "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak",
  "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue",
  "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$",
  "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet",
  "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$",
  "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne",
  "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$",
  "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff",
  "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet",
  "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee",
  "Olaf", "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider",
  "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f",
  "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne",
  "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$",
  "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses",
  "Paytak", "Pepee", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue",
  "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$",
  "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet",
  "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z",
  "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$",
  "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu",
  "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost",
  "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses",
  "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin",
  "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi",
  "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne",
  "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$",
  "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff",
  "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet",
  "Mert", "Mete", "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses",
  "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin",
  "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi",
  "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bip", "Bob", "Boncuk$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$",
  "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto",
  "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil",
  "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat",
  "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete",
  "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf",
  "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$",
  "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$",
  "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy",
  "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f",
  "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty",
  "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem",
  "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall",
  "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo",
  "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At",
  "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy",
  "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f",
  "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty",
  "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem",
  "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall",
  "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo",
  "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At",
  "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy",
  "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan",
  "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty",
  "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem",
  "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall",
  "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo",
  "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At",
  "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p",
  "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca",
  "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca",
  "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$",
  "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir",
  "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider",
  "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan",
  "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy",
  "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo",
  "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At",
  "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p",
  "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca",
  "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca",
  "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$",
  "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif",
  "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto", "Gepetto Usta", "Ghost",
  "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Pamuk Prenses",
  "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin",
  "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$",
  "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet",
  "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$",
  "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$",
  "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k$", "Gepetto",
  "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil",
  "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat",
  "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete",
  "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf",
  "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$",
  "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy", "Tom$",
  "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev$", "Ali", "Amy",
  "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f",
  "Bilgecan", "Bilgecan Dede", "Bip", "Bob", "Boncuk$", "Bulut$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Dedee", "Defne", "Dino$", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff",
  "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet",
  "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee",
  "Olaf", "Pamuk$", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam$",
  "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim$", "Timmy",
  "Tom$", "Tonti\xc5\x9f", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila"
};
static const uint16_t SUZGEC_AD_OFF[14] = {
  0, 102, 206, 309, 414, 518, 623, 728, 833, 938, 1043, 1148, 1253, 1358
};
static const int SUZGEC_AD_UZUN[1358] = {
  5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 5, 10, 5, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5,
  5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7,
  5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4,
  6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6,
  6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13,
  3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12,
  5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4,
  3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4,
  15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5,
  4, 7, 5, 10, 5, 13, 8, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4,
  4, 10, 6, 9, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4,
  8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5, 5, 6, 5, 4,
  5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 5,
  5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5, 5,
  5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9,
  5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4,
  6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6,
  6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13,
  3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12,
  5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4,
  3, 4, 5, 6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4,
  15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5,
  4, 7, 5, 10, 5, 13, 8, 13, 3, 3, 7, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4,
  10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4,
  4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6,
  5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5,
  5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13, 3, 3, 7, 6, 4, 5, 5,
  6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5,
  8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5,
  6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4,
  7, 5, 6, 6, 6, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13,
  8, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12,
  5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6,
  4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6,
  4, 4, 3, 4, 15, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3,
  4, 5, 5, 4, 7, 5, 10, 5, 8, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15,
  4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8,
  6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5,
  7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14,
  6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13, 3, 3, 7, 6,
  4, 5, 5, 6, 5, 5, 5, 5, 4, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4,
  7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14,
  6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4,
  5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5,
  10, 5, 13, 8, 13, 3, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6,
  9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8,
  3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4,
  5, 4, 6, 4, 4, 3, 4, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 8, 5,
  5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13, 3, 7, 6, 4, 5, 5, 6, 5, 5, 5,
  5, 4, 15, 4, 4, 4, 10, 6, 9, 7, 12, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5,
  5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 9, 14, 6, 5, 6, 5, 4, 6,
  13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 15, 5, 4, 5, 4, 7, 5, 6, 6,
  6, 8, 14, 6, 5, 5, 5, 8, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 13, 8, 13, 3,
  3, 7, 6, 4, 5, 5, 6, 5, 5, 5, 5, 4, 15, 4, 4, 4, 10, 6, 7, 12, 5, 12, 5, 11,
  4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4,
  5, 9, 14, 6, 5, 6, 5, 4, 6, 13, 6, 5, 7, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4,
  15, 5, 4, 5, 4, 7, 5, 6, 6, 6, 8, 14, 6, 5
};
// süzgeç token baytları vocab.h'den farklı olan token'lar (gen -Y dosyasındaki gibi)
#define SUZGEC_OZEL_N 1
static const int16_t SUZGEC_OZEL_ID[1] = {
  0
};
static const char *const SUZGEC_OZEL_BAYT[1] = {
  "<|endoftext|>"
};
// seçici (urun_uret.puanla): figur_adlari, kadro_cezalari'nın izinli kümesi, takıntı önekleri
static const char *const URUN_KADRO[20] = {
  "Balk\xc4\xb1z", "Bilgecan", "Bilgecan Dede", "Kelo\xc4\x9flan", "Pamuk", "Pamuk Prenses", "Gepetto",
  "Gepetto Usta", "Pinokyo", "Alaaddin", "Nasreddin", "Nasreddin Hoca", "Bulut", "Z\xc4\xb1pz\xc4\xb1p",
  "Tonti\xc5\x9f", "Bilge Bayku\xc5\x9f", "Ejderha Yavrusu", "Tek Boynuzlu At", "Bip", "F\xc4\xb1st\xc4\xb1k"
};
static const uint16_t URUN_KADRO_OFF[14] = {
  0, 4, 6, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20
};
static const char *const URUN_IZINLI[35] = {
  "Balk\xc4\xb1z", "Bilgecan", "Bilgecan Dede", "Dede", "Karaka\xc3\xa7" "an", "Kelo\xc4\x9flan", "Pamuk",
  "Pamuk Prenses", "Prenses", "Gepetto", "Gepetto Usta", "Pinokyo", "Usta", "Alaaddin", "Cini", "Lamba",
  "Lamba Cini", "Hoca", "Nasreddin", "Nasreddin Hoca", "Bulut", "Z\xc4\xb1pz\xc4\xb1p", "Tonti\xc5\x9f",
  "Bayku\xc5\x9f", "Bilge", "Bilge Bayku\xc5\x9f", "Ejderha", "Ejderha Yavrusu", "Yavrusu", "At", "Boynuzlu",
  "Tek", "Tek Boynuzlu At", "Bip", "F\xc4\xb1st\xc4\xb1k"
};
static const uint16_t URUN_IZINLI_OFF[14] = {
  0, 6, 9, 13, 17, 20, 21, 22, 23, 26, 29, 33, 34, 35
};
static const char *const URUN_TAKINTI_AD[24] = {
  "balk\xc4\xb1", "bilge", "dede", "kelo\xc4\x9f", "pamuk", "prens", "gepet", "pinok", "usta", "alaad",
  "hoca", "nasre", "bulut", "z\xc4\xb1pz\xc4\xb1", "tonti", "bayku", "bilge", "ejder", "yavru", "at", "boynu",
  "tek", "bip", "f\xc4\xb1st\xc4\xb1"
};
static const uint16_t URUN_TAKINTI_AD_OFF[14] = {
  0, 4, 6, 9, 10, 12, 13, 14, 15, 17, 19, 22, 23, 24
};
#define URUN_TUM_ISIM_N 70
static const char *const URUN_TUM_ISIM[70] = {
  "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Anna", "Annee", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee",
  "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede", "Bip", "Bulut", "Canan", "Chase", "Da\xc5\x9f" "a",
  "Dedee", "Doru", "Ejderha Yavrusu", "Elsa", "Fil Necati", "F\xc4\xb1st\xc4\xb1k", "Gepetto", "Gepetto Usta",
  "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Kadriye", "Kamil", "Karatay", "Kelo\xc4\x9flan",
  "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "Marshall", "Ma\xc5\x9f" "a", "Mert", "Mete",
  "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk",
  "Pamuk Prenses", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Skye", "Spider", "Spin", "Sven", "Tek Boynuzlu At",
  "Tonti\xc5\x9f", "Tospik", "Yumak", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila"
};
#define URUN_TUM_AD_N 106
static const char *const URUN_TUM_AD[106] = {
  "Ahmet", "Ak\xc4\xb1n", "Alaaddin", "Alaca", "Alev", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilge Bayku\xc5\x9f", "Bilgecan", "Bilgecan Dede",
  "Bip", "Bob", "Boncuk", "Bulut", "Can", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne",
  "Dino", "Doru", "Ejderha Yavrusu", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "F\xc4\xb1st\xc4\xb1k",
  "Gepetto", "Gepetto Usta", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff",
  "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet",
  "Mert", "Mete", "Mia", "Mimi", "Murat", "Nasreddin", "Nasreddin Hoca", "Necati", "Nenee", "Niloya", "Ninee",
  "Olaf", "Pamuk", "Pamuk Prenses", "Paytak", "Pepee", "Pinokyo", "Remzi", "Rubble", "Ryder", "Sam", "Sara",
  "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tek Boynuzlu At", "Tekir", "Tim", "Timmy", "Tom", "Tonti\xc5\x9f",
  "Tosbi", "Tospik", "Yumak", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila"
};
#define URUN_ISIM_KELIME_N 75
static const char *const URUN_ISIM_KELIME[75] = {
  "adam", "ak\xc4\xb1n", "alaaddin", "alaca", "amca", "anna", "annee", "at", "ay\xc4\xb1", "balk\xc4\xb1z",
  "basri", "bayku\xc5\x9f", "bebee", "bilge", "bilgecan", "bip", "boynuzlu", "bulut", "canan", "chase",
  "da\xc5\x9f" "a", "dede", "dedee", "doru", "ejderha", "elsa", "fil", "f\xc4\xb1st\xc4\xb1k", "gepetto",
  "ghost", "hayri", "hello", "hoca", "hulk", "kadriye", "kamil", "karatay", "kelo\xc4\x9flan", "kitty",
  "koca", "kristoff", "k\xc4\xb1rat", "marshall", "ma\xc5\x9f" "a", "mert", "mete", "mimi", "murat", "nasreddin",
  "necati", "nenee", "niloya", "ninee", "olaf", "pamuk", "pepee", "pinokyo", "prenses", "remzi", "rubble",
  "ryder", "skye", "spider", "spin", "sven", "tek", "tonti\xc5\x9f", "tospik", "usta", "yavrusu", "yumak",
  "z\xc4\xb1pz\xc4\xb1p", "\xc3\xb6r\xc3\xbcmcek", "\xc5\x9f" "akir", "\xc5\x9fila"
};
#define URUN_TAKINTI_HARIC_N 20
static const char *const URUN_TAKINTI_HARIC[20] = {
  "art\xc4\xb1k", "birde", "birli", "bunu", "daha", "dedi", "de\xc4\x9fil", "gibi", "hemen", "ikisi", "i\xc3\xa7in",
  "kadar", "onlar", "onun", "sonra", "yava\xc5\x9f", "\xc3\xa7ok", "\xc3\xa7ok\xc3\xa7" "a", "\xc3\xa7\xc3\xbcnk\xc3\xbc",
  "\xc5\x9fimdi"
};
