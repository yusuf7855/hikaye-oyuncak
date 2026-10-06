// Hikâye kuyruğu: oyuncak boştayken önceden üretilen hikâyeler flash'taki "kuyruk" bölümünde saklanır.
//
// Bölüm (partitions.csv, data alt tip 0x42) 4 KB'lık sektörlere bölünür; her sektör bir yuva, her yuvada bir hikâye:
//   [0..32)  KuyrukBaslik (sihir, imza, sıra, figür, yer, K, token sayıları, puan, CRC, tüketildi)
//   [32..)   token'lar (int16: plan + gövde, gövdedeki EOT hariç; en çok KUYRUK_TOK_MAKS)
// Yazma sırası güç kesilmesine dayanıklıdır: sektör silinir -> token'lar -> başlık (sihir hariç) -> en son sihir.
// Sihir yoksa ya da CRC tutmuyorsa yuva boş sayılır (yarım yazılmış ya da eski bölümden kalma çöp). Bir hikâye
// çalınınca "tüketildi" sözcüğü silmeden 0 yazılır (NOR flash'ta 1 -> 0 serbest); sektör ancak yuvaya yeni hikâye
// yazılırken silinir (konuşurken hiç silme yok). Yeni hikâye son yazılan yuvadan sonraki ilk boş/tüketilmiş yuvaya
// gider: yuvalar sırayla döner (aşınma dengesi). İmza (model parmak izi + istem tablosu) değişirse eski hikâyeler
// geçersiz sayılır.
//
// Kullanım: KuyrukFlash fl = {kul, oku, yaz, sil, boyut}; Kuyruk q; kuyruk_kur(&q, &fl, imza);
//   kuyruk_sonraki(&q, ...) -> sıradaki üretilecek (figür, yer) | kuyruk_yaz(...) | kuyruk_bul + kuyruk_oku +
//   kuyruk_tuket. Başlık hem C (tools/kuyruk_test.c) hem C++ (.ino) olarak derlenir; ESP'ye bağımlı değildir.
#pragma once
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#if defined(__GNUC__)
#define KUYRUK_API static __attribute__((unused))
#else
#define KUYRUK_API static
#endif

#define KUYRUK_SEKTOR 4096
#define KUYRUK_YUVA_MAKS 64
#define KUYRUK_SIHIR 0x3159484Bu   // "KHY1" (küçük uçlu)
#define KUYRUK_SURUM 1
#define KUYRUK_BASLIK 32
#define KUYRUK_TOK_MAKS ((KUYRUK_SEKTOR - KUYRUK_BASLIK) / 2)

typedef struct {
  uint32_t sihir;       // en son yazılır; KUYRUK_SIHIR değilse yuva boş
  uint32_t imza;        // model + istem tablosu imzası; farklıysa geçersiz
  uint32_t sira;        // yazılış sırası (1, 2, ...): en eskisi önce çalınır, yuvalar bu sırayla döner
  uint8_t figur, yer;   // figür (0..), figürün kart yeri (0..; YER_AD değil, FIGUR_YER indeksi)
  uint8_t K, surum;     // aday sayısı, KUYRUK_SURUM
  uint16_t n, n_plan;   // token sayısı (plan + gövde), plan token sayısı
  float puan;           // seçici puanı
  uint32_t crc;         // CRC-32: imza..puan (20 B) + token'lar
  uint32_t tuketildi;   // 0xFFFFFFFF: hazır | 0: çalındı
} KuyrukBaslik;
typedef char kuyruk_baslik_32_bayt[sizeof(KuyrukBaslik) == KUYRUK_BASLIK ? 1 : -1];

typedef struct {
  void *kul;
  int (*oku)(void *kul, uint32_t ofs, void *buf, uint32_t n);         // 0: tamam
  int (*yaz)(void *kul, uint32_t ofs, const void *buf, uint32_t n);   // 0: tamam (yalnız 1 -> 0)
  int (*sil)(void *kul, uint32_t ofs, uint32_t n);                    // ofs, n KUYRUK_SEKTOR katı
  uint32_t boyut;
} KuyrukFlash;

