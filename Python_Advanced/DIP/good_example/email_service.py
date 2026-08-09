from notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self,message):
        print(f"sending email with message : {message}")