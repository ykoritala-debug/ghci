from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.booking_id = self.scope['url_route']['kwargs']['booking_id']
        self.room_group_name = f'booking_{self.booking_id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_location',
                'location': data['location']
            }
        )

    async def send_location(self, event):
        await self.send(text_data=json.dumps({'location': event['location']}))