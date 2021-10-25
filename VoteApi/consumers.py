from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Candidate
from channels.db import database_sync_to_async
import json
from django.core import serializers
class Con(AsyncJsonWebsocketConsumer):
    #
    
    async def connect(self):
        await self.accept()
        
       # await self.add_user()
        await self.channel_layer.group_add("Vote_Count",self.channel_name)
        
        
        await self.send_json({"message" : str("Connected")})
        
        

    
    @database_sync_to_async
    def get_candidates(self) :
         data = Candidate.objects.values()
         data_list = []
         for d in data:
             point = {
                 "name" : d['candidate_name'],
                 "candidate_id" : str(d['candidate_id'])
                 , "vote_count":d['vote_count']
                 ,"position" : d['position']
             }
             data_list.append(point)
         return data_list

    
    
    

    async def send_everyone(self,event):
        data = await self.get_candidates()
       
        await self.send_json({"message":data})