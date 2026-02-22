class Notification: #Base class
    def __init__(self,message):
        self.message = message

    def send(self):
        pass #send boş olduğu için

class EmailNotification(Notification): #notification sınıfından kalıtım aldı
    #send() override edilecek
    def send(self):
        print(f"Email geldi: {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS geldi: {self.message}")
    