# Ara model c3ft_v5a (26 045 hikâye) – ürün modeli c3ft_karma (10 597 hikâye): kör ikili kıyas

- **c3ft_v5a:** urun_v2 hakemli 1030 + urun_v3 9567 + urun_v4 5922 + urun_v5 9526 (yeni 12 figür, yazımın ~%80'i;
  gece/ninni metinleri hariç, `birlestir urun_karma3 urun_v3 urun_v4 urun_v5 --gecesiz`) = 26 045 hikâye.
  `IZIN=data/urun_karma3/izin.txt TEKRAR=2 GENEL=8000000 STEPS=14000 zincir_urun.sh` (bulutta CPU, ~4 saat),
  en iyi adım 13 750, val 1,901 (aynı 41 hikâyelik doğrulama bölmesi). Golden testi geçti (C = PyTorch).
- **c3ft_karma:** 10 597 hikâye, 6000 adım, val 2,015 (`degerlendirme/urun_kiyas_karma/OZET.md`).
- Model boyutu aynı (c3, model.bin 10,3 MB).

Aynı 164 vaka (eski 11 figür; 41 figür×yer × 4 tohum), ikisi de 8 aday + isim süzgeci + seçici (`urun_uret.py
--aday 8 --tekrar-vaka 4`). c3ft_karma tarafı `urun_kiyas_karma2/mkarma.json` (güncel seçiciyle yeniden seçilmiş).
Seçici puanı: v5a −1,99 (130 cezasız) – karma −2,05 (133 cezasız).

4 parti × 2 hakem (IKILI_GENEL.md, IKILI.md; `hakem/`); A/B sırası rastgele (tohum 5151), anahtar hakemlik
süresince klasör dışındaydı (`anahtar.json` sonradan kondu). A konumu seçimi 83/164 ve 84/164 (konum yanlılığı yok).

| Hakem | v5a | karma | eşit | p (tek yönlü işaret testi, v5a > karma) |
|---|---|---|---|---|
| Genel kalite | 106 | 58 | 0 | 0,0001 |
| Olay örgüsü | 96 | 62 | 6 | 0,004 |

Figür başına (genel, v5a–karma): Chase 14–6, Doru 9–3, Elsa 8–8, Hayri 8–8, Hello Kitty 8–4, Keloğlan 11–5,
Maşa 7–5, Niloya 11–5, Örümcek Adam 6–6, Pepee 14–2, Kral Şakir 10–6. Hiçbir figürde karma önde değil.
Olay örgüsünde Hayri (5–9) ve Keloğlan (7–8) karma lehine.

**Sonuç:** ara model eski 11 figürde ürün modelini açık farkla geçti; yeni figür verisi eski figürleri bozmadı,
tersine iyileştirdi. c3ft_karma2 (16,5 bin, 10 000 adım) aynı kıyasta fark göstermemişti (83–81). Bu adımda
hem veri (urun_v5) hem eğitim (14 000 adım, 8 M genel jeton) arttığı için kazancın ne kadarının hangisinden
geldiği ayrılamaz. Son model urun_v5 tamamlanınca (1000/figür) bütün veriyle aynı ayarlarla eğitilecek.
