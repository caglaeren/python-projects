import random  # Listeden rastgele seçim yapmak için kullanılır.
from datetime import datetime # Zaman damgası oluşturmak için içeri aktarılır.


def generate_message():
    # Sistem için rastgele mesaj bildirimi üretelim
    messages = [
        "Sisteme yeni giriş yapıldı",
        "Yeni bir mesajınız var",
        "Linkedinden size önerilen kişilere bakın",
        "Watsons'da %70'e varan indirim var. Kaçırmayın!"
    ]

    message = random.choice(messages) #liste içinden rastgele eleman seçer
    created_at = datetime.now()

    return message, created_at
    