# Son model c3ft_v5 (28 493 hikâye) – ara model c3ft_v5a (26 045 hikâye): ürün figürlerinde kör ikili kıyas

- **c3ft_v5:** urun_v2 hakemli 1030 + urun_v3 9567 + urun_v4 5922 + urun_v5 11 974 (yeni 12 figür, 991–1000/figür;
  gece/ninni hariç, `birlestir urun_karma4 urun_v3 urun_v4 urun_v5 --gecesiz`) = 28 493 hikâye.
  `TAG=c3ft_v5 IZIN=data/urun_karma4/izin.txt TEKRAR=2 GENEL=8000000 STEPS=15000 bash zincir_urun.sh` (bulutta CPU,
  ~1,4 s/adım; kap iki kez yeniden başladı, kayıttan sürdü). En iyi adım 14 250, val **1,888** (aynı 41 hikâyelik
  doğrulama bölmesi). Golden testi geçti (C = PyTorch). model.bin 10,33 MB (boyut aynı).
- **c3ft_v5a:** 26 045 hikâye (urun_v5'in ~%80'i), 14 000 adım, val 1,901 (`urun_kiyas_v5a/OZET.md`).

Aynı 180 vaka (13 ürün figürü × yerler × 4 tohum), ikisi de 8 aday + isim süzgeci + seçici (`urun_uret.py
--aday 8 --tekrar-vaka 4`). Seçici puanı: v5 −2,011 (157 cezasız) – v5a −2,034 (156 cezasız); ikisinde de yanlış
isim, bozuk plan, bitmemiş hikâye yok.

4 parti × 45 vaka × 2 hakem (IKILI_GENEL.md, IKILI.md; `hakem/`); A/B sırası rastgele (tohum 7373), anahtar
hakemlik süresince klasör dışındaydı (`anahtar.json` sonradan kondu). A konumunda v5 97/180; A seçimi genel 97,
olay 92 (konum yanlılığı görünmüyor).

| Hakem | v5 | v5a | eşit | p (tek yönlü işaret testi, v5 > v5a) |
|---|---|---|---|---|
| Genel kalite | 102 | 78 | 0 | 0,043 |
| Olay örgüsü | 99 | 73 | 8 | 0,028 |

Figür başına (v5–v5a):

| Figür | genel | olay |
|---|---|---|
| Alaaddin | 10–6 | 9–6 (1 eşit) |
| Bilge Baykuş | 6–6 | 4–8 |
| Bip | 7–5 | 6–6 |
| Bulut | 7–5 | 6–3 (3 eşit) |
| Ejderha Yavrusu | 8–8 | 11–4 (1 eşit) |
| Fıstık | 7–5 | 6–6 |
| Keloğlan | 6–10 | 7–9 |
| Nasreddin Hoca | 11–5 | 11–5 |
| Pamuk Prenses | 12–4 | 11–5 |
| Pinokyo | 7–5 | 8–3 (1 eşit) |
| Tek Boynuzlu At | 10–6 | 8–7 (1 eşit) |
| Tontiş | 6–6 | 4–8 |
| Zıpzıp | 5–7 | 8–3 (1 eşit) |

Figür başına sayılar küçük (12–16 vaka); tek tek anlamlı değil.

**Sonuç:** son model ara modeli ürün figürlerinde küçük ama anlamlı farkla geçti (iki hakemde de p < 0,05).
Kalan %20 veri ve 1000 adım daha ölçülebilir kazanç verdi; geri gidiş yok. Keloğlan'daki v5a eğilimi (6–10, 7–9)
16 vakada anlamlı değil; ürün modeli c3ft_karma ile Keloğlan'a özel kıyas `urun_kiyas_v5_kel/`.
