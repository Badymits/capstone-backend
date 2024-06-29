from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
import math
import random

from user.models import CustomUser
from .models import Lobby
from .serializers import LobbySerializer

# Create your views here.

# creates a code for the room in FE
def createCode(length):
    
    result = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    
    characterLength = len(characters)
    
    counter = 0
    
    while(counter < length):
        result += characters[math.floor(random.randint(0, characterLength - 1))]
        counter += 1
    return result

# only post methods can access this view
@api_view(['POST'])
def gameLobby(request):
    
    context = {}

    # retrieve owner from request to query user obj
    user = CustomUser.objects.get(username=request.data['owner'])
    
    
    lobby_code = createCode(6)
    context['code'] = lobby_code
    
    # check if there is existing lobby
    try:
        lobby = get_object_or_404(Lobby, lobby_code=lobby_code)
    except: 
        lobby = None
    
    # create if it doesn't exist
    if lobby is None:
        lobby = Lobby.objects.create(
            owner=user,
            lobby_code=lobby_code
        )
        lobby.players.add(user)
        lobby.save()
        context['message'] = 'Lobby created'
    else:
        context['message'] = 'Lobby already exists'
    
    return Response(context)

class LobbyRoomList(mixins.ListModelMixin,generics.GenericAPIView):
    
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class LobbyView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset  = Lobby.objects.all()
    serializer_class = LobbySerializer
    lookup_field = 'lobby_code'
     
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # include lobby code in method parameters
    def patch(self, request, lobby_code, *args, **kwargs):
        
        lobby = Lobby.objects.get(lobby_code=lobby_code)
        user = CustomUser.objects.get(username=self.request.data['player']['username']) # retrieve user using frontend request data
        
        lobby.players.add(user)
        return super().patch(request, *args, **kwargs)