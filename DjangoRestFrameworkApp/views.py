from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NameSerializer

class TestAPIView(APIView):

    def get(self, requests, *args, **kwargs):
        colors = ['red', 'yellow', 'green']
        return Response({"msg": "Hpaay Diwali", "colors": colors})

    def post(self, requests, *args, **kwargs):
        serializer = NameSerializer(data=requests.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            msg = f"Hello {name}, and fuck you !"
            return Response({"msg":msg})
        else:
            return Response({"msg": serializer.errors})
    
    def put(self, requests, *args, **kwargs):
        return Response({"msg": "Thi response is from PUT."})
        
    def patch(self, requests, *args, **kwargs):
        return Response({"msg": "Thi response is from PATCH."})
    
    def delete(self, requests, *args, **kwargs):
        return Response({"msg": "Thi response is from DELETE."})

