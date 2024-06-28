from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import AccountRegisterSerializer
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
         
        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['POST', 'GET'])
def login(request):
    pass


class RegisterUser(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = CustomUser.objects.all()
    serializer_class = AccountRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        
    
        return self.create(request, *args, **kwargs)

