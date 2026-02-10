# 🚜 The Farmer Was Replaced: Algorithmic Farming Journey

Bu repo, **The Farmer Was Replaced** oyununda karşılaştığım problemleri yazılım mantığıyla nasıl çözdüğümü, algoritmik düşünme becerilerimi nasıl geliştirdiğimi ve 
otomasyon süreçlerimi belgelemek amacıyla oluşturulmuştur.

Bir **Yönetim Bilişim Sistemleri (YBS)** öğrencisi olarak hedefim, oyunun sunduğu Python benzeri kod sistemini kullanarak "maksimum hasat ve minimum satır kod" prensibiyle ilerlemek.

## 🎮 Oyun Mantığı
- Oyundaki amacımız bir drone ile tarlamızda ekin ekip hasat yapmak. Hasatlarımız kaynaklarımıza ekleniyor ve bazı bitkileri ekebilmek için diğer kaynaklarımızdan bazıları harcanıyor.
Drone tamamen yazdığımız kodlar dahilinde harekete geçiyor. Ancak her komutu istediğimiz gibi kullanamıyoruz.Oyun belli aşamalardan oluşmakta ve Her aşamada yapılanlar kendinden önceki
aşamalardaki teknikleri birleştirip kullanarak yeni aşamaları açmanızı sağlayan bir yapıda ilerliyor. Yaptığımız hasatlar ile yeni aşamaların kilidi açılabiliyoruz. Örneğin bir önceki aşamada
oyunun **"Entities.Bush"** isimli bitkisini sadece bu isimle kullanabiliyorken hasatlarımızı kullanarak açtığımız **"değişken atama"** aşaması sayesinde adını farklı bir değişkene atayarak
**(örneğin: "Entities.Bush = cali")** yazdığımız kodlarda kullanabiliyoruz. Başlangıçta sadece çimen hasat edebiliyorken açabildiğimiz aşamalar sayesinde farklı ekinlerinde kildini açabiliyoruz.
ilk ekinlerin kuralları basit ancak ilerleyen süreçte açılabilen ekinlerin daha hızlı büyümesi için belli şartların karşılanması gerekiyor. Örneğin **ağaç (tree)** bitkisinin alt, üst, sağ veya sol
karesinde bir ağaç daha ekilmişse büyüme hızı 2 kat yavaşlıyor. Bu sebeple ağaç ekimi yapacaksak tarlanın bu şartlarına uygun noktalarına ekim yapmamız gerekiyor. Bu gibi birçok problem çözme
kabiliyetini geliştirme odaklı aşamalardan oluşuyor.

## 🚀 Proje Amacı
- Python benzeri bir dil ile temel programlama mantığını (döngüler, koşullar) pekiştirmek.
- İş süreçlerini (farming) otomatize ederek verimlilik analizi yapmak.
- Karmaşıklaşan oyun mekaniklerinde sürdürülebilir kod yazmayı öğrenmek.
- Kodlarımdaki hatalı ve eksik kısımları daha hızlı görmek, algılamak ve hızlıca ayıklama yapabilmek.

## 🧠 Neler Öğreniyorum?
Bu süreçte sadece oyun oynamıyor, aynı zamanda bazı teknik yeteneklerimi geliştiriyorum:
- **Kontrol Yapıları:** Hangi durumlarda hangi eylemin yapılacağının karar mekanizmasını kurmak.
- **Kaynak Yönetimi:** Sınırlı işgücü ve kaynağı en doğru şekilde yönetmek.
- **Hata Ayıklama (Debugging):** Drone yanlış yere gittiğinde veya kodun planladığım şekilde çalışmadığı gibi durumlarda koddaki mantık hatasını bulmak.

## 📜 Gelişim Günlüğü (DevLog)
Bu kısımda oyundaki ilerleme ve gelişmelerimi tarihleriyle yazarak neler yaptığımın kaydını tutacağım.

