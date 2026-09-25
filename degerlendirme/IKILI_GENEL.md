# Kör ikili tercih: genel kalite (çocuğa okunabilirlik)

Hikâyeler 3–6 yaş çocuklara bir oyuncak tarafından sesli okunacak. Her vakada aynı istekten (aynı figür(ler), aynı
yer) yazılmış iki hikâye var: **A** ve **B**. Hangi sistemden geldikleri gizli, sıraları her vakada rastgele.

**Soru:** Bir ebeveyn olarak çocuğuna hangisini okumayı tercih ederdin?

Şunlara bak (hepsi önemli, önem sırasıyla):

1. **Karakter tutarlılığı** — Aynı karakter iki kez tanıtılıyor mu ("X adında ... yaşardı" iki kez)? Karakter kendi
   kendine mi davranıyor ("Paytak, Paytak'ı görünce")? Başka biri figürün adını kendi adı gibi söylüyor mu? Birinin
   özelliği başkasına mı geçmiş (köpeğin gagası, tavşanın baloncuk üflemesi)? Hikâyede tanıtılmamış isimler var mı?
2. **Mantık** — Sorun açık mı, çözüm o sorunu mu çözüyor, olaylar birbirine bağlı mı? Sondaki ders ("... olduğunu
   anladı") hikâyede olan bir şeyden mi çıkıyor?
3. **Dil** — Kekeme tekrarlar ("üzgün üzgün üzgün", "kucağına aldı ve kucağına aldı"), anlamsız cümleler, uydurma
   kelimeler, anlaşılmayı engelleyen bozukluklar.
4. **Çocuğa uygunluk** — kan, yara, tehlike gibi korkutucu ayrıntılar.

## Karar

- Genel olarak daha iyi olanı seç: `"A"` ya da `"B"`. Fark küçük olsa da bir taraf seç.
- `"esit"` yalnızca gerçekten ayırt edilemiyorsa.
- Uzunluğa bakma. Hangi sistemin yazdığını tahmin etmeye çalışma. Her vakayı ayrı değerlendir.

## Girdi ve çıktı

Yalnızca sana verilen `parti_N.json` dosyasını oku (aynı klasördeki başka dosyaları açma). Biçimi:
`[{"id": 7, "A": "hikâye metni ...", "B": "hikâye metni ..."}]`

Sana söylenen çıktı yoluna, aynı sırada, her vaka için bir kayıt yaz:
`[{"id": 7, "karar": "A", "neden": "B'de Paytak iki kez tanıtılıyor ve sonda kendi kendine teşekkür ediyor."}]`
`karar` yalnızca `"A"`, `"B"` ya da `"esit"`; `neden` tek satır (en fazla ~25 kelime).