enum { KY_BOS = 0, KY_HAZIR = 1, KY_TUKENDI = 2 };

typedef struct {
  uint8_t durum, figur, yer, K;
  uint32_t sira;
  float puan;
} KuyrukYuva;

typedef struct {
  KuyrukFlash fl;
  int n_yuva;
  uint32_t imza, son_sira;
  int son_yuva;          // en son yazılan yuva (-1 yok)
  KuyrukYuva y[KUYRUK_YUVA_MAKS];
} Kuyruk;

KUYRUK_API uint32_t kuyruk_crc(uint32_t crc, const void *veri, size_t n) {
  const uint8_t *p = (const uint8_t *)veri;
  crc = ~crc;
  while (n--) {
    crc ^= *p++;
    for (int k = 0; k < 8; k++) crc = (crc >> 1) ^ (0xEDB88320u & (0u - (crc & 1u)));
  }
  return ~crc;
}

// FNV-1a: imza hesabı için (model parmak izi + tablolar)
KUYRUK_API uint32_t kuyruk_fnv(uint32_t h, const void *veri, size_t n) {
  const uint8_t *p = (const uint8_t *)veri;
  while (n--) { h ^= *p++; h *= 16777619u; }
  return h;
}

KUYRUK_API uint32_t kuyruk_baslik_crc(const KuyrukBaslik *b, const int16_t *tok) {
  uint32_t c = kuyruk_crc(0, (const uint8_t *)b + 4, 20);
  return kuyruk_crc(c, tok, (size_t)b->n * 2);
}

// Token'ları flash'tan parça parça okuyup CRC'yi tamamlar (tarama: büyük tampon gerekmesin). Döner: 0 okunamadı.
KUYRUK_API int kuyruk_flash_crc(Kuyruk *q, uint32_t ofs, uint32_t n, uint32_t *crc) {
  uint8_t parca[256];
  for (uint32_t i = 0; i < n; i += sizeof parca) {
    uint32_t k = n - i < sizeof parca ? n - i : (uint32_t)sizeof parca;
    if (q->fl.oku(q->fl.kul, ofs + i, parca, k)) return 0;
    *crc = kuyruk_crc(*crc, parca, k);
  }
  return 1;
}

// Yuvanın başlığını ve (tok != NULL ise kap'a kadar) token'larını okur, doğrular. Döner: KY_BOS / KY_HAZIR /
// KY_TUKENDI (token'lar kap'a sığmıyorsa KY_BOS).
KUYRUK_API int kuyruk_yuva_oku(Kuyruk *q, int i, KuyrukBaslik *b, int16_t *tok, int kap) {
  uint32_t ofs = (uint32_t)i * KUYRUK_SEKTOR;
  if (q->fl.oku(q->fl.kul, ofs, b, sizeof *b)) return KY_BOS;
  if (b->sihir != KUYRUK_SIHIR || b->imza != q->imza || b->surum != KUYRUK_SURUM || b->n == 0 ||
      b->n > KUYRUK_TOK_MAKS || b->n_plan > b->n || (tok && b->n > kap))
    return KY_BOS;
  if (tok) {
    if (q->fl.oku(q->fl.kul, ofs + KUYRUK_BASLIK, tok, (uint32_t)b->n * 2)) return KY_BOS;
    if (kuyruk_baslik_crc(b, tok) != b->crc) return KY_BOS;
  } else {
    uint32_t c = kuyruk_crc(0, (const uint8_t *)b + 4, 20);
    if (!kuyruk_flash_crc(q, ofs + KUYRUK_BASLIK, (uint32_t)b->n * 2, &c) || c != b->crc) return KY_BOS;
  }
  return b->tuketildi == 0xFFFFFFFFu ? KY_HAZIR : KY_TUKENDI;
}

