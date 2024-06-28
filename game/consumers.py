import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.db import database_sync_to_async

class GameRoomConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.group_code = self.scope.get("url_route").get("kwargs").get("code")  # from routing url parameter
        self.user = self.scope.get("url_route").get("kwargs").get("username") # username is unique
        
        print(self.user)
        print(self.group_code)
        
        # create unique group
        self.room_name = f'lobby_{self.group_code}'
        
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name # this will be created automatically for each user
        )
        
        # next term, add token based websocket connection to avoid AnonymousUser
        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'connection established',
            'message': 'You are now connected'
        }))   
            
            
    
    