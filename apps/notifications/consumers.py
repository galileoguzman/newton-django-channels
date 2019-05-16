from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer 


class NotificationConsumer(AsyncJsonWebsocketConsumer): 
	async def connect(self): 
		await self.accept() 
		await self.channel_layer.group_add("notifications", self.channel_name) 
		
	async def disconnect(self, close_code): 
		await self.channel_layer.group_discard("notifications", self.channel_name) 
		
	async def new_notification(self, event): 
		await self.send_json(event)
