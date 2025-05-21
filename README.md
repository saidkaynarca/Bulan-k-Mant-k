**TARIM DESTEK KARAR DESTEK SİSTEMİ - PROJE RAPORU**

---
### Hazırlayan

Said Kaynarca 21430070044

(Sistemi çalıştırmak için 12. adıma bakmanız yeterli olacaktır)
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
11. Kod ve Uygulama Görselleri
12. Kurulum ve Çalıştırma Talimatları
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
### 11. Kod ve Uygulama Görselleri


![1-kod-dosya-boş](https://github.com/user-attachments/assets/ee24c2fa-6c53-4c6d-ace0-43d3f914b29a)
![2-kod-dosya-tarım-pencere](https://github.com/user-attachments/assets/918328ef-b4b4-47ba-ba65-f101657301b7)
![3-kod-dosya-tarımpencere-grafşk](https://github.com/user-attachments/assets/8c78207d-8812-4885-a7a2-d49e04c92c14)
![4-kod-dosya-tarımpencere-pdf](https://github.com/user-attachments/assets/7046f6fc-adda-436f-9a18-ba7b28c7c85a)
![5-kod-dosya-pdf](https://github.com/user-attachments/assets/65d37ee4-fe4c-4716-b1be-09be48ab6d8a)

---
### 12. Kurulum ve Çalıştırma Talimatları
Bu proje Python diliyle geliştirilmiştir. Uygulamayı çalıştırmak isteyen bir kullanıcı aşağıdaki adımları takip etmelidir:
Gerekli Yazılım
- Python 3.8 veya üzeri bir sürüm
- pip (Python paket yöneticisi)

*Gerekli Kütüphaneler
Terminal (Komut İstemi veya VS Code Terminali) üzerinden aşağıdaki komutu çalıştırarak gerekli kütüphaneler yüklenmelidir:

![Screenshot_6](https://github.com/user-attachments/assets/c46db54a-dda5-4c3d-ba27-e67abe63454c)

Not: tkinter modülü Python ile birlikte gelir, ek bir kurulum gerektirmez.

Uygulamanın Çalıştırılması
Kod dosyasını (örneğin tarim_destek_sistemi.py) çalıştırmak için terminale şu komutu yazın:

![Screenshot_7](https://github.com/user-attachments/assets/b74ae94f-8595-4bd9-9065-fa696ad70fe8)

Uygulama Özellikleri
- Kullanıcı, 0–10 arasında değerler girerek 5 çevresel faktörü tanımlar.

- “HESAPLA” butonuna basıldığında sistem:

  - Sulama süresi, gübre miktarı ve toprağın kontrol ihtiyacını hesaplar.

  - Sonuçları grafik olarak gösterir.

  - Masaüstüne otomatik olarak PDF çıktısı kaydeder.


---
**Hazırlayan:** \ Said Kaynarca 21430070044
**Bölüm:** Mersin Üniversitesi - Bilişim Sistemleri ve Teknolojileri
**Ders:** Bulanık Mantık
**Yıl:** 2025
