from email_service import EmailService
from whatsapp_service import WhatsappService

class NotificationService:
    def __init__(self, notification_type:str):
        self.notification_type = notification_type
        self.email_service = EmailService()
        self.whatsapp_service = WhatsappService()

    def send_notification(self, message):
        if self.notification_type == "email":
            self.email_service.send_email(message)

        elif self.notification_type == "whatsapp":
            self.whatsapp_service.send_whatsapp(message)

        else:
            print("Invalid notification type")

ns = NotificationService("whatsapp")
ns.send_notification("I will switch my job to a better one")
