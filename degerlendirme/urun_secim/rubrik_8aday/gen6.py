import json
M="mantiksiz";B="bozuk_dil";K="karakter_karisik";T="tekrar";Y="yarim_son";F="figur_yanlis";O="ozellik_celiski"
R=[
(5,1,[K,M,B,T],1,0,0,3,"Uydurma kelimeler (Sospik, Simanda) ve kopuk koku olayi; Skye one geciyor."),
(13,4,[M,B],1,0,1,2,"Kagit secip balonun inmesi ve 'sapka bir balon gibiydi' sebepsiz."),
(21,1,[K,M,B],1,0,0,2,"Elsa kendisi kralice iken ayri bir kralice var; yemek kaleye donusuyor."),
(29,3,[M,B,T],1,0,1,2,"Kagit tekrarlari ve anlamsiz katlama cozumu."),
(37,5,[M,B],1,1,0,2,"Elmayi agaca uzatmak ve aniden turta mantiksiz."),
(45,2,[K,M,B],0,0,0,1,"Canan/Kadriye karisikligi ve bozuk cumleler."),
(53,4,[M,B],1,0,1,3,"Kizak kumsalda el salliyor, disle tasiniyor."),
(61,2,[M,B,T],1,0,1,3,"Kum tekrarlari ve anlamsiz cumleler (Kospu, kumbara)."),
(69,5,[M,B],1,0,1,2,"Salincak konusuyor, ucaga yiyecek veriliyor."),
(77,1,[K,M,B],1,0,0,3,"Anne/kardes karisikligi; Hello Kitty 'anneciğim' diye tesekkur ediyor."),
(85,2,[M,B,Y],0,0,0,2,"Sorun yok, salincak kaleye donusuyor; Denee uydurma."),
(93,4,[M,B],1,1,1,2,"Kumdan kagit ucak, kupa, havlu atma tutarsiz."),
(101,1,[K,M,B,T],0,0,0,3,"Elsa kendine konusuyor; kum tekrarlari anlamsiz."),
(109,2,[K,M,B],1,1,0,3,"Kirpi aniden cikiyor; yagmur sepeti alip ortu seriyor."),
(117,3,[K,M,B],1,1,1,1,"Chase veriyor ama Ryder 'al bu senin' diyor; kiz/kizak karisik."),
(125,4,[M,B],1,0,1,2,"Kavanoz/recel olayi anlamsiz; 'acmuştu' bozuk."),
(133,2,[K,M,B,T],1,1,1,2,"Niloya kendine seslenip kabul ediyor; kar/kart karisik."),
(141,1,[K,M,B],0,0,0,2,"'Tesekkurler Doru' dedi Doru; agac altinda elma agaci."),
(149,5,[M,B],0,0,0,2,"Dal kirilinca ciceklerin kurtulmasi ve ilgisiz izin dersi."),
(157,4,[M,B],0,0,0,2,"Cicek kagida donusuyor, anne kagidi yiyor."),
(165,4,[M,B],1,0,1,3,"Kagit sallanmadi/sallandi celiskisi."),
(173,5,[M,B],1,1,1,2,"Niloya ruzgarin kirdigi direk icin ozur diliyor; dal basa takiliyor."),
(181,4,[M,B],1,0,0,2,"Kagit cicek aciyor, toprak kazarken ikiye bolme anlamsiz."),
(189,1,[K,M,B],1,1,0,3,"Kimle konustugu belirsiz; 'sapkasini sapkasiyla tuttu' saçma."),
(197,3,[M,B],1,0,1,3,"'Hic yumusadi ve yumusadi' gibi celiskiler, sarayda Keloglan."),
(205,1,[K,M,B],1,1,1,3,"Simsekler/Sila uydurma karakterler, olay anlasilmiyor."),
(213,1,[K,M,B],1,0,1,2,"Elsa kendine soru soruyor; buz sarayina binmek mantiksiz."),
(221,3,[M,B],1,0,1,2,"Kabuktan cicek cikiyor; 'Cileklerim' anlamsiz."),
(229,3,[M,B],1,1,1,2,"Dagda gemi, ruzgar gemi yapiyor; Tonca/Satay uydurma."),
(237,5,[M,B],1,0,0,2,"Ruzgar havluyu alip geri veriyor; son ilgisiz arkadaslik."),
(245,3,[M,B,T],0,0,0,2,"Agac konusuyor, kagit iki kez kardese veriliyor."),
(253,5,[M,B],0,0,0,1,"'Sut ve sut', 'Sostu' ve anlamsiz izin sonu."),
(261,2,[M,B,T],0,0,0,2,"Kagit/cicek olayi anlamsiz, son cumle bozuk."),
(269,4,[M,B,T],0,0,0,2,"Sandik bos sonra balon dolu; olay tekrar baslıyor."),
(277,1,[F,K,M,B],0,0,0,3,"Alastik/Alap uydurma isimleri hikayeyi ele geciriyor, Hayri kayboluyor."),
(285,3,[M,B,T],1,1,1,2,"Havlu tekrarlari ve siseden havlu cikmasi."),
(293,5,[M,B,Y],1,0,1,1,"Sorun cozulmeden bitiyor; 'kitabi' ilgisiz."),
(301,4,[M,B],1,1,1,2,"'Top topu delige sokmustu', sapkayla delik kapatma anlamsiz."),
(309,4,[M,B],1,0,0,3,"Chase havluya tirmaniyor, kale uzaga gidiyor."),
]
p=json.load(open('/tmp/claude-0/-home-user-hikaye-oyuncak/51a50a87-4e4c-59c8-8b0c-5316b89b1551/scratchpad/deney4/rubrik/parti_6.json'))
assert [x['id'] for x in p]==[r[0] for r in R]
out=[{"id":i,"puan":s,"kategoriler":c,"s1":bool(a),"s2":bool(b),"s3":bool(d),"mantiksiz":m,"not":n} for i,s,c,a,b,d,m,n in R]
json.dump(out,open('/tmp/claude-0/-home-user-hikaye-oyuncak/51a50a87-4e4c-59c8-8b0c-5316b89b1551/scratchpad/deney4/rubrik/puan_6.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(r[1] for r in R)/len(R))
