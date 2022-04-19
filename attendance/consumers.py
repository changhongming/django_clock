'''import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self): #連接時觸發
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name #直接從用戶指定的房間名

        # Join room group
        #將新的連接加到群組
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code): #斷開時觸發
        # Leave room group
        #將關閉的連接從群組中移除
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data) #接收消息時觸發
        message = text_data_json['message']

        # Send message to room group
        #訊息群發
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))'''

'''# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import json
import logging

logger = logging.getLogger('django')


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # get name from ws url args
        self.name = self.scope['url_route']['kwargs']['name']
        logger.debug('connect')
        # Join group group_add('group_name', 'channel_name')
        async_to_sync(self.channel_layer.group_add)(
            'lobby',
            self.channel_name
        )

        self.accept()
        self.group_send(f'{self.name} join the room.')

    def disconnect(self, close_code):
        # Leave group group_discard('group_name', 'channel_name')
        async_to_sync(self.channel_layer.group_discard)(
            'lobby',
            self.channel_name
        )
        self.group_send(f'{self.name} left the room.')
        

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = self.name + ': ' + text_data_json['message']
        logger.debug('send')

        # Send message to room group
        self.group_send(message)

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def group_send(self, msg, group='lobby', type_='chat_message'):
        # group_send('group_name', {'type': type, **kwargs})
        # type means what function you want to do
        async_to_sync(self.channel_layer.group_send)(
            group,
            {
                'type': type_,
                'message': msg
            }
        )'''
'''from channels.generic.websocket import WebsocketConsumer
import json

import asyncio
from concurrent.futures import TimeoutError as ConnectionTimeoutError
# whatever url is your websocket server
url = 'ws://127.0.0.1:8000'
# timeout in seconds
timeout = 10  
try:
    # make connection attempt
    connection = await asyncio.wait_for(websockets.connect(url), timeout)
except ConnectionTimeoutError as e:
    # handle error
    print('Error connecting.')


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = 'test：' + text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))'''
from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        self.accept("subprotocol")
        # To reject the connection, call:
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        self.close()
        # Or add a custom WebSocket error code!
        self.close(code=4123)

    def disconnect(self, close_code):
        # Called when the socket closes
