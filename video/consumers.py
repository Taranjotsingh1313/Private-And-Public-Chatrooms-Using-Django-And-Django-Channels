from channels.generic.websocket import AsyncJsonWebsocketConsumer

class Chat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def receive_json(self, content):
        command = content['command']
        print(command)
        if command == 'open':
            await self.channel_layer.group_add(content['group'],self.channel_name)
        elif command == 'send':
            print(content['message'])
            await self.channel_layer.group_send(content['group'],{
                'type':'chat.message',
                'message':content['message']
            })
    async def chat_message(self,event):
        await self.send_json({
            'command':'message',
            'message':event['message']
        })

    async def disconnect(self, code):
        pass