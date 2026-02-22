from datetime import datetime

#Expense sınıfı
class Expense():
    def __init__(self, amount, category, date=None):
        #date=None değil de datetime.now() alsak direkt tek bir tarihi hesaplar sonradan oluşturulan tüm Expense nesneleri aynı tarihi alır bu da bug olur. 
        #Eğer kullanıcı date verirse onu kullanır, vermezse o anın tarihini ürettik
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"Harcama: {self.date} {self.category}: {self.amount} TL'dir. "


class Budget():
    #harcamaları yönetip bütçe hesabı yapacağız
    def __init__(self, limit):
        self.limit = limit #bütçe üst sınırı
        self.expenses = [] #tüm harcamaların tutulduğu liste

    def add_expense(self, expense):
        self.expenses.append(expense) #dışarıdan gelen expense nesnesini expenses listesine ekler

    def total_expense(self): #toplam gider
        total = [] #miktarı toplamk için boş bir liste 
        for i in self.expenses:
            total.append(i.amount) #her harcamanın sadece amount kısmını aldık ve listeye ekledik
        return sum(total) #toplamı döner


    def average_expense(self): #ortalama gider
        if not self.expenses: #liste boşsa [] true olur içine girer, 0'a bölme hatasının önüne geçmek için 
            return 0
        return self.total_expense() / len(self.expenses) #toplam gider / harcamaların adedi

    def is_limit_exceeded(self): #bool
        #limiti aştı mı 
        return self.total_expense() > self.limit #toplam harcama > limit mi? true ise evet aşıldı
            
        