// Bölümü tarar (açılışta). Döner: hazır hikâye sayısı; bölüm küçükse -1.
KUYRUK_API int kuyruk_kur(Kuyruk *q, const KuyrukFlash *fl, uint32_t imza) {
  memset(q, 0, sizeof *q);
  q->fl = *fl;
  q->imza = imza;
  q->son_yuva = -1;
  q->n_yuva = (int)(fl->boyut / KUYRUK_SEKTOR);
  if (q->n_yuva > KUYRUK_YUVA_MAKS) q->n_yuva = KUYRUK_YUVA_MAKS;
  if (q->n_yuva < 2) return -1;
  int hazir = 0;
  for (int i = 0; i < q->n_yuva; i++) {
    KuyrukBaslik b;
    KuyrukYuva *y = &q->y[i];
    y->durum = (uint8_t)kuyruk_yuva_oku(q, i, &b, NULL, 0);
    if (y->durum == KY_BOS) continue;
    y->figur = b.figur; y->yer = b.yer; y->K = b.K; y->sira = b.sira; y->puan = b.puan;
    if (y->durum == KY_HAZIR) hazir++;
    if (b.sira >= q->son_sira) { q->son_sira = b.sira; q->son_yuva = i; }
  }
  return hazir;
}

// f figürünün (j >= 0 ise yalnız o yerin) hazır hikâye sayısı
KUYRUK_API int kuyruk_say(const Kuyruk *q, int f, int j) {
  int n = 0;
  for (int i = 0; i < q->n_yuva; i++)
    n += q->y[i].durum == KY_HAZIR && (f < 0 || q->y[i].figur == f) && (j < 0 || q->y[i].yer == j);
  return n;
}

// f figürü (j >= 0 ise o yer) için en eski hazır hikâyenin yuvası; yoksa -1
KUYRUK_API int kuyruk_bul(const Kuyruk *q, int f, int j) {
  int en = -1;
  for (int i = 0; i < q->n_yuva; i++) {
    const KuyrukYuva *y = &q->y[i];
    if (y->durum != KY_HAZIR || y->figur != f || (j >= 0 && y->yer != j)) continue;
    if (en < 0 || y->sira < q->y[en].sira) en = i;
  }
  return en;
}

// Yuvadaki hikâyeyi tok'a (kap token) okur, CRC denetimli. Döner: token sayısı; bozuksa ya da sığmıyorsa 0 (yuva boş
// sayılır).
KUYRUK_API int kuyruk_oku(Kuyruk *q, int i, KuyrukBaslik *b, int16_t *tok, int kap) {
  if (i < 0 || i >= q->n_yuva) return 0;
  int d = kuyruk_yuva_oku(q, i, b, tok, kap);
  if (d != KY_HAZIR) { q->y[i].durum = (uint8_t)d; return 0; }
  return b->n;
}

// Yuvadaki hikâyeyi çalındı işaretler (silmeden 4 bayt 0). Döner: 0 tamam.
KUYRUK_API int kuyruk_tuket(Kuyruk *q, int i) {
  if (i < 0 || i >= q->n_yuva || q->y[i].durum != KY_HAZIR) return -1;
  uint32_t sifir = 0;
  q->y[i].durum = KY_TUKENDI;
  return q->fl.yaz(q->fl.kul, (uint32_t)i * KUYRUK_SEKTOR + 28, &sifir, 4);
}

// Bütün hazır hikâyeleri çalındı işaretler (silmez). Döner: işaretlenen sayısı.
KUYRUK_API int kuyruk_temizle(Kuyruk *q) {
  int n = 0;
  for (int i = 0; i < q->n_yuva; i++)
    if (q->y[i].durum == KY_HAZIR && kuyruk_tuket(q, i) == 0) n++;
  return n;
}

