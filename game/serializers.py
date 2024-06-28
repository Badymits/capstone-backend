from rest_framework import serializers

from .models import Lobby
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'

class LobbySerializer(serializers.ModelSerializer):
    
    # this fixes the problem where it only shows the foreignkey ID, not the returned name string
    # many to many fields require many= parameter. By doing this, drf will show the actual object instead of null
    players             = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Lobby
        fields = '__all__'


