# Kullanıcıdan harcama tutarlarını alıp, 0 girince duracağız. Hatalı girişleri yakalayacağız
import random
from datetime import datetime

def get_user_expenses():
    expenses = []

    while True:
        try:
            amount = float(input("Harcama tutarını giriniz: "))
            if amount == 0:
                break #0 ise duracağız
            if amount < 0:
                print("Negatif harcama tutarı girmeyin.")
                continue

            expenses.append(amount)

        except ValueError:
            print("Hata ! Lütfen doğru değer girin.")

    return expenses


def generate_random_notification():
    messages = [
        "Bütçe limitlerini kontrol et.",
        "Birikim yapmak istiyorsan bütçeni düzgün kullanmayı unutma.",
        "Bugün harcamalar dengeli hadi biraz da para biriktirelim!",
        "İndirimleri takip ederken çok harcayıp limitlerini aşma!",
        "Limitini aşıyorsun!!!"
    ]

    random_message = random.choice(messages) #random şekilde mesajlardan seçer
    guncel_time = datetime.now() #şu anki zaman

    return f"[{guncel_time}] {random_message}"