// Yeni hikâyeyi son yazılandan sonraki ilk boş/tüketilmiş yuvaya yazar. Döner: yuva; yer yoksa ya da hata: -1.
KUYRUK_API int kuyruk_yaz(Kuyruk *q, int f, int j, int K, float puan, const int16_t *tok, int n, int n_plan) {
  if (n <= 0 || n > KUYRUK_TOK_MAKS || n_plan < 0 || n_plan > n) return -1;
  int i = -1;
  for (int k = 1; k <= q->n_yuva; k++) {
    int a = (q->son_yuva + k + q->n_yuva) % q->n_yuva;
    if (q->y[a].durum != KY_HAZIR) { i = a; break; }
  }
  if (i < 0) return -1;
  KuyrukBaslik b;
  memset(&b, 0xFF, sizeof b);
  b.sihir = KUYRUK_SIHIR; b.imza = q->imza; b.sira = q->son_sira + 1;
  b.figur = (uint8_t)f; b.yer = (uint8_t)j; b.K = (uint8_t)K; b.surum = KUYRUK_SURUM;
  b.n = (uint16_t)n; b.n_plan = (uint16_t)n_plan; b.puan = puan;
  b.crc = kuyruk_baslik_crc(&b, tok);
  uint32_t ofs = (uint32_t)i * KUYRUK_SEKTOR;
  q->y[i].durum = KY_BOS;  // silindi: yazma yarıda kalırsa boş
  if (q->fl.sil(q->fl.kul, ofs, KUYRUK_SEKTOR)) return -1;
  q->son_yuva = i;         // silinen yuva da dönüşte "son" sayılır (hata tekrarında aynı sektör dövülmesin)
  if (q->fl.yaz(q->fl.kul, ofs + KUYRUK_BASLIK, tok, (uint32_t)n * 2)) return -1;
  if (q->fl.yaz(q->fl.kul, ofs + 4, (const uint8_t *)&b + 4, 24)) return -1;      // imza..crc (tüketildi FF kalır)
  if (q->fl.yaz(q->fl.kul, ofs, &b, 4)) return -1;                                 // en son sihir
  KuyrukBaslik d;  // geri oku: yazma gerçekten tuttu mu
  if (kuyruk_yuva_oku(q, i, &d, NULL, 0) != KY_HAZIR) return -1;
  q->son_sira = b.sira;
  KuyrukYuva *y = &q->y[i];
  y->durum = KY_HAZIR; y->figur = (uint8_t)f; y->yer = (uint8_t)j; y->K = (uint8_t)K; y->sira = b.sira; y->puan = puan;
  return i;
}

// Sıradaki üretilecek (figür, yer): hazır hikâyesi figur_basi'ndan az olan figürlerden en azı olanı (eşitse son
// üretimi en eski olanı, o da eşitse küçük numaralısı); figürün yerlerinden hazırı en az olanı (eşitse son üretimi en
// eski). yer_n[f]: figürün yer sayısı. Döner: 1 iş var, 0 kuyruk dolu.
KUYRUK_API int kuyruk_sonraki(const Kuyruk *q, int figur_basi, int n_figur, const int8_t *yer_n, int *f_out, int *j_out) {
  int bos = 0;
  for (int i = 0; i < q->n_yuva; i++) bos += q->y[i].durum != KY_HAZIR;
  if (!bos) return 0;
  int en_f = -1, en_say = 0;
  uint32_t en_sira = 0;
  for (int f = 0; f < n_figur; f++) {
    int say = kuyruk_say(q, f, -1);
    if (say >= figur_basi) continue;
    uint32_t son = 0;  // figürün en son üretilen hikâyesinin sırası (çalınmış olsa da; hiç yoksa 0)
    for (int i = 0; i < q->n_yuva; i++)
      if (q->y[i].durum != KY_BOS && q->y[i].figur == f && q->y[i].sira > son) son = q->y[i].sira;
    if (en_f < 0 || say < en_say || (say == en_say && son < en_sira)) { en_f = f; en_say = say; en_sira = son; }
  }
  if (en_f < 0) return 0;
  int en_j = 0, en_js = 1 << 30;
  uint32_t en_jsira = 0;
  for (int j = 0; j < yer_n[en_f]; j++) {
    int say = kuyruk_say(q, en_f, j);
    uint32_t son = 0;
    for (int i = 0; i < q->n_yuva; i++)
      if (q->y[i].durum != KY_BOS && q->y[i].figur == en_f && q->y[i].yer == j && q->y[i].sira > son) son = q->y[i].sira;
    if (say < en_js || (say == en_js && son < en_jsira)) { en_j = j; en_js = say; en_jsira = son; }
  }
  *f_out = en_f;
  *j_out = en_j;
  return 1;
}
