// Üretildi: tools/basliklar.py (degerlendirme/urun_uret.py ile birebir). Figür f (0..N_FIGUR-1,
// urun_uret.FIGURLER sırası), kart yeri j (0..FIGUR_YER_N[f]-1): genel yer FIGUR_YER[f][j] (YER_AD),
// istem = ISTEM_ID[ISTEM_OFF[f*YER_MAKS+j] .. ISTEM_OFF[f*YER_MAKS+j+1]) (urun_uret.istem, Yan yok),
// süzgeç adları = SUZGEC_AD[SUZGEC_AD_OFF[f] .. SUZGEC_AD_OFF[f+1]) (urun_uret.kadro_disi, '$' =
// KELIME_BASI). URUN_* tabloları secici.h secici_urun_puanla içindir (urun_uret.puanla).
#pragma once
#include <stdint.h>
#define N_FIGUR 11
#define N_YER 6
#define YER_MAKS 5
#define EOT_ID 0
#define NL_ID 199
static const int16_t GOVDE_YASAK[2] = {
  199, 9491
};
static const char *const FIGUR_AD[11] = {
  "Niloya", "Ma\xc5\x9f" "a", "Pepee", "Kelo\xc4\x9flan", "Doru", "Hayri", "\xc5\x9e" "akir", "Elsa", "Chase",
  "\xc3\x96r\xc3\xbcmcek Adam", "Hello Kitty"
};
static const char *const FIGUR_KIMLIK[11] = {
  "niloya", "masa", "pepee", "keloglan", "doru", "hayri", "sakir", "elsa", "chase", "orumcek_adam", "hello_kitty"
};
static const char *const YER_AD[6] = {
  "orman", "deniz", "ev", "park", "\xc5\x9f" "ato", "da\xc4\x9f"
};
static const int8_t FIGUR_YER_N[11] = {
  4, 3, 4, 4, 3, 4, 4, 4, 5, 3, 3
};
static const int8_t FIGUR_YER[N_FIGUR * YER_MAKS] = {
  0, 5, 2, 3, -1, 0, 5, 2, -1, -1, 0, 1, 3, 2, -1, 0, 5, 2, 4, -1, 5, 0, 3, -1,
  -1, 1, 0, 3, 2, -1, 1, 0, 3, 2, -1, 5, 0, 1, 4, -1, 5, 1, 0, 3, 2, 1, 3, 2,
  -1, -1, 3, 0, 2, -1, -1
};
static const int16_t ISTEM_ID[630] = {
  0, 43, 962, 2846, 26, 1511, 286, 2667, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 1511, 286, 2667,
  221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 1511, 286, 2667, 221, 92, 3032, 26, 532, 199, 3953, 26,
  0, 43, 962, 2846, 26, 1511, 286, 2667, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 410, 6721, 221,
  92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 410, 6721, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43,
  962, 2846, 26, 410, 6721, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846, 26, 14441, 6983, 221, 92, 3032, 26,
  1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 14441, 6983, 221, 92, 3032, 26, 1048, 199, 3953, 26, 0, 43, 962, 2846, 26,
  14441, 6983, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 14441, 6983, 221, 92, 3032, 26, 532, 199, 3953,
  26, 0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 11057, 1217,
  488, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 532, 199, 3953,
  26, 0, 43, 962, 2846, 26, 11057, 1217, 488, 221, 92, 3032, 26, 2687, 199, 3953, 26, 0, 43, 962, 2846, 26, 487, 978,
  221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 487, 978, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0,
  43, 962, 2846, 26, 487, 978, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 2434, 1814, 221, 92, 3032,
  26, 1048, 199, 3953, 26, 0, 43, 962, 2846, 26, 2434, 1814, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846,
  26, 2434, 1814, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 2434, 1814, 221, 92, 3032, 26, 532, 199,
  3953, 26, 0, 43, 962, 2846, 26, 862, 13100, 221, 92, 3032, 26, 1048, 199, 3953, 26, 0, 43, 962, 2846, 26, 862, 13100,
  221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 862, 13100, 221, 92, 3032, 26, 531, 199, 3953, 26, 0,
  43, 962, 2846, 26, 862, 13100, 221, 92, 3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846, 26, 12732, 221, 92, 3032, 26,
  1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 12732, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 12732,
  221, 92, 3032, 26, 1048, 199, 3953, 26, 0, 43, 962, 2846, 26, 12732, 221, 92, 3032, 26, 2687, 199, 3953, 26, 0, 43,
  962, 2846, 26, 8309, 383, 69, 221, 92, 3032, 26, 1253, 199, 3953, 26, 0, 43, 962, 2846, 26, 8309, 383, 69, 221, 92,
  3032, 26, 1048, 199, 3953, 26, 0, 43, 962, 2846, 26, 8309, 383, 69, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43,
  962, 2846, 26, 8309, 383, 69, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 8309, 383, 69, 221, 92,
  3032, 26, 532, 199, 3953, 26, 0, 43, 962, 2846, 26, 5530, 1117, 221, 92, 3032, 26, 1048, 199, 3953, 26, 0, 43, 962,
  2846, 26, 5530, 1117, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846, 26, 5530, 1117, 221, 92, 3032, 26, 532,
  199, 3953, 26, 0, 43, 962, 2846, 26, 391, 313, 3960, 3573, 221, 92, 3032, 26, 531, 199, 3953, 26, 0, 43, 962, 2846,
  26, 391, 313, 3960, 3573, 221, 92, 3032, 26, 1238, 199, 3953, 26, 0, 43, 962, 2846, 26, 391, 313, 3960, 3573, 221, 92,
  3032, 26, 532, 199, 3953, 26
};
static const uint16_t ISTEM_OFF[56] = {
  0, 16, 32, 48, 64, 64, 79, 94, 109, 109, 109, 124, 139, 154, 169, 169, 185, 201, 217, 233, 233, 248, 263, 278,
  278, 278, 293, 308, 323, 338, 338, 353, 368, 383, 398, 398, 412, 426, 440, 454, 454, 470, 486, 502, 518, 534, 549, 564,
  579, 579, 579, 596, 613, 630, 630, 630
};
// isim süzgeci (runtime/isim_suzgec.h): figür başına yasaklı adlar ve bayt uzunlukları
static const char *const SUZGEC_AD[958] = {
  "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z",
  "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Canan", "Chase",
  "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fil Necati",
  "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil",
  "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat",
  "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mia",
  "Mimi", "Necati", "Nenee", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder",
  "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi",
  "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila",
  "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z",
  "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Canan", "Chase",
  "Cikcik", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "Ghost",
  "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily",
  "Lucy", "Marshall", "Max", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya",
  "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider",
  "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik", "Yumak$", "Zeynep",
  "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n",
  "Alaca", "Alev$", "Ali", "Amy", "Anna", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca",
  "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "Ghost", "Ghost-Spider", "Hayri",
  "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan",
  "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy",
  "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Necati", "Niloya",
  "Olaf", "Pamuk$", "Paytak", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot",
  "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p",
  "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy",
  "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Basri", "Basri Amca", "Bebee", "Bob", "Boncuk$", "Can$",
  "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir",
  "Fil Necati", "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat",
  "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete",
  "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi",
  "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$",
  "Timmy", "Tom$", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$",
  "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Elif", "Elsa", "Emir",
  "Fil Necati", "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder",
  "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi",
  "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z",
  "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a",
  "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy", "Ghost", "Ghost-Spider",
  "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem",
  "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall",
  "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mete", "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya", "Ninee",
  "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin",
  "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p",
  "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$",
  "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee",
  "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee",
  "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty",
  "Hulk", "Jack", "Jane", "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1",
  "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a",
  "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak",
  "Pepee", "Rubble", "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir",
  "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Annee", "Ay\xc5\x9f" "e", "Bal$",
  "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$",
  "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Emir", "Fil Necati",
  "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil",
  "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "K\xc4\xb1rat",
  "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete",
  "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya", "Ninee", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble",
  "Ryder", "Sam$", "Sara$", "Skye", "Spider", "Spin", "Spot", "Sue", "Tekir", "Tim$", "Timmy", "Tom$",
  "Tosbi", "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$",
  "Can$", "Canan", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir",
  "Fil Necati", "Fluffy", "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye",
  "Kamil", "Karaba\xc5\x9f", "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff",
  "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily", "Lucy", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete",
  "Mia", "Mimi", "Murat", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi",
  "Sam$", "Sara$", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi",
  "Tospik", "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e",
  "Bal$", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$",
  "Can$", "Canan", "Chase", "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa",
  "Emir", "Fil Necati", "Fluffy", "Hayri", "Hello Kitty", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder",
  "Sam$", "Sara$", "Skye", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik",
  "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc5\x9e" "akir", "\xc5\x9eila", "Ahmet", "Ak\xc4\xb1n",
  "Alaca", "Alev$", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal$", "Balk\xc4\xb1z", "Basri",
  "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk$", "Can$", "Canan", "Chase", "Cikcik",
  "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino$", "Doru", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "Ghost", "Ghost-Spider", "Hayri", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f", "Karatay",
  "Kelo\xc4\x9flan", "Kerem", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l", "Lily",
  "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Murat", "Necati", "Nenee",
  "Niloya", "Ninee", "Olaf", "Pamuk$", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder", "Sam$", "Sara$",
  "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim$", "Timmy", "Tom$", "Tosbi", "Tospik",
  "Yumak$", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila"
};
static const uint16_t SUZGEC_AD_OFF[12] = {
  0, 88, 177, 262, 350, 438, 523, 609, 696, 783, 869, 958
};
static const int SUZGEC_AD_UZUN[958] = {
  5, 5, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 8, 13, 3, 7, 4, 5, 5, 6, 5, 5,
  5, 5, 4, 4, 4, 4, 10, 6, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8,
  6, 7, 4, 4, 8, 3, 5, 6, 4, 3, 4, 6, 5, 5, 4, 6, 6, 5, 5, 6, 5, 4, 5, 4,
  6, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6, 6, 8, 14, 6, 5, 5, 5, 5, 5, 3, 3, 4, 5,
  5, 4, 7, 5, 10, 5, 8, 13, 3, 7, 4, 5, 5, 6, 5, 5, 5, 4, 4, 4, 4, 10, 6, 5,
  12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 8, 6, 7, 4, 4, 8, 3, 6, 4, 4, 3,
  4, 5, 6, 5, 6, 5, 4, 6, 6, 5, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 5, 4, 5,
  4, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 5, 5, 3, 3, 4, 5, 4, 7, 5, 10, 8, 13, 3,
  7, 4, 5, 5, 6, 5, 5, 5, 4, 4, 4, 4, 10, 6, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8,
  7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 6, 6, 4, 6, 6,
  5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5, 5,
  5, 5, 3, 3, 4, 5, 5, 4, 5, 10, 5, 3, 7, 4, 5, 5, 6, 5, 5, 5, 5, 4, 4, 4,
  4, 10, 6, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3,
  5, 6, 4, 4, 3, 4, 5, 6, 5, 6, 5, 4, 6, 6, 5, 5, 6, 5, 4, 5, 4, 6, 4, 4,
  3, 4, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 5, 3, 3, 4, 5, 5, 4, 7,
  5, 10, 5, 8, 13, 3, 7, 4, 5, 5, 6, 5, 5, 5, 5, 4, 4, 4, 10, 6, 5, 12, 5, 11,
  4, 4, 4, 7, 5, 8, 9, 5, 5, 9, 8, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 6,
  5, 6, 5, 4, 6, 6, 5, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6,
  6, 6, 8, 14, 6, 5, 5, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 8, 13, 3, 7, 4, 5, 5,
  6, 5, 5, 5, 5, 4, 4, 4, 4, 10, 6, 5, 12, 11, 4, 4, 4, 7, 8, 7, 9, 5, 5, 9,
  8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 3, 4, 5, 6, 5, 6, 5, 4, 6, 6, 5, 5, 6, 5,
  4, 5, 4, 6, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6, 6, 8, 14, 6, 5, 5, 5, 5, 5, 3,
  3, 4, 5, 5, 4, 7, 5, 10, 5, 8, 13, 3, 7, 4, 5, 6, 5, 5, 5, 5, 4, 4, 4, 4,
  6, 5, 12, 5, 11, 4, 4, 4, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6,
  4, 4, 3, 4, 5, 5, 6, 5, 4, 6, 6, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 5, 4,
  5, 4, 5, 6, 6, 6, 8, 14, 5, 5, 5, 5, 5, 3, 3, 5, 5, 4, 7, 5, 10, 5, 8, 13,
  3, 7, 4, 5, 5, 6, 5, 5, 5, 5, 4, 4, 4, 10, 6, 5, 12, 5, 11, 4, 4, 4, 7, 5,
  8, 7, 9, 5, 5, 9, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4, 5, 6, 5, 6, 5, 6,
  6, 5, 5, 6, 5, 4, 5, 4, 6, 4, 4, 3, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5,
  5, 5, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 8, 13, 3, 7, 4, 5, 6, 5, 5, 5,
  5, 4, 4, 4, 4, 10, 6, 5, 12, 5, 11, 4, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6,
  7, 4, 4, 3, 5, 6, 4, 4, 3, 4, 5, 6, 5, 6, 5, 4, 6, 6, 5, 5, 4, 5, 6, 4,
  4, 3, 4, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5, 5, 5, 5, 5, 3, 3, 4, 5, 5,
  4, 7, 5, 10, 5, 8, 13, 3, 7, 4, 5, 5, 6, 5, 5, 5, 5, 4, 4, 4, 4, 10, 6, 5,
  11, 4, 4, 7, 5, 8, 7, 9, 5, 5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 4,
  5, 6, 5, 6, 5, 4, 6, 6, 5, 5, 6, 5, 4, 5, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6,
  6, 6, 8, 6, 5, 5, 5, 5, 5, 3, 3, 4, 5, 5, 4, 7, 5, 10, 5, 8, 13, 3, 7, 4,
  5, 5, 6, 5, 5, 5, 5, 4, 4, 4, 4, 10, 6, 5, 12, 5, 4, 4, 4, 7, 5, 8, 7, 9,
  5, 9, 8, 6, 7, 4, 4, 8, 3, 5, 6, 4, 4, 3, 5, 6, 5, 6, 5, 4, 6, 6, 5, 5,
  6, 5, 4, 5, 4, 6, 4, 4, 3, 4, 5, 4, 5, 4, 5, 6, 6, 6, 8, 14, 6, 5
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
static const char *const URUN_KADRO[54] = {
  "Mete", "Murat", "Niloya", "Tospik", "Da\xc5\x9f" "a", "Koca Ay\xc4\xb1", "Ma\xc5\x9f" "a", "Annee",
  "Bebee", "Dedee", "Nenee", "Ninee", "Pepee", "\xc5\x9eila", "Balk\xc4\xb1z", "Bilgecan", "Bilgecan Dede",
  "Kelo\xc4\x9flan", "Alaca", "Doru", "Karatay", "K\xc4\xb1rat", "Ak\xc4\xb1n", "Basri", "Basri Amca",
  "Hayri", "Kamil", "Mert", "Yumak", "Canan", "Fil Necati", "Kadriye", "Necati", "Remzi", "\xc5\x9e" "akir",
  "Anna", "Elsa", "Kristoff", "Olaf", "Sven", "Chase", "Marshall", "Rubble", "Ryder", "Skye", "Ghost",
  "Ghost-Spider", "Hulk", "Spider", "Spin", "\xc3\x96r\xc3\xbcmcek Adam", "Hello Kitty", "Kitty", "Mimi"
};
static const uint16_t URUN_KADRO_OFF[12] = {
  0, 4, 7, 14, 18, 22, 29, 35, 40, 45, 51, 54
};
static const char *const URUN_IZINLI[69] = {
  "Anne", "Babaanne", "Dede", "Mete", "Murat", "Niloya", "Tospik", "Ay\xc4\xb1", "Da\xc5\x9f" "a", "Koca",
  "Koca Ay\xc4\xb1", "Ma\xc5\x9f" "a", "Annee", "Bebee", "Dedee", "Nenee", "Ninee", "Pepee", "\xc5\x9eila",
  "Balk\xc4\xb1z", "Bilgecan", "Bilgecan Dede", "Dede", "Karaka\xc3\xa7" "an", "Kelo\xc4\x9flan", "Alaca",
  "Doru", "Doruk\xc4\xb1srak", "Karatay", "K\xc4\xb1rat", "Ak\xc4\xb1n", "Amca", "Basri", "Basri Amca",
  "Hayri", "Kamil", "Mert", "Yumak", "Canan", "Fil", "Fil Necati", "Kadriye", "Necati", "Remzi", "\xc5\x9e" "akir",
  "Anna", "Elsa", "Kristoff", "Olaf", "Sven", "Chase", "Marshall", "Rubble", "Ryder", "Skye", "Adam", "Ghost",
  "Ghost-Spider", "Hulk", "Spider", "Spin", "\xc3\x96r\xc3\xbcmcek", "\xc3\x96r\xc3\xbcmcek Adam", "Anne",
  "Baba", "Hello", "Hello Kitty", "Kitty", "Mimi"
};
static const uint16_t URUN_IZINLI_OFF[12] = {
  0, 7, 12, 19, 25, 30, 38, 45, 50, 55, 63, 69
};
static const char *const URUN_TAKINTI_AD[55] = {
  "mete", "murat", "niloy", "tospi", "ay\xc4\xb1", "da\xc5\x9f" "a", "koca", "ma\xc5\x9f" "a", "annee",
  "bebee", "dedee", "nenee", "ninee", "pepee", "\xc5\x9fila", "balk\xc4\xb1", "bilge", "dede", "kelo\xc4\x9f",
  "alaca", "doru", "karat", "k\xc4\xb1rat", "ak\xc4\xb1n", "amca", "basri", "hayri", "kamil", "mert", "yumak",
  "canan", "fil", "kadri", "necat", "remzi", "\xc5\x9f" "akir", "anna", "elsa", "krist", "olaf", "sven",
  "chase", "marsh", "rubbl", "ryder", "skye", "adam", "ghost", "hulk", "spide", "spin", "\xc3\xb6r\xc3\xbcmc",
  "hello", "kitty", "mimi"
};
static const uint16_t URUN_TAKINTI_AD_OFF[12] = {
  0, 4, 8, 15, 19, 23, 30, 36, 41, 46, 52, 55
};
#define URUN_TUM_ISIM_N 54
static const char *const URUN_TUM_ISIM[54] = {
  "Ak\xc4\xb1n", "Alaca", "Anna", "Annee", "Balk\xc4\xb1z", "Basri", "Basri Amca", "Bebee", "Bilgecan",
  "Bilgecan Dede", "Canan", "Chase", "Da\xc5\x9f" "a", "Dedee", "Doru", "Elsa", "Fil Necati", "Ghost",
  "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Kadriye", "Kamil", "Karatay", "Kelo\xc4\x9flan", "Kitty",
  "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "Marshall", "Ma\xc5\x9f" "a", "Mert", "Mete", "Mimi",
  "Murat", "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pepee", "Remzi", "Rubble", "Ryder", "Skye", "Spider",
  "Spin", "Sven", "Tospik", "Yumak", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir", "\xc5\x9eila"
};
#define URUN_TUM_AD_N 92
static const char *const URUN_TUM_AD[92] = {
  "Ahmet", "Ak\xc4\xb1n", "Alaca", "Alev", "Ali", "Amy", "Anna", "Annee", "Ay\xc5\x9f" "e", "Bal", "Balk\xc4\xb1z",
  "Basri", "Basri Amca", "Bebee", "Bilgecan", "Bilgecan Dede", "Bob", "Boncuk", "Can", "Canan", "Chase",
  "Cikcik", "Da\xc5\x9f" "a", "Dedee", "Defne", "Dino", "Doru", "Elif", "Elsa", "Emir", "Fil Necati", "Fluffy",
  "Ghost", "Ghost-Spider", "Hayri", "Hello Kitty", "Hulk", "Jack", "Jane", "Kadriye", "Kamil", "Karaba\xc5\x9f",
  "Karatay", "Kelo\xc4\x9flan", "Kerem", "Kitty", "Koca Ay\xc4\xb1", "Kristoff", "K\xc4\xb1rat", "K\xc4\xb1z\xc4\xb1l",
  "Lily", "Lucy", "Marshall", "Max", "Ma\xc5\x9f" "a", "Mehmet", "Mert", "Mete", "Mia", "Mimi", "Murat",
  "Necati", "Nenee", "Niloya", "Ninee", "Olaf", "Pamuk", "Paytak", "Pepee", "Remzi", "Rubble", "Ryder",
  "Sam", "Sara", "Skye", "Spider", "Spin", "Spot", "Sue", "Sven", "Tekir", "Tim", "Timmy", "Tom", "Tosbi",
  "Tospik", "Yumak", "Zeynep", "Z\xc4\xb1pz\xc4\xb1p", "\xc3\x96r\xc3\xbcmcek Adam", "\xc5\x9e" "akir",
  "\xc5\x9eila"
};
#define URUN_ISIM_KELIME_N 55
static const char *const URUN_ISIM_KELIME[55] = {
  "adam", "ak\xc4\xb1n", "alaca", "amca", "anna", "annee", "ay\xc4\xb1", "balk\xc4\xb1z", "basri", "bebee",
  "bilgecan", "canan", "chase", "da\xc5\x9f" "a", "dede", "dedee", "doru", "elsa", "fil", "ghost", "hayri",
  "hello", "hulk", "kadriye", "kamil", "karatay", "kelo\xc4\x9flan", "kitty", "koca", "kristoff", "k\xc4\xb1rat",
  "marshall", "ma\xc5\x9f" "a", "mert", "mete", "mimi", "murat", "necati", "nenee", "niloya", "ninee",
  "olaf", "pepee", "remzi", "rubble", "ryder", "skye", "spider", "spin", "sven", "tospik", "yumak", "\xc3\xb6r\xc3\xbcmcek",
  "\xc5\x9f" "akir", "\xc5\x9fila"
};
#define URUN_TAKINTI_HARIC_N 20
static const char *const URUN_TAKINTI_HARIC[20] = {
  "art\xc4\xb1k", "birde", "birli", "bunu", "daha", "dedi", "de\xc4\x9fil", "gibi", "hemen", "ikisi", "i\xc3\xa7in",
  "kadar", "onlar", "onun", "sonra", "yava\xc5\x9f", "\xc3\xa7ok", "\xc3\xa7ok\xc3\xa7" "a", "\xc3\xa7\xc3\xbcnk\xc3\xbc",
  "\xc5\x9fimdi"
};
