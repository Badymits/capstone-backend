from django.shortcuts import render
from django.http import HttpResponse

from .models import TestModel
from .serializers import TestModelSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def index(request):
    
    return HttpResponse('Hello World')


class TestModelList(APIView):
    
    def get(self, request):
        test_objs = TestModel.objects.all()
        
        # make sure to serialize data before sending to front end
        serializer = TestModelSerializer(test_objs, many=True)
    
        return Response(serializer.data)

