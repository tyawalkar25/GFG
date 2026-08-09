from notification_channel import NotificationChannel

class WhatsappService(NotificationChannel):
    def send(self,message):
        print(f"sending whatsapp message : {message}")