###🗓️ 10.02.2026 
-----------------
**##📈 Seviye: Ağaç (Tree)**
-  **Ağaç (Tree)** bitkisinin kilidini açtım. Bu bitkinin çalıdan farkı daha fazla odun hasat edilebilmesi. Ancak bu bitkinin en dikkat edilmesi gereken özelliği, üst, alt, sol veya sağ tarafında bir ağaç
bulunursa 2x daha yavaş yetişmesi. Yani eğer ağaç ekmek istiyorsam ve minimum sürede olgunlaşmasını istiyorsam çevresindeki 1x1'lik alana ağaç ekmemeliyim.
- Çapraz bir ekim yapabilmek adına drone bulunduğu sütunun sıra sayısını kontrol edecek ve sütun sırası çift sayı ise olgunlaşma durumunu kontrol edecek ve hasat edilebilir ise hasat edecek, ardından bulunduğu yatay sıra sayısı çift ise ağaç dikecek, değil ise çalı ekecek. ve yukarı yönde hareket edecek. Sütun sıra sayısı tek ise ekim sırasını tam tersi olarak yapacak. Eğer bulunduğu sütunda hasat edilebilir birşey yoksa sağ yönde hareket edecek. Bu sayede tarla boyunca kontrol sağlayıp ekin ekip en erken sürede olgunlaşmalarını sağlayıp hasat gerçekleştirebileceğim.
- Kodumun fazla uzun, kontrol gerektiren ve karmaşık bir hal almaya başladığını farkettiğim için **def** komutunun kilidini açtım ve artık olgunlaşma durumuna göre hasat etmesi yada hiçbirşey yapmaması
için **olgunsatopla** ismini verdiğim bir fonksiyon oluşturdum.
- Tüm tarla boyunca bulunduğu konuma göre drone için sabit bir rota oluşturmak beni biraz zorladı ancak işin sonunda drone için sütunu boydan boya kontrol edip durumuna ve konumuna göre hasat edip etmemesi aynı zamanda ilerleyeceği yer yönü belirleyebileceği dinamik bir karar mekanizması oluşturdum. Bu sayede drone, sadece tarlayı gezmekle kalmıyor, her hücrede veriyi analiz ederek (olgunluk, sütun sırası vb.) operasyonel önceliklerini kendi belirliyor."
- Yazmış olduğum kodda her koordinat için bir if-else döngüsü olduğunu ve bunun da kodumun karmaşık bir yapıda görünmesine sebep olduğunu farkettim. Bu sebeple her sütun ve satır için hesaplama yapmak yerine neden 2 koordinat bilgisini tek seferde alarak hesaplama yapmıyorum diye düşündüm ve bir nevi dama tahtası düzenini bir matematiksel model oluşturarak bu kontrolü tek bir fonksiyona indirgedim.
Bu sayede kod satır sayım ciddi bir oranda kısalırken, sadece 6x6'lık bir modelde çalışan kodum artık daha dinamik bir yapıda ve bütün uzunluklar için kullanılabilir hale geldi.

  # 📃 Kod : src/01_grass_automation.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**##📈 Seviye: Balkabağı (Pumpkin)**
- **Balkabağı (Pumpkin)** kilidini açtım. Bu bitkinin özelliği ise 1x1 menzilindeki diğer balkabakları ile birleşerek daha büyük ve değerli bir balkabağına dönüşebilmesi. Ancak balkabakları bazen ölü yetişebiliyor ve ölü yetişen balkabakları diğerleri ile birleşemiyor, hasat edildiğinde kaynaklarımıza eklenmiyor. Bu mekanik, algoritmamı sadece tek bir hücreyi yönetmekten çıkarıp, tüm tarlayı
bir bütün olarak gören bir 'Alan Optimizasyonu' mantığına taşıdı. Tüm balkabaklarının senkronize bir şekilde büyümesini sağlamak ve ölü bitkilerin en erken sürede arındırılması için zamanlama ve kaynak yönetimini en ince ayrıntısına kadar planladığım bir sistem geliştirmeye çalışacağım.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###🗓️ 09.02.2026 
----------------- 
  **📈 Seviye: Çimen (Grass)**
