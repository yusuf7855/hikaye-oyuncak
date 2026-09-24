# Hikâye hakem rubriği (10 puan)

Hikâyeler 3–6 yaş çocuklara bir oyuncak tarafından sesli okunacak. Figür(ler) çocuğun okuttuğu oyuncak
karakterlerdir; hikâye onlar hakkında olmalı. Katı ol: bir ebeveyn "bu saçma" diyecekse puan düşer.

Her hikâyeye 1–10 arası TAM SAYI puan ver. Başlangıç 10; her kusur için düş:

| Kusur | Düşüş |
|---|---|
| İstenen figür(ler)den biri yok / başka bir figür ana karakter olmuş / isim ya da tür yanlış (Tekir adında tavşan) | −4 |
| Karakter karışıklığı: figür kendi kendine konuşuyor, aynı isim iki kişiyi gösteriyor, kim konuştuğu anlaşılmıyor | −3 |
| Olay mantıksız ya da tutarsız (nesne anlamsızca canlanıyor, sebep-sonuç yok, çelişki) — her belirgin örnek | −2 (en fazla −4) |
| Anlamsız / uydurma kelime, bozuk dilbilgisi cümlesi — her örnek | −1 (en fazla −3) |
| Figürün bilinen özelliğiyle çelişki (yavaş Tosbi koşuyor, Alev ateş püskürüyor) | −1 |
| Aynı olay/cümle gereksiz tekrarı | −1 |
| Yarım kalan, kopuk ya da sonu olmayan hikâye | −2 |
| Çocuğa uygun olmayan içerik (korkutucu, şiddet) | −5 |

10 = bir çocuk kitabında basılabilir: doğru figürler, net olay örgüsü, akıcı Türkçe, sıcak bir son.
7 = küçük pürüzler var ama çocuk sorunsuz dinler. 5 = anlaşılır ama belirgin hatalar. ≤3 = karışık/saçma.

Figür bilgileri (tür → isim, özellik): tavşan Pamuk (bembeyaz, utangaç, havuç) · kedi Tekir (çizgili, meraklı) ·
köpek Karabaş (sadık, top oyunu) · ayı Bal (kocaman, bal sever, uykucu) · tilki Kızıl (turuncu, akıllı, plan) ·
kuş Cikcik (minik, şarkı söyler, uçar) · kaplumbağa Tosbi (yavaş, sabırlı, bilge) · penguen Paytak (paytak yürür,
kayar, yüzer) · dinozor Dino (uzun boyunlu, büyük ama nazik) · ejderha Alev (ateş yerine renkli baloncuk üfler) ·
kız Elif (meraklı, cesur) · oğlan Can (enerjik, yardımsever).

## Olay örgüsü soruları (puanı değiştirmez)

Puanı yalnızca yukarıdaki tabloyla ver. Aşağıdaki sorular ayrıca kaydedilir, puana ek düşüş getirmez; böylece eski
puanlarla karşılaştırma bozulmaz. Hikâyenin teması sana verilmez: temaya uyup uymadığına değil, sorun–çözüm bağına bak.

- **s1** — Hikâyede tek cümleyle söylenebilen bir sorun var mı? (istek, engel, kayıp, korku, anlaşmazlık:
  "Pamuk'un havucu kuyuya düştü.") Olayların art arda sıralanması (gezdi, oynadı, yedi) sorun değildir.
- **s2** — Sonda çözülen şey o sorun mu? Sorun unutulup başka bir şey çözülüyorsa, hikâye sorunu çözmeden bitiyorsa ya
  da son yalnızca "çok mutlu oldular" diyorsa `false`. s1 `false` ise s2 de `false`.
- **s3** — Aradaki olaylar o sorunla ilgili mi? Hikâye ortada başka bir olaya kayıyorsa (top kaybı → yuva kaybı) ya da
  sorunla ilgisiz uzun bir bölüm varsa `false`; tek kısa ilgisiz cümle s3'ü bozmaz. s1 `false` ise s3 de `false`.
- **mantiksiz** — "Olay mantıksız ya da tutarsız" satırındaki belirgin örneklerin sayısı (tam sayı, ≥ 0). −4 sınırı
  sayıyı kesmez: 3 örnek varsa puandan −4 düşülür ama `"mantiksiz": 3` yazılır. `mantiksiz` ≥ 1 ise `kategoriler`
  "mantiksiz" içerir, 0 ise içermez.

## Çıktı biçimi

Sana verilen `parti_N.json` için aynı sırada, her hikâyeye bir kayıt içeren bir JSON listesi yaz: ilk hakem
`puan_N.json`, ikinci bağımsız hakem `puan_N_b.json` (diğer hakemin dosyasını açma).

```json
[{"id": 0, "puan": 6, "kategoriler": ["mantiksiz", "tekrar"], "s1": true, "s2": false, "s3": true,
  "mantiksiz": 1, "not": "Tek cümle: puanı en çok düşüren kusur."}]
```

`kategoriler` tablodaki satırların adlarıdır (sırasıyla): `figur_yanlis`, `karakter_karisik`, `mantiksiz`,
`bozuk_dil`, `ozellik_celiski`, `tekrar`, `yarim_son`, `uygunsuz`. Kusur yoksa boş liste.
