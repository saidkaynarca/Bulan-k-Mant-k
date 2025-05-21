**TARIM DESTEK KARAR DESTEK SİSTEMİ - PROJE RAPORU**

---

### İçindekiler

1. Giriş
2. Proje Amacı
3. Kullanılan Teknolojiler
4. Sistem Girdileri ve Çıktıları
5. Arayüz Tanıtımı
6. Hesaplama Mantığı (Bulanık Mantık Yaklaşımı)
7. PDF Raporlama Özelliği
8. Grafiksel Gösterim
9. Kullanım Talimatları
10. Sonuç ve Katkılar

---

### 1. Giriş

Bu proje, tarımsal alanlarda çiftçilere ve tarım uzmanlarına destek olabilmek için geliştirilmiştir. "Tarım Destek Karar Destek Sistemi" adlı bu uygulama, kullanıcıdan alınan 5 temel tarımsal parametreye göre sulama süreleri, gübre miktarları ve toprağın kontrol ihtiyacı gibi önerilerde bulunur.

---

### 2. Proje Amacı

Projenin temel amacı, tarımda verimliliği arttırmak ve doğru girdi kullanımını teşvik etmektir. Bu sistem ile çiftçiler, mevcut alanları için ne kadar sulama, gübreleme veya toprak kontrolü yapmaları gerektiği konusunda bilgi sahibi olur.

---

### 3. Kullanılan Teknolojiler

* Python 3
* Tkinter (Görsel arayüz)
* Matplotlib (Grafiksel gösterim)
* FPDF (PDF rapor oluşturma)
* Bulanık Mantık Yaklaşımı (manuel hesaplama modeli)

---

### 4. Sistem Girdileri ve Çıktıları

#### Girdiler (Kullanıcıdan alınır):

1. Toprak Nemi (0-10)
2. Sıcaklık (0-10)
3. Güneş Işığı (0-10)
4. Rüzgar (0-10)
5. Ürün Türü (0-10)

#### Çıktılar:

* **Sulama Süre Oranı** (% olarak)
* **Gübre Miktar Oranı** (% olarak)
* **Toprağın Kontrol İhtiyacı** (% olarak)

---

### 5. Arayüz Tanıtımı

Program şık ve sade bir arayüze sahiptir. Arka plan renkleri, Apple stilinden esinlenilerek seçilmiştir. Giriş kutuları sarımsı-krem tonlarında, butonlar yeşil tonundadır. Giriş kutularına rakam girerken Tab ya da Enter tuşları ile bir alt alana geçilebilir.

---

### 6. Hesaplama Mantığı (Bulanık Mantık Yaklaşımı)

Girdi olarak alınan parametreler, belirli katsayılarla çarpılır ve normalize edilerek yüzdelik dağılıma dönüştürülür. Bu şekilde 3 çıktı arasında toplam %100 olacak şekilde oransal dağılım sağlanır.

---

### 7. PDF Raporlama Özelliği

Her hesaplamadan sonra, kullanıcının masaüstüne otomatik olarak bir PDF dosyası oluşturulur. Bu dosyada girilen veriler ve hesaplanan çıktılar metin olarak sunulur. İçerikte Türkçe karakter desteği mevcuttur.

---

### 8. Grafiksel Gösterim

Sonuçlar ayrı bir pencerede pasta grafiği şeklinde gösterilir. Grafik 3 çıktıyı renklendirerek sunar: "Sulama Süre Oranı", "Gübre Miktar Oranı" ve "Toprağın Kontrol İhtiyacı". Grafik penceresi kapandığında uygulama hata vermemektedir.

---

### 9. Kullanım Talimatları

1. Program açıldığında 5 adet giriş kutusu görülecektir.
2. Her kutuya 0 ile 10 arasında sayı girilmelidir.
3. Enter veya Tab tuşuyla bir sonraki alana geçebilirsiniz.
4. Tüm alanlar doğru doldurulduktan sonra "HESAPLA" butonuna basın.
5. Sonuçlar aşağıdaki etikette yazılı ve grafik penceresinde görülecektir.
6. PDF masaüstüne otomatik kaydedilecektir.

---

### 10. Sonuç ve Katkılar

Bu proje, çiftçilerin tarımsal kararlarını desteklemek için pratik ve görsel bir aracı sunar. Kullanıcı dostu arayüzü, grafiksel gösterimi ve otomatik raporlama sistemi ile sahada kullanılabilirliği yüksektir.

---

**Hazırlayan:** \[Senin Adın]
**Bölüm:** Mersin Üniversitesi - Bilişim Sistemleri ve Teknolojileri
**Ders:** Bulanık Mantık
**Yıl:** 2025
**TARIM DESTEK KARAR DESTEK SİSTEMİ - PROJE RAPORU**

