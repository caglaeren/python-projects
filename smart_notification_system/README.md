# 🔔 Smart Notification System (v6 – Advanced OOP)

Bu proje, Python'da Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak geliştirilmiş modüler bir bildirim yönetim sistemidir. Proje kapsamında farklı kanallar (Email, SMS, Push) üzerinden bildirim gönderimi simüle edilmiştir.

## 🚀 Kullanılan Teknik Özellikler

* **Polymorphism (Çok Biçimlilik):** Tüm bildirim sınıfları `send()` metodunu ortak bir arayüz olarak kullanır ancak her biri farklı çıktı üretir.
* **Kalıtım (Inheritance):** `Notification` ana sınıfından türetilen alt sınıflar ile kod tekrarı önlenmiştir.
* **Dunder (Özel) Metotlar:** `__str__` ve `__len__` metotları kullanılarak nesne davranışları özelleştirilmiştir.
* **Hata Yönetimi (Error Handling):** `try-except-else-finally` blokları ile boş mesaj veya beklenmedik çalışma anı hataları kontrol altına alınmıştır.
* **Modüler Yapı:** Proje mantığı `notifications.py` ve `utils.py` modüllerine ayrılmış, testler `main.ipynb` üzerinden yürütülmüştür.

## 📂 Dosya Yapısı

- `notifications.py`: Bildirim sınıflarının (Base ve Sub-classes) bulunduğu modül.
- `utils.py`: Rastgele mesaj üretimi ve zaman damgası gibi yardımcı fonksiyonlar.
- `main.ipynb`: Sistemin test edildiği ve polymorphism kanıtlarının sunulduğu Jupyter Notebook.

## 🛠️ Nasıl Çalıştırılır?

1. Bu repoyu bilgisayarınıza indirin.
2. `main.ipynb` dosyasını Jupyter Notebook veya VS Code üzerinden açın.
3. Hücreleri sırasıyla çalıştırarak bildirimlerin nasıl yönetildiğini gözlemleyin.