- Oyuna başladım ve şuanda tek bir karelik bir çimen üzerindeyim. **harvest()** komutunu tekrar tekrar çalıştırarak çimen hasat ediyorum.
- 5 çimen hasadım karşılığında **While** aşamasının kilidini açtım. **While True:** komutu kullanarak tekrar tekrar kod çalıştırmama gerek kalmadan sonsuz döngü ile tek kare üzerinde hasat yapıyorum.
- Drone artık açtığım aşama sebebiyle daha hızlı ve çimeni daha olgunlaşmadan hasat ediyor ancak olgunlaşmamış bir bitki hasat edilirse kaynaklarımıza eklenmiyor. Bu sebeple yeni aşama ile birlikte
açılan **can_harvest()** isimli **boolean** değeri döndüren kontrolcüyü kullanarak drone'un sonuca göre hasat gerçekleştirmesi üzere kodlayacağım.
- Sonsuz döngüme bu değer için olgunlaşma kontrolcüsünü ekledim ve artık drone sadece altındaki ekin olgunlaşmışsa hasat edecek şekilde programlandı.

  # 📃 Kod : src/4_tree_and_wood.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  **##📈 Seviye: Çalı (Bush)**
- Tarlamın boyutunu üst üste 3 kare olacak şekilde uzattım ve drone ile hareket etmemi sağlayan **move("Yön")** komutunun kilidini açtım.
- Aynı zamanda **Çalı(Bush)** kilidin açtım. Çimene göre daha yavaş yetişiyor, hasattan sonra tekrar ekmem gerekiyor ve kaynaklarıma odun ekliyor. Bu bitki hasadı için **can_harvest()** komutunu
kullanmaya devam edeceğim. 3 karelik alanda da ekim yapıp hasat etmem için ise **move("Yön")** komutunu kullanacağım.
- Açtığım yeni aşama sayesinde tarlam 3x3 karelik bir alanım olacak şekilde genişledi. Artık sadece yukarı yada aşağı yönde değil, sağ ve sol yönleri de kullanarak drone yönlendirmesi yapmam gerekiyor.
Bunun için ise kullandığım yöntem şu: Eğer drone altındaki ekin olgunlaşmışsa hasat ediyor, tekrar çalı ekiyor ve yukarı yönde hareket ediyor. Bu sayede altındaki ekin yetişirken bi üstteki ekinin
durumunu kontrol edip ilerleyeceğim yönü beklirlememe yardımcı oluyor. Çünkü eğer üstteki ekin daha olgunlaşmamışsa bir sağ yönde hareket ediyor ve aynı hareketi burda da uyguluyor. Bu sayede dik bir
hiza halindeki 3 ekin yetişme sürecindeyken diğer 2x3'lük kısımdaki ekinlerin olgunlaşma durumunu en erken zamanda kontrol edebiliyorum ve olgunlaşmış olması halinde hemen hasat ediyorum.
Bu süreçte bir yandan arkamda kalan ekinler olgunlaşana kadar diğer ekinleri hasat ediyorum ve en sağdaki sütuna geldiğimde drone hemen ilk hasat edilip yenisi ekilen ekinin üzerine gidip onu
hasat ediyor.
- Ancak drone biraz yavaş kaldığı için ben 3. sütuna geçtiğimde 1. sütundaki ekinler olgunlaşmış oluyor bu yüzden drone hızlandırma aşamasını açmalıyım.

  # 📃 Kod : src/02_bush_and_wood.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  **##📈 Seviye: Havuç (Carrot)**
- **Havuç (Carrot)** bitkisinin kilidini açtım ve bu bitkinin öncekilerden farkı daha geç olgunlaşması ve sadece toprak üzerine ekilebilmesi. Yani bu bitkiyi ekebilmem için güncel olarak tarlamın zemini
olan **çimen (grass)** zeminini **toprak (soil)** olarak değiştirmeliyim. Bunun için ise drone'u tarlanın her bir karesinde gezdireceğim ve altındaki kareyi kontrol etmek için bu aşamanın kilidini açtığı
**get_ground_type()** komutunu kullanarak drone altındaki zeminin hangi tür olduğu bilgisini aldıracak ve eğer zemin **çimen** ise yine aşama ile birlikte gelen **till()** komutunu kullanarak
toprağa çevirtecek, ardından **havuç** ektireceğim. Eğer zemin şartları karşılıyorsa sadece olgunluk durumu kontrol edilecek, olgunlaştıysa hasat edilecek ve yerine tekrar **havuç** ekecek.

  # 📃 Kod : src/03_carrot.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
