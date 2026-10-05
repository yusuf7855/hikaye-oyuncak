import json
M="mantiksiz";D="bozuk_dil";K="karakter_karisik";T="tekrar";Y="yarim_son";U="uygunsuz";F="figur_yanlis"
R=[
(0,4,[M,D,T],0,0,0,2,"Şapkanın kağıt uçağa takılması anlamsız, sorun-çözüm yok."),
(8,4,[M,D],0,0,0,3,"Bulduğu çiçeği kendisinin yaptığı çelişkisi ve kağıt çiçeği yemesi."),
(16,1,[K,M,D,U],0,0,0,4,"Çocuk hikâyesinde şarap ve çalma; Niloya kendine sarılıyor."),
(24,5,[M,D,T],0,0,0,1,"'Kumla kumla kumla' ve 'burun ve bir burnu' bozuk tekrarlar."),
(32,1,[M,D,Y],0,0,0,3,"Konuşan yağmur damlaları, kopuk olaylar ve bozuk son cümle."),
(40,2,[K,M,D],0,0,0,2,"Elsa'dan ayrı bir 'Kraliçe' ve 'kızak bir kraliçeydi' karmaşası."),
(48,3,[K,M,D],1,0,1,1,"'Maşa tepede Maşa ile oynuyordu' karakter karışıklığı."),
(56,4,[M,D],0,0,0,2,"Kızın kiminle kavga ettiği belirsiz, son cümle anlamsız."),
(64,3,[M,D,T,Y],1,0,1,1,"Sesin ne olduğu hiç söylenmeden 'buldu' deniyor."),
(72,3,[M,D],0,0,0,2,"'tek başınalarıma' gibi uydurma ifadeler ve anlamsız kar tanesi olayları."),
(80,1,[K,M,D],0,0,0,3,"Maşa 'Daşa' oluyor, olaylar tamamen anlamsız."),
(88,3,[K,M,D],0,0,0,1,"Elsa'dan ayrı Kraliçe/prenses karmaşası, 'ses bir kraliçeydi'."),
(96,5,[K,D,T],0,0,0,0,"Hayri kendi sorusuna kendi cevap veriyor, 'Hayri, Hayri ile'."),
(104,5,[M,D,T],1,1,1,1,"Yıkılan kalenin kule 'yapması' ve 'evde kalmamış' bozuk anlatım."),
(112,4,[M,D],1,0,1,2,"'Bu kez uçak hiç uçmadı' çelişkisi ve bozuk uçak cümleleri."),
(120,5,[M,D],1,1,1,1,"Ryder treni alıp geri veriyor, 'kulemeleri' uydurma kelime."),
(128,3,[K,M,D],0,0,0,2,"Kız birden 'kadın' oluyor, çuval cümlesi anlamsız."),
(136,1,[M,D,U],0,0,0,3,"Şarap içeriği, 'damlaet', 'Solap' uydurma kelimeler."),
(144,1,[K,M,D],0,0,0,3,"Şakir kendi kendine şemsiye/şapka veriyor, son cümle bozuk."),
(152,6,[M,D,T],0,0,0,1,"Papatya'nın üzüntüsü unutuluyor, çiçeğin kime ait olduğu karışık."),
(160,7,[D,T],0,0,0,0,"Sorun yok, 'oynamalarına yardım etti' bozuk cümle."),
(168,3,[M,D],1,0,1,2,"'küçük bir çiçeğin sapını çiçeğe uzattı' gibi anlamsız çiçek olayları."),
(176,1,[K,M,D],0,0,0,3,"Hayri kendi kendine konuşuyor, salıncak/turta karmaşası."),
(184,2,[M,D,T],0,0,0,2,"'Kağıt kağıda resim çizdi', 'Necad' uydurma."),
(192,3,[M,D],0,0,0,2,"Kumdaki suyu içme ve 'mor su şapka taktı' anlamsızlığı."),
(200,8,[D],0,0,0,0,"Küçük dil pürüzü; belirgin sorun yok ama akıcı."),
(208,2,[K,M,D],1,0,0,2,"Uçak birden kuşa dönüşüyor, teşekkür edenin kim olduğu belirsiz."),
(216,2,[M,D,T],0,0,0,2,"'Dal dalın hiç düşmedi' gibi anlamsız dal tekrarları."),
(224,3,[M,D,Y],0,0,0,3,"Başlamamış yağmurun dinmesi, kopuk son."),
(232,4,[M,D,T],1,0,1,1,"'kağıt basan/basaması' uydurma ve 'kağıt ikiye katmıştı' sonu."),
(240,1,[F,K,D],0,0,0,0,"Elsa kayboluyor, 'Ryfel/Ryftan' uydurma isimler."),
(248,2,[M,D,Y],0,0,0,2,"Olaylar kopuk, son sorunla ilgisiz."),
(256,2,[K,M,D],0,0,0,1,"Basri Amca 'Kamil Amca' oluyor, 'bana verdi' bozuk."),
(264,4,[M,D],1,0,0,2,"Anlamsız 'Dur, kirpi' ve birden çıkan arkadaş."),
(272,2,[M,D,T],0,0,0,3,"Su damlası olayları tamamen anlamsız, Kadriye birden çıkıyor."),
(280,5,[M,D],0,0,0,1,"'bir sürü küçük kızın en sevdiği şarkı' gibi bozuk cümleler."),
(288,1,[K,M,D],0,0,0,3,"Pepee kendisiyle konuşuyor, 'Pepee ile Pepee'."),
(296,3,[M,D,T],1,0,0,2,"Kekik kaybı 'tırmanmayı öğrendim' ile bitiyor."),
(304,1,[K,M,D],0,0,0,2,"Şakir şapkayı Şakir'e veriyor, 'Şapkayım' bozuk."),
(312,5,[M,D],1,0,0,2,"Şapkayı ağaca asma çözümü anlamsız, 'kalbi özenli görünüyordu'."),
]
order=["figur_yanlis","karakter_karisik","mantiksiz","bozuk_dil","ozellik_celiski","tekrar","yarim_son","uygunsuz"]
p=json.load(open('parti_1.json'))
assert [x['id'] for x in p]==[r[0] for r in R],([x['id'] for x in p])
out=[]
for i,pu,k,s1,s2,s3,m,n in R:
    k=set(k)
    if m>0:k.add(M)
    else:k.discard(M)
    out.append({"id":i,"puan":pu,"kategoriler":[c for c in order if c in k],"s1":bool(s1),"s2":bool(s1 and s2),"s3":bool(s1 and s3),"mantiksiz":m,"not":n})
json.dump(out,open('puan_1.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(o['puan'] for o in out)/len(out))