---

### İçindekiler

1. Giriş
2. Proje Amacı
3. Kullanılan Teknolojiler
4. Sistem Girdileri ve Çıktıları
5. Arayüz Tanıtımı
6. Hesaplama Mantığı (Bulanık Mantık Yaklaşımı)
7. PDF Raporlama Özelliği
8. Grafiksel Gösterim
9. Kullanım Talimatları
10. Sonuç ve Katkılar

---

### 1. Giriş

Bu proje, tarımsal alanlarda çiftçilere ve tarım uzmanlarına destek olabilmek için geliştirilmiştir. "Tarım Destek Karar Destek Sistemi" adlı bu uygulama, kullanıcıdan alınan 5 temel tarımsal parametreye göre sulama süreleri, gübre miktarları ve toprağın kontrol ihtiyacı gibi önerilerde bulunur.

---

### 2. Proje Amacı

Projenin temel amacı, tarımda verimliliği arttırmak ve doğru girdi kullanımını teşvik etmektir. Bu sistem ile çiftçiler, mevcut alanları için ne kadar sulama, gübreleme veya toprak kontrolü yapmaları gerektiği konusunda bilgi sahibi olur.

---

### 3. Kullanılan Teknolojiler

* Python 3
* Tkinter (Görsel arayüz)
* Matplotlib (Grafiksel gösterim)
* FPDF (PDF rapor oluşturma)
* Bulanık Mantık Yaklaşımı (manuel hesaplama modeli)

---

### 4. Sistem Girdileri ve Çıktıları

#### Girdiler (Kullanıcıdan alınır):

1. Toprak Nemi (0-10)
2. Sıcaklık (0-10)
3. Güneş Işığı (0-10)
4. Rüzgar (0-10)
5. Ürün Türü (0-10)

#### Çıktılar:

* **Sulama Süre Oranı** (% olarak)
* **Gübre Miktar Oranı** (% olarak)
* **Toprağın Kontrol İhtiyacı** (% olarak)

---

### 5. Arayüz Tanıtımı

Program şık ve sade bir arayüze sahiptir. Arka plan renkleri, Apple stilinden esinlenilerek seçilmiştir. Giriş kutuları sarımsı-krem tonlarında, butonlar yeşil tonundadır. Giriş kutularına rakam girerken Tab ya da Enter tuşları ile bir alt alana geçilebilir.

---

### 6. Hesaplama Mantığı (Bulanık Mantık Yaklaşımı)

Girdi olarak alınan parametreler, belirli katsayılarla çarpılır ve normalize edilerek yüzdelik dağılıma dönüştürülür. Bu şekilde 3 çıktı arasında toplam %100 olacak şekilde oransal dağılım sağlanır.

---

### 7. PDF Raporlama Özelliği

Her hesaplamadan sonra, kullanıcının masaüstüne otomatik olarak bir PDF dosyası oluşturulur. Bu dosyada girilen veriler ve hesaplanan çıktılar metin olarak sunulur. İçerikte Türkçe karakter desteği mevcuttur.

---

### 8. Grafiksel Gösterim

Sonuçlar ayrı bir pencerede pasta grafiği şeklinde gösterilir. Grafik 3 çıktıyı renklendirerek sunar: "Sulama Süre Oranı", "Gübre Miktar Oranı" ve "Toprağın Kontrol İhtiyacı". Grafik penceresi kapandığında uygulama hata vermemektedir.

---

### 9. Kullanım Talimatları

1. Program açıldığında 5 adet giriş kutusu görülecektir.
2. Her kutuya 0 ile 10 arasında sayı girilmelidir.
3. Enter veya Tab tuşuyla bir sonraki alana geçebilirsiniz.
4. Tüm alanlar doğru doldurulduktan sonra "HESAPLA" butonuna basın.
5. Sonuçlar aşağıdaki etikette yazılı ve grafik penceresinde görülecektir.
6. PDF masaüstüne otomatik kaydedilecektir.

---

### 10. Sonuç ve Katkılar

Bu proje, çiftçilerin tarımsal kararlarını desteklemek için pratik ve görsel bir aracı sunar. Kullanıcı dostu arayüzü, grafiksel gösterimi ve otomatik raporlama sistemi ile sahada kullanılabilirliği yüksektir.

---

**Hazırlayan:** \[Senin Adın]
**Bölüm:** Mersin Üniversitesi - Bilişim Sistemleri ve Teknolojileri
**Ders:** Bulanık Mantık
**Yıl:** 2025
