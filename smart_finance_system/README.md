# 💰 Smart Expense & Notification Management System

Bu proje, Python kullanılarak geliştirilmiş **mini bir finans yönetim sistemidir**.  
Kullanıcının harcamalarını alır, bütçe analizi yapar ve limit aşımı durumunda **bildirim sistemi** çalıştırır.

Proje, Python temelleri ile birlikte **OOP, modüler yapı ve polymorphism** kavramlarını pekiştirmek amacıyla geliştirilmiştir.

---

## 🚀 Özellikler

- Kullanıcıdan sınırsız sayıda harcama alma
- Harcamaları nesne (Expense) olarak yönetme
- Toplam ve ortalama harcama hesaplama
- En büyük / en küçük harcama analizi
- Set kullanarak kategori analizi
- Bütçe limiti kontrolü
- Limit aşımında Email & SMS bildirimi (Polymorphism)
- Modüler dosya yapısı

---

## 🧠 Kullanılan Konular

### 🔹 Python Temelleri
- Değişkenler
- String işlemleri
- Tip dönüşümleri

### 🔹 Koleksiyonlar
- List
- Set
- Dict
- Bool

### 🔹 Kontrol Yapıları
- if / else
- for
- while
- break / continue
- try / except

### 🔹 Fonksiyonlar
- Parametreli fonksiyonlar
- Input / output
- Hata yönetimi

### 🔹 OOP (Object Oriented Programming)
- Class & Object
- Inheritance
- Polymorphism
- `__str__` metodu
- Encapsulation (temel seviye)

### 🔹 Modüler Yapı
- `.py` dosyaları
- Import sistemi
- `datetime` ve `random` kütüphaneleri

---

## 📁 Proje Yapısı

```text
smart_finance_system/
│
├── models.py          # Expense ve Budget sınıfları
├── notifications.py  # Notification, Email, SMS sınıfları
├── utils.py           # Yardımcı fonksiyonlar
└── main.ipynb         # Uygulamanın çalıştığı notebook
