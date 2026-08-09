from whatsapp_service import WhatsappService
from email_service import EmailService
from notification_service import NotificationService

if __name__ == "__main__":
    whatsapp = WhatsappService()
    email = EmailService()

    ns = NotificationService(whatsapp)
    ns.send_notification("Hello, this is a test message via WhatsApp!")


