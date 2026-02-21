from datetime import datetime ## Tarih ve saat bilgisini almak için standart kütüphaneyi içeri aktarıyoruz.

class Notification():
    """Base Class: Tüm bildirim türleri için temel yapı."""
    def __init__(self, message):
        # Nesne oluşturulduğunda çalışan yapıcı metot (Constructor).
        self.message = message
        self.created_at = datetime.now() #Bildirimin oluşturulduğu anın tarih/saat bilgisini kaydeder.

    def send(self): #base method (boş/genel)
    #Base method: Alt sınıfların kendi 'send' mantığını kurması için bir yer tutucudur. Polymorphism için
        pass

    def __str__(self): #mesaj bildirimlerini döndürür
        return self.message

    def __len__(self):
        # Bildirim mesajının karakter uzunluğunu döndürür
        return len(self.message)


class EmailNotification(Notification): #Notification sınıfından kalıtım alır
    def send(self):
        print(f"Email gönderildi: {self.message}") #email'e özel davranış kazandırıyoruz


class SMSNotification(Notification):
    def send(self):
        print(f"SMS gönderildi: {self.message}")

class PushNotification(Notification):
    def send(self):
        print(f"Push bildirimi gönderildi: {self.message}")
    
        