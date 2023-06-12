from channels.generic.websocket import AsyncWebsocketConsumer
from notification.api.serializers import NotificationSerializer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.accept()

    async def disconnect(self, close_code):
        # Clean up any resources if needed
        pass

    async def notify(self, event):
        notification = event['notification']
        serializer = NotificationSerializer(notification)
        await self.send(text_data=serializer.data)

