// isim_suzgec.h birim testi: küçük bir sahte sözlükle kabul/ret kararları. tests/test_isim_suzgec.py derleyip koşar.
// cc -O2 -o isim_suzgec_test runtime/host_verify/isim_suzgec_test.c && ./isim_suzgec_test
#include <stdio.h>
#include <string.h>
#include "../isim_suzgec.h"

static const char *TOK[] = {" O", "laf", " Orman", " N", "il", "oya", "'ya", " Tim", "sah", " ile", ",", "\xE2\x80\x99",
                            "nin", "\"", "Olaf", " Nil", "\xC3\xBC" /* ü */};
enum { T_O, T_LAF, T_ORMAN, T_N, T_IL, T_OYA, T_YA, T_TIM, T_SAH, T_ILE, T_VIRGUL, T_KESME, T_NIN, T_TIRNAK, T_OLAF,
       T_NIL, T_U, V };
static int uzun[V];
static const char *ADLAR[] = {"Olaf", "Niloya", "Tim$"};
static int ad_uzun[3];
static int hata = 0;

static void dene(const char *ad, const int *once, int n_once, int aday, int beklenen) {
  IsimSuzgec s;
  isim_suzgec_kur(&s, TOK, uzun, V, ADLAR, ad_uzun, 3);
  for (int i = 0; i < n_once; i++) isim_suzgec_ekle(&s, once[i]);
  int r = isim_suzgec_uygun(&s, aday);
  if (r != beklenen) { printf("HATA %s: %d bekleniyordu, %d\n", ad, beklenen, r); hata++; }
}

int main(void) {
  for (int i = 0; i < V; i++) uzun[i] = (int)strlen(TOK[i]);
  for (int i = 0; i < 3; i++) ad_uzun[i] = (int)strlen(ADLAR[i]);
  dene("' O' serbest", NULL, 0, T_O, 1);
  dene("' O'+'laf' red", (int[]){T_O}, 1, T_LAF, 0);
  dene("' Orman' serbest", NULL, 0, T_ORMAN, 1);
  dene("'Olaf' metin başı red", NULL, 0, T_OLAF, 0);
  dene("'\"Olaf' red", (int[]){T_TIRNAK}, 1, T_OLAF, 0);
  dene("' N'+'il' serbest", (int[]){T_N}, 1, T_IL, 1);
  dene("' Nil' serbest", NULL, 0, T_NIL, 1);
  dene("' N'+'il'+'oya' red", (int[]){T_N, T_IL}, 2, T_OYA, 0);
  dene("'ü'+'Olaf' kelime içi serbest", (int[]){T_U}, 1, T_OLAF, 1);
  dene("' Tim' tek başına henüz serbest ($)", NULL, 0, T_TIM, 1);
  dene("' Tim'+'sah' serbest ($)", (int[]){T_TIM}, 1, T_SAH, 1);
  dene("' Tim'+' ile' red ($)", (int[]){T_TIM}, 1, T_ILE, 0);
  dene("' Tim'+',' red ($)", (int[]){T_TIM}, 1, T_VIRGUL, 0);
  dene("' Tim'+'’' red ($, kıvrık kesme)", (int[]){T_TIM}, 1, T_KESME, 0);
  dene("'’'+'Olaf' red (kıvrık kesme sınırdır)", (int[]){T_KESME}, 1, T_OLAF, 0);
  if (!hata) printf("isim_suzgec: tamam\n");
  return hata != 0;
}
