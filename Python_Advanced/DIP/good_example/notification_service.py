from notification_channel import NotificationChannel

class NotificationService():
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel

    def send_notification(self,message):
        self.notification_channel.send(message)




